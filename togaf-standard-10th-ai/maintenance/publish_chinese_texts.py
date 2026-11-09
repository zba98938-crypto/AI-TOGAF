# -*- coding: utf-8 -*-
"""Publish actually authored Chinese body text, bound to exact web source blocks."""
from pathlib import Path
import json,re,hashlib,datetime
from bs4 import BeautifulSoup
C=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
blocksha=lambda b:hashlib.sha256(json.dumps(b,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
FOOTNOTES={'04-applying-the-adm':{'_footnotedef_1':'1. 关于如何运用一个完整ADM周期，初步建立组织架构能力的指导，见《TOGAF标准——EA能力与治理》。'}}
FOOTNOTES['01-introduction-and-core-concepts']={'_footnotedef_1':'1. TOGAF资料库提供在线公开的指南、白皮书及其他资源结构化清单，见www.opengroup.org/togaf-library。'}
FOOTNOTES['03-adm-techniques']={'_footnotedef_1':'1. Ross等2006年《作为战略的企业架构》提供了可能的模型。'}
FOOTNOTES['05-architecture-content']={'_footnotedef_1':'1. 参见 www.omg.org/spec/RAS。'}
def main():
 dest=C/'fundamental/chinese-text';dest.mkdir(exist_ok=True);entries=[];retrieval=[];checks=[]
 drafts=sorted((C/'maintenance/chinese-text-data').glob('*.txt'))+sorted((C/'maintenance/chinese-text-data/partial').glob('*.txt'))
 assert len({p.stem for p in drafts})==len(drafts),'one current text authoring source per volume'
 for draft in drafts:
  vol=draft.stem;src=C/'fundamental/web-2025/volumes'/vol/'document.json';d=json.loads(src.read_text());blocks=d['blocks']
  start=next(i for i,b in enumerate(blocks) if re.fullmatch('h[2-6]',b['kind']) and re.match(r'^\d+\.',b['text_en']));all_body=blocks[start:];body=all_body
  partial=draft.parent.name=='partial'
  if partial:
   scope=json.loads(draft.with_suffix('.scope.json').read_text());anchors=set(scope['complete_chapter_anchors'])
   assert anchors and anchors<=set(h['id'] for h in d['headings'])
   # Extracted unwrapped captions have no section_path. Retain their actual
   # preceding heading context instead of silently dropping them from a chapter.
   body=[];active_path=[]
   for b in all_body:
    if b.get('section_path'):active_path=b['section_path']
    if any(s['id'] in anchors for s in active_path):body.append(b)
   assert body and body[0]['kind'].startswith('h'),'partial selection must begin at a source heading'
  pairs=re.split(r'^@@ (b\d+)\n',draft.read_text(),flags=re.M);translations={pairs[i]:pairs[i+1].strip() for i in range(1,len(pairs),2)}
  needed={b['id'].split(':')[-1] for b in body if b['kind']!='img'}
  assert len(translations)==(len(pairs)-1)//2,'duplicate translation identities'
  assert set(translations)==needed,{'missing':sorted(needed-set(translations)),'unexpected':sorted(set(translations)-needed)}
  source_footnotes=d['footnotes'] if not partial else [f for f in d['footnotes'] if any(f['id'] in b.get('html','') for b in body)]
  footnotes={k:v for k,v in FOOTNOTES.get(vol,{}).items() if k in {f['id'] for f in source_footnotes}}
  assert set(footnotes)=={f['id'] for f in source_footnotes},'translate every in-scope source footnote'
  rows=[];sections=[];current=None;lines=['# '+d['title_zh']+'：来源逐块对应的中文正文','','状态：正文逐块译写与作者来源核对完成；不同评审人的最终语义验收待完成。出版机构、版权和前言等前置内容不在本正文译写范围，保留[英文离线原文](../web-2025/volumes/'+vol+'/index.html)。本页不是官方中文译本。','','[独立语义分析](../analysis/'+vol+'.md) · [机读逐块中英对照]('+vol+'.json)','','## 译写约定','','Engagement译为“架构工作”，不推定人事雇佣关系；feasible/viable分别保留为“可行/可持续实施”，不宣称已经验证商业收益。规范性must、should及通常、可能等限定词按源段保留。表中跨行合并的工作领域展开重复，以明确中文表格阅读归属；不增加源表列。图像保留原图，图内文字与连接的审查见语义分析，不重画成伪官方图。','']
  if partial:lines[2]='状态：仅下列选定章节的正文逐块译写完成；本卷其余正文待译，不同评审人的最终语义验收待完成。本页不是官方中文译本。选定源章节：'+', '.join(sorted(anchors))+'。'
  for b in body:
   suffix=b['id'].split(':')[-1];anchor=b['section_path'][-1]['id'] if b.get('section_path') else current['heading_id'];loc={'kind':'web-block','document_id':d['id'],'volume_id':vol,'anchor':anchor,'block_id':b['id'],'source_html_sha256':d['source']['html_sha256'],'block_sha256':blocksha(b),'fingerprint_scheme':'json-sorted-ensure-unicode'}
   if b['kind']=='img':
    soup=BeautifulSoup(b['html'],'html.parser');im=soup.find('img');asset=im.get('src','')
    # The saved HTML already uses local asset paths; never fetch a remote image.
    if not asset.startswith('assets/'):
     candidates=[i for i in d['images'] if i.get('source_url')==asset]
     if not candidates:candidates=[i for i in d['images'] if i.get('alt')==im.get('alt')]
     # A source image may be referenced more than once. Equal local identities
     # are repeat usages, not ambiguity; equal alt text alone is not identity.
     assets={i['local_asset'] for i in candidates}
     assert len(assets)==1,(b['id'],asset);asset=next(iter(assets))
     if b.get('local_asset'):assert b['local_asset']==asset
    assert (src.parent/asset).is_file();zh='原图：'+im.get('alt','')
    lines+=['<a id="'+suffix+'"></a>','![原图](../web-2025/volumes/'+vol+'/'+asset+')','']
   else:
    zh=translations[suffix];assert zh and re.search(r'[\u3400-\u9fff]',zh),b['id']
    if re.fullmatch('h[2-6]',b['kind']):
     current={'id':d['id']+'#'+b['anchor'],'heading_id':b['anchor'],'title_en':b['text_en'],'title_zh':zh,'block_ids':[]};sections.append(current)
     lines+=['<a id="'+b['anchor']+'"></a>','#'*int(b['kind'][1])+' '+zh,'']
    else:lines+=['<a id="'+suffix+'"></a>',zh,'']
   current['block_ids'].append(b['id'])
   rows.append({'id':d['id']+':zh:'+suffix,'source_block_id':b['id'],'kind':b['kind'],'source_locator':loc,'text_en':b['text_en'],'text_zh':zh,'source_exact_quote_preserved':True,'origin':'project-authored-Chinese-translation' if b['kind']!='img' else 'source-image-preserved','author_review_status':'source-aligned','independent_review_status':'pending'})
  lines+=['## 脚注','']
  for f in source_footnotes:lines+=['<a id="'+f['id']+'"></a>',footnotes[f['id']],'']
  out=dest/(vol+'.json');record={'schema_version':'source-bound-Chinese-body/1','document_id':d['id'],'volume_id':vol,'source_document_path':str(src.relative_to(C)),'source_document_sha256':sha(src),'source_html_sha256':d['source']['html_sha256'],'authoring_path':str(draft.relative_to(C)),'authoring_sha256':sha(draft),'status':'body-written-source-aligned-independent-review-pending','official_translation':False,'scope_zh':'编号正文标题、段落、列表、表格与图注全量逐块译写；原图保留；脚注译写。前置出版信息不纳入正文完成声明。','sections':sections,'blocks':rows,'footnotes':[{'id':f['id'],'text_en':f['text_en'],'text_zh':footnotes[f['id']],'source_html_sha256':d['source']['html_sha256']} for f in source_footnotes],'coverage':{'body_sections':len(sections),'body_blocks':len(rows),'translated_text_blocks':len(translations),'source_images_preserved':sum(b['kind']=='img' for b in body),'tables':sum(b['kind']=='table' for b in body),'footnotes':len(source_footnotes)},'independent_semantic_acceptance':'pending'}
  record['volume_body_complete']=not partial
  record['scope_zh']='选定章节逐块译写；本卷其余章节待译。' if partial else record['scope_zh']
  record['status']='selected-chapters-body-written-independent-review-pending' if partial else record['status']
  record['footnotes']=[{'id':f['id'],'text_en':f['text_en'],'text_zh':footnotes[f['id']],'source_html_sha256':d['source']['html_sha256']} for f in source_footnotes]
  record['coverage']['footnotes']=len(source_footnotes);record['coverage']['volume_total_body_blocks']=len(all_body)
  out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');out.with_suffix('.md').write_text('\n'.join(lines)+'\n');bm={b['source_block_id']:b for b in rows}
  for s in sections:
   retrieval.append({'id':s['id']+':Chinese-body','parent_record_id':s['id'],'document_id':d['id'],'language':'zh','content_role':'current-source-bound-Chinese-body','text':s['title_en']+'\n'+'\n'.join(bm[i]['text_zh'] for i in s['block_ids']),'source_path':str(out.relative_to(C)),'source_sha256':sha(out),'source_locators':[bm[i]['source_locator'] for i in s['block_ids']],'translation_status':record['status']})
  entries.append({'document_id':d['id'],'volume_id':vol,'json':str(out.relative_to(C)),'markdown':str(out.with_suffix('.md').relative_to(C)),'sha256':sha(out),**record['coverage'],'volume_body_complete':not partial,'status':record['status']});checks.append({'document_id':d['id'],'source_block_coverage':len(rows)==len(body),'translation_id_coverage':set(translations)==needed,'scope':'selected-chapters' if partial else 'complete-numbered-body'})
 index={'schema_version':'source-bound-Chinese-index/1','volumes':entries,'counts':{'volumes_with_body_written':len(entries),'body_sections_written':sum(e['body_sections'] for e in entries),'body_blocks':sum(e['body_blocks'] for e in entries)},'all_six_volumes_complete':len(entries)==6,'independent_acceptance_complete':False,'notice_zh':'此索引仅计算实际译写正文，章节分析不计作全文；来源结构校验不替代独立语义审阅。'}
 index['counts']['volumes_with_body_written']=sum(e['volume_body_complete'] for e in entries)
 index['counts']['volumes_with_partial_body_written']=sum(not e['volume_body_complete'] for e in entries)
 index['all_six_volumes_complete']=sum(e['volume_body_complete'] for e in entries)==6
 (dest/'index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
 (dest/'README.md').write_text('# 当前来源逐块中文正文\n\n实际译写完成'+str(index['counts']['volumes_with_body_written'])+'卷、'+str(index['counts']['body_sections_written'])+'个编号小节、'+str(index['counts']['body_blocks'])+'个来源块。逐节语义分析另存；不同评审人的最终校核尚未完成。中文为项目译写，不是官方中文译本。\n\n'+ '\n'.join('- ['+e['volume_id']+']('+e['volume_id']+'.md)：'+str(e['body_sections'])+'个编号小节，'+str(e['body_blocks'])+'个源块。' for e in entries)+'\n\n补充资料[G226中文正文](../../supplementary/chinese-text/G226.md)按75节对齐，保留764个英文来源块；W242C为本地中文原文，见[原文与校释](../../supplementary/W242C.md)。\n')
 (C/'retrieval/chinese-chunks.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in retrieval))
 graph_path=C/'architecture/source-method-graph.json'
 if graph_path.exists():
  graph=json.loads(graph_path.read_text());old={n['id'] for n in graph['nodes'] if n['kind']=='authored-Chinese-body'}
  graph['nodes']=[n for n in graph['nodes'] if n['id'] not in old];graph['edges']=[e for e in graph['edges'] if e['source'] not in old and e['target'] not in old]
  for r in retrieval:
   graph['nodes'].append({'id':r['id'],'kind':'authored-Chinese-body','document_id':r['document_id'],'source_path':r['source_path'],'origin':'project-authored-translation','independent_review':'pending'})
   graph['edges'].append({'source':r['id'],'target':r['parent_record_id'],'relation':'project-translation-of','origin':'project-authored-translation','evidence_block_ids':[x['block_id'] for x in r['source_locators']]})
  graph_path.write_text(json.dumps(graph,ensure_ascii=False,indent=2)+'\n')
  ids={n['id'] for n in graph['nodes']}
  dangling=[e for e in graph['edges'] if e['source'] not in ids or e['target'] not in ids]
  assert not dangling,dangling
  bridge=C/'quality/execution-bridge.json'
  if bridge.exists():
   b=json.loads(bridge.read_text());b['counts'].update(nodes=len(graph['nodes']),edges=len(graph['edges']),dangling_endpoints=len(dangling));b['counts_scope']='current graph including authored Chinese-body links; skill reference checks unchanged';bridge.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
  publication=C/'quality/extended-publication.json'
  if publication.exists():
   p=json.loads(publication.read_text());p['counts'].update(graph_nodes=len(graph['nodes']),graph_edges=len(graph['edges']));p['Chinese_body_progress']=index['counts'];publication.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
 report={'schema_version':'Chinese-body-verification/1','passed':all(x['source_block_coverage'] and x['translation_id_coverage'] for x in checks),'checks':checks,'counts':index['counts'],'independent_semantic_acceptance':'pending','limits_zh':['完整源块覆盖证明没有跳过正文块，不证明每个译句已经由另一评审人认证。']}
 (C/'quality/chinese-body-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(index['counts'])
if __name__=='__main__':main()
