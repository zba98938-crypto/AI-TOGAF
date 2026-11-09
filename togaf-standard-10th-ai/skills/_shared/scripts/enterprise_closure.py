#!/usr/bin/env python3
"""Enrich an audited transaction projection with independently authored simulation.
No database modifications, inferred authorization or production operations.
"""
import argparse,copy,hashlib,json
from pathlib import Path
from closure_semantics import check

def build(base):
    m=copy.deepcopy(base);m['project'].update(version='closure-synthetic-2',approval_status='candidate',implementation_status='not-started')
    m['project'].pop('decision_status',None)
    source='closure-simulation-policy';m['sources'].append({'id':source,'kind':'example','description':'独立编写的 2026Q3 合成企业政策、职责、架构假设与恢复演练；绝非真实批准。','locator':'enterprise_closure.py / simulation-v2'})
    ext=m.setdefault('extensions',{});types=ext.setdefault('entity_types',{});relations=ext.setdefault('relationship_types',{})
    for t in ['concern','value_stream','risk_policy','restore_point','compliance_review','value_review','information_contract','application_interface','value_stage']:
        types['enterprise:'+t]='独立合成企业 '+t+'；项目扩展而非正式建模语言。'
    def relation(name,st,tt,meaning):
        relations['enterprise:'+name]={'source_types':st,'target_types':tt,'meaning':meaning}
    relation('motivates',['enterprise:concern'],['requirement'],'关注点产生可检验需求')
    relation('allocates',['requirement'],['process'],'需求分配给业务流程')
    relation('produces',['process'],['data_entity'],'业务流程产生信息')
    relation('served_by',['data_entity'],['application'],'信息由应用服务支持')
    relation('deployed_on',['application'],['technology'],'应用部署于技术平台')
    relation('exposes_gap',['technology'],['gap'],'平台现状暴露架构差距')
    relation('evaluated_by',['gap'],['option'],'差距由候选方案评价')
    relation('delivered_by',['option'],['work_package'],'候选方案拆分为工作包')
    relation('reviewed_by',['transition'],['enterprise:compliance_review'],'过渡架构受实施合规复核')
    relation('assessed_by',['enterprise:compliance_review'],['enterprise:value_review'],'实施合规连接价值复核')
    relation('responsible_for',['role'],['process','application','technology','data_entity','work_package','enterprise:risk_policy'],'主责关系，不代表授权')
    relation('compensates',['activity'],['activity'],'失败后执行明确补偿')
    relation('failure_exit',['activity'],['activity'],'异常退出/人工对账')
    relation('version_transition',['process','data_entity','application','technology'],['process','data_entity','application','technology'],'相同概念在命名演进状态间的映射')
    def entity(identity,t,name,attrs=None,state=None,domain=None,concept=None):
        e={'id':identity,'type':t,'name':name,'attributes':attrs or {},'evidence':[source],'certainty':'assumed','approval_status':'candidate','implementation_status':'not-started'}
        if state:e.update(state_id='closure-state-'+state,concept_id=concept or identity,version='1',context={**m['project']['context'],'domains':[domain] if domain else m['project']['context']['domains'],'evolution':state})
        m['entities'].append(e);return identity
    def link(t,a,b,label,attrs=None):
        identity='closure-edge-'+str(len(m['relationships'])+1);m['relationships'].append({'id':identity,'type':t,'source':a,'target':b,'label':label,'attributes':attrs or {},'evidence':[source],'certainty':'assumed'});return identity
    m['states']=[{'id':'closure-state-'+s,'name':n,'evolution':s,'operating_conditions':{'order_intake':'enabled','reconciliation':'manual daily' if s=='baseline' else 'automated with human exception queue','rollback':'restorable before external settlement; otherwise manual compensation'},'evidence':[source],'approval_status':'candidate','implementation_status':'not-started'} for s,n in [('baseline','基线：跨基地批处理'),('transition','过渡：双写与对账'),('target','目标：事件同步与统一履约')]]
    transition_state=next(s for s in m['states'] if s['evolution']=='transition')
    transition_state['operating_conditions'].update(
      operations='Two-site dual-write pilot; order intake remains enabled; closure-role owns human exception queue; retained daily batch fallback. Synthetic candidate, not implemented.',
      data_consistency='SIM-DUAL-1 uses local_order_id plus event_id; at-least-once delivery with dual-write reconciliation; duplicates and missing master keys are quarantined.',
      dependencies='closure-order-hub-transition, closure-event-platform-transition and closure-interface-transition; existing ERP importer; validated closure-restore simulation restore point.',
      controls='closure-control idempotency and duplicate-event checks; exceptions reconciled by closure-role; candidate pilot scope only, no real deployment authorization.')
    org=entity('closure-org','organization','合成集团运营委员会')
    actor=entity('closure-owner','actor','合成运营责任人')
    role=entity('closure-role','role','订单与主数据治理负责人')
    link('member_of',actor,org,'属于集团运营委员会');link('assigned_to',role,actor,'承担订单与主数据治理职责')
    concern=entity('closure-concern','enterprise:concern','订单履约与跨基地数据一致性')
    req=entity('closure-requirement','requirement','跨基地订单事件 5 分钟内一致',{'metric':'consistency_latency_minutes','threshold':5,'authority':'simulation-policy'})
    link('enterprise:motivates',concern,req,'形成可测量一致性需求')
    chain={}
    defs=[('business','process','order-fulfillment','订单履约'),('data','data_entity','order-event','订单事件'),('application','application','order-hub','订单协同中心'),('technology','technology','event-platform','事件与数据库平台')]
    details={
      'business':{
        'baseline':{'summary':'每日批次履约 / 人工跨基地对账','mechanism':'local intake plus daily batch reconciliation','sites':12,'max_latency_minutes':1440},
        'transition':{'summary':'2基地双写试点 / 订单入口保持','mechanism':'dual-write pilot with manual exception queue','sites':2,'max_latency_minutes':30,'fallback':'preserved daily batch path'},
        'target':{'summary':'12基地幂等履约 / 5分钟一致','mechanism':'event-driven fulfilment with idempotent checks','sites':12,'max_latency_minutes':5}},
      'data':{
        'baseline':{'summary':'基地本地订单键 / 每日快照','key':'site_id + local_order_id','contract':'SIM-SNAPSHOT-1','delivery':'daily-batch'},
        'transition':{'summary':'本地键 + 集团事件键 / 双写核对','key':'local_order_id plus event_id','contract':'SIM-DUAL-1','delivery':'at-least-once with reconciliation'},
        'target':{'summary':'集团event_id去重 / 版本化事件','key':'site_id + event_id','contract':'SIM-ORDER-EVENT-1','delivery':'at-least-once with idempotent consumer'}},
      'application':{
        'baseline':{'summary':'集团ERP导入 / 基地MES批次接口','components':['group ERP snapshot importer','local MES batch adapters'],'interface_mode':'batch-file'},
        'transition':{'summary':'事件代理双写 / 2基地接口试点','components':['dual-write event proxy','two-site adapter pilot','existing ERP importer'],'interface_mode':'dual batch and event'},
        'target':{'summary':'订单事件中心 / 12基地版本化API','components':['stateless order event hub','idempotency store','twelve-site API adapters'],'interface_mode':'versioned event API'}},
      'technology':{
        'baseline':{'summary':'单故障域批次队列 / 快照保留','fault_domains':1,'retention_hours':24,'mechanism':'batch queue plus retained snapshots'},
        'transition':{'summary':'隔离双写队列 / 校验恢复点','fault_domains':2,'retention_hours':24,'mechanism':'isolated staging queue and verified simulation restore point'},
        'target':{'summary':'三故障域事件平台 / 幂等重放','fault_domains':3,'retention_hours':72,'mechanism':'partitioned event log and idempotent replay'}}}
    for state in ['baseline','transition','target']:
        for domain,t,identity,name in defs:
            e=entity('closure-'+identity+'-'+state,t,name+' / '+state,{'consistency':'daily batch' if state=='baseline' else 'dual-write reconciliation' if state=='transition' else 'idempotent event replication'},state,domain,identity)
            m['entities'][-1]['attributes']['architecture_detail']={**details[domain][state],'classification':'synthetic-design-assumption','owner_id':role}
            link('enterprise:responsible_for',role,e,'主责运营/治理')
            chain[(domain,state)]=e
        link('enterprise:produces',chain['business',state],chain['data',state],'产生订单事件')
        link('enterprise:served_by',chain['data',state],chain['application',state],'由订单协同中心支持')
        link('enterprise:deployed_on',chain['application',state],chain['technology',state],'部署于事件平台')
    for domain,_,identity,_ in defs:
        for a,b in [('baseline','transition'),('transition','target')]:link('enterprise:version_transition',chain[domain,a],chain[domain,b],'同一概念 '+a+' → '+b)
    link('enterprise:allocates',req,chain['business','baseline'],'业务流程承担一致性需求')
    gap=entity('closure-gap','gap','批处理延迟与不一致差距',{'baseline_minutes':1440,'target_minutes':5})
    option=entity('closure-option','option','事件复制 + 幂等订单处理',{'alternatives':['继续批处理','集中式单库'],'selection':'candidate','tradeoff':'增加事件运维与对账复杂度'})
    wp=entity('closure-package','work_package','跨基地事件平台迁移',{'duration_days':90,'owner_id':role,'cost_cny':1200000,'cost_classification':'synthetic-estimate'})
    transition=entity('closure-transition','transition','可运营双写过渡',{'entry_criteria':['恢复点验证','影子对账无未处置差异'],'exit_criteria':['模拟一致性 < 5min','异常队列有责任人'],'rollback_flow_id':'closure-rollback'})
    compliance=entity('closure-compliance','enterprise:compliance_review','实施合规模拟评审',{'result':'simulation-pass','decision':'pending-independent-review','checks':['幂等去重','最小权限','对账与恢复点'],'production_verified':False})
    value=entity('closure-value','enterprise:value_review','价值复核：只报告模拟观测',{'result':'scenario-observation','baseline_minutes':1440,'simulation_minutes':4,'realized_benefit':None})
    link('enterprise:exposes_gap',chain['technology','baseline'],gap,'暴露批处理同步差距')
    link('enterprise:evaluated_by',gap,option,'由方案权衡评估');link('enterprise:delivered_by',option,wp,'拆分工作包');link('addresses_gap',wp,gap,'处理批处理差距');link('implements_transition',wp,transition,'实现双写过渡');link('satisfies',wp,req,'实现一致性验收条件')
    link('enterprise:reviewed_by',transition,compliance,'逐项实施合规复核');link('enterprise:assessed_by',compliance,value,'连接模拟价值评估')
    stream=entity('closure-stream','enterprise:value_stream','从订单接受到履约结算',{'stages':['接受','校验','库存分配','生产','发货','结算'],'beneficiary':'合成客户'})
    policy=entity('closure-risk-policy','enterprise:risk_policy','合成风险偏好与容忍度',{'impact_unit':'CNY','risk_score_method':'likelihood(1..5) * impact(1..5)','appetite':6,'tolerance':12,'authority':'simulation-policy'})
    link('enterprise:responsible_for',role,policy,'负责模拟风险政策')
    restore=entity('closure-restore','enterprise:restore_point','迁移前合成恢复点',{'snapshot_id':'SIM-RP-20260930-01','rpo_minutes':5,'rto_minutes':30,'classification':'synthetic','external_settlement_included':False})
    # Additional enterprise context is independently authored, never inferred from transactions.
    objective=entity('closure-objective','objective','减少跨基地履约差异',{'measure':'exception_queue_age_hours','simulation_target':24})
    principle=entity('closure-principle','principle','同一订单标识、幂等处理、显式责任',{'rationale':'避免重复事件引发重复履约','status':'candidate'})
    cap=entity('closure-capability','capability','跨基地订单履约协同',{'business_owner_id':role})
    subcap=entity('closure-data-capability','capability','订单主数据与事件治理',{'business_owner_id':role})
    link('decomposes',cap,subcap,'协同能力分解为订单事件治理')
    relation('advances',['enterprise:concern'],['objective'],'关注点关联可测业务目标')
    relation('guided_by',['requirement'],['principle'],'需求受架构原则约束')
    relation('enables',['process'],['capability'],'业务流程使能业务能力')
    relation('value_stage_of',['enterprise:value_stage'],['enterprise:value_stream'],'价值阶段属于价值流')
    relation('site_unit',['enterprise:site'],['organization'],'基地对应运营组织单元')
    relation('interface_of',['enterprise:application_interface'],['application'],'应用接口属于提供应用')
    relation('exchanges',['enterprise:application_interface'],['data_entity'],'接口交换具有明确契约的信息')
    relation('local_platform',['enterprise:site'],['technology'],'基地部署对应技术平台')
    relation('mitigated_by',['risk_register_entry'],['control_objective'],'风险由明确控制目标缓解')
    link('enterprise:advances',concern,objective,'形成差异处置目标');link('enterprise:guided_by',req,principle,'以幂等与责任原则约束需求')
    link('enterprise:enables',chain['business','target'],cap,'目标业务流程使能协同能力')
    for i,name in enumerate(['接受订单','核验主数据','分配库存','协调生产','发货履约','对账结算']):
        stage=entity('closure-value-stage-'+str(i),'enterprise:value_stage',name,{'beneficiary':'合成客户','owner_id':role,'entry':'前置业务事件完整','exit':'生成可追溯履约事件'})
        link('enterprise:value_stage_of',stage,stream,'属于订单履约价值流')
    risk=entity('closure-risk-entry','risk_register_entry','重复订单事件导致重复履约',{'likelihood':2,'impact':5,'score':10,'unit':'ordinal-1..25','owner_id':role,'residual_decision':'pending','period':'2026Q3'})
    control=entity('closure-control','control_objective','幂等键去重与例外对账',{'test':'duplicate event does not duplicate shipment','authority':'simulation-policy'})
    link('enterprise:mitigated_by',risk,control,'以幂等与对账控制降低风险，不构成接受批准')
    for state in ['baseline','transition','target']:
        interface=entity('closure-interface-'+state,'enterprise:application_interface','订单事件接口 / '+state,{'protocol':'batch-file' if state=='baseline' else 'event-json','schema_id':details['data'][state]['contract'],'identity':details['data'][state]['key'],'delivery_semantics':details['data'][state]['delivery'],'transport_mode':details['application'][state]['interface_mode'],'failure_owner_id':role},state,'application','order-event-interface')
        link('enterprise:interface_of',interface,chain['application',state],'订单协同中心提供接口')
        link('enterprise:exchanges',interface,chain['data',state],'交换有版本标识的订单事件')
    for site in [e for e in m['entities'] if e['type']=='enterprise:site']:
        suffix=site['id'].split('-')[-1]
        unit=entity('closure-site-unit-'+suffix,'organization','基地运营单元-'+suffix,{'site_id':site['id'],'responsibility':'订单、库存与事件异常处置'})
        local_actor=entity('closure-site-actor-'+suffix,'actor','基地运营责任人-'+suffix,{'classification':'synthetic'})
        local_role=entity('closure-site-role-'+suffix,'role','基地事件治理岗-'+suffix,{'escalation_owner_id':role})
        link('enterprise:site_unit',site['id'],unit,'基地归属运营单元');link('member_of',local_actor,unit,'属于基地运营单元');link('assigned_to',local_role,local_actor,'承担基地事件治理职责')
        for state in ['baseline','transition','target']:
            tech=entity('closure-site-platform-'+suffix+'-'+state,'technology','基地-'+suffix+'事件代理 / '+state,{'availability':'operable in simulation','failure_queue_owner_id':local_role,'restore_point_id':restore},state,'technology','site-platform-'+suffix)
            app=entity('closure-site-app-'+suffix+'-'+state,'application','基地-'+suffix+'履约应用 / '+state,{'interface_contract':'SIM-ORDER-EVENT-1','exception_owner_id':local_role},state,'application','site-app-'+suffix)
            link('enterprise:local_platform',site['id'],tech,'基地部署本地事件平台');link('enterprise:deployed_on',app,tech,'履约应用部署于基地平台');link('communicates_with',app,chain['application',state],'调用集团订单事件接口');link('enterprise:responsible_for',local_role,app,'负责基地履约例外处置')
    flow_nodes=[]
    for identity,t,name,attrs in [
        ('start','activity','冻结写入与校验恢复点',{}),('check','decision','恢复点有效？',{'guard_field':'restore_valid','guard_values':[True,False]}),
        ('restore','activity','恢复数据库并重放幂等事件',{'writes_state':True,'compensation_id':'closure-flow-reconcile','outcome_field':'restore_result','outcome_values':['success','failure']}),
        ('verify','decision','对账一致？',{'guard_field':'consistent','guard_values':[True,False]}),
        ('settle','activity','外部结算：不可逆',{'writes_state':True,'irreversible':True,'outcome_field':'settlement_result','outcome_values':['confirmed','failure']}),
        ('reconcile','activity','人工处置差异与补偿',{}),('abort','activity','中止并升级责任人',{'terminal':True}),('done','activity','恢复服务并封存证据',{'terminal':True})]:
        flow_nodes.append(entity('closure-flow-'+identity,t,name,attrs))
    flow_edges=[]
    def control(t,a,b,label,attrs=None):flow_edges.append(link(t,'closure-flow-'+a,'closure-flow-'+b,label,attrs))
    control('flows_to','start','check','完成冻结/校验')
    for a,b,field,val in [('check','restore','restore_valid',True),('check','abort','restore_valid',False),('verify','settle','consistent',True),('verify','reconcile','consistent',False)]:control('branches',a,b,field+'='+str(val),{'guard':{'field':field,'operator':'eq','value':val}})
    control('flows_to','restore','verify','恢复成功',{'guard':{'field':'restore_result','operator':'eq','value':'success'}});control('enterprise:compensates','restore','reconcile','恢复失败：补偿/人工对账',{'guard':{'field':'restore_result','operator':'eq','value':'failure'}})
    control('flows_to','settle','done','结算确认',{'guard':{'field':'settlement_result','operator':'eq','value':'confirmed'}});control('enterprise:failure_exit','settle','reconcile','不可逆结算失败：人工对账',{'guard':{'field':'settlement_result','operator':'eq','value':'failure'}});control('flows_to','reconcile','abort','封存差异并升级')
    records=[]
    def evidence(identity,dimension,value,unit,**extra):records.append({'id':identity,'dimension':dimension,'value':value,'unit':unit,'method':'independently-authored simulation ledger, not SQL fact','owner_id':role,'source_id':source,'classification':'synthetic','period_start':'2026-07-01','period_end':'2026-09-30','max_age_days':90,**extra})
    evidence('closure-dq','valid_order_ratio',.98,'ratio',numerator=980,denominator=1000,threshold=.975)
    evidence('closure-risk','consistency_loss_risk',10,'ordinal-1..25',likelihood=2,impact=5,appetite=6,tolerance=12)
    evidence('closure-rto','restore_duration',24,'minutes',threshold=30)
    evidence('closure-rpo','restore_loss_window',3,'minutes',threshold=5)
    stages=[('concern',concern),('requirement',req)]+[(d,chain[d,'baseline']) for d,_,_,_ in defs]+[('gap',gap),('option',option),('work_package',wp),('transition',transition),('compliance',compliance),('value_review',value)]
    closure={'as_of':'2026-11-06','classification':'synthetic','evidence_records':records,'rules':[{'id':'quality-policy','dimension':'valid_order_ratio','threshold':.975,'period_start':'2026-07-01','period_end':'2026-09-30','owner_id':role,'authority':'simulation-policy'}],
        'defects':[{'id':'SIM-DEFECT-'+str(i+1),'kind':'missing-master-key' if i<10 else 'duplicate-event','owner_id':role,'disposition':'simulation-quarantine'} for i in range(20)],
        'flows':[{'id':'closure-rollback','start_id':'closure-flow-start','node_ids':flow_nodes,'edge_ids':flow_edges,'terminal_ids':['closure-flow-abort','closure-flow-done']}],
        'adm_chain':[{'stage':s,'entity_ids':[e]} for s,e in stages],
        'recovery_exercises':[{'id':'SIM-RECOVERY-01','classification':'synthetic','production_proof':False,'restore_point_id':restore,'result':'pass','rto_minutes':24,'rpo_minutes':3,'observations':['1000 independently simulated order keys compared','980 valid / 20 quarantined defect records','irreversible settlement routed to human reconciliation'],'responsible_role_id':role}],
        'acceptance':{'implementation':'candidate','source':'not-verified','business_execution':'simulation-only','human_signoff':'pending','certification':'not-claimed'}}
    closure['state_detail_contract']=True
    m.setdefault('extension_data',{})['enterprise:closure']=closure
    # Purpose-specific views use shared identities, not copies; static reader has its own pages.
    m['views']=[{'id':'closure-overview','artifact_id':'domain-architecture-alignment','title':'订单履约跨域架构闭环（合成）','context':m['project']['context'],'entity_ids':[e for _,e in stages],'relationship_ids':[e['id'] for e in m['relationships'] if e['source'] in [x for _,x in stages] and e['target'] in [x for _,x in stages]],'analysis':'关注点到模拟价值复核的完整设计链；没有真实实施批准。','legend':'项目简化关系图，不是 UML/BPMN/ArchiMate 正式符号。','allow_mixed_evolution':True,'layout':'adaptive'}]
    return m

def main():
    p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():p.error('--out must be new; sealed datasets are immutable')
    a.out.mkdir(parents=True);base=json.loads(a.base.read_text());model=build(base)
    (a.out/'enterprise-model.json').write_text(json.dumps(model,ensure_ascii=False,indent=2))
    from validate import validate
    issues=validate(model)
    (a.out/'validation.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2))
    (a.out/'input-manifest.json').write_text(json.dumps({'base':str(a.base),'base_sha256':hashlib.sha256(a.base.read_bytes()).hexdigest(),'classification':'synthetic','database_rebuilt':False,'entities':len(model['entities']),'relationships':len(model['relationships'])},indent=2))
    print(json.dumps({'entities':len(model['entities']),'relationships':len(model['relationships']),'errors':sum(i['level']=='error' for i in issues)}));return int(any(i['level']=='error' for i in issues))
if __name__=='__main__':raise SystemExit(main())
