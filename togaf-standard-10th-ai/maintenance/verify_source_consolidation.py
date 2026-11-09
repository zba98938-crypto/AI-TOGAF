"""Independently verify source preservation and the authorized deletion scope."""
from pathlib import Path
import json,hashlib,re
from urllib.parse import unquote,urlsplit
from source_paths import resolve
C=Path(__file__).resolve().parents[1];ROOT=C.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 manifest=C/'sources/relocation-manifest.json';d=json.loads(manifest.read_text());checks=[]
 def check(label,ok):checks.append({'id':label,'passed':bool(ok)})
 check('deletion-executed',d['deletion_completed'])
 for name in d['scope']:check('removed:'+name,not (ROOT/name).exists())
 check('only-AI-root-TOGAF-directory',[p.name for p in ROOT.iterdir() if p.is_dir() and p.name.startswith('togaf-')]==[C.name])
 migration=C/'quality/skills-consolidation.json'
 unified=json.loads(migration.read_text()) if migration.is_file() else None
 for name in d['retained_development_directories']:
  if name=='skills' and unified:
   check('skills-superseded-by-authorized-consolidation',not (ROOT/'skills').exists() and (C/'skills/_shared/scripts/local_tool.py').is_file() and unified['canonical_directory']=='togaf-standard-10th-ai/skills')
  else:check('retained-development:'+name,(ROOT/name).is_dir())
 for row in d['files']+d['archive']['members']:
  p=(C/row['local_path']).resolve();check('preserved:'+row.get('old_path',row.get('member')),C in p.parents and p.is_file() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'])
 for row in d['files']:check('logical-source:'+row['old_path'],resolve(ROOT/row['old_path'])==C/row['local_path'])
 for item in json.loads((C/'index.json').read_text())['documents']:
  p=resolve(ROOT/item['source']['path']);check('original-PDF:'+item['id'],p.is_file() and sha(p)==item['source']['sha256'])
 for f in (C/'translations').glob('*.json'):
  source=json.loads(f.read_text())['source'];p=resolve(ROOT/source['path']);check('original-translation:'+f.stem,p.is_file() and sha(p)==source['sha256'])
 rebindings=json.loads((C/'sources/reading-link-relocations.json').read_text())['rewrites']
 for row in rebindings:
  p=C/row['file'];target=row['new_link'].split('#')[0];check('relocated-reading-link:'+row['file']+':'+target,(p.parent/unquote(target)).resolve().is_file())
 report={'schema_version':'source-consolidation-verification/1','passed':all(r['passed'] for r in checks),'counts':{'checks':len(checks),'legacy_files_preserved':len(d['files']),'archive_members_preserved':len(d['archive']['members']),'reading_links_relocated':len(rebindings),'failed':sum(not r['passed'] for r in checks)},'failures':[r for r in checks if not r['passed']],'input_sha256':{'sources/relocation-manifest.json':sha(manifest),'sources/reading-link-relocations.json':sha(C/'sources/reading-link-relocations.json')},'scope_zh':'用户明确授权删除旧资料目录、重复ZIP及补充PDF。每一来源字节已在AI目录验证。旧快照的外部只读结论是历史证据，不扩张为本次删除后仍原位存在。'}
 (C/'quality/source-consolidation-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts']);print(report['failures']);return int(not report['passed'])
if __name__=='__main__':raise SystemExit(main())
