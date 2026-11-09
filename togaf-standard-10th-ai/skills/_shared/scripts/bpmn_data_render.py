"""Source-DI partial process/collaboration views with nested data graphics.

BPMN 2.0.2 physical398/251 permit incomplete diagrams and optional data
associations. physical405/441 require explicit DI endpoints when depictions
differ from the underlying model. No Activity-border endpoints are invented.
"""
import math
from bpmn_references import local_reference
from standards import BPMN, Invalid, Incomplete, local, sha

DI='http://www.omg.org/spec/BPMN/20100524/DI'
DC='http://www.omg.org/spec/DD/20100524/DC'
DATA={'dataInput','dataOutput','dataObjectReference','dataStoreReference','dataInputAssociation','dataOutputAssociation'}


def plan(data,root,report):
    from bpmn_render import SHAPES,EDGES,CONTAINERS
    from bpmn_design_render import notation_projection
    from bpmn_data_notation import graphic_types,selected_data,shortcut,validate_data_endpoints
    graphic_type=graphic_types()
    q=lambda name:'{'+BPMN+'}'+name
    d=lambda name:'{'+DI+'}'+name
    nodes={e.get('id'):e for e in root.iter() if isinstance(e.tag,str) and e.get('id')}
    def identity(e,v):return local_reference(e,v,root.get('targetNamespace'))[0]
    def resolve(e,v):return nodes.get(identity(e,v))
    diagrams=list(root.iter(d('BPMNDiagram')))
    if len(diagrams)!=1:raise Incomplete('Data DI rendering requires exactly one explicit BPMNDiagram')
    planes=diagrams[0].findall(d('BPMNPlane'))
    if len(planes)!=1:raise Invalid('BPMNDiagram requires one BPMNPlane')
    plane=planes[0];target=resolve(plane,plane.get('bpmnElement'))
    if target is None or local(target.tag) not in {'process','collaboration'}:
        raise Incomplete('Data DI renderer covers an explicit process/collaboration view')
    graphics=[];shapes={};edges={}
    def box(e):
        b=e.find('{'+DC+'}Bounds')
        if b is None:return None
        raw={k:b.get(k) for k in ['x','y','width','height']}
        try:
            values={k:float(v) for k,v in raw.items()}
            if not all(math.isfinite(v) for v in values.values()) or values['width']<=0 or values['height']<=0:raise ValueError()
        except (TypeError,ValueError):raise Invalid('Data DI bounds require finite coordinates and positive dimensions')
        return raw
    for index,e in enumerate(plane):
        if local(e.tag) not in {'BPMNShape','BPMNEdge'}:continue
        semantic=resolve(e,e.get('bpmnElement'));is_shape=local(e.tag)=='BPMNShape'
        special=shortcut(root,e) if not is_shape and e.get('bpmnElement') is None else None
        if not special and (semantic is None or graphic_type(semantic) not in (SHAPES if is_shape else EDGES)):
            raise Incomplete('Unsupported Data DI depiction: '+str(e.get('bpmnElement')))
        if e.get('participantBandKind'):
            raise Incomplete('Participant bands need the choreography DI renderer')
        gid=e.get('id') or '__source_di_'+str(index);sid=semantic.get('id') if semantic is not None else '__shortcut_'+gid
        if any(g['graphic_id']==gid for g in graphics):raise Invalid('Duplicate DI graphic identity: '+gid)
        g={'graphic_id':gid,'semantic_id':sid if semantic is not None else None,'type':graphic_type(semantic) if semantic is not None else 'dataAssociationShortcut','kind':'shape' if is_shape else 'edge',
           'identity_origin':'native-id' if e.get('id') else 'source-plane-position',
           'source_locator':root.getroottree().getpath(e),'name':semantic.get('name') or '' if semantic is not None else '',
           'attributes':{k:v for k,v in e.attrib.items() if k not in {'id','bpmnElement'}},'source_plane_index':index}
        if special:g['view_identity']=sid
        label=e.find(d('BPMNLabel'));g['label_bounds']=box(label) if label is not None else None
        collection=shapes if is_shape else edges
        if sid in collection:raise Invalid('Repeated ordinary BPMN element depiction is not allowed: '+sid)
        collection[sid]=g
        if is_shape:
            g['bounds']=box(e)
            if g['bounds'] is None:raise Invalid('BPMNShape requires source Bounds: '+gid)
        else:
            g['waypoints']=[{k:c.get(k) for k in ['x','y']} for c in e if local(c.tag)=='waypoint']
            try:
                if len(g['waypoints'])<2 or not all(math.isfinite(float(v)) for p in g['waypoints'] for v in p.values()):raise ValueError()
            except (ValueError,TypeError):raise Invalid('BPMNEdge requires at least two finite source waypoints: '+gid)
            g['source_graphic_id']=identity(e,e.get('sourceElement'));g['target_graphic_id']=identity(e,e.get('targetElement'))
            g['source_semantic_ids']=[identity(semantic,semantic.get('sourceRef'))] if semantic is not None and semantic.get('sourceRef') else []
            g['target_semantic_id']=identity(semantic,semantic.get('targetRef')) if semantic is not None else None
            if special:g.update(special)
            if g['type'] in {'dataInputAssociation','dataOutputAssociation'}:
                g['source_semantic_ids']=[identity(c,c.text) for c in semantic.findall(q('sourceRef'))]
                child=semantic.find(q('targetRef'));g['target_semantic_id']=identity(child,child.text) if child is not None else None
        graphics.append(g)
    expected_shapes=set();expected_edges={g['view_identity'] for g in graphics if g['type']=='dataAssociationShortcut'};hidden=[];inventory=[]
    visited_data=set()
    def data_details(owner):
        if owner in visited_data:return
        visited_data.add(owner)
        for item in selected_data(owner,graphic_type):
            sid=item.get('id');shape=graphic_type(item) in {'dataInput','dataOutput','dataObjectReference','dataStoreReference'}
            depicted=sid in (shapes if shape else edges)
            inventory.append({'id':sid,'type':graphic_type(item),'native_role':local(item.tag),'owner_id':owner.get('id'),'depicted':depicted,
                              'source_locator':root.getroottree().getpath(item),'scope':'visible owner; optional data depiction'})
            if depicted:(expected_shapes if shape else expected_edges).add(sid)
    def container(owner):
        data_details(owner)
        for item in owner:
            if not isinstance(item.tag,str) or not item.tag.startswith('{'+BPMN+'}'):continue
            kind=local(item.tag);sid=item.get('id')
            if kind=='laneSet':expected_shapes.update(e.get('id') for e in item.iter(q('lane')))
            elif kind in DATA:continue
            elif kind in SHAPES:
                expected_shapes.add(sid)
                if kind in CONTAINERS:
                    data_details(item)
                    graphic=shapes.get(sid)
                    if graphic and graphic['attributes'].get('isExpanded') in {'true','1'}:container(item)
                    else:hidden.extend({'id':c.get('id'),'type':local(c.tag),'collapsed_parent_id':sid} for c in item.iterdescendants() if isinstance(c.tag,str) and c.get('id') and c.get('id') not in shapes and c.get('id') not in edges)
                else:data_details(item)
            elif kind in EDGES:expected_edges.add(sid)
            elif kind in {'choreographyTask','subChoreography','callChoreography'}:
                raise Incomplete('Mixed choreography data views require a separately verified backend')
    if local(target.tag)=='process':container(target)
    else:
        for participant in target.findall(q('participant')):
            expected_shapes.add(participant.get('id'));process=resolve(participant,participant.get('processRef'))
            if process is not None:container(process)
        expected_edges.update(e.get('id') for e in target.findall(q('messageFlow')))
        for item in target:
            if local(item.tag) in {'textAnnotation','group'}:expected_shapes.add(item.get('id'))
            elif local(item.tag)=='association':expected_edges.add(item.get('id'))
    if None in expected_shapes or None in expected_edges:raise Invalid('Depicted BPMN elements require stable semantic IDs')
    missing=sorted((expected_shapes-shapes.keys())|(expected_edges-edges.keys()))
    if missing:raise Incomplete('Missing BPMNDI for required visible process elements: '+', '.join(missing))
    extras=sorted((shapes.keys()-expected_shapes)|(edges.keys()-expected_edges))
    if extras:raise Incomplete('Data DI graphics lie outside the visible native scope: '+', '.join(extras))
    if not shapes:raise Incomplete('BPMNDI contains no visible shapes')
    by_graphic={g['graphic_id']:g for g in graphics}
    validate_data_endpoints(root,graphics)
    for g in edges.values():
        for side in ['source','target']:
            explicit=g[side+'_graphic_id']
            if explicit:
                if explicit not in by_graphic:raise Incomplete('Explicit DI endpoint lies outside selected view: '+explicit)
                continue
            candidates=g['source_semantic_ids'] if side=='source' else [g['target_semantic_id']]
            if len(candidates)!=1 or candidates[0] not in shapes and candidates[0] not in edges:
                raise Incomplete('Data DI edge needs an explicit '+side+'Element for an undepicted or ambiguous model endpoint: '+g['graphic_id'])
            selected=shapes.get(candidates[0]) or edges[candidates[0]]
            g[side+'_graphic_id']=selected['graphic_id']
    projected,adaptations=notation_projection(root)
    return {'backend':'native-data-di','diagram_id':diagrams[0].get('id'),'plane_id':plane.get('id'),
            'root_id':target.get('id'),'root_type':local(target.tag),'shape_ids':sorted(shapes),'edge_ids':sorted({sid for sid in edges if sid in nodes}|{sid for g in graphics for sid in g.get('normalized_semantic_ids',[])}),
            'shape_graphic_ids':[g['graphic_id'] for g in graphics if g['kind']=='shape'],
            'edge_graphic_ids':[g['graphic_id'] for g in graphics if g['kind']=='edge'],'graphics':graphics,
            'source_sha256':sha(data),'notation_xml':projected,'notation_adaptations':adaptations,
            'visible_names':{sid:nodes[sid].get('name') for sid in shapes.keys()|edges.keys() if sid in nodes and nodes[sid].get('name')},
            'hidden_native_elements':hidden,'shortcut_graphic_ids':[g['graphic_id'] for g in graphics if g['type']=='dataAssociationShortcut'],'data_depiction_inventory':inventory,
            'diagram_scope':'explicit process/collaboration view; optional nested data depictions selected by source DI',
            'native_validation':report,'geometry_origin':'source BPMNDI coordinate strings and plane order; no automatic layout',
            'normative_physical_pages':[221,242,244,251,253,254,398,405,423,441,442],'auto_layout':False}
