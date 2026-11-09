"""Exercise shared-model changes and evidence boundaries through public APIs."""
import copy
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
SHARED=ROOT/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(SHARED/'scripts'))
spec=importlib.util.spec_from_file_location('g249_case',SHARED/'examples/g249-omnichannel/build.py')
CASE=importlib.util.module_from_spec(spec);spec.loader.exec_module(CASE)


class G249IntegrationTests(unittest.TestCase):
    def test_case_cli_preserves_generated_manifest_hashes(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(sys,'argv',['build.py','--out',folder]),contextlib.redirect_stdout(io.StringIO()):
                CASE.main()
            for name in ('baseline','offline-change'):
                dest=Path(folder)/name
                manifest=json.loads((dest/'manifest.json').read_text())
                self.assertEqual([],json.loads((dest/'validation.json').read_text())['issues'])
                for filename,expected in manifest['output_sha256'].items():
                    self.assertEqual(expected,hashlib.sha256((dest/filename).read_bytes()).hexdigest(),name+'/'+filename)

    def test_domain_generation_does_not_require_personnel(self):
        model=CASE.domain_model()
        self.assertFalse(model.get('analyses'))
        self.assertEqual([],CASE.validate(model))
        with tempfile.TemporaryDirectory() as folder:
            CASE.generate(model,folder,all_items=True,strict=True)
            self.assertTrue((Path(folder)/'artifacts/interface-network.svg').is_file())

    def test_offline_requirement_changes_design_and_evidence_requirements(self):
        before,after=CASE.build(),CASE.build(True)
        a={e['id']:e for e in before['entities']};b={e['id']:e for e in after['entities']}
        self.assertIn('REQ-OFFLINE',b);self.assertNotIn('REQ-OFFLINE',a)
        self.assertIn('IF-RECOVERY',b);self.assertIn('TRANS-OFFLINE',b)
        self.assertNotEqual(a['RISK-STOCK']['attributes'],b['RISK-STOCK']['attributes'])
        old=before['analyses'][0]['inputs'];new=after['analyses'][0]['inputs']
        self.assertEqual(old['assessments'],new['assessments'])
        self.assertNotEqual(old['requirements'],new['requirements'])
        result=CASE.evaluate(after['analyses'][0],after)['result']
        self.assertTrue(result['gaps'])
        self.assertIsNone(next(o for o in new['assessments'] if o['id']=='OBS-A')['proficiency'])
        self.assertEqual('candidate',after['project']['approval_status'])
        target=next(r for r in new['requirements'] if r['id']=='REQ-SKILL-SOL')
        development=next(r for r in new['development'] if r['id']=='DEV-A')
        self.assertLessEqual(set(target['behavioral_criteria']),set(development['success_criteria']))
        self.assertLessEqual(set(target['behavioral_criteria']),set(development['reassessment']['criteria']))
        self.assertEqual('2',development['requirement_versions'][target['id']])
        self.assertIn('CASE-CHANGE',b['REQ-OFFLINE']['evidence'])
        self.assertIn('LOCAL-ORDER-RECORD',b)
        self.assertTrue(any(r['source']=='ORDER-CONFIRMED' and r['target']=='ORDER-FULFIL' for r in after['relationships']))
        self.assertFalse(any(r['source']=='ORDER-PENDING' and r['target']=='ORDER-FULFIL' for r in after['relationships']))
        self.assertLessEqual({a for t in new['tasks'] for a in t['artifact_ids']},{v['artifact_id'] for v in after['views']})
        self.assertTrue(next(e for e in after['entities'] if e['id']=='DELIVERY-NOTE')['attributes']['decision_agenda'])
        self.assertIn('solution-delivery-notebook',next(t for t in new['tasks'] if t['id']=='TASK-CH')['artifact_ids'])
        information=b['DELIVERY-NOTE']['attributes']['architecture_summary']['information']
        self.assertEqual(['order-states','offline-data-boundary'],information['view_ids'])

    def test_entity_and_relationship_edits_invalidate_stale_analysis(self):
        original=CASE.build()
        for mutate in ('entity','relation','new-relation','removed-relation'):
            with self.subTest(mutate=mutate):
                model=copy.deepcopy(original)
                if mutate=='entity':
                    next(e for e in model['entities'] if e['id']=='APP-STOCK')['name']='changed boundary'
                elif mutate=='relation':model['relationships'][0]['label']='changed meaning'
                elif mutate=='new-relation':
                    item=copy.deepcopy(model['relationships'][0]);item['id']='NEW-EDGE';model['relationships'].append(item)
                else:model['relationships'].pop(0)
                with self.assertRaises(ValueError):CASE.evaluate(model['analyses'][0],model)

    def test_single_object_update_is_visible_in_all_generated_views(self):
        model=CASE.domain_model(True)
        next(e for e in model['entities'] if e['id']=='APP-STOCK')['name']='库存与承诺服务（修订）'
        model=CASE.attach_role_assessment(model)
        with tempfile.TemporaryDirectory() as folder:
            CASE.generate(model,folder,all_items=True,strict=True)
            for vid in ('application-catalog','interface-network'):
                payload=json.loads((Path(folder)/'artifacts'/f'{vid}.json').read_text())
                self.assertEqual('库存与承诺服务（修订）',next(e for e in payload['entities'] if e['id']=='APP-STOCK')['name'])
                self.assertIn('库存与承诺服务（修订）',(Path(folder)/'artifacts'/f'{vid}.md').read_text())
            svg=(Path(folder)/'artifacts/interface-network.svg').read_text()
            self.assertIn('APP-STOCK',svg)
            for coverage in (Path(folder)/'artifacts').glob('*.coverage.json'):
                self.assertFalse(json.loads(coverage.read_text()).get('errors'),coverage.name)

    def test_current_portable_source_and_runtime_mapping_are_bound(self):
        from build_corpus_registry import current_g249_structure
        from runtime_provenance import fingerprints
        for fid in ('G249/fig4-1','G249/fig4-2'):
            record=current_g249_structure(ROOT/'togaf-standard-10th-zh',fid)
            self.assertTrue(record['current_source'])
            reading=json.dumps(record['reading'],ensure_ascii=False)
            self.assertNotIn('两个灰色 Domain 框',reading)
            self.assertNotIn('System 1..* contains Building Block 1..*',reading)
        files=fingerprints(SHARED)
        self.assertIn('references/g249/skill-task-map.json',files)
        self.assertIn('references/source-structures/G249-fig4-1.json',files)


if __name__=='__main__':unittest.main()
