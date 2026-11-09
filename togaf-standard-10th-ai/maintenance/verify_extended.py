# -*- coding: utf-8 -*-
"""Verify current extended publication; no republishing during verification."""
from pathlib import Path
import hashlib,json,sys,re
from source_paths import resolve as source_path
C=Path(__file__).resolve().parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 checks=[]
 def check(ok,label):checks.append({'check':label,'passed':bool(ok)})
 report=read(C/'quality/extended-publication.json')
 for item in report['documents']:
  p=C/item['json'];d=read(p);check(sha(p)==item['sha256'],'published hash '+item['document_id'])
  if d['source_kind']=='web':
   src=C/d['source_document_path'];source=read(src);bm={b['id']:b for b in source['blocks']}
   for s in d['sections']:
    for loc in s['source_locators']:
     b=bm[loc['block_id']];check(loc['block_sha256']==hashlib.sha256(json.dumps(b,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'web locator '+s['id']+'/'+b['id']);check('pdf_page' not in loc,'web not assigned invented PDF page')
   body_path=d.get('separate_Chinese_body_path')
   body=read(C/body_path) if body_path else None
   check(d['translation_status']==('separate-body-written-independent-review-pending' if body and body.get('volume_body_complete') else 'not-complete-analysis-is-not-full-translation'),'translation scope '+d['volume_id'])
   if body:check(body['independent_semantic_acceptance']=='pending','body writing not promoted to independent acceptance '+d['volume_id'])
  else:
   check(sha(source_path(C/d['source_path']))==d['source_pdf_sha256'],'supplement source '+d['document_id']);check(sha(C/d['source_extraction_path'])==d['source_extraction_sha256'],'supplement extraction '+d['document_id'])
 # Independently read the published Chinese layer against canonical sources.
 # A missing section, stale quote or English body passed off as Chinese must
 # fail even if the publisher's own success report is present.
 body_index=read(C/'fundamental/chinese-text/index.json')
 for item in body_index['volumes']:
  body=read(C/item['json']);src=C/body['source_document_path'];original=read(src);bm={b['id']:b for b in original['blocks']}
  check(sha(C/item['json'])==item['sha256'],'Chinese body manifest '+item['volume_id'])
  check(sha(src)==body['source_document_sha256'],'Chinese original '+item['volume_id'])
  start=next(i for i,b in enumerate(original['blocks']) if re.fullmatch('h[2-6]',b['kind']) and re.match(r'^\d+\.',b['text_en']))
  check([b['source_block_id'] for b in body['blocks']]==[b['id'] for b in original['blocks'][start:]],'Chinese full block sequence '+item['volume_id'])
  for b in body['blocks']:
   check(b['text_en']==bm[b['source_block_id']]['text_en'],'exact English beside Chinese '+b['source_block_id'])
   check(bool(re.search('[\u3400-\u9fff]',b['text_zh'])),'nonempty Chinese body '+b['source_block_id'])
  check(body['independent_semantic_acceptance']=='pending','authoring not independent acceptance '+item['volume_id'])
 gb=read(C/'supplementary/chinese-text/G226.json');gs=read(C/gb['source_extraction_path']);bm={b['id']:b for b in gs['blocks']}
 check([s['id'] for s in gb['sections']]==['G226:'+s['section_number'] for s in gs['sections']],'G226 complete source section order')
 for s,canonical in zip(gb['sections'],gs['sections']):
  check(s['source_block_ids']==canonical['source_block_ids'],'G226 exact source assignment '+s['id'])
  for b in s['source_blocks']:check(b['text_en']==bm[b['id']]['text_en'],'G226 exact quote '+b['id'])
  for f in s['figures']:check(sha(C/f['render_path'])==f['render_sha256'],'G226 preserved figure '+f['figure_id'])
 wb=read(C/'supplementary/chinese-text/W242C-source.json');ws=read(C/wb['source_extraction_path'])
 check(len(wb['pages'])==len(ws['pages']),'W242C complete original page sequence')
 for page,original in zip(wb['pages'],ws['pages']):check(page['text_zh']==original['text'] and page['pdf_page']==original['pdf_page'],'W242C exact original page '+str(page['pdf_page']))
 graph=read(C/'architecture/source-method-graph.json');ids={n['id'] for n in graph['nodes']};check(len(ids)==len(graph['nodes']),'unique graph identities');check(all(e['source'] in ids and e['target'] in ids for e in graph['edges']),'graph endpoints closed');check(sum(e['relation']=='reference-proficiency' for e in graph['edges'])==426,'426 explicit matrix values')
 retrieval_ids=[]
 for name in ['extended-chunks.jsonl','chinese-chunks.jsonl','supplementary-chinese-chunks.jsonl']:
  for line in (C/'retrieval'/name).open():
   row=json.loads(line);retrieval_ids.append(row['id']);check(sha(C/row['source_path'])==row['source_sha256'],'retrieval source current '+row['id']);check(row['content_role'].startswith('current-'),'retrieval excludes historical role')
 check(len(retrieval_ids)==len(set(retrieval_ids)),'unique current extended and Chinese retrieval IDs')
 result={'schema_version':'extended-verification/1','passed':all(x['passed'] for x in checks),'counts':{'checks':len(checks),'failed':sum(not x['passed'] for x in checks)},'failures':[x for x in checks if not x['passed']],'limits_zh':['来源与结构一致性验证，不替代逐句中文校订及不同评审人的语义评审。']}
 (C/'quality/extended-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(result['counts']);return int(not result['passed'])
if __name__=='__main__':raise SystemExit(main())
