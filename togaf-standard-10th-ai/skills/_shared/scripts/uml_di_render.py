"""Bounded native UMLDI class views: original positions and routes are authoritative.

Supports ClassifierShapes for Classes, explicit text labels/compartments, ordinary
binary Associations and Generalizations. Other diagrams and notation options are
refused. Viewport and separator/arrow decorations are derived, never written into
the native model. This is not full UML/DI notation or metamodel certification.
"""
import html
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile
from functools import lru_cache

from standards import ROOT, XMI, Invalid, Incomplete, check_native, safe_xml, local, namespace, sha, write_new
from uml_design_semantics import FAMILIES, source_schema, instance_type, conforms, scalar_value, reference_values

LABELS = {'UMLLabel', 'UMLNameLabel', 'UMLMultiplicityLabel', 'UMLKeywordLabel'}
CONTAINMENT = ('ownedElement', 'compartment', 'elementInCompartment')
SUPPORTED = {'UMLClassDiagram', 'UMLClassifierShape', 'UMLCompartment', 'UMLEdge', *LABELS}


@lru_cache(maxsize=2)
def _font_metrics(path, fingerprint):
    from fontTools.ttLib import TTFont
    if sha(Path(path).read_bytes())!=fingerprint: raise Incomplete('Local bundled font changed during geometry check')
    with TTFont(path) as font:
        return font.getBestCmap(),dict(font['hmtx'].metrics),font['head'].unitsPerEm


def text_width(text, size):
    font=ROOT/'assets/fonts/NotoSansSC.ttf'
    if not font.is_file(): raise Incomplete('Bundled local font is missing')
    cmap,metrics,units=_font_metrics(str(font),sha(font.read_bytes()))
    if any(ord(c) not in cmap for c in text): raise Incomplete('Native label has a glyph unavailable in the bundled font')
    return sum(metrics[cmap[ord(c)]][0] for c in text)*size/units


def has_native_di(data):
    root = safe_xml(data) if isinstance(data, bytes) else data
    for element in root.iter():
        if not isinstance(element.tag, str): continue
        if FAMILIES.get(namespace(element.tag)) == 'UMLDI.xmi': return True
        raw = element.get('{'+XMI+'}type', '')
        if ':' in raw and FAMILIES.get(element.nsmap.get(raw.partition(':')[0])) == 'UMLDI.xmi': return True
    return False


def diagram_plan(data, package_root=None):
    validation = check_native(data, 'uml', '2.5.1', package_root)
    if validation['errors']: raise Invalid('; '.join(validation['errors']))
    blockers = [b for b in validation['blockers'] if not b.startswith('complete UML2/OCL')]
    if blockers: raise Incomplete('; '.join(blockers))
    root = safe_xml(data); schema = source_schema()
    ids = {e.get('{'+XMI+'}id'): e for e in root.iter() if isinstance(e.tag,str) and e.get('{'+XMI+'}id')}
    types = {e: instance_type(e, schema) for e in root.iter() if isinstance(e.tag,str)}
    diagrams = [e for e, kind in types.items() if kind and kind[0]=='UMLDI.xmi' and kind[1].endswith('Diagram')]
    if len(diagrams)!=1 or types[diagrams[0]]!=('UMLDI.xmi','UMLClassDiagram'):
        raise Incomplete('Only exactly one native UMLClassDiagram is supported; other diagram categories remain uncovered')
    diagram = diagrams[0]; visited = set(); native_bounds = {}; native_routes = {}
    def identity(element):
        value = element.get('{'+XMI+'}id')
        if not value: raise Incomplete('Explicit native xmi:id is required for UMLDI diagram elements')
        return value
    def refs(element, field):
        return [token.removeprefix('#') if token else None for token, _ in reference_values(element,field)]
    def one(element, field):
        values = refs(element,field)
        if len(values)!=1 or values[0] not in ids: raise Incomplete('One local '+field+' is required for '+identity(element))
        return ids[values[0]]
    def multiplicity(element, field, expected):
        values = reference_values(element,field)
        if not values: return '1'
        if len(values)!=1: raise Incomplete('One literal '+field+' is required for native multiplicity notation')
        token,child=values[0]
        literal=ids.get(token.removeprefix('#')) if token else child
        if literal is None or types.get(literal)!=('UML.xmi',expected):
            raise Incomplete('Only explicit literal native multiplicity values are supported')
        value=str(scalar_value(literal,'value',schema,'0')).strip()
        try: return '*' if value=='*' else str(int(value))
        except ValueError: raise Incomplete('Literal native multiplicity exceeds the bounded local representation')
    def attributes(element, allowed):
        unknown = [key for key in element.attrib if not (namespace(key)==XMI and local(key) in {'id','type','version'}) and key not in allowed]
        if unknown: raise Incomplete('Unrepresented native UMLDI attributes on '+identity(element)+': '+', '.join(unknown))
    def bounds(element):
        nodes = [c for c in element if isinstance(c.tag,str) and local(c.tag)=='bounds']
        if len(nodes)!=1: raise Incomplete('Explicit native bounds are required for '+identity(element)+'; no layout generated')
        node=nodes[0]
        if any(field not in node.attrib for field in ('x','y','width','height')):
            raise Incomplete('Complete native bounds are required for '+identity(element))
        row={key:node.get(key) for key in ('x','y','width','height')}
        if float(row['width'])<=0 or float(row['height'])<=0:
            raise Incomplete('Positive renderable native bounds are required for '+identity(element))
        native_bounds[identity(element)]=row
        return row
    def owned(element):
        values=[]
        for field in CONTAINMENT:
            for token in element.get(field,'').split():
                if token not in ids: raise Incomplete('Unresolved UMLDI containment: '+token)
                values.append(ids[token])
        for child in element:
            if not isinstance(child.tag,str) or local(child.tag) not in CONTAINMENT: continue
            token=child.get('{'+XMI+'}idref') or child.get('href')
            if token:
                if token.removeprefix('#') not in ids: raise Incomplete('Unresolved UMLDI containment: '+token)
                values.append(ids[token.removeprefix('#')])
            else: values.append(child)
        return values
    resolution_raw=scalar_value(diagram,'resolution',schema,'300')
    resolution=float(resolution_raw)
    if not math.isfinite(resolution) or resolution<=0: raise Invalid('Positive finite diagram resolution is required')
    def style(element):
        styled=[]
        for token in refs(element,'sharedStyle'):
            if token not in ids: raise Incomplete('Unresolved shared style')
            styled.append(ids[token])
        styled.extend(c for c in element if isinstance(c.tag,str) and local(c.tag)=='localStyle')
        result={'font_name':'TogafCJK','font_size_points':11.0,'font_units':11.0*resolution/72,
                'basis':'Bundled font and 11pt display default when no native style is supplied'}
        for node in styled:
            if types.get(node)!=('UMLDI.xmi','UMLStyle'): raise Incomplete('Only native UMLStyle is supported')
            attributes(node,{'fontName','fontSize'})
            name=scalar_value(node,'fontName',schema)
            if name not in (None,'TogafCJK'): raise Incomplete('Native fontName is not available in the bounded bundled-font renderer: '+str(name))
            size=scalar_value(node,'fontSize',schema)
            if size is None: raise Incomplete('Optional absent fontSize remains unadjudicated')
            result.update(font_size_points=float(size),font_units=float(size)*resolution/72,
                          basis='Native UMLStyle.fontSize points mapped by native Diagram.resolution user units per inch')
        return result
    def child_nodes(element, parent_style):
        return [node(child,parent_style) for child in owned(element)]
    def node(element,parent_style=None):
        nid=identity(element)
        if nid in visited: raise Incomplete('Repeated or cyclic UMLDI containment is unsupported: '+nid)
        visited.add(nid)
        kind=types.get(element)
        if kind is None or kind[0]!='UMLDI.xmi' or kind[1] not in SUPPORTED:
            raise Incomplete('Unsupported native UMLDI element: '+str(kind))
        name=kind[1]; allowed={'modelElement','sharedStyle','isIcon',*CONTAINMENT}
        if name=='UMLClassDiagram': allowed.update({'name','resolution','isFrame','isIso','isInheritedLighter','heading','isAssociationDotShown','navigabilityNotation','nonNavigabilityNotation'})
        elif name=='UMLClassifierShape': allowed.update({'isDoubleSided','isIndentForVisibility'})
        elif name in LABELS: allowed.add('text')
        elif name=='UMLEdge': allowed.update({'source','target'})
        attributes(element,allowed)
        allowed_children={'bounds','localStyle','modelElement','sharedStyle','source','target','heading',*CONTAINMENT}
        if name=='UMLEdge': allowed_children.add('waypoint')
        if name in LABELS: allowed_children.add('text')
        for child in element:
            if isinstance(child.tag,str) and local(child.tag) not in allowed_children:
                raise Incomplete('Unrepresented UMLDI child '+local(child.tag)+' on '+nid)
        if str(scalar_value(element,'isIcon',schema,'false')).strip() in ('true','1'):
            raise Incomplete('Icon notation is not supported for '+nid)
        own_style=style(element) if refs(element,'sharedStyle') or any(local(c.tag)=='localStyle' for c in element) else (parent_style or style(element))
        result={'id':nid,'kind':name,'model_ids':refs(element,'modelElement'),'style':own_style}
        if name=='UMLClassDiagram':
            result['name']=scalar_value(element,'name',schema)
            if str(scalar_value(element,'isIso',schema,'true')).strip() not in ('true','1'):
                raise Incomplete('Non-ISO native diagram notation remains unsupported')
            if str(scalar_value(element,'isInheritedLighter',schema,'false')).strip() in ('true','1'):
                raise Incomplete('Lighter inherited-element notation remains unsupported')
            if str(scalar_value(element,'isAssociationDotShown',schema,'false')).strip() in ('true','1'):
                raise Incomplete('Association dot notation remains unsupported')
            for field,default in (('navigabilityNotation','oneWay'),('nonNavigabilityNotation','never')):
                if scalar_value(element,field,schema,default)!=default:
                    raise Incomplete('Non-default native '+field+' remains unsupported')
            result['frame']=str(scalar_value(element,'isFrame',schema)).strip() in ('true','1')
            if result['frame']: result['bounds']=bounds(element)
        elif name=='UMLClassifierShape':
            model=one(element,'modelElement')
            if types.get(model)!=('UML.xmi','Class'): raise Incomplete('Only UML Classes are supported by native ClassifierShapes')
            if str(scalar_value(element,'isIndentForVisibility',schema,'false')).strip() in ('true','1'):
                raise Incomplete('Visibility heading indentation remains unsupported')
            result.update(bounds=bounds(element),abstract=str(scalar_value(model,'isAbstract',schema,'false')).strip() in ('true','1'),
                          double_sided=str(scalar_value(element,'isDoubleSided',schema,'false')).strip() in ('true','1'),class_name=scalar_value(model,'name',schema))
        elif name in LABELS:
            result['bounds']=bounds(element);text=scalar_value(element,'text',schema)
            if not isinstance(text,str) or not text.strip() or len(text)>240:
                raise Incomplete('A nonempty native text label of at most 240 characters is required for '+nid)
            result['text']=text
            if '\n' in text or '\r' in text: raise Incomplete('Multiline native labels remain unsupported')
            if name=='UMLMultiplicityLabel':
                model=one(element,'modelElement')
                lower=multiplicity(model,'lowerValue','LiteralInteger')
                upper=multiplicity(model,'upperValue','LiteralUnlimitedNatural')
                expected=lower if lower==upper else lower+'..'+upper
                if text not in (expected, '1..1' if expected=='1' else expected):
                    raise Invalid('Native multiplicity label disagrees with semantic lower/upper values: '+nid)
            width=text_width(text,own_style['font_units'])
            if width>float(result['bounds']['width']) or own_style['font_units']*1.25>float(result['bounds']['height']):
                raise Incomplete('Native label bounds are too small for source text/style: '+nid+'; no coordinates changed')
        elif name=='UMLEdge':
            source,target=one(element,'source'),one(element,'target');model=one(element,'modelElement')
            if types.get(source)!=('UMLDI.xmi','UMLClassifierShape') or types.get(target)!=('UMLDI.xmi','UMLClassifierShape'):
                raise Incomplete('Only ClassifierShape edge endpoints are supported')
            sid,tid=refs(source,'modelElement')[0],refs(target,'modelElement')[0]
            relation=types.get(model)
            if relation==('UML.xmi','Generalization'):
                specifics=refs(model,'specific')
                owner=specifics[0] if len(specifics)==1 else model.getparent().get('{'+XMI+'}id') if not specifics else None
                if owner!=sid or refs(model,'general')!=[tid]: raise Invalid('Native generalization endpoints disagree with semantic source/target')
                result['relation']='generalization'
            elif relation==('UML.xmi','Association'):
                ends=[ids.get(token) for token in refs(model,'memberEnd')]
                if len(ends)!=2 or any(e is None for e in ends): raise Incomplete('Only binary native Associations are supported')
                end_types=[refs(e,'type') for e in ends]
                if sorted(end_types)!=sorted([[sid],[tid]]): raise Invalid('Native association endpoints disagree with memberEnd types')
                if refs(model,'navigableOwnedEnd') or any(str(scalar_value(e,'aggregation',schema,'none')).strip()!='none' or e.getparent() is not model for e in ends):
                    raise Incomplete('Native association navigability/aggregation remain unsupported')
                if str(scalar_value(model,'isDerived',schema,'false')).strip() in ('true','1'):
                    raise Incomplete('Derived native association notation remains unsupported')
                result['relation']='association'
            else: raise Incomplete('Unsupported native UMLDI relation: '+str(relation))
            points=[{key:c.get(key) for key in ('x','y')} for c in element if isinstance(c.tag,str) and local(c.tag)=='waypoint']
            if len(points)<2 or len(points)>500 or any(p['x'] is None or p['y'] is None for p in points):
                raise Incomplete('Two to 500 explicit native waypoints are required; no routing generated')
            if len({(float(p['x']),float(p['y'])) for p in points})<2:
                raise Incomplete('A visible native edge requires distinct waypoints; no routing generated')
            native_routes[nid]=points
            result.update(waypoints=points,source_id=identity(source),target_id=identity(target))
        result['children']=child_nodes(element,own_style)
        if name=='UMLClassifierShape':
            titles=[c for c in result['children'] if c['kind'] in LABELS and c['model_ids']==result['model_ids'] and c.get('text')==result['class_name']]
            if not titles: raise Incomplete('An explicit native Class name label is required; no label position generated')
            for child in titles: child['italic']=result['abstract']
        return result
    scene=node(diagram)
    # A heading may be a contained label or a referenced standalone label.
    for heading in refs(diagram,'heading'):
        if heading not in visited: scene['children'].insert(0,node(ids[heading],scene['style']))
    if scene.get('frame'):
        heading=next((child for child in scene['children'] if child['id'] in refs(diagram,'heading')),None)
        if heading is None or heading['kind']!='UMLLabel': raise Incomplete('An explicit plain UMLLabel heading is required')
        scene['heading_id']=heading['id']
    if len(visited)>100: raise Incomplete('Native class view capacity is 100 diagram elements')
    unrepresented=[identity(e) for e,kind in types.items() if kind and conforms(schema,kind,('DI.xmi','DiagramElement')) and e.get('{'+XMI+'}id') not in visited]
    if unrepresented: raise Incomplete('Native UMLDI diagram elements outside supported containment remain unrepresented: '+', '.join(unrepresented))
    if not any(types[ids[n]]==('UMLDI.xmi','UMLClassifierShape') for n in visited):
        raise Incomplete('Native class view requires at least one ClassifierShape')
    ordered=[]
    def ordering(item):
        if item['kind']=='UMLClassifierShape': ordered.append({'shape_id':item['id'],'compartment_ids':[c['id'] for c in item['children'] if c['kind']=='UMLCompartment']})
        for child in item['children']: ordering(child)
    ordering(scene)
    return {'scene':scene,'native_bounds':native_bounds,'native_waypoints':native_routes,'ordered_compartments':ordered,
        'native_di_validation':validation['design_time_semantics'],'source_sha256':sha(data),'resolution':resolution_raw,
        'coordinate_policy':'Native numeric strings, coordinates, route points and compartment order preserved; no native layout generated',
        'derived_layout':False,'full_language_acceptance':False}


def svg_diagram(plan):
    esc=lambda value:html.escape(str(value),quote=True)
    bounds=plan['native_bounds']; routes=plan['native_waypoints']; points=[]
    for box in bounds.values():
        x,y,w,h=[float(box[k]) for k in ('x','y','width','height')];points.extend(((x,y),(x+w,y+h)))
    for route in routes.values(): points.extend((float(p['x']),float(p['y'])) for p in route)
    xmin=min(p[0] for p in points)-12;ymin=min(p[1] for p in points)-12
    width=max(p[0] for p in points)+12-xmin;height=max(p[1] for p in points)+12-ymin
    if max(width,height)>8192 or width*height>16777216: raise Incomplete('Native viewport exceeds local raster capacity; coordinates unchanged')
    pieces=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{xmin} {ymin} {width} {height}"><defs><marker id="native-generalization" viewBox="0 0 20 20" refX="18" refY="10" markerWidth="14" markerHeight="14" orient="auto" markerUnits="userSpaceOnUse"><path d="M1,1 L18,10 L1,19 Z" fill="white" stroke="#263440" stroke-width="1.5"/></marker></defs><rect x="{xmin}" y="{ymin}" width="{width}" height="{height}" fill="white"/>']
    decorations=[]
    def paint(item,box_parent=None):
        kind=item['kind'];pieces.append(f'<g data-native-id="{esc(item["id"])}" data-model-ids="{esc(" ".join(item["model_ids"]))}" class="native-{kind}">')
        if kind in ('UMLClassifierShape','UMLClassDiagram') and 'bounds' in item:
            b=item['bounds'];x,y,w,h=(b[k] for k in ('x','y','width','height'))
            pieces.append(f'<rect x="{esc(x)}" y="{esc(y)}" width="{esc(w)}" height="{esc(h)}" fill="white" stroke="#263440" stroke-width="1.5"/>')
            if kind=='UMLClassDiagram' and item.get('frame'):
                heading=next(c for c in item['children'] if c['id']==item['heading_id'])['bounds']
                right=float(heading['x'])+float(heading['width'])+6
                bottom=float(heading['y'])+float(heading['height'])
                if float(heading['x'])<float(x) or float(heading['y'])<float(y) or right>=float(x)+float(w) or bottom>=float(y)+float(h):
                    raise Incomplete('Native heading does not fit the diagram frame')
                pieces.append(f'<path data-derived-decoration="heading-border" d="M{x},{bottom} H{right-8} L{right},{bottom-8} V{y}" fill="none" stroke="#263440"/>')
                decorations.append({'heading_id':item['heading_id'],'right':right,'bottom':bottom,
                    'basis':'Pentagonal header border derived from native heading bounds; native label/frame coordinates unchanged'})
            if item.get('double_sided'):
                left,right=float(x)+4,float(x)+float(w)-4
                pieces.append(f'<path d="M{left},{y} V{float(y)+float(h)} M{right},{y} V{float(y)+float(h)}" fill="none" stroke="#263440"/>')
            box_parent=b
        elif kind=='UMLEdge':
            native=' '.join(p['x']+','+p['y'] for p in item['waypoints'])
            arrow=' marker-end="url(#native-generalization)"' if item['relation']=='generalization' else ''
            pieces.append(f'<polyline points="{esc(native)}" fill="none" stroke="#263440" stroke-width="1.6"{arrow}/>')
        elif kind in LABELS:
            b=item['bounds'];font=item['style']['font_units'];italic=' font-style="italic"' if item.get('italic') else ''
            skew=f' transform="translate({esc(b["x"])},{esc(b["y"])}) skewX(-12) translate({-float(b["x"])},{-float(b["y"])})"' if item.get('italic') else ''
            pieces.append(f'<text x="{esc(b["x"])}" y="{esc(b["y"])}" dominant-baseline="hanging" font-family="TogafCJK" font-size="{font}"{italic}{skew}>{esc(item["text"])}</text>')
        elif kind=='UMLCompartment' and box_parent is not None and item['children']:
            label_bounds=[c['bounds'] for c in item['children'] if 'bounds' in c]
            if label_bounds:
                y=min(float(b['y']) for b in label_bounds)-6
                if not float(box_parent['y'])<y<float(box_parent['y'])+float(box_parent['height']):
                    raise Incomplete('Native compartment label geometry lies outside its ClassifierShape')
                x=box_parent['x'];right=float(x)+float(box_parent['width'])
                pieces.append(f'<path data-derived-decoration="compartment-separator" d="M{x},{y} H{right}" fill="none" stroke="#263440"/>')
                decorations.append({'compartment_id':item['id'],'separator_y':y,'basis':'Derived separator six units before first native label; native labels/order/bounds unchanged'})
        for child in item['children']: paint(child,box_parent)
        pieces.append('</g>')
    paint(plan['scene']);pieces.append('</svg>')
    return ''.join(pieces),{'native_bounds':bounds,'native_waypoints':routes,'ordered_compartments':plan['ordered_compartments'],
        'viewport':{'x':xmin,'y':ymin,'width':width,'height':height},'derived_decorations':decorations,'derived_layout':False}


def render_native(data,out,package_root=None):
    plan=diagram_plan(data,package_root);svg,geometry=svg_diagram(plan)
    out=Path(out).resolve();base=out.with_suffix('') if out.suffix.lower() in {'.svg','.png'} else out/'diagram'
    paths={'svg':base.with_suffix('.svg'),'png':base.with_suffix('.png'),'report':base.with_suffix('.render.json'),
           'source':base.with_suffix('.native.uml')}
    if any(p.exists() for p in paths.values()): raise Invalid('Refusing to overwrite native UMLDI rendering or source evidence')
    with tempfile.TemporaryDirectory(prefix='uml-native-di-') as tmp:
        folder=Path(tmp)
        from generate import subset_font
        font=subset_font(svg,folder/'font.ttf')
        svg=svg.replace('<defs>','<defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+font+')}</style>',1)
        (folder/'diagram.svg').write_text(svg)
        (folder/'jobs.json').write_text(json.dumps({'font':'font.ttf','jobs':[{'id':'native-uml-di-class','kind':'svg','source':'diagram.svg','svg':'diagram.svg','png':'diagram.png'}]}))
        run=subprocess.run([shutil.which('node') or 'node',str(ROOT/'scripts/render.mjs'),str(folder/'jobs.json')],capture_output=True,text=True,timeout=120)
        if run.returncode: raise Incomplete('Native UMLDI local raster backend blocked: '+(run.stderr or run.stdout)[-2000:])
        raster=json.loads((folder/'render-report.json').read_text())
        result={'status':'passed','operation':'render','language':'uml','version':'2.5.1','notation_status':'native-umldi-class-subset',
            'layout_status':'native UMLDI coordinates preserved','source_sha256':sha(data),'conformance_status':'incomplete',
            'full_language_acceptance':False,'model':plan,'layout':geometry,'derived_layout':False,'raster':raster,
            'outputs':{k:str(p) for k,p in paths.items()},'svg_sha256':sha(svg.encode()),'png_sha256':sha((folder/'diagram.png').read_bytes()),
            'supported_scope':'One UMLClassDiagram; ClassifierShapes for Classes, native text/compartments, ordinary binary Associations and Generalizations; explicit bounds/routes only.',
            'limits':['Other UML diagram categories, icons, arbitrary profiles and full notation/editing remain unsupported.',
                      'Viewport and compartment/arrow decorations are derived, native model/coordinates/waypoint/order bytes are preserved.',
                      'Native Diagram.resolution maps font points to user units; unsupported fonts or insufficient native label bounds are refused.',
                      'Full applicable normative obligations and professional/business acceptance remain incomplete.']}
        for kind in ('svg','png'): write_new(paths[kind],(folder/('diagram.'+kind)).read_bytes())
        write_new(paths['source'],data);write_new(paths['report'],json.dumps(result,ensure_ascii=False,indent=2).encode())
        return result
