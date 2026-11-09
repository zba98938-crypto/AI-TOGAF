"""Implementation governance routes must preserve conditional F and G usage."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(ROOT/'scripts'))
from registry_consistency import apply_delivery_links,check,DELIVERY_LINKS


class GovernanceDeliveryRouteTest(unittest.TestCase):
    def test_route_is_required_even_if_other_work_product_links_same_delivery(self):
        caps=json.loads((ROOT/'capabilities.json').read_text())
        for identity in ('architecture-governance-checklist','decision-delegation-register'):
            changed=copy.deepcopy(caps)
            row=next(w for w in changed['work_products'] if w['id']==identity)
            row['related_deliverables'].remove('implementation-governance-model')
            self.assertIn(identity+': missing delivery route implementation-governance-model',check(changed))

    def test_targeted_sync_is_idempotent_and_preserves_profiles_and_figures(self):
        caps=json.loads((ROOT/'capabilities.json').read_text())
        untouched={k:copy.deepcopy(v) for k,v in caps.items() if k!='work_products'}
        first=copy.deepcopy(apply_delivery_links(caps))
        self.assertEqual(first,apply_delivery_links(caps))
        self.assertEqual(untouched,{k:v for k,v in caps.items() if k!='work_products'})
        for identity in ('architecture-governance-checklist','decision-delegation-register'):
            row=next(w for w in caps['work_products'] if w['id']==identity)
            self.assertIn('implementation-governance-model',row['related_deliverables'])
            self.assertIn('if any',row['related_deliverable_context']['implementation-governance-model'])

    def test_adm_output_contract_remains_conditional_not_mandatory_at_G(self):
        phases={p['id']:p for p in json.loads((ROOT/'references/adm-phases.json').read_text())['phases']}
        self.assertTrue(any(d['id']=='implementation-governance-model' and d['condition_en']=='if any'
                            for d in phases['F']['conditional_deliverables']))
        self.assertNotIn('implementation-governance-model',phases['G']['deliverables'])
        self.assertIn('compliance-assessment',phases['G']['deliverables'])


if __name__=='__main__':unittest.main()
