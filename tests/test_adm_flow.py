"""Complete ADM projection must retain candidates, conditionality and real records."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

SHARED = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED/'scripts'))
from adm_flow import build_mapping, generate_flow, mermaid_framework
from adm import initialize
from registry import load as registry


class ADMFlowTest(unittest.TestCase):
    def test_complete_current_contracts_and_all_registered_outputs(self):
        mapping = build_mapping()
        arts, dels, profiles, _ = registry()
        self.assertEqual(['Preliminary', *'ABCDEFGH', 'Requirements'], [p['id'] for p in mapping['phases']])
        self.assertEqual(94, sum(len(p['source_step_ids']) for p in mapping['phases']))
        self.assertEqual(set(dels), {d['id'] for d in mapping['deliverable_catalog']})
        self.assertEqual(set(dels), {d['id'] for p in mapping['phases'] for d in p['deliverables']})
        self.assertEqual(set(arts), {a['id'] for a in mapping['artifact_catalog']})
        self.assertTrue(all(a['phase_ids'] for a in mapping['artifact_catalog']))
        self.assertEqual(set(profiles), {i for a in mapping['artifact_catalog'] for i in a['profile_ids']})
        self.assertTrue({'catalog','matrix','diagram'} <= {a['kind'] for a in mapping['artifact_catalog']})

    def test_input_context_is_not_promoted_to_source_phase_output(self):
        p = next(p for p in build_mapping()['phases'] if p['id']=='A')
        d = next(d for d in p['deliverables'] if d['id']=='business-drivers')
        self.assertEqual('registry-phase-context', d['role'])
        p = next(p for p in build_mapping()['phases'] if p['id']=='F')
        d = next(d for d in p['deliverables'] if d['id']=='implementation-governance-model')
        self.assertEqual('if any', d['condition'])

    def test_c_coordination_and_requirements_feedback_are_preserved(self):
        mapping=build_mapping()
        p=next(p for p in mapping['phases'] if p['id']=='C')
        self.assertIn('data-application-alignment',p['criteria'])
        source=mermaid_framework(mapping)
        for phase in ['Preliminary',*'ABCDEFGH']:
            self.assertIn(f'RM -.需求与版本.-> {phase}',source)
            self.assertIn(f'{phase} -.变化与处置记录.-> RM',source)
        self.assertIn('H -.重开或新周期.-> A',source)
        self.assertIn('C -.数据应用发现修正业务.-> B',source)
        req=next(p for p in mapping['phases'] if p['id']=='Requirements')
        self.assertEqual(10,len(req['source_steps']))
        self.assertEqual({'ADM Phase Steps','Requirements Management Steps'},
                         {s['responsibility_column'] for s in req['source_steps']})
        self.assertTrue(all(s['text_en'] and s['explanation_zh'] for s in req['source_steps']))

    def test_generation_has_all_views_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            out=Path(temporary)/'flow'
            result=generate_flow(out)
            self.assertEqual('passed',result['status'])
            self.assertEqual(12,len(result['diagram_ids']))
            manifest=json.loads((out/'manifest.json').read_text())
            for identity in result['diagram_ids']:
                ET.parse(out/(identity+'.svg'))
                self.assertIn(identity+'.mmd',manifest['output_sha256'])
            self.assertFalse(result['rendered'])
            self.assertNotIn('.png]',(out/'README.md').read_text())
            reader=(out/'index.html').read_text()
            self.assertEqual(12,reader.count('data:image/svg+xml;base64,'))
            self.assertIn('<html lang="zh-CN">',reader)
            self.assertIn('跳转到流程图',reader)
            self.assertIn('summary:focus-visible',reader)
            self.assertIn('index.html',manifest['output_sha256'])
            with self.assertRaisesRegex(ValueError,'已存在'):
                generate_flow(out)

    def test_actual_cycle_needs_paired_model(self):
        with self.assertRaisesRegex(ValueError,'同时提供'):
            build_mapping(model={})

    def test_actual_dependencies_and_uncompleted_states_are_not_invented(self):
        model=json.loads((SHARED/'examples/omnichannel/adm-delivery/model.json').read_text())
        cycle=initialize(model,'flow-example','可验证的虚构架构练习')
        c=next(p for p in cycle['phases'] if p['phase']=='C')
        c['iterations'][0]['depends_on']=['B-1']
        mapping=build_mapping(cycle,model)
        actual=mapping['cycle']
        row=next(r for r in actual['iterations'] if r['id']=='C-1')
        self.assertEqual(['B-1'],row['depends_on'])
        self.assertEqual('planned',row['recorded_status'])
        self.assertFalse(actual['check']['recorded_cycle_complete'])
        self.assertEqual('incomplete',row['current_phase_check']['status'])

    def test_missing_reference_cannot_be_silently_omitted(self):
        model=json.loads((SHARED/'examples/omnichannel/adm-delivery/model.json').read_text())
        cycle=initialize(model,'flow-example','虚构练习')
        cycle['phases'][0]['iterations'][0]['output_refs']=[{'collection':'views','id':'MISSING'}]
        with self.assertRaisesRegex(ValueError,'无效周期引用'):
            build_mapping(cycle,model)


if __name__=='__main__':
    unittest.main()
