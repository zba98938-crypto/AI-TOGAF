# -*- coding: utf-8 -*-
"""Decode browser-saved full-volume MHTML, without network access or source alteration."""
from pathlib import Path
from email import policy
from email.parser import BytesParser
from urllib.parse import urljoin,urlsplit,urldefrag,unquote
from bs4 import BeautifulSoup,NavigableString,Tag
import json,re,hashlib,datetime,os,sys
sys.dont_write_bytecode=True
C=Path(__file__).resolve().parents[1];BASE=C/'fundamental/web-2025'
sys.path.insert(0,str(C/'maintenance'));from publish import guard
sys.addaudithook(guard)
PARTS=[('01-introduction-and-core-concepts','introduction','引言与核心概念'),('02-architecture-development-method','adm','架构开发方法'),('03-adm-techniques','adm-techniques','ADM技术'),('04-applying-the-adm','applying-the-adm','ADM应用'),('05-architecture-content','architecture-content','架构内容'),('06-ea-capability-and-governance','ea-capability-and-governance','EA能力与治理')]
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def norm(t):return re.sub(r'\s+',' ',t).strip()
def read_mhtml(slug):
 p=BASE/(slug+'.mhtml');b=p.read_bytes();m=BytesParser(policy=policy.default).parsebytes(b);parts=[x for x in m.walk() if not x.is_multipart()];h=next(x for x in parts if x.get_content_type()=='text/html');url=h.get('Content-Location');html=h.get_payload(decode=True)
 return p,b,m,parts,url,html
sources={slug:read_mhtml(slug) for slug,_,_ in PARTS}
urlmap={v[4]:slug for slug,v in sources.items()};chapterdirs={d:slug for slug,d,_ in PARTS};manifest={'schema_version':'fundamental-browser-archive/1','edition':'TOGAF Standard, 10th Edition — 2025 Digital Edition','acquired_date':'2026-11-08','retrieval_method':'existing Chrome session > official Single Page View > Save Page As MHTML','source_scope':'six Fundamental Content volumes linked from user-provided standard entry','content_role':'official-source-archive-and-structural-extraction-not-deep-semantic-review','source_entry_url':'https://pubs.opengroup.org/togaf-standard/','documents':[],'limits_zh':['原始MHTML保持浏览器保存字节；离线HTML和JSON为项目转换副本。','这里只确认获取、章节结构、文本和图表资源；未完成六卷逐节中文深度解释或全部原图语义审阅。','文内对其他出版物、网站和注册PDF的链接仅保留引用，不计为已下载正文。','不是对全球TOGAF出版物全集的覆盖声明。']}
chunk_lines=[]
for slug,folder,titlezh in PARTS:
 p,raw,m,parts,url,html=sources[slug];out=BASE/'volumes'/slug;assets=out/'assets';assets.mkdir(parents=True,exist_ok=True)
 (out/'source.html').write_bytes(html);soup=BeautifulSoup(html,'html.parser');content=soup.find(id='content');assert content is not None
 allids={x['id'] for x in soup.find_all(id=True)};resources={};resource_rows=[]
 for n,part in enumerate(parts):
  if part.get_content_type()=='text/html':continue
  loc=part.get('Content-Location');data=part.get_payload(decode=True) or b'';name=Path(unquote(urlsplit(loc or '').path)).name or 'resource';name=re.sub(r'[^A-Za-z0-9_.-]','_',name);local=f'assets/{n:03}-{name}'
  (out/local).write_bytes(data);resources[loc]=local;resource_rows.append({'source_url':loc,'local_path':local,'content_type':part.get_content_type(),'sha256':sha(data),'bytes':len(data)})
 headings=[{'id':x.get('id'),'level':int(x.name[1]),'title_en':x.get_text(' ',strip=True)} for x in content.find_all(re.compile('^h[1-6]$'))]
 # Retain each top-level atomic content block, then record uncovered text nodes explicitly.
 atomic={'p','ul','ol','dl','table','pre','h1','h2','h3','h4','h5','h6','img','figcaption'};blocks=[];chosen=[]
 for tag in content.descendants:
  if not isinstance(tag,Tag) or tag.name not in atomic:continue
  if any(isinstance(a,Tag) and a.name in atomic for a in tag.parents if a is not content):continue
  chosen.append(tag)
 assigned=set();current=[];dom_order={id(x):i for i,x in enumerate(content.descendants)}
 for tag in chosen:
  if re.fullmatch(r'h[1-6]',tag.name):
   lvl=int(tag.name[1]);current=[h for h in current if h['level']<lvl];current.append({'id':tag.get('id'),'level':lvl,'title_en':tag.get_text(' ',strip=True)})
  for text in tag.descendants:
   if isinstance(text,NavigableString):assigned.add(id(text))
  ident=f'C220-web-2025:{slug}:b{len(blocks)+1:05}';block={'id':ident,'source_dom_order':dom_order[id(tag)],'kind':tag.name,'anchor':tag.get('id'),'section_path':list(current),'text_en':tag.get_text(' ',strip=True),'html':str(tag),'source_url':url+('#'+(tag.get('id') or current[-1].get('id')) if (tag.get('id') or current and current[-1].get('id')) else ''),'source_mhtml_sha256':sha(raw),'source_html_sha256':sha(html)}
  if tag.name=='table':block['cells']=[[{'text_en':cell.get_text(' ',strip=True),'rowspan':int(cell.get('rowspan',1)),'colspan':int(cell.get('colspan',1)),'is_header':cell.name=='th'} for cell in row.find_all(['td','th'],recursive=False)] for row in tag.find_all('tr')]
  if tag.name=='img':block.update(image_url=urljoin(url,tag.get('src','')),alt=tag.get('alt'),local_asset=resources.get(urljoin(url,tag.get('src',''))))
  blocks.append(block)
 uncovered=[t for t in content.descendants if isinstance(t,NavigableString) and norm(str(t)) and id(t) not in assigned and t.parent.name not in {'style','script'}]
 for t in uncovered:blocks.append({'id':f'C220-web-2025:{slug}:b{len(blocks)+1:05}','kind':'unwrapped-text','source_dom_order':dom_order[id(t)],'text_en':norm(str(t)),'source_url':url,'parent_tag':t.parent.name,'parent_class':t.parent.get('class'),'source_mhtml_sha256':sha(raw)})
 blocks.sort(key=lambda b:b['source_dom_order'])
 for i,block in enumerate(blocks):block['id']=f'C220-web-2025:{slug}:b{i+1:05}'
 foot=soup.find(id='footnotes');footnotes=[{'id':x.get('id'),'text_en':x.get_text(' ',strip=True),'html':str(x)} for x in foot.find_all('div',class_='footnote')] if foot else []
 images=[]
 for im in soup.find_all('img'):
  iu=urljoin(url,im.get('src',''));images.append({'source_url':iu,'alt':im.get('alt'),'local_asset':resources.get(iu),'in_main_content':content in im.parents})
 missing_images=[x for x in images if not x['local_asset'] and not x['source_url'].startswith('data:')]
 toc=soup.find(id='toc');toc_links=[{'text_en':a.get_text(' ',strip=True),'href':a.get('href')} for a in toc.find_all('a',href=True)] if toc else []
 toc_missing=[x for x in toc_links if urldefrag(urljoin(url,x['href']))[0]==url and urldefrag(urljoin(url,x['href']))[1] and unquote(urldefrag(urljoin(url,x['href']))[1]) not in allids]
 # Offline projection: rewrite captured resources and known six-volume cross-references.
 offline=BeautifulSoup(html,'html.parser')
 repaired_title_anchors=[]
 for link in toc_missing:
  fragment=unquote(urldefrag(urljoin(url,link['href']))[1]);heading=offline.find('h1')
  if heading and norm(link['text_en'])==norm(heading.get_text(' ',strip=True)) and not heading.get('id'):
   heading['id']=fragment;repaired_title_anchors.append(fragment)

 for tag in offline.find_all(['script','base']):tag.decompose()
 for tag in offline.find_all(True):
  for attr in ('src','href','poster'):
   if not tag.has_attr(attr):continue
   val=tag[attr];absolute=urljoin(url,val);rooturl,frag=urldefrag(absolute)
   if absolute in resources:tag[attr]=resources[absolute]
   elif rooturl in resources:tag[attr]=resources[rooturl]+('#'+frag if frag else '')
   elif tag.name=='a':
    if val.startswith('#'):continue
    target=urlmap.get(rooturl)
    if target:tag[attr]=('../'+target+'/index.html' if target!=slug else 'index.html')+('#'+frag if frag else '')
    else:
     match=re.match(r'^https://pubs\.opengroup\.org/togaf-standard/([^/]+)/([^/]+)\.html$',rooturl)
     if match and match[1] in chapterdirs and re.fullmatch(r'chap\d+|apdx[a-z]',match[2]):
      target=chapterdirs[match[1]];anchor=frag or match[2];tag[attr]='../'+target+'/index.html#'+anchor
     else:tag[attr]=absolute
   elif tag.name=='link' and tag.get('rel')==['stylesheet'] and absolute not in resources:tag.decompose();break
 # Capture css remains exact in assets; derivative local css disables unresolved network fonts.
 css_missing=[]
 for row in resource_rows:
  if row['content_type']!='text/css':continue
  cp=out/row['local_path'];data=cp.read_text(errors='replace')
  def local_css(match):
   value=match[1].strip().strip('"\'');absurl=urljoin(row['source_url'],value)
   if value.startswith('data:'):return match.group(0)
   if absurl in resources:return 'url('+Path(resources[absurl]).name+')'
   css_missing.append(absurl);return 'url(data:,)'
  localdata=re.sub(r'url\(([^)]+)\)',local_css,data);localname=cp.stem+'.offline.css';cp.with_name(localname).write_text(localdata)
  for link in offline.find_all('link',href=row['local_path']):link['href']='assets/'+localname
 meta=offline.new_tag('meta');meta['http-equiv']='Content-Security-Policy';meta['content']="default-src 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self' data:; base-uri 'none'; form-action 'none'";offline.head.insert(0,meta)
 (out/'index.html').write_text(str(offline))
 record={'schema_version':'fundamental-html-source/1','id':'C220-web-2025:'+slug,'title_en':soup.title.get_text(' ',strip=True),'title_zh':titlezh,'source':{'url':url,'mhtml_path':str(p.relative_to(C)),'mhtml_sha256':sha(raw),'html_path':str((out/'source.html').relative_to(C)),'html_sha256':sha(html),'acquired_date':'2026-11-08','edition':'10th Edition: 2025'},'analysis_status':'structure-extracted-not-deep-reviewed','headings':headings,'toc':toc_links,'blocks':blocks,'footnotes':footnotes,'images':images,'resources':resource_rows,'coverage':{'main_content_text_characters':len(content.get_text()),'content_blocks':len(blocks),'unwrapped_text_recorded':len(uncovered),'tables':len(content.find_all('table')),'images':len(images),'main_content_images':sum(x['in_main_content'] for x in images),'missing_images':missing_images,'toc_links':len(toc_links),'toc_missing_anchors':toc_missing,'offline_repaired_title_anchors':repaired_title_anchors,'unresolved_toc_anchors':[x for x in toc_missing if unquote(urldefrag(urljoin(url,x['href']))[1]) not in repaired_title_anchors],'uncaptured_font_resources':sorted(set(css_missing))},'main_content_text_en':content.get_text('\n',strip=True),'limits_zh':['结构提取不是逐章语义审阅；保留英文原文及原始HTML。','表格span布局保留在html及cells，不把空格或合并格自动填值。','原始CSS保留；离线样式对未捕获网络字体改用本地回退，不发起网络请求。']}
 dump(out/'document.json',record)
 # Readable complete source, using HTML for complex source tables/lists to preserve nesting and spans.
 md=['# '+record['title_en'],'','原文保存及结构转换；未完成逐章深度语义审阅。','', '[离线原貌](index.html) · [原始HTML](source.html) · [结构化正文](document.json)','']
 for b in blocks:
  if re.fullmatch(r'h[1-6]',b['kind']):md+=['#'*int(b['kind'][1])+' '+b['text_en'],'']
  elif b['kind']=='img':md+=['!['+(b.get('alt') or '')+']('+(b.get('local_asset') or b['image_url'])+')','']
  elif b['kind'] in {'table','ul','ol','dl','pre'}:md+=[b['html'],'']
  else:md+=[b['text_en'],'']
 if footnotes:md+=['## Footnotes','']+[x['text_en']+'\n' for x in footnotes]
 (out/'document.md').write_text('\n'.join(md)+'\n')
 for b in blocks:
  if b['text_en']:chunk_lines.append(json.dumps({'id':b['id'],'kind':'fundamental-source-block','title_en':record['title_en'],'section_path':b.get('section_path',[]),'text_en':b['text_en'],'source_url':b['source_url'],'source_mhtml_sha256':sha(raw),'document_path':str((out/'document.json').relative_to(C)),'interpretation_status':'not-deep-reviewed'},ensure_ascii=False))
 manifest['documents'].append({'id':record['id'],'title_zh':titlezh,'title_en':record['title_en'],'source_url':url,'mhtml_path':str(p.relative_to(BASE)),'mhtml_sha256':sha(raw),'mhtml_bytes':len(raw),'offline_html':'volumes/'+slug+'/index.html','document_json':'volumes/'+slug+'/document.json','document_md':'volumes/'+slug+'/document.md','chapters':sum(bool(re.match(r'^\d+\.',h['title_en'])) and h['level']==2 for h in headings),'appendices':sum(bool(re.match(r'^[A-Z]:',h['title_en'])) and h['level']==2 for h in headings),'coverage':record['coverage'],'extraction_sha256':sha((out/'document.json').read_bytes())})
(BASE/'source-chunks.jsonl').write_text('\n'.join(chunk_lines)+'\n')
manifest['counts']={'volumes':len(manifest['documents']),'numbered_chapters':sum(d['chapters'] for d in manifest['documents']),'appendices':sum(d['appendices'] for d in manifest['documents']),'source_blocks':sum(d['coverage']['content_blocks'] for d in manifest['documents']),'tables':sum(d['coverage']['tables'] for d in manifest['documents']),'main_content_images':sum(d['coverage']['main_content_images'] for d in manifest['documents']),'missing_images':sum(len(d['coverage']['missing_images']) for d in manifest['documents']),'toc_missing_anchors':sum(len(d['coverage']['toc_missing_anchors']) for d in manifest['documents']),'offline_repaired_title_anchors':sum(len(d['coverage']['offline_repaired_title_anchors']) for d in manifest['documents']),'unresolved_toc_anchors':sum(len(d['coverage']['unresolved_toc_anchors']) for d in manifest['documents'])}
manifest['validation']={'status':'passed' if not manifest['counts']['missing_images'] and not manifest['counts']['unresolved_toc_anchors'] else 'needs-review','scope':'MIME resources, source hashes, top-level chapter/appendix headings, TOC anchors and text preservation; not semantic understanding','pipeline_sha256':sha(Path(__file__).read_bytes())}
dump(BASE/'manifest.json',manifest)
lines=['# TOGAF第10版基础标准：2025数字版本地副本','', '从用户已打开的Chrome会话，通过官方六卷Single Page View保存。原始MHTML、解包HTML/图片、离线浏览版、结构化英文正文分别保留。','', '**保存与结构提取已完成；逐节中文深度解析和原图语义审阅尚未完成。**','', '|基础卷|章节/附录|离线阅读|结构化资料|原始保存|','|---|---|---|---|---|']
for d in manifest['documents']:lines.append('|'+ '|'.join([d['title_zh'],str(d['chapters'])+'章 / '+str(d['appendices'])+'附录','[HTML]('+d['offline_html']+')','[MD]('+d['document_md']+') · [JSON]('+d['document_json']+')','[MHTML]('+d['mhtml_path']+')'])+'|')
lines+=['',f"共{manifest['counts']['numbered_chapters']}章、{manifest['counts']['appendices']}个附录、{manifest['counts']['tables']}张正文表格、{manifest['counts']['main_content_images']}个正文图片引用。计数不等于语义理解验收。",'', '原始版权、版本和使用条件保留在每卷正文；未将网页副本称为下载的正式PDF。网页中的其他出版物链接保留为外部引用，不计入六卷正文覆盖。','', '[文件与来源指纹](manifest.json) · [独立获取审查](acquisition-audit.md) · [源文检索块](source-chunks.jsonl)','', '离线HTML禁止自动连接外网，已捕获图片和样式使用本地文件；未捕获的外部字体使用本地回退。原始MHTML和解包source.html均保留供比对。四个源页面的卷标题目录锚点缺失，仅在离线副本补入对应标题ID，并在manifest中记录；不改原始正文。']
(BASE/'README.md').write_text('\n'.join(lines)+'\n');print(json.dumps(manifest['counts'],ensure_ascii=False,indent=2));print(manifest['validation'])
