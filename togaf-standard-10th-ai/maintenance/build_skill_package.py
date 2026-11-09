# -*- coding: utf-8 -*-
"""Refresh local corpus bindings in the single maintained skills tree.

The initial upstream copy is retired. Its manifest remains historical provenance;
refreshing must never recreate or read a second workspace skills tree.
"""
from pathlib import Path
import json,shutil,hashlib,os,re
C=Path(__file__).resolve().parents[1];DEST=C/'skills'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ignore(path,names):return [n for n in names if n in {'node_modules','__pycache__','.DS_Store','.git','.venv','generated'} or n.endswith(('.pyc','.log'))]
def main():
 if not (DEST/'_shared/scripts/local_tool.py').is_file():
  raise SystemExit('Canonical skills package missing; restore it rather than create a second version.')
 shared=DEST/'_shared';corpus=shared/'corpus';corpus.mkdir(exist_ok=True)
 for name in ['chapters','architecture/roles','architecture/guides','architecture/diagrams','architecture/adm-flow','fundamental/analysis','fundamental/chinese-text','supplementary']:
  src=C/name
  if src.exists():shutil.copytree(src,corpus/name,dirs_exist_ok=True,ignore=ignore)
 for name in ['retrieval/chapter-chunks.jsonl','retrieval/architecture-chunks.jsonl','retrieval/extended-chunks.jsonl','retrieval/chinese-chunks.jsonl','retrieval/supplementary-chinese-chunks.jsonl','architecture/source-method-graph.json','quality/extended-source-issues.json','quality/extended-publication.json']:
  src=C/name;target=corpus/name
  if src.exists():target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target)
 # The portable reader ships diagram artifacts, while optional renderer logs
 # remain with the original execution evidence. Record this derivation rather
 # than publish a manifest whose output hash points to an excluded log.
 source_flow=C/'architecture/adm-flow/manifest.json'
 portable_flow=corpus/'architecture/adm-flow/manifest.json'
 if source_flow.is_file():
  flow=json.loads(source_flow.read_text());omitted={}
  for name in list(flow['output_sha256']):
   if name.endswith('.log'):
    omitted[name]=flow['output_sha256'].pop(name)
  flow['portable_derivation']={'source_manifest_sha256':sha(source_flow),'omitted_optional_logs':omitted}
  portable_flow.write_text(json.dumps(flow,ensure_ascii=False,indent=2)+'\n')
 # Rebind the executable contracts to the current reviewed foundation sources.
 import bind_foundation_contracts
 bind_foundation_contracts.main()
 for p in DEST.glob('togaf-*/SKILL.md'):
  text=p.read_text();marker='## 本地解析与证据入口'
  if marker not in text:
   text+='\n\n'+marker+'\n\n先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。\n'
   p.write_text(text)
 # Keep the original upstream hashes and manifest untouched. seal_release.py
 # records current local hashes when publishing a new engineering archive.
 print({'skills':len(list(DEST.glob('togaf-*/SKILL.md'))),'canonical_directory':'togaf-standard-10th-ai/skills','upstream_manifest':'preserved-historical-provenance'})
if __name__=='__main__':main()
