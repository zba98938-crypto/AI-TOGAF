"""Source-bound Conversation, Choreography and DI design-time constraints.

The authoritative clauses are in the local OMG PDF; this module does not infer
full conformance from this implemented subset. QName failures are left to the
shared reference resolver, which distinguishes missing material from invalidity.
"""
from bpmn_references import local_id, local_reference

BPMN = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
PDF_SHA256 = 'd3d9258a70bf808c11ac52becea4ce645540a8b881117535f60a56fbf13e22f2'
RULES = {
    'conversation-participants': ('9.5.1, Table 9.10', [159]),
    'conversation-message-flow': ('9.5.1 and 9.5.4, Tables 9.10/9.12', [159, 161]),
    'conversation-link': ('9.5.6, Table 9.13', [162, 163]),
    'call-conversation-target': ('9.5.4, Table 9.12', [160, 161]),
    'global-conversation-content': ('9.5.5', [161]),
    'choreography-activity-scope': ('11.5 and Table 11.1', [351, 352]),
    'choreography-task-message': ('11.5.1 and Table 11.2; tChoreographyTask XSD', [353, 358]),
    'call-choreography-target': ('11.5.3, Table 11.4', [363, 365]),
    'participant-association': ('9.3.1 ParticipantAssociation, Tables 9.7/9.12/11.4', [147, 149, 161, 365]),
    'participant-multiplicity': ('9.3.1, Table 9.5', [147]),
    'global-choreography-content': ('11.5.4, Table 11.5', [365]),
    'di-attribute-applicability': ('12.2.3.3 BPMNShape attributes', [403]),
    'di-participant-band': ('12.2.3.3/4 and 11.5.1/2', [354, 358, 361, 403, 404]),
    'di-band-message': ('11.5.1, 11.5.3 and Table 12.33', [355, 363, 438, 439, 440]),
    'di-edge-endpoint': ('12.2.3.5 and 12.3.3 BPMNEdge', [405, 440, 441]),
}
CONVERSATIONS = {'conversation', 'subConversation', 'callConversation'}
CHOREOGRAPHY_ACTIVITIES = {'choreographyTask', 'subChoreography', 'callChoreography'}
ACTIVITIES = {'task', 'userTask', 'serviceTask', 'manualTask', 'sendTask',
              'receiveTask', 'scriptTask', 'businessRuleTask', 'subProcess',
              'transaction', 'adHocSubProcess', 'callActivity'}
EVENTS = {'startEvent', 'endEvent', 'boundaryEvent', 'intermediateCatchEvent',
          'intermediateThrowEvent', 'implicitThrowEvent'}
FLOW_ELEMENTS = ACTIVITIES | EVENTS | CHOREOGRAPHY_ACTIVITIES | {
    'sequenceFlow', 'exclusiveGateway', 'inclusiveGateway', 'parallelGateway',
    'complexGateway', 'eventBasedGateway', 'dataObject', 'dataObjectReference',
    'dataStoreReference'}


def check(root):
    q = lambda name: '{' + BPMN + '}' + name
    d = lambda name: '{' + DI + '}' + name
    kind = lambda e: e.tag.split('}')[-1] if e is not None and isinstance(e.tag, str) else ''
    nodes = {local_id(e.get('id')): e for e in root.iter() if isinstance(e.tag, str) and e.get('id')}
    findings = []

    def ref(owner, value):
        return local_reference(owner, value, root.get('targetNamespace'))[0]

    def resolve(owner, value):
        return nodes.get(ref(owner, value))

    def issue(rule, e, text):
        section, pages = RULES[rule]
        findings.append({'rule_id': rule, 'id': e.get('id'), 'message': text,
                         'source_locator': root.getroottree().getpath(e),
                         'normative_source': {'pdf_sha256': PDF_SHA256,
                                              'section': section, 'physical_pages': pages}})

    def refs(e, name):
        return [ref(c, c.text) for c in e.findall(q(name))]

    def scope(e, names):
        return next((p for p in e.iterancestors() if kind(p) in names), None)

    def collaboration(e):
        return scope(e, {'collaboration', 'choreography', 'globalConversation', 'globalChoreographyTask'})

    def declared_parties(owner):
        return {local_id(p.get('id')) for p in owner.findall(q('participant'))} if owner is not None else set()

    def party(endpoint, owner):
        if endpoint is None:
            return None
        if kind(endpoint) == 'participant':
            return local_id(endpoint.get('id'))
        process = scope(endpoint, {'process'})
        if process is None:
            return None
        for p in owner.findall(q('participant')) if owner is not None else []:
            if resolve(p, p.get('processRef')) is process:
                return local_id(p.get('id'))
        return None

    for e in root.iter():
        if not isinstance(e.tag, str) or not e.tag.startswith('{' + BPMN + '}'):
            continue
        k = kind(e)
        if k == 'participantMultiplicity':
            try:
                minimum = int(e.get('minimum', '0'))
                maximum = int(e.get('maximum')) if e.get('maximum') is not None else None
                if minimum < 0 or (maximum is not None and (maximum < 1 or maximum < minimum)):
                    issue('participant-multiplicity', e, 'participant minimum is nonnegative; explicit maximum is at least one and at least minimum')
            except ValueError:
                issue('participant-multiplicity', e, 'participant multiplicity bounds must be integers')
        if k in CONVERSATIONS:
            values = refs(e, 'participantRef')
            owner = collaboration(e)
            parent = e.getparent()
            available = set(refs(parent, 'participantRef')) if kind(parent) == 'subConversation' else declared_parties(owner)
            if len(values) < 2 or len({v for v in values if v}) != len([v for v in values if v]):
                issue('conversation-participants', e, 'ConversationNode requires at least two distinct participant references')
            for v in values:
                if v and v in nodes and (kind(nodes[v]) != 'participant' or v not in available):
                    issue('conversation-participants', e, 'participant must be declared by the parent conversation/collaboration')
            messages = e.findall(q('messageFlowRef'))
            if k == 'callConversation' and messages:
                issue('conversation-message-flow', e, 'messageFlowRef does not apply to CallConversation')
            for c in messages:
                flow = resolve(c, c.text)
                if flow is not None and (kind(flow) != 'messageFlow' or flow.getparent() is not owner):
                    issue('conversation-message-flow', e, 'messageFlowRef must name a message flow in the owning collaboration')
                elif flow is not None:
                    endpoints = [party(resolve(flow, flow.get(a)), owner) for a in ('sourceRef', 'targetRef')]
                    if any(p is not None and p not in values for p in endpoints):
                        issue('conversation-message-flow', e, 'grouped message flow uses a participant outside the conversation')
            if k == 'callConversation' and e.get('calledCollaborationRef'):
                target = resolve(e, e.get('calledCollaborationRef'))
                if target is not None and kind(target) not in {'collaboration', 'globalConversation'}:
                    issue('call-conversation-target', e, 'CallConversation may call Collaboration or GlobalConversation only')
        if k == 'conversationLink':
            endpoints = [resolve(e, e.get(a)) for a in ('sourceRef', 'targetRef')]
            if all(p is not None for p in endpoints):
                if sum(kind(p) in CONVERSATIONS for p in endpoints) != 1:
                    issue('conversation-link', e, 'exactly one ConversationLink endpoint must be a ConversationNode')
                if any(kind(p) not in CONVERSATIONS | ACTIVITIES | EVENTS | {'participant'} for p in endpoints):
                    issue('conversation-link', e, 'ConversationLink endpoint must be an InteractionNode')
                conversations = [p for p in endpoints if kind(p) in CONVERSATIONS]
                if len(conversations) == 1:
                    node = conversations[0]
                    owner = collaboration(e)
                    other = endpoints[1] if endpoints[0] is node else endpoints[0]
                    participant = party(other, owner)
                    if collaboration(node) is not owner or (participant is not None and participant not in refs(node, 'participantRef')):
                        issue('conversation-link', e, 'link must connect a conversation to one of its own participating InteractionNodes')
        if k == 'globalConversation' and any(kind(c) in CONVERSATIONS for c in e):
            issue('global-conversation-content', e, 'GlobalConversation must not contain ConversationNodes')
        if k in CHOREOGRAPHY_ACTIVITIES:
            if kind(e.getparent()) not in {'choreography', 'subChoreography'}:
                issue('choreography-activity-scope', e, 'Choreography Activity must be contained by Choreography or SubChoreography')
            values = refs(e, 'participantRef')
            owner = collaboration(e)
            available = declared_parties(owner)
            if len(values) < 2 or len({v for v in values if v}) != len([v for v in values if v]):
                issue('choreography-activity-scope', e, 'Choreography Activity requires at least two distinct participant references')
            for v in values:
                if v and v in nodes and (kind(nodes[v]) != 'participant' or v not in available):
                    issue('choreography-activity-scope', e, 'participantRef must name a Participant of the containing Choreography')
            initiator = ref(e, e.get('initiatingParticipantRef'))
            if not e.get('initiatingParticipantRef') or (initiator is not None and initiator not in values):
                issue('choreography-activity-scope', e, 'initiatingParticipantRef must identify a participating party')
            if k == 'choreographyTask':
                messages = e.findall(q('messageFlowRef'))
                if len(values) != 2:
                    issue('choreography-task-message', e, 'ChoreographyTask is an interaction between exactly two Participants')
                if not 1 <= len(messages) <= 2:
                    issue('choreography-task-message', e, 'ChoreographyTask requires one or two messageFlowRef entries (official XSD exchange restriction)')
                directions = []
                for c in messages:
                    flow = resolve(c, c.text)
                    if flow is not None and (kind(flow) != 'messageFlow' or flow.getparent() is not owner):
                        issue('choreography-task-message', e, 'messageFlowRef must name a MessageFlow of the containing Choreography')
                    elif flow is not None:
                        endpoints = [ref(flow, flow.get(a)) for a in ('sourceRef', 'targetRef')]
                        if all(p is not None for p in endpoints):
                            if set(endpoints) != set(values):
                                issue('choreography-task-message', e, 'message flow must connect the two task Participants')
                            directions.append(tuple(endpoints))
                if directions and initiator is not None and not any(a == initiator for a, _ in directions):
                    issue('choreography-task-message', e, 'one task message must be sent by the initiating Participant')
                if len(directions) == 2 and directions[0] != directions[1][::-1]:
                    issue('choreography-task-message', e, 'a two-message task has initiating and return directions')
            if k == 'callChoreography' and e.get('calledChoreographyRef'):
                target = resolve(e, e.get('calledChoreographyRef'))
                if target is not None and kind(target) not in {'choreography', 'globalChoreographyTask'}:
                    issue('call-choreography-target', e, 'CallChoreography may call Choreography or GlobalChoreographyTask only')
        if k in {'callConversation', 'callChoreography'}:
            target_attr = 'calledCollaborationRef' if k == 'callConversation' else 'calledChoreographyRef'
            target = resolve(e, e.get(target_attr))
            available_inner = declared_parties(target)
            available_outer = set(refs(e, 'participantRef'))
            seen = set()
            for association in e.findall(q('participantAssociation')):
                inner = association.find(q('innerParticipantRef'))
                outer = association.find(q('outerParticipantRef'))
                a = ref(inner, inner.text) if inner is not None else None
                b = ref(outer, outer.text) if outer is not None else None
                if target is not None and a is not None and b is not None:
                    if a not in available_inner or b not in available_outer or a in seen:
                        issue('participant-association', association, 'association maps distinct called Participants to the call Participants')
                    seen.add(a)
        if k == 'globalChoreographyTask':
            if any(kind(c) in FLOW_ELEMENTS for c in e):
                issue('global-choreography-content', e, 'GlobalChoreographyTask must not contain Flow Elements')
            initiator = ref(e, e.get('initiatingParticipantRef'))
            if not e.get('initiatingParticipantRef') or (initiator is not None and initiator not in declared_parties(e)):
                issue('global-choreography-content', e, 'GlobalChoreographyTask initiator must be a declared Participant')

    bands = {}
    for shape in root.iter(d('BPMNShape')):
        semantic = resolve(shape, shape.get('bpmnElement'))
        k = kind(semantic)
        applicability = {'isHorizontal': {'participant', 'lane'},
                         'isExpanded': {'subProcess', 'adHocSubProcess', 'transaction', 'subChoreography', 'callActivity', 'callChoreography'},
                         'isMarkerVisible': {'exclusiveGateway'}}
        for attr, allowed in applicability.items():
            if attr in shape.attrib and semantic is not None and k not in allowed:
                issue('di-attribute-applicability', shape, attr + ' does not apply to ' + k)
        band_kind = shape.get('participantBandKind')
        if not band_kind:
            if 'choreographyActivityShape' in shape.attrib or 'isMessageVisible' in shape.attrib:
                issue('di-attribute-applicability', shape, 'choreographyActivityShape/isMessageVisible applies only to Participant Bands')
            continue
        activity_shape = resolve(shape, shape.get('choreographyActivityShape'))
        if semantic is not None and k != 'participant':
            issue('di-participant-band', shape, 'Participant Band must depict a Participant')
        if not shape.get('choreographyActivityShape') or (activity_shape is not None and kind(activity_shape) != 'BPMNShape'):
            issue('di-participant-band', shape, 'Participant Band requires choreographyActivityShape pointing to a BPMNShape')
            continue
        if activity_shape is None:
            continue
        activity = resolve(activity_shape, activity_shape.get('bpmnElement'))
        if activity is not None and kind(activity) not in CHOREOGRAPHY_ACTIVITIES:
            issue('di-participant-band', shape, 'Participant Band owner must depict a Choreography Activity')
            continue
        bands.setdefault(activity_shape, []).append(shape)
        if activity is None:
            continue
        ident = ref(shape, shape.get('bpmnElement'))
        values = refs(activity, 'participantRef')
        initiator = ref(activity, activity.get('initiatingParticipantRef'))
        if ident is not None and ident not in values:
            issue('di-participant-band', shape, 'band Participant is not referenced by its Choreography Activity')
        if ident is not None and initiator is not None and band_kind.endswith('non_initiating') == (ident == initiator):
            issue('di-participant-band', shape, 'band shading contradicts initiatingParticipantRef')
        if local_id(shape.get('isMessageVisible')) in {'true', '1'}:
            target = resolve(activity, activity.get('calledChoreographyRef')) if kind(activity) == 'callChoreography' else None
            if kind(activity) == 'subChoreography' or (kind(activity) == 'callChoreography' and kind(target) != 'globalChoreographyTask'):
                issue('di-band-message', shape, 'envelope decorator applies only to ChoreographyTask or a call of GlobalChoreographyTask')
            else:
                flows = [resolve(c, c.text) for c in activity.findall(q('messageFlowRef'))] if kind(activity) == 'choreographyTask' else list(target.findall(q('messageFlow'))) if target is not None else []
                mapping = {}
                for a in activity.findall(q('participantAssociation')):
                    inner, outer = a.find(q('innerParticipantRef')), a.find(q('outerParticipantRef'))
                    if inner is not None and outer is not None:
                        mapping[ref(inner, inner.text)] = ref(outer, outer.text)
                if flows and not any(f is not None and mapping.get(ref(f, f.get('sourceRef')), ref(f, f.get('sourceRef'))) == ident for f in flows):
                    issue('di-band-message', shape, 'visible envelope must be tethered to a message sender')

    for activity_shape, group in bands.items():
        activity = resolve(activity_shape, activity_shape.get('bpmnElement'))
        identities = [ref(s, s.get('bpmnElement')) for s in group]
        if len(group) < 2 or len(set(identities)) != len(identities):
            issue('di-participant-band', activity_shape, 'activity depiction requires at least two distinct Participant Bands')
        if activity is not None and ref(activity, activity.get('initiatingParticipantRef')) not in identities:
            issue('di-participant-band', activity_shape, 'activity depiction must include its initiating Participant Band')
        if activity is not None and kind(activity) == 'choreographyTask' and set(identities) != set(refs(activity, 'participantRef')):
            issue('di-participant-band', activity_shape, 'task depiction must show both Participants')

    for edge in root.iter(d('BPMNEdge')):
        for attr in ('sourceElement', 'targetElement'):
            if edge.get(attr):
                target = resolve(edge, edge.get(attr))
                if target is not None and (kind(target) not in {'BPMNShape', 'BPMNEdge'} or target.get('participantBandKind')):
                    issue('di-edge-endpoint', edge, attr + ' must refer to a DI Shape/Edge and never to a Participant Band')
        semantic = resolve(edge, edge.get('bpmnElement'))
        if kind(semantic) in {'dataInputAssociation', 'dataOutputAssociation'}:
            plane=edge.getparent()
            source_ids=refs(semantic,'sourceRef');target_ids=refs(semantic,'targetRef')
            for direction,identities in [('source',source_ids),('target',target_ids)]:
                if edge.get(direction+'Element'):
                    continue
                matching=[graphic for graphic in plane if kind(graphic) in {'BPMNShape','BPMNEdge'}
                          and not graphic.get('participantBandKind') and ref(graphic,graphic.get('bpmnElement')) in identities]
                if len(identities)!=1 or len(matching)!=1:
                    issue('di-edge-endpoint', edge, 'Data Association '+direction+' is undepicted or ambiguous; explicit '+direction+'Element is required')

    from bpmn_data_compensation import check as check_data_compensation
    data_compensation = check_data_compensation(root)
    return {'implemented_rule_ids': list(RULES) + data_compensation['implemented_rule_ids'],
            'findings': findings + data_compensation['findings'],
            'normative_rule_basis': {**{r: {'section': v[0], 'physical_pages': v[1], 'pdf_sha256': PDF_SHA256} for r, v in RULES.items()},
                                    **data_compensation['normative_rule_basis']},
            'data_compensation_validation': data_compensation,
            'capability_uncovered': data_compensation['capability_uncovered'],
            'exchange_adaptations': [{'element': 'ChoreographyTask.messageFlowRef',
                                      'normative_text': 'Table 11.2 [1..*]; task prose describes one or two exchanges',
                                      'official_xsd': 'Semantic.xsd tChoreographyTask minOccurs=1 maxOccurs=2',
                                      'execution': 'enforce official XML exchange cardinality 1..2; preserve original source and record discrepancy'},
                                     {'element': 'ParticipantMultiplicity.maximum',
                                      'normative_text': 'Section 9.3.1 printed page 117: show multi-instance marker when maximum is omitted or >=2',
                                      'official_xsd': 'Semantic.xsd tParticipantMultiplicity maximum default=1',
                                      'execution': 'preserve omitted/explicit distinction; depict marker using prose and retain default discrepancy in evidence'}]
                                    + data_compensation['exchange_adaptations'],
            'full_design_time_semantics': 'incomplete',
            'independent_normative_rule_review': 'pending'}
