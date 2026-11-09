"""Source-independent MI, shortcut and mixed native data-DI counterexamples."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree

REPO=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts')]
from standards import safe_xml,check_native,make_package,package_bytes,Invalid,Incomplete
from bpmn_data_compensation import check
from bpmn_render import diagram_plan,render_native
from bpmn_mi_shortcut_fixtures import mi_model,shortcut_model,mixed_model
from bpmn_data_compensation_fixtures import by_id,change,element,association,MODEL
from bpmn_data_di_fixtures import remove_di,shape,DI,DC


def rules(data):return {e['rule_id'] for e in check(safe_xml(data))['findings']}
def remove(root,sid):
    e=by_id(root,sid);e.getparent().remove(e)


class BPMNMISemanticsTests(unittest.TestCase):
    data=mi_model()

    def test_task_and_subprocess_owner_specific_positive_models(self):
        for data in [self.data,mi_model(True)]:
            self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
            self.assertEqual([],check(safe_xml(data))['findings'])
            self.assertEqual('incomplete',check_native(data,'bpmn','2.0.2')['conformance_status'])

    def test_valid_mi_requires_cardinality_or_input_collection(self):
        def mutate(r):
            m=by_id(r,'MI');m.remove(m.find('{'+MODEL+'}loopDataInputRef'))
        bad=change(self.data,mutate)
        self.assertIn('mi-initialization',rules(bad))
        def documented(r):
            m=by_id(r,'MI');m.insert(0,etree.Element('{'+MODEL+'}loopCardinality'));m[0].text='documented number of reviews'
        good=change(bad,documented)
        self.assertEqual([],check_native(good,'bpmn','2.0.2')['errors'])
        self.assertTrue(any('integer' in e['obligation'] and 'uncovered' in e['status'] for e in check(safe_xml(good))['mi_unverified_obligations']))

    def test_task_cannot_use_external_data_object_as_loop_io(self):
        for field,target in [('loopDataInputRef','SOURCE'),('loopDataOutputRef','RESULT')]:
            bad=change(self.data,lambda r,f=field,t=target:setattr(by_id(r,'MI').find('{'+MODEL+'}'+f),'text','tns:'+t))
            self.assertIn('mi-loop-reference-type',rules(bad))

    def test_task_cannot_use_another_activity_io_even_with_correct_type(self):
        def mutate(r):
            from bpmn_data_compensation_fixtures import io
            other=element(by_id(r,'P'),'task',id='B');io(other,'B',definition='COL')
            for sid in ['B_IN0','B_OUT0']:by_id(r,sid).set('isCollection','true')
            by_id(r,'MI').find('{'+MODEL+'}loopDataInputRef').text='tns:B_IN0'
        self.assertIn('mi-loop-reference-scope',rules(change(self.data,mutate)))

    def test_subprocess_collection_must_be_a_visible_data_object(self):
        good=mi_model(True)
        def mutate(r):
            other=element(r,'process',id='FOREIGN');element(other,'dataObject',id='FD',itemSubjectRef='tns:COL',isCollection='true')
            r.remove(other);r.insert(3,other)
            by_id(r,'MI').find('{'+MODEL+'}loopDataInputRef').text='tns:FD'
        self.assertIn('mi-loop-reference-scope',rules(change(good,mutate)))
        bad=change(good,lambda r:setattr(by_id(r,'MI').find('{'+MODEL+'}loopDataInputRef'),'text','tns:ONE_IN'))
        self.assertIn('mi-loop-reference-type',rules(bad))

    def test_loop_collection_flag_including_false_default_is_required(self):
        for sid in ['A_IN0','A_OUT0']:
            bad=change(self.data,lambda r,s=sid:by_id(r,s).attrib.pop('isCollection'))
            self.assertIn('mi-loop-collection',rules(bad))

    def test_instance_input_and_output_items_cannot_be_collection_valued(self):
        for sid in ['ONE_IN','ONE_OUT']:
            def mutate(r,s=sid):by_id(r,s).set('isCollection','true');by_id(r,s).set('itemSubjectRef','tns:COL')
            self.assertIn('mi-data-item-scalar',rules(change(self.data,mutate)))

    def test_sequential_flag_uses_official_boolean_lexical_values_and_rejects_invalid(self):
        for value in ['true','false','1','0']:
            data=change(self.data,lambda r,v=value:by_id(r,'MI').set('isSequential',v))
            self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
            self.assertEqual(value,by_id(safe_xml(data),'MI').get('isSequential'))
        bad=change(self.data,lambda r:by_id(r,'MI').set('isSequential','maybe'))
        self.assertTrue(any('SCHEMAV_' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))

    def test_event_reference_type_and_optional_default_behavior_are_distinct(self):
        for field in ['oneBehaviorEventRef','noneBehaviorEventRef']:
            self.assertIn('mi-behavior-event-type',rules(change(self.data,lambda r,f=field:by_id(r,'MI').set(f,'tns:I'))))
        good=change(self.data,lambda r:by_id(r,'MI').attrib.pop('oneBehaviorEventRef'))
        self.assertEqual([],check_native(good,'bpmn','2.0.2')['errors'])
        self.assertNotIn('mi-behavior-event-type',rules(good))

    def test_mi_inner_items_support_real_io_associations_without_set_membership_fabrication(self):
        def mutate(r):
            a=by_id(r,'A');spec=by_id(r,'A_IO');ins=element(spec,'dataInput',id='INNER_IN',itemSubjectRef='tns:I');outs=element(spec,'dataOutput',id='INNER_OUT',itemSubjectRef='tns:I')
            spec.remove(ins);spec.insert(1,ins);spec.remove(outs);spec.insert(3,outs)
            for sid,tag,text in [('A_IS','dataInputRefs','INNER_IN'),('A_OS','dataOutputRefs','INNER_OUT')]:
                group=by_id(r,sid);ref=element(group,tag,text);group.remove(ref);group.insert(1,ref)
            x=association(a,'dataInputAssociation','INNER_PULL',['ONE_IN'],'INNER_IN');a.remove(x);a.insert(1,x)
            x=association(a,'dataOutputAssociation','INNER_PUSH',['INNER_OUT'],'ONE_OUT');a.remove(x);a.insert(2,x)
        data=change(self.data,mutate)
        self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
        self.assertNotIn('io-set-membership',rules(data))

    def test_scalar_type_mapping_is_explicitly_uncovered_and_source_bytes_roundtrip(self):
        report=check(safe_xml(self.data))
        self.assertEqual({'ONE_IN','ONE_OUT'},{e['id'] for e in report['mi_unverified_obligations'] if 'scalar type' in e['obligation']})
        self.assertTrue(all('uncovered' in e['status'] for e in report['mi_unverified_obligations']))
        self.assertEqual(self.data,package_bytes(make_package(self.data,'bpmn','2.0.2'),'bpmn','2.0.2'))


class BPMNShortcutAndMixedDITests(unittest.TestCase):
    data=shortcut_model()

    def test_no_bpmn_element_shortcut_binds_two_actual_native_associations(self):
        self.assertEqual([],check_native(self.data,'bpmn','2.0.2')['errors'])
        plan=diagram_plan(self.data);g=next(g for g in plan['graphics'] if g['type']=='dataAssociationShortcut')
        self.assertEqual(['OUT','IN'],g['normalized_semantic_ids']);self.assertIsNone(g['semantic_id'])
        self.assertEqual('DR_DI',g['source_graphic_id']);self.assertEqual('FLOW_DI',g['target_graphic_id'])
        self.assertIsNone(by_id(safe_xml(self.data),'SHORTCUT_DI').get('bpmnElement'))

    def test_shortcut_requires_data_shape_to_sequence_flow_edge_in_that_direction(self):
        for attr,value in [('targetElement','tns:B_DI'),('sourceElement','tns:A_DI'),('sourceElement','tns:FLOW_DI')]:
            bad=change(self.data,lambda r,a=attr,v=value:by_id(r,'SHORTCUT_DI').set(a,v))
            self.assertTrue(check_native(bad,'bpmn','2.0.2')['errors'])
            with self.assertRaises(Invalid):diagram_plan(bad)

    def test_shortcut_requires_both_underlying_associations_and_no_guessed_pair(self):
        for sid in ['OUT','IN']:
            bad=change(self.data,lambda r,s=sid:remove(r,s))
            self.assertTrue(any('both retained' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))
        bad=change(self.data,lambda r:association(by_id(r,'A'),'dataOutputAssociation','DUP',['A_OUT0'],'DR'))
        self.assertTrue(any('ambiguous' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))

    def test_zero_source_transformation_cannot_impersonate_a_source_output_shortcut(self):
        def mutate(r):
            e=by_id(r,'OUT');e.remove(e.find('{'+MODEL+'}sourceRef'));element(e,'transformation','opaque_literal()',language='urn:opaque')
        data=change(self.data,mutate)
        self.assertTrue(any('both retained' in e for e in check_native(data,'bpmn','2.0.2')['errors']))
        with self.assertRaises(Invalid):diagram_plan(data)

    def test_zero_source_directed_data_di_has_no_fabricated_graphical_context(self):
        def mutate(r):
            e=by_id(r,'DIN');e.remove(e.find('{'+MODEL+'}sourceRef'));element(e,'transformation','opaque_literal()',language='urn:opaque')
            by_id(r,'DIN_DI').set('sourceElement','tns:DR_DI')
        data=change(mixed_model(),mutate)
        self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
        with self.assertRaisesRegex(Incomplete,'no retained ItemAwareElement context'):diagram_plan(data)

    def test_referenced_but_unpictured_choreography_is_optional_native_inventory(self):
        def mutate(r):
            for sid in ['CT_DI','CT_CA_BAND','CT_CB_BAND']:remove(r,sid)
        data=change(mixed_model(),mutate);plan=diagram_plan(data)
        self.assertEqual([],plan['included_choreography_ids'])
        self.assertEqual('CHOREO',plan['referenced_choreography_inventory'][0]['id'])
        self.assertFalse(plan['referenced_choreography_inventory'][0]['depicted'])
        self.assertIn('DIN',plan['edge_ids']);self.assertIn('DR',plan['shape_ids'])
        self.assertEqual(data,package_bytes(make_package(data,'bpmn','2.0.2'),'bpmn','2.0.2'))

    def test_arbitrary_no_reference_di_edge_is_rejected(self):
        def mutate(r):
            e=by_id(r,'SHORTCUT_DI');e.attrib.pop('sourceElement');e.attrib.pop('targetElement')
        self.assertTrue(check_native(change(self.data,mutate),'bpmn','2.0.2')['errors'])

    def test_single_directed_association_cannot_replace_two_association_shortcut(self):
        bad=change(self.data,lambda r:by_id(r,'SHORTCUT_DI').set('bpmnElement','tns:OUT'))
        with self.assertRaises((Invalid,Incomplete)):diagram_plan(bad)

    def test_shortcut_coordinates_native_refs_and_roundtrip_remain_exact(self):
        root=safe_xml(self.data);before=etree.tostring(root);plan=diagram_plan(self.data)
        self.assertEqual(before,etree.tostring(root));self.assertEqual(self.data,package_bytes(make_package(self.data,'bpmn','2.0.2'),'bpmn','2.0.2'))
        self.assertEqual([{'x':'328.000','y':'100.00'},{'x':'328.000','y':'195.00'}],plan['graphics'][-1]['waypoints'])

    def test_mi_scalar_roles_render_on_collapsed_subprocess_as_optional_outer_data(self):
        data=mi_model(True);plan=diagram_plan(data)
        self.assertEqual({'A','ONE_IN','ONE_OUT'},set(plan['shape_ids']))
        self.assertEqual({'inputDataItem','outputDataItem'},{e['native_role'] for e in plan['data_depiction_inventory']})
        self.assertEqual({'dataInput','dataOutput'},{g['type'] for g in plan['graphics'] if g['semantic_id']!='A'})
        omitted=remove_di(data,'ONE_IN','ONE_OUT')
        self.assertEqual(['A'],diagram_plan(omitted)['shape_ids'])
        self.assertTrue(all(not e['depicted'] for e in diagram_plan(omitted)['data_depiction_inventory']))

    def test_mixed_collaboration_choreography_and_pool_data_view_has_explicit_scope(self):
        data=mixed_model();self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])
        plan=diagram_plan(data)
        self.assertEqual('native-design-di',plan['backend']);self.assertEqual(['CHOREO'],plan['included_choreography_ids'])
        self.assertIn('DIN',plan['edge_ids']);self.assertIn('CT',plan['shape_ids']);self.assertIn('DR',plan['shape_ids'])
        self.assertFalse(plan['auto_layout'])
        omitted=remove_di(data,'DR','DIN')
        self.assertNotIn('DR',diagram_plan(omitted)['shape_ids'])
        self.assertTrue(any(e['id']=='DR' and not e['depicted'] for e in diagram_plan(omitted)['data_depiction_inventory']))

    def test_mixed_data_owner_impersonation_and_band_endpoints_are_rejected(self):
        data=mixed_model()
        bad=change(data,lambda r:by_id(r,'DIN_DI').set('targetElement','tns:CT_DI'))
        with self.assertRaisesRegex(Invalid,'override conflicts'):diagram_plan(bad)
        bad=change(data,lambda r:by_id(r,'DIN_DI').set('targetElement','tns:CT_CA_BAND'))
        self.assertTrue(any('Participant Band' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))

    def test_mixed_geometry_label_strings_plane_order_and_native_roundtrip(self):
        data=mixed_model();root=safe_xml(data);plan=diagram_plan(data)
        self.assertEqual([e.get('id') for e in by_id(root,'PLANE')],[g['graphic_id'] for g in plan['graphics']])
        for g in plan['graphics']:
            e=by_id(root,g['graphic_id'])
            if g['kind']=='shape':self.assertEqual(dict(e.find('{'+DC+'}Bounds').attrib),g['bounds'])
            else:self.assertEqual([dict(c.attrib) for c in e if c.tag.endswith('waypoint')],g['waypoints'])
        self.assertEqual(data,package_bytes(make_package(data,'bpmn','2.0.2'),'bpmn','2.0.2'))

    def test_mixed_repeated_ordinary_shape_is_rejected_but_participant_bands_remain_valid(self):
        def mutate(r):
            e=shape(by_id(r,'PLANE'),'SEND','60.000','70.00','160.000','90.0');e.set('id','DUPLICATE_SEND_DI')
        bad=change(mixed_model(),mutate)
        self.assertTrue(any('di-ordinary-identity:' in e for e in check_native(bad,'bpmn','2.0.2')['errors']))
        with self.assertRaisesRegex(Invalid,'Repeated ordinary'):diagram_plan(bad)

    def test_actual_mi_shortcut_mixed_svg_png_and_lexical_geometry(self):
        for name,data in [('mi-parallel',mi_model()),('mi-sequential',mi_model(True,True)),('shortcut',self.data),('mixed',mixed_model())]:
            with tempfile.TemporaryDirectory() as tmp:
                report=render_native(data,Path(tmp)/name)
                svg=Path(report['outputs']['svg']).read_bytes();root=etree.fromstring(svg)
                self.assertGreater(Path(report['outputs']['png']).stat().st_size,1000)
                plan=diagram_plan(data)
                groups=root.xpath('//*[@data-di-id]')
                self.assertEqual([g['graphic_id'] for g in plan['graphics']],[e.get('data-di-id') for e in groups])
                for g,e in zip(plan['graphics'],groups):
                    if g['kind']=='shape':self.assertEqual(g['bounds']['x'],e.get('data-di-x'))
                    else:self.assertEqual(g['waypoints'],json.loads(e.get('data-source-waypoints')))
                if name=='shortcut':self.assertEqual(['OUT','IN'],json.loads(groups[-1].get('data-normalized-native-associations')))
                self.assertFalse(report['full_language_acceptance'])


if __name__=='__main__':unittest.main()
