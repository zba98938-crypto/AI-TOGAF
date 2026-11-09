"""Evidence-bounded migration calculations under explicitly adopted project rules.

These functions calculate information for decisions, never authority, causal
benefits, production operability, or a standard-prescribed ranking/threshold.
"""
from collections import defaultdict
from decimal import Decimal
from math import isclose
from numeric_contracts import finite_number, stable_id, unique_records

METHOD_IDS = {'dependency-topological-order', 'transition-operability-check',
              'work-package-prioritization', 'benefit-realization-trigger'}


def binding_issues(model, analysis):
    """Check source and object identity when an analysis is used in a model.

    Direct calls deliberately have no model binding and retain that designation
    in replay evidence. Numerical snapshots still need professional freshness
    review; this routine does not claim every free-form observation is derived.
    """
    errors=[]; sources={s['id']:s for s in model.get('sources',[])}
    entities={e['id']:e for e in model.get('entities',[])}
    def issue(code, identity, message):
        errors.append({'level':'error','code':code,'id':analysis['id']+':'+str(identity),'message':message})
    # Evidence paths are checked once by analysis_evidence before dispatch.
    data=analysis.get('inputs',{})
    for row in data.get('work_packages',[]):
        obj=entities.get(row.get('id'))
        if not obj or obj.get('type')!='work_package':
            issue('analysis-model-entity',row.get('id'),'工作包分析须绑定主模型的 work_package。')
    if analysis['method_id']=='transition-operability-check':
        tid=data.get('transition_id')
        if tid not in {s['id'] for s in model.get('states',[])} and not (
            entities.get(tid,{}).get('type') in {'transition','transition_architecture'}):
            issue('analysis-model-entity',tid,'过渡分析须绑定具名状态或过渡架构实体。')
    if analysis['method_id']=='benefit-realization-trigger' and isinstance(data.get('observed'),dict):
        observation=data['observed']
        if observation.get('kind')=='observed' and (model['project'].get('is_example') or any(
                sources.get(sid,{}).get('kind') in {'example','assumption','figure-interpretation','official','local-translation'}
                for sid in observation.get('evidence',[]))):
            issue('analysis-synthetic-observation','observed','虚构项目、假设或标准资料不能冒充真实企业观察。')
    return errors


def number(value, field):
    return finite_number(value, field)


def evidence(value, field):
    if not isinstance(value, list) or not value or any(not isinstance(x, str) or not x.strip() for x in value):
        raise ValueError('missing-evidence:' + field)
    return value


def dependency_order(inputs):
    evidence(inputs.get('rule_evidence'), 'dependency-rule')
    nodes = unique_records(inputs.get('work_packages', []), 'work_packages', nonempty=True)
    ids = [n['id'] for n in nodes]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError('duplicate-or-empty-work-packages')
    for node in nodes:
        evidence(node.get('evidence'), node['id'])
    successors = defaultdict(set); indegree = dict.fromkeys(ids, 0)
    soft = []; seen = set()
    for edge in inputs.get('dependencies', []):
        source, target, kind = edge['source'], edge['target'], edge['kind']
        if source not in indegree or target not in indegree:
            raise ValueError('unknown-dependency-endpoint')
        if kind not in {'hard', 'soft'}:
            raise ValueError('unknown-dependency-kind')
        if (source, target) in seen:
            raise ValueError('duplicate-dependency')
        seen.add((source, target)); evidence(edge.get('evidence'), source + '->' + target)
        if kind == 'soft': soft.append(edge)
        else:
            successors[source].add(target); indegree[target] += 1
    ready = sorted(n for n in ids if indegree[n] == 0)
    batches = []; visited = set()
    while ready:
        batches.append(ready); next_ready = []
        for node in ready:
            visited.add(node)
            for successor in successors[node]:
                indegree[successor] -= 1
                if not indegree[successor]: next_ready.append(successor)
        ready = sorted(next_ready)
    if len(visited) != len(ids):
        raise ValueError('cycle:' + ','.join(sorted(set(ids) - visited)))
    positions = {n: i for i, batch in enumerate(batches) for n in batch}
    return {'batches': batches, 'crossed_soft_edges': [edge for edge in soft
            if positions[edge['source']] >= positions[edge['target']]],
            'rule_evidence': inputs['rule_evidence'],
            'notice': '源端是前置、目标端是后继；批次只满足显式硬依赖，不代表工期、关键路径或资源可行性。'}


def transition_check(inputs):
    evidence(inputs.get('rule_evidence'), 'transition-project-rule')
    stable_id(inputs.get('transition_id'), 'transition_id')
    if not isinstance(inputs.get('conditions'), dict):
        raise ValueError('transition-operability-gap:missing-transition-or-conditions')
    required = {'people', 'systems', 'data', 'controls', 'rollback'}
    conditions = inputs['conditions']; gaps = []
    for key in sorted(required):
        condition = conditions.get(key)
        if not isinstance(condition, dict) or condition.get('status') != 'satisfied':
            gaps.append({'code': 'transition-operability-gap', 'condition': key,
                         'status': (condition or {}).get('status', 'missing') if isinstance(condition, dict) else 'missing'})
            continue
        if not isinstance(condition.get('description'), str) or not condition['description'].strip():
            raise ValueError('transition-operability-gap:missing-description:' + key)
        evidence(condition.get('evidence'), key)
    rollback = inputs.get('rollback', {})
    trigger = rollback.get('trigger', {})
    fields = ('metric', 'operator', 'threshold', 'period', 'consecutive_periods', 'denominator_policy')
    rollback_complete = all(key in trigger for key in fields) and bool(rollback.get('owner')) and bool(rollback.get('verification'))
    if rollback_complete:
        number(trigger['threshold'], 'rollback.threshold')
        if trigger['operator'] not in {'gt', 'ge', 'lt', 'le'} or trigger['denominator_policy'] not in {'unknown-on-zero', 'not-a-ratio'}:
            raise ValueError('measurement-basis-gap:rollback-trigger')
        periods = trigger['consecutive_periods']
        if isinstance(periods, bool) or not isinstance(periods, int) or periods < 1:
            raise ValueError('measurement-basis-gap:rollback-periods')
        evidence(rollback.get('evidence'), 'rollback')
    else:
        gaps.append({'code': 'transition-operability-gap', 'condition': 'rollback-verification', 'status': 'missing'})
    return {'transition_id': inputs['transition_id'], 'document_gate_complete': not gaps,
            'rollback_trigger_structured': rollback_complete, 'gaps': gaps,
            'runtime_operability': 'not-verified', 'business_acceptance': 'not-assessed',
            'notice': '仅判显式项目清单及回退结构是否齐备；不以完成百分比代替条件，不证明实际可运行或回退有效。'}


def prioritize(inputs):
    evidence(inputs.get('rule_evidence'), 'priority-rule')
    criteria = unique_records(inputs.get('criteria', []), 'criteria', nonempty=True)
    options = unique_records(inputs.get('work_packages', []), 'work_packages', nonempty=True)
    weights = {}
    for c in criteria:
        weight = number(c.get('weight'), c['id'] + '.weight')
        evidence(c.get('weight_evidence'), c['id'] + '.weight'); evidence(c.get('scale_evidence'), c['id'] + '.scale')
        lo, hi = number(c.get('min'), c['id'] + '.min'), number(c.get('max'), c['id'] + '.max')
        number(hi - lo, c['id'] + '.range')
        if weight < 0 or lo >= hi or c.get('higher_is_better') is not True:
            raise ValueError('measurement-basis-gap:normalized-preference-scale-required')
        weights[c['id']] = weight
    if not isclose(sum(weights.values()), 1, rel_tol=0, abs_tol=1e-9):
        raise ValueError('measurement-basis-gap:weights-must-sum-to-one')
    preference = {}
    for option in options:
        preference[option['id']] = {}
        for criterion in criteria:
            cid = criterion['id']; value = number(option.get('scores', {}).get(cid), option['id'] + '.' + cid)
            evidence(option.get('score_evidence', {}).get(cid), option['id'] + '.' + cid)
            if not criterion['min'] <= value <= criterion['max']:
                raise ValueError('measurement-basis-gap:score-out-of-scale')
            preference[option['id']][cid] = (value - criterion['min']) / (criterion['max'] - criterion['min'])
    def score(selected_weights):
        values = {identity: sum(values[cid] * w for cid, w in selected_weights.items())
                  for identity, values in preference.items()}
        ranking = sorted(values, key=lambda identity: (-values[identity], identity))
        ties = []
        for identity in ranking:
            if ties and isclose(values[identity], values[ties[-1][0]], rel_tol=1e-12, abs_tol=1e-12): ties[-1].append(identity)
            else: ties.append([identity])
        return {'scores': values, 'ranking': ranking, 'rank_groups': ties}
    sensitivity = inputs.get('sensitivity', {})
    evidence(sensitivity.get('evidence'), 'sensitivity-rule')
    delta = number(sensitivity.get('relative_weight_delta'), 'relative_weight_delta')
    if not 0 < delta < 1:
        raise ValueError('measurement-basis-gap:sensitivity-delta')
    baseline = score(weights); variants = []
    for cid in weights:
        for sign in (-1, 1):
            changed = dict(weights); changed[cid] *= 1 + sign * delta
            total = sum(changed.values()); changed = {key: w / total for key, w in changed.items()}
            variants.append({'criterion_id': cid, 'relative_change': sign * delta,
                             'weights': changed, **score(changed)})
    return {**baseline, 'weights': weights, 'sensitivity': variants,
            'ranking_changed_in_checked_scenarios': any(v['rank_groups'] != baseline['rank_groups'] for v in variants),
            'business_acceptance': 'not-assessed',
            'notice': '仅按有来源的偏好量表归一化计算；成本须先显式转成越高越好的偏好。敏感性仅覆盖列出情景，排名不授权立项。'}


def benefit_trigger(inputs):
    evidence(inputs.get('rule_evidence'), 'benefit-rule')
    observed = inputs.get('observed')
    if observed is None or observed.get('value') is None:
        return {'observation_status': 'not-observed', 'trigger_review': None,
                'notice': '没有观察值，不使用计划或目标代替，也不把未知当零。'}
    if observed.get('kind') not in {'observed', 'simulated-observation'}:
        raise ValueError('measurement-evidence-gap:planned-is-not-observed')
    target, baseline = inputs['target'], inputs['baseline']
    for label, row in [('target', target), ('baseline', baseline), ('observed', observed)]:
        number(row.get('value'), label); evidence(row.get('evidence'), label)
        if not all(row.get(k) for k in ('metric_id', 'unit', 'scope', 'basis', 'period')):
            raise ValueError('measurement-basis-gap:' + label)
    identity = ('metric_id', 'unit', 'scope', 'basis')
    if any(any(row[k] != target[k] for k in identity) for row in (baseline, observed)) or target['period'] != observed['period']:
        raise ValueError('measurement-basis-gap:incomparable-observation')
    if target['value'] <= 0 or baseline['value'] <= 0:
        raise ValueError('measurement-basis-gap:positive-relative-reference-required')
    rule = inputs['trigger']; evidence(rule.get('evidence'), 'trigger-rule')
    threshold = number(rule.get('adverse_deviation_percent'), 'adverse_deviation_percent')
    if threshold < 0 or rule.get('operator') not in {'gt', 'ge'} or rule.get('declared_before_observation') is not True:
        raise ValueError('measurement-basis-gap:trigger-rule')
    direction = inputs.get('direction')
    if direction not in {'minimize', 'maximize'}:
        raise ValueError('measurement-basis-gap:direction')
    # Decimal strings preserve the declared threshold boundary: 0.9 vs 0.6 is
    # exactly +50%, not a binary-float value just above the strict >50% rule.
    t, b, o = (Decimal(str(row['value'])) for row in (target, baseline, observed))
    absolute = o - t; relative = absolute / t * 100
    sign = 1 if direction == 'minimize' else -1
    adverse = sign * relative
    boundary = Decimal(str(threshold))
    return {'observation_status': observed['kind'], 'absolute_deviation': float(absolute),
            'relative_target_deviation_percent': float(relative),
            'baseline_improvement_percent': float(sign * (b - o) / b * 100),
            'meets_numeric_target': sign * absolute <= 0,
            'trigger_review': adverse > boundary if rule['operator'] == 'gt' else adverse >= boundary,
            'business_acceptance': 'not-assessed', 'causal_attribution': 'not-established',
            'notice': '按已声明窗口和同口径计算描述性偏差与条件触发；不是因果收益、长期趋势或正式验收。'}
