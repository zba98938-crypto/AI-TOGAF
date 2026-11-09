"""Read a sealed retry pointer and preserve the exact prior failed audit."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

POINTER_SCHEMA = 'current-independent-audit-selection/1'
SUMMARY_SCHEMA = 'actual-independent-full-recorded-geometry-scope/1'
MANIFEST_SCHEMA = 'independent-audit-integrity/1'
PRIOR_SUMMARY_SHA256 = 'f46ee571f0dea164c03949d868112f5db0a48d767ecbe7527b6e7bd08f710f75'
PRIOR_MANIFEST_SHA256 = '3c828a43868d5f8e7bc9115723ad180167390fc4dc4811aa308d270bef19e911'
EXPORT_SHA256 = '48122cf67775f66a028d9d641a530434a8b8f3272f076ff4d69fd401daa50166'
ACCEPTANCE_FIELDS = ('accepted', 'human_acceptance', 'business_acceptance',
    'professional_acceptance', 'source_equivalence_acceptance', 'full_diagram_acceptance')
REQUIRED_CHECKS = frozenset((
    'actual_root_export_schema_and_passed', 'actual_root_counts297_712',
    'actual_svg_names_exact_original712', 'actual178_diagrams_each_four_variants',
    'no_nested_untracked_svg', 'source_before_after_current_complete_maps_equal',
    'actual_request_bound_to_complete_sources_and_runner',
    'export_input_map_exact_complete_sources_plus_runner',
    'export_input_sha_current_at_start_end', 'export_output_map_exact_all_actual_files',
    'all_audit_input_bytes_stable', 'current_export_summary_sha_stable',
    'original_baseline_v8_full712_sha_binding_stable', 'portable_current_oracle_bundle_exact',
    'complete_authoritative_named_proposal_seal_verified_stable',
    'complete_authoritative_dtra_dictionary_seal_verified_stable',
    'exact_sealed20_complete_application_chain_verified_stable',
    'prior_v3_failed_attempt_exact_preserved', 'annotation_raw_full712_passed',
    'business_delta_raw_full712_passed', 'every_actual_badge_own_ink_footprint_checked',
    'actual_embedded_glyph_metrics_all_passed', 'actual_annotation_canvas_envelopes_all_inside',
    'canonical_font_source_is_export_bound',
    'canonical_weight400_instance_matches_actual_bound_producer',
    'all_relevant_owner_nonpath_exact_unchanged_and_actual_oracle_inventoried',
    'independent_annotation_instance_inventory_exact', 'no_unverified_footprints_in_relevant_scope',
    'actual_agile16_unchanged_no_annotations', 'all_changed_endpoint_card_hierarchies_preserved',
    'all_changed_relationship_ledgers_preserved'))
RETRY_ONLY_CHECKS = frozenset(('prior_v3_failed_attempt_exact_preserved',
    'canonical_weight400_instance_matches_actual_bound_producer',
    'all_relevant_owner_nonpath_exact_unchanged_and_actual_oracle_inventoried'))
PRIOR_FALSE_CHECKS = frozenset(('actual_embedded_glyph_metrics_all_passed',
    'no_unverified_footprints_in_relevant_scope'))
POINTER_FIELDS = frozenset(('schema_version', 'audit_directory', 'summary_sha256',
    'integrity_manifest_sha256', 'current_export_summary_sha256',
    'prior_failed_summary_sha256', 'prior_failed_integrity_manifest_sha256'))
HEX_SHA256 = re.compile(r'[0-9a-f]{64}\Z')


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _relative(name):
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('Invalid relative audit path')
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or path.as_posix() != name or name == '.':
        raise ValueError('Unsafe or noncanonical relative audit path: ' + name)
    return Path(*path.parts)


def _checked_path(root, name):
    root = Path(root).absolute()
    target = root / _relative(name)
    # Inspect the lexical path before resolve: resolving first erases parent symlinks.
    for part in reversed((target, *target.parents)):
        if part.is_symlink():
            raise ValueError('Audit path contains a symlink: ' + str(part))
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError('Audit path escaped its declared root')
    return target


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


def _json(path):
    try:
        data = json.loads(path.read_text(), object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError('Unreadable audit JSON: ' + str(path)) from exc
    if not isinstance(data, dict):
        raise ValueError('Audit JSON must be an object: ' + str(path))
    return data


def _digest(value):
    if not isinstance(value, str) or HEX_SHA256.fullmatch(value) is None:
        raise ValueError('Invalid SHA256 binding')
    return value


def _flags(data):
    if not all(data.get(name) is False for name in ACCEPTANCE_FIELDS):
        raise ValueError('All six audit acceptance flags must be exactly false')


def _mapping(data, field, repo):
    mapping = data.get(field)
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError('Missing complete audit map: ' + field)
    for name, digest in mapping.items():
        _checked_path(repo, name)
        _digest(digest)
    return mapping


def _sealed_directory(root, expected_summary_sha, expected_manifest_sha, repo, count=None):
    manifest_path = _checked_path(root, 'integrity-manifest.json')
    summary_path = _checked_path(root, 'summary.json')
    if not manifest_path.is_file() or _sha(manifest_path) != _digest(expected_manifest_sha):
        raise ValueError('Independent audit manifest SHA mismatch')
    manifest = _json(manifest_path)
    if (set(manifest) != {'schema_version', 'files', 'actual_runs', *ACCEPTANCE_FIELDS}
            or manifest.get('schema_version') != MANIFEST_SCHEMA
            or type(manifest.get('actual_runs')) is not int or manifest['actual_runs'] != 1):
        raise ValueError('Invalid actual independent audit manifest schema')
    _flags(manifest)
    rows = manifest.get('files')
    if not isinstance(rows, dict) or not rows or (count is not None and len(rows) != count):
        raise ValueError('Invalid complete audit seal inventory')
    if rows.get('summary.json') != _digest(expected_summary_sha):
        raise ValueError('Audit summary is not exactly bound by its manifest')
    actual = set()
    for path in root.rglob('*'):
        checked = _checked_path(root, path.relative_to(root).as_posix())
        if checked.is_file() and checked != manifest_path:
            actual.add(checked.relative_to(root).as_posix())
    if actual != set(rows):
        raise ValueError('Audit directory file set differs from its complete seal')
    bindings = {manifest_path.relative_to(repo).as_posix(): expected_manifest_sha}
    for name, digest in rows.items():
        if name == 'integrity-manifest.json':
            raise ValueError('An audit manifest cannot seal itself')
        path = _checked_path(root, name)
        if not path.is_file() or _sha(path) != _digest(digest):
            raise ValueError('Sealed independent audit bytes changed: ' + name)
        bindings[path.relative_to(repo).as_posix()] = digest
    summary = _json(summary_path)
    spec = {'root': '../' + root.relative_to(repo).as_posix(),
        'exclude_files': ['integrity-manifest.json'],
        'paths_sha256': hashlib.sha256('\n'.join(sorted(rows)).encode()).hexdigest()}
    return summary, bindings, spec


def _summary_contract(data, export, repo, retry):
    if (data.get('schema_version') != SUMMARY_SCHEMA
            or type(data.get('actual_runs')) is not int or data['actual_runs'] != 1
            or type(data.get('actual_svg_files')) is not int or data['actual_svg_files'] != 712
            or data.get('source_stable') is not True
            or data.get('current_export_summary_sha256') != EXPORT_SHA256):
        raise ValueError('Invalid actual independent full712 summary contract')
    _flags(data)
    if (_mapping(data, 'source_sha256', repo) != export['input_sha256']
            or _mapping(data, 'canonical_source_sha256', repo) != export['input_sha256']
            or _mapping(data, 'output_sha256', repo) != export['output_sha256']):
        raise ValueError('Audit source/output maps differ from the exact current export')
    _mapping(data, 'input_sha256', repo)
    checks = data.get('checks')
    if retry:
        if (not isinstance(checks, dict) or set(checks) != REQUIRED_CHECKS
                or not all(value is True for value in checks.values())
                or data.get('passed_for_recorded_geometry_scope') is not True):
            raise ValueError('Selected retry must pass all exact31 recorded-scope checks')
        if (type(data.get('prior_independent_actual_runs')) is not int or data['prior_independent_actual_runs'] != 1
                or type(data.get('cumulative_independent_actual_runs')) is not int or data['cumulative_independent_actual_runs'] != 2
                or type(data.get('actual_root_full_profile_export_count')) is not int or data['actual_root_full_profile_export_count'] != 1
                or data.get('prior_failed_summary_sha256') != PRIOR_SUMMARY_SHA256
                or data.get('prior_failed_integrity_manifest_sha256') != PRIOR_MANIFEST_SHA256):
            raise ValueError('Selected retry does not preserve the exact prior failure/run history')
    elif (not isinstance(checks, dict) or set(checks) != REQUIRED_CHECKS - RETRY_ONLY_CHECKS
            or any(value is not (name not in PRIOR_FALSE_CHECKS) for name, value in checks.items())
            or data.get('passed_for_recorded_geometry_scope') is not False):
        raise ValueError('The pinned prior failed attempt must remain an exact failed result')


def select_independent_audit(current_run, current_source, export_path, repo):
    """Absent pointer retains the old failed default; any present-pointer error raises."""
    repo = Path(repo).absolute()
    run = _checked_path(repo, Path(current_run).absolute().relative_to(repo).as_posix())
    fix = _checked_path(run, 'annotation-leader-fix')
    export_path = _checked_path(fix, Path(export_path).absolute().relative_to(fix).as_posix())
    if not export_path.is_file() or _sha(export_path) != EXPORT_SHA256:
        raise ValueError('The sole completed current export summary SHA changed')
    export = _json(export_path)
    if export.get('schema_version') != 'actual-complete-profile-export/1' or export.get('passed') is not True:
        raise ValueError('The current export must be a genuine passed complete export')
    if not isinstance(current_source, dict) or not current_source:
        raise ValueError('A nonempty complete current source map is required')
    runner = _checked_path(fix, 'run_full_export.py')
    expected_source = {**current_source, runner.relative_to(repo).as_posix(): _sha(runner)}
    if _mapping(export, 'input_sha256', repo) != expected_source:
        raise ValueError('The export source map differs from current complete sources plus runner')
    _mapping(export, 'output_sha256', repo)
    prior_root = _checked_path(fix, 'independent-audit')
    prior, prior_bindings, prior_spec = _sealed_directory(prior_root,
        PRIOR_SUMMARY_SHA256, PRIOR_MANIFEST_SHA256, repo, count=26)
    _summary_contract(prior, export, repo, retry=False)
    pointer_path = _checked_path(fix, 'current-independent-audit.json')
    if not pointer_path.exists():
        return {'audit_root': prior_root, 'pointer_present': False,
            'input_file_sets': [prior_spec], 'evidence_bindings': prior_bindings}
    if not pointer_path.is_file():
        raise ValueError('The independent audit pointer must be a regular JSON file')
    pointer = _json(pointer_path)
    if set(pointer) != POINTER_FIELDS or pointer.get('schema_version') != POINTER_SCHEMA:
        raise ValueError('Invalid unique independent audit pointer schema')
    for name in POINTER_FIELDS - {'schema_version', 'audit_directory'}:
        _digest(pointer[name])
    if (pointer['current_export_summary_sha256'] != EXPORT_SHA256
            or pointer['prior_failed_summary_sha256'] != PRIOR_SUMMARY_SHA256
            or pointer['prior_failed_integrity_manifest_sha256'] != PRIOR_MANIFEST_SHA256):
        raise ValueError('Pointer current-export or exact prior-failure SHA mismatch')
    selected_root = _checked_path(fix, pointer['audit_directory'])
    if not selected_root.is_dir() or selected_root == prior_root:
        raise ValueError('Pointer must select a new actual independent audit directory')
    selected, selected_bindings, selected_spec = _sealed_directory(selected_root,
        pointer['summary_sha256'], pointer['integrity_manifest_sha256'], repo)
    _summary_contract(selected, export, repo, retry=True)
    return {'audit_root': selected_root, 'pointer_present': True,
        'input_file_sets': [prior_spec, selected_spec],
        'evidence_bindings': {**prior_bindings, **selected_bindings,
            pointer_path.relative_to(repo).as_posix(): _sha(pointer_path)}}
