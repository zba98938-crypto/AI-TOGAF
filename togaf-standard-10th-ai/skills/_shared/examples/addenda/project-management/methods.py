# -*- coding: utf-8 -*-
"""Check explicit project records; never infer business approval or source rules."""
def factors(rows):
 for r in rows:
  if not r.get('observation') or not r.get('evidence_refs') or not r.get('effect'):raise ValueError('factor-evidence-gap')
 return {'factors':len(rows),'unknown_timing':sum('unknown' in r['timing'] for r in rows),'gaps':[r['required_action'] for r in rows if '待' in r['confidence'] or '尚无' in r['confidence'] or '未' in r['confidence']]}

def themes(rows):
 ids={r['work_package_id'] for r in rows}
 if len(ids)!=len(rows):raise ValueError('duplicate-work-package-budget')
 for r in rows:
  if r['change_kind'] not in ['keep','improve','differentiate','new-market']:raise ValueError('ambiguous-change-kind')
  if set(r['required_work_packages'])-ids:raise ValueError('missing-work-package-dependency')
  if not all(r.get(k) for k in ['importance','impact_start','effort','investment']):raise ValueError('theme-information-gap')
 graph={r['work_package_id']:r['required_work_packages'] for r in rows};done=set();active=set();ordered=[]
 def visit(id):
  if id in active:raise ValueError('dependency-cycle')
  if id in done:return
  active.add(id)
  for before in graph[id]:visit(before)
  active.remove(id);done.add(id);ordered.append(id)
 for id in graph:visit(id)
 return {'order':ordered,'themes':sorted(set(r['theme'] for r in rows)),'budget_aggregation':'not-performed; no automatic cross-scope sum'}

def sufficiency(v):
 if v.get('contingency') is None or not v.get('rule_evidence'):raise ValueError('missing-project-contingency')
 if v['previous_scope']!=v['current_scope']:raise ValueError('incomparable-estimates')
 if v['previous_estimate']<=0:raise ValueError('invalid-estimate-denominator')
 if not 0<=v['contingency']<=1:raise ValueError('invalid-contingency')
 previous_ratio=v['previous_breadth']/v['previous_depth'] if v['previous_depth']>0 else None
 current_ratio=v['current_breadth']/v['current_depth'] if v['current_depth']>0 else None
 ratio_signal=current_ratio<previous_ratio if current_ratio is not None and previous_ratio is not None else None
 change=abs(v['current_estimate']-v['previous_estimate'])/v['previous_estimate']
 estimate_signal=change<v['contingency']
 signal=ratio_signal is True or estimate_signal
 return {'previous_ratio':previous_ratio,'current_ratio':current_ratio,'relative_change':change,'ratio_signal':ratio_signal,'estimate_signal':estimate_signal,'source_diminishing_return_signal':signal,'recommendation':'investigate-open-issues' if v.get('critical_gaps') else ('submit-to-budget-decision' if signal else 'continue-targeted-analysis'),'automatic_approval':False}

def authorization(r,request_start=False):
 ready=all(p['accepted'] is True for p in r['preconditions']) and r['authorization']=='authorized-in-fixture' and r['cost_time_tolerance']['rule_status']=='confirmed-in-fixture'
 if request_start and not ready:raise ValueError('authorization-not-ready')
 if r['work_package_kind']!='project-wbs-leaf':raise ValueError('wrong-work-package-identity')
 return {'ready_to_start_in_fixture':ready,'actual_authority_granted':False,'preconditions_met':all(p['accepted'] is True for p in r['preconditions'])}

def closure(r,request_close=False):
 terminated=r['closure_reason'].startswith('terminated-')
 complete=all(p['accepted'] is True for p in r['products'])
 if not terminated and not complete and request_close:raise ValueError('closure-products-not-accepted')
 if terminated and any(not p.get('disposition') for p in r['products'] if not p['accepted']):raise ValueError('termination-undelivered-disposition-missing')
 approved=r['decision'] in ['stage-close-and-next-plan-approved-in-fixture','termination-approved-in-fixture']
 return {'closure_reason':r['closure_reason'],'products_complete':complete,'ready_to_close_in_fixture':(terminated or complete) and approved,'successful_delivery':complete and not terminated,'real_approval':False}

def lessons(rows):
 for r in rows:
  if not r.get('expected') or not r.get('actual') or not r.get('evidence_refs'):raise ValueError('learning-evidence-gap')
  if not r.get('owner') or not r.get('verification'):raise ValueError('learning-action-without-verification')
 return {'rows':len(rows),'trial_results':sum('trial-observed' in r['status'] for r in rows),'causal_generalization':'not-proven'}

def charter(r):
 for c in r['acceptance_criteria']:
  if c['id']=='AC-COVERAGE' and c['observed']<c['required_total'] and c['result']=='met':raise ValueError('criterion-result-contradiction')
 # required_total is an explicit project rule derived from the selected scope.
 criteria_met=all(c['result']=='met' for c in r['acceptance_criteria'])
 return {'criteria_met':criteria_met,'accepted':r['status']=='accepted-in-fixture' and criteria_met,'missing_inputs':[i['id'] for i in r['required_inputs'] if i['status']!='provided']}
