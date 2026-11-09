# -*- coding: utf-8 -*-
"""Forward checks against raw fictional materials, separate from the case builder.

This verifier imports no builder/generator/evaluator: declared input evidence is
compared directly to generated decisions and shared-object projections.
"""
from pathlib import Path
import json,re,copy,hashlib,sys
sys.dont_write_bytecode=True
H=Path(__file__).resolve().parent;C=H.parents[2];S=C/'skills/_shared';sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
from policy_consistency import check,classify_change
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 raw=(H/'sufficient-business-materials.md').read_text();checks=[]
 def ensure(ok,msg):
  if not ok:raise AssertionError(msg)
 def test(i,f):
  try:r=f();checks.append({'id':i,'passed':True,'actual':r})
  except Exception as e:checks.append({'id':i,'passed':False,'actual':str(e)})
 models={v:read(H/'generated'/n/'model.json') for v,n in [('v1','sufficient'),('v2','sufficient-policy-change')]};models['unknown']=read(H/'generated/offline-change/model.json')
 def entities(m):return {x['id']:x for x in m['entities']}
 def expected_online():
  values=re.search(r'A确认p95=(\d+)ms，B最终确认p95=(\d+)ms',raw);limit=re.search(r'p95≤(\d+)ms',raw);ensure(values and limit,'raw performance targets not located');a,b=map(int,values.groups());budget=int(limit[1]);ensure(a<=budget<b,'cannot uniquely recommend A against this constraint');return {'option':'A-central-synchronous','A_p95':a,'B_p95':b,'limit':budget}
 def decisions():
  x=expected_online();note=entities(models['v1'])['DELIVERY-NOTE']['attributes'];ensure(note['decision']['selected_online_option']==x['option'],'recommendation contradicts raw target');ensure(note['decision']['scope']=='online pilot only','overgeneralized recommendation');ensure(note['decision']['approval']=='not-granted','invented approval');return x
 test('recommendation-from-raw-target-and-experiment',decisions)
 def unknown():
  note=entities(models['unknown'])['DELIVERY-NOTE']['attributes'];ensure('selected_online_option' not in note.get('decision',{}),'selected with absent basis');ensure(entities(models['unknown'])['REQ-CONSISTENCY']['attributes']['status']=='needs-input','unknown erased');return 'no optimum selected'
 test('unknown-case-retains-missing-consistency',unknown)
 def staffing():
  inputs=read(H/'sufficient-role-skill-inputs.json');ensure('依次10、20、28、40小时' in raw and '8小时、企业级16小时、库存分段24小时、解决方案32小时' in raw,'raw capacity missing');available=[10,20,28,40];work=[8,16,24,32]
  actual= models['v1']['analyses'][0]['inputs']
  for section,fields in [('tasks',['work_period','workload_hours','decision','outcome']),('assignments',['valid_from','valid_until','available_hours'])]:
   for expected in inputs[section]:
    generated=next(row for row in actual[section] if row['id']==expected['id'])
    for field in fields:ensure(expected.get(field)==generated.get(field),'generated '+expected['id']+'.'+field+' differs from raw fixture')
  for i,(a,t) in enumerate(zip(inputs['assignments'],inputs['tasks'])):
   ensure(a['available_hours']==available[i]>=t['workload_hours']==work[i],'capacity mismatch');ensure(a['valid_from']<=t['work_period']['start'] and a['valid_until']>=t['work_period']['end'],'period mismatch')
  report=read(H/'sufficient-results.json')['v1'];ensure(all(x['state']=='ready-for-owner-review' and x['approval']=='not-granted' for x in report['assignments']),'false approval or unresolved expected capacity');return {'roles':4,'period':'2026-11-09/2026-12-04','real_approval':'not-granted'}
 test('capacity-and-period-from-raw-material',staffing)
 def development():
  d=read(H/'sufficient-role-skill-inputs.json');dev=d['development'][0];history=dev['history'];ensure(history[0]['proficiency'] is None,'history lost');ensure(any(h['status']=='course-completed-no-rating-change' and h['proficiency'] is None for h in history),'course auto upgraded');obs=next(o for o in d['assessments'] if o['id']==dev['reassessment']['assessment_ref']);ensure(obs['assessor']=='FICTIONAL-PEER-REVIEW' and obs['observed_on']=='2026-12-02','new independent fictional review absent');ensure(all(b['demonstrated'] and b['evidence_kind']=='reviewed-work-product' for b in obs['behavioral_evidence']),'training substituted for work');return 'unknown -> course/no change -> new behavior review; not runtime-inferred promotion'
 test('development-reassessment-traces-new-behavior',development)
 contract={'schema_version':'shared-policy-projection/1','source_ids':['FICTIONAL-POLICY'],'policy_object_ref':'CAP-RESERVE','policy_path':['attributes','policy'],'projections':[{'entity_ref':i,'path':['attributes','policy'],'policy_fields':['policy_id','policy_version','offline_item_limit','max_pending_hours','confirmation','logistics_entry']} for i in ['IF-RECOVERY','RISK-STOCK','TRANS-OFFLINE','DELIVERY-NOTE']]}
 (H/'shared-policy-contract.json').write_text(json.dumps(contract,ensure_ascii=False,indent=2)+'\n')
 def policy():
  ensure('上限由2件改为1件' in raw and '由24小时改为8小时' in raw,'raw change missing')
  for ver,limit,hours in [('v1',2,24),('v2',1,8)]:
   es=entities(models[ver]);p=es['CAP-RESERVE']['attributes']['policy'];ensure(p['offline_item_limit']==limit and p['max_pending_hours']==hours,'policy source mismatch');ensure(not check(models[ver],contract),'stale cross-view policy');n=es['DELIVERY-NOTE']['attributes'];ensure(n['operations']['pending_item_limit']==limit and n['operations']['max_pending_hours']==hours,'operations stale');ensure(n['validation_scenarios'][0]['accept_quantity']==limit and n['validation_scenarios'][1]['boundary_hours']==hours,'scenarios stale');ensure('policy_version' in es['IF-RECOVERY']['attributes']['payload'],'interface version absent')
  result=classify_change(models['v1'],models['v2'],'CAP-RESERVE',contract);ensure(result['change_type']=='business-policy-change','semantic change classified editorial');return result
 test('policy-change-propagates-to-interface-risk-operations-transition-tests',policy)
 for obj in ['IF-RECOVERY','RISK-STOCK','TRANS-OFFLINE','DELIVERY-NOTE']:
  def stale(obj=obj):
   bad=copy.deepcopy(models['v2']);entities(bad)[obj]['attributes']['policy']['policy_version']='v1';issues=check(bad,contract);ensure(any(x['id']==obj and x['code']=='policy-projection-stale' for x in issues),'stale projection accepted');return [x['code'] for x in issues]
  test('reject-stale-policy-'+obj,stale)
 def editorial():
  m=copy.deepcopy(models['v1']);entities(m)['CAP-RESERVE']['name']='库存预占（编辑性重命名）';r=classify_change(models['v1'],m,'CAP-RESERVE',contract);ensure(r['change_type']=='editorial-only' and not r['required_review_object_ids'],'editorial treated policy');return r
 test('editorial-rename-preserves-policy',editorial)
 def logistics():
  for version,m in models.items():ensure(all(r['source']=='ORDER-CONFIRMED' for r in m['relationships'] if r['type']=='transitions_to' and r['target']=='ORDER-FULFIL'),'unconfirmed order enters logistics')
  return 'all variants gate logistics on confirmation'
 test('no-unconfirmed-logistics-handoff',logistics)
 def observation_roles():
  m=models['v1'];d=m['analyses'][0]['inputs'];rels={r['id']:r for r in m['relationships']}
  for obs in d['assessments']:
   expected={r['role_ref'] for r in d['requirements'] if r['skill_id']==obs['skill_id'] and r['task_ref'] in obs['task_refs']}
   ensure(expected=={rels[obs['id']]['target']},'skill matrix assigns observation to wrong role: '+obs['id'])
  ensure('待业务定义' not in str(entities(m)['TRANS-ONLINE']['attributes']),'resolved policy still shown unknown')
  ensure('待明确' not in entities(m)['IF-RESERVE']['attributes']['payload'],'resolved interface still shown unknown')
  return 'observation-role edges and resolved policy agree with original material'
 test('cross-view-observation-role-and-policy-semantics',observation_roles)
 r={'schema_version':'forward-acceptance/1','passed':all(x['passed'] for x in checks),'checks':checks,'counts':{'checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)},'input_sha256':{p.relative_to(C).as_posix():sha(p) for p in [H/'sufficient-business-materials.md',H/'sufficient-role-skill-inputs.json',Path(__file__)]},'review_independence_zh':'不同验证程序直接从原始材料核对，不调用案例构建器；同一实现者复核，尚非不同评审人盲审。','real_business_approval':'not-granted'}
 (H/'forward-acceptance.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(r['counts']);print([x for x in checks if not x['passed']]);return int(not r['passed'])
if __name__=='__main__':raise SystemExit(main())
