"""Actual fixed data-DI dispatch and independent native transport attacks."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch
from enterprise.local_render import LocalRenderController

ROOT=Path(__file__).resolve().parents[1]
SHARED=ROOT/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(SHARED/'scripts'))
from standards import safe_xml
from bpmn_render import diagram_plan
from bpmn_data_di_fixtures import data_di_model,boundary_di_model
from bpmn_data_compensation_fixtures import by_id,change,element


def browser_path():
    if os.environ.get('TOGAF_BROWSER_PATH'):
        return Path(os.environ['TOGAF_BROWSER_PATH']).resolve()
    result=subprocess.run([shutil.which('node') or 'node','--input-type=module','-e',
        "import {resolveBrowser} from './scripts/browser_resolver.mjs';process.stdout.write(JSON.stringify(resolveBrowser()));"],
        cwd=SHARED,capture_output=True,text=True,check=True,timeout=15)
    return Path(json.loads(result.stdout)['executablePath'])


def dispatch(root,task,identity,timeout=120):
    request=root/'.render/inbox'/(identity+'.json')
    with request.open('x') as stream:json.dump(task,stream)
    response=root/'.render/outbox'/(identity+'.json');deadline=time.monotonic()+timeout
    while time.monotonic()<deadline:
        if response.is_file():return json.loads(response.read_text())
        time.sleep(.05)
    raise TimeoutError('controlled BPMN data test response missing')


class ControlledBPMNDataTests(unittest.TestCase):
    def test_actual_data_and_partial_owner_views_preserve_source_geometry_and_cleanup(self):
        with tempfile.TemporaryDirectory(prefix='controlled-data-test-') as tmp:
            directory=Path(tmp);root=directory/'session';root.mkdir()
            controller=LocalRenderController(SHARED,browser_path(),directory/'evidence')
            controller.register(root)
            try:
                for index,data in enumerate([data_di_model(),boundary_di_model()]):
                    with self.subTest(index=index):
                        source=root/('data-'+str(index)+'.bpmn');source.write_bytes(data)
                        plan=diagram_plan(data)
                        # Loader/environment injection must not reach the fixed worker.
                        with patch.dict(os.environ,{'NODE_OPTIONS':'--require /synthetic/forbidden-loader.js',
                                                    'TOGAF_RENDER_SECRET':'synthetic-secret'}):
                            row=dispatch(root,{'kind':'bpmn','source':source.name},'%032x'%index)
                        self.assertEqual('pass',row['status'],row)
                        self.assertEqual(data,source.read_bytes())
                        report=row['renderer_report'];scene=report['bpmn_data_di']
                        self.assertEqual('controlled-local-process',report['mode'])
                        self.assertEqual('native-data-di',scene['backend'])
                        self.assertEqual(hashlib.sha256(data).hexdigest(),scene['source_sha256'])
                        self.assertEqual([],report['external_requests']);self.assertTrue(report['source_authoritative'])
                        self.assertFalse(report['derived_layout']);self.assertFalse(scene['auto_layout'])
                        self.assertEqual([],report['text_geometry']['outside']);self.assertTrue(report['text_geometry']['font_loaded'])
                        self.assertTrue(scene['source_plane_order_preserved'])
                        self.assertEqual([g['graphic_id'] for g in plan['graphics']],report['native_registry'])
                        for actual,expected in zip(report['native_geometry'],plan['graphics']):
                            self.assertEqual(expected.get('bounds'),actual.get('bounds'))
                            self.assertEqual(expected.get('waypoints'),actual.get('waypoints'))
                        self.assertEqual(plan['data_depiction_inventory'],scene['data_depiction_inventory'])
                        self.assertTrue(row['cleaned']);self.assertEqual([],row['owned_processes_remaining'])
                        self.assertIn('no inherited',row['environment_policy'])
                        svg=safe_xml((root/row['outputs']['svg']['path']).read_bytes())
                        groups=svg.xpath('//*[@data-native-root]/*[@data-di-id]')
                        self.assertEqual(report['native_registry'],[g.get('data-di-id') for g in groups])
                        self.assertIn('待审',''.join(svg.itertext()))
                        for key in ['png','browser_png']:
                            self.assertEqual(b'\x89PNG\r\n\x1a\n',(root/row['outputs'][key]['path']).read_bytes()[:8])
            finally:cleanup=controller.close()
            self.assertTrue(cleanup['all_tasks_cleaned']);self.assertTrue(cleanup['private_directory_cleaned'])

    def test_native_schema_path_source_write_and_active_resource_attacks_launch_no_worker(self):
        with tempfile.TemporaryDirectory(prefix='controlled-data-attacks-') as tmp:
            directory=Path(tmp);root=directory/'session';root.mkdir();other=directory/'other';other.mkdir()
            data=data_di_model();(root/'source.bpmn').write_bytes(data);(other/'other.bpmn').write_bytes(data)
            (root/'source-link.bpmn').symlink_to(other/'other.bpmn')
            (root/'protected.bpmn').write_text('synthetic protected file')
            def imported(r):element(r,'import',importType='synthetic',location='file:///synthetic/private',namespace='urn:outside')
            (root/'import.bpmn').write_bytes(change(data,imported))
            (root/'active.bpmn').write_bytes(data.replace(b'name="\xe5\xae\xa1\xe6\xa0\xb8"',b'name="task" onclick="arbitrary()"'))
            controller=LocalRenderController(SHARED,browser_path(),directory/'evidence');controller.register(root)
            tasks=[{'kind':'bpmn','source':'../other/other.bpmn'},
                   {'kind':'bpmn','source':str(other/'other.bpmn')},
                   {'kind':'bpmn','source':'source-link.bpmn'},
                   {'kind':'bpmn','source':'file:source.bpmn'},
                   {'kind':'bpmn','source':'protected.bpmn'},
                   {'kind':'bpmn','source':'import.bpmn'},
                   {'kind':'bpmn','source':'active.bpmn'},
                   {'kind':'bpmn','source':'source.bpmn','bpmn_plan':{'backend':'arbitrary-script'}},
                   {'kind':'bpmn','source':'source.bpmn','output':'source.bpmn'},
                   {'kind':'bpmn','source':'source.bpmn','command':'arbitrary command'}]
            try:
                with patch('enterprise.local_render.subprocess.Popen',side_effect=AssertionError('attack launched worker')) as launch:
                    for index,task in enumerate(tasks):
                        row=dispatch(root,task,'%032x'%index,timeout=15)
                        self.assertEqual('refused',row['status'],row);self.assertTrue(row['cleaned'])
                    launch.assert_not_called()
                self.assertEqual(data,(root/'source.bpmn').read_bytes())
                self.assertEqual(data,(other/'other.bpmn').read_bytes())
                self.assertEqual('synthetic protected file',(root/'protected.bpmn').read_text())
                self.assertEqual([],list((root/'.render/results').iterdir()))
            finally:cleanup=controller.close()
            self.assertTrue(cleanup['all_tasks_cleaned']);self.assertTrue(cleanup['private_directory_cleaned'])


if __name__=='__main__':unittest.main()
