"""Evidence collectors must retain fixture failures, including class setup errors."""
import io
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import run_native_standard_evidence as collector
from run_native_standard_evidence import RecordedResult


class NativeStandardEvidenceTests(unittest.TestCase):
    def test_collector_and_gate_bind_java_workbench_and_nested_test_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shared = root/'togaf-standard-10th-ai/skills/_shared'
            names = ('tests/test_oracle.py', 'tests/java/Probe.java', 'tests/enterprise/runtime.py',
                     'tests/annotation_fixtures/input.svg', 'workbench/native.py',
                     'workbench/web/app.js', 'workbench/web/index.html',
                     'togaf-standard-10th-ai/skills/_shared/standards/java/backend.jar')
            for name in names:
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(('dependency '+name).encode())
            spec = importlib.util.spec_from_file_location('native_evidence_dependency_gate',
                Path(__file__).resolve().parents[1]/'togaf-standard-10th-ai/maintenance/stabilization_standard_evidence.py')
            gate = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(gate)
            with patch.object(collector, 'REPO', root), patch.object(collector, 'ROOT', shared):
                before = collector.source_snapshot()
                self.assertEqual(set(names), set(before))
                self.assertEqual(before, gate._source_snapshot(root))
                (root/'tests/java/Probe.java').write_bytes(b'changed compiled oracle source')
                self.assertNotEqual(before, collector.source_snapshot())
                self.assertEqual(collector.source_snapshot(), gate._source_snapshot(root))

    def test_class_setup_error_is_retained_without_collector_crash(self):
        class SetupFailure(unittest.TestCase):
            @classmethod
            def setUpClass(cls): raise RuntimeError('fixture setup is unavailable')
            def test_probe(self): pass
        result=unittest.TextTestRunner(stream=io.StringIO(),resultclass=RecordedResult).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(SetupFailure))
        self.assertEqual(1,len(result.errors))
        self.assertEqual(['error'],[row['status'] for row in result.rows.values()])
        self.assertIn('fixture setup is unavailable',next(iter(result.rows.values()))['detail'])

    def test_subtest_failure_and_expected_failure_are_not_labeled_passed(self):
        class SubFailure(unittest.TestCase):
            def test_probe(self):
                with self.subTest(case='invalid'): self.assertEqual(1,2)
        class ExpectedFailure(unittest.TestCase):
            @unittest.expectedFailure
            def test_probe(self): self.assertEqual(1,2)
        suite=unittest.TestSuite([SubFailure('test_probe'),ExpectedFailure('test_probe')])
        result=unittest.TextTestRunner(stream=io.StringIO(),resultclass=RecordedResult).run(suite)
        self.assertEqual({'failed','expected-failure'},{row['status'] for row in result.rows.values()})
        self.assertEqual(2,len(result.rows))


if __name__=='__main__':unittest.main()
