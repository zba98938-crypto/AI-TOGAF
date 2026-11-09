#!/usr/bin/env python3
"""Read-only identity/provenance checks for new authored procedural materials.

These checks establish which current steps and source rows are present. They do
not establish professional judgment, blind Agent behavior or human acceptance.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'skills/_shared'
MATERIALS = SHARED / 'references/method-case-materials/procedural-supplements'
POSITIONS = {
    'reference-model-tailoring': [2], 'mdm-four-plateau-operations-method': [1, 3],
    'msa-contract-consumer-evidence-method': [3], 'bi-stage-operability-and-exit-method': [3, 4],
    'bi-requirement-origin-boundary-method': [2], 'government-reference-catalog-overlay-method': [1, 3, 6, 7],
    'dbrm-mapping-suite-method': [2, 5, 6, 7, 8], 'digital-enablement-competency-mapping-method': [1],
    'product-architecture-allocation-method': [2, 4], 'msa-federated-governance-process-method': [1, 2, 3],
    'msa-value-resource-evidence-method': [2, 4], 'bi-usage-goal-measures-method': [2, 5],
    'bi-business-function-coverage-method': [1, 2, 3, 5], 'bi-application-function-coverage-method': [1, 2, 3, 5],
    'mdm-business-function-coverage-method': [1, 2, 3, 5], 'mdm-application-function-coverage-method': [1, 2, 3, 5],
    'bi-value-chain-controls-method': [3, 4], 'bi-model-operating-monitoring-method': [3, 5],
    'agile-collaboration-selection-switch': [6],
}
FUNCTION_ROWS = {'bi-business-function-coverage-method': ('G238-T4-2-', 54),
                 'bi-application-function-coverage-method': ('G238-T4-3-', 59),
                 'mdm-business-function-coverage-method': ('G21B-T5-3-', 29),
                 'mdm-application-function-coverage-method': ('G21B-T5-4-', 38)}


def digest(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reference_projection(profile):
    fields = {'source_locator', 'source_uncertainty', 'source_row_id', 'pillar', 'competency',
              'dpbok_context', 'context_kind', 'raw_cells', 'source_line', 'source_lines'}
    return [{'entity_id': e['id'], 'reference_attributes': {
        k: copy.deepcopy(v) for k, v in e['attributes'].items() if k.startswith('reference_') or k in fields}}
        for e in profile['example']['entities']]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(materials=MATERIALS):
    caps = json.loads((SHARED / 'capabilities.json').read_text())
    methods = {m['id']: m for m in caps['analysis_methods']}
    profiles = {p['id']: p for p in caps['profiles']}
    paths = {p.stem: p for p in materials.glob('*.json')}
    require(set(paths) == set(POSITIONS), 'supplement identity set differs from the 19 reviewed methods')
    hashes = {}
    for mid, positions in POSITIONS.items():
        path = paths[mid]
        data = json.loads(path.read_text())
        require(data.get('method_id') == mid and data.get('schema_version') == 'procedural-teaching-supplement/1', mid + ': identity')
        require(data.get('accepted') is False and data.get('origin') == 'new-fictional-teaching-materials', mid + ': provenance/acceptance')
        require([s['position'] for s in data['steps']] == positions, mid + ': current step positions')
        declared = methods[mid].get('analysis_steps') or methods[mid].get('steps')
        for step in data['steps']:
            require(step['declared_step'] == declared[step['position'] - 1], mid + ': stale step text')
            for field in ('new_fictional_input', 'transformation', 'candidate_output', 'adverse_variant_expected'):
                require(isinstance(step.get(field), str) and bool(step[field].strip()), mid + ': empty ' + field)
            require(step.get('runtime_execution') == 'not-claimed-by-written-example' and step.get('approval_status') == 'candidate', mid + ': writing is not execution')
        require(bool(data.get('candidate_records')), mid + ': no saved candidate record')
        case = SHARED / 'references/method-cases' / (mid + '.md')
        require('../method-case-materials/procedural-supplements/' + mid + '.json' in case.read_text(), mid + ': case does not link full material')
        for src in data['source_inputs']:
            target = (path.parent / src['path']).resolve()
            require(target.is_file() and target.is_relative_to(SHARED.resolve()), mid + ': missing/outside source')
            if 'profile_id' in src:
                projection = reference_projection(profiles[src['profile_id']])
                require(data['reference_rows'] == projection and src['reference_rows_sha256'] == digest(projection), mid + ': reference identity hash')
                forbidden = {'project_scope', 'coverage_status', 'local_roles', 'local_mapping', 'local_object_ids', 'mapping_type', 'applicability', 'gap_action'}
                require(not any(forbidden.intersection(r['reference_attributes']) for r in projection), mid + ': inherited local judgment')
            else:
                require(src['sha256'] == sha(target), mid + ': stale source file')
                hashes[str(target.relative_to(ROOT))] = sha(target)
        if mid in FUNCTION_ROWS:
            prefix, count = FUNCTION_ROWS[mid]
            expected = {prefix + f'{i:02}' for i in range(1, count + 1)}
            actual = [r['reference_id'] for r in data['candidate_records']]
            require(len(actual) == count and set(actual) == expected, mid + ': incomplete/duplicate source row IDs')
            allowed = {'evidenced-in-example', 'planned', 'unknown', 'out-of-scope-with-reason'}
            inputs = {r['id'] for r in data['fictional_input_records']}
            for row in data['candidate_records']:
                require(row['coverage_status'] in allowed and row['approval_status'] == 'candidate', mid + ': invalid row status')
                require(set(row['evidence_ids']) <= inputs, mid + ': unbound fictional input ID')
                if row['coverage_status'] in {'evidenced-in-example', 'planned'}:
                    require(bool(row['evidence_ids']), mid + ': non-unknown state without authored input')
                if row['coverage_status'] == 'planned':
                    require(all(row.get(f) for f in ('plan_owner', 'plan_date', 'plan_acceptance')), mid + ': incomplete plan')
        if 'source_catalog_snapshot' in data:
            source = json.loads((SHARED / 'references/source-tables/government-reference-catalog.json').read_text())
            require(data['source_catalog_snapshot'] == {k: source[k] for k in ('sectors', 'nodes')}, mid + ': incomplete source catalog')
            scopes = data['department_scope']
            require(len(scopes) == 11 and {s['reference_id'] for s in scopes} == {s['id'] for s in source['sectors']}, mid + ': department ledger')
            require({s['reference_id'] for s in scopes if s['scope'] == 'adopted'} == {'G21D-S08', 'G21D-S11'}, mid + ': adopted path identities')
        if mid == 'dbrm-mapping-suite-method':
            source = json.loads((SHARED / 'references/source-tables/dbrm-reference-mappings.json').read_text())
            require(data['source_tables_snapshot'] == source['tables'], mid + ': five raw source tables changed')
            ids = {r['id'] for t in source['tables'] for r in t['rows']}
            overlay = data['local_row_overlays']
            require(len(overlay) == 71 and {r['source_row_id'] for r in overlay} == ids, mid + ': incomplete local overlays')
            element_ids = {e['id'] for d in source['taxonomy'] for e in d['elements']}
            require({r['reference_element_id'] for r in data['candidate_records']} == element_ids, mid + ': ten-element IDs')
            require(data['project_only_additions'][0]['source_identity'] == 'project-only', mid + ': source/project distinction')
        if mid == 'digital-enablement-competency-mapping-method':
            require(len(data['candidate_records']) == 12 and len({r['source_row_id'] for r in data['candidate_records']}) == 12, mid + ': twelve competencies')
        if mid == 'mdm-four-plateau-operations-method':
            require(len(data['candidate_records']) == 4 and len(data['operating_condition_records']) == 20, mid + ': four states/five conditions')
            require('合同' in data['candidate_records'][3]['scope_boundary'] and '交易' in data['candidate_records'][3]['scope_boundary'], mid + ': P3 core boundary missing')
        hashes[str(path.relative_to(ROOT))] = sha(path)
        hashes[str(case.relative_to(ROOT))] = sha(case)
    return {'methods': 19, 'current_steps_with_new_authored_material': 47, 'complete_function_rows': 180,
            'dbrm_source_rows': 71, 'department_scope_rows': 11, 'inputs_sha256': hashes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = {'accepted': False, 'scope': 'current step/source identity, complete rows and authored-input bindings',
              'semantic_approval': 'not-produced', 'blind_agent_execution': 'not-run', 'business_acceptance': 'not-accepted'}
    try:
        result.update(passed=True, **verify())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result.update(passed=False, error=str(exc))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'inputs_sha256'}, ensure_ascii=False))
    return int(not result['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
