#!/usr/bin/env python3
"""Zero-model retained admission for the fixed native data-DI worker branch."""
import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from diagnose_controlled_render import hashes
from test_controlled_bpmn_data_render import ROOT,SHARED,browser_path,dispatch
from enterprise.local_render import LocalRenderController
from bpmn_data_di_fixtures import data_di_model,boundary_di_model
from bpmn_render import diagram_plan

FILES=('tests/diagnose_controlled_bpmn_data.py','tests/test_controlled_bpmn_data_render.py',
       'tests/bpmn_data_di_fixtures.py','tests/bpmn_data_compensation_fixtures.py',
       'tests/bpmn_role_type_fixtures.py','tests/test_bpmn_role_types.py')


def snapshot():
    rows=hashes()
    rows.update({name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in FILES})
    return rows


def run(out):
    before=snapshot();out=Path(out).resolve();out.mkdir(parents=True,exist_ok=False)
    rows=[]
    with tempfile.TemporaryDirectory(prefix='controlled-data-admission-') as tmp:
        root=Path(tmp)/'session';root.mkdir()
        controller=LocalRenderController(SHARED,browser_path(),out/'controller');controller.register(root)
        try:
            for index,(name,data) in enumerate([('data-full',data_di_model()),('data-owner-partial',boundary_di_model())]):
                source=name+'.bpmn';(root/source).write_bytes(data);(out/source).write_bytes(data)
                expected=diagram_plan(data);row=dispatch(root,{'kind':'bpmn','source':source},'%032x'%index)
                report=row.get('renderer_report',{});scene=report.get('bpmn_data_di',{})
                exact=(row.get('status')=='pass' and scene.get('backend')=='native-data-di'
                       and report.get('native_registry')==[g['graphic_id'] for g in expected['graphics']]
                       and report.get('native_geometry')==[{k:g[k] for k in ['graphic_id','semantic_id','kind','source_plane_index']}
                           | {k:g[k] for k in ['bounds','waypoints'] if k in g} for g in expected['graphics']]
                       and scene.get('data_depiction_inventory')==expected['data_depiction_inventory']
                       and not report.get('external_requests') and not report.get('derived_layout')
                       and report.get('text_geometry',{}).get('font_loaded') is True
                       and report.get('text_geometry',{}).get('outside')==[]
                       and (root/source).read_bytes()==data and row.get('cleaned') is True
                       and row.get('owned_processes_remaining')==[])
                artifacts={}
                for key,item in row.get('outputs',{}).items():
                    suffix='browser.png' if key=='browser_png' else key
                    filename=name+'.'+suffix;shutil.copyfile(root/item['path'],out/filename)
                    artifacts[key]={'file':filename,'sha256':hashlib.sha256((out/filename).read_bytes()).hexdigest()}
                rows.append({'case':name,'status':'pass' if exact else 'fail','input_sha256':hashlib.sha256(data).hexdigest(),
                             'artifacts':artifacts,'functional_exact_geometry_and_isolation':exact})
        finally:cleanup=controller.close()
    after=snapshot();changes=[k for k in sorted(before.keys()|after.keys()) if before.get(k)!=after.get(k)]
    passed=all(r['status']=='pass' for r in rows) and cleanup['all_tasks_cleaned'] and cleanup['private_directory_cleaned'] and not changes
    result={'schema_version':'controlled-bpmn-data-admission/1','mode':'controlled-local-process',
            'passed':passed,'model_sessions':0,'model_requests_observed':0,'functional':rows,
            'source_sha256':before,'source_stable':not changes,'changed_sources':changes,'cleanup':cleanup,
            'limits':['Fixed native-data-di process/collaboration partial view only; no command, URL or browser-argument task fields.',
                      'This group does not admit a 507-case campaign or certify full UML/BPMN capabilities.',
                      'Professional visual acceptance and organization signature remain pending.']}
    (out/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},ensure_ascii=False))
    return 0 if passed else 3


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True)
    raise SystemExit(run(parser.parse_args().out))
