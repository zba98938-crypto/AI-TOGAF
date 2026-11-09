"""Raw-business oracles for the six formerly missing generic profiles.

Expected values are recomputed here from raw material, not from the case builder
or renderer. Missing facts may produce readable drafts, never business passes.
"""
import copy
from decimal import Decimal
import json
from pathlib import Path

from planning_case_examples import PROFILE_IDS, ASSIGNMENT, KINDS, raw_case

MISSING_CODES = dict(zip(PROFILE_IDS[1:], ('foundation-factor-deduction','foundation-gap-link',
    'foundation-increment-gap','foundation-transition-evolution','foundation-index-unknown')))


def actor_raw(raw):
    """Hide the preselected modeling route, while preserving original facts."""
    hidden={'method_ids','artifact_ids','role_reuse_provenance','schema_version'}
    if isinstance(raw,dict):return {k:actor_raw(v) for k,v in raw.items() if k not in hidden}
    if isinstance(raw,list):return [actor_raw(v) for v in raw]
    return raw


def native_cases(profile):
    pid=profile['id'];rows=[]
    for variant in ('sufficient','missing','change'):
        raw=raw_case(pid,variant)
        identity='profile-'+pid if variant=='sufficient' else 'planning-'+variant+'-'+pid
        rows.append(dict(id=identity,kind='negative' if variant=='missing' else 'profile',
            target=pid,owner=profile['owner'],scenario=variant,
            request='Use the supplied synthetic business material to prepare the requested '+profile['name']+'. '+
                    'Trace the actual assumptions, dependencies and computed decisions into saved artifacts. '+
                    'Identify missing inputs and the effects of business changes. Keep real approval not-granted.',
            raw=actor_raw(raw),rubric=dict(business_fixture_status='provided',scenario=variant,
                input_sufficient_for_simulation=variant!='missing',actual_business_approval='not-granted',
                independent_oracle='tests/enterprise/planning_cases.py:verify_output',
                checks=['Recompute from raw business inputs; do not invent unavailable facts.',
                        'Preserve stable identities and cross-domain dependencies.',
                        'Actual readable output must express the substantive scenario change.',
                        'Unknown capacity, criteria, increment or dependency cannot imply acceptance.'],
                acceptable_artifacts=[profile['artifact_id']],semantic_equivalence_allowed=True)))
    return rows


def verify_output(pid, raw, model, payload, text, issues, analysis=None):
    """Check actual saved artifact payload/text; return scoped decision readiness."""
    def need(ok,message):
        if not ok:raise AssertionError(message)
    es={e['id']:e for e in payload['entities']};rs=payload.get('relationships',[])
    need(len(es)==len(payload['entities']),'duplicate output entities')
    need(model['project']['approval_status']=='candidate','example granted approval')
    need('approved' not in {e.get('attributes',{}).get('approval') for e in es.values()},'actual output granted approval')
    scenario=raw['scenario'];readiness='needs-input' if scenario=='missing' else 'candidate-only'
    if pid==ASSIGNMENT:
        inp=raw['role_inputs'];assignment=inp['assignments'][0];task=inp['tasks'][0]
        hours=assignment['available_hours'];demand=task['workload_hours']
        expected_capacity='unresolved' if hours is None else 'insufficient' if hours<demand else 'sufficient-for-declared-workload'
        row=next(x for x in analysis['assignment_reviews'] if x['id']==assignment['id'])
        need(row['capacity_state']==expected_capacity,'capacity disagrees with raw hours')
        need(row['approval']=='not-granted','analysis granted personnel approval')
        needed_ids={x['id'] for k in ('roles','tasks','assignments') for x in inp[k]}|{x['id']+'.evidence' for x in inp['assessments']}
        need(set(es)==needed_ids,'assignment subjects lost or invented')
        pairs={(inp['roles'][0]['id'],task['id']),(assignment['id'],task['id']),
               (assignment['id'],inp['assessments'][0]['id']+'.evidence')}
        need({(r['source'],r['target']) for r in rs}==pairs and len(rs)==3,'assignment relations differ from raw material')
        attrs=es[assignment['id']]['attributes']
        need(attrs['available_hours']==hours and attrs['capacity_state']==expected_capacity,'saved capacity is stale')
        need(es[task['id']]['attributes']['workload_hours']==demand,'saved workload is stale')
        need(expected_capacity in text and str(demand) in text,'actual readable artifact omits capacity/workload')
        if expected_capacity!='sufficient-for-declared-workload':readiness='needs-input-or-capacity'
    else:
        p=raw['planning'];kind=KINDS[pid]
        if kind=='factor':
            f=p['factor'];a=es[f['id']]['attributes'];rate=f['drain_events_per_hour']
            expected=None if rate is None else float(Decimal(f['backlog_events'])/Decimal(rate))
            need(a['calculated_recovery_hours']==expected,'recovery arithmetic differs from raw backlog/rate')
            need(a['action_or_constraint'] is None if expected is None else bool(a['action_or_constraint']),'missing action/deduction boundary lost')
            if expected is not None:
                need(str(expected) in text,'recovery hours absent from readable output')
                if expected>f['recovery_window_hours']:
                    need('Capacity increase' in text,'over-window change lost in actual output');readiness='needs-capacity-review'
        elif kind=='gap':
            g=p['gap'];a=es[g['id']]['attributes']
            need(a['solution_refs']==g['solution_work_packages'],'solution references changed')
            need(a['dependency_refs']==g['dependency_work_packages'],'unknown or cross-domain dependency changed')
            need(set(es)=={g['id']}|{w['id'] for w in p['work_packages']},'gap output lost supporting work packages')
            for identity in g['dependency_work_packages'] or []:need(identity in text,'dependency absent from actual table')
        elif kind=='increment':
            incs=[p['increment']]+([p['additional_increment']] if 'additional_increment' in p else [])
            expected={(i['work_package'],i['transition']):i['description'] for i in incs}
            actual={(r['source'],r['target']):r['attributes']['increment_description'] for r in rs}
            need(actual==expected and len(rs)==len(expected),'increment content or direction differs from raw decision')
            for i in incs:
                if i['description']:need(i['description'] in text,'increment detail absent from actual artifact')
        elif kind=='transition':
            t=p['transition'];a=es[t['sbb_id']]['attributes']
            need(a['service_taxonomy']==t['service_taxonomy'],'missing taxonomy was inferred')
            need(a['transition_ref']==t['id'] and a['service_refs']==[t['service_id']],'SBB service/transition binding incorrect')
            need(a['proposed_state']==t['proposed_state'] and a['scope']==t['scope'],'changed state/scope stale')
            need(t['scope'] in text and t['proposed_state'] in text,'transition change absent from actual output')
        elif kind=='value_risk':
            v=p['value_risk']
            for option in v['options']:
                a=es[option['id']]['attributes']
                for dimension in ('value','risk'):
                    cs=[c for c in v['criteria'] if c['dimension']==dimension]
                    expected=None if any(c['weight'] is None for c in cs) else sum(Decimal(str(c['weight']))*Decimal(str(option['scores'][c['id']])) for c in cs)
                    actual=a[dimension+'_index']
                    need(actual is None if expected is None else abs(Decimal(str(actual))-expected)<Decimal('0.000000001'),'index not recomputed from original weights/scores')
                    if expected is not None:need(str(float(expected)) in text,'calculated index absent from actual table')
                need(a['evaluation_state']=='simulation-only' and a['approval']=='not-granted','synthetic criteria became actual acceptance')
        if scenario=='missing':need(any(i['code']==MISSING_CODES[pid] for i in issues),'missing business input not explicitly reported')
    return dict(behavior_passed=True,business_readiness=readiness,real_approval='not-granted',independent_business_acceptance=False)


def run_profile_cases(pid,directory,render=False):
    from planning_case_examples import model as build
    from generate import generate
    from validate import validate
    from analyze import evaluate
    from architecture_delivery import output_check
    from .cases import rendered_artifact_text
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=False);rows=[]
    for variant in ('sufficient','missing','change'):
        raw=raw_case(pid,variant);m=build(pid,variant,raw);issues=validate(m)
        if any(x['level']=='error' for x in issues):raise AssertionError(str(issues))
        dest=directory/variant;dest.mkdir()
        for name,data in [('raw-business-material.json',raw),('model.json',m),('validation.json',issues)]:
            (dest/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        manifest=generate(m,dest/'generated',all_items=True,strict=True,render=render)
        _,errors=output_check(dest/'generated',m)
        if errors:raise AssertionError(str(errors))
        entry=next(x for x in manifest['artifacts'] if x['profile_id']==pid)
        payload=json.loads((dest/'generated'/entry['json']).read_text())
        text=rendered_artifact_text(dest/'generated',{'artifacts':[entry]})
        analysis=evaluate(m['analyses'][0],m)['result'] if pid==ASSIGNMENT else None
        result=verify_output(pid,raw,m,payload,text,issues,analysis)
        row=dict(profile_id=pid,variant=variant,status='pass',**result)
        if analysis:(dest/'analysis.json').write_text(json.dumps(analysis,ensure_ascii=False,indent=2)+'\n')
        (dest/'oracle.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n');rows.append(row)
    result=dict(status='pass',profile_id=pid,rows=rows,variants=3,independent_business_acceptance=False)
    (directory/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return result
