"""Independent mapped UML fixtures; no claim of full UML language coverage."""
import os,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from uml_backend import official_rules,validate_mapped
from standards import Incomplete
GOOD=b'<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:id="M" name="Ops"><packagedElement xmi:type="uml:Class" xmi:id="C1" name="Order"/><packagedElement xmi:type="uml:Class" xmi:id="C2" name="Dispatch"/></uml:Model>'

class NormativeRuleExtractionTests(unittest.TestCase):
    def test_every_declared_class_invariant_has_context_id_and_body(self):
        rows,digest=official_rules();self.assertEqual(len(rows),425);self.assertEqual(len(set(r['id'] for r in rows)),425);self.assertEqual(len(digest),64);self.assertTrue(all(r['context'] and r['body'] for r in rows))
    def test_external_resources_rejected_before_backend_load(self):
        xml=GOOD.replace(b'</uml:Model>',b'<type href="https://example.com/remote.xmi#C"/></uml:Model>')
        with self.assertRaisesRegex(Incomplete,'external href'):validate_mapped(xml)

@unittest.skipUnless(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME',''))/'bin/java').is_file(),'set isolated JAVA_HOME to execute actual UML2/OCL backend')
class ActualUMLBackendTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.good=validate_mapped(GOOD);cls.bad=validate_mapped(GOOD.replace(b'name="Dispatch"',b'name="Order"'))
    def test_mapped_backend_actually_loads_objects(self):self.assertEqual(self.good['loaded_objects'],3);self.assertEqual(self.good['diagnostics'],[])
    def test_normative_invariants_are_parsed_and_individually_reported(self):
        self.assertEqual(len(self.good['ocl_rules']),425);self.assertGreater(self.good['ocl_parsed'],300);self.assertEqual(self.good['ocl_parsed']+self.good['ocl_unmapped'],425);self.assertGreater(self.good['ocl_evaluations'],0)
    def test_duplicate_names_detected_by_independent_ocl_invariant(self):
        good=next(r for r in self.good['ocl_rules'] if r['id']=='Namespace-members_distinguishable');self.assertEqual(good['violations'],0);self.assertEqual(good['invalid_evaluations'],0)
        row=next(r for r in self.bad['ocl_rules'] if r['id']=='Namespace-members_distinguishable');self.assertEqual(row['violations'],1);self.assertEqual(row['violation_ids'],['M']);self.assertTrue(self.bad['diagnostics'])
    def test_library_load_does_not_certify_full_language(self):self.assertFalse(self.good['official_full_conformance']);self.assertEqual(self.good['conformance_status'],'incomplete');self.assertEqual('typed OCL 2.4 Boolean operation adapter; full-language equivalence not certified',self.good['value_semantics']['boolean_null_operation_equivalence']);self.assertFalse(self.good['boolean_operation_adapter']['official_full_conformance'])
    def test_original_namespace_and_byte_authority_preserved(self):
        self.assertTrue(self.good['original_bytes_preserved']);self.assertEqual(self.good['namespace_mapping']['http://www.omg.org/spec/UML/20131001'],'http://www.eclipse.org/uml2/5.0.0/UML');self.assertNotEqual(self.good['original_sha256'],self.good['mapped_sha256'])
    def test_normative_multiplicity_query_adapter_detects_pin_boundary(self):
        source=b'<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:id="M"><packagedElement xmi:type="uml:Activity" xmi:id="A"><node xmi:type="uml:ValueSpecificationAction" xmi:id="V"><value xmi:type="uml:LiteralInteger" xmi:id="L" value="1"/><result xmi:type="uml:OutputPin" xmi:id="P"><lowerValue xmi:type="uml:LiteralInteger" xmi:id="LOW" value="1"/><upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="UP" value="1"/></result></node></packagedElement></uml:Model>'
        positive=validate_mapped(source);negative=validate_mapped(source.replace(b'xmi:id="UP" value="1"',b'xmi:id="UP" value="2"'))
        good=next(r for r in positive['ocl_rules'] if r['id']=='ValueSpecificationAction-multiplicity')
        bad=next(r for r in negative['ocl_rules'] if r['id']=='ValueSpecificationAction-multiplicity')
        self.assertEqual(good['parse_status'],'parsed');self.assertEqual(good['applicable'],1)
        self.assertEqual(good['invalid_evaluations'],0);self.assertEqual(good['violations'],0)
        self.assertEqual(bad['violations'],1);self.assertEqual(bad['violation_ids'],['V'])
        self.assertTrue(positive['query_adapters'][0]['original_body'].startswith('result = '))
if __name__=='__main__':unittest.main()
