# -*- coding: utf-8 -*-
"""Materialize the portable source closure, preserving source bytes and logical IDs."""
from pathlib import Path
import json,hashlib,shutil,re
from source_paths import resolve as source_path
C=Path(__file__).resolve().parents[1];P=C/'skills';S=P/'_shared';D=S/'corpus'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def copy(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True)
 if not dst.exists() or sha(src)!=sha(dst):shutil.copy2(src,dst)
def main():
 mapping={};missing=[]
 for name in ['documents','tables','figures','fundamental/web-2025/volumes','maintenance/fundamental-review-data','maintenance/supplementary-review-data','maintenance/chapter-review-data','maintenance/chinese-text-data']:
  for src in sorted((C/name).rglob('*')):
   if src.is_file() and src.name not in {'.DS_Store'}:
    rel=src.relative_to(C).as_posix();copy(src,D/rel);mapping[rel]=rel;mapping[C.name+'/'+rel]=rel
 for name in ['architecture/roles/skills.json','index.json','quality/chinese-body-author-review.json','quality/chinese-body-author-review-additions.json','quality/adm-body-author-review.json','quality/chinese-body-author-review-final-volumes.json','quality/g226-body-author-review.json','quality/chinese-body-verification.json','quality/supplementary-chinese-body-verification.json','maintenance/cases/omnichannel/raw-business-materials.md','maintenance/cases/omnichannel/adm-business-materials.md','maintenance/cases/omnichannel/role-skill-inputs.json','maintenance/pipeline/architecture-diagram-reviews.json']:
  src=C/name;copy(src,D/name);mapping[C.name+'/'+name]=name;mapping[name]=name
 docs=json.loads((C/'index.json').read_text())['documents']
 for r in docs:
  src=source_path(C.parent/r['source']['path']);dst='sources/pdf/'+src.name
  if not src.is_file():missing.append(str(src));continue
  assert sha(src)==r['source']['sha256'];copy(src,D/dst);mapping[r['source']['path']]=dst
 for code in ['G226','W242C']:
  r=json.loads((C/'supplementary'/f'{code}.json').read_text());src=source_path(C/r['source_path']);dst='sources/pdf/'+src.name
  assert sha(src)==r['source_pdf_sha256'];copy(src,D/dst);mapping[r['source_path']]=dst;mapping[src.name]=dst
  rel=r['source_extraction_path'];copy(C/rel,D/rel);mapping[rel]=rel
 # Readable evidence locators retain their historical IDs, resolved through this map.
 for src in sorted(D.rglob('*')):
  if not src.is_file() or src.name=='source-map.json':continue
  rel=src.relative_to(D).as_posix();mapping.setdefault(rel,rel);mapping.setdefault(C.name+'/'+rel,rel)
 report={'schema_version':'portable-source-map/1','path_base':'corpus/','logical_paths':dict(sorted(mapping.items())),'missing_required_sources':missing,'notice_zh':'历史来源路径仅是身份；包内通过本映射定位同字节副本，不访问原项目。网页按卷/锚点/块定位，不生成PDF页码。'}
 (D/'source-map.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 vendor=S/'vendor';licenses=[]
 for p in sorted(vendor.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:licenses.append({'path':p.relative_to(S).as_posix(),'sha256':sha(p)})
 (S/'vendor-manifest.json').write_text(json.dumps({'origin':'existing local Python installation; byte-preserved copy','files':licenses,'license_files':[r['path'] for r in licenses if 'license' in r['path'].lower()]},indent=2)+'\n')
 assert not missing,missing
 print({'logical_paths':len(mapping),'source_files':len({v for v in mapping.values()}),'missing':missing,'vendor_files':len(licenses)})
if __name__=='__main__':main()
