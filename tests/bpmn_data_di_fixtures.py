"""Independent source-DI partial data views, with lexical geometry oracles."""
from lxml import etree
from bpmn_data_compensation_fixtures import element,io,association,bytes_xml,MODEL,by_id,change

DI='http://www.omg.org/spec/BPMN/20100524/DI'
DC='http://www.omg.org/spec/DD/20100524/DC'
WAY='http://www.omg.org/spec/DD/20100524/DI'
TARGET='urn:independent:data-di'


def shape(plane,sid,x,y,width,height,**attrs):
    e=etree.SubElement(plane,'{'+DI+'}BPMNShape',id=sid+'_DI',bpmnElement=sid,**attrs)
    etree.SubElement(e,'{'+DC+'}Bounds',x=x,y=y,width=width,height=height)
    return e


def edge(plane,sid,points,**attrs):
    e=etree.SubElement(plane,'{'+DI+'}BPMNEdge',id=sid+'_DI',bpmnElement=sid,**attrs)
    for x,y in points:etree.SubElement(e,'{'+WAY+'}waypoint',x=x,y=y)
    return e


def data_di_model():
    root=etree.Element('{'+MODEL+'}definitions',nsmap={None:MODEL,'tns':TARGET,'bpmndi':DI,'dc':DC,'di':WAY},targetNamespace=TARGET)
    element(root,'itemDefinition',id='I');element(root,'itemDefinition',id='COL',isCollection='true')
    element(root,'dataStore',id='STORE',itemSubjectRef='tns:I')
    p=element(root,'process',id='P');io(p,'PROC')
    by_id(root,'PROC_IN0').set('name','输入');by_id(root,'PROC_OUT0').set('name','输出集')
    by_id(root,'PROC_OUT0').set('itemSubjectRef','tns:COL');by_id(root,'PROC_OUT0').set('isCollection','true')
    element(p,'dataObject',id='D',itemSubjectRef='tns:COL',isCollection='true')
    ref=element(p,'dataObjectReference',id='DR',name='申请集',dataObjectRef='D');element(ref,'dataState',name='待审')
    element(p,'dataStoreReference',id='DSR',name='归档库',dataStoreRef='tns:STORE')
    a=element(p,'task',id='A',name='审核');io(a,'A')
    by_id(root,'A_IN0').set('itemSubjectRef','tns:COL');by_id(root,'A_IN0').set('isCollection','true');by_id(root,'A_IN0').set('name','入参集')
    by_id(root,'A_OUT0').set('name','结果')
    association(a,'dataInputAssociation','DIN',['DR'],'A_IN0')
    association(a,'dataOutputAssociation','DOUT',['A_OUT0'],'DSR')
    catch=element(p,'intermediateCatchEvent',id='CATCH',name='接收')
    element(catch,'dataOutput',id='CATCH_OUT',name='消息值',itemSubjectRef='tns:I')
    association(catch,'dataOutputAssociation','CATCH_ASSOC',['CATCH_OUT'],'DSR')
    group=element(catch,'outputSet',id='CATCH_OS');element(group,'dataOutputRefs','CATCH_OUT')
    element(catch,'messageEventDefinition',id='CATCH_MESSAGE')
    throw=element(p,'intermediateThrowEvent',id='THROW',name='发送')
    element(throw,'dataInput',id='THROW_IN',name='发送集',itemSubjectRef='tns:COL',isCollection='true')
    association(throw,'dataInputAssociation','THROW_ASSOC',['DR'],'THROW_IN')
    group=element(throw,'inputSet',id='THROW_IS');element(group,'dataInputRefs','THROW_IN')
    element(throw,'messageEventDefinition',id='THROW_MESSAGE')
    sub=element(p,'subProcess',id='SUB',name='后续');inner=element(sub,'task',id='INNER',name='内部')
    io(inner,'INNER');by_id(root,'INNER_IN0').set('itemSubjectRef','tns:COL');by_id(root,'INNER_IN0').set('isCollection','true')
    association(inner,'dataInputAssociation','INNER_ASSOC',['DR'],'INNER_IN0')
    diagram=etree.SubElement(root,'{'+DI+'}BPMNDiagram',id='DIAGRAM')
    plane=etree.SubElement(diagram,'{'+DI+'}BPMNPlane',id='PLANE',bpmnElement='P')
    # Order intentionally includes an edge before later endpoint shapes. The
    # source order is normative z-order, not object-construction order.
    edge(plane,'DIN',[('76.000','195.00'),('240.000','195.00')],targetElement='A_DI')
    for sid,x,y,w,h in [('PROC_IN0','40.000','40.00','36.000','50.0'),('PROC_OUT0','120.000','40.00','36.000','50.0'),
                        ('A_IN0','210.000','40.00','36.000','50.0'),('A_OUT0','320.000','40.00','36.000','50.0'),
                        ('DR','40.000','170.00','36.000','50.0'),('DSR','480.000','170.00','50.000','50.0'),
                        ('A','240.000','155.00','130.000','90.0'),('CATCH','240.000','330.00','36.000','36.0'),
                        ('CATCH_OUT','440.000','330.00','36.000','50.0'),('THROW','80.000','330.00','36.000','36.0'),
                        ('THROW_IN','160.000','420.00','36.000','50.0'),('SUB','700.000','150.00','160.000','150.0')]:
        graphic=shape(plane,sid,x,y,w,h,**({'isExpanded':'false'} if sid=='SUB' else {}))
        if sid in {'DR','DSR'}:
            label=etree.SubElement(graphic,'{'+DI+'}BPMNLabel')
            etree.SubElement(label,'{'+DC+'}Bounds',x='0.000' if sid=='DR' else '440.000',y='128.00',width='140.000',height='22.0')
    edge(plane,'DOUT',[('370.000','200.00'),('480.000','200.00')],sourceElement='A_DI')
    edge(plane,'CATCH_ASSOC',[('476.000','350.00'),('505.000','350.00'),('505.000','220.00')])
    edge(plane,'THROW_ASSOC',[('58.000','220.00'),('58.000','348.00'),('80.000','348.00')],targetElement='THROW_DI')
    return bytes_xml(root)


def remove_di(data,*ids):
    def mutate(root):
        for sid in ids:
            e=by_id(root,sid+'_DI');e.getparent().remove(e)
    return change(data,mutate)


def boundary_di_model():
    data=remove_di(data_di_model(),'A_IN0','A_OUT0','CATCH_OUT','THROW_IN')
    def mutate(root):
        edge=by_id(root,'CATCH_ASSOC_DI');edge.set('sourceElement','CATCH_DI')
        points=[p for p in edge if p.tag.endswith('waypoint')]
        points[0].set('x','276.000');points[0].set('y','348.00');points[1].set('y','348.00')
    return change(data,mutate)
