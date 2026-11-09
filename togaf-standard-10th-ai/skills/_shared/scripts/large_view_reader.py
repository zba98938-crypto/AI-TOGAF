#!/usr/bin/env python3
"""Bounded static entity/relationship reader; not a replacement topology or notation.
Every selected record and cross-page relationship is retained with original IDs.
"""
import argparse,hashlib,html,json,math
from pathlib import Path
from strict_json import load
from closure_render import wrap

def digest(data):return hashlib.sha256(data).hexdigest()
def page_svg(entities,number,total):
    pieces=['<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="#f6f9fc"/><g font-family="PingFang SC, Noto Sans CJK SC, Arial, sans-serif" fill="#172b4d">',
            f'<text x="40" y="58" font-size="32">实体目录切片 {number} / {total}（不是完整拓扑图）</text>',
            '<text x="40" y="101" font-size="22">关系、守卫与跨页端点在静态明细中完整保留；不从相邻位置推断任何关系。</text>']
    excerpts=[]
    for i,e in enumerate(entities):
        x=40+(i%3)*625;y=145+(i//3)*210
        pieces.append(f'<rect x="{x}" y="{y}" width="585" height="188" rx="12" fill="white" stroke="#b8cbe1"/>')
        name=wrap(e.get('name',e['id']),38)
        if len(name)>3:name=['长名称：见下方完整实体明细'];excerpts.append(e['id'])
        for line_no,line in enumerate(name):pieces.append(f'<text x="{x+18}" y="{y+38+line_no*31}" font-size="25">{html.escape(line)}</text>')
        # IDs and types are full in the ledger; long values are explicitly disclosed.
        for line_no,(label,value) in enumerate([('ID',e['id']),('类型',e.get('type','未指定'))]):
            shown=value if len(wrap(value,56))<=1 else '长值：见完整明细'
            pieces.append(f'<text x="{x+18}" y="{y+142+line_no*26}" font-size="20">{label}: {html.escape(shown)}</text>')
    pieces.append('<text x="40" y="1040" font-size="20">项目阅读投影 / 非严格 UML、BPMN 或 ArchiMate 表示法 / 不代表来源等价或业务验收</text></g></svg>')
    return ''.join(pieces),excerpts

def render(input_path,out,view_id):
    input_path=Path(input_path);out=Path(out)
    raw=input_path.read_bytes();model=load(input_path)
    views=[v for v in model.get('views',[]) if v['id']==view_id]
    if len(views)!=1:raise ValueError('exactly one selected project view required')
    view=views[0];byid={e['id']:e for e in model['entities']};edges={e['id']:e for e in model['relationships']}
    if len(byid)!=len(model['entities']) or len(edges)!=len(model['relationships']):raise ValueError('duplicate record ID')
    ids=list(view.get('entity_ids',[]));rids=list(view.get('relationship_ids',[]))
    if len(ids)!=len(set(ids)) or len(rids)!=len(set(rids)):raise ValueError('duplicate view membership')
    if not ids or not set(ids)<=set(byid) or not set(rids)<=set(edges):raise ValueError('empty/missing selected view records')
    selected=[byid[i] for i in ids];relationships=[edges[i] for i in rids]
    if any(e['source'] not in byid or e['target'] not in byid for e in relationships):raise ValueError('missing relationship endpoint')
    if out.exists():raise ValueError('output must be new; prior evidence is immutable')
    out.mkdir(parents=True);(out/'original-model.json').write_bytes(raw)
    pages=[];membership={};excerpts=[];total=math.ceil(len(selected)/12)
    for start in range(0,len(selected),12):
        number=start//12+1;name=f'entities-{number:04d}.svg';svg,short=page_svg(selected[start:start+12],number,total)
        (out/name).write_text(svg);excerpts+=short
        pages.append({'file':name,'entity_ids':ids[start:start+12],'width':1920,'height':1080,'pixels':2073600})
        membership.update({eid:number for eid in ids[start:start+12]})
    relationship_rows=[]
    for e in relationships:
        relationship_rows.append({**e,'source_page':membership.get(e['source']),'target_page':membership.get(e['target']),
                                  'cross_page':membership.get(e['source'])!=membership.get(e['target']),
                                  'source_name':byid[e['source']].get('name',e['source']),'target_name':byid[e['target']].get('name',e['target'])})
    for name,value in [('entities.json',selected),('relationships.json',relationships),('relationship-pages.json',relationship_rows)]:
        (out/name).write_text(json.dumps(value,ensure_ascii=False,indent=2))
    def table(headers,rows):
        return '<table><thead><tr>'+''.join('<th>'+html.escape(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(c))+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table>'
    sections=[]
    for page in pages:
        sections.append('<section><img src="'+page['file']+'" alt="实体目录切片"><h2>完整实体明细</h2>'+table(['ID','类型','完整名称','属性与证据'],[[i,byid[i].get('type',''),byid[i].get('name',''),json.dumps({k:v for k,v in byid[i].items() if k not in ('id','type','name')},ensure_ascii=False)] for i in page['entity_ids']])+'</section>')
    for start in range(0,len(relationship_rows),12):
        sections.append('<section><h2>完整关系明细 '+str(start//12+1)+'</h2>'+table(['ID / 类型','来源 / 页','实际含义','目标 / 页','全部其他字段'],[[e['id']+' / '+e['type'],e['source_name']+' / '+str(e['source_page'] or '视图外'),e.get('label','未标注'),e['target_name']+' / '+str(e['target_page'] or '视图外'),json.dumps({k:v for k,v in e.items() if k not in ('id','type','source_name','target_name','source_page','target_page','label')},ensure_ascii=False)] for e in relationship_rows[start:start+12]])+'</section>')
    (out/'reader.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>分片架构阅读包</title><style>body{font:20px "PingFang SC",Arial;color:#172b4d;margin:24px}img{width:100%;max-width:1920px}table{border-collapse:collapse;width:100%;table-layout:fixed}td,th{border:1px solid #b8cbe1;padding:12px;overflow-wrap:anywhere;vertical-align:top}th{background:#dbeafe}section{break-after:page;margin-bottom:48px}@page{size:A3 landscape}</style><h1>'+html.escape(view.get('title',view_id))+'</h1><p>实体目录切片 + 完整静态关系台账；不是单张大图的缩略拓扑，不承诺原图的表示法、布局或专业验收。原模型字节不变。</p>'+''.join(sections)+'</html>')
    manifest={'schema_version':'bounded-view-reader/1','notation':'project-record-reader','view_id':view_id,'source_sha256':digest(raw),'original_bytes_preserved':True,'entity_count':len(ids),'relationship_count':len(rids),'entity_pages':pages,'cross_page_relationship_ids':[e['id'] for e in relationship_rows if e['cross_page']],
              'excerpts_explicitly_disclosed':excerpts,'full_entity_records_file':'entities.json','full_relationship_records_file':'relationships.json','all_selected_records_retained':True,'monolithic_renderer_capacity_claimed':False,'strict_language_conformance':False,'visual_acceptance':'pending'}
    manifest['output_hashes']={p.name:digest(p.read_bytes()) for p in out.iterdir() if p.is_file()}
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));return manifest

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--model',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--view',required=True);a=p.parse_args()
    r=render(a.model,a.out,a.view);print(json.dumps({k:r[k] for k in ('entity_count','relationship_count','all_selected_records_retained')},ensure_ascii=False))
if __name__=='__main__':main()
