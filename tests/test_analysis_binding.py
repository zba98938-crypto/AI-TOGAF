"""Regression contracts for model snapshots and evidence inventory boundaries."""
import copy
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from analysis_binding import binding_issues, require_binding
from analysis_evidence import evidence_issues, require_evidence
from analysis_projection_binding import VERSION
from profile_examples import normalize_example


class BindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        registry = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/capabilities.json').read_text())
        cls.profiles = {p['id']: p for p in registry['profiles']}

    def example(self, profile):
        model = normalize_example(self.profiles[profile])
        return model, model['analyses'][0]

    def test_all_embedded_analysis_examples_bind(self):
        count = 0
        for profile in self.profiles.values():
            if not profile.get('example', {}).get('analyses'):
                continue
            model = normalize_example(profile)
            for analysis in model['analyses']:
                with self.subTest(profile=profile['id']):
                    self.assertEqual([], binding_issues(model, analysis))
                count += 1
        self.assertGreaterEqual(count, 21)

    def test_stale_domain_blocks_validation_and_evaluation(self):
        from analyze import evaluate
        from validate import validate
        model, analysis = self.example('domain-architecture-alignment-default')
        domain = next(e for e in model['entities'] if e['id'] == 'DOM-DATA')
        domain['attributes'].update(project_id='EA-2027', objective_ids=['OBJ-1'], shared_entity_ids=['cap-fulfilment'])
        self.assertIn('analysis-model-field-mismatch', {f['code'] for f in validate(model)})
        with self.assertRaises(ValueError):
            evaluate(analysis, model)

    def test_stale_domain_is_rejected_by_public_clis(self):
        model, analysis = self.example('domain-architecture-alignment-default')
        domain = next(e for e in model['entities'] if e['id'] == 'DOM-DATA')
        domain['attributes'].update(project_id='EA-2027', objective_ids=['OBJ-1'], shared_entity_ids=['cap-fulfilment'])
        with tempfile.TemporaryDirectory(prefix='togaf-stale-analysis-') as temporary:
            directory = Path(temporary)
            source = directory / 'model.json'
            source.write_text(json.dumps(model, ensure_ascii=False))
            commands = [('validate.py', [str(source)]),
                        ('analyze.py', [str(source), '--evaluate', analysis['id']]),
                        ('generate.py', [str(source), '--all', '--strict', '--out', str(directory / 'generated')])]
            for script, args in commands:
                with self.subTest(script=script):
                    result = subprocess.run([sys.executable, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts' / script), *args],
                                            cwd=directory, capture_output=True, text=True)
                    self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
                    self.assertIn('analysis-model-field-mismatch', result.stdout + result.stderr)
            self.assertFalse((directory / 'generated/manifest.json').exists())

    def test_mutations_in_every_new_projection_are_detected(self):
        cases = {
            'business-attribute-profile-default': (0, 'owner'),
            'environmental-is-assessment-default': (0, 'value'),
            'environmental-accounting-basis': (0, 'period'),
            'ea-point-of-view-register-default': (0, 'position'),
            'project-management-strategy-default': (0, 'selected_method'),
            'project-status-highlight-report-default': (0, 'tasks'),
            'architecture-role-catalog-default': (0, 'tier'),
            'solution-delivery-notebook-default': (0, 'requirements'),
            'product-constraint-register-default': (0, 'constraints'),
            'domain-architecture-alignment-default': (0, 'objective_ids'),
            'incident-architecture-adjustment-default': (0, 'risk_tolerance'),
            'dtra-adm-phase-alignment-default': (0, 'factor_ratings'),
            'business-scenario-checklist-record-default': (0, 'responses'),
            'smart-objective-assessment-default': (1, 'target'),
            'scenario-transformation-audit': (3, 'text'),
        }
        for profile, (index, key) in cases.items():
            with self.subTest(profile=profile):
                model, analysis = self.example(profile)
                model['entities'][index]['attributes'][key] = 'changed-without-review'
                self.assertIn('analysis-model-field-mismatch', {f['code'] for f in binding_issues(model, analysis)})
        for profile in ['scenario-traceability-matrix-default', 'scenario-painpoint-outcome-matrix']:
            model, analysis = self.example(profile)
            model['relationships'][0]['target'] = 'changed-endpoint'
            self.assertTrue(binding_issues(model, analysis))

    def test_missing_snapshot_field_does_not_silently_use_calculator_default(self):
        model, analysis = self.example('domain-architecture-alignment-default')
        del analysis['inputs']['domains'][0]['shared_entity_ids']
        self.assertTrue(binding_issues(model, analysis))

    def test_legacy_snapshots_check_deleted_consumed_fields_in_both_directions(self):
        for side in ('model', 'inputs'):
            model, analysis = self.example('architecture-strategic-mva-trace')
            story = next(n for n in analysis['inputs']['nodes'] if n['kind'] == 'story')
            entity = next(e for e in model['entities'] if e['id'] == story['id'])
            del (story if side == 'inputs' else entity['attributes'])['acceptance']
            self.assertIn('analysis-model-field-mismatch', {f['code'] for f in binding_issues(model, analysis)})
            model, analysis = self.example('metadata-application-function-coverage')
            tool = analysis['inputs']['tools'][0]
            entity = next(e for e in model['entities'] if e['id'] == tool['id'])
            del (tool if side == 'inputs' else entity['attributes'])['owner']
            self.assertIn('metadata-binding-field', {f['code'] for f in binding_issues(model, analysis)})

    def test_deleted_environment_basis_record_is_detected(self):
        model, analysis = self.example('environmental-accounting-basis')
        del analysis['inputs']['prior_year']
        self.assertIn('analysis-view-entity-selection', {f['code'] for f in binding_issues(model, analysis)})

    def test_specialized_snapshots_reject_unknown_explicit_binding(self):
        for profile in ('architecture-strategic-mva-trace', 'metadata-application-function-coverage'):
            model, analysis = self.example(profile)
            analysis['inputs']['model_binding'] = {'version': VERSION, 'projection': 'independent'}
            self.assertIn('analysis-binding-selection', {f['code'] for f in binding_issues(model, analysis)})

    def test_input_change_without_model_change_is_detected(self):
        model, analysis = self.example('project-status-highlight-report-default')
        analysis['inputs']['tasks'][0]['state'] = 'cancelled'
        self.assertTrue(binding_issues(model, analysis))

    def test_removed_snapshot_record_is_detected_by_view_scope(self):
        model, analysis = self.example('smart-objective-assessment-default')
        analysis['inputs']['objectives'].pop()
        self.assertIn('analysis-view-entity-selection', {f['code'] for f in binding_issues(model, analysis)})

    def test_nested_local_ids_are_not_model_ids(self):
        model, analysis = self.example('solution-delivery-notebook-default')
        ids = {e['id'] for e in model['entities']}
        self.assertNotIn(analysis['inputs']['requirements'][0]['id'], ids)
        self.assertEqual([], binding_issues(model, analysis))

    def test_partial_profiles_allow_nonprojected_inputs(self):
        for profile in ['scenario-painpoint-outcome-matrix', 'scenario-transformation-audit', 'environmental-accounting-basis']:
            model, analysis = self.example(profile)
            self.assertEqual([], binding_issues(model, analysis))
        model, analysis = self.example('annual-environmental-accounting')
        self.assertNotEqual(analysis['inputs']['prior_year']['rows'][0], analysis['inputs']['rows'][0]['value'])
        self.assertEqual([], binding_issues(model, analysis))

    def test_unknown_partial_projection_requires_binding(self):
        model, analysis = self.example('scenario-painpoint-outcome-matrix')
        model['views'] = []
        self.assertIn('analysis-binding-required', {f['code'] for f in binding_issues(model, analysis)})

    def test_empty_unlinked_projection_cannot_claim_a_binding(self):
        model, analysis = self.example('ea-point-of-view-register-default')
        model['views'] = []
        analysis['inputs']['points'] = []
        self.assertIn('analysis-binding-required', {f['code'] for f in binding_issues(model, analysis)})

    def test_singleton_does_not_bind_unrelated_global_entity(self):
        model, analysis = self.example('product-constraint-register-default')
        model['views'] = []
        self.assertIn('analysis-binding-required', {f['code'] for f in binding_issues(model, analysis)})
        analysis['inputs']['model_binding'] = {'version': VERSION, 'projection': 'full', 'selectors': {'record_id': 'PCC-REG'}}
        self.assertEqual([], binding_issues(model, analysis))

    def test_ambiguous_singleton_requires_selector(self):
        model, analysis = self.example('incident-architecture-adjustment-default')
        other = copy.deepcopy(model['entities'][0]); other['id'] = 'INC-OTHER'
        model['entities'].append(other); model['views'][0]['entity_ids'].append(other['id'])
        self.assertIn('analysis-binding-ambiguous', {f['code'] for f in binding_issues(model, analysis)})

    def test_explicit_projection_cannot_hide_registered_view(self):
        model, analysis = self.example('scenario-traceability-matrix-default')
        analysis['inputs']['model_binding'] = {'version': VERSION, 'projection': 'scenario-outcomes'}
        model['relationships'][0]['target'] = 'changed'
        self.assertTrue(binding_issues(model, analysis))

    def test_projection_metadata_rejects_downgrade_and_unknown_fields(self):
        for binding in [{'version': VERSION, 'projection': 'independent'},
                        {'version': VERSION, 'projection': 'full', 'json_path': '$.anything'}]:
            model, analysis = self.example('domain-architecture-alignment-default')
            analysis['inputs']['model_binding'] = binding
            self.assertTrue(binding_issues(model, analysis))

    def test_duplicate_id_and_wrong_type_return_structured_errors(self):
        model, analysis = self.example('architecture-role-catalog-default')
        analysis['inputs']['roles'].append(copy.deepcopy(analysis['inputs']['roles'][0]))
        self.assertIn('analysis-binding-identity', {f['code'] for f in binding_issues(model, analysis)})
        model, analysis = self.example('architecture-role-catalog-default')
        model['entities'][0]['type'] = 'requirement'
        self.assertIn('analysis-model-type', {f['code'] for f in binding_issues(model, analysis)})

    def test_binding_and_direct_evidence_do_not_mutate(self):
        model, analysis = self.example('scenario-transformation-audit')
        before = copy.deepcopy(model)
        require_binding(model, analysis)
        require_evidence(analysis)
        self.assertEqual(before, model)

    def test_standalone_snapshot_calculator_remains_usable(self):
        from analyze import evaluate
        _, analysis = self.example('domain-architecture-alignment-default')
        self.assertIn('result', evaluate(analysis))

    def test_legacy_governance_without_opt_in_is_compatible(self):
        analysis = {'id': 'gov', 'method_id': 'change-profile-checklist',
                    'inputs': {'change_profile': 'rapid', 'transition_id': 'external-transition',
                               'rule_evidence': ['S']}}
        self.assertEqual([], binding_issues({'sources': [{'id': 'S'}]}, analysis))


class EvidenceTests(unittest.TestCase):
    def risk(self):
        return {'id': 'risk', 'method_id': 'risk-explicit-rule', 'inputs': {
            'formula': 'likelihood-times-impact', 'rule_evidence': ['S'],
            'likelihood': {'scale': 'project', 'value': 2, 'evidence': ['S']},
            'impact': {'scale': 'project', 'value': 3, 'evidence': ['S']}}}

    def test_unregistered_source_rejected_even_without_source_ids(self):
        analysis = self.risk()
        self.assertEqual([], evidence_issues(analysis, {'sources': [{'id': 'S'}]}))
        analysis['inputs']['likelihood']['evidence'] = ['unregistered-source']
        findings = evidence_issues(analysis, {'sources': [{'id': 'S'}]})
        self.assertEqual('analysis-source-inventory', findings[0]['code'])
        self.assertEqual('inputs.likelihood.evidence[0]', findings[0]['path'])

    def test_shape_rejections_are_value_errors_not_type_errors(self):
        for bad in ['S', {'id': 'S'}, 0, True, None, [None], [{}], [[]], ['']]:
            with self.subTest(value=bad):
                analysis = self.risk(); analysis['inputs']['rule_evidence'] = bad
                with self.assertRaises(ValueError):
                    require_evidence(analysis)

    def test_score_evidence_map_is_checked(self):
        analysis = {'id': 'priority', 'method_id': 'work-package-prioritization',
                    'inputs': {'work_packages': [{'score_evidence': {'cost': ['unknown']}}]}}
        findings = evidence_issues(analysis, {'sources': [{'id': 'S'}]})
        self.assertIn('inputs.work_packages[0].score_evidence.cost[0]', [f['path'] for f in findings])
        analysis['inputs']['work_packages'][0]['score_evidence'] = {'cost': {'id': 'S'}}
        self.assertIn('analysis-evidence-shape', {f['code'] for f in evidence_issues(analysis)})

    def test_all_declared_evidence_paths_are_checked(self):
        from analysis_evidence import REFERENCE_PATHS
        self.assertEqual(31, len(REFERENCE_PATHS))
        count = 0
        for method, paths in REFERENCE_PATHS.items():
            for path in paths:
                value = ['unknown']
                for token in reversed(path):
                    value = [value] if token == '[]' else {'record': value} if token == '{}' else {token: value}
                analysis = {'id': 'a', 'method_id': method, 'inputs': value}
                with self.subTest(method=method, path=path):
                    self.assertIn('analysis-source-inventory', {f['code'] for f in evidence_issues(analysis, {'sources': []})})
                count += 1
        self.assertGreater(count, 100)

    def test_free_prose_is_not_interpreted_as_source_references(self):
        analysis = self.risk()
        analysis['inputs']['notes'] = {'review_evidence': 'Narrative describing further review',
                                     'source_refs': ['external-library-title'], 'evidence': {'summary': 'prose'}}
        self.assertEqual([], evidence_issues(analysis, {'sources': [{'id': 'S'}]}))

    def test_declared_inventory_is_checked_in_standalone_mode(self):
        analysis = self.risk(); analysis['inputs']['source_ids'] = ['OTHER']
        self.assertIn('analysis-source-declaration', {f['code'] for f in evidence_issues(analysis)})

    def test_business_references_are_not_sources(self):
        analysis = self.risk()
        analysis['inputs'].update(approved_plan_ref='PLAN-7', architecture_ref='VIEW-8', business_goal_ref='GOAL-9')
        self.assertEqual([], evidence_issues(analysis, {'sources': [{'id': 'S'}]}))

    def test_empty_evidence_is_left_to_method_gap_semantics(self):
        analysis = self.risk(); analysis['inputs']['likelihood']['evidence'] = []
        self.assertEqual([], evidence_issues(analysis))

    def test_unknown_inventory_and_duplicate_inventory_are_reported(self):
        analysis = self.risk(); analysis['inputs']['source_ids'] = ['S', 'S', 'UNKNOWN']
        codes = {f['code'] for f in evidence_issues(analysis, {'sources': [{'id': 'S'}]})}
        self.assertTrue({'analysis-source-inventory', 'analysis-evidence-shape'} <= codes)

    def test_special_source_paths_and_top_level_evidence(self):
        cases = [
            ('business-attribute-evaluation', {'business_case_ref': 'unknown'}),
            ('scenario-traceability-review', {'raw_record_ids': ['unknown']}),
            ('scenario-traceability-review', {'normalized_records': [{'from': 'unknown'}]}),
            ('metadata-application-coverage-review', {'evidence_records': [{'id': 'unknown'}]}),
        ]
        for method, inputs in cases:
            analysis = {'id': 'a', 'method_id': method, 'inputs': inputs}
            self.assertTrue(evidence_issues(analysis, {'sources': []}))
        analysis = self.risk(); analysis['evidence'] = ['unknown']
        self.assertTrue(evidence_issues(analysis, {'sources': [{'id': 'S'}]}))


if __name__ == '__main__':
    unittest.main()
