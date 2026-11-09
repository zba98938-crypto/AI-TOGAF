"""Explicitly selected, deterministic derived BPMNDI layout using local code.

Existing bounds/waypoints are retained verbatim. Only omitted graphics are added
to a separate derived XML document. The caller must opt in; this is not a silent
repair of invalid geometry or a professional visual acceptance decision.
"""
import math
from copy import deepcopy
from lxml import etree
from bpmn_references import local_reference
from bpmn_design_semantics import CONVERSATIONS, CHOREOGRAPHY_ACTIVITIES
from standards import BPMN, Invalid, Incomplete, check_native, safe_xml, local, sha

DI='http://www.omg.org/spec/BPMN/20100524/DI'
DC='http://www.omg.org/spec/DD/20100524/DC'
DD='http://www.omg.org/spec/DD/20100524/DI'


def derive_layout(data, package_root=None):
    from bpmn_render import SHAPES, EDGES, CONTAINERS
    root=safe_xml(data)
    semantic=deepcopy(root)
    for e in list(semantic.iter('{'+DI+'}BPMNDiagram')):
        e.getparent().remove(e)
    validation=check_native(etree.tostring(semantic),'bpmn','2.0.2',package_root)
    if validation['errors']:
        raise Invalid('; '.join(validation['errors']))
    blockers=[b for b in validation['blockers'] if not b.startswith('complete BPMN normative')]
    if blockers:
        raise Incomplete('; '.join(blockers))
    nodes={e.get('id'):e for e in root.iter() if isinstance(e.tag,str) and e.get('id')}
    q=lambda k:'{'+BPMN+'}'+k
    ref=lambda e,v:local_reference(e,v,root.get('targetNamespace'))[0]
    resolve=lambda e,v:nodes.get(ref(e,v))
    diagrams=list(root.iter('{'+DI+'}BPMNDiagram'))
    added=[]
    original_geometry=[]
    geometry_objects=[]
    for e in root.iter():
        if isinstance(e.tag,str) and local(e.tag) in {'Bounds','waypoint'}:
            original_geometry.append((root.getroottree().getpath(e),dict(e.attrib)))
            geometry_objects.append((e,dict(e.attrib)))
    def ident(prefix):
        base='Derived_'+prefix
        result=base;index=1
        while result in nodes:
            result=base+'_'+str(index);index+=1
        nodes[result]=None
        return result
    if len(diagrams)>1:
        raise Incomplete('Explicit auto-layout needs a single selected BPMNDiagram')
    if diagrams:
        planes=diagrams[0].findall('{'+DI+'}BPMNPlane')
        if len(planes)!=1:
            raise Invalid('BPMNDiagram requires one BPMNPlane')
        plane=planes[0];owner=resolve(plane,plane.get('bpmnElement'))
    else:
        called={ref(e,e.get(a)) for e in root.iter() for a in ('calledChoreographyRef','calledCollaborationRef') if e.get(a)}
        processes={ref(e,e.get('processRef')) for e in root.iter(q('participant')) if e.get('processRef')}
        candidates=[e for e in root if isinstance(e.tag,str) and local(e.tag) in {'process','collaboration','choreography'} and e.get('id') not in called|processes]
        if len(candidates)!=1:
            raise Incomplete('Explicit auto-layout requires one unambiguous noncalled Process/Collaboration/Choreography root')
        owner=candidates[0]
        diagram=etree.SubElement(root,'{'+DI+'}BPMNDiagram',id=ident('Diagram'))
        plane=etree.SubElement(diagram,'{'+DI+'}BPMNPlane',id=ident('Plane'),bpmnElement=owner.get('id'))
        added.append({'kind':'diagram','semantic_id':owner.get('id')})
    if owner is None or local(owner.tag) not in {'process','collaboration','choreography'}:
        raise Incomplete('Auto-layout root is not a supported design-time view')
    shapes={};edges={};occupied=[]
    def box(e):
        b=e.find('{'+DC+'}Bounds')
        try:
            values=[float(b.get(k)) for k in ('x','y','width','height')]
            if not all(map(math.isfinite,values)) or min(values[2:])<=0:raise ValueError()
        except (AttributeError,ValueError,TypeError):
            raise Invalid('Existing BPMNDI bounds must be finite and complete; explicit auto-layout will not replace invalid coordinates')
        return dict(zip(('x','y','width','height'),values))
    for e in plane:
        sid=ref(e,e.get('bpmnElement'))
        if local(e.tag)=='BPMNShape':
            b=box(e);shapes.setdefault(sid,[]).append(e)
            if not e.get('participantBandKind'):occupied.append(b)
        elif local(e.tag)=='BPMNEdge':
            points=[c for c in e if local(c.tag)=='waypoint']
            try:
                if len(points)<2 or not all(math.isfinite(float(c.get(k))) for c in points for k in ('x','y')):raise ValueError()
            except (TypeError,ValueError):raise Invalid('Existing BPMNDI waypoints must be finite and complete')
            edges[sid]=e
    cursor=[max([b['x']+b['width'] for b in occupied]+[0])+80,80]
    shapes_required=[];edges_required=[];visiting=set()
    def dimensions(e):
        k=local(e.tag)
        if k in CONVERSATIONS:return 56,56
        if k in CHOREOGRAPHY_ACTIVITIES:
            return 180,max(160,80+40*len(e.findall(q('participantRef'))))
        if k.endswith('Event'):return 36,36
        if k.endswith('Gateway'):return 50,50
        if k=='participant':return 150,320
        if k in {'dataObjectReference','dataInput','dataOutput'}:return 50,65
        if k=='dataStoreReference':return 60,65
        if k in {'textAnnotation','group'}:return 200,100
        return 150,100
    def graphic(e,region=None):
        sid=e.get('id')
        if not sid:raise Invalid('Auto-layout requires stable native IDs')
        existing=[s for s in shapes.get(sid,[]) if not s.get('participantBandKind')]
        if existing:return existing[0]
        w,h=dimensions(e)
        if region is None:
            x,y=cursor;cursor[0]+=w+100
        else:
            x,y=region[0],region[1]
            if x+w>region[2] or y+h>region[3]:
                raise Incomplete('Missing graphics do not fit the preserved explicit container bounds: '+sid)
            region[0]+=w+60
        s=etree.SubElement(plane,'{'+DI+'}BPMNShape',id=ident(sid),bpmnElement=sid)
        etree.SubElement(s,'{'+DC+'}Bounds',x=str(x),y=str(y),width=str(w),height=str(h))
        shapes.setdefault(sid,[]).append(s);occupied.append(box(s))
        added.append({'kind':'shape','semantic_id':sid,'graphic_id':s.get('id'),'bounds':box(s)})
        return s
    def bands(e,s):
        group=[g for items in shapes.values() for g in items if g.get('choreographyActivityShape') and ref(g,g.get('choreographyActivityShape'))==s.get('id')]
        parties=[ref(c,c.text) for c in e.findall(q('participantRef'))]
        shown={ref(g,g.get('bpmnElement')) for g in group}
        missing=[p for p in parties if p not in shown]
        if not missing:return
        # A partial arbitrary band stack cannot safely choose which authoritative
        # central gap to occupy. Existing stacks are retained and diagnosed.
        if group:
            raise Incomplete('Partial Participant Band layout needs explicit remaining band coordinates; existing band positions are retained')
        b=box(s);n=len(parties);band_h=min(40,(b['height']-80)/n)
        if band_h<32:
            raise Incomplete('Preserved activity bounds have insufficient space for participant names and markers: '+e.get('id'))
        initiator=ref(e,e.get('initiatingParticipantRef'))
        for i,party in enumerate(parties):
            pos='top' if i==0 else 'bottom' if i==n-1 else 'middle'
            y=b['y'] if i==0 else b['y']+b['height']-band_h*(n-i)
            g=etree.SubElement(plane,'{'+DI+'}BPMNShape',id=ident(e.get('id')+'_'+party+'_Band'),bpmnElement=party,
                participantBandKind=pos+('_initiating' if party==initiator else '_non_initiating'),choreographyActivityShape=s.get('id'))
            etree.SubElement(g,'{'+DC+'}Bounds',x=str(b['x']),y=str(y),width=str(b['width']),height=str(band_h))
            shapes.setdefault(party,[]).append(g)
            added.append({'kind':'participant-band','semantic_id':party,'graphic_id':g.get('id'),'bounds':box(g)})
    def container(e,region=None):
        if e in visiting:raise Incomplete('Recursive expanded called view requires a finite explicit layout')
        visiting.add(e)
        for child in e:
            if not isinstance(child.tag,str) or not child.tag.startswith('{'+BPMN+'}'):continue
            k=local(child.tag)
            if k=='laneSet':
                raise Incomplete('Automatic lane partitioning requires explicit lane bounds; the native source and declared flowNodeRef assignments are preserved')
            if k in SHAPES|CONVERSATIONS|CHOREOGRAPHY_ACTIVITIES and k!='participant':
                shapes_required.append(child);s=graphic(child,region)
                if k in CHOREOGRAPHY_ACTIVITIES:bands(child,s)
                if k in CONTAINERS|{'subChoreography','callChoreography'} and s.get('isExpanded') in {'true','1'}:
                    b=box(s);inner=[b['x']+45,b['y']+60,b['x']+b['width']-30,b['y']+b['height']-60]
                    called=resolve(child,child.get('calledChoreographyRef')) if k=='callChoreography' else child
                    if called is None:raise Incomplete('Expanded called view is unresolved')
                    container(called,inner)
            elif k in EDGES|{'conversationLink'} and not (k=='messageFlow' and local(e.tag)=='choreography'):
                edges_required.append(child)
        visiting.remove(e)
    if local(owner.tag)=='collaboration':
        for participant in owner.findall(q('participant')):
            process=resolve(participant,participant.get('processRef'))
            existing=[s for s in shapes.get(participant.get('id'),[]) if not s.get('participantBandKind')]
            if process is not None:
                if existing:
                    b=box(existing[0]);region=[b['x']+50,b['y']+50,b['x']+b['width']-30,b['y']+b['height']-30]
                    container(process,region)
                else:
                    before=len(occupied);container(process)
                    children=occupied[before:]
                    if not children:children=[{'x':cursor[0],'y':80,'width':180,'height':100}]
                    x=min(b['x'] for b in children)-50;y=min(b['y'] for b in children)-50
                    w=max(b['x']+b['width'] for b in children)-x+40;h=max(b['y']+b['height'] for b in children)-y+40
                    s=etree.SubElement(plane,'{'+DI+'}BPMNShape',id=ident(participant.get('id')),bpmnElement=participant.get('id'),isHorizontal='true')
                    etree.SubElement(s,'{'+DC+'}Bounds',x=str(x),y=str(y),width=str(w),height=str(h));shapes.setdefault(participant.get('id'),[]).append(s)
                    added.append({'kind':'pool','semantic_id':participant.get('id'),'graphic_id':s.get('id'),'bounds':box(s)})
            else:graphic(participant)
        container(owner)
        grouped={ref(c,c.text) for e in owner.iter() if local(e.tag) in CONVERSATIONS for c in e.findall(q('messageFlowRef'))}
        edges_required=[e for e in edges_required if e.get('id') not in grouped]
    else:container(owner)
    for e in edges_required:
        if e.get('id') in edges:continue
        refs=[]
        for direction in ('source','target'):
            c=e.find(q(direction+'Ref'))
            sid=ref(c,c.text) if c is not None else ref(e,e.get(direction+'Ref'))
            candidates=[s for s in shapes.get(sid,[]) if not s.get('participantBandKind')]
            if len(candidates)!=1:
                raise Incomplete('Missing connector layout requires one explicit visible endpoint depiction: '+str(e.get('id')))
            refs.append(candidates[0])
        a,z=map(box,refs);ac=(a['x']+a['width']/2,a['y']+a['height']/2);zc=(z['x']+z['width']/2,z['y']+z['height']/2)
        horizontal=abs(zc[0]-ac[0])>=abs(zc[1]-ac[1]);sign=1 if zc[0 if horizontal else 1]>=ac[0 if horizontal else 1] else -1
        points=[(ac[0]+sign*a['width']/2,ac[1]),(zc[0]-sign*z['width']/2,zc[1])] if horizontal else [(ac[0],ac[1]+sign*a['height']/2),(zc[0],zc[1]-sign*z['height']/2)]
        g=etree.SubElement(plane,'{'+DI+'}BPMNEdge',id=ident(e.get('id')),bpmnElement=e.get('id'))
        if local(e.tag) in {'dataInputAssociation','dataOutputAssociation'}:
            g.set('sourceElement',refs[0].get('id'));g.set('targetElement',refs[1].get('id'))
        for x,y in points:etree.SubElement(g,'{'+DD+'}waypoint',x=str(x),y=str(y))
        added.append({'kind':'edge','semantic_id':e.get('id'),'graphic_id':g.get('id'),'waypoints':[{'x':x,'y':y} for x,y in points]})
    if not added:return data,{'selected':True,'derived':False,'source_sha256':sha(data),'derived_sha256':sha(data),'added_graphics':[]}
    # Compare original geometry elements by object identity: their XML bytes and
    # numerical attributes have not been touched, even if extra siblings exist.
    if any(dict(e.attrib)!=attrs for e,attrs in geometry_objects):
        raise Invalid('Automatic layout changed an authoritative geometry attribute')
    preserved=[(locator,attrs) for locator,attrs in original_geometry]
    derived=etree.tostring(root,xml_declaration=True,encoding='utf-8')
    result=check_native(derived,'bpmn','2.0.2',package_root)
    if result['errors']:raise Invalid('; '.join(result['errors']))
    return derived,{'selected':True,'derived':True,'source_sha256':sha(data),'derived_sha256':sha(derived),
                    'algorithm':'local deterministic missing-graphic layout/1','authoritative_source_unchanged':True,
                    'preserved_geometry':preserved,'added_graphics':added,
                    'limits':['Existing invalid coordinates, partial participant stacks, ambiguous roots/endpoints and automatic lane partitioning are refused.',
                              'New geometry is derived, not native-authoritative or professionally accepted.']}
