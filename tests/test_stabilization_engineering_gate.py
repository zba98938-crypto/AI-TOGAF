"""Independent malformed, omitted and stale proof cases for the engineering gate."""
import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('engineering_evidence_gate', REPO /
    'togaf-standard-10th-ai/maintenance/stabilization_engineering_evidence.py')
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(value, bytes):
        path.write_bytes(value)
    elif isinstance(value, str):
        path.write_text(value)
    else:
        path.write_text(json.dumps(value, indent=2)+'\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fixture(root):
    """Synthetic complete proof fixture, independent of production output helpers."""
    out = root/'output/core-round'
    scripts = root/'togaf-standard-10th-ai/skills/_shared/scripts'
    shared = scripts.parent
    source = ('import unittest as ut\nfrom unittest import TestCase as Case\n'
              'class Base(Case):\n def test_alpha(self): pass\n'
              'class Derived(Base):\n def test_beta(self): pass\n'
              'class Helper:\n def test_not_discovered(self): pass\n')
    write(root/'tests/test_fixture.py', source)
    for name in ('run_unit_regressions.py', 'verify_core.py'):
        write(root/'tests'/name, '# source controller\n')
    for name in ('generate.py', 'verify_skill_packages.py', 'verify_method_case_constraints.py',
                 'verify_method_reasoning.py', 'verify_methods.py', 'registry_consistency.py',
                 'verify_artifact_profiles.py', 'verify_profile_geometry.py', 'verify_scale_cases.py', 'render.mjs'):
        write(scripts/name, '# fixed source\n')
    write(shared/'capabilities.json', {'profiles':[{'id':'profile'}]})
    write(shared/'deliverables.json', {'deliverables':[{'id':'delivery'}]})
    ids = ['test_fixture.Base.test_alpha', 'test_fixture.Derived.test_alpha', 'test_fixture.Derived.test_beta']
    unit = {'schema_version':'formal-unit-regressions/1', 'discovered':3, 'executed':3,
            'source_stable':True, 'failures':0, 'errors':0, 'skipped':0, 'passed':True,
            'test_ids':ids, 'actual_results':[{'id':identity,'status':'passed'} for identity in ids],
            'test_source_sha256':{'test_fixture.py':sha(root/'tests/test_fixture.py')},
            'failure_details':[], 'error_details':[], 'skipped_details':[]}
    write(out/'unit-regressions/summary.json', unit)
    verbose = '\n'.join(identity.rsplit('.',1)[1]+' ('+identity.rsplit('.',1)[0]+') ... ok' for identity in ids)
    write(out/'unit-regressions/unit-regressions.log', verbose+'\n\nRan 3 tests in 0.001s\n\nOK\n')
    compact = {key:unit[key] for key in ('schema_version','discovered','source_stable','executed',
                                       'failures','errors','skipped','passed')}
    write(out/'logs/unit-regressions.log', json.dumps(compact)+'\n')
    names = ['syntax','unit-regressions','skill-packages','method-case-constraints','method-reasoning',
             'methods','registry-consistency','production-profiles','deliverables','integrity-adm',
             'profile-expression','text-geometry','mermaid-chinese','visual-samples','scale-sql',
             'missing-historical-data','empty-verify_method_case_constraints',
             'empty-verify_method_reasoning','source-integrity']
    rows = {name:{'name':name,'status':'pass','detail':{},'seconds':0.01} for name in names}
    def command(name, script, arguments=(), expected=0):
        rows[name]['detail'] = {'argv':['python3',str(script),*map(str,arguments)],
                                'exit_code':expected,'expected_exit_code':expected}
        log = 'mermaid' if name=='mermaid-chinese' else name
        if name!='unit-regressions':write(out/'logs'/(log+'.log'), 'retained command output\n')
    command('unit-regressions',root/'tests/run_unit_regressions.py',[root/'tests','--out',out/'unit-regressions'])
    for name, script, dest in [('skill-packages','verify_skill_packages.py','packages.json'),
                              ('method-case-constraints','verify_method_case_constraints.py','method-cases.json'),
                              ('method-reasoning','verify_method_reasoning.py','method-reasoning.json'),
                              ('methods','verify_methods.py','methods')]:
        command(name,scripts/script,['--out',out/dest])
    command('registry-consistency',scripts/'registry_consistency.py')
    write(out/'logs/registry-consistency.log',json.dumps({'errors':[],'review_evidence_required':False})+'\n')
    command('profile-expression',scripts/'verify_artifact_profiles.py',['--all','--out',out/'profiles','--render','--oversized-policy','tile'])
    command('text-geometry',scripts/'verify_profile_geometry.py',[out/'profiles','--out',out/'geometry'])
    command('mermaid-chinese',scripts/'render.mjs',[out/'mermaid/jobs.json'])
    rows['mermaid-chinese']['detail']['argv'][0]='node'
    command('missing-historical-data',scripts/'verify_scale_cases.py',['--dataset-dir',out/'missing-dataset','--out',out/'missing-scale'],3)
    for script in ('verify_method_case_constraints','verify_method_reasoning'):
        name='empty-'+script
        command(name,scripts/(script+'.py'),['--cases-dir',out/'empty-cases','--out',out/(name+'.json')],3)
        write(out/(name+'.json'),{'status':'blocked'})
    write(out/'missing-scale/report.json',{'status':'blocked'})
    before = GATE.source_hashes(root)
    write(out/'source-before.json',before);write(out/'source-after.json',before)
    python_files = sorted(name for name in before if name.endswith('.py'))
    write(out/'syntax.json',{'checked':python_files});rows['syntax']['detail']={'python_files':len(python_files)}
    write(out/'packages.json',{'schema_version':'skill-package-verification/1','audit_complete':True,
                             'all_applicable_pass':True,'per_skill':{'owned':{'files':{'status':'pass'}}}})
    write(out/'method-cases.json',{'schema_version':'method-case-constraints/1','status':'passed',
                                 'methods':[{'passed':True}],'violations':[]})
    write(out/'method-reasoning.json',{'status':'passed','engineering_status':'passed',
                                     'engineering_assertions':[{'id':'normative','status':'passed'}]})
    def batch(stage, result_name, result):
        folder=out/stage/'run-fixture'
        write(folder/result_name,result)
        write(folder/'stdout.txt','actual fixed stage output\n');write(folder/'stderr.txt','')
        data={'schema_version':'execution-batch/2','passed':True,'source_root':str(shared),
              'run_root':str(folder),'run_id':folder.name,
              'runtime_before':{'scripts/generate.py':sha(scripts/'generate.py')},
              'runtime_after':{'scripts/generate.py':sha(scripts/'generate.py')},
              'changed_runtime_paths':[],'changed_input_paths':[],
              'inputs':{'source:scripts/generate.py':sha(scripts/'generate.py')},
              'outputs':{'run:'+result_name:sha(folder/result_name)},
              'runs':[{'ordinal':1,'argv':['python3',str(scripts/'generate.py')],
                       'exit_code':0,'expected_exit_code':0,'matches_expected':True,
                       'stdout':{'path':'run:stdout.txt','sha256':sha(folder/'stdout.txt')},
                       'stderr':{'path':'run:stderr.txt','sha256':sha(folder/'stderr.txt')}}]}
        write(folder/'execution.json',data)
        write(out/'logs'/('methods.log' if stage=='methods' else 'text-geometry.log'),
              json.dumps({'batch':str(folder/'execution.json'),'report':str(folder/result_name)})+'\n')
    batch('methods','methods.json',{'schema_version':'method-verification/3','failed':0,
                                   'missing_calculators':[],'records':[{'oracle_passed':True}]})
    batch('geometry','geometry-check.json',{'status':'passed','checked':4,'flagged':0})
    profile={'profile_id':'profile','output_kind':'diagram','failures':[],
             'layouts':[{'layout':'reference','valid':True},{'layout':'adaptive','valid':True}]}
    write(out/'profiles/verification.json',{'status':'passed','png_export_requested':True,'render_status':'passed',
                                          'failed_profiles':0,'results':[profile]})
    write(out/'profiles/profile.case.json',{'result':profile})
    for layout in ('reference','adaptive'):
        for variant in ('','-modified'):
            write(out/'profiles'/('profile-'+layout+variant+'.svg'),'<svg/>')
            write(out/'profiles'/('profile-'+layout+variant+'.coverage.json'),{'errors':[]})
    def generated(folder):
        write(folder/'artifact.svg','<svg>retained artifact</svg>')
        write(folder/'manifest.json',{'output_sha256':{'artifact.svg':sha(folder/'artifact.svg')}})
    for layout in ('reference','adaptive'):generated(out/'production/profile'/layout)
    write(out/'production-profiles.json',[{'profile_id':'profile','errors':[],
          'layouts':[{'layout':layout,'status':'pass','files':1} for layout in ('reference','adaptive')]}])
    write(out/'deliverables.json',[{'deliverable_id':'delivery','status':'pass','sections':1}])
    write(out/'deliverables/delivery/assembly.json',{'status':'assembled-awaiting-review','section_blocks':[{}],
                                                 'unbound_section_titles':[]})
    generated(out/'deliverables/delivery/generated')
    write(out/'integrity-adm.json',{'tampered':['output-file-stale:artifact.svg'],
          'stale_model':['output-model-stale'],'cycle':{'phases':[{}]*9},
          'check':{'phases':[{}]*9,'errors':[],'recorded_cycle_complete':False}})
    write(out/'visual-samples/index.json',{'renderer':'profile'})
    write(out/'visual-samples/renderer.png',b'\x89PNG\r\n\x1a\nfixture')
    rows['visual-samples']['detail']={'renderer_families':1}
    write(out/'mermaid/diagram.svg','<svg>中文</svg>')
    write(out/'mermaid/diagram.png',b'\x89PNG\r\n\x1a\nfixture')
    write(out/'mermaid/jobs.json',{'jobs':[{'source':'diagram.mmd'}]})
    write(out/'scale/oracle-report.json',{'passed':True,'counts':{'orders':1000},'checks':[{}]})
    write(out/'scale/negative-cases.json',{'passed':True,'cases':[{}]})
    write(out/'scale/determinism.json',{'passed':True,'hashes':['same','same']})
    rows['source-integrity']['detail']={'unchanged':True}
    data={'schema_version':'skills-core-regression/1','status':'pass','render_requested':True,'orders':1000,
          'results':list(rows.values()),'failures':[],'blocked':[],'source_changed':[]}
    reseal(out,data)
    return out, data


def reseal(out, data):
    data['evidence_sha256'] = GATE.evidence_hashes(out)
    write(out/'summary.json',data)


class EngineeringEvidenceGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.out,self.data=fixture(self.root)

    def accepted(self):
        return GATE.engineering_pass(self.out/'summary.json',self.data,self.root)

    def change_unit(self, mutate):
        path=self.out/'unit-regressions/summary.json';unit=json.loads(path.read_text())
        mutate(unit);write(path,unit);reseal(self.out,self.data)

    def test_complete_retained_proof_passes_without_writing_any_file_or_cache(self):
        before={str(p.relative_to(self.root)):sha(p) for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual([],GATE.engineering_errors(self.out/'summary.json',self.data,self.root))
        self.assertTrue(self.accepted())
        self.assertEqual(before,{str(p.relative_to(self.root)):sha(p) for p in self.root.rglob('*') if p.is_file()})

    def test_arbitrary_pass_row_and_single_handwritten_unit_record_are_rejected(self):
        self.data['results']=[{'name':'anything','status':'pass','detail':{},'seconds':1}]
        write(self.out/'logs/unit-regressions.log',json.dumps({'schema_version':'formal-unit-regressions/1',
              'passed':True,'executed':1,'failures':0,'errors':0,'skipped':0}))
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_same_stage_count_with_omitted_or_duplicate_stage_is_rejected(self):
        for name in ('invented-stage','syntax'):
            with self.subTest(name=name):
                data=copy.deepcopy(self.data);data['results'][-1]['name']=name
                reseal(self.out,data)
                self.assertFalse(GATE.engineering_pass(self.out/'summary.json',data,self.root))

    def test_nonrender_blocked_failed_and_skipped_core_never_pass(self):
        for field,value in [('render_requested',False),('status','blocked')]:
            with self.subTest(field=field):
                data=copy.deepcopy(self.data);data[field]=value;reseal(self.out,data)
                self.assertFalse(GATE.engineering_pass(self.out/'summary.json',data,self.root))
        self.data['results'][0]['status']='skipped';reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_single_unit_with_full_current_source_hash_map_is_rejected(self):
        def mutate(unit):
            unit['discovered']=unit['executed']=1;unit['test_ids']=unit['test_ids'][:1]
            unit['actual_results']=unit['actual_results'][:1]
        self.change_unit(mutate);self.assertFalse(self.accepted())

    def test_same_count_changed_test_ids_are_rejected(self):
        def mutate(unit):
            unit['test_ids'][-1]='test_fixture.Derived.test_omitted'
            unit['actual_results'][-1]['id']=unit['test_ids'][-1]
        self.change_unit(mutate);self.assertFalse(self.accepted())

    def test_duplicate_or_missing_actual_results_are_rejected(self):
        original=json.loads((self.out/'unit-regressions/summary.json').read_text())
        for results in [original['actual_results'][:-1],[original['actual_results'][0]]*3]:
            with self.subTest(results=results):
                self.change_unit(lambda u:u.update(actual_results=results));self.assertFalse(self.accepted())

    def test_all_nonpassing_actual_unit_statuses_reject_even_with_zero_counters(self):
        for status in ['failed','error','skipped','expected-failure','unexpected-success']:
            with self.subTest(status=status):
                self.change_unit(lambda u:u['actual_results'][0].update(status=status));self.assertFalse(self.accepted())

    def test_unit_source_false_stable_or_incomplete_hash_map_rejects(self):
        self.change_unit(lambda u:u.update(source_stable=False));self.assertFalse(self.accepted())
        self.change_unit(lambda u:u.update(source_stable=True,test_source_sha256={}));self.assertFalse(self.accepted())

    def test_source_added_after_execution_rejects_even_when_core_maps_are_refreshed(self):
        write(self.root/'tests/test_added.py','from unittest import TestCase\nclass Added(TestCase):\n def test_added(self): pass\n')
        current=GATE.source_hashes(self.root)
        write(self.out/'source-before.json',current);write(self.out/'source-after.json',current)
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_stale_source_before_or_after_and_empty_map_rejects(self):
        for name in ('source-before.json','source-after.json'):
            with self.subTest(name=name):
                write(self.out/name,{});reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_full_evidence_hash_map_rejects_missing_tampered_and_new_files(self):
        original=copy.deepcopy(self.data)
        self.data.pop('evidence_sha256');write(self.out/'summary.json',self.data);self.assertFalse(self.accepted())
        self.data=original;write(self.out/'summary.json',self.data)
        write(self.out/'logs/methods.log','tampered result');self.assertFalse(self.accepted())
        reseal(self.out,self.data);write(self.out/'extra-retained-result.json',{});self.assertFalse(self.accepted())

    def test_json_summary_alone_cannot_replace_actual_verbose_unit_log(self):
        write(self.out/'unit-regressions/unit-regressions.log','{"passed":true,"executed":3}\n')
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_missing_command_log_rejects_even_after_resealing(self):
        (self.out/'logs/profile-expression.log').unlink();reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_registry_and_strict_delivery_result_pass_labels_are_insufficient(self):
        write(self.out/'deliverables.json',[{'status':'pass','deliverable_id':'other','sections':1}])
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_generated_artifact_tampering_rejects_even_after_top_level_resealing(self):
        write(self.out/'production/profile/reference/artifact.svg','modified artifact')
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_missing_nested_execution_logs_and_external_reference_are_rejected(self):
        path=self.out/'methods/run-fixture/execution.json';batch=json.loads(path.read_text())
        batch['runs'][0]['stdout']['path']='run:../escape.txt';write(path,batch)
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_current_registry_extension_cannot_be_hidden_by_one_profile_result(self):
        path=self.root/'togaf-standard-10th-ai/skills/_shared/capabilities.json'
        write(path,{'profiles':[{'id':'profile'},{'id':'new-profile'}]})
        current=GATE.source_hashes(self.root)
        write(self.out/'source-before.json',current);write(self.out/'source-after.json',current)
        reseal(self.out,self.data);self.assertFalse(self.accepted())

    def test_static_inventory_resolves_unittest_aliases_local_inheritance_and_helpers(self):
        ids,hashes=GATE.discover_test_inventory(self.root)
        self.assertEqual(['test_fixture.Base.test_alpha','test_fixture.Derived.test_alpha','test_fixture.Derived.test_beta'],ids)
        self.assertEqual({'test_fixture.py':sha(self.root/'tests/test_fixture.py')},hashes)

    def test_static_inventory_resolves_imported_module_alias_testcase(self):
        path=self.root/'tests/test_fixture.py'
        write(path,path.read_text().replace('class Base(Case):','class Base(ut.TestCase):'))
        ids,_=GATE.discover_test_inventory(self.root)
        self.assertEqual(['test_fixture.Base.test_alpha','test_fixture.Derived.test_alpha','test_fixture.Derived.test_beta'],ids)

    def test_dynamic_load_tests_unknown_inheritance_and_conditional_classes_fail_closed(self):
        for source in ('def load_tests(loader,tests,pattern): return tests\n',
                       'from somewhere import Unknown\nclass Tests(Unknown):\n def test_unknown(self): pass\n',
                       'if True:\n class Conditional:\n  def test_dynamic(self): pass\n'):
            with self.subTest(source=source):
                write(self.root/'tests/test_dynamic.py',source)
                with self.assertRaises(ValueError):GATE.discover_test_inventory(self.root)

    def test_parent_escape_symlink_and_unretained_argument_data_reject(self):
        self.assertFalse(GATE.engineering_pass(self.out/'../core-round/summary.json',self.data,self.root))
        self.assertFalse(GATE.engineering_pass(self.out/'summary.json',{**self.data,'orders':2},self.root))
        (self.out/'link').symlink_to(self.root/'tests/test_fixture.py')
        self.assertFalse(self.accepted())


if __name__=='__main__':unittest.main()
