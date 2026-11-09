"""Bounded mixed workloads, backpressure, scale shapes and owned failure drills."""
import concurrent.futures
import copy
import json
import os
import queue
import shutil
import sqlite3
import sys
import tempfile
import threading
import time
import math
import struct
import xml.etree.ElementTree as ET
from pathlib import Path
from .cases import REPO, SHARED
from .data import FACT_SQL, connect, replay
from .runtime import Blocked, metrics, run_command, save, sha256


class Workload:
    def __init__(self,db,directory,budget):
        from registry import load
        from profile_examples import normalize_example
        self.db = Path(db)
        self.directory = Path(directory)
        self.directory.mkdir(parents=True,exist_ok=True)
        self.budget = budget
        self.model = normalize_example(load()[2]['trust-framework-default'])
        self.counter = 0
        self.lock = threading.Lock()
        self.expected = None
        with connect(db) as connection:
            self.expected = connection.execute('SELECT count(*),sum(quantity) FROM orders').fetchone()

    def __call__(self,kind):
        from validate import validate
        from generate import generate
        from analyze import evaluate
        from architecture_delivery import output_check
        started = time.monotonic()
        row = {'kind':kind,'status':'pass'}
        with self.lock:
            sequence = self.counter
            self.counter += 1
        try:
            self.budget.check()
            if kind=='sql':
                connection = connect(self.db)
                connection.set_progress_handler(lambda: 1 if self.budget.cancel.is_set() or time.monotonic()>=self.budget.dispatch_deadline else 0,100000)
                try:
                    actual = connection.execute('SELECT count(*),sum(quantity) FROM orders').fetchone()
                finally:
                    connection.close()
                if actual!=self.expected:
                    raise AssertionError('concurrent SQL totals changed')
                row['result'] = list(actual)
            elif kind=='validate-analyze':
                errors = [r for r in validate(self.model) if r['level']=='error']
                if errors:
                    raise AssertionError(str(errors))
                result = evaluate({'id':'stress-risk','method_id':'risk-explicit-rule','inputs':{
                    'formula':'likelihood-times-impact','rule_evidence':['explicit-synthetic-rule'],
                    'likelihood':{'value':2,'scale':'project-1-5','evidence':['explicit-synthetic-rule']},
                    'impact':{'value':4,'scale':'project-1-5','evidence':['explicit-synthetic-rule']}}})
                if result['result']['inherent_risk']!=8:
                    raise AssertionError('stress calculator oracle mismatch')
                row['result'] = 8
            else:
                # Retain early actual outputs; disposable capacity iterations are explicitly marked.
                retain = sequence<16
                destination = self.directory / ('sample-'+str(sequence)) if retain else Path(tempfile.mkdtemp(prefix='stress-scratch-',dir=str(self.directory)))
                try:
                    manifest = generate(self.model,destination,all_items=True,strict=True)
                    _, errors = output_check(destination,self.model)
                    if errors:
                        raise AssertionError(str(errors))
                    row['output_sha256'] = manifest['output_sha256']
                    row['actual_outputs_retained'] = retain
                finally:
                    if not retain:
                        shutil.rmtree(destination)
        except Blocked as exc:
            row.update(status='blocked',error=str(exc))
        except Exception as exc:
            row.update(status='fail',error=str(exc))
        row.update(sequence=sequence,seconds=round(time.monotonic()-started,6))
        return row


def sustained(work,directory,budget,seconds,workers):
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    started = time.monotonic()
    samples = []
    cycle = ('sql','sql','validate-analyze','generate')
    pending = {}
    dispatched = 0
    blocked = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool, (directory / 'samples.jsonl').open('w') as stream:
        while pending or time.monotonic()-started<seconds:
            try:
                budget.check()
                while len(pending)<workers and time.monotonic()-started<seconds:
                    kind = cycle[dispatched%4]
                    pending[pool.submit(work,kind)] = kind
                    dispatched += 1
            except Blocked:
                blocked = True
            if not pending:
                break
            completed,_ = concurrent.futures.wait(pending,timeout=.5,return_when=concurrent.futures.FIRST_COMPLETED)
            for future in completed:
                pending.pop(future)
                row = future.result()
                samples.append(row)
                stream.write(json.dumps(row,ensure_ascii=False)+'\n')
                if row['status']=='blocked':
                    blocked = True
            stream.flush()
            if blocked:
                for future in pending:
                    row = future.result()
                    samples.append(row)
                    stream.write(json.dumps(row,ensure_ascii=False)+'\n')
                break
    elapsed = time.monotonic()-started
    result = {'status':'fail' if any(r['status']=='fail' for r in samples) else 'blocked' if blocked or elapsed<seconds else 'pass',
              'workers':workers,'requested_seconds':seconds,'mix':{'sql':.5,'validate-analyze':.25,'generate':.25},
              'overall':metrics(samples,elapsed),
              'by_kind':{kind:metrics([s for s in samples if s['kind']==kind],elapsed) for kind in cycle},
              'limits':['Capacity samples are not professional semantic verification. Disposable generation iterations retain hashes, not every file.']}
    save(directory / 'summary.json',result)
    return result


def burst(work,directory,budget,seconds,baseline,workers=4,queue_cap=10000):
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    jobs = queue.Queue(maxsize=queue_cap)
    samples = []
    lock = threading.Lock()
    stopped = threading.Event()
    started = time.monotonic()
    rejected = 0
    peak = 0
    arrivals = 0
    target_rate = max(.1,baseline*10)
    def consumer():
        while not stopped.is_set() or not jobs.empty():
            try:
                kind = jobs.get(timeout=.1)
            except queue.Empty:
                continue
            row = work(kind)
            with lock:
                samples.append(row)
            jobs.task_done()
    threads = [threading.Thread(target=consumer,daemon=True) for _ in range(workers)]
    for thread in threads:
        thread.start()
    blocked = False
    try:
        while time.monotonic()-started<seconds:
            budget.check()
            due = int((time.monotonic()-started)*target_rate)
            while arrivals<due:
                kind = ('sql','sql','validate-analyze','generate')[arrivals%4]
                try:
                    jobs.put_nowait(kind)
                    peak = max(peak,jobs.qsize())
                except queue.Full:
                    rejected += 1
                arrivals += 1
            time.sleep(.01)
    except Blocked:
        blocked = True
    finally:
        stopped.set()
        # Do not drain an unbounded backlog after a burst or exceed its campaign budget.
        while True:
            try:
                jobs.get_nowait()
                jobs.task_done()
                rejected += 1
            except queue.Empty:
                break
        for thread in threads:
            thread.join()
    if len(samples)+rejected!=arrivals:
        raise AssertionError('burst queue silently lost jobs')
    save(directory / 'samples.json',samples)
    result = {'status':'fail' if any(r['status']=='fail' for r in samples) else 'blocked' if blocked else 'pass',
              'requested_seconds':seconds,'baseline_throughput':baseline,'target_arrivals_per_second':target_rate,
              'arrivals':arrivals,'queue_cap':queue_cap,'accounting':'arrivals = completed attempts + explicitly rejected/cancelled',
              **metrics(samples,time.monotonic()-started,rejected,peak)}
    save(directory / 'summary.json',result)
    return result


def shape_input(profile,objects):
    from profile_examples import normalize_example
    model = normalize_example(profile)
    if not model['entities']:
        raise Blocked('representative profile has no raw entity')
    base = copy.deepcopy(model['entities'][0])
    original_count = len(model['entities'])
    for n in range(max(0,objects-original_count)):
        entity = copy.deepcopy(base)
        entity['id'] = 'scale-object-'+str(n)
        entity['name'] = '制造集团规模对象-'+str(n)
        model['entities'].append(entity)
        model['views'][0]['entity_ids'].append(entity['id'])
    return model


def mermaid_shape_result(directory,objects,command,report):
    reason = report.get('reason','')
    if report.get('status')=='blocked' or 'enterprise-raster-capacity:' in reason:
        return {'status':'blocked','reason':reason}
    if command.get('status')!='pass' or report.get('status')!='passed':
        return {'status':command.get('status','fail') if command.get('status')!='pass' else 'fail',
                'reason':reason or 'no passed Mermaid render report'}
    directory = Path(directory)
    try:
        root = ET.parse(directory/'diagram.svg').getroot()
        nodes = sum(e.tag.rsplit('}',1)[-1]=='g' and 'node' in e.get('class','').split() for e in root.iter())
        edges = sum(e.tag.rsplit('}',1)[-1]=='path' and 'flowchart-link' in e.get('class','').split() for e in root.iter())
        if not (directory/'diagram.png').is_file():
            raise ValueError('missing actual Mermaid PNG')
        # The capacity fixture is a chain: an error placeholder or incomplete
        # projection must never pass just because the renderer exited zero.
        if nodes!=objects or edges!=objects-1:
            return {'status':'fail','reason':'rendered Mermaid chain does not express requested nodes/edges',
                    'expected_nodes':objects,'actual_nodes':nodes,'expected_edges':objects-1,'actual_edges':edges}
        return {'status':'pass','actual_nodes':nodes,'actual_edges':edges}
    except (OSError,ValueError,ET.ParseError) as exc:
        return {'status':'fail','reason':'invalid actual Mermaid evidence: '+str(exc)}


def shapes(directory,budget,sizes,render=False):
    from registry import load
    from profile_examples import normalize_example
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    profiles = load()[2]
    selected = {'network':'trust-framework-default', 'matrix':'architecture-maturity-model-default',
                'roadmap':'risk-mitigation-plan-default',
                'catalogue':'compat-application-portfolio-catalog'}
    rows = []
    for family,pid in selected.items():
        for size in sizes:
            budget.check()
            dest = directory / (family+'-'+str(size))
            dest.mkdir()
            model = shape_input(profiles[pid],size)
            save(dest / 'model.json',model)
            row = {'family':family,'objects':len(model['entities']),'requested_objects':size,'profile_id':pid}
            try:
                command = [sys.executable,REPO/'tests/verify_enterprise.py',
                    '--shape-worker',dest/'model.json','--shape-out',dest/'generated']
                if render:
                    command.append('--shape-render')
                row['command'] = run_command(command,dest/'logs',budget,cwd='/tmp',timeout=180)
                if row['command']['exit_code']!=0 and not (dest/'generated/shape-result.json').exists():
                    row['status'] = 'fail'
                    rows.append(row)
                    save(directory/'results.json',rows)
                    continue
                detail = json.loads((dest / 'generated/shape-result.json').read_text())
                row['status'] = detail['status']
                row['detail'] = detail
            except Blocked as exc:
                row.update(status='blocked',reason=str(exc))
            rows.append(row)
            save(directory / 'results.json',rows)
    # Mermaid has a different code-native renderer; preserve editable source at every size.
    for size in sizes:
        budget.check()
        dest = directory / ('mermaid-'+str(size))
        dest.mkdir()
        (dest / 'diagram.mmd').write_text('flowchart LR\n'+'\n'.join('N%d["制造对象 %d"] --> N%d'%(n,n,n+1) for n in range(size-1))+'\n')
        shutil.copyfile(SHARED/'assets/fonts/NotoSansSC.ttf',dest/'font.ttf')
        save(dest/'jobs.json',{'font':'font.ttf','jobs':[{'id':'capacity','kind':'mmd','source':'diagram.mmd','svg':'diagram.svg','png':'diagram.png','title':'合成规模验证','legend':'合成对象，不是实际企业拓扑','is_example':True}]})
        row = {'family':'mermaid','objects':size}
        if render:
            try:
                renderer = capacity_renderer(dest)
                detail = run_command(['node',renderer,dest/'jobs.json'],dest/'logs',budget,cwd='/tmp',timeout=180)
                rendered = json.loads((dest/'render-report.json').read_text()) if (dest/'render-report.json').exists() else {}
                row.update(mermaid_shape_result(dest,size,detail,rendered))
                row.update(command=detail,render_report=rendered)
            except Blocked as exc:
                row.update(status='blocked',reason=str(exc))
        else:
            row.update(status='uncovered',reason='Mermaid render not requested')
        rows.append(row)
        save(directory / 'results.json',rows)
    return {'status':'fail' if any(r['status']=='fail' for r in rows) else 'blocked' if any(r['status']!='pass' for r in rows) else 'pass',
            'rows':rows,'coverage':'representative performance shapes, not all-profile capacity certification'}


def failure_drills(directory,db,budget):
    from architecture_delivery import output_check
    from generate import generate
    from registry import load
    from profile_examples import normalize_example
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    model = normalize_example(load()[2]['trust-framework-default'])
    before = generate(model,directory/'pristine',all_items=True,strict=True)
    changed = copy.deepcopy(model)
    changed['project']['version'] = 'new-source-snapshot'
    _, stale = output_check(directory/'pristine',changed)
    if 'output-model-stale' not in stale:
        raise AssertionError('changed source accepted old output')
    # Deterministic write failure even when chmod is ineffective under an admin account.
    (directory/'not-a-directory').write_text('controlled write obstacle')
    rejected = False
    try:
        generate(model,directory/'not-a-directory'/'child',all_items=True,strict=True)
    except OSError:
        rejected = True
    if not rejected:
        raise AssertionError('controlled write failure not surfaced')
    started = time.monotonic()
    try:
        run_command([sys.executable,'-c','import subprocess,time;subprocess.Popen(["sleep","60"]);time.sleep(60)'],
                    directory/'cancelled-process',budget,timeout=.5)
        raise AssertionError('timeout not enforced')
    except Blocked as exc:
        if str(exc)!='command timeout':
            raise
    first = replay(db,directory/'recovery',budget,limit=100,interrupt_after=100)
    second = replay(db,directory/'recovery',budget,limit=10000)
    if second['consumed_events']<=first['consumed_events']:
        raise AssertionError('replay checkpoint recovery made no progress')
    result = {'status':'pass','changed_source_rejected':True,'write_failure_rejected':True,
              'owned_process_tree_cancelled':True,'cancellation_recovery_seconds':time.monotonic()-started,
              'replay_recovery':second,
              'browser_exit':'uncovered unless separate browser-exit-recovery stage passes'}
    save(directory/'results.json',result)
    return result


MAX_RASTER_PIXELS = 16_000_000
MAX_RASTER_SIDE = 16_384


def raster_dimensions(path):
    root = ET.parse(path).getroot()
    viewbox = root.get('viewBox', '').replace(',', ' ').split()
    if len(viewbox) != 4:
        raise Blocked('SVG viewport missing; cannot safely bound raster allocation')
    width,height = (float(v) for v in viewbox[2:])
    if not all(math.isfinite(v) and v > 0 for v in (width,height)):
        raise Blocked('SVG viewport invalid; cannot safely bound raster allocation')
    # Generated SVGs use viewport dimensions as pixel dimensions. Take a larger
    # explicit width/height if present rather than underestimating the bitmap.
    for i,key in enumerate(('width','height')):
        text = root.get(key,'').removesuffix('px')
        try:
            value = float(text)
        except ValueError:
            continue
        if not math.isfinite(value) or value <= 0:
            raise Blocked('SVG pixel dimension invalid')
        if i == 0:
            width = max(width,value)
        else:
            height = max(height,value)
    width,height = math.ceil(width),math.ceil(height)
    return {'width':width,'height':height,'pixels':width*height,
            'safe':width*height <= MAX_RASTER_PIXELS and max(width,height) <= MAX_RASTER_SIDE}


def capacity_renderer(directory):
    """Use the unchanged renderer with a campaign-local, pre-allocation guard.

    Keep its exact Mermaid/title/font behavior; do not patch skill sources or
    silently downscale the tested capacity point. Preserve oversized SVGs.
    """
    source = SHARED/'scripts/render.mjs'
    code = source.read_text()
    if code.startswith('#!'):
        code = code.split('\n',1)[1]
    marker = '  const plan=rasterPlan(svg);'
    if code.count(marker) != 1:
        raise Blocked('renderer changed; capacity guard needs review')
    guard = r"""  const bounds=svg.match(/viewBox="([^"]+)"/);
  if(!bounds)throw new Error('enterprise-raster-capacity: missing viewport');
  const dims=bounds[1].split(/[ ,]+/).map(Number).slice(2);
  for(let i=0;i<2;i++){const match=svg.match(new RegExp('<svg[^>]*\\b'+(i===0?'width':'height')+'="([0-9.]+)(?:px)?"'));if(match)dims[i]=Math.max(dims[i],Number(match[1]));}
  const [w,h]=dims.map(Math.ceil);
  if(!Number.isFinite(w)||!Number.isFinite(h)||w<=0||h<=0||w*h>16000000||Math.max(w,h)>16384)
    throw new Error('enterprise-raster-capacity: '+w+'x'+h+' exceeds 16000000 pixels or 16384px side; SVG retained, PNG untested');
"""
    code = code.replace(marker,guard+marker)
    code = code.replace("from './browser_resolver.mjs'",'from '+json.dumps((SHARED/'scripts/browser_resolver.mjs').as_uri()))
    code = code.replace("from './raster_tiles.mjs'",'from '+json.dumps((SHARED/'scripts/raster_tiles.mjs').as_uri()))
    # Resolve unchanged installed dependencies from the shared runtime, not from
    # the disposable output directory's package search path.
    code = code.replace("import {renderMermaid} from '@mermaid-js/mermaid-cli';",'const {renderMermaid}=await import(require.resolve("@mermaid-js/mermaid-cli"));')
    code = code.replace("import {Resvg} from '@resvg/resvg-js';",'const {Resvg}=require("@resvg/resvg-js");')
    code = 'import {createRequire} from "node:module";\nconst require=createRequire('+json.dumps(str(SHARED/'package.json'))+');\n'+code
    destination = Path(directory)/'bounded-renderer.mjs'
    destination.write_text(code)
    save(Path(directory)/'renderer-provenance.json',{'source':str(source),'source_sha256':sha256(source),
         'adapter_sha256':sha256(destination),'max_raster_pixels':MAX_RASTER_PIXELS,
         'max_raster_side':MAX_RASTER_SIDE,'behavior':'No source modification or silent downscaling; oversized SVG retained and PNG blocked'})
    return destination


def shape_worker(model_path,out,render=False):
    from generate import generate
    from validate import validate
    from architecture_delivery import output_check
    out = Path(out)
    model = json.loads(Path(model_path).read_text())
    started = time.monotonic()
    errors = [r for r in validate(model) if r['level']=='error']
    if errors:
        save(out/'shape-result.json',{'status':'blocked','reason':'expanded shape violates profile semantics','issues':errors})
        return 0
    generate(model,out,all_items=True,strict=True)
    dimensions = {str(p.relative_to(out)):raster_dimensions(p) for p in (out/'artifacts').glob('*.svg')}
    oversized = render and any(not d['safe'] for d in dimensions.values())
    blocked = False
    manifest = None
    if render and dimensions:
        try:
            manifest = generate(model,out,all_items=True,strict=True,render=True)
        except __import__('subprocess').CalledProcessError:
            report_path = out/'render-report.json'
            report = json.loads(report_path.read_text()) if report_path.exists() else {}
            if report.get('status')!='blocked':raise
            save(out/'shape-result.json',{'status':'blocked','render_requested':True,
                 'objects':len(model['entities']),'raster_dimensions':dimensions,
                 'raster_status':'blocked','reason':report.get('reason'),
                 'monolithic_capacity_claimed':False,'visual_semantics':'needs-review'})
            return 0
    _, errors = output_check(out,model)
    pngs = {}
    for p in (out/'artifacts').glob('*.png'):
        with p.open('rb') as stream:
            header = stream.read(24)
        if len(header)!=24 or header[:8]!=b'\x89PNG\r\n\x1a\n':
            errors.append('invalid PNG '+p.name)
            continue
        width,height = struct.unpack('!II',header[16:24])
        pngs[str(p.relative_to(out))] = {'width':width,'height':height,'sha256':sha256(p)}
    tile_manifests = [entry['tile_manifest'] for entry in (manifest or {}).get('artifacts',[]) if entry.get('raster_mode')=='tiles']
    if render and dimensions and not blocked and not pngs and not tile_manifests:
        errors.append('requested render produced no PNG')
    result = {'status':'fail' if errors else 'blocked' if blocked else 'pass','issues':errors,
              'seconds':time.monotonic()-started,'objects':len(model['entities']),
              'render_requested':render,'raster_dimensions':dimensions,'pngs':pngs,
              'raster_status':'tiled-native-resolution' if tile_manifests else 'not-applicable-native-markdown' if not dimensions else 'rendered' if render else 'uncovered',
              'tile_manifests':tile_manifests,'monolithic_capacity_claimed':bool(render and dimensions and not oversized),
              'reason':'Native-resolution SVG crops; single-bitmap capacity remains unclaimed' if tile_manifests else None,
              'visual_semantics':'needs-review; saved output checks do not prove readability at this density'}
    save(out/'shape-result.json',result)
    return 1 if errors else 0


def browser_drill(directory,budget):
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    script = directory/'probe.mjs'
    script.write_text("import {launchBrowser} from "+json.dumps((SHARED/'scripts/browser_resolver.mjs').as_uri())+";\n"
        "const first=await launchBrowser(); const process=first.process();\n"
        "if(!process) throw new Error('no owned browser process');\n"
        "const disconnected=new Promise(resolve=>first.once('disconnected',resolve));\n"
        "process.kill('SIGKILL'); await disconnected;\n"
        "let rejected=false;try{await first.newPage()}catch(e){rejected=true}\n"
        "if(!rejected)throw new Error('exited browser accepted work');\n"
        "const second=await launchBrowser();try{const page=await second.newPage();\n"
        "await page.setContent('<html><body>制造集团浏览器恢复</body></html>');\n"
        "await page.screenshot({path:"+json.dumps(str(directory/'recovered.png'))+"});\n"
        "console.log(JSON.stringify({status:'pass',owned_exit_rejected:true,relaunch_verified:true}));\n"
        "}finally{await second.close()}\n")
    command = run_command(['node',script],directory/'logs',budget,cwd='/tmp',timeout=60)
    if command['exit_code']!=0:
        return command
    result = json.loads((directory/'logs/stdout.jsonl').read_text().strip().splitlines()[-1])
    save(directory/'result.json',result)
    return result
