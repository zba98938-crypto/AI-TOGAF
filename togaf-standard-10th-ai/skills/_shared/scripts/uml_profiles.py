"""Source-bound UML Standard Profile application checks; never fetch references.

UML 2.5.1 §12.3.3.1.3/§12.3.3.3/§12.3.3.4 define XMI separation,
applying packages and exactly one base instance. StandardProfile.xmi supplies
stereotypes, generalizations and extension metaclasses. Arbitrary Profiles
remain opaque and retain their native payload for later capability validation.
"""
from functools import lru_cache
import json
from pathlib import Path
from standards import SOURCES, XMI, Invalid, Incomplete, local, namespace, safe_xml, sha
from uml_design_semantics import source_schema

UML_NAMESPACES={'http://www.omg.org/spec/UML/20131001','http://www.omg.org/spec/UML/20161101'}
PROFILE_FILE='uml-2.5.1/StandardProfile.xmi'
PDF_FILE='uml-2.5.1/UML-2.5.1.pdf'


def catalog():
    manifest=json.loads((SOURCES/'manifest.json').read_text())
    matches=[r for r in manifest if r.get('file')==PROFILE_FILE]
    if len(matches)!=1:raise Incomplete('Exactly one official StandardProfile source is required')
    path=SOURCES/PROFILE_FILE
    if not path.is_file():raise Incomplete('Official StandardProfile source missing')
    data=path.read_bytes()
    if sha(data)!=matches[0]['sha256']:raise Invalid('StandardProfile source fingerprint conflict')
    result=compile_profile(data)
    return {**result,'source':{'file':PROFILE_FILE,'sha256':sha(data)},
            'scope':'Official stereotypes, inherited base metaclass references and native applications',
            'full_profile_design_time_conformance':False}


@lru_cache(maxsize=2)
def compile_profile(data):
    root=safe_xml(data)
    profiles=[e for e in root if local(e.tag)=='Profile']
    if len(profiles)!=1:raise Invalid('StandardProfile source has no unique Profile')
    profile=profiles[0];stereotypes={}
    for element in profile.findall('packagedElement'):
        if element.get('{'+XMI+'}type','').split(':')[-1]!='Stereotype':continue
        name=element.get('name');identity=element.get('{'+XMI+'}id');bases={}
        for feature in element.findall('ownedAttribute'):
            field=feature.get('name','')
            if not field.startswith('base_'):continue
            kind=feature.find('type')
            href=kind.get('href','') if kind is not None else ''
            file,mark,target=href.partition('#')
            if not mark or not file.endswith('/UML.xmi') or not target:
                raise Invalid('Unsupported official StandardProfile base type')
            bases[field]={'type':target,'source_id':feature.get('{'+XMI+'}id')}
        stereotypes[name]={'id':identity,'bases':bases,
            'parents':[e.get('general') for e in element.findall('generalization')]}
    by_id={s['id']:name for name,s in stereotypes.items()}
    def inherited(name,seen=()):
        if name in seen:raise Invalid('Cyclic StandardProfile stereotype inheritance')
        result={}
        for parent in stereotypes[name]['parents']:
            if parent not in by_id:raise Invalid('Missing StandardProfile stereotype parent')
            result.update(inherited(by_id[parent],seen+(name,)))
        result.update(stereotypes[name]['bases']);return result
    for name in stereotypes:stereotypes[name]['bases']=inherited(name)
    return {'namespace':profile.get('URI'),'profile_id':profile.get('{'+XMI+'}id'),
            'stereotypes':stereotypes,'stereotype_count':len(stereotypes)}


def check(root,package_root=None):
    profile=catalog();schema=source_schema();findings=[];uncovered=[];applications=[];applied_packages=set();verified_references=set()
    uri=profile['namespace'];source=profile['source'];ids={};types={}
    official_refs={uri+'#'+profile['profile_id'],uri+'.xmi#'+profile['profile_id']}
    def issue(rule,e,message,basis=None):
        findings.append({'rule_id':rule,'id':e.get('{'+XMI+'}id'),'message':message,
                         'source':basis or {'file':PDF_FILE,'section':'12.3.3','pdf_pages':[299,300,301]}})
    def kind(e):
        if e in types:return types[e]
        if e is None:return None
        raw=e.get('{'+XMI+'}type','');result=None
        if ':' in raw:
            prefix,_,name=raw.partition(':')
            if e.nsmap.get(prefix) in UML_NAMESPACES:result=('UML.xmi',name)
        elif namespace(e.tag) in UML_NAMESPACES:result=('UML.xmi',local(e.tag))
        else:
            parent=kind(e.getparent())
            result=schema.get(parent,{}).get('features',{}).get(local(e.tag),{}).get('type')
        types[e]=result if result in schema else None;return types[e]
    def conforms(actual,expected,seen=()):
        if actual==expected:return True
        if actual in seen:return False
        return any(conforms(p,expected,seen+(actual,)) for p in schema.get(actual,{}).get('parents',[]))
    def standard_reference(raw,e):
        if raw in official_refs:return True
        file,mark,fragment=raw.partition('#')
        if file and mark and fragment==profile['profile_id'] and Path(file).name=='StandardProfile.xmi':
            if not package_root:
                uncovered.append('Relative StandardProfile material needs a package root: '+raw);return False
            # A relative reference only resolves an exact local authoritative copy.
            if ':' in file or '\\' in file or '%' in file or Path(file).is_absolute():
                issue('StandardProfile-local-reference',e,'Unsafe local Profile reference');return False
            base=Path(package_root).resolve();path=base/file
            if path.is_symlink() or not path.resolve().is_relative_to(base):
                issue('StandardProfile-local-reference',e,'Profile reference escapes package');return False
            for parent in path.parents:
                if parent==base:break
                if parent.is_symlink():issue('StandardProfile-local-reference',e,'Profile symlink escape');return False
            if not path.is_file():uncovered.append('StandardProfile local material missing: '+file);return False
            if sha(path.read_bytes())!=source['sha256']:
                issue('StandardProfile-source-fingerprint',e,'Local StandardProfile differs from official source');return False
            return True
        return False
    for e in root.iter():
        if not isinstance(e.tag,str):continue
        if e.get('{'+XMI+'}id'):ids[e.get('{'+XMI+'}id')]=e
        kind(e)
        if kind(e)==('UML.xmi','ProfileApplication'):
            refs=[]
            if e.get('appliedProfile'):refs.extend(e.get('appliedProfile').split())
            for child in e.findall('appliedProfile'):
                if child.get('href'):refs.append(child.get('href'))
                elif child.get('{'+XMI+'}idref'):refs.append(child.get('{'+XMI+'}idref'))
            if len(refs)!=1:issue('ProfileApplication-one-appliedProfile',e,'Exactly one appliedProfile reference required');continue
            if standard_reference(refs[0],e):
                verified_references.add(refs[0])
                package=e.getparent()
                if not conforms(kind(package),('UML.xmi','Package')):
                    issue('ProfileApplication-applyingPackage',e,'ProfileApplication must belong to a Package')
                else:applied_packages.add(package)
            elif not refs[0].endswith('/StandardProfile.xmi#'+profile['profile_id']):
                uncovered.append('Custom/unresolved Profile remains unverified: '+refs[0])
    for e in root.iter():
        if not isinstance(e.tag,str) or namespace(e.tag)!=uri:continue
        name=local(e.tag);definition=profile['stereotypes'].get(name)
        if definition is None:issue('StandardProfile-stereotype-exists',e,'Unknown official StandardProfile stereotype: '+name,source);continue
        references=[]
        for field,value in e.attrib.items():
            if namespace(field):continue
            if field not in definition['bases']:
                issue('StandardProfile-property-exists',e,'Undeclared StandardProfile property: '+field,source);continue
            for token in value.split():references.append((field,token))
        for child in e:
            if not isinstance(child.tag,str):continue
            field=local(child.tag)
            if field not in definition['bases']:
                issue('StandardProfile-property-exists',e,'Undeclared StandardProfile property: '+field,source);continue
            raw=child.get('{'+XMI+'}idref') or child.get('href','')
            if raw.startswith('#'):raw=raw[1:]
            if not raw or '#' in raw or ':' in raw or '/' in raw:
                issue('StandardProfile-local-base',e,'StandardProfile base must be a local model reference',source)
            else:references.append((field,raw))
        if len(references)!=1:
            issue('Stereotype-one-base-instance',e,'A stereotype instance must apply to exactly one base model instance');continue
        field,token=references[0];base=ids.get(token);expected=definition['bases'][field]['type']
        basis={**source,'id':definition['bases'][field]['source_id']}
        if base is None:issue('StandardProfile-base-exists',e,'Dangling base model reference: '+token,basis);continue
        actual=kind(base)
        if actual is None or not conforms(actual,('UML.xmi',expected)):
            issue('StandardProfile-base-metaclass',e,'Base requires '+expected+', found '+str(actual),basis);continue
        package=base
        while package is not None and package not in applied_packages:package=package.getparent()
        if package is None:
            issue('StandardProfile-applied-to-package',e,'StandardProfile is not applied to the base element package');continue
        applications.append({'id':e.get('{'+XMI+'}id'),'stereotype':name,'base_id':token,'base_metaclass':actual[1],
                             'applying_package_id':package.get('{'+XMI+'}id'),'source':basis})
    stereotype_ids={e.get('{'+XMI+'}id') for e in root.iter() if isinstance(e.tag,str) and namespace(e.tag)==uri}
    for e,actual in types.items():
        if actual is None:continue
        for field,value in e.attrib.items():
            feature=schema.get(actual,{}).get('features',{}).get(field)
            if feature and schema.get(feature['type'],{}).get('kind')=='Class' and set(value.split())&stereotype_ids:
                issue('Profile-XMI-model-does-not-reference-application',e,'Native UML model must not refer to stereotype application instances')
    return {'status':'invalid' if findings else 'passed-bounded-checks','findings':findings,
            'capability_uncovered':sorted(set(uncovered)),'applications':applications,'source':source,
            'verified_profile_namespaces':[uri],'verified_profile_references':sorted(verified_references),'external_resources_loaded':False,
            'full_profile_design_time_conformance':False,
            'scope':'Official StandardProfile applications and inherited base typing; arbitrary Profile definitions, filtering UI and full notation remain separate obligations'}
