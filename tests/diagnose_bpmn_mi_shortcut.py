#!/usr/bin/env python3
"""Retain zero-model MI/shortcut/mixed local render and counterexample evidence."""
import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
SHARED=REPO/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(SHARED/'scripts'))
from enterprise.local_render import LocalRenderController
from test_controlled_bpmn_data_render import browser_path,dispatch
from bpmn_render import diagram_plan
from standards import check_native,make_package,package_bytes,Invalid,Incomplete
from bpmn_mi_shortcut_fixtures import mi_model,shortcut_model,mixed_model
from bpmn_role_type_fixtures import multi_instance_model
from bpmn_data_compensation_fixtures import by_id,change,MODEL

OWNED=[
 'tests/bpmn_role_type_fixtures.py','tests/test_bpmn_role_types.py',
 'tests/bpmn_mi_shortcut_fixtures.py','tests/test_bpmn_mi_shortcut.py',
 'tests/test_controlled_bpmn_mi_shortcut.py','tests/diagnose_bpmn_mi_shortcut.py',
 *['togaf-standard-10th-ai/skills/_shared/scripts/'+n for n in [
 'bpmn_data_compensation.py','bpmn_data_notation.py','bpmn_data_render.py','bpmn_data_render.mjs','bpmn_data_scene.mjs',
 'bpmn_design_semantics.py','bpmn_design_render.py','bpmn_design_render.mjs','bpmn_design_scene.mjs','bpmn_render.py','bpmn_semantics.py']],
 'togaf-standard-10th-ai/maintenance/stabilization/bpmn-mi-shortcut-binding-additions.json',
 'togaf-standard-10th-ai/maintenance/stabilization/bpmn-mi-shortcut-mixed.md']
DEPENDENCIES=['tests/enterprise/local_render.py','tests/test_controlled_bpmn_attribute_gate.py','tests/test_bpmn_design_time.py',
 'tests/test_controlled_bpmn_data_render.py','tests/bpmn_data_compensation_fixtures.py','tests/bpmn_data_di_fixtures.py','tests/bpmn_design_fixtures.py',
 *['togaf-standard-10th-ai/skills/_shared/scripts/'+n for n in ['standards.py','bpmn_references.py','controlled_render_worker.mjs','browser_resolver.mjs','raster_tiles.mjs','generate.py']],
 *['togaf-standard-10th-ai/skills/_shared/standards/sources/bpmn-2.0.2/'+n for n in ['BPMN-2.0.2.pdf','BPMN-2.0.2.pages.json','BPMN20.cmof','BPMNDI.cmof','BPMN20.xsd','Semantic.xsd','BPMNDI.xsd','DI.xsd','DC.xsd']],
 'togaf-standard-10th-ai/skills/_shared/standards/coverage-bindings.json']


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def snapshot(paths):return {name:sha(REPO/name) for name in paths}
def write(path,value):
    with path.open('x') as stream:json.dump(value,stream,ensure_ascii=False,indent=2);stream.write('\n')
def record(path):return {'path':str(path.resolve().relative_to(REPO)),'sha256':sha(path),'bytes':path.stat().st_size}


def run(out):
    out=out.resolve();out.mkdir(parents=True,exist_ok=False)
    owned_before=snapshot(OWNED);dependencies_before=snapshot(DEPENDENCIES)
    session=out/'session';session.mkdir();cases=out/'cases';cases.mkdir();counter=out/'counterexamples';counter.mkdir()
    controller=LocalRenderController(SHARED,browser_path(),out/'controller-evidence');controller.register(session)
    rows=[]
    try:
        for index,(name,data) in enumerate([('mi-parallel',mi_model()),('mi-sequential',mi_model(True,True)),('sequenceflow-shortcut',shortcut_model()),('mixed-choreography-data',mixed_model())]):
            case=cases/name;case.mkdir();source=session/(name+'.bpmn');source.write_bytes(data)
            (case/'native.bpmn').write_bytes(data);plan=diagram_plan(data);write(case/'source-plan.json',plan)
            validation=check_native(data,'bpmn','2.0.2');write(case/'validation.json',validation)
            package=make_package(data,'bpmn','2.0.2');write(case/'native-package.json',package)
            if package_bytes(package,'bpmn','2.0.2')!=data:raise RuntimeError('native bytes changed in package roundtrip')
            task={'kind':'bpmn','source':source.name};write(case/'task.json',task)
            row=dispatch(session,task,'%032x'%(index+500));write(case/'response.json',row)
            if row['status']!='pass':raise RuntimeError(name+': '+str(row.get('reason')))
            if source.read_bytes()!=data or not row['cleaned'] or row['owned_processes_remaining']:raise RuntimeError('source/cleanup failure')
            for key,value in row['outputs'].items():
                native=session/value['path'];dest=case/native.name;shutil.copyfile(native,dest)
            rows.append({'name':name,'status':'passed','native_roundtrip':'byte-exact','source_sha256':hashlib.sha256(data).hexdigest(),
                         'response':record(case/'response.json'),'plan':record(case/'source-plan.json'),
                         'outputs':[record(p) for p in sorted(case.iterdir()) if p.suffix in {'.svg','.png'}]})
    finally:
        cleanup=controller.close();write(out/'cleanup.json',cleanup)
    def legacy(r):
        for sid in ['MI_INPUT','MI_OUTPUT']:
            by_id(r,sid).set('isCollection','true');by_id(r,sid).set('itemSubjectRef','tns:COLLECTION')
    invalids=[('legacy-matching-collection-mi-items',change(multi_instance_model(),legacy),[221]),
              ('task-mi-external-data-object',change(mi_model(),lambda r:setattr(by_id(r,'MI').find('{'+MODEL+'}loopDataInputRef'),'text','tns:SOURCE')),[221]),
              ('shortcut-wrong-endpoint',change(shortcut_model(),lambda r:by_id(r,'SHORTCUT_DI').set('targetElement','tns:B_DI')),[398,405,442]),
              ('shortcut-missing-output-association',change(shortcut_model(),lambda r:by_id(r,'OUT').getparent().remove(by_id(r,'OUT'))),[253,398]),
              ('mixed-unrelated-owner-endpoint',change(mixed_model(),lambda r:by_id(r,'DIN_DI').set('targetElement','tns:CT_DI')),[405,441])]
    negatives=[]
    for name,data,pages in invalids:
        source=counter/(name+'.bpmn');source.write_bytes(data);validation=check_native(data,'bpmn','2.0.2')
        try:diagram_plan(data);raise RuntimeError('counterexample was accepted: '+name)
        except (Invalid,Incomplete) as exc:error={'type':type(exc).__name__,'message':str(exc)}
        write(counter/(name+'.json'),{'input':record(source),'validation':validation,'diagram_refusal':error,'normative_physical_pages':pages})
        negatives.append({'name':name,'input':record(source),'status':'rejected','diagram_refusal':error})
    owned_after=snapshot(OWNED);dependencies_after=snapshot(DEPENDENCIES)
    if owned_before!=owned_after or dependencies_before!=dependencies_after:raise RuntimeError('group source/dependency changed during diagnosis')
    summary={'schema_version':'bpmn-mi-shortcut-mixed-diagnostic/1','mode':'controlled-local-process','cases':rows,'counterexamples':negatives,
             'owned_source_hashes':owned_after,'dependency_hashes':dependencies_after,'source_unchanged':True,'cleanup':cleanup,
             'models_started':0,'model_budget_changes':0,'full_design_time_conformance':False,'human_acceptance':'pending','organization_approval':'pending-signature',
             'limitations':['External scalar-of semantic types and opaque expression values remain uncovered.','Fixed controller/renderer only; no model sessions, arbitrary script or automatic layout.','Temporary shortcut display Association has no authoritative semantic_id and is not exported.']}
    write(out/'summary.json',summary)
    print(json.dumps({'out':str(out.relative_to(REPO)),'cases':len(rows),'counterexamples':len(negatives),'source_unchanged':True}))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',required=True,type=Path);run(parser.parse_args().out)
