# -*- coding: utf-8 -*-
"""Publish authored G226 body by section, preserving every exact PDF source block.

Chinese paragraphs are section-aligned, not a claim of word-for-word equivalence
with each small PDF text box. W242C is already a Chinese source and is not
retranslated. No network or external writes are used.
"""
from pathlib import Path
import json, re, hashlib
C=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
 src=C/'maintenance/work/supplementary/G226-blocks.json'
 draft=C/'maintenance/chinese-text-data/supplementary/G226.txt'
 doc=json.loads(src.read_text());review=json.loads((C/'supplementary/G226.json').read_text())
 parts=re.split(r'^@@ ([0-9.]+)\n',draft.read_text(),flags=re.M)
 tr={parts[i]:parts[i+1].strip() for i in range(1,len(parts),2)}
 assert len(tr)==(len(parts)-1)//2 and set(tr)=={s['section_number'] for s in doc['sections']}
 bm={b['id']:b for b in doc['blocks']};sections=[];chunks=[]
 out=C/'supplementary/chinese-text/G226.json'
 lines=['# G226：敏捷企业架构师实践手册——中文正文','',
 '依据本地2022年Version 1.0逐节译写；不是官方中文译本。保留原文全部来源块、物理页码及指纹，中文按节连续表述，不声称与每个PDF文本框逐句一一对应。独立于作者的最终语义验收待完成。', '',
 '[语义分析](../G226.md) · [中英来源对照](G226.json)','',
 '编号正文范围为第1—5章，物理第11—45页；前置版权、作者及书目保留于原始PDF和抽取记录。重复页眉页脚在中文连续正文中省略，原始块仍保留。图像使用本地原图渲染，不能将作者经验、示例原则或层级组织法当作当前企业的批准事实。','']
 assigned=set()
 for s in doc['sections']:
  n=s['section_number'];sid='G226:'+n;body=tr[n]
  assert re.search('[\u3400-\u9fff]',body)
  locs=[];blocks=[]
  for bid in s['source_block_ids']:
   b=bm[bid];assert hashlib.sha256(b['text_en'].encode()).hexdigest()==b['text_sha256']
   loc={'kind':'pdf-block','document_id':'G226','block_id':bid,'pdf_page':b['pdf_page'],'bbox':b['bbox'],'block_sha256':b['text_sha256'],'fingerprint_scheme':'text-utf8','source_pdf_sha256':doc['source_sha256']}
   locs.append(loc);blocks.append({'id':bid,'text_en':b['text_en'],'source_locator':loc});assigned.add(bid)
  figures=[f for f in review['figures'] if f['source_section_id']==sid]
  for f in figures:assert sha(C/f['render_path'])==f['render_sha256']
  row={'id':sid,'section_number':n,'title_en':s['title_en'],'text_zh':body,'origin':'project-authored-Chinese-translation','translation_alignment':'section','source_block_ids':s['source_block_ids'],'source_blocks':blocks,'source_locators':locs,'pdf_pages':s['pdf_pages'],'figures':figures,'author_review_status':'source-aligned','independent_review_status':'pending'}
  sections.append(row)
  lines+=['<a id="sec-'+n.replace('.','-')+'"></a>','## '+body.split('\n',1)[0],'',body.partition('\n')[2].strip(),'']
  for f in figures:lines+=['![原图'+str(f['figure_number'])+'](../../'+f['render_path']+')','',f['caption_en'],'']
  lines+=['来源：PDF物理页 '+', '.join(map(str,s['pdf_pages']))+'；'+', '.join(s['source_block_ids']),'','<details><summary>完整英文来源块（包括原始页眉页脚）</summary>','']
  for b in blocks:lines+=[b['id']+'：'+b['text_en'],'']
  lines+=['</details>','']
  chunks.append({'id':sid+':Chinese-body','parent_record_id':sid,'document_id':'G226','language':'zh','content_role':'current-source-bound-Chinese-body','text':s['title_en']+'\n'+body,'source_path':str(out.relative_to(C)),'source_locators':locs,'translation_status':'body-written-source-aligned-independent-review-pending'})
 # Prove that the section partition did not silently omit any numbered body box.
 first=min(bm[bid]['normalized_start'] for bid in assigned)
 last=max(bm[bid]['normalized_end'] for bid in assigned)
 unassigned=[b['id'] for b in doc['blocks'] if b['normalized_start']>=first and b['normalized_end']<=last and b['text_en'].strip() and b['id'] not in assigned]
 assert not unassigned,unassigned
 result={'schema_version':'source-bound-supplementary-Chinese-body/1','document_id':'G226','source_version':review['source_version'],'official_translation':False,'source_extraction_path':str(src.relative_to(C)),'source_extraction_sha256':sha(src),'source_pdf_sha256':doc['source_sha256'],'authoring_path':str(draft.relative_to(C)),'authoring_sha256':sha(draft),'status':'body-written-source-aligned-independent-review-pending','body_complete':True,'sections':sections,'coverage':{'body_sections':len(sections),'unique_source_blocks':len(assigned),'source_figures_preserved':sum(len(s['figures']) for s in sections),'unassigned_body_blocks':unassigned},'limits_zh':['中文按节译写，不将段落合并或压缩表达当作经不同评审人逐句认证。','W242C已经是中文原件，原文保全与校释另存；不重新翻译为伪官方版本。']}
 dump(out,result);out.with_suffix('.md').write_text('\n'.join(lines)+'\n')
 for r in chunks:r['source_sha256']=sha(out)
 (C/'retrieval/supplementary-chinese-chunks.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in chunks))
 gp=C/'architecture/source-method-graph.json'
 graph=json.loads(gp.read_text());old={n['id'] for n in graph['nodes'] if n.get('kind')=='authored-Chinese-body' and n.get('document_id')=='G226'}
 graph['nodes']=[n for n in graph['nodes'] if n['id'] not in old];graph['edges']=[e for e in graph['edges'] if e['source'] not in old and e['target'] not in old]
 for r in chunks:
  graph['nodes'].append({'id':r['id'],'kind':'authored-Chinese-body','document_id':'G226','source_path':r['source_path'],'origin':'project-authored-translation','independent_review':'pending'})
  graph['edges'].append({'source':r['id'],'target':r['parent_record_id'],'relation':'project-translation-of','origin':'project-authored-translation','evidence_block_ids':[l['block_id'] for l in r['source_locators']]})
 ids={n['id'] for n in graph['nodes']};assert len(ids)==len(graph['nodes']) and all(e['source'] in ids and e['target'] in ids for e in graph['edges'])
 dump(gp,graph)
 for name in ['quality/execution-bridge.json','quality/extended-publication.json']:
  p=C/name
  if p.exists():
   d=json.loads(p.read_text());keys=('nodes','edges') if 'execution-bridge' in name else ('graph_nodes','graph_edges');d['counts'].update({keys[0]:len(graph['nodes']),keys[1]:len(graph['edges'])});dump(p,d)
 dump(C/'quality/supplementary-chinese-body-verification.json',{'schema_version':'supplementary-Chinese-body-verification/1','passed':True,'counts':result['coverage'],'input_sha256':{str(src.relative_to(C)):sha(src),str(draft.relative_to(C)):sha(draft),str(out.relative_to(C)):sha(out)},'independent_semantic_acceptance':'pending','scope_zh':'覆盖与来源指纹校验；不是不同评审人的语义认证。'})
 # Preserve W242C as the Chinese source it is. Corrections stay in analysis,
 # and never silently replace the exact extracted wording or copyright page.
 ws=C/'maintenance/work/supplementary/W242C-source.json';wd=json.loads(ws.read_text())
 wout=out.parent/'W242C-source.json';pages=[]
 wl=['# W242C：企业领导者人工智能指南——本地中文原文','',
     '2025年4月中文白皮书。以下逐页保留本地PDF抽取文字，不是重新翻译或改写；版式、图和扫描封面以原始PDF为准。原文中的术语及印刷问题不在本页默改，见[逐节校释和来源问题](../W242C.md)。', '']
 for page in wd['pages']:
  n=page['pdf_page'];text=page['text'];digest=hashlib.sha256(text.encode()).hexdigest()
  pages.append({'id':'W242C:p%04d'%n,'pdf_page':n,'text_zh':text,'text_sha256':digest,'source_locator':{'kind':'pdf-page','document_id':'W242C','pdf_page':n,'page_sha256':digest,'source_pdf_sha256':wd['sha256']}})
  wl+=['<a id="page-'+str(n)+'"></a>','## PDF物理页'+str(n),'',text or '本页无可提取文字；图像内容保留于PDF。','']
 dump(wout,{'schema_version':'preserved-Chinese-source/1','document_id':'W242C','publication_role':'white-paper','source_version':'2025-04 Chinese edition','source_extraction_path':str(ws.relative_to(C)),'source_extraction_sha256':sha(ws),'source_pdf_sha256':wd['sha256'],'pages':pages,'status':'exact-local-Chinese-extraction-preserved','translation_performed':False,'semantic_corrections_path':'supplementary/W242C.json'})
 wout.with_suffix('.md').write_text('\n'.join(wl)+'\n')
 (out.parent/'README.md').write_text('# 补充资料中文正文\n\n- [G226中文正文](G226.md)：75节、764个精确英文来源块、8张原图。按节连续译写；不同评审人的最终校核待完成。\n- [W242C本地中文原文](W242C-source.md)：逐页保全抽取文字，不重新翻译、不默改。图像及版式仍以PDF为准；术语校释见[语义分析](../W242C.md)。\n')
 print(result['coverage'])
if __name__=='__main__':main()
