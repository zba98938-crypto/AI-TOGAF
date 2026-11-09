"""Prepare or activate entrypoints using one explicit, fully verified round manifest."""
import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[2]
UI_CHECKER = Path(__file__).with_name('verify_current_output_ui.mjs')
STAGES = ('source_freeze', 'source_closure', 'package_verification',
          'engineering_verification', 'model_evaluation')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    require(isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value), 'Invalid SHA-256')
    return value


def safe_path(value, *, repo=REPO, base=None, exists=True):
    """Check lexical components before resolving, including symlink/../ sequences."""
    repo = repo.resolve()
    require(isinstance(value, str) and value and '\\' not in value
            and not re.search(r'[\x00-\x1f\x7f]', value), 'Invalid local path')
    path = Path(value)
    require(not path.is_absolute(), 'Absolute paths are forbidden')
    cursor = repo if base is None else base
    require(cursor.is_relative_to(repo), 'Base path escapes repository')
    probe = repo
    for part in cursor.relative_to(repo).parts:
        # The base itself can contain a parent symlink even when the final path does not.
        probe = probe / part
        require(not probe.is_symlink(), 'Base symlink traversal is forbidden')
    for part in path.parts:
        cursor = cursor.parent if part == '..' else cursor / part
        require(cursor.is_relative_to(repo), 'Local path escapes repository')
        require(not cursor.is_symlink(), 'Symlink traversal is forbidden')
    if exists:
        require(cursor.exists(), 'Missing local path: ' + value)
    return cursor


def local_href_target(url, source, *, repo=REPO):
    require(isinstance(url, str) and not re.search(r'[\x00-\x20\x7f]', url), 'Invalid local URL')
    parsed = urlsplit(url)
    require(not parsed.scheme and not parsed.netloc, 'Only repository-relative URLs are allowed')
    raw = unquote(parsed.path)
    require(not re.search(r'%[0-9a-fA-F]{2}', raw), 'Nested URL encoding is forbidden')
    if not raw:
        return source
    return safe_path(raw, repo=repo, base=source.parent)


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.rows = [], set(), 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'tr' and 'data-search' in attrs:
            self.rows += 1
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append((tag, name, attrs[name]))


def verify_ref(ref, *, repo=REPO):
    require(isinstance(ref, dict) and set(ref) == {'path', 'sha256'}, 'Invalid file reference')
    path = safe_path(ref['path'], repo=repo)
    require(path.is_file(), 'Reference must be a file: ' + ref['path'])
    require(sha(path) == digest(ref['sha256']), 'File fingerprint differs: ' + ref['path'])
    return path


def verify_links(text, source, allowed, *, repo=REPO):
    document, links = Document(text), []
    for tag, attribute, url in document.links:
        if attribute == 'src' and tag == 'img' and url.startswith(
                ('data:image/svg+xml;base64,', 'data:image/png;base64,', 'data:image/jpeg;base64,')):
            continue
        target = local_href_target(url, source, repo=repo)
        require(target.is_file(), 'HTML target is not a file: ' + url)
        require(target == source or target in allowed, 'HTML target lacks a fingerprint: ' + url)
        fragment = unquote(urlsplit(url).fragment)
        if fragment and target.suffix.lower() == '.html':
            ids = document.ids if target == source else Document(target.read_text()).ids
            require(fragment in ids, 'HTML anchor does not exist: ' + url)
        links.append({'url': url, 'path': target.relative_to(repo).as_posix()})
    return document, links


def verify_git_identity(repo, source_commit):
    require(re.fullmatch(r'[0-9a-f]{40}', source_commit or ''), 'Invalid source commit')
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
    require(head == source_commit, 'Git HEAD differs from frozen source commit')
    status = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=normal'],
                            cwd=repo, capture_output=True, text=True, check=True).stdout
    require(not status.strip(), 'Source checkout is not clean')


def prepare(manifest, *, repo=REPO):
    repo = repo.resolve()
    require(manifest.get('schema_version') == 'current-entrypoint-round/1', 'Unsupported round manifest')
    round_id, commit = manifest.get('round_id'), manifest.get('source_commit')
    require(isinstance(round_id, str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,95}', round_id), 'Invalid round ID')
    require(re.fullmatch(r'[0-9a-f]{40}', commit or ''), 'Invalid source commit')
    prerequisites = manifest.get('prerequisites')
    require(isinstance(prerequisites, dict) and set(prerequisites) == set(STAGES), 'All five prerequisite stages are required')
    verified_stages, frozen_files = {}, {}
    for stage in STAGES:
        path = verify_ref(prerequisites[stage], repo=repo)
        data = json.loads(path.read_text())
        require(data.get('passed') is True and data.get('round_id') == round_id
                and data.get('source_commit') == commit, 'Prerequisite failed or belongs to another version: ' + stage)
        require(data.get('stage') == stage, 'Prerequisite stage differs: ' + stage)
        if stage == 'source_freeze':
            frozen_files = data.get('files')
            require(isinstance(frozen_files, dict) and frozen_files, 'Frozen source file map is missing')
            for name, expected in frozen_files.items():
                verify_ref({'path': name, 'sha256': expected}, repo=repo)
        if stage == 'model_evaluation':
            require(data.get('required_items') == data.get('executed_items') == data.get('passed_items') == 507
                    and data.get('unexecuted_items') == 0 and data.get('actor_scorer_independent') is True,
                    'Complete independent 507-item evaluation is required before activation')
        verified_stages[stage] = dict(prerequisites[stage])
    entries = manifest.get('entries')
    require(isinstance(entries, dict) and set(entries) == {'current_map', 'catalogue'}, 'Both current entrypoints are required')
    current = verify_ref(entries['current_map'], repo=repo)
    catalogue = verify_ref(entries['catalogue'], repo=repo)
    require(current != catalogue and current.suffix == '.json' and catalogue.suffix == '.html', 'Invalid entrypoint types')
    old_mapping = json.loads(current.read_text())
    output_paths = manifest.get('output_paths')
    require(isinstance(old_mapping, dict) and isinstance(output_paths, dict) and output_paths
            and set(old_mapping) == set(output_paths), 'Current output map keys differ')
    targets = manifest.get('targets')
    require(isinstance(targets, list) and targets, 'Target fingerprint list is missing')
    allowed = {}
    for ref in targets:
        path = verify_ref(ref, repo=repo)
        require(path not in allowed and path not in {current, catalogue}, 'Duplicate or current-entry target reference')
        allowed[path] = ref['sha256']
    mapping = {}
    for key, name in output_paths.items():
        target = safe_path(name, repo=repo)
        if target.is_dir():
            files = []
            for member in target.rglob('*'):
                safe_path(member.relative_to(repo).as_posix(), repo=repo)
                if member.is_file():
                    files.append(member)
            require(files and all(member in allowed for member in files), 'Output directory is not fully fingerprinted: ' + key)
        else:
            require(target.is_file() and target in allowed, 'Output file lacks a fingerprint: ' + key)
        mapping[key] = os.path.relpath(target, current.parent)
    config = manifest.get('catalogue')
    require(isinstance(config, dict) and type(config.get('expected_rows')) is int
            and config['expected_rows'] > 0, 'Expected catalogue rows are required')
    replacements = config.get('replacements')
    require(isinstance(replacements, list) and replacements, 'Catalogue replacements are missing')
    text, replaced = catalogue.read_text(), []
    seen = set()
    for change in replacements:
        require(isinstance(change, dict) and set(change) == {'map_key', 'from', 'to'}, 'Invalid catalogue replacement')
        key, old, new = change['map_key'], change['from'], change['to']
        require(key in output_paths and key not in seen and isinstance(old, str) and isinstance(new, str)
                and old and new and old != new and old.endswith('/') and new.endswith('/'), 'Invalid replacement prefixes')
        old_target = local_href_target(old, catalogue, repo=repo)
        require(old_target == safe_path(old_mapping[key], repo=repo, base=current.parent), 'Old catalogue prefix differs from current map')
        new_target = local_href_target(new, catalogue, repo=repo)
        require(new_target == safe_path(output_paths[key], repo=repo), 'New catalogue prefix differs from proposed map')
        count = text.count(old)
        require(count > 0, 'Catalogue prefix is absent: ' + old)
        text = text.replace(old, new)
        require(old not in text, 'Old catalogue prefix remains')
        seen.add(key)
        replaced.append({'map_key': key, 'occurrences': count})
    ui = manifest.get('ui')
    require(isinstance(ui, dict) and set(ui) == {'atlas', 'search_term', 'expected_search_rows'}, 'Fixed UI checks are required')
    atlas = verify_ref(ui['atlas'], repo=repo)
    require(atlas.suffix == '.html' and isinstance(ui['search_term'], str) and ui['search_term']
            and type(ui['expected_search_rows']) is int and 0 < ui['expected_search_rows'] <= config['expected_rows'], 'Invalid UI expectations')
    allowed[atlas] = ui['atlas']['sha256']
    document, links = verify_links(text, catalogue, allowed, repo=repo)
    require(document.rows == config['expected_rows'], 'Catalogue row count differs')
    _, atlas_links = verify_links(atlas.read_text(), atlas, allowed, repo=repo)
    new_bytes = {'current_map': (json.dumps(mapping, ensure_ascii=False, indent=2) + '\n').encode(),
                 'catalogue': text.encode()}
    request = {'schema_version': 'current-output-ui-request/1', 'round_id': round_id,
               'runtime_mode': 'local-test-controller', 'repo_root': str(repo),
               'catalogue': {'path': str(catalogue), 'sha256': hashlib.sha256(new_bytes['catalogue']).hexdigest()},
               'atlas': {'path': str(atlas), 'sha256': sha(atlas)},
               'allowed_files': {str(path): expected for path, expected in allowed.items()},
               'expected_rows': config['expected_rows'], 'search_term': ui['search_term'],
               'expected_search_rows': ui['expected_search_rows']}
    request['allowed_files'][str(catalogue)] = request['catalogue']['sha256']
    return {'paths': {'current_map': current, 'catalogue': catalogue}, 'new_bytes': new_bytes,
            'ui_request': request, 'frozen_files': frozen_files,
            'result': {'schema_version': 'current-output-activation/1', 'round_id': round_id,
                       'source_commit': commit, 'prerequisites': verified_stages,
                       'prepared': True, 'applied': False, 'passed': False,
                       'before_sha256': {key: sha(path) for key, path in {'current_map': current, 'catalogue': catalogue}.items()},
                       'proposed_sha256': {key: hashlib.sha256(value).hexdigest() for key, value in new_bytes.items()},
                       'target_files': len(allowed), 'catalogue_links': len(links), 'atlas_links': len(atlas_links),
                       'replacements': replaced, 'runtime_mode': 'local-test-controller',
                       'professional_acceptance': 'pending_signature', 'organization_approval': 'pending_signature'}}


def atomic_write(path, value):
    mode = path.stat().st_mode & 0o777
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(prefix='.' + path.name + '.activation-', dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(mode)
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def write_json(path, data):
    with path.open('x') as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write('\n')


def check_ui(request, destination):
    request_path = destination / 'ui-request.json'
    write_json(request_path, request)
    node = shutil.which('node')
    require(node, 'Installed Node is unavailable')
    environment = {name: os.environ[name] for name in ('PATH', 'HOME', 'TOGAF_BROWSER_PATH') if name in os.environ}
    environment.update({'TMPDIR': str(destination), 'TMP': str(destination), 'TEMP': str(destination)})
    process = subprocess.Popen([node, str(UI_CHECKER), '--input', str(request_path), '--out', str(destination / 'ui')],
                               env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        stdout, stderr = process.communicate(timeout=120)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGTERM)
        try:
            stdout, stderr = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
        (destination / 'ui-controller.log').write_text(stdout + stderr)
        raise ValueError('Local UI controller timed out')
    (destination / 'ui-controller.log').write_text(stdout + stderr)
    result_path = destination / 'ui/result.json'
    require(process.returncode == 0 and result_path.is_file(), 'Local UI controller failed')
    result = json.loads(result_path.read_text())
    require(result.get('passed') is True and result.get('runtime_mode') == 'local-test-controller'
            and result.get('round_id') == request['round_id'], 'Local UI evidence is incomplete')
    return {'path': str(result_path), 'sha256': sha(result_path), 'passed': True,
            'runtime_mode': 'local-test-controller'}


def _activate_locked(prepared, destination, *, ui_checker=check_ui, writer=atomic_write):
    result, paths = prepared['result'], prepared['paths']
    before = {key: path.read_bytes() for key, path in paths.items()}
    require(result['before_sha256'] == {key: sha(path) for key, path in paths.items()}, 'Current entries changed after preparation')
    snapshot = destination / 'before'
    snapshot.mkdir()
    for key, value in before.items():
        with (snapshot / (key + paths[key].suffix)).open('xb') as handle:
            handle.write(value)
    try:
        for key, path in paths.items():
            require(sha(path) == result['before_sha256'][key], 'Current entry changed before replace')
            writer(path, prepared['new_bytes'][key])
        require(result['proposed_sha256'] == {key: sha(path) for key, path in paths.items()}, 'Activated entry bytes differ')
        result['ui_verification'] = ui_checker(prepared['ui_request'], destination)
        require(result['ui_verification'].get('passed') is True, 'Post-activation UI checks failed')
        result.update({'applied': True, 'passed': True, 'rolled_back': False})
    except BaseException as error:
        rollback_errors = []
        for key, path in paths.items():
            try:
                require(sha(path) in {result['before_sha256'][key], result['proposed_sha256'][key]},
                        'Concurrent entry change prevents restoration: ' + key)
                # Restoration must not reuse a failing injected writer.
                atomic_write(path, before[key])
            except BaseException as rollback_error:
                rollback_errors.append(str(rollback_error))
        restored = result['before_sha256'] == {key: sha(path) for key, path in paths.items()}
        result.update({'applied': False, 'passed': False, 'rolled_back': restored,
                       'error': str(error), 'error_type': type(error).__name__, 'rollback_errors': rollback_errors})
        raise
    finally:
        result['after_sha256'] = {key: sha(path) for key, path in paths.items()}
        result['completed_at'] = datetime.now(timezone.utc).isoformat()
        write_json(destination / 'activation.json', result)
    return result


def activate(prepared, destination, *, ui_checker=check_ui, writer=atomic_write):
    lock = prepared['paths']['current_map'].parent / '.current-output-activation.lock'
    with lock.open('x') as handle:
        json.dump({'pid': os.getpid(), 'round_id': prepared['result']['round_id'],
                   'evidence': str(destination)}, handle)
    try:
        return _activate_locked(prepared, destination, ui_checker=ui_checker, writer=writer)
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--round', type=Path, required=True, dest='manifest')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        manifest_path = safe_path(os.path.relpath(args.manifest.absolute(), REPO), repo=REPO)
        destination = safe_path(os.path.relpath(args.out.absolute(), REPO), repo=REPO, exists=False)
        require(destination.is_relative_to(REPO / 'output') and not destination.exists(), 'Evidence must use a new repository output directory')
        destination.mkdir(parents=True)
        manifest = json.loads(manifest_path.read_text())
        verify_git_identity(REPO, manifest.get('source_commit'))
        prepared = prepare(manifest)
        shutil.copyfile(manifest_path, destination / 'round-manifest.json')
        write_json(destination / 'preparation.json', prepared['result'])
        if args.apply:
            # Re-run all fingerprints immediately before replacing either entry.
            prepared = prepare(manifest)
            interrupted = False
            def interrupt(signum, frame):
                nonlocal interrupted
                if not interrupted:
                    interrupted = True
                    raise InterruptedError('Activation interrupted by ' + signal.Signals(signum).name)
            guarded_signals = (signal.SIGINT, signal.SIGTERM, signal.SIGHUP)
            original_handlers = {value: signal.signal(value, interrupt) for value in guarded_signals}
            try:
                result = activate(prepared, destination)
            finally:
                for value, handler in original_handlers.items():
                    signal.signal(value, handler)
        else:
            result = prepared['result']
        print(json.dumps({key: result[key] for key in ('round_id', 'prepared', 'applied', 'passed')}, ensure_ascii=False))
        return 0
    except (ValueError, OSError, subprocess.SubprocessError, json.JSONDecodeError) as error:
        if 'destination' in locals() and destination.is_dir() and not (destination / 'activation.json').exists():
            write_json(destination / 'failure.json', {'passed': False, 'applied': False, 'error': str(error)})
        print(json.dumps({'passed': False, 'applied': False, 'error': str(error)}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
