#!/usr/bin/env python3
"""Real bounded topology/PNG and Mermaid partition capacity, no model calls."""
import argparse,hashlib,json,os,re,subprocess,sys,time
from pathlib import Path
from PIL import Image
from fontTools import subset
from fontTools.ttLib import TTFont
from lxml import etree
ROOT=Path(__file__).resolve().parents[1];SHARED=ROOT/'togaf-standard-10th-ai/skills/_shared'
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(inputs,out,sizes=(100,1000,10000),families=('network','matrix','roadmap','catalogue','mermaid')):
    out.mkdir(parents=True,exist_ok=False);rows=[]
    for family in families:
        for size in sizes:
            name=f'{family}-{size}';directory=out/name;source=inputs/(name+('.mmd' if family=='mermaid' else '.json'))
            started=time.monotonic();row={'family':family,'objects':size,'source_sha256':sha(source),'monolithic_capacity_claimed':False,'visual_acceptance':'pending'}
            # Preserve every code point in the input and static annotations.
            texts=source.read_text()+''.join(chr(i) for i in range(32,127))+'分层拓扑有向关系按原记录；节点可跨页重复，完整字段和跨页索引见阅读入口。项目表达，非严格建模语言认证。长名称：见完整记录分层关系候选草案虚构示例图例：项目有向关系投影；完整ID和记录见manifest；不代表原单图容量通过'
            font=subset.load_font(str(SHARED/'assets/fonts/NotoSansSC.ttf'),subset.Options());sub=subset.Subsetter();sub.populate(text=texts);sub.subset(font);font_path=out/(name+'-font.ttf');subset.save_font(font,str(font_path),subset.Options())
            argv=['node',str(SHARED/'scripts/layered_topology.mjs'),'--out',str(directory),'--font',str(font_path),'--render']
            if family=='mermaid':argv+=['--mermaid',str(source)]
            else:argv+=['--model',str(source),'--view',json.loads(source.read_text())['views'][0]['id']]
            def command(args,label,timeout=1800):
                p=subprocess.run(args,capture_output=True,text=True,timeout=timeout,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
                (out/(name+'-'+label+'.log')).write_text(p.stdout+p.stderr);return p.returncode
            try:
                code=command(argv,'topology');row['exit_code']=code
                if code:raise ValueError('topology generation failed')
                manifest=json.loads((directory/'manifest.json').read_text());records=json.loads((directory/'records.json').read_text())
                cmap=TTFont(directory/'font.ttf').getBestCmap()
                assert manifest['entity_count']==size
                assert manifest['source_sha256']==sha(source)
                assert len(set(e for p in manifest['pages'] for e in p['entity_ids']))==len(records['entities'])
                assert sorted(e for p in manifest['pages'] for e in p['relationship_ids'])==sorted(r['id'] for r in records['relationships'])
                for page in manifest['pages']:
                    actual=''.join(etree.fromstring((directory/page['svg']).read_bytes()).xpath('//*[local-name()="text"]/text()'))
                    assert all(c.isspace() or ord(c) in cmap for c in actual),'missing topology font glyph'
                    assert sha(directory/page['svg'])==page['svg_sha256']
                    assert sha(directory/page['png'])==page['png_sha256']
                    with Image.open(directory/page['png']) as im:im.verify()
                row.update(pages=len(manifest['pages']),relationships=len(records['relationships']),topology_status='engineering-pass',all_pngs_decoded=True)
                quality=out/(name+'-geometry.json')
                command(['node',str(SHARED/'scripts/diagram_quality.mjs'),str(directory),str(quality)],'geometry')
                q=json.loads(quality.read_text());row['geometry_status']=q['status'];row['geometry_findings']=sum(len(r['findings']) for r in q.get('rows',[]))
                if family=='mermaid':
                    # Subset from all actual page text; avoids embedding a 17MiB full
                    # CJK font in every Mermaid SVG. Full font hash remains recorded.
                    texts=''.join((directory/p['mermaid_source']).read_text() for p in manifest['pages'])+''.join(chr(i) for i in range(32,127))+'分层关系项目有向关系投影；完整ID和记录见manifest；不代表原单图容量通过虚构示例 / 候选草案图例：'
                    font=subset.load_font(str(SHARED/'assets/fonts/NotoSansSC.ttf'),subset.Options());sub=subset.Subsetter();sub.populate(text=texts);sub.subset(font);subset.save_font(font,str(directory/'mermaid-subset.ttf'),subset.Options())
                    spec=json.loads((directory/'render-jobs.json').read_text());spec['font']='mermaid-subset.ttf';save(directory/'mermaid-jobs.json',spec)
                    row['mermaid_exit_code']=command(['node',str(SHARED/'scripts/render.mjs'),str(directory/'mermaid-jobs.json')],'actual-mermaid')
                    actual=json.loads((directory/'render-report.json').read_text());assert actual['status']=='passed'
                    mermaid_cmap=TTFont(directory/'mermaid-subset.ttf').getBestCmap()
                    assert len(actual['results'])==len(manifest['pages'])
                    for page,result in zip(manifest['pages'],actual['results']):
                        svg=directory/result['svg'];png=directory/result['png'];assert sha(svg)==result['svg_sha256'];assert sha(png)==result['png_sha256']
                        text=svg.read_text();nodes=len(re.findall(r'class="node [^"]*"',text));edges=len(re.findall(r'class="[^"]*flowchart-link[^"]*"',text))
                        visible=''.join(etree.fromstring(svg.read_bytes()).xpath('//*[local-name()="text"]/text()'))
                        assert all(c.isspace() or ord(c) in mermaid_cmap for c in visible),'missing Mermaid font glyph'
                        assert nodes==len(page['entity_ids']),(nodes,len(page['entity_ids']))
                        assert edges==len(page['relationship_ids']),(edges,len(page['relationship_ids']))
                        with Image.open(png) as im:im.verify()
                    row.update(mermaid_partition_status='engineering-pass',mermaid_actual_node_edge_counts_verified=True,font_source_sha256=sha(SHARED/'assets/fonts/NotoSansSC.ttf'),subset_font_sha256=sha(directory/'mermaid-subset.ttf'))
                row['status']='engineering-pass' if row['geometry_status']=='engineering-pass' else 'needs_review'
            except Exception as exc:row.update(status='blocked' if isinstance(exc,subprocess.TimeoutExpired) else 'fail',reason=str(exc))
            row['seconds']=round(time.monotonic()-started,3);rows.append(row);save(out/'summary.json',{'rows':rows,'model_sessions':0,'business_acceptance':'pending','visual_acceptance':'pending'})
            print(json.dumps(row,ensure_ascii=False),flush=True)
    return rows
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    rows=run(a.inputs.resolve(),a.out.resolve());raise SystemExit(0 if all(r['status']=='engineering-pass' for r in rows) else 1)
