"""Explicit BPMNDI scene planning for Conversation and Choreography views.

All shape bounds and connector waypoints come from the source. Graphic identity
is separate from semantic identity: a Participant can own bands in many tasks.
"""
from bpmn_references import local_reference
from bpmn_design_semantics import CONVERSATIONS, CHOREOGRAPHY_ACTIVITIES
from standards import BPMN, Invalid, Incomplete, local, sha

DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
DC = 'http://www.omg.org/spec/DD/20100524/DC'


def notation_projection(root):
    """Adapt known installed-moddle XML differences for display, never export.

Official XSD uses QName references and reference children for participant
associations. The installed descriptor expects local IDs and association attrs,
and spells ConversationNode.messageFlowRef as messageFlowRefs.
"""
    from copy import deepcopy
    from lxml import etree
    from standards import bpmn_reference_fields
    fields = bpmn_reference_fields()
    projected = deepcopy(root)
    adjustments = []
    for original, e in zip(root.iter(), projected.iter()):
        if not isinstance(e.tag, str):
            continue
        for key, value in list(e.attrib.items()):
            if key not in fields['attribute']:
                continue
            resolved, problem = local_reference(original, value, root.get('targetNamespace'))
            if problem:
                raise Incomplete(problem)
            if resolved != value:
                e.set(key, resolved)
                adjustments.append({'locator': root.getroottree().getpath(original), 'field': key,
                                    'adaptation': 'QName/IDREF normalized to same-source native ID for installed renderer'})
        if local(e.tag) in fields['element'] and e.text:
            value, problem = local_reference(original, e.text, root.get('targetNamespace'))
            if problem:
                raise Incomplete(problem)
            e.text = value
    # Iterate after all reference values are independently resolved using their
    # original namespace environments; removing children cannot shift that pass.
    for e in list(projected.iter()):
        if not isinstance(e.tag, str):
            continue
        parent = e.getparent()
        if local(e.tag) in {'innerParticipantRef', 'outerParticipantRef', 'innerConversationNodeRef', 'outerConversationNodeRef', 'innerMessageFlowRef', 'outerMessageFlowRef'} and parent is not None:
            parent.set(local(e.tag), e.text)
            adjustments.append({'field': local(e.tag), 'adaptation': 'official reference child represented as installed-moddle reference attribute in display-only projection'})
            parent.remove(e)
        elif local(e.tag) == 'messageFlowRef' and parent is not None and local(parent.tag) in CONVERSATIONS:
            e.tag = '{' + BPMN + '}messageFlowRefs'
            adjustments.append({'field': 'ConversationNode.messageFlowRef', 'adaptation': 'installed-moddle descriptor spelling messageFlowRefs in display-only projection'})
    return etree.tostring(projected, encoding='unicode'), adjustments


def design_plan(data, root, report):
    from bpmn_render import SHAPES, EDGES, CONTAINERS
    shapes_supported = SHAPES | CONVERSATIONS | CHOREOGRAPHY_ACTIVITIES
    edges_supported = EDGES | {'conversationLink'}
    nodes = {e.get('id'): e for e in root.iter() if isinstance(e.tag, str) and e.get('id')}
    q = lambda name: '{' + BPMN + '}' + name
    d = lambda name: '{' + DI + '}' + name

    def ref(e, v):
        return local_reference(e, v, root.get('targetNamespace'))[0]

    def resolve(e, v):
        return nodes.get(ref(e, v))

    diagrams = list(root.iter(d('BPMNDiagram')))
    if len(diagrams) != 1:
        raise Incomplete('BPMNDI rendering requires exactly one explicit BPMNDiagram')
    planes = diagrams[0].findall(d('BPMNPlane'))
    if len(planes) != 1:
        raise Invalid('BPMNDiagram requires one BPMNPlane')
    plane = planes[0]
    target = resolve(plane, plane.get('bpmnElement'))
    if target is None or local(target.tag) not in {'process', 'collaboration', 'choreography'}:
        raise Incomplete('This BPMNDI view requires a Process, Collaboration or Choreography plane')
    graphics, shapes, edges = [], {}, {}

    def bounds(e):
        b = e.find('{' + DC + '}Bounds')
        return {k: float(b.get(k)) for k in ('x', 'y', 'width', 'height')} if b is not None else None

    for index, e in enumerate(plane):
        if local(e.tag) not in {'BPMNShape', 'BPMNEdge'}:
            continue
        semantic = resolve(e, e.get('bpmnElement'))
        is_shape = local(e.tag) == 'BPMNShape'
        if semantic is None or local(semantic.tag) not in (shapes_supported if is_shape else edges_supported):
            raise Incomplete('Unsupported native notation element: ' + str(e.get('bpmnElement')))
        sid = semantic.get('id')
        # DI IDs are optional in the official XSD; a source-position identifier is
        # an output identity only, never written back into authoritative XML.
        gid = e.get('id') or '__source_di_' + str(index)
        if any(g['graphic_id'] == gid for g in graphics):
            raise Invalid('Duplicate DI graphic identity: ' + gid)
        g = {'graphic_id': gid, 'semantic_id': sid, 'type': local(semantic.tag),
             'kind': 'shape' if is_shape else 'edge',
             'identity_origin': 'native-id' if e.get('id') else 'source-plane-position',
             'source_locator': root.getroottree().getpath(e),
             'name': semantic.get('name') or '',
             'attributes': {k: v for k, v in e.attrib.items() if k not in {'id', 'bpmnElement'}}}
        label = e.find(d('BPMNLabel'))
        g['label_bounds'] = bounds(label) if label is not None else None
        if is_shape:
            g['bounds'] = bounds(e)
            g['band_kind'] = e.get('participantBandKind')
            g['activity_graphic_id'] = ref(e, e.get('choreographyActivityShape'))
            g['loop_type'] = semantic.get('loopType', 'None')
            g['participants'] = [ref(c, c.text) for c in semantic.findall(q('participantRef'))]
            g['initiator'] = ref(semantic, semantic.get('initiatingParticipantRef'))
            call_attr = 'calledChoreographyRef' if g['type'] == 'callChoreography' else 'calledCollaborationRef' if g['type'] == 'callConversation' else None
            called = resolve(semantic, semantic.get(call_attr)) if call_attr else None
            g['called_type'] = local(called.tag) if called is not None else None
            if call_attr and called is None:
                raise Incomplete(g['type'] + ' notation needs a resolved ' + call_attr + ' to select its standard symbol')
            multiplicity = semantic.find(q('participantMultiplicity'))
            g['participant_multiplicity'] = multiplicity is not None and (multiplicity.get('maximum') is None or int(multiplicity.get('maximum')) > 1)
            shapes.setdefault(sid, []).append(g)
        else:
            g['waypoints'] = [{k: float(c.get(k)) for k in ('x', 'y')} for c in e if local(c.tag) == 'waypoint']
            g['source_graphic_id'] = ref(e, e.get('sourceElement'))
            g['target_graphic_id'] = ref(e, e.get('targetElement'))
            g['source_semantic_id'] = ref(semantic, semantic.get('sourceRef'))
            g['target_semantic_id'] = ref(semantic, semantic.get('targetRef'))
            # DataAssociation uses reference children rather than attributes.
            for direction in ('source', 'target'):
                c = semantic.find(q(direction + 'Ref'))
                if c is not None:
                    g[direction + '_semantic_id'] = ref(c, c.text)
            edges.setdefault(sid, []).append(g)
        graphics.append(g)

    expected_shapes, expected_edges, hidden = set(), set(), []
    visible_wrappers = CONTAINERS | {'subChoreography'}
    visiting = set()

    def hide(owner, parent_id):
        hidden.extend({'id': c.get('id'), 'type': local(c.tag), 'collapsed_parent_id': parent_id}
                      for c in owner.iterdescendants() if isinstance(c.tag, str) and c.get('id'))

    def conversation_details(owner):
        for child in owner:
            if not isinstance(child.tag, str) or local(child.tag) not in CONVERSATIONS:
                continue
            if child.get('id') in shapes:
                expected_shapes.add(child.get('id'))
                conversation_details(child)
            else:
                hidden.append({'id': child.get('id'), 'type': local(child.tag), 'collapsed_parent_id': owner.get('id')})
                hide(child, owner.get('id'))

    def container(owner):
        if owner in visiting:
            raise Incomplete('Recursive expanded called choreography cannot be unfolded in one finite DI view')
        visiting.add(owner)
        for e in owner:
            if not isinstance(e.tag, str) or not e.tag.startswith('{' + BPMN + '}'):
                continue
            k, sid = local(e.tag), e.get('id')
            if k == 'laneSet':
                for lane in e.iter(q('lane')):
                    expected_shapes.add(lane.get('id'))
            elif k in shapes_supported and k != 'participant':
                expected_shapes.add(sid)
                declared = shapes.get(sid, [])
                expanded = any(g['attributes'].get('isExpanded') in {'true', '1'} for g in declared)
                if k in visible_wrappers:
                    container(e) if expanded else hide(e, sid)
                elif k == 'subConversation':
                    # No isExpanded attribute applies to SubConversation. Child
                    # nodes are separate explicitly depicted detail when present.
                    conversation_details(e)
                elif k == 'callChoreography' and expanded:
                    called = resolve(e, e.get('calledChoreographyRef'))
                    if called is None or local(called.tag) != 'choreography':
                        raise Invalid('Only a call of Choreography can have an expanded choreography view')
                    container(called)
            elif k in edges_supported and not (k == 'messageFlow' and local(owner.tag) == 'choreography'):
                expected_edges.add(sid)
        visiting.remove(owner)

    target_type = local(target.tag)
    if target_type in {'process', 'choreography'}:
        container(target)
        # Choreography message flows are represented by the activity interaction
        # and optional band envelope decorators, not obligatory visible edges.
        if target_type == 'choreography':
            expected_edges -= {e.get('id') for e in target.findall(q('messageFlow'))}
    else:
        for p in target.findall(q('participant')):
            expected_shapes.add(p.get('id'))
            process = resolve(p, p.get('processRef'))
            if process is not None:
                container(process)
        container(target)
        grouped = {ref(c, c.text) for e in target.iter() if local(e.tag) in CONVERSATIONS for c in e.findall(q('messageFlowRef'))}
        expected_edges -= grouped
    if None in expected_shapes or None in expected_edges:
        raise Invalid('Visible semantic elements require explicit stable IDs')
    ordinary_ids = {sid for sid, group in shapes.items() if any(not g['band_kind'] for g in group)}
    missing = sorted((expected_shapes - ordinary_ids) | (expected_edges - set(edges)))
    if missing:
        raise Incomplete('Missing BPMNDI shapes or edges for visible semantic elements: ' + ', '.join(missing))
    extra_shapes = ordinary_ids - expected_shapes
    extra_edges = set(edges) - expected_edges
    # Explicit choreography message connectors and grouped messages remain legal
    # optional depictions when their native scope is in the selected view.
    optional_messages = {e.get('id') for e in target.findall(q('messageFlow'))}
    extra_edges -= optional_messages
    if extra_shapes or extra_edges:
        raise Incomplete('DI graphics outside the visible native scope: ' + ', '.join(sorted(extra_shapes | extra_edges)))
    if not shapes:
        raise Incomplete('BPMNDI contains no visible shapes')

    by_graphic = {g['graphic_id']: g for g in graphics}
    for band in [g for g in graphics if g.get('band_kind')]:
        activity = by_graphic.get(band['activity_graphic_id'])
        if activity is None or activity['semantic_id'] not in expected_shapes:
            raise Incomplete('Participant Band owner is outside the selected view: ' + band['graphic_id'])
    for sid in expected_shapes:
        semantic = nodes[sid]
        if local(semantic.tag) not in CHOREOGRAPHY_ACTIVITIES:
            continue
        for activity in shapes[sid]:
            group = [g for g in graphics if g.get('activity_graphic_id') == activity['graphic_id']]
            if len(group) < 2:
                raise Incomplete('Missing required Participant Bands for ' + sid)
            b = activity['bounds']
            intervals = []
            for band in group:
                r = band['bounds']
                if not (abs(r['x'] - b['x']) < 1e-7 and abs(r['width'] - b['width']) < 1e-7 and
                        r['y'] >= b['y'] and r['y'] + r['height'] <= b['y'] + b['height']):
                    raise Invalid('Participant Band bounds must align with and lie within activity: ' + band['graphic_id'])
                position = band['band_kind'].split('_')[0]
                if position == 'top' and abs(r['y'] - b['y']) > 1e-7:
                    raise Invalid('Top Participant Band must meet activity top boundary')
                if position == 'bottom' and abs(r['y'] + r['height'] - b['y'] - b['height']) > 1e-7:
                    raise Invalid('Bottom Participant Band must meet activity bottom boundary')
                intervals.append((r['y'], r['y'] + r['height']))
            intervals.sort()
            if any(a[1] > b2[0] + 1e-7 for a, b2 in zip(intervals, intervals[1:])):
                raise Invalid('Participant Bands overlap: ' + sid)
            if not any(g['band_kind'].startswith('top_') for g in group) or not any(g['band_kind'].startswith('bottom_') for g in group):
                raise Invalid('Activity requires top and bottom Participant Bands: ' + sid)
            gaps = [(a[1], z[0]) for a, z in zip(intervals, intervals[1:]) if z[0] > a[1]]
            if len(gaps) != 1:
                raise Invalid('Participant Bands must leave exactly one Activity Name Band: ' + sid)
            activity['name_band'] = {'x': b['x'], 'y': gaps[0][0], 'width': b['width'], 'height': gaps[0][1] - gaps[0][0]}
    for g in graphics:
        if g['kind'] != 'edge':
            continue
        for direction in ('source', 'target'):
            explicit = g[direction + '_graphic_id']
            if explicit:
                if explicit not in by_graphic:
                    raise Incomplete('Edge endpoint DI graphic lies outside selected view: ' + explicit)
            else:
                candidates = [s for s in shapes.get(g[direction + '_semantic_id'], []) if not s['band_kind']]
                if len(candidates) != 1:
                    # An association to an edge is legal and can be selected by ID.
                    candidates += edges.get(g[direction + '_semantic_id'], [])
                if len(candidates) != 1:
                    raise Incomplete('Edge endpoint needs an explicit DI override for hidden or repeated depiction: ' + g['graphic_id'])
                g[direction + '_graphic_id'] = candidates[0]['graphic_id']
    projected, adjustments = notation_projection(root)
    return {'backend': 'native-design-di', 'diagram_id': diagrams[0].get('id'), 'plane_id': plane.get('id'),
            'root_id': target.get('id'), 'root_type': target_type,
            'shape_ids': sorted(shapes), 'edge_ids': sorted(edges),
            'shape_graphic_ids': [g['graphic_id'] for g in graphics if g['kind'] == 'shape'],
            'edge_graphic_ids': [g['graphic_id'] for g in graphics if g['kind'] == 'edge'],
            'graphics': graphics, 'source_sha256': sha(data),
            'notation_xml': projected, 'notation_adaptations': adjustments,
            'visible_names': {i: nodes[i].get('name') for i in set(shapes) | set(edges) if nodes[i].get('name')},
            'hidden_native_elements': hidden, 'native_validation': report,
            'geometry_origin': 'source BPMNDI; no automatic node or edge layout',
            'auto_layout': False}
