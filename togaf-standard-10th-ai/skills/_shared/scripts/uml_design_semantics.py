"""Source-derived local UML reference typing and bounded UMLDI diagnostics.

This does not evaluate the full metamodel, apply Profiles or draw UMLDI. XML,
including diagram coordinates and opaque extensions, remains authoritative.
"""
from functools import lru_cache
import json
import math
from pathlib import Path
import re
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
    types = {}; declarations = {}; enum_literals = {}; source_hashes = {name: sha(data) for name, data in sources}
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
            if identity and local(element.tag)=='ownedLiteral': enum_literals[(filename,identity)]=element.get('name')
            if identity and kind in ('Class', 'DataType', 'Enumeration', 'PrimitiveType'):
                key = (filename, identity)
                types[key] = {'name': element.get('name'), 'kind': kind, 'parents': [], 'features': {}, 'constraints': {},
                              'literals': {e.get('name') for e in element.findall('ownedLiteral')}}
                declarations[key] = element
    for key, element in declarations.items():
        spec = types[key]
        spec['parents'] = [target(e, key[0], 'general') for e in element.findall('generalization')]
        for rule in element.findall('ownedRule'):
            identity = rule.get('{'+XMI+'}id')
            spec['constraints'][identity] = {'file': key[0], 'id': identity,
                'sha256': source_hashes[key[0]], 'body': rule.findtext('specification/body')}
        for feature in element.findall('ownedAttribute'):
            lower, upper = feature.find('lowerValue'), feature.find('upperValue')
            lower = int(lower.get('value', '0')) if lower is not None else 1
            raw_upper = upper.get('value', '0') if upper is not None else '1'
            default = feature.find('defaultValue')
            spec['features'][feature.get('name')] = {'type': target(feature, key[0]),
                'id': feature.get('{'+XMI+'}id'), 'file': key[0], 'sha256': source_hashes[key[0]],
                'lower': lower, 'upper': None if raw_upper == '*' else int(raw_upper),
                'ordered': feature.get('isOrdered', 'false') == 'true',
                'unique': feature.get('isUnique', 'true') == 'true',
                'derived': feature.get('isDerived', 'false') == 'true',
                'aggregation': feature.get('aggregation', 'none'),
                'default': literal_value(default, key[0], enum_literals) if default is not None else None,
                'subsetted': [e.get('href') or e.get('{'+XMI+'}idref') for e in feature.findall('subsettedProperty')],
                'redefined': [e.get('href') or e.get('{'+XMI+'}idref') for e in feature.findall('redefinedProperty')]}
    def inherited(key, seen=None):
        seen = set() if seen is None else seen
        if key in seen or key not in types: return {}
        seen.add(key); fields = {}
        for parent in types[key]['parents']: fields.update(inherited(parent, seen.copy()))
        fields.update(types[key]['features']); return fields
    for key in types: types[key]['features'] = inherited(key)
    return types


def literal_value(element, filename=None, enum_literals=None):
    kind = element.get('{'+XMI+'}type', '').split(':')[-1]
    if kind=='InstanceValue': return (enum_literals or {}).get((filename,element.get('instance')))
    default = 'false' if kind == 'LiteralBoolean' else '' if kind == 'LiteralString' else '0'
    return element.get('value', default)


def instance_type(element, schema, cache=None):
    if element is None: return None
    cache = {} if cache is None else cache
    if element in cache: return cache[element]
    explicit = element.get('{'+XMI+'}type')
    key = None
    if explicit and ':' in explicit:
        prefix, _, name = explicit.partition(':')
        family = FAMILIES.get(element.nsmap.get(prefix))
        if family: key = (family, name)
    elif namespace(element.tag) in FAMILIES:
        key = (FAMILIES[namespace(element.tag)], local(element.tag))
    else:
        parent_type = instance_type(element.getparent(), schema, cache)
        feature = schema.get(parent_type, {}).get('features', {}).get(local(element.tag))
        if feature: key = feature['type']
    cache[element] = key
    return key


def conforms(schema, actual, expected, seen=None):
    if actual == expected: return True
    seen = set() if seen is None else seen
    if actual in seen: return False
    seen.add(actual)
    return any(conforms(schema, parent, expected, seen.copy())
               for parent in schema.get(actual, {}).get('parents', []))


def reference_values(element, name):
    """Keep direct, nested reference and contained-object encodings together."""
    rows = [(token, None) for token in element.get(name, '').split()]
    for child in element:
        if not isinstance(child.tag, str) or local(child.tag) != name: continue
        token = child.get('{'+XMI+'}idref') or child.get('href')
        if token:
            rows.extend((value, child) for value in (token.split() if child.get('{'+XMI+'}idref') else [token]))
        else:
            rows.append((child.get('{'+XMI+'}id'), child))
    return rows


def scalar_values(element, name):
    values = [element.get(name)] if name in element.attrib else []
    for child in element:
        if isinstance(child.tag, str) and local(child.tag) == name:
            values.append(child.get('value') if 'value' in child.attrib else child.text)
    return values


def scalar_value(element, name, schema, fallback=None):
    values = scalar_values(element, name)
    if values: return values[0]
    feature = schema.get(instance_type(element, schema), {}).get('features', {}).get(name, {})
    return feature.get('default') if feature.get('default') is not None else fallback


def check(root):
    schema = source_schema(); identities = {}; object_types = {}; findings = []; uncovered = []
    checked = []; geometry = []; cardinalities = []; primitive_values = []; constraints = []
    def finding(rule, element, message, basis):
        findings.append({'rule_id': rule, 'id': element.get('{'+XMI+'}id'),
                         'message': message, 'source': basis})
    for element in root.iter():
        if not isinstance(element.tag, str): continue
        identity = element.get('{'+XMI+'}id')
        if identity: identities[identity] = element
        kind = instance_type(element, schema, object_types)
        if kind is not None and kind not in schema:
            finding('UML-metaclass-exists', element, 'Unknown standard metaclass: '+kind[1], {'file':kind[0]})
    for element, kind in object_types.items():
        if kind not in schema: continue
        spec = schema[kind]
        for name, feature in spec['features'].items():
            target_kind = schema.get(feature['type'], {}).get('kind')
            if target_kind != 'Class':
                values = scalar_values(element, name)
                if feature['upper'] is not None and len(values) > feature['upper']:
                    finding('UML-property-upper-multiplicity', element, name+' exceeds upper multiplicity '+str(feature['upper']), feature)
                for raw in values:
                    type_name = schema.get(feature['type'], {}).get('name')
                    text = raw.strip() if isinstance(raw, str) else None
                    valid = True
                    if target_kind == 'Enumeration': valid = text in schema[feature['type']]['literals']
                    elif type_name == 'Boolean': valid = text in ('true', 'false', '1', '0')
                    elif type_name == 'Integer': valid = text is not None and bool(re.fullmatch(r'[+-]?\d+', text))
                    elif type_name == 'UnlimitedNatural': valid = text == '*' or (text is not None and bool(re.fullmatch(r'\+?\d+', text)))
                    elif type_name == 'Real':
                        valid = text is not None and bool(re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?', text))
                        if valid: valid = math.isfinite(float(text))
                    elif type_name == 'String': valid = isinstance(raw, str)
                    else: continue  # DataType structural content is checked on its own instance.
                    primitive_values.append({'id':element.get('{'+XMI+'}id'), 'field':name, 'raw_value':raw,
                        'type':type_name, 'valid':valid, 'source_id':feature['id']})
                    if not valid:
                        finding('UML-primitive-or-enumeration-value', element, 'Invalid '+str(type_name)+' value for '+name+': '+str(raw), feature)
                continue
            values = reference_values(element, name)
            # Only the explicitly bounded UMLDI ends need serialized lower bounds:
            # implicit UML opposites/derived properties are not invented as errors.
            lower_checked = feature['id'] in {'UMLClassifierShape-modelElement', 'UMLEdge-source', 'UMLEdge-target'}
            if values or lower_checked:
                cardinalities.append({'id':element.get('{'+XMI+'}id'), 'field':name, 'count':len(values),
                    'lower':feature['lower'], 'upper':feature['upper'], 'lower_checked':lower_checked, 'source_id':feature['id']})
            if feature['upper'] is not None and len(values) > feature['upper']:
                finding('UML-property-upper-multiplicity', element, name+' exceeds upper multiplicity '+str(feature['upper']), feature)
            if lower_checked and len(values) < feature['lower']:
                finding('UML-property-lower-multiplicity', element, name+' requires at least '+str(feature['lower'])+' value(s)', feature)
            for reference, child in values:
                path, mark, fragment = (reference or '').partition('#')
                if child is not None and child.get('href') and path:
                    uncovered.append('Cross-file UML reference type remains unverified: '+reference); continue
                token = fragment if mark else reference
                referred = identities.get(token) if token else child
                if referred is None and child is not None and not child.get('href') and not child.get('{'+XMI+'}idref'):
                    referred = child
                if token is None and referred is None: continue
                checked.append({'id': element.get('{'+XMI+'}id'), 'field': name, 'reference': reference,
                                'expected_type': feature['type'][1], 'source_id': feature['id']})
                if referred is None:
                    finding('UML-local-reference-exists', element, 'Dangling '+name+' reference: '+str(reference), feature)
                elif instance_type(referred, schema, object_types) not in schema:
                    uncovered.append('Referenced opaque/untyped element cannot be type-validated: '+str(reference))
                elif not conforms(schema, instance_type(referred, schema, object_types), feature['type']):
                    finding('UML-local-reference-type', element,
                            name+' requires '+feature['type'][1]+', found '+instance_type(referred, schema, object_types)[1]+': '+str(reference), feature)
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
        def rule(identity, passed, message, owner=kind):
            basis = schema.get(owner, {}).get('constraints', {}).get(identity)
            if basis is None: raise Incomplete('UMLDI constraint source missing: '+identity)
            constraints.append({'rule_id':identity,'id':element.get('{'+XMI+'}id'),'outcome':'true' if passed else 'false','source':basis})
            if not passed: finding(identity, element, message, basis)
        def refs(name):
            return [token.removeprefix('#') if token else None for token, _ in reference_values(element, name)]
        if conforms(schema, kind, ('UMLDI.xmi','UMLDiagram')):
            headings = refs('heading'); frame = str(scalar_value(element,'isFrame',schema)).strip() in ('true','1')
            rule('UMLDiagram-no-frame-no-heading', frame == bool(headings),
                 'A frame requires a heading and a heading requires a frame', ('UMLDI.xmi','UMLDiagram'))
            heading = identities.get(headings[0]) if len(headings)==1 else None
            if heading is not None:
                heading_refs = [token.removeprefix('#') if token else None for token, _ in reference_values(heading,'modelElement')]
                rule('UMLDiagram-heading_modelElement', set(heading_refs)==set(refs('modelElement')),
                     'Heading and diagram modelElement references differ', ('UMLDI.xmi','UMLDiagram'))
        if conforms(schema, kind, ('UMLDI.xmi','UMLCompartment')):
            rule('UMLCompartment-no_modelElement', not refs('modelElement'), 'Compartments must have no modelElement', ('UMLDI.xmi','UMLCompartment'))
        if conforms(schema, kind, ('UMLDI.xmi','UMLLabel')):
            rule('UMLLabel-modelElement_mult', len(refs('modelElement')) <= 1, 'Labels have at most one modelElement', ('UMLDI.xmi','UMLLabel'))
            rule('UMLLabel-no_icon', str(scalar_value(element,'isIcon',schema)).strip() in ('false','0'), 'Labels cannot use icon notation', ('UMLDI.xmi','UMLLabel'))
        if kind == ('UMLDI.xmi','UMLClassifierShape'):
            target = identities.get(refs('modelElement')[0]) if len(refs('modelElement'))==1 else None
            double = str(scalar_value(element,'isDoubleSided',schema)).strip() in ('true','1')
            active = target is not None and conforms(schema, instance_type(target,schema), ('UML.xmi','Class')) and str(scalar_value(target,'isActive',schema)).strip() in ('true','1')
            rule('UMLClassifierShape-doubleSided_isActive', not double or active, 'Double-sided shapes require an active Class')
        if kind == ('UMLDI.xmi','UMLStyle'):
            value = scalar_value(element,'fontSize',schema)
            if value is None:
                uncovered.append('UMLStyle-fontsize_positive optional absent fontSize requires null/applicability adjudication')
            else:
                try: positive = math.isfinite(float(value)) and float(value)>0
                except (ValueError,TypeError): positive = False
                rule('UMLStyle-fontsize_positive', positive, 'Explicit fontSize must be finite and greater than zero')
        if kind == ('DC.xmi','Color'):
            values=[scalar_value(element,field,schema) for field in ('red','green','blue')]
            if any(value is None for value in values):
                uncovered.append('DC Color missing explicit RGB component; no default value inferred')
            else:
                try: valid_rgb=all(re.fullmatch(r'[+-]?\d+',value.strip()) and 0<=int(value)<=255 for value in values)
                except (ValueError,TypeError): valid_rgb=False
                rule('Color-valid_rgb', valid_rgb, 'Explicit RGB components must be integers from 0 to 255')
    return {'status': 'invalid' if findings else 'passed-bounded-checks', 'findings': findings,
            'capability_uncovered': sorted(set(uncovered)), 'checked_local_references': checked,
            'checked_cardinalities':cardinalities,'checked_primitive_values':primitive_values,'checked_constraints':constraints,
            'native_geometry': geometry, 'coordinate_policy': 'native values preserved; missing values remain uncovered; no layout generated',
            'scope': 'Source-derived local reference type and explicit upper cardinality, selected UMLDI lower bounds, native scalar/enum values, finite geometry, and bounded UMLDI frame/heading/label/compartment/classifier constraints. Full UML opposites/derived/subset/redefinition and optional fontSize null applicability remain incomplete.',
            'full_design_time_conformance': False}
