"""Independent attacks on retained session identity and observed scorer review.

These are synthetic event records, not model sessions or 507-item completion
evidence. Rehashing forged records must not bypass semantic evidence checks.
"""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from enterprise.review_evidence import canonical_observations, observed_review


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'stabilization_model_evidence_test_target',
    REPO / 'togaf-standard-10th-ai/maintenance/stabilization_evidence.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class RetainedModelEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.runtime = self.root / 'agents-01'
        self.runtime.mkdir()
        self.binary = self.root / 'codex-local'
        self.binary.write_bytes(b'local synthetic binary identity\n')
        self.commit = 'a' * 40
        self.metadata = {
            'source_commit': self.commit,
            'frozen_runtime_manifest_sha256': 'b' * 64,
            'codex_binary': {'path': str(self.binary), 'sha256': module.sha(self.binary)},
            'workspace_bindings': {},
        }
        self.base, self.workspace, self.artifacts, self.session = self.case_fixture('case-000')

    def tearDown(self):
        self.temp.cleanup()

    @staticmethod
    def write(path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

    def case_fixture(self, name, actor_number=1, scorer_number=2):
        base = self.runtime / name
        base.mkdir()
        actor_workspace = base / 'workspace'
        actor_workspace.mkdir()
        scoring_workspace = self.runtime / (name + '-scoring') / 'workspace'
        (scoring_workspace / 'actual-output').mkdir(parents=True)
        artifacts = {}
        for relative, content in (('raw-input.json', b'{"request":"synthetic"}\n'),
                                  ('first.png', b'first synthetic image\n'),
                                  ('second.png', b'second synthetic image\n')):
            path = actor_workspace / relative
            path.write_bytes(content)
            artifacts[relative] = {'sha256': module.sha(path), 'bytes': path.stat().st_size}
            shutil.copyfile(path, scoring_workspace / 'actual-output' / relative)
        for role, workspace_name, number, workspace in (
                ('actor', name, actor_number, actor_workspace),
                ('scorer', name + '-scoring', scorer_number, scoring_workspace)):
            live = self.root / 'removed-live-home' / 'workspaces' / workspace_name
            self.metadata['workspace_bindings'][workspace_name] = {
                'live_path': str(live),
                'retained_path': workspace.relative_to(self.runtime).as_posix(),
            }
            self.make_session(base, role, workspace_name, number, live, artifacts)
        scorer = json.loads((base / 'scorer/session.json').read_text())
        return base, scoring_workspace, artifacts, scorer

    def make_session(self, base, role, workspace_name, number, live, artifacts):
        directory = base / role
        directory.mkdir()
        private = self.root / 'removed-live-home' / 'sessions' / str(number)
        argv = [str(self.binary), '--no-daemon', '-a', 'never', '-c',
                'default_permissions=' + json.dumps('enterprise-' + role), '-c',
                'shell_environment_policy.set.TMPDIR=' + json.dumps(str(live / '.tmp')),
                'exec', '--ephemeral', '--json', '--ignore-rules', '--skip-git-repo-check',
                '-C', str(live), '--output-schema', str(private / 'schema.json'),
                '--output-last-message', str(private / 'final.json'), '--color', 'never']
        attached = 'actual-output/first.png' if role == 'scorer' else None
        if attached:
            argv += ['--image', str(live / attached)]
        argv += ['-']
        command = {'argv': argv, 'exit_code': 0, 'seconds': .1, 'status': 'pass'}
        self.write(directory / 'command.json', command)
        self.write(directory / 'schema.json', {'type': 'object', 'properties': {
            'status': {'type': 'string'}}, 'required': ['status']})
        self.write(directory / 'final.json', {'status': 'pass'})
        (directory / 'prompt.txt').write_text('Inspect the retained synthetic evidence.\n')
        events = [
            {'type': 'thread.started', 'thread_id': 'thread-' + workspace_name},
            {'type': 'turn.started'},
            {'type': 'item.completed', 'item': {'type': 'command_execution', 'command':
                'python -c "from pathlib import Path; print(Path(\'rubric.json\').read_text())"',
                'exit_code': 0}},
        ]
        if role == 'scorer':
            events.append({'type': 'item.completed', 'item': {'type': 'mcp_tool_call',
                'tool': 'functions.view_image', 'status': 'completed',
                'arguments': {'path': 'actual-output/second.png'}}})
        events.append({'type': 'turn.completed', 'usage': {
            'input_tokens': 11, 'cached_input_tokens': 3, 'output_tokens': 7}})
        self.write_events(directory / 'stdout.jsonl', events)
        (directory / 'stderr.log').write_text('')
        session = {**command, 'session_number': number,
            'usage': [events[-1]['usage']], 'event_count': len(events),
            'tool_event_count': 2 if role == 'scorer' else 1, 'command_event_count': 1,
            'execution_identity': {'role': role, 'workspace_name': workspace_name,
                'live_workspace': str(live), 'source_commit': self.commit,
                'frozen_runtime_manifest_sha256': self.metadata['frozen_runtime_manifest_sha256'],
                'schema_sha256': module.sha(directory / 'schema.json'),
                'prompt_sha256': module.sha(directory / 'prompt.txt'),
                'command_sha256': module.sha(directory / 'command.json'),
                'events_sha256': module.sha(directory / 'stdout.jsonl'),
                'thread_id': events[0]['thread_id'], 'attached_image': attached}}
        self.write(directory / 'session.json', session)
        return session

    @staticmethod
    def write_events(path, events):
        path.write_text(''.join(json.dumps(event) + '\n' for event in events))

    def events(self, base=None, role='scorer'):
        return [json.loads(line) for line in ((base or self.base) / role / 'stdout.jsonl').read_text().splitlines()]

    def sync(self, session=None, base=None, role='scorer', recount=False):
        """Bind fresh forged bytes so tests exercise more than digest mismatch."""
        session = self.session if session is None else session
        directory = (base or self.base) / role
        for filename, field in (('schema.json', 'schema_sha256'), ('prompt.txt', 'prompt_sha256'),
                                ('command.json', 'command_sha256'), ('stdout.jsonl', 'events_sha256')):
            session['execution_identity'][field] = module.sha(directory / filename)
        if recount:
            events = self.events(base, role)
            session['usage'] = [e['usage'] for e in events if 'usage' in e]
            session['event_count'] = len(events)
            types = [e.get('item', {}).get('type') for e in events]
            session['tool_event_count'] = sum(t in ('command_execution', 'mcp_tool_call', 'file_change', 'web_search') for t in types)
            session['command_event_count'] = types.count('command_execution')
        self.write(directory / 'session.json', session)

    def change_command(self, edit, sync_session=True):
        path = self.base / 'scorer/command.json'
        command = json.loads(path.read_text())
        edit(command)
        self.write(path, command)
        if sync_session:
            for key, value in command.items():
                self.session[key] = copy.deepcopy(value)
        self.sync()

    def verify_session(self):
        return module.verify_session_evidence(self.base, 'scorer', self.session,
            self.metadata, self.workspace, artifacts=self.artifacts)

    def review_row(self):
        identity = self.session['execution_identity']
        live = Path(identity['live_workspace'])
        observation = observed_review(self.base / 'scorer/stdout.jsonl',
            [self.workspace / 'actual-output' / n for n in self.artifacts if n.endswith('.png')],
            live / identity['attached_image'] if identity['attached_image'] else None,
            workspace=live, retained_workspace=self.workspace)
        return {'id': self.base.name, 'status': 'pass',
                'review_observations': canonical_observations(observation, self.workspace)}

    def verify_review(self, row):
        return module.verify_review_observations(self.base, row, self.artifacts,
            self.workspace, self.session)

    def test_valid_bound_session_and_relative_image_review_are_read_only(self):
        before = {p.relative_to(self.root).as_posix(): module.sha(p)
                  for p in self.root.rglob('*') if p.is_file()}
        thread, attached = self.verify_session()
        self.assertEqual(thread, 'thread-case-000-scoring')
        self.assertEqual(Path(attached), self.workspace / 'actual-output/first.png')
        self.verify_review(self.review_row())
        after = {p.relative_to(self.root).as_posix(): module.sha(p)
                 for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_recomputed_usage_event_and_tool_counts_reject_forged_statistics(self):
        original = copy.deepcopy(self.session)
        for field in ('event_count', 'tool_event_count', 'command_event_count', 'usage'):
            with self.subTest(field=field):
                self.session = copy.deepcopy(original)
                if field == 'usage': self.session[field][0]['output_tokens'] += 1
                else: self.session[field] += 1
                self.write(self.base / 'scorer/session.json', self.session)
                with self.assertRaises(ValueError): self.verify_session()
        self.session = original

    def test_retained_command_disagrees_with_session_even_when_digest_is_refreshed(self):
        self.change_command(lambda command: command.update(exit_code=4), sync_session=False)
        with self.assertRaises(ValueError): self.verify_session()

    def test_nonzero_and_blocked_command_cannot_be_a_completed_session(self):
        for values in ({'exit_code': 4, 'status': 'fail'}, {'exit_code': 0, 'status': 'blocked'}):
            with self.subTest(values=values):
                self.change_command(lambda command: command.update(values))
                with self.assertRaises(ValueError): self.verify_session()

    def test_role_commit_and_frozen_runtime_identity_cannot_be_relabelled(self):
        original = copy.deepcopy(self.session)
        for field, value in (('role', 'actor'), ('source_commit', 'c' * 40),
                             ('frozen_runtime_manifest_sha256', 'c' * 64),
                             ('workspace_name', 'case-000')):
            with self.subTest(field=field):
                self.session = copy.deepcopy(original)
                self.session['execution_identity'][field] = value
                self.sync()
                with self.assertRaises(ValueError): self.verify_session()
        self.session = original

    def test_permission_and_exact_live_C_are_checked_after_rehash(self):
        original = copy.deepcopy(self.session)
        for mode in ('permission', 'workspace'):
            with self.subTest(mode=mode):
                self.session = copy.deepcopy(original)
                self.write(self.base / 'scorer/command.json', {
                    k: copy.deepcopy(self.session[k]) for k in ('argv', 'exit_code', 'seconds', 'status')})
                def edit(command):
                    if mode == 'permission':
                        index = command['argv'].index('default_permissions="enterprise-scorer"')
                        command['argv'][index] = 'default_permissions="enterprise-actor"'
                    else:
                        index = command['argv'].index('-C') + 1
                        command['argv'][index] += '-other'
                self.change_command(edit)
                with self.assertRaises(ValueError): self.verify_session()
        self.session = original

    def test_duplicate_C_and_missing_json_ephemeral_or_schema_flag_are_rejected(self):
        original = copy.deepcopy(self.session)
        for flag in ('-C', '--json', '--ephemeral', '--output-schema'):
            with self.subTest(flag=flag):
                self.session = copy.deepcopy(original)
                self.write(self.base / 'scorer/command.json', {
                    k: copy.deepcopy(self.session[k]) for k in ('argv', 'exit_code', 'seconds', 'status')})
                def edit(command):
                    if flag == '-C': command['argv'][-1:-1] = ['-C', self.session['execution_identity']['live_workspace']]
                    else:
                        index = command['argv'].index(flag)
                        del command['argv'][index:index + (2 if flag == '--output-schema' else 1)]
                self.change_command(edit)
                with self.assertRaises(ValueError): self.verify_session()
        self.session = original

    def test_prompt_schema_events_and_command_bytes_are_bound(self):
        for filename in ('prompt.txt', 'schema.json', 'stdout.jsonl', 'command.json'):
            path = self.base / 'scorer' / filename
            original = path.read_bytes()
            with self.subTest(filename=filename):
                path.write_bytes(original + b' ')
                with self.assertRaises(ValueError): self.verify_session()
            path.write_bytes(original)

    def test_binary_path_and_fingerprint_are_verified(self):
        original = self.binary.read_bytes()
        self.binary.write_bytes(b'changed binary')
        with self.assertRaises(ValueError): self.verify_session()
        self.binary.write_bytes(original)
        self.change_command(lambda command: command['argv'].__setitem__(0, str(self.root / 'other-codex')))
        with self.assertRaises(ValueError): self.verify_session()

    def test_workspace_mapping_cannot_escape_or_alias_another_session(self):
        binding = self.metadata['workspace_bindings']['case-000-scoring']
        original = binding['retained_path']
        for path in ('../outside', 'case-000/workspace', str(self.workspace)):
            with self.subTest(path=path):
                binding['retained_path'] = path
                with self.assertRaises(ValueError): self.verify_session()
        binding['retained_path'] = original
        binding['live_path'] += '-other'
        with self.assertRaises(ValueError): self.verify_session()

    def test_thread_requires_one_started_identity_and_a_completed_turn(self):
        original = self.events()
        for mode in ('no-start', 'duplicate-start', 'no-completion', 'different-identity'):
            with self.subTest(mode=mode):
                events = copy.deepcopy(original)
                if mode == 'no-start': events = [e for e in events if e['type'] != 'thread.started']
                elif mode == 'duplicate-start': events.insert(0, copy.deepcopy(events[0]))
                elif mode == 'no-completion': events = [e for e in events if e['type'] != 'turn.completed']
                else: events[0]['thread_id'] = 'thread-forged-identity'
                self.write_events(self.base / 'scorer/stdout.jsonl', events)
                self.sync(recount=True)
                with self.assertRaises(ValueError): self.verify_session()

    def test_attached_image_matches_exact_retained_artifact_bytes(self):
        path = self.workspace / 'actual-output/first.png'
        path.write_bytes(b'other image')
        with self.assertRaises(ValueError): self.verify_session()

    def test_attached_image_outside_workspace_or_not_an_artifact_is_rejected(self):
        original = copy.deepcopy(self.session)
        for name in ('../case-000/workspace/first.png', 'actual-output/unregistered.png'):
            with self.subTest(name=name):
                self.session = copy.deepcopy(original)
                self.session['execution_identity']['attached_image'] = name
                self.write(self.base / 'scorer/command.json', {
                    k: copy.deepcopy(self.session[k]) for k in ('argv', 'exit_code', 'seconds', 'status')})
                self.change_command(lambda command: command['argv'].__setitem__(
                    command['argv'].index('--image') + 1,
                    str(Path(self.session['execution_identity']['live_workspace']) / name)))
                with self.assertRaises(ValueError): self.verify_session()
        self.session = original

    def test_actor_cannot_attach_a_scorer_artifact(self):
        actor = json.loads((self.base / 'actor/session.json').read_text())
        actor['execution_identity']['attached_image'] = 'actual-output/first.png'
        self.sync(actor, role='actor')
        with self.assertRaises(ValueError):
            module.verify_session_evidence(self.base, 'actor', actor, self.metadata,
                self.base / 'workspace')

    def test_review_relocates_only_exact_live_workspace_and_accepts_string_arguments(self):
        events = self.events()
        live = Path(self.session['execution_identity']['live_workspace'])
        events[3]['item']['arguments'] = json.dumps({'path': str(live / 'actual-output/second.png')})
        self.write_events(self.base / 'scorer/stdout.jsonl', events)
        self.sync(recount=True)
        row = self.review_row()
        self.assertTrue(row['review_observations']['all_images_observed'])
        self.assertEqual(row['review_observations']['viewed_images'],
                         ['actual-output/first.png', 'actual-output/second.png'])
        self.verify_review(row)

    def test_forged_retained_review_flags_and_paths_do_not_substitute_for_events(self):
        original = self.review_row()
        for field, value in (('successful_inspection_commands', ['cat nonexistent.json']),
                             ('viewed_images', ['actual-output/first.png']),
                             ('unviewed_images', ['actual-output/second.png']),
                             ('inspection_observed', False), ('all_images_observed', False)):
            with self.subTest(field=field):
                row = copy.deepcopy(original)
                row['review_observations'][field] = value
                with self.assertRaises(ValueError): self.verify_review(row)

    def test_failed_or_missing_image_event_cannot_be_forged_as_viewed(self):
        original_events = self.events()
        claimed = self.review_row()
        for mode in ('failed', 'missing', 'other-session', 'prefix-neighbour'):
            with self.subTest(mode=mode):
                events = copy.deepcopy(original_events)
                if mode == 'failed': events[3]['item']['status'] = 'failed'
                elif mode == 'missing': del events[3]
                elif mode == 'other-session': events[3]['item']['arguments']['path'] = str(
                    self.root / 'removed-live-home/workspaces/another/actual-output/second.png')
                else: events[3]['item']['arguments']['path'] = (
                    self.session['execution_identity']['live_workspace'] + '-neighbour/actual-output/second.png')
                self.write_events(self.base / 'scorer/stdout.jsonl', events)
                self.sync(recount=True)
                with self.assertRaises(ValueError): self.verify_review(claimed)

    def test_correctly_recorded_unviewed_image_still_cannot_pass(self):
        events = self.events()
        del events[3]
        self.write_events(self.base / 'scorer/stdout.jsonl', events)
        self.sync(recount=True)
        row = self.review_row()
        self.assertFalse(row['review_observations']['all_images_observed'])
        with self.assertRaises(ValueError): self.verify_review(row)

    def test_failed_command_is_not_inspection_even_when_retained_claims_say_pass(self):
        claimed = self.review_row()
        events = self.events()
        events[2]['item']['exit_code'] = 1
        self.write_events(self.base / 'scorer/stdout.jsonl', events)
        self.sync(recount=True)
        with self.assertRaises(ValueError): self.verify_review(claimed)
        row = self.review_row()
        self.assertFalse(row['review_observations']['inspection_observed'])
        with self.assertRaises(ValueError): self.verify_review(row)

    def test_scorer_copy_of_nonattached_image_also_matches_actor_artifact(self):
        (self.workspace / 'actual-output/second.png').write_bytes(b'changed second image')
        with self.assertRaises(ValueError): self.verify_review(self.review_row())


if __name__ == '__main__':
    unittest.main()
