#!/usr/bin/env python3
"""Zero-model functional and isolation admission for the controlled renderer."""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from enterprise.local_render import LocalRenderController, PROTOCOL

REPO = Path(__file__).resolve().parents[1]
FILES = ('tests/enterprise/local_render.py', 'tests/test_controlled_render.py',
         'tests/diagnose_controlled_render.py',
         'tests/test_bpmn_render.py','tests/bpmn_design_fixtures.py',
         'tests/test_uml_render.py',
         'togaf-standard-10th-ai/skills/_shared/scripts/controlled_render_client.py',
         'togaf-standard-10th-ai/skills/_shared/scripts/controlled_render_worker.mjs')


def hashes():
    shared=REPO/'togaf-standard-10th-ai/skills/_shared'
    paths={REPO/p for p in FILES}
    # Bind transitive native validation/render adapters, normative material and
    # the fixed font/lock bytes as well as the queue transport itself.
    for directory in (shared/'scripts',shared/'standards',shared/'assets/fonts'):
        paths.update(p for p in directory.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    paths.update(shared/name for name in ('package-lock.json','requirements.txt'))
    return {p.relative_to(REPO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def run(out, shared, browser):
    before=hashes()
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    test = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(REPO/'tests'),
                           '-p', 'test_controlled_render.py', '-v'], capture_output=True, text=True, timeout=60)
    (out/'isolation-tests.log').write_text(test.stdout+test.stderr)
    rows = []
    with tempfile.TemporaryDirectory(prefix='togaf-render-admission-') as temp:
        root = Path(temp)/'actor';root.mkdir()
        other = Path(temp)/'other';other.mkdir();(other/'secret.svg').write_text('synthetic other session')
        controller = LocalRenderController(shared, browser, out/'controller')
        controller.register(root)
        from test_controlled_render import SVG
        from test_bpmn_render import BPMN
        from bpmn_design_fixtures import conversation,choreography
        from test_uml_render import UML
        inputs = [('svg','svg',SVG.replace(b'safe','中文字体'.encode())),
                  ('mmd','mmd','flowchart LR\nA[业务需求] --> B[架构评审]\nB --> C[交付证据]'.encode()),
                  ('bpmn','bpmn',BPMN),('conversation','bpmn',conversation()),
                  ('choreography','bpmn',choreography()),('choreography-expanded','bpmn',choreography(True,True)),
                  ('uml-class','uml-class-layout',UML)]
        for name,kind,data in inputs:
            source=name+('.uml' if kind=='uml-class-layout' else '.'+kind)
            (root/source).write_bytes(data)
            (root/'task.json').write_text(json.dumps({'kind':kind,'source':source}))
            done = subprocess.run([sys.executable, '-B', str(Path(shared)/'scripts/controlled_render_client.py'), 'task.json'],
                                  cwd=root, capture_output=True, text=True, timeout=180,
                                  env={'PATH':os.environ['PATH'], 'PYTHONDONTWRITEBYTECODE':'1'})
            (out/(name+'.log')).write_text(done.stdout+done.stderr)
            rows.append({'name':name,'kind':kind,'status':'pass' if done.returncode==0 else 'fail','exit_code':done.returncode})
        for path in (root/'.render/results').iterdir():
            (out/path.name).write_bytes(path.read_bytes())
        cleaned = controller.close()
        timeout_root=Path(temp)/'timeout-actor';timeout_root.mkdir()
        chain='flowchart LR\n'+'\n'.join('N%d[阶段%d] --> N%d[阶段%d]'%(i,i,i+1,i+1) for i in range(449))
        (timeout_root/'input.mmd').write_text(chain)
        (timeout_root/'task.json').write_text(json.dumps({'kind':'mmd','source':'input.mmd'}))
        timeout_controller=LocalRenderController(shared,browser,out/'timeout-controller',timeout=1)
        timeout_controller.register(timeout_root)
        timed=subprocess.run([sys.executable,'-B',str(Path(shared)/'scripts/controlled_render_client.py'),'task.json'],
                             cwd=timeout_root,capture_output=True,text=True,timeout=30)
        (out/'timeout.log').write_text(timed.stdout+timed.stderr)
        timeout_cleanup=timeout_controller.close()
        timeout_event=timeout_controller.events[-1] if timeout_controller.events else {}
        timeout_passed=(timed.returncode!=0 and 'timeout' in timeout_event.get('reason','')
                        and timeout_event.get('cleaned') is True
                        and timeout_event.get('owned_processes_remaining')==[]
                        and bool(timeout_event.get('terminated_owned_processes')))
    after=hashes();stable=before==after
    result = {'schema_version':PROTOCOL, 'mode':'controlled-local-process',
              'passed':test.returncode==0 and all(r['status']=='pass' for r in rows)
                       and cleaned['private_directory_cleaned'] and cleaned['all_tasks_cleaned'] and timeout_passed and stable,
              'status':'pass' if test.returncode==0 and all(r['status']=='pass' for r in rows) and timeout_passed and stable else 'fail',
              'model_sessions':0,'model_requests_observed':0,'functional':rows,
              'isolation_tests_exit_code':test.returncode,'source_sha256':before,'source_stable':stable,
              'changed_sources':[p for p in sorted(set(before)|set(after)) if before.get(p)!=after.get(p)],
              'controller_cleanup':cleaned,
              'timeout_cleanup':timeout_cleanup,'timeout_isolation_passed':timeout_passed,
              'limits':['Controller process is a fixed graphic adapter, not the native Actor browser sandbox.',
                        'Supported rendering scopes and full UML/BPMN completeness are separate gates.']}
    (out/'summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'}, ensure_ascii=False))
    return 0 if result['passed'] else 3


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--shared', type=Path, default=REPO/'togaf-standard-10th-ai/skills/_shared')
    parser.add_argument('--browser', type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.out,args.shared,args.browser))
