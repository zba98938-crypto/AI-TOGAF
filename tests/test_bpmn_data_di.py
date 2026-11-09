"""Native partial DI, explicit endpoint and source geometry oracles."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import safe_xml,check_native,make_package,package_bytes,Incomplete,Invalid
from bpmn_render import diagram_plan,render_native
from bpmn_data_di_fixtures import data_di_model,boundary_di_model,remove_di,shape,edge,DI,DC
from bpmn_data_compensation_fixtures import by_id,change,element,association,MODEL


class BPMNDataDITests(unittest.TestCase):
    data=data_di_model()

    def test_native_activity_event_process_data_view_is_valid_and_explicit(self):
        self.assertEqual([],check_native(self.data,'bpmn','2.0.2')['errors'])
        plan=diagram_plan(self.data)
        self.assertEqual('native-data-di',plan['backend'])
        self.assertEqual(12,len(plan['shape_ids']));self.assertEqual(4,len(plan['edge_ids']))
        self.assertIn('CATCH_OUT',plan['shape_ids']);self.assertIn('THROW_IN',plan['shape_ids'])
        self.assertFalse(plan['auto_layout'])

    def test_collaboration_qnames_and_valid_pool_endpoint_context_are_preserved(self):
        def mutate(r):
            col=element(r,'collaboration',id='COLLAB')
            element(col,'participant',id='POOL',name='运营',processRef='tns:P')
            # RootElements precede DI; keep the native document schema-valid.
            r.remove(col);r.insert(4,col)
            plane=by_id(r,'PLANE');plane.set('bpmnElement','tns:COLLAB')
            shape(plane,'POOL','10.000','10.00','900.000','510.0',isHorizontal='true')
            by_id(r,'DIN_DI').set('targetElement','POOL_DI')
        data=change(self.data,mutate)
        self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
        plan=diagram_plan(data)
        self.assertEqual('COLLAB',plan['root_id']);self.assertIn('POOL',plan['shape_ids'])
        self.assertEqual('POOL_DI',plan['graphics'][0]['target_graphic_id'])

    def test_raw_coordinate_strings_and_source_plane_order_are_preserved(self):
        plan=diagram_plan(self.data);root=safe_xml(self.data)
        for g in plan['graphics']:
            source=by_id(root,g['graphic_id'])
            if g['kind']=='shape':
                self.assertEqual(dict(source.find('{'+DC+'}Bounds').attrib),g['bounds'])
            else:self.assertEqual([dict(c.attrib) for c in source if c.tag.endswith('waypoint')],g['waypoints'])
        self.assertEqual('DIN_DI',plan['graphics'][0]['graphic_id'])
        self.assertEqual('40.000',next(g for g in plan['graphics'] if g['semantic_id']=='PROC_IN0')['bounds']['x'])

    def test_data_endpoints_honor_forward_explicit_di_override(self):
        plan=diagram_plan(self.data);edges={g['semantic_id']:g for g in plan['graphics'] if g['kind']=='edge'}
        self.assertEqual('A_DI',edges['DIN']['target_graphic_id'])
        self.assertEqual('A_DI',edges['DOUT']['source_graphic_id'])
        self.assertEqual('CATCH_OUT_DI',edges['CATCH_ASSOC']['source_graphic_id'])

    def test_directly_depicted_data_endpoints_need_no_redundant_override(self):
        data=change(self.data,lambda r:by_id(r,'DIN_DI').attrib.pop('targetElement'))
        self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
        self.assertEqual('A_IN0_DI',diagram_plan(data)['graphics'][0]['target_graphic_id'])

    def test_explicit_di_override_cannot_impersonate_a_sibling_business_owner(self):
        bad=change(self.data,lambda r:by_id(r,'DIN_DI').set('targetElement','THROW_DI'))
        self.assertEqual([],check_native(bad,'bpmn','2.0.2')['errors'])
        with self.assertRaisesRegex(Invalid,'override conflicts'):diagram_plan(bad)
        bad=change(self.data,lambda r:by_id(r,'DOUT_DI').set('sourceElement','CATCH_DI'))
        with self.assertRaisesRegex(Invalid,'override conflicts'):diagram_plan(bad)

    def test_native_di_inference_is_plane_local_and_same_plane_ambiguity_is_rejected(self):
        def another_view(r):
            diagram=etree.SubElement(r,'{'+DI+'}BPMNDiagram',id='SECOND_VIEW')
            plane=etree.SubElement(diagram,'{'+DI+'}BPMNPlane',id='SECOND_PLANE',bpmnElement='P')
            shape(plane,'CATCH_OUT','600','600','36','50').set('id','SECOND_DATA')
        two=change(self.data,another_view)
        self.assertEqual([],check_native(two,'bpmn','2.0.2')['errors'])
        with self.assertRaisesRegex(Incomplete,'exactly one explicit'):diagram_plan(two)
        def ambiguous(r):shape(by_id(r,'PLANE'),'CATCH_OUT','600','600','36','50').set('id','DUPLICATE_DATA')
        bad=change(self.data,ambiguous)
        self.assertTrue(any('source is undepicted or ambiguous' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))
        with self.assertRaises(Invalid):diagram_plan(bad)

    def test_undepicted_model_data_endpoint_requires_explicit_override(self):
        partial=boundary_di_model()
        self.assertEqual(8,len(diagram_plan(partial)['shape_ids']))
        bad=change(partial,lambda r:by_id(r,'DIN_DI').attrib.pop('targetElement'))
        self.assertTrue(any('explicit targetElement' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))
        with self.assertRaisesRegex(Invalid,'explicit targetElement'):diagram_plan(bad)

    def test_omitting_optional_data_shapes_and_associations_does_not_fail_model_or_view(self):
        missing=remove_di(self.data,'PROC_IN0','PROC_OUT0','A_IN0','A_OUT0','CATCH_OUT','THROW_IN','DIN','DOUT','CATCH_ASSOC','THROW_ASSOC')
        self.assertEqual([],check_native(missing,'bpmn','2.0.2')['errors'])
        plan=diagram_plan(missing)
        self.assertEqual('native-data-di',plan['backend']);self.assertFalse(plan['edge_ids'])
        self.assertTrue(plan['data_depiction_inventory'])
        self.assertTrue(all(not row['depicted'] for row in plan['data_depiction_inventory']
                            if row['type'] not in {'dataObjectReference','dataStoreReference'}))
        self.assertFalse(check_native(missing,'bpmn','2.0.2').get('full_language_acceptance',False))
        without_refs=remove_di(missing,'DR','DSR')
        self.assertEqual([],check_native(without_refs,'bpmn','2.0.2')['errors'])
        self.assertEqual(4,len(diagram_plan(without_refs)['shape_ids']))
        self.assertTrue(all(not row['depicted'] for row in diagram_plan(without_refs)['data_depiction_inventory']))

    def test_optional_data_visibility_preserves_collapsed_subprocess_scope(self):
        plan=diagram_plan(self.data)
        self.assertTrue(any(row['id']=='INNER_ASSOC' for row in plan['hidden_native_elements']))
        def outside(r):
            plane=by_id(r,'PLANE');shape(plane,'INNER_IN0','700.00','310.00','36.00','50.00')
        bad=change(self.data,outside)
        with self.assertRaisesRegex(Incomplete,'outside the visible native scope'):diagram_plan(bad)

    def test_missing_required_activity_graphic_remains_a_material_error(self):
        with self.assertRaisesRegex(Incomplete,'Missing BPMNDI.*A'):diagram_plan(remove_di(self.data,'A','DIN','DOUT'))

    def test_explicit_override_cannot_select_a_graphic_from_another_di_view(self):
        def mutate(r):
            by_id(r,'DIN_DI').set('targetElement','OTHER_DI')
            diagram=etree.SubElement(r,'{'+DI+'}BPMNDiagram',id='OTHER_VIEW')
            plane=etree.SubElement(diagram,'{'+DI+'}BPMNPlane',id='OTHER_PLANE',bpmnElement='P')
            shape(plane,'A','0','0','130','90').set('id','OTHER_DI')
        with self.assertRaisesRegex(Incomplete,'exactly one explicit'):diagram_plan(change(self.data,mutate))

    def test_multiple_source_transformation_requires_an_explicit_di_source_selection(self):
        def mutate(r):
            item=by_id(r,'DIN');child=element(item,'sourceRef','PROC_IN0');item.remove(child);item.insert(0,child)
            element(item,'transformation','opaque_expression()',language='urn:fixture-expression')
        data=change(self.data,mutate);self.assertTrue(any('explicit sourceElement' in e for e in check_native(data,'bpmn','2.0.2')['errors']))
        with self.assertRaisesRegex(Invalid,'explicit sourceElement'):diagram_plan(data)
        selected=change(data,lambda r:by_id(r,'DIN_DI').set('sourceElement','DR_DI'))
        self.assertEqual('DR_DI',diagram_plan(selected)['graphics'][0]['source_graphic_id'])

    def test_native_package_roundtrip_preserves_all_original_di_strings_and_order(self):
        package=make_package(self.data,'bpmn','2.0.2')
        self.assertEqual(self.data,package_bytes(package,'bpmn','2.0.2'))
        self.assertEqual(hashlib.sha256(self.data).hexdigest(),package['native_sha256'])

    def test_repeated_data_depiction_is_rejected_without_losing_native_bytes(self):
        def mutate(r):
            plane=by_id(r,'PLANE');shape(plane,'A_IN0','500','50','36','50').set('id','REPEATED')
        bad=change(self.data,mutate)
        with self.assertRaises(Invalid):diagram_plan(bad)

    def test_actual_native_data_symbols_and_di_geometry_are_rendered(self):
        with tempfile.TemporaryDirectory(prefix='native-data-di-test-') as tmp:
            before=self.data;out=Path(tmp)/'data.svg';report=render_native(self.data,out)
            self.assertEqual('passed',report['status']);self.assertEqual([],report['warnings'])
            self.assertTrue(report['source_plane_order_preserved']);self.assertEqual(before,self.data)
            self.assertTrue(report['native_source_unchanged']);self.assertEqual('disabled',report['network'])
            source=diagram_plan(self.data);self.assertEqual(source['graphics'][0]['graphic_id'],report['svg_graphic_ids'][0])
            for expected,actual in zip(source['graphics'],report['source_geometry']):
                self.assertEqual(expected.get('bounds'),actual.get('bounds'));self.assertEqual(expected.get('waypoints'),actual.get('waypoints'))
            svg=safe_xml(out.read_bytes());groups=svg.xpath('//*[@data-native-root]/*[@data-di-id]')
            self.assertEqual(report['svg_graphic_ids'],[g.get('data-di-id') for g in groups])
            self.assertEqual('A_DI',groups[0].get('data-target-di-endpoint'))
            self.assertEqual(b'\x89PNG\r\n\x1a\n',out.with_suffix('.png').read_bytes()[:8])
            for sid in ['PROC_IN0','PROC_OUT0','A_IN0','A_OUT0','CATCH_OUT','THROW_IN','DR','DSR']:
                g=svg.xpath('//*[@data-element-id="'+sid+'"]')[0]
                self.assertTrue(g.xpath('.//*[local-name()="path"]'),sid)
            self.assertIn('待审',''.join(svg.itertext()))
            self.assertFalse(report['full_language_acceptance'])


if __name__=='__main__':unittest.main()
