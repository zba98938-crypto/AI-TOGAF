# -*- coding: utf-8 -*-
"""Close relative Markdown reading dependencies; record every portable link rewrite."""
from pathlib import Path
import re,json,os,shutil,hashlib,sys
from urllib.parse import unquote
C=Path(__file__).resolve().parents[1];P=C/'skills';D=P/'_shared/corpus';changes=[];copied=[]
sys.path.insert(0,str(P/'_shared/scripts'))
from package_links import MARKDOWN_LINK_PATTERN as PATTERN, markdown_files
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def retained_figure_dependency(document,path):
 """Resolve only a chapter's explicitly identified retained translation assets."""
 if not path.startswith('figs/') or not document.is_relative_to(D):return None
 sidecar=document.with_suffix('.json')
 if not sidecar.is_file():return None
 legacy=json.loads(sidecar.read_text()).get('legacy_translation',{})
 if not legacy.get('path') or not legacy.get('sha256'):return None
 retained=(C/'sources/retained').resolve()
 original=(retained/legacy['path']).resolve()
 if retained not in original.parents or not original.is_file() or sha(original)!=legacy['sha256']:return None
 source=(original.parent/path).resolve()
 if retained not in source.parents or not source.is_file():return None
 return source,D/'sources/retained'/source.relative_to(retained)

def main():
 changes.clear();copied.clear()
 previous_path=P/'reading-link-manifest.json'
 previous=json.loads(previous_path.read_text()) if previous_path.exists() else {}
 # Earlier versions replaced the manifest on each verification. Recover only
 # comparisons that can still be proved against an existing byte-fingerprinted
 # source; do not manufacture an execution history for that earlier run.
 recovered=[]
 for p in markdown_files(P,excluded_top_level={'work'}):
  rel=p.relative_to(P)
  if D.resolve() in p.resolve().parents:
   logical=p.relative_to(D);base=(C.parent/'tools/togaf_corpus'/logical.relative_to('source-tools')) if logical.parts[0]=='source-tools' else C/logical
  else:base=P/rel  # One maintained skills tree; upstream comparisons are historical.
  if not base.is_file() or base.resolve()==p.resolve():continue
  old=list(PATTERN.finditer(base.read_text()));new=list(PATTERN.finditer(p.read_text()))
  if len(old)!=len(new):continue
  for a,b in zip(old,new):
   if a[1]!=b[1] or a[2]==b[2]:continue
   recovered.append({'file':rel.as_posix(),'old':a[2],'new':b[2],'evidence_kind':'reconstructed-current-source-comparison','baseline_path':str(base.relative_to(C.parent)),'baseline_sha256':sha(base)})
 for turn in range(8):
  actions=0
  for p in markdown_files(P,excluded_top_level={'work'}):
   original=p.read_text()
   def resolve(m):
    nonlocal actions
    dest=m[2].strip('<>');path,sep,anchor=dest.partition('#')
    if not path or re.match(r'[a-zA-Z]+://|mailto:|data:',path):return m[0]
    path=unquote(path);target=(p.parent/path).resolve()
    if target.is_file() and P.resolve() in target.parents:return m[0]
    source=None
    if 'skills/_shared/' in path:
     target=P/'_shared'/path.split('skills/_shared/',1)[1];source=target
    elif D/'source-tools' in p.parents:
     rel=p.parent.relative_to(D/'source-tools')/path;source=(C.parent/'tools/togaf_corpus'/rel).resolve();target=(D/'source-tools'/rel).resolve()
    elif 'togaf-standard-10th-ai/' in path:
     rel=path.split('togaf-standard-10th-ai/',1)[1];source=C/rel;target=D/rel
    elif D.resolve() in p.resolve().parents:
     rel=p.parent.relative_to(D)/path;source=(C/rel).resolve();target=(D/rel).resolve()
     if C.resolve() not in source.parents:
      source=None
    if source is None and ('tools/togaf_corpus/' in path):
     rel=path.split('tools/togaf_corpus/',1)[1];source=C.parent/'tools/togaf_corpus'/rel;target=D/'source-tools'/rel
    if source is None and path.startswith('../../../togaf-standard-10th/'):
     source=C.parent/'togaf-standard-10th'/Path(path).name;target=D/'sources/pdf'/source.name
    if source is None or not source.is_file():
     retained=retained_figure_dependency(p,path)
     if retained:source,target=retained
    if source and source.is_file():
     if P.resolve() not in target.resolve().parents:target=D/'sources/pdf'/source.name
     target.parent.mkdir(parents=True,exist_ok=True)
     if not target.exists():shutil.copy2(source,target);copied.append(target.relative_to(P).as_posix());actions+=1
     relative=os.path.relpath(target,p.parent);replacement=relative+('#'+anchor if sep else '')
     if replacement!=dest:changes.append({'file':p.relative_to(P).as_posix(),'old':dest,'new':replacement});actions+=1
     return m[1]+replacement+m[3]
    return m[0]
   updated=PATTERN.sub(resolve,original)
   if updated!=original:p.write_text(updated)
  if not actions:break
 missing=[]
 for p in markdown_files(P,excluded_top_level={'work'}):
  for m in PATTERN.finditer(p.read_text()):
   target=m[2].strip('<>').split('#')[0]
   if not target or re.match(r'[a-zA-Z]+://|mailto:|data:',target):continue
   dest=(p.parent/unquote(target)).resolve()
   if not dest.is_file() or P.resolve() not in dest.parents:missing.append({'file':p.relative_to(P).as_posix(),'target':target})
 # Rechecking an already closed package must not erase its derivation history.
 merged={json.dumps(x,sort_keys=True,ensure_ascii=False):x for x in previous.get('rewrites',[])+recovered+changes}
 report={'schema_version':'portable-reading-links/1','passed':not missing,'copied_dependencies':sorted(set(previous.get('copied_dependencies',[])+copied)),'rewrites':list(merged.values()),'unresolved':missing,'notice_zh':'原始来源JSON及PDF字节不变；包内Markdown为可迁移阅读派生件，链接修订记入本清单。历次改写合并保留，复核不清空历史。'}
 (P/'reading-link-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print({'copied':len(copied),'rewrites':len(changes),'missing':len(missing),'sample':missing[:12]});return int(bool(missing))
if __name__=='__main__':raise SystemExit(main())
