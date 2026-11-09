"""Explicit-rule reviews for G249 §4, G186 Appendix D and G186 §12.

Checks are project operating contracts derived from the guides' statements. They check
structure, traceability and declared evidence; they never judge professional adequacy,
grant approval, invent targets, or infer causation.
"""
from datetime import date
from evidence_analysis import require, unique, evidence, sources
from gap_closure_tables import ROLE_TIERS

def present(value):
    return value not in (None, '', [], {})

def gap(gaps, ident, reason, action):
    gaps.append({'id': ident, 'reason': reason, 'action': action})

def need(record, fields, gaps, ident=None):
    for field in fields:
        if not present(record.get(field)):
            gap(gaps, (ident or record.get('id', '?')) + ':' + field, 'missing-input',
                '由责任人补充来源与值；不把未知填为通过或零')

def refs_ok(refs, known, code, ident, gaps):
    if not refs:
        gap(gaps, ident + ':evidence', 'missing-evidence', '补充事实或项目规则证据')
    else:
        evidence(refs, known, code, ident)

def iso(value, code, ident):
    require(isinstance(value, str), code, ident, 'ISO date required')
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValueError(code + ' [' + ident + ']: invalid ISO date')

def architecture_role_catalog_review(data):
    """Review typed, scoped role relationships; hierarchy is an optional project policy."""
    known = sources(data, 'ROLE-001', 'roles')
    roles = unique(data.get('roles', []), 'ROLE-001', 'roles')
    require(roles, 'ROLE-001', 'roles', 'At least one architecture role is required')
    rows, gaps, relationships = [], [], []
    relation_types = {'architecture_guidance', 'architecture_constraint', 'specialization',
                      'collaborates_with', 'reports_to', 'handoff'}
    policy = data.get('hierarchy_policy')
    if policy:
        require(isinstance(policy, dict) and policy.get('mode') == 'strict-tier'
                and policy.get('origin') == 'project-adopted', 'ROLE-POLICY', 'hierarchy_policy',
                'Strict hierarchy requires an explicitly adopted project policy')
        evidence(policy.get('evidence'), known, 'ROLE-POLICY', 'hierarchy_policy')
        order = policy.get('tier_order')
        require(isinstance(order, list) and len(order) == len(set(order)) and set(order) == set(ROLE_TIERS),
                'ROLE-POLICY', 'hierarchy_policy', 'Declare every role category once in tier_order')
        require(policy.get('applies_to') == ['architecture_guidance'], 'ROLE-POLICY', 'hierarchy_policy',
                'Tier ordering can constrain adopted professional guidance only; other relationship types have separate semantics')
    as_of = iso(data['as_of'], 'ROLE-DATE', 'as_of') if data.get('as_of') else None
    for r in roles.values():
        ident, local = r['id'], []
        require(r.get('tier') in ROLE_TIERS, 'ROLE-002', ident, 'tier must be chief/enterprise/segment/solution/specialist')
        need(r, ['name', 'scope', 'primary_responsibility', 'activities', 'key_stakeholders', 'kpis'], local)
        if r['tier'] == 'segment':
            need(r, ['segment_scope'], local)
        for target in r.get('leads', []):
            require(target in roles, 'ROLE-003', ident, 'leads references an unknown role: ' + str(target))
            gap(local, ident + ':leads:' + target, 'untyped-legacy-lead',
                '旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。')
        for rel in unique(r.get('relationships', []), 'ROLE-REL', ident).values():
            target, kind = rel.get('target'), rel.get('type')
            require(target in roles and target != ident, 'ROLE-REL', rel['id'], 'Relationship target must be another declared role')
            require(kind in relation_types, 'ROLE-REL', rel['id'], 'Unknown role relationship semantics')
            need(rel, ['scope'], local)
            refs_ok(rel.get('evidence'), known, 'ROLE-005', rel['id'], local)
            if kind == 'reports_to':
                need(rel, ['authority', 'valid_from', 'valid_until'], local)
            if kind == 'handoff':
                need(rel, ['deliverable_ref', 'acceptance_criteria', 'authority'], local)
            start = iso(rel['valid_from'], 'ROLE-DATE', rel['id']) if rel.get('valid_from') else None
            end = iso(rel['valid_until'], 'ROLE-DATE', rel['id']) if rel.get('valid_until') else None
            require(not (start and end) or start <= end, 'ROLE-DATE', rel['id'], 'Relationship validity dates are inverted')
            if as_of and ((start and as_of < start) or (end and as_of > end)):
                gap(local, rel['id'] + ':period', 'outside-validity-period', '关系不在本次有效期间；需重新确认。')
            if policy and kind in policy['applies_to']:
                require(policy['tier_order'].index(roles[target]['tier']) > policy['tier_order'].index(r['tier']),
                        'ROLE-POLICY', rel['id'], 'Relationship violates the explicitly adopted project hierarchy, not a universal G249 rule')
            relationships.append({'source': ident, **rel})
        for assignment in unique(r.get('assignments', []), 'ROLE-ASSIGN', ident).values():
            need(assignment, ['person_ref', 'job_ref', 'task_refs', 'authority', 'valid_from', 'valid_until'], local)
            refs_ok(assignment.get('evidence'), known, 'ROLE-005', assignment['id'], local)
            start = iso(assignment['valid_from'], 'ROLE-DATE', assignment['id']) if assignment.get('valid_from') else None
            end = iso(assignment['valid_until'], 'ROLE-DATE', assignment['id']) if assignment.get('valid_until') else None
            require(not (start and end) or start <= end, 'ROLE-DATE', assignment['id'], 'Assignment validity dates are inverted')
            if as_of and ((start and as_of < start) or (end and as_of > end)):
                gap(local, assignment['id'] + ':period', 'outside-validity-period', '人员任务分配不在本次有效期间，不能视为当前授权。')
        for k in unique(r.get('kpis', []), 'ROLE-004', ident + ':kpis').values():
            need(k, ['measure', 'target', 'target_origin'], local)
            origin = k.get('target_origin')
            require(origin in (None, 'project-adopted', 'source-illustrative'), 'ROLE-004', k['id'],
                    'target_origin must be project-adopted or source-illustrative')
            if origin == 'source-illustrative':
                gap(local, k['id'] + ':target', 'kpi-target-not-adopted',
                    '来源的3/5或（xxx）四分位仅是示例；由企业设定并批准自己的目标值')
            if origin == 'project-adopted':
                require('xxx' not in str(k.get('target', '')).lower(), 'ROLE-004', k['id'],
                        'Placeholder quartile cannot be an adopted target')
                refs_ok(k.get('evidence'), known, 'ROLE-005', k['id'], local)
            need(k, ['unit', 'measurement_period', 'measurement_source', 'owner', 'formula_or_rule'], local)
            if origin == 'project-adopted':
                need(k, ['adopted_by'], local)
        refs_ok(r.get('evidence'), known, 'ROLE-005', ident, local)
        rows.append({'id': ident, 'tier': r['tier'], 'leads': sorted(r.get('leads', [])),
                     'relationships': r.get('relationships', []), 'assignments': r.get('assignments', []),
                     'state': 'needs-input' if local else 'defined-awaiting-hr-and-governance-review', 'gaps': local})
        gaps += local
    present_tiers = {r['tier'] for r in roles.values()}
    covered = present_tiers | ({'enterprise'} if 'chief' in present_tiers else set())  # chief is a special enterprise architect
    missing = sorted({'enterprise', 'segment', 'solution'} - covered)
    if missing and not data.get('tier_tailoring_reason'):
        gap(gaps, 'tiers', 'fewer-than-three-levels', '标准模型至少区分企业、分段、解决方案三级；裁剪须记录理由：' + ','.join(missing))
    # A declared reporting cycle is structurally contradictory. Collaboration
    # cycles and lateral guidance are meaningful and are deliberately allowed.
    unique(relationships, 'ROLE-REL', 'all-role-relationships')
    reporting = {ident: [] for ident in roles}
    for rel in relationships:
        if rel['type'] == 'reports_to':
            reporting[rel['source']].append(rel['target'])
    visiting, visited = set(), set()
    def walk(ident):
        require(ident not in visiting, 'ROLE-REPORT-CYCLE', ident, 'Organizational reporting cycle')
        if ident in visited:
            return
        visiting.add(ident)
        for target in reporting[ident]:
            walk(target)
        visiting.remove(ident)
        visited.add(ident)
    for ident in roles:
        walk(ident)
    return {'rows': rows, 'relationships': relationships, 'tiers_present': sorted(present_tiers, key=ROLE_TIERS.get), 'gaps': gaps,
            'hierarchy_policy': policy,
            'notice': '角色类别不是通用职级总序；专业指导、约束、特化、协作、汇报与交接分别审查。KPI需口径和采用证据，不评价人员绩效、不替代组织批准。'}

def solution_delivery_notebook_review(data):
    """G186 Table D-1: requirement/specification and risk/control pairs, gap scope, reference summary."""
    known = sources(data, 'SDN-001', 'notebook')
    ident = data.get('id', 'notebook'); gaps = []
    need({**data, 'id': ident}, ['work_package_id', 'solution_concept_ref', 'implementation_strategy'], gaps)
    sh = unique(data.get('stakeholders', []), 'SDN-002', 'stakeholders')
    rq = unique(data.get('requirements', []), 'SDN-002', 'requirements')
    sp = unique(data.get('specifications', []), 'SDN-002', 'specifications')
    rk = unique(data.get('risks', []), 'SDN-002', 'risks')
    ct = unique(data.get('controls', []), 'SDN-002', 'controls')
    gp = unique(data.get('gaps', []), 'SDN-002', 'gaps')
    for s in sh.values():
        need(s, ['name', 'requirement_ids'], gaps)
        for rid in s.get('requirement_ids', []):
            require(rid in rq, 'SDN-003', s['id'], 'Stakeholder references unknown requirement ' + rid)
    for r in rq.values():
        need(r, ['statement', 'stakeholder_ids'], gaps)
        for sid in r.get('stakeholder_ids', []):
            require(sid in sh, 'SDN-003', r['id'], 'Requirement references unknown stakeholder ' + sid)
    for s in sp.values():
        require(s.get('requirement_id') in rq, 'SDN-004', s['id'], 'Every specification must trace to a requirement')
        need(s, ['statement', 'spec_type', 'applies_to'], gaps)
    for c in ct.values():
        require(c.get('risk_id') in rk, 'SDN-005', c['id'], 'Every control must trace to a risk')
        need(c, ['statement', 'applies_to'], gaps)
    pairs = {'requirement_specification': [], 'risk_control': []}
    for r in rq.values():
        mine = sorted(s['id'] for s in sp.values() if s['requirement_id'] == r['id'])
        pairs['requirement_specification'].append({'requirement_id': r['id'], 'specification_ids': mine})
        if not mine:
            gap(gaps, r['id'] + ':specification', 'untestable-requirement', '补充回应该需求的架构规格，否则设计与实施无法据此测试')
    for k in rk.values():
        need(k, ['description'], gaps)
        mine = sorted(c['id'] for c in ct.values() if c['risk_id'] == k['id'])
        pairs['risk_control'].append({'risk_id': k['id'], 'control_ids': mine})
        if not mine:
            treatment = k.get('treatment')
            if treatment in ('accept', 'transfer', 'avoid'):
                refs_ok(k.get('treatment_evidence'), known, 'SDN-006', k['id'], gaps)
            else:
                gap(gaps, k['id'] + ':control', 'uncontrolled-risk', '补充缓解控制，或记录有证据的接受/转移/规避决定')
    for g in gp.values():
        require(isinstance(g.get('in_scope'), bool), 'SDN-007', g['id'], 'Gap must state in_scope true/false')
        need(g, ['description'], gaps)
    if not any(g['in_scope'] for g in gp.values()):
        gap(gaps, ident + ':gaps', 'no-addressed-gap', '列出本工作包处理的差距')
    if not any(not g['in_scope'] for g in gp.values()) and not data.get('out_of_scope_gap_statement'):
        gap(gaps, ident + ':out-of-scope', 'out-of-scope-gaps-not-identified', '标出项目未处理的差距，或记录已核对无此类差距的依据')
    summary = data.get('architecture_summary', {})
    for domain in ('business', 'information', 'application', 'infrastructure', 'security'):
        entry = summary.get(domain, {})
        if not entry.get('view_ids') and not entry.get('not_applicable_reason'):
            gap(gaps, ident + ':summary:' + domain, 'summary-domain-missing', '引用目标架构视图，或说明不适用理由（本节仅供参考）')
    refs_ok(data.get('evidence'), known, 'SDN-006', ident, gaps)
    return {'id': ident, 'pairs': pairs, 'gaps': gaps,
            'in_scope_gap_ids': sorted(g['id'] for g in gp.values() if g['in_scope']),
            'out_of_scope_gap_ids': sorted(g['id'] for g in gp.values() if not g['in_scope']),
            'notice': '配对只证明可追溯结构；规格是否充分、控制是否有效、合同是否签署由治理责任方评审。'}

def product_constraint_conformance_review(data):
    """G186 §12.1: architecture defines products, boundaries and owner constraints; Phase G guards them."""
    known = sources(data, 'PCC-001', 'products')
    products = unique(data.get('products', []), 'PCC-001', 'products')
    constraints = unique(data.get('constraints', []), 'PCC-001', 'constraints')
    items = unique(data.get('backlog_items', []), 'PCC-001', 'backlog_items')
    dispensations = unique(data.get('dispensations', []), 'PCC-001', 'dispensations')
    require(products, 'PCC-001', 'products', 'At least one product is required')
    gaps, findings = [], []
    as_of = iso(data['as_of'], 'PCC-003', 'as_of') if data.get('as_of') else None
    usable_dispensations = set()
    for p in products.values():
        need(p, ['name', 'boundary', 'product_owner', 'architecture_ref'], gaps)
        refs_ok(p.get('evidence'), known, 'PCC-002', p['id'], gaps)
    for c in constraints.values():
        require(c.get('product_id') in products, 'PCC-002', c['id'], 'Constraint must name a registered product')
        need(c, ['statement', 'architecture_ref'], gaps)
        refs_ok(c.get('evidence'), known, 'PCC-002', c['id'], gaps)
    for d in dispensations.values():
        local = []
        need(d, ['constraint_ids', 'authority', 'rationale', 'expiry'], local)
        for field in ('authority', 'rationale'):
            if present(d.get(field)) and (not isinstance(d[field], str) or not d[field].strip()):
                gap(local, d['id'] + ':' + field, 'invalid-dispensation-detail', '权限方和豁免理由必须有可审阅的明确文字。')
        if d.get('expiry'):
            expiry = iso(d['expiry'], 'PCC-003', d['id'])
            if as_of and expiry < as_of:
                gap(local, d['id'] + ':expiry', 'dispensation-expired', '豁免已超过声明的审查日期，需重新取得有效治理决定。')
        if as_of is None:
            gap(local, d['id'] + ':validity', 'dispensation-validity-unknown', '未提供本次审查日期，无法确认豁免当前有效；补充日期并复核前保留约束冲突阻断。')
        refs_ok(d.get('evidence'), known, 'PCC-003', d['id'], local)
        if not local:
            usable_dispensations.add(d['id'])
        gaps += local
    for i in items.values():
        require(i.get('product_id') in products, 'PCC-004', i['id'], 'Backlog item must name a registered product')
        for cid in i.get('conflicts_with', []):
            require(cid in constraints, 'PCC-004', i['id'], 'Unknown constraint ' + cid)
            require(constraints[cid]['product_id'] == i['product_id'], 'PCC-004', i['id'], 'Constraint belongs to another product')
            did = i.get('dispensation_id')
            ok = did in usable_dispensations and cid in dispensations[did].get('constraint_ids', [])
            findings.append({'backlog_item_id': i['id'], 'constraint_id': cid,
                             'state': 'dispensation-recorded' if ok else 'blocked-local-preference',
                             'validity_state': 'current-at-declared-date' if ok else ('unknown-no-as-of' if did in dispensations and as_of is None else 'invalid-or-incomplete'),
                             'meaning': '产品负责人的局部偏好不能越过企业约束；不完整、过期或有效性未知的豁免不能解除阻断' if not ok else '豁免在声明的审查日期有效，仍需在到期前复核'})
    return {'findings': findings, 'blocked_item_ids': sorted({f['backlog_item_id'] for f in findings if f['state'] == 'blocked-local-preference'}),
            'gaps': gaps, 'notice': '检查约束可追溯与豁免记录；不评价产品价值，不替代阶段G治理决定。'}

def domain_architecture_alignment_review(data):
    """G186 §12.2: a domain fits the whole EA; security is a concern referencing other domains."""
    known = sources(data, 'DAA-001', 'domains')
    project = data.get('ea_project') or {}
    require(project.get('id') and project.get('objective_ids'), 'DAA-001', 'ea_project', 'EA project id and objective_ids required')
    domains = unique(data.get('domains', []), 'DAA-001', 'domains')
    require(domains, 'DAA-001', 'domains', 'At least one domain architecture is required')
    rows, gaps = [], []
    for d in domains.values():
        local, findings = [], []
        need(d, ['name', 'kind', 'project_id', 'objective_ids'], local)
        if d.get('project_id') and d['project_id'] != project['id']:
            findings.append('separate-project: 领域架构按另一个项目工作，未融入整体EA')
        unknown = set(d.get('objective_ids', [])) - set(project['objective_ids'])
        if unknown:
            findings.append('divergent-purpose: 目的不在EA项目目标内：' + ','.join(sorted(unknown)))
        if not d.get('shared_entity_ids'):
            gap(local, d['id'] + ':shared-model', 'no-shared-model-reference', '引用共享模型中的对象，避免平行架构')
        if d.get('kind') == 'security':
            if d.get('treated_as') != 'concern' or not d.get('referenced_domain_ids'):
                findings.append('security-standalone: 安全架构只在参照其他域时存在，应作为关注点并引用相关域')
            for ref in d.get('referenced_domain_ids', []):
                require(ref in domains, 'DAA-002', d['id'], 'Security references unknown domain ' + ref)
        refs_ok(d.get('evidence'), known, 'DAA-003', d['id'], local)
        rows.append({'id': d['id'], 'kind': d.get('kind'), 'findings': findings,
                     'state': 'misaligned' if findings else ('needs-input' if local else 'aligned-awaiting-review'), 'gaps': local})
        gaps += local
    return {'rows': rows, 'gaps': gaps, 'notice': '对齐只按声明的项目与目标核对；不评价领域方案质量。'}

def incident_architecture_adjustment_review(data):
    """G186 §12.3: an incident changes risk preference; that is a requirement change with explicit options."""
    known = sources(data, 'IAA-001', 'incident')
    gaps = []
    incident = data.get('incident') or {}
    need({**incident, 'id': incident.get('id', 'incident')}, ['description', 'occurred_on'], gaps)
    require(incident.get('id'), 'IAA-001', 'incident', 'Incident id required')
    refs_ok(incident.get('evidence'), known, 'IAA-001', incident['id'], gaps)
    objectives = unique(data.get('objectives', []), 'IAA-002', 'objectives')
    for key in ('risk_appetite_before', 'risk_appetite_after', 'risk_tolerance'):
        need({'id': key, **(data.get(key) or {})}, ['statement', 'authority'], gaps, key)
    changed = (data.get('risk_appetite_before') or {}).get('statement') != (data.get('risk_appetite_after') or {}).get('statement')
    changes = unique(data.get('requirement_changes', []), 'IAA-003', 'requirement_changes')
    if changed and not changes:
        gap(gaps, 'requirement-changes', 'appetite-change-without-requirement-change', '风险偏好变化是需求变更；登记受影响需求与目标')
    for c in changes.values():
        require(c.get('objective_id') in objectives, 'IAA-003', c['id'], 'Requirement change must name an affected objective')
        need(c, ['change', 'impact_assessment_ref'], gaps)
    options = unique(data.get('options', []), 'IAA-004', 'options')
    kinds = {o.get('kind') for o in options.values()}
    for o in options.values():
        require(o.get('kind') in ('change-target', 'cancel-objective', 'cancel-change'), 'IAA-004', o['id'], 'Unknown option kind')
        if o['kind'] == 'change-target':
            need(o, ['target_change', 'work', 'cost', 'certainty_basis', 'residual_vs_appetite'], gaps)
            if o.get('residual_vs_appetite') == 'exceeds':
                need(o, ['excess_strategy'], gaps)
        else:
            need(o, ['consequence'], gaps)
    if 'change-target' not in kinds:
        gap(gaps, 'options:change-target', 'no-target-change-option', '提出目标与工作变更方案并说明成本与确定性')
    if not {'cancel-objective', 'cancel-change'} <= kinds:
        gap(gaps, 'options:cancellation', 'cancellation-options-not-assessed', '来源提醒可接受成本的变更可能很少；评估取消目标与取消变更两种后果')
    decision = data.get('decision') or {}
    if decision.get('status') == 'decided':
        require(decision.get('option_id') in options, 'IAA-005', 'decision', 'Decision must select a registered option')
        need({'id': 'decision', **decision}, ['authority'], gaps)
        refs_ok(decision.get('evidence'), known, 'IAA-005', 'decision', gaps)
    return {'appetite_changed': changed, 'option_kinds': sorted(k for k in kinds if k),
            'decision_state': decision.get('status', 'pending'), 'gaps': gaps,
            'notice': '把事件后的风险偏好变化当作需求变更处理；不推断事件原因，不代替利益相关者决定。'}
