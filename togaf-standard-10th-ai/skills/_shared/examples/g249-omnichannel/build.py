#!/usr/bin/env python3
"""Reproducible, explicitly fictional G249 cross-artifact example.

The alternatives and design judgments are authored casework, not a general
algorithm claiming to derive an architecture from arbitrary natural language.
Generation and analysis use the same public tools as normal project models.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

SHARED = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SHARED / 'scripts'))
from generate import generate
from analyze import evaluate, impact
from validate import validate

CASE = Path(__file__).resolve().parent
CONTEXT = dict(domains=['business', 'data', 'application', 'technology'],
               landscape='segment', purpose='project', abstraction='logical', evolution='target')


def entity(identity, typ, name, **attrs):
    return dict(id=identity, type=typ, name=name, attributes=attrs,
                evidence=['CASE-REVIEW'], certainty='assumed')


def edge(identity, typ, source, target, label, **attrs):
    return dict(id=identity, type=typ, source=source, target=target, label=label,
                attributes=attrs, evidence=['CASE-REVIEW'], certainty='assumed')


def view(identity, artifact, profile, title, ids, edges=(), analysis=None):
    return dict(id=identity, artifact_id=artifact, profile_id=profile, title=title,
                context=copy.deepcopy(CONTEXT), entity_ids=list(ids), relationship_ids=list(edges),
                analysis=analysis or '依据虚构材料表达候选设计；证据不足的结论保留缺口。',
                legend='虚构教学案例；稳定ID跨视图复用。候选设计和项目规则不表示官方模板或业务批准。')


def domain_model(changed=False):
    revision = '2' if changed else '1'
    raw = 'examples/g249-omnichannel/raw-business-materials.md'
    sources = [dict(id=k, kind='example', description=v, locator=raw + '#' + k.lower())
               for k, v in [('CASE-MANDATE', '虚构架构工作委托'), ('CASE-BASELINE', '虚构现状及未决要求'),
                            ('CASE-CHANGE', '虚构离线门店销售新增约束'), ('CASE-REVIEW', '虚构项目分析约定')]]
    es = [
        entity('CAP-FULFIL', 'capability', '全渠道履约', definition='跨渠道协调订单、库存与交付', level=1, category='核心'),
        entity('CAP-ORDER', 'capability', '订单承诺', definition='记录并管理订单受理与履约承诺', level=2, category='核心'),
        entity('CAP-RESERVE', 'capability', '库存预占', definition='在明确的一致性与承诺规则下协调可售库存', level=2, category='核心'),
        entity('CAP-LOGISTICS', 'capability', '物流履约', definition='依据确认订单安排交付', level=2, category='核心'),
        entity('APP-ORDER', 'application', '线上订单应用', version='候选v'+revision, owner='订单分段', lifecycle='候选目标', criticality='待业务评价', cost='待估算'),
        entity('APP-STORE', 'application', '门店销售应用', version='候选v'+revision, owner='门店运营', lifecycle='候选目标', criticality='待业务评价', cost='待估算'),
        entity('APP-STOCK', 'application', '库存服务', version='候选v'+revision, owner='库存分段', lifecycle='候选目标', criticality='待业务评价', cost='待估算'),
        entity('IF-RESERVE', 'interface', '中央库存预占接口', protocol='候选 HTTPS 请求/响应', payload='订单标识、商品、数量；一致性规则待明确', version='候选v'+revision),
        entity('IF-EVENT', 'interface', '订单事件处理接口', protocol='候选异步事件', payload='事件标识、订单标识、数量；幂等与补偿策略待验证', version='候选v'+revision),
        entity('REQ-CONSISTENCY', 'requirement', '库存一致性与承诺标准待明确', statement='需业务确定超卖容忍、受理与最终承诺的界限及恢复目标', owner='库存业务负责人', priority='待排序', status='needs-input', acceptance='待提供业务接受标准'),
        entity('WP-ONLINE', 'work_package', '在线试点准备', owner='方案团队', start='2026-11-09', end='2026-11-20', status='候选；日期仅教学计划'),
        entity('TRANS-ONLINE', 'transition', '受控在线试点', definition='保留在线同步与异步两种候选，等待业务一致性要求', operating_conditions=dict(operations='试点值守及人工异常处理', data_consistency='待业务定义', dependencies='接口验证及库存业务接受标准', controls='重复请求识别与审计待验证', rollback='停止新试点订单，保留存量记录并对账'), ordinal=1, start='2026-11-09', end='2026-11-20'),
        entity('RISK-STOCK', 'risk_treatment', '库存冲突风险处理', risk='并发与延迟可能导致库存承诺冲突', action='明确一致性政策并演练重复事件与库存不足', owner='库存分段架构师', due_date='2026-11-20', control='候选幂等、冲突检测和人工补偿', expected_residual='待演练，不填概率或残余风险分数', start='2026-11-09', end='2026-11-20'),
    ]
    rs = [edge('CAP-PART-'+x, 'decomposes', 'CAP-FULFIL', x, '能力分解') for x in ['CAP-ORDER','CAP-RESERVE','CAP-LOGISTICS']]
    rs += [edge('EX-RESERVE', 'exposes', 'APP-STOCK', 'IF-RESERVE', '提供预占契约'),
           edge('USE-RESERVE', 'consumes', 'APP-ORDER', 'IF-RESERVE', '候选A：在线请求'),
           edge('EX-EVENT', 'exposes', 'APP-STOCK', 'IF-EVENT', '候选B：处理事件'),
           edge('USE-EVENT', 'consumes', 'APP-ORDER', 'IF-EVENT', '候选B：提交事件'),
           edge('WP-TO-ONLINE', 'implements_transition', 'WP-ONLINE', 'TRANS-ONLINE', '准备运营状态'),
           edge('REQ-IF', 'traces_to', 'IF-RESERVE', 'REQ-CONSISTENCY', '接口设计依赖业务一致性要求'),
           edge('CAP-IF', 'traces_to', 'CAP-RESERVE', 'IF-RESERVE', '能力的候选实现接口'),
           edge('RISK-REQ', 'traces_to', 'RISK-STOCK', 'REQ-CONSISTENCY', '政策缺口影响风险处理'),
           edge('TRANS-REQ', 'traces_to', 'TRANS-ONLINE', 'REQ-CONSISTENCY', '试点进入条件依赖业务接受标准')]
    app_ids = ['APP-ORDER','APP-STORE','APP-STOCK']; interface_ids = ['IF-RESERVE','IF-EVENT']
    network_edges = ['EX-RESERVE','USE-RESERVE','EX-EVENT','USE-EVENT']
    transitions = ['WP-ONLINE','TRANS-ONLINE']; transition_edges = ['WP-TO-ONLINE']
    requirements = ['REQ-CONSISTENCY']
    if changed:
        es += [entity('REQ-OFFLINE', 'requirement', '门店断连仍可受理销售', statement='断连可受理；最终承诺、额度及冲突政策待业务决定', owner='门店运营', priority='新增约束', status='candidate', acceptance='断连受理、重连、重复提交、冲突与回退场景待验收'),
               entity('IF-RECOVERY', 'interface', '门店恢复同步接口', protocol='候选持久队列与批量重放', payload='幂等事件标识、订单、商品数量、重放检查点；保留冲突记录', version='候选v2'),
               entity('WP-OFFLINE', 'work_package', '断连与恢复演练', owner='方案团队', start='2026-11-21', end='2026-12-04', status='候选；日期仅教学计划'),
               entity('TRANS-OFFLINE', 'transition', '断连受理与恢复对账试点', definition='条件满足后增加离线受理，不预先承诺超卖或恢复指标', operating_conditions=dict(operations='断连订单和异常补偿责任待确认', data_consistency='本地额度、中央冲突与重放幂等待业务接受', dependencies='持久记录、恢复接口及冲突演练', controls='检查点、审计及重放去重', rollback='停止离线受理，保留队列，逐笔对账后恢复在线'), ordinal=2, start='2026-11-21', end='2026-12-04')]
        rs += [edge('EX-RECOVERY', 'exposes', 'APP-STOCK', 'IF-RECOVERY', '恢复后接收并检查事件'),
               edge('USE-RECOVERY', 'consumes', 'APP-STORE', 'IF-RECOVERY', '断连持久保存，重连后重放'),
               edge('RECOVERY-REQ', 'traces_to', 'IF-RECOVERY', 'REQ-OFFLINE', '新增接口回应断连约束'),
               edge('WP-TO-OFFLINE', 'implements_transition', 'WP-OFFLINE', 'TRANS-OFFLINE', '验证后进入候选运营状态'),
               edge('WP-DEP', 'depends_on', 'WP-OFFLINE', 'WP-ONLINE', '依赖已验证的在线契约'),
               edge('TRANS-OFFLINE-REQ', 'traces_to', 'TRANS-OFFLINE', 'REQ-OFFLINE', '进入条件依赖断连与恢复验收'),
               edge('RISK-OFFLINE', 'traces_to', 'RISK-STOCK', 'REQ-OFFLINE', '新增断连与重复执行风险')]
        stock_risk = next(e for e in es if e['id']=='RISK-STOCK')
        stock_risk['attributes'].update(risk='断连积压、重复执行、库存冲突及恢复后未对账', action='演练断连、重连、幂等重放、库存不足、丢失恢复和回退', control='候选持久队列、检查点、冲突检测及人工补偿', end='2026-12-04', due_date='2026-12-04')
        stock_risk['evidence'].append('CASE-CHANGE')
        next(e for e in es if e['id']=='IF-EVENT')['attributes']['payload'] += '；新增断连重放和恢复对账语境'
        interface_ids += ['IF-RECOVERY']; network_edges += ['EX-RECOVERY','USE-RECOVERY']
        transitions += ['WP-OFFLINE','TRANS-OFFLINE']; transition_edges += ['WP-TO-OFFLINE','WP-DEP']
        requirements += ['REQ-OFFLINE']
    # Explicitly model the business handoff without inventing a logistics app.
    state_ids=['ORDER-PENDING','ORDER-CONFIRMED','ORDER-EXCEPTION','ORDER-FULFIL']
    es += [entity('ORDER-PENDING','data_state','订单已受理／待确认',owner='订单分段（候选责任）',retention='保留期限待业务与法务确定',entry='请求已记录；离线时需本地持久化',exit='依据待确定的承诺规则确认或转异常'),
           entity('ORDER-CONFIRMED','data_state','订单已确认',owner='订单分段（候选责任）',retention='保留期限待定',entry='库存与承诺条件已满足；详细规则待业务定义',exit='交给物流履约或按变更政策处置'),
           entity('ORDER-EXCEPTION','data_state','库存或同步异常待处理',owner='库存与门店联合责任待明确',retention='保留至冲突处理与审计完成，时限待定',entry='库存不足、重放冲突或恢复未对账',exit='人工补偿或重新确认；规则待明确'),
           entity('ORDER-FULFIL','data_state','允许物流履约的订单记录',owner='物流分段（来自工作范围）',retention='保留期限待定',entry='只接收已确认订单',exit='履约结果回传；接口待调查')]
    state_edges=[edge('ORDER-CONFIRM','transitions_to','ORDER-PENDING','ORDER-CONFIRMED','满足待确定的库存与承诺条件'),
                 edge('ORDER-EXCEPT','transitions_to','ORDER-PENDING','ORDER-EXCEPTION','库存不足、重放冲突或未对账'),
                 edge('ORDER-TO-FULFIL','transitions_to','ORDER-CONFIRMED','ORDER-FULFIL','确认后才允许交付物流')]
    rs += state_edges+[edge('CAP-ORDER-STATE','traces_to','CAP-ORDER','ORDER-PENDING','订单能力管理受理与确认'),
                       edge('CAP-LOGISTICS-STATE','traces_to','CAP-LOGISTICS','ORDER-FULFIL','物流只使用已确认订单'),
                       edge('RISK-ORDER','traces_to','RISK-STOCK','ORDER-EXCEPTION','冲突与重放影响承诺状态')]
    vs = [view('capability-map', 'business-capability-map', 'capability-decomposition', '履约能力边界', ['CAP-FULFIL','CAP-ORDER','CAP-RESERVE','CAP-LOGISTICS'], ['CAP-PART-'+x for x in ['CAP-ORDER','CAP-RESERVE','CAP-LOGISTICS']]),
          view('application-catalog','application-portfolio-catalog','compat-application-portfolio-catalog','候选应用边界与责任', app_ids),
          view('interface-network','application-communication-diagram','compat-application-communication-diagram','候选接口与交互', app_ids+interface_ids, network_edges,
               'A同步预占与B异步处理均为候选。一致性要求不足，不能排名。'+('纯同步方案不能单独覆盖断连受理；增加持久记录、恢复同步及补偿待决项。' if changed else '缺少超卖、承诺及恢复标准。')),
          view('requirements','requirements-catalog','compat-requirements-catalog','需求与未决接受条件',requirements),
          view('transition-roadmap','transition-architecture-model','transition-architecture-model-default','候选运营过渡与工作包',transitions,transition_edges),
          view('risk-treatment','risk-mitigation-plan','risk-mitigation-plan-default','库存与恢复风险处理',['RISK-STOCK'])]
    vs.append(view('order-states','data-lifecycle-diagram','compat-data-lifecycle-diagram','订单受理、承诺与物流交接边界',state_ids,[r['id'] for r in state_edges],
                   '业务给定物流只接收已确认订单。中间状态和异常处理为候选；确认条件、保留期限及物流接口尚待明确。'))
    notebook=dict(work_package_id='WP-OFFLINE' if changed else 'WP-ONLINE',solution_concept_ref='interface-network',
        implementation_strategy='受控试点；先明确接受条件和异常责任，再验证接口并决定是否进入候选运营状态',
        stakeholders=[dict(id='SH-OPS',name='门店运营',requirement_ids=requirements)],
        requirements=[dict(id=i,statement=next(e for e in es if e['id']==i)['attributes']['statement'],stakeholder_ids=['SH-OPS']) for i in requirements],
        specifications=[dict(id='SPEC-ONLINE',requirement_id='REQ-CONSISTENCY',statement='候选A：销售确认前同步预占；候选B：事件受理与异步库存处理。没有一致性标准，无法定优。',spec_type='候选接口与业务契约',applies_to='APP-ORDER / APP-STOCK')],
        risks=[dict(id='RISK-STOCK',description=next(e for e in es if e['id']=='RISK-STOCK')['attributes']['risk'])],
        controls=[dict(id='CTRL-STOCK',risk_id='RISK-STOCK',statement=next(e for e in es if e['id']=='RISK-STOCK')['attributes']['control'],applies_to='APP-STOCK')],
        gaps=[dict(id='GAP-CONSISTENCY',description='缺库存一致性、承诺、恢复与业务接受标准；候选控制尚未验证',in_scope=True)],
        architecture_summary=dict(business=dict(view_ids=['capability-map','requirements']),information=dict(view_ids=['order-states']+(['offline-data-boundary'] if changed else []),status='needs-input',reason='已表达订单受理、确认、异常及物流交接状态'+('，以及本地持久记录与中央恢复边界' if changed else '')+'；完整数据模型、保留政策与业务接受标准仍待展开，不能据此声称数据架构充分'),application=dict(view_ids=['application-catalog','interface-network']),infrastructure=dict(status='needs-input',reason='部署拓扑和容量未提供，本例只表达逻辑接口候选；上线前仍需基础设施分析'),security=dict(status='needs-input',reason='安全与隐私要求未提供，保留待评审输入；不宣称安全充分')))
    if changed:
        notebook['specifications'].append(dict(id='SPEC-OFFLINE',requirement_id='REQ-OFFLINE',statement='纯同步中央调用不能单独支撑断连受理。新增持久事件、幂等标识、恢复重放与人工冲突处理候选；受理不等于最终承诺。',spec_type='候选恢复与订单状态契约',applies_to='APP-STORE / IF-RECOVERY'))
        notebook['gaps'].append(dict(id='GAP-OFFLINE-POLICY',description='本地额度、承诺责任、冲突处理和数据保留规则待业务与安全评审',in_scope=True))
        local=entity('LOCAL-ORDER-RECORD','information','门店本地待同步订单记录',definition='候选本地持久记录，区别中央接收；写入何时算成功与故障丢失窗口尚待验证',owner='门店数据与运营责任待确认',retention='断连时长、对账后保留期限和法律要求待明确',fields=['事件标识','订单标识','商品数量','本地记录状态','恢复检查点'],design_status='candidate',evidence_origin='derived-from-CASE-CHANGE')
        es.append(local)
        es.append(entity('CENTRAL-ORDER-RECORD','information','中央接收与承诺记录',definition='候选中央记录分别保存事件接收、去重、库存承诺和异常处置结果；接收不自动等于履约确认',owner='订单与库存责任边界待确认',design_status='candidate'))
        rs += [edge('STORE-PERSIST','traces_to','APP-STORE','LOCAL-ORDER-RECORD','候选：断连先持久记录，不能仅驻留内存'),
               edge('RECOVERY-RECORD','traces_to','LOCAL-ORDER-RECORD','IF-RECOVERY','恢复后按标识重放并对账'),
               edge('PENDING-RECORD','traces_to','LOCAL-ORDER-RECORD','ORDER-PENDING','本地受理不自动成为最终承诺')]
        rs.append(edge('RECONCILE-RECORDS','traces_to','LOCAL-ORDER-RECORD','CENTRAL-ORDER-RECORD','按事件/订单标识逐笔对账；保留冲突与检查点'))
        vs.append(view('offline-data-boundary','information-map','information-concept-network','本地持久记录与中央恢复边界',['LOCAL-ORDER-RECORD','CENTRAL-ORDER-RECORD'],['RECONCILE-RECORDS'],
                       '两个记录边界分别承担离线保存与中央恢复接收；持久成功、丢失容忍、重试和对账目标待确定。'))
        notebook['recovery_contract']={'local_record_ref':'LOCAL-ORDER-RECORD','central_receiver_ref':'APP-STOCK','interface_ref':'IF-RECOVERY',
            'durable_ack':'记录持久成功后才答复受理；故障窗口与可接受丢失量待验证',
            'replay':'候选稳定事件标识去重、检查点重试；具体重试/保留策略待确定',
            'reconciliation':'逐笔检查本地记录与中央接收/承诺状态；冲突交由责任方决定，不能自动覆盖库存',
            'rollback':'停止新的离线受理；保留本地记录与检查点，逐笔核对后恢复在线',
            'verification_scenarios':['断连仍能受理','重连重放','重复事件不重复生效','库存不足转异常','存储故障与丢失窗口','恢复后长期未对账','停止离线受理并回退'],
            'status':'candidate-awaiting-business-and-operational-review'}
    notebook['decision_agenda']=[
        {'id':'DEC-STRATEGY','role_ref':'ROLE-CHIEF','question':'先受控试点还是扩大渠道承诺范围？','goal':'打通线上订单、门店库存和物流履约','options':['先在线试点后评估离线','并行验证在线与离线方案'],'tradeoff':'并行可提前暴露离线风险但增加设计、门店改造与运行投入；成本收益未估算','needed_input':['渠道价值/服务目标','预算与人员工作量','库存风险接受者'],'status':'pending-decision','evidence':['CASE-MANDATE','CASE-BASELINE']},
        {'id':'DEC-CROSS-SEGMENT','role_ref':'ROLE-EA','question':'订单、库存、物流之间由谁承诺和接受风险？','proposed_boundary':'订单区分受理与最终确认；库存提供承诺条件；物流仅使用已确认订单；异常与恢复责任待确认','needed_input':['一致性与承诺政策','跨分段责任接受记录','门店在线调用与物流交接契约'],'status':'pending-decision','evidence':['CASE-MANDATE','CASE-BASELINE']},
        {'id':'DEC-STOCK','role_ref':'ROLE-SEG','question':'允许怎样的库存、断连及恢复行为？','proposed_boundary':'待确认记录与可履约记录分开；冲突进入异常处理，不把异步等同于避免超卖','needed_input':['超卖容忍','本地额度','恢复目标及对账责任'],'status':'pending-decision','evidence':['CASE-BASELINE']+(['CASE-CHANGE'] if changed else [])}]
    es.append(entity('DELIVERY-NOTE','guide:solution-delivery-notebook','方案备选与需求、规格、风险配对',**notebook))
    vs.append(view('delivery-notebook','solution-delivery-notebook','solution-delivery-notebook-default','方案备选、跨域交接与运营条件',['DELIVERY-NOTE']))
    gaps=[dict(id='GAP-CONSISTENCY',description='库存一致性、承诺和恢复目标未明确，方案不能定优',impact='接口、风险及试点进入条件未定',needed_input='业务接受标准与服务水平'),
          dict(id='GAP-STORE-ONLINE',description='门店在线销售与中央库存的当前交互尚未调查',impact='不能由线上订单接口推断门店在线行为',needed_input='门店在线流程、接口与失败处理材料'),
          dict(id='GAP-LOGISTICS-HANDOFF',description='已确认订单交给物流的具体接口和责任未提供',impact='只明确确认前不进入物流，交接规格待定',needed_input='物流接收契约与责任方')]
    if changed:
        for identity,description,need in [('GAP-OFFLINE-DURATION','最大断连时间未知','断连上限与存储容量依据'),('GAP-LOSS','可容忍的数据丢失窗口未知','持久成功标准、故障演练与数据丢失容忍'),('GAP-RECOVERY','恢复和对账服务目标未知','恢复时限与未对账告警规则'),('GAP-LOCAL-QUOTA','本地额度与超卖政策未定','业务承诺、额度与冲突接受决定'),('GAP-EXCEPTION-OWNER','冲突、补偿与回退责任待确认','业务与运营责任人的交接接受记录')]:
            gaps.append(dict(id=identity,description=description,impact='阻断离线候选方案接受与运营状态进入',needed_input=need))
        for obj in es:
            if obj['id'] in {'REQ-OFFLINE','IF-RECOVERY','WP-OFFLINE','TRANS-OFFLINE','LOCAL-ORDER-RECORD','CENTRAL-ORDER-RECORD'}:
                obj['evidence']=['CASE-CHANGE','CASE-REVIEW']
                obj['attributes']['source_role']='stated-fictional-requirement' if obj['id']=='REQ-OFFLINE' else 'authored-design-candidate'
        for relation in rs:
            if any(x in {'REQ-OFFLINE','IF-RECOVERY','LOCAL-ORDER-RECORD','CENTRAL-ORDER-RECORD','TRANS-OFFLINE','WP-OFFLINE'} for x in [relation['source'],relation['target']]):relation['evidence']=['CASE-CHANGE','CASE-REVIEW']
    return dict(schema_version='2.0',project=dict(id='g249-omnichannel',name='虚构全渠道订单履约改造',version=revision,context=copy.deepcopy(CONTEXT),is_example=True,approval_status='candidate',implementation_status='not-started'), sources=sources,entities=es,relationships=rs,views=vs,deliverables=[],gaps=gaps)


def attach_role_assessment(model):
    """Use the runtime-contract fixture, binding its tasks to this shared model."""
    data = json.loads((CASE / 'role-skill-inputs.json').read_text())
    if 'inputs' in data:
        data = data['inputs']
    if model['project']['version']=='2':
        data['as_of']='2026-11-08'
        task=next(t for t in data['tasks'] if t['id']=='TASK-SOL')
        task['scope']='预占、断连受理及恢复同步候选比较'
        task['outcome']='接口契约、断连持久化、幂等重放、补偿与回退的验证场景'
        task['evidence'].append('CASE-CHANGE')
        requirement=next(r for r in data['requirements'] if r['id']=='REQ-SKILL-SOL')
        requirement['behavioral_criteria'].append('评审断连、重连、幂等重放和库存冲突的恢复设计')
        requirement['requirement_version']='2'
        requirement['evidence'].append('CASE-CHANGE')
        development=next(d for d in data['development'] if d['id']=='DEV-A')
        development['history'].append({'observed_on':'2026-11-08','event':'task-requirement-changed','status':'requirements-revised','rationale':'新增离线恢复目标，保留旧评价并更新实践/复评计划；没有新增能力评级','previous_success_criteria':copy.deepcopy(development['success_criteria']),'evidence':['CASE-CHANGE']})
        development['action']+='；新增断连持久记录、恢复重放、库存冲突和回退演练的设计及独立复评'
        development['success_criteria']=copy.deepcopy(requirement['behavioral_criteria'])
        development['reassessment']['criteria']=copy.deepcopy(requirement['behavioral_criteria'])
        development['requirement_versions']={requirement['id']:'2'}
    for sid in data['source_ids']:
        if sid not in {s['id'] for s in model['sources']}:
            model['sources'].append(dict(id=sid,kind='example',description='虚构人员与任务配置证据：'+sid,locator='examples/g249-omnichannel/role-skill-inputs.json'))
    from proficiency_contract import collaboration_profile, scale, sources as proficiency_sources
    for source in proficiency_sources():
        if source['id'] not in {s['id'] for s in model['sources']}:
            model['sources'].append(source)
    data['source_ids']=list(dict.fromkeys(data['source_ids']+[s['id'] for s in model['sources']]))
    model['scales'] = [scale()]
    role_ids=[]
    for role in data['roles']:
        tasks=[t for t in data['tasks'] if role['id'] in t['role_refs']]
        attrs={k:copy.deepcopy(v) for k,v in role.items() if k not in {'id','name','evidence'}}
        attrs.update(primary_responsibility='；'.join(t['outcome'] for t in tasks),
                     definition='本次任务角色：'+'；'.join(t['scope'] for t in tasks))
        model['entities'].append(dict(id=role['id'],type='guide:architecture-role',name=role['name'],attributes=attrs,evidence=role['evidence'],certainty='assumed'))
        role_ids.append(role['id'])
    relationship_definitions=collaboration_profile()['example']['extensions']['relationship_types']
    model.setdefault('extensions',{}).setdefault('relationship_types',{}).update(relationship_definitions)
    cooperation=[('SPECIAL-CH','specialization','ROLE-CHIEF','ROLE-EA','首席作为企业架构角色特例'),
                 ('GUIDE-EA','architecture_guidance','ROLE-EA','ROLE-SEG','跨分段原则与协调'),
                 ('CONSTRAINT-SEG','architecture_constraint','ROLE-SEG','ROLE-SOL','库存边界与未决一致性约束'),
                 ('COOPERATE-SOL','collaborates_with','ROLE-SOL','ROLE-SEG','反馈方案可行性与异常场景'),
                 ('HANDOFF-IF','handoff','ROLE-SEG','ROLE-SOL','交接接口范围和未决接受条件')]
    collaboration_edges=[]
    for identity,kind,src,dst,label in cooperation:
        attrs=dict(semantic_type=kind,scope='全渠道履约候选架构工作')
        if kind=='handoff':attrs.update(deliverable_ref='interface-network',acceptance_criteria=['能力边界、接口约束与未决条件均能追溯至需求'])
        model['relationships'].append(edge(identity,'g249:'+kind,src,dst,label,**attrs));collaboration_edges.append(identity)
    model['views'].append(view('role-collaboration','architecture-role-catalog','architecture-role-collaboration','角色协作与交接',role_ids,collaboration_edges))
    mapping=json.loads((SHARED/'references/g249/skill-task-map.json').read_text())
    source_skills={x['skill_id']:x for x in mapping['skills']}
    selected_skills=list(dict.fromkeys(r['skill_id'] for r in data['requirements']))
    skill_ids={sid:'SKILL-'+str(i+1) for i,sid in enumerate(selected_skills)}
    for sid,eid in skill_ids.items():
        original=source_skills[sid]
        model['entities'].append(entity(eid,'skill',original['source_name_en'],skill_id=sid,category=original['category_en'],subskill=original['source_name_en']))
    matrix_edges=[]
    for requirement in data['requirements']:
        attrs={k:copy.deepcopy(v) for k,v in requirement.items() if k not in {'id','skill_id','role_ref','evidence'}}
        attrs['task_refs']=[requirement['task_ref']]
        relation=edge(requirement['id'],'supports_role',skill_ids[requirement['skill_id']],requirement['role_ref'],'项目裁剪目标',**attrs)
        relation['evidence']=requirement['evidence'];model['relationships'].append(relation);matrix_edges.append(relation['id'])
        if requirement['role_ref']=='ROLE-EA':
            source_role='G249:role:enterprise-architect'
            source_value=source_skills[requirement['skill_id']]['official']['reference_proficiencies'][source_role]
            reference=edge('REF-'+requirement['id'],'supports_role',skill_ids[requirement['skill_id']],requirement['role_ref'],'原文参考目标',proficiency=source_value,assessment_kind='source_reference_target',assessment_state='reference',scale_id='G249-table5-1',reference_role_id=source_role,source_locator='G249 table5-2 '+requirement['skill_id'])
            reference['evidence']=['g249-table-source'];model['relationships'].append(reference);matrix_edges.append(reference['id'])
    for observation in data['assessments']:
        attrs={k:copy.deepcopy(v) for k,v in observation.items() if k not in {'id','skill_id','evidence'}}
        relation=edge(observation['id'],'supports_role',skill_ids[observation['skill_id']],'ROLE-SOL','人员观察证据',**attrs)
        relation['evidence']=observation['evidence'];model['relationships'].append(relation);matrix_edges.append(relation['id'])
    model['views'].append(view('skill-matrix','architecture-skill-matrix','ea-skill-role-proficiency','任务技能目标与独立人员观察',list(skill_ids.values())+role_ids,matrix_edges))
    development_ids=[]
    for development in data['development']:
        attrs={k:copy.deepcopy(v) for k,v in development.items() if k not in {'id','evidence'}}
        attrs.update(start=data['as_of'],end=development['due'],evidence=development['evidence'],current_assessment_state='evidence_insufficient' if development['current_proficiency'] is None else 'assessed')
        item=entity(development['id'],'skill_development','异常接口分析实践与复评',**attrs);item['evidence']=development['evidence']
        model['entities'].append(item);development_ids.append(item['id'])
    model['views'].append(view('development-plan','architecture-development-plan','architecture-development-plan-default','人员发展行动与复评条件',development_ids))
    # Each role's decision uses a deliberately selected part of the same model.
    role_scope={'ROLE-CHIEF':{'capability','transition','risk_treatment'},
                'ROLE-EA':{'capability','application','interface','requirement'},
                'ROLE-SEG':{'capability','interface','requirement','risk_treatment'},
                'ROLE-SOL':{'application','interface','requirement','work_package','transition','risk_treatment'}}
    for task in data['tasks']:
        kinds=set().union(*(role_scope[r] for r in task['role_refs']))
        task['model_object_refs']=[e['id'] for e in model['entities'] if e['type'] in kinds or e['id'] in task['role_refs'] or e['type'] in {'skill','skill_development'}]
        task['model_object_refs'] += [e['id'] for e in model['entities'] if e['type'] in {'data_state','information'}] + ['DELIVERY-NOTE']
        adopted_artifacts={'TASK-CH':['business-capability-map','transition-architecture-model','solution-delivery-notebook'],
                           'TASK-EA':['business-capability-map','application-portfolio-catalog','solution-delivery-notebook'],
                           'TASK-SEG':['requirements-catalog','data-lifecycle-diagram','solution-delivery-notebook'],
                           'TASK-SOL':['application-communication-diagram','transition-architecture-model','risk-mitigation-plan','solution-delivery-notebook']}
        task['artifact_ids']=adopted_artifacts[task['id']]
        if model['project']['version']=='2' and task['id'] in {'TASK-SEG','TASK-SOL'}:task['artifact_ids'].append('information-map')
        task['output_tailoring_reason']='本轮以实际需求、接口候选和运营过渡支持决策；来源映射的其他候选视图未选，不能声称其已完成。'
    wanted={a for t in data['tasks'] for a in t['artifact_ids']}
    data['model_views']=copy.deepcopy([v for v in model['views'] if v['artifact_id'] in wanted])
    data['model_objects'] = copy.deepcopy(model['entities'])
    data['model_relationships'] = copy.deepcopy(model['relationships'])
    context_id = 'G249-ASSESSMENT-CONTEXT'
    data['model_binding'] = dict(version='g249-assessment-binding/1',context_ref=context_id)
    model['entities'].append(entity(context_id,'guide:g249-assessment-context','架构工作、角色与技能配置',assessment_inputs=copy.deepcopy(data)))
    model.setdefault('extensions',{}).setdefault('entity_types',{})['guide:g249-assessment-context']='G249任务、技能与证据的项目分析上下文'
    analysis = dict(id='g249-assessment',method_id='architecture-role-skill-assessment',inputs=data,evidence=data['source_ids'])
    model['analyses']=[analysis]
    v=view('role-assignment','architecture-role-catalog','architecture-work-assignment-review','任务、角色、能力证据与配置条件',[context_id])
    v['attributes']={'analysis_ids':[analysis['id']]};model['views'].append(v)
    return model


def build(changed=False):
    return attach_role_assessment(domain_model(changed))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--render',action='store_true')
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    summary={}
    for name,changed in [('baseline',False),('offline-change',True)]:
        model=build(changed)
        findings=validate(model)
        errors=[f for f in findings if f['level']=='error']
        if errors:raise ValueError(json.dumps(errors,ensure_ascii=False,indent=2))
        dest=args.out/name
        manifest=generate(model,dest,all_items=True,render=args.render,strict=True)
        assessment=evaluate(model['analyses'][0],model)
        (dest/'role-assessment.json').write_text(json.dumps(assessment,ensure_ascii=False,indent=2)+'\n')
        summary[name]={'entities':len(model['entities']),'relationships':len(model['relationships']),'views':len(model['views']),'validation_errors':len(errors),'validation_warnings':len(findings)-len(errors),'model_sha256':hashlib.sha256(json.dumps(model,sort_keys=True,ensure_ascii=False).encode()).hexdigest()}
    changed_model=build(True)
    # Traverse every reachable shared object; this is a candidate dependency
    # closure, not proof that every reachable object requires a design change.
    delta=impact(changed_model,['REQ-OFFLINE'],max_depth=len(changed_model['entities']))
    (args.out/'change-impact.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2)+'\n')
    (args.out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
