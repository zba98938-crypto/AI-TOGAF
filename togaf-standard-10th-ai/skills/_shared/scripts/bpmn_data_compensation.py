"""Source-bound BPMN Data/IO and compensation design-time constraints.

Types come from the acquired official CMOF, not from an implementation allowlist.
Expressions, process execution and implicit compensation adapters are not invented.
"""
import hashlib
from pathlib import Path
from lxml import etree
from bpmn_references import local_id, local_reference

BPMN = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
PDF_SHA256 = 'd3d9258a70bf808c11ac52becea4ce645540a8b881117535f60a56fbf13e22f2'
CMOF_SHA256 = '72f5bf035da7bea80dc53131a22e6ba466789abd7437532e64abd3a7cff20139'
XSD_SHA256 = 'c4318842f7d2bbc262d7954c9452c501db16f0868eac0b8732ec5d7fb384d9a7'
META_PATH = Path(__file__).resolve().parents[1]/'standards/sources/bpmn-2.0.2/BPMN20.cmof'
SCHEMA_PATH = META_PATH.with_name('Semantic.xsd')
RULES = {
    'mi-initialization': ('10.3.8 Table 10.29', [220,221], ['MultiInstanceLoopCharacteristics-loopCardinality', 'MultiInstanceLoopCharacteristics-loopDataInputRef']),
    'mi-loop-reference-type': ('10.3.8 Table 10.29', [221], ['MultiInstanceLoopCharacteristics-loopDataInputRef', 'MultiInstanceLoopCharacteristics-loopDataOutputRef']),
    'mi-loop-reference-scope': ('10.3.8 Table 10.29 and Data lifecycle', [221,236,240], ['MultiInstanceLoopCharacteristics-loopDataInputRef', 'MultiInstanceLoopCharacteristics-loopDataOutputRef']),
    'mi-loop-collection': ('10.3.8 Table 10.29', [220,221], ['MultiInstanceLoopCharacteristics-loopDataInputRef', 'MultiInstanceLoopCharacteristics-loopDataOutputRef']),
    'mi-data-item-scalar': ('10.3.8 Table 10.29', [221], ['MultiInstanceLoopCharacteristics-inputDataItem', 'MultiInstanceLoopCharacteristics-outputDataItem']),
    'mi-behavior-event-type': ('10.3.8 Table 10.29', [222], ['MultiInstanceLoopCharacteristics-oneBehaviorEventRef', 'MultiInstanceLoopCharacteristics-noneBehaviorEventRef']),
    'data-association-type': ('10.3 DataAssociation, Table 10.63', [252], ['DataAssociation-sourceRef', 'DataAssociation-targetRef']),
    'data-association-direction': ('10.3 DataInputAssociation/DataOutputAssociation', [252,253], ['DataInputAssociation', 'DataOutputAssociation', 'Activity-dataInputAssociations', 'Activity-dataOutputAssociations']),
    'data-association-source-cardinality': ('10.3 DataAssociation copying/transformation', [251,252], ['DataAssociation-sourceRef', 'DataAssociation-transformation']),
    'data-association-scope': ('10.3 Lifecycle/Accessibility and association scope', [236,237,239,240,252,253], ['DataAssociation-sourceRef', 'DataAssociation-targetRef']),
    'data-item-subject-type': ('ItemAwareElement and DataAssociation type', [250,252], ['ItemAwareElement-itemSubjectRef']),
    'data-item-collection': ('Tables 10.52/10.59/10.60', [235,244,246], ['DataObject-isCollection', 'DataInput-isCollection', 'DataOutput-isCollection']),
    'data-association-item-definition': ('10.3 DataAssociation ItemDefinition compatibility', [250], ['DataAssociation-transformation', 'ItemAwareElement-itemSubjectRef']),
    'data-reference-type': ('Tables 10.53/10.56', [235,238], ['DataObjectReference-dataObjectRef', 'DataStoreReference-dataStoreRef']),
    'data-reference-item-definition': ('10.3 DataObjectReference semantic restriction', [234], ['DataObjectReference', 'ItemAwareElement-itemSubjectRef']),
    'data-object-containment': ('10.3 DataObject containment and lifecycle', [234,236], ['DataObject']),
    'property-containment': ('10.3 Properties', [238,239], ['Property']),
    'embedded-subprocess-io': ('10.3 InputOutputSpecification applicability', [240], ['SubProcess', 'Activity-ioSpecification']),
    'io-set-reference-type': ('Tables 10.61/10.62', [248,250], ['InputSet-dataInputRefs', 'OutputSet-dataOutputRefs']),
    'io-set-reference-scope': ('InputOutputSpecification and set associations', [247,248,250], ['InputSet-outputSetRefs', 'OutputSet-inputSetRefs']),
    'io-set-subset': ('Tables 10.61/10.62 subset requirements', [248,250], ['InputSet-optionalInputRefs', 'InputSet-whileExecutingInputRefs', 'OutputSet-optionalOutputRefs', 'OutputSet-whileExecutingOutputRefs']),
    'io-set-membership': ('DataInput/Output set membership', [244,246,247,248], ['DataInput-inputSetRefs', 'DataOutput-outputSetRefs']),
    'compensation-start-scope': ('10.6 Compensation Event', [292], ['CompensateEventDefinition']),
    'compensation-catch-placement': ('10.6 Compensation Event', [292], ['CompensateEventDefinition']),
    'compensation-boundary-flow': ('10.6 Intermediate Event SequenceFlow exceptions', [288], ['CompensateEventDefinition']),
    'compensation-activity-reference-type': ('Table 10.94', [293], ['CompensateEventDefinition-activityRef']),
    'compensation-activity-visibility': ('Tables 10.88/10.89 Compensation target visibility', [277,281], ['CompensateEventDefinition-activityRef']),
}
ADAPTATIONS = [
    {'element':'DataObjectReference.itemSubjectRef', 'normative_text':'PDF physical234: DataObjectReference cannot specify ItemDefinitions.',
     'official_exchange':'Inherited ItemAwareElement field remains representable in CMOF/XSD.',
     'execution':'Reject explicit declarations on references; resolve effective ItemDefinition through dataObjectRef. Preserve original invalid XML bytes.'},
    {'element':'DataOutputAssociation.direction', 'normative_text':'PDF physical244 direction wording conflicts with the explicit association definition on physical253.',
     'official_exchange':'DataOutputAssociation inherits sourceRef/targetRef ItemAwareElement references.',
     'execution':'Apply physical253: owned Activity/Event output as source, accessible item as target; do not reverse the model from physical244 wording.'},
    {'element':'SubProcess.compensable', 'normative_text':'PDF physical333 mentions compensable for implicit default compensation.',
     'official_exchange':'Present official BPMN20.cmof/Semantic.xsd SubProcess expose no compensable property.',
     'execution':'No synthetic compensable attribute and no blanket explicit-handler requirement. Default-compensation representation remains unadjudicated.'},
    {'element':'DataObject.dataState', 'normative_text':'PDF physical234 forbids DataObject state, physical235 permits DataState.',
     'official_exchange':'ItemAwareElement inherits an optional dataState containment.',
     'execution':'Retain both texts; do not impose a blanket DataState rejection before source adjudication.'},
]


def _metamodel():
    raw = META_PATH.read_bytes()
    if hashlib.sha256(raw).hexdigest() != CMOF_SHA256:
        raise ValueError('BPMN20.cmof fingerprint conflict')
    root = etree.fromstring(raw, etree.XMLParser(no_network=True, resolve_entities=False))
    # Official exchange wraps the Package in xmi:XMI; classes are Package
    # ownedMember children, not direct XMI children.
    xmi_type = '{http://schema.omg.org/spec/XMI/2.1}type'
    classes = {e.get('name'):e for e in root.iter() if e.get('name') and
               e.get(xmi_type)=='cmof:Class'}
    graph = {name:set(e.get('superClass','').split()) for name,e in classes.items()}
    required = {'Activity','Task','SubProcess','Process','CallableElement',
                'FlowElementsContainer','Event','CatchEvent','ThrowEvent',
                'EventDefinition','CompensateEventDefinition','ItemAwareElement',
                'ItemDefinition','DataInput','DataOutput','DataObject','Property',
                'DataStore','InputSet','OutputSet'}
    if required - graph.keys():
        raise ValueError('BPMN20.cmof required classes unavailable: '+', '.join(sorted(required-graph.keys())))
    unresolved = {parent for parents in graph.values() for parent in parents if parent not in graph}
    if unresolved:
        raise ValueError('BPMN20.cmof superclass unavailable: '+', '.join(sorted(unresolved)))
    def subtype(name, base, visited=()):
        if name == base:
            return True
        if name in visited or name not in graph:
            return False
        return any(subtype(parent,base,visited+(name,)) for parent in graph[name])
    return subtype, graph


def _exchange_types(subtype, graph):
    """Join declared XSD type names to CMOF classes and scoped role types.

    BPMN's official exchange declares complex types named t<ClassName>. The
    join uses those actual declarations, never XML-tag capitalization. Local
    element declarations override globals only in their declared owner type;
    every class-valued local role must match a composite CMOF property.
    """
    parser = etree.XMLParser(no_network=True, resolve_entities=False)
    schema_raw = SCHEMA_PATH.read_bytes()
    if hashlib.sha256(schema_raw).hexdigest() != XSD_SHA256:
        raise ValueError('Semantic.xsd fingerprint conflict')
    schema = etree.fromstring(schema_raw, parser)
    meta_raw = META_PATH.read_bytes()
    if hashlib.sha256(meta_raw).hexdigest() != CMOF_SHA256:
        raise ValueError('BPMN20.cmof fingerprint conflict')
    meta = etree.fromstring(meta_raw, parser)
    xmi = '{http://schema.omg.org/spec/XMI/2.1}'
    xs = '{http://www.w3.org/2001/XMLSchema}'
    complex_types = {e.get('name'):e for e in schema.findall(xs+'complexType')}
    declared_types = {'t'+name:name for name in graph if 't'+name in complex_types}
    classes = {e.get('name'):e for e in meta.iter() if e.get(xmi+'type')=='cmof:Class' and e.get('name')}
    globals = {e.get('name'):declared_types[e.get('type')]
               for e in schema.findall(xs+'element') if e.get('type') in declared_types}
    roles, audit = {}, []
    for type_name, owner in declared_types.items():
        for declaration in complex_types[type_name].iter(xs+'element'):
            role, target = declaration.get('name'), declared_types.get(declaration.get('type'))
            if not role or target is None:
                continue  # Primitive/QName values are references, not objects.
            prop = classes[owner].find('ownedAttribute[@name="'+role+'"]')
            if prop is None or prop.get('type')!=target or prop.get('isComposite')!='true':
                raise ValueError('BPMN exchange containment role/type conflict: '+owner+'.'+role+' -> '+target)
            roles[owner,role] = target
            audit.append({'owner_class':owner,'role':role,'schema_type':declaration.get('type'),
                          'model_class':target,'cmof_native_id':prop.get(xmi+'id'),
                          'cmof_locator':meta.getroottree().getpath(prop),
                          'xsd_locator':schema.getroottree().getpath(declaration),
                          'global_class':globals.get(role),'containment_cross_checked':True})
    required = {('MultiInstanceLoopCharacteristics','inputDataItem'):'DataInput',
                ('MultiInstanceLoopCharacteristics','outputDataItem'):'DataOutput'}
    if any(roles.get(key)!=value for key,value in required.items()):
        raise ValueError('BPMN exchange required MultiInstance data role declarations unavailable')

    def model_class(element):
        if element is None or not isinstance(element.tag,str) or not element.tag.startswith('{'+BPMN+'}'):
            return None
        name = element.tag.split('}')[-1]
        parent_class = model_class(element.getparent())
        matching = {target for (owner,role),target in roles.items()
                    if role==name and subtype(parent_class,owner)}
        if len(matching)>1:
            raise ValueError('BPMN exchange ambiguous containment role: '+str(parent_class)+'.'+name)
        declared = next(iter(matching)) if matching else globals.get(name)
        # QName-valued xsi:type may specialize the declared class. Unknown or
        # incompatible types belong to schema validation, not a tag heuristic.
        explicit = element.get('{http://www.w3.org/2001/XMLSchema-instance}type')
        if explicit:
            prefix,separator,type_name = explicit.partition(':')
            namespace = element.nsmap.get(prefix) if separator else element.nsmap.get(None)
            type_name = type_name if separator else prefix
            specialized = declared_types.get(type_name) if namespace==BPMN else None
            return specialized if specialized and declared and subtype(specialized,declared) else None
        return declared

    return model_class, {'schema_file':'Semantic.xsd','schema_sha256':XSD_SHA256,
                         'cmof_sha256':CMOF_SHA256,'global_element_count':len(globals),
                         'local_roles':audit,'mapping':'declared XSD t<ClassName> joined to official CMOF class; scoped composite roles override globals',
                         'unmapped_complex_types':sorted(set(complex_types)-set(declared_types))}


def check(root):
    findings, uncovered = [], []
    basis = {key:{'pdf_sha256':PDF_SHA256,'section':section,'physical_pages':pages,
                  'machine_source':{'file':'BPMN20.cmof','sha256':CMOF_SHA256,'native_ids':ids},
                  'exchange_type_source':{'file':'Semantic.xsd','sha256':XSD_SHA256}}
             for key,(section,pages,ids) in RULES.items()}
    try:
        subtype, graph = _metamodel()
        model_class, type_audit = _exchange_types(subtype, graph)
    except (OSError,ValueError,etree.XMLSyntaxError) as exc:
        return {'implemented_rule_ids':list(RULES),'findings':[], 'normative_rule_basis':basis,
                'capability_uncovered':['material missing: trusted BPMN Data/Comp metamodel unavailable: '+str(exc)],
                'source_status':'unusable','exchange_adaptations':ADAPTATIONS,'full_design_time_semantics':'incomplete'}
    q = lambda name:'{'+BPMN+'}'+name
    def kind(e):
        return e.tag.split('}')[-1] if e is not None and isinstance(e.tag,str) else ''
    def native(e):
        return e is not None and isinstance(e.tag,str) and e.tag.startswith('{'+BPMN+'}')
    def is_type(e, base):
        return subtype(model_class(e),base)
    nodes = {local_id(e.get('id')):e for e in root.iter() if e.get('id') and isinstance(e.tag,str)}
    def reference(owner, value):
        identity, problem = local_reference(owner,value,root.get('targetNamespace'))
        return nodes.get(identity), problem
    def resolved(owner, value):
        return reference(owner,value)[0]
    def children_refs(e, name):
        return [(child,*reference(child,child.text)) for child in e.findall(q(name))]
    def issue(rule,e,message,context=None):
        row={'rule_id':rule,'id':e.get('id'),'message':message,
             'source_locator':root.getroottree().getpath(e),'normative_source':basis[rule]}
        if context is not None:
            row['model_context_locator']=root.getroottree().getpath(context)
        findings.append(row)
    def typed(e,base,rule,context):
        if e is None:
            return False
        if not native(e):
            uncovered.append('BPMN '+base+' reference type to vendor element remains unverified: '+str(e.get('id')))
            return False
        if not is_type(e,base):
            issue(rule,context,'resolved reference must identify '+base+', not '+kind(e))
            return False
        return True
    def ancestor(e,owner):
        return e is owner or any(p is owner for p in e.iterancestors())
    def flow_scope(e):
        return next((p for p in e.iterancestors() if is_type(p,'FlowElementsContainer')),None)
    def data_owner(e):
        return next((p for p in e.iterancestors() if is_type(p,'Activity') or is_type(p,'CallableElement') or is_type(p,'Event')),None)
    def effective_item(e,seen=()):
        if e is None or e in seen:
            return None
        if kind(e)=='dataObjectReference':
            return effective_item(resolved(e,e.get('dataObjectRef')),seen+(e,))
        if e.get('itemSubjectRef'):
            return resolved(e,e.get('itemSubjectRef'))
        if kind(e)=='dataStoreReference':
            return effective_item(resolved(e,e.get('dataStoreRef')),seen+(e,))
        return None
    def visible(e,accessor):
        if kind(e)=='dataObjectReference':
            target=resolved(e,e.get('dataObjectRef'))
            return visible(target,accessor) if is_type(target,'DataObject') else True
        if kind(e)=='dataObject':
            return ancestor(accessor,e.getparent())
        if kind(e)=='property':
            owner=e.getparent()
            return ancestor(accessor,owner) if is_type(owner,'Process') or is_type(owner,'SubProcess') else accessor is owner
        if is_type(e,'DataInput') or is_type(e,'DataOutput'):
            owner=data_owner(e)
            return owner is not None and ancestor(accessor,owner)
        return True
    def boolean(e,name):
        value=e.get(name,'false').strip()
        return True if value in {'true','1'} else False if value in {'false','0'} else None

    for e in root.iter():
        if not native(e):
            continue
        k=kind(e)
        if is_type(e,'ItemAwareElement') and e.get('itemSubjectRef'):
            typed(resolved(e,e.get('itemSubjectRef')),'ItemDefinition','data-item-subject-type',e)
        if k in {'dataObjectReference','dataStoreReference'}:
            field,base=('dataObjectRef','DataObject') if k=='dataObjectReference' else ('dataStoreRef','DataStore')
            if e.get(field):
                typed(resolved(e,e.get(field)),base,'data-reference-type',e)
            if k=='dataObjectReference' and e.get('itemSubjectRef') is not None:
                issue('data-reference-item-definition',e,'DataObjectReference cannot declare an ItemDefinition; it reuses the referenced DataObject definition')
            if not visible(e,e):
                issue('data-association-scope',e,'DataObjectReference cannot access a DataObject outside its guaranteed lifecycle scope')
        if k=='dataObject' and not (is_type(e.getparent(),'Process') or is_type(e.getparent(),'SubProcess')):
            issue('data-object-containment',e,'DataObject must be contained in Process or SubProcess')
        if k=='property' and not any(is_type(e.getparent(),base) for base in ('Process','Activity','Event')):
            issue('property-containment',e,'Property must be contained in Process, Activity or Event')
        if any(is_type(e,base) for base in ('DataObject','DataInput','DataOutput')):
            item=effective_item(e)
            if is_type(item,'ItemDefinition') and boolean(item,'isCollection') is not None and boolean(e,'isCollection') is not None:
                if boolean(item,'isCollection') != boolean(e,'isCollection'):
                    issue('data-item-collection',e,'isCollection must match the referenced ItemDefinition including false defaults')
        if k=='ioSpecification' and is_type(e.getparent(),'SubProcess') and any(kind(c) in {'dataInput','dataOutput'} for c in e):
            issue('embedded-subprocess-io',e,'embedded SubProcess cannot define DataInputs/DataOutputs directly; MultiInstanceLoopCharacteristics is separate')
        if k not in {'dataInputAssociation','dataOutputAssociation'}:
            continue
        owner=e.getparent()
        sources=children_refs(e,'sourceRef')
        target_ref=e.find(q('targetRef'))
        target=resolved(target_ref,target_ref.text) if target_ref is not None else None
        transformation=e.find(q('transformation'))
        if transformation is None and len(sources)!=1:
            issue('data-association-source-cardinality',e,'without transformation exactly one sourceRef is required')
        if not (is_type(owner,'Activity') or is_type(owner,'Event')):
            issue('data-association-direction',e,'DataAssociation must be contained by Activity or Event')
        for child,source,problem in sources:
            if typed(source,'ItemAwareElement','data-association-type',child) and not visible(source,owner):
                issue('data-association-scope',child,'source ItemAwareElement is not accessible in the association scope')
            if k=='dataOutputAssociation' and source is not None and native(source):
                if not is_type(source,'DataOutput') or data_owner(source) is not owner:
                    issue('data-association-direction',child,'DataOutputAssociation source must be a DataOutput owned by its Activity/catch Event')
        if target_ref is not None and typed(target,'ItemAwareElement','data-association-type',target_ref) and not visible(target,owner):
            issue('data-association-scope',target_ref,'target ItemAwareElement is not accessible in the association scope')
        if k=='dataInputAssociation' and target is not None and native(target):
            if not is_type(target,'DataInput') or data_owner(target) is not owner:
                issue('data-association-direction',target_ref,'DataInputAssociation target must be a DataInput owned by its Activity/throw Event')
        target_item=effective_item(target)
        if transformation is None and is_type(target_item,'ItemDefinition'):
            for child,source,problem in sources:
                item=effective_item(source)
                if is_type(item,'ItemDefinition') and item is not target_item:
                    issue('data-association-item-definition',e,'differing identified source and target ItemDefinitions require transformation')

    # MI collection roles are outer interface data; contained input/output items
    # are scalar inner-instance data. Opaque expressions remain non-executable.
    mi_unverified = []
    for loop in root.iter(q('multiInstanceLoopCharacteristics')):
        owner = loop.getparent()
        input_ref = loop.find(q('loopDataInputRef'))
        if loop.find(q('loopCardinality')) is None and input_ref is None:
            issue('mi-initialization',loop,'valid MultiInstance requires loopCardinality or loopDataInputRef')
        if loop.find(q('loopCardinality')) is not None:
            mi_unverified.append({'id':loop.get('id'),'obligation':'loopCardinality evaluates to integer','status':'uncovered: opaque expression is retained, never executed'})
        for direction in ('Input','Output'):
            child = loop.find(q('loopData'+direction+'Ref'))
            target = resolved(child,child.text) if child is not None else None
            if child is not None and typed(target,'ItemAwareElement','mi-loop-reference-type',child):
                if is_type(owner,'Task'):
                    if not is_type(target,'Data'+direction):
                        issue('mi-loop-reference-type',child,'Task MI loop reference must identify Data'+direction)
                    elif kind(target.getparent())!='ioSpecification' or target.getparent().getparent() is not owner:
                        issue('mi-loop-reference-scope',child,'Task MI loop data must belong to the same Activity InputOutputSpecification')
                elif is_type(owner,'SubProcess'):
                    if not is_type(target,'DataObject'):
                        issue('mi-loop-reference-type',child,'SubProcess MI loop reference must identify a DataObject')
                    elif not visible(target,owner):
                        issue('mi-loop-reference-scope',child,'SubProcess MI collection DataObject is outside visible lifecycle scope')
                else:
                    mi_unverified.append({'id':loop.get('id'),'obligation':'MI owner-specific loop reference semantics for '+kind(owner),'status':'uncovered'})
                item = effective_item(target)
                if boolean(target,'isCollection') is False or is_type(item,'ItemDefinition') and boolean(item,'isCollection') is False:
                    issue('mi-loop-collection',child,'MI loop data must be collection-valued')
            data_item = loop.find(q(direction.lower()+'DataItem'))
            if data_item is not None:
                item = effective_item(data_item)
                if boolean(data_item,'isCollection') is True or is_type(item,'ItemDefinition') and boolean(item,'isCollection') is True:
                    issue('mi-data-item-scalar',data_item,'MI instance data item must be scalar, not a collection')
                # CMOF exposes no scalar-of relationship. Equality of external
                # structureRef strings would not prove semantic scalarization.
                mi_unverified.append({'id':data_item.get('id'),'obligation':'scalar type of corresponding loopData'+direction,
                                      'status':'uncovered: external ItemDefinition structure scalarization is not adjudicated'})
        for field in ('oneBehaviorEventRef','noneBehaviorEventRef'):
            if loop.get(field):
                typed(resolved(loop,loop.get(field)),'EventDefinition','mi-behavior-event-type',loop)
        if loop.find(q('completionCondition')) is not None or loop.findall(q('complexBehaviorDefinition')):
            mi_unverified.append({'id':loop.get('id'),'obligation':'boolean expression result/type and Complex behavior event selection',
                                  'status':'uncovered: expressions and optional event/default behavior remain preserved without execution'})

    # Event sets have direct containment; IOSpecification sets have shared ownership.
    for owner in root.iter():
        if not native(owner) or kind(owner) not in {'ioSpecification','startEvent','endEvent','boundaryEvent','intermediateCatchEvent','intermediateThrowEvent','implicitThrowEvent'}:
            continue
        for direction,opposite in [('Input','Output'),('Output','Input')]:
            tag=direction[0].lower()+direction[1:]
            main='data'+direction+'Refs'
            sets=owner.findall(q(tag+'Set'))
            declared=owner.findall(q('data'+direction))
            covered=set();uncertain=False
            for group in sets:
                main_refs=children_refs(group,main)
                valid=set()
                for child,target,problem in main_refs:
                    uncertain=uncertain or bool(problem) or target is None
                    if typed(target,'Data'+direction,'io-set-reference-type',child):
                        if target.getparent() is not owner:
                            issue('io-set-reference-scope',child,'set data reference must belong to the same IO specification/Event')
                        else:
                            valid.add(target);covered.add(target)
                for field in ['optional'+direction+'Refs','whileExecuting'+direction+'Refs']:
                    for child,target,problem in children_refs(group,field):
                        if typed(target,'Data'+direction,'io-set-reference-type',child):
                            if target.getparent() is not owner:
                                issue('io-set-reference-scope',child,'subset reference belongs to another IO specification/Event')
                            if not any(p for _,_,p in main_refs) and target not in valid:
                                issue('io-set-subset',child,'optional/while-executing references must be listed in the main data refs')
                paired=opposite[0].lower()+opposite[1:]+'SetRefs'
                for child,target,problem in children_refs(group,paired):
                    if typed(target,opposite+'Set','io-set-reference-type',child) and target.getparent() is not owner:
                        issue('io-set-reference-scope',child,'paired InputSet/OutputSet belongs to another IO specification/Event')
            if not uncertain:
                for item in declared:
                    if item not in covered:
                        issue('io-set-membership',item,'every declared Data'+direction+' must be referenced by at least one corresponding set')

    def definitions(event):
        return [e for e in event if is_type(e,'EventDefinition')] + [target for _,target,_ in children_refs(event,'eventDefinitionRef') if target is not None]
    outgoing={}
    for flow in root.iter(q('sequenceFlow')):
        source=resolved(flow,flow.get('sourceRef'))
        if source is not None:
            outgoing.setdefault(source,[]).append(flow)
    for event in root.iter():
        if not is_type(event,'Event'):
            continue
        comp=[e for e in definitions(event) if is_type(e,'CompensateEventDefinition')]
        if not comp:
            continue
        if kind(event)=='startEvent' and not (is_type(event.getparent(),'SubProcess') and boolean(event.getparent(),'triggeredByEvent')):
            issue('compensation-start-scope',event,'Compensation StartEvent is allowed only in an Event SubProcess')
        if is_type(event,'CatchEvent') and kind(event)!='startEvent' and kind(event)!='boundaryEvent':
            issue('compensation-catch-placement',event,'catching Compensation IntermediateEvent must attach to an Activity boundary')
        if kind(event)=='boundaryEvent' and outgoing.get(event):
            issue('compensation-boundary-flow',event,'boundary CompensationEvent cannot have outgoing SequenceFlow; use Association')
        for definition in comp:
            if not definition.get('activityRef'):
                continue
            target=resolved(definition,definition.get('activityRef'))
            if not typed(target,'Activity','compensation-activity-reference-type',definition):
                continue
            if not is_type(event,'ThrowEvent'):
                continue
            event_scope=flow_scope(event);target_scope=flow_scope(target)
            normal=event_scope is target_scope
            compensating=(is_type(event_scope,'SubProcess') and boolean(event_scope,'triggeredByEvent')
                          and any(kind(child)=='startEvent' and any(is_type(d,'CompensateEventDefinition') for d in definitions(child)) for child in event_scope)
                          and flow_scope(event_scope) is target_scope)
            if not (normal or compensating):
                issue('compensation-activity-visibility',definition,'Activity is not visible from this normal/compensating event-subprocess throw scope',event)
    return {'implemented_rule_ids':list(RULES),'findings':findings,'normative_rule_basis':basis,
            'capability_uncovered':sorted(set(uncovered)), 'source_status':'verified-local-cmof',
            'metamodel_class_count':len(graph),'exchange_adaptations':ADAPTATIONS,
            'exchange_type_audit':type_audit,'mi_unverified_obligations':mi_unverified,
            'full_design_time_semantics':'incomplete','independent_normative_rule_review':'pending'}
