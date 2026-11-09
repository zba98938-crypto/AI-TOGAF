"""A successful unittest exit with skipped work must not support acceptance."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class FormalUnitGateTests(unittest.TestCase):
    def test_skipped_failed_empty_and_executed_suites_have_distinct_results(self):
        body='import unittest\nclass Example(unittest.TestCase):\n DECORATOR\n def test_work(self): BODY\n'
        for name,decorator,statement,expected in (
            ('pass','', 'self.assertTrue(True)',0),
            ('skip','@unittest.skip("required prerequisite absent")','self.fail()',1),
            ('fail','','self.fail("actual failure")',1),
            ('empty','','',3)):
            with self.subTest(name=name),tempfile.TemporaryDirectory() as tmp:
                if name!='empty':
                    (Path(tmp)/'test_gate_fixture.py').write_text(body.replace('DECORATOR',decorator).replace('BODY',statement))
                done=subprocess.run([sys.executable,'-B',str(Path(__file__).with_name('run_unit_regressions.py')),tmp],
                                    capture_output=True,text=True,timeout=10)
                report=json.loads(done.stdout.splitlines()[-1])
                self.assertEqual(done.returncode,expected,done.stderr)
                self.assertEqual(report['passed'],name=='pass')
                if name=='skip':self.assertEqual(report['skipped'],1)
