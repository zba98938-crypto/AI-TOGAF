"""G249 behavioral regressions: evidence, scope, hierarchy and stale model binding."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from analyze import evaluate
from g249_reasoning import review_role_skills, skill_routes
from g249_skill_routes import build as build_routes
from gap_closure_analysis import architecture_role_catalog_review
from gap_closure_examples import roles as role_example


def complete_case():
    data = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json').read_text())
    data['tasks'] = [data['tasks'][-1]]
    data['tasks'][0]['required_skill_ids'].pop()
    data['tasks'][0]['workload_hours'] = 32
    # Explicit synthetic coverage for the newer task-period evidence contract.
    data['tasks'][0]['work_period'] = {'start': '2026-11-07', 'end': '2026-11-30'}
    data['requirements'] = [data['requirements'][-1]]
    data['assessments'] = [data['assessments'][0]]
    data['assessments'][0].update(assessment_state='assessed', proficiency=3, assessor='Independent reviewer')
    data['assessments'][0]['behavioral_evidence'][0]['demonstrated'] = True
    data['assignments'][0].pop('support')
    data['development'] = []
    return data


def analysis(data):
    return {'id': 'ASSESS-1', 'method_id': 'architecture-role-skill-assessment', 'inputs': data}


def bound_case():
    data = complete_case()
    obj = {'id': 'IF-RESERVE', 'type': 'interface', 'name': 'Reservation contract',
           'attributes': {'version': '1'}, 'evidence': ['CASE-REVIEW']}
    data['tasks'][0]['model_object_refs'] = [obj['id']]
    data['model_objects'] = [copy.deepcopy(obj)]
    selected_view = {'id': 'INTERFACE-VIEW', 'artifact_id': 'application-communication-diagram',
                     'entity_ids': ['IF-RESERVE'], 'relationship_ids': []}
    data['model_views'] = [copy.deepcopy(selected_view)]
    data['model_binding'] = {'version': 'g249-assessment-binding/1', 'context_ref': 'ASSESS-CONTEXT'}
    context = {'id': 'ASSESS-CONTEXT', 'type': 'guide:g249-assessment-context', 'name': 'Task competence context',
               'attributes': {'assessment_inputs': copy.deepcopy(data)}}
    model = {'entities': [obj, context], 'relationships': [], 'views': [selected_view],
             'sources': [{'id': sid} for sid in data['source_ids']]}
    return model, analysis(data)


class G249ReasoningTests(unittest.TestCase):
    def test_all_71_routes_reproduce_source_and_use_registered_ids(self):
        built = build_routes()
        self.assertEqual(built, skill_routes())
        self.assertEqual(71, len(built['skills']))
        self.assertEqual(71, len({r['skill_id'] for r in built['skills']}))
        unresolved = [r for r in built['skills'] if r['definition_status'] == 'source-name-unresolved']
        self.assertEqual(['Optimistic/ Pessimistic Patterns'], [r['source_name_en'] for r in unresolved])
        for row in built['skills']:
            self.assertEqual(6, len(row['official']['reference_proficiencies']))
            self.assertTrue(row['official']['evidence']['source_sha256'])
            self.assertIn('project-derived', row['mapping_origin'])

    def test_complete_evidence_allows_owner_review_never_approval(self):
        result = evaluate(analysis(complete_case()))['result']
        self.assertEqual([], result['gaps'])
        row = result['assignment_reviews'][0]
        self.assertEqual('ready-for-owner-review', row['state'])
        self.assertEqual('not-granted', row['approval'])

    def test_missing_level_three_evidence_stays_unknown_not_level_two(self):
        data = complete_case()
        data['assessments'][0].update(assessment_state='evidence_insufficient', proficiency=None)
        result = review_role_skills(data)
        self.assertEqual('unproven', result['assignment_reviews'][0]['requirements'][0]['state'])
        self.assertIsNone(data['assessments'][0]['proficiency'])
        self.assertNotIn('development-needed', result['assignment_reviews'][0]['state'])

    def test_missing_behavior_prevents_meeting_target_even_with_same_rating(self):
        data = complete_case()
        data['assessments'][0]['behavioral_evidence'][0]['demonstrated'] = False
        row = review_role_skills(data)['assignment_reviews'][0]
        self.assertEqual('development-needed', row['state'])
        self.assertTrue(row['requirements'][0]['missing_behavioral_criteria'])

    def test_capacity_unknown_and_shortage_do_not_lower_competence(self):
        for workload, expected in [(None, 'unresolved'), (80, 'insufficient')]:
            data = complete_case()
            data['tasks'][0]['workload_hours'] = workload
            row = review_role_skills(data)['assignment_reviews'][0]
            self.assertEqual(expected, row['capacity_state'])
            self.assertEqual('evidenced-for-declared-task', row['requirements'][0]['state'])
            self.assertEqual(3, data['assessments'][0]['proficiency'])

    def test_source_target_is_never_observed_personal_proficiency(self):
        data = complete_case()
        data['assessments'][0]['assessment_kind'] = 'source_reference_target'
        with self.assertRaisesRegex(ValueError, 'G249-KIND'):
            review_role_skills(data)

    def test_reference_cell_value_must_match_official_matrix(self):
        data = complete_case()
        req = data['requirements'][0]
        req.update(assessment_kind='source_reference_target', assessment_state='reference', proficiency=1,
                   reference_role_ref='G249:role:solution-architect')
        with self.assertRaisesRegex(ValueError, 'G249-SOURCE-TARGET'):
            review_role_skills(data)

    def test_invalid_ordinal_is_rejected_not_coerced(self):
        for value in (99, 0, 2.5, True, '3'):
            data = complete_case()
            data['assessments'][0]['proficiency'] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'G249-LEVEL'):
                review_role_skills(data)

    def test_different_scales_require_reassessment(self):
        data = complete_case()
        data['scales'] = [{'id': 'project-independent-v1', 'anchors': [{'value': i, 'meaning': str(i)} for i in range(1, 5)], 'evidence': ['CASE-REVIEW']}]
        data['assessments'][0]['scale_id'] = 'project-independent-v1'
        result = review_role_skills(data)
        self.assertIn('incomparable-scales', {g['reason'] for g in result['gaps']})
        self.assertEqual('unproven', result['assignment_reviews'][0]['requirements'][0]['state'])

    def test_upstream_mandate_or_task_gap_prevents_ready_state(self):
        for location in ('mandate', 'task'):
            data = complete_case()
            (data['mandate'] if location == 'mandate' else data['tasks'][0])['evidence'] = []
            self.assertEqual('needs-evidence', review_role_skills(data)['assignment_reviews'][0]['state'])

    def test_omitted_requirement_cannot_make_assignment_look_complete(self):
        data = complete_case()
        extra = copy.deepcopy(data['requirements'][0])
        extra['id'] = 'REQ-OMITTED'
        data['requirements'].append(extra)
        result = review_role_skills(data)
        self.assertIn('assignment-requirement-omitted', {g['reason'] for g in result['gaps']})
        self.assertEqual('needs-evidence', result['assignment_reviews'][0]['state'])

    def test_unknown_evidence_and_wrong_person_block_execution(self):
        data = complete_case()
        data['assessments'][0]['behavioral_evidence'][0]['evidence'] = ['NONEXISTENT']
        with self.assertRaises(ValueError):
            evaluate(analysis(data))
        data = complete_case()
        data['assessments'][0]['person_ref'] = 'SOMEONE-ELSE'
        with self.assertRaisesRegex(ValueError, 'G249-ASSIGNMENT'):
            review_role_skills(data)

    def test_training_completion_cannot_close_development_without_reassessment(self):
        data = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json').read_text())
        data['development'][0]['reassessment'].update(status='completed', evidence=['CASE-PERSON'])
        result = review_role_skills(data)
        self.assertIn('missing-reassessment', {g['reason'] for g in result['gaps']})
        self.assertEqual('needs-input', result['development_reviews'][0]['state'])
        self.assertEqual('not-inferred', result['development_reviews'][0]['rating_change'])

    def test_requirement_behavior_change_invalidates_old_development_plan(self):
        data = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json').read_text())
        target = next(r for r in data['requirements'] if r['id'] == 'REQ-SKILL-SOL')
        original = copy.deepcopy(data['development'][0])
        target['behavioral_criteria'].append('评审断连、重连、幂等重放和库存冲突的恢复设计')
        result = review_role_skills(data)
        self.assertIn('development-criteria-outdated', {g['reason'] for g in result['gaps']})
        self.assertEqual('needs-input', result['development_reviews'][0]['state'])
        self.assertEqual(original, data['development'][0])
        gap_ids = {g['id'] for g in result['gaps'] if g['reason'] == 'development-criteria-outdated'}
        self.assertEqual({'DEV-A:REQ-SKILL-SOL:success_criteria', 'DEV-A:REQ-SKILL-SOL:reassessment.criteria'}, gap_ids)

    def test_success_and_reassessment_each_require_exact_current_criterion(self):
        for field in ('success_criteria', 'reassessment.criteria'):
            data = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json').read_text())
            plan = data['development'][0]
            if field == 'success_criteria':
                plan['success_criteria'] = ['意思相近但未明确映射的改写文字']
            else:
                plan['reassessment']['criteria'] = ['意思相近但未明确映射的改写文字']
            result = review_role_skills(data)
            gaps = {g['id'] for g in result['gaps'] if g['reason'] == 'development-criteria-outdated'}
            self.assertEqual({'DEV-A:REQ-SKILL-SOL:' + field}, gaps)

    def test_requirement_version_change_invalidates_old_plan_without_rewriting(self):
        data = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json').read_text())
        next(r for r in data['requirements'] if r['id'] == 'REQ-SKILL-SOL')['version'] = 'REQ-SKILL-SOL-v2'
        data['development'][0]['requirement_versions'] = {'REQ-SKILL-SOL': 'REQ-SKILL-SOL-v1'}
        result = review_role_skills(data)
        self.assertIn('development-requirement-version-unconfirmed', {g['reason'] for g in result['gaps']})
        self.assertEqual('REQ-SKILL-SOL-v1', data['development'][0]['requirement_versions']['REQ-SKILL-SOL'])

    def test_selected_artifact_view_is_required_when_context_binding_is_used(self):
        data = complete_case()
        data['model_binding'] = {'version': 'g249-assessment-binding/1', 'context_ref': 'C'}
        data['tasks'][0]['artifact_ids'] = ['application-communication-diagram']
        result = review_role_skills(data)
        self.assertIn('artifact-view-selection-unverified', {g['reason'] for g in result['gaps']})
        data['model_views'] = [{'id': 'V-APP', 'artifact_id': 'application-communication-diagram'}]
        result = review_role_skills(data)
        self.assertNotIn('artifact-view-selection-unverified', {g['reason'] for g in result['gaps']})
        data['model_views'] = []
        self.assertIn('task-artifact-view-missing', {g['reason'] for g in review_role_skills(data)['gaps']})

    def test_current_task_view_addition_deletion_or_change_requires_resync(self):
        model, item = bound_case()
        evaluate(item, model)
        for change in ('add', 'delete', 'change'):
            edited = copy.deepcopy(model)
            if change == 'add':
                edited['views'].append({**edited['views'][0], 'id': 'ANOTHER-INTERFACE-VIEW'})
            elif change == 'delete':
                edited['views'] = []
            else:
                edited['views'][0]['entity_ids'] = []
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, 'g249-analysis-binding'):
                evaluate(item, edited)

    def test_expert_support_does_not_upgrade_person_or_prove_capacity(self):
        data = json.loads((ROOT / 'togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json').read_text())
        row = review_role_skills(data)['assignment_reviews'][0]
        self.assertEqual('expert-evidence-recorded', row['support_reviews'][0]['state'])
        self.assertEqual('unproven', row['requirements'][0]['state'])
        self.assertEqual('unresolved', row['capacity_state'])

    def test_model_context_and_domain_object_mutations_block_public_evaluate(self):
        model, item = bound_case()
        self.assertEqual('ready-for-owner-review', evaluate(item, model)['result']['assignment_reviews'][0]['state'])
        for mutate in ('context', 'domain', 'input'):
            current_model, current_item = copy.deepcopy(model), copy.deepcopy(item)
            if mutate == 'context':
                current_model['entities'][1]['attributes']['assessment_inputs']['scope'] = 'changed'
            elif mutate == 'domain':
                current_model['entities'][0]['attributes']['version'] = '2'
            else:
                current_item['inputs']['tasks'][0]['decision'] = 'changed'
            with self.subTest(mutate=mutate), self.assertRaisesRegex(ValueError, 'g249-analysis-binding'):
                evaluate(current_item, current_model)

    def test_scoped_relationship_change_addition_and_deletion_invalidate_analysis(self):
        model, item = bound_case()
        obj = {'id': 'APP-STOCK', 'type': 'application', 'name': 'Stock service', 'attributes': {}, 'evidence': ['CASE-REVIEW']}
        model['entities'].insert(0, obj)
        item['inputs']['model_objects'].append(copy.deepcopy(obj))
        item['inputs']['tasks'][0]['model_object_refs'].append(obj['id'])
        edge = {'id': 'EXPOSES-1', 'type': 'exposes', 'source': 'APP-STOCK', 'target': 'IF-RESERVE', 'attributes': {}, 'evidence': ['CASE-REVIEW']}
        model['relationships'] = [edge]
        item['inputs']['model_relationships'] = [copy.deepcopy(edge)]
        model['entities'][-1]['attributes']['assessment_inputs'] = copy.deepcopy(item['inputs'])
        evaluate(item, model)
        for change in ('change', 'add', 'delete'):
            edited = copy.deepcopy(model)
            if change == 'change':
                edited['relationships'][0]['attributes']['contract_version'] = '2'
            elif change == 'add':
                edited['relationships'].append({**edge, 'id': 'EXPOSES-2'})
            else:
                edited['relationships'] = []
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, 'g249-analysis-binding'):
                evaluate(item, edited)


class RoleRelationshipTests(unittest.TestCase):
    def example(self):
        _, entities, builder = role_example()
        data = builder(entities)
        for role in data['roles']:
            role['leads'] = []
        return data

    def test_legacy_reverse_lead_is_untyped_gap_not_universal_hierarchy_error(self):
        data = self.example()
        data['roles'][-1]['leads'] = ['ROLE-EA']
        self.assertIn('untyped-legacy-lead', {g['reason'] for g in architecture_role_catalog_review(data)['gaps']})

    def test_lateral_guidance_allowed_and_explicit_strict_policy_enforced(self):
        data = self.example()
        data['roles'][-1]['relationships'] = [{'id': 'REL-1', 'type': 'architecture_guidance', 'target': 'ROLE-EA', 'scope': '专项接口验证', 'evidence': ['ROLE-R1']}]
        self.assertEqual(1, len(architecture_role_catalog_review(data)['relationships']))
        data['hierarchy_policy'] = {'mode': 'strict-tier', 'origin': 'project-adopted', 'evidence': ['ROLE-R1'],
                                    'applies_to': ['architecture_guidance'], 'tier_order': ['chief', 'enterprise', 'segment', 'solution', 'specialist']}
        with self.assertRaisesRegex(ValueError, 'ROLE-POLICY'):
            architecture_role_catalog_review(data)

    def test_collaboration_is_not_constrained_by_tier_policy(self):
        data = self.example()
        data['roles'][-1]['relationships'] = [{'id': 'REL-1', 'type': 'collaborates_with', 'target': 'ROLE-EA', 'scope': '共同评审', 'evidence': ['ROLE-R1']}]
        data['hierarchy_policy'] = {'mode': 'strict-tier', 'origin': 'project-adopted', 'evidence': ['ROLE-R1'],
                                    'applies_to': ['architecture_guidance'], 'tier_order': ['chief', 'enterprise', 'segment', 'solution', 'specialist']}
        self.assertEqual(1, len(architecture_role_catalog_review(data)['relationships']))

    def test_reporting_cycle_rejected_handoff_missing_acceptance_is_gap(self):
        data = self.example()
        for index, target in [(0, 'ROLE-EA'), (1, 'ROLE-CHIEF')]:
            data['roles'][index]['relationships'] = [{'id': 'REL-' + str(index), 'type': 'reports_to', 'target': target, 'scope': '组织', 'evidence': ['ROLE-R1']}]
        with self.assertRaisesRegex(ValueError, 'ROLE-REPORT-CYCLE'):
            architecture_role_catalog_review(data)
        data = self.example()
        data['roles'][0]['relationships'] = [{'id': 'HANDOFF-1', 'type': 'handoff', 'target': 'ROLE-EA', 'scope': '架构方案', 'evidence': ['ROLE-R1']}]
        self.assertIn('HANDOFF-1:acceptance_criteria', {g['id'] for g in architecture_role_catalog_review(data)['gaps']})

    def test_role_policy_and_collaboration_graph_are_bound_to_current_model(self):
        sources, entities, builder = role_example()
        for entity in entities:
            entity['attributes']['leads'] = []
        rel = {'id': 'REL-1', 'type': 'architecture_guidance', 'target': 'ROLE-SEG', 'scope': 'Order segment', 'evidence': ['ROLE-R1']}
        entities[1]['attributes']['relationships'] = [rel]
        data = builder(entities)
        data['hierarchy_policy'] = {'mode': 'strict-tier', 'origin': 'project-adopted', 'evidence': ['ROLE-R1'],
                                    'applies_to': ['architecture_guidance'], 'tier_order': ['chief', 'enterprise', 'segment', 'solution', 'specialist']}
        data['policy_context_ref'] = 'POLICY-CONTEXT'
        policy_entity = {'id': 'POLICY-CONTEXT', 'type': 'repository_asset', 'name': 'Adopted policy',
                         'attributes': {'role_review_context': {'hierarchy_policy': copy.deepcopy(data['hierarchy_policy'])}}}
        item = {'id': 'ROLE-REVIEW', 'method_id': 'architecture-role-catalog-review', 'inputs': data}
        model = {'sources': sources, 'entities': entities + [policy_entity],
                 'relationships': [{'id': 'REL-1', 'type': 'g249:architecture_guidance', 'source': 'ROLE-EA', 'target': 'ROLE-SEG',
                                    'attributes': {'scope': 'Order segment', 'semantic_type': 'architecture_guidance'}, 'evidence': ['ROLE-R1']}],
                 'views': [{'id': 'ROLE-VIEW', 'profile_id': 'architecture-role-collaboration', 'entity_ids': [e['id'] for e in entities],
                            'relationship_ids': ['REL-1'], 'attributes': {'analysis_ids': ['ROLE-REVIEW']}}]}
        evaluate(item, model)
        graph_changed = copy.deepcopy(model)
        graph_changed['relationships'][0]['attributes']['scope'] = 'Different scope'
        with self.assertRaisesRegex(ValueError, 'g249-role-binding'):
            evaluate(item, graph_changed)
        policy_changed = copy.deepcopy(item)
        policy_changed['inputs']['hierarchy_policy']['tier_order'][0:2] = ['enterprise', 'chief']
        with self.assertRaisesRegex(ValueError, 'g249-role-binding'):
            evaluate(policy_changed, model)


if __name__ == '__main__':
    unittest.main()
