"""Independent synthetic probes for explicitly registered work-product checks.

The expected codes below and mutations are authored independently of run_check's
return values. These are engineering fixtures, not adaptations or certification
of historical prose counterexamples, project facts, or professional decisions.
"""
import argparse
import copy
import json
from pathlib import Path
from field_contracts import apply_contract_overlay, resolve_semantics, run_check

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CODES = {
    'field-values': 'field-contract-value',
    'bi-retirement': 'bi-retirement-not-ready',
    'msa-authorization': 'msa-authorization-evidence-gap',
    'sbce-contract': 'sbce-contract-violation',
}


def _value(schema):
    """Small constructive schema subset; unsupported syntax is a real gap.

    Never learns a valid value from validator failures. The positive execution
    independently verifies that the construction satisfies the actual contract.
    """
    if not schema:
        return 'synthetic-fixture-value'
    if 'const' in schema:
        return copy.deepcopy(schema['const'])
    if 'enum' in schema:
        return copy.deepcopy(schema['enum'][0])
    for union in ('anyOf', 'oneOf'):
        if union in schema:
            return _value(schema[union][0])
    kind = schema.get('type')
    if isinstance(kind, list):
        return _value({**schema, 'type': kind[0]})
    if kind == 'string':
        if schema.get('format') == 'date':
            return '2026-01-01'
        if schema.get('format') == 'date-time':
            return '2026-01-01T00:00:00Z'
        if schema.get('pattern') not in (None, r'\S'):
            raise ValueError('unsupported fixture string pattern: ' + schema['pattern'])
        return 'synthetic-fixture-value' + 'x' * schema.get('minLength', 0)
    if kind in ('integer', 'number'):
        number = max(0, schema.get('minimum', 0))
        if 'exclusiveMinimum' in schema:
            number = max(number, schema['exclusiveMinimum'] + 1)
        return number
    if kind == 'boolean':
        return False
    if kind == 'null':
        return None
    if kind == 'array':
        count = schema.get('minItems', 0)
        if count > 1 and schema.get('uniqueItems'):
            raise ValueError('multi-item unique array needs an explicit fixture')
        return [_value(schema.get('items', {})) for _ in range(count)]
    if kind == 'object':
        properties = schema.get('properties', {})
        value = {key: _value(properties.get(key, {})) for key in schema.get('required', [])}
        while len(value) < schema.get('minProperties', 0):
            key = next((key for key in properties if key not in value), None)
            if key is not None:
                value[key] = _value(properties[key])
            elif schema.get('additionalProperties') is False:
                raise ValueError('object needs an explicit fixture')
            else:
                additional = schema.get('additionalProperties', {})
                value[f'fixture-{len(value)}'] = _value(additional if isinstance(additional, dict) else {})
        return value
    raise ValueError('unsupported fixture schema: ' + json.dumps(schema, ensure_ascii=False))


def _entity(wp, kind, identity='synthetic-entity'):
    entity = {'id': identity, 'type': kind, 'name': 'Synthetic engineering probe', 'attributes': {}}
    for field in wp['required_attributes'][kind]:
        if field != 'name':
            entity['attributes'][field] = _value(resolve_semantics(wp, kind, field).get('value_schema'))
    return entity


def _fixtures(wp, spec):
    executor = spec['executor']
    if executor == 'field-values':
        fixtures = []
        for kind in spec['applies_to']['entity_types']:
            fields = wp['required_attributes'][kind]
            if not fields:
                raise ValueError('no required field available for a rejection probe')
            valid = {'entities': [_entity(wp, kind)]}
            invalid = copy.deepcopy(valid)
            field = fields[0]
            if field == 'name':
                del invalid['entities'][0]['name']
                path = '/entities/0/name'
            else:
                del invalid['entities'][0]['attributes'][field]
                path = '/entities/0/attributes/' + field.replace('~', '~0').replace('/', '~1')
            fixtures.append((valid, invalid, path, 'delete-required-field', kind))
        return fixtures
    if executor == 'bi-retirement':
        entity = _entity(wp, 'guide:bi_operating_state')
        entity['attributes'].update({
            'retirement_authorized': True, 'evolution_kind': 'target',
            'legacy_requirement_coverage': {'synthetic-old-use': 'verified'},
            'operating_exit_gate': {'accepted': True, 'authority': 'synthetic-authority',
                                    'evidence_refs': ['synthetic-acceptance-evidence']}})
        valid = {'entities': [entity]}
        invalid = copy.deepcopy(valid)
        invalid['entities'][0]['attributes']['legacy_requirement_coverage']['synthetic-old-use'] = 'unknown'
        return [(valid, invalid, '/entities/0/attributes/legacy_requirement_coverage/synthetic-old-use',
                 'retirement-with-unverified-old-use', entity['type'])]
    if executor == 'msa-authorization':
        entity = _entity(wp, 'ops:msa_governance')
        entity['attributes'].update({'decision_status': 'approved', 'authority': 'synthetic-authority',
                                     'evidence_detail': {'evidence_refs': ['synthetic-decision-evidence']},
                                     'waiver': {'status': 'requested'}})
        valid = {'entities': [entity]}
        invalid = copy.deepcopy(valid)
        del invalid['entities'][0]['attributes']['authority']
        return [(valid, invalid, '/entities/0/attributes/authority',
                 'approved-decision-without-authority', entity['type'])]
    if executor == 'sbce-contract':
        rows = []
        for identity in ('synthetic-A', 'synthetic-B'):
            entity = _entity(wp, 'guide:sbce_iteration', identity)
            entity['attributes'].update({'option_id': identity, 'subsystem': identity, 'iteration': 1,
                                         'status': 'selected', 'evidence_refs': ['synthetic-trial']})
            rows.append(entity)
        constraint = _entity(wp, 'guide:sbce_constraint', 'synthetic-coupling')
        constraint['attributes'].update({'source_option_id': 'synthetic-A', 'target_option_id': 'synthetic-B',
                                         'status': 'satisfied', 'evidence_refs': ['synthetic-trial']})
        valid = {'entities': rows + [constraint]}
        invalid = copy.deepcopy(valid)
        invalid['entities'][2]['attributes']['status'] = 'unknown'
        return [(valid, invalid, '/entities/2/attributes/status',
                 'selected-set-with-unverified-coupling', constraint['type'])]
    raise ValueError('no independent fixture adapter for executor: ' + str(executor))


def run_explicit_counterexamples(caps):
    """Execute every actual WP machine spec; preserve N/A and fixture failures.

    Results contain replayable input models, mutation/registry JSON paths and
    independently fixed expected codes. Method calculators are intentionally out
    of scope; historical narrative examples remain a separate pending review.
    """
    specs, not_applicable, problems = [], [], []
    for wi, wp in enumerate(caps['work_products']):
        machine = [(si, s) for si, s in enumerate(wp.get('check_specs', [])) if s.get('mode') == 'machine']
        if not machine:
            not_applicable.append({'work_product_id': wp['id'], 'status': 'not-applicable',
                                   'professional_review': 'pending', 'reason': 'no machine check_spec'})
        for si, spec in machine:
            row = {'work_product_id': wp['id'], 'check_spec_id': spec['id'],
                   'registry_path': f'capabilities.json#/work_products/{wi}/check_specs/{si}',
                   'executor': spec.get('executor'), 'cases': [], 'status': 'fail'}
            specs.append(row)
            try:
                expected = EXPECTED_CODES[spec['executor']]
                for valid, invalid, path, mutation, kind in _fixtures(wp, spec):
                    valid_result = run_check(spec, copy.deepcopy(valid), wp)
                    invalid_result = run_check(spec, copy.deepcopy(invalid), wp)
                    passed = (valid_result['status'] == 'pass' and invalid_result['status'] == 'fail'
                              and expected in {issue['code'] for issue in invalid_result['issues']})
                    row['cases'].append({'entity_type': kind, 'mutation_path': path, 'mutation': mutation,
                                         'expected_code': expected, 'expected_valid_status': 'pass',
                                         'expected_invalid_status': 'fail', 'valid_input': valid,
                                         'invalid_input': invalid, 'valid_result': valid_result,
                                         'invalid_result': invalid_result, 'status': 'pass' if passed else 'fail'})
                if row['cases'] and all(c['status'] == 'pass' for c in row['cases']):
                    row['status'] = 'pass'
                else:
                    problems.append(f'{wp["id"]}.{spec["id"]}: independent positive/negative expectation failed')
            except (KeyError, ValueError, TypeError) as error:
                row['error'] = str(error)
                problems.append(f'{wp["id"]}.{spec["id"]}: {error}')
    return {'status': 'fail' if problems else ('pass' if specs else 'not-applicable'),
            'specs': specs, 'spec_count': len(specs), 'case_count': sum(len(s['cases']) for s in specs),
            'not_applicable': not_applicable, 'problems': problems, 'acceptance_granted': False,
            'notice': 'Synthetic engineering probes only; no historical narrative or professional acceptance claimed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', default=str(ROOT / 'capabilities.json'))
    parser.add_argument('--out', help='optional replayable JSON report; default prints summary without writing files')
    args = parser.parse_args()
    caps = apply_contract_overlay(json.loads(Path(args.registry).read_text()))
    report = run_explicit_counterexamples(caps)
    if args.out:
        Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'specs'}, ensure_ascii=False, indent=2))
    raise SystemExit(report['status'] == 'fail')


if __name__ == '__main__':
    main()
