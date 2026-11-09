"""Deterministic fake-runtime attacks; never independent model review evidence."""
import copy
import importlib.util
import json
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
import unittest

from enterprise import material_review as module
from enterprise.runtime import Blocked, sha256


class FakeBudget:
    def __init__(self, state=None):
        self.value = copy.deepcopy(state or {'started_wall': 12345, 'batch': 1, 'batch_started_wall': 12346,
            'batch_session_start': 0, 'batch_history': [], 'sessions': [], 'consecutive_timeouts': 0,
            'consecutive_429': 0, 'stop_reason': None})
        self.limit = 4000

    def check(self):
        if self.value['stop_reason']: raise Blocked(self.value['stop_reason'])
        if len(self.value['sessions']) >= self.limit: raise Blocked('shared session allowance exhausted')

    def allocate_session(self, name, role):
        self.check(); number = len(self.value['sessions']) + 1
        self.value['sessions'].append({'number': number, 'case_id': name, 'role': role})
        return number

    def state(self): return copy.deepcopy(self.value)
    def trip(self, reason): self.value['stop_reason'] = reason


class FakeRuntime:
    """Emit synthetic native-shaped logs; only the local read probe is executed."""
    def __init__(self, root, budget, edit=None, inspect=True, view_images=True, thread=None, failure=None):
        self.root = root; self.budget = budget; self.directory = root / ('runtime-' + str(len(list(root.glob('runtime-*')))))
        self.directory.mkdir(); self.home = self.directory / 'private'; self.home.mkdir(); self.shared = root / 'shared'
        self.edit = edit; self.inspect = inspect; self.view_images = view_images; self.thread = thread; self.failure = failure
        self.binary = root / 'native-binary'; self.binary.write_text('synthetic identity, never executed\n')
        frozen = {'source_hashes': {'fixture': 'a' * 64}, 'frozen_hashes': {'fixture': 'a' * 64},
                  'dependency_hashes': {'fixture': 'b' * 64}, 'python': str(self.shared / '.venv/bin/python')}
        module.write_new(self.directory / 'frozen-runtime-manifest.json', frozen)
        self.metadata = {'source_commit': 'a' * 40, 'source_config_sha256': 'b' * 64, 'permissions_sha256': 'c' * 64,
            'model': 'existing-fixture-model', 'provider': 'existing-fixture-provider', 'model_reasoning_effort': 'existing',
            'frozen_runtime_manifest_sha256': sha256(self.directory / 'frozen-runtime-manifest.json'),
            'codex_binary': {'path': str(self.binary), 'sha256': sha256(self.binary)}}
        module.write_new(self.directory / 'preflight.json', {'status': 'pass', 'toolchain': {'status': 'pass'}, 'fixture': True})
        self.workspaces = {}; self.calls = []

    def workspace(self, name, expose_skills):
        if expose_skills: raise AssertionError('material reviewer may not expose Actor skills/rubrics')
        root = self.home / 'workspaces' / module.text_sha(name)[:24]; root.mkdir(parents=True)
        self.workspaces[name] = root; return root

    def session(self, name, role, root, prompt, schema, image=None, timeout=600):
        self.calls.append((name, role, timeout)); number = self.budget.allocate_session(name, role)
        if self.failure: raise Blocked(self.failure)
        directory = self.directory / name / role; directory.mkdir(parents=True)
        private = self.home / 'sessions' / str(number)
        module.write_new(directory / 'schema.json', schema); (directory / 'prompt.txt').write_text(prompt)
        plan = module.load(root / 'read-plan.json'); results = []
        events = [{'type': 'thread.started', 'thread_id': self.thread or ('fixture-thread-' + str(number))}, {'type': 'turn.started'}]
        for unit_id, relative in plan['unit_files'].items():
            payload = module.load(root / relative)
            row = copy.deepcopy(payload['binding']); row.update(classification='body', disposition='retain and compare the located body',
                findings=[], revision='', review_status='pass', evidence={'source_quote': payload['source_text'],
                'candidate_quotes': [{'context_id': k, 'quote': v} for k, v in payload['candidate_text'].items() if v.strip()],
                'reason': 'synthetic fixture comparison of exact source and candidate'})
            results.append(row)
            if self.inspect:
                read = subprocess.run([sys.executable, '-B', str(root / 'material_read.py'), unit_id], cwd=root,
                                      capture_output=True, text=True, check=True)
                events.append({'type': 'item.completed', 'item': {'type': 'command_execution',
                    'command': shlex.join([str(self.shared / '.venv/bin/python'), 'material_read.py', unit_id]),
                    'exit_code': 0, 'aggregated_output': read.stdout}})
        if self.view_images:
            for relative in plan['source_image_files'].values():
                events.append({'type': 'item.completed', 'item': {'type': 'mcp_tool_call', 'tool': 'functions.view_image',
                    'status': 'completed', 'arguments': {'path': relative}}})
        result = {'shard_id': plan['shard_id'], 'source_commit': self.metadata['source_commit'],
            'input_manifest_sha256': plan['input_manifest_sha256'], 'shard_sha256': plan['shard_sha256'],
            'review_phase': plan['review_phase'], 'unit_results': results}
        if self.edit: self.edit(result, events)
        events.append({'type': 'turn.completed', 'usage': {'input_tokens': 5, 'cached_input_tokens': 1, 'output_tokens': 3}})
        (directory / 'stdout.jsonl').write_text(''.join(json.dumps(e) + '\n' for e in events)); (directory / 'stderr.log').write_text('')
        module.write_new(directory / 'final.json', result)
        argv = [str(self.binary), '--no-daemon', '-a', 'never', '-c', 'default_permissions=' + json.dumps('enterprise-' + role),
                '-c', 'shell_environment_policy.set.TMPDIR=' + json.dumps(str(root / '.tmp')), 'exec', '--ephemeral', '--json',
                '--ignore-rules', '--skip-git-repo-check', '-C', str(root), '--output-schema', str(private / 'schema.json'),
                '--output-last-message', str(private / 'final.json'), '--color', 'never', '-']
        command = {'argv': argv, 'exit_code': 0, 'seconds': .01, 'status': 'pass'}; module.write_new(directory / 'command.json', command)
        identity = {'role': role, 'workspace_name': name + '-scoring', 'live_workspace': str(root.resolve()),
            'source_commit': self.metadata['source_commit'], 'frozen_runtime_manifest_sha256': self.metadata['frozen_runtime_manifest_sha256'],
            'schema_sha256': sha256(directory / 'schema.json'), 'prompt_sha256': sha256(directory / 'prompt.txt'),
            'command_sha256': sha256(directory / 'command.json'), 'events_sha256': sha256(directory / 'stdout.jsonl'),
            'thread_id': events[0]['thread_id'], 'attached_image': None}
        session = {**command, 'session_number': number, 'usage': [events[-1]['usage']], 'event_count': len(events),
            'command_event_count': sum(e.get('item', {}).get('type') == 'command_execution' for e in events),
            'tool_event_count': sum(e.get('item', {}).get('type') in ('command_execution', 'mcp_tool_call') for e in events),
            'execution_identity': identity}
        module.write_new(directory / 'session.json', session); return result, session


class MaterialCollectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name).resolve()
        self.budget = FakeBudget(); self.create_inputs()

    def tearDown(self): self.temp.cleanup()

    def write(self, relative, data):
        path = self.root / relative; path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n'); return module.ref(path, self.root)

    def create_inputs(self, count=2, missing=False, image=False, shards=1):
        (self.root / 'original.html').write_text('original fixture source, never normative')
        source = module.ref(self.root / 'original.html', self.root)
        rows = [{'id': 'unit-' + str(i), 'text_en': 'Source body ' + str(i)} for i in range(count)]
        docref = self.write('document.json', {'blocks': rows, 'toc': [], 'footnotes': []})
        zh = self.write('candidate.json', {'blocks': [{'text_zh': '候选正文 ' + str(i)} for i in range(count)]})
        inputs = {x['path']: x['sha256'] for x in (source, docref, zh)}; units = []; contexts = {}
        if image:
            (self.root / 'source.png').write_bytes(b'synthetic image identity, no model image review')
            image_ref = module.ref(self.root / 'source.png', self.root); inputs[image_ref['path']] = image_ref['sha256']
        for i, row in enumerate(rows):
            candidate = {'context_id': 'candidate.json#/blocks/' + str(i), 'reference': zh,
                'json_pointer': '/blocks/' + str(i), 'text_sha256': module.text_sha('候选正文 ' + str(i)), 'alignment': 'unit', 'status': 'pending'}
            units.append({'id': row['id'], 'document_id': 'fixture-volume', 'family': 'fundamental', 'kind': 'web-block',
                'text_en': row['text_en'], 'source_content_sha256': module.text_sha(row['text_en']), 'source': source,
                'source_document': docref, 'source_locator': {'json_pointer': '/blocks/' + str(i)}, 'classification': 'body',
                'source_material_form': 'image' if image else 'text', 'translation_candidates': [] if missing else [candidate],
                **({'source_images': [image_ref]} if image else {})})
            if not missing: contexts[candidate['context_id']] = {'reference': zh, 'json_pointer': candidate['json_pointer'], 'text_zh': '候选正文 ' + str(i)}
        inventory = {'schema_version': 'full-material-source-unit-inventory/1', 'input_sha256': inputs, 'units': units,
            'documents': [{'document_id': 'fixture-volume', 'family': 'fundamental', 'source_document': docref}]}
        inventory_ref = self.write('preparation/inventory.json', inventory); entries = []
        for n in range(shards):
            part = units[n::shards]
            if not part: continue
            cid = {c['context_id'] for u in part for c in u['translation_candidates']}
            context = {key: contexts[key] for key in cid}; identity = 'material-review-' + str(n+1)
            shard = {'schema_version': 'independent-material-review-shard/1', 'id': identity, 'document_id': 'fixture-volume',
                'units': part, 'candidate_translation_context': context, 'content_characters': sum(len(u['text_en']) for u in part) + sum(len(c['text_zh']) for c in context.values()), 'character_budget': 24000}
            sref = self.write('preparation/shards/' + identity + '.json', shard)
            entries.append({'id': identity, **sref, 'document_id': 'fixture-volume', 'unit_ids': [u['id'] for u in part]})
        # Source inventory is ordered by actual shard assignment in this fixture.
        inventory['units'] = [u for e in entries for u in self.root_shard(e)['units']]
        inventory_ref = self.write('preparation/inventory.json', inventory)
        self.manifest = self.write('preparation/manifest.json', {'schema_version': 'independent-material-review-inputs/1',
            'source_unit_inventory': inventory_ref, 'input_sha256': inputs, 'source_units': count, 'shard_count': len(entries), 'shards': entries})

    def root_shard(self, entry): return module.load(self.root / entry['path'])

    def run_fake(self, *, out='review', **options):
        runtime = FakeRuntime(self.root, self.budget, **options)
        result = module.dispatch(runtime, self.budget, self.manifest, self.root / out, root=self.root, fixture_execution=True)
        return result, runtime

    def packet(self, out='review'): return module.load(self.root / out / 'collection.json')

    def revised_inputs(self, old_manifest):
        old_inputs = module.ReviewInputs(old_manifest, self.root)
        inventory = copy.deepcopy(old_inputs.inventory)
        candidate_ref = self.write('candidate-v2.json', {'blocks': [{'text_zh': '已修订候选正文 ' + str(i)} for i in range(len(inventory['units']))]})
        inventory['input_sha256'][candidate_ref['path']] = candidate_ref['sha256']
        for i, unit in enumerate(inventory['units']):
            unit['translation_candidates'] = [{'context_id': 'candidate-v2.json#/blocks/' + str(i), 'reference': candidate_ref,
                'json_pointer': '/blocks/' + str(i), 'text_sha256': module.text_sha('已修订候选正文 ' + str(i)), 'alignment': 'unit', 'status': 'pending'}]
        iref = self.write('preparation-v2/inventory.json', inventory); entries = []
        for entry, shard in old_inputs.shards.values():
            shard = copy.deepcopy(shard); shard['units'] = [next(u for u in inventory['units'] if u['id']==identity) for identity in entry['unit_ids']]
            shard['candidate_translation_context'] = {c['context_id']: {'reference': c['reference'], 'json_pointer': c['json_pointer'],
                'text_zh': '已修订候选正文 ' + str(inventory['units'].index(u))} for u in shard['units'] for c in u['translation_candidates']}
            shard['content_characters'] = sum(len(u['text_en']) for u in shard['units']) + sum(len(c['text_zh']) for c in shard['candidate_translation_context'].values())
            sref = self.write('preparation-v2/shards/'+shard['id']+'.json',shard)
            entries.append({'id':shard['id'],**sref,'document_id':shard['document_id'],'unit_ids':entry['unit_ids']})
        return self.write('preparation-v2/manifest.json',{'schema_version':'independent-material-review-inputs/1','source_unit_inventory':iref,
            'input_sha256':inventory['input_sha256'],'source_units':len(inventory['units']),'shard_count':len(entries),'shards':entries})

    def revision(self, previous, old_manifest, new_manifest):
        old_inputs=module.ReviewInputs(old_manifest,self.root);new_inputs=module.ReviewInputs(new_manifest,self.root)
        prior=module.collect_existing(previous,self.root)
        old_results={r['id']:r for r in prior['unit_results']}
        return self.write('revision.json',{'schema_version':'material-review-revisions/1','previous_collection':previous,
            'old_input_manifest_sha256':old_manifest['sha256'],'new_input_manifest_sha256':new_manifest['sha256'],
            'units':[{'id':u['id'],'old_binding':module.unit_binding(old_inputs.by_id[u['id']]),'new_binding':module.unit_binding(u),
                      'findings':old_results[u['id']]['findings'],'revision_note':'explicit fixture candidate revision'} for u in new_inputs.units]})

    def test_actual_probe_and_collection_are_read_only_but_fixture_never_promotes(self):
        before = {p: sha256(self.root / p) for p in module.ReviewInputs(self.manifest, self.root).all_refs}
        result, runtime = self.run_fake()
        self.assertEqual(result['reviewed_units'], 0); self.assertFalse(result['complete'])
        self.assertEqual(result['executed_shards'], 1)
        self.assertEqual(result['attempt_results'][0]['read_unit_ids'], ['unit-0', 'unit-1'])
        self.assertTrue(all(r['fixture_assessed_status'] == 'independently_reviewed' for r in result['unit_results']))
        self.assertEqual(before, {p: sha256(self.root / p) for p in before})
        self.assertEqual(runtime.calls[0][1:], ('scorer', 600)); self.assertEqual(len(self.budget.state()['sessions']), 1)

    def test_manifest_rejects_missing_duplicate_and_wrong_shard_ids(self):
        original = module.load(self.root / 'preparation/manifest.json')
        for edit in ('missing', 'duplicate', 'wrong'):
            with self.subTest(edit=edit):
                value = copy.deepcopy(original)
                if edit == 'missing': value['shards'][0]['unit_ids'].pop()
                elif edit == 'duplicate': value['shards'].append(value['shards'][0])
                else: value['shards'][0]['id'] = 'another-shard'
                reference = self.write('preparation/attacked.json', value)
                with self.assertRaises(ValueError): module.ReviewInputs(reference, self.root)

    def test_all_source_candidate_and_locator_fingerprints_are_rechecked(self):
        for name in ('original.html', 'document.json', 'candidate.json'):
            with self.subTest(name=name):
                path = self.root / name; original = path.read_bytes(); path.write_bytes(original + b' ')
                with self.assertRaises(ValueError): module.ReviewInputs(self.manifest, self.root)
                path.write_bytes(original)
        for pointer in ('/blocks/99', '/blocks/00', '/blocks/~3'):
            with self.assertRaises((ValueError, IndexError, KeyError)): module.pointer({'blocks': [0]}, pointer)

    def test_source_derived_closure_rejects_omitted_body_even_after_rehash(self):
        m = module.load(self.root / self.manifest['path']); inv = module.load(self.root / m['source_unit_inventory']['path'])
        inv['units'].pop(); m['source_unit_inventory'] = self.write('preparation/inventory.json', inv)
        shard = self.root_shard(m['shards'][0]); shard['units'].pop(); shard['candidate_translation_context'].pop('candidate.json#/blocks/1')
        shard['content_characters'] = len(shard['units'][0]['text_en']) + len('候选正文 0')
        sref = self.write(m['shards'][0]['path'], shard); m['shards'][0].update(sref, unit_ids=['unit-0']); m['source_units'] = 1
        attacked = self.write('preparation/omitted.json', m)
        with self.assertRaisesRegex(ValueError, 'unit closure'): module.ReviewInputs(attacked, self.root)

    def test_original_source_binding_must_match_extraction_metadata(self):
        document = module.load(self.root / 'document.json')
        document.update(id='fixture-volume', source={'html_path': 'wrong-source.html', 'html_sha256': module.text_sha('wrong'),
            'mhtml_path': 'captured.mhtml', 'mhtml_sha256': module.text_sha('captured')})
        for name, content in (('wrong-source.html', 'wrong'), ('captured.mhtml', 'captured')):
            path = self.root / 'togaf-standard-10th-ai' / name; path.parent.mkdir(exist_ok=True); path.write_text(content)
        docref = self.write('document.json', document)
        inventory = module.load(self.root / 'preparation/inventory.json')
        inventory['input_sha256'][docref['path']] = docref['sha256']
        for name in ('wrong-source.html', 'captured.mhtml'):
            reference = module.ref(self.root / 'togaf-standard-10th-ai' / name, self.root)
            inventory['input_sha256'][reference['path']] = reference['sha256']
        inventory['documents'][0]['source_document'] = docref
        for unit in inventory['units']: unit['source_document'] = docref
        manifest = module.load(self.root / self.manifest['path'])
        for entry in manifest['shards']:
            shard = self.root_shard(entry)
            shard['units'] = [u for u in inventory['units'] if u['id'] in entry['unit_ids']]
            entry.update(self.write(entry['path'], shard))
        manifest['source_unit_inventory'] = self.write('preparation/inventory.json', inventory)
        manifest['input_sha256'] = inventory['input_sha256']
        attacked = self.write('preparation/attacked.json', manifest)
        with self.assertRaisesRegex(ValueError, 'extraction metadata'): module.ReviewInputs(attacked, self.root)

    def test_unknown_body_gap_and_unrechecked_revision_stay_pending(self):
        def edit(result, events):
            result['unit_results'][0]['classification'] = 'unknown'
            result['unit_results'][1]['revision'] = 'repair qualifier'
            result['unit_results'][1]['findings'] = [{'description': 'missing qualifier', 'source_quote': 'Source'}]
        result, _ = self.run_fake(edit=edit)
        self.assertIn('classification-unknown', result['unit_results'][0]['pending_reasons'])
        self.assertIn('revision-requires-new-input-and-independent-recheck', result['unit_results'][1]['pending_reasons'])
        self.create_inputs(missing=True)
        result, _ = self.run_fake(out='gap-review')
        self.assertTrue(all('body-translation-missing' in r['pending_reasons'] for r in result['unit_results']))

    def test_arbitrary_successful_command_cannot_fake_actual_reading(self):
        def edit(result, events):
            events.append({'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'echo inspected', 'exit_code': 0}})
        result, runtime = self.run_fake(inspect=False, edit=edit)
        self.assertEqual(result['executed_shards'], 0); self.assertEqual(result['reviewed_units'], 0)
        self.assertIn('reading', self.budget.state()['stop_reason']); self.assertEqual(len(runtime.calls), 1)

    def test_visual_observation_is_actual_and_per_unit(self):
        self.create_inputs(image=True)
        result, _ = self.run_fake(view_images=False)
        self.assertTrue(all('required-source-images-not-observed' in r['pending_reasons'] for r in result['unit_results']))
        result, _ = self.run_fake(out='viewed-review')
        self.assertTrue(result['attempt_results'][0]['review_observations']['all_images_observed'])
        self.assertEqual(result['reviewed_units'], 0)

    def test_duplicate_missing_and_changed_final_bindings_are_rejected_and_retained(self):
        edits = [lambda r: r['unit_results'].pop(), lambda r: r['unit_results'].append(copy.deepcopy(r['unit_results'][0])),
                 lambda r: r['unit_results'][0].update(source_content_sha256='0'*64), lambda r: r.update(extra='manufactured-signature')]
        for i, edit in enumerate(edits):
            with self.subTest(edit=i):
                self.budget = FakeBudget(); result, runtime = self.run_fake(out='bad-' + str(i), edit=lambda r,e: edit(r))
                self.assertEqual(result['executed_shards'], 0); self.assertEqual(result['reviewed_units'], 0)
                self.assertIsNotNone(self.budget.state()['stop_reason'])
                self.assertTrue(list((self.root / ('bad-'+str(i)) / 'sessions').glob('*/scorer/final.json')))

    def test_existing_output_and_raw_results_are_immutable(self):
        result, runtime = self.run_fake(); original = (self.root / 'review/collection.json').read_bytes()
        with self.assertRaises(ValueError): module.dispatch(runtime, self.budget, self.manifest, self.root / 'review', root=self.root, fixture_execution=True)
        self.assertEqual((self.root / 'review/collection.json').read_bytes(), original)

    def test_rehashing_summary_counters_cannot_fabricate_review_or_signatures(self):
        self.run_fake(); packet = self.packet(); packet['assessment'].update(reviewed_units=2, pending_units=0, complete=True)
        reference = self.write('review/forged-collection.json', packet)
        with self.assertRaisesRegex(ValueError, 'canonical'): module.collect_existing(reference, self.root)
        packet = self.packet(); packet['assessment']['human_professional_acceptance'] = 'signed'
        with self.assertRaisesRegex(ValueError, 'canonical'): module.collect_existing(self.write('review/forged-signature.json', packet), self.root)

    def test_retained_statistics_workspace_and_command_drift_are_rejected(self):
        self.run_fake(); packet = self.packet(); reference = packet['attempts'][0]; attempt = module.load(self.root / reference['path'])
        source = self.root / attempt['workspace_path'] / 'material_read.py'; old = source.read_bytes(); source.write_bytes(old+b'\n')
        with self.assertRaisesRegex(ValueError, 'workspace'): module.collect_existing(module.ref(self.root / 'review/collection.json', self.root), self.root)
        source.write_bytes(old)
        session_path = self.root / attempt['raw_session_files']['session.json']['path']; session = module.load(session_path)
        session['usage'][0]['output_tokens'] += 1; self.write(attempt['raw_session_files']['session.json']['path'], session)
        attempt['raw_session_files']['session.json'] = module.ref(session_path, self.root)
        packet['attempts'][0] = self.write(reference['path'], attempt)
        attacked = self.write('review/statistics-attack.json', packet)
        with self.assertRaisesRegex(ValueError, 'statistics'): module.collect_existing(attacked, self.root)

    def test_runtime_budget_mismatch_and_unpreflighted_runtime_never_dispatch(self):
        runtime = FakeRuntime(self.root, self.budget)
        with self.assertRaises(Blocked): module.dispatch(runtime, FakeBudget(), self.manifest, self.root/'no-run', root=self.root, fixture_execution=True)
        self.write((runtime.directory/'preflight.json').relative_to(self.root).as_posix(), {'status':'pass', 'toolchain': {'status':'blocked'}})
        with self.assertRaises(Blocked): module.dispatch(runtime, self.budget, self.manifest, self.root/'no-run', root=self.root, fixture_execution=True)
        self.assertEqual(runtime.calls, [])

    def test_native_type_required_without_explicit_fixture_mode(self):
        runtime = FakeRuntime(self.root, self.budget)
        with self.assertRaises(Blocked): module.dispatch(runtime, self.budget, self.manifest, self.root/'no-run', root=self.root)
        self.assertEqual(self.budget.state()['sessions'], [])

    def test_session_limit_timeout_and_resource_trip_preserve_budget(self):
        self.budget.limit = 1; self.create_inputs(count=2, shards=2)
        result, runtime = self.run_fake(); self.assertEqual(len(runtime.calls), 1)
        self.assertEqual(len(self.budget.state()['sessions']), 1); self.assertEqual(result['executed_shards'], 1)
        state = self.budget.state(); self.budget = FakeBudget(state); self.budget.trip('owned RSS limit')
        runtime = FakeRuntime(self.root, self.budget)
        with self.assertRaisesRegex(Blocked, 'RSS'): module.dispatch(runtime, self.budget, self.manifest, self.root/'resource-run', root=self.root, fixture_execution=True)
        self.assertEqual(self.budget.state()['started_wall'], state['started_wall'])

    def test_resumption_reuses_sessions_time_and_skips_already_retained_shards(self):
        self.create_inputs(count=2, shards=2); self.budget.limit=1; self.run_fake()
        previous = module.ref(self.root/'review/collection.json', self.root); state=self.budget.state(); self.budget=FakeBudget(state)
        runtime = FakeRuntime(self.root, self.budget)
        result=module.dispatch(runtime,self.budget,self.manifest,self.root/'continued',root=self.root,resume_from=previous,fixture_execution=True)
        self.assertEqual(len(runtime.calls),1);self.assertEqual(len(self.budget.state()['sessions']),2)
        self.assertEqual(result['executed_shards'],2);self.assertEqual(self.budget.state()['started_wall'],12345)
        self.budget=FakeBudget();runtime=FakeRuntime(self.root,self.budget)
        with self.assertRaisesRegex(Blocked,'reset'):module.dispatch(runtime,self.budget,self.manifest,self.root/'reset',root=self.root,resume_from=previous,fixture_execution=True)

    def test_recheck_without_new_inputs_and_manifest_cannot_promote(self):
        self.run_fake(); previous=module.ref(self.root/'review/collection.json',self.root)
        runtime=FakeRuntime(self.root,self.budget)
        revision=self.write('revision.json',{'schema_version':'material-review-revisions/1','previous_collection':previous,
            'old_input_manifest_sha256':self.manifest['sha256'],'new_input_manifest_sha256':self.manifest['sha256'],'units':[]})
        with self.assertRaisesRegex(ValueError,'new immutable'):module.dispatch(runtime,self.budget,self.manifest,self.root/'recheck',root=self.root,revision_manifest=revision,fixture_execution=True)

    def test_changed_candidates_recheck_on_new_thread_and_keep_old_bytes(self):
        self.run_fake();previous=module.ref(self.root/'review/collection.json',self.root);old=self.manifest
        oldbytes=(self.root/'review/collection.json').read_bytes();new=self.revised_inputs(old);revision=self.revision(previous,old,new)
        runtime=FakeRuntime(self.root,self.budget);runtime.metadata['source_commit']='b'*40
        result=module.dispatch(runtime,self.budget,new,self.root/'recheck',root=self.root,revision_manifest=revision,fixture_execution=True)
        self.assertEqual(result['source_commit'],'b'*40);self.assertEqual(result['executed_shards'],1)
        self.assertEqual(result['attempt_results'][0]['review_phase'],'recheck');self.assertEqual(result['reviewed_units'],0)
        self.assertEqual(result['attempt_results'][0]['thread_id'],'fixture-thread-2')
        self.assertEqual((self.root/'review/collection.json').read_bytes(),oldbytes)

    def test_recheck_cannot_reuse_first_thread_or_reset_campaign(self):
        self.run_fake();previous=module.ref(self.root/'review/collection.json',self.root);old=self.manifest;new=self.revised_inputs(old)
        revision=self.revision(previous,old,new);runtime=FakeRuntime(self.root,self.budget,thread='fixture-thread-1')
        with self.assertRaisesRegex(ValueError,'reused a thread'):module.dispatch(runtime,self.budget,new,self.root/'reused',root=self.root,revision_manifest=revision,fixture_execution=True)
        runtime=FakeRuntime(self.root,FakeBudget())
        with self.assertRaisesRegex(Blocked,'reset'):module.dispatch(runtime,runtime.budget,new,self.root/'reset-recheck',root=self.root,revision_manifest=revision,fixture_execution=True)

    def test_revision_forged_old_binding_and_findings_are_rejected(self):
        self.run_fake();previous=module.ref(self.root/'review/collection.json',self.root);old=self.manifest;new=self.revised_inputs(old)
        revision=self.revision(previous,old,new);value=module.load(self.root/revision['path'])
        value['units'][0]['findings']=[{'description':'invented old defect','source_quote':'Source'}]
        forged=self.write('forged-revision.json',value);runtime=FakeRuntime(self.root,self.budget)
        with self.assertRaisesRegex(ValueError,'prior finding'):module.dispatch(runtime,self.budget,new,self.root/'bad-recheck',root=self.root,revision_manifest=forged,fixture_execution=True)

    def test_same_thread_two_shards_is_rejected(self):
        self.create_inputs(count=2,shards=2)
        with self.assertRaisesRegex(ValueError,'reused a thread'):self.run_fake(thread='shared-fixture-thread')

    def test_shell_wrappers_are_supported_and_echoed_receipts_are_not(self):
        def wrapper(result,events):
            for event in events:
                item=event.get('item',{})
                if item.get('type')=='command_execution':item['command']=shlex.join(['/bin/zsh','-lc',item['command']])
        result,_=self.run_fake(edit=wrapper);self.assertEqual(len(result['attempt_results'][0]['read_unit_ids']),2)
        self.budget=FakeBudget()
        def echo(result,events):
            for event in events:
                item=event.get('item',{})
                if item.get('type')=='command_execution':item['command']='echo '+shlex.quote(item['aggregated_output'])
        result,_=self.run_fake(out='echo-review',edit=echo);self.assertEqual(result['executed_shards'],0)

    def test_concurrency_ramps_one_two_four_without_extra_budget(self):
        self.create_inputs(count=7,shards=7);runtime=FakeRuntime(self.root,self.budget)
        result=module.dispatch(runtime,self.budget,self.manifest,self.root/'ramped',root=self.root,max_workers=4,fixture_execution=True)
        status=module.load(self.root/'ramped/dispatch-status.json')
        self.assertEqual([w['admitted_workers'] for w in status['concurrency_waves']],[1,2,4])
        self.assertEqual(len(self.budget.state()['sessions']),7);self.assertEqual(result['executed_shards'],7)

    def test_timeout_preserves_allocated_session_and_rejected_attempt(self):
        result,runtime=self.run_fake(failure='native session timeout')
        self.assertEqual(len(self.budget.state()['sessions']),1);self.assertEqual(result['executed_shards'],0)
        rejected=list((self.root/'review/sessions').glob('*/rejected-attempt.json'))
        self.assertEqual(len(rejected),1);self.assertIn('timeout',module.load(rejected[0])['reason'])

    def test_actual_shared_campaign_429_trip_is_respected(self):
        from enterprise.campaign import CampaignBudget
        out=self.root/'campaign';out.mkdir();budget=CampaignBudget(out);budget.free_limit=0;budget.begin_batch()
        budget.observe_http(429);budget.observe_http(429);runtime=FakeRuntime(self.root,budget)
        with self.assertRaisesRegex(Blocked,'429'):module.dispatch(runtime,budget,self.manifest,self.root/'blocked',root=self.root,fixture_execution=True)
        self.assertEqual(runtime.calls,[]);self.assertEqual(budget.state()['consecutive_429'],2)

    def test_shared_session_completion_can_reset_counters_without_resetting_budget(self):
        from enterprise.campaign import CampaignBudget
        out = self.root / 'counter-campaign'; out.mkdir(); budget = CampaignBudget(out); budget.free_limit = 0; budget.begin_batch()
        budget.allocate_session('external-1', 'scorer'); budget.observe_session('timeout'); budget.observe_http(429)
        previous = copy.deepcopy(budget.state()); forged = copy.deepcopy(previous)
        forged.update(consecutive_timeouts=0, consecutive_429=0)
        with self.assertRaisesRegex(ValueError, 'reset'): module._verify_budget_states(previous, forged)
        budget.allocate_session('external-2', 'scorer'); budget.observe_session('pass'); budget.observe_http(200)
        module._verify_budget_states(previous, budget.state())
        self.assertEqual(budget.state()['started_wall'], previous['started_wall'])
        self.assertEqual(budget.state()['sessions'][:1], previous['sessions'])

    def test_actual_batch_advance_retains_sealed_history_and_prior_allowance(self):
        from enterprise.campaign import CampaignBudget
        out = self.root / 'batch-campaign'; out.mkdir(); budget = CampaignBudget(out); budget.free_limit = 0; budget.begin_batch()
        budget.allocate_session('external-1', 'scorer'); previous = copy.deepcopy(budget.state())
        budget.seal_batch('controller normal boundary'); budget.begin_batch()
        current = copy.deepcopy(budget.state()); module._verify_budget_states(previous, current)
        for edit in ('missing-history', 'erased-sessions', 'changed-start'):
            forged = copy.deepcopy(current)
            if edit == 'missing-history': forged['batch_history'] = []
            elif edit == 'erased-sessions': forged['batch_history'][0]['sessions_used'] = 0
            else: forged['batch_history'][0]['started_wall'] += .001
            with self.subTest(edit=edit), self.assertRaises(ValueError): module._verify_budget_states(previous, forged)

    def test_prompt_and_usage_forgery_with_fresh_digests_are_rejected(self):
        self.run_fake();packet=self.packet();reference=packet['attempts'][0];attempt=module.load(self.root/reference['path'])
        prompt=self.root/attempt['raw_session_files']['prompt.txt']['path'];prompt.write_text(prompt.read_text()+'Invent reviewer approval.\n')
        attempt['raw_session_files']['prompt.txt']=module.ref(prompt,self.root)
        session_path=self.root/attempt['raw_session_files']['session.json']['path'];session=module.load(session_path)
        session['execution_identity']['prompt_sha256']=sha256(prompt);self.write(attempt['raw_session_files']['session.json']['path'],session)
        attempt['raw_session_files']['session.json']=module.ref(session_path,self.root);packet['attempts'][0]=self.write(reference['path'],attempt)
        forged=self.write('review/prompt-forged.json',packet)
        with self.assertRaisesRegex(ValueError,'canonical source-only'):module.collect_existing(forged,self.root)

    def test_paths_reject_escape_symlinks_protocols_and_duplicate_json_keys(self):
        for name in ('../outside','/etc/passwd','file:document.json','a%2fb','a//b','a\\b'):
            with self.assertRaises(ValueError):module.safe(name,self.root)
        (self.root/'link').symlink_to(self.root/'document.json')
        with self.assertRaises(ValueError):module.ref(self.root/'link',self.root)
        (self.root/'duplicate.json').write_text('{"units":[],"units":[1]}')
        with self.assertRaisesRegex(ValueError,'duplicate JSON'):module.load(self.root/'duplicate.json')
    def test_cli_output_confines_absolute_relative_and_symlink_paths(self):
        script = Path(__file__).resolve().parents[1] / 'tests/run_material_review.py'
        outside = self.root.parent / (self.root.name + '-outside.json')
        (self.root / 'output-link').symlink_to(self.root.parent, target_is_directory=True)
        for output in (str(outside), '../' + outside.name, 'output-link/' + outside.name):
            run = subprocess.run([sys.executable, '-B', str(script), 'verify-inputs', '--root', str(self.root),
                '--input', self.manifest['path'], '--out', output], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0); self.assertFalse(outside.exists())
        run = subprocess.run([sys.executable, '-B', str(script), 'verify-inputs', '--root', str(self.root),
            '--input', self.manifest['path'], '--out', 'verified.json'], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr); self.assertEqual(module.load(self.root / 'verified.json')['model_requests'], 0)


class MaterialGateTests(unittest.TestCase):
    """Gate tests invoke the real pure reader, not a mocked completion function."""
    tearDown = MaterialCollectionTests.tearDown
    write = MaterialCollectionTests.write
    create_inputs = MaterialCollectionTests.create_inputs
    root_shard = MaterialCollectionTests.root_shard
    run_fake = MaterialCollectionTests.run_fake
    packet = MaterialCollectionTests.packet

    def setUp(self):
        MaterialCollectionTests.setUp(self)
        path=Path(__file__).resolve().parents[1]/'togaf-standard-10th-ai/maintenance/stabilization_material_evidence.py'
        spec=importlib.util.spec_from_file_location('material_gate_test',path);self.gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.gate)

    def test_gate_recomputes_fixtures_and_stays_incomplete(self):
        self.run_fake();reference=module.ref(self.root/'review/collection.json',self.root)
        before={p.relative_to(self.root).as_posix():sha256(p) for p in self.root.rglob('*') if p.is_file() and not p.is_symlink()}
        result=self.gate.material_checks({'source_commit':'a'*40,'material_review':reference,'material_input_manifest':self.manifest},self.root)
        self.assertEqual(result['status'],'incomplete');self.assertFalse(result['complete']);self.assertEqual(result['reviewed_units'],0)
        after={p.relative_to(self.root).as_posix():sha256(p) for p in self.root.rglob('*') if p.is_file() and not p.is_symlink()}
        self.assertEqual(before,after)

    def test_gate_rejects_version_and_single_fake_unit_labels(self):
        self.run_fake();reference=module.ref(self.root/'review/collection.json',self.root)
        self.assertEqual(self.gate.material_checks({'source_commit':'b'*40,'material_review':reference},self.root)['status'],'invalid')
        fake=self.write('fake.json',{'source_commit':'a'*40,'reviewed_units':34571,'complete':True,'units':[{'id':'one','status':'pass'}]})
        self.assertEqual(self.gate.material_checks({'source_commit':'a'*40,'material_review':fake},self.root)['status'],'invalid')


if __name__=='__main__':unittest.main()
