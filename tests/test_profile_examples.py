"""Registered fragments must be production-ready, and builders preserve the fixes."""
import copy
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from profile_examples import normalize_example
from registry import load
from validate import validate


class ProfileExamplesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profiles = load()[2]

    def test_registered_repairs_are_production_ready(self):
        ids = ('application-gap-dependency', 'metadata-three-part-solution',
               'metadata-inference-structure', 'metadata-application-function-coverage',
               'architecture-landscape-projection', 'security-adm-concept-map',
               'soa-layered-reference')
        for pid in ids:
            with self.subTest(profile=pid):
                errors = [i for i in validate(normalize_example(self.profiles[pid])) if i['level'] == 'error']
                self.assertEqual([], errors)

    def test_application_builder_retains_detailed_topology(self):
        from capability_examples import specialize
        profile = self.profiles['application-gap-dependency']
        for _ in range(2):
            rebuilt = {'id': profile['id']}
            example = specialize(rebuilt, [], None)
            self.assertEqual(profile, rebuilt)
            self.assertTrue(example['view']['allow_mixed_evolution'])

    def test_specialized_builders_declare_used_relationships(self):
        from specialized_view_profiles import builders
        first = builders()
        self.assertEqual(first, builders())
        for profile in first:
            example = profile['example']
            used = {r['type'] for r in example['relationships'] if ':' in r['type']}
            self.assertLessEqual(used, set(example.get('extensions', {}).get('relationship_types', {})))

    def test_metadata_solution_builder_is_self_contained(self):
        from expand_metadata_views import solution_example
        example = solution_example()
        self.assertEqual(example, solution_example())
        self.assertIn('g234:supports-requirements', example['extensions']['relationship_types'])

    def test_metadata_coverage_builder_keeps_extensions(self):
        path = SHARED / 'capability-addenda/build_metadata_coverage.py'
        spec = importlib.util.spec_from_file_location('metadata_case_builder_test', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        outputs = {}
        def capture(path, value):
            outputs[path] = copy.deepcopy(value)
        with patch.object(module, 'save', capture), redirect_stdout(io.StringIO()):
            module.main()
            first = copy.deepcopy(outputs)
            module.main()
        self.assertEqual(first, outputs)
        package = outputs['capability-addenda/metadata-function-coverage-addenda.json']
        example = package['profiles'][0]['example']
        self.assertEqual(module.RELATIONS, example['extensions']['relationship_types'])

    def test_wrapper_preserves_explicit_evolution_and_does_not_repair(self):
        profile = copy.deepcopy(self.profiles['application-gap-dependency'])
        model = normalize_example(profile)
        self.assertEqual(profile['example']['entities'], model['entities'])
        del profile['example']['view']['allow_mixed_evolution']
        self.assertNotIn('allow_mixed_evolution', normalize_example(profile)['views'][0])

    def test_work_assignment_nested_scope_has_a_real_visible_change(self):
        from verify_artifact_profiles import verify_profile, visible_text
        profile = self.profiles['architecture-work-assignment-review']
        result, outputs = verify_profile(profile)
        self.assertEqual([], result['failures'])
        self.assertEqual(4, len(outputs))
        token = result['substantive_change']['expected_text']
        for identity, content, report in outputs:
            text = visible_text(content, profile) + report.get('companion_html', '')
            self.assertEqual(identity.endswith('-modified'), token in text)
        self.assertEqual('assessment_inputs.scope', result['substantive_change']['field'])

    def test_render_preparation_failure_keeps_a_nonpassing_summary(self):
        import verify_artifact_profiles as verifier
        for failure, status, code in ((ImportError('fontTools unavailable'), 'blocked', 3),
                                      (FileNotFoundError('node unavailable'), 'blocked', 3),
                                      (ValueError('invalid font'), 'failed', 1)):
            with self.subTest(status=status, failure=str(failure)), tempfile.TemporaryDirectory() as temporary:
                destination = Path(temporary) / 'evidence'
                argv = ['verify', '--profile', 'trust-framework-default', '--render', '--out', str(destination)]
                with patch.object(sys, 'argv', argv), patch.object(verifier, 'render_outputs', side_effect=failure), redirect_stdout(io.StringIO()):
                    self.assertEqual(code, verifier.main())
                report = json.loads((destination/'verification.json').read_text())
                self.assertEqual(status, report['status'])
                self.assertEqual(status, report['render_status'])
                self.assertEqual(str(failure), report['render_error'])


if __name__ == '__main__':
    unittest.main()
