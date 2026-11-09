# -*- coding: utf-8 -*-
"""Adversarial local-runtime checks; source inputs and approvals remain unchanged."""
from pathlib import Path
import copy,json,sys,hashlib,datetime
sys.dont_write_bytecode=True
C=Path(__file__).resolve().parents[1];S=C/'skills/_shared';sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
from g249_reasoning import review_role_skills
from gap_closure_analysis import architecture_role_catalog_review
from assignment_projection import prepare,projection_issues
from validate import validate
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 raw=C/'maintenance/cases/omnichannel/role-skill-inputs.json';base=json.loads(raw.read_text());checks=[]
 def check(identity,fn):
  try:detail=fn();checks.append({'id':identity,'passed':True,'detail':detail})
  except Exception as e:checks.append({'id':identity,'passed':False,'detail':type(e).__name__+': '+str(e)})
 def ensure(test,msg):
  if not test:raise AssertionError(msg)
 def review(mutator):
  d=copy.deepcopy(base);mutator(d);return review_role_skills(d)
 def reject(code,mutator):
  try:review(mutator)
  except ValueError as e:ensure(str(e).startswith(code+' '),str(e));return str(e)
  raise AssertionError('invalid input accepted')
 for value in [99,0,True,2.5]:check('invalid-level-'+str(value),lambda v=value:reject('G249-LEVEL',lambda d:d['assessments'][0].update(proficiency=v)))
 def missing_level():
  r=review(lambda d:d['assessments'][0].pop('proficiency'));ensure(r['assessment_reviews'][0]['state']=='needs-evidence','missing level became assessed');ensure(r['assignment_reviews'][0]['state']=='needs-evidence','assignment incorrectly ready');return 'unknown preserved'
 check('missing-level-stays-unknown',missing_level)
 for tier in ['chief','segment']:
  check('no-fabricated-official-column-'+tier,lambda t=tier:reject('G249-REF',lambda d:d['requirements'][0].update(assessment_kind='source_reference_target',assessment_state='reference',reference_role_ref='G249:role:'+t+'-architect')))
 def period_case(kind):
  d=copy.deepcopy(base);t=d['tasks'][-1]
  if kind!='missing':t['work_period']={'start':'2026-11-09','end':'2026-12-04' if kind=='short' else '2026-11-20'}
  if kind=='bad':t['work_period']['end']='yesterday'
  if kind=='reversed':t['work_period']={'start':'2026-11-21','end':'2026-11-20'}
  if kind in {'bad','reversed'}:
   try:review_role_skills(d)
   except ValueError as e:ensure(str(e).startswith('G249-DATE '),str(e));return str(e)
   raise AssertionError('invalid task period accepted')
  r=review_role_skills(d)['assignment_reviews'][0];expected={'missing':'unresolved','short':'not-covered','covered':'covered-for-declared-task-periods'}[kind];ensure(r['period_state']==expected,str(r));ensure(r['approval']=='not-granted','approval inferred');return r['period_state']
 for k in ['missing','short','covered','bad','reversed']:check('task-period-'+k,lambda k=k:period_case(k))
 def training():
  d=copy.deepcopy(base);obs=d['assessments'][0];obs.update(assessment_state='assessed',proficiency=3,assessor='FICTIONAL-REVIEWER');obs['behavioral_evidence'][0].update(demonstrated=True,evidence_kind='course-completion');r=review_role_skills(d);ensure(r['assessment_reviews'][0]['state']=='needs-evidence','training passed');ensure('behavior-not-demonstrated-by-learning-record' in [x['reason'] for x in r['gaps']],'missing learning gap');return 'training cannot establish criterion'
 check('course-does-not-prove-competence',training)
 def capacity_unknown():
  r=review_role_skills(base);a=r['assignment_reviews'][0];ensure(a['capacity_state']=='unresolved','unknown workload sufficient');return a['capacity_state']
 check('unknown-workload-not-sufficient',capacity_unknown)
 def projection():
  m=json.loads((C/'maintenance/cases/omnichannel/generated/offline-change/model.json').read_text());projected=prepare(m,view_id='role-assignment');ensure(prepare(projected,view_id='role-assignment')==projected,'projection not idempotent');v=next(v for v in projected['views'] if v['id']=='role-assignment');ensure(len(v['relationship_ids'])==7,'expected 7 real relations');ensure(not projection_issues(projected,v),'projection incomplete');return {'relationships':7,'idempotent':True}
 check('generic-projection-idempotent-seven-relations',projection)
 def projection_negative(field):
  m=json.loads((C/'maintenance/cases/omnichannel/generated/offline-change/model.json').read_text());v=next(v for v in m['views'] if v['id']=='role-assignment');v[field].pop();issues=validate(m);ensure(any(x['code']=='assignment-projection-selection' for x in issues),'missing main projection accepted');return 'assignment-projection-selection'
 for field in ['entity_ids','relationship_ids']:check('projection-rejects-incomplete-'+field,lambda f=field:projection_negative(f))
 def collision():
  m=json.loads((C/'maintenance/cases/omnichannel/generated/offline-change/model.json').read_text());next(e for e in m['entities'] if e['id']=='TASK-SOL')['type']='application'
  try:prepare(m,view_id='role-assignment')
  except ValueError as e:ensure('collides' in str(e) or 'binding' in str(e),str(e));return 'rejected conflicting task identity'
  raise AssertionError('collision accepted')
 check('projection-collision-rejected',collision)
 def lateral():
  def role(i):return {'id':i,'tier':'solution','name':i,'scope':'虚构专项','primary_responsibility':'接口协调','activities':['评审'],'key_stakeholders':['OWNER'],'kpis':[],'evidence':['SRC']}
  a,b=role('R-A'),role('R-B');a['relationships']=[{'id':'REL-SAME','type':'architecture_guidance','target':'R-B','scope':'专项接口协调','evidence':['SRC']}]
  r=architecture_role_catalog_review({'source_ids':['SRC'],'roles':[a,b],'tier_tailoring_reason':'本实验只检查两个同级方案角色'})
  ensure(r['relationships'][0]['type']=='architecture_guidance','guidance became reporting');ensure(not any(x['type']=='reports_to' for x in r['relationships']),'reporting fabricated');return 'lateral guidance accepted with declared scope and evidence'
 check('same-tier-coordination-without-reporting',lateral)
 from corpus_query import resolve_source,query
 def local_sources():
  paths=['togaf-standard-10th/G249e.pdf','../g226.pdf','../w242c.pdf','fundamental/web-2025/volumes/06-ea-capability-and-governance/source.html']
  result=[resolve_source(x) for x in paths];ensure(all(x['exists'] for x in result),'source closure missing');hits=query('需求管理',document='C220-web-2025:02-architecture-development-method');ensure(hits and all(x['source_exists_in_package'] for x in hits),'web query missing');return {'sources':result,'web_hits':len(hits)}
 check('pdf-web-source-closure-and-current-query',local_sources)
 report={'schema_version':'local-runtime-regression/1','executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':all(x['passed'] for x in checks),'checks':checks,'counts':{'checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)},'input_sha256':{p.relative_to(C).as_posix():sha(p) for p in [raw,S/'scripts/g249_reasoning.py',S/'scripts/assignment_projection.py',S/'scripts/validate.py',S/'scripts/corpus_query.py']},'limits_zh':['只验证项目执行契约和已列反例，不验证人员行为真伪。','所有实际组织批准保持未授予。']}
 (C/'quality/local-runtime-regression.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report['counts']));print([r for r in checks if not r['passed']]);return int(not report['passed'])
if __name__=='__main__':raise SystemExit(main())
