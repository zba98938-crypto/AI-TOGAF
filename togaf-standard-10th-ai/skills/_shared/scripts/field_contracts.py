"""Validate project field contracts and execute only explicitly bound assertions.

No keyword classification, no inferred professional judgement. Legacy flat
semantics remain readable; scoped semantics override them without aliasing types.
"""
import argparse
import copy
import json
import os
import tempfile
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'schemas/capability-field-contract.schema.json').read_text())
FORMATS = FormatChecker()
OVERLAY_INDEX = ROOT / 'capability-addenda/field-contracts.json'


def _load_packages():
    if not OVERLAY_INDEX.is_file():
        return []
    index = json.loads(OVERLAY_INDEX.read_text())
    return [json.loads((OVERLAY_INDEX.parent / name).read_text()) for name in index['packages']]


OVERLAY_PACKAGES = _load_packages()
OVERLAY_FIELDS = {'entity_attribute_semantics', 'attribute_semantics', 'check_specs',
                  'calculator_id', 'calculator_status', 'calculation_policy',
                  'implementation_status', 'execution_mode', 'professional_review',
                  'structural_check_path', 'review_reference'}


def apply_contract_overlay(caps, packages=None):
    """Pure, idempotent copy-on-write overlay. No file I/O and no input mutation.

    Registered JSON data is read once at module import. Optional packages support
    isolated tests. Only named work_products/analysis_methods and whitelisted
    contract fields may change; no profile, vocabulary or source verification edit.
    A null calculator_id explicitly removes a semantically unrelated binding.
    """
    result = copy.deepcopy(caps)
    for package in OVERLAY_PACKAGES if packages is None else packages:
        for patch in package['patches']:
            group = patch['group']
            updates = patch['set']
            if group not in ('work_products', 'analysis_methods') or not set(updates) <= OVERLAY_FIELDS:
                raise ValueError('overlay禁止越界字段或登记组')
            matches = [item for item in result[group] if item['id'] == patch['id']]
            if len(matches) != 1:
                raise ValueError(f'overlay目标须唯一存在: {group}.{patch["id"]}')
            item = matches[0]
            for key, value in updates.items():
                if key == 'calculator_id' and value is None:
                    item.pop(key, None)
                elif key in ('entity_attribute_semantics', 'attribute_semantics'):
                    target = item.setdefault(key, {})
                    for name, entry in value.items():
                        if key == 'entity_attribute_semantics':
                            target.setdefault(name, {}).update(copy.deepcopy(entry))
                        else:
                            target[name] = copy.deepcopy(entry)
                else:
                    item[key] = copy.deepcopy(value)
    return result


def resolve_semantics(item, entity_type, field):
    scoped = item.get('entity_attribute_semantics', {}).get(entity_type, {})
    return scoped[field] if field in scoped else item.get('attribute_semantics', {}).get(field, {})


def _field_values(model, item, types):
    issues = []
    for entity in model.get('entities', []):
        kind = entity.get('type')
        if kind not in types:
            continue
        attrs = entity.get('attributes') or {}
        for field in item.get('required_attributes', {}).get(kind, []):
            # Name is a first-class model property, not an attributes duplicate.
            value = entity.get('name') if field == 'name' else attrs.get(field)
            sem = resolve_semantics(item, kind, field)
            schema = sem.get('value_schema')
            present = 'name' in entity if field == 'name' else field in attrs
            if not present or (value is None and not schema):
                issues.append({'code': 'field-contract-value', 'id': entity.get('id'),
                               'field': field, 'message': '必填值缺失，不以未知推断通过'})
                continue
            if schema:
                for error in Draft202012Validator(schema, format_checker=FORMATS).iter_errors(value):
                    issues.append({'code': 'field-contract-value', 'id': entity.get('id'),
                                   'field': field, 'message': error.message})
            elif value in ('', [], {}):
                issues.append({'code': 'field-contract-value', 'id': entity.get('id'),
                               'field': field, 'message': '旧式契约必填值为空'})
    return issues


def _bi_retirement(model, item, types):
    issues = []
    for entity in model.get('entities', []):
        if entity.get('type') not in types:
            continue
        attrs = entity.get('attributes') or {}
        if attrs.get('retirement_authorized') is not True:
            continue
        coverage = attrs.get('legacy_requirement_coverage')
        gate = attrs.get('operating_exit_gate')
        # Text evidence cannot prove the gate. Require explicit recorded outcomes.
        if (not isinstance(coverage, dict) or not coverage
                or any(v != 'verified' for v in coverage.values())
                or not isinstance(gate, dict) or gate.get('accepted') is not True
                or not gate.get('evidence_refs') or not gate.get('authority')):
            issues.append({'code': 'bi-retirement-not-ready', 'id': entity.get('id'),
                           'message': '退役须逐旧需求验证且有退出验收、证据与有权责任方；目标态不授予退役'})
    return issues


def _msa_authorization(model, item, types):
    issues = []
    for entity in model.get('entities', []):
        if entity.get('type') not in types:
            continue
        attrs = entity.get('attributes') or {}
        waiver = attrs.get('waiver')
        approved = attrs.get('decision_status') == 'approved'
        waiver_approved = isinstance(waiver, dict) and waiver.get('status') == 'approved'
        if approved and (not attrs.get('authority') or not isinstance(attrs.get('evidence_detail'), dict)
                         or not attrs['evidence_detail'].get('evidence_refs')):
            issues.append({'code': 'msa-authorization-evidence-gap', 'id': entity.get('id'),
                           'message': '已批准治理决定须记录授权主体和结构化决定证据'})
        if waiver_approved and (not waiver.get('authority') or not waiver.get('evidence_refs')
                                or not waiver.get('scope') or not waiver.get('expiry')):
            issues.append({'code': 'msa-authorization-evidence-gap', 'id': entity.get('id'),
                           'message': '批准豁免须范围、期限、授权方与决定证据，申请不等于批准'})
    return issues


def _sbce_contract(model, item, types):
    """Adapt explicitly modelled SBCE rows to the existing qualitative executor.

    Constraint-review evidence is only an execution precondition here, never an
    independent business verdict. Unmodelled coupling stays a professional review.
    """
    from delivery_analysis import review_options
    rows, constraints = [], []
    for entity in model.get('entities', []):
        attrs = dict(entity.get('attributes') or {})
        if entity.get('type') == 'guide:sbce_iteration':
            rows.append(attrs)
        elif entity.get('type') == 'guide:sbce_constraint':
            attrs['id'] = entity.get('id')
            constraints.append(attrs)
    try:
        refs = [ref for constraint in constraints
                for ref in (constraint.get('evidence_refs') or [])]
        review_options({'iterations': rows, 'constraints': constraints,
                        'constraint_review': {'evidence_refs': refs}})
    except (ValueError, KeyError, TypeError) as error:
        return [{'code': 'sbce-contract-violation', 'id': item['id'], 'message': str(error)}]
    return []


EXECUTORS = {
    'field-values': ('field-contract-value', _field_values, None),
    'bi-retirement': ('bi-retirement-not-ready', _bi_retirement, {'guide:bi_operating_state'}),
    'msa-authorization': ('msa-authorization-evidence-gap', _msa_authorization, {'ops:msa_governance'}),
    'sbce-contract': ('sbce-contract-violation', _sbce_contract,
                      {'guide:sbce_iteration', 'guide:sbce_constraint'}),
}


def _spec_problems(spec, item):
    validator = Draft202012Validator(SCHEMA['$defs']['check'])
    problems = [e.message for e in validator.iter_errors(spec)]
    if problems or spec['mode'] != 'machine':
        return problems
    entry = EXECUTORS.get(spec.get('executor'))
    if not entry or not callable(entry[1]):
        return ['未绑定真实执行器']
    if spec.get('code') != entry[0]:
        problems.append('断言码与执行器实际输出不一致')
    types = set(spec['applies_to']['entity_types'])
    if not types <= set(item.get('required_attributes', {})):
        problems.append('适用类型不在本工作产品字段契约内')
    if entry[2] is not None and not types <= entry[2]:
        problems.append('适用类型超出执行器实现范围')
    return problems


def validate_contracts(caps):
    problems = []
    validator = Draft202012Validator(SCHEMA)
    for group in ('work_products', 'analysis_methods'):
        for item in caps.get(group, []):
            identity = item['id']
            for kind, fields in item.get('required_attributes', {}).items():
                for field in fields:
                    sem = resolve_semantics(item, kind, field)
                    if not isinstance(sem, dict):
                        problems.append(f'{identity}.{kind}.{field}: 字段语义须为对象')
                        continue
                    if not all(isinstance(sem.get(k), str) and sem[k].strip()
                               for k in ('meaning', 'value_rule', 'definition_origin')):
                        problems.append(f'{identity}.{kind}.{field}: 缺少含义/取值规则/来源')
                    if field in item.get('entity_attribute_semantics', {}).get(kind, {}):
                        problems.extend(f'{identity}.{kind}.{field}: {e.message}'
                                        for e in validator.iter_errors(sem))
                    schema = sem.get('value_schema')
                    if schema is not None:
                        if not isinstance(schema, dict):
                            problems.append(f'{identity}.{kind}.{field}: value_schema须为对象')
                            continue
                        try:
                            Draft202012Validator.check_schema(schema)
                            if not any(k in schema for k in ('type', 'enum', 'const', 'anyOf', 'oneOf')):
                                problems.append(f'{identity}.{kind}.{field}: 没有有效取值约束')
                        except SchemaError as error:
                            problems.append(f'{identity}.{kind}.{field}: {error.message}')
            specs = item.get('check_specs', [])
            if not isinstance(specs, list) or not all(isinstance(s, dict) for s in specs):
                problems.append(f'{identity}: check_specs须为对象列表')
                continue
            if len({s.get('id') for s in specs}) != len(specs):
                problems.append(f'{identity}: 重复check_specs ID')
            for spec in specs:
                problems.extend(f'{identity}.{spec.get("id")}: {p}' for p in _spec_problems(spec, item))
            for source in ('checks', 'semantic_checks'):
                for text in item.get(source, []):
                    if not any(s.get('text') == text and s.get('source') == source for s in specs):
                        problems.append(f'{identity}: {source}未显式分类: {text}')
    return problems


def run_check(spec, model, item):
    problems = _spec_problems(spec, item)
    if problems:
        raise ValueError('; '.join(problems))
    if spec['mode'] != 'machine':
        return {'status': 'review-required', 'issues': [], 'acceptance_granted': False}
    types = set(spec['applies_to']['entity_types'])
    if not any(e.get('type') in types for e in model.get('entities', [])):
        return {'status': 'not-applicable', 'issues': [], 'acceptance_granted': False}
    issues = EXECUTORS[spec['executor']][1](model, item, types)
    return {'status': 'fail' if issues else 'pass', 'issues': issues, 'acceptance_granted': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', default=str(ROOT / 'capabilities.json'))
    parser.add_argument('--materialize', action='store_true',
                        help='write only contract-overlay fields into this registry; no other files')
    args = parser.parse_args()
    path = Path(args.registry)
    original = path.read_bytes()
    caps = apply_contract_overlay(json.loads(original))
    problems = validate_contracts(caps)
    if args.materialize and not problems:
        # Avoid clobbering a concurrent registry edit, and never invoke the broad
        # addenda merger (which also writes metamodel/artifacts/evidence reports).
        if path.read_bytes() != original:
            raise RuntimeError('registry在物化期间已变化；拒绝覆盖')
        with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, prefix='.field-contract-',
                                         encoding='utf-8', delete=False) as handle:
            json.dump(caps, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
            temporary = handle.name
        if path.read_bytes() != original:
            os.unlink(temporary)
            raise RuntimeError('registry在物化期间已变化；拒绝覆盖')
        os.replace(temporary, path)
    print(json.dumps({'status': 'fail' if problems else 'pass', 'problems': problems,
                      'materialized': bool(args.materialize and not problems),
                      'acceptance_granted': False}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(problems))


if __name__ == '__main__':
    main()
