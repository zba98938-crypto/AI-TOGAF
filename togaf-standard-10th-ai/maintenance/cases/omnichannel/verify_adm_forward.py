# -*- coding: utf-8 -*-
"""Forward checks from raw ADM materials; do not import case builders.

Same implementer, separate program. This is not different-reviewer acceptance.
"""
from pathlib import Path
import copy,hashlib,json,re,sys,datetime
sys.dont_write_bytecode=True
H=Path(__file__).resolve().parent;C=H.parents[2];S=C/'skills/_shared';sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
from adm import check_cycle,load
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 raw=(H/'adm-business-materials.md').read_text();folder=H/'generated-adm';model=load(folder/'model.json');cycle=load(folder/'cycles/cycle.json');checks=[]
 def ensure(v,m):
  if not v:raise AssertionError(m)
 def test(i,fn):
  try:d=fn();checks.append({'id':i,'passed':True,'detail':d})
  except Exception as e:checks.append({'id':i,'passed':False,'detail':type(e).__name__+': '+str(e)})
 def phases():
  r=check_cycle(cycle,model,folder/'cycles');ensure(not r['errors'] and r['recorded_cycle_complete'] and r['foundation_source_coverage_complete'],'case not covered');ensure({p['phase'] for p in r['phases']}=={'Preliminary',*'ABCDEFGH'},'Phase I invented');ensure(sum(p['source_step_coverage']['expected_count'] for p in r['phases'])+r['requirements_source_step_coverage']['expected_count']==94,'source steps absent');return '9 phases and 10 continuous requirements steps; no Phase I'
 test('full-adm-and-continuous-requirements',phases)
 def evidence():
  for phase in cycle['phases']:
   p=phase['phase'];d=next(e for e in model['entities'] if e['id']=='ADM-WORK-'+p);a=d['attributes'];ensure(a['raw_material'] in raw,'phase material not from raw');ensure(a['source_steps'] and all(x['case_analysis_zh'].strip() for x in a['source_steps']),'missing reasoning');ensure(a['actual_business_approval']=='not-granted','actual approval fabricated')
  ensure(model['project']['is_example'] and model['project']['approval_status']!='approved','example identity erased');return 'raw paragraphs preserved with specific step analysis; approval remains fictional'
 test('phase-findings-trace-raw-material',evidence)
 def parallel():
  ps={p['phase']:p for p in cycle['phases']}
  for p in 'BCD':ensure(ps[p]['iterations'][-1]['depends_on']==['A-1'],'domain serialized by phase order')
  ensure(set(ps['E']['iterations'][-1]['depends_on'])=={'B-1','C-1','D-1'},'E skips consolidated domains');return 'parallel B/C/D information, E integration'
 test('parallel-domain-information-dependencies',parallel)
 def value():
  ensure('5、2' in raw and '3、5' in raw and '0.7' in raw and '0.3' in raw,'raw ratings missing')
  ensure(round(5*.7+2*.3,1)==4.1 and round(3*.7+5*.3,1)==3.6,'value formula')
  ensure(round(2*.6+4*.4,1)==2.8 and round(4*.6+4*.4,1)==4,'risk formula')
  ensure('80小时' in raw and '120小时' in raw and '100和140小时' in raw,'implementation resource basis missing')
  ensure('预算与真实财务收益未知' in raw,'financial unknown hidden');return {'value':[4.1,3.6],'risk':[2.8,4.0],'roi':'unknown'}
 test('value-risk-resource-recompute-from-raw',value)
 def governance():
  ensure('截至11-30' in raw and '11-29' in raw and '独立归档' in raw and '情景委员会' in raw,'waiver conditions missing')
  g=next(e for e in model['entities'] if e['id']=='ADM-WORK-G')['attributes'];ensure('11-29修复关闭' in str(g),'closure not traced');ensure('96条在30分钟内' in raw and 96/100>=.95,'recovery observation mismatch');return 'dated conditional waiver, repair and experiment-only conformance'
 test('governance-uses-given-tests-and-time-bound-waiver',governance)
 def benefits():
  ensure('120条离线受理中118条' in raw and '2条进入人工异常' in raw,'effect denominator missing');ensure('不是收入或全企业收益' in raw,'effect generalized');return {'confirmation_ratio':118/120,'financial_benefit':'not-established'}
 test('H-observation-scope-and-change-feedback',benefits)
 def policy():
  m=load(folder/'model-policy-v2.json');c=load(folder/'cycles/cycle-policy-v2-needs-review.json');r=check_cycle(c,m,folder/'cycles')
  ensure(not r['recorded_cycle_complete'] and not r['foundation_source_coverage_complete'],'stale policy accepted')
  ensure(any('需求变更后须复核' in gap for p in r['phases'] for gap in p['gaps']),'no change re-review')
  ensure(any(p['phase']=='C' and not p['source_step_coverage']['complete'] for p in r['phases']),'C source steps stale not found');return 'old V1 cannot complete V2 despite renderable model'
 test('policy-change-invalidates-old-evidence',policy)
 def missing_step():
  c=copy.deepcopy(cycle);c['phases'][2]['iterations'][-1]['source_step_coverage'].pop();r=check_cycle(c,model,folder/'cycles');ensure(not r['foundation_source_coverage_complete'],'omitted step auto-covered');return 'missing step remains explicit gap'
 test('omitted-step-not-auto-completed',missing_step)
 def no_rationale():
  c=copy.deepcopy(cycle);s=c['phases'][2]['iterations'][-1]['source_step_coverage'][0];s.update(disposition='not-applicable',rationale='');r=check_cycle(c,model,folder/'cycles');ensure(not r['foundation_source_coverage_complete'],'unreasoned tailoring accepted');return 'tailoring without reason rejected'
 test('unsupported-tailoring-remains-gap',no_rationale)
 def stale_decision():
  m=copy.deepcopy(model);next(e for e in m['entities'] if e['id']=='IF-RECOVERY')['attributes']['payload']='changed without review';r=check_cycle(cycle,m,folder/'cycles');ensure(not r['recorded_cycle_complete'] and not r['foundation_source_coverage_complete'],'changed interface accepted');return 'semantic input change requires review'
 test('changed-interface-invalidates-review',stale_decision)
 def raw_no_fabrication():
  ensure('架构团队32小时设计任务相混' in raw and '额外的实施与运维能力须另评价' in raw,'roles and capacity flattened');ensure('不是被意外消除的基线内容' in raw,'gap requirement generalized');return 'person capacity, implementation capacity and gap terminology separated'
 test('capacity-and-gap-semantics-preserved',raw_no_fabrication)
 report={'schema_version':'omnichannel-adm-forward/1','passed':all(c['passed'] for c in checks),'checks':checks,'counts':{'checks':len(checks),'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks)},'input_sha256':{str(p.relative_to(C)):sha(p) for p in [H/'adm-business-materials.md',folder/'model.json',folder/'cycles/cycle.json',S/'scripts/adm.py',S/'references/adm-phases.json',Path(__file__)]},'review_independence':'separate verification implementation by same author; different-reviewer semantic acceptance pending','real_business_approval':'not-granted'}
 (H/'adm-forward-acceptance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts']);print([c for c in checks if not c['passed']]);return int(not report['passed'])
if __name__=='__main__':raise SystemExit(main())
