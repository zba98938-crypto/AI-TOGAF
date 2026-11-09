"""Public explicit-layout selection preserves native XML and separates hashes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
CLI=REPO/'togaf-standard-10th-ai/skills/_shared/scripts/standards.py'
SOURCE=b'''<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" targetNamespace="urn:layout-cli">
 <process id="P"><startEvent id="S"/><task id="T"/><endEvent id="E"/>
 <sequenceFlow id="F1" sourceRef="S" targetRef="T"/>
 <sequenceFlow id="F2" sourceRef="T" targetRef="E"/></process></definitions>'''


class NativeStandardCLITests(unittest.TestCase):
    def test_bpmn_layout_requires_explicit_selection_and_preserves_source(self):
        with tempfile.TemporaryDirectory(prefix='native-layout-cli-') as tmp:
            tmp=Path(tmp);source=tmp/'native.bpmn';source.write_bytes(SOURCE)
            argv=[sys.executable,'-B',str(CLI),'render','--language','bpmn','--version','2.0.2',
                  '--input',str(source),'--out',str(tmp/'view.svg')]
            blocked=subprocess.run(argv,capture_output=True,text=True,timeout=30)
            self.assertEqual(3,blocked.returncode,blocked.stdout+blocked.stderr)
            self.assertFalse((tmp/'view.svg').exists())
            result=subprocess.run(argv+['--auto-layout'],capture_output=True,text=True,timeout=120)
            self.assertEqual(0,result.returncode,result.stdout+result.stderr)
            report=json.loads(result.stdout)
            self.assertTrue(report['auto_layout'])
            self.assertEqual(hashlib.sha256(SOURCE).hexdigest(),report['source_sha256'])
            self.assertNotEqual(report['source_sha256'],report['rendered_model_sha256'])
            self.assertEqual(SOURCE,source.read_bytes())
            self.assertTrue((tmp/'view.layout.bpmn').is_file())
            self.assertEqual(b'\x89PNG\r\n\x1a\n',(tmp/'view.png').read_bytes()[:8])
            self.assertEqual('incomplete',report['conformance_status'])

    def test_auto_layout_option_rejects_other_commands_and_languages(self):
        result=subprocess.run([sys.executable,'-B',str(CLI),'catalog','--language','uml',
                               '--version','2.5.1','--auto-layout'],capture_output=True,text=True,timeout=10)
        self.assertEqual(1,result.returncode)
        self.assertIn('--auto-layout requires BPMN render',json.loads(result.stdout)['reason'])


if __name__=='__main__':unittest.main()
