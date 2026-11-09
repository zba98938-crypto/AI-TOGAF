"""Composing cases may rename identities, never units, classifications or prose."""
import unittest
from core_cases import namespace_model, normalize_example, load
from analysis_binding import binding_issues
from proficiency_semantics import OFFICIAL_SCALE
from validate import validate


class CoreFixtureContractsTest(unittest.TestCase):
    def test_nested_target_literals_are_not_identity_fields(self):
        model = {'entities': [{'id': 'kg', 'type': 'measure'}, {'id': 'domain', 'type': 'goal'}],
                 'analyses': [{'id': 'analysis', 'method_id': 'smart-objective-review', 'inputs': {
                     'target': {'unit': 'kg', 'description': 'domain', 'object_id': 'domain'}}}]}
        target = namespace_model(model, 'case-')['analyses'][0]['inputs']['target']
        self.assertEqual({'unit': 'kg', 'description': 'domain', 'object_id': 'case-domain'}, target)

    def test_all_embedded_profiles_preserve_binding_after_composition(self):
        count = 0
        for profile in load()[2].values():
            if not profile.get('example', {}).get('analyses'):
                continue
            model = namespace_model(normalize_example(profile), 'case-')
            for analysis in model['analyses']:
                with self.subTest(profile=profile['id']):
                    self.assertEqual([], binding_issues(model, analysis))
                count += 1
        self.assertGreater(count, 0)

    def test_official_proficiency_identity_remains_official_after_composition(self):
        model = namespace_model(normalize_example(load()[2]['architecture-skill-matrix-default']), 'case-')
        self.assertEqual([OFFICIAL_SCALE], [scale['id'] for scale in model['scales']])
        reference = next(edge for edge in model['relationships']
                         if edge.get('attributes', {}).get('assessment_kind') == 'source_reference_target')
        self.assertEqual(OFFICIAL_SCALE, reference['attributes']['scale_id'])
        self.assertEqual([], [issue for issue in validate(model) if issue['level'] == 'error'])


if __name__ == '__main__':
    unittest.main()
