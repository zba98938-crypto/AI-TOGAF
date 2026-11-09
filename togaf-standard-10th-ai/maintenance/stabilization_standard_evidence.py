#!/usr/bin/env python3
"""Read-only source-derived UML/BPMN coverage and executed-oracle gate.

Published coverage labels are compared with fresh source extraction and current
bindings. Passing bounded fixtures never certifies the full design-time scope.
"""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


VERSIONS = {'uml': '2.5.1', 'bpmn': '2.0.2'}


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _safe(root, name):
    if (not isinstance(name, str) or not name or Path(name).is_absolute()
            or any(part in ('', '.', '..') for part in name.split('/'))
            or any(char in name for char in ('\\', '\x00', ':', '%'))):
        raise ValueError('noncanonical standard evidence path')
    root = Path(root).resolve()
    path = root
    for part in Path(name).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('standard evidence symlink is forbidden: ' + name)
    if not path.resolve().is_relative_to(root) or not path.is_file():
        raise ValueError('standard evidence file missing or outside root: ' + name)
    return path


def _verified_ref(root, ref):
    if (not isinstance(ref, dict) or set(ref) != {'path', 'sha256'}
            or not re.fullmatch(r'[0-9a-f]{64}', str(ref.get('sha256', '')))):
        raise ValueError('explicit standard evidence reference is required')
    path = _safe(root, ref['path'])
    if _sha(path) != ref['sha256']:
        raise ValueError('standard evidence fingerprint conflict: ' + ref['path'])
    return path


def _source_snapshot(root):
    """Use exactly the native evidence collector's source/dependency scope."""
    shared = root / 'togaf-standard-10th-ai/skills/_shared'
    paths = set((root / 'tests').glob('*.py'))
    for suffix in ('*.py', '*.java', '*.mjs'):
        paths.update((shared / 'scripts').glob(suffix))
    paths.update((shared / 'standards').glob('*.json'))
    paths.add(shared / 'standards/java/manifest.json')
    paths.add(shared / 'standards/sources/manifest.json')
    return {path.relative_to(root).as_posix(): _sha(_safe(root, path.relative_to(root).as_posix()))
            for path in sorted(paths) if path.is_file()}


def _normative_snapshot(root):
    base = root / 'togaf-standard-10th-ai/skills/_shared/standards/sources'
    manifest = json.loads(_safe(base, 'manifest.json').read_text())
    if not isinstance(manifest, list) or not manifest:
        raise ValueError('empty normative source manifest')
    result = {}
    for row in manifest:
        name = row.get('file')
        if name in result:
            raise ValueError('duplicate normative source declaration: ' + str(name))
        actual = _sha(_safe(base, name))
        if actual != row.get('sha256'):
            raise ValueError('current normative source fingerprint conflict: ' + str(name))
        result[name] = actual
    return result


def _symbols(path):
    result = set()
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            result.add(node.name)
        if isinstance(node, ast.ClassDef):
            result.update(node.name + '.' + method.name for method in node.body
                          if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)))
    return result


def _execution(round_data, root):
    path = _verified_ref(root, round_data.get('standard_test_evidence'))
    log = _verified_ref(root, round_data.get('standard_test_log'))
    if log.parent != path.parent or log.name != 'execution.log':
        raise ValueError('standard execution log must be the retained evidence sibling')
    data = json.loads(path.read_text())
    if data.get('schema_version') != 'native-standard-test-evidence/1':
        raise ValueError('unsupported standard test evidence format')
    count = data.get('executed')
    if (not isinstance(count, int) or isinstance(count, bool) or count < 1
            or data.get('discovered') != count or data.get('passed') is not True
            or any(type(data.get(key)) is not int or data[key] != 0
                   for key in ('failures', 'errors', 'skipped'))
            or data.get('source_changed_during_execution') != []):
        raise ValueError('standard tests require actual execution and zero failures/errors/skips/source changes')
    sources = _source_snapshot(root)
    if not sources or data.get('source_hashes') != sources:
        raise ValueError('standard execution source snapshot differs from current files')
    if data.get('normative_source_hashes') != _normative_snapshot(root):
        raise ValueError('standard execution normative source snapshot differs')
    modules = data.get('modules')
    if (not isinstance(modules, list) or not modules or len(modules) != len(set(modules))
            or any(not isinstance(name, str) or not re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*', name) for name in modules)):
        raise ValueError('explicit standard test module selection is required')
    rows = data.get('tests')
    if not isinstance(rows, list) or len(rows) != count:
        raise ValueError('standard executed test count differs from retained rows')
    ids = set()
    locations = set()
    for row in rows:
        if not isinstance(row, dict) or row.get('status') != 'passed':
            raise ValueError('standard test result is failed, skipped or unexecuted')
        name, symbol, identity = row.get('file'), row.get('symbol'), row.get('id')
        file = _safe(root, name)
        if not file.is_relative_to(root / 'tests') or file.suffix != '.py':
            raise ValueError('standard oracle must be a current Python test file')
        if symbol not in _symbols(file):
            raise ValueError('standard oracle symbol missing: ' + str(symbol))
        test_module = file.relative_to(root / 'tests').with_suffix('').as_posix().replace('/', '.')
        if (identity != test_module + '.' + symbol
                or not any(identity == name or identity.startswith(name + '.') for name in modules)):
            raise ValueError('standard oracle identity differs from file/symbol/module selection')
        if identity in ids or (name, symbol) in locations:
            raise ValueError('duplicate standard executed test identity')
        ids.add(identity)
        locations.add((name, symbol))
    text = log.read_text()
    outcomes = []
    pattern = re.compile(r'^(\S+)\s+\(([^()]+)\)\s+\.\.\.\s+(.*)$')
    for line in text.splitlines():
        match = pattern.fullmatch(line.strip())
        if match:
            method, label, status = match.groups()
            # Python 3.9 prints module.Class; newer versions can print the full
            # test ID. Both descriptions must bind to the exact method row.
            identity = label if label.endswith('.' + method) else label + '.' + method
            outcomes.append((identity, status))
    if (len(outcomes) != count or len({identity for identity, _ in outcomes}) != count
            or {identity for identity, _ in outcomes} != ids
            or any(status != 'ok' for _, status in outcomes)):
        raise ValueError('standard execution log does not establish every retained test passed')
    runs = re.findall(r'^Ran (\d+) tests? in [^\n]+$', text, re.M)
    summaries = re.findall(r'^(OK(?:\s*\([^\n]*\))?|FAILED(?:\s*\([^\n]*\))?)$', text, re.M)
    if runs != [str(count)] or summaries != ['OK']:
        raise ValueError('standard execution log summary is failed, skipped, ambiguous or missing')
    return data, {'status': 'valid', 'executed': count, 'failures': 0, 'errors': 0, 'skipped': 0,
                  'evidence': round_data['standard_test_evidence'], 'log': round_data['standard_test_log']}


def _current_ledger(root, language, evidence):
    scripts = root / 'togaf-standard-10th-ai/skills/_shared/scripts'
    path = _safe(root, (scripts / 'standards_coverage.py').relative_to(root).as_posix())
    spec = importlib.util.spec_from_file_location('_current_standard_coverage_gate', path)
    coverage = importlib.util.module_from_spec(spec)
    previous = list(sys.path)
    sys.path.insert(0, str(scripts))
    try:
        spec.loader.exec_module(coverage)
        return coverage.ledger(language, VERSIONS[language], evidence=evidence)
    except RuntimeError as exc:
        # standards.Incomplete is a RuntimeError, not an implementation pass.
        raise ValueError(str(exc)) from exc
    finally:
        sys.path[:] = previous


def standard_checks(round_data, root):
    """Return (complete, assessment) without writing or trusting claimed coverage."""
    root = Path(root).resolve()
    assessment = {}
    try:
        capabilities = round_data.get('standard_capabilities')
        if not isinstance(capabilities, dict) or set(capabilities) != set(VERSIONS):
            raise ValueError('both explicit UML and BPMN coverage references are required')
        evidence, execution = _execution(round_data, root)
        assessment['test_evidence'] = execution
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as exc:
        reason = str(exc)
        return False, {'test_evidence': {'status': 'invalid', 'reason': reason},
                       **{language: {'complete': False, 'status': 'invalid', 'reason': reason}
                          for language in VERSIONS}}
    for language in VERSIONS:
        try:
            published = json.loads(_verified_ref(root, capabilities[language]).read_text())
            current = _current_ledger(root, language, evidence)
            if published != current:
                raise ValueError('published standard ledger differs from current source-derived obligations, declarations or bindings')
            completeness = current['completeness']
            # Recompute the final obligation condition independently of labels.
            applicable = [item for item in current['items']
                          if item.get('applicability') != 'not-applicable-reviewed']
            closed = [item for item in applicable
                      if item.get('implementation_status') == 'implemented'
                      and item.get('verification_status') == 'passed'
                      and item.get('implementation') and item.get('positive_tests') and item.get('negative_tests')]
            complete = (completeness.get('source_scope_complete') is True
                        and completeness.get('applicability_adjudication_complete') is True
                        and bool(applicable) and len(closed) == len(applicable)
                        and completeness.get('status') == 'complete')
            assessment[language] = {'status': 'complete' if complete else 'incomplete',
                'complete': complete, 'ledger_verified': True, 'item_count': len(current['items']),
                'applicable_obligations': len(applicable), 'verified_obligations': len(closed),
                'completeness': completeness, 'blockers': current['blockers'],
                'evidence': capabilities[language]}
        except (OSError, ValueError, KeyError, TypeError, SyntaxError) as exc:
            assessment[language] = {'complete': False, 'status': 'invalid', 'reason': str(exc)}
    return all(assessment[language]['complete'] for language in VERSIONS), assessment
