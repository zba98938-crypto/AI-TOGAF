#!/usr/bin/env python3
"""Offline closure checks and explicitly bounded native campaign, preserving evidence."""
import argparse,hashlib,json,os,subprocess,sys,time,traceback
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SHARED=ROOT/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0,str(SHARED/'scripts'));sys.path.insert(0,str(ROOT/'tests'))
from enterprise.runtime import Blocked,save
from enterprise.campaign import CampaignBudget
from enterprise.cases import inventory,agent_cases
from enterprise.closure_cases import cases as closure_cases
from enterprise.frozen_runtime import hashes
from strict_json import load

def execute(args):
    out=args.out.resolve()
    if out.exists() and not args.resume:raise ValueError('--out must be new; existing evidence immutable')
    if args.resume and not out.is_dir():raise ValueError('resume requires original campaign directory')
    out.mkdir(parents=True,exist_ok=True)
    revision=hashes(ROOT/'togaf-standard-10th-ai/skills',('.venv','node_modules','__pycache__','.DS_Store'))
    revision.update({'tests/'+k:v for k,v in hashes(ROOT/'tests',('__pycache__',)).items()})
    revision_hash=hashlib.sha256(json.dumps(revision,sort_keys=True).encode()).hexdigest()
    if args.resume and (out/'source-sha256.json').is_file() and load(out/'source-sha256.json')!=revision:raise Blocked('revision changed: frozen-source results cannot count as current coverage; retain ledger and create an explicit new revision campaign')
    save(out/'source-sha256.json',revision)
    specs=inventory();native_cases=closure_cases()+agent_cases();save(out/'coverage-inventory.json',{'existing':specs,'native_case_count':len(native_cases),'native_cases':[{'id':c['id'],'kind':c['kind'],'target':c['target'],'owner':c['owner']} for c in native_cases],'full_language_normative_constructs':'tracked separately; not deemed covered by these business cases'})
    rows=[]
    def record(name,fn):
        started=time.monotonic()
        try:
            result=fn();row={'name':name,'status':result.get('status','pass'),'detail':result}
        except Exception as exc:row={'name':name,'status':'blocked' if isinstance(exc,Blocked) else 'fail','error':str(exc),'traceback':traceback.format_exc()}
        row['seconds']=round(time.monotonic()-started,3);rows.append(row);save(out/'offline-results.json',rows);print(json.dumps({k:v for k,v in row.items() if k!='detail'},ensure_ascii=False),flush=True);return row
    def unit_tests():
        discovery='import sys,unittest;s=unittest.defaultTestLoader.discover(sys.argv[1]);n=s.countTestCases();print("discovered tests:",n);sys.exit(3 if not n else int(not unittest.TextTestRunner(verbosity=2).run(s).wasSuccessful()))'
        result=subprocess.run([sys.executable,'-c',discovery,str(ROOT/'tests')],capture_output=True,text=True,timeout=300)
        (out/'unit-tests.log').write_text(result.stdout+result.stderr)
        return {'status':'pass' if result.returncode==0 else 'fail','exit_code':result.returncode}
    record('regression-and-independent-negative-tests',unit_tests)
    def simulation():
        from validate import validate
        from closure_simulator import replay
        model=load(args.model);issues=validate(model);scenarios={'happy':{'restore_valid':True,'restore_result':'success','consistent':True,'settlement_result':'confirmed'},'invalid-restore':{'restore_valid':False},'restore-failure':{'restore_valid':True,'restore_result':'failure'},'inconsistent':{'restore_valid':True,'restore_result':'success','consistent':False},'irreversible-failure':{'restore_valid':True,'restore_result':'success','consistent':True,'settlement_result':'failure'}}
        results={name:replay(model,'closure-rollback',observation) for name,observation in scenarios.items()};save(out/'symbolic-replay.json',results);save(out/'model-validation.json',issues)
        return {'status':'fail' if any(i['level']=='error' for i in issues) else 'pass','entities':len(model['entities']),'relationships':len(model['relationships']),'warnings':sum(i['level']=='warning' for i in issues),'symbolic_paths':len(results),'production_proof':False}
    record('enterprise-model-and-guarded-paths',simulation)
    def source_and_language():
        from closure_source_coverage import ledger
        from standards import catalog
        from reference_models import catalog as references
        source=ledger();save(out/'source-coverage.json',source)
        catalogs={lang:catalog(lang,version) for lang,version in [('bpmn','2.0.2'),('uml','2.5.1'),('archimate','4')]};save(out/'language-coverage.json',catalogs);save(out/'reference-coverage.json',references())
        return {'status':'pass','source_registry_evaluated':True,'strict_language_conformance':'incomplete','official_reference_model_sources':'blocked','source_verified_count':sum(p['source_verified'] for p in source['profiles']),'profile_count':source['profile_count'],'automatic_verified_flip':False}
    record('source-and-native-coverage-ledgers',source_and_language)
    all_pass=all(r['status']=='pass' for r in rows)
    native_result={'status':'not-dispatched','rows':[],'case_count':len(native_cases),'reason':'native explicitly disabled'}
    if args.native and all_pass:
        old=load(out/'campaign-ledger.json') if args.resume and (out/'campaign-ledger.json').is_file() else None
        budget=CampaignBudget(out,old);budget.start_heartbeat()
        try:
            from enterprise.closure_campaign import coordinate
            native_result=coordinate(out,budget,specs['skills'],native_cases,args.runtime_root,args.case_limit,args.resume)
        finally:
            budget.close();native_result['budget']=budget.state()
    elif args.native:native_result['reason']='offline regression failed; native dispatch forbidden'
    save(out/'native-results.json',native_result)
    summary={'source_revision_sha256':revision_hash,'offline_status':'pass' if all_pass else 'fail','native_status':native_result['status'],'native_case_count':len(native_cases),'native_passes':sum(r['status']=='pass' for r in native_result['rows']),'strict_language_conformance':'incomplete','source_acceptance':'pending','human_signoff':'pending','implementation_not_all_complete':True}
    save(out/'summary.json',summary)
    if revision!= {**hashes(ROOT/'togaf-standard-10th-ai/skills',('.venv','node_modules','__pycache__','.DS_Store')),**{'tests/'+k:v for k,v in hashes(ROOT/'tests',('__pycache__',)).items()}}:raise ValueError('source changed during frozen-version verification')
    seal={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob('*') if p.is_file() and p.name!='evidence-sha256.json'};save(out/'evidence-sha256.json',seal)
    print(json.dumps(summary,ensure_ascii=False));return 1 if not all_pass else 3 if native_result['status'] not in ('pass','not-dispatched') else 0

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--model',type=Path,required=True);p.add_argument('--native',action='store_true');p.add_argument('--runtime-root',type=Path);p.add_argument('--case-limit',type=int,default=0,help='initial directed subset; remaining cases explicitly uncovered');p.add_argument('--resume',action='store_true');a=p.parse_args()
    if a.case_limit<0:p.error('--case-limit cannot be negative')
    if a.native and not a.runtime_root:p.error('--runtime-root required for isolated native evaluation')
    try:return execute(a)
    except (ValueError,Blocked) as e:print(str(e),file=sys.stderr);return 3 if isinstance(e,Blocked) else 1
if __name__=='__main__':raise SystemExit(main())
