"""Actual controlled dispatch of MI, two-association shortcut and mixed views."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from enterprise.local_render import LocalRenderController
from test_controlled_bpmn_data_render import browser_path,dispatch
from bpmn_mi_shortcut_fixtures import mi_model,shortcut_model,mixed_model
from bpmn_data_compensation_fixtures import by_id,change

REPO=Path(__file__).resolve().parents[1]
SHARED=REPO/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(SHARED/'scripts'))
from standards import safe_xml
from bpmn_render import diagram_plan


class ControlledBPMNMISceneTests(unittest.TestCase):
    def test_actual_mi_shortcut_and_mixed_scene_preserve_source_geometry_and_cleanup(self):
        with tempfile.TemporaryDirectory(prefix='controlled-bpmn-next-') as tmp:
            folder=Path(tmp);root=folder/'session';root.mkdir()
            controller=LocalRenderController(SHARED,browser_path(),folder/'evidence');controller.register(root)
            try:
                for index,data in enumerate([mi_model(True,True),shortcut_model(),mixed_model()]):
                    source=root/('native-'+str(index)+'.bpmn');source.write_bytes(data)
                    row=dispatch(root,{'kind':'bpmn','source':source.name},'%032x'%(index+100))
                    self.assertEqual('pass',row['status'],row)
                    self.assertEqual(data,source.read_bytes());self.assertTrue(row['cleaned']);self.assertEqual([],row['owned_processes_remaining'])
                    report=row['renderer_report'];plan=diagram_plan(data)
                    self.assertEqual('controlled-local-process',report['mode']);self.assertEqual([],report['external_requests'])
                    self.assertTrue(report['source_authoritative']);self.assertFalse(report['derived_layout'])
                    self.assertEqual([],report['text_geometry']['outside']);self.assertTrue(report['text_geometry']['font_loaded'])
                    self.assertEqual([g['graphic_id'] for g in plan['graphics']],report['native_registry'])
                    svg=safe_xml((root/row['outputs']['svg']['path']).read_bytes());groups=svg.xpath('//*[@data-native-root]/*[@data-di-id]')
                    self.assertEqual(report['native_registry'],[e.get('data-di-id') for e in groups])
                    for g,e in zip(plan['graphics'],groups):
                        if g['kind']=='shape':
                            for key,value in g['bounds'].items():self.assertEqual(value,e.get('data-di-'+key))
                        else:self.assertEqual(g['waypoints'],json.loads(e.get('data-source-waypoints')))
                    for key in ['png','browser_png']:
                        self.assertEqual(b'\x89PNG\r\n\x1a\n',(root/row['outputs'][key]['path']).read_bytes()[:8])
                    if index==1:self.assertEqual(['OUT','IN'],json.loads(groups[-1].get('data-normalized-native-associations')))
            finally:cleanup=controller.close()
            self.assertTrue(cleanup['all_tasks_cleaned']);self.assertTrue(cleanup['private_directory_cleaned'])

    def test_invalid_shortcut_model_and_executable_plan_fields_launch_no_worker(self):
        with tempfile.TemporaryDirectory(prefix='controlled-bpmn-next-bad-') as tmp:
            folder=Path(tmp);root=folder/'session';root.mkdir()
            controller=LocalRenderController(SHARED,browser_path(),folder/'evidence');controller.register(root)
            bad=change(shortcut_model(),lambda r:by_id(r,'SHORTCUT_DI').set('targetElement','tns:B_DI'))
            (root/'bad.bpmn').write_bytes(bad);(root/'good.bpmn').write_bytes(shortcut_model())
            try:
                tasks=[{'kind':'bpmn','source':'bad.bpmn'},{'kind':'bpmn','source':'good.bpmn','bpmn_plan':{'backend':'arbitrary-script'}},{'kind':'bpmn','source':'good.bpmn','command':'synthetic arbitrary command'}]
                with patch('enterprise.local_render.subprocess.Popen',side_effect=AssertionError('invalid task launched worker')) as launch:
                    for index,task in enumerate(tasks):
                        row=dispatch(root,task,'%032x'%(index+200))
                        self.assertEqual('refused',row['status'],row);self.assertTrue(row['cleaned'])
                    launch.assert_not_called()
            finally:cleanup=controller.close()
            self.assertTrue(cleanup['all_tasks_cleaned']);self.assertTrue(cleanup['private_directory_cleaned'])


if __name__=='__main__':unittest.main()
