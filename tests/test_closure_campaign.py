"""No model calls: independent lifecycle, resume and byte-tamper tests."""
import json,sys,tempfile,unittest
from pathlib import Path
from enterprise.campaign import CampaignBudget
from enterprise.closure_campaign import coordinate
from enterprise.frozen_runtime import binary_record,dependency_hashes,hashes,verify
from enterprise.runtime import Blocked,save,sha256

class FakeRuntime:
    def __init__(self,directory,budget,skills,**kwargs):self.directory=Path(directory);self.directory.mkdir();self.budget=budget
    def preflight(self):return {'status':'pass'}
    def close(self):pass

class CoordinatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.out=Path(self.tmp.name);self.b=CampaignBudget(self.out);self.b.free_limit=0
        self.cases=[{'id':'c%d'%i,'kind':'profile','owner':'test','target':'test'} for i in range(40)];self.workers=[]
    def tearDown(self):self.b.close();self.tmp.cleanup()
    def runner(self,runtime,cases,workers):
        self.workers.append(workers)
        for c in cases:runtime.budget.allocate_session(c['id'],'actor');runtime.budget.allocate_session(c['id'],'scorer')
        return {'status':'pass','rows':[{**c,'status':'pass'} for c in cases]}
    def runit(self,**kw):return coordinate(self.out,self.b,[],self.cases,None,runtime_factory=FakeRuntime,runner=kw.pop('runner',self.runner),**kw)
    def test_concurrency_gates_and_all_evidence(self):
        r=self.runit();self.assertEqual(r['status'],'pass');self.assertEqual(self.workers,[1,1,1,2,4,4]);self.assertEqual(len(r['rows']),40);self.assertEqual(len(self.b.sessions),80)
    def test_partial_then_resume_keeps_sessions_and_passes(self):
        r=self.runit(limit=3);self.assertEqual(r['status'],'partial');self.assertEqual(sum(x['status']=='uncovered' for x in r['rows']),37)
        wall=self.b.started_wall;r=self.runit(resume=True)
        self.assertEqual(r['status'],'pass');self.assertEqual(self.b.started_wall,wall);self.assertEqual(len(self.b.sessions),80);self.assertEqual(len(r['attempts']),6)
    def test_failed_directed_gate_stops_before_parallel(self):
        def fail(r,c,workers):self.workers.append(workers);return {'status':'fail','rows':[{**c[0],'status':'fail'}]}
        r=self.runit(runner=fail);self.assertEqual(r['status'],'blocked');self.assertEqual(self.workers,[1]);self.assertEqual(r['rows'][0]['status'],'fail')
        r=self.runit(resume=True);self.assertEqual(r['status'],'blocked');self.assertEqual(self.workers,[1])
    def test_normal_boundary_rolls_over_without_losing_rows(self):
        roll=[False]
        def run(runtime,cases,workers):
            if len(self.b.sessions)>=6 and not roll[0]:
                roll[0]=True
                return {'status':'blocked','stop_type':'BatchExhausted','stop_reason':'batch time boundary','rows':[{**c,'status':'uncovered'} for c in cases]}
            return self.runner(runtime,cases,workers)
        r=self.runit(runner=run);self.assertEqual(r['status'],'pass');self.assertEqual(self.b.batch,2);self.assertEqual(len(self.b.sessions),80);self.assertEqual(r['rows'][0]['status'],'pass')
    def test_circuit_breaker_never_opens_next_batch(self):
        def run(runtime,cases,workers):
            self.b.observe_http(429);self.b.observe_http(429)
            return {'status':'blocked','rows':[{**cases[0],'status':'blocked'}]}
        r=self.runit(runner=run);self.assertEqual(r['status'],'blocked');self.assertEqual(self.b.batch,1);self.assertIn('429',self.b.stop_reason)
    def test_preflight_failure_spends_no_business_sessions(self):
        class Bad(FakeRuntime):
            def preflight(self):raise Blocked('toolchain/isolation preflight failed: browser')
        r=coordinate(self.out,self.b,[],self.cases,None,runtime_factory=Bad,runner=self.runner)
        self.assertEqual(r['status'],'blocked');self.assertEqual(self.b.sessions,[]);self.assertTrue(self.b.cancel.is_set())

class FrozenTamperTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);shared=self.root/'skills/_shared'
        for p in (shared/'.venv',shared/'node_modules',self.root/'wheels',self.root/'java/bin'):p.mkdir(parents=True)
        (shared/'package-lock.json').write_text('{}');(shared/'node_modules/file.js').write_text('sealed');(self.root/'java/bin/java').write_text('fixture');(self.root/'wheels/a.whl').write_text('fixture')
        self.manifest={'schema_version':'frozen-runtime/2','frozen_hashes':hashes(self.root/'skills',('.venv','node_modules','__pycache__','.DS_Store')),'dependency_hashes':dependency_hashes(self.root),'wheel_hashes':hashes(self.root/'wheels'),'dependencies_sha256':sha256(shared/'package-lock.json'),'tool_binaries':{'python':binary_record(sys.executable)},'java_home':str(self.root/'java'),'java_hashes':hashes(self.root/'java')}
        save(self.root/'runtime-manifest.json',self.manifest)
    def tearDown(self):self.tmp.cleanup()
    def test_matching_byte_manifest_passes(self):self.assertEqual(verify(self.root)['schema_version'],'frozen-runtime/2')
    def test_dependency_tamper(self):
        (self.root/'skills/_shared/node_modules/file.js').write_text('changed')
        with self.assertRaisesRegex(Blocked,'dependency bytes'):verify(self.root)
    def test_java_tamper(self):
        (self.root/'java/bin/java').write_text('changed')
        with self.assertRaisesRegex(Blocked,'Java bytes'):verify(self.root)
    def test_wheel_tamper(self):
        (self.root/'wheels/a.whl').write_text('changed')
        with self.assertRaisesRegex(Blocked,'wheel bytes'):verify(self.root)
    def test_symlink_escape(self):
        (self.root/'skills/_shared/node_modules/escape').symlink_to('/etc/hosts')
        with self.assertRaises(Blocked):verify(self.root)
    def test_old_manifest_rejected(self):
        self.manifest['schema_version']='frozen-runtime/1';save(self.root/'runtime-manifest.json',self.manifest)
        with self.assertRaisesRegex(Blocked,'resealed'):verify(self.root)

if __name__=='__main__':unittest.main()
