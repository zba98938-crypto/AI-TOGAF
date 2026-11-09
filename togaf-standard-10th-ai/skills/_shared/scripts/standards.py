#!/usr/bin/env python3
"""Native design-language packages, inventories, secure exchange and honest gates.
0 = requested exchange operation complete, 1 = definite error, 3 = incomplete.
A successful import is NOT full-language conformance or notation certification.
"""
import argparse,base64,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
from urllib.parse import unquote,urlsplit
if __name__=='__main__':sys.modules['standards']=sys.modules[__name__]
ROOT=Path(__file__).resolve().parents[1]
SOURCES=ROOT/'standards/sources'
VERSIONS={'bpmn':'2.0.2','uml':'2.5.1','archimate':'4'}
BPMN='http://www.omg.org/spec/BPMN/20100524/MODEL'
XMI='http://www.omg.org/spec/XMI/20131001'
KNOWN={BPMN,'http://www.omg.org/spec/BPMN/20100524/DI','http://www.omg.org/spec/DD/20100524/DI','http://www.omg.org/spec/DD/20100524/DC',XMI,'http://www.omg.org/spec/UML/20131001','http://www.omg.org/spec/UML/20131001/UMLDI','http://www.omg.org/spec/UML/20161101/UMLDI','http://www.omg.org/spec/DD/20131001/DI','http://www.omg.org/spec/DD/20131001/DC','http://www.w3.org/2001/XMLSchema-instance'}
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

def bpmn_reference_fields():
    """Derive QName/IDREF fields from the acquired normative exchange schemas."""
    fields={'attribute':{},'element':{}}
    xsd='{http://www.w3.org/2001/XMLSchema}'
    for name in ('Semantic.xsd','BPMNDI.xsd','DI.xsd'):
        path=SOURCES/'bpmn-2.0.2'/name
        if not path.is_file():raise Incomplete('normative reference schema missing: '+name)
        schema=safe_xml(path.read_bytes())
        for element in schema.iter():
            if element.tag not in (xsd+'attribute',xsd+'element'):continue
            if element.get('type','').split(':')[-1] in ('QName','IDREF','IDREFS') and element.get('name'):
                fields[local(element.tag)][element.get('name')]=element.get('type').split(':')[-1]
    return fields

def validate_references(root,package_root=None,verified_external_refs=None,resource_context=None,document_path=None):
    from bpmn_references import local_reference, local_id
    ids={};errors=[];blocked=[]
    for e in root.iter():
        if not isinstance(e.tag,str):continue
        identity=local_id(e.get('id') or e.get('{'+XMI+'}id'))
        if identity:
            if identity in ids:errors.append('duplicate native ID: '+identity)
            ids[identity]=e
    fields=bpmn_reference_fields() if namespace(root.tag)==BPMN else {'attribute':{},'element':{}}
    refattrs=fields['attribute']
    for e in root.iter():
        if not isinstance(e.tag,str):continue
        for key,value in e.attrib.items():
            if namespace(e.tag) in (BPMN,'http://www.omg.org/spec/BPMN/20100524/DI') and not namespace(key) and local(key) in refattrs:
                # QName prefixes are namespace-qualified, not silently local IDs.
                for token in value.split() if refattrs[local(key)]=='IDREFS' else [value]:
                    if resource_context is not None and refattrs[local(key)]=='QName':
                        resource_context.resolve(document_path,e,local(key),token,'attribute')
                        continue
                    ref,problem=local_reference(e,token,root.get('targetNamespace'))
                    if problem:blocked.append(problem)
                    elif ref not in ids:errors.append('dangling BPMN reference: '+token)
            if namespace(key) in ('',XMI) and local(key) in ('href','idref'):
                if local(key)=='idref':
                    for ref in value.split():
                        if ref not in ids:errors.append('dangling XMI idref: '+ref)
                    continue
                if resource_context is not None:
                    blocked.append('BPMN non-import href retained opaquely and never read: '+value)
                    continue
                if value in (verified_external_refs or set()):continue
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
        if namespace(e.tag)==BPMN and local(e.tag) in fields['element']:
            if e.text:
                for token in e.text.split() if fields['element'][local(e.tag)]=='IDREFS' else [e.text]:
                    if resource_context is not None and fields['element'][local(e.tag)]=='QName':
                        resource_context.resolve(document_path,e,local(e.tag),token,'element')
                        continue
                    ref,problem=local_reference(e,token,root.get('targetNamespace'))
                    if problem:blocked.append(problem)
                    elif ref not in ids:errors.append('dangling BPMN reference element: '+token.strip())
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
    from standards_coverage import ledger
    coverage=ledger(language,version)
    profile_catalog={}
    if language=='uml':
        from uml_profiles import catalog as standard_profile_catalog
        profile_catalog={'standard_profile':standard_profile_catalog()}
    return {'language':language,'version':version,'sources':[{'file':p.name,'sha256':sha(p.read_bytes())} for p in files if p.suffix in ('.cmof','.xmi','.xsd')],
        'constructs':constructs,'construct_count':len(constructs),'full_design_time_validation':'incomplete','official_oracle':'machine-readable source, not implementation generator','coverage_status':'uncovered','coverage_ledger':coverage,'di_source':'BPMNDI/DI/DC' if language=='bpmn' else 'UMLDI/PrimitiveTypes/StandardProfile','certification':'not-claimed',**profile_catalog}

def _check_native_one(data,language,version,package_root=None,resource_context=None,document_path=None):
    if VERSIONS.get(language)!=version:raise Invalid('unsupported version; no fallback')
    if language=='archimate':raise Incomplete(catalog(language,version)['reason'])
    root=resource_context.documents[document_path]['root'] if resource_context is not None else safe_xml(data);errors=[];blocked=[]
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
        from bpmn_design_semantics import check as check_design_time
        design_time=check_design_time(root)
        errors.extend(f["rule_id"]+': '+str(f['id'])+': '+f['message'] for f in design_time['findings'])
        blocked.extend(design_time.get('capability_uncovered',[]))
    elif namespace(root.tag) not in (XMI,'http://www.omg.org/spec/UML/20131001'):
        errors.append('UML 2.5.1 requires normative UML/XMI namespaces; Eclipse namespaces require explicit mapping, not silent substitution')
    if language=='uml' and not errors:
        from uml_design_semantics import check as check_uml_design_time
        design_time=check_uml_design_time(root)
        errors.extend(f['rule_id']+': '+str(f['id'])+': '+f['message'] for f in design_time['findings'])
        from uml_profiles import check as check_standard_profiles
        profiles=check_standard_profiles(root,package_root)
        verified_refs=set(profiles['verified_profile_references'])
        errors.extend(f['rule_id']+': '+str(f['id'])+': '+f['message'] for f in profiles['findings'])
        blocked.extend(profiles['capability_uncovered'])
        blocked.extend(message for message in design_time['capability_uncovered']
                       if not any(message=='Cross-file UML reference type remains unverified: '+ref for ref in verified_refs))
    referrors,refblocked=validate_references(root,package_root,verified_refs if 'verified_refs' in locals() else None,resource_context,document_path);errors+=referrors;blocked+=refblocked
    vendor=sorted({uri for e in root.iter() if isinstance(e.tag,str)
                   for uri in [namespace(e.tag),*(namespace(key) for key in e.attrib)]
                   if uri and uri not in KNOWN and uri not in (profiles['verified_profile_namespaces'] if 'profiles' in locals() else []) and uri!='http://www.w3.org/XML/1998/namespace'})
    if vendor:blocked.append('vendor/profile extensions opaque, not standard-validated: '+', '.join(vendor))
    if language=='uml':blocked.append('complete UML2/OCL/Profiles/UMLDI metamodel validation and notation suite not yet verified')
    else:blocked.append('complete BPMN normative semantic, choreography and notation constraint suite not yet verified')
    missing=[item for item in blocked if any(token in item for token in ('file missing','source missing','material missing','resource missing','not acquired','needs a package root')) or item.startswith('package root required')]
    groups={'validation_errors':errors,'missing_material':missing,'capability_uncovered':[item for item in blocked if item not in missing]}
    return {'language':language,'version':version,'errors':errors,'blockers':blocked,'diagnostic_groups':groups,'native_inventory':native_inventory(root),'vendor_namespaces':vendor,'conformance_status':'invalid' if errors else 'incomplete','source_sha256':sha(data),**({'behavior_validation':behavior,'design_time_semantics':design_time} if language=='bpmn' else {'design_time_semantics':design_time} if 'design_time' in locals() else {}),**({'standard_profile_validation':profiles} if 'profiles' in locals() else {})}

def check_native(data,language,version,package_root=None,*,resources=None,document_path=None,_resource_context=None):
    """Validate each native document while preserving per-owner qualified identity."""
    if language!='bpmn':
        if resources is not None or document_path is not None:raise Invalid('native resources/document_path are currently BPMN-only')
        return _check_native_one(data,language,version,package_root)
    if VERSIONS.get(language)!=version:raise Invalid('unsupported version; no fallback')
    from bpmn_imports import ResourceContext
    context=_resource_context or ResourceContext.from_root(data,package_root,resources,document_path)
    report=_check_native_one(data,language,version,package_root,context,context.main_path)
    imported=[]
    errors=list(report['errors']);missing=list(report['diagnostic_groups']['missing_material']);capability=list(report['diagnostic_groups']['capability_uncovered'])
    for path,document in sorted(context.documents.items()):
        if path==context.main_path:continue
        sub=_check_native_one(document['data'],language,version,None,context,path)
        imported.append({'document_path':path,**{k:v for k,v in sub.items() if k!='native_inventory'}})
        errors.extend('BPMN resource '+path+': '+message for message in sub['errors'])
        missing.extend('BPMN resource '+path+': '+message for message in sub['diagnostic_groups']['missing_material'])
        capability.extend('BPMN resource '+path+': '+message for message in sub['diagnostic_groups']['capability_uncovered'] if not message.startswith('complete BPMN normative'))
    closure=context.report()
    errors.extend(closure['validation_errors']);missing.extend(closure['missing_material']);capability.extend(closure['capability_uncovered'])
    report.update(errors=list(dict.fromkeys(errors)),blockers=list(dict.fromkeys(missing+capability)),
                  diagnostic_groups={'validation_errors':list(dict.fromkeys(errors)),'missing_material':list(dict.fromkeys(missing)),'capability_uncovered':list(dict.fromkeys(capability))},
                  resource_closure=closure,imported_document_validation=imported,
                  conformance_status='invalid' if errors else 'incomplete')
    return report

def make_package(data,language,version,package_root=None,*,resources=None,document_path=None):
    context=None
    if language=='bpmn':
        from bpmn_imports import ResourceContext
        context=ResourceContext.from_root(data,package_root,resources,document_path)
    report=check_native(data,language,version,package_root,resources=resources,document_path=document_path,_resource_context=context)
    if report['errors']:raise Invalid('; '.join(report['errors']))
    package={'format':'ai-togaf-native-language-package','package_version':'1.0','language':language,'language_version':version,'payload_encoding':'base64','native_xml':base64.b64encode(data).decode(),'native_sha256':sha(data),'native_inventory':report['native_inventory'],'inventory_sha256':sha(json.dumps(report['native_inventory'],sort_keys=True).encode()),'bindings':[],'report':report,'editing':'derived inventory read-only; editing unsupported constructs is blocked','exchange_mode':'lossless native preservation, not invented official exchange'}
    if context is not None and (context.imports or context.values or document_path is not None or resources is not None):
        from bpmn_imports import encode_resources
        package.update(document_path=context.main_path,resources=encode_resources(context.values))
    return package

def package_bytes(package,language,version):
    if not isinstance(package,dict):raise Invalid('native language package must be an object')
    if package.get('format')!='ai-togaf-native-language-package' or package.get('package_version')!='1.0':raise Invalid('invalid native language package')
    if (package.get('language'),package.get('language_version'))!=(language,version):raise Invalid('package language/version mismatch')
    if package.get('payload_encoding')!='base64':raise Invalid('native XML payload_encoding must be base64')
    payload=package.get('native_xml')
    if not isinstance(payload,str) or len(payload)>((64*1024*1024+2)//3)*4:raise Invalid('native XML encoded payload exceeds 64MiB safety budget')
    if len(payload)%4 or not re.fullmatch(r'[A-Za-z0-9+/]*={0,2}',payload):raise Invalid('invalid XML payload encoding')
    root_size=len(payload)//4*3-(2 if payload.endswith('==') else 1 if payload.endswith('=') else 0)
    if root_size>64*1024*1024:raise Invalid('native XML decoded payload exceeds 64MiB safety budget')
    if 'resources' in package or 'document_path' in package:
        if language!='bpmn':raise Invalid('native resources/document_path are currently BPMN-only')
        if 'resources' in package and not isinstance(package['resources'],list):raise Invalid('native resources must be a list')
        if 'document_path' in package and not isinstance(package['document_path'],str):raise Invalid('native document_path must be a string')
        from bpmn_imports import decode_resources,document_path
        decode_resources(package.get('resources',[]),root_size,document_path(package.get('document_path')),check_only=True)
    try:data=base64.b64decode(payload,validate=True)
    except Exception as exc:raise Invalid('invalid XML payload: '+str(exc))
    if sha(data)!=package.get('native_sha256'):raise Invalid('native payload hash mismatch')
    if sha(json.dumps(package.get('native_inventory'),sort_keys=True).encode())!=package.get('inventory_sha256'):raise Invalid('editing inventory without supported native mapping is prohibited')
    if native_inventory(safe_xml(data))!=package['native_inventory']:raise Invalid('native inventory does not match payload')
    if 'resources' in package or 'document_path' in package:
        decode_resources(package.get('resources',[]),len(data),document_path(package.get('document_path')))
    bindings=package.get('bindings',[])
    if not isinstance(bindings,list):raise Invalid('native package bindings must be a list')
    native_ids={e['id'] for e in package['native_inventory'] if e['id']}
    for binding in bindings:
        if not isinstance(binding,dict):raise Invalid('native package binding must be an object')
        if not isinstance(binding.get('namespace'),str) or not re.fullmatch(r'[A-Za-z][\w.-]*:[\w.:-]+',binding['namespace']):raise Invalid('binding requires namespace')
        if not isinstance(binding.get('native_id'),str) or binding['native_id'] not in native_ids:raise Invalid('binding native_id does not exist')
        if not isinstance(binding.get('project_id'),str) or not binding['project_id']:raise Invalid('binding project_id required')
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
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['catalog','import','validate','export','render']);parser.add_argument('--language',choices=VERSIONS,required=True);parser.add_argument('--version',required=True);parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path);parser.add_argument('--package-root',type=Path);parser.add_argument('--normalize',action='store_true');parser.add_argument('--auto-layout',action='store_true');parser.add_argument('--mapped-uml-backend',action='store_true');parser.add_argument('--java-home',type=Path)
    parser.add_argument('--document-path',help='Canonical main-document path in an explicit BPMN package')
    parser.add_argument('--materialize',action='store_true',help='Export a verified BPMN root and all resources into a new directory')
    args=parser.parse_args()
    result={};code=0
    try:
        if args.auto_layout and (args.command!='render' or args.language!='bpmn'):
            raise Invalid('--auto-layout requires BPMN render')
        if args.document_path is not None and args.language!='bpmn':raise Invalid('--document-path requires BPMN')
        if args.materialize and (args.command!='export' or args.language!='bpmn' or args.normalize):raise Invalid('--materialize requires unnormalized BPMN export')
        if args.command=='catalog':
            result=catalog(args.language,args.version);code=3 if result.get('source_status')=='blocked' else 0
        else:
            if not args.input:raise Invalid('--input required')
            if args.input.stat().st_size>192*1024*1024:raise Invalid('native input exceeds the 192MiB serialized package budget')
            raw=args.input.read_bytes();package=json.loads(raw) if raw.lstrip().startswith(b'{') else None
            data=package_bytes(package,args.language,args.version) if package else raw
            context_args={};package_root=args.package_root
            if args.language=='bpmn':
                if package:
                    package_root=None  # Embedded packages never fill gaps from ambient disk.
                    if args.document_path is not None and args.document_path!=package.get('document_path','main.bpmn'):raise Invalid('--document-path conflicts with stored package identity')
                    context_args={'resources':package.get('resources',[]),'document_path':package.get('document_path')}
                else:
                    main_path=args.document_path
                    if package_root is not None:
                        from bpmn_imports import resolved_path
                        base=resolved_path(package_root);source=resolved_path(args.input)
                        if not base.is_dir() or not source.is_relative_to(base):raise Invalid('BPMN input must remain inside explicit --package-root')
                        inferred=source.relative_to(base).as_posix()
                        if main_path is not None and main_path!=inferred:raise Invalid('--document-path conflicts with input path in --package-root')
                        main_path=inferred
                    context_args={'document_path':main_path}
            if args.command=='import':
                result=make_package(data,args.language,args.version,package_root,**context_args)
                if not args.out:raise Invalid('--out required')
                write_new(args.out,json.dumps(result,ensure_ascii=False,indent=2).encode())
                result={'operation':'import','exchange_status':'preserved','conformance_status':'incomplete','manifest_sha256':sha(args.out.read_bytes()),'report':result['report']}
            elif args.command=='validate':
                result=check_native(data,args.language,args.version,package_root,**context_args);code=1 if result['errors'] else 3
                if args.mapped_uml_backend:
                    if args.language!='uml':raise Invalid('--mapped-uml-backend requires UML 2.5.1')
                    if not result['errors']:
                        from uml_backend import validate_mapped
                        result['mapped_backend']=validate_mapped(data,args.java_home)
                        result['mapped_findings_not_equivalence']='Compiled and mapped OCL diagnostics require source/mapping adjudication; not a full standard pass'
            elif args.command=='export':
                if not package:raise Invalid('export requires native package, not project JSON')
                report=check_native(data,args.language,args.version,package_root,**context_args)
                if report['errors']:raise Invalid('; '.join(report['errors']))
                if args.materialize:
                    if not args.out:raise Invalid('--out required')
                    from bpmn_imports import materialize_bundle
                    result={'operation':'export',**materialize_bundle(package,args.out)}
                    print(json.dumps(result,ensure_ascii=False,indent=2));return 0
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
                report=check_native(data,args.language,args.version,package_root,**context_args)
                if report['errors']:raise Invalid('; '.join(report['errors']))
                if report['resource_closure']['imports']:
                    raise Incomplete('Cross-document BPMN semantics/DI/rendering remains uncovered; resources are preserved but renderer permissions are unchanged')
                from bpmn_render import render_native, Invalid as BpmnInvalid, Incomplete as BpmnIncomplete
                try:result=render_native(data,args.out,args.package_root,auto_layout=args.auto_layout)
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
