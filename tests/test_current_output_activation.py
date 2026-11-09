"""Current entrypoint activation must preserve originals on any validation failure."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / 'togaf-standard-10th-ai/maintenance/activate_current_outputs.py'
spec = importlib.util.spec_from_file_location('current_output_activation', MODULE)
activation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(activation)


def build_fixture(root):
    """Small real HTML/SVG fixture usable by the fixed local UI controller."""
    root = root.resolve()
    current = root / 'output/current'
    old, new = current / 'old', root / 'output/new/profiles'
    old.mkdir(parents=True)
    new.mkdir(parents=True)
    source = root / 'source.py'
    source.write_text('value = 1\n')
    (root / 'README.md').write_text('# Fixture\n')
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="320" height="120"><rect width="320" height="120" fill="white"/><text x="15" y="45" font-size="24">业务需求与架构评审</text></svg>'
    for directory in (old, new):
        (directory / 'example.svg').write_text(svg)
    catalogue = current / 'artifacts.html'
    catalogue.write_text('''<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{margin:12px}table{width:100%}tr[hidden]{display:none}:focus-visible{outline:2px solid orange}</style>
<h1>本地制品图册</h1><a href="../../README.md">阅读说明</a><label for="q">搜索</label><input id="q" type="search"><p id="count"></p>
<table><tbody><tr data-search="four-box 四框业务模型"><td><a href="old/example.svg">四框业务模型图</a></td></tr></tbody></table>
<script>const q=document.querySelector('#q'),rows=[...document.querySelectorAll('tr[data-search]')];q.addEventListener('input',()=>{let n=0;for(const row of rows){row.hidden=!row.dataset.search.includes(q.value.toLowerCase());n+=!row.hidden}document.querySelector('#count').textContent=n+' / '+rows.length});</script></html>''')
    atlas = root / 'atlas.html'
    atlas.write_text('''<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{margin:12px}img{max-width:100%}</style><h1>ADM 图册</h1><nav><a href="#panel-a">架构愿景</a></nav>
<details id="panel-a"><summary>架构愿景</summary><img src="output/new/profiles/example.svg" alt="中文架构流程"></details><a href="README.md">阅读说明</a>
<script>document.querySelector('nav a').addEventListener('click',event=>{event.preventDefault();const panel=document.getElementById('panel-a');panel.open=true;panel.querySelector('summary').focus()})</script></html>''')
    mapping = current / 'current-output-paths.json'
    mapping.write_text(json.dumps({'profiles-current': 'old'}) + '\n')
    round_id, commit = 'fixture-current-entrypoints', 'a' * 40
    prerequisites = {}
    stages = root / 'output/stages'
    stages.mkdir()
    def ref(path):
        return {'path': path.relative_to(root).as_posix(), 'sha256': activation.sha(path)}
    for stage in activation.STAGES:
        data = {'stage': stage, 'round_id': round_id, 'source_commit': commit, 'passed': True}
        if stage == 'source_freeze':
            data['files'] = {p.relative_to(root).as_posix():activation.sha(p) for p in [source,mapping,catalogue]}
            data['entry_inputs'] = {'schema_version':'stabilization-entry-inputs/1','round_id':round_id,
                                   'entries':{'current_map':ref(mapping),'catalogue':ref(catalogue)}}
        if stage == 'model_evaluation':
            data.update(required_items=507, executed_items=507, passed_items=507,
                        unexecuted_items=0, actor_scorer_independent=True)
        path = stages / (stage + '.json')
        path.write_text(json.dumps(data) + '\n')
        prerequisites[stage] = ref(path)
    manifest = {'schema_version': 'current-entrypoint-round/1', 'round_id': round_id, 'source_commit': commit,
                'prerequisites': prerequisites, 'entries': {'current_map': ref(mapping), 'catalogue': ref(catalogue)},
                'output_paths': {'profiles-current': 'output/new/profiles'},
                'targets': [ref(new / 'example.svg'), ref(root / 'README.md')],
                'catalogue': {'expected_rows': 1, 'replacements': [
                    {'map_key': 'profiles-current', 'from': 'old/', 'to': '../new/profiles/'}]},
                'ui': {'atlas': ref(atlas), 'search_term': 'four-box', 'expected_search_rows': 1}}
    return manifest


class CurrentOutputActivationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='togaf-activation-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.manifest = build_fixture(self.root)
        self.paths = {key: self.root / ref['path'] for key, ref in self.manifest['entries'].items()}
        self.before = {key: path.read_bytes() for key, path in self.paths.items()}

    def prepared(self):
        return activation.prepare(self.manifest, repo=self.root)

    def output(self):
        destination = self.root / 'output/evidence'
        destination.mkdir()
        return destination

    def change_stage(self, stage, **changes):
        ref = self.manifest['prerequisites'][stage]
        path = self.root / ref['path']
        data = json.loads(path.read_text())
        data.update(changes)
        path.write_text(json.dumps(data) + '\n')
        ref['sha256'] = activation.sha(path)

    def assert_originals(self):
        self.assertEqual(self.before, {key: path.read_bytes() for key, path in self.paths.items()})

    def test_preparation_verifies_one_round_without_mutating_current_entries(self):
        prepared = self.prepared()
        self.assertTrue(prepared['result']['prepared'])
        self.assertFalse(prepared['result']['applied'])
        self.assertFalse(prepared['result']['passed'])
        self.assertEqual({'profiles-current': '../new/profiles'}, json.loads(prepared['new_bytes']['current_map']))
        self.assertIn(b'../new/profiles/example.svg', prepared['new_bytes']['catalogue'])
        self.assertEqual('local-test-controller', prepared['ui_request']['runtime_mode'])
        self.assert_originals()

    def test_repository_relative_parent_links_are_allowed(self):
        source = self.paths['catalogue']
        self.assertEqual(self.root / 'README.md', activation.local_href_target('../../README.md', source, repo=self.root))
        self.assertEqual(self.root / 'README.md', activation.local_href_target('../current/../../README.md', source, repo=self.root))

    def test_escape_protocols_absolute_encoding_and_controls_are_rejected(self):
        for url in ('../../../outside.md', '/README.md', '%2FREADME.md', 'https://example.org/a',
                    'javascript:alert(1)', 'file:///etc/hosts', 'data:text/html,x', '//example.org/a',
                    'a\\b', 'a%00b', '%252e%252e/README.md', 'a%0ab'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                activation.local_href_target(url, self.paths['catalogue'], repo=self.root)
        self.assert_originals()

    def test_symlink_file_parent_and_symlink_followed_by_parent_are_rejected(self):
        folder = self.root / 'output/current'
        (folder / 'alias.svg').symlink_to(folder / 'old/example.svg')
        (folder / 'alias').symlink_to(folder / 'old', target_is_directory=True)
        for url in ('alias.svg', 'alias/example.svg', 'alias/../old/example.svg'):
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, 'Symlink'):
                activation.local_href_target(url, self.paths['catalogue'], repo=self.root)

    def test_missing_stale_and_unfingerprinted_output_files_block_preparation(self):
        target = self.root / self.manifest['targets'][0]['path']
        original = target.read_bytes()
        target.unlink()
        with self.assertRaisesRegex(ValueError, 'Missing'):
            self.prepared()
        target.write_bytes(original + b' ')
        with self.assertRaisesRegex(ValueError, 'fingerprint'):
            self.prepared()
        target.write_bytes(original)
        (target.parent / 'unlisted.svg').write_bytes(original)
        with self.assertRaisesRegex(ValueError, 'fully fingerprinted'):
            self.prepared()
        self.assert_originals()

    def test_unfingerprinted_catalogue_link_blocks_preparation(self):
        self.manifest['targets'].pop()
        with self.assertRaisesRegex(ValueError, 'lacks a fingerprint'):
            self.prepared()
        self.assert_originals()

    def test_duplicate_targets_and_different_catalogue_map_prefixes_are_rejected(self):
        original = copy.deepcopy(self.manifest)
        self.manifest['targets'].append(self.manifest['targets'][0])
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.prepared()
        self.manifest = original
        self.manifest['catalogue']['replacements'][0]['to'] = 'old/'
        with self.assertRaises(ValueError):
            self.prepared()
        self.assert_originals()

    def test_failed_missing_and_cross_round_prerequisites_are_rejected(self):
        for stage in activation.STAGES:
            with self.subTest(stage=stage):
                original = copy.deepcopy(self.manifest)
                path = self.root / self.manifest['prerequisites'][stage]['path']
                before = path.read_bytes()
                self.change_stage(stage, passed=False)
                with self.assertRaisesRegex(ValueError, 'Prerequisite failed'):
                    self.prepared()
                path.write_bytes(before)
                self.manifest = original
        self.change_stage('engineering_verification', round_id='another-round')
        with self.assertRaisesRegex(ValueError, 'another version'):
            self.prepared()
        self.manifest['prerequisites'].pop('package_verification')
        with self.assertRaisesRegex(ValueError, 'five prerequisite'):
            self.prepared()
        self.assert_originals()

    def test_incomplete_or_nonindependent_evaluation_never_authorizes_activation(self):
        for changes in ({'executed_items': 506}, {'passed_items': 506}, {'unexecuted_items': 1},
                        {'actor_scorer_independent': False}):
            with self.subTest(changes=changes):
                self.change_stage('model_evaluation', required_items=507, executed_items=507, passed_items=507,
                                  unexecuted_items=0, actor_scorer_independent=True)
                self.change_stage('model_evaluation', **changes)
                with self.assertRaisesRegex(ValueError, '507-item'):
                    self.prepared()
        self.assert_originals()

    def test_changed_frozen_source_is_rejected(self):
        (self.root / 'source.py').write_text('value = 2\n')
        with self.assertRaisesRegex(ValueError, 'fingerprint'):
            self.prepared()
        self.assert_originals()

    def test_second_replace_failure_restores_both_original_entrypoints(self):
        prepared, out = self.prepared(), self.output()
        calls = []
        def fail_second(path, value):
            calls.append(path)
            if len(calls) == 2:
                raise OSError('injected second replacement failure')
            activation.atomic_write(path, value)
        with self.assertRaisesRegex(OSError, 'second replacement'):
            activation.activate(prepared, out, writer=fail_second,
                                ui_checker=lambda *_: self.fail('UI must not run before both replacements'))
        self.assert_originals()
        evidence = json.loads((out / 'activation.json').read_text())
        self.assertFalse(evidence['passed'])
        self.assertTrue(evidence['rolled_back'])
        for key, path in self.paths.items():
            self.assertEqual(path.relative_to(self.root).as_posix(), evidence['entry_files'][key]['path'])
            self.assertEqual(evidence['before_sha256'][key], evidence['entry_files'][key]['after_sha256'])
            self.assertEqual(self.before[key], (out / 'before' / (key + path.suffix)).read_bytes())
        self.assertEqual([], list(self.root.rglob('*.activation-*')))

    def test_failed_post_activation_ui_restores_originals(self):
        prepared, out = self.prepared(), self.output()
        def fail_ui(request, destination):
            self.assertEqual(prepared['new_bytes'], {key: path.read_bytes() for key, path in self.paths.items()})
            raise ValueError('injected mobile layout failure')
        with self.assertRaisesRegex(ValueError, 'mobile layout'):
            activation.activate(prepared, out, ui_checker=fail_ui)
        self.assert_originals()
        self.assertTrue(json.loads((out / 'activation.json').read_text())['rolled_back'])

    def test_interruption_rolls_back_and_releases_activation_lock(self):
        prepared, out = self.prepared(), self.output()
        def interrupt(*_):
            raise InterruptedError('injected SIGTERM')
        with self.assertRaisesRegex(InterruptedError, 'SIGTERM'):
            activation.activate(prepared, out, ui_checker=interrupt)
        self.assert_originals()
        self.assertFalse((self.paths['current_map'].parent / '.current-output-activation.lock').exists())
        self.assertTrue(json.loads((out / 'activation.json').read_text())['rolled_back'])

    def test_second_maintenance_activation_is_refused_while_locked(self):
        prepared, out = self.prepared(), self.output()
        lock = self.paths['current_map'].parent / '.current-output-activation.lock'
        lock.write_text('another maintenance operation')
        with self.assertRaises(FileExistsError):
            activation.activate(prepared, out)
        self.assert_originals()
        self.assertEqual('another maintenance operation', lock.read_text())

    def test_uncoordinated_user_edit_is_not_overwritten_during_rollback(self):
        prepared, out = self.prepared(), self.output()
        def editing_ui(*_):
            self.paths['catalogue'].write_text('concurrent user edit')
            raise ValueError('concurrent edit')
        with self.assertRaisesRegex(ValueError, 'concurrent edit'):
            activation.activate(prepared, out, ui_checker=editing_ui)
        self.assertEqual(self.before['current_map'], self.paths['current_map'].read_bytes())
        self.assertEqual('concurrent user edit', self.paths['catalogue'].read_text())
        evidence = json.loads((out / 'activation.json').read_text())
        self.assertFalse(evidence['rolled_back'])
        for key, path in self.paths.items():
            self.assertEqual(activation.sha(path), evidence['entry_files'][key]['after_sha256'])
        self.assertTrue(any('Concurrent entry change' in reason for reason in evidence['rollback_errors']))

    def test_successful_fixture_activation_records_ui_and_preserves_pending_signatures(self):
        prepared, out = self.prepared(), self.output()
        def success_ui(request, destination):
            self.assertEqual(prepared['new_bytes'], {key: path.read_bytes() for key, path in self.paths.items()})
            self.assertEqual('local-test-controller', request['runtime_mode'])
            return {'passed': True, 'runtime_mode': 'local-test-controller'}
        result = activation.activate(prepared, out, ui_checker=success_ui)
        self.assertTrue(result['passed'])
        self.assertTrue(result['applied'])
        self.assertFalse(result['rolled_back'])
        for key, path in self.paths.items():
            self.assertEqual(path.relative_to(self.root).as_posix(), result['entry_files'][key]['path'])
            self.assertEqual(result['before_sha256'][key], result['entry_files'][key]['before_sha256'])
            self.assertEqual(activation.sha(path), result['entry_files'][key]['after_sha256'])
            self.assertNotEqual(result['entry_files'][key]['before_sha256'], result['entry_files'][key]['after_sha256'])
        self.assertEqual('pending_signature', result['organization_approval'])
        self.assertEqual('pending_signature', result['professional_acceptance'])

    def test_entry_changed_after_preparation_is_not_overwritten(self):
        prepared, out = self.prepared(), self.output()
        self.paths['catalogue'].write_text('concurrent entry change')
        with self.assertRaisesRegex(ValueError, 'changed after preparation'):
            activation.activate(prepared, out)
        self.assertEqual('concurrent entry change', self.paths['catalogue'].read_text())
        self.assertEqual(self.before['current_map'], self.paths['current_map'].read_bytes())

    def test_git_version_guard_rejects_different_head_and_dirty_source(self):
        clean = subprocess.CompletedProcess([], 0, 'a' * 40 + '\n', '')
        dirty = subprocess.CompletedProcess([], 0, ' M source.py\n', '')
        with patch.object(activation.subprocess, 'run', side_effect=[clean, dirty]):
            with self.assertRaisesRegex(ValueError, 'not clean'):
                activation.verify_git_identity(self.root, 'a' * 40)
        with patch.object(activation.subprocess, 'run', return_value=clean):
            with self.assertRaisesRegex(ValueError, 'HEAD differs'):
                activation.verify_git_identity(self.root, 'b' * 40)

    def git_guard(self, status):
        head=subprocess.CompletedProcess([],0,'a'*40+'\n','')
        state=subprocess.CompletedProcess([],0,status,'')
        with patch.object(activation.subprocess,'run',side_effect=[head,state]):
            return activation.verify_git_identity(self.root,'a'*40,
                freeze_ref=self.manifest['prerequisites']['source_freeze'],round_id=self.manifest['round_id'])

    def test_git_guard_allows_only_verified_freeze_generated_changes(self):
        self.change_stage('source_freeze',excluded_generated_paths=sorted(activation.GENERATED_PATHS),
                          excluded_generated_prefixes=sorted(activation.GENERATED_PREFIXES))
        names=['togaf-standard-10th-ai/skills/package-manifest.json',
               'togaf-standard-10th-ai/skills/build-history/new.json',
               'togaf-standard-10th-ai/maintenance/stabilization/rounds/round.json',
               'togaf-standard-10th-ai/quality/implementation-ledger.md']
        self.assertEqual(sorted(names),self.git_guard(''.join(' M '+n+'\0' for n in names)))
        self.assert_originals()

    def test_git_guard_rejects_source_changes_broad_exclusions_and_code_in_generated_scope(self):
        self.change_stage('source_freeze',excluded_generated_paths=sorted(activation.GENERATED_PATHS),
                          excluded_generated_prefixes=sorted(activation.GENERATED_PREFIXES))
        for name in ['source.py','tests/new.py',
                     'togaf-standard-10th-ai/maintenance/stabilization/rounds/injected.py',
                     'togaf-standard-10th-ai/skills/build-history/injected.mjs']:
            with self.subTest(name=name),self.assertRaisesRegex(ValueError,'not clean'):
                self.git_guard('?? '+name+'\0')
        self.change_stage('source_freeze',excluded_generated_prefixes=['tests/'])
        with self.assertRaisesRegex(ValueError,'scope is not authorized'):
            self.git_guard(' M tests/new.py\0')
        self.assert_originals()

    def test_git_guard_does_not_allow_rename_of_source_to_generated_file(self):
        self.change_stage('source_freeze',excluded_generated_paths=sorted(activation.GENERATED_PATHS))
        with self.assertRaisesRegex(ValueError,'not clean'):
            self.git_guard('R  togaf-standard-10th-ai/skills/package-manifest.json\0source.py\0')

    def test_git_guard_rejects_unresolved_conflict_in_generated_file(self):
        self.change_stage('source_freeze',excluded_generated_paths=sorted(activation.GENERATED_PATHS))
        with self.assertRaisesRegex(ValueError,'unresolved Git conflict'):
            self.git_guard('UU togaf-standard-10th-ai/skills/package-manifest.json\0')

    def test_git_guard_rejects_stale_freeze_or_generated_overlap_with_frozen_source(self):
        ref=self.manifest['prerequisites']['source_freeze']
        self.change_stage('source_freeze',excluded_generated_paths=sorted(activation.GENERATED_PATHS))
        ref['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'fingerprint'):
            self.git_guard(' M togaf-standard-10th-ai/skills/package-manifest.json\0')
        ref['sha256']=activation.sha(self.root/ref['path'])
        generated=self.root/'togaf-standard-10th-ai/skills/package-manifest.json'
        generated.parent.mkdir(parents=True,exist_ok=True);generated.write_text('{}\n')
        files=json.loads((self.root/ref['path']).read_text())['files']
        files[generated.relative_to(self.root).as_posix()]=activation.sha(generated)
        self.change_stage('source_freeze',files=files)
        with self.assertRaisesRegex(ValueError,'overlap frozen source'):
            self.git_guard(' M '+generated.relative_to(self.root).as_posix()+'\0')

    def test_verified_freeze_data_allows_exact_activated_entry_hashes_only(self):
        frozen=json.loads((self.root/self.manifest['prerequisites']['source_freeze']['path']).read_text())
        entry=self.paths['catalogue'];entry.write_text('activated entry bytes')
        name=entry.relative_to(self.root).as_posix()
        head=subprocess.CompletedProcess([],0,'a'*40+'\n','')
        dirty=subprocess.CompletedProcess([],0,' M '+name+'\0','')
        with patch.object(activation.subprocess,'run',side_effect=[head,dirty]):
            self.assertEqual([name],activation.verify_git_identity(self.root,'a'*40,freeze_data=frozen,
                round_id=self.manifest['round_id'],replacements={name:activation.sha(entry)}))
        with patch.object(activation.subprocess,'run',return_value=head):
            with self.assertRaisesRegex(ValueError,'Only frozen current entry'):
                activation.verify_git_identity(self.root,'a'*40,freeze_data=frozen,round_id=self.manifest['round_id'],
                    replacements={'source.py':activation.sha(self.root/'source.py')})

    def test_manifest_cannot_substitute_an_entry_after_source_freeze(self):
        alternate=self.root/'output/current/alternate.html';alternate.write_bytes(self.before['catalogue'])
        self.manifest['entries']['catalogue']={'path':alternate.relative_to(self.root).as_posix(),'sha256':activation.sha(alternate)}
        with self.assertRaisesRegex(ValueError,'differ from frozen entry inputs'):self.prepared()

    def test_source_freeze_missing_entry_inputs_is_not_a_current_round(self):
        self.change_stage('source_freeze',entry_inputs=None)
        with self.assertRaisesRegex(ValueError,'Frozen entry inputs'):self.prepared()


if __name__ == '__main__':
    unittest.main()
