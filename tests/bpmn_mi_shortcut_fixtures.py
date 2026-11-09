"""Independent MI/Table10.29, shortcut/Table12.35 and mixed/9.7 fixtures."""
from lxml import etree
from bpmn_data_compensation_fixtures import definitions,element,io,association,bytes_xml,by_id
from bpmn_data_di_fixtures import shape,edge,DI,DC,WAY
from bpmn_design_fixtures import activity,bands,mapping


def add_plane(root,target='P'):
    diagram=etree.SubElement(root,'{'+DI+'}BPMNDiagram',id='DIAGRAM')
    return etree.SubElement(diagram,'{'+DI+'}BPMNPlane',id='PLANE',bpmnElement='tns:'+target)


def mi_model(subprocess=False,sequential=False):
    root=definitions();element(root,'itemDefinition',id='I');element(root,'itemDefinition',id='COL',isCollection='true')
    element(root,'signalEventDefinition',id='SIGNAL')
    process=element(root,'process',id='P')
    element(process,'dataObject',id='SOURCE',itemSubjectRef='tns:COL',isCollection='true')
    element(process,'dataObject',id='RESULT',itemSubjectRef='tns:COL',isCollection='true')
    owner=element(process,'subProcess' if subprocess else 'task',id='A',name='逐项审核' if sequential else '并行审核')
    if not subprocess:
        io(owner,'A',definition='COL')
        for sid in ['A_IN0','A_OUT0']:by_id(root,sid).set('isCollection','true')
    loop=element(owner,'multiInstanceLoopCharacteristics',id='MI',isSequential='true' if sequential else 'false',behavior='One',oneBehaviorEventRef='tns:SIGNAL')
    element(loop,'loopDataInputRef','tns:SOURCE' if subprocess else 'tns:A_IN0')
    element(loop,'loopDataOutputRef','tns:RESULT' if subprocess else 'tns:A_OUT0')
    element(loop,'inputDataItem',id='ONE_IN',name='单项输入',itemSubjectRef='tns:I')
    element(loop,'outputDataItem',id='ONE_OUT',name='单项输出',itemSubjectRef='tns:I')
    plane=add_plane(root)
    shape(plane,'A','220.000','130.00','160.000','90.0',**({'isExpanded':'false'} if subprocess else {}))
    shape(plane,'ONE_IN','80.000','150.00','36.000','50.0')
    shape(plane,'ONE_OUT','480.000','150.00','36.000','50.0')
    return bytes_xml(root)


def shortcut_model():
    root=definitions();element(root,'itemDefinition',id='I')
    process=element(root,'process',id='P')
    element(process,'dataObject',id='D',itemSubjectRef='tns:I');element(process,'dataObjectReference',id='DR',name='审核资料',dataObjectRef='D')
    a=element(process,'task',id='A',name='准备资料');io(a,'A')
    association(a,'dataOutputAssociation','OUT',['A_OUT0'],'DR')
    b=element(process,'task',id='B',name='核对资料');io(b,'B')
    association(b,'dataInputAssociation','IN',['DR'],'B_IN0')
    element(process,'sequenceFlow',id='FLOW',sourceRef='A',targetRef='B')
    plane=add_plane(root)
    shape(plane,'A','40.000','150.00','140.000','90.0');shape(plane,'B','480.000','150.00','140.000','90.0')
    edge(plane,'FLOW',[('180.000','195.00'),('480.000','195.00')])
    shape(plane,'DR','310.000','50.00','36.000','50.0')
    shortcut=etree.SubElement(plane,'{'+DI+'}BPMNEdge',id='SHORTCUT_DI',sourceElement='tns:DR_DI',targetElement='tns:FLOW_DI')
    for x,y in [('328.000','100.00'),('328.000','195.00')]:etree.SubElement(shortcut,'{'+WAY+'}waypoint',x=x,y=y)
    return bytes_xml(root)


def mixed_model():
    root=definitions();element(root,'itemDefinition',id='I')
    process=element(root,'process',id='P')
    element(process,'dataObject',id='D',itemSubjectRef='tns:I');element(process,'dataObjectReference',id='DR',name='订单数据',dataObjectRef='D')
    task=element(process,'task',id='SEND',name='提交订单');io(task,'SEND')
    association(task,'dataInputAssociation','DIN',['DR'],'SEND_IN0')
    col=element(root,'collaboration',id='COLLAB')
    element(col,'participant',id='BUYER',name='采购流程',processRef='tns:P');element(col,'participant',id='SELLER',name='供应方')
    mapping(col,'CA','BUYER');mapping(col,'CB','SELLER')
    element(col,'choreographyRef','tns:CHOREO')
    choreo=element(root,'choreography',id='CHOREO')
    element(choreo,'participant',id='CA',name='采购方');element(choreo,'participant',id='CB',name='供应方')
    element(choreo,'messageFlow',id='M',sourceRef='tns:CA',targetRef='tns:CB')
    activity(choreo,'choreographyTask','CT','订单交互',['CA','CB'],'CA',['M'])
    plane=add_plane(root,'COLLAB')
    shape(plane,'BUYER','20.000','20.00','720.000','240.0',isHorizontal='true')
    shape(plane,'SELLER','20.000','490.00','720.000','120.0',isHorizontal='true')
    shape(plane,'SEND','480.000','95.00','160.000','90.0')
    shape(plane,'DR','120.000','100.00','36.000','50.0')
    edge(plane,'DIN',[('156.000','125.00'),('480.000','125.00')],targetElement='tns:SEND_DI')
    shape(plane,'CT','300.000','290.00','200.000','160.0')
    bands(plane,'CT',300,290,200,160,['CA','CB'],'CA')
    return bytes_xml(root)
