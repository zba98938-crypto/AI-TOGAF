"""Independent design-time BPMN checks; rule coverage is explicit, never full-language proof."""
BPMN = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
RULES = {
 'sequence-scope':'Sequence flows stay within the same flow-element container.',
 'sequence-endpoint-type':'Sequence flow endpoints are FlowNodes of the containing process or choreography.',
 'flow-node-association':'Explicit incoming/outgoing references name sequence flows connected to that node.',
 'default-flow':'A default reference names an outgoing sequence flow of its owner.',
 'event-direction':'Start/end events cannot receive/send sequence flows respectively.',
 'boundary-attachment':'Boundary events attach to a process or choreography activity in their own container.',
 'boundary-flow':'Boundary events have no incoming sequence flow.',
 'event-subprocess-flow':'Event subprocesses have no incoming or outgoing sequence flow.',
 'parallel-conditions':'Parallel gateway outgoing sequence flows have no condition.',
 'event-gateway-target':'Event-based gateways lead to catching events or receive tasks.',
 'event-gateway-conditions':'Event-based gateway outgoing flows have no conditions/default.',
 'event-gateway-cardinality':'Event-based gateways have at least two outgoing sequence flows.',
 'event-gateway-configuration':'Event gateway catches use allowed triggers, no mixed message/receive configuration, attached events or additional incoming flows.',
 'event-gateway-instantiation':'Parallel event gateways instantiate with message triggers; instantiating process gateways have no incoming flow.',
 'compensation-flow':'Compensation activities are outside normal sequence flow.',
 'cancel-scope':'Cancel events belong to transaction scope.',
 'throw-trigger':'Throw events cannot throw timer or conditional triggers.',
 'message-pool':'Message flows cannot connect endpoints within one participant.',
 'message-endpoint-type':'Message flow endpoints are Participants, Activities or Events.',
 'choreography-participants':'Initiator references a participating party.',
 'di-shape':'Diagram shapes reference semantic elements and have positive bounds.',
 'di-edge':'Diagram edges reference flows/associations and contain two or more waypoints.',
}


def check(root):
    from bpmn_references import local_reference, local_id
    import math
    findings=[]
    q=lambda name:'{'+BPMN+'}'+name
    local=lambda e:e.tag.split('}')[-1] if isinstance(e.tag,str) else ''
    nodes={local_id(e.get('id')):e for e in root.iter() if isinstance(e.tag,str) and e.get('id')}
    def reference(e,value):
        return local_reference(e,value,root.get('targetNamespace'))[0]
    def resolve(e,value):
        return nodes.get(reference(e,value))
    def standard(e,kinds):
        return e is not None and e.tag in {q(k) for k in kinds}
    def yes(value):
        return local_id(value) in ('true','1')
    def issue(rule,e,message):
        findings.append({'rule_id':rule,'id':e.get('id'),'message':message,
                         'source_locator':'//*[@id='+repr(e.get('id'))+']'})
    def container(e):
        for p in e.iterancestors():
            if local(p) in ('process','subProcess','transaction','adHocSubProcess','choreography','subChoreography'):return p
        return None
    activity_types={'task','userTask','serviceTask','manualTask','sendTask','receiveTask','scriptTask','businessRuleTask','subProcess','transaction','adHocSubProcess','callActivity'}
    event_types={'startEvent','endEvent','boundaryEvent','intermediateCatchEvent','intermediateThrowEvent','implicitThrowEvent'}
    gateway_types={'exclusiveGateway','inclusiveGateway','parallelGateway','complexGateway','eventBasedGateway'}
    choreography_types={'choreographyTask','subChoreography','callChoreography'}
    outgoing={};incoming={}
    flows=list(root.iter(q('sequenceFlow')))
    for flow in flows:
        source=nodes.get(local_id(flow.get('sourceRef')));target=nodes.get(local_id(flow.get('targetRef')))
        outgoing.setdefault(local_id(flow.get('sourceRef')),[]).append(flow);incoming.setdefault(local_id(flow.get('targetRef')),[]).append(flow)
        owner=container(flow)
        allowed=(choreography_types if owner is not None and local(owner) in ('choreography','subChoreography') else activity_types)|event_types|gateway_types
        for endpoint in (source,target):
            if endpoint is not None and not standard(endpoint,allowed):
                issue('sequence-endpoint-type',flow,'sequence flow endpoint is not an allowed FlowNode')
        if source is not None and target is not None and (container(source) is not container(target) or container(source) is not container(flow)):
            issue('sequence-scope',flow,'sequence flow crosses flow-element container boundary')
    def definitions(event):
        result=[x for x in event if isinstance(x.tag,str) and x.tag.startswith('{'+BPMN+'}') and local(x).endswith('EventDefinition')]
        unresolved=False
        for child in event.findall(q('eventDefinitionRef')):
            target=resolve(child,child.text)
            if target is None:unresolved=True
            else:result.append(target)
        return result,unresolved
    for e in root.iter():
        if not isinstance(e.tag,str) or not e.tag.startswith('{'+BPMN+'}'):continue
        kind=local(e);identity=local_id(e.get('id'));inc=incoming.get(identity,[]);out=outgoing.get(identity,[])
        for direction,endpoint_attr in (('incoming','targetRef'),('outgoing','sourceRef')):
            for child in e.findall(q(direction)):
                flow=resolve(child,child.text)
                if flow is not None and (not standard(flow,{'sequenceFlow'}) or local_id(flow.get(endpoint_attr))!=identity):
                    issue('flow-node-association',e,'explicit '+direction+' reference is not a sequence flow connected to this node')
        if e.get('default'):
            default=resolve(e,e.get('default'))
            if default is not None and (not standard(default,{'sequenceFlow'}) or local_id(default.get('sourceRef'))!=identity):
                issue('default-flow',e,'default reference is not an outgoing sequence flow of this node')
        if kind=='startEvent' and inc:issue('event-direction',e,'start event has incoming sequence flow')
        if kind=='endEvent' and out:issue('event-direction',e,'end event has outgoing sequence flow')
        if kind=='boundaryEvent':
            attached=resolve(e,e.get('attachedToRef'))
            ref,problem=local_reference(e,e.get('attachedToRef'),root.get('targetNamespace'))
            owner=container(e)
            allowed_activities=choreography_types if owner is not None and local(owner) in ('choreography','subChoreography') else activity_types
            if not problem and (attached is None or not standard(attached,allowed_activities) or container(attached) is not owner):issue('boundary-attachment',e,'boundary event must attach to an activity in the same scope')
            if inc:issue('boundary-flow',e,'boundary event has incoming sequence flow')
        if kind=='subProcess' and yes(e.get('triggeredByEvent')) and (inc or out):issue('event-subprocess-flow',e,'event subprocess participates in normal sequence flow')
        if kind=='parallelGateway' and any(f.find(q('conditionExpression')) is not None for f in out):issue('parallel-conditions',e,'parallel gateway has conditional outgoing flow')
        if kind=='eventBasedGateway':
            owner=container(e)
            choreography=owner is not None and local(owner) in ('choreography','subChoreography')
            if len(out)<2:issue('event-gateway-cardinality',e,'event gateway requires two or more outgoing sequence flows')
            if not choreography:
                if e.get('eventGatewayType')=='Parallel' and not yes(e.get('instantiate')):
                    issue('event-gateway-instantiation',e,'parallel event gateway must instantiate its process')
                if yes(e.get('instantiate')) and inc:
                    issue('event-gateway-instantiation',e,'instantiating event gateway has incoming sequence flow')
            has_message=False;has_receive=False
            for f in out:
                target=nodes.get(local_id(f.get('targetRef')))
                allowed_targets=choreography_types|{'intermediateCatchEvent'} if choreography else {'intermediateCatchEvent','receiveTask'}
                if target is not None and not standard(target,allowed_targets):issue('event-gateway-target',f,'event gateway target is not an allowed process/choreography target')
                if target is not None:
                    if not choreography and any(local_id(other.get('sourceRef'))!=identity for other in incoming.get(local_id(target.get('id')),[])):
                        issue('event-gateway-configuration',target,'event gateway target has an additional incoming sequence flow')
                    if standard(target,{'receiveTask'}):
                        has_receive=True
                        if any(resolve(boundary,boundary.get('attachedToRef')) is target for boundary in root.iter(q('boundaryEvent'))):
                            issue('event-gateway-configuration',target,'event gateway receive task has an attached event')
                    elif standard(target,{'intermediateCatchEvent'}):
                        triggers,unresolved=definitions(target)
                        allowed_triggers={'signalEventDefinition','timerEventDefinition'} if choreography else {'messageEventDefinition','signalEventDefinition','timerEventDefinition','conditionalEventDefinition'}
                        if not choreography and e.get('eventGatewayType')=='Parallel':
                            allowed_triggers={'messageEventDefinition'}
                        if (not triggers and not unresolved) or any(not standard(trigger,allowed_triggers) for trigger in triggers):
                            issue('event-gateway-configuration',target,'event gateway catch uses a missing or prohibited trigger')
                        has_message=has_message or any(standard(trigger,{'messageEventDefinition'}) for trigger in triggers)
                if f.find(q('conditionExpression')) is not None:issue('event-gateway-conditions',f,'event gateway outgoing flow has condition')
            if not choreography and has_message and has_receive:issue('event-gateway-configuration',e,'event gateway mixes message catches and receive tasks')
            if e.get('default'):issue('event-gateway-conditions',e,'event gateway has default sequence flow')
        if kind in activity_types and yes(e.get('isForCompensation')) and (inc or out):issue('compensation-flow',e,'compensation activity participates in normal sequence flow')
        if kind in event_types and any(standard(trigger,{'cancelEventDefinition'}) for trigger in definitions(e)[0]):
            parent=e;owner=container(parent)
            # A boundary cancel event is outside the transaction it attaches to.
            attached=resolve(parent,parent.get('attachedToRef')) if local(parent)=='boundaryEvent' else None
            choreography_cancel=(owner is not None and local(owner) in ('choreography','subChoreography')
                                and standard(attached,choreography_types) and container(attached) is owner)
            if not ((local(parent)=='endEvent' and owner is not None and local(owner)=='transaction')
                    or standard(attached,{'transaction'}) or choreography_cancel):
                issue('cancel-scope',parent,'cancel event must end/attach to a transaction, or catch on a choreography activity')
            if kind=='boundaryEvent' and local_id(e.get('cancelActivity')) in ('false','0'):
                issue('cancel-scope',e,'boundary cancel event must interrupt its attached activity')
        if kind in ('endEvent','intermediateThrowEvent','implicitThrowEvent') and any(standard(trigger,{'timerEventDefinition','conditionalEventDefinition'}) for trigger in definitions(e)[0]):issue('throw-trigger',e,'timer and conditional event definitions are catch-only')
        if kind in ('choreographyTask','subChoreography','callChoreography'):
            parties={reference(x,x.text) for x in e.findall(q('participantRef')) if x.text}
            initiator=reference(e,e.get('initiatingParticipantRef'))
            if initiator is not None and initiator not in parties:issue('choreography-participants',e,'initiator is not a participant in this choreography activity')
    process_parties={reference(e,e.get('processRef')):local_id(e.get('id')) for e in root.iter(q('participant')) if e.get('processRef')}
    def party(e):
        if e is None:return None
        if local(e)=='participant':return local_id(e.get('id'))
        for p in e.iterancestors(q('process')):return process_parties.get(local_id(p.get('id')))
        return None
    for flow in root.iter(q('messageFlow')):
        for value in (flow.get('sourceRef'),flow.get('targetRef')):
            endpoint=resolve(flow,value)
            if endpoint is not None and not standard(endpoint,activity_types|event_types|{'participant'}):
                issue('message-endpoint-type',flow,'message flow endpoint is not a Participant, Activity or Event')
        a,b=party(resolve(flow,flow.get('sourceRef'))),party(resolve(flow,flow.get('targetRef')))
        if a and b and a==b:issue('message-pool',flow,'message flow endpoints belong to the same participant')
    for shape in root.iter('{'+DI+'}BPMNShape'):
        ref,problem=local_reference(shape,shape.get('bpmnElement'),root.get('targetNamespace'))
        if not problem and ref not in nodes:issue('di-shape',shape,'shape has unresolved semantic element')
        bounds=next((x for x in shape if local(x)=='Bounds'),None)
        try:
            values=[float(bounds.get(k)) for k in ('x','y','width','height')]
            if not all(map(math.isfinite,values)) or values[2]<=0 or values[3]<=0:raise ValueError()
        except (ValueError,TypeError,AttributeError):issue('di-shape',shape,'shape requires finite positive bounds')
    for edge in root.iter('{'+DI+'}BPMNEdge'):
        target=resolve(edge,edge.get('bpmnElement'))
        ref,problem=local_reference(edge,edge.get('bpmnElement'),root.get('targetNamespace'))
        if not problem and (target is None or not standard(target,{'sequenceFlow','messageFlow','association','dataInputAssociation','dataOutputAssociation','conversationLink'})):issue('di-edge',edge,'diagram edge does not refer to a semantic connector')
        points=[x for x in edge if local(x)=='waypoint']
        if len(points)<2:issue('di-edge',edge,'diagram edge has fewer than two waypoints')
        try:
            if not all(math.isfinite(float(point.get(axis))) for point in points for axis in ('x','y')):raise ValueError()
        except (ValueError,TypeError):issue('di-edge',edge,'diagram edge requires finite waypoints')
    from pathlib import Path
    import hashlib,json
    basis_path=Path(__file__).resolve().parents[1]/'standards/bpmn-rule-basis.json'
    basis_bytes=basis_path.read_bytes();basis=json.loads(basis_bytes)
    if set(basis['rules'])!=set(RULES):raise ValueError('BPMN rule basis does not match implemented family IDs')
    return {'implemented_rule_ids':list(RULES),'findings':findings,
            'normative_rule_basis':basis,'normative_rule_basis_sha256':hashlib.sha256(basis_bytes).hexdigest(),
            'full_behavior_semantics':'incomplete','independent_normative_rule_review':'pending'}
