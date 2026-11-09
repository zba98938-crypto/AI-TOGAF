"""Contract definitions must match model extension rules without scope leakage."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(ROOT / 'scripts'))
from contract_vocabulary import audit_contract, core_vocabulary
from planning_case_examples import base_model, entity
from validate import validate
from verify_skill_packages import check_vocabulary


def contract(name='probe', kind='probe:task'):
    return {'id': name, 'entity_types': [kind], 'relationship_types': [],
            'example': {'extensions': {'entity_types': {kind: 'A scoped test task'}}}}


def model(extensions, kind='probe:task'):
    value = base_model({'scenario': 'vocabulary-test'})
    value['extensions'] = copy.deepcopy(extensions)
    value['entities'] = [entity('PROBE', kind, 'Vocabulary probe', {})]
    return value


def error_codes(value):
    return {item['code'] for item in validate(value) if item['level'] == 'error'}


class ContractVocabularyTest(unittest.TestCase):
    def test_local_entity_and_relation_are_accepted_without_becoming_core(self):
        row = contract()
        row['relationship_types'] = ['probe:depends']
        ext = row['example']['extensions']
        ext['relationship_types'] = {'probe:depends': {
            'source_types': ['probe:task'], 'target_types': ['probe:task'], 'meaning': 'Needs target work'}}
        result = audit_contract(row, {})
        self.assertFalse(result['missing_entities'] or result['missing_relations'] or result['invalid_definitions'])
        self.assertEqual(set(), error_codes(model(ext)))
        entities, relations = core_vocabulary()
        self.assertNotIn('probe:task', entities)
        self.assertNotIn('probe:depends', relations)

    def test_other_profile_cannot_supply_missing_definition(self):
        first = contract('first')
        second = contract('second')
        second.pop('example')
        result = check_vocabulary({'work_products': [], 'profiles': [first, second]})
        self.assertEqual('fail', result['status'])
        self.assertEqual(['second'], [r['id'] for r in result['contract_problems']])
        self.assertEqual(['probe:task'], result['missing_entities'])

    def test_global_pool_is_available_but_model_must_embed_definition(self):
        row = contract()
        row.pop('example')
        caps = {'extension_entity_definitions': {'probe:task': 'Explicit reusable task definition'}}
        self.assertEqual([], audit_contract(row, caps)['missing_entities'])
        self.assertIn('undefined-entity-type', error_codes(model({})))
        self.assertEqual(set(), error_codes(model({'entity_types': caps['extension_entity_definitions']})))
        caps['extension_entity_definitions']['probe:task'] = ''
        result = audit_contract(row, caps)
        self.assertEqual(['probe:task'], result['missing_entities'])
        self.assertIn('schema', {p['code'] for p in result['invalid_definitions']})

    def test_core_override_and_bad_namespace_match_validator_rejections(self):
        for name, expected in [('activity', 'core-vocabulary-override'), ('unnamespaced', 'extension-namespace')]:
            with self.subTest(name=name):
                row = contract(kind=name)
                result = audit_contract(row, {})
                self.assertIn(expected, {p['code'] for p in result['invalid_definitions']})
                self.assertIn(expected, error_codes(model(row['example']['extensions'], name)))

    def test_missing_relation_endpoint_and_malformed_rule_fail(self):
        row = contract()
        row['relationship_types'] = ['probe:depends']
        ext = row['example']['extensions']
        rule = {'source_types': ['probe:task'], 'target_types': ['probe:absent'], 'meaning': 'Needs target'}
        ext['relationship_types'] = {'probe:depends': rule}
        result = audit_contract(row, {})
        self.assertEqual(['probe:depends'], result['missing_relations'])
        self.assertIn('dangling-reference', {p['code'] for p in result['invalid_definitions']})
        self.assertIn('dangling-reference', error_codes(model(ext)))
        del rule['meaning']
        self.assertIn('schema', {p['code'] for p in audit_contract(row, {})['invalid_definitions']})
        self.assertIn('schema', error_codes(model(ext)))

    def test_work_product_registry_types_are_core(self):
        from registry import load
        registered, _, _, _ = load()
        base = json.loads((ROOT / 'artifacts.json').read_text())['artifacts']
        meta = json.loads((ROOT / 'metamodel.json').read_text())
        base_types = {t for row in base for t in row.get('entity_types', [])} | set(meta['entity_types'])
        additions = {t for row in registered.values() for t in row.get('entity_types', [])} - base_types
        self.assertTrue(additions)
        for kind in sorted(additions):
            with self.subTest(kind=kind):
                self.assertIn(kind, core_vocabulary()[0])
                self.assertNotIn('undefined-entity-type', error_codes(model({}, kind)))

    def test_wildcard_fields_are_not_types_but_unknown_typed_fields_fail(self):
        row = {'id': 'fields', 'required_attributes': {'*': ['name'], 'probe:missing': ['owner']}}
        self.assertEqual(['probe:missing'], audit_contract(row, {})['missing_entities'])

    def test_legacy_case_aliases_are_explicit_local_definitions(self):
        caps = json.loads((ROOT / 'capabilities.json').read_text())
        row = next(r for r in caps['profiles'] if r['id'] == 'architecture-work-assignment-map')
        self.assertFalse(audit_contract(row, caps)['invalid_definitions'])
        for kind, meaning in row['extensions']['entity_types'].items():
            self.assertNotIn(kind, core_vocabulary()[0])
            self.assertEqual(set(), error_codes(model({'entity_types': {kind: meaning}}, kind)))

    def test_repository_contracts_pass_scoped_vocabulary_audit(self):
        self.assertEqual('pass', check_vocabulary()['status'])


if __name__ == '__main__':
    unittest.main()
