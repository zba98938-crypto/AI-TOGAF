"""Persistent coordinator: directed gates, staged concurrency, normal batch rollover.
The budget and attempt ledger survive resumes; failed gates cannot be bypassed.
"""
from pathlib import Path
from .runtime import Blocked,save
from .campaign import BatchExhausted

def coordinate(out,budget,skills,cases,runtime_root,limit=0,resume=False,runtime_factory=None,runner=None):
    if runtime_factory is None:
        from .agents import NativeAgents,run_cases
        runtime_factory=NativeAgents;runner=run_cases
    out=Path(out);result_path=out/'native-progress.json'
    import json
    previous=json.loads(result_path.read_text()) if resume and result_path.is_file() else {}
    attempts=list(previous.get('attempts',[]));latest={r['id']:r for r in previous.get('rows',[]) if r['status']!='uncovered'}
    workers=previous.get('workers',1);chosen=cases[:limit] if limit else cases
    runtime=None;status='partial';reason=None
    def persist():
        save(result_path,{'attempts':attempts,'rows':list(latest.values()),'workers':workers,'case_count':len(cases)})
    try:
        if any(r['status'] in ('fail','needs_review') for r in latest.values()):raise Blocked('previous directed/quality failure requires repair; resume cannot bypass it')
        while True:
            remaining=[c for c in chosen if latest.get(c['id'],{}).get('status')!='pass']
            if not remaining:break
            if budget.batch_state!='active':budget.begin_batch()
            else:
                try:budget.begin_batch(resume=True)
                except BatchExhausted:
                    budget.seal_batch('normal resumed batch boundary');continue
            budget.phase='runtime-preflight'
            runtime=runtime_factory(out/('agents-%d-attempt-%d'%(budget.batch,len(attempts))),budget,skills,runtime_root=runtime_root)
            preflight=runtime.preflight();save(out/('native-preflight-%d-%d.json'%(budget.batch,len(attempts))),preflight)
            budget.phase='business-cases'
            try:
                while remaining:
                    budget.check()
                    # Only first three independently authored cases are admission gates.
                    directed=[c for c in chosen[:3] if latest.get(c['id'],{}).get('status')!='pass']
                    block=directed[:1] if directed else remaining[:16]
                    concurrency=1 if directed else workers
                    result=runner(runtime,block,workers=concurrency)
                    attempts.append({'batch':budget.batch,'concurrency':concurrency,'result':result})
                    for row in result['rows']:
                        if row['status']!='uncovered':latest[row['id']]=row
                    persist()
                    if result.get('stop_type')=='BatchExhausted':raise BatchExhausted(result['stop_reason'])
                    if result['status']!='pass':raise Blocked('business/independent scoring gate did not pass; stop wider dispatch')
                    if not directed and workers==2:workers=4
                    elif directed and all(latest.get(c['id'],{}).get('status')=='pass' for c in chosen[:3]):workers=2
                    remaining=[c for c in chosen if latest.get(c['id'],{}).get('status')!='pass']
                    persist()
                break
            except BatchExhausted as exc:
                runtime.close();runtime=None
                budget.seal_batch(str(exc));persist()
                # A timeout/429/isolation trip is not a normal batch boundary.
                budget.check();continue
        if budget.batch_state=='active':budget.seal_batch('selected cases completed')
        status='pass' if len(chosen)==len(cases) else 'partial'
    except Exception as exc:
        status='blocked';reason=str(exc)
        if 'isolation' in reason or 'preflight failed' in reason:budget.trip('isolation/toolchain failure: '+reason)
    except KeyboardInterrupt:
        status='blocked';reason='interrupted; budget clocks and attempts retained'
    finally:
        if runtime:runtime.close()
        persist()
    rows=[latest.get(c['id'],{'id':c['id'],'kind':c['kind'],'owner':c['owner'],'target':c['target'],'status':'uncovered','reason':'not independently completed in retained campaign'}) for c in cases]
    return {'status':status,'reason':reason,'rows':rows,'attempts':attempts,'case_count':len(cases),'workers':workers}
