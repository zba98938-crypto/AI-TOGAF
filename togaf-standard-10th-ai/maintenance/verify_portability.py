# -*- coding: utf-8 -*-
"""Extract the actual sealed archives and reject original-project reads from Python."""
from pathlib import Path
import json,subprocess,hashlib,sys,datetime,os,tarfile,posixpath,argparse
sys.dont_write_bytecode=True
C=Path(__file__).resolve().parents[1];BASE=C/'maintenance/work/portable-verification'
CLOSURE_RUNNER= '''import json,sys
from pathlib import Path
sys.dont_write_bytecode=True
allowed=Path(sys.argv[1]).resolve();original=Path(sys.argv[2]).resolve()
sys.path.insert(0,str(allowed/'_shared/scripts'))
def audit(event,args):
 if event=='open' and not isinstance(args[0],int):
  path=Path(args[0]).resolve()
  if original in path.parents and allowed not in path.parents:raise PermissionError('Relocation forbids original project access: '+str(path))
sys.addaudithook(audit)
from source_closure import verify_source_closure
report=verify_source_closure(allowed/'_shared/corpus')
print(json.dumps(report,ensure_ascii=False))
raise SystemExit(int(not report['passed']))
'''
RUNNER='''import sys,os,runpy
from pathlib import Path
sys.dont_write_bytecode=True
allowed=Path(sys.argv[1]).resolve();original=Path(sys.argv[2]).resolve();script=allowed/'_shared/scripts/local_tool.py'
sys.path.insert(0,str(allowed/'_shared/vendor'))
sys.path.insert(0,str(allowed/'_shared/scripts'))
def audit(event,args):
 if event=='open' and not isinstance(args[0],int):
  path=Path(os.fsdecode(args[0])).resolve()
  if original in path.parents and allowed not in path.parents and path!=allowed:raise PermissionError('Relocation forbids original project access: '+str(path))
sys.addaudithook(audit)
sys.argv=[str(script)]+sys.argv[3:]
runpy.run_path(str(script),run_name='__main__')
'''
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def extract(archive,dest):
 with tarfile.open(archive,'r:gz') as tf:
  for m in tf.getmembers():
   assert m.name.startswith('skills/') and '..' not in Path(m.name).parts and not Path(m.name).is_absolute(),m.name
   if m.issym():assert posixpath.normpath(posixpath.join(posixpath.dirname(m.name),m.linkname)).startswith('skills/_shared/node_modules/'),m.name
   if m.islnk():assert m.linkname.startswith('skills/') and '..' not in Path(m.linkname).parts,m.name
  tf.extractall(dest)
def main(release_dir=None,run_dir=None,out=None):
 release_root=Path(release_dir).resolve() if release_dir is not None else C/'release'
 report_path=Path(out) if out is not None else C/'quality/portability-validation.json'
 run_dir=Path(run_dir).resolve() if run_dir is not None else BASE/('archive-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
 if report_path.exists():raise ValueError('Report path must be new; previous evidence is immutable: '+str(report_path))
 if run_dir.exists():raise ValueError('Extraction directory must be new; previous evidence is immutable: '+str(run_dir))
 run_dir.mkdir(parents=True,exist_ok=False);target=run_dir/'skills';checks=[]
 release=json.loads((release_root/'release-manifest.json').read_text());assert release['passed']
 for key in ['package','optional_node_dependencies']:
  item=release[key];archive=release_root/item['path'];assert sha(archive)==item['sha256'];extract(archive,run_dir)
 sealed=json.loads((target/'package-manifest.json').read_text());bad=[x['path'] for x in sealed['files'] if sha(target/x['path'])!=x['sha256']]
 checks.append({'id':'extracted-archive-content-hashes','passed':not bad,'files':len(sealed['files']),'mismatches':bad})
 driver=target/'isolation-driver.py';driver.write_text(RUNNER)
 closure_driver=target/'source-closure-isolation-driver.py';closure_driver.write_text(CLOSURE_RUNNER)
 closure_run=subprocess.run([sys.executable,'-B',str(closure_driver),str(target),str(C.parent)],cwd=target,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':''})
 closure=json.loads(closure_run.stdout) if closure_run.returncode==0 else {}
 checks.append({'id':'full-retrieval-source-closure','passed':closure_run.returncode==0 and closure.get('passed') is True,
                'returncode':closure_run.returncode,'counts':closure.get('counts',{}),'issues':closure.get('issues',[]),
                'stderr':closure_run.stderr[-2000:]})
 (run_dir/'retrieval-source-closure.json').write_text(closure_run.stdout)
 tests=[('doctor',['doctor']),('query',['query','架构角色 库存 一致性','--document','G249','--limit','2']),('Chinese-body-query',['query','先详细细化目标解决方案','--document','C220-web-2025:04-applying-the-adm','--limit','2']),('validate',['validate','_shared/examples/omnichannel/sufficient.json','--report','work/validation.json']),('generate-render',['generate','_shared/examples/omnichannel/sufficient.json','--out','work/output','--view','role-assignment','--render','--strict']),('policy',['policy','_shared/examples/omnichannel/sufficient-policy-change.json','--contract','_shared/examples/omnichannel/shared-policy-contract.json','--before','_shared/examples/omnichannel/sufficient.json','--out','work/policy-check.json'])]
 tests += [('ADM-source-steps',['adm','check','--model','_shared/examples/omnichannel/adm/model.json','--cycle','_shared/examples/omnichannel/adm/cycles/cycle.json','--require-complete','--require-source-coverage']),
           ('ADM-policy-v2-stale',['adm','check','--model','_shared/examples/omnichannel/adm/model-policy-v2.json','--cycle','_shared/examples/omnichannel/adm/cycles/cycle-policy-v2-needs-review.json','--require-complete','--require-source-coverage'])]
 tests += [('G226-Chinese-body-query',['query','不应带着预设答案开始评审','--document','G226','--limit','2'])]
 tests += [('ADM-formal-cycle',['adm','check','--model','_shared/examples/omnichannel/adm-delivery/model.json','--cycle','_shared/examples/omnichannel/adm-delivery/cycles/cycle.json','--require-complete','--require-source-coverage']),
           ('ADM-formal-generate',['generate','_shared/examples/omnichannel/adm-delivery/model.json','--out','work/adm-delivery','--all','--strict']),
           ('ADM-formal-v2-stale',['adm','check','--model','_shared/examples/omnichannel/adm-delivery/model-policy-v2.json','--cycle','_shared/examples/omnichannel/adm-delivery/cycles/cycle.json','--require-complete','--require-source-coverage'])]
 tests += [('ADM-flow',['adm','flow','--model','_shared/examples/omnichannel/adm-delivery/model.json','--cycle','_shared/examples/omnichannel/adm-delivery/cycles/cycle.json','--out','work/adm-flow','--render'])]
 for name,args in tests:
  r=subprocess.run([sys.executable,'-B',str(driver),str(target),str(C.parent)]+args,cwd=target,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':''});passed=r.returncode==0;detail={}
  if name in {'ADM-policy-v2-stale','ADM-formal-v2-stale'}:
   data=json.loads(r.stdout);passed=r.returncode!=0 and not data['recorded_cycle_complete'] and not data['foundation_source_coverage_complete'];detail={'stale_policy_evidence_rejected':passed}
  elif passed and name in {'ADM-source-steps','ADM-formal-cycle'}:
   data=json.loads(r.stdout);passed=data['recorded_cycle_complete'] and data['foundation_source_coverage_complete'];detail={'fictional_record_coverage':passed,'real_business_approval':'not-granted'}
  elif passed and name=='doctor':passed=json.loads(r.stdout)['passed']
  elif passed and name in {'query','Chinese-body-query','G226-Chinese-body-query'}:
   data=json.loads(r.stdout);matches=data['matches'];passed=bool(matches) and all(x['resolved_source']['exists'] for x in matches)
   if name in {'Chinese-body-query','G226-Chinese-body-query'}:passed=passed and any(x['content_role']=='current-source-bound-Chinese-body' for x in matches)
   detail={'match_count':len(matches),'resolved_sources_exist':all(x['resolved_source']['exists'] for x in matches)}
  elif passed and name=='validate':passed=json.loads(r.stdout)['errors']==0 and json.loads(r.stdout)['warnings']==0
  elif passed and name=='generate-render':passed=(target/'work/output/artifacts/role-assignment.png').is_file() and (target/'work/output/artifacts/role-assignment.svg').is_file()
  elif passed and name=='ADM-formal-generate':
   manifest=json.loads((target/'work/adm-delivery/manifest.json').read_text());deliveries=manifest['deliverables']
   passed=len(deliveries)==23 and all((target/'work/adm-delivery'/row[key]).is_file() for row in deliveries for key in ['path','json'])
   for row in deliveries:
    payload=json.loads((target/'work/adm-delivery'/row['json']).read_text())
    passed=passed and payload['deliverable']['approval_status']=='candidate' and payload['assembly']['content_status']=='all-sections-bound-business-review-pending'
   detail={'actual_deliverables':len(deliveries),'candidate_status_preserved':passed,'independent_business_acceptance':False}
  elif passed and name=='ADM-flow':
   manifest=json.loads((target/'work/adm-flow/manifest.json').read_text())
   coverage=json.loads((target/'work/adm-flow/coverage.json').read_text())
   diagrams=coverage['diagram_ids']
   passed=len(diagrams)==13 and (target/'work/adm-flow/index.html').is_file()
   passed=passed and all((target/'work/adm-flow'/(did+suffix)).is_file() for did in diagrams for suffix in ['.svg','.png','.mmd'])
   passed=passed and all(sha(target/'work/adm-flow'/name)==expected for name,expected in manifest['output_sha256'].items())
   detail={'actual_diagrams':len(diagrams),'offline_reader_present':passed,'approval_granted':False}
  elif passed and name=='policy':passed=json.loads(r.stdout)['passed']
  checks.append({'id':name,'passed':passed,'returncode':r.returncode,**detail,'output':r.stdout[-6000:],'stderr':r.stderr[-2000:]})
 standards_driver=target/'standards-isolation-driver.py'
 standards_driver.write_text(RUNNER.replace("scripts/local_tool.py", "scripts/standards.py"))
 for language,version,fixture in [('bpmn','2.0.2','order-collaboration.bpmn'),('uml','2.5.1','order-domain.uml')]:
  destination='work/native-'+language+'/order.svg'
  argv=['render','--language',language,'--version',version,'--input','_shared/examples/native-modeling/'+fixture,'--out',destination]
  r=subprocess.run([sys.executable,'-B',str(standards_driver),str(target),str(C.parent)]+argv,cwd=target,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':''})
  sidecar=target/Path(destination).with_suffix('.render.json')
  data=json.loads(sidecar.read_text()) if sidecar.is_file() else {}
  passed=r.returncode==0 and (target/destination).is_file() and (target/Path(destination).with_suffix('.png')).is_file() and data.get('full_language_acceptance') is False
  checks.append({'id':'native-'+language+'-render','passed':passed,'returncode':r.returncode,'full_language_acceptance':False,'output':r.stdout[-6000:],'stderr':r.stderr[-2000:]})
 negative=target/'isolation-negative.py';negative.write_text(RUNNER.replace("runpy.run_path(str(script),run_name='__main__')","open(original/'togaf-standard-10th-ai/skills/_shared/capabilities.json').read()"));r=subprocess.run([sys.executable,'-B',str(negative),str(target),str(C.parent)],cwd=target,capture_output=True,text=True);checks.append({'id':'original-project-read-rejected','passed':r.returncode!=0 and 'Relocation forbids original project access' in r.stderr,'returncode':r.returncode,'stderr':r.stderr[-1500:]})
 report={'schema_version':'portable-runtime-verification/3','passed':all(x['passed'] for x in checks),'counts':{'checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)},'relocated_directory':os.path.relpath(target,C),'source':'actual sealed archives, not copied working files','checks':checks,'environment':{'python':sys.version.split()[0],'node':subprocess.run(['node','--version'],capture_output=True,text=True).stdout.strip(),'platform':sys.platform,'browser':'existing local Chrome/Chromium; not downloaded'},'boundary_zh':'Python审计拒绝原项目读取；Node渲染使用归档解压后本地模块和资源。本次未提供内核级子进程文件访问隔离或跨平台认证。','input_sha256':{Path(os.path.relpath(release_root/'release-manifest.json',C)).as_posix():sha(release_root/'release-manifest.json'),'skills/package-manifest.json':sha(C/'skills/package-manifest.json')},'real_business_approval':'not-granted'}
 report_path.parent.mkdir(parents=True,exist_ok=True)
 report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts']);print([x for x in checks if not x['passed']]);return int(not report['passed'])
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--release-dir',type=Path);parser.add_argument('--run-dir',type=Path);parser.add_argument('--out',type=Path)
 args=parser.parse_args()
 raise SystemExit(main(args.release_dir,args.run_dir,args.out))
