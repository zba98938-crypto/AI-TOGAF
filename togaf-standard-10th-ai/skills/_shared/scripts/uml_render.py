"""Native UML 2.5.1 class-diagram subset, with explicit generated layout.

Unsupported constructs, unresolved types, navigability and aggregation are refused.
This renderer does not claim UMLDI preservation or full metamodel/OCL acceptance.
"""
import html
import json
import math
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from standards import ROOT, XMI, Invalid, Incomplete, check_native, safe_xml, namespace, local, sha, write_new

UML='http://www.omg.org/spec/UML/20131001'
VISIBILITY={'public':'+','private':'-','protected':'#','package':'~'}


def diagram_model(data, package_root=None):
    validation=check_native(data,'uml','2.5.1',package_root)
    if validation['errors']:raise Invalid('; '.join(validation['errors']))
    blockers=[b for b in validation['blockers'] if not b.startswith('complete UML2/OCL')]
    if blockers:raise Incomplete('; '.join(blockers))
    root=safe_xml(data)
    if root.tag=='{'+XMI+'}XMI':
        models=[e for e in root if isinstance(e.tag,str)]
        if len(models)!=1 or models[0].tag!='{'+UML+'}Model':raise Incomplete('Class rendering requires exactly one native UML Model')
        root=models[0]
    if root.tag!='{'+UML+'}Model':raise Incomplete('Class rendering requires a native UML Model')
    objects={e.get('{'+XMI+'}id'):e for e in root.iter() if isinstance(e.tag,str) and e.get('{'+XMI+'}id')}
    defaults=[]

    def identity(e):
        value=e.get('{'+XMI+'}id')
        if not value or not value.strip():raise Invalid('Explicit native xmi:id required for '+local(e.tag))
        return value

    def name(e):
        value=e.get('name')
        if not isinstance(value,str) or not value.strip():raise Incomplete('Named UML element has no display name: '+identity(e))
        if len(value)>240:raise Incomplete('UML label exceeds 240-character rendering limit: '+identity(e))
        return value

    def typed(e):
        raw=e.get('{'+XMI+'}type')
        if not raw:return local(e.tag)
        if ':' not in raw or e.nsmap.get(raw.split(':')[0])!=UML:raise Incomplete('UML xmi:type must bind the normative UML namespace: '+raw)
        return raw.split(':')[-1]

    def attributes(e,allowed):
        for key in e.attrib:
            if namespace(key)==XMI and local(key) in {'id','type','version'}:continue
            if namespace(key) or local(key) not in allowed:raise Incomplete('Unrepresented UML attribute '+key+' on '+str(e.get('{'+XMI+'}id')))

    def boolean(e,key):
        raw=e.get(key,'false')
        if raw not in {'true','false'}:raise Invalid('Invalid UML boolean '+key+' on '+identity(e))
        return raw=='true'

    def visibility(e):
        value=e.get('visibility')
        if value is not None and value not in VISIBILITY:raise Invalid('Invalid UML visibility on '+identity(e))
        return VISIBILITY.get(value,'')

    packages=[];classifiers=[];associations=[];generalizations=[]

    def collect(package,parent=None):
        attributes(package,{'name','visibility'})
        pid=identity(package);packages.append({'id':pid,'name':name(package),'visibility':visibility(package),'parent_id':parent,'kind':'Model' if package is root else 'Package'})
        for e in package:
            if not isinstance(e.tag,str):continue
            if local(e.tag)!='packagedElement':raise Incomplete('Unsupported package child: '+local(e.tag))
            kind=typed(e)
            if kind=='Package':collect(e,pid)
            elif kind in {'Class','PrimitiveType'}:
                attributes(e,{'name','visibility','isAbstract'})
                classifiers.append({'id':identity(e),'name':name(e),'visibility':visibility(e),'kind':kind,'package_id':pid,'abstract':boolean(e,'isAbstract'),'element':e})
            elif kind=='Association':associations.append(e)
            else:raise Incomplete('Unsupported native UML classifier/relationship: '+kind)
    collect(root)
    if not classifiers:raise Incomplete('UML class rendering requires at least one Class or PrimitiveType')
    if len(classifiers)>40 or len(packages)>20:raise Incomplete('UML class rendering capacity is 40 classifiers / 20 packages')
    classifier_map={c['id']:c for c in classifiers}

    def type_ref(e):
        refs=[]
        if e.get('type'):refs.append(e.get('type'))
        for child in e:
            if local(child.tag)=='type':
                if any(key not in {'{'+XMI+'}idref','href'} for key in child.attrib) or len(child):raise Incomplete('Unsupported UML type-reference payload')
                raw=child.get('{'+XMI+'}idref') or child.get('href')
                if child.get('href') and child.get('href').partition('#')[0]:raise Incomplete('External UML type resolution is not supported')
                if raw:refs.append(raw.removeprefix('#') if hasattr(raw,'removeprefix') else raw.lstrip('#'))
        if len(refs)!=1:raise Incomplete('One explicitly resolved type required for '+identity(e))
        ref=refs[0]
        if ref not in classifier_map:raise Incomplete('Unresolved or unsupported UML type: '+ref)
        return ref

    def multiplicity(e,required=False):
        lo=e.find('lowerValue');hi=e.find('upperValue')
        if lo is None and hi is None and not required:
            defaults.append({'id':identity(e),'field':'multiplicity','value':'1',
                             'basis':'UML MultiplicityElement lowerBound/upperBound default to 1 when bound values are absent',
                             'notation':'default [1] omitted as shorthand; not unknown'})
            return None
        if lo is None or hi is None:raise Incomplete('Both lowerValue and upperValue are required for explicit multiplicity: '+identity(e))
        for v in (lo,hi):
            attributes(v,{'value'})
            if typed(v) not in {'LiteralInteger','LiteralUnlimitedNatural'}:raise Incomplete('Only literal integer/unlimited UML bounds are supported')
            if len(v):raise Incomplete('Multiplicity expression bodies are unsupported')
        lower,upper=lo.get('value'),hi.get('value')
        if lower is None or not re.fullmatch(r'\d+',lower):raise Invalid('Nonnegative UML lower bound required')
        if upper in {'*','-1'}:upper='*'
        elif upper is None or not re.fullmatch(r'\d+',upper):raise Invalid('Integer or unlimited UML upper bound required')
        if upper!='*' and int(upper)<int(lower):raise Invalid('Inverted UML multiplicity on '+identity(e))
        return lower if lower==upper else lower+'..'+upper

    def feature(e,parameter=False):
        attributes(e,{'name','type','direction'} if parameter else {'name','type','visibility','isStatic','isReadOnly'})
        if e.get('aggregation') not in (None,'none'):raise Incomplete('UML aggregation/composition is not supported')
        for child in e:
            if local(child.tag) not in {'type','lowerValue','upperValue'}:raise Incomplete('Unsupported UML feature child '+local(child.tag))
        tid=type_ref(e);mul=multiplicity(e)
        result={'id':identity(e),'name':e.get('name','') if parameter and e.get('direction')=='return' else name(e),'type_id':tid,'type_name':classifier_map[tid]['name'],
                'visibility':visibility(e),'multiplicity':mul,'effective_multiplicity':mul if mul is not None else '1',
                'multiplicity_explicit':mul is not None,'static':boolean(e,'isStatic'),'read_only':boolean(e,'isReadOnly')}
        result['text']=result['visibility']+result['name']+' : '+result['type_name']+((' ['+mul+']') if mul else '')+(' {readOnly}' if result['read_only'] else '')
        return result

    for cls in classifiers:
        cls['attributes']=[];cls['operations']=[]
        for e in cls.pop('element'):
            tag=local(e.tag)
            if cls['kind']=='PrimitiveType':raise Incomplete('PrimitiveType features are outside this class-diagram subset')
            if tag=='ownedAttribute':cls['attributes'].append(feature(e))
            elif tag=='ownedOperation':
                attributes(e,{'name','visibility','isStatic','isAbstract','isQuery'})
                params=[];returns=[]
                for p in e:
                    if local(p.tag)!='ownedParameter':raise Incomplete('Unsupported UML operation child: '+local(p.tag))
                    record=feature(p,parameter=True);direction=p.get('direction','in')
                    if p.get('direction') is None:defaults.append({'id':record['id'],'field':'direction','value':'in','basis':'UML Parameter default'})
                    if direction not in {'in','out','inout','return'}:raise Invalid('Invalid UML parameter direction')
                    record['direction']=direction
                    (returns if direction=='return' else params).append(record)
                if len(returns)>1:raise Incomplete('Multiple return parameters are not supported')
                op={'id':identity(e),'name':name(e),'visibility':visibility(e),'static':boolean(e,'isStatic'),'abstract':boolean(e,'isAbstract'),'query':boolean(e,'isQuery'),'parameters':params,'returns':returns}
                op['text']=op['visibility']+op['name']+'('+', '.join(p['direction']+' '+p['name']+' : '+p['type_name']+((' ['+p['multiplicity']+']') if p['multiplicity'] else '') for p in params)+')'+((' : '+returns[0]['type_name']+((' ['+returns[0]['multiplicity']+']') if returns[0]['multiplicity'] else '')) if returns else '')+(' {query}' if op['query'] else '')
                cls['operations'].append(op)
            elif tag=='generalization':
                attributes(e,{'general'})
                if len(e):raise Incomplete('Generalization child constraints are unsupported')
                parent=e.get('general')
                if parent not in classifier_map or classifier_map[parent]['kind']!='Class':raise Incomplete('Generalization requires a resolved native Class')
                generalizations.append({'id':identity(e),'source_id':cls['id'],'target_id':parent,'kind':'generalization'})
            else:raise Incomplete('Unsupported UML Class feature: '+tag)
    relations=list(generalizations)
    for assoc in associations:
        attributes(assoc,{'name','visibility','memberEnd'})
        aid=identity(assoc);ends=[e for e in assoc if local(e.tag)=='ownedEnd']
        if len(ends)!=len(assoc) or len(ends)!=2:raise Incomplete('Only ordinary binary Association-owned ends are supported')
        member=assoc.get('memberEnd','').split()
        if len(member)!=2 or len(set(member))!=2 or set(member)!={identity(e) for e in ends}:raise Invalid('Binary Association memberEnd must name its two ownedEnd IDs')
        end_map={identity(e):e for e in ends};rows=[]
        for eid in member:
            e=end_map[eid];attributes(e,{'name','type','aggregation','visibility','association'})
            if e.get('aggregation') not in (None,'none'):raise Incomplete('Aggregation/composition notation is not implemented')
            if e.get('association') not in (None,aid):raise Invalid('Association end references another Association')
            if any(local(c.tag) not in {'type','lowerValue','upperValue'} for c in e):raise Incomplete('Association-end qualifiers/defaults are unsupported')
            tid=type_ref(e)
            if classifier_map[tid]['kind']!='Class':raise Incomplete('This ordinary association subset requires Class endpoints')
            rows.append({'id':eid,'type_id':tid,'name':e.get('name',''),'multiplicity':multiplicity(e,required=True)})
        relations.append({'id':aid,'kind':'association','name':assoc.get('name',''),'visibility':visibility(assoc),'source_id':rows[0]['type_id'],'target_id':rows[1]['type_id'],'ends':rows})
    if len(relations)>100:raise Incomplete('UML class rendering capacity is 100 relations')
    feature_count=sum(len(c['attributes'])+len(c['operations'])+sum(len(o['parameters'])+len(o['returns']) for o in c['operations']) for c in classifiers)
    if feature_count>400:raise Incomplete('UML class rendering capacity is 400 feature/parameter records')
    parents={c['id']:[] for c in classifiers}
    for r in generalizations:parents[r['source_id']].append(r['target_id'])
    visiting=set();ranks={}
    def rank(ident):
        if ident in visiting:raise Invalid('Cyclic UML generalization')
        if ident in ranks:return ranks[ident]
        visiting.add(ident);value=max([rank(p)+1 for p in parents[ident]] or [0]);visiting.remove(ident);ranks[ident]=value;return value
    for ident in parents:rank(ident)
    return {'model_id':identity(root),'name':name(root),'packages':packages,'classifiers':classifiers,'relations':relations,'ranks':ranks,'applied_defaults':defaults,'native_validation':validation,'source_sha256':sha(data)}


def svg_diagram(model):
    esc=lambda s:html.escape(str(s),quote=True)
    def text_width(s):return sum(14 if ord(c)>255 else 8 for c in s)
    boxes={};package_boxes={};end_labels=[];by_package={p['id']:[] for p in model['packages']}
    for c in model['classifiers']:
        lines=[c['name']]+[a['text'] for a in c['attributes']]+[o['text'] for o in c['operations']]
        c['width']=max(240,max(map(text_width,lines))+44)
        c['height']=70+max(1,len(c['attributes']))*25+max(1,len(c['operations']))*25 if c['kind']=='Class' else 76
        by_package[c['package_id']].append(c)
    children={p['id']:[] for p in model['packages']}
    for p in model['packages']:
        if p['parent_id']:children[p['parent_id']].append(p)
    def layout(pid,x,y):
        start=y;right=x+360;cursor=y+64
        rows={}
        for c in sorted(by_package[pid],key=lambda c:(model['ranks'][c['id']],c['id'])):rows.setdefault(model['ranks'][c['id']],[]).append(c)
        for _,row in sorted(rows.items()):
            for offset in range(0,len(row),3):
                part=row[offset:offset+3];cx=x+32;rh=max(c['height'] for c in part)
                for c in part:
                    boxes[c['id']]={'x':cx,'y':cursor,'width':c['width'],'height':c['height']};cx+=c['width']+220
                right=max(right,cx-180);cursor+=rh+100
        for child in children[pid]:
            w,h=layout(child['id'],x+32,cursor);right=max(right,x+32+w+32);cursor+=h+54
        height=max(120,cursor-start-32);package_boxes[pid]={'x':x,'y':start,'width':right-x,'height':height}
        return right-x,height
    width,height=layout(model['model_id'],20,70);width+=70;height+=140
    pieces=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><defs><marker id="uml-generalization" viewBox="0 0 20 20" refX="18" refY="10" markerWidth="14" markerHeight="14" orient="auto" markerUnits="userSpaceOnUse"><path d="M1,1 L18,10 L1,19 Z" fill="white" stroke="#263440" stroke-width="1.5"/></marker></defs><rect width="100%" height="100%" fill="white"/>',f'<text x="24" y="36" font-family="TogafCJK" font-size="22">{esc(model["name"])} — UML 类图</text>']
    for p in model['packages']:
        b=package_boxes[p['id']];x,y,w,h=b['x'],b['y'],b['width'],b['height'];label=('«model» ' if p['kind']=='Model' else '')+p['visibility']+p['name'];tab=max(150,text_width(label)+24)
        pieces.append(f'<g data-native-id="{esc(p["id"])}" class="uml-package"><path d="M{x},{y+22} V{y} H{x+tab} V{y+22} H{x+w} V{y+h} H{x} Z" fill="white" stroke="#647583" stroke-width="1.3"/><text x="{x+10}" y="{y+17}" font-family="TogafCJK" font-size="14">{esc(label)}</text></g>')
    for relation in model['relations']:
        a,b=boxes[relation['source_id']],boxes[relation['target_id']];ax,ay=a['x']+a['width']/2,a['y']+a['height']/2;bx,by=b['x']+b['width']/2,b['y']+b['height']/2
        if relation['source_id']==relation['target_id']:
            sx,sy=a['x']+a['width'],a['y']+a['height']/3;tx,ty=sx,a['y']+2*a['height']/3;d=f'M{sx},{sy} H{sx+50} V{ty} H{tx}';lx,ly=sx+52,(sy+ty)/2
        elif abs(ay-by)<max(a['height'],b['height'])*0.5:
            direction=1 if bx>ax else -1;sx,sy=ax+direction*a['width']/2,ay;tx,ty=bx-direction*b['width']/2,by;d=f'M{sx},{sy} L{tx},{ty}';lx,ly=(sx+tx)/2,(sy+ty)/2-12
        else:
            direction=1 if by>ay else -1;sx,sy=ax,ay+direction*a['height']/2;tx,ty=bx,by-direction*b['height']/2;middle=(sy+ty)/2;d=f'M{sx},{sy} V{middle} H{tx} V{ty}';lx,ly=(sx+tx)/2+10,middle-10
        arrow=' marker-end="url(#uml-generalization)"' if relation['kind']=='generalization' else ''
        pieces.append(f'<g data-native-id="{esc(relation["id"])}" class="uml-{relation["kind"]}"><path d="{d}" fill="none" stroke="#263440" stroke-width="1.7"{arrow}/>')
        if relation['kind']=='association':
            for index,(end,x,y) in enumerate(((relation['ends'][0],sx,sy),(relation['ends'][1],tx,ty))):
                label=(end['name']+' ' if end['name'] else '')+end['multiplicity']
                # Move endpoint text into the inter-class corridor, away from box compartments.
                if relation['source_id']==relation['target_id']:
                    dx,dy,anchor=12,-10,'start'
                elif abs(ay-by)<max(a['height'],b['height'])*0.5:
                    toward=(tx-sx) if index==0 else (sx-tx)
                    dx=12 if toward>0 else -12;dy=-10;anchor='start' if dx>0 else 'end'
                else:
                    toward=(ty-sy) if index==0 else (sy-ty)
                    dx,dy,anchor=12,20 if toward>0 else -10,'start'
                end_labels.append({'id':end['id'],'text':label,'x':x+dx,'y':y+dy,'anchor':anchor,'type_id':end['type_id']})
                pieces.append(f'<text data-native-id="{esc(end["id"])}" x="{x+dx}" y="{y+dy}" text-anchor="{anchor}" font-family="TogafCJK" font-size="13">{esc(label)}</text>')
            if relation['name'] or relation['visibility']:pieces.append(f'<text x="{lx}" y="{ly-18}" text-anchor="middle" font-family="TogafCJK" font-size="13">{esc(relation["visibility"]+relation["name"])}</text>')
        pieces.append('</g>')
    # Opaque classifier rectangles are painted after edges, so connectors never show through compartments.
    for c in model['classifiers']:
        b=boxes[c['id']];x,y,w,h=b['x'],b['y'],b['width'],b['height'];style='font-style:italic;' if c['abstract'] else ''
        pieces.append(f'<g data-native-id="{esc(c["id"])}" class="uml-classifier"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#263440" stroke-width="1.5"/>')
        title_y=y+28
        if c['kind']=='PrimitiveType':pieces.append(f'<text x="{x+w/2}" y="{title_y}" text-anchor="middle" font-family="TogafCJK" font-size="14">«primitive»</text>');title_y+=24
        skew=f' transform="translate({x+w/2},{title_y}) skewX(-12) translate({-(x+w/2)},{-title_y})"' if c['abstract'] else ''
        pieces.append(f'<text x="{x+w/2}" y="{title_y}" text-anchor="middle" font-family="TogafCJK" font-size="16" style="{style}"{skew}>{esc(c["visibility"]+c["name"])}</text>')
        if c['kind']=='Class':
            sep1=y+44;sep2=sep1+max(1,len(c['attributes']))*25+10
            pieces.append(f'<path d="M{x},{sep1} H{x+w} M{x},{sep2} H{x+w}" stroke="#263440" fill="none"/>')
            for i,a in enumerate(c['attributes']):
                decoration='text-decoration:underline;' if a['static'] else ''
                pieces.append(f'<text data-native-id="{esc(a["id"])}" x="{x+14}" y="{sep1+23+i*25}" font-family="TogafCJK" font-size="14" style="{decoration}">{esc(a["text"])}</text>')
            for i,o in enumerate(c['operations']):
                decoration=('text-decoration:underline;' if o['static'] else '')+('font-style:italic;' if o['abstract'] else '')
                parameter_ids=' '.join(p['id'] for p in o['parameters']+o['returns'])
                baseline=sep2+23+i*25;skew=f' transform="translate({x+14},{baseline}) skewX(-12) translate({-(x+14)},{-baseline})"' if o['abstract'] else ''
                pieces.append(f'<text data-native-id="{esc(o["id"])}" data-parameter-native-ids="{esc(parameter_ids)}" x="{x+14}" y="{baseline}" font-family="TogafCJK" font-size="14" style="{decoration}"{skew}>{esc(o["text"])}</text>')
        pieces.append('</g>')
    pieces.append('</svg>')
    return ''.join(pieces),{'classifiers':boxes,'packages':package_boxes,'relation_end_labels':end_labels}


def render_native(data,out,package_root=None):
    model=diagram_model(data,package_root);svg,layout=svg_diagram(model)
    out=Path(out).resolve();base=out.with_suffix('') if out.suffix.lower() in {'.svg','.png'} else out/'diagram'
    paths={'svg':base.with_suffix('.svg'),'png':base.with_suffix('.png'),'report':base.with_suffix('.render.json')}
    if any(p.exists() for p in paths.values()):raise Invalid('Refusing to overwrite an existing UML rendering or evidence report')
    with tempfile.TemporaryDirectory(prefix='uml-notation-') as tmp:
        folder=Path(tmp)
        from generate import subset_font
        font_b64=subset_font(svg,folder/'font.ttf')
        svg=svg.replace('<defs>','<defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+font_b64+')}</style>',1)
        (folder/'diagram.svg').write_text(svg)
        jobs={'font':'font.ttf','jobs':[{'id':'native-uml-class','kind':'svg','source':'diagram.svg','svg':'diagram.svg','png':'diagram.png'}]}
        (folder/'jobs.json').write_text(json.dumps(jobs))
        run=subprocess.run([shutil.which('node') or 'node',str(ROOT/'scripts/render.mjs'),str(folder/'jobs.json')],capture_output=True,text=True,timeout=120)
        if run.returncode:
            if run.returncode==3:raise Incomplete('UML notation raster backend blocked: '+(run.stderr or run.stdout)[-2000:])
            raise Invalid('UML notation raster backend failed: '+(run.stderr or run.stdout)[-2000:])
        raster=json.loads((folder/'render-report.json').read_text())
        result={'status':'passed','operation':'render','language':'uml','version':'2.5.1','notation_status':'native-class-diagram-subset',
                'renderer':'Native UML compartment/relationship renderer + resvg 2.6.2','layout_status':'layout generated; UMLDI not preserved',
                'supported_scope':'Model/Package, Class/PrimitiveType, attributes, operations/parameters, acyclic Class generalization and ordinary non-navigable binary Class associations with explicit literal bounds.',
                'conformance_status':'incomplete','full_language_acceptance':False,'source_sha256':sha(data),
                'classifier_count':len(model['classifiers']),'relation_count':len(model['relations']),'model':model,'layout':layout,'raster':raster,
                'outputs':{k:str(p) for k,p in paths.items()},'svg_sha256':sha(svg.encode()),'png_sha256':sha((folder/'diagram.png').read_bytes()),
                'limits':['Full UML metamodel/OCL, all 673 constructs, Profiles and UMLDI acceptance are incomplete.','Unsupported constructs/properties, external or unresolved types, navigability, association classes, aggregation and composition are refused.','Generated layout is a new reading view; original XML bytes/IDs are preserved in inventory and mapped fields.','This operation does not grant professional notation certification or business acceptance.']}
        for kind in ('svg','png'):write_new(paths[kind],(folder/('diagram.'+kind)).read_bytes())
        write_new(paths['report'],json.dumps(result,ensure_ascii=False,indent=2).encode())
        return result
