"""Atomic evidence, campaign limits and cancellable owned-process execution."""
import hashlib
import json
import math
import os
import resource
import shutil
import signal
import stat
import subprocess
import threading
import time
from pathlib import Path


class Blocked(RuntimeError):
    """A prerequisite, resource or campaign budget prevents execution."""


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    os.replace(str(temporary), str(path))


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def tree_hashes(root, excluded=('.venv', 'node_modules', '__pycache__', '.DS_Store')):
    root = Path(root)
    result = {}
    for current, folders, files in os.walk(str(root), followlinks=False):
        folders[:] = sorted(d for d in folders if d not in excluded)
        for name in sorted(files):
            if name not in excluded:
                path = Path(current) / name
                result[str(path.relative_to(root))] = sha256(path)
    return result


def owned_resources():
    """Only this harness and descendants; never signal unrelated applications."""
    output = subprocess.check_output(['ps', '-axo', 'pid=,ppid=,rss=,time=,command='], text=True)
    rows = {}
    for line in output.splitlines():
        parts = line.split(None,4)
        if len(parts) != 5:
            continue
        pid, parent, rss = map(int, parts[:3])
        cpu = parts[3].replace('-', ':').split(':')
        seconds = 0.0
        for part in cpu:
            seconds = seconds * 60 + float(part)
        rows[pid] = (parent, rss * 1024, seconds, parts[4])
    owned = {os.getpid()}
    while True:
        children = {pid for pid, (parent, _, _, _) in rows.items() if parent in owned}
        if children <= owned:
            break
        owned |= children
    self_usage = resource.getrusage(resource.RUSAGE_SELF)
    children_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    return {'cpu_seconds_completed':self_usage.ru_utime+self_usage.ru_stime+children_usage.ru_utime+children_usage.ru_stime,
            'io_input_blocks_completed':self_usage.ru_inblock+children_usage.ru_inblock,
            'io_output_blocks_completed':self_usage.ru_oublock+children_usage.ru_oublock,
            'rss_bytes': sum(rows.get(pid, (0, 0, 0))[1] for pid in owned),
            'cpu_seconds_live': sum(rows.get(pid, (0, 0, 0))[2] for pid in owned),
            'process_count': len(owned),
            'browser_roots': sum('chrome' in rows.get(pid,(0,0,0,''))[3].lower()
                                 and '--type=' not in rows.get(pid,(0,0,0,''))[3]
                                 and ('/MacOS/Google Chrome' in rows.get(pid,(0,0,0,''))[3]
                                      or '/chrome ' in rows.get(pid,(0,0,0,''))[3]) for pid in owned)}


def output_bytes(root):
    """Sample retained regular files while owned scratch jobs create/delete files.

    A file disappearing between directory traversal and lstat is normal under
    pressure, not a lost retained artifact or a campaign failure. Never follow
    symlinks into skills or user files when accounting campaign output.
    """
    total = 0
    for current,folders,files in os.walk(str(root),followlinks=False):
        for name in files:
            try:
                sample = (Path(current)/name).lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISREG(sample.st_mode):
                total += sample.st_size
    return total


class Budget:
    def __init__(self, out, max_hours=4, max_sessions=1000, rss_gib=8,
                 output_gib=25, min_free_gib=15, reserve_seconds=600,
                 started_wall=None, prior_sessions=None, prior_output_roots=()):
        self.out = Path(out)
        self.started_wall = time.time() if started_wall is None else started_wall
        self.started = time.monotonic() - max(0,time.time()-self.started_wall)
        self.prior_output_roots = tuple(Path(p) for p in prior_output_roots)
        self.deadline = self.started + max_hours * 3600
        self.dispatch_deadline = self.deadline - min(reserve_seconds, max_hours * 360)
        self.max_sessions = max_sessions
        self.rss_limit = rss_gib * 1024 ** 3
        self.output_limit = output_gib * 1024 ** 3
        self.free_limit = min_free_gib * 1024 ** 3
        self.lock = threading.RLock()
        self.sessions = list(prior_sessions or [])
        if self.sessions:
            save(self.out / 'session-ledger.json',self.sessions)
        self.stop_reason = None
        self.last_sample = 0
        self.samples = []
        self.cancel = threading.Event()

    def check(self, dispatch=True, force=False):
        with self.lock:
            if self.cancel.is_set():
                raise Blocked(self.stop_reason or 'campaign cancelled')
            now = time.monotonic()
            if now >= (self.dispatch_deadline if dispatch else self.deadline):
                raise Blocked('campaign time budget exhausted; preserving partial evidence')
            if force or now - self.last_sample >= 5:
                resources = owned_resources()
                size = sum(output_bytes(p) for p in (self.out,)+self.prior_output_roots)
                free = shutil.disk_usage(str(self.out)).free
                resources.update(elapsed_seconds=round(now - self.started, 3),
                                 output_bytes=size, disk_free_bytes=free)
                self.samples.append(resources)
                with (self.out / 'resources.jsonl').open('a') as stream:
                    stream.write(json.dumps(resources) + '\n')
                self.last_sample = now
                for failed, reason in ((resources['rss_bytes'] > self.rss_limit, 'owned RSS limit'),
                                       (size > self.output_limit, 'campaign output limit'),
                                       (free < self.free_limit, 'minimum free disk'),
                                       (resources['browser_roots'] > 2, 'owned browser concurrency limit')):
                    if failed:
                        self.stop_reason = reason
                        self.cancel.set()
                        raise Blocked(reason)

    def allocate_session(self, case_id, role):
        with self.lock:
            self.check()
            if len(self.sessions) >= self.max_sessions:
                raise Blocked('Agent session allowance exhausted')
            row = {'number': len(self.sessions) + 1, 'case_id': case_id, 'role': role,
                   'started_elapsed': round(time.monotonic() - self.started, 3)}
            self.sessions.append(row)
            save(self.out / 'session-ledger.json', self.sessions)
            return row['number']

    def snapshot(self):
        return {'started_wall':self.started_wall,'elapsed_seconds': round(time.monotonic() - self.started, 3),
                'prior_output_roots':[str(p) for p in self.prior_output_roots],
                'max_seconds': self.deadline - self.started, 'sessions_used': len(self.sessions),
                'max_sessions': self.max_sessions, 'stop_reason': self.stop_reason,
                'rss_limit_bytes': self.rss_limit, 'output_limit_bytes': self.output_limit,
                'min_disk_free_bytes': self.free_limit}


def terminate(process):
    # The leader may already have exited while a background descendant survives.
    # This group was created by us; never target a globally discovered process.
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        process.wait()
        return
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait()
    # Terminate resistant orphaned descendants too, even after leader exit.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    except PermissionError:
        groups = subprocess.check_output(['ps','-axo','pgid=,stat='],text=True)
        live = [line for line in groups.splitlines() if line.split() and int(line.split()[0])==process.pid
                and not line.split()[1].startswith('Z')]
        if live:
            raise Blocked('cannot terminate owned descendants')


def run_command(argv, directory, budget, cwd=None, env=None, timeout=1800, stdin=None):
    """Stream logs to disk, poll budgets; terminate the entire owned process group."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    budget.check()
    started = time.monotonic()
    status = 'pass'
    reason = None
    with (directory / 'stdout.jsonl').open('w') as stdout, (directory / 'stderr.log').open('w') as stderr:
        process = subprocess.Popen([str(x) for x in argv], cwd=cwd, env=env,
                                   stdout=stdout, stderr=stderr,
                                   stdin=subprocess.PIPE if stdin is not None else subprocess.DEVNULL,
                                   start_new_session=True, text=True)
        try:
            if stdin is not None:
                process.stdin.write(stdin)
                process.stdin.close()
            while process.poll() is None:
                budget.check(dispatch=False)
                if time.monotonic() - started > timeout:
                    raise Blocked('command timeout')
                time.sleep(.2)
        except (Blocked, KeyboardInterrupt) as exc:
            reason = str(exc) or 'interrupted'
            status = 'blocked'
        finally:
            terminate(process)
    result = {'argv': [str(x) for x in argv], 'exit_code': process.returncode,
              'seconds': round(time.monotonic() - started, 4),
              'status': status if status == 'blocked' else 'pass' if process.returncode == 0 else 'fail'}
    if reason:
        result['reason'] = reason
    save(directory / 'command.json', result)
    if status == 'blocked':
        raise Blocked(reason)
    return result


def metrics(samples, seconds, rejected=0, queue_peak=0):
    elapsed = sorted(row['seconds'] for row in samples)
    def percentile(q):
        return elapsed[max(0, math.ceil(q * len(elapsed)) - 1)] if elapsed else None
    return {'seconds': seconds, 'sample_count': len(samples),
            'completed': sum(row['status'] == 'pass' for row in samples),
            'errors': sum(row['status'] != 'pass' for row in samples),
            'error_rate': sum(row['status'] != 'pass' for row in samples) / len(samples) if samples else None,
            'throughput_per_second': len(samples) / seconds if seconds else None,
            'p50_seconds': percentile(.5), 'p95_seconds': percentile(.95),
            'p99_seconds': percentile(.99), 'explicit_rejections': rejected, 'queue_peak': queue_peak}
