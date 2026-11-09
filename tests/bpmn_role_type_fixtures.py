"""Independent official-exchange MI role fixtures; never inferred from validator."""
from bpmn_data_compensation_fixtures import definitions,element,bytes_xml


def multi_instance_model():
    root=definitions()
    element(root,'itemDefinition',id='SCALAR',isCollection='false')
    element(root,'itemDefinition',id='COLLECTION',isCollection='true')
    process=element(root,'process',id='P')
    element(process,'dataObject',id='LOOP_SOURCE',itemSubjectRef='tns:COLLECTION',isCollection='true')
    element(process,'dataObject',id='LOOP_RESULT',itemSubjectRef='tns:COLLECTION',isCollection='true')
    task=element(process,'subProcess',id='A')
    loop=element(task,'multiInstanceLoopCharacteristics',id='LOOP')
    element(loop,'loopDataInputRef','tns:LOOP_SOURCE')
    element(loop,'loopDataOutputRef','tns:LOOP_RESULT')
    element(loop,'inputDataItem',id='MI_INPUT',itemSubjectRef='tns:SCALAR')
    element(loop,'outputDataItem',id='MI_OUTPUT',itemSubjectRef='tns:SCALAR')
    behavior=element(loop,'complexBehaviorDefinition',id='BEHAVIOR')
    element(behavior,'condition','opaque_boolean_expression()',id='CONDITION',language='urn:fixture-language')
    event=element(behavior,'event',id='IMPLICIT_EVENT')
    element(event,'messageEventDefinition',id='MESSAGE')
    element(loop,'completionCondition','opaque_completion_expression()',id='COMPLETE')
    element(process,'exclusiveGateway',id='G')
    return bytes_xml(root)


# Hand-transcribed class-valued local declarations in the acquired XSD,
# independently matched against official composite CMOF properties.
LOCAL_ROLE_ORACLE = {
    ('AdHocSubProcess','completionCondition'):'Expression',
    ('Assignment','from'):'Expression', ('Assignment','to'):'Expression',
    ('ComplexBehaviorDefinition','condition'):'FormalExpression',
    ('ComplexBehaviorDefinition','event'):'ImplicitThrowEvent',
    ('ComplexGateway','activationCondition'):'Expression',
    ('ConditionalEventDefinition','condition'):'Expression',
    ('CorrelationPropertyBinding','dataPath'):'FormalExpression',
    ('CorrelationPropertyRetrievalExpression','messagePath'):'FormalExpression',
    ('DataAssociation','transformation'):'FormalExpression',
    ('Lane','partitionElement'):'BaseElement', ('Lane','childLaneSet'):'LaneSet',
    ('MultiInstanceLoopCharacteristics','loopCardinality'):'Expression',
    ('MultiInstanceLoopCharacteristics','inputDataItem'):'DataInput',
    ('MultiInstanceLoopCharacteristics','outputDataItem'):'DataOutput',
    ('MultiInstanceLoopCharacteristics','completionCondition'):'Expression',
    ('SequenceFlow','conditionExpression'):'Expression',
    ('StandardLoopCharacteristics','loopCondition'):'Expression',
    ('TimerEventDefinition','timeDate'):'Expression',
    ('TimerEventDefinition','timeDuration'):'Expression',
    ('TimerEventDefinition','timeCycle'):'Expression',
}
