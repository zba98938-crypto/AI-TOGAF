"""Actual argument/result frames, original operation roles and independent XML oracle."""
import json
import os
from pathlib import Path
import sys
import unittest
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import Invalid,Incomplete,sha
from uml_backend import validate_mapped,multiplicity_case_records
from uml_ocl_obligations import multiplicity_execution_catalog
from uml_operation_derived_fixtures import multiplicity_operation_fixture,scalar_xml_oracle,expected_native_value,positive_cases

class MultiplicitySourceContractTests(unittest.TestCase):
    def test_all_eight_queries_ten_roles_and_two_explicit_derived_links_remain_catalog_only(self):
        catalog=multiplicity_execution_catalog();operations=catalog['operations'];rules=[r for o in operations for r in o['rules']]
        self.assertEqual(8,len(operations));self.assertEqual(10,len(rules));self.assertEqual(2,sum(o['derived'] is not None for o in operations))
        self.assertEqual(8,sum(r['role']=='bodyCondition' for r in rules));self.assertEqual(2,sum(r['role']=='precondition' for r in rules))
        self.assertEqual(0,catalog['catalog_execution_count']);self.assertFalse(catalog['full_standard_acceptance'])
        for rule in rules:self.assertEqual(sha(rule['original_body'].encode()),rule['original_body_sha256'])
        query=next(o for o in operations if o['name']=='is')
        self.assertEqual([('result','return','Boolean'),('lowerbound','in','Integer'),('upperbound','in','UnlimitedNatural')],[(p['name'],p['direction'],p['type']) for p in query['parameters']])
        self.assertIn('unlimitedValue()',next(o['rules'][0]['original_body'] for o in operations if o['name']=='upperBound'))
    def test_cases_cannot_supply_code_unknown_sources_or_duplicate_ids(self):
        key=multiplicity_execution_catalog()['operations'][0]['source_identity']['key']
        case={'id':'x','self':'DEFAULT','obligation':key}
        for cases in [[{**case,'body':'true'}],[case,case],{},[{'id':'x','self':'DEFAULT','obligation':'unknown'}]]:
            with self.assertRaises((Invalid,Incomplete)):multiplicity_case_records(cases)
    def test_return_probes_are_fixed_and_never_expand_preconditions(self):
        operation=next(o for o in multiplicity_execution_catalog()['operations'] if o['name']=='isMultivalued')
        case={'id':'x','self':'FINITE','obligation':operation['source_identity']['key'],'result_probe':'invalid'}
        rows,metadata,_=multiplicity_case_records([case]);self.assertEqual(1,len(rows));self.assertEqual('bodyCondition',metadata[0]['role'])
        self.assertTrue(metadata[0]['result_probe_is_diagnostic_only']);self.assertFalse(metadata[0]['full_obligation_implemented'])
        with self.assertRaises(Invalid):multiplicity_case_records([{**case,'result_probe':'arbitrary'}])

class ActualMultiplicityOperationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=multiplicity_execution_catalog();cls.data=multiplicity_operation_fixture();cls.oracle=scalar_xml_oracle(cls.data)
        cls.cases=positive_cases(cls.catalog,cls.oracle);by_name={o['name']:o for o in cls.catalog['operations']}
        cls.valid_cases=list(cls.cases)
        for probe in ['false','null','invalid']:
            cls.cases.append({'id':'result-'+probe,'self':'FINITE','obligation':by_name['isMultivalued']['source_identity']['key'],'result_probe':probe})
        cls.cases.extend([
            {'id':'no-instance','self':'MISSING','obligation':by_name['upperBound']['source_identity']['key']},
            {'id':'missing-args','self':'FINITE','obligation':by_name['is']['source_identity']['key']},
            {'id':'wrong-arg-type','self':'FINITE','obligation':by_name['is']['source_identity']['key'],'arguments':[{'kind':'unlimited','value':2},{'kind':'unlimited','value':5}]},
            {'id':'unlimited-negative','self':'FINITE','obligation':by_name['is']['source_identity']['key'],'arguments':[{'kind':'integer','value':2},{'kind':'unlimited','value':-1}]},
            {'id':'int-overflow','self':'FINITE','obligation':by_name['is']['source_identity']['key'],'arguments':[{'kind':'integer','value':2**64},{'kind':'unlimited','value':5}]},
            {'id':'missing-object-arg','self':'FINITE','obligation':by_name['compatibleWith']['source_identity']['key'],'arguments':[{'kind':'object','value':'MISSING'}]},
            {'id':'wrong-self-type','self':'C','obligation':by_name['upperBound']['source_identity']['key']},
            {'id':'null-arg','self':'FINITE','obligation':by_name['is']['source_identity']['key'],'arguments':[{'kind':'null','value':'null'},{'kind':'unlimited','value':5}]},
            {'id':'invalid-arg','self':'FINITE','obligation':by_name['is']['source_identity']['key'],'arguments':[{'kind':'invalid','value':'invalid'},{'kind':'unlimited','value':5}]},
        ])
        for identity,values in cls.oracle.items():
            if not values['nullable_carrier_boundaries']:continue
            for name in ['lowerBound','upperBound']:
                cls.cases.append({'id':'carrier-'+identity+'-'+name,'self':identity,'obligation':by_name[name]['source_identity']['key']})
        cls.report=validate_mapped(cls.data,operation_cases=cls.cases)
        cls.rows=cls.report['operation_derived_cases'];cls.index={}
        for row in cls.rows:cls.index.setdefault(row['case_id'],[]).append(row)
    def test_each_original_constraint_and_derived_definition_executes_with_actual_values(self):
        for case in self.valid_cases:
            for row in self.index[case['id']]:
                self.assertEqual('executed-bounded-original-constraint',row['execution_status'],row)
                self.assertEqual(1,row['evaluation_count']);self.assertEqual('true',row['constraint_outcome']['kind'],row)
                self.assertTrue(row['original_body_preserved']);self.assertTrue(row['source_role_preserved']);self.assertTrue(row['frame_cleared'])
                self.assertFalse(row['uses_postcondition_api']);self.assertFalse(row['uses_body_rhs_substitution'])
        identities={row['obligation_identity_key'] for case in self.valid_cases for row in self.index[case['id']]}
        expected={r['source_identity']['key'] for o in self.catalog['operations'] for r in o['rules']}|{o['derived']['source_identity']['key'] for o in self.catalog['operations'] if o['derived']}
        self.assertEqual(expected,identities);self.assertEqual(12,len(identities))
    def test_native_scalar_boolean_and_unlimited_results_match_independent_xml_oracle(self):
        for case in self.valid_cases:
            for row in self.index[case['id']]:
                if row['normative_role']!='bodyCondition':continue
                expected=expected_native_value(row['operation_name'],case['self'],case.get('arguments',[]),self.oracle)
                actual=row['native_result'];self.assertEqual(expected,(actual['kind'],actual['value']),row)
        star=next(r for r in self.rows if r['case_id']=='is-UNLIMITED-match')
        self.assertEqual('*',star['argument_bindings'][1]['value']['value']);self.assertEqual('UnlimitedNatural',star['argument_bindings'][1]['type'])
    def test_parameter_names_direction_order_and_runtime_result_binding_are_preserved(self):
        row=self.index['is-FINITE-match'][0]
        self.assertEqual([('lowerbound','Integer',0),('upperbound','UnlimitedNatural',1)],[(r['name'],r['type'],r['argument_slot']) for r in row['argument_bindings']])
        self.assertEqual('result',row['result_binding']['name']);self.assertEqual('Boolean',row['result_binding']['type'])
        self.assertTrue(all(r['runtime_parameter_uri'].endswith(r['name']) for r in row['argument_bindings']))
        forward=self.index['includesMultiplicity-UNLIMITED-FINITE'][-1]['native_result']['kind']
        reverse=self.index['includesMultiplicity-FINITE-UNLIMITED'][-1]['native_result']['kind'];self.assertEqual(('true','false'),(forward,reverse))
    def test_false_null_and_invalid_result_probes_are_distinct_and_never_acceptance(self):
        expected={'false':('false','false'),'null':('null','false'),'invalid':('invalid','invalid')}
        for probe,(bound,outcome) in expected.items():
            row=self.index['result-'+probe][0]
            self.assertEqual(bound,row['result_binding']['value']['kind']);self.assertEqual(outcome,row['constraint_outcome']['kind'])
            self.assertEqual('true',row['native_result']['kind']);self.assertEqual('executed-diagnostic-result-probe',row['execution_status'])
            self.assertTrue(row['result_probe_is_diagnostic_only']);self.assertFalse(row['full_obligation_implemented'])
    def test_missing_instances_wrong_types_bad_arguments_and_carrier_overflow_stay_uncovered(self):
        identities=['no-instance','missing-args','wrong-arg-type','unlimited-negative','int-overflow','missing-object-arg','wrong-self-type','null-arg','invalid-arg']
        for identity in identities:
            for row in self.index[identity]:
                self.assertTrue(row['execution_status'].startswith('uncovered'),row);self.assertEqual(0,row['evaluation_count'])
                self.assertNotIn('constraint_outcome',row);self.assertFalse(row['full_obligation_implemented'])
    def test_optional_native_int_carriers_are_disclosed_and_do_not_certify_null_semantics(self):
        rows=[r for r in self.rows if r['case_id'].startswith('carrier-')]
        self.assertEqual(12,len(rows))
        for row in rows:
            self.assertFalse(row['native_nullable_carrier_certified']);self.assertFalse(row['full_obligation_implemented'])
            self.assertTrue(self.oracle[row['self_id']]['nullable_carrier_boundaries'])
            expected=expected_native_value(row['operation_name'],row['self_id'],[],self.oracle)
            self.assertEqual(expected,(row['native_result']['kind'],row['native_result']['value']))
        affected=[r for r in rows if ('LOWER' in r['self_id'] and r['operation_name']=='lowerBound') or ('UPPER' in r['self_id'] and r['operation_name']=='upperBound')]
        self.assertEqual(6,len(affected))
        for row in affected:
            self.assertEqual('invalid',row['constraint_outcome']['kind']);self.assertEqual('uncovered-original-constraint-not-true',row['obligation_status'])
        self.assertFalse(self.report['official_full_conformance']);self.assertEqual('incomplete',self.report['conformance_status'])
        self.assertFalse(self.report['operation_derived_capability']['full_obligation_implemented'])

if __name__=='__main__':unittest.main()
