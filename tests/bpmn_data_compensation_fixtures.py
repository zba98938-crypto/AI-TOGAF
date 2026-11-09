"""Hand-authored BPMN data, lifecycle scopes and compensation oracle fixtures."""
from lxml import etree

MODEL='http://www.omg.org/spec/BPMN/20100524/MODEL'
TARGET='urn:independent:data-compensation'


def element(parent,tag,text=None,**attributes):
    child=etree.SubElement(parent,'{'+MODEL+'}'+tag,**attributes)
    child.text=text
    return child


def definitions():
    return etree.Element('{'+MODEL+'}definitions',nsmap={None:MODEL,'tns':TARGET,'outside':'urn:outside'},targetNamespace=TARGET)


def bytes_xml(root):
    return etree.tostring(root,xml_declaration=True,encoding='utf-8')


def io(owner,prefix,definition='I',inputs=1,outputs=1):
    spec=element(owner,'ioSpecification',id=prefix+'_IO')
    ins=[];outs=[]
    for index in range(inputs):
        sid=prefix+'_IN'+str(index);element(spec,'dataInput',id=sid,itemSubjectRef='tns:'+definition);ins.append(sid)
    for index in range(outputs):
        sid=prefix+'_OUT'+str(index);element(spec,'dataOutput',id=sid,itemSubjectRef='tns:'+definition);outs.append(sid)
    a=element(spec,'inputSet',id=prefix+'_IS')
    for sid in ins:element(a,'dataInputRefs',sid)
    b=element(spec,'outputSet',id=prefix+'_OS')
    for sid in outs:element(b,'dataOutputRefs',sid)
    element(a,'outputSetRefs',prefix+'_OS');element(b,'inputSetRefs',prefix+'_IS')
    return spec


def association(owner,name,sid,sources,target,transformation=False):
    e=element(owner,name,id=sid)
    for source in sources:element(e,'sourceRef',source)
    element(e,'targetRef',target)
    if transformation:element(e,'transformation','literal(42)',language='urn:fictional-expression')
    return e


def data_model():
    root=definitions()
    element(root,'itemDefinition',id='I',isCollection='false')
    element(root,'itemDefinition',id='OTHER_I',isCollection='false')
    element(root,'dataStore',id='STORE',itemSubjectRef='tns:I')
    p=element(root,'process',id='P')
    element(p,'property',id='P_PROP',itemSubjectRef='tns:I')
    element(p,'dataObject',id='D',itemSubjectRef='tns:I',isCollection='false')
    element(p,'dataObjectReference',id='DR',dataObjectRef='D')
    element(p,'dataStoreReference',id='DSR',dataStoreRef='tns:STORE')
    a=element(p,'task',id='A');io(a,'A');element(a,'property',id='A_PROP',itemSubjectRef='tns:I')
    association(a,'dataInputAssociation','DIN',['DR'],'A_IN0')
    association(a,'dataOutputAssociation','DOUT',['A_OUT0'],'DSR')
    b=element(p,'task',id='B');io(b,'B')
    element(p,'exclusiveGateway',id='G')
    sub=element(p,'subProcess',id='SUB')
    element(sub,'property',id='SUB_PROP',itemSubjectRef='tns:I')
    element(sub,'dataObject',id='INNER_D',itemSubjectRef='tns:I')
    child=element(sub,'task',id='CHILD');io(child,'CHILD')
    association(child,'dataInputAssociation','CHILD_IN',['D'],'CHILD_IN0')
    nested=element(sub,'subProcess',id='NESTED')
    grandchild=element(nested,'task',id='GRANDCHILD');io(grandchild,'GRANDCHILD')
    association(grandchild,'dataInputAssociation','GRAND_IN',['SUB_PROP'],'GRANDCHILD_IN0')
    q=element(root,'process',id='Q')
    element(q,'dataObject',id='FOREIGN_D',itemSubjectRef='tns:I')
    return bytes_xml(root)


def event_data_model():
    root=definitions();element(root,'itemDefinition',id='I')
    p=element(root,'process',id='P');element(p,'dataObject',id='D',itemSubjectRef='tns:I')
    catch=element(p,'intermediateCatchEvent',id='CATCH')
    element(catch,'dataOutput',id='EVENT_OUT',itemSubjectRef='tns:I')
    association(catch,'dataOutputAssociation','CATCH_ASSOC',['EVENT_OUT'],'D')
    group=element(catch,'outputSet',id='EVENT_OS');element(group,'dataOutputRefs','EVENT_OUT')
    element(catch,'messageEventDefinition',id='MESSAGE_CATCH')
    throw=element(p,'intermediateThrowEvent',id='THROW')
    element(throw,'dataInput',id='EVENT_IN',itemSubjectRef='tns:I')
    association(throw,'dataInputAssociation','THROW_ASSOC',['D'],'EVENT_IN')
    group=element(throw,'inputSet',id='EVENT_IS');element(group,'dataInputRefs','EVENT_IN')
    element(throw,'messageEventDefinition',id='MESSAGE_THROW')
    return bytes_xml(root)


def compensation_model():
    root=definitions();p=element(root,'process',id='P')
    a=element(p,'task',id='A');element(p,'task',id='B');element(p,'exclusiveGateway',id='G')
    element(p,'task',id='HANDLER',isForCompensation='true')
    boundary=element(p,'boundaryEvent',id='BOUNDARY',attachedToRef='tns:A')
    element(boundary,'compensateEventDefinition',id='BOUNDARY_COMP')
    end=element(p,'endEvent',id='END');element(end,'compensateEventDefinition',id='END_COMP',activityRef='tns:A')
    throw=element(p,'intermediateThrowEvent',id='THROW');element(throw,'compensateEventDefinition',id='THROW_COMP',activityRef='tns:A',waitForCompletion='false')
    sub=element(p,'subProcess',id='SUB')
    element(sub,'task',id='INNER')
    inner_end=element(sub,'endEvent',id='INNER_END');element(inner_end,'compensateEventDefinition',id='INNER_END_COMP',activityRef='tns:INNER')
    handler=element(p,'subProcess',id='EVENT_SUB',triggeredByEvent='true')
    start=element(handler,'startEvent',id='COMP_START');element(start,'compensateEventDefinition',id='COMP_START_DEF')
    end=element(handler,'endEvent',id='COMP_END');element(end,'compensateEventDefinition',id='COMP_END_DEF',activityRef='tns:A')
    # Artifact is after all FlowElements, respecting actual official XSD order.
    element(p,'association',id='HANDLER_LINK',sourceRef='tns:BOUNDARY',targetRef='tns:HANDLER',associationDirection='One')
    return bytes_xml(root)


def by_id(root,sid):
    return root.xpath('//*[@id="'+sid+'"]')[0]


def change(data,fn):
    root=etree.fromstring(data,etree.XMLParser(resolve_entities=False,no_network=True))
    fn(root)
    return bytes_xml(root)


def add_flow_element(root,name,**attributes):
    owner=by_id(root,'P');e=etree.Element('{'+MODEL+'}'+name,**attributes)
    # Process Properties precede FlowElements; Artifacts follow them.
    for index,child in enumerate(owner):
        if child.tag in {'{'+MODEL+'}'+tag for tag in ['association','group','textAnnotation']}:
            owner.insert(index,e);break
    else:owner.append(e)
    return e
