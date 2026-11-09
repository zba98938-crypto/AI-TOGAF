# -*- coding: utf-8 -*-
"""Check source binding, real artifact generation and adversarial ADM coverage.

Synthetic coverage records test version/evidence mechanics only; they are not a
semantic acceptance of the 94 activities or real organizational approval.
"""
from pathlib import Path
import copy, datetime, hashlib, json, sys
sys.dont_write_bytecode=True
C=Path(__file__).resolve().parents[1];S=C/'skills/_shared'
sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
from adm import initialize, check_cycle, digest, iteration_fingerprint, requirements_context, CONTRACT_PATH
from generate import generate
from validate import validate
from architecture_delivery import catalog
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())

def main():
 checks=[]
 def test(ident,fn):
  try:detail=fn();checks.append({'id':ident,'passed':True,'detail':detail})
  except Exception as e:checks.append({'id':ident,'passed':False,'detail':type(e).__name__+': '+str(e)})
 def ensure(value,text):
  if not value:raise AssertionError(text)
 contracts=load(CONTRACT_PATH);arts=load(S/'artifacts.json');dels=load(S/'deliverables.json')
 def source_bindings():
  count=0
  for item in arts['artifacts']+dels['deliverables']+contracts['phases']+[contracts['requirements_management']]:
   for ref in item['foundation_binding']['refs']:
    src=C/ref['source_document_path'];ensure(sha(src)==ref['source_document_sha256'],'stale source document')
    data=load(src);blocks={b['id']:b for b in data['blocks']}
    for loc in ref['source_locators']:
     ensure(loc['block_id'] in blocks,'missing source block');ensure(digest_block(blocks[loc['block_id']])==loc['block_sha256'],'changed source block');count+=1
    for quote in ref['source_quotes_en']:ensure(quote['text_en'] in blocks[quote['block_id']]['text_en'],'quote not exact')
  ensure(len(arts['artifacts'])==75 and len(dels['deliverables'])==23,'registry cardinality');return {'bindings':108,'block_links':count}
 test('exact-source-blocks-and-hashes',source_bindings)
 def rm_responsibility():
  p=contracts['requirements_management'];steps=p['source_step_records'];ensure(len(steps)==10,'RM steps missing')
  ensure([x['source_row'] for x in steps]==list(range(1,11)),'wrong row order')
  ensure([x['source_row'] for x in steps if x['responsibility_column_index']==1]==[2,3,5,8],'RM responsibility flattened')
  ensure([x['source_row'] for x in steps if x['responsibility_column_index']==2]==[1,4,6,7,9,10],'phase responsibility changed')
  ensure('by accident' in steps[-1]['text_en'],'gap requirement qualification lost');return '10 rows; 4 RM and 6 phase actions retained'
 test('requirements-two-responsibility-columns',rm_responsibility)
 def source_phase_catalog():
  c=catalog(['E','F']);e,f=c['phases'];ensure(any(a['id']=='implementation-factor-catalog' and a['phase_basis']=='source-artifact-phase-list' for a in e['artifact_candidates']),'missing E source routing')
  ensure('implementation-governance-model' not in e['suggested_deliverable_ids'],'E invents output')
  ensure(f['conditional_deliverables'][0]['condition_en']=='if any','lost conditional output')
  for p in c['phases']:
   for a in p['artifact_candidates']:ensure((S/a['definition']).is_file(),'missing definition '+a['id'])
  return 'source-listed phase and owner routing distinguished; governance output conditional at F'
 test('phase-catalog-uses-foundation-and-conditions',source_phase_catalog)
 context={'domains':['business','data','application','technology'],'landscape':'segment','purpose':'project','abstraction':'logical','evolution':'target'}
 model={'schema_version':'2.0','project':{'id':'foundation-execution-fixture','name':'虚构基础标准执行回归','version':'1','is_example':True,'approval_status':'candidate','implementation_status':'not-started','context':context},'sources':[{'id':'FIXTURE','kind':'example','description':'纯虚构执行回归材料，不是实际证据','locator':'fixture-evidence.md'}],'entities':[],'relationships':[],'views':[],'deliverables':[],'gaps':[]}
 def entity(i,t,attrs):
  model['entities'].append({'id':i,'type':t,'name':'虚构 '+i,'attributes':attrs,'evidence':['FIXTURE'],'certainty':'assumed'})
 entity('FACTOR','implementation_factor',{'category':'assumption','description':'恢复同步容量未测量','deduction':'切换前须测量恢复积压的排空时间','action_or_constraint':'未通过阈值验证不得扩店'})
 entity('GAP','gap',{'solution_refs':['WP'],'dependency_refs':['TRANS']})
 entity('WP','work_package',{'value_index':None,'risk_index':None,'criteria_basis':None})
 entity('TRANS','transition',{'description':'虚构受控试点'})
 entity('SERVICE','business_service',{'description':'库存预占'})
 entity('SBB','sbb',{'service_taxonomy':'虚构履约服务分类','proposed_state':'transition','transition_ref':'TRANS','service_refs':['SERVICE']})
 entity('ROLE','role',{'responsibility':'虚构试点评审职责；无真实授权'})
 model['relationships']=[{'id':'INC','type':'implements_transition','source':'WP','target':'TRANS','label':'候选增量交付','attributes':{'increment_description':'仅启用在线预占；门店断连持续销售另行决策'},'evidence':['FIXTURE'],'certainty':'assumed'}]
 selections=[('implementation-factor-catalog',['FACTOR'],[]),('consolidated-gaps-solutions-dependencies-matrix',['GAP','WP','TRANS'],[]),('architecture-definition-increments-table',['WP','TRANS'],['INC']),('transition-architecture-state-evolution-table',['SERVICE','TRANS','SBB'],[]),('business-value-risk-matrix',['WP'],[])]
 for a,es,rs in selections:model['views'].append({'id':a,'artifact_id':a,'profile_id':'c220-'+a,'title':'虚构 '+a,'context':context,'entity_ids':es,'relationship_ids':rs,'analysis':'回归验证表达；未评价指数保留未知，规划均为候选。','legend':'虚构；未记录不表示0或无依赖。'})
 governance=next(d for d in dels['deliverables'] if d['id']=='implementation-governance-model')
 model['deliverables']=[{'id':'GOVERNANCE','deliverable_id':governance['id'],'title':'虚构实施治理模型草稿','view_ids':[],'entity_ids':['ROLE'],'sections':{s['title']:s['instruction']+'虚构教学设计，实际授权、责任人和执行结果待核验。' for s in governance['sections']},'approval_status':'candidate','implementation_status':'not-started'}]
 work=C/'maintenance/work/foundation-execution';work.mkdir(parents=True,exist_ok=True)
 (work/'fixture-evidence.md').write_text('# Synthetic mechanics fixture\n\nNo real execution, approval or semantic acceptance is asserted.\n')
 (work/'model.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
 def generation():
  issues=validate(model);ensure(not [i for i in issues if i['level']=='error'],str(issues))
  before=copy.deepcopy(model);manifest=generate(model,work/'generated',all_items=True,strict=True)
  ensure(model==before,'generator mutated evidence or indices')
  ensure(len(manifest['artifacts'])==5 and len(manifest['deliverables'])==1,'new outputs absent')
  for entry in manifest['artifacts']:
   payload=load(work/'generated'/entry['json']);coverage=load(work/'generated'/entry['coverage'])
   ensure(not coverage['errors'],'table expression errors');ensure(set(e['id'] for e in payload['entities'])==set(next(v for v in model['views'] if v['id']==entry['view_id'])['entity_ids']),'lost selected entities')
  wp=next(e for e in load(work/'generated/model.json')['entities'] if e['id']=='WP');ensure(wp['attributes']['value_index'] is None and wp['attributes']['risk_index'] is None,'unknown converted to score')
  text=(work/'generated/deliverables/implementation-governance-model.md').read_text();ensure('candidate' in text and '批准状态：approved' not in text,'approval fabricated')
  return {'artifacts':5,'deliverables':1,'table_rendering':'Markdown+JSON; PNG not applicable to table profiles','actual_approval':'not-granted'}
 test('five-artifacts-and-governance-genuinely-generate',generation)
 def invalid_index():
  m=copy.deepcopy(model);next(e for e in m['entities'] if e['id']=='WP')['attributes']['value_index']=True
  ensure(any(i['code']=='foundation-index-value' for i in validate(m)),'boolean score accepted');return 'rejected'
 test('index-cannot-be-boolean',invalid_index)
 def no_fake_approval():
  m=copy.deepcopy(model);next(e for e in m['entities'] if e['id']=='WP')['attributes'].update(value_index=2,evaluation_state='assessed',criteria_basis={'method':'虚构方法','source_refs':['FIXTURE'],'approval_evidence':['FIXTURE'],'approved_by':'虚构高层','criteria_defined_before_options':True})
  ensure(any(i['code']=='foundation-criteria-approval' for i in validate(m)),'example became actual approved criteria');return 'example cannot establish real criteria approval'
 test('index-needs-preexisting-approved-criteria',no_fake_approval)
 # Submitted organizational evidence is checked for consistency, not certified
 # by this fixture. These inputs deliberately do not assert real approval.
 def assessment_fixture():
  m=copy.deepcopy(model)
  m['sources'].append({'id':'CRITERIA','kind':'user','description':'Synthetic submitted-criteria consistency fixture; no real approval','locator':'fixture-evidence.md'})
  next(e for e in m['entities'] if e['id']=='WP')['attributes'].update(
   value_index=4.1,risk_index=2.8,evaluation_state='assessed',criterion_scores={'V1':5,'V2':2,'R1':2,'R2':4},
   criteria_basis={'method':'weighted sum; numeric consistency fixture','source_refs':['CRITERIA'],
    'approval_evidence':['CRITERIA'],'approved_by':'synthetic declared authority',
    'criteria_defined_before_options':True,'defined_on':'2026-11-08','approved_on':'2026-11-09','options_disclosed_on':'2026-11-10',
    'criteria':[{'id':'V1','dimension':'value','weight':.7},{'id':'V2','dimension':'value','weight':.3},
                {'id':'R1','dimension':'risk','weight':.6},{'id':'R2','dimension':'risk','weight':.4}]})
  return m
 def assessment_check(mutate=None,code=None):
  m=assessment_fixture();a=next(e for e in m['entities'] if e['id']=='WP')['attributes']
  if mutate:mutate(a)
  findings=validate(m);ensure(not [i for i in findings if i['code']=='schema'],str(findings))
  errors=[i for i in findings if i['level']=='error' and i['code'].startswith('foundation-')]
  ensure(any(e['code']==code for e in errors) if code else not errors,str(errors))
  return 'submitted criteria consistency checked; no human authority authenticated'
 test('explicit-predefined-weighted-scores-consistent',lambda:assessment_check())
 test('post-option-criteria-rejected',lambda:assessment_check(lambda a:a['criteria_basis'].update(approved_on='2026-11-10'),'foundation-criteria-approval'))
 test('bad-criteria-date-rejected',lambda:assessment_check(lambda a:a['criteria_basis'].update(defined_on='yesterday'),'foundation-criteria-approval'))
 test('implicit-equal-weights-rejected',lambda:assessment_check(lambda a:a['criteria_basis']['criteria'][0].pop('weight'),'foundation-criteria-weights'))
 test('unknown-criteria-dimension-rejected',lambda:assessment_check(lambda a:a['criteria_basis']['criteria'][0].update(dimension='profit'),'foundation-criteria-weights'))
 test('raw-score-required-not-reconstructed',lambda:assessment_check(lambda a:a['criterion_scores'].pop('V1'),'foundation-criteria-scores'))
 test('wrong-weighted-index-rejected',lambda:assessment_check(lambda a:a.update(value_index=5),'foundation-index-calculation'))
 test('malformed-basis-produces-gap-not-crash',lambda:assessment_check(lambda a:a.update(criteria_basis=None),'foundation-criteria-approval'))
 cycle=initialize(model,'fixture-cycle','虚构版本绑定机制测试；并非94步工作已执行')
 base=check_cycle(cycle,model,work)
 test('94-pending-steps-not-completed-by-init',lambda:ensure(sum(x['source_step_coverage']['expected_count'] for x in base['phases'])+base['requirements_source_step_coverage']['expected_count']==94 and not base['foundation_source_coverage_complete'],'initialization auto-executed steps'))
 legacy=copy.deepcopy(cycle)
 for p in legacy['phases']:
  for it in p['iterations']:it.pop('source_step_coverage')
 legacy['requirements'].pop('source_step_coverage')
 test('legacy-cycle-remains-readable-with-explicit-gaps',lambda:ensure(not check_cycle(legacy,model,work)['errors'] and not check_cycle(legacy,model,work)['foundation_source_coverage_complete'],'legacy auto-covered or rejected'))
 evidence=[{'path':'fixture-evidence.md','sha256':sha(work/'fixture-evidence.md'),'locator':'Synthetic mechanics fixture'}]
 filled=copy.deepcopy(cycle)
 for p in filled['phases']:
  it=p['iterations'][-1]
  for s in it['source_step_coverage']:s.update(disposition='not-applicable',rationale='纯机制反例夹具；本记录不作为真实裁剪或语义验收证据。',evidence=evidence,context_sha256=iteration_fingerprint(model,it,filled['scope']))
 for s in filled['requirements']['source_step_coverage']:s.update(disposition='reuse',rationale='纯机制测试；不宣称实际完成需求管理。',evidence=evidence,context_sha256=requirements_context(model,filled))
 test('mechanics-coverage-does-not-complete-project',lambda:ensure(check_cycle(filled,model,work)['foundation_source_coverage_complete'] and not check_cycle(filled,model,work)['recorded_cycle_complete'],'coverage granted completion'))
 def rejection(mutate,code=None):
  c=copy.deepcopy(filled);mutate(c);r=check_cycle(c,model,work)
  ensure(not r['foundation_source_coverage_complete'],'invalid source coverage accepted')
  if code:ensure(any(x['code']==code for x in r['errors']),str(r['errors']))
  return 'coverage rejected; no authority granted'
 test('unknown-source-step-rejected',lambda:rejection(lambda c:c['phases'][0]['iterations'][-1]['source_step_coverage'][0].update(source_step_id='NOT-A-STEP'),'source-step-unknown'))
 test('duplicate-source-step-rejected',lambda:rejection(lambda c:c['phases'][0]['iterations'][-1]['source_step_coverage'].append(copy.deepcopy(c['phases'][0]['iterations'][-1]['source_step_coverage'][0])),'source-step-duplicate'))
 test('changed-evidence-rejected',lambda:rejection(lambda c:c['requirements']['source_step_coverage'][0]['evidence'][0].update(sha256='0'*64)))
 test('stale-source-step-contract-rejected',lambda:rejection(lambda c:c['requirements']['source_step_coverage'][0].update(source_step_sha256='0'*64)))
 test('stale-step-model-context-rejected',lambda:rejection(lambda c:c['phases'][0]['iterations'][-1]['source_step_coverage'][0].update(context_sha256='0'*64)))
 report={'schema_version':'foundation-execution-verification/1','executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':all(x['passed'] for x in checks),'checks':checks,'counts':{'checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)},'input_sha256':{str(p.relative_to(C)):sha(p) for p in [S/'artifacts.json',S/'deliverables.json',S/'capabilities.json',CONTRACT_PATH,S/'scripts/adm.py',S/'scripts/architecture_delivery.py',S/'scripts/validate.py',S/'scripts/foundation_planning.py',S/'schemas/adm-cycle.schema.json']},'limits_zh':['机械覆盖夹具只测试证据和版本失效，不证明94步实际执行或语义充分。','新规划制品为项目表格表达，不宣称官方视觉等价。']}
 (C/'quality/foundation-execution-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts']);print([c for c in checks if not c['passed']]);return int(not report['passed'])

def digest_block(block):return hashlib.sha256(json.dumps(block,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
if __name__=='__main__':raise SystemExit(main())
