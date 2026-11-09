# -*- coding: utf-8 -*-
"""Materialize the portable source closure, preserving source bytes and logical IDs."""
from pathlib import Path
import json,hashlib,shutil,re,sys
from source_paths import resolve as source_path
C=Path(__file__).resolve().parents[1];P=C/'skills';S=P/'_shared';D=S/'corpus'
sys.path.insert(0,str(S/'scripts'))
from source_closure import source_requirements, require_source_closure
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def copy(src,dst,expected=None):
 src=src.resolve();dst=dst.resolve()
 if C.resolve() not in src.parents or D.resolve() not in dst.parents:
  raise ValueError('Source copy escapes approved local roots: '+str(src)+' -> '+str(dst))
 if not src.is_file():raise ValueError('Required source file missing: '+str(src))
 if expected is not None and sha(src)!=expected:raise ValueError('Source fingerprint mismatch: '+str(src))
 dst.parent.mkdir(parents=True,exist_ok=True)
 if not dst.exists() or sha(src)!=sha(dst):shutil.copy2(src,dst)

def indexed_source(logical,expected,relocation):
 """Resolve retained identities and verify both migration and index fingerprints."""
 base=logical.partition('#')[0]
 local=relocation.get('logical_paths',{}).get(base)
 migration=next((r for r in relocation.get('files',[]) if r['old_path']==base),None)
 if local is None:local=base.removeprefix(C.name+'/')
 if not isinstance(local,str) or Path(local).is_absolute() or '..' in Path(local).parts or ':' in local or '\\' in local:
  raise ValueError('Indexed source path escapes project: '+logical)
 src=(C/local).resolve()
 if C.resolve() not in src.parents or not src.is_file():
  raise ValueError('Indexed source missing or outside project: '+logical)
 if migration and (migration['local_path']!=local or migration['sha256']!=expected):
  raise ValueError('Migration/index fingerprint conflict: '+logical)
 if sha(src)!=expected:raise ValueError('Indexed source fingerprint mismatch: '+logical)
 prefix='skills/_shared/corpus/'
 destination=local.removeprefix(prefix) if local.startswith(prefix) else local
 return src,destination

def main():
 mapping={};missing=[]
 requirements=source_requirements(C)
 if requirements['issues']:raise ValueError('Invalid retrieval requirements: '+json.dumps(requirements['issues']))
 relocation=json.loads((C/'sources/relocation-manifest.json').read_text())
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
  copy(src,D/dst,r['source']['sha256']);mapping[r['source']['path']]=dst
 for code in ['G226','W242C']:
  r=json.loads((C/'supplementary'/f'{code}.json').read_text());src=source_path(C/r['source_path']);dst='sources/pdf/'+src.name
  copy(src,D/dst,r['source_pdf_sha256']);mapping[r['source_path']]=dst;mapping[src.name]=dst
  rel=r['source_extraction_path'];copy(C/rel,D/rel);mapping[rel]=rel
 # Fixed publication directories are only supporting material. The authoritative
 # required set comes from every record in every current retrieval index.
 for logical,entry in sorted(requirements['requirements'].items()):
  src,dst=indexed_source(logical,entry['sha256'],relocation)
  copy(src,D/dst);mapping[logical.partition('#')[0]]=dst
  if logical.startswith(C.name+'/'):mapping.setdefault(logical.removeprefix(C.name+'/'),dst)
 # Readable evidence locators retain their historical IDs, resolved through this map.
 for src in sorted(D.rglob('*')):
  if not src.is_file() or src.name=='source-map.json':continue
  if D.resolve() not in src.resolve().parents:raise ValueError('Package source symlink escapes corpus: '+str(src))
  rel=src.relative_to(D).as_posix();mapping.setdefault(rel,rel);mapping.setdefault(C.name+'/'+rel,rel)
 report={'schema_version':'portable-source-map/2','path_base':'corpus/','logical_paths':dict(sorted(mapping.items())),
         'file_sha256':{rel:sha(D/rel) for rel in sorted(set(mapping.values()))},
         'retrieval_index_sha256':requirements['index_sha256'],'required_source_count':len(requirements['requirements']),
         'missing_required_sources':missing,'notice_zh':'历史来源路径仅是身份；包内通过本映射定位同字节副本，不访问原项目。网页按卷/锚点/块定位，不生成PDF页码。来源可达和指纹一致不授予译文或语义验收。'}
 (D/'source-map.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 closure=require_source_closure(D)
 vendor=S/'vendor';licenses=[]
 for p in sorted(vendor.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:licenses.append({'path':p.relative_to(S).as_posix(),'sha256':sha(p)})
 (S/'vendor-manifest.json').write_text(json.dumps({'origin':'existing local Python installation; byte-preserved copy','files':licenses,'license_files':[r['path'] for r in licenses if 'license' in r['path'].lower()]},indent=2)+'\n')
 assert not missing,missing
 print({'logical_paths':len(mapping),'source_files':len({v for v in mapping.values()}),'missing':missing,'vendor_files':len(licenses),'retrieval_source_closure':closure['counts']})
if __name__=='__main__':main()
