"""Actual parser/AST/value/branch acceptance against independent XML expressions."""
import base64,json,os,subprocess,sys,tempfile,unittest
from pathlib import Path
from lxml import etree
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from uml_backend import JARS,ROOT,conditional_ast_adapter,conditional_type_adapter,OCL_PUBLICATION_SHA256,validate_mapped
from uml_conditional_fixtures import cases,common_type_regressions,native_shape,trace_mapping,branch_paths,oracle,type_oracle,assert_native_types,TYPES,COMMON_TYPES
from test_uml_ocl_boundaries import query_report

NATIVE=bool(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME',''))/'bin/java').is_file())
@unittest.skipUnless(NATIVE,'set the existing local JAVA_HOME for actual conditional AST evaluation')
class ActualConditionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases=cases();cls.type_cases=common_type_regressions();cls.model=b'<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:id="M"/>'
        cls.controls=['let condition : Boolean = '+v+' in if condition then true else false endif' for v in ('true','false','null','invalid')]
        cls.long=['('*65+'true'+')'*65,' and '.join(['true']*1025),'not '*64+'false']
        cls.rejected=['if 1 then true else false endif','if null then true endif','if null then true else false endif extra',
            'if null then self.name else false endif','if null then \'arbitrary\' else false endif','if null then true else false endif;true',
            'if (null and invalid then true else false endif','if null then true else endif',
            '(' * 65+'if null then true else false endif'+')' * 65,
            'if null then ' * 65+'true'+' else false endif' * 65]
        cls.bodies=[r['body'] for r in cls.cases+cls.type_cases]+cls.controls+cls.long+cls.rejected
        cls.folder=tempfile.TemporaryDirectory(prefix='uml-if-ast-');folder=Path(cls.folder.name)
        expression_file=folder/'expressions.b64';expression_file.write_text('\n'.join(base64.b64encode(s.encode()).decode() for s in cls.bodies)+'\n')
        java=Path(os.environ['JAVA_HOME'])/'bin';classes=folder/'classes';classes.mkdir()
        subprocess.run([str(java/'javac'),'-cp',str(JARS/'*'),'-d',str(classes),str(ROOT/'scripts/UmlValidate.java'),str(REPO/'tests/java/UmlConditionalProbe.java')],capture_output=True,text=True,timeout=60,check=True)
        run=subprocess.run([str(java/'java'),'-Xmx512m','-cp',str(JARS/'*')+os.pathsep+str(classes),'UmlConditionalProbe',str(JARS),str(expression_file)],capture_output=True,text=True,timeout=120,check=True)
        cls.trace_rows=json.loads(run.stdout);cls.trace={r['body']:r for r in cls.trace_rows}
        cls.report=query_report(cls.model,[{'context':'Model','id':r['id'],'body':r['body']} for r in cls.cases])
    @classmethod
    def tearDownClass(cls):cls.folder.cleanup()
    def test_all_four_condition_and_branch_values_match_independent_xml_oracle(self):
        for r in self.cases:
            with self.subTest(case=r['id']):
                actual=self.trace[r['body']]['current'];self.assertEqual('parsed',actual['parse_status'],actual)
                self.assertEqual(r['expected'],actual['value_kind']);self.assertEqual(1,actual['evaluation_count'])
    def test_adapted_ast_preserves_condition_literals_and_branch_order(self):
        for r in self.cases:
            with self.subTest(case=r['id']):self.assertEqual(r['shape'],native_shape(self.trace[r['body']]['current']['ast']))
    def test_xml_oracle_rejects_actual_false_condition_and_swapped_branch_counterexamples(self):
        for body in ('if null then true else false endif','if true then true else false endif'):
            with self.subTest(body=body):
                row=next(r for r in self.cases if r['body']==body);changed=self.trace[body]['counterexample']
                self.assertTrue(changed['deliberate_test_counterexample']);self.assertEqual('parsed',changed['parse_status'])
                self.assertEqual('false',changed['value_kind']);self.assertNotEqual(row['expected'],changed['value_kind'])
                self.assertNotEqual(row['shape'],native_shape(changed['ast']));self.assertEqual(1,changed['evaluation_count'])
    def test_only_xml_oracle_selected_branches_are_actually_visited(self):
        for r in self.cases:
            with self.subTest(case=r['id']):
                node=etree.fromstring(r['xml'].encode());selected=[];oracle(node,selected=selected)
                actual=self.trace[r['body']]['current'];mapping=trace_mapping(actual['ast']);visits=[mapping[v] for v in actual['visits']]
                found={branch for branch in branch_paths(node) if any(v==branch or v.startswith(branch+'/') for v in visits)}
                self.assertEqual(set(selected),found)
    def test_null_invalid_and_false_remain_disjoint_report_outcomes(self):
        self.assertEqual(len(self.cases),self.report['ocl_evaluations']);self.assertEqual(0,self.report['ocl_unmapped'])
        counters={'true':'true_evaluations','false':'violations','null':'null_evaluations','invalid':'invalid_evaluations'}
        for expected,actual in zip(self.cases,self.report['ocl_rules']):
            with self.subTest(case=expected['id']):
                self.assertEqual([{'id':'M','value_kind':expected['expected']}],actual['evaluation_outcomes'])
                for value,field in counters.items():self.assertEqual(int(expected['expected']==value),actual[field])
    def test_original_parser_runs_before_each_conditional_fallback(self):
        for r in self.cases:
            original=self.trace[r['body']]['original'];actual=self.trace[r['body']]['current']
            with self.subTest(case=r['id']):
                if original['parse_status']=='parsed':
                    self.assertFalse(actual['literal_ast_adapter']);self.assertFalse(actual['conditional_ast_adapter']);self.assertEqual(original['value_kind'],actual['value_kind'])
                else:self.assertTrue(actual['conditional_ast_adapter']);self.assertEqual(original['error'],actual['original_parser_error'])
    def test_typed_let_and_long_original_parser_inputs_keep_the_native_path(self):
        for body,value in zip(self.controls+self.long,['true','false','invalid','invalid','true','true','false']):
            for mode in ('original','current'):
                with self.subTest(mode=mode,body=body[:80]):
                    actual=self.trace[body][mode];self.assertEqual('parsed',actual['parse_status']);self.assertEqual(value,actual['value_kind'])
                    if mode=='current':
                        self.assertFalse(actual['literal_ast_adapter']);self.assertFalse(actual['conditional_ast_adapter'])
                        self.assertEqual('uncovered',actual['conditional_type_adapter']['status']);self.assertFalse(actual['conditional_type_adapter']['adjusted']);self.assertEqual([],actual['conditional_type_adapter']['nodes'])
            self.assertEqual(self.trace[body]['original'].get('ast',self.trace[body]['original'].get('ast_summary')),self.trace[body]['current'].get('ast',self.trace[body]['current'].get('ast_summary')))
    def test_every_recursive_static_type_matches_independent_xml_oracle_in_both_branch_orders(self):
        for r in self.cases+self.type_cases:
            with self.subTest(case=r['id']):
                node=etree.fromstring(r['xml'].encode());actual=self.trace[r['body']]['current'];self.assertEqual('parsed',actual['parse_status'])
                assert_native_types(node,actual['ast']);self.assertEqual(type_oracle(node),actual['ast']['type'])
                self.assertEqual('bounded-covered',actual['conditional_type_adapter']['status'])
                self.assertEqual(sum(n.tag=='if' for n in node.iter()),len(actual['conditional_type_adapter']['nodes']))
        for body in ('if true then null else invalid endif','if true then invalid else null endif'):
            self.assertEqual('OclVoid',self.trace[body]['current']['ast']['type'])
    def test_type_adjustments_disclose_original_and_fallback_witness_without_changing_native_values(self):
        origins=set()
        for r in self.type_cases:
            with self.subTest(case=r['id']):
                original=self.trace[r['body']]['original'];actual=self.trace[r['body']]['current'];adapter=actual['conditional_type_adapter']
                self.assertEqual(r['original_status'],original['parse_status']);self.assertEqual(r['expected'],actual['value_kind']);self.assertEqual(r['shape'],native_shape(actual['ast']))
                self.assertEqual(r['original_status']=='failed',actual['conditional_ast_adapter']);self.assertEqual(r['original_status']=='failed',actual['literal_ast_adapter'])
                origin='original-parser' if r['original_status']=='parsed' else 'fallback-witness-parser';origins.add(origin)
                self.assertTrue(adapter['adjusted']);self.assertFalse(adapter['full_language_equivalence_certified'])
                for item in adapter['nodes']:
                    self.assertEqual(origin,item['origin']);self.assertEqual('source-logical',item['path_kind'])
                    self.assertIn(item['before'],TYPES);self.assertIn(item['then_before_type'],TYPES);self.assertIn(item['else_before_type'],TYPES)
                    self.assertEqual(COMMON_TYPES[TYPES.index(item['then_type'])][TYPES.index(item['else_type'])],item['after'])
                    self.assertEqual(item['before']!=item['after'],item['adjusted'])
                self.assertTrue(any(n['before']=='OclInvalid' and n['after']=='OclVoid' for n in adapter['nodes']))
                if original['parse_status']=='parsed':self.assertEqual(original['value_kind'],actual['value_kind']);self.assertIsNone(actual['original_parser_error'])
                else:self.assertEqual(original['error'],actual['original_parser_error'])
        self.assertEqual({'original-parser','fallback-witness-parser'},origins)
    def test_independent_type_oracle_rejects_value_preserving_native_type_counterexamples(self):
        count=0
        for r in self.cases:
            actual=self.trace[r['body']]['current']
            for changed in self.trace[r['body']].get('type_counterexamples',[]):
                with self.subTest(case=r['id'],mode=changed['mode']):
                    self.assertEqual('parsed',changed['parse_status']);self.assertEqual(actual['value_kind'],changed['value_kind'])
                    self.assertEqual(actual['visits'],changed['visits']);self.assertEqual(r['shape'],native_shape(changed['ast']))
                    with self.assertRaises(AssertionError):assert_native_types(etree.fromstring(r['xml'].encode()),changed['ast'])
                    count+=1
        self.assertEqual(4,count)
    def test_source_ast_mismatch_cancels_all_planned_type_changes(self):
        row=self.type_cases[1];changed=self.trace[row['body']]['gate_counterexample']
        self.assertEqual('parsed',changed['parse_status']);self.assertEqual(changed['ast_before_gate'],changed['ast'])
        self.assertEqual('uncovered',changed['conditional_type_adapter']['status']);self.assertEqual([],changed['conditional_type_adapter']['nodes']);self.assertFalse(changed['conditional_type_adapter']['adjusted'])
        self.assertEqual('OclInvalid',changed['ast']['thenExpression']['type'])
    def test_non_boolean_malformed_nonliteral_and_over_limit_inputs_stay_uncovered(self):
        for body in self.rejected:
            with self.subTest(body=body[:80]):self.assertEqual('failed',self.trace[body]['current']['parse_status']);self.assertEqual(0,self.trace[body]['current']['evaluation_count'])
    def test_absent_context_does_not_turn_parsed_expression_into_a_pass(self):
        report=query_report(self.model,[{'context':'Lifeline','id':'no-instance','body':'if null then true else true endif'}]);row=report['ocl_rules'][0]
        self.assertEqual('parsed',row['parse_status']);self.assertEqual(0,row['applicable']);self.assertEqual([],row['evaluation_outcomes']);self.assertEqual(0,report['ocl_evaluations']);self.assertFalse(report['official_full_conformance'])
    def test_source_basis_and_adaptation_do_not_claim_full_equivalence(self):
        report=validate_mapped(self.model);self.assertIn('conditional_ast_adapter',report)
        self.assertEqual('OCL-2.4-bounded-literal-conditional-typing',report['conditional_ast_adapter']['id'])
        adapter=conditional_ast_adapter();self.assertEqual(OCL_PUBLICATION_SHA256,adapter['basis']['sha256'])
        self.assertEqual(['8.2.1 InvalidType/VoidType','8.3.7 IfExp/LetExp/Variable/VariableExp','10.4.2.2 IfExpEval','A.3.1.2'],adapter['basis']['clauses'])
        self.assertEqual(adapter['basis']['clauses'],report['conditional_ast_adapter']['basis']['clauses'])
        self.assertEqual([57,58,73,77,80,148,248],adapter['basis']['pdf_pages']);self.assertEqual('invalid',adapter['undefined_condition_result'])
        self.assertFalse(adapter['undefined_condition_evaluates_else']);self.assertFalse(adapter['source_ast_identity_claimed']);self.assertFalse(adapter['full_language_equivalence_certified']);self.assertEqual('pending',adapter['human_acceptance'])
        common=conditional_type_adapter();self.assertEqual(common,report['conditional_type_adapter']);self.assertEqual(OCL_PUBLICATION_SHA256,common['basis']['sha256'])
        self.assertEqual(['8.2.1 InvalidType/VoidType','8.3.7 IfExp','8.3.8 Classifier.commonSuperType'],common['basis']['clauses']);self.assertEqual([57,58,73,80],common['basis']['pdf_pages'])
        self.assertEqual(list(TYPES),common['types']);self.assertEqual([list(row) for row in COMMON_TYPES],common['common_types'])
        self.assertFalse(common['source_ast_identity_claimed']);self.assertFalse(common['full_language_equivalence_certified']);self.assertEqual('pending',common['human_acceptance'])

if __name__=='__main__':unittest.main()
