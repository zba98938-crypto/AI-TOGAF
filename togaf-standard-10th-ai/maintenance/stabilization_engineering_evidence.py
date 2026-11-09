"""Read-only acceptance of complete, byte-bound current engineering evidence.

This gate parses test sources; it never imports or runs tests, commands or model
sessions. Unsupported dynamic discovery is incomplete rather than a smaller
passing inventory. Passing this gate does not grant standards/business approval.
"""
import ast
import hashlib
import json
import math
import re
from pathlib import Path


CORE_STAGES = frozenset({
    'syntax', 'unit-regressions', 'skill-packages', 'method-case-constraints',
    'method-reasoning', 'methods', 'registry-consistency', 'production-profiles',
    'deliverables', 'integrity-adm', 'profile-expression', 'text-geometry',
    'mermaid-chinese', 'visual-samples', 'scale-sql', 'missing-historical-data',
    'empty-verify_method_case_constraints', 'empty-verify_method_reasoning',
    'source-integrity',
})
SOURCE_EXCLUSIONS = frozenset({'.venv', 'node_modules', '__pycache__', '.DS_Store'})
ENVELOPES = frozenset({'summary.json', 'progress.json'})


def _need(condition, message):
    if not condition:
        raise ValueError(message)


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _inside(base, name):
    _need(isinstance(name, (str, Path)) and str(name), 'invalid local evidence path')
    base = Path(base).resolve()
    raw = Path(name)
    _need('..' not in raw.parts, 'parent traversal in evidence path')
    path = (raw if raw.is_absolute() else base / raw).resolve()
    _need(path.is_relative_to(base) and path != base, 'evidence path escapes root')
    _need(path.is_file(), 'missing evidence: ' + str(path))
    return path


def _pairs(items):
    value = {}
    for key, item in items:
        _need(key not in value, 'duplicate JSON field: ' + key)
        value[key] = item
    return value


def _read(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def source_hashes(root):
    """Match core_cases.source_hashes without importing executable source."""
    root = Path(root).resolve()
    result = {}
    for name in ('togaf-standard-10th-ai/skills', 'tests'):
        folder = root / name
        _need(folder.is_dir(), 'missing core source directory')
        for path in folder.rglob('*'):
            if not SOURCE_EXCLUSIONS.intersection(path.parts) and path.is_file():
                checked = _inside(root, path)
                result[str(path.relative_to(root))] = _sha(checked)
    _need(bool(result), 'empty current source inventory')
    return result


def evidence_hashes(out):
    """Full retained-file inventory, excluding only the two root envelopes."""
    out = Path(out).resolve()
    result = {}
    for path in out.rglob('*'):
        _need(not path.is_symlink(), 'symlink in engineering evidence')
        if path.is_file() and str(path.relative_to(out)) not in ENVELOPES:
            result[str(path.relative_to(out))] = _sha(_inside(out, path))
    return result


def discover_test_inventory(root):
    """Statically identify the current ordinary unittest discovery inventory."""
    folder = Path(root).resolve() / 'tests'
    files = sorted(folder.glob('test_*.py'))
    _need(bool(files), 'no discoverable unit source')
    _need(not any(p.parent != folder for p in folder.rglob('test_*.py')),
          'nested test discovery requires an explicit supported inventory')
    identities = []
    hashes = {}
    for path in files:
        _inside(folder, path)
        hashes[path.name] = _sha(path)
        tree = ast.parse(path.read_text(), filename=str(path))
        modules, bases = set(), set()
        classes = {}
        for node in tree.body:
            if isinstance(node, ast.Import):
                for entry in node.names:
                    if entry.name == 'unittest':
                        modules.add(entry.asname or entry.name)
            elif isinstance(node, ast.ImportFrom) and node.module == 'unittest':
                for entry in node.names:
                    if entry.name == 'TestCase':
                        bases.add(entry.asname or entry.name)
                    _need(entry.name != '*', 'wildcard unittest discovery is uncertain')
            elif isinstance(node, ast.ClassDef):
                _need(node.name not in classes, 'duplicate test class definition')
                classes[node.name] = node
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                _need(node.name != 'load_tests', 'dynamic load_tests discovery unsupported')
            else:
                _need(not any(isinstance(child, ast.ClassDef) for child in ast.walk(node)),
                      'conditional/dynamic test class discovery unsupported')
                _need(not any(isinstance(child, ast.Call) and isinstance(child.func, ast.Name)
                              and child.func.id in {'setattr', 'exec', 'eval', 'type'}
                              for child in ast.walk(node)), 'dynamic module discovery unsupported')
        def base_name(node):
            if isinstance(node, ast.Name):
                return node.id
            if (isinstance(node, ast.Attribute) and node.attr == 'TestCase'
                    and isinstance(node.value, ast.Name) and node.value.id in modules):
                return '__unittest_TestCase__'
            raise ValueError('unresolved test inheritance')
        resolved = {}
        def methods(name, pending=()):
            if name in bases or name == '__unittest_TestCase__':
                return True, set()
            if name == 'object':
                return False, set()
            if name in resolved:
                return resolved[name]
            _need(name in classes and name not in pending, 'unresolved/cyclic test inheritance')
            node = classes[name]
            names, testcase = set(), False
            for base in node.bases:
                inherited_case, inherited_names = methods(base_name(base), pending + (name,))
                testcase = testcase or inherited_case
                names.update(inherited_names)
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name.startswith('test_'):
                    names.add(child.name)
                elif isinstance(child, (ast.Assign, ast.AnnAssign)):
                    targets = child.targets if isinstance(child, ast.Assign) else [child.target]
                    _need(not any(isinstance(t, ast.Name) and t.id.startswith('test_') for t in targets),
                          'dynamic test method assignment unsupported')
            resolved[name] = testcase, names
            return resolved[name]
        for name in sorted(classes):
            testcase, names = methods(name)
            if testcase:
                identities.extend(path.stem + '.' + name + '.' + method for method in sorted(names))
    _need(bool(identities) and len(identities) == len(set(identities)), 'empty/duplicate static test inventory')
    return identities, hashes


def _unit(out, root):
    report = _read(_inside(out, 'unit-regressions/summary.json'))
    ids, hashes = discover_test_inventory(root)
    count = len(ids)
    _need(report.get('schema_version') == 'formal-unit-regressions/1'
          and report.get('passed') is True and report.get('source_stable') is True,
          'formal unit execution did not pass/stabilize')
    for field in ('discovered', 'executed'):
        _need(type(report.get(field)) is int and report[field] == count, 'unit count differs from current discovery')
    _need(all(type(report.get(k)) is int and report[k] == 0 for k in ('failures', 'errors', 'skipped')),
          'unit failure/error/skip present')
    recorded = report.get('test_ids')
    _need(isinstance(recorded, list) and len(recorded) == count and set(recorded) == set(ids)
          and len(recorded) == len(set(recorded)), 'unit discovered IDs are incomplete/stale/duplicate')
    actual = report.get('actual_results')
    _need(isinstance(actual, list) and len(actual) == count and all(
        isinstance(row, dict) and row.get('status') == 'passed' and isinstance(row.get('id'), str)
        for row in actual), 'actual unit results incomplete/nonpassing')
    executed_ids = [row['id'] for row in actual]
    _need(len(set(executed_ids)) == count and set(executed_ids) == set(ids), 'actual execution IDs differ from discovery')
    _need(report.get('test_source_sha256') == hashes, 'unit test source inventory/hash differs from current')
    _need(all(report.get(k) == [] for k in ('failure_details', 'error_details', 'skipped_details')),
          'nonempty unit failure detail')
    text = _inside(out, 'unit-regressions/unit-regressions.log').read_text()
    starts = re.findall(r'^([A-Za-z_]\w*) \(([^)\n]+)\)', text, re.M)
    log_ids = [owner if owner.endswith('.' + method) else owner + '.' + method for method, owner in starts]
    _need(len(log_ids) == count and set(log_ids) == set(ids), 'retained verbose unit log does not contain actual inventory')
    _need(re.findall(r'^Ran (\d+) tests? in [\d.]+s$', text, re.M) == [str(count)]
          and re.findall(r'^OK$', text, re.M) == ['OK'], 'retained unit completion missing')
    outer = _json_lines(_inside(out, 'logs/unit-regressions.log'))
    compact = [row for row in outer if row.get('schema_version') == 'formal-unit-regressions/1']
    _need(len(compact) == 1 and compact[0] == {k: report[k] for k in (
        'schema_version', 'discovered', 'source_stable', 'executed', 'failures', 'errors', 'skipped', 'passed')},
        'core unit command result differs from actual unit report')


def _json_lines(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        try:
            row = json.loads(line, object_pairs_hook=_pairs)
        except ValueError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def _batch(path, root, out):
    path = _inside(out, path)
    data = _read(path)
    shared = Path(root).resolve() / 'togaf-standard-10th-ai/skills/_shared'
    _need(data.get('schema_version') == 'execution-batch/2' and data.get('passed') is True,
          'nested execution batch missing/nonpassing')
    _need(data.get('source_root') == str(shared) and data.get('run_root') == str(path.parent)
          and data.get('run_id') == path.parent.name, 'nested batch identity differs')
    _need(data.get('runtime_before') and data['runtime_before'] == data.get('runtime_after')
          and data.get('changed_runtime_paths') == [] and data.get('changed_input_paths') == [],
          'nested execution changed inputs/runtime')
    for name, value in data['runtime_before'].items():
        _need(_sha(_inside(shared, name)) == value, 'stale nested execution runtime')
    def asset(ref, value):
        _need(isinstance(ref, str), 'invalid nested asset reference')
        prefix, sep, name = ref.partition(':')
        _need(sep and prefix in {'source', 'run'} and not Path(name).is_absolute(), 'invalid nested asset scope')
        _need(_sha(_inside(shared if prefix == 'source' else path.parent, name)) == value,
              'nested asset/log fingerprint differs')
    for collection in ('inputs', 'outputs'):
        values = data.get(collection)
        _need(isinstance(values, dict) and values, 'nested asset inventory missing')
        for name, value in values.items():
            _need(collection != 'outputs' or name.startswith('run:'), 'nested output outside run')
            asset(name, value)
    runs = data.get('runs')
    _need(isinstance(runs, list) and runs, 'nested execution has no commands')
    for ordinal, row in enumerate(runs, 1):
        _need(row.get('ordinal') == ordinal and row.get('matches_expected') is True
              and type(row.get('exit_code')) is int and row['exit_code'] == row.get('expected_exit_code')
              and isinstance(row.get('argv'), list) and row['argv'], 'nested actual command result missing')
        for stream in ('stdout', 'stderr'):
            log = row.get(stream, {})
            asset(log.get('path'), log.get('sha256'))
        for name, value in row.get('inputs_sha256', {}).items():
            asset(name, value)
    return data


def _commands(out, root, rows):
    scripts = Path(root) / 'togaf-standard-10th-ai/skills/_shared/scripts'
    contracts = {
        'unit-regressions': (Path(root) / 'tests/run_unit_regressions.py', [str(Path(root)/'tests'), '--out', str(out/'unit-regressions')], 0),
        'skill-packages': (scripts/'verify_skill_packages.py', ['--out', str(out/'packages.json')], 0),
        'method-case-constraints': (scripts/'verify_method_case_constraints.py', ['--out', str(out/'method-cases.json')], 0),
        'method-reasoning': (scripts/'verify_method_reasoning.py', ['--out', str(out/'method-reasoning.json')], 0),
        'methods': (scripts/'verify_methods.py', ['--out', str(out/'methods'), '--fixtures',str(Path(root)/'tests/method_fixtures.py')], 0),
        'registry-consistency': (scripts/'registry_consistency.py', [], 0),
        'profile-expression': (scripts/'verify_artifact_profiles.py', ['--all', '--out', str(out/'profiles'), '--render', '--oversized-policy', 'tile'], 0),
        'text-geometry': (scripts/'verify_profile_geometry.py', [str(out/'profiles'), '--out', str(out/'geometry')], 0),
        'mermaid-chinese': (scripts/'render.mjs', [str(out/'mermaid/jobs.json')], 0),
        'missing-historical-data': (scripts/'verify_scale_cases.py', ['--dataset-dir', str(out/'missing-dataset'), '--out', str(out/'missing-scale')], 3),
    }
    for script in ('verify_method_case_constraints', 'verify_method_reasoning'):
        name = 'empty-' + script
        contracts[name] = (scripts/(script+'.py'), ['--cases-dir', str(out/'empty-cases'), '--out', str(out/(name+'.json'))], 3)
    for name, (script, arguments, expected) in contracts.items():
        detail = rows[name]['detail']
        argv = detail.get('argv')
        _need(isinstance(argv, list) and len(argv) >= 2 and argv[1:] == [str(script), *arguments],
              'core command contract differs: ' + name)
        interpreter = Path(argv[0]).name.lower() if isinstance(argv[0], str) else ''
        _need(interpreter == 'node' if script.suffix == '.mjs' else bool(re.fullmatch(r'python(?:\d+(?:\.\d+)?)?', interpreter)),
              'core command interpreter differs: ' + name)
        _need(type(detail.get('exit_code')) is int and detail['exit_code'] == expected
              and detail.get('expected_exit_code') == expected, 'core command exit differs: ' + name)
        log_name = 'mermaid' if name == 'mermaid-chinese' else name
        _inside(out, 'logs/' + log_name + '.log')
    registry = _json_lines(_inside(out, 'logs/registry-consistency.log'))
    _need(registry == [{'errors': [], 'review_evidence_required': False}], 'registry result unavailable/nonpassing')
    return contracts


def _stage_results(out, root, rows, orders):
    def read(name):
        return _read(_inside(out, name))
    def generated(directory):
        manifest = _read(_inside(out, directory/'manifest.json'))
        assets = manifest.get('output_sha256')
        _need(isinstance(assets, dict) and assets, 'generated output fingerprint map missing')
        for name, digest in assets.items():
            _need(_sha(_inside(out, directory/name)) == digest, 'generated deliverable fingerprint differs')
        return len(assets)
    shared = Path(root)/'togaf-standard-10th-ai/skills/_shared'
    capabilities = _read(_inside(shared, 'capabilities.json'))
    registered_profiles = {p['id'] for p in capabilities['profiles'] if not p.get('alias_of')}
    registered_deliveries = {d['id'] for d in _read(_inside(shared, 'deliverables.json'))['deliverables']}
    syntax = read('syntax.json').get('checked')
    expected_python = {p for p in source_hashes(root) if p.endswith('.py')}
    _need(isinstance(syntax, list) and len(syntax) == len(expected_python) and set(syntax) == expected_python
          and rows['syntax']['detail'].get('python_files') == len(syntax), 'syntax inventory incomplete')
    package = read('packages.json')
    _need(package.get('schema_version') == 'skill-package-verification/1' and package.get('audit_complete') is True
          and package.get('all_applicable_pass') is True and package.get('per_skill'), 'skill package result missing/nonpassing')
    cases = read('method-cases.json')
    _need(cases.get('schema_version') == 'method-case-constraints/1' and cases.get('status') == 'passed'
          and cases.get('methods') and cases.get('violations') == []
          and all(row.get('passed') is True for row in cases['methods']), 'method case result missing/nonpassing')
    reasoning = read('method-reasoning.json')
    _need(reasoning.get('status') == 'passed' and reasoning.get('engineering_status') == 'passed'
          and reasoning.get('engineering_assertions') and all(r.get('status') == 'passed' for r in reasoning['engineering_assertions']),
          'method reasoning result missing/nonpassing')
    for stage, report_name in [('methods', 'methods.json'), ('text-geometry', 'geometry-check.json')]:
        lines = _json_lines(_inside(out, 'logs/'+stage+'.log'))
        references = [r for r in lines if r.get('batch')]
        _need(len(references) == 1, 'actual nested stage result reference missing: ' + stage)
        batch_path = _inside(out, references[0]['batch'])
        _batch(batch_path, root, out)
        result = _read(_inside(out, batch_path.parent/report_name))
        if stage == 'methods':
            _need(result.get('schema_version') == 'method-verification/3' and result.get('failed') == 0
                  and result.get('missing_calculators') == [] and result.get('records')
                  and all(r.get('oracle_passed') is True for r in result['records']), 'method execution result missing/nonpassing')
        else:
            _need(result.get('status') == 'passed' and type(result.get('checked')) is int and result['checked'] > 0
                  and result.get('flagged') == 0, 'actual text geometry result missing/nonpassing')
    profiles = read('profiles/verification.json')
    _need(profiles.get('status') == 'passed' and profiles.get('png_export_requested') is True
          and profiles.get('render_status') == 'passed' and profiles.get('failed_profiles') == 0
          and profiles.get('results') and all(not r.get('failures') for r in profiles['results']), 'profile rendering result missing/nonpassing')
    _need(len(profiles['results']) == len(registered_profiles)
          and {r.get('profile_id') for r in profiles['results']} == registered_profiles,
          'registered profile expression inventory incomplete')
    for profile in profiles['results']:
        pid = profile['profile_id']
        _need(len(profile.get('layouts', [])) == 2 and {r.get('layout') for r in profile['layouts']} == {'reference', 'adaptive'}
              and all(r.get('valid') is True for r in profile['layouts']), 'profile dual-layout validation incomplete')
        _need(read('profiles/'+pid+'.case.json').get('result') == profile, 'authored profile case/result reference differs')
        for layout in ('reference', 'adaptive'):
            for variant in ('', '-modified'):
                identity = pid+'-'+layout+variant
                extension = '.svg' if profile.get('output_kind') == 'diagram' else '.md'
                _inside(out, 'profiles/'+identity+extension)
                _need(read('profiles/'+identity+'.coverage.json').get('errors') == [], 'actual profile expression failed')
    for name, key in [('production-profiles.json', 'profile_id'), ('deliverables.json', 'deliverable_id')]:
        entries = read(name)
        _need(isinstance(entries, list) and entries and len({r.get(key) for r in entries}) == len(entries), 'production/delivery inventory missing')
        if key == 'profile_id':
            _need({r[key] for r in entries} == registered_profiles, 'registered production profile inventory incomplete')
            _need(all(not row.get('errors') and row.get('status') != 'blocked' and
                      len(row.get('layouts', [])) == 2 and {r.get('layout') for r in row['layouts']} == {'reference','adaptive'}
                      and all(r.get('status') == 'pass' for r in row['layouts']) for row in entries), 'production dual layouts failed')
            for row in entries:
                for layout in row['layouts']:
                    _need(generated(Path('production')/row[key]/layout['layout']) == layout.get('files'),
                          'production output count differs from retained generated files')
        else:
            _need({r[key] for r in entries} == registered_deliveries, 'registered strict delivery inventory incomplete')
            _need(all(row.get('status') == 'pass' for row in entries), 'strict delivery failed')
            for row in entries:
                folder = Path('deliverables')/row[key]
                assembly = read(folder/'assembly.json')
                _need(assembly.get('status') == 'assembled-awaiting-review' and not assembly.get('unbound_section_titles')
                      and len(assembly.get('section_blocks', [])) == row.get('sections'), 'actual strict delivery assembly differs')
                generated(folder/'generated')
    integrity = read('integrity-adm.json')
    _need(integrity.get('tampered') and 'output-model-stale' in integrity.get('stale_model', [])
          and len(integrity.get('cycle', {}).get('phases', [])) == 9
          and len(integrity.get('check', {}).get('phases', [])) == 9
          and integrity['check'].get('errors') == [] and integrity['check'].get('recorded_cycle_complete') is False,
          'integrity/ADM actual result missing')
    visual = read('visual-samples/index.json')
    _need(isinstance(visual, dict) and visual and rows['visual-samples']['detail'].get('renderer_families') == len(visual), 'visual samples inventory missing')
    for name in visual:
        _need(_inside(out, 'visual-samples/'+name+'.png').read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), 'visual PNG missing')
    for suffix, magic in [('svg', b'<'), ('png', b'\x89PNG\r\n\x1a\n')]:
        _need(_inside(out, 'mermaid/diagram.'+suffix).read_bytes().lstrip().startswith(magic), 'Mermaid export missing')
    for name in ('oracle-report', 'negative-cases', 'determinism'):
        result = read('scale/'+name+'.json')
        _need(result.get('passed') is True, 'actual scale result nonpassing')
        if name == 'oracle-report':
            _need(result.get('counts', {}).get('orders') == orders and result.get('checks'), 'requested scale not executed')
        if name == 'determinism':
            hashes = result.get('hashes')
            _need(isinstance(hashes, list) and len(hashes) == 2 and hashes[0] == hashes[1], 'scale repeat result missing')
    _need(read('missing-scale/report.json').get('status') == 'blocked', 'missing-source negative not rejected')
    for name in ('empty-verify_method_case_constraints', 'empty-verify_method_reasoning'):
        _need(read(name+'.json').get('status') == 'blocked', 'empty-input negative not rejected')
    _need(rows['source-integrity']['detail'].get('unchanged') is True, 'source-integrity stage did not verify')


def engineering_errors(path, data, root):
    """Return one explicit failed gate reason; perform only local reads."""
    try:
        root = Path(root).resolve()
        path = _inside(root, path)
        out = path.parent
        _need(path.name == 'summary.json' and _read(path) == data, 'core report argument differs from retained bytes')
        _need(isinstance(data, dict) and data.get('schema_version') == 'skills-core-regression/1'
              and data.get('status') == 'pass' and data.get('render_requested') is True,
              'current complete core --render did not pass')
        _need(type(data.get('orders')) is int and data['orders'] > 0, 'scale request invalid')
        _need(all(data.get(k) == [] for k in ('failures', 'blocked', 'source_changed')), 'core has failed/blocked/changed work')
        results = data.get('results')
        _need(isinstance(results, list) and len(results) == len(CORE_STAGES), 'core fixed stage count incomplete')
        _need(all(isinstance(r, dict) and r.get('status') == 'pass' and isinstance(r.get('detail'), dict)
                  and type(r.get('seconds')) in (int, float) and math.isfinite(r['seconds']) and r['seconds'] >= 0
                  for r in results), 'core stage did not actually pass')
        rows = {row.get('name'): row for row in results}
        _need(set(rows) == CORE_STAGES and len(rows) == len(results), 'core fixed stage inventory differs')
        current = source_hashes(root)
        _need(_read(_inside(out, 'source-before.json')) == current
              and _read(_inside(out, 'source-after.json')) == current, 'core source maps differ from current code')
        _need(data.get('evidence_sha256') == evidence_hashes(out), 'retained full evidence inventory/hash differs')
        _commands(out, root, rows)
        _unit(out, root)
        _stage_results(out, root, rows, data['orders'])
        return []
    except (OSError, ValueError, TypeError, KeyError, AttributeError, SyntaxError) as exc:
        return [str(exc)]


def engineering_pass(path, data, root):
    return not engineering_errors(path, data, root)
