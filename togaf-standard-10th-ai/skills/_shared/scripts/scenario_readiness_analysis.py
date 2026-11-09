"""Explicit-rule reviews for G212 §6 (DTRA x ADM) and G176 §9-11 (checklists, roles, SMART).

Checklist accounting and structural SMART checks only. No pass rate, no score threshold
beyond the guide's own "Strongly Agree/Agree" review rule, and no claim that an objective
is realistic or that a stage is approved.
"""
from evidence_analysis import require, unique, sources
from gap_closure_analysis import gap, need, refs_ok, iso
from gap_closure_tables import (DTRA_CATEGORIES, DTRA_PHASES, LIKERT_AGREE, SCENARIO_STAGES,
                                SCENARIO_ROLES, ROLE_ITEMS, GOAL_CATEGORIES)

FACTORS = {f: cat for cat, fs in DTRA_CATEGORIES.items() for f in fs}
PHASES = {p[0]: p for p in DTRA_PHASES}

def dtra_adm_phase_alignment_review(data):
    """Each phase record considers its Figure 6-1 zone factors; low-rated factors get an action or deferral."""
    known = sources(data, 'DAP-001', 'dtra-adm')
    gaps = []
    require(data.get('assessment_ref'), 'DAP-001', 'assessment', 'Reference the DTRA readiness assessment')
    ratings = data.get('factor_ratings', {})
    require(isinstance(ratings, dict) and set(ratings) <= set(FACTORS), 'DAP-002', 'ratings', 'Unknown DTRA factor id')
    for f, v in ratings.items():
        require(isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 7, 'DAP-002', f, 'Rating must be 1-7 (G212 Table A-1)')
    for f in sorted(set(FACTORS) - set(ratings)):
        gap(gaps, 'rating:' + f, 'factor-not-rated', '补充该因素评分或记录未评估原因；不按0或通过处理')
    if data.get('initiated_in_phase') != 'A':
        gap(gaps, 'initiation', 'not-initiated-in-vision', 'G212 §6建议在阶段A启动DTRA；如另有安排须记录理由')
    records = unique(data.get('phase_records', []), 'DAP-003', 'phase_records')
    by_phase, rows, handled = {}, [], set()
    for r in records.values():
        ph = r.get('phase')
        require(ph in PHASES, 'DAP-003', r['id'], 'Unknown phase; use Preliminary, A-H or Requirements')
        require(ph not in by_phase, 'DAP-003', r['id'], 'Duplicate phase record')
        by_phase[ph] = r
        local = []
        need(r, ['implication', 'actions'], local)
        actions = r.get('actions', [])
        require(isinstance(actions, list), 'DAP-004', r['id'], 'Actions must be a list of records')
        for index, action in enumerate(actions):
            action_id = r['id'] + ':action:' + str(index)
            if not isinstance(action, dict):
                gap(local, action_id, 'invalid-action-record', '行动须记录具体内容和所处理的因素；空值或状态不能替代行动。')
                continue
            factor_ids = action.get('factor_ids', [])
            require(isinstance(factor_ids, list) and all(isinstance(f, str) for f in factor_ids)
                    and set(factor_ids) <= set(FACTORS),
                    'DAP-004', action_id, 'Action factor_ids must list known DTRA factors')
            content = action.get('action')
            if not isinstance(content, str) or not content.strip():
                gap(local, action_id, 'action-content-missing', '补充可审阅的具体行动文字；仅列因素ID不能解除弱项处理缺口。')
                continue
            handled.update(factor_ids)
        considered = set(r.get('considered_factor_ids', []))
        require(considered <= set(FACTORS), 'DAP-004', r['id'], 'Unknown considered factor')
        tailored = r.get('tailored_out', {})
        for f in PHASES[ph][2]:
            if f not in considered and not tailored.get(f):
                gap(local, r['id'] + ':' + f, 'zone-factor-not-considered', '图6-1把该因素放在本阶段区域；考虑它或记录裁剪理由（该映射为图示推断）')
        if ph == 'G' and 'governance-compliance' in considered and not r.get('governance_distinction'):
            gap(local, r['id'] + ':governance', 'phase-g-governance-confusion', '说明阶段G治理指实施方法恰当性，区别于C/D的“治理与合规”因素')
        if ph == 'Requirements':
            for c in unique(r.get('requirement_changes', []), 'DAP-005', r['id']).values():
                need(c, ['impact_assessment_ref', 'target_cycle'], local)
                if c.get('target_cycle') not in (None, 'next') and not c.get('timing_reason'):
                    gap(local, c['id'] + ':cycle', 'requirement-change-timing', '表6-1：变更在下一周期相关阶段实施；当期实施须记录理由')
        refs_ok(r.get('evidence'), known, 'DAP-006', r['id'], local)
        rows.append({'phase': ph, 'id': r['id'], 'considered_factor_ids': sorted(considered), 'gaps': local})
        gaps += local
    for ph in PHASES:
        if ph not in by_phase:
            gap(gaps, 'phase:' + ph, 'phase-not-recorded', '记录该阶段的数字采用含义与行动，或记录裁剪理由')
    attention = sorted(f for f, v in ratings.items() if v < LIKERT_AGREE)
    deferrals = data.get('deferred_factors', {})
    require(isinstance(deferrals, dict) and set(deferrals) <= set(FACTORS),
            'DAP-004', 'deferred_factors', 'Deferrals must map known factors to reasons')
    deferred = {factor for factor, reason in deferrals.items()
                if isinstance(reason, str) and reason.strip()}
    for f in attention:
        if f not in handled and f not in deferred:
            gap(gaps, 'attention:' + f, 'low-rated-factor-unaddressed', '评分低于“同意”需复核；安排行动或记录有理由的延后')
    weak_foundation = [f for f in attention if FACTORS[f] == 'foundational']
    advanced = sorted(f for f in handled if FACTORS.get(f) in ('impact', 'sustaining'))
    if weak_foundation and advanced and not data.get('progression_note'):
        gap(gaps, 'progression', 'foundational-not-met-first', '基础因素未满足时评估影响与持续因素无意义；说明递进安排')
    if data.get('reassessment') not in ('end-of-cycle', 'next-vision'):
        gap(gaps, 'reassessment', 'no-reassessment-point', '指定在周期结束或下一周期愿景阶段重新评估')
    return {'rows': rows, 'attention_factor_ids': attention, 'weak_foundational_factor_ids': weak_foundation,
            'gaps': gaps, 'notice': '阶段-因素区域来自图6-1的同区位置推断；评分低于“同意”只触发复核，不是不合格判定。'}

def _stage_index():
    out = {}
    for st in SCENARIO_STAGES:
        for it in st['items']:
            item_id, text, kind, children = it[:4]
            cond = it[4] if len(it) > 4 else None
            out[item_id] = {'stage': st['id'], 'kind': kind, 'children': [c[0] for c in children], 'condition': cond, 'text': text}
            for c in children:
                out[c[0]] = {'stage': st['id'], 'kind': 'child', 'parent': item_id, 'condition': cond, 'text': c[1]}
    return out

def _response_ok(resp, known, ident, gaps):
    status = resp.get('status')
    require(status in ('done', 'not-applicable', 'open'), 'BSC-002', ident, 'status must be done, not-applicable or open')
    if status == 'done':
        refs_ok(resp.get('evidence'), known, 'BSC-003', ident, gaps)
    elif status == 'not-applicable':
        need({'id': ident, **resp}, ['reason'], gaps)
    else:
        need({'id': ident, **resp}, ['owner', 'action'], gaps)
    return status

def business_scenario_checklist_review(data):
    """G176 §11 checklists per stage, with §10 roles staffed in the Plan step."""
    known = sources(data, 'BSC-001', 'checklist')
    index = _stage_index(); stages = {s['id'] for s in SCENARIO_STAGES}
    selected = data.get('stages') or sorted(stages)
    require(set(selected) <= stages, 'BSC-001', 'stages', 'Unknown stage')
    responses = data.get('responses', {})
    require(set(responses) <= set(index), 'BSC-001', 'responses', 'Response for unknown checklist item')
    workshop = bool(data.get('uses_workshop'))
    rows, gaps, open_items = [], [], []
    for item_id, meta in index.items():
        if meta['stage'] not in selected or meta['kind'] == 'child':
            continue
        if meta['condition'] == 'workshop' and not workshop:
            rows.append({'id': item_id, 'state': 'condition-not-met'}); continue
        resp = responses.get(item_id)
        if resp is None:
            open_items.append(item_id); rows.append({'id': item_id, 'state': 'unreviewed'}); continue
        state = _response_ok(resp, known, item_id, gaps)
        child_states = {c: _response_ok(responses[c], known, c, gaps) if c in responses else 'unreviewed' for c in meta['children']}
        if state == 'done' and meta['kind'] == 'any-of' and 'done' not in child_states.values():
            gap(gaps, item_id, 'any-of-without-child', '至少一个子项须有证据完成')
        if state == 'done' and meta['kind'] == 'all-of' and any(s not in ('done', 'not-applicable') for s in child_states.values()):
            gap(gaps, item_id, 'all-of-incomplete', '每个子项须完成或说明不适用')
        if state != 'done':
            open_items.append(item_id)
        rows.append({'id': item_id, 'state': state, 'children': child_states})
    roles = {r[0] for r in SCENARIO_ROLES}
    assignments = unique(data.get('role_assignments', []), 'BSC-004', 'role_assignments')
    staffed = {}
    for a in assignments.values():
        require(a.get('role_id') in roles, 'BSC-004', a['id'], 'Unknown G176 §10 role')
        need(a, ['person', 'assigned_in_stage'], gaps)
        refs_ok(a.get('evidence'), known, 'BSC-004', a['id'], gaps)
        staffed.setdefault(a['role_id'], []).append(a)
    if 'plan' in selected:
        for item_id, role in ROLE_ITEMS.items():
            if not any(x.get('assigned_in_stage') == 'plan' for x in staffed.get(role, [])):
                gap(gaps, 'role:' + role, 'role-not-staffed-in-plan', 'G176 §10/§11：' + role + '应在规划步骤指定')
            if (responses.get(item_id) or {}).get('status') == 'done' and role not in staffed:
                gap(gaps, item_id + ':role', 'checklist-role-mismatch', '清单标记已指定，但没有对应角色分配记录')
    return {'rows': rows, 'open_item_ids': sorted(open_items), 'staffed_role_ids': sorted(staffed),
            'unstaffed_role_ids': sorted(roles - set(staffed)), 'gaps': gaps,
            'notice': '逐项记录清单完成情况；不计算完成率，不表示业务场景已被接受。一人可担任多个角色。'}

def smart_objective_review(data):
    """G176 §9: each objective is checked against S/M/A/R/T structure and traced to a goal."""
    known = sources(data, 'SMART-001', 'objectives')
    cats = {c[0] for c in GOAL_CATEGORIES}
    goals = unique(data.get('goals', []), 'SMART-001', 'goals')
    objectives = unique(data.get('objectives', []), 'SMART-001', 'objectives')
    require(objectives, 'SMART-001', 'objectives', 'At least one objective is required')
    rows, gaps = [], []
    for g in goals.values():
        need(g, ['statement', 'business_goal_ref'], gaps)
        if g.get('category') not in cats and not g.get('organization_category'):
            gap(gaps, g['id'] + ':category', 'goal-category-unclassified', '使用G176 §9.3的13类之一，或记录组织自定类别')
    for o in objectives.values():
        require(o.get('goal_id') in goals, 'SMART-002', o['id'], 'Objective must trace to a registered goal')
        local, crit = [], {}
        need(o, ['statement'], local)
        crit['specific'] = present_all(o, ['statement', 'scope'])
        crit['measurable'] = present_all(o, ['measure', 'unit', 'target'])
        if crit['measurable'] and o.get('baseline') in (None, ''):
            gap(local, o['id'] + ':baseline', 'no-baseline', '有目标但无基线，无法判断改进幅度')
        crit['actionable'] = present_all(o, ['owner', 'action'])
        crit['realistic'] = present_all(o, ['realism_rationale']) and bool(o.get('realism_evidence'))
        if o.get('realism_evidence'):
            refs_ok(o['realism_evidence'], known, 'SMART-003', o['id'], local)
        crit['time-bound'] = bool(o.get('due'))
        if o.get('due'):
            iso(o['due'], 'SMART-004', o['id'])
        for k, ok in crit.items():
            if not ok:
                gap(local, o['id'] + ':' + k, 'smart-' + k + '-missing', '按G176 §9.2补充该维度的具体内容')
        rows.append({'id': o['id'], 'goal_id': o['goal_id'], 'criteria': crit,
                     'state': 'structurally-smart-awaiting-review' if all(crit.values()) and not local else 'needs-input', 'gaps': local})
        gaps += local
    return {'rows': rows, 'gaps': gaps, 'notice': 'SMART只检查五个维度是否有可核对内容；现实性与数值是否合理由责任人判断。'}

def present_all(record, fields):
    return all(record.get(f) not in (None, '', [], {}) for f in fields)
