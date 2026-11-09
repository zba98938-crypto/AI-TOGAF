"""Immutable execution evidence with separate source and run roots (v1 readable)."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import subprocess
import uuid
from runtime_provenance import fingerprints

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def current(root=ROOT):
    root = Path(root).resolve()
    return {**fingerprints(root), **{name: digest(root/name) for name in
            ('capabilities.json', 'artifacts.json', 'deliverables.json', 'metamodel.json')}}


def inside(root, path):
    root = Path(root).resolve()
    path = Path(path)
    if '..' in path.parts:
        raise ValueError('Parent traversal is not an evidence path')
    path = (root/path).resolve() if not path.is_absolute() else path.resolve()
    if not path.is_relative_to(root) or path == root:
        raise ValueError('Evidence path must stay inside its declared root')
    return path


def resolve_ref(reference, source_root, run_root):
    """Only source:/run: relative references; symlinks must remain in the root."""
    prefix, sep, relative = reference.partition(':')
    if not sep or prefix not in {'source', 'run'} or not relative or Path(relative).is_absolute():
        raise ValueError('Invalid evidence reference')
    return inside(source_root if prefix == 'source' else run_root, relative)


class Batch:
    def __init__(self, directory, inputs=(), root=ROOT, purpose='engineering execution'):
        self.root = Path(root).resolve()
        self.run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:12]
        directory = Path(directory)
        if not directory.is_absolute():
            directory = Path.cwd() / directory
        if '..' in directory.parts:
            raise ValueError('Parent traversal is not an output path')
        if directory.resolve().is_relative_to(self.root):
            raise ValueError('New execution batches must be outside the runtime package')
        self.directory = directory.resolve()/self.run_id
        self.directory.mkdir(parents=True, exist_ok=False)
        self.started_at = datetime.now(timezone.utc).isoformat()
        self.before = current(self.root)
        self._original_inputs = {}
        self.external_inputs = {}
        self.inputs = self.assets(inputs, snapshot_external=True)
        self.runs = []
        self.purpose = purpose

    def reference(self, path):
        if '..' in Path(path).parts:
            raise ValueError('Parent traversal is not an evidence path')
        path = Path(path).resolve()
        if path.is_relative_to(self.directory):
            return 'run:' + str(path.relative_to(self.directory))
        if path.is_relative_to(self.root):
            return 'source:' + str(path.relative_to(self.root))
        raise ValueError('Output must be inside the source or run root')

    def assets(self, paths, snapshot_external=False, outputs=False):
        assets = {}
        for value in paths:
            path = Path(value)
            if '..' in path.parts:
                raise ValueError('Parent traversal is not an evidence path')
            path = (self.root/path).resolve() if not path.is_absolute() else path.resolve()
            if outputs and not path.is_relative_to(self.directory):
                raise ValueError('New batch outputs must stay inside the run root')
            value_hash = digest(path)
            try:
                ref = self.reference(path)
            except ValueError:
                if not snapshot_external:
                    raise
                # Include the original identity in the name to distinguish identical files.
                key = hashlib.sha256(str(path).encode()).hexdigest()[:16]
                snapshot = self.directory/'input-snapshots'/key/path.name
                snapshot.parent.mkdir(parents=True, exist_ok=True)
                if not snapshot.exists():
                    shutil.copyfile(path, snapshot)
                    snapshot.chmod(0o444)
                ref = self.reference(snapshot)
                self.external_inputs[ref] = {'original_path': str(path), 'sha256': value_hash}
            if snapshot_external:
                self._original_inputs.setdefault(str(path), value_hash)
            assets[ref] = value_hash
        return assets

    def run(self, arguments, expected=0, timeout=1800):
        if not isinstance(arguments, list) or not arguments:
            raise ValueError('A nonempty argv list is required; no shell evaluation')
        ordinal = len(self.runs)+1
        local_inputs = set()
        for argument in arguments[1:]:
            candidate = Path(str(argument))
            candidate = (self.root/candidate).resolve() if not candidate.is_absolute() else candidate.resolve()
            if candidate.is_file():
                local_inputs.add(candidate)
        argv_inputs = self.assets(local_inputs, snapshot_external=True)
        try:
            result = subprocess.run([str(a) for a in arguments], cwd=self.root,
                                    capture_output=True, text=True, timeout=timeout)
        except (OSError, subprocess.TimeoutExpired) as exc:
            result = subprocess.CompletedProcess(arguments, 124 if isinstance(exc, subprocess.TimeoutExpired) else 127, '', str(exc))
        logs = {}
        for stream in ('stdout', 'stderr'):
            path = self.directory/f'{ordinal:04d}.{stream}.txt'
            path.write_text(getattr(result, stream), encoding='utf-8')
            logs[stream] = {'path': self.reference(path), 'sha256': digest(path)}
        row = {'ordinal': ordinal, 'argv': [str(a) for a in arguments],
               'inputs_sha256': argv_inputs, 'exit_code': result.returncode,
               'expected_exit_code': expected, 'matches_expected': result.returncode == expected, **logs}
        self.runs.append(row)
        return row, result

    def finish(self, outputs=(), observations=()):
        after = current(self.root)
        changed = sorted(k for k in self.before.keys() | after.keys() if self.before.get(k) != after.get(k))
        input_changes = [p for p, h in self._original_inputs.items() if not Path(p).is_file() or digest(p) != h]
        report = {'schema_version': 'execution-batch/2', 'run_id': self.run_id,
                  'source_root': str(self.root), 'run_root': str(self.directory),
                  'purpose': self.purpose, 'started_at': self.started_at,
                  'finished_at': datetime.now(timezone.utc).isoformat(),
                  'runtime_before': self.before, 'runtime_after': after,
                  'changed_runtime_paths': changed, 'changed_input_paths': sorted(input_changes),
                  'inputs': self.inputs, 'external_inputs': self.external_inputs,
                  'outputs': self.assets(outputs, outputs=True), 'runs': self.runs, 'observations': list(observations),
                  'passed': bool(self.runs) and not changed and not input_changes and all(r['matches_expected'] for r in self.runs),
                  'accepted': False,
                  'limit': 'Bounded execution only; snapshots preserve external inputs, not professional approval.'}
        path = self.directory/'execution.json'
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
        return path, report


def verify(report, root=ROOT, expected_current=None, run_root=None):
    errors = []
    root = Path(root).resolve()
    version = report.get('schema_version')
    if version not in {'execution-batch/1', 'execution-batch/2'} or not report.get('run_id'):
        errors.append('batch-identity-missing')
    if version == 'execution-batch/2':
        declared = report.get('source_root')
        if (not isinstance(declared, str) or not declared
                or not Path(declared).is_absolute() or '..' in Path(declared).parts
                or Path(declared).resolve() != root):
            # Fail before runtime discovery or any transitive asset access.
            return errors + ['source-root-identity-mismatch']
    now = expected_current if expected_current is not None else current(root)
    if not report.get('runtime_before') or report.get('runtime_before') != report.get('runtime_after'):
        errors.append('runtime-changed-during-run')
    if report.get('runtime_before') != now:
        errors.append('runtime-stale')
    if report.get('changed_runtime_paths') or report.get('changed_input_paths'):
        errors.append('inputs-changed-during-run')
    if not report.get('runs') or report.get('passed') is not True:
        errors.append('batch-not-passed')
    raw_destination = Path(run_root or report.get('run_root') or root)
    destination = raw_destination.resolve()
    if version == 'execution-batch/2' and ('..' in raw_destination.parts or destination.is_relative_to(root)):
        errors.append('unsafe-run-root')
    if version == 'execution-batch/2' and (not report.get('run_root') or destination.name != report.get('run_id')):
        errors.append('run-root-identity-mismatch')
    def asset(name):
        return resolve_ref(name, root, destination) if version == 'execution-batch/2' else inside(root, name)
    def check(name, expected, code):
        try:
            if digest(asset(name)) != expected:
                errors.append(code+'-stale:'+name)
        except (ValueError, OSError, TypeError, AttributeError):
            errors.append(code+'-unavailable:'+str(name))
    for collection in ('inputs', 'outputs'):
        if not report.get(collection):
            errors.append('missing-'+collection)
        for name, value in report.get(collection, {}).items():
            if version == 'execution-batch/2' and collection == 'outputs' and not str(name).startswith('run:'):
                errors.append('output-outside-run-root:' + str(name))
            check(name, value, 'asset')
    for row in report.get('runs', []):
        if row.get('exit_code') != row.get('expected_exit_code') or row.get('matches_expected') is not True:
            errors.append('unexpected-exit:'+str(row.get('ordinal')))
        for name, value in row.get('inputs_sha256', {}).items():
            check(name, value, 'command-input')
        for stream in ('stdout', 'stderr'):
            ref = row.get(stream, {})
            check(ref.get('path'), ref.get('sha256'), 'log')
    return sorted(set(errors))
