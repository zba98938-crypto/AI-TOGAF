"""Adversarial delivery/recovery cases with independently specified outcomes."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import subprocess

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
sys.path.insert(0,str(ROOT/'tests'))
from business_exercise import recovery,risk_analysis,quality_analysis
from enterprise.closure_cases import cases
from finalize_render import finalize
from bpmn_semantics import check as bpmn_check
from standards import safe_xml
from enterprise.agents import observed_review


class ReviewEvidenceTests(unittest.TestCase):
    def test_actor_claim_and_unviewed_additional_image_cannot_establish_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);events=root/'events.jsonl'
            events.write_text(json.dumps({'type':'item.completed','item':{'type':'agent_message','text':'all reviewed'}})+'\n')
            r=observed_review(events,[root/'first.png',root/'second.png'],root/'first.png')
            self.assertFalse(r['inspection_observed']);self.assertFalse(r['all_images_observed'])
            events.write_text('\n'.join(json.dumps(e) for e in [
                {'type':'item.completed','item':{'type':'command_execution','exit_code':0,'command':'cat rubric.json actor-events.jsonl actual-output/result.json'}},
                {'type':'item.completed','item':{'type':'mcp_tool_call','tool':'view_image','status':'completed','arguments':{'path':str(root/'second.png')}}}]))
            r=observed_review(events,[root/'first.png',root/'second.png'],root/'first.png')
            self.assertTrue(r['inspection_observed']);self.assertTrue(r['all_images_observed'])


class ExecutableRecoveryTests(unittest.TestCase):
    def test_restore_replays_durable_events_exactly_once_after_corruption(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'run';r=recovery(out)
            self.assertTrue(r['recovery_success']);self.assertEqual(r['applied_events'],100)
            self.assertEqual(r['second_replay_duplicates'],110)
            self.assertEqual(json.loads((out/'actual-restored.json').read_text()),json.loads((out/'independent-expected.json').read_text()))
            self.assertGreater(r['observed_rto_seconds'],0);self.assertEqual(r['observed_rpo_seconds'],0)
            self.assertFalse(r['production_proof']);self.assertEqual(r['business_acceptance'],'pending')
    def test_every_failure_has_an_explicit_non_success_terminal(self):
        for fault,expected in [('invalid-restore','abort-and-escalate'),('restore-failure','manual-compensation-and-escalate'),('inconsistent','manual-compensation-and-escalate'),('settlement-failure','manual-reconciliation-no-automatic-undo')]:
            with self.subTest(fault=fault),tempfile.TemporaryDirectory() as tmp:
                r=recovery(Path(tmp)/'run',fault)
                self.assertFalse(r['recovery_success']);self.assertEqual(r['terminal'],expected)
                self.assertIsNone(r['observed_rto_seconds'])
                if fault=='settlement-failure':
                    side_effect=json.loads((Path(tmp)/'run/external-settlement-test-double.json').read_text())
                    self.assertTrue(side_effect['sent']);self.assertFalse(side_effect['automatic_undo'])


class RiskBoundaryTests(unittest.TestCase):
    def setUp(self):self.raw=copy.deepcopy(cases()[0]['raw'])
    def test_five_boundaries_and_residual_scores_have_independent_expected_decisions(self):
        r=risk_analysis(self.raw)
        self.assertEqual([v['disposition'] for v in r['boundary_checks']],['within-appetite','within-appetite','escalate','escalate','do-not-enter-change'])
        self.assertEqual([v['gross_score'] for v in r['scenarios']],[10,15])
        self.assertEqual([v['residual_score'] for v in r['scenarios']],[5,9])
        self.assertEqual(r['risk_acceptance'],'pending')
    def test_missing_scale_control_or_stale_policy_cannot_produce_decisions(self):
        for change in ('scale','control','stale','residual','boundary'):
            with self.subTest(change=change):
                raw=copy.deepcopy(self.raw)
                if change=='scale':del raw['scales']['impact_definitions']['2']
                if change=='control':raw['control_evidence']=[]
                if change=='stale':raw['period_end']='2024-09-30'
                if change=='residual':raw['scenarios'][0]['residual_score']=1
                if change=='boundary':raw['boundary_cases'][2]['impact']=2
                with self.assertRaises(ValueError):risk_analysis(raw)


class QualityGateTests(unittest.TestCase):
    def test_ratio_pass_cannot_hide_failed_zero_null_key_control(self):
        r=quality_analysis(cases()[1]['raw'])
        self.assertEqual(r['valid_ratio'],'0.98');self.assertTrue(r['ratio_pass'])
        self.assertFalse(r['key_pass']);self.assertEqual(r['overall_quality_gate'],'fail')
        self.assertEqual(r['quarantined'],20);self.assertEqual(r['business_acceptance'],'pending')
    def test_missing_conflicting_and_reconciliation_inputs_block_acceptance(self):
        for mode in ('missing','conflict','reconcile','owner'):
            raw=copy.deepcopy(cases()[1]['raw'])
            if mode=='missing':del raw['quality_policy']
            if mode=='conflict':raw['conflicting_policy']={'valid_ratio':.99}
            if mode=='reconcile':raw['observations']['valid']=999
            if mode=='owner':raw['defects'][0]['owner']=''
            with self.subTest(mode=mode),self.assertRaises(ValueError):quality_analysis(raw)


class RenderFinalizationTests(unittest.TestCase):
    def fixture(self,root):
        from PIL import Image
        (root/'artifacts').mkdir();model={'project':{'version':'1'}}
        (root/'model.json').write_text(json.dumps(model))
        (root/'artifacts/view.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50" viewBox="0 0 100 50"><text x="2" y="20">saved</text></svg>')
        (root/'artifacts/view.md').write_text('PNG 尚未渲染；使用 --render。可编辑源与模型见同目录。\n')
        (root/'index.md').write_text('# Delivery\n')
        Image.new('RGB',(100,50),'white').save(root/'artifacts/view.png')
        sha=lambda p:hashlib.sha256((root/p).read_bytes()).hexdigest()
        manifest={'model_sha256':hashlib.sha256(json.dumps(model,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
                  'artifacts':[{'view_id':'view','path':'artifacts/view.md','svg':'artifacts/view.svg','png':None,'status':'generated-awaiting-review'}],
                  'output_sha256':{p:sha(p) for p in ['model.json','artifacts/view.md','artifacts/view.svg','index.md']},'rendered':False}
        (root/'manifest.json').write_text(json.dumps(manifest))
        report={'status':'passed','results':[{'id':'view','png':'view.png','svg_sha256':sha('artifacts/view.svg'),'png_sha256':sha('artifacts/view.png'),'width':100,'height':50}]}
        (root/'render-report.json').write_text(json.dumps(report))
    def test_supplemental_render_synchronizes_hashes_and_readable_status_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);self.fixture(root);first=finalize(root);second=finalize(root)
            self.assertEqual(first,second);self.assertTrue(first['rendered'])
            self.assertNotIn('PNG 尚未渲染',(root/'artifacts/view.md').read_text())
            self.assertEqual(first['artifacts'][0]['status'],'generated-awaiting-review')
            self.assertEqual(first['artifacts'][0]['png'],'artifacts/view.png')
            for name,digest in first['output_sha256'].items():self.assertEqual(hashlib.sha256((root/name).read_bytes()).hexdigest(),digest)
    def test_invalid_inputs_cannot_mutate_delivery(self):
        for mode in ('missing','fake','hash','model','escape','sealed'):
            with self.subTest(mode=mode),tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);self.fixture(root)
                if mode=='missing':(root/'artifacts/view.png').unlink()
                if mode=='fake':
                    (root/'artifacts/view.png').write_bytes(b'not a PNG')
                    p=root/'render-report.json';r=json.loads(p.read_text());r['results'][0]['png_sha256']=hashlib.sha256(b'not a PNG').hexdigest();p.write_text(json.dumps(r))
                if mode=='hash':(root/'artifacts/view.svg').write_text('changed')
                if mode=='model':(root/'model.json').write_text('{}')
                if mode=='escape':
                    p=root/'render-report.json';r=json.loads(p.read_text());r['results'][0]['png']='../../outside.png';p.write_text(json.dumps(r))
                if mode=='sealed':(root/'evidence-sha256.json').write_text('{}')
                before={str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*') if p.is_file()}
                with self.assertRaises((ValueError,OSError)):finalize(root)
                self.assertEqual(before,{str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*') if p.is_file()})


class BPMNBehaviorTests(unittest.TestCase):
    def test_each_implemented_family_has_authored_positive_and_negative(self):
        from bpmn_rule_fixtures import PAIRS,document
        from bpmn_semantics import RULES
        self.assertEqual(set(PAIRS),set(RULES))
        for identity,(positive,negative) in PAIRS.items():
            with self.subTest(rule=identity):
                self.assertEqual(bpmn_check(safe_xml(document(positive)))['findings'],[])
                self.assertIn(identity,{f['rule_id'] for f in bpmn_check(safe_xml(document(negative)))['findings']})
    def check(self,body):
        xml='<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" targetNamespace="urn:test">'+body+'</definitions>'
        return bpmn_check(safe_xml(xml.encode()))['findings']
    def test_event_direction_uses_actual_flows_even_if_incoming_tags_omitted(self):
        f=self.check('<process id="p"><task id="a"/><startEvent id="s"/><sequenceFlow id="f" sourceRef="a" targetRef="s"/></process>')
        self.assertIn('event-direction',[r['rule_id'] for r in f])
    def test_nested_scope_and_invalid_boundary_attachment_rejected(self):
        f=self.check('<process id="p"><task id="a"/><subProcess id="sub"><task id="b"/></subProcess><sequenceFlow id="f" sourceRef="a" targetRef="b"/><exclusiveGateway id="g"/><boundaryEvent id="be" attachedToRef="g"/></process>')
        self.assertTrue({'sequence-scope','boundary-attachment'}<={r['rule_id'] for r in f})
    def test_valid_subprocess_flow_and_boundary_attachment_not_rejected(self):
        self.assertEqual(self.check('<process id="p"><task id="a"/><subProcess id="sub"><startEvent id="s"/><task id="b"/><sequenceFlow id="f" sourceRef="s" targetRef="b"/></subProcess><boundaryEvent id="be" attachedToRef="a"/></process>'),[])
    def test_gateway_and_throw_event_semantics(self):
        f=self.check('<process id="p"><eventBasedGateway id="g"/><task id="a"/><sequenceFlow id="f" sourceRef="g" targetRef="a"/><endEvent id="e"><timerEventDefinition id="timer"/></endEvent></process>')
        self.assertTrue({'event-gateway-target','throw-trigger'}<={r['rule_id'] for r in f})


class ActualConnectorGeometryTests(unittest.TestCase):
    def test_horizontal_strokes_count_but_empty_metadata_does_not(self):
        resolver=(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts/browser_resolver.mjs').as_uri()
        checker=(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts/diagram_quality.mjs').as_uri()
        script='import {launchBrowser} from '+json.dumps(resolver)+';import {inspect} from '+json.dumps(checker)+''';
const browser=await launchBrowser();
try {
 const page=await browser.newPage();
 const body='<svg xmlns="http://www.w3.org/2000/svg" width="500" height="160"><defs><marker id="arrow" orient="auto" markerWidth="10" markerHeight="10" refX="10" refY="5"><path d="M0 0 L10 5 L0 10Z"/></marker></defs><g data-entity-id="a"><rect x="10" y="30" width="100" height="80"/></g><g data-entity-id="b"><rect x="300" y="30" width="100" height="80"/></g>CONNECTOR</svg>';
 const expected={entity_ids:['a','b'],relationships:[{id:'r',source:'a',target:'b',label:''}]};
 await page.setContent(body.replace('CONNECTOR','<path data-relationship-id="r" d="M110 70 L300 70" stroke="black" marker-end="url(#arrow)"/>'));
 const good=await inspect(page,expected);
 await page.setContent(body.replace('CONNECTOR','<metadata data-relationship-id="r">stored only</metadata><g data-relationship-id="r"/>'));
 const empty=await inspect(page,expected);
 if(good.findings.length||!empty.findings.some(f=>f.code==='relationship-no-visible-connector'))throw Error(JSON.stringify({good,empty}));
} finally {await browser.close();}
'''
        result=subprocess.run(['node','--input-type=module','-e',script],capture_output=True,text=True,timeout=30)
        self.assertEqual(result.returncode,0,result.stderr)


if __name__=='__main__':unittest.main()
