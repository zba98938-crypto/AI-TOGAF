# -*- coding: utf-8 -*-
"""Authored sufficient fictional case; no generated claim of actual business approval."""
from pathlib import Path
import json,copy,sys,hashlib
sys.dont_write_bytecode=True
H=Path(__file__).resolve().parent;C=H.parents[2];S=C/'skills/_shared';sys.path[:0]=[str(S/'scripts'),str(S/'vendor'),str(H)]
import base_build as base
from assignment_projection import prepare
from g249_reasoning import review_role_skills
from generate import generate
from validate import validate
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def inputs():
 d=json.loads((H/'role-skill-inputs.json').read_text());d['scope']='输入充分的虚构全渠道实验：已声明政策、行为及同期工作量';d['as_of']='2026-12-04';d['mandate'].update(decision_owner='虚构经营责任人；仅用于实验的责任声明',authority_status='fictional-analysis-mandate-not-real-approval')
 d['source_ids']+=['FICTIONAL-POLICY','FICTIONAL-BEHAVIOR','FICTIONAL-CAPACITY'];d['tasks'][-1]['required_skill_ids']=[d['requirements'][-1]['skill_id']];d['tasks'][-1]['decision']='依据声明的一致性与延迟目标比较线上同步及异步最终确认；离线仅受理待确认';d['tasks'][-1]['outcome']='线上同步试点建议、离线待确认契约及异常验证清单'
 d['tasks'][1].update(decision='核查中央承诺、门店待确认及物流确认门槛之间的跨分段一致性',outcome='跨分段责任和接口政策核对记录')
 d['tasks'][2].update(decision='在给定限量与期限政策下审查库存及恢复行为',outcome='库存确认、过期隔离和人工处理条件')
 hours=[8,16,24,32];available=[10,20,28,40];d['assessments']=[];d['assignments']=[]
 for i,(t,r) in enumerate(zip(d['tasks'],d['requirements'])):
  t.update(work_period={'start':'2026-11-09','end':'2026-12-04'},workload_hours=hours[i]);t['evidence']+=['FICTIONAL-POLICY','FICTIONAL-CAPACITY'];person='PERSON-'+['CH','EA','SEG','A'][i];oid='BEH-'+['CH','EA','SEG','SOL'][i]
  obs={'id':oid,'person_ref':person,'skill_id':r['skill_id'],'assessment_kind':'observed_assessment','assessment_state':'assessed','proficiency':3,'scale_id':'G249-table5-1','task_refs':[t['id']],'observed_on':'2026-12-02','assessor':'FICTIONAL-PEER-REVIEW','evidence':['FICTIONAL-BEHAVIOR'],'behavioral_evidence':[{'criterion':s,'demonstrated':True,'evidence_kind':'reviewed-work-product','evidence':['FICTIONAL-BEHAVIOR']} for s in r['behavioral_criteria']],'note':'本任务行为已在虚构材料中给定；困难情形仍需专家，不表示通用认证。'}
  d['assessments'].append(obs);d['assignments'].append({'id':'ASSIGN-'+['CH','EA','SEG','A'][i],'person_ref':person,'role_ref':r['role_ref'],'task_refs':[t['id']],'requirement_refs':[r['id']],'assessment_refs':[oid],'mandate_ref':d['mandate']['id'],'authority':'虚构候选配置；真实批准未授予','valid_from':'2026-11-09','valid_until':'2026-12-04','available_hours':available[i],'evidence':['FICTIONAL-CAPACITY','CASE-MANDATE']})
 dev=d['development'][0];dev.update(current_proficiency=3,behavioral_gap='历史上缺异常设计评审证据；本次新增行为观察另列，不覆盖旧记录',action='11月10日课程；11月29日提交实践；12月02日独立评审',due='2026-12-03');dev['reassessment'].update(status='completed',due_on='2026-12-02',assessment_ref='BEH-SOL',evidence=['FICTIONAL-BEHAVIOR']);dev['history'].append({'observed_on':'2026-11-10','status':'course-completed-no-rating-change','rationale':'仅完成课程，尚未新增实践行为证据，保留原未评价状态','proficiency':None,'evidence':['CASE-PERSON']});dev['history'].append({'observed_on':'2026-12-02','status':'assessed','rationale':'虚构材料明确给出任务实践、异常分析和独立评审记录，按对应行为准则本次评价3级','assessment_ref':'BEH-SOL','proficiency':3,'evidence':['FICTIONAL-BEHAVIOR']})
 d['example_notice']='所有材料、行为、容量均为虚构教学输入；真实批准未授予';return d

def policy_projection(version):
 return {'policy_id':'POLICY-STOCK','policy_version':version,'capability_id':'CAP-RESERVE','offline_item_limit':2 if version=='v1' else 1,'max_pending_hours':24 if version=='v1' else 8,'confirmation':'central-atomic-reservation-only','logistics_entry':'ORDER-CONFIRMED','origin':'explicit-fictional-business-material','real_business_approval':'not-granted'}
def build(version):
 # Reuse shared domain IDs, not a parallel mock model.
 m=base.domain_model(True);d=inputs();entity={e['id']:e for e in m['entities']};policy=policy_projection(version)
 m['relationships'] += [base.edge('WP-ONLINE-CAP','traces_to','WP-ONLINE','CAP-RESERVE','在线试点实施库存能力政策'),base.edge('WP-OFFLINE-CAP','traces_to','WP-OFFLINE','CAP-RESERVE','断连恢复演练核对同一库存能力政策')]
 for rel in m['relationships']:
  if rel['type']=='transitions_to' and rel['target']=='ORDER-CONFIRMED':rel['label']='中央原子预占成功，确认ID与订单唯一关联'
 entity['REQ-CONSISTENCY']['attributes'].update(statement='中央原子预占后才确认，总承诺不得超过可用；线上确认p95≤300ms',status='fictional-input-provided',acceptance='固定虚构1000请求集：不超量且确认p95≤300ms')
 entity['REQ-OFFLINE']['attributes'].update(statement='离线仅持久受理待中央确认，限量及期限按POLICY-STOCK',status='fictional-input-provided',acceptance='额度、超时、重放、冲突及回退演练')
 entity['CAP-RESERVE']['attributes'].update(policy=policy,definition='按中央原子预占确认；离线持久受理与最终承诺分离')
 entity['IF-RESERVE']['attributes'].update(payload='order_id, sku, quantity, idempotency_key；中央原子预占成功返回reservation_id后才最终确认')
 entity['IF-EVENT']['attributes'].update(payload='event_id, order_id, sku, quantity；中央原子预占后最终确认；虚构p95=420ms，不满足本次线上300ms目标')
 entity['ORDER-PENDING']['attributes'].update(exit='中央原子预占成功则确认；超额、过期、库存不足或身份冲突转异常')
 entity['ORDER-CONFIRMED']['attributes'].update(entry='中央原子预占成功，确认ID与订单唯一关联')
 entity['TRANS-ONLINE']['attributes'].update(definition='虚构实验推荐同步A的受控线上试点；成本及生产性能仍待验证',operating_conditions={'operations':'虚构库存运营值守并处理异常','data_consistency':'中央原子预占后确认，总承诺不超过可用量','dependencies':'固定虚构测试集已给定；生产契约与负载需另验','controls':'幂等、库存不足及隔离审计','rollback':'停止新试点订单，保留存量逐笔核对'})
 entity['TRANS-OFFLINE']['attributes']['definition']='按当前版本限量和期限持久受理待确认；中央重验库存后确认，过期及冲突转人工'
 entity['IF-RECOVERY']['attributes'].update(policy=policy,payload='event_id, order_id, sku, quantity, accepted_at, policy_version；按'+version+'核对限量与期限')
 entity['RISK-STOCK']['attributes'].update(policy=policy,risk='旧政策事件、过期受理及库存冲突',control='按'+version+'隔离超额/过期，中央重验库存；不把待确认订单发物流')
 entity['TRANS-OFFLINE']['attributes'].update(policy=policy,operating_conditions={'operations':f"库存运营每班巡检队列；{policy['max_pending_hours']}小时临界记录进入人工处理",'data_consistency':'中央原子预占成功才确认','dependencies':'版本化接口和混合队列演练','controls':'幂等、超额、过期与冲突隔离','rollback':'停止新离线受理，保留存量逐笔对账'})
 note=entity['DELIVERY-NOTE']['attributes'];note['policy']=policy;note['operations']={'pending_item_limit':policy['offline_item_limit'],'max_pending_hours':policy['max_pending_hours'],'owner':'虚构库存运营负责人','escalation':'超额/过期隔离并人工联系，不自动发货'};note['validation_scenarios']=[{'id':'TEST-LIMIT','policy_version':version,'accept_quantity':policy['offline_item_limit'],'exception_quantity':policy['offline_item_limit']+1},{'id':'TEST-EXPIRY','policy_version':version,'boundary_hours':policy['max_pending_hours']},{'id':'TEST-DUPLICATE','policy_version':version,'expect':'同事件同订单幂等，不同订单隔离'},{'id':'TEST-FULFIL','policy_version':version,'expect':'只允许确认订单进入物流'}];note['decision']={'selected_online_option':'A-central-synchronous','basis':'fictional 1000-request experiment; p95 A160/B420 vs target300; both central no-overcommit','scope':'online pilot only','offline':'received-pending-central-confirmation','unproven':['production latency','cost','scaling'],'approval':'not-granted'}
 note['requirements']=[{**r,'statement':entity[r['id']]['attributes']['statement']} for r in note['requirements']]
 note['specifications'][0]['statement']='A在中央原子预占后确认，虚构p95=160ms；B待中央确认p95=420ms；本次300ms线上目标下推荐A，生产性能仍待测。'
 note['specifications'][1]['statement']='离线持久受理待确认，按'+version+'限量和期限核验，重连去重且中央重新验库存；超限、过期和冲突转人工。'
 note['gaps']=[]
 note['architecture_summary']['information']['reason']='本次政策及恢复目标已由虚构材料给定；完整数据模型、安全和生产验证仍待工程补充。'
 note['recovery_contract'].update(policy=policy,replay='按event_id/order_id去重；超过当前policy期限隔离',reconciliation='中央重验库存后确认；同事件不同订单隔离，运营人工逐笔核对',status='fictional-design-evidenced-production-unverified')
 for agenda in note['decision_agenda']:
  if agenda['id'] in {'DEC-CROSS-SEGMENT','DEC-STOCK'}:
   agenda.update(status='fictional-policy-provided-real-approval-not-granted',needed_input=['实际责任人签认与工程验证'],evidence=['FICTIONAL-POLICY'])
 m['gaps']=[g for g in m['gaps'] if g['id'] not in {'GAP-CONSISTENCY','GAP-LOCAL-QUOTA','GAP-RECOVERY'}]
 # Build the role/artifact structure using this case's explicit sufficient input file.
 m['project']['version']='1';dump(H/'sufficient-role-skill-inputs.json',d)
 m=base.attach_role_assessment(m,H/'sufficient-role-skill-inputs.json',configuration_mode='generic')
 m['project']['version']='fictional-'+version;m['project']['name']='输入充分的虚构全渠道履约 '+version
 for rel in m['relationships']:
  if rel['id']=='CONSTRAINT-SEG':rel['label']='库存边界与'+version+'一致性政策'
  if rel['id']=='HANDOFF-IF':
   rel['label']='交接已声明接口与验证条件'
   rel['attributes']['acceptance_criteria']=['能力边界、接口政策和验证条件追溯至虚构原始材料']
 for src in m['sources']:
  if src['id'] in {'example-source','CASE-PERSON','CASE-EXPERT','CASE-ROLE-TARGET'}:src['locator']='sufficient-role-skill-inputs.json'
  if src['id'].startswith('FICTIONAL-'):src['locator']='sufficient-business-materials.md';src['description']='明确虚构的政策、行为或容量声明'
 from verify_semantic_change import synchronize_domain
 synchronize_domain(m)
 m=prepare(m,view_id='role-assignment')
 # Recompute stale legacy case labels from the new evidence states.
 for e in m['entities']:
  if e['id']=='DEV-A':e['attributes'].update(start='2026-11-10',end='2026-12-03')
  if e['id'] in {a['id'] for a in d['assignments']}:
   e['attributes'].update(competence_state='evidenced-for-declared-task',period_gap='declared task period covered; real approval not-granted',workload_hours=next(t['workload_hours'] for t in d['tasks'] if t['id'] in e['attributes']['task_refs']))
  if e['id'] in {t['id'] for t in d['tasks']}:e['attributes']['configuration_status']='declared workload and behavioral evidence present; owner review pending'
 # Model snapshots are explicit and synchronized after editorial projection changes.
 from verify_semantic_change import synchronize_domain
 synchronize_domain(m)
 return prepare(m,view_id='role-assignment')
def main():
 results={}
 for version in ['v1','v2']:
  m=build(version);errors=[x for x in validate(m) if x['level']=='error'];assert not errors,errors
  result=review_role_skills(m['analyses'][0]['inputs']);assert not result['gaps'],result['gaps']
  dest=H/'generated'/('sufficient' if version=='v1' else 'sufficient-policy-change');generate(m,dest,all_items=True,render=True,strict=True);dump(dest/'role-assessment.json',result);dump(dest/'policy-projections.json',{'policy':policy_projection(version),'interface':next(e for e in m['entities'] if e['id']=='IF-RECOVERY')['attributes'],'risk':next(e for e in m['entities'] if e['id']=='RISK-STOCK')['attributes'],'operations':next(e for e in m['entities'] if e['id']=='DELIVERY-NOTE')['attributes']['operations'],'transition':next(e for e in m['entities'] if e['id']=='TRANS-OFFLINE')['attributes'],'scenarios':next(e for e in m['entities'] if e['id']=='DELIVERY-NOTE')['attributes']['validation_scenarios']})
  from run import write_projections
  write_projections(dest,m)
  results[version]={'structural_errors':0,'declared_evidence_gaps':0,'assignments':[{'id':a['id'],'state':a['state'],'capacity':a['capacity_state'],'period':a['period_state'],'approval':a['approval']} for a in result['assignment_reviews']],'development':result['development_reviews'],'source_material_sha256':sha(H/'sufficient-business-materials.md'),'limits_zh':'虚构材料给定的事实可复算；不证明真实人员能力、生产性能或实际批准。'}
 dump(H/'sufficient-results.json',results);print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
