#!/usr/bin/env python3
"""Acquire publicly offered OMG artifacts; no license submission or access bypass."""
import argparse, hashlib, json, re, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'standards'
PAGES={'bpmn-2.0.2':'https://www.omg.org/spec/BPMN/2.0.2/About-BPMN/',
       'uml-2.5.1':'https://www.omg.org/spec/UML/2.5.1/About-UML/',
       'xmi-2.5.1':'https://www.omg.org/spec/XMI/2.5.1/About-XMI/'}
def acquire(out=ROOT/'sources'):
 from urllib.parse import urljoin,urlparse
 out=Path(out);out.mkdir(parents=True,exist_ok=True); rows=[]
 for name,url in PAGES.items():
  folder=out/name;folder.mkdir(exist_ok=True)
  try:
   page=urllib.request.urlopen(url,timeout=45).read();(folder/'about.html').write_bytes(page)
   links=sorted(set(urljoin(url,x.replace('&amp;','&')) for x in re.findall(r'href=[\"\']([^\"\']+)[\"\']',page.decode('utf-8','replace')) if re.search(r'\.(xmi|xsd|cmof)(?:$|\?)',x,re.I)))
   for link in links:
    if urlparse(link).hostname!='www.omg.org':continue
    filename=Path(urlparse(link).path).name
    try:
     data=urllib.request.urlopen(link,timeout=45).read()
     if b'<html' in data[:500].lower():raise ValueError('HTML is not a normative machine-readable file')
     (folder/filename).write_bytes(data)
     rows.append({'language':name,'url':link,'file':str((folder/filename).relative_to(out)),'sha256':hashlib.sha256(data).hexdigest(),'status':'acquired','source_class':'official-machine-readable','normative_equivalence':'not-inferred'})
    except Exception as exc:rows.append({'language':name,'url':link,'status':'blocked','reason':str(exc)})
  except Exception as exc:rows.append({'language':name,'url':url,'status':'blocked','reason':str(exc)})
 (out/'manifest.json').write_text(json.dumps(rows,indent=2));return rows
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT/'sources');a=p.parse_args();print(json.dumps(acquire(a.out),indent=2))
