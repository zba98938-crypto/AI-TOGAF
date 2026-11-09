#!/usr/bin/env python3
"""Case-specific semantic mutations, never an automatic business acceptance engine.

Counterfactual models live only in memory. Existing generated case products are
read-only; only the two reports beside this file are written. The gates encode
the fictional case's stated business handoff and its authored recovery contract.
"""
from pathlib import Path
import copy
import datetime
import hashlib
import json
import runpy
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ns = runpy.run_path(str(HERE / 'run.py'), run_name='semantic_change_review')
from analysis_binding import binding_issues


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def item(rows, identity):
    return next(row for row in rows if row['id'] == identity)


def synchronize_domain(model):
    """Refresh selected domain snapshots; never invent assessment/approval data."""
    data = model['analyses'][0]['inputs']
    selected = {identity for task in data['tasks'] for identity in task['model_object_refs']}
    data['model_objects'] = copy.deepcopy([e for e in model['entities'] if e['id'] in selected])
    data['model_relationships'] = copy.deepcopy([
        r for r in model['relationships'] if r['source'] in selected and r['target'] in selected])
    wanted = {identity for task in data['tasks'] for identity in task['artifact_ids']}
    data['model_views'] = copy.deepcopy([v for v in model['views'] if v['artifact_id'] in wanted])
    item(model['entities'], data['model_binding']['context_ref'])['attributes']['assessment_inputs'] = copy.deepcopy(data)


def business_gate(model):
    """Limited explicit checks, not natural-language policy interpretation."""
    errors = []
    entities = {e['id']: e for e in model['entities']}
    note = entities['DELIVERY-NOTE']['attributes']
    contract = note['recovery_contract']
    receiver = contract['central_receiver_ref']
    interface = contract['interface_ref']
    providers = [r['source'] for r in model['relationships']
                 if r['type'] == 'exposes' and r['target'] == interface]
    if providers != [receiver]:
        errors.append('recovery-provider-contract-mismatch')
    receiver_controls = [c for c in note['controls'] if c['id'] == 'CTRL-CENTRAL-REPLAY']
    if not receiver_controls or not all(receiver in c['applies_to'] and interface in c['applies_to'] for c in receiver_controls):
        errors.append('central-recovery-control-scope-missing')
    local = contract['local_record_ref']
    local_controls = [c for c in note['controls'] if c['id'] == 'CTRL-LOCAL-DURABILITY']
    if not local_controls or not all('APP-STORE' in c['applies_to'] and local in c['applies_to'] for c in local_controls):
        errors.append('local-durability-control-scope-missing')
    if any(r['type'] == 'transitions_to' and r['target'] == 'ORDER-FULFIL'
           and r['source'] != 'ORDER-CONFIRMED' for r in model['relationships']):
        errors.append('unconfirmed-order-to-logistics')
    for task in model['analyses'][0]['inputs']['tasks']:
        assigned_roles = sorted(r['source'] for r in model['relationships']
                                if r['id'] == 'CONFIG-' + task['id'] and r['target'] == task['id'])
        if assigned_roles != sorted(task['role_refs']):
            errors.append('task-responsibility-mismatch:' + task['id'])
    return errors


def unresolved_preserved(model):
    data = model['analyses'][0]['inputs']
    return (model['project']['approval_status'] == 'candidate'
            and item(model['entities'], 'REQ-CONSISTENCY')['attributes']['status'] == 'needs-input'
            and all(task['workload_hours'] is None for task in data['tasks'])
            and all(row['proficiency'] is None for row in data['assessments'])
            and item(model['entities'], 'ASSIGN-A')['attributes']['approval'] == 'not-granted')


def main():
    original = ns['build'](True)
    checks = []
    def check(identity, assertion, action):
        try:
            actual = action()
            checks.append({'id': identity, 'assertion_zh': assertion, 'status': 'passed', 'actual': actual})
        except Exception as exc:
            checks.append({'id': identity, 'assertion_zh': assertion, 'status': 'failed',
                           'actual': {'exception': type(exc).__name__, 'message': str(exc)}})
    def ensure(condition, message):
        if not condition:
            raise AssertionError(message)
    def baseline_gate():
        ensure(not business_gate(original), 'Baseline business gates unexpectedly reject current case')
        ensure(unresolved_preserved(original), 'Baseline lost explicit unknowns')
        return {'explicit_gate_errors': [], 'business_approval': 'not-granted'}
    check('current-case-gates', '当前断连候选的恢复提供者、控制范围、物流交接和任务职责互相一致；真实证据仍未知。', baseline_gate)

    def provider_projection():
        changed = copy.deepcopy(original)
        item(changed['relationships'], 'EX-RESERVE')['source'] = 'APP-STORE'
        before = next(r for r in ns['projections'](original)['catalog'] if r['capability_id'] == 'CAP-RESERVE')
        after = next(r for r in ns['projections'](changed)['catalog'] if r['capability_id'] == 'CAP-RESERVE')
        matrix = next(r for r in ns['projections'](changed)['capability_application_matrix'] if r['capability_id'] == 'CAP-RESERVE')
        ensure(before['application_refs'] == ['APP-STOCK'], 'Unexpected original mapping')
        ensure(after['application_refs'] == matrix['application_ids'] == ['APP-STORE'], 'Provider change did not propagate to catalog and matrix')
        ensure(binding_issues(changed, changed['analyses'][0]), 'Stale analysis snapshots were accepted')
        synchronize_domain(changed)
        ensure(not binding_issues(changed, changed['analyses'][0]), 'Refreshed snapshots remain inconsistent')
        ensure(unresolved_preserved(changed), 'Projection mutation inferred business acceptance or competence')
        return {'relationship': 'EX-RESERVE', 'before_provider': 'APP-STOCK', 'after_provider': 'APP-STORE',
                'catalog_and_matrix': 'changed-with-same-CAP-RESERVE-ID',
                'stale_analysis': 'rejected', 'synchronized_analysis': 'binding-passed',
                'business_disposition': 'hypothetical-rerouting-requires-review-not-approved'}
    check('provider-change-projection-and-stale-analysis', '更改实际提供者关系会改变能力应用映射；过期分析被拒绝，同步只恢复绑定，不批准新设计。', provider_projection)

    def mutation_gate(identity, mutate, expected, description):
        def action():
            changed = copy.deepcopy(original)
            mutate(changed)
            synchronize_domain(changed)
            errors = business_gate(changed)
            ensure(expected in errors, 'Semantic counterexample accepted: ' + expected)
            ensure(unresolved_preserved(changed), 'Counterexample changed unrelated business evidence')
            findings = ns['base'].validate(changed)
            rejected_contracts = [row for row in findings if row['level'] == 'error']
            if expected == 'task-responsibility-mismatch:TASK-SOL':
                ensure(rejected_contracts and all(row['code'] == 'assignment-projection-selection' for row in rejected_contracts),
                       'Responsibility mutation must also be rejected by the general assignment contract')
            else:
                ensure(not rejected_contracts, 'Counterexample has an unrelated validation failure')
            return {'rejected': True, 'business_errors': errors,
                    'structural_findings': findings,
                    'business_approval': 'not-granted', 'mutation_disposition': 'in-memory-only'}
        check(identity, description, action)
    mutation_gate('recovery-provider-conflict',
                  lambda m: item(m['relationships'], 'EX-RECOVERY').update(source='APP-STORE'),
                  'recovery-provider-contract-mismatch',
                  '恢复接口提供者改为门店，但契约中央接收者仍为APP-STOCK，应识别业务边界冲突，不能仅因模型结构有效接受。')
    mutation_gate('missing-local-durability-control',
                  lambda m: item(m['entities'], 'DELIVERY-NOTE')['attributes'].update(
                      controls=[c for c in item(m['entities'], 'DELIVERY-NOTE')['attributes']['controls'] if c['id'] != 'CTRL-LOCAL-DURABILITY']),
                  'local-durability-control-scope-missing',
                  '删除门店持久化控制应暴露数据丢失范围缺口；中央恢复控制不能替代门店控制。')
    mutation_gate('central-control-wrong-scope',
                  lambda m: item(item(m['entities'], 'DELIVERY-NOTE')['attributes']['controls'], 'CTRL-CENTRAL-REPLAY').update(applies_to='APP-STORE / LOCAL-ORDER-RECORD'),
                  'central-recovery-control-scope-missing',
                  '将中央恢复控制范围改成门店记录应暴露中央接收和恢复对账未覆盖。')
    mutation_gate('responsibility-handoff-conflict',
                  lambda m: item(m['relationships'], 'CONFIG-TASK-SOL').update(source='ROLE-CHIEF'),
                  'task-responsibility-mismatch:TASK-SOL',
                  '职责关系改交首席架构师但任务仍要求解决方案角色时，应识别任务—角色语义冲突，不能通过共享ID同步掩盖。')
    mutation_gate('logistics-handoff-semantic-change',
                  lambda m: item(m['relationships'], 'ORDER-TO-FULFIL').update(source='ORDER-PENDING'),
                  'unconfirmed-order-to-logistics',
                  '更改既有交接关系使待确认订单直达物流，应违反原始材料“只使用已确认订单”的约束。')

    def unchanged_dependents():
        changed = copy.deepcopy(original)
        item(changed['entities'], 'IF-RECOVERY')['attributes']['payload'] += '；反事实拟改变：本地受理即库存承诺，等待业务决定'
        impacted = ns['base'].impact(changed, ['IF-RECOVERY'], max_depth=len(changed['entities']))
        affected = {row['id']: row for row in impacted['candidates']}
        required = ['REQ-OFFLINE', 'RISK-STOCK', 'DELIVERY-NOTE', 'WP-OFFLINE', 'TASK-SOL', 'ROLE-SOL', 'DEV-A']
        ensure(set(required) <= affected.keys(), 'Expected explicit dependents are missing from candidate traversal')
        unchanged = [identity for identity in required if item(original['entities'], identity) == item(changed['entities'], identity)]
        ensure(unchanged == required, 'Counterfactual unexpectedly auto-rewrote decisions or risk controls')
        ensure(unresolved_preserved(changed), 'Hypothetical interface policy approved or filled missing evidence')
        return {'changed_semantic_field': 'IF-RECOVERY.attributes.payload',
                'pending_review_objects': [{'id': identity, 'relationship_path': affected[identity]['relationship_path'],
                                            'disposition': 'content-unchanged-needs-human-review'} for identity in required],
                'finding': 'explicit-graph-candidates-found-business-effects-not-auto-resolved',
                'limits': 'Text change classification is authored for this counterfactual; graph reachability does not prove all actual business impact.'}
    check('interface-policy-change-exposes-unchanged-dependents', '拟改变受理/承诺含义时，明确关联的需求、风险、交付契约、工作包、角色、任务和发展仍需逐项复核，不能宣称已自动传播设计。', unchanged_dependents)

    reports = [HERE / 'semantic-change-verification.json', HERE / 'semantic-change-verification.md']
    result = {'schema_version': 'omnichannel-semantic-change-verification/1',
              'generated_at': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),
              'review_kind': 'case-specific-counterfactual-regression',
              'status': 'passed' if all(row['status'] == 'passed' for row in checks) else 'failed',
              'checks': checks, 'business_approval': 'not-granted',
              'input_sha256': {str(p.relative_to(HERE)): digest(p) for p in [HERE / 'run.py', HERE / 'base_build.py', HERE / 'raw-business-materials.md', HERE / 'role-skill-inputs.json', HERE / 'generated/offline-change/model.json']},
              'limits_zh': ['反事实只在内存中运行，没有改变三份教学案例或真实业务事实。',
                            '这些接受门槛是本案例显式编码的业务条件，未推广到共享skills，也不声称能理解任意自然语言政策。',
                            '8项检查通过只证明所列变化与反例；接口业务政策变化的真实影响仍待业务决定与运行证据。',
                            '图可达仅生成候选；库存一致性/恢复目标、工作量/容量、人员能力和授权保持未知。']}
    reports[0].write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    lines = ['# 共享对象与业务语义变更回归', '',
             f"结论：{result['status']}，{sum(row['status'] == 'passed' for row in checks)}/{len(checks)}项。业务批准：未授予。", '',
             '这次直接改变接口提供者、控制范围、职责交接和物流交接关系，并检查过期分析及未复核依赖。反事实只在内存中运行。', '',
             '|检查|结果|实际边界|', '|---|---|---|']
    lines += [f"|{row['id']}|{row['status']}|{row['assertion_zh']}|" for row in checks]
    lines += ['', '接口含义变化的候选排查已涉及需求、风险、交付契约、工作包、角色、任务和发展计划。其原有内容未被自动改写，因此保留逐项业务复核缺口；不会把一致的投影解释为政策正确。', '',
              '完整反例、依赖路径、结构检查和来源指纹见[JSON](semantic-change-verification.json)。', '']
    lines += ['- ' + line for line in result['limits_zh']]
    reports[1].write_text('\n'.join(lines) + '\n')
    print(json.dumps({'status': result['status'], 'checks': len(checks), 'failed': [r['id'] for r in checks if r['status'] == 'failed']}, ensure_ascii=False))
    return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    raise SystemExit(main())
