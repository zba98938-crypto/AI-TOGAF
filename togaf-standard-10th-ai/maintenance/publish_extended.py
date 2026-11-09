# -*- coding: utf-8 -*-
"""Publish source-bound web/PDF reviews without upgrading analysis to translation."""
from pathlib import Path
import hashlib,json,re,copy,collections,sys
sys.dont_write_bytecode=True
from source_paths import resolve as source_path
C=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def chunks(text,size=10000):return [text[i:i+size] for i in range(0,len(text),size)]
def numbered(blocks):
 current=None;out=[]
 for b in blocks:
  if re.fullmatch(r'h[2-6]',b['kind']):
   current=None
   if re.match(r'^(?:\d+\.|[A-C][.:])',b['text_en']):
    current={'id':b['anchor'],'blocks':[]};out.append(current)
  if current is not None:current['blocks'].append(b)
 return out
FIELDS=['concepts_zh','applicability_zh','logic_zh','decisions_zh','artifacts_evidence_zh','limits_zh']
LABELS=['概念','适用条件','逻辑关系','决策方法','制品及证据','适用边界']
def main():
 checks=[];entries=[];retrieval=[];graph={'schema_version':'source-method-graph/1','nodes':[],'edges':[],'relation_origins_zh':{'official-citation':'源文引用，仅限有源证据时','interpretation-guide-bridge':'编者跨文档解释关联','project-operationalization':'项目任务/决策/制品设计'}};issues=[]
 def check(ok,msg):
  checks.append({'check':msg,'passed':bool(ok)})
  if not ok:raise ValueError(msg)
 guides={p.stem:read(p) for p in (C/'chapters').glob('G*.json')}
 def refs(values):
  result=[]
  for v in values:
   code=v.get('document_id') if isinstance(v,dict) else v.split(':')[0]
   sid=v.get('section_id') if isinstance(v,dict) else (v if ':' in v else None)
   check(code in guides,'guide reference '+str(v))
   ss=[s for s in guides[code]['sections'] if sid in (s['source_section_id'],s['id'])] if sid else []
   check(not sid or len(ss)==1,'guide section '+str(sid))
   if isinstance(v,dict) and v.get('review_sha256'):
    check(v['review_sha256']==sha(C/'chapters'/(code+'.json')),'guide reference fingerprint '+str(sid))
   result.append({'document_id':code,'source_section_id':sid,'path':'chapters/'+code+'.json','sha256':sha(C/'chapters'/(code+'.json')),'relation_type':'interpretation-guide-bridge','source_unit_ids':[u['id'] for s in ss for u in s['source_units']]})
  return result
 for p in sorted((C/'maintenance/fundamental-review-data').glob('0[1-6]-*.json')):
  if p.name.endswith('visual-review.json'):continue
  review=read(p);vol=review['volume_id'];src=C/'fundamental/web-2025/volumes'/vol/'document.json';doc=read(src);bm={b['id']:b for b in doc['blocks']};expected=numbered(doc['blocks']);sections={s['heading_id']:s for s in review['sections']}
  check(review['source_document_sha256']==sha(src),'source document hash '+vol)
  check(set(sections)=={s['id'] for s in expected},'all numbered headings '+vol)
  translation=C/'fundamental/chinese-text'/(vol+'.json')
  body=read(translation) if translation.exists() else None
  written={s['id'] for s in body['sections']} if body else set()
  status='separate-body-written-independent-review-pending' if body and body.get('volume_body_complete') else 'not-complete-analysis-is-not-full-translation'
  pub=copy.deepcopy(review);pub.update(schema_version='published-source-method-review/1',document_id=doc['id'],source_kind='web',publication_role='fundamental-content',maintenance_sha256=sha(p),source_document_path=str(src.relative_to(C)),translation_status=status);pub['sections']=[]
  visuals=read(C/'maintenance/fundamental-review-data/05-visual-review.json') if vol.startswith('05-') else review
  for kind,source_kind in [('figures','img'),('tables','table')]:
   rows=visuals.get(kind,[]);expected_ids={b['id'] for b in doc['blocks'] if b['kind']==source_kind}
   check({x['block_id'] for x in rows}==expected_ids,'all '+kind+' '+vol)
   for v in rows:
    b=bm[v['block_id']]
    if kind=='tables':v['table_role']='frontmatter-contributors' if v.get('caption_en')=='Acknowledgements: contributor names' else 'body-table'
    if v.get('asset_sha256'):check(sha(C/v['asset_path'])==v['asset_sha256'],'visual asset '+v['block_id'])
    if v.get('source_block_sha256'):
     candidates={'html-utf8':hashlib.sha256(b['html'].encode()).hexdigest(),'json-sorted-ensure-unicode':hashlib.sha256(json.dumps(b,ensure_ascii=False,sort_keys=True).encode()).hexdigest()}
     matches=[k for k,h in candidates.items() if h==v['source_block_sha256']];check(len(matches)==1,'visual source block '+v['block_id']);v['source_block_fingerprint_scheme']=matches[0]
   pub[kind]=copy.deepcopy(rows)
  translation=C/'fundamental/chinese-text'/(vol+'.json')
  notice='本页为逐节语义解释，不能把解释当全文译文。'
  if translation.exists():
   notice+='本卷另有[逐块中文正文](../chinese-text/'+vol+'.md)，已写正文的最终独立语义校核仍待完成。'
   pub['separate_Chinese_body_path']='fundamental/chinese-text/'+vol+'.json'
  else:notice+='本卷完整中文正文尚未完成。'
  text=['# '+doc['title_zh']+'：当前语义解析','',notice,'', '[英文及离线原文](../web-2025/volumes/'+vol+'/index.html)','']
  for expected_s in expected:
   s=copy.deepcopy(sections[expected_s['id']]);ids=[b['id'] for b in expected_s['blocks']]
   check(s['source_block_ids']==ids,'exact section block assignment '+vol+'#'+s['heading_id'])
   for k in FIELDS:check(k in s,'analysis field '+vol+'#'+s['heading_id']+'/'+k)
   if s.get('source_content_sha256'):check(s['source_content_sha256']==hashlib.sha256('\n'.join(b.get('text_en','') for b in expected_s['blocks']).encode()).hexdigest(),'section content hash '+vol+'#'+s['heading_id'])
   # Source fingerprints are evidence, not a claim that all statements are official.
   s['source_locators']=[{'kind':'web-block','document_id':doc['id'],'volume_id':vol,'anchor':s['heading_id'],'block_id':i,'source_html_sha256':doc['source']['html_sha256'] if 'html_sha256' in doc['source'] else review.get('source_html_sha256'),'block_sha256':hashlib.sha256(json.dumps(bm[i],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'fingerprint_scheme':'json-sorted-ensure-unicode'} for i in ids]
   s['guide_refs']=refs(s.get('guide_refs',[]));s['source_evidence']=[{'block_id':i,'text_en':bm[i]['text_en']} for i in ids];s['interpretation_origin']='authored-interpretation-not-official-translation';s['translation_status']='body-written-independent-review-pending' if doc['id']+'#'+s['heading_id'] in written else 'pending-full-Chinese-text'
   sid=doc['id']+'#'+s['heading_id'];s['id']=sid;pub['sections'].append(s)
   graph['nodes'].append({'id':sid,'kind':'source-section','document_id':doc['id'],'title':s['title_en']})
   for ref in s['guide_refs']:graph['edges'].append({'source':sid,'target':ref['source_section_id'] or ref['document_id'],'relation':'interpretation-guide-bridge','evidence_block_ids':ids,'target_sha256':ref['sha256']})
   chain=[]
   for field,typ in [('decisions_zh','decision-task'),('artifacts_evidence_zh','artifact-evidence-requirement')]:
    for i,value in enumerate(s[field]):
     nid=sid+':'+typ+':'+str(i+1);chain.append(nid);graph['nodes'].append({'id':nid,'kind':typ,'text_zh':value,'origin':'project-operationalization'});graph['edges'].append({'source':sid,'target':nid,'relation':'project-operationalization','evidence_block_ids':ids})
   if len(chain)>1:graph['edges'].append({'source':chain[0],'target':chain[-1],'relation':'supports-reviewable-output','origin':'project-operationalization'})
   text+=['<a id="'+s['heading_id']+'"></a>','## '+s['title_en'],'']
   for k,label in zip(FIELDS,LABELS):
    if s[k]:text+=[label+'：'+'；'.join(s[k]),'']
   text+=['来源块：'+', '.join(ids),'','<details><summary>展开本节完整英文来源</summary>','']+[bm[i]['text_en']+'\n' for i in ids]+['</details>','']
   payload=s['title_en']+'\n'+json.dumps(s,ensure_ascii=False)
   parts=chunks(payload)
   for i,t in enumerate(parts,1):retrieval.append({'id':sid+':c'+str(i),'parent_record_id':sid,'part':i,'part_count':len(parts),'document_id':doc['id'],'language':'zh','content_role':'current-source-method-analysis','text':t,'source_path':'fundamental/analysis/'+vol+'.json','source_locators':s['source_locators'],'translation_status':s['translation_status']})
  pub['coverage']={'numbered_sections':len(pub['sections']),'source_blocks':sum(len(s['source_block_ids']) for s in pub['sections']),'figures':len(pub['figures']),'tables':len(pub['tables']),'full_translation_sections':sum(s['translation_status']=='body-written-independent-review-pending' for s in pub['sections'])}
  out=C/'fundamental/analysis'/(vol+'.json');dump(out,pub);out.with_suffix('.md').write_text('\n'.join(text)+'\n')
  entries.append({'document_id':doc['id'],'publication_role':'fundamental-content','json':str(out.relative_to(C)),'markdown':str(out.with_suffix('.md').relative_to(C)),**pub['coverage'],'sha256':sha(out),'translation_status':pub['translation_status']})
  for issue in pub.get('source_issues',[]):issues.append({'document_id':doc['id'],**issue})
 for code in ['G226','W242C']:
  p=C/'maintenance/supplementary-review-data'/(code+'.json');review=read(p);src=source_path(C/review['source_path']);check(sha(src)==review['source_pdf_sha256'],'supplement PDF '+code);check(sha(C/review['source_extraction_path'])==review['source_extraction_sha256'],'supplement extraction '+code)
  gbody=C/'supplementary/chinese-text/G226.json'
  pub=copy.deepcopy(review);pub.update(source_kind='pdf',maintenance_sha256=sha(p),translation_status='source-Chinese-preserved-with-corrections' if code=='W242C' else ('separate-body-written-independent-review-pending' if gbody.exists() and read(gbody)['body_complete'] else 'full-Chinese-translation-pending'))
  if code=='G226' and gbody.exists():pub['separate_Chinese_body_path']=str(gbody.relative_to(C))
  for section in pub['sections']:
   if section.get('guide_refs'):section['guide_refs']=refs(section['guide_refs'])
   section['source_locators']=([{'kind':'pdf-block','document_id':code,'block_id':bid,'pdf_page':int(re.search(r':p(\d+):',bid)[1]),'block_sha256':digest,'source_pdf_sha256':pub['source_pdf_sha256']} for bid,digest in section.get('source_block_fingerprints',{}).items()] if code=='G226' else [{'kind':'pdf-page','document_id':code,'pdf_page':int(page),'page_sha256':digest,'source_pdf_sha256':pub['source_pdf_sha256']} for page,digest in section['source_page_sha256'].items()])
  out=C/'supplementary'/ (code+'.json');dump(out,pub);out.with_suffix('.md').write_text(p.with_suffix('.md').read_text().replace('../work/supplementary/','../maintenance/work/supplementary/'))
  entries.append({'document_id':code,'publication_role':review['publication_role'],'json':str(out.relative_to(C)),'markdown':str(out.with_suffix('.md').relative_to(C)),'numbered_sections':len(pub['sections']),'figures':len(pub['figures']),'tables':len(pub['tables']),'sha256':sha(out),'translation_status':pub['translation_status']})
  for s in pub['sections']:
   sid=s.get('section_id',s.get('id'));graph['nodes'].append({'id':sid,'kind':'source-section','document_id':code,'title':s.get('title_en',s.get('title_zh'))})
   for i,t in enumerate(chunks(json.dumps(s,ensure_ascii=False)),1):retrieval.append({'id':sid+':c'+str(i),'parent_record_id':sid,'document_id':code,'language':'zh','content_role':'current-supplementary-analysis','text':t,'source_path':str(out.relative_to(C)),'source_locators':s['source_locators'],'translation_status':pub['translation_status']})
  for issue in pub.get('source_issues',[]):issues.append({'document_id':code,**issue})
 for r in retrieval:r['source_sha256']=sha(C/r['source_path'])
 dump(C/'architecture/source-method-graph.json',graph);dump(C/'quality/extended-source-issues.json',issues)
 (C/'retrieval/extended-chunks.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in retrieval))
 report={'schema_version':'extended-publication/1','documents':entries,'counts':{'documents':len(entries),'sections':sum(e['numbered_sections'] for e in entries),'figures':sum(e['figures'] for e in entries),'tables':sum(e['tables'] for e in entries),'retrieval_chunks':len(retrieval),'source_issues':len(issues),'graph_nodes':len(graph['nodes']),'graph_edges':len(graph['edges'])},'checks':checks,'passed':all(x['passed'] for x in checks),'translation_complete':False,'body_authoring_complete':all(e['translation_status'] in {'separate-body-written-independent-review-pending','source-Chinese-preserved-with-corrections'} for e in entries),'limits_zh':['机械校验核对来源指纹、标题/源块/图表覆盖和关联目标；不能代替独立语义验收。','中文正文与语义分析分别发布；正文已写状态不代表不同评审人的最终校核通过。']}
 dump(C/'quality/extended-publication.json',report)
 lines=['# 基础标准与补充资料解析入口','','逐节语义分析、实际中文正文和不同评审人的校核状态分别记录。','','|资料|章节分析|图|表|中文正文状态|','|---|---:|---:|---:|---|']
 for e in entries:lines.append('|['+e['document_id']+'](../'+e['markdown']+')|'+str(e['numbered_sections'])+'|'+str(e['figures'])+'|'+str(e['tables'])+'|'+e['translation_status']+'|')
 lines+=['','表中状态是语义分析记录的性质；实际译写的中文正文及进度另见[中文正文索引](../fundamental/chinese-text/README.md)，不能据分析覆盖计数推定全文完成。','','[机器验证](extended-publication.json) · [跨文档关系](../architecture/source-method-graph.json) · [源文问题](extended-source-issues.json)','']
 (C/'quality/extended-publication.md').write_text('\n'.join(lines))
 import bind_foundation_contracts
 bind_foundation_contracts.main()
 import link_execution_graph
 link_execution_graph.main()
 final_graph=read(C/'architecture/source-method-graph.json')
 report['counts'].update(graph_nodes=len(final_graph['nodes']),graph_edges=len(final_graph['edges']))
 dump(C/'quality/extended-publication.json',report)
 import publish_chinese_texts
 publish_chinese_texts.main()
 import publish_supplementary_chinese
 publish_supplementary_chinese.main()
 print(report['counts'])
if __name__=='__main__':main()
