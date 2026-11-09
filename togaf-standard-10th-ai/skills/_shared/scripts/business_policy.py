"""Check explicitly supplied, project-scoped business policy contracts.

These checks do not infer a policy from TOGAF or from free-text descriptions.
The contract is authored from project material and must name that material's
source ID. Structural model validation remains a separate result.
"""
from pathlib import Path
import argparse
import hashlib
import json


def evaluate_event_batch(contract, events):
    """Evaluate a declared identity-conflict rule on concrete events.

    A repeated key with conflicting identity quarantines *all* records sharing
    that key, irrespective of arrival order. Nonconflicting duplicates are
    idempotent. Charging authorization is deliberately outside this rule.
    """
    rules = [r for r in contract.get('rules', []) if r.get('kind') == 'conflicting-event-identity']
    if len(rules) != 1:
        raise ValueError('事件批次须选择恰好一条 conflicting-event-identity 项目规则。')
    rule = rules[0]
    fields = rule.get('event_fields', {})
    key, identity = fields.get('key'), fields.get('identity')
    if not key or not identity or any(not isinstance(e, dict) or key not in e or identity not in e for e in events):
        raise ValueError('事件缺少契约指定的事件键或身份字段。')
    identities = {}
    for event in events:
        identities.setdefault(event[key], set()).add(event[identity])
    conflicted = {k for k, values in identities.items() if len(values) > 1}
    seen = set()
    decisions = []
    for index, event in enumerate(events):
        pair = (event[key], event[identity])
        if event[key] in conflicted:
            action = 'quarantine'; charge_blocked = True
        elif pair in seen:
            action = 'duplicate-idempotent'; charge_blocked = None
        else:
            action = 'accept-once'; charge_blocked = None
        seen.add(pair)
        decisions.append({'input_index': index, key: event[key], identity: event[identity],
                          'action': action, 'automatic_charge_blocked': charge_blocked})
    return {'rule_id': rule['id'], 'event_count': len(events),
            'conflicting_keys': sorted(conflicted, key=str), 'decisions': decisions,
            'charge_authorization_status': 'unknown-for-nonconflicting-events'}


def compare_event_decisions(expected, observed):
    """Reject a claimed handling result that differs from the rule oracle."""
    problems = []
    actual = observed.get('decisions', []) if isinstance(observed, dict) else []
    wanted = expected['decisions']
    if len(actual) != len(wanted):
        problems.append({'code': 'business-event-count', 'expected': len(wanted), 'actual': len(actual)})
    for index, row in enumerate(wanted):
        if index >= len(actual):
            break
        for field in row:
            if actual[index].get(field) != row[field]:
                problems.append({'code': 'business-event-decision', 'input_index': index,
                                 'field': field, 'expected': row[field], 'actual': actual[index].get(field)})
    if isinstance(observed, dict) and observed.get('conflicting_keys') != expected['conflicting_keys']:
        problems.append({'code': 'business-conflicting-keys',
                         'expected': expected['conflicting_keys'], 'actual': observed.get('conflicting_keys')})
    return problems


def _issue(code, rule_id, message):
    return {'level': 'error', 'code': code, 'id': rule_id, 'message': message}


def check(model, contract, contract_path=None):
    issues = []
    if contract.get('schema_version') != 'project-business-rules/1':
        return [_issue('business-rule-contract', 'contract', '不支持的项目业务规则格式。')]
    if contract.get('project_id') != model.get('project', {}).get('id'):
        issues.append(_issue('business-rule-project', 'contract', '业务规则契约与模型项目 ID 不一致。'))
    sources = {s['id'] for s in model.get('sources', [])}
    entities = {e['id']: e for e in model.get('entities', [])}
    material = contract.get('material', {})
    if contract_path is not None:
        path = (Path(contract_path).resolve().parent / material.get('path', '')).resolve()
        root = Path(contract_path).resolve().parent
        if not material.get('path') or root not in path.parents or not path.is_file():
            issues.append(_issue('business-rule-material', 'contract', '规则原料必须是契约同目录内的现存文件。'))
        elif hashlib.sha256(path.read_bytes()).hexdigest() != material.get('sha256'):
            issues.append(_issue('business-rule-material-stale', 'contract', '规则原料哈希已变化。'))
    for rule in contract.get('rules', []):
        rid = rule.get('id', 'missing-id')
        if not rule.get('source_ids') or not set(rule['source_ids']) <= sources:
            issues.append(_issue('business-rule-source', rid, '规则未引用模型中存在的项目原料来源。'))
        if rule.get('kind') != 'conflicting-event-identity':
            issues.append(_issue('business-rule-kind', rid, '不支持的业务规则类型。'))
            continue
        entity = entities.get(rule.get('entity_id'))
        if entity is None:
            issues.append(_issue('business-rule-entity', rid, '规则目标实体不存在。'))
            continue
        fields = rule.get('event_fields', {})
        key, identity = fields.get('key'), fields.get('identity')
        events = rule.get('example_events', [])
        if not key or not identity or len(events) < 2 or any(key not in e or identity not in e for e in events):
            issues.append(_issue('business-rule-example', rid, '须提供同一事件 ID、不同身份的可核反例。'))
            continue
        conflict = any(a[key] == b[key] and a[identity] != b[identity]
                       for i, a in enumerate(events) for b in events[i + 1:])
        if not conflict:
            issues.append(_issue('business-rule-example', rid, '示例未形成同一事件 ID 的身份冲突。'))
        attr = rule.get('policy_attribute')
        expected = rule.get('expected_action')
        actual = entity.get('attributes', {}).get(attr)
        if not isinstance(expected, str) or not expected or actual != expected:
            issues.append(_issue('business-policy-conflict', rid,
                                 f'{rule.get("entity_id")}.{attr}={actual!r}；项目原料要求 {expected!r}。'))
    return issues


def load_and_check(model, path):
    return check(model, json.loads(Path(path).read_text()), path)


def main():
    parser = argparse.ArgumentParser(description='Evaluate project-scoped event identity conflicts.')
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--events', type=Path, required=True)
    parser.add_argument('--observed', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    from datetime import datetime, timezone
    import uuid
    contract = json.loads(args.contract.read_text())
    events = json.loads(args.events.read_text())
    if contract.get('schema_version') != 'project-business-rules/1' or not isinstance(events, list):
        parser.error('无效契约或事件批次格式。')
    expected = evaluate_event_batch(contract, events)
    problems = compare_event_decisions(expected, json.loads(args.observed.read_text())) if args.observed else []
    result = {'schema_version': 'business-event-evaluation/1', 'run_id': uuid.uuid4().hex,
              'checked_at': datetime.now(timezone.utc).isoformat(),
              'contract_sha256': hashlib.sha256(args.contract.read_bytes()).hexdigest(),
              'events_sha256': hashlib.sha256(args.events.read_bytes()).hexdigest(),
              'observed_sha256': hashlib.sha256(args.observed.read_bytes()).hexdigest() if args.observed else None,
              'expected': expected, 'comparison_problems': problems, 'passed': not problems,
              'limit': '按虚构项目规则核算事件去向；非实际收费、授权或真实企业事实。'}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'run_id': result['run_id'], 'passed': result['passed'], 'problems': len(problems)}, ensure_ascii=False))
    return int(bool(problems))


if __name__ == '__main__':
    raise SystemExit(main())
