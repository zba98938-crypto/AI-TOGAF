"""Fictional worked examples (星河零售) for the 2026-11-05 gap-closure capabilities.

Every example returns (sources, entities, analysis_input_builder). Analysis inputs are
derived from the entities so a model edit and the analysis snapshot cannot drift.
All names, numbers and decisions are invented teaching material, not enterprise facts.
"""

def src(i, text):
    return {'id': i, 'kind': 'example', 'description': text, 'locator': 'raw-materials.json#' + i}

def ent(i, typ, name, ev, **attrs):
    return {'id': i, 'type': typ, 'name': name, 'attributes': attrs, 'evidence': ev, 'certainty': 'assumed'}

def records(entities, typ):
    return [{'id': e['id'], 'name': e['name'], **e['attributes'], 'evidence': e['evidence']} for e in entities if e['type'] == typ]

def roles():
    s = [src('ROLE-R1', '虚构星河零售EA章程：首席架构师统筹，下设企业架构师1名、订单分段架构师1名、门店解决方案架构师1名。'),
         src('ROLE-R2', '人力资源与EA负责人约定：利益相关者满意度目标暂按来源示例3/5记录，尚未批准；交付准时率目标90%已由架构委员会批准。')]
    def kpi(i, measure, target, origin, ev=None):
        k = {'id': i, 'measure': measure, 'target': target, 'target_origin': origin}
        if ev:
            k['evidence'] = ev
        return k
    t = 'guide:architecture-role'
    es = [
        ent('ROLE-CHIEF', t, '首席架构师', ['ROLE-R1'], tier='chief', scope='企业整体战略与运营语境',
            primary_responsibility='为企业期望的战略变革创造有效响应条件', segment_scope='不适用（企业级）',
            activities=['支持业务战略制定', '把战略转为运营模式变更', '对最大、最复杂、风险最高的变更负责'],
            key_stakeholders=['董事会', '高管', '分段架构师'], leads=['ROLE-EA', 'ROLE-SEG', 'ROLE-SOL'],
            kpis=[kpi('KPI-CH-1', '利益相关者满意度', '3/5（来源示例）', 'source-illustrative')]),
        ent('ROLE-EA', t, '企业架构师', ['ROLE-R1'], tier='enterprise', scope='跨多个分段的变革',
            primary_responsibility='为解决方案组件的集成、互操作与治理创造条件', segment_scope='不适用（跨分段）',
            activities=['创建跨分段路线图', '定义塑造全景的原则与政策', '参与架构变更治理'],
            key_stakeholders=['首席架构师', '组合经理', '分段架构师'], leads=['ROLE-SEG', 'ROLE-SOL'],
            kpis=[kpi('KPI-EA-1', '解决方案按约定时间、资源与成本交付并签核的比例', '90%', 'project-adopted', ['ROLE-R2'])]),
        ent('ROLE-SEG', t, '订单分段架构师', ['ROLE-R1'], tier='segment', scope='订单与履约业务分段',
            primary_responsibility='塑造并治理订单分段的系统、子系统与组件', segment_scope='业务域：订单与履约',
            activities=['制定分段演进路线图', '识别分段政策与标准', '支持解决方案架构师'],
            key_stakeholders=['订单业务负责人', '产品负责人', '解决方案架构师'], leads=['ROLE-SOL'],
            kpis=[kpi('KPI-SEG-1', '分段服务达到计划服务水平的比例', '90%', 'project-adopted', ['ROLE-R2'])]),
        ent('ROLE-SOL', t, '门店解决方案架构师', ['ROLE-R1'], tier='solution', scope='门店自提解决方案',
            primary_responsibility='基于特定需求塑造并治理所需解决方案', segment_scope='订单分段内的门店自提',
            activities=['规定服务、流程与技术变更', '为过渡架构建立路线图', '管理变更请求与规格偏差'],
            key_stakeholders=['门店运营', '交付团队', '分段架构师'], leads=[],
            kpis=[kpi('KPI-SOL-1', '解决方案在约定边界内交付并签核', '按项目边界', 'project-adopted', ['ROLE-R2'])])]
    return s, es, lambda m: {'source_ids': [x['id'] for x in s], 'roles': records(m, t)}

def notebook():
    s = [src('SDN-R1', '虚构工作包WP-7“门店自提”：处理差距G-1（无自提预约）；G-2（退货流程）不在本工作包。'),
         src('SDN-R2', '门店运营要求自提预约准确率≥99%（R-ACC），法务要求只显示脱敏手机号（R-PRIV）；风险RK-1为预约超卖。'),
         src('SDN-R3', '规格S-1：预约须通过库存服务锁定；S-2：前台仅读取脱敏视图。控制C-1：锁定失败时禁止确认预约。')]
    t = 'guide:solution-delivery-notebook'
    e = ent('SDN-WP7', t, '解决方案交付笔记本：门店自提', ['SDN-R1', 'SDN-R2', 'SDN-R3'],
            work_package_id='WP-7', solution_concept_ref='v-solution-concept-pickup', implementation_strategy='先在两家门店试点，再分批推广',
            stakeholders=[{'id': 'SH-OPS', 'name': '门店运营', 'requirement_ids': ['R-ACC']}, {'id': 'SH-LEGAL', 'name': '法务', 'requirement_ids': ['R-PRIV']}],
            requirements=[{'id': 'R-ACC', 'statement': '自提预约准确率≥99%', 'stakeholder_ids': ['SH-OPS']},
                          {'id': 'R-PRIV', 'statement': '前台只显示脱敏手机号', 'stakeholder_ids': ['SH-LEGAL']}],
            specifications=[{'id': 'S-1', 'requirement_id': 'R-ACC', 'statement': '预约通过库存服务锁定', 'spec_type': '接口规格', 'applies_to': '自提预约服务'},
                            {'id': 'S-2', 'requirement_id': 'R-PRIV', 'statement': '前台只读脱敏视图', 'spec_type': '数据访问规格', 'applies_to': '门店前台应用'}],
            risks=[{'id': 'RK-1', 'description': '预约超卖导致到店无货'}],
            controls=[{'id': 'C-1', 'risk_id': 'RK-1', 'statement': '锁定失败时禁止确认预约', 'applies_to': '自提预约服务'}],
            gaps=[{'id': 'G-1', 'description': '无自提预约能力', 'in_scope': True}, {'id': 'G-2', 'description': '退货流程未覆盖自提订单', 'in_scope': False}],
            architecture_summary={'business': {'view_ids': ['v-process-pickup']}, 'information': {'view_ids': ['v-data-reservation']},
                                  'application': {'view_ids': ['v-app-communication-pickup']}, 'infrastructure': {'not_applicable_reason': '沿用现有平台，无基础设施变化'},
                                  'security': {'view_ids': ['v-data-security-pickup']}})
    return s, [e], lambda m: {**records(m, t)[0], 'source_ids': [x['id'] for x in s]}

def products():
    s = [src('PCC-R1', '虚构架构定义：订单服务边界含下单与支付确认，产品负责人李某；库存预占只能经库存服务（约束K-1）。'),
         src('PCC-R2', '促销团队待办B-3要求直接写库存表以加快秒杀；B-4同样冲突，但架构委员会已于10月批准临时豁免D-1至2027-01-31。')]
    t = 'guide:product-constraint-register'
    e = ent('PCC-REG', t, '产品边界与约束登记：订单与促销', ['PCC-R1', 'PCC-R2'],
            purpose='登记订单与促销产品的企业约束、冲突待办与阶段G豁免',
            products=[{'id': 'P-ORDER', 'name': '订单服务', 'boundary': '下单与支付确认', 'product_owner': '李某', 'architecture_ref': 'v-app-portfolio', 'evidence': ['PCC-R1']},
                      {'id': 'P-PROMO', 'name': '促销引擎', 'boundary': '价格与券规则', 'product_owner': '王某', 'architecture_ref': 'v-app-portfolio', 'evidence': ['PCC-R1']}],
            constraints=[{'id': 'K-1', 'product_id': 'P-PROMO', 'statement': '库存预占只能经库存服务', 'architecture_ref': 'S-1', 'evidence': ['PCC-R1']}],
            backlog_items=[{'id': 'B-3', 'product_id': 'P-PROMO', 'title': '秒杀直接写库存表', 'conflicts_with': ['K-1']},
                           {'id': 'B-4', 'product_id': 'P-PROMO', 'title': '大促预热直接写库存表', 'conflicts_with': ['K-1'], 'dispensation_id': 'D-1'}],
            dispensations=[{'id': 'D-1', 'constraint_ids': ['K-1'], 'authority': '架构委员会', 'rationale': '库存服务扩容前的临时安排', 'expiry': '2027-01-31', 'evidence': ['PCC-R2']}])
    return s, [e], lambda m: {**{k: v for k, v in records(m, t)[0].items() if k not in ('id', 'evidence')}, 'source_ids': [x['id'] for x in s]}

def domains():
    s = [src('DAA-R1', '虚构EA项目EA-2027：目标OBJ-1缩短履约时长、OBJ-2降低合规风险，共享模型M-1。'),
         src('DAA-R2', '数据领域团队按自建“数据中台项目DP-9”推进，目标为“建设统一数据平台”；安全团队计划单独编写安全架构文档。')]
    t, p = 'guide:domain-architecture', 'guide:ea-project-scope'
    es = [ent('EA-2027', p, 'EA项目EA-2027', ['DAA-R1'], objective_ids=['OBJ-1', 'OBJ-2'], model_id='M-1'),
          ent('DOM-BIZ', t, '业务架构', ['DAA-R1'], kind='business', project_id='EA-2027', objective_ids=['OBJ-1'], shared_entity_ids=['cap-fulfilment']),
          ent('DOM-DATA', t, '数据架构', ['DAA-R2'], kind='data', project_id='DP-9', objective_ids=['OBJ-DP'], shared_entity_ids=[]),
          ent('DOM-SEC', t, '安全架构', ['DAA-R2'], kind='security', project_id='EA-2027', objective_ids=['OBJ-2'], shared_entity_ids=['req-privacy'],
              treated_as='standalone-document', referenced_domain_ids=[])]
    def build(m):
        proj = records(m, p)[0]
        return {'source_ids': [x['id'] for x in s], 'ea_project': {'id': proj['id'], 'objective_ids': proj['objective_ids']}, 'domains': records(m, t)}
    return s, es, build

def incident():
    s = [src('IAA-R1', '虚构事件INC-31：2026-10-18周末订单服务中断6小时，客服记录与监控截图已归档。'),
         src('IAA-R2', '事件前风险委员会接受单次中断<4小时；事件后改为大促期间零中断容忍。目标OBJ-AV：大促期间订单可用。'),
         src('IAA-R3', '方案X：双活改造，估算120万元、9个月，压测与供应商SLA支持其确定性，残余风险仍高于新偏好需购买业务中断保险。')]
    t = 'guide:incident-adjustment'
    e = ent('INC-31-ADJ', t, '事件后的架构调整：订单中断', ['IAA-R1', 'IAA-R2', 'IAA-R3'],
            summary='订单中断后按新风险偏好复议大促可用性目标与相关工作',
            incident={'id': 'INC-31', 'description': '订单服务中断6小时', 'occurred_on': '2026-10-18', 'evidence': ['IAA-R1']},
            objectives=[{'id': 'OBJ-AV', 'statement': '大促期间订单可用'}],
            risk_appetite_before={'statement': '接受单次中断<4小时', 'authority': '风险委员会'},
            risk_appetite_after={'statement': '大促期间零中断容忍', 'authority': '风险委员会'},
            risk_tolerance={'statement': '大促期间中断>15分钟即启动目标复议', 'authority': '风险委员会'},
            requirement_changes=[{'id': 'RC-1', 'objective_id': 'OBJ-AV', 'change': '大促期间可用性要求提高到99.95%', 'impact_assessment_ref': 'RIA-12'}],
            options=[{'id': 'OPT-X', 'kind': 'change-target', 'target_change': '订单服务双活', 'work': '双活改造与切换演练', 'cost': '估算120万元、9个月',
                      'certainty_basis': '压测与供应商SLA', 'residual_vs_appetite': 'exceeds', 'excess_strategy': '转移：购买业务中断保险'},
                     {'id': 'OPT-Y', 'kind': 'cancel-objective', 'consequence': '放弃大促零中断目标，维持事件前偏好'},
                     {'id': 'OPT-Z', 'kind': 'cancel-change', 'consequence': '不改造，接受与新偏好不一致的风险并上报'}],
            decision={'status': 'pending'})
    return s, [e], lambda m: {**{k: v for k, v in records(m, t)[0].items() if k not in ('id', 'name', 'evidence')}, 'source_ids': [x['id'] for x in s]}

def dtra():
    s = [src('DAP-R1', '虚构DTRA问卷汇总（DTRA-2026Q3）：文化4、IT能力5、生态系统5，其余因素6或7；评估在阶段A启动。'),
         src('DAP-R2', '各阶段行动记录：B阶段安排文化变革工作坊；C/D阶段安排伙伴生态评审；D阶段安排平台能力补强；周期结束复评。')]
    ratings = {'vision': 6, 'sponsorship-direction': 7, 'it-capability': 5, 'culture': 4, 'scope-scale': 6, 'business-rationale': 7,
               'implementation-approach': 6, 'business-model-adaptability': 6, 'skills-competence': 6, 'technology-maturity': 6,
               'ecosystem': 5, 'governance-compliance': 6, 'value-realization': 6, 'policy-regulations': 7, 'funding-resources': 6}
    from gap_closure_tables import DTRA_PHASES
    acts = {'B': [{'id': 'ACT-B1', 'factor_ids': ['culture'], 'action': '文化变革工作坊与试点团队'}],
            'C': [{'id': 'ACT-C1', 'factor_ids': ['ecosystem'], 'action': '伙伴数据共享评审'}],
            'D': [{'id': 'ACT-D1', 'factor_ids': ['it-capability'], 'action': '平台能力补强'}, {'id': 'ACT-D2', 'factor_ids': ['ecosystem'], 'action': '伙伴接口技术评审'}]}
    t, r = 'guide:dtra-alignment-summary', 'guide:dtra-phase-record'
    es = [ent('DAP-SUM', t, 'DTRA与ADM对齐汇总', ['DAP-R1'], assessment_ref='DTRA-2026Q3', initiated_in_phase='A', factor_ratings=ratings,
              reassessment='end-of-cycle', progression_note='文化与IT能力补强先于生态系统扩展；生态评审只做准备性工作')]
    for ph, implication, zone in DTRA_PHASES:
        rec = {'phase': ph, 'implication': implication, 'considered_factor_ids': list(zone), 'actions': acts.get(ph, [{'id': 'ACT-' + ph, 'factor_ids': [], 'action': '按表6-1含义记录本阶段考虑'}])}
        if ph == 'Requirements':
            rec['requirement_changes'] = [{'id': 'RQ-1', 'impact_assessment_ref': 'RIA-20', 'target_cycle': 'next'}]
        es.append(ent('DAP-' + ph, r, 'DTRA阶段记录：' + ph, ['DAP-R2'], **rec))
    def build(m):
        summ = records(m, t)[0]
        return {'source_ids': [x['id'] for x in s], 'assessment_ref': summ['assessment_ref'], 'initiated_in_phase': summ['initiated_in_phase'],
                'factor_ratings': summ['factor_ratings'], 'reassessment': summ['reassessment'], 'progression_note': summ['progression_note'],
                'phase_records': records(m, r)}
    return s, es, build

def checklist():
    s = [src('BSC-R1', '虚构星河零售“门店自提”业务场景：前提为“顾客希望当日自提”；发起人为零售副总裁；触发因素为业务需求不清。'),
         src('BSC-R2', '规划会议纪要：指定项目经理赵某、顾问钱某、作者孙某、编辑周某；时间6周、人员4人、预算待定。')]
    t = 'guide:scenario-checklist-stage'
    done = lambda *ev: {'status': 'done', 'evidence': list(ev)}
    premise = {'premise-01': done('BSC-R1'), 'premise-02': done('BSC-R1'), 'premise-03': done('BSC-R1'),
               'premise-04': done('BSC-R1'), 'premise-04a': done('BSC-R1'),
               'premise-05': done('BSC-R1'), 'premise-06': done('BSC-R1'),
               'premise-07': {'status': 'open', 'owner': '钱某', 'action': '联系两家物流供方'}, 'premise-08': done('BSC-R1')}
    plan = {'plan-01': done('BSC-R2'), 'plan-02': done('BSC-R2'), 'plan-03': done('BSC-R2'),
            'plan-04': done('BSC-R2'), 'plan-04a': done('BSC-R2'), 'plan-04b': done('BSC-R2'),
            'plan-04c': {'status': 'open', 'owner': '赵某', 'action': '确认预算'}}
    roles = [{'id': 'RA-' + str(i), 'role_id': rid, 'person': p, 'assigned_in_stage': 'plan', 'evidence': ['BSC-R2']}
             for i, (rid, p) in enumerate([('project-manager', '赵某'), ('business-scenario-consultant', '钱某'),
                                          ('business-scenario-author', '孙某'), ('business-scenario-editor', '周某')], 1)]
    es = [ent('BSC-PREMISE', t, '清单：前提形成', ['BSC-R1'], stage='premise', responses=premise, uses_workshop=False, role_assignments=[]),
          ent('BSC-PLAN', t, '清单：规划', ['BSC-R2'], stage='plan', responses=plan, uses_workshop=False, role_assignments=roles)]
    def build(m):
        st = records(m, t)
        return {'source_ids': [x['id'] for x in s], 'stages': [x['stage'] for x in st],
                'responses': {k: v for x in st for k, v in x['responses'].items()},
                'uses_workshop': any(x['uses_workshop'] for x in st), 'role_assignments': [a for x in st for a in x['role_assignments']]}
    return s, es, build

def smart():
    s = [src('SMART-R1', '虚构目标G-UP（类别：提高用户生产率）：门店前台界面一致；业务目标引用BG-3。'),
         src('SMART-R2', '目的O-1：2027-06-30前三类前台设备界面一致，订单录入错误由5%降到4%，负责人UX组；可用性测试支持可行性。')]
    g, o = 'guide:goal', 'guide:smart-objective'
    es = [ent('G-UP', g, '提高门店前台用户生产率', ['SMART-R1'], statement='门店前台用户生产率提高', category='user-productivity', business_goal_ref='BG-3'),
          ent('O-1', o, '一致的前台界面', ['SMART-R2'], goal_id='G-UP', statement='三类前台设备提供一致的订单录入界面', scope='门店前台三类设备',
              measure='订单录入错误率', unit='%', baseline=5, target=4, owner='UX组', action='统一组件库并迁移三类设备',
              realism_rationale='可用性测试显示组件复用可行', realism_evidence=['SMART-R2'], due='2027-06-30'),
          ent('O-2', o, '缩短前台培训时间', ['SMART-R1'], goal_id='G-UP', statement='缩短新员工前台培训时间', scope='新入职门店员工',
              measure='培训时长', unit='小时', baseline='', target=6, owner='培训组', action='', realism_rationale='', realism_evidence=[], due='')]
    return s, es, lambda m: {'source_ids': [x['id'] for x in s], 'goals': records(m, g), 'objectives': records(m, o)}
