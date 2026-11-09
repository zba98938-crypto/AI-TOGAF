# -*- coding: utf-8 -*-
"""Business invariants from raw fictional inputs plus source-linked guide methods."""
from pathlib import Path
import json,hashlib,copy,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;C=HERE.parents[2]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ent(m,i):return next(x for x in m['entities'] if x['id']==i)
def rel(m,i):return next(x for x in m['relationships'] if x['id']==i)
def text(x):return json.dumps(x,ensure_ascii=False)
models={n:read(HERE/'generated'/n/'model.json') for n in ['baseline','offline-change','shared-object-change']};base,off,changed=[models[x] for x in models]
links=[('G184','G184:chapter-review:4.2.6:rule03','工作委托不等于审批权','DELIVERY-NOTE decision_agenda及人员配置approval'),('G186','G186:3.2:rule01','在相互竞争偏好间准备知情权衡','同步/异步候选比较，缺一致性不排名'),('G186','G186:5.1.1:rule01','候选状态与批准目标分开','所有版本project.approval_status=candidate'),('G188','G188:3.2.7:rule06','排程需要依赖、工期、资源与约束','WP-OFFLINE/ASSIGN-A期间与容量缺口'),('G248','G248:3.1:rule02','选择和排除构建块保留理由与影响','在线同步可保留，纯同步无法单独覆盖离线'),('G233','G233:3.3:rule01','共享元素目录支持跨域追踪','CAP-RESERVE稳定ID投影到目录/矩阵/图/路线图'),('G233','G233:7.2:rule03','交付时间依据真实容量确认','工时未知不宣称排程可行'),('G249','G249:3:rule02','任务需求到角色技能与证据','四任务、目标/观察/配置/发展分别记录')]
source_links=[]
for code,rid,meaning,output in links:
 p=C/'chapters'/f'{code}.json';d=read(p);rule=next(r for s in d['sections'] for r in s.get('semantic_rules',[]) if r['id']==rid);source_links.append({'guide':code,'rule_id':rid,'rule':rule,'published_sha256':sha(p),'case_interpretation_zh':meaning,'output_binding':output,'relation_origin':'project-derived-guide-to-case-mapping'})
checks=[]
def check(name,condition,detail):
 checks.append({'id':name,'passed':bool(condition),'evidence':detail})
online_spec=next(s for s in ent(base,'DELIVERY-NOTE')['attributes']['specifications'] if s['id']=='SPEC-ONLINE')
check('candidate-no-ranking',base['project']['approval_status']=='candidate' and all(s in online_spec['statement'] for s in ['候选A','候选B','没有一致性标准，无法定优']) and online_spec['requirement_id']=='REQ-CONSISTENCY' and ent(base,'REQ-CONSISTENCY')['attributes']['status']=='needs-input','CASE-BASELINE缺少一致性与承诺目标；候选A/B仍保留，且SPEC-ONLINE明确记录不可定优并追溯REQ-CONSISTENCY。')
check('offline-interface-risk-transition-tests',all(any(e['id']==i for e in off['entities']) for i in ['REQ-OFFLINE','IF-RECOVERY','TRANS-OFFLINE','WP-OFFLINE','LOCAL-ORDER-RECORD','CENTRAL-ORDER-RECORD']) and ent(off,'RISK-STOCK')!=ent(base,'RISK-STOCK') and len(ent(off,'DELIVERY-NOTE')['attributes']['recovery_contract']['verification_scenarios'])>=7,'CASE-CHANGE要求断连受理；接口、存储、风险、过渡及恢复演练联动。')
check('online-sync-still-candidate',ent(off,'IF-RESERVE')['attributes']['protocol']==ent(base,'IF-RESERVE')['attributes']['protocol'] and any(r['id']=='USE-RESERVE' for r in off['relationships']),'离线约束未把在线同步能力一概删除。')
check('confirmed-before-logistics',[(r['source'],r['target']) for r in off['relationships'] if r['type']=='transitions_to' and r['target']=='ORDER-FULFIL']==[('ORDER-CONFIRMED','ORDER-FULFIL')],'原始材料明确物流只使用确认订单；无待确认直达物流边。')
controls=ent(off,'DELIVERY-NOTE')['attributes']['controls'];check('local-central-controls-separated',any('APP-STORE' in c['applies_to'] and 'LOCAL-ORDER-RECORD' in c['applies_to'] for c in controls) and any('APP-STOCK' in c['applies_to'] and 'IF-RECOVERY' in c['applies_to'] for c in controls),'门店掉电/丢失与中央重放/对账分属不同候选控制范围，责任待确认。')
check('capacity-and-period-open',all(t['workload_hours'] is None for t in off['analyses'][0]['inputs']['tasks']) and any(g['id']=='GAP-ASSIGNMENT-PERIOD' for g in off['gaps']),'ASSIGN-A11/30到期，离线工作包12/04；不延长配置或凭可用小时认定充分。')
a=read(HERE/'generated/offline-change/role-assessment.json')['result'];check('observations-not-upgraded',all(x['proficiency'] is None for x in off['analyses'][0]['inputs']['assessments']) and all(x['proficiency'] is None for x in base['analyses'][0]['inputs']['assessments']) and 'not-inferred' in text(a['development_reviews']),'培训/新增目标不提高人员等级；甲和专家当前均缺充分评价证据。')
check('role-scope-and-decisions', '物流' in next(r for r in off['analyses'][0]['inputs']['roles'] if r['id']=='ROLE-EA')['scope'] and all(d['status']=='pending-decision' for d in ent(off,'DELIVERY-NOTE')['attributes']['decision_agenda']),'经营、跨分段及库存决策都有待定输入，未编造委员会授权。')
impact=text(read(HERE/'generated/change-impact.json'));check('impact-includes-role-development-decisions',all(x in impact for x in ['ROLE-SOL','DEV-A','DELIVERY-NOTE']),'影响遍历包含技能发展与决策上下文；可达仍仅代表人工复核候选。')
p=read(HERE/'generated/shared-object-change/shared-object-projections.json');new=ent(changed,'CAP-RESERVE');previous=ent(off,'CAP-RESERVE');check('shared-object-id-stable',new['id']==previous['id'] and new['name']!=previous['name'] and new['attributes']['definition']!=previous['attributes']['definition'],'实际变更名称与定义，保持CAP-RESERVE身份。')
check('catalog-matrix-roadmap-agree',all(all(e['name']==new['name'] and e['definition']==new['attributes']['definition'] for e in p[k] if e['capability_id']=='CAP-RESERVE') for k in ['catalog','capability_application_matrix','roadmap']) and all(any(e['capability_id']=='CAP-RESERVE' for e in p[k]) for k in ['catalog','capability_application_matrix','roadmap']),'三种投影均有变更后的同一对象，未靠空集合通过。')
svg=(HERE/'generated/shared-object-change/artifacts/capability-map.svg').read_text();payload=read(HERE/'generated/shared-object-change/artifacts/capability-map.json');check('diagram-agrees-with-object',new['name'] in svg and any(e['id']=='CAP-RESERVE' and e['name']==new['name'] and e['attributes']['definition']==new['attributes']['definition'] for e in payload['entities']),'可编辑SVG标签及制品JSON定义均更新；第三版现已同时生成PNG；PNG视觉记录单独核对。')
# Reject meaningful adverse variants rather than merely matching field presence.
def business_gate(m):
 errors=[]
 if any(r['type']=='transitions_to' and r['source']=='ORDER-PENDING' and r['target']=='ORDER-FULFIL' for r in m['relationships']):errors.append('unconfirmed-order-to-logistics')
 if m['project']['approval_status']!='candidate' and ent(m,'REQ-CONSISTENCY')['attributes']['status']=='needs-input':errors.append('approval-with-unresolved-consistency')
 return errors
for case,mutate,expected in [('bypass-confirmation',lambda m:m['relationships'].append({'id':'INVALID','source':'ORDER-PENDING','target':'ORDER-FULFIL','type':'transitions_to'}),'unconfirmed-order-to-logistics'),('premature-approval',lambda m:m['project'].update(approval_status='approved'),'approval-with-unresolved-consistency')]:
 m=copy.deepcopy(off);mutate(m);check(case,expected in business_gate(m),'针对原始业务约束注入反例，必须被本地案例接受门槛拒绝。')
result={'schema_version':'cross-guide-case-verification/1','passed':all(x['passed'] for x in checks),'checks':checks,'source_method_links':source_links,'source_inputs':{n:sha(HERE/n) for n in ['raw-business-materials.md','role-skill-inputs.json','run.py','base_build.py','assignment_expression.py']},'model_sha256':{n:sha(HERE/'generated'/n/'model.json') for n in models},'business_approval':'not-granted','limits_zh':['本地业务反例门槛和投影为本案例的显式项目实现，不声称官方指定算法。','测试证明限定断言，独立原始材料审阅另见independent-review.md及F08复核。','共享对象修改是名称/定义一致性验证，不等于变更业务政策后的所有影响自动得到正确设计。','真实一致性、容量、技能能力与审批仍缺依据。']}
(HERE/'generated/cross-guide-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'checks':len(checks),'failed':[x for x in checks if not x['passed']]},ensure_ascii=False,indent=2));raise SystemExit(0 if result['passed'] else 1)
