"""Regression tests for evidence roots, blocked inputs and browser prerequisites."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
SHARED = REPO / 'togaf-standard-10th-ai/skills/_shared'
SCRIPTS = SHARED / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from execution_batch import Batch, digest, inside, resolve_ref, verify
from evidence_integrity import verify_reference
from run_remediation_acceptance import preflight as historical_preflight
from verify_scale_cases import preflight as scale_preflight


class ExecutionEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='togaf-evidence-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'
        self.source.mkdir()
        self.inputs = self.base / 'external-input.json'
        self.inputs.write_text('{"fact": 1}\n')
        self.runtime = {'runtime.py': 'known-runtime'}
        self.patcher = patch('execution_batch.current', return_value=self.runtime)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def batch(self):
        return Batch(self.base / 'outputs', inputs=[self.inputs], root=self.source)

    def finished(self):
        batch = self.batch()
        batch.run([sys.executable, '-c', 'print("bounded execution")'])
        output = batch.directory / 'result.json'
        output.write_text('{"result": "example"}\n')
        _, report = batch.finish(outputs=[output])
        return batch, report, output

    def test_external_inputs_are_readonly_snapshots_and_survive_original_removal(self):
        batch, report, _ = self.finished()
        self.assertEqual('execution-batch/2', report['schema_version'])
        reference = next(iter(report['inputs']))
        snapshot = resolve_ref(reference, self.source, batch.directory)
        self.assertEqual(self.inputs.read_bytes(), snapshot.read_bytes())
        self.assertEqual(0, snapshot.stat().st_mode & 0o222)
        self.inputs.unlink()
        self.assertEqual([], verify(report, root=self.source, expected_current=self.runtime))

    def test_output_tamper_is_rejected(self):
        batch, report, output = self.finished()
        self.assertEqual([], verify(report, root=self.source, expected_current=self.runtime))
        output.write_text('tampered')
        self.assertTrue(any('asset-stale:' in x for x in verify(report, root=self.source, expected_current=self.runtime)))

    def test_report_cannot_choose_another_source_root(self):
        _, report, _ = self.finished()
        for forged in (str(self.base / 'untrusted'), None, 'relative', str(self.source / '..' / 'source')):
            with self.subTest(source_root=forged):
                changed = copy.deepcopy(report)
                changed['source_root'] = forged
                with patch('execution_batch.current', side_effect=AssertionError('must not inspect declared root')):
                    self.assertEqual(['source-root-identity-mismatch'], verify(changed, root=self.source))

    def test_v2_reference_uses_trusted_or_installed_source_root(self):
        batch, report, _ = self.finished()
        path = batch.directory / 'execution.json'
        reference = {'path': path.name, 'sha256': digest(path)}
        expected = {'source_root': self.source, 'runtime_fingerprints': self.runtime}
        self.assertEqual([], verify_reference(reference, batch.directory, expected))
        with patch('execution_batch.ROOT', self.source):
            self.assertEqual([], verify_reference(reference, batch.directory))
        report['source_root'] = str(self.base / 'forged-source')
        path.write_text(json.dumps(report))
        reference['sha256'] = digest(path)
        with patch('execution_batch.current', side_effect=AssertionError('must not inspect declared root')):
            self.assertEqual(['source-root-identity-mismatch'], verify_reference(reference, batch.directory, expected))

    def test_transitive_reference_keeps_runtime_root_but_not_method_identity(self):
        batch, _, _ = self.finished()
        evidence_root = batch.directory.parent
        case = evidence_root / 'case.json'
        case.write_text('{}')
        method = evidence_root / 'method.json'
        method.write_text(json.dumps({'schema_version': 'method-execution/1', 'method_id': 'child-method',
            'case_path': case.name, 'case_sha256': digest(case),
            'execution_refs': [{'path': batch.run_id + '/execution.json',
                                'sha256': digest(batch.directory / 'execution.json')}]}))
        wrapper = evidence_root / 'wrapper.json'
        wrapper.write_text(json.dumps({'schema_version': 'evidence-node/1',
            'references': [{'path': method.name, 'sha256': digest(method)}]}))
        expected = {'source_root': self.source, 'runtime_fingerprints': self.runtime, 'method_id': 'parent-method'}
        with patch('execution_batch.current', side_effect=AssertionError('caller fingerprints must survive recursion')):
            self.assertEqual([], verify_reference({'path': wrapper.name, 'sha256': digest(wrapper)}, evidence_root, expected))

    def test_input_change_during_run_is_rejected(self):
        batch = self.batch()
        batch.run([sys.executable, '-c', 'print(1)'])
        output = batch.directory / 'output.txt'
        output.write_text('result')
        self.inputs.write_text('changed')
        _, report = batch.finish(outputs=[output])
        self.assertFalse(report['passed'])
        self.assertIn(str(self.inputs.resolve()), report['changed_input_paths'])

    def test_no_commands_cannot_pass(self):
        batch = self.batch()
        output = batch.directory / 'output.txt'
        output.write_text('unexecuted')
        _, report = batch.finish(outputs=[output])
        self.assertFalse(report['passed'])

    def test_outputs_cannot_write_or_reference_source(self):
        with self.assertRaises(ValueError):
            Batch(self.source / 'runs', root=self.source)
        batch = self.batch()
        output = self.source / 'not-a-run-output.txt'
        output.write_text('source')
        with self.assertRaises(ValueError):
            batch.finish(outputs=[output])
        alias = batch.directory / 'escaped.txt'
        alias.symlink_to(output)
        with self.assertRaises(ValueError):
            batch.finish(outputs=[alias])

    def test_parent_and_symlink_escape_are_rejected(self):
        batch, report, output = self.finished()
        for path in ('../escape', 'nested/../result.json'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                inside(batch.directory, path)
        alias = batch.directory / 'escape'
        alias.symlink_to(self.inputs)
        with self.assertRaises(ValueError):
            resolve_ref('run:escape', self.source, batch.directory)
        for reference in ('run:nested/../result.json', 'run:escape', 'run:/etc/passwd', 'file:result.json'):
            changed = copy.deepcopy(report)
            changed['outputs'] = {reference: digest(output)}
            self.assertTrue(verify(changed, root=self.source, expected_current=self.runtime))

    def test_version_one_reports_remain_readable(self):
        names = ('input.json', 'output.json', 'stdout.txt', 'stderr.txt')
        for name in names:
            (self.source / name).write_text(name)
        report = {'schema_version': 'execution-batch/1', 'run_id': 'historical',
                  'runtime_before': self.runtime, 'runtime_after': self.runtime,
                  'inputs': {'input.json': digest(self.source / 'input.json')},
                  'outputs': {'output.json': digest(self.source / 'output.json')}, 'passed': True,
                  'runs': [{'ordinal': 1, 'exit_code': 0, 'expected_exit_code': 0, 'matches_expected': True,
                            'stdout': {'path': 'stdout.txt', 'sha256': digest(self.source / 'stdout.txt')},
                            'stderr': {'path': 'stderr.txt', 'sha256': digest(self.source / 'stderr.txt')}}]}
        self.assertEqual([], verify(report, root=self.source, expected_current=self.runtime))


class VerificationPrerequisiteTest(unittest.TestCase):
    def test_empty_cases_are_blocked_with_no_traceback(self):
        with tempfile.TemporaryDirectory(prefix='togaf-empty-') as tmp:
            root = Path(tmp)
            for script in ('verify_method_case_constraints.py', 'verify_method_reasoning.py'):
                with self.subTest(script=script):
                    output = root / (script + '.json')
                    result = subprocess.run([sys.executable, str(SCRIPTS / script), '--cases-dir', str(root), '--out', str(output)], cwd='/tmp', capture_output=True, text=True)
                    self.assertEqual(3, result.returncode, result.stdout + result.stderr)
                    self.assertEqual('blocked', json.loads(output.read_text())['status'])
                    self.assertNotIn('Traceback', result.stderr)

    def test_missing_scale_inputs_are_structurally_reported(self):
        with tempfile.TemporaryDirectory(prefix='togaf-scale-') as tmp:
            output = Path(tmp) / 'output'
            result = subprocess.run([sys.executable, str(SCRIPTS / 'verify_scale_cases.py'), '--dataset-dir', str(Path(tmp) / 'absent'), '--out', str(output)], cwd='/tmp', capture_output=True, text=True)
            self.assertEqual(3, result.returncode, result.stdout + result.stderr)
            report = json.loads((output / 'report.json').read_text())
            self.assertEqual('blocked', report['status'])
            self.assertTrue(report['missing_requirements'])
            self.assertNotIn('Traceback', result.stderr)

    def test_historical_empty_suite_is_blocked(self):
        with tempfile.TemporaryDirectory(prefix='togaf-history-') as tmp:
            with patch('run_remediation_acceptance.ROOT', Path(tmp)):
                self.assertTrue(historical_preflight(['tests'], False))
            output = Path(tmp) / 'output'
            result = subprocess.run([sys.executable, str(SCRIPTS / 'run_remediation_acceptance.py'), '--stages', 'tests', '--no-render', '--out', str(output)], cwd='/tmp', capture_output=True, text=True)
            self.assertEqual(3, result.returncode, result.stdout + result.stderr)
            report = json.loads((output / 'repair-summary.json').read_text())
            self.assertEqual('blocked', report['status'])
            self.assertFalse(report['engineering_passed'])

    def test_scale_requires_template_beside_external_dataset(self):
        with tempfile.TemporaryDirectory(prefix='togaf-scale-preflight-') as tmp:
            dataset = Path(tmp) / 'dataset'
            (dataset / 'context').mkdir(parents=True)
            (dataset / 'context/one.json').write_text(json.dumps({'entities': [{'id': 'A', 'type': 'application', 'context': {}, 'attributes': {}}]}))
            (dataset / 'relationships.json').write_text('[]')
            self.assertTrue(any('projection-template' in x for x in scale_preflight(dataset)))
            (dataset.parent / 'projection').mkdir()
            (dataset.parent / 'projection/model.json').write_text(json.dumps({'schema_version': '2.0', 'project': {}, 'sources': []}))
            self.assertEqual([], scale_preflight(dataset))


class BrowserToolsTest(unittest.TestCase):
    def test_browser_precedence_and_missing_explicit_path(self):
        script = """
import assert from 'node:assert/strict';
import {resolveBrowser} from './browser_resolver.mjs';
const base={env:{},platform:'linux',home:'/home/example'};
assert.equal(resolveBrowser({...base,bundled:()=>'/cached/chrome',executable:p=>p==='/cached/chrome'}).source,'puppeteer-installed');
assert.equal(resolveBrowser({...base,bundled:()=>'/missing',executable:p=>p==='/usr/bin/chromium'}).executablePath,'/usr/bin/chromium');
assert.equal(resolveBrowser({...base,env:{TOGAF_BROWSER_PATH:'/explicit'},bundled:()=>'/cached/chrome',executable:()=>true}).executablePath,'/explicit');
assert.throws(()=>resolveBrowser({...base,env:{TOGAF_BROWSER_PATH:'/invalid'},bundled:()=>'/cached/chrome',executable:p=>p==='/cached/chrome'}),{code:'BROWSER_EXECUTABLE_INVALID'});
assert.throws(()=>resolveBrowser({...base,bundled:()=>'/missing',executable:()=>false}),{code:'BROWSER_NOT_FOUND'});
console.log('browser resolution cases passed');
"""
        result = subprocess.run(['node', '--input-type=module', '-e', script], cwd=SCRIPTS, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_launch_failure_preserves_cause_without_retry_or_sandbox_bypass(self):
        script = """
import assert from 'node:assert/strict';
import puppeteer from 'puppeteer';
import {launchBrowser} from './browser_resolver.mjs';
process.env.TOGAF_BROWSER_PATH=process.execPath;
const cause=new Error('Protocol error (Target.setDiscoverTargets): Target closed');
let launches=0;
puppeteer.launch=async options=>{
  launches++;assert.equal(options.pipe,true);assert.equal(options.headless,true);
  assert.equal(options.executablePath,process.execPath);
  assert.ok(!(options.args||[]).includes('--no-sandbox'));
  throw cause;
};
await assert.rejects(()=>launchBrowser(),error=>error.code==='BROWSER_LAUNCH_FAILED'&&error.cause===cause&&error.message.includes('browser-unavailable'));
assert.equal(launches,1);
let closed=false;
puppeteer.launch=async()=>({version:async()=>{throw cause;},close:async()=>{closed=true;}});
await assert.rejects(()=>launchBrowser(),error=>error.code==='BROWSER_PROTOCOL_FAILED'&&error.cause===cause);
assert.ok(closed);
"""
        result = subprocess.run(['node', '--input-type=module', '-e', script], cwd=SCRIPTS, capture_output=True, text=True, timeout=10)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def geometry(self, root, env=None):
        root = Path(root)
        (root / 'clipped.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50"><text x="90" y="20" font-size="20">Long clipped label</text></svg>')
        (root / 'manifest.json').write_text(json.dumps({'artifacts': [{'view_id': 'clipped', 'svg': 'clipped.svg'}]}))
        result = subprocess.run(['node', str(SCRIPTS / 'check_geometry.mjs'), str(root / 'manifest.json')], cwd='/tmp', env=env, capture_output=True, text=True, timeout=60)
        return result, json.loads((root / 'geometry-check.json').read_text())

    def test_missing_browser_is_blocked(self):
        with tempfile.TemporaryDirectory(prefix='togaf-no-browser-') as tmp:
            result, report = self.geometry(tmp, {**os.environ, 'TOGAF_BROWSER_PATH': str(Path(tmp) / 'absent')})
            self.assertEqual(3, result.returncode, result.stderr)
            self.assertEqual('blocked', report['status'])
            self.assertEqual(0, report['checked'])

    def test_clipped_text_requires_review(self):
        with tempfile.TemporaryDirectory(prefix='togaf-geometry-') as tmp:
            result, report = self.geometry(tmp)
            if report['status'] == 'blocked' and 'browser-unavailable' in report.get('reason', ''):
                self.skipTest('An installed Chrome/Chromium is required for the real geometry probe')
            self.assertEqual(1, result.returncode, result.stdout + result.stderr)
            self.assertEqual('review-required', report['status'])
            self.assertEqual(1, report['flagged'])
            self.assertTrue(report['browser']['executablePath'])
            self.assertTrue(report['browser']['version'])


if __name__ == '__main__':
    unittest.main()
