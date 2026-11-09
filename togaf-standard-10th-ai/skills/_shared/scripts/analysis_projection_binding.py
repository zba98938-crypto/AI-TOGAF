"""Versioned, method-specific projections of calculator snapshots into models.

Only registered projections can bind a snapshot. Local business references and
historical observations are not guessed to be current model entity IDs.
"""

VERSION = 'analysis-binding/1'
MISSING = object()
META = {'source_ids', 'model_binding'}

# A projection selects the portion of an analysis represented by a work product.
# Several views may project different portions of the same complete analysis.
PROFILE_PROJECTIONS = {
    'architecture-strategic-mva-trace': ('architecture-backlog-trace-review', 'full'),
    'metadata-application-function-coverage': ('metadata-application-coverage-review', 'full'),
    'business-attribute-profile-default': ('business-attribute-evaluation', 'full'),
    'business-attribute-profile-trace': ('business-attribute-evaluation', 'full'),
    'environmental-is-assessment-default': ('environmental-annual-accounting', 'environment-rows'),
    'annual-environmental-accounting': ('environmental-annual-accounting', 'environment-rows'),
    'environmental-accounting-basis': ('environmental-annual-accounting', 'environment-basis'),
    'scenario-traceability-matrix-default': ('scenario-traceability-review', 'scenario-associations'),
    'scenario-painpoint-outcome-matrix': ('scenario-traceability-review', 'scenario-outcomes'),
    'scenario-transformation-audit': ('scenario-traceability-review', 'scenario-audit'),
    'ea-point-of-view-register-default': ('ea-point-of-view-review', 'full'),
    'project-management-strategy-default': ('project-management-strategy-review', 'full'),
    'project-status-highlight-report-default': ('project-highlight-review', 'full'),
    'architecture-role-catalog-default': ('architecture-role-catalog-review', 'full'),
    'architecture-role-collaboration': ('architecture-role-catalog-review', 'full'),
    'solution-delivery-notebook-default': ('solution-delivery-notebook-review', 'full'),
    'product-constraint-register-default': ('product-constraint-conformance-review', 'full'),
    'domain-architecture-alignment-default': ('domain-architecture-alignment-review', 'full'),
    'incident-architecture-adjustment-default': ('incident-architecture-adjustment-review', 'full'),
    'dtra-adm-phase-alignment-default': ('dtra-adm-phase-alignment-review', 'full'),
    'business-scenario-checklist-record-default': ('business-scenario-checklist-review', 'full'),
    'smart-objective-assessment-default': ('smart-objective-review', 'full'),
}
METHOD_PROJECTIONS = {}
for _method, _projection in PROFILE_PROJECTIONS.values():
    METHOD_PROJECTIONS.setdefault(_method, set()).add(_projection)

# Fields consumed by the calculator are checked in both directions. Additional
# supplied fields are also checked, but unrelated model metadata is not an input.
FIELDS = {
    'business_attribute': 'business_case_ref definition measurement_approach metric target tolerable_deviation corrective_action_trigger frequency_or_cost_threshold owner source_refs',
    'guide:ea-point-of-view': 'charter_alignment ecosystem_change decision_question position rationale alternatives recommendation adoption_timing cost_risk_tradeoff audience_ids document_version distribution_record reading_events initiated_changes follow_up evidence',
    'guide:project-management-strategy': 'project_scope selected_method method_tailoring project_governance architecture_governance confirmation_state confirmation_evidence topics evidence',
    'guide:project-highlight-report': 'period next_period audience communication_plan_ref approved_plan_ref previous_planned_task_ids tasks next_period_activities risks_issues corrective_actions remaining_stage_forecast remaining_project_forecast decisions_required changes schedule_tolerance evidence',
    'guide:architecture-role': 'name tier scope primary_responsibility segment_scope activities key_stakeholders leads relationships assignments kpis evidence',
    'guide:solution-delivery-notebook': 'name work_package_id solution_concept_ref implementation_strategy stakeholders requirements specifications risks controls gaps architecture_summary out_of_scope_gap_statement evidence',
    'guide:product-constraint-register': 'name purpose products constraints backlog_items dispensations',
    'guide:ea-project-scope': 'objective_ids',
    'guide:domain-architecture': 'name kind project_id objective_ids shared_entity_ids treated_as referenced_domain_ids evidence',
    'guide:incident-adjustment': 'summary incident objectives risk_appetite_before risk_appetite_after risk_tolerance requirement_changes options decision',
    'guide:dtra-alignment-summary': 'assessment_ref initiated_in_phase factor_ratings reassessment progression_note deferred_factors',
    'guide:dtra-phase-record': 'name phase implication considered_factor_ids actions requirement_changes tailored_out governance_distinction evidence',
    'guide:goal': 'name statement category organization_category business_goal_ref evidence',
    'guide:smart-objective': 'name goal_id statement scope measure unit baseline target owner action realism_rationale realism_evidence due evidence',
    'environment_measure': 'object organization_scope lifecycle_stage activity activity_unit factor_ref allocation value unit evidence overlap_group cloud_ref provider_scope_refs',
}
FIELDS = {key: set(value.split()) for key, value in FIELDS.items()}

SIMPLE_LISTS = {
    'ea-point-of-view-review': ('points', 'guide:ea-point-of-view'),
    'architecture-role-catalog-review': ('roles', 'guide:architecture-role'),
}
SIMPLE_ROOTS = {
    'project-management-strategy-review': 'guide:project-management-strategy',
    'project-highlight-review': 'guide:project-highlight-report',
    'solution-delivery-notebook-review': 'guide:solution-delivery-notebook',
    'product-constraint-conformance-review': 'guide:product-constraint-register',
    'incident-architecture-adjustment-review': 'guide:incident-adjustment',
}
SELECTORS = {
    'product-constraint-conformance-review': {'record_id'},
    'incident-architecture-adjustment-review': {'record_id'},
    'dtra-adm-phase-alignment-review': {'summary_id'},
    'business-scenario-checklist-review': {'stage_entity_ids'},
    'environmental-annual-accounting': {'basis_entity_ids'},
    'scenario-traceability-review': {'raw_entity_ids'},
}


def _equal(left, right):
    """JSON equality with bool distinct from number, including nested fields."""
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is type(right) and left == right
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(_equal(left[k], right[k]) for k in left)
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(_equal(a, b) for a, b in zip(left, right))
    return left == right


class ProjectionBinding:
    def __init__(self, model, analysis):
        self.model, self.analysis = model, analysis
        self.data = analysis.get('inputs', {})
        self.method = analysis.get('method_id')
        self.findings = []
        self.entities = self.index(model.get('entities', []), 'entities')
        self.relations = self.index(model.get('relationships', []), 'relationships')
        self.views = self.index(model.get('views', []), 'views')
        self.selectors = {}
        self.bound_entity_ids = set()
        self.linked = [v for v in self.views.values()
                       if analysis.get('id') in v.get('attributes', {}).get('analysis_ids', [])]

    def issue(self, code, path, message):
        self.findings.append({'level': 'error', 'code': code,
                              'id': str(self.analysis.get('id', 'analysis')) + ':' + str(path),
                              'path': str(path), 'message': message})

    def index(self, rows, path):
        result = {}
        if not isinstance(rows, list):
            self.issue('analysis-binding-shape', path, 'Expected a list of records.')
            return result
        for pos, row in enumerate(rows):
            identity = row.get('id') if isinstance(row, dict) else None
            if not isinstance(identity, str) or not identity.strip():
                self.issue('analysis-binding-shape', path + '[' + str(pos) + ']', 'Record requires a nonempty string ID.')
            elif identity in result:
                self.issue('analysis-binding-identity', path + '.' + identity, 'Duplicate stable ID in the same record collection.')
            else:
                result[identity] = row
        return result

    def records(self, key):
        return self.index(self.data.get(key, []), 'inputs.' + key)

    def compare(self, actual, expected, path):
        if not _equal(actual, expected):
            self.issue('analysis-model-field-mismatch', path,
                       'Analysis snapshot differs from the current model; review and synchronize before reusing conclusions.')

    def entity(self, identity, typ):
        current = self.entities.get(identity) if isinstance(identity, str) else None
        if current is None:
            self.issue('analysis-model-entity', str(identity), 'Snapshot requires an existing same-ID model entity.')
        elif current.get('type') != typ:
            self.issue('analysis-model-type', str(identity), 'Expected model entity type ' + typ + '.')
            return None
        if current is not None:
            self.bound_entity_ids.add(identity)
        return current

    def snapshot(self, row, typ, identity=None, attributes_only=False, fields=None):
        if not isinstance(row, dict):
            self.issue('analysis-binding-shape', str(identity), 'Snapshot must be an object.')
            return
        identity = identity if identity is not None else row.get('id')
        current = self.entity(identity, typ)
        if current is None:
            return
        attrs = current.get('attributes', {})
        checked = (set(row) - META - {'id'}) | (FIELDS.get(typ, set()) if fields is None else set(fields))
        if attributes_only and 'id' in row:
            checked.add('id')
        for field in sorted(checked):
            origin = current if not attributes_only and field in ('name', 'evidence') else attrs
            self.compare(origin.get(field, MISSING), row.get(field, MISSING), str(identity) + '.' + field)

    def choose(self, typ, views, selector, predicate=None):
        explicit = self.selectors.get(selector)
        if explicit is not None:
            current = self.entity(explicit, typ)
            if current is not None and predicate is not None and not predicate(current):
                self.issue('analysis-binding-selection', selector, 'Selected entity does not satisfy the projection contract.')
            if views and not any(explicit in v.get('entity_ids', []) for v in views):
                self.issue('analysis-binding-selection', selector, 'Selected entity is outside the bound views.')
            return explicit
        # A type-only global search would bind an unrelated project register.
        candidates = {eid for view in views for eid in view.get('entity_ids', [])
                      if self.entities.get(eid, {}).get('type') == typ
                      and (predicate is None or predicate(self.entities[eid]))}
        if len(candidates) != 1:
            code = 'analysis-binding-ambiguous' if len(candidates) > 1 else 'analysis-binding-required'
            self.issue(code, selector, 'Provide a unique view-selected entity or an explicit registered selector.')
            return None
        identity = next(iter(candidates))
        self.bound_entity_ids.add(identity)
        return identity

    def closure(self, views, expected, types, relations=None):
        for view in views:
            actual = {eid for eid in view.get('entity_ids', []) if self.entities.get(eid, {}).get('type') in types}
            if actual != set(expected):
                self.issue('analysis-view-entity-selection', view['id'], 'View projection entity set differs from the analysis snapshot.')
            if relations is not None and set(view.get('relationship_ids', [])) != set(relations):
                self.issue('analysis-view-relationship-selection', view['id'], 'View projection relationship set differs from the analysis snapshot.')

    def projections(self):
        allowed = METHOD_PROJECTIONS[self.method]
        selected = {}
        for view in self.linked:
            registered = PROFILE_PROJECTIONS.get(view.get('profile_id'))
            if registered:
                if registered[0] != self.method:
                    self.issue('analysis-binding-selection', view['id'], 'View profile is registered for another analysis method.')
                else:
                    selected.setdefault(registered[1], []).append(view)
        binding = self.data.get('model_binding')
        if binding is not None:
            if not isinstance(binding, dict) or binding.get('version') != VERSION:
                self.issue('analysis-binding-shape', 'inputs.model_binding', 'Expected ' + VERSION + ' binding metadata.')
                return {}
            if set(binding) - {'version', 'projection', 'view_ids', 'selectors'}:
                self.issue('analysis-binding-shape', 'inputs.model_binding', 'Unsupported binding metadata field.')
            projection = binding.get('projection')
            if not isinstance(projection, str) or projection not in allowed:
                self.issue('analysis-binding-selection', 'inputs.model_binding.projection', 'Projection is not registered for this method.')
                return {}
            self.selectors = binding.get('selectors', {})
            if not isinstance(self.selectors, dict) or set(self.selectors) - SELECTORS.get(self.method, set()):
                self.issue('analysis-binding-shape', 'inputs.model_binding.selectors', 'Unsupported selector for this method.')
                return {}
            for key, value in self.selectors.items():
                if key.endswith('_ids') and not isinstance(value, dict):
                    self.issue('analysis-binding-shape', 'inputs.model_binding.selectors.' + key, 'Expected a map of semantic selector keys to entity IDs.')
                    return {}
                values = value.values() if key.endswith('_ids') else [value]
                if any(not isinstance(v, str) or not v.strip() for v in values):
                    self.issue('analysis-binding-shape', 'inputs.model_binding.selectors.' + key, 'Selectors must contain nonempty entity IDs.')
            vids = binding.get('view_ids', [])
            if not isinstance(vids, list) or any(not isinstance(v, str) for v in vids) or len(vids) != len(set(vids)):
                self.issue('analysis-binding-shape', 'inputs.model_binding.view_ids', 'Expected unique view IDs.')
                return {}
            views = []
            for vid in vids:
                view = self.views.get(vid)
                if view is None or view not in self.linked:
                    self.issue('analysis-binding-selection', vid, 'Bound view must exist and reference this analysis.')
                    continue
                registered = PROFILE_PROJECTIONS.get(view.get('profile_id'))
                if registered and registered != (self.method, projection):
                    self.issue('analysis-binding-selection', vid, 'Explicit projection disagrees with the registered view profile.')
                    continue
                views.append(view)
            selected.setdefault(projection, [])
            selected[projection] += [v for v in views if v not in selected[projection]]
        if not selected:
            if allowed == {'full'}:
                selected['full'] = self.linked
            else:
                self.issue('analysis-binding-required', 'inputs.model_binding', 'A partial snapshot needs a registered view profile or an explicit projection.')
        return selected

    def full(self, views):
        method, data = self.method, self.data
        if method in SIMPLE_LISTS:
            key, typ = SIMPLE_LISTS[method]
            records = self.records(key)
            for row in records.values():
                self.snapshot(row, typ)
            self.closure(views, records, {typ})
        elif method in SIMPLE_ROOTS:
            typ = SIMPLE_ROOTS[method]
            identity = data.get('id')
            if method in ('product-constraint-conformance-review', 'incident-architecture-adjustment-review'):
                identity = self.choose(typ, views, 'record_id')
            if identity is not None:
                self.snapshot(data, typ, identity)
                self.closure(views, {identity}, {typ})
            else:
                self.issue('analysis-binding-required', 'inputs.id', 'Snapshot needs an explicit stable model record ID.')
        elif method == 'business-attribute-evaluation':
            row = {k: v for k, v in data.items() if k != 'attribute_id'}
            identity = data.get('attribute_id')
            self.snapshot(row, 'business_attribute', identity)
            self.closure(views, {identity}, {'business_attribute'})
        elif method == 'domain-architecture-alignment-review':
            project = data.get('ea_project', {})
            self.snapshot(project, 'guide:ea-project-scope')
            domains = self.records('domains')
            for row in domains.values():
                self.snapshot(row, 'guide:domain-architecture')
            self.closure(views, set(domains) | {project.get('id')}, {'guide:ea-project-scope', 'guide:domain-architecture'})
        elif method == 'smart-objective-review':
            ids = set()
            for key, typ in [('goals', 'guide:goal'), ('objectives', 'guide:smart-objective')]:
                records = self.records(key)
                ids.update(records)
                for row in records.values():
                    self.snapshot(row, typ)
            self.closure(views, ids, {'guide:goal', 'guide:smart-objective'})
        elif method == 'dtra-adm-phase-alignment-review':
            summary = self.choose('guide:dtra-alignment-summary', views, 'summary_id')
            if summary is not None:
                row = {k: v for k, v in data.items() if k != 'phase_records'}
                self.snapshot(row, 'guide:dtra-alignment-summary', summary)
            records = self.records('phase_records')
            for row in records.values():
                self.snapshot(row, 'guide:dtra-phase-record')
            self.closure(views, set(records) | ({summary} if summary else set()), {'guide:dtra-alignment-summary', 'guide:dtra-phase-record'})
        elif method == 'business-scenario-checklist-review':
            self.checklist(views)

    def checklist(self, views):
        from scenario_readiness_analysis import _stage_index
        from gap_closure_tables import SCENARIO_STAGES
        data = self.data
        stages = data.get('stages') or [s['id'] for s in SCENARIO_STAGES]
        stage_map = _stage_index()
        choices = self.selectors.get('stage_entity_ids', {})
        ids = set()
        for stage in stages:
            selector = 'stage:' + stage
            if stage in choices:
                self.selectors[selector] = choices[stage]
            identity = self.choose('guide:scenario-checklist-stage', views, selector,
                                   lambda e: e.get('attributes', {}).get('stage') == stage)
            if identity is None:
                continue
            ids.add(identity)
            row = {'stage': stage, 'responses': {k: v for k, v in data.get('responses', {}).items()
                                                if stage_map.get(k, {}).get('stage') == stage},
                   'uses_workshop': bool(data.get('uses_workshop')),
                   'role_assignments': [a for a in data.get('role_assignments', []) if a.get('assigned_in_stage') == stage]}
            self.snapshot(row, 'guide:scenario-checklist-stage', identity, fields=row)
        self.closure(views, ids, {'guide:scenario-checklist-stage'})

    def environment(self, projection, views):
        data = self.data
        if projection == 'environment-rows':
            rows = self.records('rows')
            for row in rows.values():
                self.snapshot(row, 'environment_measure', attributes_only=True)
            self.closure(views, rows, {'environment_measure'})
            return
        expected = set()
        choices = self.selectors.get('basis_entity_ids', {})
        # Each record is a separate declared basis, including prior-year values.
        for key in ('boundary', 'factor', 'factors', 'cloud_record', 'cloud_records', 'prior_year', 'offsets', 'rules'):
            if key not in data:
                continue
            selector = 'basis:' + key
            if key in choices:
                self.selectors[selector] = choices[key]
            identity = self.choose('repository_asset', views, selector,
                                   lambda e: e.get('attributes', {}).get('record_kind') == key)
            if identity is None:
                continue
            expected.add(identity)
            current = self.entities.get(identity, {}).get('attributes', {})
            actual = {k: v for k, v in current.items() if k != 'record_kind'}
            self.compare(actual, data[key], identity + '.attributes')
        self.closure(views, expected, {'repository_asset'})

    def scenario(self, projection, views):
        data = self.data
        kinds = {'stakeholder': 'stakeholder', 'human_actor': 'actor', 'computer_actor': 'application', 'problem': 'problem', 'objective': 'goal'}
        cats = data.get('categories', {})
        if projection in ('scenario-associations', 'scenario-outcomes'):
            expected = set()
            selected_kinds = kinds if projection == 'scenario-associations' else {'problem': 'problem', 'objective': 'goal'}
            for kind, typ in selected_kinds.items():
                for identity in cats.get(kind, []):
                    self.entity(identity, typ)
                    expected.add(identity)
            if projection == 'scenario-associations':
                for identity in data.get('processes', []):
                    self.entity(identity, 'process')
                    expected.add(identity)
            key = 'associations' if projection == 'scenario-associations' else 'painpoint_outcomes'
            rows = self.records(key)
            for identity, row in rows.items():
                current = self.relations.get(identity)
                if current is None:
                    self.issue('analysis-model-relationship', identity, 'Projected relationship is missing from the current model.')
                    continue
                wanted = {'type': 'traces_to', 'source': row.get('process', row.get('problem')),
                          'target': row.get('target', row.get('outcome')), 'evidence': row.get('evidence')}
                for field, value in wanted.items():
                    self.compare(current.get(field, MISSING), value, identity + '.' + field)
                self.compare(current.get('extension_data', {}).get('togaf-addenda:g176-scenario', {}).get('association_kind'),
                             row.get('kind', 'painpoint-outcome'), identity + '.association_kind')
            self.closure(views, expected, set(selected_kinds.values()) | {'process'}, rows)
            return
        expected = set()
        choices = self.selectors.get('raw_entity_ids', {})
        for sid in data.get('raw_record_ids', []):
            selector = 'raw:' + sid
            if sid in choices:
                self.selectors[selector] = choices[sid]
            identity = self.choose('repository_asset', views, selector,
                                   lambda e: e.get('attributes', {}).get('record_kind') == 'raw' and e.get('attributes', {}).get('raw_id') == sid)
            if identity is None:
                continue
            expected.add(identity)
            source = next((s for s in self.model.get('sources', []) if s.get('id') == sid), {})
            self.compare(self.entities[identity].get('attributes', {}).get('text'), source.get('description'), identity + '.text')
            self.compare(self.entities[identity].get('evidence'), [sid], identity + '.evidence')
        for key, kind in [('normalized_records', 'normalized'), ('transformation_log', 'transformation'), ('derived_requirements', 'derived-requirement')]:
            records = self.records(key)
            for identity, row in records.items():
                expected.add(identity)
                current = self.entity(identity, 'repository_asset')
                if current is None:
                    continue
                self.compare(current.get('attributes', {}), dict(row, record_kind=kind), identity + '.attributes')
        self.closure(views, expected, {'repository_asset'}, [])

    def run(self):
        for projection, views in self.projections().items():
            if projection == 'full':
                self.full(views)
            elif projection.startswith('environment-'):
                self.environment(projection, views)
            else:
                self.scenario(projection, views)
        if (not self.findings and not self.bound_entity_ids and
                self.method not in ('architecture-backlog-trace-review', 'metadata-application-coverage-review')):
            self.issue('analysis-binding-required', 'inputs', 'Snapshot projection did not bind any current model record.')
        return self.findings


def binding_issues(model, analysis):
    if analysis.get('method_id') not in METHOD_PROJECTIONS:
        return []
    checker = None
    try:
        checker = ProjectionBinding(model, analysis)
        return checker.run()
    except (KeyError, TypeError, AttributeError, IndexError) as exc:
        finding = {'level': 'error', 'code': 'analysis-binding-shape',
                   'id': str(analysis.get('id', 'analysis')) + ':inputs', 'path': 'inputs',
                   'message': 'Malformed projection input: ' + str(exc)}
        return (checker.findings if checker is not None else []) + [finding]
