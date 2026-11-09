#!/usr/bin/env python3
"""Audited OMG -> Eclipse namespace mapping and isolated UML2/OCL diagnostics.
The original bytes never change; mapped diagnostics do not certify OMG equivalence.
"""
import argparse,base64,json,os,shutil,subprocess,tempfile
from pathlib import Path
from standards import Invalid,Incomplete,safe_xml,sha,namespace,XMI
ROOT=Path(__file__).resolve().parents[1];JARS=ROOT/'standards/java'
OMG_UML='http://www.omg.org/spec/UML/20131001';ECLIPSE_UML='http://www.eclipse.org/uml2/5.0.0/UML'
SYNTAX_ADAPTERS={
    'OpaqueExpression-only_in_or_return_parameters': {
        'context':'OpaqueExpression',
        'original_body_sha256':'37a7493cd49e89db067d2e3dcb34daf40d65461e1d76820deee75f68dc15c847',
        'original_token':'ParameterDirectionKind::in ',
        'execution_token':"ParameterDirectionKind::_'in' ",
        'basis':'ParameterDirectionKind-in is the normative literal named in; Eclipse quoted-simple-name syntax preserves that literal identity.',
    },
    'Transition-transition_vertices': {
        'context':'Transition',
        'original_body_sha256':'31113c8725cf1b0e4a241f331b36502a2de22275b990ab3520c35257f1eff602',
        'original_token':'let stateMachine =',
        'execution_token':'let stateMachine : StateMachine =',
        'basis':'Normative Transition-containingStateMachine-result has exact return type StateMachine; the query isQuery=true. The let binding and expression remain unchanged.',
    },
}
LIFELINE_RULE='Lifeline-interaction_uses_share_lifeline'
LIFELINE_SOURCE_SHA256='79da3aca775088ee979b72e9bbc16774cfcb4fee0bef79f1c6a4ae23bf72753f'
LIFELINE_CLASSIFIER_RULE='Lifeline-same_classifier'
LIFELINE_CLASSIFIER_SOURCE_SHA256='596379a2f9be5fbce04025106cc1ea79e1ecce7c017588f792c256c7be594567'
UML_PUBLICATION_SHA256='416b57e1933780eb48bd60fe513e031da220c28a521bdd334a366bebc78a463e'
OCL_PUBLICATION_SHA256='b97e46a946418ba3c8db6f33def013e4d8a56ac500cb1bed055fed660977a7ef'

def boolean_semantics_adapter():
    publication=ROOT/'standards/sources/ocl-2.4/OCL-2.4.pdf'
    if not publication.is_file() or sha(publication.read_bytes())!=OCL_PUBLICATION_SHA256:
        raise Incomplete('Boolean semantic adapter normative OCL fingerprint mismatch')
    return {'id':'OCL-2.4-Boolean-four-valued-operations','kind':'typed-standard-library-evaluation-adapter',
            'operations':['and','or','xor','implies','not'],'implementation':'scripts/UmlValidate.java:BooleanEvaluationVisitor',
            'basis':{'file':'standards/sources/ocl-2.4/OCL-2.4.pdf','sha256':OCL_PUBLICATION_SHA256,
                     'url':'https://www.omg.org/spec/OCL/2.4/PDF','clause':'11.5.4 Boolean','pdf_page':178,'printed_page':162},
            'scope':'Only operation owner identity equal to the backend standard Boolean classifier; custom operations delegate to the original evaluator.',
            'literal_ast_scope':'The original eighteen whole expressions plus explicitly grouped pure Boolean literal trees that the installed parser cannot type. The installed parser runs before the bounded fallback; its accepted expressions bypass fallback limits. The fallback accepts only true/false/null/invalid, not, and/or/xor/implies and balanced parentheses; at most one binary operation per grouping level, a nesting guard at 64 and 2048 tokens. Identifiers, strings, conditionals, custom operations and model text are never rewritten.',
            'source_body_preserved':True,'human_acceptance':'pending','official_full_conformance':False}

def lifeline_adapter(row):
    """Use §17.12.17.5 prose to make the published collection RHS executable.

    This is a separately disclosed semantic adaptation. The published OCL is
    ill-typed (Boolean implies Bag(Lifeline)) and uses the peer selector inside
    the enclosing-lifeline selection. The prose explicitly requires existence
    of a common enclosing lifeline, with the same represents and selector.
    """
    body=row['body']
    if row.get('context')!='Lifeline' or sha(body.encode())!=LIFELINE_SOURCE_SHA256:
        raise Incomplete('Lifeline semantic adapter source fingerprint/context mismatch')
    publication=ROOT/'standards/sources/uml-2.5.1/UML-2.5.1.pdf'
    if not publication.is_file() or sha(publication.read_bytes())!=UML_PUBLICATION_SHA256:
        raise Incomplete('Lifeline semantic adapter normative prose fingerprint mismatch')
    marker='peerUses->forAll('
    if body.count(marker)!=1:raise Incomplete('Lifeline semantic adapter quantifier boundary mismatch')
    def common(candidate):
        return '('+candidate+'.represents = self.represents and '+\
            '(if self.selector = null then '+candidate+'.selector = null '+\
            'else if '+candidate+'.selector = null then false '+\
            'else if self.selector.oclIsKindOf(LiteralString) then '+\
            'if '+candidate+'.selector.oclIsKindOf(LiteralString) then '+\
            'self.selector.oclAsType(LiteralString).value = '+candidate+'.selector.oclAsType(LiteralString).value else false endif '+\
            'else if self.selector.oclIsKindOf(LiteralInteger) then '+\
            'if '+candidate+'.selector.oclIsKindOf(LiteralInteger) then '+\
            'self.selector.oclAsType(LiteralInteger).value = '+candidate+'.selector.oclAsType(LiteralInteger).value else false endif '+\
            'else false endif endif endif endif))'
    execution='let intUses : Set(InteractionUse) = interaction.interactionUse in\n'+\
        'intUses->forAll(iuse : InteractionUse |\n'+\
        ' let usingInteraction : Set(Interaction) = iuse.enclosingInteraction->asSet()->union(\n'+\
        '  iuse.enclosingOperand->asSet().combinedFragment->asSet()\n'+\
        '   ->closure(cf : CombinedFragment | cf.enclosingOperand->asSet().combinedFragment->asSet())\n'+\
        '   .enclosingInteraction->asSet()) in\n'+\
        ' let peerUses : Set(InteractionUse) =\n'+\
        '  usingInteraction.fragment->select(oclIsKindOf(InteractionUse))\n'+\
        '   ->collect(f : InteractionFragment | f.oclAsType(InteractionUse))->asSet()->union(\n'+\
        '  usingInteraction.fragment->select(oclIsKindOf(CombinedFragment))\n'+\
        '   ->collect(f : InteractionFragment | f.oclAsType(CombinedFragment))->asSet()\n'+\
        '   ->closure(cf : CombinedFragment | cf.operand.fragment->select(oclIsKindOf(CombinedFragment))\n'+\
        '    ->collect(f : InteractionFragment | f.oclAsType(CombinedFragment))->asSet())\n'+\
        '   .operand.fragment->select(oclIsKindOf(InteractionUse))\n'+\
        '   ->collect(f : InteractionFragment | f.oclAsType(InteractionUse))->asSet())->excluding(iuse) in\n'+\
        'peerUses->forAll(peerUse : InteractionUse |\n'+\
        ' peerUse.refersTo.lifeline->forAll(peer : Lifeline |\n'+\
        '  '+common('peer')+' implies\n'+\
        '  usingInteraction.lifeline->exists(enclosing : Lifeline | '+common('enclosing')+')\n'+\
        ' ))\n)'
    return execution,{'id':LIFELINE_RULE,'context':'Lifeline','kind':'normative-prose-semantic-adapter',
        'status':'applied-to-execution-body','original_body':body,'original_body_sha256':LIFELINE_SOURCE_SHA256,
        'execution_body':execution,'execution_body_sha256':sha(execution.encode()),'source_body_preserved':True,
        'basis':{'file':'standards/sources/uml-2.5.1/UML-2.5.1.pdf','sha256':UML_PUBLICATION_SHA256,
                 'url':'https://www.omg.org/spec/UML/2.5.1/PDF','clause':'17.12.17.5 interaction_uses_share_lifeline',
                 'pdf_pages':[664,665],'printed_pages':[622,623],
                 'prose':'It must be common to a lifeline within that enclosing Interaction. By common Lifelines we mean Lifelines with the same selector and represents associations.'},
        'adaptation':'Use the published enclosing/peer-use containment paths, with optional ends lifted to sets and element-wise typed casts; replace collection-valued implication RHS with exists, bind the candidate selector, and compare absent/string/integer selectors symmetrically.',
        'scope':'Standard LiteralString/LiteralInteger/absent selectors; unsupported selector kinds are not accepted as common.',
        'human_acceptance':'pending','official_full_conformance':False}

def lifeline_classifier_adapter(row):
    """Keep the published body and disclose the classifier-ancestry prose rule."""
    body=row['body']
    if row.get('context')!='Lifeline' or sha(body.encode())!=LIFELINE_CLASSIFIER_SOURCE_SHA256:
        raise Incomplete('Lifeline classifier semantic adapter source fingerprint/context mismatch')
    publication=ROOT/'standards/sources/uml-2.5.1/UML-2.5.1.pdf'
    if not publication.is_file() or sha(publication.read_bytes())!=UML_PUBLICATION_SHA256:
        raise Incomplete('Lifeline classifier semantic adapter normative prose fingerprint mismatch')
    # Namespace containment identifies the closest owning Classifier; it is
    # not generalization ancestry. Include the starting namespace explicitly.
    execution="if self.represents = null or self.represents.namespace = null or self.interaction = null or self.interaction._'context' = null then\n"+body+"\nelse\n"+\
        "let namespaces : Set(Namespace) = self.represents.namespace->asSet()->union(self.represents.namespace->asSet()->closure(namespace)) in\n"+\
        "let classifiers : Set(Classifier) = namespaces->select(oclIsKindOf(Classifier))->collect(n : Namespace | n.oclAsType(Classifier))->asSet() in\n"+\
        "let closest : Set(Classifier) = classifiers->select(candidate : Classifier | not classifiers->exists(inner : Classifier |\n"+\
        " inner <> candidate and inner.namespace->asSet()->union(inner.namespace->asSet()->closure(namespace))->includes(candidate))) in\n"+\
        "closest->exists(candidate : Classifier | candidate = self.interaction._'context' or self.interaction._'context'.allParents()->includes(candidate))\nendif"
    return execution,{'id':LIFELINE_CLASSIFIER_RULE,'context':'Lifeline','kind':'normative-prose-semantic-adapter',
        'status':'applied-to-execution-body','original_body':body,'original_body_sha256':LIFELINE_CLASSIFIER_SOURCE_SHA256,
        'execution_body':execution,'execution_body_sha256':sha(execution.encode()),'source_body_preserved':True,
        'basis':{'file':'standards/sources/uml-2.5.1/UML-2.5.1.pdf','sha256':UML_PUBLICATION_SHA256,
            'url':'https://www.omg.org/spec/UML/2.5.1/PDF','clause':'17.12.17.5 same_classifier',
            'pdf_pages':[665],'printed_pages':[623],
            'prose':'The classifier containing the referenced ConnectableElement must be the same classifier, or an ancestor, of the classifier that contains the interaction enclosing this lifeline.'},
        'adaptation':'Find the closest containing Classifier in namespace containment, then compare that classifier with the Interaction context or its generalization ancestors. Namespace containment is not interpreted as inheritance.',
        'scope':'Classifier containment/generalization on resolvable local models; absent represents/namespace/Interaction/context retain the published OCL expression outcome. No global closure or metamodel-source correction.',
        'source_execution_equivalence':'not claimed; native published-body/prose differences are retained and independently tested',
        'human_acceptance':'pending','official_full_conformance':False}

def official_rules():
    source=ROOT/'standards/sources/uml-2.5.1/UML.xmi';xml=safe_xml(source.read_bytes());rows=[]
    for cls in xml.iter('packagedElement'):
        if cls.get('{'+XMI+'}type')!='uml:Class':continue
        for rule in cls.findall('ownedRule'):
            spec=rule.find('specification')
            if spec is not None and spec.findtext('language')=='OCL' and spec.findtext('body'):
                rows.append({'context':cls.get('name'),'id':rule.get('{'+XMI+'}id'),'body':spec.findtext('body')})
    return rows,sha(source.read_bytes())

def execution_rules(rows):
    """Copy source rules, keeping pinned syntax and prose adaptations separate."""
    executable=[];adapters=[];seen=set()
    for row in rows:
        item=dict(row);config=SYNTAX_ADAPTERS.get(row['id'])
        if config:
            body=row['body'];digest=sha(body.encode())
            if row['id'] in seen or row.get('context')!=config['context'] or digest!=config['original_body_sha256']:
                raise Incomplete('UML syntax adapter source fingerprint/context mismatch: '+row['id'])
            if body.count(config['original_token'])!=1:
                raise Incomplete('UML syntax adapter token contract mismatch: '+row['id'])
            seen.add(row['id']);item['body']=body.replace(config['original_token'],config['execution_token'],1)
            adapters.append({'id':row['id'],'context':row['context'],'status':'applied-to-execution-body',
                'kind':'exact-source-syntax-adapter','original_body':body,'execution_body':item['body'],
                'original_body_sha256':digest,'execution_body_sha256':sha(item['body'].encode()),
                'adaptation':config['original_token']+' -> '+config['execution_token'],'basis':config['basis'],
                'source_body_preserved':True,'scope':'Only the pinned rule ID, context and original body bytes; not a full-language equivalence certificate.'})
        if row['id']==LIFELINE_RULE:
            if row['id'] in seen:raise Incomplete('duplicate Lifeline semantic adapter source rule')
            seen.add(row['id']);item['body'],adapter=lifeline_adapter(row);adapters.append(adapter)
        if row['id']==LIFELINE_CLASSIFIER_RULE:
            if row['id'] in seen:raise Incomplete('duplicate Lifeline classifier semantic adapter source rule')
            seen.add(row['id']);item['body'],adapter=lifeline_classifier_adapter(row);adapters.append(adapter)
        executable.append(item)
    required=set(SYNTAX_ADAPTERS)|{LIFELINE_RULE,LIFELINE_CLASSIFIER_RULE}
    if seen!=required:
        raise Incomplete('UML adapter pinned rule missing: '+', '.join(sorted(required-seen)))
    return executable,adapters

def official_query_adapters():
    """Expose the missing standard multiplicity query, retaining its source body.

    Its normative bodyCondition uniquely defines Boolean result. The executable
    definition uses that equality's RHS; equivalence is tested independently.
    """
    source=ROOT/'standards/sources/uml-2.5.1/UML.xmi';xml=safe_xml(source.read_bytes())
    for operation in xml.iter('ownedOperation'):
        if operation.get('{'+XMI+'}id')!='MultiplicityElement-is':continue
        body=operation.findtext('ownedRule/specification/body')
        if not body or not body.startswith('result = '):raise Incomplete('normative multiplicity query changed; adapter review required')
        return [{'context':'MultiplicityElement','id':'MultiplicityElement-is','original_body':body,
                 'source_constraint_role':'operation-body-condition',
                 'original_body_sha256':sha(body.encode()),'definition':'is(lowerbound : Integer, upperbound : Integer) : Boolean = '+body[len('result = '):],
                 'adaptation':'finite Integer argument overload for the standard UnlimitedNatural query; functional Boolean bodyCondition RHS unchanged; unlimited bounds remain on the metamodel operation',
                 'scope':'finite Integer arguments only; adapter equivalence and unlimited-bound execution not certified','independent_acceptance':'pending'}]
    raise Incomplete('normative multiplicity query missing')

def validate_mapped(data,java_home=None):
    xml=safe_xml(data)
    if namespace(xml.tag) not in (OMG_UML,XMI):raise Invalid('explicit OMG UML 2.5.1 namespace required')
    # No native/profile package resolution here: even lawful references stay blocked
    # rather than enabling a network or arbitrary local-file resource loader.
    if any(k.split('}')[-1]=='href' and v.partition('#')[0] for e in xml.iter() if isinstance(e.tag,str) for k,v in e.attrib.items()):raise Incomplete('mapped backend forbids external href resolution')
    manifest=json.loads((JARS/'manifest.json').read_text())
    for row in manifest:
        p=JARS/row['file']
        if not p.is_file() or sha(p.read_bytes())!=row['sha256']:raise Incomplete('Java dependency hash mismatch: '+row['file'])
    home=Path(java_home or os.environ.get('JAVA_HOME',''))
    java=str(home/'bin/java') if (home/'bin/java').is_file() else shutil.which('java')
    if not java:raise Incomplete('Java21 unavailable; pass --java-home or JAVA_HOME')
    rules,source_sha=official_rules();executable,syntax_adapters=execution_rules(rules);queries=official_query_adapters();boolean_adapter=boolean_semantics_adapter()
    # Map namespace declarations and Clark tags only through a serialized copy.
    # In contrast to byte.replace, this does not rewrite business string literals.
    from lxml import etree
    mapping={OMG_UML:ECLIPSE_UML,XMI:'http://www.omg.org/XMI'}
    def mapped(e):
        if not isinstance(e.tag,str):return __import__('copy').deepcopy(e)
        tag=e.tag
        for a,b in mapping.items():tag=tag.replace('{'+a+'}','{'+b+'}')
        n=etree.Element(tag,nsmap={k:mapping.get(v,v) for k,v in e.nsmap.items()} if e is xml else None)
        for k,v in e.attrib.items():
            for a,b in mapping.items():k=k.replace('{'+a+'}','{'+b+'}')
            n.set(k,v)
        n.text=e.text;n.tail=e.tail
        for c in e:n.append(mapped(c))
        return n
    copy=etree.tostring(mapped(xml),xml_declaration=True,encoding='UTF-8')
    with tempfile.TemporaryDirectory(prefix='uml-mapped-') as tmp:
        tmp=Path(tmp);p=tmp/'input.uml';p.write_bytes(copy);tsv=tmp/'rules.tsv'
        tsv.write_text('\n'.join('\t'.join(base64.b64encode(r[k].encode()).decode() for k in ('context','id','body')) for r in executable)+'\n')
        query_tsv=tmp/'queries.tsv';query_tsv.write_text('\n'.join('\t'.join(base64.b64encode(r[k].encode()).decode() for k in ('context','id','definition')) for r in queries)+'\n')
        result=subprocess.run([java,'-Xmx512m','--class-path',str(JARS/'*'),str(ROOT/'scripts/UmlValidate.java'),str(p),str(tsv),str(JARS),str(query_tsv)],capture_output=True,text=True,timeout=120)
        if result.returncode:raise Incomplete('mapped UML2/OCL backend failed: '+result.stderr[-4000:])
        report=json.loads(result.stdout)
    report.update(original_sha256=sha(data),mapped_sha256=sha(copy),namespace_mapping=mapping,original_bytes_preserved=True,normative_ocl_source_sha256=source_sha,normative_ocl_rule_count=len(rules),query_adapters=queries,syntax_adapters=[a for a in syntax_adapters if a['kind']=='exact-source-syntax-adapter'],semantic_adapters=[a for a in syntax_adapters if a['kind']=='normative-prose-semantic-adapter'],boolean_operation_adapter=boolean_adapter,dependency_manifest_sha256=sha((JARS/'manifest.json').read_bytes()),mapping_equivalence='explicit adapter, not independently certified',conformance_status='incomplete',value_semantics={'outcomes':['true','false','null','invalid','non-boolean'],'null_is_false':False,'null_is_invalid':False,'boolean_null_operation_equivalence':'typed OCL 2.4 Boolean operation adapter; full-language equivalence not certified'})
    from uml_ocl_obligations import execution_inventory
    report['normative_ocl_execution_scope']=execution_inventory()['summary']
    return report

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--java-home',type=Path);a=p.parse_args()
    try:
        report=validate_mapped(a.input.read_bytes(),a.java_home);a.out.parent.mkdir(parents=True,exist_ok=True)
        with a.out.open('x') as f:json.dump(report,f,ensure_ascii=False,indent=2)
        print(json.dumps({k:report[k] for k in ('loaded_objects','ocl_parsed','ocl_unmapped','ocl_evaluations','conformance_status')}));return 3
    except (Invalid,Incomplete,subprocess.TimeoutExpired) as e:print(str(e));return 3
if __name__=='__main__':raise SystemExit(main())
