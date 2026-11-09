#!/usr/bin/env python3
"""Loopback-only HTTP/SQLite workbench; no model API or external service calls."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import hashlib
import fcntl
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ipaddress
import json
import logging
import mimetypes
import os
from pathlib import Path
import re
import shutil
import signal
import site
import socket
import sqlite3
import subprocess
import sys
import threading
import time
from urllib.parse import parse_qs, quote, unquote, urlsplit
import uuid

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'togaf-standard-10th-ai/skills' / '_shared' / 'scripts'
WEB = Path(__file__).resolve().parent / 'web'
MAX_BODY = 8 * 1024 * 1024
NOTICE = '本地声明身份，不是身份认证、专业批准或业务合规证明；生成不代表评审通过。'
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS.parent / 'vendor'))


def now():
    return datetime.now(timezone.utc).isoformat()


def dumps(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(dumps(value).encode()).hexdigest()


def reject_constant(value):
    raise ValueError('Non-finite JSON number: ' + value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


class APIError(Exception):
    def __init__(self, status, error, message, issues=None):
        super().__init__(message)
        self.status = status
        self.payload = {'error': error, 'message': message}
        if issues is not None:
            self.payload['issues'] = issues


def required_text(data, key, limit=1000):
    value = data.get(key)
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise APIError(400, 'invalid_request', f'{key} must be a nonempty string (max {limit})')
    return value


def validation(model):
    from validate import validate
    try:
        issues = validate(model)
    except (ValueError, TypeError, KeyError, RecursionError, OverflowError) as exc:
        # Malformed input must fail closed, never be repaired or count as a pass.
        issues = [{'level': 'error', 'code': 'validation-input', 'id': 'model', 'message': str(exc)}]
    return {'issues': issues, 'valid': not any(i['level'] == 'error' for i in issues)}


def checked_model(model):
    result = validation(model)
    if not result['valid']:
        raise APIError(422, 'validation_failed', 'Model has validation errors', result['issues'])
    return result


def native_source(value):
    from workbench.native import normalize
    try:
        return normalize(value)
    except (ValueError, TypeError) as exc:
        raise APIError(400, 'invalid_native_request', str(exc)) from None


def snapshot_validation(model, native=None):
    result = checked_model(model)
    if native is not None:
        from workbench.native import diagnose
        result['native'] = diagnose(native)
        result['valid'] = result['valid'] and result['native']['valid']
    return result


def checked_native(native):
    if native is None:
        raise APIError(422, 'native_material_missing', 'This version has no native XML source')
    from workbench.native import diagnose
    result = diagnose(native)
    if not result['valid']:
        raise APIError(422, 'native_validation_failed', 'Native draft has validation errors', result['validation_errors'])
    return result


def native_companion(name):
    """A native-only project has no invented architecture entities or relations."""
    return {'schema_version': '2.0', 'project': {
        'id': 'native-' + uuid.uuid4().hex, 'name': name, 'version': '1',
        'context': {'domains': ['business'], 'landscape': 'capability', 'purpose': 'solution-delivery',
                    'abstraction': 'logical', 'evolution': 'target'},
        'is_example': False, 'approval_status': 'unknown', 'implementation_status': 'unknown'},
        'sources': [], 'entities': [], 'relationships': [], 'views': [], 'deliverables': [], 'gaps': []}


def loopback(host):
    if host.lower() == 'localhost':
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def safe_parts(path):
    if not path or '\\' in path or '\x00' in path or path.startswith('/'):
        raise APIError(403, 'unsafe_path', 'Invalid file path')
    parts = path.split('/')
    if any(part in ('', '.', '..') for part in parts):
        raise APIError(403, 'unsafe_path', 'Path traversal is forbidden')
    return parts


def open_safe(root, relative):
    """Open each component without following symlinks, including the root."""
    parts = safe_parts(relative)
    fd = None
    try:
        root_path = Path(root).absolute()
        fd = os.open(root_path.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        for part in list(root_path.parts[1:]) + parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        file_fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
        import stat
        if not stat.S_ISREG(os.fstat(file_fd).st_mode):
            os.close(file_fd)
            raise APIError(403, 'unsafe_path', 'Only regular files can be downloaded')
        return os.fdopen(file_fd, 'rb')
    except OSError:
        raise APIError(404, 'not_found', 'File not found (symlinks are forbidden)') from None
    finally:
        if fd is not None:
            os.close(fd)


def diff_snapshots(before, after):
    changes = []
    missing = object()

    def add(group, identity, a, b):
        if a == b:
            return
        changes.append({'group': group, 'id': identity,
                        'kind': 'added' if a is missing else 'removed' if b is missing else 'modified',
                        'before': None if a is missing else a, 'after': None if b is missing else b})

    for group in sorted(set(before['model']) | set(after['model'])):
        a, b = before['model'].get(group, missing), after['model'].get(group, missing)
        if isinstance(a, list) and isinstance(b, list) and all(
                isinstance(x, dict) and isinstance(x.get('id'), str) for x in a + b):
            aa, bb = {x['id']: x for x in a}, {x['id']: x for x in b}
            for identity in sorted(set(aa) | set(bb)):
                add(group, identity, aa.get(identity, missing), bb.get(identity, missing))
            # Ordering itself is part of the model (e.g. process/view selection order).
            if [x['id'] for x in a] != [x['id'] for x in b]:
                add(group, '$order', [x['id'] for x in a], [x['id'] for x in b])
        else:
            add(group, group, a, b)
    add('layout', 'layout', before['layout'], after['layout'])
    a, b = before.get('native') or {}, after.get('native') or {}
    for field in sorted(set(a) | set(b)):
        add('native', field, a.get(field, missing), b.get(field, missing))
    return changes


class Workbench:
    def __init__(self, data_dir, *, job_timeout=180, max_job_bytes=512 * 1024 ** 2,
                 max_job_store_bytes=2 * 1024 ** 3, failed_output_retention_days=7,
                 start_worker=True):
        if max_job_bytes <= 0 or max_job_store_bytes <= 0 or failed_output_retention_days < 0:
            raise ValueError('Job storage limits must be positive; retention days cannot be negative')
        self.max_job_bytes = max_job_bytes
        self.max_job_store_bytes = max_job_store_bytes
        self.failed_output_retention_days = failed_output_retention_days
        self.data_dir = Path(data_dir).expanduser().resolve()
        shared = (ROOT / 'togaf-standard-10th-ai/skills').resolve()
        if self.data_dir == ROOT or self.data_dir == WEB or self.data_dir.is_relative_to(shared) or self.data_dir.is_relative_to(WEB):
            raise ValueError('Data directory must not be the repository, static web root, or shared skills')
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.jobs_dir = self.data_dir / 'jobs'
        self.jobs_dir.mkdir(exist_ok=True)
        if self.jobs_dir.is_symlink():
            raise ValueError('Job directory cannot be a symlink')
        self.db_path = self.data_dir / 'workbench.sqlite3'
        if self.db_path.is_symlink():
            raise ValueError('Database cannot be a symlink')
        self.instance_fd = os.open(self.data_dir / '.server.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        try:
            fcntl.flock(self.instance_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            os.close(self.instance_fd)
            self.instance_fd = None
            raise ValueError('Another workbench server is already using this data directory') from None
        self.lock = threading.RLock()
        self.wake = threading.Event()
        self.stop = threading.Event()
        self.job_timeout = job_timeout
        self.process = None
        self.thread = None
        with self.db() as db:
            db.executescript('''
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY, name TEXT NOT NULL, head_version TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS versions (
                    project_id TEXT NOT NULL, id TEXT NOT NULL, parent TEXT,
                    created_at TEXT NOT NULL, message TEXT NOT NULL, model TEXT NOT NULL,
                    layout TEXT NOT NULL, validation TEXT NOT NULL, model_hash TEXT NOT NULL,
                    PRIMARY KEY(project_id,id), FOREIGN KEY(project_id) REFERENCES projects(id));
                CREATE TABLE IF NOT EXISTS reviews (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL, version TEXT NOT NULL,
                    action TEXT NOT NULL, author TEXT NOT NULL, comment TEXT NOT NULL,
                    state TEXT NOT NULL, created_at TEXT NOT NULL,
                    FOREIGN KEY(project_id,version) REFERENCES versions(project_id,id));
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL, version TEXT NOT NULL,
                    status TEXT NOT NULL, render INTEGER NOT NULL, created_at TEXT NOT NULL,
                    started_at TEXT, finished_at TEXT, error TEXT, outputs_pruned_at TEXT,
                    FOREIGN KEY(project_id,version) REFERENCES versions(project_id,id));
            ''')
            for table, name, declaration in (
                    ('versions', 'native', 'TEXT'),
                    ('jobs', 'kind', "TEXT NOT NULL DEFAULT 'project'"),
                    ('jobs', 'auto_layout', 'INTEGER NOT NULL DEFAULT 0'),
                    ('jobs', 'outputs_pruned_at', 'TEXT')):
                columns = {row['name'] for row in db.execute('PRAGMA table_info(' + table + ')')}
                if name not in columns:
                    db.execute('ALTER TABLE ' + table + ' ADD COLUMN ' + name + ' ' + declaration)
            db.execute("UPDATE jobs SET status='failed', finished_at=?, error=? WHERE status='running'",
                       (now(), 'Server restarted while generation was running; no result accepted'))
        self.prune_failed_outputs()
        if start_worker:
            self.thread = threading.Thread(target=self._worker, name='workbench-generator', daemon=True)
            self.thread.start()

    @contextmanager
    def db(self):
        with self.lock:
            conn = sqlite3.connect(self.db_path, timeout=10)
            conn.row_factory = sqlite3.Row
            conn.execute('PRAGMA foreign_keys=ON')
            try:
                with conn:
                    yield conn
            finally:
                conn.close()

    @staticmethod
    def tree_bytes(root):
        total = 0
        if not root.is_dir() or root.is_symlink():
            return total
        for directory, folders, files in os.walk(root, followlinks=False):
            folders[:] = [name for name in folders if not (Path(directory) / name).is_symlink()]
            for name in files:
                path = Path(directory) / name
                if not path.is_symlink():
                    try:
                        total += path.lstat().st_blocks * 512
                    except FileNotFoundError:
                        pass
        return total

    def storage_issue(self, identity):
        if self.tree_bytes(self.jobs_dir / identity) > self.max_job_bytes:
            return 'Job output exceeded the per-job storage limit'
        if self.tree_bytes(self.jobs_dir) > self.max_job_store_bytes:
            return 'Job store exceeded the total storage limit'
        return None

    def trim_generation_log(self, identity):
        """Keep the diagnostic tail without retaining an unbounded worker log."""
        path = self.jobs_dir / identity / 'generation.log'
        if not path.is_file() or path.is_symlink():
            return
        limit = max(1, min(8 * 1024 ** 2, self.max_job_bytes // 8))
        if path.stat().st_size <= limit:
            return
        with path.open('rb') as stream:
            stream.seek(-limit, os.SEEK_END)
            tail = stream.read()
        path.write_bytes(tail)

    def prune_failed_outputs(self, *, older_than_days=None):
        """Retain failed job metadata and logs, discard only expired partial outputs."""
        days = self.failed_output_retention_days if older_than_days is None else older_than_days
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
        with self.db() as db:
            identities = [row['id'] for row in db.execute(
                "SELECT id FROM jobs WHERE status='failed' AND finished_at IS NOT NULL AND finished_at<=?", (cutoff,))]
        removed = 0
        for identity in identities:
            output = self.output_root(identity)
            if output.is_dir() and not output.is_symlink():
                shutil.rmtree(output)
                removed += 1
        return removed

    def prune_completed_outputs(self, older_than_days, *, apply=False):
        """Preview or remove old successful/blocked attachments, keeping job records."""
        if older_than_days < 0:
            raise ValueError('Completed job retention days cannot be negative')
        cutoff = (datetime.now(timezone.utc) - timedelta(days=older_than_days)).isoformat()
        with self.db() as db:
            rows = [dict(row) for row in db.execute(
                "SELECT id,status FROM jobs WHERE status IN ('succeeded','blocked') "
                "AND finished_at IS NOT NULL AND finished_at<=? AND outputs_pruned_at IS NULL", (cutoff,))]
        candidates = []
        for row in rows:
            output = self.output_root(row['id'])
            if output.is_dir() and not output.is_symlink():
                candidates.append({'id': row['id'], 'status': row['status'], 'bytes': self.tree_bytes(output)})
        if apply:
            for row in candidates:
                shutil.rmtree(self.output_root(row['id']))
                with self.db() as db:
                    db.execute('UPDATE jobs SET outputs_pruned_at=? WHERE id=?', (now(), row['id']))
        return {'applied': apply, 'jobs': candidates, 'total_bytes': sum(row['bytes'] for row in candidates)}

    @staticmethod
    def project_row(db, identity):
        row = db.execute('SELECT * FROM projects WHERE id=?', (identity,)).fetchone()
        if row is None:
            raise APIError(404, 'not_found', 'Project not found')
        return dict(row)

    @staticmethod
    def state(db, project, version):
        row = db.execute("SELECT state FROM reviews WHERE project_id=? AND version=? ORDER BY rowid DESC LIMIT 1",
                         (project, version)).fetchone()
        return row['state'] if row else 'draft'

    def version(self, db, project, identity):
        row = db.execute('SELECT * FROM versions WHERE project_id=? AND id=?', (project, identity)).fetchone()
        if row is None:
            raise APIError(404, 'not_found', 'Version not found')
        result = dict(row)
        for key in ('model', 'layout', 'validation'):
            result[key] = json.loads(result[key])
        result['native'] = json.loads(result['native']) if result['native'] is not None else None
        result['native_sha256'] = result['native']['source_sha256'] if result['native'] else None
        result['review_state'] = self.state(db, project, identity)
        result['version_hash'] = result['id']
        return result

    def detail(self, db, identity):
        project = self.project_row(db, identity)
        rows = db.execute('SELECT id FROM versions WHERE project_id=? ORDER BY rowid', (identity,)).fetchall()
        versions = [self.version(db, identity, row['id']) for row in rows]
        head = next(v for v in versions if v['id'] == project['head_version'])
        project.update(model=head['model'], layout=head['layout'], native=head['native'], validation=head['validation'],
                       versions=[{k: v for k, v in row.items() if k not in ('model', 'layout', 'native')} for row in versions],
                       reviews=[self.review_dict(r) for r in db.execute(
                           'SELECT * FROM reviews WHERE project_id=? ORDER BY rowid', (identity,))],
                       jobs=[self.job(db, r['id']) for r in db.execute(
                           'SELECT id FROM jobs WHERE project_id=? ORDER BY rowid', (identity,))],
                       review_states={v['id']: v['review_state'] for v in versions},
                       review_state=head['review_state'], notice=NOTICE)
        return project

    @staticmethod
    def review_dict(row):
        result = dict(row)
        result.update(version_hash=result['version'], notice=NOTICE)
        return result

    def insert_version(self, db, project, model, layout, message, parent, result, native=None):
        stamp = now()
        content = dict(model=model, layout=layout, parent=parent, created_at=stamp, message=message)
        if native is not None:
            content['native'] = native
        identity = digest(content)
        db.execute('INSERT INTO versions (project_id,id,parent,created_at,message,model,layout,validation,model_hash,native) VALUES (?,?,?,?,?,?,?,?,?,?)',
                   (project, identity, parent, stamp, message, dumps(model), dumps(layout), dumps(result), digest(model),
                    dumps(native) if native is not None else None))
        db.execute('UPDATE projects SET head_version=?, updated_at=? WHERE id=?', (identity, stamp, project))
        return identity

    def create_project(self, data):
        name = required_text(data, 'name', 200)
        native = native_source(data.get('native'))
        if 'model' in data:
            model = data['model']
        elif native is not None:
            model = native_companion(name)
        else:
            from registry import load
            from profile_examples import normalize_example
            template = data.get('template', 'trust-framework-default')
            if not isinstance(template, str):
                raise APIError(400, 'invalid_request', 'template must be a catalog id')
            profile = load()[2].get(template)
            if not profile or not isinstance(profile.get('example'), dict):
                raise APIError(400, 'unknown_template', 'Unknown template')
            model = normalize_example(profile)
        result = snapshot_validation(model, native)
        identity, stamp = uuid.uuid4().hex, now()
        with self.db() as db:
            db.execute('INSERT INTO projects VALUES (?,?,?,?,?)', (identity, name, '', stamp, stamp))
            self.insert_version(db, identity, model, {}, 'Initial version', None, result, native)
            return self.detail(db, identity)

    def save_version(self, project, data):
        base = required_text(data, 'base_version', 128)
        if 'model' not in data or not isinstance(data.get('layout', {}), dict):
            raise APIError(400, 'invalid_request', 'model is required; layout must be an object')
        message = data.get('message', '')
        if not isinstance(message, str) or len(message) > 4000:
            raise APIError(400, 'invalid_request', 'message must be a string (max 4000)')
        with self.db() as db:
            current = self.project_row(db, project)
            if current['head_version'] != base:
                raise APIError(409, 'version_conflict', 'Head changed; reload and explicitly merge before saving')
            previous = self.version(db, project, base)
            native = native_source(data['native']) if 'native' in data else previous['native']
            result = snapshot_validation(data['model'], native)
            self.insert_version(db, project, data['model'], data.get('layout', {}), message, base, result, native)
            return self.detail(db, project)

    def review(self, project, data):
        version = required_text(data, 'version', 128)
        author = required_text(data, 'author', 200)
        action = data.get('action')
        comment = data.get('comment', '')
        if action not in ('submit', 'comment', 'request_changes', 'accept') or not isinstance(comment, str) or len(comment) > 20000:
            raise APIError(400, 'invalid_request', 'Invalid review action or comment')
        with self.db() as db:
            self.project_row(db, project)
            snapshot = self.version(db, project, version)
            state = snapshot['review_state']
            if action == 'submit':
                if state != 'draft':
                    raise APIError(409, 'review_transition', 'Only draft versions can be submitted; revise to create a new draft')
                state = 'in_review'
            elif action in ('request_changes', 'accept'):
                if state != 'in_review':
                    raise APIError(409, 'review_transition', 'Version must be in_review')
                if action == 'accept':
                    checked_model(snapshot['model'])
                    if snapshot['native'] is not None:
                        checked_native(snapshot['native'])
                state = 'accepted' if action == 'accept' else 'changes_requested'
            row = dict(id=uuid.uuid4().hex, project_id=project, version=version, action=action,
                       author=author, comment=comment, state=state, created_at=now())
            db.execute('INSERT INTO reviews VALUES (:id,:project_id,:version,:action,:author,:comment,:state,:created_at)', row)
            return self.review_dict(row)

    def enqueue(self, project, data):
        version = required_text(data, 'version', 128)
        render = data.get('render', False)
        kind, auto_layout = data.get('kind', 'project'), data.get('auto_layout', False)
        if not isinstance(render, bool):
            raise APIError(400, 'invalid_request', 'render must be a boolean')
        if kind not in ('project', 'native') or not isinstance(auto_layout, bool):
            raise APIError(400, 'invalid_request', 'kind must be project/native; auto_layout must be a boolean')
        self.prune_failed_outputs()
        if self.tree_bytes(self.jobs_dir) >= self.max_job_store_bytes:
            raise APIError(507, 'storage_limit', 'Job store is full; archive or remove older job outputs before generating')
        with self.db() as db:
            self.project_row(db, project)
            snapshot = self.version(db, project, version)
            checked_model(snapshot['model'])
            if kind == 'native' or snapshot['native'] is not None:
                checked_native(snapshot['native'])
            identity = uuid.uuid4().hex
            db.execute('INSERT INTO jobs (id,project_id,version,status,render,created_at,kind,auto_layout) VALUES (?,?,?,?,?,?,?,?)',
                       (identity, project, version, 'queued', int(render), now(), kind, int(auto_layout)))
            result = self.job(db, identity)
        self.wake.set()
        return result

    def output_root(self, identity):
        if not re.fullmatch('[0-9a-f]{32}', identity):
            raise APIError(404, 'not_found', 'Job not found')
        job_root = self.jobs_dir / identity
        if job_root.is_symlink():
            raise APIError(403, 'unsafe_path', 'Job directory symlink forbidden')
        return job_root / 'outputs'

    def job(self, db, identity):
        row = db.execute('SELECT * FROM jobs WHERE id=?', (identity,)).fetchone()
        if row is None:
            raise APIError(404, 'not_found', 'Job not found')
        result = dict(row)
        result.update(render=bool(result['render']), auto_layout=bool(result['auto_layout']),
                      outputs_pruned=bool(result['outputs_pruned_at']), version_hash=result['version'], outputs=[], notice=NOTICE)
        root = self.output_root(identity)
        if result['status'] in ('succeeded', 'blocked') and root.is_dir() and not root.is_symlink():
            for path in sorted(root.rglob('*')):
                relative = path.relative_to(root).as_posix()
                if path.is_symlink() or not path.is_file():
                    continue
                try:
                    with open_safe(root, relative):
                        pass
                except APIError:
                    continue
                result['outputs'].append({'name': relative, 'url': f'/api/jobs/{identity}/files/{quote(relative)}'})
            if result['kind'] == 'native':
                with open_safe(root, 'manifest.json') as stream:
                    manifest = json.load(stream)
                result['native_preview'] = manifest.get('preview')
                result['native_source_sha256'] = manifest.get('native_source_sha256')
                result['full_language_acceptance'] = manifest.get('full_language_acceptance', False)
        return result

    def _worker(self):
        while not self.stop.is_set():
            # The child inherits this semaphore descriptor: even an orphaned
            # generation process after a server crash cannot overlap a new job.
            fd = os.open(self.data_dir / '.generation.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
            try:
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    self.stop.wait(.1)
                    continue
                with self.db() as db:
                    row = db.execute("SELECT * FROM jobs WHERE status='queued' ORDER BY rowid LIMIT 1").fetchone()
                    if row:
                        db.execute("UPDATE jobs SET status='running', started_at=? WHERE id=?", (now(), row['id']))
                if row:
                    try:
                        self._run_job(dict(row), fd)
                    except Exception as exc:
                        logging.warning('Generation job %s failed: %s', row['id'], exc)
                        with self.db() as db:
                            db.execute("UPDATE jobs SET status='failed', finished_at=?, error=? WHERE id=?",
                                       (now(), str(exc)[-8000:], row['id']))
                    finally:
                        try:
                            self.trim_generation_log(row['id'])
                        except OSError as exc:
                            logging.warning('Could not trim generation log for %s: %s', row['id'], exc)
            finally:
                os.close(fd)
            if row is None:
                self.wake.wait()
                self.wake.clear()

    def _run_job(self, job, semaphore_fd):
        with self.db() as db:
            snapshot = self.version(db, job['project_id'], job['version'])
        root = self.output_root(job['id'])
        root.parent.mkdir(exist_ok=False)
        root.mkdir()
        native = job.get('kind') == 'native'
        model_file = root.parent / ('input-native.json' if native else 'input.json')
        model_file.write_text(dumps(snapshot['native'] if native else snapshot['model']), encoding='utf-8')
        # This snapshot is retained separately: drag layout is editorial metadata,
        # not generate.py's reference/adaptive renderer selection.
        (root.parent / 'layout.json').write_text(dumps(snapshot['layout']), encoding='utf-8')
        command = [sys.executable, str(Path(__file__).resolve()), '--native-worker' if native else '--generate-worker', str(model_file), '--out', str(root),
                   '--worker-timeout', str(self.job_timeout)]
        if job['render']:
            command.append('--render')
        if native and job.get('auto_layout'):
            command.append('--auto-layout')
        env = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'HOME': str(root.parent),
               # HOME is job-local; keep the invoking interpreter's installed
               # Python dependencies available without a second skills venv.
               'PYTHONUSERBASE': site.getuserbase(),
               'TMPDIR': str(root.parent), 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONIOENCODING': 'utf-8',
               'LANG': os.environ.get('LANG', 'en_US.UTF-8')}
        if os.environ.get('TOGAF_BROWSER_PATH'):
            env['TOGAF_BROWSER_PATH'] = os.environ['TOGAF_BROWSER_PATH']
        with (root.parent / 'generation.log').open('wb') as log:
            process = subprocess.Popen(command, cwd=root.parent, env=env, stdout=log, stderr=subprocess.STDOUT,
                                       start_new_session=True, pass_fds=(semaphore_fd,))
            with self.lock:
                self.process = process
                if self.stop.is_set():
                    self._kill(process)
            try:
                deadline = time.monotonic() + self.job_timeout
                while True:
                    try:
                        code = process.wait(timeout=min(1, max(0.01, deadline - time.monotonic())))
                        break
                    except subprocess.TimeoutExpired:
                        issue = self.storage_issue(job['id'])
                        if issue:
                            self._kill(process)
                            process.wait()
                            shutil.rmtree(root)
                            raise RuntimeError(issue) from None
                        if time.monotonic() >= deadline:
                            self._kill(process)
                            process.wait()
                            raise RuntimeError(f'Generation timed out after {self.job_timeout:g}s') from None
            finally:
                with self.lock:
                    self.process = None
        issue = self.storage_issue(job['id'])
        if issue:
            shutil.rmtree(root)
            raise RuntimeError(issue)
        if code:
            with (root.parent / 'generation.log').open('rb') as log:
                log.seek(max(0, log.seek(0, os.SEEK_END) - 6000))
                detail = log.read().decode('utf-8', errors='replace')
            raise RuntimeError(f'Generator exited {code}: {detail}')
        with open_safe(root, 'manifest.json') as handle:
            manifest = json.load(handle)
        if not manifest.get('runtime_stable') or not manifest.get('output_sha256'):
            raise RuntimeError('Incomplete or unstable generation manifest')
        if native:
            expected_source = snapshot['native']['source_sha256']
            original_name = 'native.bpmn' if snapshot['native']['language'] == 'bpmn' else 'native.uml'
            if manifest.get('native_source_sha256') != expected_source:
                raise RuntimeError('Native manifest does not bind the immutable version source')
            with open_safe(root, original_name) as handle:
                if hashlib.sha256(handle.read()).hexdigest() != expected_source:
                    raise RuntimeError('Native output does not preserve the immutable version source')
        for name, expected in manifest['output_sha256'].items():
            with open_safe(root, name) as handle:
                actual = hashlib.sha256(handle.read()).hexdigest()
            if actual != expected:
                raise RuntimeError('Output hash mismatch: ' + name)
        (root / 'workbench-layout.json').write_text(dumps(snapshot['layout']), encoding='utf-8')
        with self.db() as db:
            status = manifest.get('job_status', 'succeeded') if native else 'succeeded'
            if status not in ('succeeded', 'blocked'):
                raise RuntimeError('Native generator returned an unsupported completion status')
            db.execute("UPDATE jobs SET status=?, finished_at=?, error=NULL WHERE id=?", (status, now(), job['id']))

    @staticmethod
    def _kill(process):
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass

    def close(self):
        self.stop.set()
        self.wake.set()
        with self.lock:
            if self.process:
                self._kill(self.process)
        if self.thread:
            self.thread.join(timeout=10)
        if self.instance_fd is not None:
            os.close(self.instance_fd)
            self.instance_fd = None


class Handler(BaseHTTPRequestHandler):
    server_version = 'LocalWorkbench/1.0'
    protocol_version = 'HTTP/1.1'

    def log_message(self, fmt, *args):
        logging.info('%s %s', self.address_string(), fmt % args)

    def security(self, mutation=False):
        if not loopback(self.client_address[0]):
            raise APIError(403, 'forbidden_host', 'Only loopback clients are allowed')
        hosts = self.headers.get_all('Host', [])
        if len(hosts) != 1:
            raise APIError(403, 'forbidden_host', 'One loopback Host header is required')
        try:
            host = urlsplit('http://' + hosts[0])
            allowed = (not host.username and not host.password and not host.path and not host.query and not host.fragment
                       and host.hostname and loopback(host.hostname) and host.port == self.server.server_port)
        except ValueError:
            allowed = False
        if not allowed:
            raise APIError(403, 'forbidden_host', 'Host must identify this loopback server and port')
        origins = self.headers.get_all('Origin', [])
        if origins:
            try:
                origin = urlsplit(origins[0])
                same = (len(origins) == 1 and origin.scheme == 'http' and not origin.username and not origin.password
                        and not origin.path and not origin.query and not origin.fragment
                        and origin.hostname == host.hostname and origin.port == host.port)
            except ValueError:
                same = False
            if not same:
                raise APIError(403, 'forbidden_origin', 'Cross-origin requests are forbidden')
        if self.headers.get('Sec-Fetch-Site') == 'cross-site':
            raise APIError(403, 'forbidden_origin', 'Cross-site requests are forbidden')
        if mutation and self.headers.get_content_type() != 'application/json':
            raise APIError(415, 'content_type', 'Content-Type must be application/json')

    def body(self):
        lengths = self.headers.get_all('Content-Length', [])
        if self.headers.get_all('Transfer-Encoding') or len(lengths) != 1 or not re.fullmatch(r'[0-9]+', lengths[0]):
            raise APIError(400, 'invalid_request', 'One Content-Length and no Transfer-Encoding required')
        if len(lengths[0]) > 9:
            raise APIError(413, 'body_too_large', 'Request body limit is 8 MiB')
        length = int(lengths[0])
        if length > MAX_BODY:
            raise APIError(413, 'body_too_large', 'Request body limit is 8 MiB')
        self.connection.settimeout(15)
        raw = self.rfile.read(length)
        if len(raw) != length:
            raise APIError(400, 'invalid_json', 'Incomplete request body')
        try:
            data = json.loads(raw.decode('utf-8'), parse_constant=reject_constant, object_pairs_hook=unique_object)
            dumps(data)  # Also reject floating point overflow (1e999).
        except (ValueError, UnicodeError, RecursionError):
            raise APIError(400, 'invalid_json', 'Expected finite UTF-8 JSON without duplicate keys') from None
        if not isinstance(data, dict):
            raise APIError(400, 'invalid_request', 'Request must be a JSON object')
        return data

    def do_GET(self):
        self.handle_request(False)

    def do_POST(self):
        self.handle_request(True)

    def do_OPTIONS(self):
        self.json_response(405, {'error': 'method_not_allowed', 'message': 'Cross-origin access is not enabled'})

    def do_PUT(self):
        self.do_OPTIONS()

    do_DELETE = do_PUT
    do_PATCH = do_PUT

    def handle_request(self, mutation):
        self.close_connection = True  # No ambiguous body/pipeline reuse on failures.
        try:
            self.security(mutation)
            url = urlsplit(self.path)
            if url.scheme or url.netloc or url.fragment:
                raise APIError(400, 'invalid_request', 'Only origin-form URLs are supported')
            try:
                path = unquote(url.path, errors='strict')
            except UnicodeError:
                raise APIError(400, 'invalid_request', 'Invalid URL encoding') from None
            if '\\' in path or '\x00' in path or any(part in ('.', '..') for part in path.split('/')):
                raise APIError(403, 'unsafe_path', 'Path traversal is forbidden')
            data = self.body() if mutation else None
            status, result = self.route(path, parse_qs(url.query), data)
            if result is not None:
                self.json_response(status, result)
        except APIError as exc:
            self.json_response(exc.status, exc.payload)
        except (BrokenPipeError, ConnectionResetError, socket.timeout):
            self.close_connection = True
        except Exception:
            logging.exception('HTTP request failed')
            self.json_response(500, {'error': 'internal_error', 'message': 'Internal error; see local server log'})

    def route(self, path, query, data):
        app = self.server.app
        get = data is None
        parts = path.strip('/').split('/')
        if path == '/api/health' and get:
            return 200, {'status': 'ok', 'local_only': True, 'notice': NOTICE}
        if path == '/api/catalog' and get:
            from registry import load
            arts, dels, profiles, methods = load()
            return 200, {'templates': [{'id': p['id'], 'name': p.get('name', p['id'])}
                                       for p in profiles.values() if isinstance(p.get('example'), dict)],
                         'artifacts': list(arts.values()), 'deliverables': list(dels.values()),
                         'profiles': list(profiles.values()), 'analysis_methods': methods, 'notice': NOTICE}
        if path == '/api/validate' and not get:
            if 'model' not in data:
                raise APIError(400, 'invalid_request', 'model is required')
            return 200, validation(data['model'])
        if path == '/api/native/unpack' and not get:
            from workbench.native import unpack_package,diagnose
            from standards import Incomplete
            try:
                native=unpack_package(data.get('package'))
            except Incomplete as exc:
                raise APIError(422,'native_capability_uncovered',str(exc)) from None
            except (ValueError,TypeError) as exc:
                raise APIError(400,'invalid_native_request',str(exc)) from None
            return 200,{'native':native,'diagnostic':diagnose(native)}
        if path == '/api/native/validate' and not get:
            native = native_source(data.get('native'))
            if native is None:
                raise APIError(400, 'invalid_native_request', 'native source is required')
            from workbench.native import diagnose
            return 200, diagnose(native)
        if path == '/api/projects':
            if not get:
                return 201, app.create_project(data)
            with app.db() as db:
                return 200, {'projects': [dict(r) for r in db.execute('SELECT * FROM projects ORDER BY updated_at DESC')]}
        if len(parts) >= 3 and parts[:2] == ['api', 'projects']:
            project = parts[2]
            if len(parts) == 3 and get:
                with app.db() as db:
                    return 200, app.detail(db, project)
            if len(parts) == 4 and parts[3] == 'versions' and not get:
                return 201, app.save_version(project, data)
            if len(parts) == 5 and parts[3] == 'versions' and get:
                with app.db() as db:
                    return 200, app.version(db, project, parts[4])
            if len(parts) == 4 and parts[3] == 'reviews' and not get:
                return 201, app.review(project, data)
            if len(parts) == 4 and parts[3] == 'generate' and not get:
                return 202, app.enqueue(project, data)
            if len(parts) == 4 and parts[3] == 'diff' and get:
                if len(query.get('from', [])) != 1 or len(query.get('to', [])) != 1:
                    raise APIError(400, 'invalid_request', 'from and to version ids are required')
                a, b = query['from'][0], query['to'][0]
                with app.db() as db:
                    before, after = app.version(db, project, a), app.version(db, project, b)
                return 200, {'from': a, 'to': b, 'changes': diff_snapshots(before, after)}
        if len(parts) >= 3 and parts[:2] == ['api', 'jobs'] and get:
            with app.db() as db:
                job = app.job(db, parts[2])
            if len(parts) == 3:
                return 200, job
            if len(parts) >= 5 and parts[3] == 'files':
                if job['status'] not in ('succeeded', 'blocked'):
                    raise APIError(409, 'job_not_ready', 'Only successful job outputs are downloadable')
                self.send_file(app.output_root(parts[2]), '/'.join(parts[4:]), download=True)
                return 200, None
        if path.startswith('/api/') or not get:
            raise APIError(404, 'not_found', 'API route not found')
        self.send_file(WEB, 'index.html' if path == '/' else path.lstrip('/'), download=False)
        return 200, None

    def common_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Connection', 'close')

    def json_response(self, status, value):
        body = dumps(value).encode('utf-8')
        self.send_response(status)
        self.common_headers()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, root, relative, download):
        with open_safe(root, relative) as handle:
            self.send_response(200)
            self.common_headers()
            self.send_header('Content-Type', (mimetypes.guess_type(relative)[0] or 'application/octet-stream'))
            self.send_header('Content-Length', str(os.fstat(handle.fileno()).st_size))
            if download:
                self.send_header('Content-Disposition', "attachment; filename*=UTF-8''" + quote(Path(relative).name))
                self.send_header('Content-Security-Policy', "sandbox; default-src 'none'")
            else:
                self.send_header('Content-Security-Policy', "default-src 'self'; connect-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
            self.end_headers()
            shutil.copyfileobj(handle, self.wfile)


def create_server(host='127.0.0.1', port=8765, data_dir=None, **kwargs):
    if not loopback(host):
        raise ValueError('Refusing non-loopback bind; use 127.0.0.1, ::1, or localhost')
    cls = ThreadingHTTPServer
    if ':' in host:
        class IPv6Server(ThreadingHTTPServer):
            address_family = socket.AF_INET6
        cls = IPv6Server
    app = Workbench(data_dir or ROOT / 'output' / 'workbench-data', **kwargs)
    try:
        server = cls((host, port), Handler)
        server.app = app
        server.daemon_threads = True
        return server
    except Exception:
        app.close()
        raise


def generation_worker(model_path, out, render=False, native=False, auto_layout=False):
    """Fixed local generator entrypoint, with Python egress/write protection."""
    allowed = Path(out).resolve().parent

    def writable(path):
        if isinstance(path, int):
            return
        resolved = Path(os.fsdecode(path)).resolve()
        if not resolved.is_relative_to(allowed):
            raise PermissionError('Generator writes must stay within its job directory')

    def audit(event, args):
        if event in ('socket.connect', 'socket.connect_ex', 'socket.bind', 'socket.getaddrinfo', 'urllib.Request'):
            raise PermissionError('External network is disabled in generation workers')
        if event == 'open':
            mode, flags = args[1], args[2]
            if (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)):
                writable(args[0])
        elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.truncate'):
            writable(args[0])
        elif event in ('os.rename', 'os.link', 'os.symlink'):
            writable(args[0])
            writable(args[1])
        elif event == 'subprocess.Popen':
            command = args[1]
            if (native and isinstance(command, (list, tuple)) and len(command) == 3
                    and command[0] in {'node', shutil.which('node')}
                    and Path(command[1]).resolve() in {SCRIPTS / 'bpmn_render.mjs', SCRIPTS / 'bpmn_design_render.mjs', SCRIPTS / 'render.mjs'}
                    and Path(command[2]).resolve().is_relative_to(allowed)
                    and Path(command[2]).suffix == '.json'):
                return
            # generate.py --render only needs the bundled, network-free SVG/resvg entrypoint.
            if not (isinstance(command, (list, tuple)) and len(command) == 3 and command[0] == 'node'
                    and Path(command[1]).resolve() == SCRIPTS / 'render.mjs'
                    and Path(command[2]).resolve() == Path(out).resolve() / 'render-jobs.json'):
                raise PermissionError('Only bundled offline rendering may run a subprocess')

    sys.addaudithook(audit)
    from strict_json import load
    if native:
        from workbench.native import generate
        generate(load(model_path), out, render=render, auto_layout=auto_layout)
        return
    from generate import generate
    generate(load(model_path), out, all_items=True, render=render, strict=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--data-dir', default=str(ROOT / 'output' / 'workbench-data'))
    parser.add_argument('--job-timeout', type=float, default=180)
    parser.add_argument('--max-job-mib', type=int, default=512)
    parser.add_argument('--max-job-store-mib', type=int, default=2048)
    parser.add_argument('--failed-output-retention-days', type=int, default=7)
    parser.add_argument('--prune-failed-now', action='store_true', help='Remove failed job partial outputs after stopping the server')
    parser.add_argument('--prune-completed-days', type=int, help='Preview completed job outputs older than this many days')
    parser.add_argument('--apply-prune', action='store_true', help='Apply --prune-completed-days after reviewing its preview')
    parser.add_argument('--generate-worker', help=argparse.SUPPRESS)
    parser.add_argument('--native-worker', help=argparse.SUPPRESS)
    parser.add_argument('--out', help=argparse.SUPPRESS)
    parser.add_argument('--render', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--auto-layout', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--worker-timeout', type=float, default=180, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.generate_worker or args.native_worker:
        if not args.out:
            parser.error('worker requires --out')
        # An independent process-group deadline also applies if the server dies.
        signal.signal(signal.SIGALRM, lambda *_: os.killpg(os.getpgrp(), signal.SIGKILL))
        signal.setitimer(signal.ITIMER_REAL, args.worker_timeout)
        generation_worker(args.native_worker or args.generate_worker, args.out, args.render,
                          native=bool(args.native_worker), auto_layout=args.auto_layout)
        return
    if args.job_timeout <= 0 or args.max_job_mib <= 0 or args.max_job_store_mib <= 0 or args.failed_output_retention_days < 0:
        parser.error('Timeout and storage limits must be positive; retention days cannot be negative')
    if args.apply_prune and args.prune_completed_days is None:
        parser.error('--apply-prune requires --prune-completed-days')
    if args.prune_completed_days is not None and args.prune_completed_days < 0:
        parser.error('--prune-completed-days cannot be negative')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    storage = dict(max_job_bytes=args.max_job_mib * 1024 ** 2,
                   max_job_store_bytes=args.max_job_store_mib * 1024 ** 2,
                   failed_output_retention_days=args.failed_output_retention_days)
    if args.prune_failed_now or args.prune_completed_days is not None:
        try:
            app = Workbench(args.data_dir, job_timeout=args.job_timeout, start_worker=False, **storage)
        except (ValueError, OSError) as exc:
            parser.error(str(exc))
        try:
            report = {}
            if args.prune_failed_now:
                report['failed_output_directories_removed'] = app.prune_failed_outputs(older_than_days=0)
            if args.prune_completed_days is not None:
                report['completed_outputs'] = app.prune_completed_outputs(args.prune_completed_days, apply=args.apply_prune)
            print(json.dumps(report))
        finally:
            app.close()
        return
    try:
        server = create_server(args.host, args.port, args.data_dir, job_timeout=args.job_timeout, **storage)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(f'Workbench: http://{args.host}:{server.server_port} (loopback only); data: {server.app.data_dir}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        server.app.close()


if __name__ == '__main__':
    main()
