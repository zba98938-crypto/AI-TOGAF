"""Evidence semantics on the effective G249 generator profiles, not just prose."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from generate import generate
from matrix_semantics import cell_label
from profile_examples import normalize_example
from registry import load
from validate import validate


def model(profile='ea-skill-role-proficiency'):
    return normalize_example(load()[2][profile])


def observed(value):
    return next(r for r in value['relationships'] if r['attributes']['assessment_kind'] == 'observed_assessment')


def codes(value, level=None):
    return {i['code'] for i in validate(value) if level is None or i['level'] == level}


class ProficiencyContractTest(unittest.TestCase):
    def test_registered_examples_validate(self):
        for pid in ['ea-skill-role-proficiency', 'architecture-skill-matrix-default',
                    'architecture-development-plan-default', 'architecture-role-collaboration',
                    'architecture-work-assignment-review']:
            with self.subTest(profile=pid):
                self.assertEqual([], validate(model(pid)))

    def test_invalid_values_are_errors_at_actual_generation_entry(self):
        for value in [99, 0, 5, -1, 2.5, True, '3']:
            with self.subTest(value=value):
                m = model()
                observed(m)['attributes']['proficiency'] = value
                self.assertIn('proficiency-value', codes(m, 'error'))
        m = model()
        observed(m)['attributes']['proficiency'] = 99
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, 'proficiency-value'):
                generate(m, Path(directory), all_items=True)

    def test_legacy_missing_value_has_gap_and_no_implied_minimum(self):
        m = model()
        edge = observed(m)
        edge['attributes'] = {}
        self.assertNotIn('proficiency-value', codes(m, 'error'))
        self.assertIn('proficiency-value-gap', codes(m, 'warning'))
        self.assertIn('proficiency-context-gap', codes(m, 'warning'))
        self.assertIn('待补/未评级', cell_label(edge, '行→列'))

    def test_unknown_is_not_a_low_grade(self):
        m = model()
        edge = observed(m)
        edge['attributes'].update(assessment_state='evidence_insufficient', proficiency=None)
        self.assertNotIn('proficiency-value-gap', codes(m))
        self.assertEqual(set(), codes(m, 'error'))
        edge['attributes']['proficiency'] = 1
        self.assertIn('unassessed-proficiency', codes(m, 'error'))

    def test_source_target_cannot_be_silently_tailored(self):
        m = model()
        edge = next(r for r in m['relationships'] if r['attributes']['assessment_kind'] == 'source_reference_target')
        edge['attributes']['proficiency'] = 4
        self.assertIn('source-proficiency-mismatch', codes(m, 'error'))

    def test_chief_and_generic_segment_have_no_official_matrix_column(self):
        for role in ['chief-architect', 'segment-architect']:
            with self.subTest(role=role):
                m = model()
                m['relationships'][0]['attributes']['reference_role_id'] = 'G249:role:' + role
                self.assertIn('source-role-column', codes(m, 'error'))

    def test_original_target_local_target_and_personal_observation_are_not_duplicates(self):
        m = model()
        self.assertNotIn('duplicate-edge', codes(m))
        copy_edge = copy.deepcopy(observed(m))
        copy_edge['id'] += '-duplicate'
        m['relationships'].append(copy_edge)
        self.assertIn('duplicate-edge', codes(m))

    def test_matrix_display_uses_fields_not_stale_label(self):
        m = model()
        edge = observed(m)
        edge['label'] = '误导的目标熟练度4'
        text = cell_label(edge, '行→列')
        self.assertIn('人员观察 2', text)
        self.assertNotIn('目标熟练度4', text)
        self.assertIn('G249-table5-1', text)

    def test_custom_scales_must_be_explicit_and_official_anchors_immutable(self):
        m = model()
        observed(m)['attributes']['scale_id'] = 'project-observed-v1'
        self.assertIn('proficiency-scale-gap', codes(m, 'warning'))
        m['scales'].append({'id': 'project-observed-v1', 'name': '明确的项目锚点',
                            'anchors': [{'value': 2, 'meaning': '在指导下应用'}], 'evidence': ['example-source']})
        self.assertNotIn('proficiency-scale-gap', codes(m))
        m['scales'][0]['anchors'][2]['meaning'] = '完全不需要专家'
        self.assertIn('source-scale-redefinition', codes(m, 'error'))

    def test_absence_of_higher_evidence_does_not_prove_lower_grade(self):
        m = model()
        evidence = observed(m)['attributes']['behavioral_evidence'][0]
        evidence.update(criterion='不能证明三级行为', demonstrated=False)
        self.assertIn('proficiency-positive-evidence-gap', codes(m, 'warning'))

    def test_reference_document_is_not_observed_personnel_evidence(self):
        m = model()
        edge = observed(m)
        edge['evidence'] = ['g249-table-source']
        edge['attributes']['behavioral_evidence'][0]['evidence'] = ['g249-table-source']
        self.assertIn('proficiency-observation-source', codes(m, 'error'))

    def test_collaboration_and_matrix_can_reuse_the_same_role(self):
        m = model()
        role = next(e for e in m['entities'] if e['type'] == 'architecture_role')
        role['type'] = 'guide:architecture-role'
        role['attributes'].update(tier='enterprise', scope='同一任务范围', primary_responsibility='跨域决策')
        self.assertEqual([], validate(m))

    def test_kind_state_and_scale_shape_fail_cleanly(self):
        for field, value in [('assessment_kind', []), ('assessment_state', {}), ('scale_id', {'value': 2})]:
            m = model()
            observed(m)['attributes'][field] = value
            self.assertTrue(codes(m, 'error'))

    def test_development_needs_task_evidence_and_reassessment(self):
        m = model('architecture-development-plan-default')
        attrs = m['entities'][0]['attributes']
        for field in ['skill_id', 'task_refs', 'requirement_refs', 'behavioral_gap', 'success_criteria', 'history']:
            attrs.pop(field)
        self.assertIn('development-contract-gap', codes(m, 'warning'))
        attrs['reassessment']['status'] = 'completed'
        self.assertIn('development-reassessment-unproven', codes(m, 'error'))

    def test_development_explicit_unknown_is_valid_and_not_missing(self):
        for state in ['unassessed', 'evidence_insufficient']:
            m = model('architecture-development-plan-default')
            attrs = m['entities'][0]['attributes']
            attrs.update(current_proficiency=None, current_assessment_state=state, history=[])
            self.assertEqual([], validate(m))
            attrs['current_proficiency'] = 1
            self.assertIn('unassessed-proficiency', codes(m, 'error'))

    def test_development_missing_current_stays_a_gap(self):
        m = model('architecture-development-plan-default')
        attrs = m['entities'][0]['attributes']
        attrs.update(current_assessment_state='evidence_insufficient')
        attrs.pop('current_proficiency')
        self.assertIn('development-current-proficiency-gap', codes(m, 'warning'))
        self.assertIn('profile-attribute-gap', codes(m, 'warning'))
        attrs['current_proficiency'] = None
        attrs.pop('current_assessment_state')
        self.assertIn('development-current-proficiency-gap', codes(m, 'warning'))

    def test_generation_accepts_deliberate_unknown_current(self):
        m = model('architecture-development-plan-default')
        m['entities'][0]['attributes'].update(current_proficiency=None, current_assessment_state='evidence_insufficient', history=[])
        with tempfile.TemporaryDirectory() as directory:
            generate(m, Path(directory), all_items=True, strict=True)
            self.assertTrue((Path(directory) / 'artifacts/v-architecture-development-plan-default.svg').is_file())

    def test_generators_keep_effective_contracts(self):
        from build_capabilities import build_work_products, build_profiles, build_methods
        products = build_work_products()
        profiles = {p['id']: p for p in build_profiles(products)}
        self.assertIn('architecture-role-collaboration', profiles)
        self.assertIn('architecture-work-assignment-review', profiles)
        for pid in ['ea-skill-role-proficiency', 'architecture-development-plan-default']:
            actual = load()[2][pid]
            registered, rebuilt = copy.deepcopy(actual['example']), copy.deepcopy(profiles[pid]['example'])
            # Portable source binding changes only the locator, never the
            # behavioral example. Verify both allowed identities explicitly.
            allowed = {'https://pubs.opengroup.org/togaf-standard/architecture-roles-and-skills/Architecture-Roles-and-Skills.html#chap05',
                       'corpus/sources/pdf/G249e.pdf#page=27'}
            for example in (registered, rebuilt):
                source=next(s for s in example['sources'] if s['id']=='g249-table-source')
                self.assertIn(source.pop('locator'),allowed)
            shared=ROOT/'togaf-standard-10th-ai/skills/_shared'
            source_map=json.loads((shared/'corpus/source-map.json').read_text())
            self.assertIn('sources/pdf/G249e.pdf',source_map['logical_paths'].values())
            self.assertTrue((shared/'corpus/sources/pdf/G249e.pdf').is_file())
            self.assertEqual(registered, rebuilt)
            self.assertEqual(actual['required_attributes'], profiles[pid]['required_attributes'])
        method = next(m for m in build_methods() if m['id'] == 'architecture-role-skill-assessment')
        self.assertEqual('architecture-role-skill-assessment', method['execution_method'])
        self.assertEqual('architecture-role-skill-assessment', method['calculator_id'])
        self.assertIn('不计算人员合格分', method['calculation_policy'])


if __name__ == '__main__':
    unittest.main()
