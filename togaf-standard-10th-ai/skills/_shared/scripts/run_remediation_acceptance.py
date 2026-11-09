#!/usr/bin/env python3
"""Reproduce fresh F01–F12 engineering evidence without modifying historical audits."""
import argparse,copy,datetime,hashlib,json,os,re,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[1]
sys.path.insert(0,str(ROOT/'tests'))
from runtime_provenance import fingerprints

def acceptance_fingerprints(root=ROOT):
 paths=set(root.glob('scripts/*.py'))|set(root.glob('scripts/*.mjs'))|set(root.glob('tests/*.py'))|set(root.glob('tests/*.mjs'))|set(root.glob('*.json'))
 return {str(p.relative_to(root)):sha(p) for p in sorted(paths)}

def save(path,value):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight(stages, render=True):
 """Historical replay requires its original sources, never an empty suite."""
 required=[];problems=[]
 if 'tests' in stages and not any((ROOT/'tests').glob('test_*.py')):
  problems.append({'stage':'tests','reason':'no-historical-tests-discovered','path':str(ROOT/'tests')})
 if 'full' in stages:
  required.extend([('full',ROOT/'tests/build_full_example.py')])
  if render:required.append(('full',ROOT/'tests/test_output_integrity.py'))
 if 'cases' in stages:
  required.extend([('cases',ROOT/'examples/independent-adm-delivery/chapter_materials.py'),
   ('cases',ROOT/'examples/qianlin-synthetic/case_materials.py'),
   ('cases',ROOT/'examples/qianlin-synthetic/projection/model.json'),
   ('cases',ROOT/'examples/qianlin-synthetic/dataset/relationships.json')])
  if not any((ROOT/'examples/qianlin-synthetic/dataset/context').glob('*.json')):
   problems.append({'stage':'cases','reason':'historical-context-inventory-missing'})
 if 'sources' in stages:
  required.append(('sources',ROOT/'evidence-registry.json'))
  if not (ROOT/'reviews/source-package-2026-11-02-v2/original-crops').is_dir():
   problems.append({'stage':'sources','reason':'historical-source-crops-missing'})
 if 'portable' in stages:required.append(('portable',ROOT/'tests/test_portable.py'))
 problems.extend({'stage':stage,'reason':'historical-input-missing','path':str(path)} for stage,path in required if not path.is_file())
 return problems

def run(out,stages,render=True):
 out=Path(out).resolve()
 if out.is_relative_to(ROOT):raise ValueError('Historical replay output must be outside the runtime package')
 out.mkdir(parents=True,exist_ok=False)
 missing=preflight(stages,render)
 if missing:
  save(out/'repair-summary.json',{'status':'blocked','engineering_passed':False,'missing_requirements':missing,
   'current_runner':str(REPO/'tests/verify_core.py'),'notice':'Historical replay inputs are missing; run the current core regression separately.'})
  return out
 (out/'logs').mkdir();before=fingerprints(ROOT)
 save(out/'acceptance-inputs-before.json',acceptance_fingerprints());save(out/'runtime-before.json',before);save(out/'baseline.json',{'capabilities_sha256':sha(ROOT/'capabilities.json'),'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_limit':'26 guides; C220全文缺失','stages':stages,'render':render})
 env=dict(os.environ);env['TOGAF_TEST_PORTABLE_RENDER']='1'
 results=[]
 def command(name,args,extra=None,timeout=1800):
  start=time.monotonic();proc=subprocess.run([str(x) for x in args],cwd=REPO,env={**env,**(extra or {})},capture_output=True,text=True,timeout=timeout)
  log=out/'logs'/(name+'.log');log.write_text(proc.stdout+proc.stderr)
  row={'name':name,'argv':[str(x) for x in args],'exit_code':proc.returncode,'seconds':round(time.monotonic()-start,2),'log':str(log.relative_to(out))}
  count=re.search(r'Ran (\d+) tests?',proc.stdout+proc.stderr)
  if count:
   row['test_count']=int(count.group(1))
   if not row['test_count']:row['exit_code']=1;row['reason']='empty-test-discovery'
  results.append(row);save(out/'execution-progress.json',results);print(json.dumps(row),flush=True);return row
 if 'profiles' in stages:
  command('all-profiles',[sys.executable,ROOT/'scripts/verify_artifact_profiles.py','--all','--out',out/'profiles']+(['--render'] if render else []))
  # Geometry uses actual original and modified payloads, not claimed coverage IDs.
  from registry import load
  from verify_artifact_profiles import inputs,substantive_change
  artifacts=[]
  for p in load()[2].values():
   if p.get('alias_of') or p.get('output_kind')=='table':continue
   m,v=inputs(p)
   for layout in ['reference','adaptive']:
    for variant in ['', '-modified']:
     identity=p['id']+'-'+layout+variant;payload=copy.deepcopy(m)
     if variant:substantive_change(payload,v)
     save(out/'profiles'/(identity+'.payload.json'),payload)
     artifacts.append({'view_id':identity,'svg':identity+'.svg','json':identity+'.payload.json'})
  save(out/'profiles/manifest.json',{'artifacts':artifacts})
  if render:command('profile-geometry',['node',ROOT/'scripts/check_geometry.mjs',out/'profiles'])
  command('focused-schedule',[sys.executable,ROOT/'scripts/focused_remediation_acceptance.py','--out',out/'focused-schedule']+([] if render else ['--no-render']))
  if render:
   for layout in ['reference','adaptive']:command('focused-geometry-'+layout,['node',ROOT/'scripts/check_geometry.mjs',out/'focused-schedule'/layout])
 if 'full' in stages:
  from build_full_example import build
  from generate import generate
  model,inventory=build();save(out/'full-model.json',model);save(out/'full-inventory.json',inventory)
  for layout in ['reference','adaptive']:
   manifest=generate(model,out/'full-output'/layout,all_items=True,render=render,layout=layout);print('generated full '+layout,flush=True)
   if render:command('full-geometry-'+layout,['node',ROOT/'scripts/check_geometry.mjs',out/'full-output'/layout])
  if render:command('test_output_integrity',[sys.executable,ROOT/'tests/test_output_integrity.py'],{'TOGAF_OUTPUT_CORPUS':str(out/'full-output')})
 if 'cases' in stages:
  command('scale',[sys.executable,ROOT/'scripts/verify_scale_cases.py','--out',out/'scale'])
  for case in ['lingang','qianlin']:
   command(case,[sys.executable,ROOT/'scripts/enterprise_acceptance.py','--case',case,'--out',out/'cases'/case]+([] if render else ['--no-render']))
   if render:
    for layout in ['reference','adaptive']:command(case+'-geometry-'+layout,['node',ROOT/'scripts/check_geometry.mjs',out/'cases'/case/layout])
 if 'language' in stages:
  from natural_language_acceptance import run as language
  save(out/'natural-language-summary.json',language(out/'natural-language'))
 if 'sources' in stages:
  command('source-integrity',[sys.executable,ROOT/'scripts/audit_source_integrity.py','--report',out/'source-integrity.json'])
  from source_dispositions import disposition
  from registry import load
  cap=json.loads((ROOT/'capabilities.json').read_text());reg=json.loads((ROOT/'evidence-registry.json').read_text());ps=load()[2];methods={m['id'] for m in load()[3]};rows=[]
  for f in reg['figures']:
   role=disposition(f['id'],[],ps,methods);rows.append({'id':f['id'],'route':role,'registered_profile_ids':f['profile_ids'],'unresolved':sorted(set(role['profile_ids'])-ps.keys()),'source_status_retained':f.get('source_status'),'interpretation':f['portable_structure'],'original':f['json_path'],'uncertainty':f.get('uncertainty'),'conflict_ids':f.get('conflict_ids'),'source_verified':{pid:ps[pid].get('template',{}).get('source_verified',False) for pid in role['profile_ids']}})
  save(out/'source-routes.json',{'entry_count':len(rows),'entries':rows,'limit':'243入口逐项可达性和覆盖状态复核；不授予语义批准，不批量设置source_verified。详细目视范围另列画廊。'})
 if 'portable' in stages:command('portable',[sys.executable,ROOT/'tests/test_portable.py','--out',out/'portable'],timeout=1800)
 if 'full' in stages:
  command('source-verification-index',[sys.executable,ROOT/'scripts/classify_source_verification.py','--write-evidence'])
  command('profile-review-index',[sys.executable,ROOT/'scripts/build_visual_review_records.py','--write','--output-root',out/'full-output'])
 if 'tests' in stages:
  paths=sorted(p for p in (ROOT/'tests').glob('test_*.py') if p.name not in {'test_portable.py','test_output_integrity.py'})
  for p in paths:command(p.stem,[sys.executable,p],timeout=600)
  suites=[r for r in results if r['name'].startswith('test_')];save(out/'unittest-results.json',{'suite_count':len(suites),'suite_failures':sum(r['exit_code']!=0 for r in suites),'tests_executed':sum(r.get('test_count',0) for r in suites),'suites':suites})
 snapshot_before=json.loads((out/'acceptance-inputs-before.json').read_text());snapshot_after=acceptance_fingerprints();save(out/'acceptance-inputs-after.json',snapshot_after)
 after=fingerprints(ROOT);save(out/'runtime-after.json',after);save(out/'execution-summary.json',{'runs':results,'all_commands_succeeded':all(r['exit_code']==0 for r in results),'runtime_stable':before==after,'source_snapshot_stable':snapshot_before==snapshot_after,'changed_paths':[k for k in before.keys()|after.keys() if before.get(k)!=after.get(k)],'rendered':render,'business_acceptance':'not-assessed','professional_review':'pending-professional-review'})
 from build_remediation_report import build as report
 report(out)
 return out

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',required=True);p.add_argument('--stages',nargs='+',choices=['tests','profiles','full','cases','language','sources','portable'],default=['tests','profiles','full','cases','language','sources','portable']);p.add_argument('--no-render',action='store_true');a=p.parse_args();destination=run(a.out,a.stages,not a.no_render);print(destination)
 result=json.loads((destination/'repair-summary.json').read_text())
 sys.exit(3 if result.get('status')=='blocked' else 0 if result['engineering_passed'] else 1)
