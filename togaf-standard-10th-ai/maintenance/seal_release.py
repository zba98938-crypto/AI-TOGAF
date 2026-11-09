# -*- coding: utf-8 -*-
"""Seal a local engineering preview; archive integrity is not semantic completion."""
from pathlib import Path
import json,hashlib,tarfile,platform,sys,datetime,os,subprocess,posixpath,argparse
C=Path(__file__).resolve().parents[1];P=C/'skills';R=C/'release'
sys.path.insert(0,str(P/'_shared/scripts'))
from source_closure import require_source_closure
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def include(p,package_root=None):
 rel=p.relative_to(package_root or P)
 return p.is_file() and not p.is_symlink() and rel.as_posix()!='package-manifest.json' and rel.parts[0]!='work' and not any(x in {'node_modules','__pycache__','.DS_Store','.git','.venv'} for x in rel.parts) and p.suffix not in {'.pyc','.log'}
def verify_archive(archive,expected):
 actual={};issues=[]
 with tarfile.open(archive,'r:gz') as tf:
  for item in tf:
   if not item.isfile():continue
   name=item.name
   if name.startswith('/') or '..' in Path(name).parts:issues.append('unsafe '+name);continue
   f=tf.extractfile(item);h=hashlib.sha256()
   for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
   actual[name]=h.hexdigest()
 if actual!=expected:issues+=['archive-file-set-or-content-mismatch']
 return {'passed':not issues,'files':len(actual),'issues':issues}

def git_provenance():
 def read(*args):
  result=subprocess.run(['git',*args],cwd=C.parent,capture_output=True,text=True)
  return result.stdout.strip() if result.returncode==0 else None
 return {'current_revision':read('rev-parse','HEAD'),
         'baseline_revisions':(read('rev-list','--max-parents=0','HEAD') or '').splitlines(),
         'binding':'current source bytes below include uncommitted repairs; no remote configured or used'}

def record_build_provenance():
 """Append immutable local records; never rewrite the historical upstream seal."""
 upstream=P/'upstream-manifest.json';pointer=P/'build-provenance.json';history=P/'build-history'
 previous=None
 if pointer.exists():
  previous=json.loads(pointer.read_text())['record']
  item=previous;seen=set()
  while item is not None:
   relative=Path(item['path'])
   if relative.is_absolute() or '..' in relative.parts or (P/relative).resolve().parent!=history.resolve():
    raise ValueError('Previous build record escapes build history')
   if item['path'] in seen:raise ValueError('Build history cycle')
   seen.add(item['path'])
   if sha(P/relative)!=item['sha256']:raise ValueError('Previous build history changed')
   prior=json.loads((P/relative).read_text())
   if prior['historical_upstream']['sha256']!=sha(upstream):raise ValueError('Historical upstream changed')
   item=prior['previous_record']
 files={p.relative_to(P).as_posix():sha(p) for p in sorted(P.rglob('*'))
        if include(p) and p.relative_to(P).parts[0] not in {'build-history','build-provenance.json'}}
 record={'schema_version':'local-build-provenance/1',
         'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'git':git_provenance(),'previous_record':previous,
         'historical_upstream':{'path':'upstream-manifest.json','sha256':sha(upstream)},
         'source_files':files,
         'scope':'Byte-bound local repair chain; semantic acceptance and organization approval remain separate.'}
 data=(json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
 digest=hashlib.sha256(data).hexdigest();relative='build-history/'+digest+'.json';target=P/relative
 history.mkdir(exist_ok=True)
 if target.exists():
  if target.read_bytes()!=data:raise ValueError('Immutable build record collision')
 else:
  with target.open('xb') as stream:stream.write(data)
 current={'schema_version':'current-local-build-provenance/1','record':{'path':relative,'sha256':digest}}
 pointer.write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
 return current

def main(release_dir=None):
 global R
 if release_dir is not None:R=Path(release_dir).resolve()
 if R.exists():raise ValueError('Release directory must be new; previous archives are immutable: '+str(R))
 closure=require_source_closure(P/'_shared/corpus')
 provenance=record_build_provenance()
 R.mkdir(parents=True,exist_ok=False)
 body=json.loads((C/'fundamental/chinese-text/index.json').read_text())
 source_manifest=json.loads((C/'fundamental/web-2025/manifest.json').read_text())
 completed={v['volume_id'] for v in body['volumes'] if v['volume_body_complete']}
 remaining=[v['id'].split(':')[-1] for v in source_manifest['documents'] if v['id'].split(':')[-1] not in completed]
 files=[{'path':p.relative_to(P).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(P.rglob('*')) if include(p)]
 upstream=json.loads((P/'upstream-manifest.json').read_text());old={x['path']:x for x in upstream['files']};patches=[]
 for f in files:
  if f['path'] in old and f['sha256']!=old[f['path']]['upstream_sha256']:patches.append({'path':f['path'],'upstream_sha256':old[f['path']]['upstream_sha256'],'local_sha256':f['sha256']})
 manifest={'schema_version':'portable-package-seal/1','release_status':'engineering-preview-verification-pending','all_plan_items_complete':False,'files':files,'file_count':len(files),'bytes':sum(f['bytes'] for f in files),'skills':upstream['skills'],'upstream_file_count':len(old),'local_modifications':patches,'added_file_count':sum(f['path'] not in old for f in files),'excluded_zh':'顶层work、node_modules、缓存及日志；嵌套corpus/maintenance/work中的来源抽取证据保留。','rights_zh':'保留各原件的版权、许可和指纹；本地打包不改变上游许可。','self_hash_omission_zh':'清单不包含自身哈希；归档清单另记录本文件哈希。'}
 manifest['build_provenance']=provenance
 (P/'package-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 archive=R/'togaf-skills-engineering-preview.tar.gz';expected={}
 with tarfile.open(archive,'w:gz',compresslevel=6) as tf:
  for f in files+[{'path':'package-manifest.json'}]:
   p=P/f['path'];name='skills/'+f['path'];tf.add(p,arcname=name,recursive=False);expected[name]=sha(p)
 verified=verify_archive(archive,expected)
 # Native Node dependencies are a separate, explicitly platform-bound optional pack.
 deps=P/'_shared/node_modules';dep_archive=R/('togaf-node-dependencies-'+sys.platform+'-'+platform.machine()+'.tar.gz');dep_count=0;unsafe=[]
 with tarfile.open(dep_archive,'w:gz',compresslevel=6) as tf:
  for p in sorted(deps.rglob('*')):
   if p.name in {'.DS_Store','__pycache__'}:continue
   if p.is_symlink():
    target=p.resolve()
    if deps.resolve() not in target.parents:unsafe.append(p.relative_to(P).as_posix());continue
   if p.is_file() or p.is_symlink():tf.add(p,arcname='skills/'+p.relative_to(P).as_posix(),recursive=False);dep_count+=1
 assert not unsafe,unsafe
 dependency_paths={}
 # Stream-verify every dependency file and every symbolic link against local bytes.
 with tarfile.open(dep_archive,'r:gz') as tf:
  for item in tf:
   relative=Path(item.name).relative_to('skills');p=P/relative
   if item.issym():assert os.readlink(p)==item.linkname
   elif item.isfile():
    h=hashlib.sha256();stream=tf.extractfile(item)
    for b in iter(lambda:stream.read(1024*1024),b''):h.update(b)
    assert h.hexdigest()==sha(p),relative
   dependency_paths[relative.as_posix()]={'sha256':sha(p) if item.isfile() else None,'link_target':item.linkname if item.issym() else None,'bytes':item.size}
 (R/'node-dependency-manifest.json').write_text(json.dumps({'schema_version':'platform-node-dependencies/1','platform':sys.platform,'machine':platform.machine(),'lockfile_sha256':sha(P/'_shared/package-lock.json'),'files':dependency_paths,'notice_zh':'只验证本机依赖字节与链接；跨操作系统需按锁文件重新准备依赖。'},ensure_ascii=False,indent=2)+'\n')
 report={'schema_version':'local-release/1','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':verified['passed'],'release_status':'engineering-preview-verification-pending','all_plan_items_complete':False,'package':{'path':archive.name,'sha256':sha(archive),'bytes':archive.stat().st_size,'verified_contents':verified},'optional_node_dependencies':{'path':dep_archive.name,'sha256':sha(dep_archive),'bytes':dep_archive.stat().st_size,'files':dep_count,'platform':sys.platform,'machine':platform.machine(),'manifest':'node-dependency-manifest.json','manifest_sha256':sha(R/'node-dependency-manifest.json')},'package_manifest_sha256':sha(P/'package-manifest.json'),'local_patch_count':len(patches),'installations_performed':[],'semantic_remaining':['independent-material-unit-review-and-recheck','complete-UML-2.5.1-design-time-obligations','complete-BPMN-2.0.2-design-time-obligations','507-independent-current-version-Actor-scorer-cases','current-round-entrypoint-and-publication-verification','human-professional-acceptance','real-organization-signature'],'validation_scope_zh':'passed只表示归档内容与封存字节逐项一致，不表示全部计划或语义验收完成。'}
 report['body_translation_progress']=body['counts']
 report['retrieval_source_closure']={'passed':closure['passed'],'counts':closure['counts']}
 report['build_provenance']=provenance
 report['foundation_body_remaining_volume_ids']=remaining
 gb=json.loads((C/'supplementary/chinese-text/G226.json').read_text())
 report['G226_body_progress']=gb['coverage']
 report['semantic_remaining'].extend((['remaining-foundation-volumes-full-Chinese-body'] if remaining else [])+([] if gb['body_complete'] else ['G226-full-Chinese-body']))
 (R/'release-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 (R/'README.md').write_text('''# TOGAF skills工程预览交付\n\n本目录封存待验证的本地工程预览包；封存本身不宣称工程交付或标准能力已完成。六卷基础标准874个编号小节、3522个来源块，以及G226的75节中文正文均已译写，W242C中文原文逐页保全。独立模型逐项资料复核与复查、完整 UML/BPMN 设计时义务、当前版本 507 项评测及正式入口切换均须以本轮实际记录判定。人工专业验收与真实组织批准保持待签署。\n\n- [skills源码、规范、字体及本地资料包](togaf-skills-engineering-preview.tar.gz)：17入口、共享执行器、当前来源和5版可编辑案例。不包含node_modules、Python环境或浏览器。\n- [归档指纹及校验结果](release-manifest.json)：源码归档每个文件与封存清单逐字节核对；原件版权、许可证和原始引用保留。\n- 本轮实施证据与未完成项由显式轮次清单和总报告记录；历史 quality 台账不作为本归档的当前验收结论。\n\n在目标目录解包：\n\n```bash\ntar -xzf togaf-skills-engineering-preview.tar.gz\ncd skills\npython3 -B _shared/scripts/local_tool.py doctor\n```\n\n可选离线Node依赖包名称、平台和SHA-256见归档清单，在同一目标目录解开，使其位于`skills/_shared/node_modules/`。该依赖包仅适用于本次macOS本机平台；Python依赖、Node运行时及Chrome/Chromium未随包提供。其他环境按[包内依赖说明](../skills/_shared/references/local-package.md)及锁文件准备。\n\n保留17个技能目录与`_shared/`同级。解包到任意自选位置不会自动注册为全局技能；本轮未向外部技能目录安装任何内容。所有运行输出放包内`work/`。\n\n隔离副本的检索、模型校验、生成与渲染证据见[迁移检查](../quality/portability-validation.json)。这证明已测试本机的路径独立性，不是所有平台的运行认证。\n''')
 readme=R/'README.md';text=readme.read_text()
 for old,target in [('../quality/implementation-ledger.md',C/'quality/implementation-ledger.md'),
                    ('../skills/_shared/references/local-package.md',P/'_shared/references/local-package.md')]:
  text=text.replace(old,Path(os.path.relpath(target,R)).as_posix())
 text=text.replace('隔离副本的检索、模型校验、生成与渲染证据见[迁移检查](../quality/portability-validation.json)。这证明已测试本机的路径独立性，不是所有平台的运行认证。',
                   '本归档的隔离迁移检查由正式轮次调用 `verify_portability.py --release-dir <本目录> --run-dir <新解包目录> --out <新报告路径>` 保存。只有该轮实际执行结果可以支持本轮迁移结论；归档封存不授予语义验收或真实组织批准。')
 readme.write_text(text)
 print({'files':len(files),'patches':len(patches),'source_archive_bytes':archive.stat().st_size,'node_archive_bytes':dep_archive.stat().st_size,'passed':report['passed']})
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--release-dir',type=Path)
 args=parser.parse_args()
 main(args.release_dir)
