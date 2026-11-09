#!/usr/bin/env python3
"""All isolated toolchain probes, no model/business calls or budget reset."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tests'))
from enterprise.agents import NativeAgents,sandbox_argv
from enterprise.runtime import Budget,Blocked,save,sha256

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--runtime-root',type=Path,required=True);a=p.parse_args()
 out=a.out.resolve()
 if out.exists():p.error('--out must be new; prior failure evidence is immutable')
 out.mkdir(parents=True);b=Budget(out,max_hours=.5,max_sessions=0);r=None
 try:
  names=sorted(p.name for p in (ROOT/'togaf-standard-10th-ai/skills').iterdir() if (p/'SKILL.md').is_file())
  r=NativeAgents(out/'runtime',b,names,runtime_root=a.runtime_root)
  root=r.workspace('toolchain',True);(root/'.tmp').mkdir()
  result=r.toolchain_preflight(root,sandbox_argv(r.codex,root),{**r.env,'TMPDIR':str(root/'.tmp')},collect_all=True)
 except Exception as e:
  detail=out/'runtime/toolchain-preflight.json'
  result=json.loads(detail.read_text()) if detail.exists() else {'status':'blocked' if isinstance(e,Blocked) else 'fail','probes':{}}
  result['reason']=str(e);result['status']='blocked' if isinstance(e,Blocked) else 'fail'
 finally:
  if r:r.close()
 result.update(model_sessions=len(b.sessions),model_requests_observed=r.relay.requests if r else 0,diagnostic_only=True,business_dispatch_authorized=False,runtime_manifest_sha256=sha256(a.runtime_root/'runtime-manifest.json'),budget=b.snapshot())
 save(out/'summary.json',result)
 save(out/'evidence-sha256.json',{str(p.relative_to(out)):sha256(p) for p in out.rglob('*') if p.is_file() and p.name!='evidence-sha256.json'})
 print(json.dumps({k:result[k] for k in ('status','model_sessions','model_requests_observed')},ensure_ascii=False));return 0 if result['status']=='pass' else 3
if __name__=='__main__':raise SystemExit(main())
