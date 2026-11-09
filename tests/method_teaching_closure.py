"""Authored synthetic materials and independent expectations for eight methods.

Inputs are explicit teaching records, not populated from production examples or
calculator output. Each variant changes a business fact or a traceability claim.
"""
import copy


def variant(base, expected, explanation, mutate=None):
    data = copy.deepcopy(base)
    if mutate:
        mutate(data)
    return {'inputs': data, 'expected': expected, 'explanation': explanation}


def role_case():
    roles = []
    for identity, tier, scope in [('EA', 'enterprise', '全渠道预约'), ('SEG', 'segment', '门店履约'), ('SOL', 'solution', '双店预约试点')]:
        roles.append(dict(id=identity, name=scope+'架构角色', tier=tier, scope=scope,
            segment_scope=scope, primary_responsibility='界定'+scope+'的变更与接口责任',
            activities=['维护'+scope+'的接口决定'], key_stakeholders=['运营负责人'], evidence=['MANDATE'],
            kpis=[dict(id=identity+'-KPI', measure='带评审依据的接口决定比例', target=100,
                target_origin='project-adopted', unit='%', measurement_period='2026年11月',
                measurement_source='决定登记册', owner='架构实践负责人', formula_or_rule='有评审依据条数/全部决定条数×100',
                adopted_by='虚构实践负责人', evidence=['KPI-POLICY'])]))
    roles[0]['relationships']=[dict(id='GUIDANCE',type='architecture_guidance',target='SEG',scope='预约接口一致性',evidence=['MANDATE'])]
    roles[1]['assignments']=[dict(id='ASSIGN',person_ref='PERSON-LIN',job_ref='JOB-ANALYST',task_refs=['REVIEW-RESERVATION'],
        authority='虚构实践负责人',valid_from='2026-11-01',valid_until='2026-11-30',evidence=['ASSIGNMENT'])]
    base=dict(source_ids=['MANDATE','KPI-POLICY','ASSIGNMENT'],as_of='2026-11-08',roles=roles)
    return dict(title='预约试点中的角色、指导关系与任期', source='G249 §4、§4.1–4.4',
        decision='林某的分析岗位是否因此成为企业架构管理岗位，以及月底之后能否继续视为当前任务授权？',
        materials=[('MANDATE','企业、履约分段、双店解决方案分别承担接口决定责任；企业角色向分段提供专业指导，没有人事汇报声明。'),
            ('KPI-POLICY','虚构实践负责人采用11月100%决定条目带评审依据的过程目标；它不是人员能力或绩效评级。'),
            ('ASSIGNMENT','林某的岗位为分析师，11月1日至30日承担预约接口审查任务；没有12月续期材料。')],
        reasoning=['专业指导只覆盖预约接口，不推出人事管理关系。','岗位、角色和任务以三个独立引用保存；一条任务分配不构成胜任认证。','目标100%来自本项目材料；不是把G249示例3/5搬成企业目标。','11月8日属于授权期，12月1日不属于；任期变化与角色定义是否齐全分开判断。'],
        scenarios={
            'sufficient':variant(base,{'gap_reasons':[],'row_states':['defined-awaiting-hr-and-governance-review']*3},'字段齐全只允许进入人力与治理评审。'),
            'missing':variant(base,{'gap_ids':['SEG-KPI:measurement_source'],'row_states':['defined-awaiting-hr-and-governance-review','needs-input','defined-awaiting-hr-and-governance-review']},'删除KPI取数来源，不能用目标值代替观察口径。',lambda d:d['roles'][1]['kpis'][0].pop('measurement_source')),
            'change':variant(base,{'gap_ids':['ASSIGN:period']},'复核日改到12月1日，11月任务分配不再是当前授权。',lambda d:d.update(as_of='2026-12-01')),
            'counterexample':variant(base,{'reject':'ROLE-REL'},'把专业指导指向未登记角色，拒绝悬空关系。',lambda d:d['roles'][0]['relationships'][0].update(target='NOT-A-ROLE')),
        })


def notebook_case():
    base=dict(id='NB-PILOT',source_ids=['SCOPE','SPEC','RISK'],evidence=['SCOPE','SPEC','RISK'],work_package_id='WP-PILOT',
        solution_concept_ref='VIEW-RESERVATION',implementation_strategy='先双店试点；中央预占成功才确认预约',
        stakeholders=[dict(id='OPS',name='门店运营',requirement_ids=['REQ-RESERVE'])],
        requirements=[dict(id='REQ-RESERVE',statement='确认前取得中央库存预占凭证',stakeholder_ids=['OPS'])],
        specifications=[dict(id='SPEC-RESERVE',requirement_id='REQ-RESERVE',statement='确认事件引用预占凭证ID',spec_type='事件接口',applies_to='预约服务')],
        risks=[dict(id='RISK-DUP',description='重试重复预占')],
        controls=[dict(id='CTRL-IDEM',risk_id='RISK-DUP',statement='重复请求键只返回同一预占结果',applies_to='预约接口')],
        gaps=[dict(id='GAP-RESERVE',description='当前确认无中央预占',in_scope=True),dict(id='GAP-RETURN',description='自提退货流程未覆盖',in_scope=False)],
        architecture_summary={k:{'view_ids':['VIEW-'+k]} for k in ['business','information','application','security']})
    base['architecture_summary']['infrastructure']={'not_applicable_reason':'沿用已声明的试点平台，本工作包不改变基础设施'}
    return dict(title='预约工作包的需求规格与风险控制配对',source='G186 附录D 表D-1',
        decision='仅有目标架构概念图，能否据此判断重试控制和退货能力已交付？',
        materials=[('SCOPE','工作包只补预约中央预占，不处理自提退货；双店试点后才讨论推广。'),('SPEC','需求是确认前取得预占凭证；事件接口规格必须携带该凭证ID。'),('RISK','重试可能重复预占，候选控制为请求键幂等；尚无控制运行结果。')],
        reasoning=['概念图只解释方案，不能代替可检查的事件规格。','需求与规格、风险与控制分别配对，不能把同一条连线当两种证明。','退货是明确范围外差距，保留后续工作责任。','有控制条目只证明设计已记录；没有运行证据就不能判断重复预占已被消除。'],
        scenarios={
            'sufficient':variant(base,{'gap_reasons':[],'in_scope_gap_ids':['GAP-RESERVE'],'out_of_scope_gap_ids':['GAP-RETURN']},'一项规格与一项控制分别回链需求和风险。'),
            'missing':variant(base,{'gap_reasons':['uncontrolled-risk']},'删除控制且无风险处理决定，保留未受控风险。',lambda d:d.update(controls=[])),
            'change':variant(base,{'in_scope_gap_ids':['GAP-RESERVE','GAP-RETURN'],'out_of_scope_gap_ids':[],'gap_reasons':['out-of-scope-gaps-not-identified']},'将退货纳入工作包后，原范围外说明失效，需重新确认未处理差距。',lambda d:d['gaps'][1].update(in_scope=True)),
            'counterexample':variant(base,{'reject':'SDN-004'},'规格指向不存在的需求必须拒绝。',lambda d:d['specifications'][0].update(requirement_id='REQ-ABSENT')),
        })


def product_case():
    base=dict(source_ids=['ARCH','DISP'],as_of='2026-11-08',products=[dict(id='PROMO',name='促销产品',boundary='促销资格与价格',product_owner='虚构产品负责人',architecture_ref='ARCH-1',evidence=['ARCH'])],
        constraints=[dict(id='K-RESERVE',product_id='PROMO',statement='库存操作必须经过库存服务',architecture_ref='ARCH-1',evidence=['ARCH'])],
        backlog_items=[dict(id='B-DIRECT',product_id='PROMO',title='预热批次绕过库存服务',conflicts_with=['K-RESERVE'],dispensation_id='D-TEMP')],
        dispensations=[dict(id='D-TEMP',constraint_ids=['K-RESERVE'],authority='虚构架构委员会',rationale='限11月预热批次，隔离执行并核对库存差额',expiry='2026-11-30',evidence=['DISP'])])
    return dict(title='促销待办对库存约束的临时豁免',source='G186 §12.1',
        decision='产品负责人能否以大促紧急为由绕过库存服务，缺少豁免权限时能否解除冲突阻断？',
        materials=[('ARCH','促销产品只管理资格和价格；企业架构约束库存写入经库存服务，产品偏好不能自行解除约束。'),('DISP','虚构委员会仅对11月预热批次登记临时安排，理由、权限和到期日分别记录。')],
        reasoning=['待办与约束归属于同一产品；跨产品豁免不能复用。','豁免是阶段G治理材料，记录完整仍不等于真实组织已授权。','权限方、理由、期限及证据构成同一条记录的必要条件，缺字段不能只靠证据ID解除阻断。','业务变更去掉豁免时，原冲突仍然存在；不能把紧急程度当作授权。'],
        scenarios={
            'sufficient':variant(base,{'blocked_item_ids':[],'finding_states':['dispensation-recorded'],'gap_reasons':[]},'本情景完整记录临时豁免；效果与真实授权另行审阅。'),
            'missing':variant(base,{'blocked_item_ids':['B-DIRECT'],'gap_ids':['D-TEMP:authority']},'没有权限方的豁免草稿不能解除约束冲突。',lambda d:d['dispensations'][0].pop('authority')),
            'change':variant(base,{'blocked_item_ids':['B-DIRECT'],'finding_states':['blocked-local-preference']},'撤销临时豁免后，库存约束继续阻断直接写库待办。',lambda d:d.update(dispensations=[])),
            'counterexample':variant(base,{'reject':'PCC-004'},'待办引用不存在的约束应拒绝，不制造空约束。',lambda d:d['backlog_items'][0].update(conflicts_with=['K-ABSENT'])),
        })


def domain_case():
    base=dict(source_ids=['CHARTER','SECURITY'],ea_project=dict(id='EA-PILOT',objective_ids=['OBJ-RESERVE','OBJ-PRIVACY']),domains=[
        dict(id='DOM-APP',name='预约应用',kind='application',project_id='EA-PILOT',objective_ids=['OBJ-RESERVE'],shared_entity_ids=['APP-RESERVE'],evidence=['CHARTER']),
        dict(id='DOM-SEC',name='预约安全关注',kind='security',project_id='EA-PILOT',objective_ids=['OBJ-PRIVACY'],shared_entity_ids=['REQ-MASK'],treated_as='concern',referenced_domain_ids=['DOM-APP'],evidence=['SECURITY'])])
    return dict(title='预约项目的应用域与安全关注点对齐',source='G186 §12.2',decision='安全方案与应用方案是否服务同一项目，独立文档能否替代共享模型和跨域引用？',
        materials=[('CHARTER','EA-PILOT目标为中央预约和隐私保护，应用域引用共享对象APP-RESERVE。'),('SECURITY','手机号脱敏需求REQ-MASK适用于预约应用DOM-APP，安全作为跨域关注点记录。')],
        reasoning=['对齐基于项目ID、目的和共享对象，不以文档标题相同为证。','安全关注指向实际受影响的应用域，不能孤立成与整体EA无关的第二项目。','共享引用缺失时只保留待补，不宣称架构质量不合格。','项目切换是业务范围改变，应明确报出separate-project而非沿用原结论。'],
        scenarios={
            'sufficient':variant(base,{'row_states':['aligned-awaiting-review']*2,'gap_reasons':[]},'共同项目与目标成立；不评价脱敏方案强度。'),
            'missing':variant(base,{'row_states':['needs-input','aligned-awaiting-review'],'gap_reasons':['no-shared-model-reference']},'应用域没有共享对象引用，不能仅靠项目名推断已融入共享模型。',lambda d:d['domains'][0].update(shared_entity_ids=[])),
            'change':variant(base,{'row_states':['misaligned','aligned-awaiting-review']},'应用域转入另一个项目后原整体EA对齐失效。',lambda d:d['domains'][0].update(project_id='EA-OTHER')),
            'counterexample':variant(base,{'reject':'DAA-002'},'安全引用未登记域时拒绝悬空引用。',lambda d:d['domains'][1].update(referenced_domain_ids=['DOM-ABSENT'])),
        })


def incident_case():
    base=dict(source_ids=['INCIDENT','RISK-DECISION','IMPACT'],incident=dict(id='INC-4',description='预约中断40分钟',occurred_on='2026-11-01',evidence=['INCIDENT']),
        objectives=[dict(id='OBJ-RESERVE',statement='试点预约可用')],risk_appetite_before=dict(statement='接受一次60分钟中断',authority='虚构风险委员会'),
        risk_appetite_after=dict(statement='接受一次15分钟中断',authority='虚构风险委员会'),risk_tolerance=dict(statement='超过15分钟即升级复议',authority='虚构风险委员会'),
        requirement_changes=[dict(id='RC-RECOVERY',objective_id='OBJ-RESERVE',change='恢复目标由60分钟改为15分钟',impact_assessment_ref='IMPACT-1')],
        options=[dict(id='OPT-RECOVER',kind='change-target',target_change='自动切换',work='恢复流程及演练',cost='虚构估算20万元',certainty_basis='尚待故障演练验证的方案',residual_vs_appetite='exceeds',excess_strategy='评估转移业务损失并保留服务中断残余风险'),
            dict(id='OPT-CANCEL-GOAL',kind='cancel-objective',consequence='取消试点预约可用性目标，改人工受理'),dict(id='OPT-CANCEL-CHANGE',kind='cancel-change',consequence='保留原系统并上报与新偏好不符的风险')],decision=dict(status='pending'))
    return dict(title='预约中断后的风险偏好变化与三类方案',source='G186 §12.3',decision='40分钟中断后，是否必然选择双活系统，还是需要重审目标、变更与残余风险？',
        materials=[('INCIDENT','事件记录仅确认中断40分钟，根因尚未确认。'),('RISK-DECISION','虚构风险委员会将可接受中断由60分钟调整为15分钟，并规定超出后升级复议。'),('IMPACT','自动切换估算20万元但未演练；取消目标和取消变更分别有业务后果。')],
        reasoning=['观察到中断不等于知道根因，不能直接宣称双活能解决问题。','偏好变化需形成有目标追溯和影响评估的需求变更。','取消目标是改变业务承诺；取消变更是保留现状，两者不可合并为一个“不做”。','保险转移经济后果不会减少服务中断概率；残余服务风险继续由责任方决定。'],
        scenarios={
            'sufficient':variant(base,{'appetite_changed':True,'decision_state':'pending','gap_reasons':[],'option_kinds':['cancel-change','cancel-objective','change-target']},'三类方案记录完整，但没有授权选择。'),
            'missing':variant(base,{'gap_reasons':['appetite-change-without-requirement-change']},'偏好已变而需求变更为空，不能跳到实施方案。',lambda d:d.update(requirement_changes=[])),
            'change':variant(base,{'appetite_changed':False,'decision_state':'pending'},'委员会撤回偏好调整并保持原口径；不因发生事件就强制认定偏好已变。',lambda d:d.update(risk_appetite_after=copy.deepcopy(d['risk_appetite_before']),requirement_changes=[])),
            'counterexample':variant(base,{'reject':'IAA-003'},'需求变更必须指向受影响的已登记目标。',lambda d:d['requirement_changes'][0].update(objective_id='OBJ-ABSENT')),
        })


def dtra_case():
    ratings={k:6 for k in ['vision','sponsorship-direction','it-capability','culture','scope-scale','business-rationale','implementation-approach','business-model-adaptability','skills-competence','technology-maturity','ecosystem','governance-compliance','value-realization','policy-regulations','funding-resources']}
    ratings['culture']=4
    # The selected stage is deliberately A; other phases remain explicit gaps.
    # Sufficient here means sufficient for the A-stage decision, not full-cycle acceptance.
    base=dict(source_ids=['SURVEY','VISION'],assessment_ref='DTRA-PILOT',initiated_in_phase='A',factor_ratings=ratings,reassessment='next-vision',
        phase_records=[dict(id='PHASE-A',phase='A',implication='用就绪度结果裁剪试点愿景与路径',considered_factor_ids=['vision','sponsorship-direction'],
            actions=[dict(id='ACT-CULTURE',factor_ids=['culture'],action='先在两店演练新预约责任，再决定扩围')],evidence=['VISION'])])
    return dict(title='文化就绪度弱项对试点愿景的影响',source='G212 §6、表6-1、图6-1及表A-1',decision='文化因素4分是否等于数字化不合格，空白延后理由能否关闭复核项？',
        materials=[('SURVEY','本次15因素调查中，文化4分、其余6分；量表1至7，6为同意，评分只触发复核。'),('VISION','本轮只审阶段A试点愿景，文化责任演练先行；其余阶段计划未提供，明确保留阶段缺口。')],
        reasoning=['4分低于同意只产生文化因素复核，不推断组织认证失败。','阶段A已有文化行动，满足本次弱项处理；其他九个阶段缺口仍在。','图6-1区域映射是来源图解释，不冒充阶段与因素的强制一一关系。','空白延后理由不能替代行动；有明确延期范围和条件才可登记延后。'],
        scenarios={
            'sufficient':variant(base,{'attention_factor_ids':['culture'],'weak_foundational_factor_ids':['culture'],'absent_gap_reasons':['low-rated-factor-unaddressed']},'充分支持阶段A决策，保留未记录的其他阶段。'),
            'missing':variant(base,{'gap_reasons':['low-rated-factor-unaddressed']},'删除行动并给空延后理由，文化弱项仍未处理。',lambda d:(d['phase_records'][0].update(actions=[dict(id='ACT-VISION',factor_ids=[],action='记录愿景')]),d.update(deferred_factors={'culture':''}))),
            'change':variant(base,{'attention_factor_ids':[],'weak_foundational_factor_ids':[]},'取得同口径补充调查后文化评分改6；这里只解除低分复核，不认定组织能力充分。',lambda d:d['factor_ratings'].update(culture=6)),
            'counterexample':variant(base,{'reject':'DAP-002'},'评分9超出来源1至7量表，拒绝。',lambda d:d['factor_ratings'].update(culture=9)),
        })


def checklist_case():
    responses={f'gather-{i:02}':dict(status='done',evidence=['INTERVIEWS']) for i in range(1,10)}
    responses['gather-09c']=dict(status='done',evidence=['INTERVIEWS'])
    base=dict(source_ids=['INTERVIEWS'],stages=['gather'],uses_workshop=False,responses=responses,role_assignments=[])
    return dict(title='访谈收集切换为工作坊后的适用清单',source='G176 §10、§11.3',decision='原计划使用访谈，改成工作坊后是否还能沿用全部清单已处理的结论？',
        materials=[('INTERVIEWS','虚构试点记录包含问题清单、公开数据预处理、场景草稿、参与者、匿名措施和访谈收集材料；本轮只审收集阶段，未采用工作坊。')],
        reasoning=['收集阶段范围明确，不自动声称规划、文档和评审阶段完成。','访谈是收集方式any-of的一项，以访谈记录支撑，不要求工作坊同时完成。','未采用工作坊时条件项为condition-not-met；改用工作坊使其重新适用。','done缺证据须保留missing-evidence；状态字段自身不能构成完成证明。'],
        scenarios={
            'sufficient':variant(base,{'open_item_ids':[],'gap_reasons':[],'condition_not_met_count':6},'访谈收集范围内各项有模拟记录，工作坊六条件项不适用。'),
            'missing':variant(base,{'gap_reasons':['missing-evidence']},'删除公开数据收集的证据，不能由done标签填补。',lambda d:d['responses']['gather-02'].update(evidence=[])),
            'change':variant(base,{'open_item_ids':['gather-w1','gather-w2','gather-w3','gather-w4','gather-w5','gather-w6'],'condition_not_met_count':0},'改成工作坊后六项变为未审，原访谈记录不能支持工作坊准备。',lambda d:d.update(uses_workshop=True)),
            'counterexample':variant(base,{'reject':'BSC-002'},'passed不是清单合法状态，拒绝泛化测试状态。',lambda d:d['responses']['gather-01'].update(status='passed')),
        })


def smart_case():
    base=dict(source_ids=['GOAL','BASELINE','PILOT'],goals=[dict(id='GOAL-ERROR',statement='减少试点预约录入错误',category='user-productivity',business_goal_ref='BUSINESS-RELIABILITY')],
        objectives=[dict(id='OBJ-ERROR',goal_id='GOAL-ERROR',statement='双店预约录入错误率从5%降至4%',scope='双店试点同一抽样口径',measure='录入错误事件/全部录入事件',unit='%',baseline=5,target=4,
            owner='虚构运营改进组',action='统一预约字段并试点培训',realism_rationale='同口径小样本试点支持继续验证，但不可外推全公司',realism_evidence=['PILOT'],due='2026-12-31')])
    return dict(title='双店预约错误率目标的结构与现实性边界',source='G176 §9.1–9.3',decision='填写5%到4%的目标能否证明改善已实现，扩大范围后能否沿用原现实性依据？',
        materials=[('GOAL','业务目标为减少双店预约录入差错，目标5%到4%由虚构运营组提出。'),('BASELINE','基线取同一双店抽样口径；没有全公司数据。'),('PILOT','小样本组件与培训试点支持继续验证，尚不足以证明长期效果。')],
        reasoning=['5%和4%是业务材料给出的基线与目标，不能由分析者自行填充。','SMART结构完整只表示字段可复核，现实性仍需责任人审阅。','从5%到4%是目标绝对下降1个百分点，不是已观察到改善。','扩为全国门店后原双店证据不覆盖新范围，必须撤下现实性支持并补证据。'],
        scenarios={
            'sufficient':variant(base,{'row_states':['structurally-smart-awaiting-review'],'gap_reasons':[]},'结构齐全，效果与合理性待业务评审。'),
            'missing':variant(base,{'row_states':['needs-input'],'gap_reasons':['no-baseline']},'缺基线不能判断改进幅度，不按零补齐。',lambda d:d['objectives'][0].pop('baseline')),
            'change':variant(base,{'row_states':['needs-input'],'gap_reasons':['smart-realistic-missing']},'目标扩为全国门店，撤回仅覆盖双店的现实性证据后重评。',lambda d:d['objectives'][0].update(scope='全国门店',realism_rationale='',realism_evidence=[])),
            'counterexample':variant(base,{'reject':'SMART-002'},'目的没有已登记目标时拒绝悬空追溯。',lambda d:d['objectives'][0].update(goal_id='GOAL-ABSENT')),
        })


def cases():
    return {name: build() for name, build in [
        ('architecture-role-catalog-review',role_case),('solution-delivery-notebook-review',notebook_case),
        ('product-constraint-conformance-review',product_case),('domain-architecture-alignment-review',domain_case),
        ('incident-architecture-adjustment-review',incident_case),('dtra-adm-phase-alignment-review',dtra_case),
        ('business-scenario-checklist-review',checklist_case),('smart-objective-review',smart_case)]}


def assert_expected(result, expected):
    """Authored business expectations; no calls back into production predicates."""
    for key, value in expected.items():
        if key == 'reject':
            raise AssertionError('Expected rejection '+value)
        if key in ('gap_reasons','absent_gap_reasons','gap_ids'):
            observed={g['id' if key=='gap_ids' else 'reason'] for g in result['gaps']}
            assert not observed.intersection(value) if key=='absent_gap_reasons' else set(value)<=observed, (key,value,observed)
            if value==[] and key=='gap_reasons':assert observed==set(),observed
        elif key=='row_states':assert [r['state'] for r in result['rows']]==value,result['rows']
        elif key=='finding_states':assert [r['state'] for r in result['findings']]==value,result['findings']
        elif key=='condition_not_met_count':assert sum(r['state']=='condition-not-met' for r in result['rows'])==value,result['rows']
        else:assert result[key]==value,(key,value,result[key])
