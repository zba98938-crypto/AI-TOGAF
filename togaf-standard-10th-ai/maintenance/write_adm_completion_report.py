"""Publish current bounded engineering evidence without granting full acceptance."""
import argparse
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

from verify_implementation_ledger import declared_inputs
from report_outcome import report_outcome
from independent_audit_selection import select_independent_audit

C = Path(__file__).resolve().parents[1]
REPO = C.parent
SHARED = C / 'skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from runtime_provenance import fingerprints
from execution_batch import current as execution_fingerprints


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def generated_runtime_issues(data, current):
    """A matching output hash alone does not make a generated bundle current."""
    issues = []
    for field in ('implementation_dependencies_sha256', 'runtime_after_sha256'):
        mapping = data.get(field)
        if not isinstance(mapping, dict) or not mapping:
            issues.append({'field': field, 'reason': 'missing-runtime-map'})
            continue
        if mapping != current:
            issues.append({'field': field, 'reason': 'runtime-file-set-or-content-mismatch',
                           'paths': sorted(name for name in set(mapping) | set(current)
                                           if mapping.get(name) != current.get(name))})
    if data.get('runtime_stable') is not True:
        issues.append({'field': 'runtime_stable', 'reason': 'runtime-not-stable'})
    return issues


def historical_runtime_snapshots(mapping, run, repo=REPO):
    """Bind changed declared historical inputs to their exact saved bytes."""
    replacements = {}
    for name, expected in mapping.items():
        current = (repo / name).resolve()
        if current.is_file() and sha(current) == expected:
            continue
        candidates = [run / folder / current.name for folder in
                      ('before-arrow-label-fix', 'before-label-clearance-fix',
                       'before-dtra-type-label-fix', 'before-annotation-leader-fix')]
        snapshot = next((path for path in candidates if path.is_file() and sha(path) == expected), None)
        if snapshot is None:
            raise ValueError('Missing exact historical source: ' + name)
        replacements[name] = str(snapshot.resolve())
    return replacements


def reviewed_proposal_manifest(run, directory):
    names = ('integrity-manifest.json', 'proposal-seal.json') if directory == 'annotation-leader-proposal' else ('integrity-manifest.json',)
    found = [run / directory / name for name in names if (run / directory / name).is_file()]
    if len(found) != 1:
        raise ValueError('Exactly one reviewed proposal seal is required: ' + directory)
    return found[0]


def sealed_evidence_files(path, repo=REPO):
    """Resolve one complete relative-path seal without treating it as acceptance."""
    path = path.resolve()
    repo = repo.resolve()
    rows = json.loads(path.read_text())['files']
    if isinstance(rows, list):
        if path.name != 'proposal-seal.json':
            raise ValueError('Unexpected list seal format')
        normalized = {}
        for row in rows:
            name = row['path']
            relative = Path(name)
            if (relative.is_absolute() or '..' in relative.parts or relative.as_posix() != name
                    or name in normalized or (path.parent / relative).is_symlink()
                    or (path.parent / relative).stat().st_size != row['bytes']):
                raise ValueError('Invalid or duplicate proposal seal input: ' + name)
            normalized[name] = row['sha256']
        rows = normalized
    if not isinstance(rows, dict) or not rows:
        raise ValueError('Missing sealed file map: ' + str(path))
    actual = {p.relative_to(path.parent).as_posix() for p in path.parent.rglob('*')
              if p.is_file() and p != path}
    if set(rows) != actual:
        raise ValueError('Sealed evidence file set differs: ' + str(path))
    mapping = {}
    for name, expected in rows.items():
        relative = Path(name)
        if (relative.is_absolute() or '..' in relative.parts or relative.as_posix() != name
                or not isinstance(expected, str) or len(expected) != 64):
            raise ValueError('Invalid sealed relative path or SHA: ' + name)
        target = path.parent / relative
        if target.is_symlink() or sha(target) != expected:
            raise ValueError('Sealed evidence bytes differ: ' + name)
        key = target.relative_to(repo).as_posix() if target.is_relative_to(repo) else str(target)
        mapping[key] = expected
    key = path.relative_to(repo).as_posix() if path.is_relative_to(repo) else str(path)
    mapping[key] = sha(path)
    return mapping


def annotation_application_bindings(data, run, current_source, repo=REPO):
    """Check every applied byte against the stopped proposal and current map."""
    repo, run = repo.resolve(), run.resolve()
    if (data.get('applied') is not True or data.get('passed_for_exact_applied_bytes') is not True
            or data.get('source_topology_unchanged') is not True
            or data.get('source_after') != current_source):
        raise ValueError('Application is not complete at the current source map')
    mapping = {}
    for kind, directory in (('annotation', 'annotation-leader-proposal'), ('dtra', 'dtra-type-label-proposal')):
        manifest = reviewed_proposal_manifest(run, directory)
        if data['proposal_manifest_sha256'].get(kind) != sha(manifest):
            raise ValueError('Application proposal manifest differs: ' + kind)
        mapping.update(sealed_evidence_files(manifest, repo))
    driver = run / 'annotation-leader-fix/apply_reviewed_sources.py'
    if data['application_driver_sha256'] != sha(driver):
        raise ValueError('Application driver differs')
    mapping[driver.relative_to(repo).as_posix()] = sha(driver)
    copies = data.get('copies', [])
    destinations = set()
    for row in copies:
        source, destination = repo / row['source'], repo / row['destination']
        if (not source.resolve().is_relative_to(run.resolve()) or not destination.resolve().is_relative_to(repo.resolve())
                or row['destination'] in destinations or row['source_sha256'] != sha(source)
                or row['source_sha256'] != sha(destination)
                or mapping.get(row['source']) != row['source_sha256']
                or current_source.get(row['destination']) != row['source_sha256']):
            raise ValueError('Applied source differs or escapes its declared scope: ' + row['destination'])
        destinations.add(row['destination'])
        mapping[row['source']] = mapping[row['destination']] = row['source_sha256']
    changed = sorted(name for name in data['source_before'].keys() | data['source_after'].keys()
                     if data['source_before'].get(name) != data['source_after'].get(name))
    if not copies or changed != data.get('changed_or_added_source_paths') or set(changed) != destinations:
        raise ValueError('Application changed-path scope differs from its exact copy list')
    portable = run / 'annotation-leader-proposal/tests/independent-oracle-application-inputs-v1.json'
    if sha(portable) != data['portable_oracle_manifest_sha256']:
        raise ValueError('Application portable oracle manifest differs')
    portable_data = json.loads(portable.read_text())
    items = [*portable_data['oracles'], portable_data['auxiliary_self_test'],
             portable_data['font'], *portable_data['fixtures']]
    required = {'togaf-standard-10th-ai/skills/_shared/scripts/' + name
                for name in ('profile_render.py', 'annotation_clearance.py', 'source_shape_render.py')}
    required.add('tests/test_dtra_type_label_clearance.py')
    required.update('tests/' + item['source_relative_to_tests'] for item in items)
    if not required <= destinations or not any(Path(name).name.startswith('test_annotation_') for name in destinations):
        raise ValueError('Application omits a required renderer, portable oracle input or behavior test')
    request = run / 'annotation-leader-fix/source-application-request.json'
    prior = json.loads(request.read_text())
    for field in ('copies', 'source_before', 'proposal_manifest_sha256', 'application_driver_sha256', 'portable_oracle_manifest_sha256'):
        if prior.get(field) != data.get(field):
            raise ValueError('Application differs from its retained request: ' + field)
    mapping[request.relative_to(repo).as_posix()] = sha(request)
    return mapping


def annotation_export_bindings(data, run, current_source, repo=REPO):
    """Require the real complete export, exact current source and output file set."""
    repo, run = repo.resolve(), run.resolve()
    counts = data.get('counts', {})
    if (data.get('passed') is not True or data.get('source_stable') is not True
            or data.get('returncode') != 0 or data.get('timed_out') is not False
            or data.get('complete_summary_files_exist') is not True
            or counts != {'profiles': 297, 'families': 196, 'kinds': {'diagram': 178, 'table': 119},
                          'svg_files': 712, 'png_files': 760, 'raster_jobs': 712, 'failed_profiles': 0}):
        raise ValueError('Annotation export is not a complete successful actual run')
    runner = run / 'annotation-leader-fix/run_full_export.py'
    declared = dict(data.get('input_sha256', {}))
    if declared.pop(runner.relative_to(repo).as_posix(), None) != sha(runner) or declared != current_source:
        raise ValueError('Annotation export source keys or bytes differ from current source')
    directory = run / 'profiles-after-annotation-leader'
    outputs = data.get('output_sha256', {})
    profile = json.loads((directory / 'verification.json').read_text())
    raster = json.loads((directory / 'render-report.json').read_text())
    if (len(list(directory.glob('*.svg'))) != 712 or len(list(directory.rglob('*.png'))) != 760
            or len(raster.get('results', [])) != 712 or raster.get('status') != 'passed'
            or profile.get('status') != 'passed' or profile.get('failed_profiles') != 0
            or profile.get('independent_profiles_checked') != 297 or profile.get('artifact_families_checked') != 196):
        raise ValueError('Actual annotation output inventory or completed summaries differ')
    actual = {p.relative_to(repo).as_posix() for p in directory.rglob('*') if p.is_file()}
    if not outputs or set(outputs) != actual or any(sha(repo / name) != digest for name, digest in outputs.items()):
        raise ValueError('Annotation export output bytes or complete file set differ')
    return {**data['input_sha256'], **outputs}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--campaign', type=Path, required=True)
    parser.add_argument('--units', type=Path, required=True)
    parser.add_argument('--production', type=Path, required=True)
    parser.add_argument('--current-run', type=Path,
                        help='Actual continuation outputs; --campaign retains unchanged historical inputs.')
    parser.add_argument('--outputs', type=Path,
                        help='JSON map of continuation output names to subsequent actual execution paths.')
    args = parser.parse_args()
    run = args.campaign.resolve()
    current_run = args.current_run.resolve() if args.current_run else run
    continuation = args.current_run is not None
    current_runtime = fingerprints(SHARED)
    output_paths = json.loads(args.outputs.read_text()) if args.outputs else {}
    checks, dependencies, file_sets = [], {}, []

    def path_key(path):
        path = path.resolve()
        return path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else str(path)

    def current_path(new, old):
        if not continuation:
            return run / old
        path = (current_run / output_paths.get(new, new)).resolve()
        if not path.is_relative_to(current_run):
            raise ValueError('unsafe continuation output path: ' + str(path))
        return path

    if args.outputs:
        dependencies[path_key(args.outputs)] = sha(args.outputs)
    dependencies[path_key(Path(__file__))] = sha(Path(__file__))

    def record(ident, path, predicate):
        path = path.resolve()
        value = json.loads(path.read_text())
        inputs = declared_inputs(C, path)
        stale = [row['path'] for row in inputs if not row['passed']]
        passed = bool(predicate(value)) and not stale
        checks.append({'id': ident, 'passed': passed, 'evidence': path.relative_to(REPO).as_posix(),
                       'declared_inputs_checked': len(inputs), 'stale_inputs': stale})
        dependencies[path.relative_to(REPO).as_posix()] = sha(path)
        for spec in value.get('input_file_sets', []):
            if spec not in file_sets:
                file_sets.append(spec)
        for row in inputs:
            if row['field'] == 'input_file_sets':
                continue
            name = row['path']
            target = next((p for p in [path.parent / name, C / name, REPO / name] if p.is_file()), None)
            if target is not None:
                dependencies[target.resolve().relative_to(REPO).as_posix()] = row['expected_sha256']
        return value

    def bind_files(ident, mapping, base=REPO, replacements=None):
        bad = []
        for name, expected in mapping.items():
            path = (base / name).resolve()
            if replacements and path_key(path) in replacements:
                path = Path(replacements[path_key(path)]).resolve()
            if not path.is_file() or sha(path) != expected:
                bad.append(name)
            dependencies[path_key(path)] = expected
        checks.append({'id': ident, 'passed': bool(mapping) and not bad,
                       'files_checked': len(mapping), 'mismatches': bad})

    def bind_generated_bundle(ident, directory, expected_manifests, historical_runtime=None, replacements=None):
        mapping = {}
        runtime_issues = []
        manifests = sorted(directory.glob('**/manifest.json'))
        for manifest in manifests:
            mapping[manifest.relative_to(REPO).as_posix()] = sha(manifest)
            data = json.loads(manifest.read_text())
            expected_runtime = historical_runtime if historical_runtime is not None else current_runtime
            runtime_issues.extend({'manifest': path_key(manifest), **row}
                                  for row in generated_runtime_issues(data, expected_runtime))
            for field in ('implementation_dependencies_sha256', 'runtime_after_sha256'):
                for name, expected in data.get(field, {}).items():
                    mapping[path_key(SHARED / name)] = expected
            for field, name in {'generator_sha256': 'scripts/generate.py',
                                'renderer_sha256': 'scripts/profile_render.py',
                                'table_renderer_sha256': 'scripts/table_expression.py',
                                'metamodel_sha256': 'metamodel.json', 'artifacts_sha256': 'artifacts.json',
                                'deliverables_sha256': 'deliverables.json',
                                'assembly_renderer_sha256': 'scripts/deliverable_assembly.py',
                                'assembly_rules_sha256': 'capability-addenda/deliverable-assembly-rules.json',
                                'capabilities_sha256': 'capabilities.json'}.items():
                if data.get(field):
                    mapping[path_key(SHARED / name)] = data[field]
            for name, expected in data['output_sha256'].items():
                target = (manifest.parent / name).resolve()
                if not target.is_relative_to(manifest.parent.resolve()):
                    raise ValueError('unsafe generated output path: ' + name)
                mapping[target.relative_to(REPO).as_posix()] = expected
        bind_files(ident, mapping, replacements=replacements)
        checks[-1]['manifest_count'] = len(manifests)
        checks[-1]['runtime_issues'] = runtime_issues
        checks[-1]['passed'] = checks[-1]['passed'] and not runtime_issues and len(manifests) == expected_manifests

    def bind_evidence_manifest(ident, path):
        data = json.loads(path.read_text())
        dependencies[path_key(path)] = sha(path)
        rows = data['files']
        if isinstance(rows, dict):
            mapping = {name: row['sha256'] for name, row in rows.items()}
            bind_files(ident, mapping)
        else:
            bind_files(ident, {row['path']: row['sha256'] for row in rows}, path.parent)
        return data

    def bind_raster(ident, directory):
        path = directory / 'render-report.json'
        data = json.loads(path.read_text())
        dependencies[path_key(path)] = sha(path)
        mapping = {}
        for row in data['results']:
            mapping[row['svg']] = row['svg_sha256']
            if row.get('mode') == 'tiles':
                mapping[row['tile_manifest']] = row['tile_manifest_sha256']
                tile_data = json.loads((directory / row['tile_manifest']).read_text())
                for tile in tile_data['tiles']:
                    mapping[tile['png']] = tile['sha256']
            elif row.get('png_sha256'):
                mapping[row['png']] = row['png_sha256']
        bind_files(ident, mapping, directory)
        checks[-1]['passed'] = checks[-1]['passed'] and data['status'] == 'passed'

    def bind_execution(ident, path, replacements=None, historical_runtime=None):
        data = json.loads(path.read_text())
        dependencies[path_key(path)] = sha(path)
        mapping = {}
        for field in ('inputs', 'outputs'):
            for name, expected in data[field].items():
                scope, name = name.split(':', 1)
                if scope not in {'source', 'run'}:
                    raise ValueError('unknown execution input scope: ' + scope)
                mapping[path_key((SHARED if scope == 'source' else path.parent) / name)] = expected
        for row in data.get('external_inputs', {}).values():
            mapping[path_key(Path(row['original_path']))] = row['sha256']
        for field in ('runtime_before', 'runtime_after'):
            for name, expected in data[field].items():
                mapping[path_key(SHARED / name)] = expected
        bind_files(ident, mapping, replacements=replacements)
        expected_runtime = historical_runtime if historical_runtime is not None else execution_fingerprints(SHARED)
        runtime_mismatches = sorted(name for name in set(data['runtime_before']) | set(expected_runtime)
                                    if data['runtime_before'].get(name) != expected_runtime.get(name))
        checks[-1]['historical_runtime_binding'] = historical_runtime is not None
        checks[-1]['runtime_mismatches'] = runtime_mismatches
        checks[-1]['passed'] = (checks[-1]['passed'] and data['passed']
                               and data['runtime_before'] == expected_runtime == data['runtime_after']
                               and not data['changed_input_paths'] and not data['changed_runtime_paths'])

    units = record('stable-full-unit-regressions', args.units,
                   lambda d: d['passed'] and d['source_stable'] and d['counts']['tests'] > 0
                   and not any(d['counts'][k] for k in ['failures', 'errors', 'skipped']))
    production = record('stable-production-profiles', args.production,
                        lambda d: d['passed'] and d['source_stable'] and all(r['status'] == 'pass' for r in d['checks'])
                        and d['checks'][0]['detail']['profiles'] == 297 and d['checks'][0]['detail']['layouts'] == 594)
    delivery_root = current_path('delivery-final', 'delivery-fixture-recheck')
    delivery = record('23-strict-candidate-deliverables', delivery_root / 'summary.json',
                      lambda d: d['passed'] and d['source_stable'] and d['result'] == {'deliverables': 23, 'sections': 90})
    bind_generated_bundle('594-current-production-output-bundles', args.production.resolve().parent / 'production', 594)
    bind_generated_bundle('23-current-candidate-delivery-output-bundles', delivery_root / 'current/deliverables', 23)
    coherent_root = current_path('adm-delivery-final', 'adm-delivery-current')
    coherent = record('same-case-23-deliverables-and-33-views', coherent_root / 'manifest.json',
                      lambda d: d['runtime_stable'] and d['rendered'] and len(d['deliverables']) == 23 and len(d['artifacts']) == 33)
    bind_generated_bundle('same-case-current-rendered-output-bundle', coherent_root, 1)
    method = record('44-procedural-method-candidate-review', run / 'procedural-review-current.json',
                    lambda d: d['passed'] and d['accepted'] is False and d['counts']['procedural_methods'] == 44
                    and d['counts']['current_declared_steps_reviewed'] == 201 and d['counts']['partial_or_missing_steps'] == 0)
    profile_root = current_path('profiles-current', 'profiles-tiled')
    profiles = record('297-profile-expression-and-render', profile_root / 'verification.json',
                      lambda d: d['independent_profiles_checked'] == 297 and d['artifact_families_checked'] == 196
                      and d['failed_profiles'] == 0 and d['render_status'] == 'passed')
    annotation_scope = {}
    annotation_export = current_run / 'annotation-leader-fix/export-summary.json'
    if continuation and annotation_export.is_file():
        canonical_runner = current_run / 'run-annotation-stable-verification.py'
        spec = importlib.util.spec_from_file_location('annotation_report_current_inputs', canonical_runner)
        stable = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(stable)
        current_source = stable.inputs()
        exported = record('actual-annotation-export-complete-at-current-source', annotation_export,
                          lambda d: d['passed'] and d['source_stable'])
        bind_files('actual-annotation-export-source-and-complete-output-bytes',
                   annotation_export_bindings(exported, current_run, current_source))
        application_path = current_run / 'annotation-leader-fix/source-application.json'
        application = record('reviewed-stopped-proposals-actually-applied', application_path,
                             lambda d: d['applied'] and d['passed_for_exact_applied_bytes'])
        bind_files('applied-annotation-and-dtra-proposal-current-bytes',
                   annotation_application_bindings(application, current_run, current_source))
        for name in ('annotation-leader-proposal', 'dtra-type-label-proposal', 'profiles-after-annotation-leader'):
            directory = current_run / name
            excluded = ([] if name == 'profiles-after-annotation-leader' else
                        [reviewed_proposal_manifest(current_run, name).name] if name in ('annotation-leader-proposal', 'dtra-type-label-proposal') else
                        ['integrity-manifest.json'])
            names = [p.relative_to(directory).as_posix() for p in directory.rglob('*')
                     if p.is_file() and p.relative_to(directory).as_posix() not in excluded]
            file_sets.append({'root': str(directory.relative_to(REPO)), 'exclude_files': excluded,
                              'paths_sha256': hashlib.sha256('\n'.join(sorted(names)).encode()).hexdigest()})
            # The published file-set roots use the ledger's TOGAF root base.
            file_sets[-1]['root'] = '../' + file_sets[-1]['root']
        selector_source = Path(select_independent_audit.__code__.co_filename).absolute()
        expected_selector_source = Path(__file__).absolute().with_name('independent_audit_selection.py')
        if selector_source != expected_selector_source or selector_source.is_symlink():
            raise ValueError('Independent audit selection helper was imported from an unexpected path')
        dependencies[path_key(selector_source)] = sha(selector_source)
        audit_selection = select_independent_audit(current_run, current_source, annotation_export, REPO)
        audit_root = audit_selection['audit_root']
        for spec in audit_selection['input_file_sets']:
            if spec not in file_sets:
                file_sets.append(spec)
        bind_files('independent-annotation-selected-pointer-and-prior-complete-sealed-evidence-bytes',
                   audit_selection['evidence_bindings'])
        audit = record('independent-annotation-audit-at-recorded-supported-scope', audit_root / 'summary.json',
                       lambda d: d['source_stable'] and d['actual_svg_files'] == 712
                       and d['passed_for_recorded_geometry_scope']
                       and d['current_export_summary_sha256'] == sha(annotation_export)
                       and all(d.get(field) is False for field in ('accepted', 'full_diagram_acceptance',
                                                                 'business_acceptance', 'professional_acceptance')))
        for field in ('input_sha256', 'source_sha256', 'output_sha256'):
            mapping = audit.get(field, {})
            if not isinstance(mapping, dict) or not mapping:
                raise ValueError('Missing independent audit byte bindings: ' + field)
            bind_files('independent-annotation-audit-' + field, mapping)
        bind_files('independent-annotation-audit-complete-sealed-evidence-bytes',
                   sealed_evidence_files(audit_root / 'integrity-manifest.json'))
        for field in ('annotation_geometry_report', 'path_delta_report'):
            target = (audit_root / audit[field]).resolve()
            if not target.is_relative_to(audit_root.resolve()) or not target.is_file():
                raise ValueError('Invalid independent annotation report path: ' + field)
            dependencies[path_key(target)] = sha(target)
        annotation_scope = {'actual_svg_files': audit['actual_svg_files'],
                            'passed_for_recorded_geometry_scope': audit['passed_for_recorded_geometry_scope'],
                            'unsupported_annotation_shape_cases': audit['unsupported_annotation_shape_cases'],
                            'full_shape_or_professional_acceptance': False}
    raster = record('712-svg-760-png-integrity', current_path('profile-raster-integrity.json', 'profile-raster-integrity-final.json'),
                    lambda d: d['passed'] and d['counts']['checked'] == 712 and d['counts']['png_files'] == 760)
    bind_raster('current-profile-raster-bytes', profile_root)
    geometry_path = next(current_path('profile-geometry', 'profile-geometry').glob('*/geometry-check.json'))
    geometry = record('712-svg-text-geometry', geometry_path,
                      lambda d: d['status'] == 'passed' and d['checked'] == 712 and d['flagged'] == 0)
    if continuation:
        bind_execution('current-svg-geometry-source-input-output-bytes', geometry_path.parent / 'execution.json')
    native_root = current_path('native-current', 'native-current-validation')
    native = record('native-public-render-and-rejection', native_root / ('cli/public-cli-summary.json' if continuation else 'public-cli-summary.json'),
                    lambda d: d['passed'] and d['source_stable'] and len(d['cases']) == 12
                    and d['full_language_acceptance'] is False)
    native_manifest = bind_evidence_manifest('native-current-files', native_root / 'integrity-manifest.json')
    bind_files('native-current-source-files', native_manifest['runtime_source_files'] if continuation else native_manifest['source_files'])
    ocl_unmapped = 3
    language_scope = {}
    if continuation:
        native_summary = record('native-current-bounded-summary', native_root / 'summary.json',
                                lambda d: d['passed'] and d['source_stable'] and d['full_language_acceptance'] is False)
        bind_files('native-external-runtime-files', {name: row['sha256'] for name, row in native_manifest['external_runtime_files'].items()})
        ocl_unmapped = native_summary['mapped_ocl']['ocl_unmapped']
        ocl = record('pinned-ocl-syntax-adapters-and-boundaries', current_run / 'ocl/summary.json',
                     lambda d: d['official_rules_match_original_snapshot'] and d['normative_document_bytes_match_before_snapshot']
                     and d['normative_rule_count'] == 425 and d['public_cli']['parsed'] == 424
                     and d['public_cli']['unmapped'] == 1 and d['official_full_conformance'] is False
                     and all(row['returncode'] == 0 for row in d['tests'][:2]))
        ocl_manifest = bind_evidence_manifest('ocl-current-evidence-files', current_run / 'ocl/integrity-manifest.json')
        bind_files('ocl-current-adapter-sources', {row['source']: row['after_sha256'] for row in ocl_manifest['source_snapshots']})
        bpmn_root = current_path('bpmn-independent-review', 'bpmn-independent-review')
        bpmn = record('bounded-bpmn-independent-counterexamples', bpmn_root / 'final-audit.json',
                      lambda d: d['passed_for_targeted_implemented_family_checks'] and d['source_stable']
                      and d['matches_final_native_source_baseline'] and d['event_condition_case_count'] == 15
                      and d['reference_cancel_case_count'] == 23 and d['full_language_conformance'] is False)
        bind_evidence_manifest('bpmn-current-and-retained-evidence-files', bpmn_root / 'final-integrity-manifest.json')
        if bpmn.get('native_source_baseline'):
            bind_files('bpmn-current-native-baseline-binding', {bpmn['native_source_baseline']: bpmn['native_source_baseline_sha256']})
        else:
            checks.append({'id': 'bpmn-current-native-baseline-binding', 'passed': False,
                           'reason': 'missing-native-source-baseline-reference'})
        prior_path = bpmn_root / 'prior-evidence-after.json'
        if prior_path.is_file():
            prior = json.loads(prior_path.read_text())
            dependencies[path_key(prior_path)] = sha(prior_path)
            bind_files('bpmn-unchanged-historical-evidence-chain', prior['files'], REPO / prior['path'])
            checks[-1]['passed'] = checks[-1]['passed'] and not prior.get('changes')
        for name in ['event-probes', 'reference-probes']:
            path = bpmn_root / name / 'final-recheck/summary.json'
            report = json.loads(path.read_text())
            dependencies[path_key(path)] = sha(path)
            bind_files('bpmn-final-' + name + '-source-files', report['source_before'])
        language_scope = {'mapped_ocl': native_summary['mapped_ocl'],
                          'ocl_original_rule_count': ocl['normative_rule_count'],
                          'bpmn_bounded_counterexamples': {'event_conditions': bpmn['event_condition_case_count'],
                                                         'reference_cancel': bpmn['reference_cancel_case_count']},
                          'bpmn_remaining_conditions': bpmn['remaining_conditions']}
    method_manifest_path = REPO / 'output/adm-goal-20261108/methods/current-input-output-sha256.json'
    method_manifest = json.loads(method_manifest_path.read_text())
    dependencies[method_manifest_path.relative_to(REPO).as_posix()] = sha(method_manifest_path)
    bind_files('procedural-method-teaching-inputs', method_manifest['inputs_sha256_relative_to_togaf_root'], C)
    if continuation:
        for ident, folder, count in [('12-current-procedural-tables', 'procedural-generated-current', 12),
                                    ('4-current-agile-svg-png', 'procedural-agile-generated-current', 4)]:
            directory = current_path(folder, folder)
            summary = record(ident, directory / 'summary.json',
                             lambda d, count=count: d['passed'] and d['accepted'] is False
                             and len(d['runs']) == count and all(r['passed'] for r in d['runs']))
            bind_generated_bundle(ident + '-bundles', directory, count)
    else:
        bind_files('procedural-method-generated-outputs', method_manifest['outputs_sha256_relative_to_workspace'])
    record('current-normal-render-wrapper', current_path('profile-render-wrapper-small/verification.json', 'profile-render-wrapper-small-current/verification.json'),
           lambda d: d['status'] == 'passed' and d['render_status'] == 'passed')
    record('explicit-original-resolution-tiled-render-wrapper', current_path('profile-render-wrapper-tile/verification.json', 'profile-render-wrapper-tile-current/verification.json'),
           lambda d: d['status'] == 'passed' and d['render_status'] == 'passed' and d['oversized_policy'] == 'tile')
    if continuation:
        for name in ['small', 'tile']:
            directory = current_path('profile-render-wrapper-' + name + '/verification.json', '').parent
            bind_raster('current-' + name + '-wrapper-raster-bytes', directory)
    reader = record('offline-297-profile-catalogue', current_run / 'artifacts-reader-verification.json', lambda d: d['passed'])
    if continuation:
        bind_files('offline-reader-screenshot-bytes', {name: row['sha256'] for name, row in reader['output_files'].items()})
        record('actual-reader-layout-observations', current_run / 'artifacts-reader-observations.json',
               lambda d: d['passed_for_reader_layout'] and d['actual_images_viewed'] == 2
               and d['diagram_visual_acceptance'] is False)
    dependencies[(current_run / 'artifacts.html').relative_to(REPO).as_posix()] = sha(current_run / 'artifacts.html')
    visual_scope = {}
    if continuation and (current_run / 'visual-current-coverage.json').is_file():
        visual = record('bounded-actual-visual-observations-at-current-bytes', current_run / 'visual-current-coverage.json',
                        lambda d: d['passed_for_recorded_observation_byte_freshness']
                        and d['accepted'] is False and d['full_diagram_acceptance'] is False)
        visual_scope = visual['counts']

    isolated_method_scope = {}
    isolated_method_root = current_run / 'method-independent-next'
    if continuation and (isolated_method_root / 'summary.json').is_file():
        exercise = record('one-context-separated-ai-method-exercise', isolated_method_root / 'summary.json',
                          lambda d: d['passed_for_precommitted_checks'] and d['actual_execution']['runtime_stable']
                          and d['counts']['selected_procedural_methods'] == 1
                          and d['counts']['actual_cli_runs_in_selected_batch'] == 3
                          and d['counts']['successful_cli_runs_in_selected_batch'] == 3
                          and d['counts']['step_observations_across_variants'] == 15
                          and d['counts']['failed_assertions'] == 0
                          and d['precommitted_criteria']['fixed_before_executor_spawn']
                          and not d['precommitted_criteria']['changed_to_match_outputs']
                          and d['executor_isolation']['fork_turns'] == 'none'
                          and not d['executor_isolation']['read_authored_examples']
                          and not d['executor_isolation']['read_precommitted_criteria']
                          and d['accepted'] is False and d['full_method_acceptance'] is False
                          and d['counts']['native507_independent_execution_increment'] == 0)
        path = isolated_method_root / 'integrity-manifest.json'
        method_integrity = json.loads(path.read_text())
        dependencies[path_key(path)] = sha(path)
        bind_files('isolated-method-local-evidence-bytes', method_integrity['files'], isolated_method_root)
        projection_root = current_path('method-projection-current', 'method-projection-current')
        replacements = None
        historical_runtime = None
        historical_execution_runtime = None
        if (projection_root / 'summary.json').is_file():
            replay = record('current-source-replay-of-three-frozen-method-inputs', projection_root / 'summary.json',
                            lambda d: d['passed'] and d['source_stable'] and d['actual_cli_runs'] == 3
                            and d['independent_method_execution_increment'] == d['native507_execution_increment'] == 0
                            and d['accepted'] is False and all(row['passed'] for row in d['comparisons']))
            replacements = historical_runtime_snapshots(method_integrity['runtime_source_files'], current_run)
            replay_snapshots = replay['historical_runtime_replacements']
            bind_files('method-replay-declared-historical-runtime-snapshot-bytes',
                       {row['snapshot']: row['historical_sha256'] for row in replay_snapshots.values()})
            checks[-1]['passed'] = (checks[-1]['passed'] and set(replay_snapshots) == set(replacements)
                                   and all(method_integrity['runtime_source_files'].get(name) == row['historical_sha256']
                                           for name, row in replay_snapshots.items()))
            prior_execution = json.loads(Path(exercise['actual_execution']['execution_json']).read_text())
            historical_execution_runtime = prior_execution['runtime_before']
            registries = {'capabilities.json', 'artifacts.json', 'deliverables.json', 'metamodel.json'}
            historical_runtime = {name: value for name, value in historical_execution_runtime.items() if name not in registries}
            replay_manifest = json.loads((projection_root / 'integrity-manifest.json').read_text())
            dependencies[path_key(projection_root / 'integrity-manifest.json')] = sha(projection_root / 'integrity-manifest.json')
            bind_files('current-method-projection-replay-evidence', replay_manifest['files'], projection_root)
            bind_execution('current-method-projection-replay-actual-execution', Path(replay['execution_json']))
            bind_generated_bundle('current-method-projection-three-replayed-bundles', Path(replay['generated_root']), 3)
        bind_files('isolated-method-original-runtime-bytes', method_integrity['runtime_source_files'], replacements=replacements)
        bind_execution('isolated-method-original-cli-source-input-output-bytes', Path(exercise['actual_execution']['execution_json']),
                       replacements=replacements, historical_runtime=historical_execution_runtime)
        bind_generated_bundle('isolated-method-three-original-output-bundles', isolated_method_root / 'isolated-executor', 3,
                              historical_runtime=historical_runtime, replacements=replacements)
        isolated_method_scope = {**exercise['counts'], 'original_execution_is_historical': historical_execution_runtime is not None,
                                 'current_frozen_input_projection_replay_cli_runs': 3 if historical_execution_runtime is not None else 0,
                                 'additional_independent_method_executions': 0}

    native_freeze_scope = {}
    if continuation and (current_run / 'current-native-freeze.json').is_file():
        freeze = record('current-native-frozen-source-copy-bytes', current_run / 'current-native-freeze.json',
                        lambda d: d['passed_for_current_snapshot_bytes'] and d['source_stable']
                        and d['counts']['native507_executions'] == 0 and d['counts']['model_requests'] == 0
                        and d['accepted'] is False and d['full_native_readiness'] is False
                        and not d['permissions_or_formal_budget_changed'])
        frozen_root = Path(freeze['runtime'])
        frozen_manifest_path = frozen_root / 'runtime-manifest.json'
        frozen_manifest = json.loads(frozen_manifest_path.read_text())
        bind_files('current-native-source-file-bytes', freeze['source_sha256'])
        bind_files('current-native-freeze-builder-bytes', freeze['builder_sha256'])
        frozen_files = {str(frozen_manifest_path): freeze['runtime_manifest_sha256']}
        for base, field, excluded in [(frozen_root / 'skills', 'frozen_hashes', ['.venv', 'node_modules', '__pycache__', '.DS_Store']),
                                      (frozen_root / 'skills/_shared', 'dependency_hashes', ['__pycache__']),
                                      (frozen_root / 'wheels', 'wheel_hashes', []),
                                      (Path(frozen_manifest['java_home']), 'java_hashes', []),
                                      (Path(frozen_manifest['browser_home']), 'browser_hashes', [])]:
            rows = frozen_manifest[field]
            frozen_files.update({str(base / name): expected for name, expected in rows.items()})
            if field == 'dependency_hashes':
                for prefix in ['node_modules', '.venv']:
                    names = [name[len(prefix) + 1:] for name in rows if name.startswith(prefix + '/')]
                    file_sets.append({'root': str(base / prefix), 'exclude_parts': excluded,
                                      'paths_sha256': hashlib.sha256('\n'.join(sorted(names)).encode()).hexdigest()})
            else:
                file_sets.append({'root': str(base), 'exclude_parts': excluded,
                                  'paths_sha256': hashlib.sha256('\n'.join(sorted(rows)).encode()).hexdigest()})
        for row in frozen_manifest['tool_binaries'].values():
            frozen_files[row['path']] = row['sha256']
        bind_files('current-frozen-source-dependency-and-external-runtime-bytes', frozen_files)
        source_names = frozen_manifest['source_hashes']
        file_sets.append({'root': 'skills', 'exclude_parts': ['.venv', 'node_modules', '__pycache__', '.DS_Store'],
                          'paths_sha256': hashlib.sha256('\n'.join(sorted(source_names)).encode()).hexdigest()})
        checks[-1]['passed'] = (checks[-1]['passed'] and frozen_manifest['source_hashes'] == frozen_manifest['frozen_hashes']
                               and len(source_names) == freeze['counts']['current_source_files'])
        native_freeze_scope = {'runtime': freeze['runtime'], 'counts': freeze['counts'],
                               'manifest_sha256': freeze['runtime_manifest_sha256'],
                               'native_sandbox_preflight': 'not-currently-passed',
                               'native507_independent_executions': 0}

    native_preflight_path = current_run / 'current-native-preflight.json'
    if continuation and native_preflight_path.is_file():
        preflight = record('current-zero-model-native-preflight-outcome', native_preflight_path,
                           lambda d: d['passed_for_actual_zero_model_evidence'] and d['source_stable']
                           and d['model_sessions'] == 0 and d['model_requests_observed'] == 0
                           and d['native507_executions'] == 0 and d['accepted'] is False
                           and not d['formal_campaign_budget_changed'] and not d['permissions_changed']
                           and d['actual_preflight_status'] in {'pass', 'blocked', 'fail'})
        preflight_root = Path(preflight['evidence_root'])
        path = preflight_root / 'integrity-manifest.json'
        preflight_integrity = json.loads(path.read_text())
        dependencies[path_key(path)] = sha(path)
        bind_files('current-native-preflight-actual-evidence-bytes', preflight_integrity['files'], preflight_root)
        bind_files('current-native-preflight-source-code-bytes', preflight['source_code_sha256'])
        checks[-1]['passed'] = checks[-1]['passed'] and preflight['runtime_manifest_sha256'] == native_freeze_scope.get('manifest_sha256')
        native_freeze_scope.update(native_sandbox_preflight=preflight['actual_preflight_status'],
                                   native_preflight_passed=preflight['native_preflight_passed'],
                                   actual_preflight_failed_probes=preflight['failed_probes'])

    flow_root = C / 'architecture/adm-flow'
    manifest = json.loads((flow_root / 'manifest.json').read_text())
    flow = json.loads((run / 'adm-flow-final-verification.json').read_text())
    flow_inputs = {'togaf-standard-10th-ai/skills/_shared/' + name: expected
                   for name, expected in manifest['input_sha256'].items()}
    flow_inputs.update({'togaf-standard-10th-ai/architecture/adm-flow/' + name: expected
                        for name, expected in manifest['output_sha256'].items()})
    flow_inputs['togaf-standard-10th-ai/architecture/adm-flow/manifest.json'] = sha(flow_root / 'manifest.json')
    flow.update(input_sha256=flow_inputs, passed=flow['status'] == 'passed', accepted=False)
    write(C / 'quality/adm-flow-verification.json', flow)
    record('complete-adm-flow-reader', C / 'quality/adm-flow-verification.json',
           lambda d: d['passed'] and d['coverage']['source_step_count'] == 94
           and d['coverage']['deliverable_count'] == 23 and len(d['coverage']['diagram_ids']) == 13)
    record('release-current-files-and-lock', C / 'quality/release-current-validation.json', lambda d: d['passed'])
    portable = record('actual-sealed-archive-portability', C / 'quality/portability-validation.json', lambda d: d['passed'])
    record('current-entrypoint-links', C / 'quality/current-entrypoint-links.json', lambda d: d['passed'])
    record('semantic-regressions', C / 'maintenance/semantic-regression-report.json', lambda d: report_outcome(d)['passed'])
    record('local-runtime-regressions', C / 'quality/local-runtime-regression.json', lambda d: d['passed'])

    result = {'schema_version': 'adm-completion-engineering/2',
              'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'passed': all(r['passed'] for r in checks),
              'counts': {'checks': len(checks), 'passed': sum(r['passed'] for r in checks),
                         'failed': sum(not r['passed'] for r in checks)},
              'checks': checks, 'input_sha256': dict(sorted(dependencies.items())), 'input_file_sets': file_sets,
              'executed_scope': {'unit_regressions': units['counts'], 'production_profiles': production['checks'],
                                 'strict_candidate_deliverables': delivery['result'],
                                 'same_case_rendered_delivery': {'deliverables': len(coherent['deliverables']), 'views': len(coherent['artifacts'])},
                                 'procedural_candidate_review': method['counts'],
                                 'profile_count': profiles['independent_profiles_checked'],
                                 'artifact_families': profiles['artifact_families_checked'],
                                 'profile_output_kinds': profiles['output_kinds_checked'],
                                 'raster_integrity': raster['counts'], 'svg_text_geometry': geometry['checked'],
                                 'bounded_annotation_geometry_evidence': annotation_scope,
                                 'adm_source_steps': 94, 'adm_diagrams': 13,
                                 'native_public_cli_checks': len(native['cases']), 'portable_checks': portable['counts'],
                                 'bounded_language_evidence': language_scope,
                                 'bounded_actual_visual_observations': visual_scope,
                                 'bounded_context_separated_ai_method_exercise': isolated_method_scope,
                                 'current_native_frozen_byte_snapshot': native_freeze_scope},
              'all_capabilities_accepted': False, 'accepted': False, 'business_acceptance': False,
              'real_business_approval': 'not-granted',
              'remaining': {'independent_evaluation_inventory': 507,
                            'professional_method_blind_executions': 0,
                            'full_generated_diagram_semantic_visual_acceptance': False,
                            'UML_673_BPMN_442_complete_construct_acceptance': False,
                            'unmapped_UML_OCL_rules': ocl_unmapped,
                            'ArchiMate_4_normative_source': 'not-acquired; authorized source required'},
              'history': ['Earlier reports and archives retain their recorded bytes and revision; they are historical after source changes.',
                          'The interrupted production-current and initial diagnostic mismatch remain in the continuation directory.',
                          'First failing production run remains in the historical campaign production/.',
                          'Missing-render-prerequisite and default oversized blocking evidence remain saved.',
                          'Old archives and stored status are preserved under before/.',
                          'This report replaces stale evidence as the current engineering entry; it does not refresh old test hashes.'],
              'limits_zh': ['passed只表示本报告逐项列明的工程检查通过。',
                            '文字边界、PNG完整性和作者观察不授予全图专业或来源等价接受。',
                            '23份交付物及44方法材料属于虚构候选；真实组织批准未授予。',
                            '当前原生语言渲染仅支持声明的子集，完整正式符合性未完成。',
                            '不同套件计数有重叠，不累加为能力覆盖率。']}
    if annotation_scope:
        result['limits_zh'].append('独立标注审计仅覆盖其明确支持的实际几何；未充分验证的形状范围保留在bounded_annotation_geometry_evidence，不能解释为全形状或专业接受。')
    write(C / 'quality/adm-completion-verification.json', result)
    write(current_run / 'current-engineering-summary.json', result)
    print(json.dumps({'passed': result['passed'], 'counts': result['counts'],
                      'failed_checks': [r['id'] for r in checks if not r['passed']]}, ensure_ascii=False))
    return int(not result['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
