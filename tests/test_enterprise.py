"""Harness regressions use tiny datasets, never consume model sessions."""
import json
import os
import signal
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from enterprise.agents import NativeAgents, SCORE_DIMENSIONS, permission_configuration, provider_configuration, reviewed_status, write_red_png
from enterprise.cases import agent_cases, business_text_mutations, inventory, rendered_artifact_text
from enterprise.data import audit, build, derive, dirty_copy, replay
from enterprise.runtime import Blocked, Budget, metrics, output_bytes, run_command, save, sha256
from enterprise.stress import Workload, burst, capacity_renderer, failure_drills, mermaid_shape_result, raster_dimensions, sustained


class EnterpriseHarnessTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='enterprise-unit-')
        self.root = Path(self.temporary.name)
        self.budget = Budget(self.root,max_hours=.1,max_sessions=4,min_free_gib=0,reserve_seconds=0)

    def tearDown(self):
        self.temporary.cleanup()

    def dataset(self,n=100):
        directory = self.root/'data'
        build(directory,n,20261105,self.budget,chunk=37)
        return directory/'enterprise.sqlite'

    def test_continuation_inherits_original_clock_session_and_output_limits(self):
        previous = self.root/'previous'
        previous.mkdir()
        (previous/'retained').write_bytes(b'12345678')
        current = self.root/'current'
        current.mkdir()
        rows=[{'number':1,'case_id':'prior-preflight','role':'actor'}]
        budget=Budget(current,max_hours=.1,max_sessions=2,min_free_gib=0,reserve_seconds=0,
                      started_wall=time.time()-30,prior_sessions=rows,prior_output_roots=[previous])
        self.assertGreaterEqual(budget.snapshot()['elapsed_seconds'],30)
        self.assertEqual(budget.allocate_session('new-preflight','actor'),2)
        with self.assertRaises(Blocked):
            budget.allocate_session('extra','actor')
        budget.output_limit=4
        with self.assertRaisesRegex(Blocked,'campaign output limit'):
            budget.check(force=True)

    def test_cli_schema_and_final_paths_are_inside_private_isolation(self):
        from unittest.mock import patch
        runtime = NativeAgents.__new__(NativeAgents)
        runtime.home = self.root/'private'
        runtime.directory = self.root/'evidence'
        runtime.budget = self.budget
        runtime.codex = '/synthetic/codex'
        runtime.env = {}
        root = self.root/'opaque-live-root'
        root.mkdir()
        def fake_command(argv,directory,budget,**kwargs):
            schema = Path(argv[argv.index('--output-schema')+1])
            final = Path(argv[argv.index('--output-last-message')+1])
            self.assertTrue(schema.is_relative_to(runtime.home))
            self.assertTrue(final.is_relative_to(runtime.home))
            self.assertNotIn('trust-framework',str(schema))
            save(final,{'verified':True})
            (directory/'stdout.jsonl').write_text('{"type":"turn.completed","usage":{"input_tokens":1,"output_tokens":1}}\n')
            return {'status':'pass','exit_code':0}
        schema={'type':'object','properties':{'verified':{'type':'boolean'}},'required':['verified']}
        with patch('enterprise.agents.run_command',side_effect=fake_command):
            output,detail=runtime.session('profile-trust-framework-default','actor',root,'synthetic',schema)
        self.assertTrue(output['verified'])
        self.assertEqual(detail['session_number'],1)
        self.assertTrue((runtime.directory/'profile-trust-framework-default/actor/schema.json').exists())
        self.assertTrue((runtime.directory/'profile-trust-framework-default/actor/final.json').exists())

    @unittest.skipUnless(sys.platform=='darwin','native Codex macOS sandbox')
    def test_native_profile_denies_home_and_other_contexts_allows_linked_skills(self):
        from enterprise.cases import REPO, SHARED
        import shutil
        codex=shutil.which('codex')
        if not codex:
            self.skipTest('native CLI unavailable')
        private=self.root/'private'
        home=private/'.codex'
        home.mkdir(parents=True)
        (home/'config.toml').write_text(permission_configuration(Path.home(),REPO/'togaf-standard-10th-ai/skills',private))
        root=private/'opaque-workspace'
        root.mkdir()
        tmp=root/'.tmp'
        tmp.mkdir()
        link=root/'skills-link'
        link.symlink_to(REPO/'togaf-standard-10th-ai/skills',target_is_directory=True)
        other=private/'other-context'
        other.mkdir()
        (other/'rubric.json').write_text('SYNTHETIC_EXPECTED_ROUTE')
        env={**os.environ,'HOME':str(private),'CODEX_HOME':str(home),'TMPDIR':str(tmp)}
        base=[codex,'--no-daemon','sandbox','-P','enterprise-actor','-C',str(root),'--']
        for denied_path in (REPO/'tests/README.md',other/'rubric.json'):
            result=subprocess.run(base+['/bin/cat',str(denied_path)],capture_output=True,timeout=15,env=env,cwd=root)
            self.assertNotEqual(result.returncode,0)
        allowed=subprocess.run(base+['/bin/cat',str(link/'togaf-security-risk/SKILL.md')],capture_output=True,timeout=15,env=env,cwd=root)
        self.assertEqual(allowed.returncode,0,allowed.stderr.decode())
        # Retained evidence is deliberately outside the writable workspace.
        # Inherited stdout must target the allowed local tree before archiving.
        runtime=NativeAgents.__new__(NativeAgents)
        runtime.directory=private/'retained-evidence'
        runtime.directory.mkdir()
        runtime.budget=self.budget
        probe=runtime.sandbox_probe('linked-skill',root,
            base+['/bin/cat',link/'togaf-security-risk/SKILL.md'],env)
        self.assertEqual(probe['exit_code'],0)
        self.assertIn('name:',(runtime.directory/'linked-skill/stdout.jsonl').read_text())
        sentinel=runtime.directory/'sentinel.txt'
        sentinel.write_text('SYNTHETIC_RETAINED_EVIDENCE_MUST_STAY_DENIED')
        denied_probe=runtime.sandbox_probe('denied-retained',root,base+['/bin/cat',sentinel],env)
        self.assertNotEqual(denied_probe['exit_code'],0)
        self.assertNotIn('SYNTHETIC_RETAINED_EVIDENCE_MUST_STAY_DENIED',
                         (runtime.directory/'denied-retained/stdout.jsonl').read_text())
        output=root/'native-output.txt'
        written=subprocess.run(base+['/bin/sh','-c','printf valid > '+str(output)],capture_output=True,timeout=15,env=env,cwd=root)
        self.assertEqual(written.returncode,0,written.stderr.decode())
        self.assertEqual(output.read_text(),'valid')

    def test_actor_live_workspace_does_not_disclose_target_route_in_path(self):
        runtime = NativeAgents.__new__(NativeAgents)
        runtime.home = self.root/'private'
        runtime.directory = self.root/'evidence'
        runtime.workspaces = {}
        from enterprise.cases import REPO, SHARED
        runtime.frozen_skills=REPO/'togaf-standard-10th-ai/skills'
        runtime.shared=SHARED
        runtime.skills = inventory()['skills']
        name = 'profile-trust-framework-default'
        root = runtime.workspace(name,True)
        self.assertNotIn('trust-framework',str(root))
        self.assertFalse(root.is_relative_to(runtime.directory))
        (root/'actual.json').write_text('{"verified":true}')
        runtime.retain_workspaces()
        self.assertEqual((runtime.directory/name/'workspace/actual.json').read_text(),'{"verified":true}')
        self.assertFalse((runtime.directory/name/'workspace/.agents').exists())

    def test_workspace_bootstrap_declares_supported_runtime_without_route_leak(self):
        from enterprise.cases import SHARED
        runtime = NativeAgents.__new__(NativeAgents)
        runtime.home = self.root/'bootstrap-private'
        runtime.directory = self.root/'bootstrap-evidence'
        runtime.workspaces = {}
        from enterprise.cases import REPO, SHARED
        runtime.frozen_skills=REPO/'togaf-standard-10th-ai/skills'
        runtime.shared=SHARED
        runtime.skills = inventory()['skills']
        root = runtime.workspace('profile-risk-appetite-default',True)
        instructions = (root/'AGENTS.md').read_text()
        self.assertIn(str(SHARED/'.venv/bin/python'),instructions)
        self.assertIn('Do not cat the entire large raw-input.json',instructions)
        self.assertIn('.agents/skills/_shared is intentionally absent',instructions)
        self.assertNotIn('risk-appetite',instructions)
        self.assertNotIn('expected_route',instructions)
        self.assertTrue((root/'_shared').is_dir())
        self.assertFalse((root/'.agents/skills/_shared').exists())

    def test_semantic_pass_requires_all_independent_review_dimensions(self):
        import copy
        verdict = {'verdict':'pass','routing':'accepted','reason':'verified',
                   'dimensions':[{'name':n,'verdict':'pass','evidence':'actual-output/model.json: checked raw records'} for n in SCORE_DIMENSIONS]}
        self.assertEqual(reviewed_status(verdict,'profile',['model.json']),'pass')
        incomplete = copy.deepcopy(verdict)
        incomplete['dimensions'].pop()
        self.assertEqual(reviewed_status(incomplete,'profile',['model.json']),'needs_review')
        self.assertEqual(reviewed_status(verdict,'profile',['model.json'],has_image=True),'needs_review')
        self.assertEqual(reviewed_status(copy.deepcopy(verdict),'profile',[]),'fail')
        unsupported = copy.deepcopy(verdict)
        unsupported['dimensions'][0]['evidence']=''
        self.assertEqual(reviewed_status(unsupported,'profile',['model.json']),'needs_review')

    def test_output_accounting_handles_deleted_scratch_without_following_links(self):
        from unittest.mock import patch
        scratch = self.root/'scratch'
        scratch.write_bytes(b'123')
        (self.root/'retained').write_bytes(b'12345')
        (self.root/'external-link').symlink_to('/etc/hosts')
        original = Path.lstat
        def disappeared(path):
            if path == scratch:
                raise FileNotFoundError('scratch completed concurrently')
            return original(path)
        with patch.object(Path,'lstat',disappeared):
            self.assertEqual(output_bytes(self.root),5)

    def test_paced_replay_tolerates_sampler_crossing_sleep_deadline(self):
        db=self.dataset(100)
        base=self.budget
        class DelayedSampler:
            def __init__(self): self.calls=0
            def __getattr__(self,key): return getattr(base,key)
            def check(self,*args,**kwargs):
                self.calls+=1
                base.check(*args,**kwargs)
                if self.calls==2: time.sleep(.1)
        sampler=DelayedSampler()
        result=replay(db,self.root/'paced-replay',sampler,limit=1,pace_seconds=.05)
        self.assertGreaterEqual(sampler.calls,2)
        self.assertEqual(result['consumed_events'],1)
        self.assertEqual(result['status'],'pass')

    def test_positive_business_mutation_excludes_semantic_enum_fields(self):
        model={'entities':[{'id':'e1','attributes':{
            'factor_category':'foundational','perspective':'客户','block':'关键伙伴',
            'change_kind':'retain','unit_kind':'source','approval_status':'candidate',
            'owner_id':'manager-1','definition':'需要跨基地订单核对'}}]}
        candidates=list(business_text_mutations(model))
        self.assertEqual(len(candidates),1)
        changed,field=candidates[0]
        self.assertEqual(field['field'],'definition')
        self.assertEqual(changed['entities'][0]['attributes']['block'],'关键伙伴')
        self.assertNotIn('增加跨基地核对要求',model['entities'][0]['attributes']['definition'])

    def test_expression_oracle_reads_declared_svg_and_html_not_json_echo(self):
        (self.root/'primary.md').write_text('See linked diagram and details.')
        (self.root/'diagram.svg').write_text('<svg><text>增加跨基地核对要求</text></svg>')
        (self.root/'details.html').write_text('<p>HTML business details</p>')
        (self.root/'raw.json').write_text('JSON-only echo must not count')
        manifest={'artifacts':[{'path':'primary.md','svg':'diagram.svg','details':'details.html','json':'raw.json'}]}
        text=rendered_artifact_text(self.root,manifest)
        self.assertIn('增加跨基地核对要求',text)
        self.assertIn('HTML business details',text)
        self.assertNotIn('JSON-only',text)
        with self.assertRaisesRegex(ValueError,'escapes output'):
            rendered_artifact_text(self.root,{'artifacts':[{'svg':'../outside.svg'}]})

    def test_mermaid_placeholder_cannot_pass_requested_capacity(self):
        (self.root/'diagram.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><g class="node default"><text>Maximum text size in diagram exceeded</text></g></svg>')
        write_red_png(self.root/'diagram.png')
        result=mermaid_shape_result(self.root,10000,{'status':'pass'},{'status':'passed'})
        self.assertEqual(result['status'],'fail')
        self.assertEqual(result['actual_nodes'],1)
        self.assertEqual(mermaid_shape_result(self.root,1000,{'status':'fail'},
            {'status':'blocked','reason':'Edge limit exceeded.'})['status'],'blocked')
        (self.root/'diagram.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><g class="node default"/><g class="node default"/><g class="node default"/><path class="flowchart-link"/><path class="flowchart-link"/></svg>')
        self.assertEqual(mermaid_shape_result(self.root,3,{'status':'pass'},{'status':'passed'})['status'],'pass')

    def test_original_renderer_reports_limits_and_syntax_not_success_cards(self):
        from enterprise.cases import REPO,SHARED
        import shutil
        node=shutil.which('node')
        if not node or not (SHARED/'node_modules/@mermaid-js/mermaid-cli').is_dir():
            self.skipTest('installed Mermaid runtime unavailable')
        shutil.copyfile(SHARED/'assets/fonts/NotoSansSC.ttf',self.root/'font.ttf')
        cases=(('normal','flowchart LR\nA[制造订单] --> B[发票]\n',0,'passed'),
               ('text-limit','flowchart LR\n%% '+('x'*50001)+'\n',3,'blocked'),
               ('edge-limit','flowchart LR\n'+'\n'.join('N%d --> N%d'%(i,i+1) for i in range(501))+'\n',3,'blocked'),
               ('syntax','flowchart LR\nA --> [\n',1,'failed'))
        for name,definition,code,status in cases:
            with self.subTest(name=name):
                dest=self.root/name
                dest.mkdir()
                (dest/'diagram.mmd').write_text(definition)
                save(dest/'jobs.json',{'font':'../font.ttf','jobs':[{'id':name,'kind':'mmd',
                    'source':'diagram.mmd','svg':'diagram.svg','png':'diagram.png',
                    'title':'合成回归','legend':'合成输入，不是真实批准','is_example':True}]})
                result=subprocess.run([node,str(SHARED/'scripts/render.mjs'),str(dest/'jobs.json')],
                                      capture_output=True,timeout=30,cwd=str(REPO))
                self.assertEqual(result.returncode,code,result.stderr.decode())
                self.assertEqual(json.loads((dest/'render-report.json').read_text())['status'],status)
                self.assertEqual((dest/'diagram.png').is_file(),status=='passed')

    def test_markdown_catalogue_has_no_false_png_requirement(self):
        from enterprise.stress import shape_input, shape_worker
        from registry import load
        model = shape_input(load()[2]['compat-application-portfolio-catalog'],10)
        save(self.root/'model.json',model)
        self.assertEqual(shape_worker(self.root/'model.json',self.root/'catalogue',render=True),0)
        result = json.loads((self.root/'catalogue/shape-result.json').read_text())
        self.assertEqual(result['status'],'pass')
        self.assertEqual(result['raster_status'],'not-applicable-native-markdown')

    def test_raster_safety_ceiling_does_not_silently_downscale(self):
        svg = self.root/'capacity.svg'
        svg.write_text('<svg viewBox="0 0 100 100" width="20000" height="100"/>')
        result = raster_dimensions(svg)
        self.assertFalse(result['safe'])
        self.assertEqual(result['width'],20000)
        svg.write_text('<svg viewBox="0 0 100 100"/>')
        self.assertTrue(raster_dimensions(svg)['safe'])
        svg.write_text('<svg viewBox="0 0 NaN 100"/>')
        with self.assertRaises(Blocked):
            raster_dimensions(svg)

    def test_bounded_renderer_retains_svg_and_blocks_large_bitmap(self):
        from enterprise.cases import SHARED
        import shutil
        shutil.copyfile(SHARED/'assets/fonts/NotoSansSC.ttf',self.root/'font.ttf')
        svg = self.root/'large.svg'
        svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20000 20000" width="20000" height="20000"><rect width="20" height="20"/></svg>')
        before = sha256(svg)
        save(self.root/'jobs.json',{'font':'font.ttf','jobs':[{'id':'large','kind':'svg','source':'large.svg','svg':'large.svg','png':'large.png'}]})
        renderer = capacity_renderer(self.root)
        command = run_command(['node',renderer,self.root/'jobs.json'],self.root/'render-logs',self.budget,timeout=20)
        self.assertNotEqual(command['exit_code'],0)
        report = json.loads((self.root/'render-report.json').read_text())
        self.assertIn('enterprise-raster-capacity:',report['reason'])
        self.assertEqual(sha256(svg),before)
        self.assertFalse((self.root/'large.png').exists())

    def test_required_field_warning_is_not_strict_acceptance(self):
        from enterprise.cases import profile_mutations
        result = profile_mutations(self.root/'mutation',self.budget,limit=1)
        self.assertEqual(result['status'],'pass')
        rejection = json.loads((self.root/'mutation/risk-appetite-default/missing-required-rejection.json').read_text())
        self.assertEqual(rejection['phase'],'strict-generation')
        self.assertIn('missing-profile-attribute',rejection['reason'])

    def test_inventory_and_actor_budget(self):
        scope = inventory()
        self.assertEqual(len(scope['skills']),17)
        self.assertEqual(set(scope['independent_profiles']), set(scope['profiles']) - set(scope['aliases']))
        cases = agent_cases()
        self.assertEqual({c['target'] for c in cases if c['kind']=='profile'},set(scope['independent_profiles']))
        self.assertEqual(len(cases),len(scope['independent_profiles'])+len(scope['methods'])+
                         len(scope['deliverables'])+5*len(scope['skills'])+6+12)
        self.assertLessEqual(len(cases)*2+2,1000)
        self.assertEqual(sum(c['kind']=='method' for c in cases),72)

    def test_profile_without_business_fixture_is_an_explicit_missing_input_case(self):
        from enterprise.cases import blind_fragment
        raw=blind_fragment({'id':'unprovided-profile'})
        self.assertEqual(raw['business_material_status'],'not-provided')
        self.assertEqual(raw['business_records'],[])

    def test_six_planning_profiles_have_three_business_scenarios(self):
        from enterprise.planning_cases import PROFILE_IDS
        cases=agent_cases()
        for pid in PROFILE_IDS:
            rows=[c for c in cases if c['target']==pid and c['kind']!='repeat']
            self.assertEqual({'sufficient','missing','change'},{c['scenario'] for c in rows})
            self.assertTrue(all(c['rubric']['business_fixture_status']=='provided' for c in rows))

    def test_blind_actor_input_has_no_selected_view(self):
        for case in agent_cases():
            if case['kind']=='profile':
                self.assertNotIn('view',case['raw'])
                self.assertNotIn(case['target'],json.dumps(case['raw']))
                self.assertNotIn(case['target'],case['request'])

    def test_generic_data_and_independent_oracle(self):
        db = self.dataset()
        result = audit(db,self.root/'audit',self.budget)
        self.assertEqual(result['status'],'pass')
        self.assertEqual(result['counts']['orders'],100)
        self.assertEqual(result['counts']['events'],300)
        facts = derive(db,self.root/'facts',self.budget)
        self.assertEqual(facts['independent_oracle']['scanned_orders'],100)
        self.assertEqual(facts['independent_oracle']['decimal_totals'],facts['independent_oracle']['sql_totals'])
        self.assertTrue(db.is_file())

    def test_deterministic_snapshot(self):
        db = self.dataset()
        build(self.root/'second',100,20261105,self.budget,chunk=37)
        self.assertEqual(sha256(db),sha256(self.root/'second/enterprise.sqlite'))

    def test_dirty_types_are_rejected(self):
        db = self.dataset(200)
        result = dirty_copy(db,self.root/'dirty',.05,self.budget)
        self.assertEqual(result['status'],'pass')
        self.assertIn('payment-balance',result['detected'])
        self.assertEqual(audit(db,self.root/'clean-audit',self.budget)['status'],'pass')

    def test_replay_checkpoint_and_duplicate_idempotence(self):
        db = self.dataset()
        one = replay(db,self.root/'replay',self.budget,limit=60)
        two = replay(db,self.root/'replay',self.budget,limit=60)
        self.assertEqual(one['consumed_events'],60)
        self.assertEqual(two['consumed_events'],120)
        self.assertEqual(two['new_events'],60)

    def test_late_event_id_uses_arrival_checkpoint(self):
        db = self.dataset()
        replay(db,self.root/'replay',self.budget,limit=300)
        with sqlite3.connect(db) as con:
            con.execute('INSERT INTO orders VALUES(101,1,1,1,10,100,1)')
            con.execute('INSERT INTO events VALUES(1,101,"order-created",1,10000)')
        result = replay(db,self.root/'replay',self.budget,limit=10)
        self.assertEqual(result['new_events'],1)
        self.assertEqual(result['consumed_events'],301)
        self.assertEqual(result['applied_business_events'],301)

    def test_duplicate_business_event_is_quarantined(self):
        db = self.dataset()
        with sqlite3.connect(db) as con:
            con.execute('INSERT INTO events SELECT 1,order_id,kind,occurred_day,10000 FROM events WHERE id=3')
        result = replay(db,self.root/'replay',self.budget,limit=1000)
        self.assertEqual(result['quarantined']['duplicate-business-event'],1)
        self.assertEqual(result['applied_business_events'],300)
        self.assertEqual(result['consumed_events'],301)

    def test_missing_reference_detected_independently(self):
        db = self.dataset()
        with sqlite3.connect(db) as con:
            con.execute('UPDATE orders SET customer_id=-1 WHERE id=1')
        rows = audit(db,self.root/'audit',self.budget)['checks']
        self.assertEqual(next(r['violations'] for r in rows if r['name']=='order-dimensions'),1)

    def test_session_cap_is_reserved_before_execution(self):
        for n in range(4):
            self.budget.allocate_session(str(n),'actor')
        with self.assertRaises(Blocked):
            self.budget.allocate_session('retry','scorer')
        self.assertEqual(len(json.loads((self.root/'session-ledger.json').read_text())),4)

    def test_campaign_time_cap(self):
        self.budget.dispatch_deadline = time.monotonic()-1
        with self.assertRaises(Blocked):
            self.budget.check()

    def test_output_cap(self):
        self.budget.output_limit = 1
        (self.root/'obstacle').write_text('too much')
        with self.assertRaises(Blocked):
            self.budget.check(force=True)

    def test_no_stdout_memory_capture_and_owned_cancellation(self):
        with self.assertRaises(Blocked):
            run_command([sys.executable,'-c','import time;print("started",flush=True);time.sleep(30)'],self.root/'command',self.budget,timeout=.1)
        result = json.loads((self.root/'command/command.json').read_text())
        self.assertEqual(result['status'],'blocked')
        self.assertIn('started',(self.root/'command/stdout.jsonl').read_text())

    def test_finished_leader_does_not_leak_child(self):
        command = 'import subprocess; p=subprocess.Popen(["sleep","60"]);print(p.pid,flush=True)'
        run_command([sys.executable,'-c',command],self.root/'orphan',self.budget)
        pid = int((self.root/'orphan/stdout.jsonl').read_text())
        time.sleep(.1)
        result = subprocess.run(['ps','-o','stat=','-p',str(pid)],capture_output=True,text=True)
        self.assertTrue(not result.stdout.strip() or result.stdout.strip().startswith('Z'),result.stdout)

    def test_config_isolated_preserves_exact_provider(self):
        config = self.root/'config.toml'
        config.write_text('model="gpt-6.1-sol"\nmodel_provider="custom"\nmodel_reasoning_effort="xhigh"\nnotify=["bad"]\n[model_providers.custom]\nbase_url="http://127.0.0.1:1/v1"\nexperimental_bearer_token="test-not-secret"\nwire_api="responses"\n[plugins.unrelated]\nenabled=true\n[mcp_servers.unrelated]\ncommand="bad"\n')
        private,metadata = provider_configuration(config)
        self.assertIn('experimental_bearer_token="test-not-secret"',private)
        self.assertIn('model="gpt-6.1-sol"'.replace('=',' = '),private)
        self.assertNotIn('notify',private)
        self.assertNotIn('plugins',private)
        self.assertNotIn('mcp_servers',private)
        self.assertNotIn('test-not-secret',json.dumps(metadata))

    def test_no_provider_fallback(self):
        config = self.root/'config.toml'
        config.write_text('model="unknown"')
        with self.assertRaises(Blocked):
            provider_configuration(config)

    def test_metrics_no_fabricated_percentiles(self):
        self.assertIsNone(metrics([],1)['p99_seconds'])
        result = metrics([{'seconds':n,'status':'pass'} for n in (1,2,3,4)],2)
        self.assertEqual(result['p95_seconds'],4)
        self.assertEqual(result['throughput_per_second'],2)

    def test_sustained_mixed_workload(self):
        db = self.dataset()
        work = Workload(db,self.root/'work',self.budget)
        result = sustained(work,self.root/'sustained',self.budget,.2,2)
        self.assertEqual(result['status'],'pass')
        self.assertEqual(result['overall']['errors'],0)

    def test_burst_no_silent_loss(self):
        def work(kind):
            time.sleep(.01)
            return {'kind':kind,'status':'pass','seconds':.01}
        result = burst(work,self.root/'burst',self.budget,.2,1000,workers=1,queue_cap=2)
        self.assertEqual(result['arrivals'],result['sample_count']+result['explicit_rejections'])
        self.assertGreater(result['explicit_rejections'],0)
        self.assertLessEqual(result['queue_peak'],2)

    def test_failure_drill_checkpoint_recovery(self):
        db = self.dataset()
        result = failure_drills(self.root/'drills',db,self.budget)
        self.assertEqual(result['status'],'pass')

    def test_png_image_preflight_asset(self):
        write_red_png(self.root/'red.png')
        self.assertEqual((self.root/'red.png').read_bytes()[:8],b'\x89PNG\r\n\x1a\n')

    def test_atomic_json_rejects_nonfinite(self):
        with self.assertRaises(ValueError):
            save(self.root/'nonfinite.json',{'x':float('nan')})
        self.assertFalse((self.root/'nonfinite.json').exists())

class RelayTests(unittest.TestCase):
    def test_same_endpoint_authentication_is_not_in_actor_config(self):
        import http.client
        import threading
        from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
        from enterprise.relay import ProviderRelay
        observed = []
        class Handler(BaseHTTPRequestHandler):
            def log_message(self,*args):
                pass
            def do_POST(self):
                body = self.rfile.read(int(self.headers['Content-Length']))
                observed.append((self.path,self.headers.get('Authorization'),body))
                self.send_response(200)
                self.send_header('Content-Length','2')
                self.end_headers()
                self.wfile.write(b'{}')
        upstream = ThreadingHTTPServer(('127.0.0.1',0),Handler)
        thread = threading.Thread(target=upstream.serve_forever,daemon=True)
        thread.start()
        config = 'model="same-model"\n[model_providers.custom]\nbase_url="http://127.0.0.1:%d/v1"\nexperimental_bearer_token="synthetic-secret"\nrequires_openai_auth=false\n'%upstream.server_port
        relay = ProviderRelay(config,{})
        try:
            self.assertNotIn('synthetic-secret',relay.config)
            self.assertIn('same-model',relay.config)
            connection = http.client.HTTPConnection('127.0.0.1',relay.server.server_port)
            connection.request('POST','/v1/responses',body='{}',headers={'Content-Type':'application/json'})
            response = connection.getresponse()
            self.assertEqual(response.status,200)
            self.assertEqual(response.read(),b'{}')
            self.assertEqual(observed,[('/v1/responses','Bearer synthetic-secret',b'{}')])
            connection.close()
        finally:
            relay.close();upstream.shutdown();upstream.server_close();thread.join()


if __name__=='__main__':
    unittest.main()
