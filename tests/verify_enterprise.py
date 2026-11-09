#!/usr/bin/env python3
"""Run a fresh, retained-evidence generic enterprise skills campaign.

0 = all mandatory requested coverage passed; 1 = defect; 2 = bad arguments;
3 = prerequisites, budget, review or coverage remain incomplete.
Quick runs validate this harness only, never certify full enterprise coverage.
"""
import argparse
import concurrent.futures
import json
import math
import os
import platform
import signal
import subprocess
import sys
import threading
import time
import traceback
from pathlib import Path
from enterprise.runtime import Blocked, Budget, run_command, save, sha256, tree_hashes
from enterprise.cases import REPO, SHARED, agent_cases, inventory, profile_mutations
from enterprise.data import audit, build, derive, dirty_copy, replay
from enterprise.stress import Workload, burst, browser_drill, failure_drills, shape_worker, shapes, sustained


def fingerprint():
    return {folder:tree_hashes(REPO/folder) for folder in ('togaf-standard-10th-ai/skills','tests')}


def environment():
    rows = {'python':sys.version,'platform':platform.platform(),'cpus':os.cpu_count(),
            'sqlite':__import__('sqlite3').sqlite_version}
    for name,argv in (('node',['node','--version']),('codex',['codex','--version'])):
        try:
            rows[name] = subprocess.check_output(argv,text=True,timeout=10).strip()
        except (OSError,subprocess.SubprocessError) as exc:
            rows[name] = {'blocked':str(exc)}
    rows['dependencies'] = {str(p.relative_to(REPO)):sha256(p) for p in (
        SHARED/'package-lock.json',SHARED/'requirements.txt') if p.is_file()}
    return rows


def report(out,rows,coverage,budget,args,before,after):
    changed = [folder+'/'+name for folder in before for name in before[folder].keys()|after[folder].keys()
               if before[folder].get(name)!=after[folder].get(name)]
    failed = [r['name'] for r in rows if r['status']=='fail']
    blocked = [r['name'] for r in rows if r['status'] not in ('pass','fail')]
    if changed:
        failed.append('source-integrity')
    status = 'fail' if failed else 'blocked' if blocked else 'pass'
    agent_rows = next((r.get('detail',{}).get('rows',[]) for r in rows if r['name']=='real-agents'),[])
    if not agent_rows:
        agent_rows = [{'id':c['id'],'owner':c['owner'],'kind':c['kind'],'status':'uncovered'} for c in agent_cases()]
    mutations = next((r.get('detail',{}).get('rows',[]) for r in rows if r['name']=='profile-mutations'),[])
    matrix = []
    for skill in coverage['skills']:
        actual = [r for r in agent_rows if r.get('owner')==skill]
        engineering = [r for r in mutations if r.get('owner')==skill]
        matrix.append({'skill':skill,'engineering':{s:sum(r['status']==s for r in engineering) for s in ('pass','fail','blocked')},
                       'real_agent':{s:sum(r['status']==s for r in actual) for s in ('pass','fail','blocked','needs_review','uncovered')},
                       'real_agent_expected':sum(c['owner']==skill for c in agent_cases()),
                       'scope':'Engineering generation != actual agent routing/reasoning != professional approval'})
    defects = []
    for row in mutations:
        if row['status']=='fail':
            defects.append({'id':'engineering-'+row['profile_id'],'severity':'untriaged',
                            'status':'reproducible-test-failure-pending-triage','actual':row.get('error'),
                            'reproduction':row.get('reproduction'),'skill':row['owner']})
    for row in agent_rows:
        for n,defect in enumerate(row.get('score',{}).get('defects',[])):
            defects.append({'id':row['id']+'-'+str(n),'severity':'untriaged','status':'independent-review-finding-not-yet-confirmed',
                            'skill':row.get('owner'),**defect})
    summary = {'schema_version':'skills-enterprise-regression/1','status':status,
               'scope':'harness-validation-only' if args.quick else 'formal-enterprise-campaign',
               'campaign':args.campaign,'parent_evidence':str(args.baseline) if args.baseline else None,
               'continuation_of':str(args.continue_campaign) if args.continue_campaign else None,
               'master_seed':20261105,'requested_scales':args.scales,'render_requested':args.render,'coverage_inventory':coverage,
               'budget':budget.snapshot(),'results':rows,'failures':failed,'blocked_or_uncovered':blocked,
               'source_changed':sorted(changed),'agent_case_count':len(agent_cases()),
               'limits':['No business approval, actual realized benefit, TOGAF source-equivalence certification or production availability claim.',
                         'Transaction volume is evidence/workload, not diagram-node count or raw prompt size.',
                         'Offline SQLite capacity is not ERP OLTP capacity.',
                         'Needs-review, missing prerequisites and unexecuted stages never count as passes.',
                         'A quick run is not the requested 1M/3M/10M formal campaign.']}
    save(out/'source-after.json',after)
    save(out/'summary.json',summary)
    save(out/'skill-coverage.json',matrix)
    save(out/'defects.json',defects)
    lines = ['# 企业级 skills 能力与压力测试报告','',
             '**状态：'+status+'**；范围：'+summary['scope']+'；轮次：'+args.campaign+'。',
             '', '本次证据独立生成，原始数据库、SQL、哈希、日志与实际成果均保存在本目录。',
             '未覆盖、预算阻断及待人工复核不算通过；性能结果不代表生产ERP容量或专业批准。','',
             '## 预算','',json.dumps(budget.snapshot(),ensure_ascii=False),'',
             '## 阶段结果','','| 阶段 | 状态 | 秒 |','|---|---|---:|']
    lines.extend('| '+r['name']+' | '+r['status']+' | '+str(r.get('seconds',''))+' |' for r in rows)
    lines += ['', '## 按技能覆盖','','| 技能 | 工程通过/失败/阻断 | Agent通过/失败/待复核/未覆盖 |','|---|---|---|']
    for row in matrix:
        e,a = row['engineering'],row['real_agent']
        lines.append('| '+row['skill']+' | '+str(e['pass'])+'/'+str(e['fail'])+'/'+str(e['blocked'])+' | '+
                     '/'.join(str(a[k]) for k in ('pass','fail','needs_review','uncovered'))+' |')
    lines += ['', '## 缺陷与后续修复','',
              '已记录 '+str(len(defects))+' 条工程失败或独立评审发现。独立评审意见须经最小复现确认后才进入修复。',
              '首轮证据不改写。修复后必须使用新的 `--out` 和 `--campaign post-fix --baseline <首轮目录>`；',
              '复测有独立4小时/1,000会话预算，不能以针对性单测代替正式完整复测。','',
              '## 证据索引','',
              '- `summary.json` / `progress.jsonl`：执行结果与阶段进度',
              '- `source-before.json` / `source-after.json` / `environment.json`：源码与运行依赖指纹',
              '- `datasets/`：原始SQLite、独立SQL/Decimal核算、数据污染副本、事件重放',
              '- `agents/` / `session-ledger.json`：真实Actor/独立评分上下文、JSONL工具事件、token用量',
              '- `stress/` / `resources.jsonl`：容量样本、队列、拒绝、CPU/RSS/磁盘证据',
              '- `skill-coverage.json` / `defects.json`：技能覆盖与待确认缺陷']
    (out/'REPORT.zh-CN.md').write_text('\n'.join(lines)+'\n')
    # Seal only after producing final report; raw historical evidence is never rewritten later.
    save(out/'evidence-index.json',tree_hashes(out,excluded=('__pycache__','.DS_Store')))
    return status


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path)
    parser.add_argument('--scales',type=int,nargs='+',default=[1000000,3000000,10000000])
    parser.add_argument('--max-hours',type=float,default=4)
    parser.add_argument('--max-agent-sessions',type=int,default=1000)
    parser.add_argument('--render',action='store_true')
    parser.add_argument('--quick',action='store_true',help='Harness validation only: 1000 orders, short stress; not full coverage')
    parser.add_argument('--live-agents',action='store_true',help='Include 2 real cases in quick mode (formal defaults to all)')
    parser.add_argument('--skip-agents',action='store_true',help='Explicitly leave real Agent coverage blocked')
    parser.add_argument('--agent-workers',type=int,choices=(1,2,4),default=1)
    parser.add_argument('--campaign',choices=('baseline','post-fix'),default='baseline')
    parser.add_argument('--baseline',type=Path,help='Immutable first-campaign evidence for post-fix run')
    parser.add_argument('--continue-campaign',type=Path,help='Sealed failed/blocked attempt of the SAME campaign; inherit original wall/session/output allowance')
    parser.add_argument('--shape-worker',type=Path,help=argparse.SUPPRESS)
    parser.add_argument('--shape-out',type=Path,help=argparse.SUPPRESS)
    parser.add_argument('--shape-render',action='store_true',help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.shape_worker:
        if not args.shape_out:
            parser.error('--shape-out required')
        return shape_worker(args.shape_worker,args.shape_out,render=args.shape_render)
    if not args.out:
        parser.error('--out required')
    if not math.isfinite(args.max_hours) or args.max_hours<=0 or args.max_hours>4 or args.max_agent_sessions<0 or args.max_agent_sessions>1000:
        parser.error('each campaign must use 0<hours<=4, 0<=sessions<=1000')
    if not 1<=args.agent_workers<=8 or any(s<=0 for s in args.scales) or len(set(args.scales))!=len(args.scales):
        parser.error('positive distinct scales and 1..8 Agent workers required')
    if args.live_agents and args.skip_agents:
        parser.error('--live-agents conflicts with --skip-agents')
    if args.campaign=='post-fix' and not args.baseline:
        parser.error('--baseline required for post-fix campaign')
    if args.baseline and not (args.baseline/'evidence-index.json').is_file():
        parser.error('baseline must be a sealed campaign directory')
    if args.baseline:
        parent = json.loads((args.baseline/'summary.json').read_text())
        if parent.get('campaign')!='baseline' or parent.get('scope')!='formal-enterprise-campaign':
            parser.error('post-fix parent must be a formal baseline campaign')
        sealed = json.loads((args.baseline/'evidence-index.json').read_text())
        if any(not (args.baseline/name).is_file() or sha256(args.baseline/name)!=digest for name,digest in sealed.items()):
            parser.error('baseline evidence changed after sealing')
    continuation = None
    prior_sessions = []
    prior_roots = []
    started_wall = None
    if args.continue_campaign:
        previous = args.continue_campaign.resolve()
        try:
            continuation = json.loads((previous/'summary.json').read_text())
            sealed = json.loads((previous/'evidence-index.json').read_text())
            if any(not (previous/name).is_file() or sha256(previous/name)!=digest for name,digest in sealed.items()):
                parser.error('continuation evidence changed after sealing')
            if args.quick or continuation.get('scope')!='formal-enterprise-campaign' or continuation.get('campaign')!=args.campaign:
                parser.error('continuation must use the same formal campaign, not quick mode')
            if continuation.get('status')=='pass':
                parser.error('a completed passing campaign cannot receive extra attempts')
            old_parent = continuation.get('parent_evidence')
            if (str(Path(old_parent).resolve()) if old_parent else None)!=(str(args.baseline.resolve()) if args.baseline else None):
                parser.error('continuation must preserve its original baseline parent')
            if continuation['requested_scales']!=args.scales or continuation['render_requested']!=args.render:
                parser.error('continuation cannot narrow scales or rendering coverage')
            old_budget = continuation['budget']
            if args.max_hours*3600>old_budget['max_seconds'] or args.max_agent_sessions>old_budget['max_sessions']:
                parser.error('continuation cannot expand the original campaign allowance')
            started_wall = old_budget.get('started_wall', (previous/'source-before.json').stat().st_mtime-1)
            if time.time()-started_wall>=args.max_hours*3600:
                parser.error('original campaign wall-clock allowance already exhausted')
            prior_sessions = json.loads((previous/'session-ledger.json').read_text()) if (previous/'session-ledger.json').exists() else []
            if len(prior_sessions)!=old_budget['sessions_used']:
                parser.error('continuation session ledger does not match sealed summary')
            prior_roots = [previous]+[Path(p).resolve() for p in old_budget.get('prior_output_roots',[])]
        except (OSError,ValueError,KeyError,TypeError) as exc:
            parser.error('invalid sealed continuation: '+str(exc))
    out = args.out.resolve()
    if out.exists():
        parser.error('--out must be a new directory; no historical evidence overwrite')
    if any(out.is_relative_to(REPO/p) for p in ('togaf-standard-10th-ai/skills','tests')):
        parser.error('output must be outside source directories')
    if args.quick:
        args.scales = [1000]
    if any(out==p or out.is_relative_to(p) or p.is_relative_to(out) for p in prior_roots):
        parser.error('continuation output must be disjoint from all sealed attempts')
    out.mkdir(parents=True,exist_ok=False)
    budget = Budget(out,args.max_hours,args.max_agent_sessions,started_wall=started_wall,
                    prior_sessions=prior_sessions,prior_output_roots=prior_roots)
    before = fingerprint()
    save(out/'source-before.json',before)
    save(out/'environment.json',environment())
    save(out/'arguments.json',{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()})
    coverage = inventory()
    save(out/'coverage-inventory.json',coverage)
    cases = agent_cases()
    # Rubrics frozen separately from actors; raw inputs are not expected output fixtures.
    save(out/'agent-case-manifest.json',cases)
    rows = []
    progress_lock = threading.Lock()
    agent_pool = None
    agent_future = None
    agent_runtime = None
    agent_preflight = None
    def cancel(signum,frame):
        budget.stop_reason = 'signal '+str(signum)
        budget.cancel.set()
    for signum in (signal.SIGTERM,signal.SIGINT):
        signal.signal(signum,cancel)
    def stage(name,fn):
        started = time.monotonic()
        print(json.dumps({'stage':name,'status':'running'},ensure_ascii=False),flush=True)
        try:
            budget.check()
            detail = fn()
            row = {'name':name,'status':detail.get('status','pass'),'detail':detail}
        except Blocked as exc:
            row = {'name':name,'status':'blocked','reason':str(exc)}
        except Exception as exc:
            row = {'name':name,'status':'blocked' if budget.cancel.is_set() else 'fail','error':str(exc),'traceback':traceback.format_exc()}
        row['seconds'] = round(time.monotonic()-started,3)
        with progress_lock:
            rows.append(row)
            save(out/'progress.json',rows)
            with (out/'progress.jsonl').open('a') as stream:
                stream.write(json.dumps(row,ensure_ascii=False)+'\n')
        print(json.dumps({k:v for k,v in row.items() if k not in ('detail','traceback')},ensure_ascii=False),flush=True)
        return row
    try:
        if not args.skip_agents and (not args.quick or args.live_agents):
            def preflight():
                nonlocal agent_runtime
                from enterprise.agents import NativeAgents
                agent_runtime = NativeAgents(out/'agents',budget,coverage['skills'])
                return agent_runtime.preflight()
            agent_preflight = stage('agent-runtime-preflight',preflight)
        def core():
            argv = [sys.executable,REPO/'tests/verify_core.py','--out',out/'core','--orders','1000']
            if args.quick:
                argv = [sys.executable,'-m','unittest','discover','-s',REPO/'tests','-p','test_*.py','-v']
            elif args.render:
                argv.append('--render')
            command = run_command(argv,out/'logs/core',budget,cwd='/tmp',env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},timeout=1800)
            if (out/'core/summary.json').exists():
                return {'status':json.loads((out/'core/summary.json').read_text())['status'],'command':command,'report':'core/summary.json'}
            return command
        stage('core-engineering',core)
        stage('profile-mutations',lambda:profile_mutations(out/'profile-mutations',budget,limit=3 if args.quick else None))
        databases = []
        for scale in args.scales:
            directory = out/'datasets'/str(scale)
            row = stage('dataset-'+str(scale),lambda d=directory,s=scale:build(d,s,20261105+s,budget))
            if row['status']!='pass':
                continue
            db = directory/'enterprise.sqlite'
            databases.append(db)
            stage('audit-'+str(scale),lambda d=directory,p=db:audit(p,d,budget))
            stage('projection-'+str(scale),lambda d=directory,p=db:derive(p,d,budget))
        if databases:
            primary = databases[0]
            for rate in (.001,.01,.05):
                stage('dirty-'+str(rate),lambda r=rate:dirty_copy(primary,out/'datasets'/('dirty-'+str(r)),r,budget))
            def dirty_stream():
                result = replay(out/'datasets/dirty-0.001/enterprise.sqlite',out/'datasets/dirty-replay',budget,limit=3000 if args.quick else 1000000)
                if not result['quarantined']:
                    raise AssertionError('dirty stream produced no quarantine')
                return result
            stage('dirty-event-replay',dirty_stream)
            stage('million-event-replay',lambda:replay(primary,out/'datasets/replay',budget,limit=1000 if args.quick else 1000000))
            stage('failure-recovery',lambda:failure_drills(out/'failure-recovery',primary,budget))
            stage('browser-exit-recovery',lambda:browser_drill(out/'browser-recovery',budget) if args.render else {'status':'uncovered','reason':'browser not requested'})
            if args.skip_agents or args.quick and not args.live_agents:
                stage('real-agents',lambda:{'status':'blocked','reason':'explicitly not dispatched in this scope',
                      'rows':[{'id':c['id'],'kind':c['kind'],'owner':c['owner'],'status':'uncovered'} for c in cases]})
            else:
                def real_agents():
                    from enterprise.agents import run_cases
                    if agent_preflight is None or agent_preflight['status']!='pass':
                        return {'status':'blocked','reason':'configured runtime preflight did not pass',
                                'rows':[{'id':c['id'],'kind':c['kind'],'owner':c['owner'],'status':'uncovered'} for c in cases]}
                    selected = [cases[0],next(c for c in cases if c['kind']=='adversarial')] if args.quick else cases
                    return run_cases(agent_runtime,selected,primary.parent/'facts.json',workers=args.agent_workers)
                agent_pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)
                agent_future = agent_pool.submit(stage,'real-agents',real_agents)
            stage('representative-shapes',lambda:shapes(out/'shapes',budget,[10] if args.quick else [100,1000,10000],args.render))
            work = Workload(databases[-1],out/'stress/workload',budget)
            for workers in (1,2,4,8):
                stage('concurrency-'+str(workers),lambda w=workers:sustained(work,out/'stress'/('workers-'+str(w)),budget,1 if args.quick else 480,w))
            def soak_with_replay():
                with concurrent.futures.ThreadPoolExecutor(max_workers=1) as replay_pool:
                    replay_future = replay_pool.submit(replay,primary,out/'datasets/soak-replay',budget,1000 if args.quick else 3000000,pace_seconds=2 if args.quick else 3600)
                    result = sustained(work,out/'stress/soak',budget,2 if args.quick else 3600,4)
                    result['concurrent_event_replay'] = replay_future.result()
                    return result
            stage('soak',soak_with_replay)
            measured = next((r['detail']['overall']['throughput_per_second'] for r in rows if r['name']=='concurrency-4' and r['status']=='pass'),None)
            for n in range(3):
                stage('burst-'+str(n+1),lambda i=n:burst(work,out/'stress'/('burst-'+str(i+1)),budget,1 if args.quick else 120,measured,4)
                      if measured is not None else {'status':'blocked','reason':'no successful measured baseline; do not invent throughput'})
        else:
            stage('dependent-coverage',lambda:{'status':'blocked','reason':'no retained valid enterprise dataset'})
    finally:
        if agent_pool is not None:
            agent_pool.shutdown(wait=True)
        if agent_runtime is not None:
            agent_runtime.close()
        after = fingerprint()
        status = report(out,rows,coverage,budget,args,before,after)
        print(json.dumps({'status':status,'scope':'quick' if args.quick else 'formal','report':str(out/'REPORT.zh-CN.md'),
                          'sessions_used':len(budget.sessions)},ensure_ascii=False),flush=True)
    return 1 if status=='fail' else 3 if status=='blocked' else 0


if __name__=='__main__':
    raise SystemExit(main())
