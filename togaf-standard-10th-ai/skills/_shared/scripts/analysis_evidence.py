"""Validate declared evidence references without mistaking business IDs for sources.

Empty evidence remains a calculator-specific missing-input decision. A supplied
reference must have the right shape and resolve in every declared inventory.
"""
import json

# These are input contracts, not a suffix heuristic. [] traverses records and {}
# traverses a keyed record map. Names in free-form notes remain ordinary prose.
REFERENCE_PATHS = {
    'weighted-normalized-decision': 'rule_evidence',
    'preference-weighted-decision': 'rule_evidence',
    'risk-explicit-rule': 'rule_evidence likelihood.evidence impact.evidence',
    'maturity-weighted': 'rule_evidence factors.[].evidence',
    'dtra-factor-review': 'rule_evidence attention_threshold_evidence factors.[].evidence',
    'environmental-delta': 'method_evidence rows.[].evidence',
    'lean-serial-flow': 'rule_evidence steps.[].evidence',
    'change-profile-checklist': 'rule_evidence responses.{}.evidence tailoring.{}.evidence',
    'business-attribute-evaluation': 'source_refs measurement_approach.source_refs metric.evidence target.evidence tolerable_deviation.evidence corrective_action_trigger.evidence frequency_or_cost_threshold.evidence',
    'scenario-traceability-review': 'raw_record_ids associations.[].evidence painpoint_outcomes.[].evidence derived_requirements.[].evidence',
    'environmental-annual-accounting': 'rules.source_refs boundary.scope1_evidence rows.[].evidence factor.evidence factor.applicability.evidence factors.[].evidence factors.[].applicability.evidence cloud_record.evidence cloud_record.scope1.evidence cloud_records.[].evidence cloud_records.[].scope1.evidence offsets.organization.evidence offsets.provider.evidence prior_year.evidence',
    'architecture-backlog-trace-review': 'hierarchy_policy.evidence nodes.[].evidence nodes.[].priority_evidence nodes.[].decision_evidence nodes.[].acceptance.evidence nodes.[].history.[].evidence relationships.[].evidence',
    'delivery-style-review': 'features.[].evidence_refs decisions.[].evidence_refs',
    'set-based-options-review': 'constraint_review.evidence_refs constraints.[].evidence_refs iterations.[].evidence_refs iterations.[].new_evidence_refs',
    'ea-point-of-view-review': 'points.[].evidence points.[].distribution_record.evidence points.[].reading_events.[].evidence points.[].initiated_changes.[].evidence',
    'project-management-strategy-review': 'evidence confirmation_evidence topics.[].evidence topics.[].delegated_tolerances.[].evidence',
    'project-highlight-review': 'evidence schedule_tolerance.evidence tasks.[].evidence tasks.[].acceptance_evidence risks_issues.[].evidence changes.[].evidence changes.[].approval_evidence',
    'metadata-application-coverage-review': 'scope_evidence tools.[].evidence assets.[].evidence assessments.[].requirement_evidence assessments.[].exclusion.evidence assessments.[].excluded_facets.[].evidence assessments.[].excluded_categories.[].evidence assessments.[].bindings.[].plan.evidence assessments.[].bindings.[].verification.evidence assessments.[].bindings.[].verification.acceptance_observations.[].evidence',
    'dependency-topological-order': 'rule_evidence work_packages.[].evidence dependencies.[].evidence',
    'transition-operability-check': 'rule_evidence conditions.{}.evidence rollback.evidence',
    'work-package-prioritization': 'rule_evidence criteria.[].weight_evidence criteria.[].scale_evidence work_packages.[].score_evidence.{} sensitivity.evidence',
    'benefit-realization-trigger': 'rule_evidence baseline.evidence target.evidence observed.evidence trigger.evidence',
    'architecture-role-catalog-review': 'roles.[].evidence roles.[].kpis.[].evidence roles.[].relationships.[].evidence roles.[].assignments.[].evidence hierarchy_policy.evidence',
    'architecture-role-skill-assessment': 'mandate.evidence tasks.[].evidence roles.[].evidence requirements.[].evidence assessments.[].evidence assessments.[].behavioral_evidence.[].evidence assignments.[].evidence assignments.[].support.evidence development.[].evidence development.[].reassessment.evidence development.[].history.[].evidence scales.[].evidence interpretations.[].evidence model_objects.[].evidence model_relationships.[].evidence',
    'solution-delivery-notebook-review': 'evidence risks.[].treatment_evidence',
    'product-constraint-conformance-review': 'products.[].evidence constraints.[].evidence dispensations.[].evidence',
    'domain-architecture-alignment-review': 'domains.[].evidence',
    'incident-architecture-adjustment-review': 'incident.evidence decision.evidence',
    'dtra-adm-phase-alignment-review': 'phase_records.[].evidence',
    'business-scenario-checklist-review': 'responses.{}.evidence role_assignments.[].evidence',
    'smart-objective-review': 'goals.[].evidence objectives.[].evidence objectives.[].realism_evidence',
}
REFERENCE_PATHS = {method: tuple(path.split('.') for path in paths.split())
                   for method, paths in REFERENCE_PATHS.items()}
SCALAR_REFERENCE_PATHS = {
    'business-attribute-evaluation': (('business_case_ref',),),
    'scenario-traceability-review': (('normalized_records', '[]', 'from'),),
    'metadata-application-coverage-review': (('evidence_records', '[]', 'id'),),
}


def evidence_issues(analysis, model=None):
    findings = []
    aid = analysis.get('id', 'analysis') if isinstance(analysis, dict) else 'analysis'

    def issue(code, path, message):
        findings.append({'level': 'error', 'code': code, 'id': str(aid) + ':' + path,
                         'path': path, 'message': message})

    if not isinstance(analysis, dict) or not isinstance(analysis.get('inputs'), dict):
        issue('analysis-evidence-shape', 'inputs', 'Analysis inputs must be an object.')
        return findings
    data = analysis['inputs']
    known = None
    if model is not None:
        known = {s.get('id') for s in model.get('sources', [])
                 if isinstance(s, dict) and isinstance(s.get('id'), str)}
    declared = None

    def references(value, path, inventory=False):
        if not isinstance(value, list):
            issue('analysis-evidence-shape', path, 'Evidence references must be a list of nonempty source IDs.')
            return
        seen = set()
        for index, sid in enumerate(value):
            position = path + '[' + str(index) + ']'
            if not isinstance(sid, str) or not sid.strip():
                issue('analysis-evidence-shape', position, 'A source reference must be a nonempty string.')
                continue
            if inventory and sid in seen:
                issue('analysis-evidence-shape', position, 'Source inventory contains a duplicate ID.')
            seen.add(sid)
            if known is not None and sid not in known:
                issue('analysis-source-inventory', position, 'Evidence source is absent from model.sources: ' + sid)
            if not inventory and declared is not None and sid not in declared:
                issue('analysis-source-declaration', position, 'Evidence source is absent from inputs.source_ids: ' + sid)

    if 'source_ids' in data:
        references(data['source_ids'], 'inputs.source_ids', inventory=True)
        if isinstance(data['source_ids'], list):
            declared = {s for s in data['source_ids'] if isinstance(s, str) and s.strip()}

    def select(value, tokens, path, scalar=False):
        if not tokens:
            references([value] if scalar else value, path)
            return
        token, remaining = tokens[0], tokens[1:]
        if token == '[]':
            if not isinstance(value, list):
                issue('analysis-evidence-shape', path, 'Expected a list of records containing evidence references.')
                return
            for index, child in enumerate(value):
                select(child, remaining, path + '[' + str(index) + ']', scalar)
        elif token == '{}':
            if not isinstance(value, dict):
                issue('analysis-evidence-shape', path, 'Expected a keyed object containing evidence references.')
                return
            for key, child in value.items():
                select(child, remaining, path + '.' + str(key), scalar)
        elif not isinstance(value, dict):
            issue('analysis-evidence-shape', path, 'Expected a record containing evidence references.')
        elif token in value:
            select(value[token], remaining, path + '.' + token, scalar)

    method = analysis.get('method_id')
    for tokens in REFERENCE_PATHS.get(method, ()):
        select(data, tokens, 'inputs')
    for tokens in SCALAR_REFERENCE_PATHS.get(method, ()):
        select(data, tokens, 'inputs', scalar=True)
    if 'evidence' in analysis:
        references(analysis['evidence'], 'evidence')
    return findings


def require_evidence(analysis, model=None):
    findings = evidence_issues(analysis, model)
    if findings:
        raise ValueError(json.dumps(findings, ensure_ascii=False))
