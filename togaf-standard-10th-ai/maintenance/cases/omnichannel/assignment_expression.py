"""Case-local configuration subjects and readable artifact rendering.

The shared skills and registry remain read-only. These are project expression
rules, not a TOGAF official template or personnel/assignment authorization.
"""
import copy
import json

ROLE_IDS = ['ROLE-CHIEF', 'ROLE-EA', 'ROLE-SEG', 'ROLE-SOL']
TASK_IDS = ['TASK-CH', 'TASK-EA', 'TASK-SEG', 'TASK-SOL']
EVIDENCE_IDS = ['EVIDENCE-A', 'EVIDENCE-EXPERT']
SUBJECT_IDS = ROLE_IDS + TASK_IDS + ['ASSIGN-A'] + EVIDENCE_IDS
RELATION_IDS = ['CONFIG-'+t for t in TASK_IDS] + ['CONFIG-ASSIGN-TASK', 'CONFIG-EVIDENCE-A', 'CONFIG-EVIDENCE-EXPERT']


def add_configuration_subjects(model, data):
    types = model.setdefault('extensions', {}).setdefault('entity_types', {})
    types.update({'case:architecture-task': '本案例需完成的架构工作，区别于职位和人员分配',
                  'case:person-assignment': '本案例有期间与容量条件的候选人员分配',
                  'case:competence-evidence': '本案例人员观察及其证据状态，不表示认证'})
    entities, relations = [], []
    def add(identity, typ, name, attrs, evidence):
        entities.append(dict(id=identity, type=typ, name=name, attributes=attrs,
                             evidence=copy.deepcopy(evidence), certainty='assumed'))
    def relate(identity, source, target, label):
        relations.append(dict(id=identity, type='traces_to', source=source,
                             target=target, label=label, attributes={},
                             evidence=['CASE-REVIEW'], certainty='assumed'))
    for task in data['tasks']:
        requirements = [r for r in data['requirements'] if r['task_ref'] == task['id']]
        assignments = [a for a in data['assignments'] if task['id'] in a['task_refs']]
        add(task['id'], 'case:architecture-task', task['scope'], {
            'scope': task['scope'], 'decision': task['decision'], 'outcome': task['outcome'],
            'role_refs': task['role_refs'], 'requirement_refs': [r['id'] for r in requirements],
            'required_skill_ids': task['required_skill_ids'], 'workload_hours': task['workload_hours'],
            'configuration_status': '候选配置需补能力、容量与授权证据' if assignments else '人员未配置；期间与容量待明确',
            'assignment_refs': [a['id'] for a in assignments],
        }, task['evidence'])
        for role in task['role_refs']:
            relate('CONFIG-'+task['id'], role, task['id'], '本次工作职责')
    for assignment in data['assignments']:
        review = {
            'person_ref': assignment['person_ref'], 'role_ref': assignment['role_ref'],
            'task_refs': assignment['task_refs'], 'requirement_refs': assignment['requirement_refs'],
            'assessment_refs': assignment['assessment_refs'], 'authority': assignment['authority'],
            'valid_from': assignment['valid_from'], 'valid_until': assignment['valid_until'],
            'available_hours': assignment['available_hours'], 'workload_hours': None,
            'capacity_state': 'unresolved', 'competence_state': 'needs-evidence',
            'approval': 'not-granted', 'support': copy.deepcopy(assignment['support']),
            'period_gap': '12月1日至4日续任/替代与容量待确认；GAP-ASSIGNMENT-PERIOD'
                if model['project']['version'] == '2' else '本次工作量未知，不能认定容量充分',
        }
        add(assignment['id'], 'case:person-assignment', '甲的候选履约架构任务配置', review, assignment['evidence'])
        relate('CONFIG-ASSIGN-TASK', assignment['id'], 'TASK-SOL', '候选承担；未批准')
    for observation in data['assessments']:
        identity = 'EVIDENCE-EXPERT' if observation['person_ref'] == 'PERSON-EXPERT' else 'EVIDENCE-A'
        attrs = {'person_ref': observation['person_ref'], 'observation_ref': observation['id'],
                 'state': observation['assessment_state'], 'current_proficiency': observation['proficiency'],
                 'observed_on': observation['observed_on'], 'behavioral_evidence': copy.deepcopy(observation['behavioral_evidence']),
                 'note': observation['note']}
        if observation.get('prior_claim'): attrs['prior_claim'] = copy.deepcopy(observation['prior_claim'])
        add(identity, 'case:competence-evidence', '专家支持证据未证实' if identity.endswith('EXPERT') else '甲的任务能力证据不足', attrs, observation['evidence'])
        relate('CONFIG-'+identity, 'ASSIGN-A', identity, '支持者证据待审' if identity.endswith('EXPERT') else '任职能力待举证')
    model['entities'].extend(entities)
    model['relationships'].extend(relations)
    return [e['id'] for e in entities], [r['id'] for r in relations]


def table(headers, rows):
    def cell(value):
        if value is None: return '未知'
        if isinstance(value, list): return '<br>'.join(cell(v) for v in value) or '未记录'
        return str(value).replace('|', '\\|').replace('\n', '<br>')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---']*len(headers)) + ' |'] +
                     ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows]) + '\n\n'


def assessment_data(model):
    return next(a for a in model['analyses'] if a['id'] == 'g249-assessment')['inputs']


def configuration_markdown(model, view, artifact, entities, relationships):
    data = assessment_data(model)
    result = view['analysis_results'][0]['result']
    rows = []
    for role in data['roles']:
        tasks = [t for t in data['tasks'] if role['id'] in t['role_refs']]
        assignments = [a for a in data['assignments'] if a['role_ref'] == role['id']]
        rows.append([role['id'], role['name'], role['scope'], [t['id'] for t in tasks],
                     [a['id'] for a in assignments] or ['未配置；人员、期限和容量待明确']])
    s = '# '+view['title']+'\n\n**虚构教学案例；候选配置未获业务批准，不构成人员评级或上线授权。**\n\n'
    s += '这是本案例的任务与人员配置表达。角色、任务、配置和证据对象使用共享模型的稳定 ID；项目目标与实际能力分别记录。\n\n'
    s += '## 角色与工作责任\n\n' + table(['角色 ID', '角色', '工作范围', '任务 ID', '人员配置'], rows)
    s += '## 四项任务与未决条件\n\n' + table(['任务 ID', '负责角色', '需支持的决定', '预期成果', '工作量 / 配置状态'], [
        [t['id'], t['role_refs'], t['decision'], t['outcome'],
         '工作量未知；'+entities[t['id']]['attributes']['configuration_status']] for t in data['tasks']])
    s += '## 任务技能目标\n\n'
    s += '下列3级是虚构项目裁剪目标，不能作为人员已具备能力的证据；原文参考等级另见[技能矩阵](skill-matrix.md)。\n\n'
    s += table(['目标 ID / 任务', '技能', '项目目标 / 量表', '可观察完成条件', '裁剪依据'], [
        [r['id']+' / '+r['task_ref'], r['skill_id'], str(r['proficiency'])+' / '+r['scale_id'],
         r['behavioral_criteria'], r['tailoring_reason']] for r in data['requirements']])
    s += 'TASK-SOL还要求 `optimistic-pessimistic-patterns`：来源定义和项目目标尚未解决，不自动解释为并发控制。\n\n'
    s += '## 人员配置、容量与有效期\n\n'
    s += table(['配置 ID / 人员', '角色与任务', '有效期', '可用时间 / 工作量', '能力与批准状态'], [
        [a['id']+' / '+a['person_ref'], a['role_ref']+' / '+', '.join(a['task_refs']),
         a['valid_from']+' 至 '+a['valid_until'], str(a['available_hours'])+'小时 / 工作量未知',
         '能力证据不足；容量 unresolved；approval not-granted'] for a in data['assignments']])
    s += 'ASSIGN-A的授权说明：'+data['assignments'][0]['authority']+'。经营负责人只委托分析，具体决定人、库存风险接受者和审批机制仍待确认。\n\n'
    if model['project']['version'] == '2':
        s += '**期间缺口 GAP-ASSIGNMENT-PERIOD：ASSIGN-A仅到2026-11-30；离线工作包到2026-12-04。12月1日至4日续任、替代或交接与容量证据缺失，不能自动延长配置。**\n\n'
    s += '专家支持：PERSON-EXPERT拟提供8小时共同评审；工作量和支持能力未证实，不替代甲的能力证据。\n\n'
    s += '## 人员观察与证据缺口\n\n' + table(['证据对象 / 观察 ID', '人员', '当前等级 / 状态', '已有行为证据', '缺口'], [
        [('EVIDENCE-EXPERT' if a['id']=='OBS-EXPERT' else 'EVIDENCE-A')+' / '+a['id'], a['person_ref'],
         '未知 / '+a['assessment_state'],
         [b['criterion']+'：'+('已记录行为' if b['demonstrated'] else '未获证实') for b in a['behavioral_evidence']], a['note']]
        for a in data['assessments']])
    s += '专家原4级仅保留为未证实历史声明；当前不自动降为3级，也不因“专家”称谓确认支持资格。\n\n'
    s += '## 发展行动与复评\n\n' + table(['行动 ID', '人员 / 任务', '行动', '计划复评', '等级变化'], [
        [d['id'], d['person']+' / '+', '.join(d['task_refs']), d['action'], d['reassessment']['due_on']+'；尚无复评结果', 'not-inferred']
        for d in data['development']])
    s += '发展行动可早于工作包结束完成；这不自动解决人员配置后半段的覆盖缺口。\n\n'
    s += '## 待补证据清单\n\n' + table(['缺口 ID', '状态原因', '所需行动'], [[g['id'], g['reason'], g['action']] for g in result['gaps']])
    s += '## 配置关系图\n\n![角色、任务、配置与证据](role-assignment.svg)\n\n'
    s += '独立图片：[role-assignment.png](role-assignment.png)。可编辑源：[SVG](role-assignment.svg)、[Mermaid](role-assignment.mmd)；[共享模型](../model.json)。\n\n'
    s += '箭头表示本案例职责或配置证据追溯；不表示组织汇报、能力达标或批准。完整分析输入与确定性结果保留于[制品 JSON](role-assignment.json)和[分析结果](../role-assessment.json)。\n\n'
    return s


def render_configuration(model, view, profile, layout='adaptive'):
    from profile_render import Drawing
    selected = {e['id']: e for e in model['entities'] if e['id'] in view['entity_ids']}
    rels = [r for r in model['relationships'] if r['id'] in view['relationship_ids']]
    if set(selected) != set(SUBJECT_IDS):
        raise ValueError('F08 role assignment requires four roles, four tasks, ASSIGN-A and two evidence subjects')
    if {r['id'] for r in rels} != set(RELATION_IDS):
        raise ValueError('F08 role assignment requires explicit role-task and assignment-evidence relations')
    local_profile = copy.deepcopy(profile)
    local_profile['template'] = {'separate_detail_ledger': True}
    d = Drawing(view, local_profile, layout)
    d.width = 1590
    d.text(30, 130, '角色责任 → 架构任务；人员配置 → 任务 / 证据。所有配置均未批准。', 18)
    d.text(30, 162, '缺口直接列在主制品；完整字段在伴随记录保留，未把未知当最低等级。', 16)
    y = 215
    for rid, tid in zip(ROLE_IDS, TASK_IDS):
        role_fields = ['scope', 'primary_responsibility']
        task_fields = ['outcome', 'requirement_refs', 'workload_hours', 'configuration_status']
        h = max(d.card_height(selected[rid], 410, role_fields), d.card_height(selected[tid], 520, task_fields))
        d.card(selected[rid], 30, y, 410, h=h, fields=role_fields)
        d.card(selected[tid], 510, y, 520, h=h, fields=task_fields)
        relation = next(r for r in rels if r['source']==rid and r['target']==tid)
        d.line(440, y+h/2, 510, y+h/2, relation=relation)
        y += h + 40
    assignment_fields = ['person_ref', 'valid_from', 'valid_until', 'available_hours', 'workload_hours', 'capacity_state', 'competence_state', 'approval', 'period_gap']
    ay = 215
    ah = d.card(selected['ASSIGN-A'], 1110, ay, 430, fields=assignment_fields, fill='#fff2dc')
    for identity in EVIDENCE_IDS:
        ay += ah + 45
        ah = d.card(selected[identity], 1110, ay, 430,
                    fields=['person_ref', 'observation_ref', 'state', 'current_proficiency', 'note'], fill='#fff1ed')
    assignment_box = d.positions['ASSIGN-A']
    task_box = d.positions['TASK-SOL']
    # Configuration/task connector runs through the column gutter.
    for r in rels:
        if r['id'].startswith('CONFIG-TASK-'): continue
        d.relation_ids.add(r['id'])
        if r['target']=='TASK-SOL':
            x1,y1,w1,h1=assignment_box;x2,y2,w2,h2=task_box
            d.parts.append(f'<g data-relationship-id="{r["id"]}"><path d="M{x1} {y1+h1/2} H1070 V{y2+h2/2} H{x2+w2}" fill="none" stroke="#46647e" stroke-width="2" marker-end="url(#arrow)"/></g>')
    # Evidence is associated by explicitly labelled records, avoiding implied reporting arrows.
    d.edge_register = rels
    svg, report = d.finish(list(selected.values()), rels)
    report['local_expression_contract'] = 'omnichannel-assignment/1'
    report['semantic_subject_counts'] = {'roles':4, 'tasks':4, 'assignments':1, 'evidence_states':2}
    report['business_approval'] = 'not-granted'
    return svg, report


def install():
    """Patch only loaded module functions for this process; no shared file writes."""
    import generate
    import profile_render
    import registry
    original_registry = registry.load
    def local_registry():
        arts, dels, profiles, methods = original_registry()
        profiles = dict(profiles)
        adapted = copy.deepcopy(profiles['architecture-work-assignment-review'])
        adapted.update(entity_types=['guide:architecture-role', 'case:architecture-task', 'case:person-assignment', 'case:competence-evidence'],
                       relationship_types=['traces_to'],
                       local_expression_contract='omnichannel-assignment/1',
                       required_attributes={},
                       structural_requirements={'minimum_entity_types': {'guide:architecture-role':4, 'case:architecture-task':4, 'case:person-assignment':1, 'case:competence-evidence':2}})
        profiles[adapted['id']] = adapted
        return arts, dels, profiles, methods
    registry.load = local_registry
    generate.load_registry = local_registry
    original_md = generate.artifact_markdown
    original_render = profile_render.render_profile
    def markdown(model, view, artifact, entities, relations):
        if view['id'] == 'role-assignment':
            return configuration_markdown(model, view, artifact, entities, relations)
        return original_md(model, view, artifact, entities, relations)
    def render(model, view, profile, layout='adaptive'):
        if view['id'] == 'role-assignment':
            return render_configuration(model, view, profile, layout)
        return original_render(model, view, profile, layout)
    generate.artifact_markdown = markdown
    profile_render.render_profile = render
