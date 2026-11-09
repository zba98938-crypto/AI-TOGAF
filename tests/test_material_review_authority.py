"""Independent rehashed fixture attacks against upstream material authority.

No native model is launched. Bounded origin checks never grant review status.
"""
import copy
import importlib.util
from pathlib import Path
import unittest

from enterprise import material_authority as authority
from enterprise import material_review as module
from enterprise.runtime import Blocked, sha256
import test_material_review_collection as fixtures


class MaterialAuthorityTests(unittest.TestCase):
    setUp = fixtures.MaterialCollectionTests.setUp
    tearDown = fixtures.MaterialCollectionTests.tearDown
    write = fixtures.MaterialCollectionTests.write
    create_inputs = fixtures.MaterialCollectionTests.create_inputs
    root_shard = fixtures.MaterialCollectionTests.root_shard
    run_fake = fixtures.MaterialCollectionTests.run_fake
    packet = fixtures.MaterialCollectionTests.packet

    def gate(self, packet_ref, **extra):
        path = module.REPO/'togaf-standard-10th-ai/maintenance/stabilization_material_evidence.py'
        spec = importlib.util.spec_from_file_location('independent_material_authority_gate',path)
        gate = importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
        return gate.material_checks({'round_id':'actual-fixture-audit','source_commit':'a'*40,
            'material_input_manifest':self.manifest,'material_review':packet_ref,**extra},self.root)

    def source_authority(self, runtime=None, **changes):
        inputs = module.ReviewInputs(self.manifest,self.root)
        files = dict(inputs.all_refs)
        files.update({name:sha256(module.REPO/name) for name in authority.SOURCE_FILES})
        freeze = self.write('upstream-freeze.json',{'schema_version':'stabilization-source-freeze/1',
            'stage':'source_freeze','passed':True,'round_id':'actual-fixture-audit','source_commit':'a'*40,
            'files':files,'bound_material_review_inputs':{'input_manifest':self.manifest,'visual_source_manifest':None}})
        value = {'schema_version':'material-review-authority/1','round_id':'actual-fixture-audit','source_commit':'a'*40,
            'source_freeze':freeze,'input_manifest':self.manifest,'acquisition_inventory':inputs.manifest['source_unit_inventory'],
            'visual_source_manifest':None,'runtime':runtime}
        value.update(changes)
        return self.write('fake-authority.json',value)

    def test_fixture_flip_with_rehashed_records_cannot_recount_or_collect(self):
        self.run_fake()
        original = (self.root/'review/collection.json').read_bytes()
        packet = self.packet();packet['fixture_execution'] = False
        for i,reference in enumerate(packet['attempts']):
            attempt = module.load(self.root/reference['path']);attempt['fixture_execution'] = False
            packet['attempts'][i] = self.write('review/forged-attempt-'+str(i)+'.json',attempt)
        state = module.load(self.root/packet['campaign_budget_state']['path'])
        state.update(max_sessions=4000,max_seconds=57600,limits={'max_hours':16,'max_sessions':4000,'batches':4,
            'hours_per_batch':4,'sessions_per_batch':1000,'concurrency_stages':[1,2,4],'session_timeout_seconds':600})
        packet['campaign_budget_state'] = self.write('review/forged-budget.json',state)
        inputs = module.ReviewInputs(self.manifest,self.root)
        with self.assertRaisesRegex(ValueError,'independent frozen authority'):
            module._recount_packet(packet,inputs,self.root)
        packet['assessment'].update(complete=True,reviewed_units=2,pending_units=0)
        forged = self.write('review/forged-native.json',packet)
        with self.assertRaisesRegex(ValueError,'independent frozen authority'):
            module.collect_existing(forged,self.root)
        self.assertEqual(self.gate(forged)['status'],'invalid')
        self.assertEqual((self.root/'review/collection.json').read_bytes(),original)

    def test_fake_runtime_cannot_make_upstream_native_admission(self):
        runtime = fixtures.FakeRuntime(self.root,self.budget)
        with self.assertRaisesRegex(Blocked,'actual NativeAgents'):
            authority.make_runtime_admission(runtime,self.root)
        self.assertFalse((runtime.directory/'material-review-admission-runtime.json').exists())
        self.assertEqual(self.budget.state()['sessions'],[])

    def test_fake_frozen_identity_is_not_actual_runtime_verification(self):
        runtime = fixtures.FakeRuntime(self.root,self.budget)
        metadata = self.write((runtime.directory/'material-review-admission-runtime.json').relative_to(self.root).as_posix(),runtime.metadata)
        refs = {'directory':runtime.directory.relative_to(self.root).as_posix(),'metadata':metadata,
            'preflight':module.ref(runtime.directory/'preflight.json',self.root),
            'frozen_runtime_manifest':module.ref(runtime.directory/'frozen-runtime-manifest.json',self.root)}
        with self.assertRaisesRegex(ValueError,'frozen runtime/source revision'):
            authority.verified_runtime(refs,self.root,{'source_commit':'a'*40,'files':{}})

    def test_self_reported_inventory_cannot_replace_full_acquisition(self):
        inputs = module.ReviewInputs(self.manifest,self.root)
        with self.assertRaises((OSError,ValueError,KeyError)):
            authority.verified_acquisition(inputs,self.root)
        with self.assertRaises((OSError,ValueError,KeyError)):
            authority.required_freeze_refs(self.manifest,self.root)
        # Even a rehashed upstream-shaped envelope does not create the corpus.
        reference = self.source_authority()
        with self.assertRaises((OSError,ValueError,KeyError)):
            authority.verify_authority(reference,inputs,self.root,historical=True)

    def test_freeze_omission_and_changed_explicit_round_are_rejected(self):
        reference = self.source_authority()
        value = module.load(self.root/reference['path'])
        freeze = module.load(self.root/value['source_freeze']['path']);freeze['files'].pop('original.html')
        value['source_freeze'] = self.write('omitted-freeze.json',freeze)
        reference = self.write('omitted-authority.json',value)
        inputs = module.ReviewInputs(self.manifest,self.root)
        with self.assertRaisesRegex(ValueError,'omits or replaces'):
            authority.verify_authority(reference,inputs,self.root,historical=True)
        with self.assertRaisesRegex(ValueError,'another explicit frozen round'):
            authority.verify_authority(reference,inputs,self.root,historical=True,
                expected_round={'round_id':'another','source_commit':'a'*40,'prerequisites':{'source_freeze':value['source_freeze']}})

    def origin(self):
        result,runtime = self.run_fake()
        packet = self.packet();attempt = module.load(self.root/packet['attempts'][0]['path'])
        base = self.root/attempt['session_base']
        attempt['origin_raw_session_files'] = {n:module.ref(runtime.directory/base.name/'scorer'/n,self.root)
            for n in authority.RUNTIME_FILES}
        binding = {'runtime':{'directory':runtime.directory,'metadata':copy.deepcopy(runtime.metadata)},
            'data':{'runtime':{'frozen_runtime_manifest':attempt['frozen_runtime_manifest']}}}
        return result,attempt,base,binding

    def test_original_session_byte_binding_is_bounded_and_never_promotes_fixture(self):
        result,attempt,base,binding = self.origin()
        authority.verify_origin(attempt,base,binding,self.root)
        self.assertEqual(result['reviewed_units'],0)
        self.assertFalse(result['complete'])

    def test_original_session_must_belong_to_admitted_directory(self):
        _,attempt,base,binding = self.origin()
        original = self.root/attempt['origin_raw_session_files']['final.json']['path']
        duplicate = self.root/'another-controller/final.json';duplicate.parent.mkdir();duplicate.write_bytes(original.read_bytes())
        attempt['origin_raw_session_files']['final.json'] = module.ref(duplicate,self.root)
        with self.assertRaisesRegex(ValueError,'original admitted controller'):
            authority.verify_origin(attempt,base,binding,self.root)

    def test_original_session_tamper_and_model_identity_drift_are_rejected(self):
        _,attempt,base,binding = self.origin()
        original = self.root/attempt['origin_raw_session_files']['final.json']['path']
        raw = original.read_bytes();original.write_bytes(raw+b' ')
        attempt['origin_raw_session_files']['final.json'] = module.ref(original,self.root)
        with self.assertRaisesRegex(ValueError,'original admitted controller'):
            authority.verify_origin(attempt,base,binding,self.root)
        original.write_bytes(raw);attempt['origin_raw_session_files']['final.json'] = module.ref(original,self.root)
        binding['runtime']['metadata']['model'] = 'a fabricated replacement model'
        with self.assertRaisesRegex(ValueError,'admitted native runtime identity'):
            authority.verify_origin(attempt,base,binding,self.root)

    def test_fixture_cannot_receive_authority_and_native_gate_cannot_omit_round_binding(self):
        self.run_fake();packet = self.packet();packet['authority'] = {'path':'fabricated','sha256':'a'*64}
        forged = self.write('review/fixture-with-authority.json',packet)
        with self.assertRaisesRegex(ValueError,'fixtures may not claim native authority'):
            module.collect_existing(forged,self.root)
        packet['fixture_execution'] = False
        forged = self.write('review/native-without-round-binding.json',packet)
        result = self.gate(forged)
        self.assertEqual(result['status'],'invalid');self.assertEqual(result['reviewed_units'],0)
        self.assertFalse(result['complete'])

    def test_native_probe_requires_actual_integer_exit_codes_and_executable(self):
        expected=['/existing/native','sandbox','--','/bin/cat','/synthetic/fixture']
        for denied in (False,True):
            code=1 if denied else 0
            original={'argv':expected,'exit_code':code,'status':'fail' if denied else 'pass'}
            detail={**original,'status':'pass'}
            module_ref=authority.verify_probe_command
            module_ref('bounded-probe',detail,original,expected,denied=denied)
            for attack in ('missing-exit','boolean-exit','prefix-only','empty-executable','non-string-argument','changed-executable','timeout'):
                command=copy.deepcopy(original);row=copy.deepcopy(detail)
                if attack=='missing-exit':command.pop('exit_code');row.pop('exit_code')
                elif attack=='boolean-exit':command['exit_code']=row['exit_code']=bool(code)
                elif attack=='prefix-only':command['argv']=row['argv']=expected[:3]
                elif attack=='empty-executable':command['argv']=row['argv']=expected[:3]+['']
                elif attack=='non-string-argument':command['argv']=row['argv']=expected[:3]+[True]
                elif attack=='changed-executable':command['argv']=row['argv']=expected[:3]+['/bin/false']
                else:command['timeout']=row['timeout']='false'
                with self.subTest(denied=denied,attack=attack),self.assertRaises(ValueError):
                    module_ref('bounded-probe',row,command,expected,denied=denied)

    def test_native_probe_receipts_preserve_real_read_only_status_format(self):
        expected=['/existing/native','sandbox','--','/bin/cat','/synthetic/fixture']
        for denied in (False,True):
            original={'argv':expected,'exit_code':1 if denied else 0,'timeout':False}
            detail={**original,'status':'pass','execution_status':None}
            authority.verify_probe_command('scorer-bounded-probe',detail,original,expected,denied=denied,read_only=True)
            original['timeout']=None
            with self.assertRaises(ValueError):
                authority.verify_probe_command('scorer-bounded-probe',detail,original,expected,denied=denied,read_only=True)


if __name__ == '__main__':
    unittest.main()
