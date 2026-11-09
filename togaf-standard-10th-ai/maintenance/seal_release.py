# -*- coding: utf-8 -*-
"""Seal a local engineering preview; archive integrity is not semantic completion."""
from pathlib import Path
import json,hashlib,tarfile,platform,sys,datetime,os,subprocess,posixpath
C=Path(__file__).resolve().parents[1];P=C/'skills';R=C/'release'
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
def main():
 R.mkdir(exist_ok=True)
 body=json.loads((C/'fundamental/chinese-text/index.json').read_text())
 source_manifest=json.loads((C/'fundamental/web-2025/manifest.json').read_text())
 completed={v['volume_id'] for v in body['volumes'] if v['volume_body_complete']}
 remaining=[v['id'].split(':')[-1] for v in source_manifest['documents'] if v['id'].split(':')[-1] not in completed]
 upath=P/'upstream-manifest.json';snapshot=json.loads(upath.read_text())
 for item in snapshot['files']:
  local=P/item['path'];item['local_sha256']=sha(local) if local.is_file() else None
 snapshot['local_hashes_recorded_at']='release sealing; original upstream hashes preserved'
 upath.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
 files=[{'path':p.relative_to(P).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(P.rglob('*')) if include(p)]
 upstream=json.loads((P/'upstream-manifest.json').read_text());old={x['path']:x for x in upstream['files']};patches=[]
 for f in files:
  if f['path'] in old and f['sha256']!=old[f['path']]['upstream_sha256']:patches.append({'path':f['path'],'upstream_sha256':old[f['path']]['upstream_sha256'],'local_sha256':f['sha256']})
 manifest={'schema_version':'portable-package-seal/1','release_status':'engineering-delivered-final-review-pending','all_plan_items_complete':False,'files':files,'file_count':len(files),'bytes':sum(f['bytes'] for f in files),'skills':upstream['skills'],'upstream_file_count':len(old),'local_modifications':patches,'added_file_count':sum(f['path'] not in old for f in files),'excluded_zh':'顶层work、node_modules、缓存及日志；嵌套corpus/maintenance/work中的来源抽取证据保留。','rights_zh':'保留各原件的版权、许可和指纹；本地打包不改变上游许可。','self_hash_omission_zh':'清单不包含自身哈希；归档清单另记录本文件哈希。'}
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
 report={'schema_version':'local-release/1','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':verified['passed'],'release_status':'engineering-delivered-final-review-pending','all_plan_items_complete':False,'package':{'path':archive.name,'sha256':sha(archive),'bytes':archive.stat().st_size,'verified_contents':verified},'optional_node_dependencies':{'path':dep_archive.name,'sha256':sha(dep_archive),'bytes':dep_archive.stat().st_size,'files':dep_count,'platform':sys.platform,'machine':platform.machine(),'manifest':'node-dependency-manifest.json','manifest_sha256':sha(R/'node-dependency-manifest.json')},'package_manifest_sha256':sha(P/'package-manifest.json'),'local_patch_count':len(patches),'installations_performed':[],'semantic_remaining':['remaining-foundation-volumes-full-Chinese-body','G226-full-Chinese-body','different-reviewer-final-semantic-acceptance'],'validation_scope_zh':'passed只表示归档内容与封存字节逐项一致，不表示全部计划或语义验收完成。'}
 report['body_translation_progress']=body['counts']
 report['foundation_body_remaining_volume_ids']=remaining
 gb=json.loads((C/'supplementary/chinese-text/G226.json').read_text())
 report['G226_body_progress']=gb['coverage']
 report['semantic_remaining']=(['remaining-foundation-volumes-full-Chinese-body'] if remaining else [])+([] if gb['body_complete'] else ['G226-full-Chinese-body'])+['different-reviewer-final-semantic-acceptance']
 (R/'release-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 (R/'README.md').write_text('''# TOGAF skills工程预览交付\n\n本目录交付可迁移工程包。六卷基础标准874个编号小节、3522个来源块，以及G226的75节中文正文均已译写，W242C中文原文逐页保全。不同评审人的最终语义验收仍待完成，真实业务批准未授予。\n\n- [skills源码、规范、字体及本地资料包](togaf-skills-engineering-preview.tar.gz)：17入口、共享执行器、当前来源和5版可编辑案例。不包含node_modules、Python环境或浏览器。\n- [归档指纹及校验结果](release-manifest.json)：源码归档每个文件与封存清单逐字节核对；原件版权、许可证和原始引用保留。\n- [实施证据与未完成项](../quality/implementation-ledger.md)。\n\n在目标目录解包：\n\n```bash\ntar -xzf togaf-skills-engineering-preview.tar.gz\ncd skills\npython3 -B _shared/scripts/local_tool.py doctor\n```\n\n可选离线Node依赖包名称、平台和SHA-256见归档清单，在同一目标目录解开，使其位于`skills/_shared/node_modules/`。该依赖包仅适用于本次macOS本机平台；Python依赖、Node运行时及Chrome/Chromium未随包提供。其他环境按[包内依赖说明](../skills/_shared/references/local-package.md)及锁文件准备。\n\n保留17个技能目录与`_shared/`同级。解包到任意自选位置不会自动注册为全局技能；本轮未向外部技能目录安装任何内容。所有运行输出放包内`work/`。\n\n隔离副本的检索、模型校验、生成与渲染证据见[迁移检查](../quality/portability-validation.json)。这证明已测试本机的路径独立性，不是所有平台的运行认证。\n''')
 print({'files':len(files),'patches':len(patches),'source_archive_bytes':archive.stat().st_size,'node_archive_bytes':dep_archive.stat().st_size,'passed':report['passed']})
if __name__=='__main__':main()
