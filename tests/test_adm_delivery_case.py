"""Current ADM formal outputs must retain scenario sources and version boundaries."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

CASE=Path(__file__).resolve().parents[1]/'togaf-standard-10th-ai/maintenance/cases/omnichannel'
sys.path.insert(0,str(CASE))
def module(name):
    spec=importlib.util.spec_from_file_location(name,CASE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
builder=module('build_adm_delivery_case')
forward=module('verify_adm_delivery_forward')

class ADMFormalDeliveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.material=json.loads((CASE/'adm-delivery-materials.json').read_text())
        cls.model,cls.cycle,cls.mapping=builder.build(cls.material)

    def test_same_model_has_all_authored_formal_outputs_and_stage_bindings(self):
        self.assertEqual(23,len(self.model['deliverables']))
        self.assertEqual(90,sum(len(d['sections']) for d in self.model['deliverables']))
        self.assertEqual([],forward.binding_findings(self.material,self.model,self.cycle,self.mapping))

    def test_missing_chapter_input_is_not_filled_from_contract_instructions(self):
        changed=copy.deepcopy(self.material);changed['deliverables'][0]['sections'].pop()
        with self.assertRaisesRegex(ValueError,'chapters differ'):
            builder.build(changed)

    def test_formal_output_must_be_part_of_actual_phase(self):
        changed=copy.deepcopy(self.cycle)
        phase=next(p for p in changed['phases'] if p['phase']=='G')
        phase['iterations'][-1]['output_refs']=[r for r in phase['iterations'][-1]['output_refs'] if r['collection']!='deliverables']
        result=forward.binding_findings(self.material,self.model,changed,self.mapping)
        self.assertTrue(any(x.startswith('formal-output-not-in-phase:') for x in result))

    def test_business_policy_material_change_invalidates_existing_text(self):
        material=copy.deepcopy(self.material)
        spec=next(d for d in material['deliverables'] if d['deliverable_id']=='architecture-requirements-specification')
        spec['sections'][1]['conclusion']=spec['sections'][1]['conclusion'].replace('2件','1件').replace('24小时','8小时')
        result=forward.binding_findings(material,self.model,self.cycle,self.mapping)
        self.assertTrue(any(x.startswith('stale-chapter-prose:') for x in result))
        self.assertTrue(any(x.startswith('stale-phase-material-map:') for x in result))

    def test_candidate_draft_cannot_be_marked_as_real_approval(self):
        model=copy.deepcopy(self.model);model['deliverables'][0]['approval_status']='approved'
        result=forward.binding_findings(self.material,model,self.cycle,self.mapping)
        self.assertTrue(any(x.startswith('fabricated-delivery-acceptance:') for x in result))

    def test_inherited_serial_dates_cannot_replace_shared_experiment_window(self):
        model=copy.deepcopy(self.model)
        next(e for e in model['entities'] if e['id']=='WP-OFFLINE')['attributes'].update(start='2026-11-21',end='2026-12-04')
        result=forward.binding_findings(self.material,model,self.cycle,self.mapping)
        self.assertIn('experiment-window-mismatch:WP-OFFLINE',result)

    def test_policy_semantic_change_reopens_old_cycle_even_when_model_valid(self):
        model=copy.deepcopy(self.model)
        policy=next(e for e in model['entities'] if e['id']=='ADM-DELIVERY-POLICY')
        policy['attributes']['active_policy']={'version':'V2-candidate','offline_max_items':1,'pending_hours':8}
        self.assertEqual([], [i for i in builder.validate(model) if i['level']=='error'])
        result=forward.check_cycle(self.cycle,model,CASE/'generated-adm/cycles')
        self.assertFalse(result['recorded_cycle_complete'])
        self.assertFalse(result['foundation_source_coverage_complete'])
        affected={p['phase'] for p in result['phases'] if p['gaps']}
        self.assertTrue(set('BCDEFG')<=affected)

    def test_chapter_evidence_missing_blocks_strict_assembly(self):
        model=copy.deepcopy(self.model)
        delivery=next(d for d in model['deliverables'] if d['deliverable_id']=='architecture-contract')
        references=delivery['assembly']['section_bindings']['验收与证据']['entity_ids']
        record=next(e for e in model['entities'] if e['id'] in references and e['type']=='project:section_evidence')
        record['attributes']['decision']='';record['evidence']=[]
        _,contracts,_,_=forward.registry()
        result=forward.assemble(model,delivery,contracts['architecture-contract'])
        self.assertEqual('blocked',result['status'])
        self.assertTrue(any(r['code']=='assembly-section-record-evidence' for r in result['gaps']))

    def test_nonrendered_assignment_outputs_link_only_to_generated_files(self):
        from generate import generate
        from assignment_projection import markdown
        view=next(v for v in self.model['views'] if v['id']=='role-assignment')
        # The render-enabled source still includes PNG; the real non-rendered
        # generation must remove that link while retaining SVG and Mermaid.
        self.assertIn('(role-assignment.png)',markdown(self.model,view))
        with tempfile.TemporaryDirectory() as temporary:
            directory=Path(temporary)
            generate(self.model,directory,view_ids=['role-assignment'],render=False,strict=True)
            checked,missing=forward.generated_markdown_links(directory)
            self.assertTrue(checked)
            self.assertEqual([],missing)
            self.assertFalse((directory/'artifacts/role-assignment.png').exists())
            self.assertIn('PNG 尚未渲染',(directory/'artifacts/role-assignment.md').read_text())

if __name__=='__main__':unittest.main()
