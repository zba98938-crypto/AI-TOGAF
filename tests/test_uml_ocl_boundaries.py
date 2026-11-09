"""Independent XML/classifier and four-valued OCL boundary acceptance."""
import base64
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from lxml import etree
REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import Incomplete,sha,XMI
from uml_backend import (ROOT,JARS,validate_mapped,official_rules,execution_rules,official_query_adapters,
    LIFELINE_CLASSIFIER_RULE,LIFELINE_CLASSIFIER_SOURCE_SHA256)
from uml_ocl_obligations import execution_inventory
from uml_ocl_boundary_fixtures import (lifeline_classifier_fixture,classifier_oracle,
    boolean_boundary_expressions,parser_compatible_large_boolean_expressions,
    balanced_over_token_boolean_expression,multiplicity_boundary_fixture,UML)

def query_report(data,probes):
    # These generated fixtures have no external href or business URL literals.
    # Preserve the original fixture; namespace substitution is a separate copy.
    mapped=data.replace(UML.encode(),b'http://www.eclipse.org/uml2/5.0.0/UML').replace(
        XMI.encode(),b'http://www.omg.org/XMI')
    def tsv(rows):return '\n'.join('\t'.join(base64.b64encode(str(value).encode()).decode() for value in row) for row in rows)+'\n'
    with tempfile.TemporaryDirectory(prefix='uml-ocl-boundaries-') as folder:
        folder=Path(folder);model=folder/'probe.uml';model.write_bytes(mapped)
        rules=folder/'rules.tsv';rules.write_text(tsv([(row['context'],row['id'],row['body']) for row in probes]))
        queries=folder/'queries.tsv';queries.write_text(tsv([(row['context'],row['id'],row['definition']) for row in official_query_adapters()]))
        run=subprocess.run([str(Path(os.environ['JAVA_HOME'])/'bin/java'),'-Xmx512m','--class-path',str(JARS/'*'),
            str(ROOT/'scripts/UmlValidate.java'),str(model),str(rules),str(JARS),str(queries)],capture_output=True,text=True,timeout=120,check=True)
        return json.loads(run.stdout)

class OCLExecutionScopeTests(unittest.TestCase):
    def test_every_source_obligation_is_classified_without_executing_it(self):
        report=execution_inventory();summary=report['summary']
        self.assertEqual((425,225,205,202,23,0,73,8),(summary['class_ocl_invariants'],summary['operation_owned_ocl_constraints'],
            summary['operation_declarations'],summary['operation_body_condition_references'],summary['operation_precondition_references'],
            summary['operation_postcondition_references'],summary['derived_features'],summary['duplicate_xml_native_id_groups']))
        self.assertEqual(650,len(report['ocl_rules']));self.assertEqual(650,len({r['source_identity']['key'] for r in report['ocl_rules']}))
        self.assertTrue(report['source_fingerprint_verified']);self.assertTrue(report['source_bytes_preserved'])
        self.assertEqual(0,summary['catalog_execution_count']);self.assertEqual('incomplete',summary['independent_operation_and_derived_scope'])
        self.assertFalse(summary['body_conditions_are_postcondition_declarations']);self.assertFalse(summary['full_standard_acceptance'])
        self.assertTrue(all(sha(r['original_body'].encode())==r['original_body_sha256'] for r in report['ocl_rules']))

    def test_duplicate_operation_reference_does_not_get_a_hidden_resolution(self):
        report=execution_inventory()
        ops=[r for r in report['operations'] if r['native_id']=='State-isConsistentWith']
        self.assertEqual({'State','Vertex'},{r['context'] for r in ops})
        self.assertEqual(2,len({r['source_identity']['key'] for r in ops}))
        for op in ops:
            for ref in op['constraint_references']:
                self.assertEqual('ambiguous-source-reference',ref['status']);self.assertIsNone(ref['resolved_target']);self.assertEqual(2,len(ref['candidates']))
        feature=report['vertex_inherited_features']
        self.assertEqual(1,len(feature));self.assertEqual('RedefinableElement',feature[0]['declaring_classifier'])
        self.assertTrue(feature[0]['is_derived']);self.assertTrue(feature[0]['is_derived_union'])
        self.assertIsNone(feature[0]['operation_parameter_resolution'])

    def test_classifier_semantic_adapter_keeps_the_pinned_body_and_prose(self):
        rows,_=official_rules();original=copy.deepcopy(rows);_,adapters=execution_rules(rows)
        adapter=next(row for row in adapters if row['id']==LIFELINE_CLASSIFIER_RULE)
        self.assertEqual(original,rows);self.assertEqual(LIFELINE_CLASSIFIER_SOURCE_SHA256,adapter['original_body_sha256'])
        self.assertEqual([665],adapter['basis']['pdf_pages']);self.assertEqual([623],adapter['basis']['printed_pages'])
        self.assertFalse(adapter['official_full_conformance']);self.assertEqual('pending',adapter['human_acceptance'])
        self.assertIn('not claimed',adapter['source_execution_equivalence'])

NATIVE=bool(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME',''))/'bin/java').is_file())
@unittest.skipUnless(NATIVE,'set the existing local JAVA_HOME for actual native OCL')
class ActualLifelineClassifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=lifeline_classifier_fixture();cls.expected=classifier_oracle(cls.data);cls.report=validate_mapped(cls.data)
        original=next(row for row in official_rules()[0] if row['id']==LIFELINE_CLASSIFIER_RULE)
        cls.published_report=query_report(cls.data,[original])
    def test_every_lifeline_matches_closest_classifier_and_explicit_inheritance_oracle(self):
        row=next(row for row in self.report['ocl_rules'] if row['id']==LIFELINE_CLASSIFIER_RULE)
        self.assertEqual(self.expected,{r['id']:r['value_kind'] for r in row['evaluation_outcomes']})
        self.assertEqual(11,row['applicable']);self.assertEqual(1,row['invalid_evaluations']);self.assertEqual(['L_ABSENT'],row['invalid_ids'])
        self.assertEqual({'L_UNRELATED','L_NESTED'},set(row['violation_ids']))
    def test_published_body_and_prose_differences_stay_visible(self):
        source=self.published_report['ocl_rules'][0];values={r['id']:r['value_kind'] for r in source['evaluation_outcomes']}
        self.assertEqual('false',values['L_SELF']);self.assertEqual('false',values['L_PARENT']);self.assertEqual('false',values['L_GRAND'])
        self.assertEqual('true',values['L_NESTED']);self.assertEqual('invalid',values['L_ABSENT'])
        self.assertFalse(self.report['official_full_conformance']);self.assertEqual('incomplete',self.report['conformance_status'])
        self.assertEqual(225,self.report['normative_ocl_execution_scope']['operation_owned_ocl_constraints'])
    def test_other_lifeline_constraints_have_independent_selector_counterexamples(self):
        rows={r['id']:r for r in self.report['ocl_rules']}
        self.assertEqual({'L_MULTI_ABSENT','L_SINGLE_INT'},set(rows['Lifeline-selector_specified']['violation_ids']))
        self.assertEqual({'L_MULTI_BOOLEAN'},set(rows['Lifeline-selector_int_or_string']['violation_ids']))
        self.assertEqual(11,rows['Lifeline-interaction_uses_share_lifeline']['true_evaluations'])

@unittest.skipUnless(NATIVE,'set the existing local JAVA_HOME for actual native OCL')
class ActualGroupedBooleanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=b'<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:id="M" name="Boolean boundaries"/>'
        cls.expected=boolean_boundary_expressions()
        cls.compatible=parser_compatible_large_boolean_expressions()
        cls.expected.update(cls.compatible)
        cls.rejected=['null (and invalid)','(null and invalid','not null )','(null and invalid) and',
            '(' * 65+'null and invalid'+')' * 65,balanced_over_token_boolean_expression()]
        cls.probes=[{'context':'Model','id':body,'body':body} for body in cls.expected]
        cls.probes.extend({'context':'Model','id':'rejected-'+str(i),'body':body} for i,body in enumerate(cls.rejected))
        cls.report=query_report(cls.data,cls.probes)
    def test_grouped_null_invalid_false_and_true_remain_distinct(self):
        rows={r['id']:r for r in self.report['ocl_rules']}
        for body,value in self.expected.items():
            row=rows[body]
            if body.startswith('if '):continue
            self.assertEqual('parsed',row['parse_status'],row);self.assertEqual([{'id':'M','value_kind':value}],row['evaluation_outcomes'])
        adapted={r['id'] for r in rows.values() if r['literal_ast_adapter']}
        self.assertEqual(set(list(self.expected)[:6]),adapted)
    def test_installed_parser_compatible_inputs_bypass_fallback_limits(self):
        rows={r['id']:r for r in self.report['ocl_rules']}
        for body,value in self.compatible.items():
            row=rows[body]
            self.assertEqual('parsed',row['parse_status'],row)
            self.assertFalse(row['literal_ast_adapter'])
            self.assertEqual([{'id':'M','value_kind':value}],row['evaluation_outcomes'])
    def test_conditionals_and_malformed_or_over_limit_inputs_are_not_promoted(self):
        rows={r['id']:r for r in self.report['ocl_rules']}
        for identity in [body for body in self.expected if body.startswith('if ')]+['rejected-'+str(i) for i in range(len(self.rejected))]:
            row=rows[identity];self.assertEqual('unmapped-or-parse-failed',row['parse_status'],row);self.assertEqual(0,row['applicable'])
            self.assertFalse(row['literal_ast_adapter']);self.assertEqual([],row['evaluation_outcomes'])
        self.assertFalse(self.report['official_full_conformance'])

@unittest.skipUnless(NATIVE,'set the existing local JAVA_HOME for actual native OCL')
class ActualMultiplicityScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data,cls.expected=multiplicity_boundary_fixture()
        source=etree.parse(str(ROOT/'standards/sources/uml-2.5.1/UML.xmi'))
        body=lambda identity:next(r.findtext('specification/body') for r in source.iter('ownedRule') if r.get('{'+XMI+'}id')==identity)
        cls.probes=[{'context':'Property','id':'standard-precondition','body':body('MultiplicityElement-isMultivalued-pre')},
            {'context':'Property','id':'standard-body-condition','body':'let result : Boolean = self.isMultivalued() in '+body('MultiplicityElement-isMultivalued-spec')},
            {'context':'Property','id':'derived-lower-body-condition','body':'let result : Integer = self.lower in '+body('MultiplicityElement-lower.1-spec')},
            {'context':'Property','id':'derived-upper-body-condition','body':'let result : UnlimitedNatural = self.upper in '+body('MultiplicityElement-upper.1-spec')}]
        for field,number in [('lower',0),('upper',1)]:
            conditions=['(self.name = \''+identity+'\' implies self.'+field+' = '+str(values[number])+')' for identity,values in cls.expected.items()]
            cls.probes.append({'context':'Property','id':'xml-'+field+'-oracle','body':' and '.join(conditions)})
        cls.report=query_report(cls.data,cls.probes)
    def test_selected_native_precondition_body_condition_and_derived_feature_cases_execute(self):
        self.assertEqual(len(self.probes),self.report['ocl_parsed']);self.assertEqual(0,self.report['ocl_unmapped'])
        for row in self.report['ocl_rules']:
            self.assertEqual(4,row['applicable']);self.assertEqual(4,row['true_evaluations'],row)
            self.assertEqual([],row['invalid_ids']);self.assertEqual([],row['violation_ids'])
        self.assertFalse(self.report['official_full_conformance'])

if __name__=='__main__':unittest.main()
