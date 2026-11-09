"""Readable companion output, with independently inspectable identity anchors."""
import json
import xml.etree.ElementTree as ET
from html import escape
from urllib.parse import quote

def anchor(kind,identity):return kind+'-'+quote(identity,safe='')

def companion(entities,relationships,title):
    def text(value):return escape(json.dumps(value,ensure_ascii=False,indent=2) if isinstance(value,(dict,list)) else str(value))
    body=['<html lang="zh-CN"><head><meta charset="utf-8"/><title>'+text(title)+'</title>',
          '<style>body{font:16px sans-serif;max-width:1100px;margin:32px auto;line-height:1.7}section{break-inside:avoid;border:1px solid #ccd;padding:20px;margin:24px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere}a{overflow-wrap:anywhere}@media print{section{break-before:page}}</style></head><body>',
          '<h1>'+text(title)+'：分组明细</h1><p>与主图共用模型ID。下列关系登记提供完整语义，不表示每条关系均为主图上的连线。每个对象为可独立打印的明细页。</p><nav>']
    for e in entities:body.append('<a href="#'+anchor('entity',e['id'])+'">'+text(e['name'])+'</a> · ')
    body.append('</nav>')
    groups={}
    for e in entities:groups.setdefault(e['type'],[]).append(e)
    body.append('<nav aria-label="分组分页">')
    pages=[]
    for typ,members in groups.items():
        for start in range(0,len(members),8):
            page='page-'+quote(typ,safe='')+'-'+str(start//8+1);pages.append((page,typ,members[start:start+8]))
            body.append('<a href="#'+page+'">'+text(typ)+' / '+str(start//8+1)+'</a> · ')
    body.append('</nav>')
    for page,typ,members in pages:
        body.append('<article id="'+page+'" style="break-before:page"><h2>'+text(typ)+' 分页</h2>')
        for e in members:
            body.append('<section id="'+anchor('entity',e['id'])+'" data-entity-id="'+escape(e['id'],quote=True)+'"><h2>'+text(e['name'])+'</h2><pre>'+text(e)+'</pre></section>')
        body.append('</article>')
    body.append('<h2>关系明细</h2>')
    for r in relationships:
        body.append('<section id="'+anchor('relationship',r['id'])+'" data-relationship-id="'+escape(r['id'],quote=True)+'"><h3>'+text(r['label'])+'</h3><p><a href="#'+anchor('entity',r['source'])+'">'+text(r['source'])+'</a> → <a href="#'+anchor('entity',r['target'])+'">'+text(r['target'])+'</a></p><pre>'+text(r)+'</pre></section>')
    return ''.join(body)+'</body></html>'

def locations(svg,details,filename):
    result={'entities':{},'relationships':{}}
    for where,content in [('main',svg),('companion',details)]:
        tree=ET.fromstring(content)
        for group,attr in [('entities','data-entity-id'),('relationships','data-relationship-id')]:
            for node in tree.iter():
                identity=node.get(attr)
                if identity:
                    result[group].setdefault(identity,[]).append({'kind':where,'file':filename if where=='companion' else None,
                                                               'anchor':node.get('id'),'representation':'readable-record' if where=='companion' else 'diagram'})
    return result

def identity_failures(svg,details,entities,relationships):
    result=[]
    for attr,expected in [('data-entity-id',entities),('data-relationship-id',relationships)]:
        actual=set()
        for content in (svg,details):
            if content:
                tree=ET.fromstring(content)
                actual.update(n.get(attr) for n in tree.iter() if n.get(attr))
        if actual!=expected:result.append({'code':'output-identity-coverage','attribute':attr,'missing':sorted(expected-actual),'extra':sorted(actual-expected)})
    return result

def location_failures(svg,details,declared,filename):
    """Verify declared output positions against actual files and stable anchors."""
    actual=locations(svg,details,filename)
    errors=[]
    if declared!=actual:errors.append({'code':'output-location-mismatch','message':'声明的主图/明细位置必须匹配实际DOM'})
    for group in ('entities','relationships'):
        for identity,places in actual[group].items():
            for place in places:
                if place['kind']=='companion' and place['anchor']!=anchor('entity' if group=='entities' else 'relationship',identity):
                    errors.append({'code':'output-anchor-mismatch','id':identity})
    return errors
