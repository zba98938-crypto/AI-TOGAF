"""Native UMLDI geometry, ordering, notation and actual local raster evidence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from lxml import etree

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import Invalid,Incomplete,safe_xml,make_package,package_bytes,sha
from uml_di_render import diagram_plan,svg_diagram,render_native,has_native_di
from uml_di_fixtures import HEAD,MODEL,DI,document,framed_document


class UmlNativeDiRenderTests(unittest.TestCase):
    def test_native_decimal_bounds_routes_and_compartment_order_are_unchanged(self):
        data=document();before=bytes(data);plan=diagram_plan(data);svg,geometry=svg_diagram(plan)
        self.assertEqual(before,data)
        self.assertFalse(plan['derived_layout'])
        self.assertEqual({'x':'20.5000','y':'30.25','width':'240','height':'240'},geometry['native_bounds']['S_ORDER'])
        self.assertEqual([{'x':'260.5000','y':'60.25'},{'x':'355.7500','y':'60.25'},{'x':'450.25','y':'60.25'}],geometry['native_waypoints']['E_GENERAL'])
        self.assertEqual(['C_ATTR','C_OP'],geometry['ordered_compartments'][0]['compartment_ids'])
        root=etree.fromstring(svg.encode())
        rect=root.xpath('//*[@data-native-id="S_ORDER"]/s:rect',namespaces={'s':'http://www.w3.org/2000/svg'})[0]
        self.assertEqual('20.5000',rect.get('x'))
        points=root.xpath('//*[@data-native-id="E_GENERAL"]/s:polyline',namespaces={'s':'http://www.w3.org/2000/svg'})[0]
        self.assertEqual('260.5000,60.25 355.7500,60.25 450.25,60.25',points.get('points'))
        package=make_package(data,'uml','2.5.1')
        self.assertEqual(data,package_bytes(package,'uml','2.5.1'))

    def test_source_compartment_reordering_preserves_geometry_and_render_order(self):
        tree=safe_xml(document());shape=tree.xpath('//*[@xmi:id="S_ORDER"]',namespaces={'xmi':'http://www.omg.org/spec/XMI/20131001'})[0]
        compartments=shape.findall('compartment');shape.remove(compartments[1]);shape.insert(list(shape).index(compartments[0]),compartments[1])
        raw=etree.tostring(tree);plan=diagram_plan(raw);svg,geometry=svg_diagram(plan)
        self.assertEqual(['C_OP','C_ATTR'],geometry['ordered_compartments'][0]['compartment_ids'])
        self.assertEqual('164.500',geometry['native_bounds']['L_OP']['y'])
        self.assertLess(svg.index('data-native-id="C_OP"'),svg.index('data-native-id="C_ATTR"'))
        self.assertEqual(raw,etree.tostring(tree))

    def test_explicit_frame_heading_and_abstract_notation_are_rendered(self):
        svg,geometry=svg_diagram(diagram_plan(framed_document()))
        root=etree.fromstring(svg.encode());ns={'s':'http://www.w3.org/2000/svg'}
        self.assertEqual('680',root.xpath('//*[@data-native-id="D"]/s:rect',namespaces=ns)[0].get('width'))
        self.assertEqual('class Native view',root.xpath('//*[@data-native-id="H"]/s:text',namespaces=ns)[0].text)
        self.assertEqual('italic',root.xpath('//*[@data-native-id="L_ENTITY"]/s:text',namespaces=ns)[0].get('font-style'))
        self.assertEqual(2,sum('compartment_id' in d for d in geometry['derived_decorations']))
        self.assertEqual(1,len(root.xpath('//*[@data-derived-decoration="heading-border"]')))
        self.assertIn('skewX(-12)',svg)

    def test_generalization_hollow_arrow_and_ordinary_association_no_arrow(self):
        svg,_=svg_diagram(diagram_plan(document()));root=etree.fromstring(svg.encode());ns={'s':'http://www.w3.org/2000/svg'}
        self.assertEqual('url(#native-generalization)',root.xpath('//*[@data-native-id="E_GENERAL"]/s:polyline',namespaces=ns)[0].get('marker-end'))
        self.assertIsNone(root.xpath('//*[@data-native-id="E_ASSOC"]/s:polyline',namespaces=ns)[0].get('marker-end'))
        self.assertEqual('white',root.xpath('//s:marker[@id="native-generalization"]/s:path',namespaces=ns)[0].get('fill'))
        self.assertIn('0..*',svg)

    def test_source_resolution_maps_font_points_to_native_user_units(self):
        plan=diagram_plan(document());svg,_=svg_diagram(plan)
        root=etree.fromstring(svg.encode());ns={'s':'http://www.w3.org/2000/svg'}
        label=root.xpath('//*[@data-native-id="L_ORDER"]/s:text',namespaces=ns)[0]
        self.assertEqual(16,float(label.get('font-size')))
        with self.assertRaisesRegex(Incomplete,'bounds are too small'):
            diagram_plan(document(diagram=DI.replace('resolution="96"','resolution="300"')))

    def test_missing_bounds_waypoints_or_class_name_label_do_not_generate_layout(self):
        for raw,reason in ((document(diagram=DI.replace('<bounds xmi:type="dc:Bounds" x="20.5000" y="30.25" width="240" height="240"/>','')),'native bounds'),
                           (document(diagram=DI.replace('<waypoint xmi:type="dc:Point" x="355.7500" y="60.25"/>','').replace('<waypoint xmi:type="dc:Point" x="450.25" y="60.25"/>','')),'waypoints'),
                           (document(diagram=DI.replace('text="Order"','text="Missing title"')),'Class name label')):
            with self.subTest(reason=reason):
                with self.assertRaisesRegex(Incomplete,reason): diagram_plan(raw)

    def test_semantic_endpoint_mismatch_is_invalid_before_drawing(self):
        self.assertTrue(has_native_di(document()))
        for raw in (document(diagram=DI.replace('target="S_ENTITY"','target="S_LINE"')),
                    document(diagram=DI.replace('target="S_LINE"','target="S_ENTITY"'))):
            with self.assertRaisesRegex(Invalid,'endpoints disagree'): diagram_plan(raw)

    def test_unsupported_diagram_classifier_icons_and_notation_are_explicit(self):
        for raw in (document(diagram=DI.replace('UMLClassDiagram','UMLComponentDiagram')),
                    document(MODEL.replace('xmi:id="LINE" name="OrderLine"','xmi:id="LINE" name="OrderLine"').replace('xmi:type="u:Class" xmi:id="LINE"','xmi:type="u:Interface" xmi:id="LINE"')),
                    document(diagram=DI.replace('xmi:id="S_ORDER"','xmi:id="S_ORDER" isIcon="true"')),
                    document(diagram=DI.replace('isFrame="false"','isFrame="false" isAssociationDotShown="true"')),
                    document(diagram=DI.replace('isFrame="false"','isFrame="false" isIso="false"')),
                    document(diagram=DI.replace('isFrame="false"','isFrame="false" isInheritedLighter="true"')),
                    document(MODEL.replace('association="REL"/>','association="REL" aggregation="composite"/>')),
                    document(MODEL.replace('memberEnd="END_ORDER END_LINE"','memberEnd="END_ORDER END_LINE" isDerived="true"'))):
            with self.subTest(raw=raw[-40:]):
                with self.assertRaises(Incomplete): diagram_plan(raw)

    def test_unknown_di_fields_font_names_and_too_small_labels_are_refused(self):
        for raw in (document(diagram=DI.replace('xmi:id="S_ORDER"','xmi:id="S_ORDER" invented="true"')),
                    document(MODEL.replace('fontSize="12"','fontSize="12" fontName="Uninstalled"')),
                    document(diagram=DI.replace('width="200" height="24"','width="1" height="24"'))):
            with self.assertRaises(Incomplete): diagram_plan(raw)

    def test_local_and_nested_model_ref_encodings_render_same_native_geometry(self):
        direct=diagram_plan(document())
        nested=document(diagram=DI.replace('modelElement="ORDER" sharedStyle="STYLE">','sharedStyle="STYLE"><modelElement xmi:idref="ORDER"/>',1))
        plan=diagram_plan(nested)
        self.assertEqual(direct['native_bounds'],plan['native_bounds'])
        self.assertEqual(direct['native_waypoints'],plan['native_waypoints'])

    def test_nested_semantic_scalars_and_explicit_specific_are_resolved_once(self):
        nested=MODEL.replace('xmi:id="ORDER" name="Order">','xmi:id="ORDER"><name>Order</name>')
        nested=nested.replace('xmi:id="GENERAL" general="ENTITY"/>','xmi:id="GENERAL" general="ENTITY"><specific xmi:idref="ORDER"/></generalization>')
        self.assertEqual(diagram_plan(document())['native_bounds'],diagram_plan(document(nested))['native_bounds'])
        nested=MODEL.replace('association="REL"/>','association="REL"><aggregation value="composite"/></ownedEnd>')
        with self.assertRaisesRegex(Incomplete,'aggregation'): diagram_plan(document(nested))

    def test_multiplicity_mismatch_and_unrepresented_di_elements_are_refused(self):
        with self.assertRaisesRegex(Invalid,'multiplicity label disagrees'):
            diagram_plan(document(diagram=DI.replace('text="0..*"','text="1"')))
        orphan='<ud:UMLLabel xmi:id="ORPHAN" text="Hidden"/>'
        with self.assertRaisesRegex(Incomplete,'outside supported containment'):
            diagram_plan(document(MODEL+orphan))

    def test_active_class_double_sides_use_native_rectangle_edges(self):
        model=MODEL.replace('name="Order"','name="Order" isActive="true"')
        diagram=DI.replace('xmi:id="S_ORDER"','xmi:id="S_ORDER" isDoubleSided="true"')
        svg,_=svg_diagram(diagram_plan(document(model,diagram)))
        root=etree.fromstring(svg.encode());ns={'s':'http://www.w3.org/2000/svg'}
        sides=root.xpath('//*[@data-native-id="S_ORDER"]/s:path',namespaces=ns)
        self.assertEqual('M24.5,30.25 V270.25 M256.5,30.25 V270.25',sides[0].get('d'))

    def test_duplicate_compartment_and_outside_compartment_geometry_are_refused(self):
        repeated=DI.replace('xmi:id="S_ORDER"','xmi:id="S_ORDER" compartment="C_ATTR C_ATTR"')
        with self.assertRaisesRegex(Incomplete,'Repeated or cyclic'):
            diagram_plan(document(diagram=repeated))
        outside=DI.replace('y="102.50"','y="999.50"')
        with self.assertRaisesRegex(Incomplete,'outside its ClassifierShape'):
            svg_diagram(diagram_plan(document(diagram=outside)))

    def test_degenerate_native_edge_is_refused_without_derived_route(self):
        diagram=DI.replace('x="355.7500" y="60.25"','x="260.5000" y="60.25"').replace('x="450.25" y="60.25"','x="260.5000" y="60.25"')
        with self.assertRaisesRegex(Incomplete,'distinct waypoints'):
            diagram_plan(document(diagram=diagram))

    def test_public_cli_actual_svg_png_and_native_source_are_bound(self):
        with tempfile.TemporaryDirectory(prefix='native-di-cli-') as tmp:
            folder=Path(tmp);source=folder/'source.uml';data=framed_document().replace(b'class Native view','class \u8ba2\u5355\u7c7b\u56fe'.encode())
            source.write_bytes(data)
            run=subprocess.run([sys.executable,'-B',str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts/standards.py'),
                'render','--language','uml','--version','2.5.1','--input',str(source),'--out',str(folder/'view.svg')],capture_output=True,text=True,timeout=120)
            self.assertEqual(0,run.returncode,run.stdout+run.stderr)
            report=json.loads(run.stdout)
            self.assertEqual('native UMLDI coordinates preserved',report['layout_status'])
            self.assertFalse(report['derived_layout']);self.assertFalse(report['full_language_acceptance'])
            self.assertEqual('incomplete',report['conformance_status'])
            self.assertEqual(data,(folder/'view.native.uml').read_bytes())
            self.assertEqual(sha(data),report['source_sha256'])
            self.assertEqual(b'\x89PNG\r\n\x1a\n',(folder/'view.png').read_bytes()[:8])

    def test_actual_native_raster_does_not_overwrite_prior_artifacts(self):
        with tempfile.TemporaryDirectory(prefix='native-di-render-') as tmp:
            folder=Path(tmp);data=document();report=render_native(data,folder/'view.svg')
            before={p.name:p.read_bytes() for p in folder.iterdir()}
            with self.assertRaisesRegex(Invalid,'overwrite'): render_native(data,folder/'view.svg')
            self.assertEqual(before,{p.name:p.read_bytes() for p in folder.iterdir()})
            self.assertEqual(data,(folder/'view.native.uml').read_bytes())
            self.assertEqual(sha((folder/'view.svg').read_bytes()),report['svg_sha256'])
            self.assertEqual(sha((folder/'view.png').read_bytes()),report['png_sha256'])


if __name__=='__main__': unittest.main()
