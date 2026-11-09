# -*- coding: utf-8 -*-
"""Check current reading entrypoints; historical reports remain versioned evidence."""
from pathlib import Path
import re,json,hashlib
from urllib.parse import unquote
from bs4 import BeautifulSoup
C=Path(__file__).resolve().parents[1]
FILES=['README.md','fundamental/README.md','fundamental/chinese-text/README.md','quality/completion-status.md','quality/implementation-ledger.md','quality/extended-publication.md','maintenance/README.md','maintenance/cases/omnichannel/README.md','maintenance/cases/omnichannel/current-delivery-review.md','release/README.md']
FILES+=['skills/_shared/references/togaf-explained.md','skills/_shared/references/adm-cycle.md','skills/_shared/examples/omnichannel/README.md','maintenance/cases/omnichannel/generated-adm/adm-check.md']
FILES+=['supplementary/chinese-text/README.md','fundamental/chinese-text/01-introduction-and-core-concepts.md','fundamental/chinese-text/03-adm-techniques.md','fundamental/chinese-text/05-architecture-content.md','supplementary/chinese-text/G226.md','supplementary/chinese-text/W242C-source.md']
FILES+=['sources/README.md']
FILES+=['quality/seven-gap-reconciliation.md']
FILES+=['architecture/adm-flow/README.md','skills/_shared/examples/adm-flow/README.md']
PAT=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
def main():
 issues=[];rows=[]
 for name in FILES:
  p=C/name
  if not p.is_file():issues.append({'file':name,'code':'missing-entry'});continue
  for match in PAT.finditer(p.read_text()):
   url=match[1].strip('<>');path,_,fragment=url.partition('#')
   if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',path):continue
   target=(p.parent/unquote(path)).resolve() if path else p
   row={'file':name,'target':url,'passed':target.is_file()}
   if target.is_file() and fragment and target.suffix in {'.md','.html'}:
    text=target.read_text();ids={x.get('id') for x in BeautifulSoup(text,'html.parser').find_all(id=True)}
    if target.suffix=='.md':
     slugs=[]
     for title in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
      slug=re.sub(r'[^\w\s-]','',title.lower()).replace(' ','-');base=slug;index=0
      while slug in slugs:index+=1;slug=base+'-'+str(index)
      slugs.append(slug)
     ids.update(slugs)
    row['passed']=fragment in ids
   rows.append(row)
   if not row['passed']:issues.append(row)
 report={'schema_version':'current-entrypoint-links/1','passed':not issues,'counts':{'entrypoints':len(FILES),'local_links':len(rows),'issues':len(issues)},'issues':issues,'links':rows,'scope_zh':'只验证当前入口、本地文件与Markdown/HTML锚点；历史报告的旧相对路径和外部网址不声称已验证。'}
 (C/'quality/current-entrypoint-links.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts']);print(issues);return int(not report['passed'])
if __name__=='__main__':raise SystemExit(main())
