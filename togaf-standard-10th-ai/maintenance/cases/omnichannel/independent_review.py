# -*- coding: utf-8 -*-
"""Independent source/design review; never grants business approval."""
from pathlib import Path
import hashlib,json,runpy,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
RAW=ROOT/'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/raw-business-materials.md'
INPUTS=ROOT/'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json'
BUILD=ROOT/'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/build.py'
def ev(path,needle):
 text=path.read_text();assert needle in text,(path,needle)
 return {'path':str(path.relative_to(ROOT)),'line':text[:text.index(needle)].count('\n')+1,'quote':needle,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def evidence(*pairs):return [ev(p,s) for p,s in pairs]
ns=runpy.run_path(str(BUILD),run_name='independent_case_review')
models={name:ns['build'](changed) for name,changed in [('baseline',False),('offline-change',True)]}
assessments={name:ns['evaluate'](m['analyses'][0],m)['result'] for name,m in models.items()}
impact=ns['impact'](models['offline-change'],['REQ-OFFLINE'],max_depth=len(models['offline-change']['entities']))
ids={name:{e['id'] for e in m['entities']} for name,m in models.items()}
checks=[
 {'id':'C01','topic':'缺一致性输入时不能定优','status':'source-design-consistent','observation_zh':'两候选均保留；纯同步仅被判为不能独自覆盖断连受理，未被全局退役；异步不被宣称避免超卖。','evidence':evidence((RAW,'不得据材料自动宣称 B 能避免超卖、A 总是不可用或某方案最优。'),(BUILD,'A同步预占与B异步处理均为候选。一致性要求不足，不能排名。'))},
 {'id':'C02','topic':'新增断连约束传播','status':'source-design-consistent-with-limits','observation_zh':'版本2新增恢复接口、门店与中央记录、离线需求、过渡和工作包；更新风险、解决方案任务目标、发展行动及复评，保留原人员观察。通用图影响的边界见F06。','evidence':evidence((RAW,'设计评审要求新增断连存储与恢复同步接口分析'),(BUILD,"task['scope']='预占、断连受理及恢复同步候选比较'"),(BUILD,"requirement['behavioral_criteria'].append('评审断连、重连、幂等重放和库存冲突的恢复设计')"),(BUILD,"development['reassessment']['criteria']=copy.deepcopy(requirement['behavioral_criteria'])"))},
 {'id':'C03','topic':'物流只接受确认订单','status':'source-design-consistent','observation_zh':'物流交接唯一状态迁移起点为ORDER-CONFIRMED；无待确认订单直接进入物流边。未提供物流系统时没有臆造物流应用，交接契约明确为缺口。','evidence':evidence((RAW,'物流履约使用已确认订单。'),(BUILD,"edge('ORDER-TO-FULFIL','transitions_to','ORDER-CONFIRMED','ORDER-FULFIL','确认后才允许交付物流')"),(BUILD,"dict(id='GAP-LOGISTICS-HANDOFF'"))},
 {'id':'C04','topic':'任务缺技能定义与目标','status':'correctly-retained-gap','observation_zh':'TASK-SOL所需optimistic-pessimistic-patterns没有采用目标；当前分析明确source-definition-unresolved与missing-task-skill-requirement，不自动猜成并发控制，不宣布任务技能完备。','evidence':evidence((INPUTS,'"G249:skill:application:optimistic-pessimistic-patterns"'))},
 {'id':'C05','topic':'个人证据及容量未知','status':'correctly-retained-gap','observation_zh':'甲proficiency=null而非自动降为2；所有任务workload_hours=null，40小时及8小时专家支持不能证明够用。实际分析保持needs-evidence、capacity unresolved和approval not-granted；另外期间缺口见F04。','evidence':evidence((INPUTS,'没有2级所需行为证据，不能自动记2级。'),(INPUTS,'"workload_hours": null'),(INPUTS,'"available_hours": 8'))},
 {'id':'C06','topic':'共享ID与退役','status':'source-design-consistent','observation_zh':'两个内存模型保留28个原实体ID，新增6个，没有退役任何实体。源材料未要求删除在线同步能力，保留IF-RESERVE用于在线场景合理；不凭新离线约束退役旧应用。','shared_entity_count':len(ids['baseline']&ids['offline-change']),'added_entity_ids':sorted(ids['offline-change']-ids['baseline']),'retired_entity_ids':sorted(ids['baseline']-ids['offline-change']),'evidence':evidence((RAW,'它仍可能用于在线场景。'),(RAW,'能力、应用及接口在不同视图沿用同一对象。'))},
 {'id':'C07','topic':'过渡是运营状态且需进入条件','status':'source-design-consistent','observation_zh':'TRANS-ONLINE和TRANS-OFFLINE提供运营、数据一致性、依赖、控制和回退条件；WP为准备/演练工作。日期为候选计划，不等于进入批准；多个运营条件仍未知，不能标为已可运营。','evidence':evidence((RAW,'进入条件是接口验证、业务接受标准与回退安排就绪，不以计划日期代替可运营条件。'),(BUILD,"implementation_strategy='受控试点；先明确接受条件和异常责任，再验证接口并决定是否进入候选运营状态'"))},
 {'id':'C08','topic':'技能发展不自动升级','status':'source-design-consistent','observation_zh':'版本2保留历史观察并增加任务要求变更记录，更新实践与复评；输出rating_change=not-inferred。支持专家对新增离线行为也不自动视为满足。','evidence':evidence((BUILD,"'rationale':'新增离线恢复目标，保留旧评价并更新实践/复评计划；没有新增能力评级'"))}]
findings=[
 {'id':'F01','priority':'P1','kind':'independent-evidence-gap','status':'open-in-original-input','title_zh':'专家4级只有同一条3级任务行为，未独立证实等级','observation_zh':'OBS-EXPERT直接给4级，唯一行为与REQ-SKILL-SOL的3级条件相同；无相应更高层行为/组织认可内容。基线运行给evidence-contract-complete和expert-evidence-recorded，只说明声明结构完整；本独立审阅不能将它视为4级或专家支持资格已经证实。','impact_zh':'若把该记录用于认定指导/补足人员能力，会高估可用支持；目前assignment仍未批准，尚未造成自动配置批准。','recommendation_zh':'保留原4级为历史声明，将当前观察设为证据不足或补真实相应证据；不因不能证实4级自动降3。专家能力、组织认可和可用容量分别记录。','evidence':evidence((RAW,'技能目标、实际行为证据、组织认可与可用容量分别记录'),(INPUTS,'"id": "OBS-EXPERT"'),(INPUTS,'"proficiency": 4'),(INPUTS,'"criterion": "独立完成异常接口设计并经评审"'))},
 {'id':'F02','priority':'P2','kind':'source-scope-drift','status':'open-in-original-input','title_zh':'企业架构师元数据遗漏物流分段','observation_zh':'原始委托为订单、库存、物流；ROLE-EA.scope及TASK-EA.decision变为订单、库存、门店。构建器决策议程又写订单/库存/物流，形成不同视图责任口径不一致。','impact_zh':'物流确认交接与跨分段风险的协调责任可能只留在说明正文，而不进入角色任务定义。','recommendation_zh':'恢复订单/库存/物流主责任范围，门店作为受影响渠道一并列明；沿用同一个ROLE-EA及TASK-EA。','evidence':evidence((RAW,'企业架构师协调订单、库存、物流三分段'),(INPUTS,'"scope": "跨订单、库存和门店能力"'),(INPUTS,'"decision": "确定订单、库存与门店之间的责任和约束"'))},
 {'id':'F03','priority':'P2','kind':'authority-source-gap','status':'open-in-original-input','title_zh':'架构委员会被添加为决策主体但委托无此授权','observation_zh':'MANDATE-STOCK将decision_owner写作架构委员会与库存业务负责人并引CASE-MANDATE；原文只说经营负责人委托分析，没有指定架构委员会或授予该组织审批权。','impact_zh':'候选治理建议可能被读成现有真实授权，形成证据来源错配。','recommendation_zh':'标记拟议治理责任待经营负责人确认，或补明确虚构授权材料；不以AI审阅代替确认。','evidence':evidence((RAW,'经营负责人委托架构团队分析跨分段影响并提交候选方案'),(INPUTS,'"decision_owner": "架构委员会与库存业务负责人"'))},
 {'id':'F04','priority':'P1','kind':'assignment-period-and-capacity-gap','status':'open-in-original-design','title_zh':'人员有效期未覆盖离线试点后半段','observation_zh':'ASSIGN-A有效期到2026-11-30，离线工作包/过渡计划到2026-12-04。工作量未知，40小时以及专家8小时不能说明整个期间覆盖。当前分析正确保留容量未知，但没有具体指出12月1日至4日覆盖未定。','impact_zh':'只按as_of核对有效性，会漏掉试点后半段人员与异常处理覆盖。','recommendation_zh':'在候选计划列为期间覆盖缺口，确认工作量、实际排期、续任/交接及专家容量；不能为通过检查直接延长有效期或补造估算。','evidence':evidence((INPUTS,'"valid_until": "2026-11-30"'),(INPUTS,'"available_hours": 40'),(BUILD,"entity('WP-OFFLINE', 'work_package', '断连与恢复演练', owner='方案团队', start='2026-11-21', end='2026-12-04'"))},
 {'id':'F05','priority':'P2','kind':'risk-control-scope-gap','status':'open-in-original-design','title_zh':'门店持久化控制被单一中央库存控制范围吞并','observation_zh':'断连版风险控制包括持久队列、检查点、冲突检测与人工补偿，但DELIVERY-NOTE的唯一CTRL-STOCK全部applies_to=APP-STOCK；APP-STORE和LOCAL-ORDER-RECORD的本地持久成功/掉电丢失风险没有对应控制范围。','impact_zh':'风险控制表可能误导为中央库存控制已覆盖本地断连数据丢失，即使详细恢复契约保留了未知。','recommendation_zh':'拆分门店持久记录控制与中央接收去重/对账控制；分别引用应用、记录边界、未决责任和验证场景，不虚构已通过。','evidence':evidence((RAW,'风险至少包括库存冲突、重复执行、断连数据丢失与恢复后长时间未对账'),(BUILD,"controls=[dict(id='CTRL-STOCK',risk_id='RISK-STOCK',statement=next(e for e in es if e['id']=='RISK-STOCK')['attributes']['control'],applies_to='APP-STOCK')]"))},
 {'id':'F06','priority':'P2','kind':'generic-change-propagation-limit','status':'open-capability-boundary','title_zh':'角色技能传播来自案例分支，图影响尚未覆盖','observation_zh':'REQ-OFFLINE的图可达结果有22个领域对象，不含DEV-A、DELIVERY-NOTE、任务技能目标或角色配置上下文；这些虽在本案例被显式分支更新，但影响引擎未给出相应依赖路径。','impact_zh':'本案例正确输出不能证明任意需求变化都能自动传递到技能目标和复评。','recommendation_zh':'补typed依赖或增加独立的任务/目标/发展引用影响分析；继续将图可达标为候选而非已证实全部影响。','evidence':evidence((BUILD,"if model['project']['version']=='2':"),(BUILD,"delta=impact(changed_model,['REQ-OFFLINE'],max_depth=len(changed_model['entities']))"))},
 {'id':'F07','priority':'P2','kind':'role-target-derivation-improvement','status':'open-evidence-improvement','title_zh':'四个角色均采用3级，裁剪依据仍过于通用','observation_zh':'每条目标说明均为虚构主管采用3级，只有一条工作行为；已经正确区分原表参考与项目目标，但尚未解释任务复杂性、独立完成程度、所需复核和为何该级足够。','impact_zh':'可复用到真实项目时，容易退化为将等级字段填满而不是从工作要求推导目标。','recommendation_zh':'为每项任务补可观察的完成标准、预期独立性/支持条件和项目采用理由；如无决定保持拟议目标，不能让AI独立认可。','evidence':evidence((INPUTS,'虚构角色主管针对本次候选分析采用3级；不是原表直接批准。'),(INPUTS,'"behavioral_criteria": ['))}]
result={'schema_version':'independent-business-case-review/1','reviewer_kind':'independent-AI-source-and-design-review','business_approval':'not-granted','person_certification':'not-granted','deployment_authorization':'not-granted','overall_status':'candidate-design-with-material-evidence-and-scope-gaps','scope_zh':'先从三份原始教学材料与案例生成设计逐项推导期望，再以只读内存build/evaluate/impact核对结果；未把schema通过当业务验收。未修改skills目录。','source_snapshots':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [RAW,INPUTS,BUILD]],'checks':checks,'findings':findings,'readonly_runtime_observations':{'schema_validator_used_for_acceptance':False,'generated_files_created_by_reviewer':False,'assessment_summary':{n:{'task_sol':next(x for x in a['task_routes'] if x['id']=='TASK-SOL')['state'],'assignment_state':a['assignment_reviews'][0]['state'],'capacity_state':a['assignment_reviews'][0]['capacity_state'],'approval':a['assignment_reviews'][0]['approval'],'support_reviews':a['assignment_reviews'][0]['support_reviews'],'rating_change':a['development_reviews'][0]['rating_change'],'gap_reasons':[x['reason'] for x in a['gaps']]} for n,a in assessments.items()},'impact_candidate_count':len(impact['candidates']),'impact_candidate_ids':[x['id'] for x in impact['candidates']],'impact_notice':impact['notice']},'generated_artifact_review':{'status':'pending-root-generation','path':'togaf-standard-10th-ai/maintenance/cases/omnichannel/generated','limits_zh':'当前独立结论针对来源和构建设计，尚未声明最终生成目录、图形版式或修订副本已验收。'},'business_decisions_still_needed_zh':['超卖容忍、一致性及受理/承诺边界','离线额度、断连时长、可容忍丢失窗口与恢复对账目标','库存冲突、重复提交、补偿、回退的责任与接受标准','预算、人员工作量、有效期及支持容量','角色技能目标的项目认可与真实行为/组织认可证据'],'review_limit_zh':'所有材料是虚构教学资料。独立AI审阅可识别逻辑和证据缺口，不授予真实业务批准、人员评级或上线权限。'}
result=runpy.run_path(str(OUT/'generated_review.py'))['augment'](result)
(OUT/'independent-review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
def link(e):return '['+e['path'].split('/')[-1]+':'+str(e['line'])+']('+str(ROOT/e['path'])+':'+str(e['line'])+')'
lines=['# 全渠道案例独立来源与设计审阅','', '状态：F08主制品主体缺失已在本地案例修复，人员覆盖与专业证据缺口仍保留。首次独立审阅与修复作者自检分别记录；不是业务批准、人员认证或上线授权。','', result['scope_zh'],'', '## 原始材料支持的结论','']
for c in checks:lines.append('- **'+c['topic']+'**：'+c['observation_zh'])
lines+=['','## 原始问题与修订复核','', 'F01–F07保留首次对只读原材料的观察；每项后附当前本地修订与生成结果，避免把已修订问题误报为仍未处理。F08–F09为本次生成结果复核新增。','']
for f in result['findings']:
 lines += ['### '+f['id']+' · '+f['priority']+' · '+f['title_zh'],'',f['observation_zh'],'', '影响：'+f['impact_zh'],'','建议：'+f['recommendation_zh'],'','证据：'+'；'.join(link(e) for e in f['evidence']),'']
 if f.get('generated_resolution'):
  g=f['generated_resolution']
  lines+=['当前复核：**'+g['status']+'**。'+g['observation_zh'],'','当前证据：'+'；'.join(link(e) for e in g['evidence']),'']
gr=result['generated_artifact_review']
lines+=['## 生成结果复核','','|输出|视图|实体|关系|schema错误|渲染状态|','|---|---:|---:|---:|---:|---|']
for name,s in gr['generation_summary'].items():
 lines.append('|'+name+'|'+str(s['views'])+'|'+str(s['entities'])+'|'+str(s['relationships'])+'|'+str(len(s['validation_findings']))+'|'+('已运行' if s['rendered'] else '未运行')+'|')
lines+=['', '上述数字是生成执行记录，不构成业务或内容充分性验收。','']
for c in gr['checks']:
 lines+=['- **'+c['id']+' · '+c['topic']+'**：'+c['observation_zh'],'  证据：'+'；'.join(link(e) for e in c['evidence'])]
lines+=['','## 审阅范围与未完成部分','',gr['limits_zh'],'',result['review_limit_zh']]
(OUT/'independent-review.md').write_text('\n'.join(lines)+'\n')
print('Wrote independent review:',len(checks),'source checks,',len(gr['checks']),'generated checks,',len(result['findings']),'findings; status:',gr['status'])
