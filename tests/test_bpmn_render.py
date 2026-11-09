"""Native notation evidence and DI omission counterexamples, independent of project diagrams."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import Invalid, Incomplete, safe_xml
from bpmn_render import diagram_plan, render_native, DI

BPMN='''<?xml version="1.0" encoding="utf-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" targetNamespace="urn:independent:bpmn-notation">
 <process id="ORDER" isExecutable="false">
  <laneSet id="LANES"><lane id="INTAKE" name="受理"><flowNodeRef>START</flowNodeRef><flowNodeRef>VALIDATE</flowNodeRef><flowNodeRef>CHOICE</flowNodeRef><flowNodeRef>RESERVE</flowNodeRef><flowNodeRef>REPLY</flowNodeRef><flowNodeRef>TIMER</flowNodeRef></lane><lane id="FULFIL" name="履约"><flowNodeRef>MANUAL</flowNodeRef><flowNodeRef>REJECT</flowNodeRef><flowNodeRef>SUB</flowNodeRef><flowNodeRef>END</flowNodeRef></lane></laneSet>
  <startEvent id="START" name="订单到达"><messageEventDefinition id="TRIGGER"/></startEvent>
  <userTask id="VALIDATE" name="人工核验"/>
  <boundaryEvent id="TIMER" name="超时" attachedToRef="VALIDATE"><timerEventDefinition id="TIMEOUT"/></boundaryEvent>
  <exclusiveGateway id="CHOICE" name="可履约？"/>
  <serviceTask id="RESERVE" name="库存预占"/>
  <sendTask id="REPLY" name="确认订单"/>
  <manualTask id="MANUAL" name="人工处置"/>
  <endEvent id="REJECT" name="关闭订单"/>
  <subProcess id="SUB" name="履约子流程"><startEvent id="SUB_START"/><task id="PICK" name="拣货复核"/><endEvent id="SUB_END"/><sequenceFlow id="SF1" sourceRef="SUB_START" targetRef="PICK"/><sequenceFlow id="SF2" sourceRef="PICK" targetRef="SUB_END"/></subProcess>
  <endEvent id="END" name="完成履约"/>
  <sequenceFlow id="F1" sourceRef="START" targetRef="VALIDATE"/>
  <sequenceFlow id="F2" sourceRef="VALIDATE" targetRef="CHOICE"/>
  <sequenceFlow id="F3" name="是" sourceRef="CHOICE" targetRef="RESERVE"/>
  <sequenceFlow id="F4" sourceRef="RESERVE" targetRef="REPLY"/>
  <sequenceFlow id="F5" sourceRef="REPLY" targetRef="SUB"/>
  <sequenceFlow id="F6" sourceRef="SUB" targetRef="END"/>
  <sequenceFlow id="F7" name="否" sourceRef="CHOICE" targetRef="MANUAL"/>
  <sequenceFlow id="F8" sourceRef="TIMER" targetRef="MANUAL"/>
  <sequenceFlow id="F9" sourceRef="MANUAL" targetRef="REJECT"/>
 </process>
 <collaboration id="COLLAB"><participant id="OPERATIONS" name="订单运营" processRef="ORDER"/><participant id="CUSTOMER" name="客户系统"/><messageFlow id="MESSAGE" name="订单确认" sourceRef="REPLY" targetRef="CUSTOMER"/></collaboration>
 <bpmndi:BPMNDiagram id="DIAGRAM"><bpmndi:BPMNPlane id="PLANE" bpmnElement="COLLAB">
  <bpmndi:BPMNShape id="OPERATIONS_DI" bpmnElement="OPERATIONS" isHorizontal="true"><dc:Bounds x="40" y="60" width="1440" height="500"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="INTAKE_DI" bpmnElement="INTAKE" isHorizontal="true"><dc:Bounds x="70" y="60" width="1410" height="220"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="FULFIL_DI" bpmnElement="FULFIL" isHorizontal="true"><dc:Bounds x="70" y="280" width="1410" height="280"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="START_DI" bpmnElement="START"><dc:Bounds x="120" y="160" width="36" height="36"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="VALIDATE_DI" bpmnElement="VALIDATE"><dc:Bounds x="200" y="138" width="100" height="80"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="TIMER_DI" bpmnElement="TIMER"><dc:Bounds x="257" y="200" width="36" height="36"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="CHOICE_DI" bpmnElement="CHOICE" isMarkerVisible="true"><dc:Bounds x="335" y="153" width="50" height="50"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="RESERVE_DI" bpmnElement="RESERVE"><dc:Bounds x="430" y="138" width="100" height="80"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="REPLY_DI" bpmnElement="REPLY"><dc:Bounds x="580" y="138" width="100" height="80"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="MANUAL_DI" bpmnElement="MANUAL"><dc:Bounds x="390" y="355" width="100" height="80"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="REJECT_DI" bpmnElement="REJECT"><dc:Bounds x="560" y="377" width="36" height="36"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="SUB_DI" bpmnElement="SUB" isExpanded="true"><dc:Bounds x="760" y="300" width="460" height="220"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="SUB_START_DI" bpmnElement="SUB_START"><dc:Bounds x="810" y="392" width="36" height="36"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="PICK_DI" bpmnElement="PICK"><dc:Bounds x="910" y="370" width="100" height="80"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="SUB_END_DI" bpmnElement="SUB_END"><dc:Bounds x="1110" y="392" width="36" height="36"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="END_DI" bpmnElement="END"><dc:Bounds x="1300" y="392" width="36" height="36"/></bpmndi:BPMNShape>
  <bpmndi:BPMNShape id="CUSTOMER_DI" bpmnElement="CUSTOMER" isHorizontal="true"><dc:Bounds x="40" y="630" width="1440" height="100"/></bpmndi:BPMNShape>
  <bpmndi:BPMNEdge id="F1_DI" bpmnElement="F1"><di:waypoint x="156" y="178"/><di:waypoint x="200" y="178"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F2_DI" bpmnElement="F2"><di:waypoint x="300" y="178"/><di:waypoint x="335" y="178"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F3_DI" bpmnElement="F3"><di:waypoint x="385" y="178"/><di:waypoint x="430" y="178"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F4_DI" bpmnElement="F4"><di:waypoint x="530" y="178"/><di:waypoint x="580" y="178"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F5_DI" bpmnElement="F5"><di:waypoint x="680" y="178"/><di:waypoint x="735" y="178"/><di:waypoint x="735" y="410"/><di:waypoint x="760" y="410"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F6_DI" bpmnElement="F6"><di:waypoint x="1220" y="410"/><di:waypoint x="1300" y="410"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F7_DI" bpmnElement="F7"><di:waypoint x="360" y="203"/><di:waypoint x="360" y="375"/><di:waypoint x="390" y="375"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F8_DI" bpmnElement="F8"><di:waypoint x="275" y="236"/><di:waypoint x="275" y="410"/><di:waypoint x="390" y="410"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="F9_DI" bpmnElement="F9"><di:waypoint x="490" y="395"/><di:waypoint x="560" y="395"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="SF1_DI" bpmnElement="SF1"><di:waypoint x="846" y="410"/><di:waypoint x="910" y="410"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="SF2_DI" bpmnElement="SF2"><di:waypoint x="1010" y="410"/><di:waypoint x="1110" y="410"/></bpmndi:BPMNEdge>
  <bpmndi:BPMNEdge id="MESSAGE_DI" bpmnElement="MESSAGE"><di:waypoint x="630" y="218"/><di:waypoint x="630" y="600"/><di:waypoint x="600" y="600"/><di:waypoint x="600" y="630"/></bpmndi:BPMNEdge>
 </bpmndi:BPMNPlane></bpmndi:BPMNDiagram>
</definitions>'''.encode('utf-8')


def without(xpath):
    root=safe_xml(BPMN)
    for e in root.xpath(xpath):e.getparent().remove(e)
    return etree.tostring(root)


class BpmnNotationTests(unittest.TestCase):
    def test_complete_di_preserves_declared_nodes_and_flows(self):
        plan=diagram_plan(BPMN)
        self.assertEqual(17,len(plan['shape_ids']))
        self.assertEqual(12,len(plan['edge_ids']))
        self.assertIn('TIMER',plan['shape_ids'])
        self.assertIn('PICK',plan['shape_ids'])
        self.assertEqual([],plan['native_validation']['errors'])

    def test_missing_di_is_blocked(self):
        with self.assertRaisesRegex(Incomplete,'exactly one explicit BPMNDiagram'):
            diagram_plan(without('//*[local-name()="BPMNDiagram"]'))

    def test_missing_visible_node_di_is_blocked(self):
        with self.assertRaisesRegex(Incomplete,'Missing BPMNDI.*VALIDATE'):
            diagram_plan(without('//*[@id="VALIDATE_DI"]'))

    def test_missing_flow_di_is_blocked(self):
        with self.assertRaisesRegex(Incomplete,'Missing BPMNDI.*MESSAGE'):
            diagram_plan(without('//*[@id="MESSAGE_DI"]'))

    def test_expanded_subprocess_requires_child_di(self):
        with self.assertRaisesRegex(Incomplete,'Missing BPMNDI.*PICK'):
            diagram_plan(without('//*[@id="PICK_DI"]'))

    def test_nonfinite_edge_waypoint_is_rejected(self):
        with self.assertRaisesRegex(Invalid,'finite waypoints'):
            diagram_plan(BPMN.replace(b'x="156" y="178"',b'x="NaN" y="178"'))

    def test_collapsed_subprocess_renders_only_visible_contract(self):
        root=safe_xml(BPMN)
        root.xpath('//*[@id="SUB_DI"]')[0].set('isExpanded','false')
        for ident in ('SUB_START_DI','PICK_DI','SUB_END_DI','SF1_DI','SF2_DI'):
            element=root.xpath('//*[@id="'+ident+'"]')[0];element.getparent().remove(element)
        plan=diagram_plan(etree.tostring(root))
        self.assertNotIn('PICK',plan['shape_ids'])
        self.assertNotIn('SF1',plan['edge_ids'])
        self.assertIn('SUB',plan['shape_ids'])
        self.assertIn('PICK',{i['id'] for i in plan['hidden_native_elements']})
        self.assertIn('SF1',{i['id'] for i in plan['hidden_native_elements']})

    def test_actual_native_renderer_and_public_cli(self):
        with tempfile.TemporaryDirectory(prefix='native-bpmn-test-') as tmp:
            folder=Path(tmp);source=folder/'source.bpmn';source.write_bytes(BPMN)
            run=subprocess.run([sys.executable,'-B',str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts/standards.py'),'render','--language','bpmn','--version','2.0.2','--input',str(source),'--out',str(folder/'order.svg')],capture_output=True,text=True,timeout=120)
            self.assertEqual(0,run.returncode,run.stdout+run.stderr)
            report=json.loads(run.stdout)
            self.assertEqual('rendered-explicit-bpmndi',report['notation_status'])
            self.assertEqual('incomplete',report['conformance_status'])
            self.assertFalse(report['full_language_acceptance'])
            self.assertEqual([],report['warnings'])
            self.assertEqual(17,len(report['shape_ids']))
            self.assertEqual(12,len(report['edge_ids']))
            self.assertEqual(b'\x89PNG\r\n\x1a\n',(folder/'order.png').read_bytes()[:8])
            svg=(folder/'order.svg').read_text()
            self.assertNotIn('<!DOCTYPE',svg)
            self.assertIn('人工核验',svg)
            self.assertIn('marker-end',svg)
            self.assertNotIn("url('#",svg)
            self.assertTrue((folder/'order.render.json').is_file())
            with self.assertRaisesRegex(Invalid,'overwrite'):render_native(BPMN,folder/'order.svg')

    def test_public_cli_no_di_returns_structured_blocked_result(self):
        with tempfile.TemporaryDirectory(prefix='native-bpmn-no-di-') as tmp:
            folder=Path(tmp);source=folder/'source.bpmn';source.write_bytes(without('//*[local-name()="BPMNDiagram"]'))
            run=subprocess.run([sys.executable,'-B',str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts/standards.py'),'render','--language','bpmn','--version','2.0.2','--input',str(source),'--out',str(folder/'order.svg')],capture_output=True,text=True,timeout=30)
            self.assertEqual(3,run.returncode,run.stdout+run.stderr)
            self.assertEqual('blocked',json.loads(run.stdout)['status'])
            self.assertFalse((folder/'order.svg').exists())
            self.assertFalse((folder/'order.png').exists())


if __name__=='__main__':unittest.main()
