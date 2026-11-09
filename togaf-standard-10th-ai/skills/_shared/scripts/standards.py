#!/usr/bin/env python3
"""Native design-language packages, inventories, secure exchange and honest gates.
0 = requested exchange operation complete, 1 = definite error, 3 = incomplete.
A successful import is NOT full-language conformance or notation certification.
"""
import argparse,base64,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]
SOURCES=ROOT/'standards/sources'
VERSIONS={'bpmn':'2.0.2','uml':'2.5.1','archimate':'4'}
BPMN='http://www.omg.org/spec/BPMN/20100524/MODEL'
XMI='http://www.omg.org/spec/XMI/20131001'
KNOWN={BPMN,'http://www.omg.org/spec/BPMN/20100524/DI','http://www.omg.org/spec/DD/20100524/DI','http://www.omg.org/spec/DD/20100524/DC',XMI,'http://www.omg.org/spec/UML/20131001','http://www.omg.org/spec/UML/20131001/UMLDI','http://www.omg.org/spec/DD/20131001/DI','http://www.omg.org/spec/DD/20131001/DC','http://www.w3.org/2001/XMLSchema-instance'}
class Invalid(ValueError):pass
class Incomplete(RuntimeError):pass

def sha(data):return hashlib.sha256(data).hexdigest()
def safe_xml(data):
    # Lexical rejection precedes parser; never load DTD, entities or network schema.
    if len(data)>64*1024*1024:raise Invalid('native package XML exceeds 64MiB safety limit')
    if re.search(br'<!\s*(DOCTYPE|ENTITY)\b',data,re.I):raise Invalid('DTD/entities are forbidden')
    from lxml import etree
    try:return etree.fromstring(data,etree.XMLParser(resolve_entities=False,no_network=True,load_dtd=False,huge_tree=False))
    except etree.XMLSyntaxError as exc:raise Invalid(str(exc))

def namespace(tag):return tag[1:].split('}')[0] if isinstance(tag,str) and tag.startswith('{') else ''
def local(tag):return tag.split('}')[-1] if isinstance(tag,str) else ''
def native_inventory(root):
    result=[]
    for e in root.iter():
        if not isinstance(e.tag,str):continue
        identity=e.get('id') or e.get('{'+XMI+'}id')
        result.append({'id':identity,'tag':e.tag,'attributes':dict(e.attrib),'text':e.text if e.text and e.text.strip() else None,'children':[c.tag for c in e if isinstance(c.tag,str)]})
    return result

def validate_references(root,package_root=None):
    from bpmn_references import local_reference, local_id
    ids={};errors=[];blocked=[]
    for e in root.iter():
        if not isinstance(e.tag,str):continue
        identity=local_id(e.get('id') or e.get('{'+XMI+'}id'))
        if identity:
            if identity in ids:errors.append('duplicate native ID: '+identity)
            ids[identity]=e
    refattrs={'sourceRef','targetRef','processRef','attachedToRef','bpmnElement','default','activityRef','messageRef','participantRef','initiatingParticipantRef','itemSubjectRef','errorRef','escalationRef','signalRef','operationRef','calledElement','choreographyRef'}
    for e in root.iter():
        if not isinstance(e.tag,str):continue
        for key,value in e.attrib.items():
            if namespace(e.tag) in (BPMN,'http://www.omg.org/spec/BPMN/20100524/DI') and not namespace(key) and local(key) in refattrs:
                # QName prefixes are namespace-qualified, not silently local IDs.
                ref,problem=local_reference(e,value,root.get('targetNamespace'))
                if problem:blocked.append(problem)
                elif ref not in ids:errors.append('dangling BPMN reference: '+value)
            if namespace(key) in ('',XMI) and local(key) in ('href','idref'):
                if local(key)=='idref':
                    for ref in value.split():
                        if ref not in ids:errors.append('dangling XMI idref: '+ref)
                    continue
                path,_,fragment=value.partition('#');path=unquote(path)
                if not path:
                    if fragment and fragment not in ids:errors.append('dangling href fragment: '+fragment)
                    continue
                if urlsplit(path).scheme:
                    blocked.append('external reference is retained but never fetched: '+value);continue
                if Path(path).is_absolute():errors.append('absolute href paths prohibited: '+path);continue
                if package_root is None:blocked.append('package root required for external href: '+path);continue
                base=Path(package_root).resolve();target=(base/path).resolve()
                if not target.is_relative_to(base):errors.append('href path escape: '+path)
                elif not target.is_file():blocked.append('external package resource missing: '+path)
                else:
                    ext=safe_xml(target.read_bytes())
                    if fragment and not any(c.get('{'+XMI+'}id')==fragment or c.get('id')==fragment for c in ext.iter()):errors.append('external href fragment missing: '+value)
        if namespace(e.tag)==BPMN and local(e.tag) in ('incoming','outgoing','flowNodeRef','participantRef','messageFlowRef','eventDefinitionRef','sourceRef','targetRef'):
            if e.text:
                ref,problem=local_reference(e,e.text,root.get('targetNamespace'))
                if problem:blocked.append(problem)
                elif ref not in ids:errors.append('dangling BPMN reference element: '+e.text.strip())
    return errors,blocked

def catalog(language,version):
    if VERSIONS.get(language)!=version:raise Invalid('explicit supported version required: '+str(VERSIONS))
    if language=='archimate':
        # Public publication metadata is not an acquired normative specification.
        return {'language':language,'version':version,'source_status':'blocked',
                'official_publication':{'id':'C260','title':'ArchiMate 4 Specification',
                    'catalog_url':'https://publications.opengroup.org/c260',
                    'acquisition_status':'publication-metadata-only',
                    'normative_content_acquired':False,'license_accepted':False},
                'reason':'authorized ArchiMate 4 metamodel, notation and applicable official exchange specification are not acquired',
                'constructs':[],'coverage_status':'blocked','compatibility_substitution':False}
    files=list((SOURCES/(language+'-'+version)).glob('*'))
    if not files:raise Incomplete('official machine-readable sources missing')
    sourcefile=SOURCES/(language+'-'+version)/('BPMN20.cmof' if language=='bpmn' else 'UML.xmi')
    root=safe_xml(sourcefile.read_bytes());constructs=[]
    for e in root.iter():
        t=e.get('{'+XMI+'}type') or next((v for k,v in e.attrib.items() if local(k)=='type' and namespace(k).endswith('/2.1')),None)
        if t and t.split(':')[-1] in ('Class','Enumeration','DataType','PrimitiveType','Association'):
            props=[{'name':p.get('name'),'tag':local(p.tag),'id':p.get('{'+XMI+'}id') or next((v for k,v in p.attrib.items() if local(k)=='id'),None),'validation_status':'uncovered'} for p in e if local(p.tag) in ('ownedAttribute','ownedRule','ownedLiteral')]
            identity=e.get('{'+XMI+'}id') or next((v for k,v in e.attrib.items() if local(k)=='id'),None)
            constructs.append({'name':e.get('name'),'kind':t.split(':')[-1],'native_id':identity,'source_file':sourcefile.name,'properties_constraints':props,'source_locator':'xmi:id='+str(identity),'implementation_status':'inventory-only','conformance_tests':'uncovered'})
    return {'language':language,'version':version,'sources':[{'file':p.name,'sha256':sha(p.read_bytes())} for p in files if p.suffix in ('.cmof','.xmi','.xsd')],
        'constructs':constructs,'construct_count':len(constructs),'full_design_time_validation':'incomplete','official_oracle':'machine-readable source, not implementation generator','coverage_status':'uncovered','di_source':'BPMNDI/DI/DC' if language=='bpmn' else 'UMLDI/PrimitiveTypes/StandardProfile','certification':'not-claimed'}

def check_native(data,language,version,package_root=None):
    if VERSIONS.get(language)!=version:raise Invalid('unsupported version; no fallback')
    if language=='archimate':raise Incomplete(catalog(language,version)['reason'])
    root=safe_xml(data);errors=[];blocked=[]
    if language=='bpmn':
        if root.tag!='{'+BPMN+'}definitions':errors.append('BPMN 2.0.2 root must be definitions in normative namespace')
        from lxml import etree
        folder=SOURCES/'bpmn-2.0.2';xsd=folder/'BPMN20.xsd'
        if xsd.is_file():
            try:
                schema=etree.XMLSchema(etree.parse(str(xsd),etree.XMLParser(no_network=True,resolve_entities=False)))
                if not schema.validate(root):errors.extend(str(x) for x in schema.error_log)
            except (etree.XMLSchemaParseError,etree.XMLSyntaxError) as exc:blocked.append('official XSD load failed: '+str(exc))
        else:blocked.append('official XSD not acquired')
        from bpmn_references import local_id
        processes={local_id(e.get('id')):e for e in root.iter('{'+BPMN+'}process')}
        for flow in root.iter('{'+BPMN+'}sequenceFlow'):
            a=local_id(flow.get('sourceRef'));b=local_id(flow.get('targetRef'))
            for process in processes.values():
                owned={local_id(e.get('id')) for e in process.iter()}
                if (a in owned)!=(b in owned):errors.append('sequenceFlow crosses process boundary: '+str(flow.get('id')))
        # Independent semantic checks are deliberately narrower than full standard.
        for event in root.iter('{'+BPMN+'}startEvent'):
            if list(event.iter('{'+BPMN+'}incoming')):errors.append('startEvent has incoming flow: '+str(event.get('id')))
        for event in root.iter('{'+BPMN+'}endEvent'):
            if list(event.iter('{'+BPMN+'}outgoing')):errors.append('endEvent has outgoing flow: '+str(event.get('id')))
        from bpmn_semantics import check as check_behavior
        behavior=check_behavior(root)
        errors.extend(f["rule_id"]+': '+str(f['id'])+': '+f['message'] for f in behavior['findings'])
    elif namespace(root.tag) not in (XMI,'http://www.omg.org/spec/UML/20131001'):
        errors.append('UML 2.5.1 requires normative UML/XMI namespaces; Eclipse namespaces require explicit mapping, not silent substitution')
    referrors,refblocked=validate_references(root,package_root);errors+=referrors;blocked+=refblocked
    vendor=sorted({uri for e in root.iter() if isinstance(e.tag,str)
                   for uri in [namespace(e.tag),*(namespace(key) for key in e.attrib)]
                   if uri and uri not in KNOWN and uri!='http://www.w3.org/XML/1998/namespace'})
    if vendor:blocked.append('vendor/profile extensions opaque, not standard-validated: '+', '.join(vendor))
    if language=='uml':blocked.append('complete UML2/OCL/Profiles/UMLDI metamodel validation and notation suite not yet verified')
    else:blocked.append('complete BPMN normative semantic, choreography and notation constraint suite not yet verified')
    return {'language':language,'version':version,'errors':errors,'blockers':blocked,'native_inventory':native_inventory(root),'vendor_namespaces':vendor,'conformance_status':'invalid' if errors else 'incomplete','source_sha256':sha(data),**({'behavior_validation':behavior} if language=='bpmn' else {})}

def make_package(data,language,version,package_root=None):
    report=check_native(data,language,version,package_root)
    if report['errors']:raise Invalid('; '.join(report['errors']))
    return {'format':'ai-togaf-native-language-package','package_version':'1.0','language':language,'language_version':version,'payload_encoding':'base64','native_xml':base64.b64encode(data).decode(),'native_sha256':sha(data),'native_inventory':report['native_inventory'],'inventory_sha256':sha(json.dumps(report['native_inventory'],sort_keys=True).encode()),'bindings':[],'report':report,'editing':'derived inventory read-only; editing unsupported constructs is blocked','exchange_mode':'lossless native preservation, not invented official exchange'}

def package_bytes(package,language,version):
    if package.get('format')!='ai-togaf-native-language-package' or package.get('package_version')!='1.0':raise Invalid('invalid native language package')
    if (package.get('language'),package.get('language_version'))!=(language,version):raise Invalid('package language/version mismatch')
    try:data=base64.b64decode(package['native_xml'],validate=True)
    except Exception as exc:raise Invalid('invalid XML payload: '+str(exc))
    if sha(data)!=package.get('native_sha256'):raise Invalid('native payload hash mismatch')
    if sha(json.dumps(package.get('native_inventory'),sort_keys=True).encode())!=package.get('inventory_sha256'):raise Invalid('editing inventory without supported native mapping is prohibited')
    if native_inventory(safe_xml(data))!=package['native_inventory']:raise Invalid('native inventory does not match payload')
    for binding in package.get('bindings',[]):
        if not re.fullmatch(r'[A-Za-z][\w.-]*:[\w.:-]+',binding.get('namespace','')):raise Invalid('binding requires namespace')
        if binding.get('native_id') not in {e['id'] for e in package['native_inventory'] if e['id']}:raise Invalid('binding native_id does not exist')
        if not binding.get('project_id'):raise Invalid('binding project_id required')
    return data

def moddle(data):
    with tempfile.TemporaryDirectory(prefix='bpmn-exchange-') as tmp:
        path=Path(tmp)/'input.bpmn';out=Path(tmp)/'output.bpmn';path.write_bytes(data)
        result=subprocess.run([shutil.which('node') or 'node',str(ROOT/'scripts/bpmn_native.mjs'),str(path),str(out)],capture_output=True,text=True,timeout=60)
        if result.returncode:raise Incomplete('bpmn-moddle backend failed: '+result.stderr[-2000:])
        return out.read_bytes(),json.loads(result.stdout)

def write_new(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:stream.write(data)

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['catalog','import','validate','export','render']);parser.add_argument('--language',choices=VERSIONS,required=True);parser.add_argument('--version',required=True);parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path);parser.add_argument('--package-root',type=Path);parser.add_argument('--normalize',action='store_true');parser.add_argument('--mapped-uml-backend',action='store_true');parser.add_argument('--java-home',type=Path);args=parser.parse_args()
    result={};code=0
    try:
        if args.command=='catalog':
            result=catalog(args.language,args.version);code=3 if result.get('source_status')=='blocked' else 0
        else:
            if not args.input:raise Invalid('--input required')
            raw=args.input.read_bytes();package=json.loads(raw) if raw.lstrip().startswith(b'{') else None
            data=package_bytes(package,args.language,args.version) if package else raw
            if args.command=='import':
                result=make_package(data,args.language,args.version,args.package_root)
                if not args.out:raise Invalid('--out required')
                write_new(args.out,json.dumps(result,ensure_ascii=False,indent=2).encode())
                result={'operation':'import','exchange_status':'preserved','conformance_status':'incomplete','manifest_sha256':sha(args.out.read_bytes()),'report':result['report']}
            elif args.command=='validate':
                result=check_native(data,args.language,args.version,args.package_root);code=1 if result['errors'] else 3
                if args.mapped_uml_backend:
                    if args.language!='uml':raise Invalid('--mapped-uml-backend requires UML 2.5.1')
                    if not result['errors']:
                        from uml_backend import validate_mapped
                        result['mapped_backend']=validate_mapped(data,args.java_home)
                        result['mapped_findings_not_equivalence']='Compiled and mapped OCL diagnostics require source/mapping adjudication; not a full standard pass'
            elif args.command=='export':
                if not package:raise Invalid('export requires native package, not project JSON')
                report=check_native(data,args.language,args.version,args.package_root)
                if report['errors']:raise Invalid('; '.join(report['errors']))
                backend=None
                if args.normalize:
                    if args.language!='bpmn':raise Incomplete('normalized native writer not yet verified for '+args.language)
                    output,backend=moddle(data)
                    original= native_inventory(safe_xml(data));normalized=native_inventory(safe_xml(output))
                    if original!=normalized or backend['warnings']:raise Incomplete('strict normalization refused: lexical/semantic inventory changes or warnings require explicit mapping review')
                    data=output
                if not args.out:raise Invalid('--out required')
                write_new(args.out,data);result={'operation':'export','exchange_status':'preserved','semantic_loss':False,'normalized':args.normalize,'backend':backend,'conformance_status':'incomplete','sha256':sha(data)}
            elif args.command=='render' and args.language=='bpmn':
                if args.version!='2.0.2':raise Invalid('unsupported BPMN rendering version; no fallback')
                if not args.out:raise Invalid('--out required')
                from bpmn_render import render_native, Invalid as BpmnInvalid, Incomplete as BpmnIncomplete
                try:result=render_native(data,args.out,args.package_root)
                except BpmnInvalid as exc:raise Invalid(str(exc))
                except BpmnIncomplete as exc:raise Incomplete(str(exc))
            elif args.command=='render' and args.language=='uml':
                if args.version!='2.5.1':raise Invalid('unsupported UML rendering version; no fallback')
                if not args.out:raise Invalid('--out required')
                from uml_render import render_native, Invalid as UmlInvalid, Incomplete as UmlIncomplete
                try:result=render_native(data,args.out,args.package_root)
                except UmlInvalid as exc:raise Invalid(str(exc))
                except UmlIncomplete as exc:raise Incomplete(str(exc))
            else:
                raise Incomplete('strict native notation rendering not verified; use a disclosed project reading projection, never relabel it as official notation')
        if args.out and args.command in ('catalog','validate'):write_new(args.out,json.dumps(result,ensure_ascii=False,indent=2).encode())
    except (Invalid,ValueError,OSError) as exc:result={'status':'error','reason':str(exc)};code=1
    except (Incomplete,ImportError,subprocess.TimeoutExpired) as exc:result={'status':'blocked','reason':str(exc)};code=3
    print(json.dumps(result,ensure_ascii=False,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
