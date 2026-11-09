"""A successful G249 CLI cannot conceal invented personnel acceptance."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from analyze import evaluate
from profile_examples import normalize_example
from method_fixtures import embedded_oracle


class MethodFixtureOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        profiles = json.loads((SHARED / 'capabilities.json').read_text())['profiles']
        profile = next(row for row in profiles if row['id'] == 'architecture-work-assignment-review')
        model = normalize_example(profile)
        analysis = next(row for row in model['analyses']
                        if row['method_id'] == 'architecture-role-skill-assessment')
        cls.result = evaluate(analysis, model)['result']

    def accepts(self, result):
        return embedded_oracle('architecture-role-skill-assessment', result)

    def test_current_bound_example_preserves_unknowns(self):
        self.assertTrue(self.accepts(self.result))

    def test_invented_personnel_acceptance_is_rejected(self):
        for field, value in [('state', 'ready-for-owner-review'), ('approval', 'approved'),
                             ('capacity_state', 'sufficient-for-declared-workload'),
                             ('period_state', 'covered')]:
            result = copy.deepcopy(self.result)
            result['assignment_reviews'][0][field] = value
            with self.subTest(field=field):
                self.assertFalse(self.accepts(result))

    def test_expert_support_cannot_become_personal_evidence_or_promotion(self):
        result = copy.deepcopy(self.result)
        result['assignment_reviews'][0]['requirements'][0]['state'] = 'evidenced-for-declared-task'
        self.assertFalse(self.accepts(result))
        result = copy.deepcopy(self.result)
        result['development_reviews'][0]['rating_change'] = 3
        self.assertFalse(self.accepts(result))


if __name__ == '__main__':
    unittest.main()
