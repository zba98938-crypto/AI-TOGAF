"""Independent explicit-DI examples derived from BPMN PDF sections 9.5/11.5/12.

Semantic names, coordinates and message directions are authored here; they are
not synthesized from renderer output or a standard-coverage binding table.
"""
from lxml import etree

MODEL = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
DC = 'http://www.omg.org/spec/DD/20100524/DC'
DD = 'http://www.omg.org/spec/DD/20100524/DI'


def element(parent, tag, text=None, **attrs):
    e = etree.SubElement(parent, '{' + MODEL + '}' + tag, attrs)
    e.text = text
    return e


def definitions():
    return etree.Element('{' + MODEL + '}definitions', nsmap={None: MODEL, 'bpmndi': DI, 'dc': DC, 'di': DD, 'tns': 'urn:independent:design'}, targetNamespace='urn:independent:design')


def shape(plane, sid, x, y, w, h, gid=None, **attrs):
    e = etree.SubElement(plane, '{' + DI + '}BPMNShape', id=gid or sid+'_DI', bpmnElement='tns:'+sid, **attrs)
    etree.SubElement(e, '{' + DC + '}Bounds', x=str(x), y=str(y), width=str(w), height=str(h))
    return e


def edge(plane, sid, points, **attrs):
    e = etree.SubElement(plane, '{' + DI + '}BPMNEdge', id=sid+'_DI', bpmnElement='tns:'+sid, **attrs)
    for x, y in points:
        etree.SubElement(e, '{' + DD + '}waypoint', x=str(x), y=str(y))
    return e


def plane(root, target):
    diagram = etree.SubElement(root, '{' + DI + '}BPMNDiagram', id='DIAGRAM')
    return etree.SubElement(diagram, '{' + DI + '}BPMNPlane', id='PLANE', bpmnElement='tns:'+target)


def participants(owner, ids):
    for sid, name in ids:
        element(owner, 'participant', id=sid, name=name)


def activity(owner, kind, sid, name, parties, initiator, messages=(), called=None, loop='None'):
    attrs = {'id': sid, 'name': name, 'initiatingParticipantRef': 'tns:'+initiator, 'loopType': loop}
    if called:
        attrs['calledChoreographyRef'] = 'tns:'+called
    e = element(owner, kind, **attrs)
    for p in parties:
        element(e, 'participantRef', 'tns:'+p)
    for m in messages:
        element(e, 'messageFlowRef', 'tns:'+m)
    return e


def mapping(owner, inner, outer):
    e = element(owner, 'participantAssociation', id=owner.get('id')+'_'+inner+'_'+outer)
    element(e, 'innerParticipantRef', 'tns:'+inner)
    element(e, 'outerParticipantRef', 'tns:'+outer)


def bands(p, sid, x, y, w, h, parties, initiator, visible=()):
    for index, party in enumerate(parties):
        pos = 'top' if index == 0 else 'bottom' if index == len(parties)-1 else 'middle'
        by = y if index == 0 else y+h-36*(len(parties)-index)
        shading = 'initiating' if party == initiator else 'non_initiating'
        shape(p, party, x, by, w, 36, gid=sid+'_'+party+'_BAND', participantBandKind=pos+'_'+shading,
              choreographyActivityShape='tns:'+sid+'_DI', isMessageVisible='true' if party in visible else 'false')


def conversation():
    root = definitions()
    owner = element(root, 'collaboration', id='COLLAB')
    participants(owner, [('A', '采购方'), ('B', '供应方')])
    element(owner, 'messageFlow', id='M', sourceRef='tns:A', targetRef='tns:B')
    for k, sid, name, called in [('conversation', 'CV', '订单协商', None), ('subConversation', 'SC', '交付会话', None),
                                 ('callConversation', 'CG', '通用沟通', 'GLOBAL'), ('callConversation', 'CC', '调用协作', 'REUSE')]:
        e = element(owner, k, id=sid, name=name, **({'calledCollaborationRef':'tns:'+called} if called else {}))
        for party in ['A', 'B']:
            element(e, 'participantRef', 'tns:'+party)
        if sid == 'CV':
            element(e, 'messageFlowRef', 'tns:M')
        if sid == 'SC':
            child = element(e, 'conversation', id='DETAIL', name='详细交付')
            for party in ['A', 'B']:
                element(child, 'participantRef', 'tns:'+party)
        if called:
            mapping(e, called+'_A', 'A')
            mapping(e, called+'_B', 'B')
    for sid, a, b in [('L1','A','CV'),('L2','CV','B'),('L3','A','SC'),('L4','CG','B'),('L5','CC','B')]:
        element(owner,'conversationLink',id=sid,sourceRef='tns:'+a,targetRef='tns:'+b)
    for k, sid in [('globalConversation','GLOBAL'),('collaboration','REUSE')]:
        called = element(root,k,id=sid)
        participants(called,[(sid+'_A','被调用方甲'),(sid+'_B','被调用方乙')])
    p=plane(root,'COLLAB')
    shape(p,'A',40,40,120,360,isHorizontal='false')
    shape(p,'B',580,40,120,360,isHorizontal='false')
    for sid, x, y in [('CV',270,80),('SC',370,180),('CG',270,280),('CC',450,280)]:
        shape(p,sid,x,y,48,48)
    edge(p,'L1',[(160,104),(270,104)])
    edge(p,'L2',[(318,104),(580,104)])
    edge(p,'L3',[(160,204),(370,204)])
    edge(p,'L4',[(318,304),(350,304),(350,380),(580,380)])
    edge(p,'L5',[(498,304),(580,304)])
    return etree.tostring(root,xml_declaration=True,encoding='utf-8')


def choreography(expanded_sub=False, expanded_call=False):
    root=definitions()
    owner=element(root,'choreography',id='CHOREO')
    participants(owner,[('A','采购方'),('B','供应方'),('C','物流方')])
    multiplicity=element(owner.find('{'+MODEL+'}participant[@id="C"]'),'participantMultiplicity',id='C_MULTI',minimum='1',maximum='3')
    for sid,a,b in [('M1','A','B'),('M2','B','A'),('M3','A','B'),('M4','B','C')]:
        element(owner,'messageFlow',id=sid,sourceRef='tns:'+a,targetRef='tns:'+b)
    element(owner,'startEvent',id='START',name='开始')
    activity(owner,'choreographyTask','T1','订购与答复',['A','B'],'A',['M1','M2'],loop='Standard')
    activity(owner,'choreographyTask','T2','批量订购',['A','B'],'A',['M3'],loop='MultiInstanceParallel')
    sub=activity(owner,'subChoreography','SUB','协同交付',['A','C','B'],'B',loop='MultiInstanceSequential')
    activity(sub,'choreographyTask','INNER','配送交接',['B','C'],'B',['M4'])
    call=activity(owner,'callChoreography','CG','通用订购',['A','B'],'A',called='GLOBAL')
    mapping(call,'GA','A');mapping(call,'GB','B')
    call=activity(owner,'callChoreography','CC','调用编排',['A','B'],'A',called='REUSE')
    mapping(call,'RA','A');mapping(call,'RB','B')
    element(owner,'exclusiveGateway',id='GATE',name='确认？')
    element(owner,'endEvent',id='END',name='结束')
    chain=['START','T1','T2','SUB','CG','CC','GATE','END']
    for index,(a,b) in enumerate(zip(chain,chain[1:])):
        element(owner,'sequenceFlow',id='F'+str(index),sourceRef=a,targetRef=b)
    global_task=element(root,'globalChoreographyTask',id='GLOBAL',initiatingParticipantRef='tns:GA')
    participants(global_task,[('GA','通用采购'),('GB','通用供应')])
    element(global_task,'messageFlow',id='GM',sourceRef='tns:GA',targetRef='tns:GB')
    called=element(root,'choreography',id='REUSE')
    participants(called,[('RA','内部采购'),('RB','内部供应')])
    element(called,'messageFlow',id='RM',sourceRef='tns:RA',targetRef='tns:RB')
    activity(called,'choreographyTask','REUSED','被调用订购',['RA','RB'],'RA',['RM'])
    p=plane(root,'CHOREO')
    shape(p,'START',40,167,36,36)
    centers={'START':(76,185)}
    x=120
    for sid,party_list,initiator,visible in [('T1',['A','B'],'A',['A','B']),('T2',['A','B'],'A',['A']),('SUB',['A','C','B'],'B',[]),('CG',['A','B'],'A',['A']),('CC',['A','B'],'A',[])]:
        expanded=(sid=='SUB' and expanded_sub) or (sid=='CC' and expanded_call)
        w,h=(360,300) if expanded else (160,170)
        shape(p,sid,x,100,w,h,**({'isExpanded':'true' if expanded else 'false'} if sid in {'SUB','CC'} else {}))
        bands(p,sid,x,100,w,h,party_list,initiator,visible)
        centers[sid]=(x+w,185)
        if expanded:
            child='INNER' if sid=='SUB' else 'REUSED'
            parties=['B','C'] if sid=='SUB' else ['RA','RB']
            shape(p,child,x+95,175,170,140)
            bands(p,child,x+95,175,170,140,parties,parties[0])
        x+=w+70
    shape(p,'GATE',x,160,50,50,isMarkerVisible='true');centers['GATE']=(x+50,185)
    shape(p,'END',x+100,167,36,36)
    by_id={e.get('id'):e for e in p}
    for index,(a,b) in enumerate(zip(chain,chain[1:])):
        target=by_id[b+'_DI'].find('{'+DC+'}Bounds')
        edge(p,'F'+str(index),[centers[a],(float(target.get('x')),185)])
    return etree.tostring(root,xml_declaration=True,encoding='utf-8')
