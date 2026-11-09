"""Source-derived local UML reference typing and bounded UMLDI diagnostics.

This does not evaluate the full metamodel, apply Profiles or draw UMLDI. XML,
including diagram coordinates and opaque extensions, remains authoritative.
"""
from functools import lru_cache
import json
import math
from pathlib import Path
from urllib.parse import urlsplit

from standards import SOURCES, XMI, Invalid, Incomplete, local, namespace, safe_xml, sha

FAMILIES = {
    'http://www.omg.org/spec/UML/20131001': 'UML.xmi',
    'http://www.omg.org/spec/UML/20131001/UMLDI': 'UMLDI.xmi',
    'http://www.omg.org/spec/UML/20161101/UMLDI': 'UMLDI.xmi',
    'http://www.omg.org/spec/DD/20131001/DI': 'DI.xmi',
    'http://www.omg.org/spec/DD/20131001/DC': 'DC.xmi',
}
FILES = ('UML.xmi', 'UMLDI.xmi', 'DI.xmi', 'DC.xmi', 'PrimitiveTypes.xmi')


def source_schema():
    manifest = json.loads((SOURCES/'manifest.json').read_text())
    rows = {}
    for row in manifest:
        name = Path(row.get('file', '')).name
        if row.get('language') != 'uml-2.5.1' or name not in FILES: continue
        relative = Path(row['file'])
        if relative.is_absolute() or '..' in relative.parts: raise Invalid('UML source path escape')
        if name in rows: raise Invalid('duplicate UML reference metamodel source: '+name)
        rows[name] = row
    verified = []
    for name in FILES:
        row = rows.get(name)
        if not row: raise Incomplete('UML reference metamodel source missing: '+name)
        path = (SOURCES/row['file']).resolve()
        if not path.is_relative_to(SOURCES.resolve()): raise Invalid('UML source path escape')
        if not path.is_file(): raise Incomplete('UML reference metamodel source missing: '+name)
        data = path.read_bytes()
        if sha(data) != row['sha256']: raise Invalid('UML reference metamodel fingerprint conflict: '+name)
        verified.append((name, data))
    return compile_schema(tuple(verified))


@lru_cache(maxsize=2)
def compile_schema(sources):
    types = {}; declarations = {}
    def target(element, source, role='type'):
        direct = element.get(role)
        if direct: return (source, direct)
        child = element.find(role)
        href = child.get('href') if child is not None else None
        if href:
            file, _, fragment = href.partition('#')
            return (Path(urlsplit(file).path).name or source, fragment)
        return None
    for filename, data in sources:
        xml = safe_xml(data)
        for element in xml.iter():
            if not isinstance(element.tag, str): continue
            identity = element.get('{'+XMI+'}id')
            kind = element.get('{'+XMI+'}type', '').split(':')[-1]
            if identity and kind in ('Class', 'DataType', 'Enumeration', 'PrimitiveType'):
                key = (filename, identity)
                types[key] = {'name': element.get('name'), 'kind': kind, 'parents': [], 'features': {},
                              'literals': {e.get('name') for e in element.findall('ownedLiteral')}}
                declarations[key] = element
    for key, element in declarations.items():
        spec = types[key]
        spec['parents'] = [target(e, key[0], 'general') for e in element.findall('generalization')]
        for feature in element.findall('ownedAttribute'):
            spec['features'][feature.get('name')] = {'type': target(feature, key[0]),
                'id': feature.get('{'+XMI+'}id'), 'file': key[0], 'sha256': sha(dict(sources)[key[0]])}
    def inherited(key, seen=None):
        seen = set() if seen is None else seen
        if key in seen or key not in types: return {}
        seen.add(key); fields = {}
        for parent in types[key]['parents']: fields.update(inherited(parent, seen.copy()))
        fields.update(types[key]['features']); return fields
    for key in types: types[key]['features'] = inherited(key)
    return types


def check(root):
    schema = source_schema(); identities = {}; object_types = {}; findings = []; uncovered = []
    checked = []; geometry = []
    def instance_type(element):
        if element in object_types: return object_types[element]
        explicit = element.get('{'+XMI+'}type')
        key = None
        if explicit and ':' in explicit:
            prefix, _, name = explicit.partition(':')
            family = FAMILIES.get(element.nsmap.get(prefix))
            if family: key = (family, name)
        elif namespace(element.tag) in FAMILIES:
            key = (FAMILIES[namespace(element.tag)], local(element.tag))
        else:
            parent = element.getparent()
            parent_type = instance_type(parent) if parent is not None else None
            feature = schema.get(parent_type, {}).get('features', {}).get(local(element.tag))
            if feature: key = feature['type']
        object_types[element] = key if key in schema else None
        if key is not None and key not in schema:
            findings.append({'rule_id':'UML-metaclass-exists','id':element.get('{'+XMI+'}id'),
                             'message':'Unknown standard metaclass: '+key[1],
                             'source':{'file':key[0]}})
        return object_types[element]
    def conforms(actual, expected, seen=None):
        if actual == expected: return True
        seen = set() if seen is None else seen
        if actual in seen: return False
        seen.add(actual)
        return any(conforms(parent, expected, seen.copy())
                   for parent in schema.get(actual, {}).get('parents', []))
    def finding(rule, element, message, basis):
        findings.append({'rule_id': rule, 'id': element.get('{'+XMI+'}id'),
                         'message': message, 'source': basis})
    for element in root.iter():
        if not isinstance(element.tag, str): continue
        identity = element.get('{'+XMI+'}id')
        if identity: identities[identity] = element
        instance_type(element)
    for element, kind in object_types.items():
        if kind is None: continue
        spec = schema[kind]
        for name, value in element.attrib.items():
            if namespace(name): continue
            feature = spec['features'].get(name)
            if not feature or schema.get(feature['type'], {}).get('kind') != 'Class': continue
            for reference in value.split():
                checked.append({'id': element.get('{'+XMI+'}id'), 'field': name, 'reference': reference,
                                'expected_type': feature['type'][1], 'source_id': feature['id']})
                referred = identities.get(reference)
                if referred is None:
                    finding('UML-local-reference-exists', element, 'Dangling '+name+' reference: '+reference, feature)
                elif instance_type(referred) is None:
                    uncovered.append('Referenced opaque/untyped element cannot be type-validated: '+reference)
                elif not conforms(instance_type(referred), feature['type']):
                    finding('UML-local-reference-type', element,
                            name+' requires '+feature['type'][1]+', found '+instance_type(referred)[1]+': '+reference, feature)
        for child in element:
            if not isinstance(child.tag, str): continue
            feature = spec['features'].get(local(child.tag))
            if not feature or schema.get(feature['type'], {}).get('kind') != 'Class': continue
            reference = child.get('{'+XMI+'}idref') or child.get('href')
            if not reference: continue
            path, mark, fragment = reference.partition('#')
            if child.get('href') and path:
                uncovered.append('Cross-file UML reference type remains unverified: '+reference); continue
            token = fragment if mark else reference
            referred = identities.get(token)
            checked.append({'id': element.get('{'+XMI+'}id'), 'field': local(child.tag), 'reference': token,
                            'expected_type': feature['type'][1], 'source_id': feature['id']})
            if referred is not None and instance_type(referred) is not None and not conforms(instance_type(referred), feature['type']):
                finding('UML-local-reference-type', element,
                        local(child.tag)+' requires '+feature['type'][1]+', found '+instance_type(referred)[1]+': '+token, feature)
        if kind in {('DC.xmi','Bounds'), ('DC.xmi','Dimension'), ('DC.xmi','Point')}:
            fields = ('x','y') if kind[1] == 'Point' else ('width','height') if kind[1] == 'Dimension' else ('x','y','width','height')
            row = {'id': element.get('{'+XMI+'}id'), 'type': kind[1], 'native_values': dict(element.attrib)}
            geometry.append(row)
            for field in fields:
                if field not in element.attrib:
                    uncovered.append('UMLDI '+kind[1]+' missing explicit '+field+'; no derived coordinate generated'); continue
                try: number = float(element.get(field))
                except ValueError: number = float('nan')
                basis = {'file':'DC.xmi','id':kind[1]+'-'+field}
                if not math.isfinite(number):
                    finding('UMLDI-finite-real-coordinate',element,'Finite '+field+' required',basis)
                elif field in ('width','height') and number < 0:
                    finding('UMLDI-non-negative-size',element,'Negative '+field+' is forbidden',
                            {'file':'DC.xmi','id':kind[1]+'-non_negative_size' if kind[1]=='Bounds' else 'Dimension-non_negative_dimension'})
        if kind == ('UMLDI.xmi', 'UMLClassDiagram') and (element.get('modelElement', '').strip() or element.find('modelElement') is not None):
            finding('UMLClassDiagram-no_modelElement',element,'UMLClassDiagram must have no modelElement',
                    {'file':'UMLDI.xmi','id':'UMLClassDiagram-no_modelElement'})
    return {'status': 'invalid' if findings else 'passed-bounded-checks', 'findings': findings,
            'capability_uncovered': sorted(set(uncovered)), 'checked_local_references': checked,
            'native_geometry': geometry, 'coordinate_policy': 'native values preserved; missing values remain uncovered; no layout generated',
            'scope': 'Source-derived local UML/UMLDI reference existence/type, explicit finite DC values and two DC size constraints, UMLClassDiagram modelElement prohibition.',
            'full_design_time_conformance': False}
