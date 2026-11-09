"""A refreshed report hash must not hide changed inputs or an empty ledger."""
import importlib.util
import json
from pathlib import Path
import tempfile
import sys
import unittest
import contextlib
import io
import subprocess
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/maintenance/verify_implementation_ledger.py'
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location('ledger_verification', SCRIPT)
ledger_verification = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ledger_verification)
STATUS_SPEC = importlib.util.spec_from_file_location('ledger_status', SCRIPT.parent / 'update_status.py')
ledger_status = importlib.util.module_from_spec(STATUS_SPEC)
STATUS_SPEC.loader.exec_module(ledger_status)
import update_implementation_ledger as ledger_generator
from report_outcome import engineering_complete, report_outcome, ledger_state


class LedgerFreshnessTest(unittest.TestCase):
    def test_current_report_hash_does_not_hide_stale_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source.txt'
            source.write_text('reviewed version')
            report = root / 'report.json'
            report.write_text(json.dumps({'passed': True, 'source_files': {'source.txt': ledger_verification.sha(source)}}))
            ledger = {'items': [{'id': 'EXAMPLE', 'evidence': [{'path': 'report.json', 'sha256': ledger_verification.sha(report)}]}]}
            self.assertTrue(ledger_verification.verify(root, ledger)['passed'])
            source.write_text('unreviewed change')
            result = ledger_verification.verify(root, ledger)
            self.assertFalse(result['passed'])
            self.assertTrue(result['evidence'][0]['fingerprint_current'])
            self.assertEqual('stale-declared-input', result['issues'][0]['code'])

    def test_changed_and_missing_report_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / 'report.json'
            report.write_text('{"passed": true}')
            ledger = {'items': [{'id': 'EXAMPLE', 'evidence': [{'path': 'report.json', 'sha256': ledger_verification.sha(report)}]}]}
            current = ledger_verification.verify(root, ledger)
            self.assertEqual('not-recorded', current['evidence'][0]['input_freshness'])
            report.write_text('{"passed": false}')
            self.assertEqual('stale-evidence', ledger_verification.verify(root, ledger)['issues'][0]['code'])
            report.unlink()
            self.assertEqual('missing-evidence', ledger_verification.verify(root, ledger)['issues'][0]['code'])

    def test_zero_evidence_cannot_pass(self):
        self.assertFalse(ledger_verification.verify(Path('.'), {'items': []})['passed'])
        self.assertFalse(ledger_verification.verify(Path('.'), {'items': [{'id': 'EMPTY', 'evidence': []}]})['passed'])

    def test_refreshing_failed_report_hash_cannot_support_done(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / 'report.json'
            report.write_text('{"passed": false}')
            ledger = {'items': [{'id': 'EXAMPLE', 'state': 'done', 'evidence': [{'path': 'report.json', 'sha256': ledger_verification.sha(report)}]}]}
            result = ledger_verification.verify(root, ledger)
            self.assertFalse(result['passed'])
            self.assertTrue(result['evidence'][0]['fingerprint_current'])
            self.assertEqual('failed-evidence-for-complete-item', result['issues'][0]['code'])

    def test_status_does_not_claim_undeclared_inputs_are_current(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'report.json').write_text('{"passed": true}')
            with patch.object(ledger_status, 'C', root):
                result = ledger_status.evidence('report.json')
            self.assertIsNone(result['inputs_current'])
            self.assertEqual('not-recorded', result['input_freshness'])

    def test_status_checks_all_supported_input_maps(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source.txt'
            for field in ('input_sha256', 'inputs', 'source_files'):
                with self.subTest(field=field), patch.object(ledger_status, 'C', root):
                    source.write_text('reviewed')
                    (root / 'report.json').write_text(json.dumps({'passed': True, field: {'source.txt': ledger_verification.sha(source)}}))
                    self.assertTrue(ledger_status.evidence('report.json')['inputs_current'])
                    source.write_text('changed')
                    result = ledger_status.evidence('report.json')
                    self.assertFalse(result['inputs_current'])
                    self.assertEqual(['source.txt'], result['stale_inputs'])

    def test_failure_formats_block_generator_verifier_and_status(self):
        reports = [
            {'passed': False}, {'schema_version': 'semantic-regression/1', 'result': 'failed'},
            {'counts': {'failed': 1}}, {'status': 'fail'}, {'status': 'failed'},
            {'counts': {'errors': 1}},
            {'schema_version': 'skill-package-verification/1', 'all_applicable_pass': False},
            {'successful': False},
            {'passed': True, 'result': 'failed'},
            {'status': 'pass', 'counts': {'checks': 2, 'passed': 1, 'failed': 1}},
            # Real producer formats, including conflicting aggregate success.
            {'schema_version': 'method-verification/3', 'calculator_cases': 1,
             'registered_calculators_exercised': 0, 'failed': 1},
            {'schema_version': 'method-verification/3', 'passed': True, 'failed': 1},
            {'schema_version': '2.0', 'errors': 1},
            {'schema_version': '2.0', 'passed': True, 'errors': 1},
            {'schema_version': 'togaf-corpus-validation/1', 'error_count': 1},
            {'schema_version': 'togaf-corpus-validation/1', 'passed': True, 'error_count': 1},
            {'status': 'pass', 'failures': 1},
            {'passed': True, 'errors': [{'code': 'undefined-entity-type'}]},
            {'passed': True, 'failures': ['failed-case']},
            {'passed': True, 'failed': ['failed-check']},
            {'schema_version': 'semantic-regression/1', 'result': None},
            {'result': None, 'passed': True},
            {'status': None}, {'status': None, 'passed': True},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'quality').mkdir()
            (root / 'supplementary').mkdir()
            (root / 'supplementary/G226.json').write_text('{"sections": []}')
            report = root / 'report.json'
            for payload in reports:
                for declaration in ('done', 'conditional'):
                    with self.subTest(payload=payload, declaration=declaration):
                        report.write_text(json.dumps(payload))
                        forged = {'engineering_implementation_complete': True, 'items': [{'id': 'EXAMPLE', 'state': 'done', 'evidence': [{'path': 'report.json', 'sha256': ledger_verification.sha(report)}]}]}
                        result = ledger_verification.verify(root, forged)
                        self.assertFalse(result['passed'])
                        self.assertIn('inconsistent-engineering-completion', [i['code'] for i in result['issues']])
                        self.assertTrue(result['evidence'][0]['fingerprint_current'])
                        with patch.object(ledger_status, 'C', root):
                            self.assertFalse(ledger_status.evidence('report.json')['passed'])
                        rows = [('EXAMPLE', 'Example', declaration, ['report.json'], 'Validation only')]
                        with patch.object(ledger_generator, 'C', root), patch.object(ledger_generator, 'ROWS', rows), contextlib.redirect_stdout(io.StringIO()):
                            ledger_generator.main()
                        generated = json.loads((root / 'quality/implementation-ledger.json').read_text())
                        self.assertEqual('pending', generated['items'][0]['state'])
                        self.assertFalse(generated['engineering_implementation_complete'])

    def test_success_formats_require_affirmative_evidence(self):
        for payload in ({'passed': True}, {'all_applicable_pass': True, 'acceptance_granted': False}, {'successful': True}, {'result': 'passed'}, {'status': 'pass'},
                        {'status': 'passed-with-explicit-limits', 'counts': {'failed': 0}}):
            with self.subTest(payload=payload):
                outcome = report_outcome(payload)
                self.assertEqual('passed', outcome['state'])
                self.assertEqual('done', ledger_state('conditional', [outcome]))
        for payload in ({}, {'counts': {'failed': 0}}, {'result': {'domain_result': 'valid'}}):
            with self.subTest(payload=payload):
                self.assertIsNone(report_outcome(payload)['passed'])
                self.assertEqual('pending', ledger_state('conditional', [report_outcome(payload)]))
        # Source documents with no execution result remain legitimate static evidence.
        self.assertEqual('done', ledger_state('done', [report_outcome({'schema_version': 'source-index/1'})]))
        self.assertEqual('pending', ledger_state('pending', [report_outcome({'passed': True})]))

    def test_incomplete_and_malformed_results_cannot_be_completed(self):
        for payload in ({'status': 'blocked'}, {'result': 'not-executed'},
                        {'passed': True, 'counts': {'skipped': 1}},
                        {'passed': 'false'}, {'passed': 1}, {'status': 'unknown-success'},
                        {'passed': True, 'counts': {'failed': '1'}},
                        {'passed': True, 'counts': {'failed': -1}},
                        {'passed': True, 'counts': {'failed': True}}):
            with self.subTest(payload=payload):
                self.assertFalse(report_outcome(payload)['passed'])
                self.assertEqual('pending', ledger_state('done', [report_outcome(payload)]))

    def test_top_level_failure_counts_reject_malformed_values(self):
        for field in ('failed', 'failures', 'errors', 'error_count'):
            for value in (None, True, -1, '1', 1.5, {}):
                with self.subTest(field=field, value=value):
                    outcome = report_outcome({'passed': True, field: value})
                    self.assertEqual('invalid', outcome['state'])
                    self.assertEqual('pending', ledger_state('done', [outcome]))

    def test_zero_failures_do_not_prove_execution_and_nested_domain_results_are_opaque(self):
        for payload in ({'failed': 0}, {'errors': 0}, {'error_count': 0},
                        {'failures': 0}, {'errors': []}, {'failures': []}, {'failed': []}):
            with self.subTest(payload=payload):
                self.assertIsNone(report_outcome(payload)['passed'])
                self.assertEqual('pending', ledger_state('conditional', [report_outcome(payload)]))
                self.assertTrue(report_outcome(dict(payload, passed=True))['passed'])
        payload = {'passed': True, 'result': {'failed': 1, 'errors': ['business-domain-record']},
                   'checks': [{'expected': {'status': 'failed', 'error_count': 1}}]}
        self.assertTrue(report_outcome(payload)['passed'])
        # Missing outcome fields still preserve legitimate static source evidence.
        static = report_outcome({'schema_version': 'source-index/1', 'documents': []})
        self.assertEqual('done', ledger_state('done', [static]))

    def test_readonly_cli_rejects_failed_report_with_fresh_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'quality').mkdir()
            (root / 'report.json').write_text('{"result": "failed", "counts": {"failed": 1}}')
            ledger = {'items': [{'id': 'EXAMPLE', 'state': 'done', 'evidence': [{'path': 'report.json', 'sha256': ledger_verification.sha(root / 'report.json')}]}]}
            ledger_path = root / 'quality/implementation-ledger.json'
            ledger_path.write_text(json.dumps(ledger))
            before = ledger_path.read_bytes()
            command = 'import sys;from pathlib import Path;sys.path.insert(0,sys.argv[1]);import verify_implementation_ledger as v;v.C=Path(sys.argv[2]);sys.argv=["verify"];raise SystemExit(v.main())'
            result = subprocess.run([sys.executable, '-B', '-c', command, str(SCRIPT.parent), str(root)], capture_output=True, text=True)
            self.assertEqual(1, result.returncode, result.stderr)
            self.assertIn('failed-evidence-for-complete-item', result.stdout)
            self.assertEqual(before, ledger_path.read_bytes())

    def test_stored_completion_cannot_override_pending_or_empty_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / 'report.json'
            report.write_text('{"status": "fail"}')
            ledger = {'engineering_implementation_complete': True, 'items': [{'id': 'EXAMPLE', 'state': 'pending', 'evidence': [{'path': 'report.json', 'sha256': ledger_verification.sha(report)}]}]}
            result = ledger_verification.verify(root, ledger)
            self.assertFalse(result['passed'])
            self.assertIn('inconsistent-engineering-completion', [i['code'] for i in result['issues']])
            self.assertFalse(engineering_complete(ledger['items'], result['passed']))
            ledger['engineering_implementation_complete'] = False
            self.assertTrue(ledger_verification.verify(root, ledger)['passed'])
            self.assertFalse(engineering_complete([]))
            self.assertFalse(engineering_complete([{'id': 'INDEPENDENT-SEMANTIC', 'state': 'pending'}]))
            self.assertTrue(engineering_complete([{'id': 'EXAMPLE', 'state': 'done'}, {'id': 'INDEPENDENT-SEMANTIC', 'state': 'pending'}]))


if __name__ == '__main__':
    unittest.main()
