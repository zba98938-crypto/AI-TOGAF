"""Regression for exact sandbox argv and fail-closed collective diagnostics."""
import sys,tempfile,unittest,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tests'))
from enterprise.agents import NativeAgents,sandbox_argv,browser_probe_source
from enterprise.runtime import Blocked
from enterprise.frozen_runtime import admission_location
class NativeToolchainTests(unittest.TestCase):
 def test_temp_policy_is_in_cli_not_only_parent_environment(self):
  argv=sandbox_argv('codex',Path('/tmp/work'),'scorer');self.assertIn('enterprise-scorer',argv);self.assertIn('shell_environment_policy.set.TMPDIR="/private/tmp/work/.tmp"' if sys.platform=='darwin' else 'shell_environment_policy.set.TMPDIR="/tmp/work/.tmp"',argv);self.assertEqual(argv[-1],'--')
 def test_invalid_role_rejected(self):
  with self.assertRaises(ValueError):sandbox_argv('codex',Path('/tmp/work'),'unrestricted')
 def fake_runtime(self,root,failed):
  r=object.__new__(NativeAgents);r.directory=root/'evidence';r.shared=root/'shared';r.shared.mkdir();r.java_home=root/'java';r.java_home.mkdir();r.codex='codex'
  def probe(name,workspace,argv,env,read_only=False):
   allowed=name not in ('cross-session-read-denied','frozen-write-denied','scorer-write-denied','shell-network-denied')
   return {'exit_code':1 if name==failed else 0 if allowed else 1,'timeout':False}
  r.sandbox_probe=probe
  def workspace(name,expose):
   p=root/name;p.mkdir();return p
  r.workspace=workspace;return r
 def test_collective_failure_still_reports_every_tool_without_passing_gate(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);r=self.fake_runtime(root,'browser-render-probe');workspace=root/'workspace';workspace.mkdir()
   with self.assertRaisesRegex(Blocked,'browser-render-probe'):r.toolchain_preflight(workspace,['codex'],{},collect_all=True)
   result=json.loads((r.directory/'toolchain-preflight.json').read_text());self.assertEqual(result['status'],'blocked');self.assertIn('uml2-ocl-load-probe',result['probes']);self.assertIn('shell-network-denied',result['probes']);self.assertFalse(result['real_home_granted'])
 def test_default_preflight_stops_at_failed_tool(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);r=self.fake_runtime(root,'python-import-render-probe');workspace=root/'workspace';workspace.mkdir()
   with self.assertRaises(Blocked):r.toolchain_preflight(workspace,['codex'],{})
   result=json.loads((r.directory/'toolchain-preflight.json').read_text());self.assertEqual(list(result['probes']),['python-import-render-probe'])
 def test_browser_launch_failure_is_classified_without_claiming_specific_os_cause(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);r=self.fake_runtime(root,'browser-render-probe');workspace=root/'workspace';workspace.mkdir();(workspace/'.tmp').mkdir()
   (workspace/'.tmp/browser-probe-result.json').write_text(json.dumps({'status':'blocked','stage':'launch','code':'BROWSER_LAUNCH_FAILED','message':'Target closed','cause':'Target closed'}))
   with self.assertRaises(Blocked):r.toolchain_preflight(workspace,['codex'],{})
   report=json.loads((r.directory/'toolchain-preflight.json').read_text());detail=report['probes']['browser-render-probe']
   self.assertEqual(detail['failure_category'],'BROWSER_LAUNCH_FAILED');self.assertEqual(detail['browser_diagnostic']['stage'],'launch')
   self.assertIn('unconfirmed',detail['runtime_boundary']);self.assertEqual(report['status'],'blocked')
 def test_browser_probe_records_launch_render_and_success_without_skips(self):
  for mode in ('launch','render','bad-png','pass'):
   with self.subTest(mode=mode),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);shared=root/'shared';(shared/'scripts').mkdir(parents=True);(root/'.tmp').mkdir()
    mock="""export async function launchBrowser(options) {
if(!options.pipe||!options.dumpio)throw Error('missing native diagnostic options');
if(MODE==='launch')throw Object.assign(new Error('Target closed'),{code:'BROWSER_LAUNCH_FAILED'});
return {newPage:async()=>({setContent:async()=>{if(MODE==='render')throw Error('render failed');},
screenshot:async()=>Buffer.from(MODE==='bad-png'?'0000':'89504e470d0a1a0a','hex')}),
close:async()=>{(await import('node:fs')).writeFileSync('closed','yes');}};
} """.replace('MODE',json.dumps(mode))
    (shared/'scripts/browser_resolver.mjs').write_text(mock);script=root/'browser-probe.mjs';script.write_text(browser_probe_source(shared))
    done=subprocess.run(['node',str(script)],cwd=root,capture_output=True,text=True,timeout=10)
    report=json.loads((root/'.tmp/browser-probe-result.json').read_text())
    self.assertEqual(done.returncode,0 if mode=='pass' else 1,done.stderr)
    self.assertEqual(report['status'],'pass' if mode=='pass' else 'blocked')
    if mode!='launch':self.assertTrue((root/'closed').exists())
    if mode=='launch':self.assertEqual(report['code'],'BROWSER_LAUNCH_FAILED')
    if mode in ('render','bad-png'):self.assertEqual(report['stage'],'render')
 def test_timeout_cannot_count_as_expected_denial(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);r=self.fake_runtime(root,None);old=r.sandbox_probe
   def probe(name,*args,**kw):
    result=old(name,*args,**kw)
    if name=='cross-session-read-denied':result['timeout']=True
    return result
   r.sandbox_probe=probe;workspace=root/'workspace';workspace.mkdir()
   with self.assertRaisesRegex(Blocked,'cross-session-read-denied'):r.toolchain_preflight(workspace,['codex'],{})

 def test_expected_denial_reports_probe_pass_separate_from_process_exit(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);r=self.fake_runtime(root,None);workspace=root/'workspace';workspace.mkdir()
   report=r.toolchain_preflight(workspace,['codex'],{})
   self.assertEqual(report['probes']['cross-session-read-denied']['status'],'pass')
   self.assertNotEqual(report['probes']['cross-session-read-denied']['exit_code'],0)

 def test_native_admission_rejects_macos_tmp_for_java_and_runtime(self):
  for label in ('Java runtime','frozen runtime','browser distribution'):
   with self.assertRaisesRegex(Blocked,'denied /tmp'):admission_location('/tmp/togaf-runtime',label,platform='darwin',home='/Users/synthetic-no-home')
 def test_scoped_shared_runtime_is_admitted_without_home_grant(self):
  self.assertEqual(admission_location('/Users/Shared/scoped-runtime','Java runtime',platform='darwin',home='/Users/synthetic-no-home'),Path('/Users/Shared/scoped-runtime'))
 def test_actual_java_probe_uses_source_file_mode_not_unavailable_workspace_classpath(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);r=self.fake_runtime(root,None);workspace=root/'workspace';workspace.mkdir();old=r.sandbox_probe;seen={}
   def probe(name,root,argv,*args,**kw):
    seen[name]=argv;return old(name,root,argv,*args,**kw)
   r.sandbox_probe=probe;r.toolchain_preflight(workspace,['codex'],{})
   self.assertTrue(str(seen['java-run-probe'][-1]).endswith('Probe.java'));self.assertNotIn('-cp',seen['java-run-probe'])
