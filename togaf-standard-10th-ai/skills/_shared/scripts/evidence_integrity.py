"""Read-only, typed transitive evidence validation; never grants semantic approval.

Only declared evidence schemas are traversed. An arbitrary business JSON file is
an asset, not an instruction to read other paths. All references remain inside root.
"""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

DIGEST = re.compile(r'^[0-9a-f]{64}$')
METHOD_RECORDS = {'method-execution/1', 'method-cross-review/1',
                  'method-structure-observation/2', 'method-execution/2'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe_path(root, name):
    if (not isinstance(name, str) or not name or '\\' in name
            or any(c in name for c in '#?:') or name.startswith('~')
            or PurePosixPath(name).is_absolute() or '..' in PurePosixPath(name).parts):
        raise ValueError('unsafe-evidence-path')
    root = Path(root).resolve(strict=True)
    path = (root / name).resolve(strict=True)
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError('evidence-outside-root-or-not-file')
    return path


def verify_reference(reference, root, expected=None, _active=None):
    """Return concrete errors, including stale bindings inside a hashed record.

    expected is caller-derived identity/context, not copied from the evidence.
    A valid digest proves integrity only, never performance or reviewer honesty.
    """
    expected = expected or {}
    active = set(_active or ())
    if not isinstance(reference, dict):
        return ['evidence-reference-not-object']
    name = reference.get('path')
    if isinstance(name, str) and name in active:
        return ['evidence-reference-cycle:' + name]
    try:
        path = safe_path(root, name)
    except (OSError, ValueError, TypeError, RuntimeError) as exc:
        return ['evidence-unavailable:' + str(name) + ':' + str(exc)]
    digest = reference.get('sha256')
    if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
        return ['evidence-hash-required:' + name]
    if sha(path) != digest:
        return ['evidence-hash-stale:' + name]
    active.add(name)
    try:
        document = json.loads(path.read_text())
    except (ValueError, UnicodeError):
        return []
    if not isinstance(document, dict):
        return []
    schema = document.get('schema_version')
    errors = []
    refs = []
    if schema in METHOD_RECORDS:
        for key in ('method_id', 'scope_id', 'state_id', 'view_id'):
            if key in expected and document.get(key) != expected[key]:
                errors.append('evidence-identity-mismatch:' + key + ':' + name)
        refs.append({'path': document.get('case_path'),
                     'sha256': document.get('case_sha256')})
        refs.extend(document.get('execution_refs', []))
        if schema == 'method-execution/2':
            refs.extend(v['input'] for v in document.get('variants', []) if isinstance(v, dict) and 'input' in v)
            from execution_batch import current
            runtime = expected.get('runtime_fingerprints')
            if runtime is None:
                runtime = current(expected.get('source_root', root))
            if not document.get('runtime_fingerprints') or document['runtime_fingerprints'] != runtime:
                errors.append('method-runtime-stale:' + name)
    elif schema == 'execution-batch/2':
        from execution_batch import ROOT as installed_source_root, verify
        # The report's source_root describes its origin; it cannot authorize a
        # different filesystem root or choose the current runtime used to verify it.
        trusted_root = expected.get('source_root', installed_source_root)
        try:
            return verify(document, root=trusted_root,
                          expected_current=expected.get('runtime_fingerprints'),
                          run_root=path.parent)
        except (OSError, ValueError, TypeError, RuntimeError) as exc:
            return ['batch-verification-unavailable:' + name + ':' + str(exc)]
    elif schema == 'execution-batch/1':
        for collection in ('inputs', 'outputs'):
            items = document.get(collection, {})
            if isinstance(items, dict):
                refs.extend({'path': k, 'sha256': v} for k, v in items.items())
        for run in document.get('runs', []):
            if isinstance(run, dict):
                refs.extend(run[k] for k in ('stdout', 'stderr') if k in run)
                refs.extend({'path': k, 'sha256': v} for k, v in run.get('inputs_sha256', {}).items())
    elif schema in ('acceptance-review-records-v1', 'acceptance-review-records-v2'):
        selected = document.get('records', [])
        if reference.get('record_id'):
            selected = [r for r in selected if r.get('id') == reference['record_id']]
            if len(selected) != 1:
                errors.append('unique-review-record-required:' + name)
        for record in selected:
            if isinstance(record, dict):
                refs.extend(record.get('assets', []))
    elif schema == 'evidence-node/1':
        refs.extend(document.get('references', []))
    for ref in refs:
        # Runtime/root expectations remain trusted through the evidence graph.
        # Method/scope/view identity belongs only to its directly bound record.
        inherited = {key: expected[key] for key in ('source_root', 'runtime_fingerprints') if key in expected}
        errors.extend(verify_reference(ref, root, inherited, active))
    return sorted(set(errors))
