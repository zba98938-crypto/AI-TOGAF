# -*- coding: utf-8 -*-
"""Check the current delivery against its seal without resealing stale bytes."""
from pathlib import Path
import hashlib,json,tarfile,sys,os,argparse
from seal_release import include
C=Path(__file__).resolve().parents[1];P=C/'skills';R=C/'release'
sys.path.insert(0,str(P/'_shared/scripts'))
from source_closure import verify_source_closure
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for data in iter(lambda:f.read(1024*1024),b''):h.update(data)
 return h.hexdigest()
def verify(release_dir=None):
 global R
 if release_dir is not None:R=Path(release_dir).resolve()
 seal=json.loads((P/'package-manifest.json').read_text());release=json.loads((R/'release-manifest.json').read_text());issues=[]
 expected={'skills/'+x['path']:x['sha256'] for x in seal['files']}
 current_paths={p.relative_to(P).as_posix() for p in P.rglob('*') if include(p,P)}
 sealed_paths={x['path'] for x in seal['files']}
 for path in sorted(current_paths-sealed_paths):issues.append('unsealed source file '+path)
 for path in sorted(sealed_paths-current_paths):issues.append('missing sealed source file '+path)
 for row in seal['files']:
  p=P/row['path']
  if not p.is_file() or sha(p)!=row['sha256']:issues.append('changed sealed file '+row['path'])
 expected['skills/package-manifest.json']=sha(P/'package-manifest.json')
 if expected['skills/package-manifest.json']!=release['package_manifest_sha256']:issues.append('package manifest changed after sealing')
 for key in ['package','optional_node_dependencies']:
  item=release[key];path=R/item['path']
  if not path.is_file() or sha(path)!=item['sha256']:issues.append('changed archive '+item['path'])
 dependency_manifest=R/release['optional_node_dependencies']['manifest']
 if not dependency_manifest.is_file() or sha(dependency_manifest)!=release['optional_node_dependencies']['manifest_sha256']:
  issues.append('changed dependency manifest')
 else:
  dependencies=json.loads(dependency_manifest.read_text())
  if sha(P/'_shared/package-lock.json')!=dependencies['lockfile_sha256']:
   issues.append('dependency archive was prepared for a different lockfile')
 archive=R/release['package']['path'];actual={}
 with tarfile.open(archive,'r:gz') as tf:
  for item in tf:
   if not item.isfile():continue
   if item.name in actual or item.name.startswith('/') or '..' in Path(item.name).parts:issues.append('unsafe or duplicate archive member '+item.name)
   h=hashlib.sha256();f=tf.extractfile(item)
   for data in iter(lambda:f.read(1024*1024),b''):h.update(data)
   actual[item.name]=h.hexdigest()
 if actual!=expected:issues.append('archive differs from current sealed file set')
 source_map=json.loads((P/'_shared/corpus/source-map.json').read_text())
 closure=verify_source_closure(P/'_shared/corpus')
 for row in closure['issues']:issues.append('retrieval source closure '+json.dumps(row,ensure_ascii=False,sort_keys=True))
 inputs={'skills/'+x['path']:x['sha256'] for x in seal['files']}
 release_prefix=Path(os.path.relpath(R.resolve(),C.resolve())).as_posix()+'/'
 inputs.update({'skills/package-manifest.json':sha(P/'package-manifest.json'),release_prefix+'release-manifest.json':sha(R/'release-manifest.json'),
                release_prefix+release['package']['path']:release['package']['sha256'],
                release_prefix+release['optional_node_dependencies']['path']:release['optional_node_dependencies']['sha256'],
                release_prefix+release['optional_node_dependencies']['manifest']:release['optional_node_dependencies']['manifest_sha256']})
 report={'schema_version':'release-current-validation/4','passed':not issues,'counts':{'sealed_files_checked':len(seal['files']),'current_source_files':len(current_paths),'archives_checked':2,'source_map_files_checked':len(set(source_map['logical_paths'].values())),'issues':len(issues)},'issues':issues,'retrieval_source_closure':{'passed':closure['passed'],'counts':closure['counts'],'issues':closure['issues']},'input_sha256':inputs,
         'input_file_sets':[{'root':'skills','exclude_parts':['node_modules','__pycache__','.DS_Store','.git','.venv'],
                            'exclude_root_parts':['work'],'exclude_files':['package-manifest.json'],
                            'exclude_suffixes':['.pyc','.log'],'exclude_symlinks':True,
                            'paths_sha256':hashlib.sha256('\n'.join(sorted(sealed_paths)).encode()).hexdigest()}],
         'scope_zh':'当前源码文件集合及字节、实际归档、依赖锁文件及来源映射一致；不增加语义验收或组织批准结论。'}
 return report
def main(release_dir=None,out=None):
 target=Path(out) if out is not None else C/'quality/release-current-validation.json'
 if target.exists():raise ValueError('Report path must be new; previous evidence is immutable: '+str(target))
 report=verify(release_dir);issues=report['issues']
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts']);print(issues);return int(bool(issues))
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--release-dir',type=Path);parser.add_argument('--out',type=Path)
 args=parser.parse_args()
 raise SystemExit(main(args.release_dir,args.out))
