"""Independent primitive, multiplicity and UMLDI invariant counterexamples."""
from pathlib import Path
import sys
import unittest
from lxml import etree

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import check_native,safe_xml
from uml_design_semantics import source_schema
from uml_di_fixtures import HEAD,MODEL,DI,document,framed_document


class UmlNativeConstraintTests(unittest.TestCase):
    def check(self,data): return check_native(data,'uml','2.5.1')
    def assert_rule(self,data,rule):
        result=self.check(data)
        self.assertTrue(any(rule in error for error in result['errors']),result['errors'])
        self.assertEqual('invalid',result['conformance_status'])
        return result

    def test_source_defaults_multiplicity_and_primitive_provenance(self):
        schema=source_schema()
        self.assertEqual((0,1),(schema[('UML.xmi','Property')]['features']['type']['lower'],schema[('UML.xmi','Property')]['features']['type']['upper']))
        self.assertEqual('true',schema[('UMLDI.xmi','UMLClassDiagram')]['features']['isFrame']['default'])
        self.assertEqual('oneWay',schema[('UMLDI.xmi','UMLClassDiagram')]['features']['navigabilityNotation']['default'])
        self.assertEqual(('PrimitiveTypes.xmi','Boolean'),schema[('UML.xmi','Class')]['features']['isAbstract']['type'])
        self.assertEqual([],self.check(document())['errors'])
        self.assertEqual([],self.check(framed_document())['errors'])

    def test_boolean_and_enumeration_values_accept_xsd_aliases_without_rewriting(self):
        for value in ('true','false','1','0','  true  '):
            data=document(MODEL.replace('isAbstract="true"','isAbstract="'+value+'"'))
            before=bytes(data);report=self.check(data)
            self.assertEqual([],report['errors'])
            self.assertEqual(before,data)
            self.assertTrue(any(r['raw_value']==value for r in report['design_time_semantics']['checked_primitive_values']))
        for value in ('public','private','protected','package'):
            self.assertEqual([],self.check(document(MODEL.replace('name="Order"','name="Order" visibility="'+value+'"')))['errors'])

    def test_invalid_boolean_and_unknown_enum_are_errors(self):
        for value in ('banana','TRUE','False','','2'):
            self.assert_rule(document(MODEL.replace('isAbstract="true"','isAbstract="'+value+'"')),'UML-primitive-or-enumeration-value')
        self.assert_rule(document(MODEL.replace('name="Order"','name="Order" visibility="invented"')),'UML-primitive-or-enumeration-value')

    def test_direct_nested_and_mixed_type_references_obey_upper_one(self):
        nested=MODEL.replace('name="status" type="STRING"/>','name="status"><type xmi:idref="STRING"/></ownedAttribute>')
        self.assertEqual([],self.check(document(nested))['errors'])
        for model in (MODEL.replace('type="STRING"','type="STRING ORDER"'),
                      nested.replace('<type xmi:idref="STRING"/>','<type xmi:idref="STRING"/><type xmi:idref="ORDER"/>'),
                      MODEL.replace('name="status" type="STRING"/>','name="status" type="STRING"><type xmi:idref="STRING"/></ownedAttribute>')):
            self.assert_rule(document(model),'UML-property-upper-multiplicity')

    def test_classifier_and_edge_required_reference_cardinality(self):
        for diagram in (DI.replace('modelElement="ORDER" sharedStyle','modelElement="ORDER LINE" sharedStyle',1),
                        DI.replace('modelElement="ORDER" sharedStyle','sharedStyle',1),
                        DI.replace('source="S_ORDER" target="S_ENTITY"','target="S_ENTITY"'),
                        DI.replace('target="S_ENTITY"','target="S_ENTITY S_LINE"')):
            report=self.check(document(diagram=diagram))
            self.assertTrue(any('multiplicity' in error for error in report['errors']),report['errors'])
        diagram=DI.replace('modelElement="ORDER" sharedStyle="STYLE">','sharedStyle="STYLE"><modelElement xmi:idref="ORDER"/>',1)
        self.assertEqual([],self.check(document(diagram=diagram))['errors'])

    def test_default_frame_heading_and_explicit_frame_counterexamples(self):
        self.assert_rule(document(diagram=DI.replace(' isFrame="false"','')),'UMLDiagram-no-frame-no-heading')
        self.assert_rule(document(diagram=DI.replace('isFrame="false"','isFrame="true"')),'UMLDiagram-no-frame-no-heading')
        self.assert_rule(framed_document().replace(b'isFrame="true"',b'isFrame="false"'),'UMLDiagram-no-frame-no-heading')
        self.assertEqual([],self.check(framed_document().replace(b'isFrame="true"',b'isFrame="1"'))['errors'])

    def test_heading_model_element_and_heading_upper_bound(self):
        data=framed_document()
        self.assert_rule(data.replace(b'xmi:id="H" text=',b'xmi:id="H" modelElement="ORDER" text='),'UMLDiagram-heading_modelElement')
        self.assert_rule(data.replace(b'heading="H"',b'heading="H L_ORDER"'),'UML-property-upper-multiplicity')

    def test_label_model_element_cardinality_and_icon_invariant(self):
        self.assert_rule(document(diagram=DI.replace('xmi:id="L_ORDER" modelElement="ORDER"','xmi:id="L_ORDER" modelElement="ORDER ENTITY"')),'UMLLabel-modelElement_mult')
        self.assert_rule(document(diagram=DI.replace('xmi:id="L_ORDER"','xmi:id="L_ORDER" isIcon="true"')),'UMLLabel-no_icon')
        self.assertEqual([],self.check(document(diagram=DI.replace('xmi:id="L_ORDER"','xmi:id="L_ORDER" isIcon="0"')))['errors'])

    def test_compartment_has_no_model_element(self):
        self.assert_rule(document(diagram=DI.replace('xmi:id="C_ATTR"','xmi:id="C_ATTR" modelElement="STATUS"')),'UMLCompartment-no_modelElement')
        self.assertEqual([],self.check(document())['errors'])

    def test_double_sided_shape_requires_an_active_class(self):
        diagram=DI.replace('xmi:id="S_ORDER"','xmi:id="S_ORDER" isDoubleSided="true"')
        self.assert_rule(document(diagram=diagram),'UMLClassifierShape-doubleSided_isActive')
        model=MODEL.replace('name="Order"','name="Order" isActive="true"')
        self.assertEqual([],self.check(document(model,diagram))['errors'])
        self.assert_rule(document(model.replace('isActive="true"','isActive="false"'),diagram),'UMLClassifierShape-doubleSided_isActive')

    def test_explicit_font_size_positive_and_absent_null_adjudication_are_distinct(self):
        for value in ('0','-1','nan','Infinity','not-real'):
            self.assert_rule(document(MODEL.replace('fontSize="12"','fontSize="'+value+'"')),'UMLStyle-fontsize_positive')
        missing=document(MODEL.replace(' fontSize="12"',''))
        report=self.check(missing)
        self.assertEqual([],report['errors'])
        self.assertTrue(any('null/applicability' in msg for msg in report['diagnostic_groups']['capability_uncovered']))
        self.assertEqual('incomplete',report['conformance_status'])

    def test_explicit_rgb_integer_range_and_missing_component_are_separate(self):
        for red in ('0','255','+128'):
            model=MODEL+'<dc:Color xmi:id="COLOR" red="'+red+'" green="0" blue="255"/>'
            self.assertEqual([],self.check(document(model))['errors'])
        for red in ('-1','256','1.5','banana'):
            model=MODEL+'<dc:Color xmi:id="COLOR" red="'+red+'" green="0" blue="255"/>'
            self.assert_rule(document(model),'Color-valid_rgb')
        missing=self.check(document(MODEL+'<dc:Color xmi:id="COLOR" red="0" green="255"/>'))
        self.assertEqual([],missing['errors'])
        self.assertTrue(any('missing explicit RGB' in b for b in missing['blockers']))


if __name__=='__main__': unittest.main()
