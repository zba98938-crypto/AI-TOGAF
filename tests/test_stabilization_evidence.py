"""Round/revision identity and actual execution are required, independent of reports."""
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('stabilization_evidence',REPO/'togaf-standard-10th-ai/maintenance/stabilization_evidence.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


class StabilizationEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name).resolve()
        self.round={'round_id':'current','source_commit':'a'*40,'prerequisites':{}}
        (self.root/'source.py').write_text('original bytes')

    def tearDown(self):self.temp.cleanup()

    def ref(self,name,data):
        if data.get('stage')=='source_freeze':data.setdefault('schema_version','stabilization-source-freeze/1')
        module.write_new(self.root/name,data)
        return module.reference(self.root/name,self.root)

    def test_pending_stages_and_unexecuted_standards_never_claim_completion(self):
        result=module.report(self.round,self.root/'report.json',self.root)
        self.assertFalse(result['engineering_stable']);self.assertFalse(result['technical_scope_complete'])
        self.assertFalse(result['all_work_complete'])
        self.assertEqual(result['human_professional_acceptance'],'pending_signature')

    def test_old_round_and_changed_frozen_bytes_are_invalid(self):
        data={'stage':'source_freeze','round_id':'old','source_commit':'a'*40,'passed':True,
              'files':{'source.py':module.sha(self.root/'source.py')}}
        self.round['prerequisites']['source_freeze']=self.ref('freeze.json',data)
        result=module.report(self.round,self.root/'old-report.json',self.root)
        self.assertEqual(result['stages'][0]['status'],'invalid')
        data['round_id']='current';self.round['prerequisites']['source_freeze']=self.ref('current-freeze.json',data)
        (self.root/'source.py').write_text('changed bytes')
        result=module.report(self.round,self.root/'changed-report.json',self.root)
        self.assertEqual(result['stages'][0]['status'],'invalid')

    def test_downstream_report_cannot_authorize_upstream_source_closure(self):
        freeze={'stage':'source_freeze','round_id':'current','source_commit':'a'*40,'passed':True,
                'files':{'source.py':module.sha(self.root/'source.py')}}
        self.round['prerequisites']['source_freeze']=self.ref('freeze.json',freeze)
        self.ref('total-report.json',{'schema_version':'stabilization-report/1','passed':True})
        with self.assertRaisesRegex(ValueError,'downstream'):
            module.record(self.round,'source_closure',self.root/'total-report.json',self.root/'stage.json',self.root)

    def test_registered_507_pass_labels_without_sessions_are_unexecuted(self):
        ids=['case-%03d'%i for i in range(507)]
        (self.root/'coverage-inventory.json').write_text(json.dumps({'native_cases':[{'id':i} for i in ids]}))
        data={'status':'pass','rows':[{'id':i,'status':'pass'} for i in ids]}
        result=module.model_evidence(self.root/'native-results.json',data,self.root)
        self.assertFalse(result['passed']);self.assertEqual(result['executed_items'],0)
        self.assertEqual(result['unexecuted_items'],507)
        self.assertFalse(result['actor_scorer_independent'])

    def test_recorded_bounded_fixtures_cannot_close_full_standard(self):
        refs={}
        for language,version in [('uml','2.5.1'),('bpmn','2.0.2')]:
            data={'schema_version':'native-design-time-coverage/1','language':language,'version':version,
                  'completeness':{'source_scope_complete':True,'applicability_adjudication_complete':True},
                  'items':[{'id':'one','implementation_status':'partial','verification_status':'passed-bounded-fixtures',
                            'implementation':[],'positive_tests':[],'negative_tests':[]}]}
            refs[language]=self.ref(language+'.json',data)
        self.round['standard_capabilities']=refs
        result=module.report(self.round,self.root/'bounded.json',self.root)
        self.assertFalse(result['standard_capabilities_complete'])

    def test_evidence_and_output_are_immutable_and_paths_stay_local(self):
        ref=self.ref('source.json',{'passed':True})
        (self.root/'source.json').write_text('{}')
        with self.assertRaises(ValueError):module.read_ref(ref,self.root)
        with self.assertRaises(FileExistsError):module.write_new(self.root/'source.json',{})
        for name in ('../elsewhere','/etc/passwd','a\\b','a//b','./a','a%2fb','file:a'):
            with self.assertRaises(ValueError):module.safe(name,self.root)

    def test_one_way_publications_preserve_pending_signature_and_input_bytes(self):
        report=module.report(self.round,self.root/'report.json',self.root)
        self.round['prerequisites']['total_report']=module.reference(self.root/'report.json',self.root)
        before=module.sha(self.root/'report.json')
        pack=module.acceptance_pack(self.round,self.root/'acceptance.json',self.root)
        self.assertFalse(pack['ready_for_signature']);self.assertTrue((self.root/'acceptance.md').is_file())
        self.assertTrue(all(v is None for v in pack['signatures'].values()))
        self.round['acceptance_pack']=module.reference(self.root/'acceptance.json',self.root)
        ledger=module.ledger(self.round,self.root/'ledger.json',self.root)
        self.assertFalse(ledger['technical_delivery_complete'])
        self.round['prerequisites']['ledger']=module.reference(self.root/'ledger.json',self.root)
        status=module.completion_status(self.round,self.root/'status.json',self.root)
        self.assertFalse(status['all_requested_delivery_complete'])
        self.assertEqual(status['real_organization_approval'],'pending_signature')
        self.round['prerequisites']['completion_status']=module.reference(self.root/'status.json',self.root)
        final=module.final_readonly(self.round,self.root/'readonly.json',self.root)
        self.assertFalse(final['passed']);self.assertEqual(final['upstream_writes'],0)
        self.assertEqual(module.sha(self.root/'report.json'),before)

    def test_stale_report_cannot_create_current_ledger(self):
        module.report(self.round,self.root/'report.json',self.root)
        self.round['prerequisites']['total_report']=module.reference(self.root/'report.json',self.root)
        self.round['round_id']='next'
        with self.assertRaisesRegex(ValueError,'another stage/round/revision'):
            module.ledger(self.round,self.root/'ledger.json',self.root)

    def test_only_applied_frozen_entrypoint_bytes_are_authorized_differences(self):
        (self.root/'catalogue.md').write_text('old catalogue')
        files={n:module.sha(self.root/n) for n in ('source.py','catalogue.md')}
        self.round['prerequisites']['source_freeze']=self.ref('freeze.json',{
            'stage':'source_freeze','round_id':'current','source_commit':'a'*40,'passed':True,'files':files})
        (self.root/'source.py').write_text('current map')
        (self.root/'catalogue.md').write_text('new catalogue')
        paths={'current_map':'source.py','catalogue':'catalogue.md'}
        after={k:module.sha(self.root/n) for k,n in paths.items()}
        before={k:files[n] for k,n in paths.items()}
        activation={'schema_version':'current-output-activation/1','round_id':'current','source_commit':'a'*40,
                    'applied':True,'passed':True,'before_sha256':before,'after_sha256':after,'proposed_sha256':after,
                    'entry_files':{k:{'path':n,'before_sha256':before[k],'after_sha256':after[k]} for k,n in paths.items()}}
        replacements=module.activated_files(self.round,self.root,activation)
        _,freeze=module.read_ref(self.round['prerequisites']['source_freeze'],self.root)
        module.verify_frozen(freeze,self.root,replacements)
        (self.root/'source.py').write_text('unreviewed edit')
        with self.assertRaisesRegex(ValueError,'after bytes differ'):module.activated_files(self.round,self.root,activation)

    def test_execution_record_consumes_actual_evidence_after_verifying_prerequisites(self):
        self.round['prerequisites']['source_freeze']=self.ref('freeze.json',{
            'stage':'source_freeze','round_id':'current','source_commit':'a'*40,'passed':True,
            'files':{'source.py':module.sha(self.root/'source.py')}})
        corpus=self.root/'togaf-standard-10th-ai/skills/_shared/corpus'
        (corpus/'retrieval').mkdir(parents=True);(corpus/'source.txt').write_text('source evidence')
        source_sha=module.sha(corpus/'source.txt')
        (corpus/'retrieval/chunks.jsonl').write_text(json.dumps({'id':'case-1','source_path':'historical/source.txt','source_sha256':source_sha})+'\n')
        (corpus/'source-map.json').write_text(json.dumps({'logical_paths':{'historical/source.txt':'source.txt'},
            'file_sha256':{'source.txt':source_sha},'required_source_count':1,
            'retrieval_index_sha256':{'retrieval/chunks.jsonl':module.sha(corpus/'retrieval/chunks.jsonl')}}))
        raw=module.current_source_closure(corpus)
        self.ref('source-closure.json',raw)
        record=module.record(self.round,'source_closure',self.root/'source-closure.json',self.root/'record.json',self.root)
        self.assertTrue(record['passed']);self.assertEqual(record['evidence']['path'],'source-closure.json')
        raw['counts']['records']+=1;self.ref('forged-source-closure.json',raw)
        with self.assertRaisesRegex(ValueError,'actual full-index'):
            module.record(self.round,'source_closure',self.root/'forged-source-closure.json',self.root/'forged-record.json',self.root)

    def entry_freeze_fixture(self):
        subprocess.run(['git','init','-q'],cwd=self.root,check=True)
        (self.root/'.gitignore').write_text('output/\nfreeze*.json\n')
        subprocess.run(['git','add','source.py','.gitignore'],cwd=self.root,check=True)
        subprocess.run(['git','-c','user.name=Local test','-c','user.email=local@example.invalid',
                        'commit','-qm','fixture'],cwd=self.root,check=True)
        (self.root/'output').mkdir()
        (self.root/'output/current.json').write_text('{"atlas":"old"}')
        (self.root/'output/catalogue.html').write_text('<!doctype html><p>Old atlas</p>')
        return {'schema_version':'stabilization-entry-inputs/1','round_id':'current',
                'entries':{k:module.reference(self.root/n,self.root) for k,n in (
                    ('current_map','output/current.json'),('catalogue','output/catalogue.html'))}}

    def test_freeze_includes_exact_ignored_entry_bytes(self):
        inputs=self.entry_freeze_fixture()
        data=module.freeze('current',self.root/'freeze.json',self.root,inputs)
        self.assertEqual(data['entry_inputs'],inputs)
        for ref in inputs['entries'].values():self.assertEqual(data['files'][ref['path']],ref['sha256'])
        module.verify_frozen(data,self.root)
        (self.root/'output/catalogue.html').write_text('changed outside activation')
        with self.assertRaisesRegex(ValueError,'frozen source changed'):module.verify_frozen(data,self.root)

    def test_freeze_rejects_wrong_round_tampered_entry_and_invalid_file_type(self):
        inputs=self.entry_freeze_fixture()
        inputs['round_id']='old'
        with self.assertRaisesRegex(ValueError,'current-round'):module.freeze('current',self.root/'freeze.json',self.root,inputs)
        inputs['round_id']='current'
        inputs['entries']['catalogue']['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'bytes differ'):module.freeze('current',self.root/'freeze.json',self.root,inputs)
        inputs['entries']['catalogue']=inputs['entries']['current_map']
        with self.assertRaisesRegex(ValueError,'input type'):module.freeze('current',self.root/'freeze.json',self.root,inputs)

    def test_ignored_normative_material_is_frozen_and_tampering_blocks(self):
        inputs=self.entry_freeze_fixture()
        name='togaf-standard-10th-ai/skills/_shared/standards/sources'
        directory=self.root/name;directory.mkdir(parents=True)
        (directory/'normative.pdf').write_bytes(b'synthetic normative material')
        (directory/'manifest.json').write_text(json.dumps([{'file':'normative.pdf','status':'acquired',
            'sha256':module.sha(directory/'normative.pdf')},{'file':'absent.cmof','status':'failed'}]))
        (self.root/'.gitignore').write_text('output/\nfreeze*.json\n*.pdf\n')
        subprocess.run(['git','add','.gitignore',name+'/manifest.json'],cwd=self.root,check=True)
        subprocess.run(['git','-c','user.name=Local test','-c','user.email=local@example.invalid',
                        'commit','-qm','normative fixture'],cwd=self.root,check=True)
        data=module.freeze('current',self.root/'freeze.json',self.root,inputs)
        self.assertIn(name+'/normative.pdf',data['files'])
        self.assertNotIn(name+'/absent.cmof',data['files'])
        module.verify_frozen(data,self.root)
        (directory/'normative.pdf').write_bytes(b'changed normative material')
        with self.assertRaisesRegex(ValueError,'frozen source changed'):module.verify_frozen(data,self.root)
