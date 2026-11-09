"""Native UML class notation with independent unsupported-construct mutations."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import Invalid,Incomplete,safe_xml
from uml_render import diagram_model,svg_diagram

UML='''<?xml version="1.0" encoding="utf-8"?>
<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:version="2.5.1" xmi:id="MODEL" name="订单领域模型">
 <packagedElement xmi:type="uml:PrimitiveType" xmi:id="INTEGER" name="Integer"/>
 <packagedElement xmi:type="uml:PrimitiveType" xmi:id="STRING" name="String"/>
 <packagedElement xmi:type="uml:Package" xmi:id="DOMAIN" name="订单域">
  <packagedElement xmi:type="uml:Class" xmi:id="ENTITY" name="Entity" isAbstract="true"><ownedAttribute xmi:id="ENTITY_ID" name="id" visibility="protected" type="STRING" isReadOnly="true"/></packagedElement>
  <packagedElement xmi:type="uml:Class" xmi:id="ORDER" name="Order">
   <ownedAttribute xmi:id="ORDER_STATUS" name="status" visibility="private" type="STRING"/>
   <ownedAttribute xmi:id="ORDER_TOTAL" name="total" visibility="private" type="INTEGER"/>
   <ownedOperation xmi:id="ORDER_CREATE" name="create" visibility="public" isStatic="true"><ownedParameter xmi:id="ORDER_CREATE_QTY" name="quantity" direction="in" type="INTEGER"/><ownedParameter xmi:id="ORDER_CREATE_RESULT" direction="return" type="ORDER"/></ownedOperation>
   <generalization xmi:id="ORDER_IS_ENTITY" general="ENTITY"/>
  </packagedElement>
  <packagedElement xmi:type="uml:Class" xmi:id="LINE" name="OrderLine"><ownedAttribute xmi:id="LINE_QTY" name="quantity" visibility="private" type="INTEGER"/><generalization xmi:id="LINE_IS_ENTITY" general="ENTITY"/></packagedElement>
  <packagedElement xmi:type="uml:Association" xmi:id="ORDER_LINES" name="包含明细" memberEnd="END_ORDER END_LINE">
   <ownedEnd xmi:id="END_ORDER" name="order" type="ORDER" association="ORDER_LINES" aggregation="none"><lowerValue xmi:type="uml:LiteralInteger" xmi:id="END_ORDER_LOWER" value="1"/><upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="END_ORDER_UPPER" value="1"/></ownedEnd>
   <ownedEnd xmi:id="END_LINE" name="lines" type="LINE" association="ORDER_LINES" aggregation="none"><lowerValue xmi:type="uml:LiteralInteger" xmi:id="END_LINE_LOWER" value="0"/><upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="END_LINE_UPPER" value="*"/></ownedEnd>
  </packagedElement>
 </packagedElement>
</uml:Model>'''.encode('utf-8')


class UmlNotationTests(unittest.TestCase):
    def test_class_features_operations_and_explicit_association_bounds(self):
        model=diagram_model(UML)
        self.assertEqual(5,len(model['classifiers']))
        self.assertEqual(3,len(model['relations']))
        classes={c['id']:c for c in model['classifiers']}
        self.assertTrue(classes['ENTITY']['abstract'])
        self.assertEqual('1',classes['ENTITY']['attributes'][0]['effective_multiplicity'])
        self.assertFalse(classes['ENTITY']['attributes'][0]['multiplicity_explicit'])
        self.assertEqual('+create(in quantity : Integer) : Order',classes['ORDER']['operations'][0]['text'])
        relation=next(r for r in model['relations'] if r['kind']=='association')
        self.assertEqual(['1','0..*'],[e['multiplicity'] for e in relation['ends']])

    def test_compartments_hollow_triangle_and_undirected_association(self):
        svg,layout=svg_diagram(diagram_model(UML));root=etree.fromstring(svg.encode())
        self.assertEqual(5,len(root.xpath('//*[@class="uml-classifier"]')))
        self.assertEqual(2,len(root.xpath('//*[@class="uml-generalization"]/*[@marker-end="url(#uml-generalization)"]')))
        self.assertEqual([],root.xpath('//*[@class="uml-association"]/*[@marker-end]'))
        self.assertIn('text-decoration:underline',svg)
        self.assertIn('data-parameter-native-ids="ORDER_CREATE_QTY ORDER_CREATE_RESULT"',svg)
        self.assertIn('skewX(-12)',svg)
        for label in layout['relation_end_labels']:
            box=layout['classifiers'][label['type_id']]
            self.assertFalse(box['x']<=label['x']<=box['x']+box['width'] and box['y']<=label['y']<=box['y']+box['height'])

    def test_unsupported_classifier_is_blocked(self):
        with self.assertRaisesRegex(Incomplete,'Unsupported native UML classifier'):
            diagram_model(UML.replace(b'uml:Class" xmi:id="LINE"',b'uml:Interface" xmi:id="LINE"'))

    def test_aggregation_and_navigability_are_blocked(self):
        for raw in (UML.replace(b'aggregation="none"',b'aggregation="composite"'),UML.replace('name="包含明细"'.encode('utf-8'),b'name="contains" navigableOwnedEnd="END_LINE"')):
            with self.subTest(raw=raw[-40:]):
                with self.assertRaises(Incomplete):diagram_model(raw)

    def test_unresolved_and_external_type_is_blocked(self):
        with self.assertRaisesRegex(Incomplete,'Unresolved'):
            diagram_model(UML.replace(b'type="INTEGER"',b'type="MISSING"'))
        raw=UML.replace(b'name="status" visibility="private" type="STRING"/>',b'name="status" visibility="private"><type href="https://example.invalid/types.uml#String"/></ownedAttribute>')
        with self.assertRaises(Incomplete):diagram_model(raw)

    def test_local_xmi_type_reference_is_resolved(self):
        raw=UML.replace(b'name="status" visibility="private" type="STRING"/>',b'name="status" visibility="private"><type xmi:idref="STRING"/></ownedAttribute>')
        model=diagram_model(raw)
        self.assertEqual('STRING',next(c for c in model['classifiers'] if c['id']=='ORDER')['attributes'][0]['type_id'])

    def test_missing_and_inverted_multiplicity_are_refused(self):
        root=safe_xml(UML);end=root.xpath('//*[@xmi:id="END_LINE"]',namespaces={'xmi':'http://www.omg.org/spec/XMI/20131001'})[0];end.remove(end.find('upperValue'))
        with self.assertRaisesRegex(Incomplete,'Both lowerValue'):diagram_model(etree.tostring(root))
        with self.assertRaisesRegex(Invalid,'Inverted'):
            diagram_model(UML.replace(b'id="END_ORDER_UPPER" value="1"',b'id="END_ORDER_UPPER" value="0"'))

    def test_generalization_cycle_is_invalid(self):
        raw=UML.replace(b'<ownedAttribute xmi:id="ENTITY_ID"',b'<generalization xmi:id="CYCLE" general="ORDER"/><ownedAttribute xmi:id="ENTITY_ID"')
        with self.assertRaisesRegex(Invalid,'Cyclic'):diagram_model(raw)

    def test_public_cli_renders_real_svg_png_and_discloses_generated_layout(self):
        with tempfile.TemporaryDirectory(prefix='native-uml-test-') as tmp:
            folder=Path(tmp);source=folder/'source.uml';source.write_bytes(UML)
            argv=[sys.executable,'-B',str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts/standards.py'),'render','--language','uml','--version','2.5.1','--input',str(source),'--out',str(folder/'diagram.svg')]
            run=subprocess.run(argv,capture_output=True,text=True,timeout=120)
            self.assertEqual(0,run.returncode,run.stdout+run.stderr)
            report=json.loads(run.stdout)
            self.assertEqual('layout generated; UMLDI not preserved',report['layout_status'])
            self.assertEqual('incomplete',report['conformance_status'])
            self.assertFalse(report['full_language_acceptance'])
            self.assertEqual(b'\x89PNG\r\n\x1a\n',(folder/'diagram.png').read_bytes()[:8])
            self.assertTrue((folder/'diagram.render.json').is_file())
            source.write_bytes(UML.replace(b'aggregation="none"',b'aggregation="shared"'))
            argv[-1]=str(folder/'rejected.svg');run=subprocess.run(argv,capture_output=True,text=True,timeout=30)
            self.assertEqual(3,run.returncode,run.stdout+run.stderr)
            self.assertEqual('blocked',json.loads(run.stdout)['status'])
            self.assertFalse((folder/'rejected.svg').exists())


if __name__=='__main__':unittest.main()
