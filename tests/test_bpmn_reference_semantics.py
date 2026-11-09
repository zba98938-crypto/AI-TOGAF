"""Normative BPMN adversarial cases: references, FlowNodes and event gateways.

Oracle basis: BPMN 2.0.2 tables 8.51/8.52/10.3, section 10.6.6,
section 15.3.2 and Annex B Point/Edge. This is a bounded subset review.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import safe_xml, check_native, validate_references
from bpmn_semantics import check
from bpmn_rule_fixtures import document


def xml(body):
    return document(body).replace(b'targetNamespace=', b'xmlns:tns="urn:independent-rules" xmlns:foreign="urn:outside" targetNamespace=')


GATEWAY='<process id="p"><eventBasedGateway id="g"/><receiveTask id="a"/><receiveTask id="b"/><sequenceFlow id="f" sourceRef="g" targetRef="a"/><sequenceFlow id="h" sourceRef="g" targetRef="b"/></process>'


class BPMNReferenceSemanticsTests(unittest.TestCase):
    def findings(self, body):
        return check(safe_xml(xml(body)))['findings']

    def rules(self, body):
        return {row['rule_id'] for row in self.findings(body)}

    def test_local_qname_boundary_and_di_are_valid(self):
        body='<process id="p"><task id="a"/><boundaryEvent id="b" attachedToRef="tns:a"/></process><bpmndi:BPMNDiagram id="d"><bpmndi:BPMNPlane id="pl" bpmnElement="tns:p"><bpmndi:BPMNShape id="s" bpmnElement="tns:a"><dc:Bounds x="10" y="10" width="100" height="80"/></bpmndi:BPMNShape></bpmndi:BPMNPlane></bpmndi:BPMNDiagram>'
        report=check_native(xml(body),'bpmn','2.0.2')
        self.assertEqual(report['errors'],[])
        self.assertEqual(report['conformance_status'],'incomplete')

    def test_local_qname_message_flow_cannot_evade_same_pool_rule(self):
        body='<process id="p"><task id="a"/><task id="b"/></process><collaboration id="c"><participant id="party" processRef="tns:p"/><messageFlow id="m" sourceRef="tns:a" targetRef="tns:b"/></collaboration>'
        self.assertIn('message-pool',self.rules(body))

    def test_local_qname_message_flow_between_pools_is_valid(self):
        body='<process id="p"><task id="a"/></process><process id="q"><task id="b"/></process><collaboration id="c"><participant id="party" processRef="tns:p"/><participant id="other" processRef="tns:q"/><messageFlow id="m" sourceRef="tns:a" targetRef="tns:b"/></collaboration>'
        self.assertEqual(self.findings(body),[])

    def test_foreign_qname_is_blocked_despite_same_local_id(self):
        body='<process id="p"><task id="a"/><boundaryEvent id="b" attachedToRef="foreign:a"/></process>'
        report=check_native(xml(body),'bpmn','2.0.2')
        self.assertTrue(any('foreign:a' in item for item in report['blockers']))
        self.assertNotIn('boundary-attachment',self.rules(body))

    def test_reference_elements_obey_their_own_namespace_bindings(self):
        body='<process id="p"><task id="a"><outgoing xmlns:tns="urn:outside">tns:f</outgoing></task><task id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
        errors,blocked=validate_references(safe_xml(xml(body)))
        self.assertEqual(errors,[])
        self.assertTrue(any('tns:f' in item for item in blocked))

    def test_flow_node_associations_allow_local_qnames(self):
        body='<process id="p"><task id="a"><outgoing>tns:f</outgoing></task><task id="b"><incoming>tns:f</incoming></task><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
        self.assertEqual(self.findings(body),[])

    def test_explicit_flow_associations_reject_wrong_type_and_direction(self):
        base='<process id="p"><task id="a">ASSOCIATION</task><task id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
        for reference in ('<outgoing>tns:b</outgoing>','<incoming>tns:f</incoming>'):
            with self.subTest(reference=reference):
                self.assertIn('flow-node-association',self.rules(base.replace('ASSOCIATION',reference)))

    def test_sequence_endpoint_type_rejects_data_objects_lanes_and_processes(self):
        for element in ('<dataObject id="a"/>','<laneSet id="l"><lane id="a"/></laneSet>','<process id="a"/>'):
            with self.subTest(element=element):
                body='<process id="p">'+element+'<task id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
                self.assertIn('sequence-endpoint-type',self.rules(body))

    def test_idref_whitespace_is_normalized_for_type_direction_and_scope(self):
        base='<process id="p"><task id="a"/><task id="b"/><sequenceFlow id="f" sourceRef=" a " targetRef=" b "/></process>'
        report=check_native(xml(base),'bpmn','2.0.2')
        self.assertEqual(report['errors'],[])
        self.assertEqual(self.findings(base),[])
        self.assertIn('sequence-endpoint-type',self.rules(base.replace('<task id="a"/>','<dataObject id="a"/>')))
        self.assertIn('event-direction',self.rules(base.replace('<task id="b"/>','<startEvent id="b"/>')))
        crossing=base.replace('<task id="b"/>','<subProcess id="sub"><task id="b"/></subProcess>')
        self.assertIn('sequence-scope',self.rules(crossing))
        one_space=base.replace('sourceRef=" a "','sourceRef="a"')
        self.assertEqual(check_native(xml(one_space),'bpmn','2.0.2')['errors'],[])

    def test_vendor_reference_like_attributes_remain_opaque(self):
        body='<process id="p"><task xmlns:v="urn:vendor" id="a" v:targetRef="outside"/></process>'
        report=check_native(xml(body),'bpmn','2.0.2')
        self.assertEqual(report['errors'],[])
        self.assertIn('urn:vendor',report['vendor_namespaces'])
        self.assertTrue(any('opaque' in item for item in report['blockers']))

    def test_process_and_choreography_flow_nodes_remain_distinct(self):
        invalid='<process id="p"><choreographyTask id="a"/><task id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
        valid='<choreography id="p"><choreographyTask id="a"/><endEvent id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></choreography>'
        self.assertIn('sequence-endpoint-type',self.rules(invalid))
        self.assertNotIn('sequence-endpoint-type',self.rules(valid))

    def test_message_endpoint_types_reject_gateways_and_data_objects(self):
        for element in ('<dataObject id="a"/>','<exclusiveGateway id="a"/>'):
            with self.subTest(element=element):
                body='<process id="p">'+element+'</process><collaboration id="c"><participant id="b"/><messageFlow id="f" sourceRef="tns:a" targetRef="tns:b"/></collaboration>'
                self.assertIn('message-endpoint-type',self.rules(body))

    def test_default_reference_requires_its_owners_outgoing_flow(self):
        base='<process id="p"><task id="a" DEFAULT/><task id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
        self.assertEqual(self.findings(base.replace('DEFAULT','default="f"')),[])
        self.assertIn('default-flow',self.rules(base.replace('DEFAULT','default="b"')))
        wrong=base.replace('DEFAULT','').replace('<task id="b"/>','<task id="b" default="f"/>')
        self.assertIn('default-flow',self.rules(wrong))

    def test_event_gateway_cardinality_uses_actual_flows(self):
        self.assertEqual(self.findings(GATEWAY),[])
        self.assertIn('event-gateway-cardinality',self.rules(GATEWAY.replace('<sequenceFlow id="h" sourceRef="g" targetRef="b"/>','')))

    def test_event_gateway_instantiation_contract(self):
        parallel=GATEWAY.replace('<eventBasedGateway id="g"/>','<eventBasedGateway id="g" eventGatewayType="Parallel"/>')
        self.assertIn('event-gateway-instantiation',self.rules(parallel))
        valid=parallel.replace('eventGatewayType="Parallel"','eventGatewayType="Parallel" instantiate=" 1 "')
        self.assertEqual(check_native(xml(valid),'bpmn','2.0.2')['errors'],[])
        incoming=valid.replace('</process>','<task id="extra"/><sequenceFlow id="x" sourceRef="extra" targetRef=" g "/></process>')
        self.assertIn('event-gateway-instantiation',self.rules(incoming))
        for trigger in ('timer','signal','conditional'):
            catch='<intermediateCatchEvent id="a"><'+trigger+'EventDefinition/></intermediateCatchEvent>'
            with self.subTest(trigger=trigger):
                self.assertIn('event-gateway-configuration',self.rules(valid.replace('<receiveTask id="a"/>',catch)))

    def test_choreography_gateway_allows_activities_and_checks_trigger_subset(self):
        body='<choreography id="c"><eventBasedGateway id="g"/><choreographyTask id="a"/><choreographyTask id="b"/><sequenceFlow id="f" sourceRef="g" targetRef="a"/><sequenceFlow id="h" sourceRef="g" targetRef="b"/></choreography>'
        self.assertEqual(self.findings(body),[])
        for trigger in ('timer','signal'):
            event='<intermediateCatchEvent id="a"><'+trigger+'EventDefinition/></intermediateCatchEvent>'
            self.assertEqual(self.findings(body.replace('<choreographyTask id="a"/>',event)),[])
        for trigger in ('message','conditional'):
            event='<intermediateCatchEvent id="a"><'+trigger+'EventDefinition/></intermediateCatchEvent>'
            self.assertIn('event-gateway-configuration',self.rules(body.replace('<choreographyTask id="a"/>',event)))

    def test_event_gateway_allowed_catch_trigger_matrix(self):
        for trigger in ('message','signal','timer','conditional'):
            with self.subTest(trigger=trigger):
                event='<intermediateCatchEvent id="a"><'+trigger+'EventDefinition/></intermediateCatchEvent>'
                other='<intermediateCatchEvent id="b"><timerEventDefinition/></intermediateCatchEvent>'
                self.assertEqual(self.findings(GATEWAY.replace('<receiveTask id="a"/>',event).replace('<receiveTask id="b"/>',other)),[])
        for trigger in ('error','cancel','compensate','link','escalation','terminate',None):
            with self.subTest(trigger=trigger):
                event='<intermediateCatchEvent id="a">'+('<'+trigger+'EventDefinition/>' if trigger else '')+'</intermediateCatchEvent>'
                self.assertIn('event-gateway-configuration',self.rules(GATEWAY.replace('<receiveTask id="a"/>',event)))

    def test_event_gateway_multiple_trigger_and_mixed_configuration(self):
        multiple='<intermediateCatchEvent id="a"><timerEventDefinition/><signalEventDefinition/></intermediateCatchEvent>'
        self.assertEqual(self.findings(GATEWAY.replace('<receiveTask id="a"/>',multiple)),[])
        mixed='<intermediateCatchEvent id="a"><messageEventDefinition/></intermediateCatchEvent>'
        self.assertIn('event-gateway-configuration',self.rules(GATEWAY.replace('<receiveTask id="a"/>',mixed)))

    def test_event_gateway_rejects_attached_events_and_additional_incoming(self):
        attached=GATEWAY.replace('</process>','<boundaryEvent id="be" attachedToRef="tns:a"/></process>')
        incoming=GATEWAY.replace('</process>','<task id="extra"/><sequenceFlow id="x" sourceRef="extra" targetRef="a"/></process>')
        for body in (attached,incoming):
            with self.subTest(body=body):
                self.assertIn('event-gateway-configuration',self.rules(body))

    def test_referenced_event_definitions_are_checked_in_event_context(self):
        timer='<timerEventDefinition id="t"/>'
        catch=GATEWAY.replace('<receiveTask id="a"/>','<intermediateCatchEvent id="a"><eventDefinitionRef>tns:t</eventDefinitionRef></intermediateCatchEvent>')+timer
        self.assertEqual(self.findings(catch),[])
        throw='<process id="p"><intermediateThrowEvent id="e"><eventDefinitionRef>tns:t</eventDefinitionRef></intermediateThrowEvent></process>'+timer
        self.assertIn('throw-trigger',self.rules(throw))
        cancel='<process id="p"><transaction id="tr"><endEvent id="e"><eventDefinitionRef>tns:c</eventDefinitionRef></endEvent></transaction></process><cancelEventDefinition id="c"/>'
        self.assertEqual(self.findings(cancel),[])

    def test_cancel_boundary_is_interrupting_in_transaction_and_choreography(self):
        for attached in ('<transaction id="a"/>','<choreographyTask id="a"/>'):
            container='choreography' if 'choreographyTask' in attached else 'process'
            base='<'+container+' id="p">'+attached+'<boundaryEvent id="e" attachedToRef="tns:a" CANCEL><eventDefinitionRef>tns:c</eventDefinitionRef></boundaryEvent></'+container+'><cancelEventDefinition id="c"/>'
            for value in ('','cancelActivity="true"','cancelActivity="1"'):
                with self.subTest(attached=attached,value=value):
                    self.assertEqual(self.findings(base.replace('CANCEL',value)),[])
            for value in ('false','0',' 0 '):
                with self.subTest(attached=attached,value=value):
                    self.assertIn('cancel-scope',self.rules(base.replace('CANCEL','cancelActivity="'+value+'"')))

    def test_boolean_one_is_not_a_way_to_evade_flow_restrictions(self):
        for node,rule in (('<subProcess id="a" triggeredByEvent="1"/>','event-subprocess-flow'),('<task id="a" isForCompensation="1"/>','compensation-flow')):
            with self.subTest(node=node):
                body='<process id="p">'+node+'<task id="b"/><sequenceFlow id="f" sourceRef="a" targetRef="b"/></process>'
                self.assertIn(rule,self.rules(body))

    def test_di_edges_reject_nonfinite_or_missing_coordinates(self):
        from bpmn_rule_fixtures import PAIRS
        good=PAIRS['di-edge'][0]
        self.assertEqual(self.findings(good),[])
        for bad in ('NaN','INF','-INF','nan','1e999'):
            with self.subTest(coordinate=bad):
                self.assertIn('di-edge',self.rules(good.replace('x="100"','x="'+bad+'"')))
        self.assertIn('di-edge',self.rules(good.replace('x="100" ','')))

    def test_initiator_qnames_cannot_alias_or_evade_membership(self):
        base='<choreography id="c"><participant id="x"/><participant id="y"/><choreographyTask id="t" initiatingParticipantRef="INIT"><participantRef>tns:x</participantRef></choreographyTask></choreography>'
        self.assertEqual(self.findings(base.replace('INIT','tns:x')),[])
        self.assertIn('choreography-participants',self.rules(base.replace('INIT','tns:y')))
        errors,blocked=validate_references(safe_xml(xml(base.replace('INIT','foreign:x'))))
        self.assertEqual(errors,[])
        self.assertTrue(blocked)


if __name__=='__main__':
    unittest.main()
