"""Normative positive/negative and actual DI rendering tests for new BPMN views."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import safe_xml,check_native,make_package,package_bytes,Invalid,Incomplete
from bpmn_design_semantics import check,RULES,PDF_SHA256
from bpmn_render import diagram_plan,render_native
from bpmn_layout import derive_layout
from bpmn_design_fixtures import conversation,choreography,element,shape,edge,MODEL,DI,DC


def change(data, mutate):
    root=safe_xml(data);mutate(root);return etree.tostring(root,encoding='utf-8')


def by_id(root,sid):
    return root.xpath('//*[@id="'+sid+'"]')[0]


def remove(root,sid):
    e=by_id(root,sid);e.getparent().remove(e)


class BPMNDesignSemanticsTests(unittest.TestCase):
    def assert_rule(self,data,rule):
        findings=check(safe_xml(data))['findings']
        self.assertIn(rule,{f['rule_id'] for f in findings},findings)
        self.assertTrue(all(f['normative_source']['pdf_sha256']==PDF_SHA256 for f in findings))

    def test_positive_conversation_and_choreography_are_native_valid(self):
        for data in [conversation(),choreography(),choreography(True,True)]:
            with self.subTest(sha256=hashlib.sha256(data).hexdigest()):
                self.assertEqual([],check(safe_xml(data))['findings'])
                self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])

    def test_conversation_requires_two_distinct_parent_participants(self):
        for mutate in [lambda r:by_id(r,'CV').remove(by_id(r,'CV').find('{'+MODEL+'}participantRef')),
                       lambda r:by_id(r,'CV').findall('{'+MODEL+'}participantRef')[1].__setattr__('text','tns:A'),
                       lambda r:by_id(r,'CV').findall('{'+MODEL+'}participantRef')[1].__setattr__('text','tns:GLOBAL_B')]:
            self.assert_rule(change(conversation(),mutate),'conversation-participants')

    def test_conversation_grouped_flow_must_use_its_parties_and_scope(self):
        bad=change(conversation(),lambda r:by_id(r,'CV').find('{'+MODEL+'}messageFlowRef').__setattr__('text','tns:CV'))
        self.assert_rule(bad,'conversation-message-flow')
        bad=change(conversation(),lambda r:element(by_id(r,'CG'),'messageFlowRef','tns:M'))
        self.assert_rule(bad,'conversation-message-flow')

    def test_conversation_link_has_exactly_one_conversation_endpoint(self):
        data=change(conversation(),lambda r:by_id(r,'L2').set('targetRef','tns:SC'))
        self.assert_rule(data,'conversation-link')
        data=change(conversation(),lambda r:by_id(r,'L2').set('sourceRef','tns:A'))
        self.assert_rule(data,'conversation-link')
        bad=change(conversation(),lambda r:by_id(r,'L1').set('sourceRef','tns:GLOBAL_A'))
        self.assert_rule(bad,'conversation-link')

    def test_conversation_call_excludes_choreography(self):
        def mutate(r):
            by_id(r,'GLOBAL').tag='{'+MODEL+'}choreography'
        self.assert_rule(change(conversation(),mutate),'call-conversation-target')

    def test_global_conversation_cannot_contain_conversation_nodes(self):
        self.assert_rule(change(conversation(),lambda r:element(by_id(r,'GLOBAL'),'conversation',id='BAD')),'global-conversation-content')

    def test_choreography_activity_cardinality_type_scope_and_initiator(self):
        cases=[lambda r:by_id(r,'T1').findall('{'+MODEL+'}participantRef')[1].__setattr__('text','tns:A'),
               lambda r:by_id(r,'T1').findall('{'+MODEL+'}participantRef')[1].__setattr__('text','tns:T2'),
               lambda r:by_id(r,'T1').set('initiatingParticipantRef','tns:C'),
               lambda r:by_id(r,'T1').getparent().remove(by_id(r,'T1'))]
        for mutate in cases[:3]:
            self.assert_rule(change(choreography(),mutate),'choreography-activity-scope')
        def wrong_owner(r):
            e=by_id(r,'T1');e.getparent().remove(e);element(r,'process',id='P').append(e)
        self.assert_rule(change(choreography(),wrong_owner),'choreography-activity-scope')

    def test_choreography_task_messages_have_two_parties_and_return_direction(self):
        for mutate in [lambda r:by_id(r,'M2').set('sourceRef','tns:A'),
                       lambda r:by_id(r,'M1').set('targetRef','tns:C'),
                       lambda r:element(by_id(r,'T2'),'participantRef','tns:C')]:
            self.assert_rule(change(choreography(),mutate),'choreography-task-message')
        def missing(r):
            e=by_id(r,'T2').find('{'+MODEL+'}messageFlowRef');e.getparent().remove(e)
        self.assert_rule(change(choreography(),missing),'choreography-task-message')
        bad=change(choreography(),lambda r:by_id(r,'M3').set('sourceRef','tns:B'))
        self.assert_rule(bad,'choreography-task-message')
        third=change(choreography(),lambda r:element(by_id(r,'T1'),'messageFlowRef','tns:M3'))
        self.assert_rule(third,'choreography-task-message')
        self.assertTrue(check_native(third,'bpmn','2.0.2')['errors'])

    def test_choreography_call_rejects_conversation_target(self):
        self.assert_rule(change(choreography(),lambda r:by_id(r,'GLOBAL').__setattr__('tag','{'+MODEL+'}globalConversation')),'call-choreography-target')

    def test_participant_mapping_rejects_wrong_inner_and_outer_parties(self):
        cases=[(choreography(),'CG_GA_A','innerParticipantRef','tns:RA'),
               (choreography(),'CG_GA_A','outerParticipantRef','tns:C'),
               (conversation(),'CG_GLOBAL_A_A','innerParticipantRef','tns:REUSE_A'),
               (conversation(),'CG_GLOBAL_A_A','outerParticipantRef','tns:GLOBAL_B')]
        for data,sid,field,value in cases:
            with self.subTest(sid=sid,field=field):
                self.assert_rule(change(data,lambda r:by_id(r,sid).find('{'+MODEL+'}'+field).__setattr__('text',value)),'participant-association')

    def test_participant_multiplicity_rejects_negative_minimum_and_invalid_maximum(self):
        for attr,value in [('minimum','-1'),('maximum','0'),('minimum','4')]:
            self.assert_rule(change(choreography(),lambda r:by_id(r,'C_MULTI').set(attr,value)),'participant-multiplicity')

    def test_global_choreography_is_atomic_and_has_its_own_initiator(self):
        self.assert_rule(change(choreography(),lambda r:element(by_id(r,'GLOBAL'),'startEvent',id='BAD_START')),'global-choreography-content')
        self.assert_rule(change(choreography(),lambda r:by_id(r,'GLOBAL').set('initiatingParticipantRef','tns:A')),'global-choreography-content')

    def test_di_attributes_apply_only_to_their_native_shape_types(self):
        for attr in ['isExpanded','isMarkerVisible','isHorizontal','isMessageVisible','choreographyActivityShape']:
            value='tns:T1_DI' if attr=='choreographyActivityShape' else 'false'
            self.assert_rule(change(choreography(),lambda r:by_id(r,'T1_DI').set(attr,value)),'di-attribute-applicability')

    def test_participant_band_owner_membership_and_shading(self):
        for mutate in [lambda r:by_id(r,'T1_A_BAND').attrib.pop('choreographyActivityShape'),
                       lambda r:by_id(r,'T1_A_BAND').set('choreographyActivityShape','tns:START_DI'),
                       lambda r:by_id(r,'T1_A_BAND').set('participantBandKind','top_non_initiating'),
                       lambda r:by_id(r,'T1_A_BAND').set('bpmnElement','tns:C'),
                       lambda r:remove(r,'T1_A_BAND')]:
            self.assert_rule(change(choreography(),mutate),'di-participant-band')

    def test_invalid_participant_band_kind_is_an_exchange_error(self):
        for value in ['middle_false','top','non_initiating']:
            report=check_native(change(choreography(),lambda r:by_id(r,'T1_A_BAND').set('participantBandKind',value)),'bpmn','2.0.2')
            self.assertTrue(report['errors'])

    def test_envelopes_cannot_be_on_subchoreography_or_nonsender(self):
        for sid in ['SUB_A_BAND','CC_A_BAND','T2_B_BAND']:
            self.assert_rule(change(choreography(),lambda r:by_id(r,sid).set('isMessageVisible','true')),'di-band-message')

    def test_di_edge_endpoint_cannot_target_a_participant_band(self):
        self.assert_rule(change(choreography(),lambda r:by_id(r,'F0_DI').set('targetElement','tns:T1_A_BAND')),'di-edge-endpoint')
        self.assert_rule(change(choreography(),lambda r:by_id(r,'F0_DI').set('targetElement','tns:T1')),'di-edge-endpoint')

    def test_external_qname_is_blocked_without_local_aliasing(self):
        bad=choreography().replace(b'xmlns:tns="urn:independent:design"',b'xmlns:tns="urn:independent:design" xmlns:outside="urn:outside"').replace(b'calledChoreographyRef="tns:GLOBAL"',b'calledChoreographyRef="outside:GLOBAL"')
        report=check_native(bad,'bpmn','2.0.2')
        self.assertTrue(any('outside:GLOBAL' in b for b in report['blockers']))
        self.assertFalse(any('call-choreography-target' in e for e in report['errors']))

    def test_lossless_package_roundtrip_keeps_xml_and_di_bytes(self):
        for original in [conversation(),choreography(True,True)]:
            package=make_package(original,'bpmn','2.0.2')
            self.assertEqual(original,package_bytes(package,'bpmn','2.0.2'))
            self.assertFalse(package['report'].get('full_language_acceptance',False))


class BPMNDesignNotationTests(unittest.TestCase):
    def test_di_graphic_identity_preserves_repeated_semantic_participants(self):
        data=choreography();plan=diagram_plan(data)
        self.assertEqual(19,len(plan['shape_graphic_ids']))
        self.assertEqual(5,len([g for g in plan['graphics'] if g['semantic_id']=='A']))
        self.assertEqual(hashlib.sha256(data).hexdigest(),plan['source_sha256'])
        self.assertFalse(plan['auto_layout'])
        self.assertEqual([],plan['native_validation']['errors'])

    def test_collapsed_and_expanded_sub_and_call_follow_explicit_di(self):
        collapsed=diagram_plan(choreography())
        self.assertNotIn('INNER',collapsed['shape_ids']);self.assertNotIn('REUSED',collapsed['shape_ids'])
        expanded=diagram_plan(choreography(True,True))
        self.assertIn('INNER',expanded['shape_ids']);self.assertIn('REUSED',expanded['shape_ids'])
        self.assertEqual(25,len(expanded['shape_graphic_ids']))
        self.assertIn('INNER',{r['id'] for r in collapsed['hidden_native_elements']})

    def test_missing_di_or_bands_are_blocked(self):
        for sid,reason in [('DIAGRAM','exactly one explicit'),('T1_DI','dangling BPMN reference'),('T1_A_BAND','di-participant-band')]:
            data=change(choreography(),lambda r:remove(r,sid))
            expected=Incomplete if sid=='DIAGRAM' else Invalid
            with self.assertRaisesRegex(expected,reason):diagram_plan(data)

    def test_missing_all_bands_are_uncovered_not_silently_invented(self):
        def mutate(r):
            remove(r,'T1_A_BAND');remove(r,'T1_B_BAND')
        with self.assertRaisesRegex(Incomplete,'Missing required Participant Bands'):
            diagram_plan(change(choreography(),mutate))

    def test_band_bounds_do_not_escape_or_overlap_the_activity(self):
        for sid,attr,value in [('T1_A_BAND','x','121'),('T1_B_BAND','y','110')]:
            data=change(choreography(),lambda r:by_id(r,sid).find('{'+DC+'}Bounds').set(attr,value))
            with self.assertRaisesRegex(Invalid,'Band'):
                diagram_plan(data)

    def test_repeated_graphics_need_explicit_edge_endpoint_selection(self):
        def repeat(r):
            e=etree.fromstring(etree.tostring(by_id(r,'T1_DI')));e.set('id','T1_DI_COPY');by_id(r,'PLANE').append(e)
        # BPMN 2.0.2 12.2.1 (physical 398) forbids repeating an ordinary
        # element within one diagram. Only choreography Participant Bands
        # may repeat; an explicit endpoint cannot legalize this activity.
        with self.assertRaisesRegex(Invalid,'Repeated ordinary BPMN element'):
            diagram_plan(change(choreography(),repeat))

    def test_di_ids_are_optional_for_nonreferenced_graphics(self):
        data=change(conversation(),lambda r:by_id(r,'CV_DI').attrib.pop('id'))
        plan=diagram_plan(data)
        self.assertTrue(any(g['identity_origin']=='source-plane-position' for g in plan['graphics']))

    def test_nested_subconversation_detail_is_visible_only_when_explicitly_depicted(self):
        def mutate(r):
            detail=by_id(r,'DETAIL');detail.tag='{'+MODEL+'}subConversation'
            nested=element(detail,'conversation',id='NESTED',name='三级会话')
            element(nested,'participantRef','tns:A');element(nested,'participantRef','tns:B')
            shape(by_id(r,'PLANE'),'DETAIL',370,230,48,48)
            shape(by_id(r,'PLANE'),'NESTED',450,230,48,48)
        data=change(conversation(),mutate);plan=diagram_plan(data)
        self.assertIn('DETAIL',plan['shape_ids']);self.assertIn('NESTED',plan['shape_ids'])
        self.assertEqual([],plan['native_validation']['errors'])

    def test_edge_override_can_reference_a_later_edge_graphic(self):
        def mutate(r):
            owner=by_id(r,'COLLAB')
            association=element(owner,'association',id='AS',sourceRef='tns:L1',targetRef='tns:CV')
            owner.remove(association);owner.insert(3,association)
            p=by_id(r,'PLANE')
            graphic=edge(p,'AS',[(210,104),(210,60),(294,60),(294,80)],sourceElement='tns:L1_DI',targetElement='tns:CV_DI')
            p.remove(graphic);p.insert(0,graphic)
        data=change(conversation(),mutate)
        self.assertEqual([],diagram_plan(data)['native_validation']['errors'])
        with tempfile.TemporaryDirectory(prefix='bpmn-edge-override-') as tmp:
            report=render_native(data,Path(tmp)/'view.svg')
            self.assertEqual('passed',report['status']);self.assertIn('AS_DI',report['svg_graphic_ids'])

    def test_actual_middle_initiator_and_explicit_single_participant_multiplicity(self):
        def mutate(r):
            by_id(r,'SUB').set('initiatingParticipantRef','tns:C')
            by_id(r,'SUB_C_BAND').set('participantBandKind','middle_initiating')
            by_id(r,'SUB_B_BAND').set('participantBandKind','bottom_non_initiating')
            by_id(r,'C_MULTI').set('maximum','1')
        data=change(choreography(),mutate)
        with tempfile.TemporaryDirectory(prefix='bpmn-middle-band-') as tmp:
            folder=Path(tmp);report=render_native(data,folder/'view.svg')
            svg=safe_xml((folder/'view.svg').read_bytes())
            band=svg.xpath('//*[@data-di-id="SUB_C_BAND"]')[0]
            self.assertEqual('white',band.xpath('./*[local-name()="path"]')[0].get('fill'))
            self.assertFalse(band.xpath('.//*[@data-marker="parallel"]'))
            self.assertEqual('passed',report['status'])

    def test_notation_projection_records_official_descriptor_differences(self):
        original=conversation();plan=diagram_plan(original)
        self.assertIn('<messageFlowRefs>',plan['notation_xml'])
        self.assertIn('innerParticipantRef="GLOBAL_A"',plan['notation_xml'])
        self.assertIn(b'<messageFlowRef>tns:M</messageFlowRef>',original)
        self.assertTrue(plan['notation_adaptations'])

    def test_actual_conversation_and_choreography_rendering_preserve_geometry(self):
        for label,data in [('conversation',conversation()),('choreography',choreography()),('expanded',choreography(True,True))]:
            with self.subTest(view=label),tempfile.TemporaryDirectory(prefix='bpmn-design-test-') as tmp:
                original=bytes(data);folder=Path(tmp);report=render_native(data,folder/'view.svg')
                self.assertEqual('passed',report['status'])
                self.assertEqual('disabled',report['network'])
                self.assertEqual([],report['warnings'])
                self.assertTrue(report['native_source_unchanged'])
                self.assertEqual(original,data)
                self.assertEqual(hashlib.sha256(original).hexdigest(),report['source_sha256'])
                svg=safe_xml((folder/'view.svg').read_bytes())
                self.assertEqual(set(report['shape_graphic_ids']+report['edge_graphic_ids']),{e.get('data-di-id') for e in svg.iter() if e.get('data-di-id')})
                for g in report['source_geometry']:
                    e=svg.xpath('//*[@data-di-id="'+g['graphic_id']+'"]')[0]
                    if g['kind']=='shape':
                        for key,value in g['bounds'].items():self.assertEqual(value,float(e.get('data-di-'+key)))
                    else:self.assertEqual(g['waypoints'],json.loads(e.get('data-source-waypoints')))
                if label=='conversation':
                    self.assertEqual(10,len(svg.xpath('//*[@data-conversation-link-line]')))
                    self.assertEqual(4,len(svg.xpath('//*[@data-notation="conversation-hexagon"]')))
                else:
                    self.assertNotIn('url(&quot;#',(folder/'view.svg').read_text())
                    self.assertTrue(svg.xpath('//*[contains(@style,"marker-end: url(#")]'))
                    self.assertTrue(svg.xpath('//*[@data-band-kind="top_initiating"]'))
                    self.assertTrue(svg.xpath('//*[@data-band-kind="bottom_non_initiating"]'))
                    self.assertTrue(svg.xpath('//*[@data-message-envelope="return"]'))
                    self.assertTrue(svg.xpath('//*[@data-marker="parallel"]'))
                    self.assertTrue(svg.xpath('//*[@data-call-boundary]'))
                    self.assertTrue(report['common_symbol_evidence'])
                self.assertEqual(b'\x89PNG\r\n\x1a\n',(folder/'view.png').read_bytes()[:8])
                self.assertEqual('incomplete',report['conformance_status'])
                self.assertFalse(report['full_language_acceptance'])
                with self.assertRaisesRegex(Invalid,'overwrite'):render_native(data,folder/'view.svg')


class BPMNExplicitLayoutTests(unittest.TestCase):
    def no_di(self,data):
        return change(data,lambda r:remove(r,'DIAGRAM'))

    def test_default_refuses_missing_geometry_and_explicit_selection_derives_it(self):
        for original in [self.no_di(conversation()),self.no_di(choreography())]:
            with self.assertRaises(Incomplete):diagram_plan(original)
            derived,report=derive_layout(original)
            self.assertTrue(report['derived'])
            self.assertTrue(report['authoritative_source_unchanged'])
            self.assertEqual(hashlib.sha256(original).hexdigest(),report['source_sha256'])
            self.assertEqual([],check_native(derived,'bpmn','2.0.2')['errors'])
            self.assertTrue(diagram_plan(derived)['shape_ids'])
            selected=diagram_plan(original,auto_layout=True)
            self.assertTrue(selected['auto_layout']);self.assertTrue(selected['layout']['derived'])

    def test_complete_explicit_di_is_returned_byte_for_byte(self):
        original=choreography();derived,report=derive_layout(original)
        self.assertEqual(original,derived)
        self.assertFalse(report['derived'])

    def test_missing_graphic_is_added_without_changing_any_existing_coordinate(self):
        original=change(conversation(),lambda r:remove(r,'SC_DI'))
        before=safe_xml(original)
        geometry={e.getparent().get('id')+':'+str(i):dict(e.attrib) for i,e in enumerate(before.iter()) if e.tag=='{'+DC+'}Bounds' or e.tag.endswith('}waypoint')}
        derived,report=derive_layout(original);after=safe_xml(derived)
        for graphic in before.xpath('//*[local-name()="BPMNShape" or local-name()="BPMNEdge"]'):
            current=by_id(after,graphic.get('id'))
            self.assertEqual(etree.tostring(graphic),etree.tostring(current))
        self.assertTrue(report['preserved_geometry'])
        self.assertTrue(any(g['semantic_id']=='SC' for g in report['added_graphics']))

    def test_invalid_source_geometry_and_ambiguous_view_are_not_repaired(self):
        invalid=change(conversation(),lambda r:by_id(r,'SC_DI').find('{'+DC+'}Bounds').set('x','NaN'))
        with self.assertRaisesRegex(Invalid,'finite'):derive_layout(invalid)
        ambiguous=self.no_di(conversation())
        # REUSE is called, so add another noncalled independent Collaboration.
        ambiguous=change(ambiguous,lambda r:element(r,'collaboration',id='AMBIGUOUS'))
        with self.assertRaisesRegex(Incomplete,'unambiguous'):derive_layout(ambiguous)

    def test_layout_selection_does_not_accept_truthy_string_values(self):
        with self.assertRaisesRegex(Invalid,'Boolean'):diagram_plan(self.no_di(conversation()),auto_layout='false')
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(Invalid,'Boolean'):render_native(self.no_di(conversation()),Path(tmp)/'view.svg',auto_layout='true')

    def test_partial_participant_stack_requires_explicit_remaining_positions(self):
        original=change(choreography(),lambda r:remove(r,'T1_A_BAND'))
        with self.assertRaisesRegex(Incomplete,'Partial Participant Band'):derive_layout(original)

    def test_automatic_lane_partition_is_reported_as_uncovered(self):
        original=b'<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" targetNamespace="urn:lanes"><process id="P"><laneSet id="LS"><lane id="L"><flowNodeRef>T</flowNodeRef></lane></laneSet><task id="T"/></process></definitions>'
        with self.assertRaisesRegex(Incomplete,'Automatic lane partitioning'):derive_layout(original)

    def test_actual_explicit_layout_render_delivers_derived_xml_and_source_binding(self):
        original=self.no_di(choreography())
        with tempfile.TemporaryDirectory(prefix='bpmn-explicit-layout-') as tmp:
            folder=Path(tmp);report=render_native(original,folder/'view.svg',auto_layout=True)
            self.assertTrue(report['auto_layout'])
            self.assertTrue(report['layout']['derived'])
            self.assertEqual(hashlib.sha256(original).hexdigest(),report['source_sha256'])
            derived=(folder/'view.layout.bpmn').read_bytes()
            self.assertEqual(hashlib.sha256(derived).hexdigest(),report['rendered_model_sha256'])
            self.assertEqual(hashlib.sha256(derived).hexdigest(),report['layout']['derived_sha256'])
            self.assertEqual(b'\x89PNG\r\n\x1a\n',(folder/'view.png').read_bytes()[:8])
            self.assertEqual('incomplete',report['conformance_status'])


if __name__=='__main__':unittest.main()
