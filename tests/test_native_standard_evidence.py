"""Evidence collectors must retain fixture failures, including class setup errors."""
import io
import unittest
from run_native_standard_evidence import RecordedResult


class NativeStandardEvidenceTests(unittest.TestCase):
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
