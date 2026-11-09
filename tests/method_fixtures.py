"""Small authored method inputs and independent expected outcomes; no saved output dependency."""
import copy
import json
import math
from pathlib import Path
SHARED = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared'


def direct_cases():
    rows=[]
    def run(mid, inputs, predicate, label):
        rows.append(dict(method_id=mid, inputs=inputs, oracle=predicate, case=label, reject=False))
    def reject(mid, inputs, label):
        rows.append(dict(method_id=mid, inputs=inputs, case=label, reject=True))
    rule=['explicit-synthetic-project-rule']
    pref=dict(rule_evidence=rule,criteria=[dict(id='cost',weight=2),dict(id='benefit',weight=1)],options=[dict(id='A',scores=dict(cost=5,benefit=2)),dict(id='B',scores=dict(cost=2,benefit=5))])
    run('preference-weighted-decision',pref,lambda r:r['ranking']==['A','B'] and r['results'][0]['weighted_sum']==12,'preference-no-cost-reversal')
    bad=copy.deepcopy(pref);bad['options'][0]['scores']['cost']=500000;reject('preference-weighted-decision',bad,'raw-money-rejected')
    norm=dict(rule_evidence=rule,criteria=[dict(id='cost',weight=1,min=0,max=100,direction='minimize')],options=[dict(id='A',scores=dict(cost=20)),dict(id='B',scores=dict(cost=80))])
    run('weighted-normalized-decision',norm,lambda r:r['ranking']==['A','B'] and math.isclose(r['results'][0]['score'],.8),'normalization')
    bad=copy.deepcopy(norm);bad['options'][0]['scores']={};reject('weighted-normalized-decision',bad,'missing-not-zero')
    mat=dict(rule_evidence=rule,scale=dict(min=0,max=5),factors=[dict(id='A',value=1,weight=1,evidence=rule),dict(id='B',value=4,weight=3,evidence=rule)])
    run('maturity-weighted',mat,lambda r:r['weighted_level']==3.25,'maturity-weighted-mean')
    bad=copy.deepcopy(mat);bad['factors'][0]['evidence']=[];reject('maturity-weighted',bad,'maturity-no-evidence')
    risk=dict(formula='likelihood-times-impact',rule_evidence=rule,likelihood=dict(value=2,scale='project-1-5',evidence=rule),impact=dict(value=4,scale='project-1-5',evidence=rule))
    run('risk-explicit-rule',risk,lambda r:r['inherent_risk']==8,'risk-declared-formula')
    bad=copy.deepcopy(risk);bad.pop('formula');reject('risk-explicit-rule',bad,'risk-no-default-formula')
    categories=dict(foundational=['vision','sponsorship-direction','it-capability','culture','scope-scale','business-rationale','implementation-approach'],impact=['business-model-adaptability','skills-competence','technology-maturity','ecosystem','governance-compliance'],sustaining=['value-realization','policy-regulations','funding-resources'])
    dtra=dict(rule_evidence=rule,factor_rating_rule='explicit-project-rating',attention_min_rating=6,attention_threshold_evidence=rule,factors=[dict(id=i,category=c,rating=6,evidence=rule) for c,ids in categories.items() for i in ids])
    run('dtra-factor-review',dtra,lambda r:r['readiness_type']==3,'dtra-complete-15')
    bad=copy.deepcopy(dtra);bad['factors'].pop();run('dtra-factor-review',bad,lambda r:r['readiness_type'] is None and bool(r['missing_factor_ids']),'dtra-partial-no-type')
    dep=dict(rule_evidence=rule,work_packages=[dict(id=i,evidence=rule) for i in ['A','B','C']],dependencies=[dict(source='A',target='C',kind='hard',evidence=rule),dict(source='B',target='C',kind='soft',evidence=rule)])
    run('dependency-topological-order',dep,lambda r:r['batches']==[['A','B'],['C']],'dependency-batches')
    bad=copy.deepcopy(dep);bad['dependencies'].append(dict(source='C',target='A',kind='hard',evidence=rule));reject('dependency-topological-order',bad,'hard-cycle-rejected')
    transition=dict(rule_evidence=rule,transition_id='T1',conditions={k:dict(status='satisfied',description='synthetic documented condition',evidence=rule) for k in ['people','systems','data','controls','rollback']},rollback=dict(owner='test-owner',verification='simulation-only',evidence=rule,trigger=dict(metric='error-rate',operator='gt',threshold=2,period='daily',consecutive_periods=2,denominator_policy='unknown-on-zero')))
    run('transition-operability-check',transition,lambda r:r['document_gate_complete'] and r['runtime_operability']=='not-verified','document-complete-no-runtime-claim')
    bad=copy.deepcopy(transition);bad['conditions'].pop('data');run('transition-operability-check',bad,lambda r:not r['document_gate_complete'] and bool(r['gaps']),'transition-missing-condition')
    criterion=dict(id='value',weight=1,min=1,max=5,higher_is_better=True,weight_evidence=rule,scale_evidence=rule)
    priority=dict(rule_evidence=rule,criteria=[criterion],work_packages=[dict(id='A',scores=dict(value=5),score_evidence=dict(value=rule)),dict(id='B',scores=dict(value=1),score_evidence=dict(value=rule))],sensitivity=dict(evidence=rule,relative_weight_delta=.1))
    run('work-package-prioritization',priority,lambda r:r['ranking']==['A','B'] and r['scores']==dict(A=1,B=0),'priority-normalized')
    bad=copy.deepcopy(priority);bad['criteria'][0]['weight']=2;reject('work-package-prioritization',bad,'priority-bad-weight-sum')
    basis=dict(metric_id='error-rate',unit='%',scope='synthetic-orders',basis='failed/total',period='2026-11',evidence=rule)
    benefit=dict(rule_evidence=rule,direction='minimize',baseline={**basis,'value':1.2},target={**basis,'value':.6},observed={**basis,'value':.9,'kind':'simulated-observation'},trigger=dict(evidence=rule,adverse_deviation_percent=50,operator='gt',declared_before_observation=True))
    run('benefit-realization-trigger',benefit,lambda r:r['relative_target_deviation_percent']==50 and r['trigger_review'] is False,'decimal-boundary-strict-gt')
    changed=copy.deepcopy(benefit);changed['trigger']['operator']='ge';run('benefit-realization-trigger',changed,lambda r:r['trigger_review'] is True,'decimal-boundary-ge')
    bad=copy.deepcopy(benefit);bad['observed']['unit']='seconds';reject('benefit-realization-trigger',bad,'incomparable-units')
    run('benefit-realization-trigger',dict(rule_evidence=rule),lambda r:r['trigger_review'] is None and r['observation_status']=='not-observed','unknown-observation-not-zero')
    guidance=json.loads((SHARED/'references/source-tables/delivery-styles.json').read_text())['features']
    styles=dict(features=[dict(feature_id=x['id'],applies='unknown',observation='needs-evidence',evidence_refs=rule) for x in guidance],decisions=[dict(scope_id='test',styles=['agile'],rationale='explicit-project-choice',evidence_refs=rule,owner='test-owner',conflicting_features=[guidance[0]['id']],tailoring='review-after-pilot')])
    run('delivery-style-review',styles,lambda r:r['weighted_score'] is None and r['automatic_approval'] is False,'style-no-majority-score')
    reject('delivery-style-review',{},'style-empty-input')
    options=dict(iterations=[dict(option_id='A',iteration=1,subsystem='orders',goal='delivery',hypothesis='test',evidence_refs=rule,decision_owner='test-owner',assessment='candidate',status='selected')],constraint_review=dict(evidence_refs=rule))
    run('set-based-options-review',options,lambda r:r['selected_ids']==['A'] and r['automatic_approval'] is False,'option-selection-no-approval')
    reject('set-based-options-review',{},'options-empty-input')

    checklist=dict(change_profile='rapid',transition_id='T1',rule_evidence=rule,responses={})
    run('change-profile-checklist',checklist,lambda r:r['included_count']>0 and len(r['pending_included_checks'])==r['included_count'],'missing-responses-remain-unreviewed')
    bad=copy.deepcopy(checklist);bad['change_profile']='invented';reject('change-profile-checklist',bad,'unknown-change-profile')
    environment=dict(boundary='synthetic scope',method_evidence=rule,rows=[dict(id='E1',unit='kgCO2e',scope='Scope 2',period='2026',evidence=rule,added=12,retired=5,reported_net=8)])
    run('environmental-delta',environment,lambda r:r['rows'][0]['calculated_net']==7 and r['rows'][0]['source_difference']['reported']==8,'printed-and-calculated-values-retained')
    bad=copy.deepcopy(environment);bad['rows'][0].pop('unit');reject('environmental-delta',bad,'environment-unit-required')
    lean=dict(boundary='synthetic serial flow',rule_evidence=rule,aggregation_rule='serial-conditional-first-pass',steps=[dict(id='A',lead_time=dict(value=1,unit='hour'),process_time=dict(value=10,unit='minute'),complete_accurate_percent=90,evidence=rule),dict(id='B',lead_time=dict(value=40,unit='minute'),process_time=dict(value=10,unit='minute'),complete_accurate_percent=80,evidence=rule)])
    run('lean-serial-flow',lean,lambda r:r['total_lead_time_minutes']==100 and r['total_process_time_minutes']==20 and math.isclose(r['cumulative_complete_accurate_percent'],72),'serial-time-and-conditional-yield')
    bad=copy.deepcopy(lean);bad['aggregation_rule']='parallel';reject('lean-serial-flow',bad,'parallel-not-summed-as-serial')
    return rows


def role_skill_example_oracle(result):
    """CASE-PERSON is insufficient; expert help supplies no personal rating.

    The registered G249 case has no task workload/period and only a planned
    reassessment. These input facts require unresolved capacity and no approval
    or inferred promotion, even though the expert's own evidence is complete.
    """
    assessments = {row['id']: row for row in result['assessment_reviews']}
    assignments = {row['id']: row for row in result['assignment_reviews']}
    development = {row['id']: row for row in result['development_reviews']}
    assignment = assignments['ASSIGN-A']
    requirements = {row['requirement_ref']: row for row in assignment['requirements']}
    support = {row['requirement_ref']: row for row in assignment['support_reviews']}
    return (assessments['OBS-A']['state'] == 'needs-evidence'
            and assessments['OBS-A']['demonstrated_criteria'] == []
            and assessments['OBS-EXPERT']['state'] == 'evidence-contract-complete'
            and requirements['REQ-SKILL-SOL']['state'] == 'unproven'
            and support['REQ-SKILL-SOL']['state'] == 'expert-evidence-recorded'
            and assignment['state'] == 'needs-evidence'
            and assignment['capacity_state'] == 'unresolved'
            and assignment['period_state'] == 'unresolved'
            and assignment['approval'] == 'not-granted'
            and development['DEV-A']['state'] == 'development-planned'
            and development['DEV-A']['rating_change'] == 'not-inferred')


def embedded_oracle(method_id, result):
    """Independent invariants on the declared fictional cases, not output snapshots."""
    checks={
      'architecture-role-skill-assessment': role_skill_example_oracle,
      'business-attribute-evaluation': lambda r:r['observed']==99.6 and r['status']=='meets-target' and r['corrective_action'] is False,
      'scenario-traceability-review': lambda r:r['process_rows']==2 and r['column_categories']==5 and r['shared_human_actor_count']==1 and r['unspecified_cell_meaning']=='unknown-not-proven-absent',
      'environmental-annual-accounting': lambda r:r['gross_kgco2e']==890 and r['scope2_kgco2e']==480 and r['scope3_kgco2e']==410 and r['offsets_separate_kgco2e']==40,
      'architecture-backlog-trace-review': lambda r:len(r['traces'])==2 and r['mva_assessments'][0]['readiness']=='pending-evidence',
      'ea-point-of-view-review': lambda r:r['rows'][0]['unique_observed_readers']==1 and not r['gaps'],
      'project-management-strategy-review': lambda r:len(r['topic_reviews'])==5 and r['state']=='ready-for-governance-review',
      'project-highlight-review': lambda r:r['pending_change_ids']==['CH-1'] and r['approved_change_ids']==[] and r['task_reviews'][1]['completion_supported'] is False,
      'metadata-application-coverage-review': lambda r:len(r['source_universe']['function_ids'])==24 and len(r['rows'])==24 and any(x['status']=='unknown' for x in r['rows']),
      'architecture-role-catalog-review': lambda r:r['tiers_present']==['chief','enterprise','segment','solution'] and r['rows'][0]['state']=='needs-input',
      'solution-delivery-notebook-review': lambda r:r['in_scope_gap_ids']==['G-1'] and r['out_of_scope_gap_ids']==['G-2'] and len(r['pairs']['requirement_specification'])==2,
      'product-constraint-conformance-review': lambda r:r['blocked_item_ids']==['B-3','B-4'] and any(x['validity_state']=='unknown-no-as-of' for x in r['findings']) and any(g['reason']=='dispensation-validity-unknown' for g in r['gaps']),
      'domain-architecture-alignment-review': lambda r:[x['state'] for x in r['rows']]==['aligned-awaiting-review','misaligned','misaligned'],
      'incident-architecture-adjustment-review': lambda r:r['appetite_changed'] is True and r['decision_state']=='pending' and set(r['option_kinds'])=={'cancel-change','cancel-objective','change-target'},
      'dtra-adm-phase-alignment-review': lambda r:len(r['rows'])==10 and r['weak_foundational_factor_ids']==['culture','it-capability'],
      'business-scenario-checklist-review': lambda r:'premise-07' in r['open_item_ids'] and 'plan-11' in r['open_item_ids'] and any(x['reason']=='all-of-incomplete' for x in r['gaps']),
      'smart-objective-review': lambda r:[x['state'] for x in r['rows']]==['structurally-smart-awaiting-review','needs-input'] and any(x['reason']=='no-baseline' for x in r['gaps']),
    }
    return checks[method_id](result)
