"""Controller-owned graphic worker. No command/URL/argument transport from Actors.

Only registered workspace directory descriptors can be read. Input is copied
into a per-task private directory; outputs have fixed names under .render/results.
Directory-descriptor I/O refuses symlinks, including races and named pipes.
"""
import contextlib
import ctypes
import hashlib
import json
import os
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath

MAX_INPUT = 1024 * 1024
MAX_OUTPUT = 64 * 1024 * 1024
PROTOCOL = 'controlled-local-render/1'


class OutputCleanupError(RuntimeError):
    pass


def parts(name):
    if not isinstance(name, str) or not name or len(name) > 1024:
        raise ValueError('invalid session-relative path')
    path = PurePosixPath(name)
    if path.is_absolute() or any(p in {'', '.', '..'} for p in name.split('/')):
        raise ValueError('path must be canonical and session-relative')
    if any(c in name for c in ('\\', '\x00', ':', '%')):
        raise ValueError('protocols and encoded paths are not allowed')
    return path.parts


@contextlib.contextmanager
def directory(root_fd, names):
    descriptor = os.dup(root_fd)
    try:
        for name in names:
            next_fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = next_fd
        yield descriptor
    finally:
        os.close(descriptor)


def read_session(root_fd, name, limit=MAX_INPUT):
    names = parts(name)
    with directory(root_fd, names[:-1]) as parent:
        fd = os.open(names[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        try:
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or info.st_size > limit or info.st_nlink != 1:
                raise ValueError('input must be a bounded regular file')
            data = bytearray()
            while len(data) <= limit:
                chunk = os.read(fd, min(65536, limit + 1 - len(data)))
                if not chunk:
                    break
                data.extend(chunk)
            if len(data) > limit:
                raise ValueError('input exceeds size limit')
            return bytes(data)
        finally:
            os.close(fd)


def write_session(root_fd, name, data):
    names = parts(name)
    with directory(root_fd, names[:-1]) as parent:
        fd = os.open(names[-1], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                     0o600, dir_fd=parent)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)


def publish_session(root_fd, payloads, quarantine_parent=None):
    """Reserve the whole result set; roll back only files this call created."""
    created = []
    try:
        for name, data in payloads.items():
            names = parts(name)
            with directory(root_fd, names[:-1]) as parent:
                fd = os.open(names[-1], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                             0o600, dir_fd=parent)
                info = os.fstat(fd)
                created.append({'path': name, 'device': info.st_dev, 'inode': info.st_ino, 'fd': fd})
        for item, data in zip(created, payloads.values()):
            view = memoryview(data)
            while view:
                written = os.write(item['fd'], view)
                if written <= 0:
                    raise OSError('render output write did not progress')
                view = view[written:]
        return [{k: v for k, v in item.items() if k != 'fd'} for item in created]
    except Exception:
        rollback_session(root_fd, created, quarantine_parent)
        raise
    finally:
        for item in created:
            os.close(item['fd'])


def rename_exclusive(source_fd, source, target_fd, target):
    """Use the installed OS's atomic, non-overwriting rename operation."""
    library = ctypes.CDLL(None, use_errno=True)
    if sys.platform == 'darwin':
        function = library.renameatx_np
        flag = 0x00000004  # RENAME_EXCL, acquired local SDK sys/stdio.h.
    elif sys.platform.startswith('linux') and hasattr(library, 'renameat2'):
        function = library.renameat2
        flag = 1  # RENAME_NOREPLACE.
    else:
        raise OSError('atomic exclusive rename is unavailable; displaced output is retained')
    function.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    function.restype = ctypes.c_int
    if function(source_fd, os.fsencode(source), target_fd, os.fsencode(target), flag) != 0:
        error = ctypes.get_errno()
        raise OSError(error, os.strerror(error), target)


def rollback_session(root_fd, created, quarantine_parent=None):
    """Inspect only entries atomically moved out of the Actor's writable tree."""
    if not created:
        return
    quarantine = Path(tempfile.mkdtemp(prefix='render-rollback-', dir=quarantine_parent))
    quarantine_fd = os.open(quarantine, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    errors = []
    try:
        for index, item in enumerate(reversed(created)):
            names = parts(item['path'])
            displaced = str(index)+'-'+names[-1]
            try:
                with directory(root_fd, names[:-1]) as parent:
                    os.rename(names[-1], displaced, src_dir_fd=parent, dst_dir_fd=quarantine_fd)
                    info = os.stat(displaced, dir_fd=quarantine_fd, follow_symlinks=False)
                    if (info.st_dev, info.st_ino) == (item['device'], item['inode']):
                        os.unlink(displaced, dir_fd=quarantine_fd)
                    else:
                        errors.append('render output ownership changed during cleanup: '+item['path'])
                        rename_exclusive(quarantine_fd, displaced, parent, names[-1])
            except FileNotFoundError:
                continue
            except OSError as exc:
                errors.append(str(exc))
    finally:
        os.close(quarantine_fd)
        try:
            quarantine.rmdir()
        except OSError:
            errors.append('displaced outputs retained without deletion: '+str(quarantine))
    if errors:
        raise OutputCleanupError('; '.join(errors))


def validate_graphic(kind, data):
    text = data.decode('utf-8')
    if kind == 'mmd':
        if len(text) > 50000:
            raise ValueError('Mermaid maxTextSize is 50000')
        if re.search(r'(?im)^\s*(?:click|link)\s|%%\{|<\s*/?\s*[a-zA-Z]|(?:https?|file|data|javascript|ftp):|\\', text):
            raise ValueError('Mermaid scripts, links, HTML and external resources are refused')
        return
    if kind not in {'svg', 'bpmn','uml-class-layout'}:
        raise ValueError('unsupported graphic kind')
    if re.search(r'<!DOCTYPE|<!ENTITY|<\?', text, re.I):
        # An XML declaration is data, not a processing instruction.
        text = re.sub(r'^\s*<\?xml\s[^?]*\?>', '', text, count=1)
        if re.search(r'<!DOCTYPE|<!ENTITY|<\?', text, re.I):
            raise ValueError('XML entities and processing instructions are refused')
    node = ET.fromstring(text)
    expected = ({'{http://www.w3.org/2000/svg}svg'} if kind=='svg' else
                {'{http://www.omg.org/spec/BPMN/20100524/MODEL}definitions'} if kind=='bpmn' else
                {'{http://www.omg.org/spec/UML/20131001}Model','{http://www.omg.org/spec/XMI/20131001}XMI'})
    if node.tag not in expected:
        raise ValueError('graphic root/namespace differs from supported format')
    for element in node.iter():
        tag = element.tag.split('}')[-1].lower()
        if tag in {'script', 'foreignobject', 'iframe', 'object', 'embed', 'audio', 'video', 'image',
                   'set', 'animate', 'animatemotion', 'animatetransform'}:
            raise ValueError('active or embedded graphic content is refused')
        for attribute, value in element.attrib.items():
            key = attribute.split('}')[-1].lower()
            # BPMN 2.0.2 Semantic.xsd, tMultiInstanceLoopCharacteristics,
            # declares this unqualified QName reference (Table 10.41).
            # Its "on" prefix is not a browser event handler. Keep the
            # exception exact: no foreign element/namespace/case aliases,
            # and never carry it into the rendered SVG admission boundary.
            standard_mi_reference = (kind == 'bpmn'
                and element.tag == '{http://www.omg.org/spec/BPMN/20100524/MODEL}multiInstanceLoopCharacteristics'
                and attribute == 'oneBehaviorEventRef')
            if (key.startswith('on') and not standard_mi_reference) or key in {'base', 'schemaLocation'.lower()}:
                raise ValueError('active attributes and external schemas are refused')
            standard_profile_href='http://www.omg.org/spec/UML/20161101/StandardProfile.xmi#_0'
            if key in {'href', 'src'} and not re.fullmatch(r'#[\w.:-]+', value) and not (kind=='uml-class-layout' and key=='href' and value==standard_profile_href):
                raise ValueError('external graphic references are refused')
        if kind == 'svg':
            value = ' '.join(element.attrib.values()) + ' ' + (element.text or '') + ' ' + (element.tail or '')
            if '\\' in value or re.search(r'@import|(?:https?|file|data|javascript|ftp):', value, re.I):
                raise ValueError('external CSS/resources are refused')
            for match in re.finditer(r'url\s*\(([^)]*)\)', value, re.I):
                if not re.fullmatch(r'''[\s'"]*#[\w.:-]+[\s'"]*''', match.group(1)):
                    raise ValueError('only local SVG paint-server fragments are allowed')
    if kind == 'bpmn':
        for element in node.iter():
            if element.tag.split('}')[-1] in {'import', 'extensionElements'}:
                raise ValueError('external imports and vendor extension graphics are refused')


def owned_processes(pid, task_root, browser=None):
    """Inspect only the worker descendants and its unique browser profile."""
    result = subprocess.run(['/bin/ps', '-axo', 'pid=,ppid=,rss=,command='],
                            capture_output=True, text=True, timeout=3)
    if result.returncode != 0 or not result.stdout.strip():
        raise RuntimeError('owned-process inspection unavailable; cleanup cannot be certified')
    rows = {}
    for line in result.stdout.splitlines():
        fields = line.strip().split(None, 3)
        if len(fields) != 4:
            continue
        try:
            ident, parent, rss = map(int, fields[:3])
        except ValueError:
            continue
        rows[ident] = {'pid': ident, 'ppid': parent, 'rss_kib': rss, 'command': fields[3]}
    ids = ({pid} if pid in rows and str(task_root/'spec.json') in rows[pid]['command'] else set())
    profile = re.compile(r'(?<!\S)--user-data-dir='+re.escape(str(task_root/'.profile'))+r'(?=\s|$)')
    ids |= {ident for ident, row in rows.items()
            if browser and row['command'].startswith(str(browser)+' ') and profile.search(row['command'])}
    while True:
        additional = {ident for ident, row in rows.items() if row['ppid'] in ids}
        if additional <= ids:
            break
        ids |= additional
    return [{k: v for k, v in rows[ident].items() if k != 'command'} for ident in ids if ident in rows]


def terminate_owned(process, task_root, browser=None):
    before = owned_processes(process.pid, task_root, browser)
    for row in before:
        try:
            os.kill(row['pid'], signal.SIGTERM)
        except ProcessLookupError:
            pass
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        pass
    for row in owned_processes(process.pid, task_root, browser):
        try:
            os.kill(row['pid'], signal.SIGKILL)
        except ProcessLookupError:
            pass
    process.wait(timeout=3)
    return before


class LocalRenderController:
    def __init__(self, shared, browser, evidence, timeout=120, private_parent=None, budget=None):
        self.shared = Path(shared).resolve()
        self.browser = Path(browser).resolve()
        self.evidence = Path(evidence)
        self.evidence.mkdir(parents=True, exist_ok=False)
        self.timeout = min(max(timeout, 1), 120)
        self.budget = budget
        self.sessions = {}
        self.lock = threading.Lock()
        self.stop = threading.Event()
        self.events = []
        self.temporary = tempfile.TemporaryDirectory(prefix='togaf-controlled-render-', dir=private_parent)
        self.private = Path(self.temporary.name)
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def register(self, root):
        root = Path(root).resolve()
        fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            os.mkdir('.render', 0o700, dir_fd=fd)
            with directory(fd, ('.render',)) as queue:
                for name in ('inbox', 'outbox', 'results'):
                    os.mkdir(name, 0o700, dir_fd=queue)
            with self.lock:
                self.sessions[str(root)] = {'fd': fd, 'seen': set(), 'number': len(self.sessions),
                                           'tasks': 0, 'output_bytes': 0, 'quota_exceeded': False}
        except Exception:
            os.close(fd)
            raise

    def loop(self):
        while not self.stop.wait(.05):
            with self.lock:
                sessions = list(self.sessions.values())
            for session in sessions:
                if session['quota_exceeded']:
                    continue
                try:
                    with directory(session['fd'], ('.render', 'inbox')) as inbox:
                        requests = []
                        with os.scandir(inbox) as entries:
                            for entry in entries:
                                if entry.name not in session['seen']:
                                    requests.append(entry.name)
                                    if len(requests) > 64:
                                        break
                    if len(requests) > 64:
                        session['quota_exceeded'] = True
                        name = next((n for n in requests if re.fullmatch('[0-9a-f]{32}\.json', n)), None)
                        if name:
                            self.handle(session, name[:-5], 'controlled renderer pending queue limit (64) exceeded')
                        continue
                    for name in requests:
                        if name in session['seen']:
                            continue
                        if len(session['seen']) >= 64:
                            session['quota_exceeded'] = True
                            if re.fullmatch('[0-9a-f]{32}\.json', name):
                                self.handle(session,name[:-5],'controlled renderer per-session task limit (64) exceeded')
                            break
                        session['seen'].add(name)
                        if not re.fullmatch('[0-9a-f]{32}\.json', name):
                            continue
                        self.handle(session, name[:-5])
                except OSError:
                    continue

    def handle(self, session, identity, forced_reason=None):
        row = {'protocol': PROTOCOL, 'session': session['number'], 'task': identity,
               'mode': 'controlled-local-process', 'status': 'refused'}
        started = time.monotonic()
        task_root = self.private / identity
        process = None
        published = []
        accounted_output_bytes = 0
        try:
            if forced_reason:
                raise ValueError(forced_reason)
            if self.budget:
                self.budget.check()
            session['tasks'] += 1
            if session['tasks'] > 64 or len(self.events) >= 4096:
                session['quota_exceeded'] = True
                raise ValueError('controlled renderer task quota exceeded')
            task = json.loads(read_session(session['fd'], '.render/inbox/'+identity+'.json', 4096))
            if not isinstance(task, dict) or set(task) != {'kind', 'source'}:
                raise ValueError('only kind and source are accepted; commands, URLs and browser arguments are refused')
            source_parts = parts(task['source'])
            if source_parts[0] in {'.render', '.agents', '_shared', '.git'}:
                raise ValueError('only session-created graphic sources are readable')
            suffixes = {'svg': {'.svg'}, 'mmd': {'.mmd'}, 'bpmn': {'.bpmn', '.xml'},'uml-class-layout':{'.uml','.xmi','.xml'}}
            if task.get('kind') not in suffixes or Path(task['source']).suffix not in suffixes[task['kind']]:
                raise ValueError('source extension must match a supported graphic format')
            data = read_session(session['fd'], task['source'])
            validate_graphic(task['kind'], data)
            row.update(kind=task['kind'], source=task['source'], input_sha256=hashlib.sha256(data).hexdigest())
            task_root.mkdir(mode=0o700)
            for name in ('.home', '.tmp', '.profile'):
                (task_root/name).mkdir(mode=0o700)
            (task_root/'input').write_bytes(data)
            import sys
            sys.path.insert(0, str(self.shared/'scripts'))
            spec = {'kind': task['kind']}
            if task['kind'] == 'bpmn':
                from bpmn_render import diagram_plan
                spec['bpmn_plan'] = {k: v for k, v in diagram_plan(data).items() if k != 'native_validation'}
            if task['kind']=='uml-class-layout':
                from uml_render import diagram_model,svg_diagram
                model=diagram_model(data);svg,layout=svg_diagram(model)
                spec['uml_layout']=layout
                spec['uml_source_sha256']=row['input_sha256']
                spec['uml_profile_applications']=model.get('profile_applications',[])
                data=svg.encode('utf-8')
                (task_root/'input').write_bytes(data)
            from generate import subset_font
            subset_font(data.decode('utf-8'), task_root/'font.ttf')
            (task_root/'spec.json').write_text(json.dumps(spec))
            environment = {'PATH': '/opt/homebrew/bin:/usr/bin:/bin', 'HOME': str(task_root/'.home'),
                           'TMPDIR': str(task_root/'.tmp'), 'LANG': 'en_US.UTF-8',
                           'TOGAF_BROWSER_PATH': str(self.browser)}
            with (task_root/'stdout.log').open('wb') as stdout_log, (task_root/'stderr.log').open('wb') as stderr_log:
                process = subprocess.Popen([shutil.which('node') or 'node', '--max-old-space-size=512', str(self.shared/'scripts/controlled_render_worker.mjs'),
                                            str(task_root/'spec.json')], cwd=task_root, env=environment,
                                           stdout=stdout_log, stderr=stderr_log, start_new_session=True)
                deadline = time.monotonic() + self.timeout
                peak_rss = 0
                while process.poll() is None:
                    if self.stop.is_set():
                        raise ValueError('controlled renderer cancelled by controller shutdown')
                    if self.budget:
                        self.budget.check(dispatch=False)
                    memory = sum(r['rss_kib'] for r in owned_processes(process.pid, task_root, self.browser))
                    peak_rss = max(peak_rss, memory)
                    if memory > 1024 * 1024:
                        raise ValueError('controlled renderer exceeded 1 GiB owned-process RSS limit')
                    if sum(p.stat().st_size for p in task_root.rglob('*') if p.is_file()) > MAX_OUTPUT:
                        raise ValueError('controlled renderer output resource limit exceeded')
                    if time.monotonic() >= deadline:
                        raise ValueError('controlled renderer timeout')
                    try:
                        process.wait(timeout=.25)
                    except subprocess.TimeoutExpired:
                        pass
            row['peak_owned_rss_kib'] = peak_rss
            stderr = (task_root/'stderr.log').read_bytes()
            if process.returncode:
                raise ValueError('controlled renderer failed: '+stderr.decode('utf-8', 'replace')[-2000:])
            report = json.loads((task_root/'diagram.json').read_text())
            if report.get('status') != 'pass' or report.get('external_requests'):
                raise ValueError('renderer functional/resource checks did not pass')
            total = sum(p.stat().st_size for p in task_root.rglob('*') if p.is_file())
            if total > MAX_OUTPUT:
                raise ValueError('controlled renderer output resource limit exceeded')
            outputs = {}
            output_files = {'svg':'diagram.svg', 'png':'diagram.png', 'json':'diagram.json',
                            'browser_png':'browser-screenshot.png'}
            output_bytes = sum((task_root/name).stat().st_size for name in output_files.values())
            if session['output_bytes'] + output_bytes > 512 * 1024 * 1024:
                session['quota_exceeded'] = True
                raise ValueError('controlled renderer per-session output quota (512 MiB) exceeded')
            payloads = {}
            for suffix, filename in output_files.items():
                data_out = (task_root/filename).read_bytes()
                output = '.render/results/'+identity+'.'+('browser.png' if suffix=='browser_png' else suffix)
                payloads[output] = data_out
                outputs[suffix] = {'path': output, 'sha256': hashlib.sha256(data_out).hexdigest(), 'bytes': len(data_out)}
            published = publish_session(session['fd'], payloads, self.evidence)
            session['output_bytes'] += output_bytes
            accounted_output_bytes = output_bytes
            row.update(status='pass', outputs=outputs, renderer_report=report,
                       environment_policy='allowlist; no inherited Node/Python/loader/credential variables')
        except Exception as exc:
            row['reason'] = str(exc)
            if isinstance(exc, OutputCleanupError):
                row['output_cleanup_verification_failed'] = True
        finally:
            try:
                if process is not None:
                    if process.poll() is None or owned_processes(process.pid, task_root, self.browser):
                        row['terminated_owned_processes'] = terminate_owned(process, task_root, self.browser)
                    row['owned_processes_remaining'] = owned_processes(process.pid, task_root, self.browser)
                    if row['owned_processes_remaining']:
                        raise RuntimeError('owned browser/worker processes remain after cleanup')
            except Exception as exc:
                row.update(status='refused', reason='controlled renderer cleanup verification failed: '+str(exc),
                           cleanup_verification_failed=True)
                if self.budget:
                    self.budget.trip(row['reason'])
            finally:
                if row['status'] != 'pass':
                    try:
                        rollback_session(session['fd'], published, self.evidence)
                        session['output_bytes'] -= accounted_output_bytes
                        row.pop('outputs', None)
                    except Exception as exc:
                        row.update(reason='controlled renderer output cleanup verification failed: '+str(exc),
                                   output_cleanup_verification_failed=True)
                        if self.budget:
                            self.budget.trip(row['reason'])
                shutil.rmtree(task_root, ignore_errors=True)
                row.update(seconds=round(time.monotonic()-started, 3),
                           cleaned=not task_root.exists() and not row.get('owned_processes_remaining')
                                   and not row.get('cleanup_verification_failed')
                                   and not row.get('output_cleanup_verification_failed'))
            self.events.append(row)
            (self.evidence/'events.json').write_text(json.dumps(self.events, ensure_ascii=False, indent=2)+'\n')
            try:
                write_session(session['fd'], '.render/outbox/'+identity+'.json', json.dumps(row, ensure_ascii=False).encode())
            except OSError:
                pass
        return row

    def close(self):
        self.stop.set()
        self.thread.join(timeout=self.timeout+5)
        if self.thread.is_alive():
            raise RuntimeError('render controller did not stop')
        for session in self.sessions.values():
            os.close(session['fd'])
        self.temporary.cleanup()
        summary = {'protocol': PROTOCOL, 'mode': 'controlled-local-process', 'model_sessions': 0,
                   'tasks': len(self.events), 'passed': sum(r['status']=='pass' for r in self.events),
                   'refused': sum(r['status']=='refused' for r in self.events),
                   'all_tasks_cleaned': all(r['cleaned'] for r in self.events),
                   'private_directory_cleaned': not self.private.exists(),
                   'browser_sha256': hashlib.sha256(self.browser.read_bytes()).hexdigest()}
        (self.evidence/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
        return summary
