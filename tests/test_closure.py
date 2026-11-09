"""Independent mutations and XML fixtures; no native/model session consumption."""
import copy,json,sys,tempfile,time,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from closure_semantics import check
from enterprise_closure import build
from standards import (Invalid,Incomplete,safe_xml,make_package,package_bytes,check_native,catalog,moddle)
from enterprise.campaign import CampaignBudget
from enterprise.runtime import Blocked

BASE={'schema_version':'2.0','project':{'id':'independent-test','name':'独立合成企业','version':'1','is_example':True,'context':{'domains':['business','data','application','technology'],'landscape':'segment','purpose':'project','abstraction':'logical','evolution':'baseline'},'approval_status':'candidate','implementation_status':'not-started'},'sources':[],'entities':[],'relationships':[],'views':[],'deliverables':[],'gaps':[]}
BPMN=b'''<?xml version="1.0"?><definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" targetNamespace="urn:independent"><process id="P" isExecutable="false"><startEvent id="S"><outgoing>F1</outgoing></startEvent><task id="T"><incoming>F1</incoming><outgoing>F2</outgoing></task><endEvent id="E"><incoming>F2</incoming></endEvent><sequenceFlow id="F1" sourceRef="S" targetRef="T"/><sequenceFlow id="F2" sourceRef="T" targetRef="E"/></process></definitions>'''
UML=b'''<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:version="2.5.1" xmi:id="M" name="Independent"><packagedElement xmi:type="uml:Class" xmi:id="C" name="Order"/></uml:Model>'''

class ClosureContractTests(unittest.TestCase):
    def setUp(self):self.model=build(BASE);self.c=self.model['extension_data']['enterprise:closure']
    def codes(self):return {i['code'] for i in check(self.model)}
    def test_positive_complete_simulation(self):self.assertEqual(check(self.model),[])
    def test_state_details_cannot_be_only_labels(self):
        for e in self.model['entities']:
            if e.get('concept_id')=='order-event':e['attributes']['architecture_detail']['summary']='same'
        self.assertIn('architecture-state-difference',self.codes())
    def test_state_interface_contract_is_cross_view_consistent(self):
        next(e for e in self.model['entities'] if e['id']=='closure-interface-target')['attributes']['schema_id']='WRONG'
        self.assertIn('architecture-interface-contract',self.codes())
    def test_state_detail_requires_owner(self):
        next(e for e in self.model['entities'] if e.get('concept_id')=='order-event')['attributes']['architecture_detail'].pop('owner_id')
        self.assertIn('architecture-state-detail',self.codes())
    def test_no_opt_in_does_not_force_full_adm(self):self.assertEqual(check(BASE),[])
    def test_simulation_never_approves(self):self.model['project']['approval_status']='approved';self.assertIn('synthetic-authority',self.codes())
    def test_simulation_never_realizes(self):self.model['entities'][0]['implementation_status']='realized';self.assertIn('synthetic-authority',self.codes())
    def test_missing_evidence_period(self):del self.c['evidence_records'][0]['period_start'];self.assertIn('evidence-required',self.codes())
    def test_stale_evidence(self):self.c['evidence_records'][0]['period_end']='2025-09-30';self.assertIn('evidence-stale',self.codes())
    def test_future_evidence(self):self.c['evidence_records'][0]['period_end']='2027-09-30';self.assertIn('evidence-period',self.codes())
    def test_wrong_ratio(self):self.c['evidence_records'][0]['value']=.8;self.assertIn('evidence-calculation',self.codes())
    def test_zero_denominator(self):self.c['evidence_records'][0]['denominator']=0;self.assertIn('evidence-denominator',self.codes())
    def test_fake_rule_authority(self):self.c['rules'][0]['authority']='real-approved';self.assertIn('rule-authority',self.codes())
    def test_conflicting_policy(self):r=copy.deepcopy(self.c['rules'][0]);r.update(id='conflict',threshold=.5);self.c['rules'].append(r);self.assertIn('conflicting-rule',self.codes())
    def test_no_owner(self):self.c['evidence_records'][0]['owner_id']='missing';self.assertIn('evidence-owner',self.codes())
    def test_missing_guard(self):next(e for e in self.model['relationships'] if e['type']=='branches')['attributes']={};self.assertIn('branch-guard',self.codes())
    def test_non_exhaustive_guard(self):next(e for e in self.model['relationships'] if e['type']=='branches')['attributes']['guard']['value']='unknown';self.assertIn('branch-partition',self.codes())
    def test_compensation_is_explicit(self):next(e for e in self.model['entities'] if e['id']=='closure-flow-restore')['attributes'].pop('compensation_id');self.assertIn('compensation-missing',self.codes())
    def test_irreversible_operation_needs_exit(self):self.model['relationships']=[e for e in self.model['relationships'] if e['type']!='enterprise:failure_exit'];self.assertIn('irreversible-exit',self.codes())
    def test_terminal_has_no_outgoing(self):self.c['flows'][0]['terminal_ids'].append('closure-flow-settle');self.assertIn('flow-terminal',self.codes())
    def test_control_cannot_be_generic_trace(self):next(e for e in self.model['relationships'] if e['type']=='branches')['type']='traces_to';self.assertIn('flow-semantic',self.codes())
    def test_missing_adm_domain(self):del self.c['adm_chain'][3];self.assertIn('adm-chain-stages',self.codes())
    def test_no_real_recovery_claim(self):self.c['recovery_exercises'][0]['production_proof']=True;self.assertIn('recovery-authority',self.codes())
    def test_existing_validator_integrates_closure(self):
        from validate import validate
        self.model['project']['approval_status']='approved';self.assertIn('synthetic-authority',{i['code'] for i in validate(self.model)})
    def test_operation_outcomes_need_guards(self):
        next(e for e in self.model['relationships'] if e['type']=='enterprise:compensates')['attributes']={};self.assertIn('operation-outcomes',self.codes())
    def test_symbolic_happy_path(self):
        from closure_simulator import replay
        r=replay(self.model,'closure-rollback',{'restore_valid':True,'restore_result':'success','consistent':True,'settlement_result':'confirmed'})
        self.assertEqual(r['terminal_id'],'closure-flow-done');self.assertTrue(all(e['actual_operation_executed'] is False for e in r['events']))
    def test_symbolic_missing_restore_point(self):
        from closure_simulator import replay
        self.assertEqual(replay(self.model,'closure-rollback',{'restore_valid':False})['terminal_id'],'closure-flow-abort')
    def test_symbolic_restore_failure_compensates(self):
        from closure_simulator import replay
        r=replay(self.model,'closure-rollback',{'restore_valid':True,'restore_result':'failure'})
        self.assertIn('enterprise:compensates',[e['semantic'] for e in r['events']]);self.assertFalse(r['production_proof'])
    def test_symbolic_irreversible_failure_goes_to_human(self):
        from closure_simulator import replay
        r=replay(self.model,'closure-rollback',{'restore_valid':True,'restore_result':'success','consistent':True,'settlement_result':'failure'})
        self.assertIn('enterprise:failure_exit',[e['semantic'] for e in r['events']]);self.assertEqual(r['terminal_id'],'closure-flow-abort')
    def test_symbolic_guard_data_is_required(self):
        from closure_simulator import replay
        with self.assertRaisesRegex(ValueError,'missing guard'):replay(self.model,'closure-rollback',{})
    def test_endpoint_constraint(self):
        from validate import validate
        next(e for e in self.model['relationships'] if e['type']=='member_of')['target']='closure-requirement';self.assertTrue(any(i['level']=='error' and 'endpoint' in i['code'] for i in validate(self.model)))

    def test_missing_transition_operating_dimensions_are_not_hidden_in_entity_details(self):
        state=next(s for s in self.model['states'] if s['evolution']=='transition')
        for field in ('operations','data_consistency','dependencies','controls','rollback'):
            changed=copy.deepcopy(self.model);next(s for s in changed['states'] if s['evolution']=='transition')['operating_conditions'].pop(field)
            self.assertIn('transition-operability',{r['code'] for r in check(changed)})
    def test_stopped_order_intake_is_not_an_operable_transition(self):
        next(s for s in self.model['states'] if s['evolution']=='transition')['operating_conditions']['order_intake']='disabled'
        self.assertIn('transition-order-intake',self.codes())

class NativeLanguageTests(unittest.TestCase):
    def test_archimate_four_publication_metadata_is_not_normative_acquisition(self):
        report=catalog('archimate','4')
        self.assertEqual(report['official_publication']['id'],'C260')
        self.assertFalse(report['official_publication']['normative_content_acquired'])
        self.assertFalse(report['official_publication']['license_accepted'])
        self.assertEqual(report['source_status'],'blocked')
        with self.assertRaises(Incomplete):check_native(UML,'archimate','4')
    def test_archimate_four_does_not_substitute_previous_version(self):
        with self.assertRaises(Invalid):catalog('archimate','3.2')
    def test_official_bpmn_xsd_and_independent_semantics(self):self.assertEqual(check_native(BPMN,'bpmn','2.0.2')['errors'],[])
    def test_bpmn_roundtrip_preserves_native_bytes(self):
        p=make_package(BPMN,'bpmn','2.0.2');export=package_bytes(p,'bpmn','2.0.2');q=make_package(export,'bpmn','2.0.2');self.assertEqual(p['native_inventory'],q['native_inventory']);self.assertEqual(export,BPMN)
    def test_uml_roundtrip_preserves_native_ids(self):self.assertEqual(package_bytes(make_package(UML,'uml','2.5.1'),'uml','2.5.1'),UML)
    def test_doctype_xxe_rejected(self):
        with self.assertRaises(Invalid):safe_xml(b'<!DOCTYPE x [<!ENTITY a SYSTEM "file:///etc/passwd">]><x>&a;</x>')
    def test_duplicate_native_id(self):self.assertTrue(check_native(BPMN.replace(b'id="E"',b'id="T"'),'bpmn','2.0.2')['errors'])
    def test_dangling_reference(self):self.assertTrue(check_native(BPMN.replace(b'targetRef="E"',b'targetRef="UNKNOWN"'),'bpmn','2.0.2')['errors'])
    def test_cross_process_flow(self):
        data=BPMN.replace(b'<endEvent id="E"><incoming>F2</incoming></endEvent>',b'').replace(b'</definitions>',b'<process id="Other"><endEvent id="E"/></process></definitions>')
        self.assertTrue(any('crosses process' in e for e in check_native(data,'bpmn','2.0.2')['errors']))
    def test_no_false_full_language_pass(self):self.assertEqual(check_native(BPMN,'bpmn','2.0.2')['conformance_status'],'incomplete')
    def test_no_archimate_32_substitute(self):
        with self.assertRaises(Invalid):catalog('archimate','3.2')
        self.assertEqual(catalog('archimate','4')['source_status'],'blocked')
    def test_payload_tamper(self):
        p=make_package(BPMN,'bpmn','2.0.2');p['native_sha256']='bad'
        with self.assertRaises(Invalid):package_bytes(p,'bpmn','2.0.2')
    def test_inventory_edit_rejected(self):
        p=make_package(BPMN,'bpmn','2.0.2');p['native_inventory'][0]['tag']='changed'
        with self.assertRaises(Invalid):package_bytes(p,'bpmn','2.0.2')
    def test_no_xmi_path_escape(self):
        with tempfile.TemporaryDirectory() as tmp:self.assertTrue(check_native(UML.replace(b'/></uml:Model>',b'/><type href="../outside.xmi#X"/></uml:Model>'),'uml','2.5.1',tmp)['errors'])
    def test_remote_href_is_never_resolved(self):
        data=UML.replace(b'/></uml:Model>',b'/><type href="https://example.com/remote.xmi#X"/></uml:Model>');self.assertTrue(any('never fetched' in b for b in check_native(data,'uml','2.5.1')['blockers']))
    def test_catalog_includes_all_normative_constructs_without_hiding_gaps(self):
        for language,version in [('bpmn','2.0.2'),('uml','2.5.1')]:
            c=catalog(language,version);self.assertGreater(c['construct_count'],100);self.assertTrue(all(e['conformance_tests']=='uncovered' for e in c['constructs']))
    def test_actual_moddle_backend_reads_and_writes(self):
        output,info=moddle(BPMN);self.assertIn(b'id="F1"',output);self.assertEqual(info['version'],'10.3.1');self.assertEqual(info['warnings'],[])

class CampaignTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.b=CampaignBudget(Path(self.tmp.name));self.b.free_limit=0
    def tearDown(self):self.b.close();self.tmp.cleanup()
    def test_two_timeout_circuit(self):
        self.b.observe_session('timeout');self.b.observe_session('timeout')
        with self.assertRaisesRegex(Blocked,'two consecutive'):self.b.begin_batch()
    def test_two_429_circuit(self):
        self.b.observe_http(429);self.b.observe_http(429)
        with self.assertRaises(Blocked):self.b.begin_batch()
    def test_success_resets_consecutive_counter(self):self.b.observe_http(429);self.b.observe_http(200);self.b.observe_http(429);self.assertFalse(self.b.cancel.is_set())
    def test_resume_does_not_reset_batch_clock(self):self.b.begin_batch();start=self.b.batch_started_wall;self.b.begin_batch(resume=True);self.assertEqual(self.b.batch_started_wall,start)
    def test_four_batch_limit(self):
        for _ in range(4):self.b.begin_batch();self.b.seal_batch("test complete")
        with self.assertRaisesRegex(Blocked,'four batch'):self.b.begin_batch()
    def test_active_batch_cannot_be_bypassed(self):
        self.b.begin_batch()
        with self.assertRaisesRegex(Blocked,'active batch'):self.b.begin_batch()
    def test_sealed_batch_cannot_resume(self):
        self.b.begin_batch();self.b.seal_batch('complete')
        with self.assertRaisesRegex(Blocked,'no active'):self.b.begin_batch(resume=True)
    def test_seal_preserves_history_and_global_clock(self):
        self.b.begin_batch();wall=self.b.started_wall;self.b.sessions=[{}]*17
        self.b.seal_batch('time boundary');self.b.begin_batch()
        self.assertEqual(self.b.started_wall,wall);self.assertEqual(self.b.batch_history[0]['sessions_used'],17)
    def test_dispatch_requires_active_batch(self):
        with self.assertRaisesRegex(Blocked,'active batch'):self.b.allocate_session('x','actor')
    def test_batch_session_cap(self):
        self.b.begin_batch();self.b.sessions=[{}]*1000
        with self.assertRaisesRegex(Blocked,'batch session'):self.b.allocate_session('retry','actor')
    def test_restored_breaker_cannot_be_bypassed(self):
        b=CampaignBudget(Path(self.tmp.name),{'stop_reason':'isolation failure'})
        with self.assertRaises(Blocked):b.begin_batch()
        b.close()
    def test_ledger_separates_session_from_request_budget(self):self.assertFalse(self.b.state()['model_request_or_money_cap'])

if __name__=='__main__':unittest.main()
