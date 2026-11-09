"""Rewrite derived reading links, preserving original source bytes separately."""
from pathlib import Path
import json,re,os
from urllib.parse import unquote,urlsplit
C=Path(__file__).resolve().parents[1];ROOT=C.parent
PAT=re.compile(r'(!?\[[^\]\n]*\]\()(<[^>]+>|[^\s)]+)(\))')
def main():
 mapping=json.loads((C/'sources/relocation-manifest.json').read_text())['logical_paths'];rows=[]
 for base in ['README.md','reading-guide.md','fundamental','chapters','architecture','documents','translations','figures','supplementary','quality','maintenance/README.md']:
  parent=C/base
  for p in ([parent] if parent.is_file() else sorted(parent.rglob('*.md'))):
   def replace(m):
    dest=m[2].strip('<>');part,sep,anchor=dest.partition('#')
    if not part or urlsplit(part).scheme:return m[0]
    target=(p.parent/unquote(part)).resolve()
    try:old=target.relative_to(ROOT).as_posix()
    except ValueError:return m[0]
    if old not in mapping:return m[0]
    new=os.path.relpath(C/mapping[old],p.parent)+('#'+anchor if sep else '')
    rows.append({'file':str(p.relative_to(C)),'old_link':dest,'new_link':new})
    return m[1]+('<'+new+'>' if ' ' in new else new)+m[3]
   original=p.read_text();updated=PAT.sub(replace,original)
   if updated!=original:p.write_text(updated)
 report_path=C/'sources/reading-link-relocations.json'
 history=json.loads(report_path.read_text()).get('rewrites',[]) if report_path.exists() else []
 report_path.write_text(json.dumps({'schema_version':'relocated-reading-links/1','rewrites':history+rows,'notice_zh':'仅修订派生阅读页中的本地链接；原件字节和历史source路径身份不变。'},ensure_ascii=False,indent=2)+'\n')
 print({'rewritten_links':len(rows)})
if __name__=='__main__':main()
