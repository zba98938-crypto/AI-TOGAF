# -*- coding: utf-8 -*-
"""Consolidate explicitly selected legacy sources, then delete only verified inputs.

Preservation deduplicates exact bytes. Old logical source paths remain identities
in audit records and resolve through sources/relocation-manifest.json.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,zipfile,datetime
C=Path(__file__).resolve().parents[1];ROOT=C.parent
DIRECTORIES=['togaf-standard-10th','togaf-standard-10th-zh','togaf-architecture-roles-and-skills']
FILES=['g226.pdf','w242c.pdf'];ARCHIVE='togaf-architecture-roles-and-skills.zip'
DEST=C/'sources';MANIFEST=DEST/'relocation-manifest.json'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def candidates():
 # Prefer genuine source assets, not transient migration-test copies/archives.
 for base in [C/'skills/_shared/corpus/sources/pdf',C/'figures',C/'translations',C/'fundamental',C/'documents',C/'sources',C/'skills/_shared/corpus']:
  if not base.exists():continue
  for p in sorted(base.rglob('*')):
   if p.is_file() and not p.is_symlink() and p!=MANIFEST and 'node_modules' not in p.parts:yield p

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--delete-verified',action='store_true');args=ap.parse_args()
 if MANIFEST.exists() and json.loads(MANIFEST.read_text()).get('deletion_completed'):
  report=json.loads(MANIFEST.read_text())
  for row in report['files']+report['archive']['members']:assert sha(C/row['local_path'])==row['sha256']
  assert not any((ROOT/name).exists() for name in report['deleted_paths'])
  print({'already_consolidated':True,'verified_files':len(report['files']),'archive_members':len(report['archive']['members'])});return
 if MANIFEST.exists() and args.delete_verified:
  report=json.loads(MANIFEST.read_text())
  for r in report['files']+report['archive']['members']:
   assert sha(C/r['local_path'])==r['sha256'],r['local_path']
  for name in DIRECTORIES:
   p=ROOT/name
   if not p.exists():continue
   assert p.is_dir() and not p.is_symlink() and p.parent==ROOT
   lookup={r['old_path']:r for r in report['files']}
   for f in p.rglob('*'):
    if f.is_file() and f.name!='.DS_Store':
     row=lookup[f.relative_to(ROOT).as_posix()];assert sha(f)==row['sha256']
   shutil.rmtree(p)
  for name in FILES+[ARCHIVE]:
   p=ROOT/name
   if p.exists():
    want=report['archive']['sha256'] if name==ARCHIVE else next(r['sha256'] for r in report['files'] if r['old_path']==name)
    assert sha(p)==want
    p.unlink()
  report['deletion_completed']=True;report['deleted_paths']=DIRECTORIES+FILES+[ARCHIVE]
  report['deleted_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
  MANIFEST.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
  print(report['counts']);print({'deletion_completed':True});return
 DEST.mkdir(exist_ok=True);known={};seen=set()
 for p in candidates():
  if p in seen:continue
  seen.add(p);known.setdefault((p.stat().st_size,sha(p)),p)
 rows=[];copied=[]
 for name in DIRECTORIES+FILES:
  base=ROOT/name
  if not base.exists():continue
  paths=sorted(base.rglob('*')) if base.is_dir() else [base]
  for p in paths:
   if not p.is_file():continue
   if p.is_symlink():raise ValueError('Unexpected source symlink: '+str(p))
   if p.name=='.DS_Store':continue
   logical=p.relative_to(ROOT).as_posix();digest=sha(p);key=(p.stat().st_size,digest);target=known.get(key)
   if target is None:
    target=DEST/'retained'/logical;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
    assert sha(target)==digest;known[key]=target;copied.append(str(target.relative_to(C)))
   rows.append({'old_path':logical,'local_path':target.relative_to(C).as_posix(),'sha256':digest,'bytes':p.stat().st_size,'preservation':'newly-retained' if target.relative_to(C).as_posix() in copied else 'existing-identical-bytes'})
 # The ZIP is a duplicate container. Preserve every member, including a member
 # whose bytes differ from the expanded download; the container is unnecessary.
 zip_rows=[];archive=ROOT/ARCHIVE
 if archive.exists():
  archive_hash=sha(archive)
  with zipfile.ZipFile(archive) as z:
   for member in z.infolist():
    if member.is_dir() or Path(member.filename).name=='.DS_Store':continue
    if member.filename.startswith('/') or '..' in Path(member.filename).parts:raise ValueError(member.filename)
    data=z.read(member);digest=hashlib.sha256(data).hexdigest();key=(len(data),digest);target=known.get(key)
    if target is None:
     target=DEST/'retained/archive-members'/member.filename;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);known[key]=target;copied.append(str(target.relative_to(C)))
    zip_rows.append({'member':member.filename,'local_path':str(target.relative_to(C)),'sha256':digest,'bytes':len(data)})
 else:archive_hash=None
 mapping={r['old_path']:r['local_path'] for r in rows}
 for row in rows+zip_rows:assert sha(C/row['local_path'])==row['sha256']
 report={'schema_version':'local-source-relocation/1','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'canonical_root':C.name,'scope':DIRECTORIES+FILES+[ARCHIVE],'retained_development_directories':['skills','tools','tests','workbench'],'files':rows,'logical_paths':mapping,'archive':{'old_path':ARCHIVE,'sha256':archive_hash,'members':zip_rows,'container_policy':'all members preserved; duplicate ZIP container removed'},'counts':{'legacy_files':len(rows),'archive_members':len(zip_rows),'newly_retained_files':len(copied),'distinct_retained_bytes':len({r['sha256'] for r in rows+zip_rows}),'legacy_bytes':sum(r['bytes'] for r in rows)},'all_source_bytes_verified':True,'deletion_completed':False,'notice_zh':'原路径保留为历史身份；当前访问按logical_paths映射。不将迁移解释为新增语义审阅。.DS_Store为系统缓存，不保留。'}
 MANIFEST.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 if args.delete_verified:
  for name in DIRECTORIES:
   p=ROOT/name
   if p.exists():
    assert p.parent==ROOT and p.name in DIRECTORIES and not p.is_symlink()
    for f in p.rglob('*'):
     if f.is_file() and f.name!='.DS_Store':
      row=next(r for r in rows if r['old_path']==f.relative_to(ROOT).as_posix());assert sha(f)==row['sha256'] and sha(C/row['local_path'])==row['sha256']
    shutil.rmtree(p)
  for name in FILES+[ARCHIVE]:
   p=ROOT/name
   if p.exists():p.unlink()
  report['deletion_completed']=True;report['deleted_paths']=DIRECTORIES+FILES+[ARCHIVE];MANIFEST.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(report['counts']);print({'deletion_completed':report['deletion_completed'],'manifest':str(MANIFEST)})
if __name__=='__main__':main()
