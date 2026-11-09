# -*- coding: utf-8 -*-
"""Query only the portable package's current, source-bound interpretation corpus."""
from pathlib import Path
import argparse,json,re,math,collections,hashlib
from source_closure import SourceResolver
ROOT=Path(__file__).resolve().parents[1];CORPUS=ROOT/'corpus'
def resolve_source(logical,expected_sha256=None):
 return SourceResolver(CORPUS).resolve(logical,expected_sha256)

def terms(text):
 out=re.findall(r'[A-Za-z][A-Za-z0-9_-]*|[\u3400-\u9fff]+',text.lower());tokens=[]
 for token in out:
  tokens.append(token)
  if re.search('[\u3400-\u9fff]',token) and len(token)>2:tokens.extend(token[i:i+2] for i in range(len(token)-1))
 return list(dict.fromkeys(tokens))
def query(q,limit=8,document=None):
 qs=terms(q);matches=[];resolver=SourceResolver(CORPUS)
 diagram_index=CORPUS/'architecture/diagrams/index.json'
 current_diagrams={r['id'] for r in json.loads(diagram_index.read_text())['diagrams']} if diagram_index.is_file() and (CORPUS/'retrieval/architecture-chunks.jsonl').is_file() else set()
 for p in sorted((CORPUS/'retrieval').glob('*.jsonl')):
  if CORPUS.resolve() not in p.resolve().parents:raise ValueError('Retrieval index escapes package')
  with p.open() as stream:
   for line in stream:
    r=json.loads(line)
    # Raw extraction retains historical interpretations for audit; default
    # package retrieval must prefer the current, reviewed diagram projection.
    if r.get('content_role')=='figure' and any(fid in current_diagrams for fid in r.get('figure_ids',[])):continue
    if document and document not in r.get('document_ids',[r.get('document_id')]):continue
    text=r['text'].lower();counts=[text.count(t) for t in qs];score=sum(1+math.log1p(n) for n in counts if n)
    if not score:continue
    # Literal phrases are valuable for Chinese multiword architecture terms.
    score+=sum(2 for t in qs if len(t)>2 and t in text)
    path=r.get('source_path','');path=path.removeprefix('togaf-standard-10th-ai/') if hasattr(path,'removeprefix') else re.sub('^togaf-standard-10th-ai/','',path)
    resolved=resolver.resolve(path,r.get('source_sha256'))
    quality=r.get('quality',{})
    matches.append({'id':r['id'],'score':round(score,3),'document_id':r.get('document_id'),'source_path':path,'source_exists_in_package':resolved['exists'],'source_available':resolved['source_available'],'resolved_source':resolved,'source_sha256':r.get('source_sha256'),'source_locators':r.get('source_locators',[]),'content_role':r.get('content_role'),'translation_status':r.get('translation_status') or quality.get('status'),'quality':quality,'semantic_acceptance':'not-established-by-source-accessibility','excerpt':r['text'][:1300]})
 return sorted(matches,key=lambda x:(-x['score'],x['id']))[:limit]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('query');p.add_argument('--limit',type=int,default=8);p.add_argument('--document');a=p.parse_args();print(json.dumps({'query':a.query,'matches':query(a.query,a.limit,a.document),'notice':'检索命中只是定位；读取来源块和相邻章节后作判断。'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
