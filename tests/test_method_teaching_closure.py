"""Execute eight methods against authored teaching materials and adverse changes."""
import copy
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(ROOT/'scripts'))
from analyze import evaluate
from method_teaching_closure import cases, assert_expected


class MethodTeachingClosureTest(unittest.TestCase):
    def test_eight_methods_four_business_variants(self):
        for method,case in cases().items():
            for variant,record in case['scenarios'].items():
                with self.subTest(method=method,variant=variant):
                    expected=record['expected']
                    analysis={'id':'TEACHING','method_id':method,'inputs':record['inputs']}
                    if 'reject' in expected:
                        with self.assertRaisesRegex(ValueError,expected['reject']):evaluate(analysis)
                    else:assert_expected(evaluate(analysis)['result'],expected)

    def test_dtra_deferral_requires_a_nonblank_reason(self):
        case=cases()['dtra-adm-phase-alignment-review']['scenarios']['missing']['inputs']
        for reason in ('','   ',None,False,{},[]):
            with self.subTest(reason=reason):
                data=copy.deepcopy(case);data['deferred_factors']={'culture':reason}
                result=evaluate({'id':'DTRA','method_id':'dtra-adm-phase-alignment-review','inputs':data})['result']
                self.assertIn('low-rated-factor-unaddressed',{g['reason'] for g in result['gaps']})
        data=copy.deepcopy(case);data['deferred_factors']={'culture':'先完成双店职责演练；下一愿景阶段复评后才扩围'}
        result=evaluate({'id':'DTRA','method_id':'dtra-adm-phase-alignment-review','inputs':data})['result']
        self.assertNotIn('low-rated-factor-unaddressed',{g['reason'] for g in result['gaps']})

    def test_dtra_factor_reference_without_action_cannot_close_attention(self):
        base=cases()['dtra-adm-phase-alignment-review']['scenarios']['sufficient']['inputs']
        for content in (None, '', '   ', False, True, 0, [], {}, {'text':'培训'}):
            with self.subTest(content=content):
                data=copy.deepcopy(base)
                action={'factor_ids':['culture']}
                if content is not None:action['action']=content
                data['phase_records'][0]['actions']=[action]
                result=evaluate({'id':'DTRA','method_id':'dtra-adm-phase-alignment-review','inputs':data})['result']
                self.assertIn('attention:culture',{g['id'] for g in result['gaps']})
                self.assertIn('action-content-missing',{g['reason'] for g in result['rows'][0]['gaps']})

    def test_dtra_action_state_or_string_cannot_close_attention(self):
        base=cases()['dtra-adm-phase-alignment-review']['scenarios']['sufficient']['inputs']
        for action in (None, '', '培训', False):
            with self.subTest(action=action):
                data=copy.deepcopy(base);data['phase_records'][0]['actions']=[action]
                result=evaluate({'id':'DTRA','method_id':'dtra-adm-phase-alignment-review','inputs':data})['result']
                self.assertIn('attention:culture',{g['id'] for g in result['gaps']})
                self.assertIn('invalid-action-record',{g['reason'] for g in result['gaps']})

    def test_dtra_action_factor_ids_are_typed_and_known(self):
        base=cases()['dtra-adm-phase-alignment-review']['scenarios']['sufficient']['inputs']
        for factor_ids in ('culture', False, ['absent-factor'], [False], [{}]):
            with self.subTest(factor_ids=factor_ids):
                data=copy.deepcopy(base);data['phase_records'][0]['actions'][0]['factor_ids']=factor_ids
                with self.assertRaisesRegex(ValueError,'DAP-004'):
                    evaluate({'id':'DTRA','method_id':'dtra-adm-phase-alignment-review','inputs':data})

    def test_dtra_action_only_handles_its_named_factors(self):
        base=cases()['dtra-adm-phase-alignment-review']['scenarios']['sufficient']['inputs']
        data=copy.deepcopy(base);data['factor_ratings']['it-capability']=4
        result=evaluate({'id':'DTRA','method_id':'dtra-adm-phase-alignment-review','inputs':data})['result']
        attention_gaps={g['id'] for g in result['gaps'] if g['reason']=='low-rated-factor-unaddressed'}
        self.assertEqual({'attention:it-capability'},attention_gaps)

    def test_incomplete_or_expired_dispensation_cannot_unblock_conflict(self):
        base=cases()['product-constraint-conformance-review']['scenarios']['sufficient']['inputs']
        for field in ('authority','rationale','expiry','evidence'):
            with self.subTest(field=field):
                data=copy.deepcopy(base);data['dispensations'][0].pop(field)
                result=evaluate({'id':'PCC','method_id':'product-constraint-conformance-review','inputs':data})['result']
                self.assertEqual(['B-DIRECT'],result['blocked_item_ids'])
        data=copy.deepcopy(base);data['as_of']='2026-12-01'
        result=evaluate({'id':'PCC','method_id':'product-constraint-conformance-review','inputs':data})['result']
        self.assertEqual(['B-DIRECT'],result['blocked_item_ids'])
        self.assertIn('dispensation-expired',{g['reason'] for g in result['gaps']})

    def test_no_review_date_keeps_dispensation_validity_unknown_and_conflict_blocked(self):
        base=cases()['product-constraint-conformance-review']['scenarios']['sufficient']['inputs']
        for expiry in ('2000-01-01','2099-12-31'):
            for missing_date in (None,'',False):
                with self.subTest(expiry=expiry,as_of=missing_date):
                    data=copy.deepcopy(base);data['dispensations'][0]['expiry']=expiry
                    if missing_date is None:data.pop('as_of')
                    else:data['as_of']=missing_date
                    result=evaluate({'id':'PCC','method_id':'product-constraint-conformance-review','inputs':data})['result']
                    self.assertEqual(['B-DIRECT'],result['blocked_item_ids'])
                    self.assertEqual('blocked-local-preference',result['findings'][0]['state'])
                    self.assertEqual('unknown-no-as-of',result['findings'][0]['validity_state'])
                    self.assertIn('dispensation-validity-unknown',{g['reason'] for g in result['gaps']})

    def test_expiry_day_is_usable_only_at_declared_review_date(self):
        base=cases()['product-constraint-conformance-review']['scenarios']['sufficient']['inputs']
        data=copy.deepcopy(base);data['as_of']=data['dispensations'][0]['expiry']
        result=evaluate({'id':'PCC','method_id':'product-constraint-conformance-review','inputs':data})['result']
        self.assertEqual([],result['blocked_item_ids'])
        self.assertEqual('dispensation-recorded',result['findings'][0]['state'])
        self.assertEqual('current-at-declared-date',result['findings'][0]['validity_state'])
        self.assertEqual([],result['gaps'])


if __name__=='__main__':unittest.main()
