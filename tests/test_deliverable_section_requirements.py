"""Required direct chapters need their own bindings in strict and draft assembly."""
import copy
import sys
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from deliverable_assembly import assemble, load_rules
from registry import load


class DirectSectionRequirementsTest(unittest.TestCase):
    def setUp(self):
        self.rules = load_rules()
        self.contract = load()[1]['implementation-governance-model']
        self.model = {'schema_version': '2.0', 'project': {'id': 'fictional', 'version': '1'},
                      'sources': [{'id': 'input', 'kind': 'user', 'description': 'Fictional candidate evidence'}],
                      'entities': [], 'relationships': [], 'views': [], 'analyses': [], 'gaps': []}
        self.delivery = {'id': 'delivery', 'deliverable_id': self.contract['id'], 'view_ids': [],
                         'entity_ids': [], 'sections': {},
                         'assembly': {'rules_version': '1.0', 'mode': 'strict', 'section_bindings': {}}}

    def test_empty_required_chapters_block_strict_and_keep_same_draft_gaps(self):
        strict = assemble(self.model, self.delivery, self.contract, self.rules)
        draft_delivery = copy.deepcopy(self.delivery)
        draft_delivery['assembly']['mode'] = 'draft'
        draft = assemble(self.model, draft_delivery, self.contract, self.rules)
        self.assertEqual('blocked', strict['status'])
        self.assertEqual('draft-with-gaps', draft['status'])
        self.assertEqual(strict['gaps'], draft['gaps'])
        self.assertEqual({section['title'] for section in self.contract['sections']},
                         {gap['object_id'] for gap in strict['gaps'] if gap['code'] == 'assembly-section-unbound'})

    def test_narrative_only_does_not_remove_required_section_gaps(self):
        self.delivery['sections'] = {section['title']: 'Fictional candidate narrative only.'
                                     for section in self.contract['sections']}
        result = assemble(self.model, self.delivery, self.contract, self.rules)
        self.assertEqual('blocked', result['status'])
        self.assertEqual(4, len(result['unbound_section_titles']))
        self.assertTrue(all(section['status'] == 'narrative-only-unverified'
                            for section in result['section_coverage']))

    def test_one_chapter_binding_cannot_fill_other_direct_entity_chapters(self):
        title = '治理角色与责任'
        self.model['entities'] = [{'id': 'owner', 'type': 'role', 'name': 'Fictional delivery owner',
                                   'attributes': {'responsibility': 'Retain evidence'}, 'evidence': ['input']}]
        self.delivery['assembly']['section_bindings'] = {title: {'entity_ids': ['owner']}}
        result = assemble(self.model, self.delivery, self.contract, self.rules)
        self.assertEqual('blocked', result['status'])
        self.assertEqual([title], [section['title'] for section in result['section_coverage']
                                  if section['status'] == 'bound-not-business-accepted'])
        self.assertEqual(3, len(result['unbound_section_titles']))


if __name__ == '__main__':
    unittest.main()
