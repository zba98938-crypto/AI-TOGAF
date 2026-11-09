"""Independent native UML references and unchanged UMLDI geometry fixtures."""
import base64
from pathlib import Path
import sys
import unittest
from lxml import etree

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import check_native, make_package, package_bytes
from uml_design_semantics import source_schema

XMI = 'http://www.omg.org/spec/XMI/20131001'
HEAD = '''<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001"
 xmlns:u="http://www.omg.org/spec/UML/20131001"
 xmlns:ud="http://www.omg.org/spec/UML/20161101/UMLDI"
 xmlns:dc="http://www.omg.org/spec/DD/20131001/DC">'''
MODEL = '''<u:Model xmi:id="M" name="Native">
 <packagedElement xmi:type="u:PrimitiveType" xmi:id="S" name="String"/>
 <packagedElement xmi:type="u:Class" xmi:id="A" name="A">
  <ownedAttribute xmi:id="P" name="p" type="S"/>
  <generalization xmi:id="G" general="B"/>
 </packagedElement>
 <packagedElement xmi:type="u:Class" xmi:id="B" name="B"/>
 <packagedElement xmi:type="u:Profile" xmi:id="PROFILE" name="LocalProfile"/>
 <profileApplication xmi:id="APPLIED" appliedProfile="PROFILE"/>
</u:Model>'''
DI = '''<ud:UMLClassDiagram xmi:id="D" name="Class view" isFrame="false">
 <ownedElement xmi:type="ud:UMLShape" xmi:id="SA" modelElement="A">
  <bounds xmi:type="dc:Bounds" xmi:id="RECT" x="-24.25" y="12.5" width="0" height="100"/>
 </ownedElement>
</ud:UMLClassDiagram>'''


def native(model=MODEL, diagram=''):
    return (HEAD+model+diagram+'</xmi:XMI>').encode()


class UmlDesignSemanticsTests(unittest.TestCase):
    def test_inherited_feature_types_local_profile_and_alias_prefix(self):
        report = check_native(native(), 'uml', '2.5.1')
        self.assertEqual([], report['errors'])
        checked = {(r['id'], r['field'], r['reference'], r['expected_type'])
                   for r in report['design_time_semantics']['checked_local_references']}
        self.assertTrue({('P','type','S','Type'), ('G','general','B','Classifier'),
                         ('APPLIED','appliedProfile','PROFILE','Profile')} <= checked)
        self.assertEqual('incomplete', report['conformance_status'])
        self.assertFalse(report['design_time_semantics']['full_design_time_conformance'])

    def test_dangling_and_wrong_typed_ids_are_distinct_errors(self):
        for old, new, rule in [('type="S"','type="MISSING"','UML-local-reference-exists'),
                               ('type="S"','type="G"','UML-local-reference-type'),
                               ('general="B"','general="P"','UML-local-reference-type'),
                               ('appliedProfile="PROFILE"','appliedProfile="A"','UML-local-reference-type')]:
            with self.subTest(new=new):
                report=check_native(native(MODEL.replace(old,new)),'uml','2.5.1')
                self.assertTrue(any(rule in error for error in report['errors']))
                self.assertEqual('invalid',report['conformance_status'])
        report=check_native(native(MODEL.replace('xmi:type="u:Class" xmi:id="B"','xmi:type="u:InventedClass" xmi:id="B"')),'uml','2.5.1')
        self.assertTrue(any('UML-metaclass-exists' in error for error in report['errors']))

    def test_nested_idref_encoding_also_checks_type(self):
        valid=MODEL.replace('name="p" type="S"/>','name="p"><type xmi:idref="S"/></ownedAttribute>')
        self.assertEqual([],check_native(native(valid),'uml','2.5.1')['errors'])
        invalid=valid.replace('<type xmi:idref="S"/>','<type xmi:idref="G"/>')
        self.assertTrue(any('UML-local-reference-type' in e for e in check_native(native(invalid),'uml','2.5.1')['errors']))

    def test_native_umldi_bounds_and_exchange_preserve_every_byte(self):
        data=native(diagram=DI)
        report=check_native(data,'uml','2.5.1')
        self.assertEqual([],report['errors'])
        self.assertEqual([],report['vendor_namespaces'])
        geometry=report['design_time_semantics']['native_geometry']
        self.assertEqual(1,len(geometry))
        self.assertEqual({'x':'-24.25','y':'12.5','width':'0','height':'100'},
                         {k:geometry[0]['native_values'][k] for k in ('x','y','width','height')})
        package=make_package(data,'uml','2.5.1')
        self.assertEqual(data,base64.b64decode(package['native_xml']))
        self.assertEqual(data,package_bytes(package,'uml','2.5.1'))

    def test_negative_nonreal_and_nonfinite_di_values_are_rejected(self):
        for old,new,rule in [('width="0"','width="-1"','UMLDI-non-negative-size'),
                             ('height="100"','height="nan"','UMLDI-finite-real-coordinate'),
                             ('x="-24.25"','x="Infinity"','UMLDI-finite-real-coordinate'),
                             ('y="12.5"','y="twelve"','UMLDI-finite-real-coordinate')]:
            with self.subTest(new=new):
                report=check_native(native(diagram=DI.replace(old,new)),'uml','2.5.1')
                self.assertTrue(any(rule in error for error in report['errors']))

    def test_missing_coordinate_remains_uncovered_without_layout(self):
        report=check_native(native(diagram=DI.replace(' height="100"','')),'uml','2.5.1')
        self.assertEqual([],report['errors'])
        self.assertTrue(any('no derived coordinate generated' in row
                            for row in report['diagnostic_groups']['capability_uncovered']))
        self.assertNotIn('height',report['design_time_semantics']['native_geometry'][0]['native_values'])

    def test_diagram_constraint_and_style_reference_have_independent_counterexamples(self):
        bad=DI.replace('name="Class view"','name="Class view" modelElement="M"')
        self.assertTrue(any('UMLClassDiagram-no_modelElement' in error
                            for error in check_native(native(diagram=bad),'uml','2.5.1')['errors']))
        bad=DI.replace('modelElement="A"','modelElement="A" sharedStyle="SA"')
        self.assertTrue(any('sharedStyle requires UMLStyle' in error
                            for error in check_native(native(diagram=bad),'uml','2.5.1')['errors']))
        bad=DI.replace('modelElement="A"','modelElement="RECT"')
        self.assertTrue(any('modelElement requires Element' in error
                            for error in check_native(native(diagram=bad),'uml','2.5.1')['errors']))

    def test_reference_definitions_are_derived_from_current_normative_metamodel(self):
        schema=source_schema()
        self.assertEqual(('UML.xmi','Type'),schema[('UML.xmi','Property')]['features']['type']['type'])
        self.assertEqual(('DC.xmi','Bounds'),schema[('UMLDI.xmi','UMLShape')]['features']['bounds']['type'])
        self.assertEqual('TypedElement-type',schema[('UML.xmi','Property')]['features']['type']['id'])


if __name__ == '__main__': unittest.main()
