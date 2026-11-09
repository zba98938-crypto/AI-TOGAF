"""Bounded source-bound data roles and SequenceFlow visual shortcuts.

PDF physical253/398/405/442: a shorthand has no bpmnElement, its target is a
SequenceFlow DI edge, and it normalizes exactly two retained DataAssociations.
No semantic model object or automatic coordinates are written into native XML.
"""
from bpmn_references import local_reference
from standards import BPMN, Invalid, Incomplete, local

DI='http://www.omg.org/spec/BPMN/20100524/DI'
DATA_SHAPES={'dataInput','dataOutput','dataObjectReference','dataStoreReference'}
DATA_EDGES={'dataInputAssociation','dataOutputAssociation'}


def graphic_types():
    from bpmn_data_compensation import _metamodel,_exchange_types
    subtype,graph=_metamodel();model_class,_=_exchange_types(subtype,graph)
    aliases={'DataInput':'dataInput','DataOutput':'dataOutput'}
    def kind(element):
        return aliases.get(model_class(element),local(element.tag))
    return kind


def selected_data(owner,kind):
    """Direct, IO and MI data roles belong to the visible native owner."""
    selected=list(owner)
    for child in owner:
        if isinstance(child.tag,str) and child.tag in {'{'+BPMN+'}ioSpecification','{'+BPMN+'}multiInstanceLoopCharacteristics'}:
            selected.extend(child)
    return [e for e in selected if isinstance(e.tag,str) and e.tag.startswith('{'+BPMN+'}') and kind(e) in DATA_SHAPES|DATA_EDGES]


def shortcut(root,edge):
    """Resolve the official no-bpmnElement exception without guessing a pair."""
    q=lambda name:'{'+BPMN+'}'+name
    d=lambda name:'{'+DI+'}'+name
    nodes={e.get('id'):e for e in root.iter() if isinstance(e.tag,str) and e.get('id')}
    def resolve(owner,value):
        identity,problem=local_reference(owner,value,root.get('targetNamespace'))
        if problem:raise Invalid(problem)
        return nodes.get(identity)
    if edge.get('bpmnElement') is not None:
        raise Invalid('SequenceFlow data shortcut must omit bpmnElement')
    source=resolve(edge,edge.get('sourceElement'));target=resolve(edge,edge.get('targetElement'))
    if source is None or source.tag!=d('BPMNShape') or source.get('participantBandKind') or target is None or target.tag!=d('BPMNEdge'):
        raise Invalid('Data shortcut requires sourceElement data shape and targetElement SequenceFlow edge')
    if source.getparent() is not edge.getparent() or target.getparent() is not edge.getparent():
        raise Invalid('Data shortcut endpoints must belong to the same source BPMNPlane')
    data=resolve(source,source.get('bpmnElement'));flow=resolve(target,target.get('bpmnElement'))
    if data is None or data.tag!=q('dataObjectReference') or flow is None or flow.tag!=q('sequenceFlow'):
        raise Invalid('Data shortcut source must depict DataObjectReference and target must depict SequenceFlow')
    data_object=resolve(data,data.get('dataObjectRef'))
    if data_object is None:raise Invalid('Data shortcut DataObjectReference requires its retained DataObject')
    start=resolve(flow,flow.get('sourceRef'));end=resolve(flow,flow.get('targetRef'))
    def is_data(element):return element is data or element is data_object
    output=[];input=[]
    for owner,name,rows in [(start,'dataOutputAssociation',output),(end,'dataInputAssociation',input)]:
        if owner is None:continue
        for assoc in owner.findall(q(name)):
            sources=[resolve(e,e.text) for e in assoc.findall(q('sourceRef'))]
            child=assoc.find(q('targetRef'));dest=resolve(child,child.text) if child is not None else None
            if name=='dataOutputAssociation' and len(sources)==1 and is_data(dest) or name=='dataInputAssociation' and len(sources)==1 and is_data(sources[0]):
                rows.append(assoc)
    if not output or not input:
        raise Invalid('Data shortcut requires both retained source-output and target-input DataAssociations')
    if len(output)!=1 or len(input)!=1:
        raise Incomplete('Data shortcut association pair is ambiguous; no native pair is guessed')
    if not all(e.get('id') for e in output+input):raise Incomplete('Data shortcut normalized associations require stable native IDs')
    return {'data_semantic_id':data.get('id'),'sequence_flow_id':flow.get('id'),
            'normalized_semantic_ids':[output[0].get('id'),input[0].get('id')],
            'source_graphic_id':source.get('id'),'target_graphic_id':target.get('id'),
            'resolution_origin':'source BPMNDI exception and two retained native DataAssociations',
            'normative_physical_pages':[253,254,398,405,442]}


def validate_data_endpoints(root,graphics):
    """Native item/owner context, plane-local DI and the shorthand exception."""
    nodes={e.get('id'):e for e in root.iter() if isinstance(e.tag,str) and e.get('id')}
    by_graphic={g['graphic_id']:g for g in graphics}
    def resolve(owner,value):return nodes.get(local_reference(owner,value,root.get('targetNamespace'))[0])
    def depicts(item,g):
        depicted=nodes.get(g['semantic_id'])
        if depicted is None or g.get('band_kind'):return False
        if depicted is item:return True
        if local(item.tag) in {'dataInput','dataOutput','inputDataItem','outputDataItem','property'} and any(depicted is p for p in item.iterancestors()):return True
        if local(item.tag)=='dataObject' and local(depicted.tag)=='dataObjectReference' and resolve(depicted,depicted.get('dataObjectRef')) is item:return True
        if local(depicted.tag)=='participant':
            process=resolve(depicted,depicted.get('processRef'))
            return process is not None and any(process is p for p in item.iterancestors())
        return False
    for g in graphics:
        if g['kind']!='edge' or g['type'] not in DATA_EDGES:continue
        for side in ['source','target']:
            explicit=g[side+'_graphic_id']
            if not explicit:continue
            target=by_graphic.get(explicit)
            if target is None:raise Incomplete('Explicit DI endpoint lies outside selected view: '+explicit)
            if target['kind']=='edge':raise Incomplete('Directed Data Association endpoint-to-edge requires the separate no-bpmnElement shortcut, not a single association override')
            identities=g['source_semantic_ids'] if side=='source' else [g['target_semantic_id']]
            candidates=[nodes[sid] for sid in identities if sid in nodes]
            if not candidates:raise Incomplete('Data DI '+side+' has no retained ItemAwareElement context; an arbitrary graphical endpoint is not inferred')
            if target.get('band_kind') or candidates and not any(depicts(e,target) for e in candidates):
                raise Invalid('Data DI '+side+' override conflicts with its ItemAwareElement/owner context: '+g['graphic_id'])
