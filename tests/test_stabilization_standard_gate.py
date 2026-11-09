"""Independent coverage/publication attacks with an actually executed tiny oracle.

The synthetic sources exercise gate integrity, not UML/BPMN completeness.
"""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('stabilization_standard_gate_test_target',
    REPO / 'togaf-standard-10th-ai/maintenance/stabilization_standard_evidence.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class StabilizationStandardGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.fixture = Path(cls.temp.name).resolve() / 'fixture'
        cls.fixture.mkdir()
        shared = cls.fixture / 'togaf-standard-10th-ai/skills/_shared'
        scripts = shared / 'scripts'
        scripts.mkdir(parents=True)
        for name in ('standards_coverage.py', 'standards.py'):
            shutil.copyfile(REPO / 'togaf-standard-10th-ai/skills/_shared/scripts' / name, scripts / name)
        (scripts / 'implementation.py').write_text('def check(value):\n    return bool(value)\n')
        tests = cls.fixture / 'tests'
        tests.mkdir()
        (tests / 'test_oracle.py').write_text(
            'import unittest\nfrom xml.etree import ElementTree as ET\n'
            'class NativeOracle(unittest.TestCase):\n'
            '    def test_positive(self):\n'
            '        self.assertEqual(ET.fromstring("<Class/>").tag, "Class")\n'
            '    def test_negative(self):\n'
            '        with self.assertRaises(ET.ParseError): ET.fromstring("<Class>")\n')
        sources = shared / 'standards/sources'
        sources.mkdir(parents=True)
        manifest = []
        bindings = []
        for language, version, main in (('uml', '2.5.1', 'UML.xmi'), ('bpmn', '2.0.2', 'BPMN20.cmof')):
            relative = language + '-' + version
            (sources / relative).mkdir()
            source = sources / relative / main
            source.write_text('<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001" '
                'xmlns:uml="http://www.omg.org/spec/UML/20131001"><uml:Model xmi:id="model">'
                '<packagedElement xmi:type="uml:Class" xmi:id="Class" name="Class">'
                '<ownedAttribute xmi:id="Class-peer" type="Class" name="peer"/>'
                '</packagedElement></uml:Model></xmi:XMI>')
            publication = sources / relative / 'body.pdf'
            publication.write_bytes(b'Synthetic publication marker for gate fixtures; not normative.\n')
            for path, source_class in ((source, 'official-machine-readable'),
                                       (publication, 'official-normative-publication')):
                manifest.append({'language': relative, 'file': path.relative_to(sources).as_posix(),
                    'sha256': module._sha(path), 'source_class': source_class})
            bindings.append({'obligation_id': ':'.join((language, version, 'construct', main, 'Class')),
                'implementation': [{'file': 'togaf-standard-10th-ai/skills/_shared/scripts/implementation.py', 'symbol': 'check'}],
                'positive_tests': [{'file': 'tests/test_oracle.py', 'symbol': 'NativeOracle.test_positive'}],
                'negative_tests': [{'file': 'tests/test_oracle.py', 'symbol': 'NativeOracle.test_negative'}],
                'basis': 'synthetic gate fixture', 'limitations': ['bounded synthetic oracles']})
        cls.write(sources / 'manifest.json', manifest)
        cls.write(shared / 'standards/coverage-bindings.json', bindings)
        cls.write(shared / 'standards/java/manifest.json', {'synthetic': True})
        evidence_dir = cls.fixture / 'evidence'
        evidence_dir.mkdir()
        done = subprocess.run([sys.executable, '-B', '-m', 'unittest', '-v', 'test_oracle'],
            cwd=tests, text=True, capture_output=True, check=True)
        (evidence_dir / 'execution.log').write_text(done.stderr)
        cls.evidence = {'schema_version': 'native-standard-test-evidence/1', 'modules': ['test_oracle'],
            'discovered': 2, 'executed': 2, 'failures': 0, 'errors': 0, 'skipped': 0,
            'tests': [{'file': 'tests/test_oracle.py', 'symbol': 'NativeOracle.' + name,
                       'id': 'test_oracle.NativeOracle.' + name, 'status': 'passed'}
                      for name in ('test_negative', 'test_positive')],
            'source_hashes': module._source_snapshot(cls.fixture),
            'normative_source_hashes': module._normative_snapshot(cls.fixture),
            'source_changed_during_execution': [], 'passed': True,
            'full_design_time_conformance': False, 'human_acceptance': 'pending',
            'organization_approval': 'pending-signature'}
        cls.write(evidence_dir / 'test-evidence.json', cls.evidence)
        for language in ('uml', 'bpmn'):
            cls.write(evidence_dir / (language + '-coverage.json'),
                      module._current_ledger(cls.fixture, language, cls.evidence))

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.case_temp = tempfile.TemporaryDirectory()
        self.root = Path(self.case_temp.name).resolve() / 'repo'
        shutil.copytree(self.fixture, self.root)
        self.round = {'round_id': 'current', 'source_commit': 'a' * 40,
            'standard_capabilities': {language: self.ref('evidence/' + language + '-coverage.json')
                                      for language in ('uml', 'bpmn')},
            'standard_test_evidence': self.ref('evidence/test-evidence.json'),
            'standard_test_log': self.ref('evidence/execution.log')}

    def tearDown(self):
        self.case_temp.cleanup()

    @staticmethod
    def write(path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + '\n')

    def ref(self, name):
        return {'path': name, 'sha256': module._sha(self.root / name)}

    def change_evidence(self, edit):
        path = self.root / 'evidence/test-evidence.json'
        data = json.loads(path.read_text())
        edit(data)
        self.write(path, data)
        self.round['standard_test_evidence'] = self.ref('evidence/test-evidence.json')

    def change_ledger(self, edit, language='uml'):
        path = self.root / 'evidence' / (language + '-coverage.json')
        data = json.loads(path.read_text())
        edit(data)
        self.write(path, data)
        self.round['standard_capabilities'][language] = self.ref('evidence/' + language + '-coverage.json')

    def result(self):
        return module.standard_checks(self.round, self.root)

    def assert_invalid(self, language=None):
        complete, checks = self.result()
        self.assertFalse(complete)
        self.assertEqual(checks[language or 'test_evidence']['status'], 'invalid', checks)

    def test_actual_bounded_execution_validates_full_inventory_but_stays_incomplete(self):
        before = {p.relative_to(self.root).as_posix(): module._sha(p)
                  for p in self.root.rglob('*') if p.is_file()}
        complete, checks = self.result()
        self.assertFalse(complete)
        self.assertEqual(checks['test_evidence']['executed'], 2)
        for language in ('uml', 'bpmn'):
            self.assertTrue(checks[language]['ledger_verified'])
            self.assertEqual(checks[language]['status'], 'incomplete')
            self.assertEqual(checks[language]['item_count'], 2)
            self.assertEqual(checks[language]['verified_obligations'], 0)
        after = {p.relative_to(self.root).as_posix(): module._sha(p)
                 for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_fake_one_item_all_pass_ledger_cannot_close_full_source_inventory(self):
        def forge(data):
            data['items'] = data['items'][:1]
            data['item_count'] = 1
            data['items'][0].update(implementation_status='implemented', verification_status='passed')
            data['completeness'].update(status='complete', source_scope_complete=True,
                applicability_adjudication_complete=True, applicable_obligations=1, verified_obligations=1)
        self.change_ledger(forge)
        self.assert_invalid('uml')

    def test_rehashed_source_locator_declaration_applicability_and_binding_forgery(self):
        original = (self.root / 'evidence/uml-coverage.json').read_bytes()
        for field in ('id', 'source', 'declaration', 'applicability', 'implementation_status', 'verification_status', 'implementation'):
            with self.subTest(field=field):
                (self.root / 'evidence/uml-coverage.json').write_bytes(original)
                def edit(data):
                    item = data['items'][0]
                    if field == 'source': item['source']['locator'] = 'xmi:id=forged'
                    elif field == 'declaration': item['declaration']['body'] = 'forged requirement'
                    elif field == 'implementation': item['implementation'] = []
                    else: item[field] = 'forged'
                self.change_ledger(edit)
                self.assert_invalid('uml')

    def test_duplicate_or_missing_stable_id_and_source_hash_are_invalid(self):
        original = (self.root / 'evidence/uml-coverage.json').read_bytes()
        for mode in ('duplicate', 'missing', 'source-hash'):
            with self.subTest(mode=mode):
                (self.root / 'evidence/uml-coverage.json').write_bytes(original)
                def edit(data):
                    if mode == 'duplicate': data['items'].append(copy.deepcopy(data['items'][0]))
                    elif mode == 'missing': del data['items'][0]
                    else: data['items'][0]['source']['sha256'] = '0' * 64
                self.change_ledger(edit)
                self.assert_invalid('uml')

    def test_current_binding_change_invalidates_old_execution_snapshot(self):
        path = self.root / 'togaf-standard-10th-ai/skills/_shared/standards/coverage-bindings.json'
        bindings = json.loads(path.read_text())
        bindings[0]['limitations'] = ['changed coverage boundary']
        self.write(path, bindings)
        self.assert_invalid()

    def test_normative_and_implementation_bytes_cannot_change_after_execution(self):
        for name in ('togaf-standard-10th-ai/skills/_shared/scripts/implementation.py',
                     'togaf-standard-10th-ai/skills/_shared/standards/sources/uml-2.5.1/UML.xmi'):
            path = self.root / name
            original = path.read_bytes()
            with self.subTest(path=name):
                path.write_bytes(original + b' ')
                self.assert_invalid()
            path.write_bytes(original)

    def test_rehashed_missing_or_extra_source_hash_is_rejected(self):
        for mode in ('missing', 'extra', 'normative'):
            with self.subTest(mode=mode):
                self.write(self.root / 'evidence/test-evidence.json', self.evidence)
                def edit(data):
                    if mode == 'missing': data['source_hashes'].pop('tests/test_oracle.py')
                    elif mode == 'extra': data['source_hashes']['tests/unexecuted.py'] = '0' * 64
                    else: data['normative_source_hashes'].pop('uml-2.5.1/UML.xmi')
                self.change_evidence(edit)
                self.assert_invalid()

    def test_duplicate_failed_skipped_unexecuted_or_missing_symbol_tests_are_rejected(self):
        for mode in ('duplicate', 'failed', 'skipped', 'missing-symbol', 'id-mismatch'):
            with self.subTest(mode=mode):
                self.write(self.root / 'evidence/test-evidence.json', self.evidence)
                def edit(data):
                    if mode == 'duplicate': data['tests'][1] = copy.deepcopy(data['tests'][0])
                    elif mode in ('failed', 'skipped'): data['tests'][0]['status'] = mode
                    elif mode == 'missing-symbol': data['tests'][0]['symbol'] = 'NativeOracle.test_absent'
                    else: data['tests'][0]['id'] = 'other.NativeOracle.test_negative'
                self.change_evidence(edit)
                self.assert_invalid()

    def test_nonzero_failure_error_skip_or_execution_source_change_is_rejected(self):
        for field, value in (('failures', 1), ('errors', 1), ('skipped', 1), ('executed', 0),
                             ('discovered', 3), ('passed', False),
                             ('source_changed_during_execution', ['tests/test_oracle.py'])):
            with self.subTest(field=field):
                self.write(self.root / 'evidence/test-evidence.json', self.evidence)
                self.change_evidence(lambda data: data.__setitem__(field, value))
                self.assert_invalid()

    def test_explicit_test_evidence_and_log_references_are_required(self):
        for field in ('standard_test_evidence', 'standard_test_log'):
            with self.subTest(field=field):
                saved = self.round.pop(field)
                self.assert_invalid()
                self.round[field] = saved

    def test_rehashed_log_without_exact_test_lines_or_success_summary_is_rejected(self):
        path = self.root / 'evidence/execution.log'
        original = path.read_text()
        for text in ('Ran 2 tests in 0.001s\n\nOK\n', original.replace(' ... ok', ' ... FAIL', 1),
                     original.replace('Ran 2 tests', 'Ran 3 tests'), original + '\nOK\n',
                     original.replace('\nOK\n', '\nOK (skipped=1)\n')):
            with self.subTest(text=text):
                path.write_text(text)
                self.round['standard_test_log'] = self.ref('evidence/execution.log')
                self.assert_invalid()

    def test_fingerprint_conflict_path_escape_and_symlink_reference_are_rejected(self):
        original = copy.deepcopy(self.round['standard_test_evidence'])
        for name, digest in (('../outside.json', original['sha256']),
                             ('evidence/test-evidence.json', '0' * 64)):
            with self.subTest(name=name):
                self.round['standard_test_evidence'] = {'path': name, 'sha256': digest}
                self.assert_invalid()
        (self.root / 'evidence/linked.json').symlink_to(self.root / original['path'])
        self.round['standard_test_evidence'] = {'path': 'evidence/linked.json', 'sha256': original['sha256']}
        self.assert_invalid()


if __name__ == '__main__':
    unittest.main()
