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
    """Copy source rules, applying only two fingerprint-pinned syntax adapters.

    The source bodies remain authoritative. Lifeline's ill-typed constraint is
    deliberately not interpreted here; parsing is not normative certification.
    """
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
        executable.append(item)
    if seen!=set(SYNTAX_ADAPTERS):
        raise Incomplete('UML syntax adapter pinned rule missing: '+', '.join(sorted(set(SYNTAX_ADAPTERS)-seen)))
    return executable,adapters

def official_query_adapters():
    """Expose the missing standard multiplicity query, retaining its source body.

    Its normative postcondition uniquely defines Boolean result. The executable
    definition uses that equality's RHS; equivalence is tested independently.
    """
    source=ROOT/'standards/sources/uml-2.5.1/UML.xmi';xml=safe_xml(source.read_bytes())
    for operation in xml.iter('ownedOperation'):
        if operation.get('{'+XMI+'}id')!='MultiplicityElement-is':continue
        body=operation.findtext('ownedRule/specification/body')
        if not body or not body.startswith('result = '):raise Incomplete('normative multiplicity query changed; adapter review required')
        return [{'context':'MultiplicityElement','id':'MultiplicityElement-is','original_body':body,
                 'original_body_sha256':sha(body.encode()),'definition':'is(lowerbound : Integer, upperbound : Integer) : Boolean = '+body[len('result = '):],
                 'adaptation':'finite Integer argument overload for the standard UnlimitedNatural query; functional Boolean postcondition RHS unchanged; unlimited bounds remain on the metamodel operation',
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
    rules,source_sha=official_rules();executable,syntax_adapters=execution_rules(rules);queries=official_query_adapters()
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
    report.update(original_sha256=sha(data),mapped_sha256=sha(copy),namespace_mapping=mapping,original_bytes_preserved=True,normative_ocl_source_sha256=source_sha,normative_ocl_rule_count=len(rules),query_adapters=queries,syntax_adapters=syntax_adapters,dependency_manifest_sha256=sha((JARS/'manifest.json').read_bytes()),mapping_equivalence='explicit adapter, not independently certified',conformance_status='incomplete')
    return report

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--java-home',type=Path);a=p.parse_args()
    try:
        report=validate_mapped(a.input.read_bytes(),a.java_home);a.out.parent.mkdir(parents=True,exist_ok=True)
        with a.out.open('x') as f:json.dump(report,f,ensure_ascii=False,indent=2)
        print(json.dumps({k:report[k] for k in ('loaded_objects','ocl_parsed','ocl_unmapped','ocl_evaluations','conformance_status')}));return 3
    except (Invalid,Incomplete,subprocess.TimeoutExpired) as e:print(str(e));return 3
if __name__=='__main__':raise SystemExit(main())
