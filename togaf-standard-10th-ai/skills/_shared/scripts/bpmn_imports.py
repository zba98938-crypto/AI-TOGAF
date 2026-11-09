"""Bounded local BPMN document identity and byte-preserving resource packages.

This implements the local BPMN subset of 2.0.2 sections 8.2.2 and 15.3.1/2.
Qualified identity resolution does not certify cross-document semantics or DI.
The official source files and their original logical identities are never edited.
"""
import base64
from collections import defaultdict
import hashlib
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote, urlsplit

BPMN = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
XSD = 'http://www.w3.org/2001/XMLSchema'
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
XMI = 'http://schema.omg.org/spec/XMI/2.1'
MAX_RESOURCES = 63  # main document plus resources must fit MAX_DOCUMENTS
MAX_DOCUMENTS = 64
MAX_TOTAL_BYTES = 64 * 1024 * 1024
MAX_DEPTH = 16
MAX_REFERENCES = 20000
DEFAULT_DOCUMENT_PATH = 'main.bpmn'
MAX_PATH_CHARS = 4096
MAX_REFERENCE_CHARS = 4096
# The acquired exchange and CMOF use different lexical names for these roles.
REFERENCE_ADAPTATIONS = {'calledElement': 'calledElementRef',
                        'eventDefinitionRef': 'eventDefinitionRefs',
                        'participantRef': 'participantRefs'}


def _invalid(message):
    from standards import Invalid
    raise Invalid(message)


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def resolved_path(value):
    try:
        try:
            # Python 3.13 non-strict resolution no longer raises for symlink
            # loops. Probe strictly so unsafe paths cannot become material gaps.
            return Path(value).resolve(strict=True)
        except FileNotFoundError:
            # An absent source or new output is legitimate; callers still
            # enforce package containment and classify missing source material.
            return Path(value).resolve(strict=False)
    except (RuntimeError,OSError) as exc:
        _invalid('BPMN filesystem path cannot be safely resolved: '+str(exc))


def document_path(value=None):
    """A stored package identity is canonical, relative and URI-free."""
    value = DEFAULT_DOCUMENT_PATH if value is None else value
    if not isinstance(value, str) or not value or len(value) > MAX_PATH_CHARS or '\\' in value or any(ord(c)<32 or ord(c)==127 for c in value):
        _invalid('invalid native document_path')
    if urlsplit(value).scheme or value.startswith(('/', '//')) or '?' in value or '#' in value:
        _invalid('unsafe native document_path: ' + value)
    if '%' in value:
        _invalid('encoded native document_path is prohibited: ' + value)
    parts = value.split('/')
    if any(p in ('', '.', '..') for p in parts):
        _invalid('native document_path must be canonical and stay in the package: ' + value)
    return '/'.join(parts)


def check_path_hierarchy(path, known):
    for other in known:
        if path.startswith(other+'/') or other.startswith(path+'/'):
            _invalid('native resource file/directory path conflict: '+path+' and '+other)


def relative_location(owner_path, value):
    """Resolve a URI reference against this document, never the package root."""
    if not isinstance(value, str) or not value or len(value) > MAX_PATH_CHARS:
        _invalid('BPMN import location is missing')
    if '%' in value or '\\' in value or any(ord(c)<32 or ord(c)==127 for c in value):
        _invalid('dangerous BPMN import location encoding: ' + value)
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or value.startswith('/'):
        _invalid('BPMN import location must be a package-relative path: ' + value)
    if parts.query or parts.fragment:
        _invalid('BPMN import location cannot contain a query or fragment: ' + value)
    decoded = unquote(parts.path)
    if decoded.split('/')[-1] in ('','.','..'):
        _invalid('BPMN import location identifies a directory rather than a document: '+value)
    # Never interpret a second encoding layer, encoded protocols or backslashes.
    if '%' in decoded or '\\' in decoded or '\x00' in decoded or urlsplit(decoded).scheme or decoded.startswith('/'):
        _invalid('dangerous decoded BPMN import location: ' + value)
    stack = list(PurePosixPath(document_path(owner_path)).parent.parts)
    for component in decoded.split('/'):
        if component in ('', '.'):
            continue
        if component == '..':
            if not stack:
                _invalid('BPMN import path escapes the package: ' + value)
            stack.pop()
        else:
            stack.append(component)
    if not stack:
        _invalid('BPMN import location does not identify a file: ' + value)
    return document_path('/'.join(stack))


def decode_resources(records, root_size=0, root_document_path=None, check_only=False):
    """Validate cardinality and encoded lengths before allocating decoded data."""
    if records is None:
        return {}
    if not isinstance(records, list) or len(records) > MAX_RESOURCES:
        _invalid('native resource count exceeds the supported budget')
    estimated = root_size
    identities = []
    for row in records:
        if not isinstance(row, dict) or set(row) != {'path', 'payload_encoding', 'content', 'sha256'}:
            _invalid('native resources require path, payload_encoding, content and sha256')
        key = document_path(row['path'])
        if root_document_path is not None and key == document_path(root_document_path):
            _invalid('native resource duplicates the authoritative main document: ' + key)
        if key in identities:
            _invalid('duplicate native resource path: ' + key)
        check_path_hierarchy(key,identities+([document_path(root_document_path)] if root_document_path is not None else []))
        identities.append(key)
        content = row['content']
        if row['payload_encoding'] != 'base64' or not isinstance(content, str):
            _invalid('native resource payload must be base64')
        if len(content) > ((MAX_TOTAL_BYTES + 2) // 3) * 4:
            _invalid('native resource encoded length exceeds the supported budget')
        if not isinstance(row['sha256'], str) or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
            _invalid('native resource requires a lowercase SHA-256 fingerprint')
        if len(content) % 4 or not re.fullmatch(r'[A-Za-z0-9+/]*={0,2}', content):
            _invalid('invalid native resource base64 encoding')
        padding = 2 if content.endswith('==') else 1 if content.endswith('=') else 0
        estimated += len(content) // 4 * 3 - padding
        if estimated > MAX_TOTAL_BYTES:
            _invalid('native resource decoded total exceeds the supported budget')
    if check_only:
        return {}
    decoded = {}
    total = root_size
    for row, key in zip(records, identities):
        try:
            value = base64.b64decode(row['content'], validate=True)
        except (ValueError, TypeError) as exc:
            _invalid('invalid native resource base64: ' + str(exc))
        total += len(value)
        if total > MAX_TOTAL_BYTES:
            _invalid('native resource decoded total exceeds the supported budget')
        if _sha(value) != row['sha256']:
            _invalid('native resource fingerprint mismatch: ' + key)
        decoded[key] = value
    return decoded


def encode_resources(values):
    return [{'path': path, 'payload_encoding': 'base64',
             'content': base64.b64encode(data).decode('ascii'), 'sha256': _sha(data)}
            for path, data in sorted(values.items())]


def _read_resource_bytes(path):
    """Separate bounded reading makes rejection-before-read independently testable."""
    size = path.stat().st_size
    if size > MAX_TOTAL_BYTES:
        _invalid('BPMN resource exceeds the supported byte budget')
    with path.open('rb') as stream:
        data = stream.read(MAX_TOTAL_BYTES + 1)
    if len(data) > MAX_TOTAL_BYTES:
        _invalid('BPMN resource exceeds the supported byte budget')
    return data


def _role_model():
    """Use acquired BPMN classes, inheritance and native XSD element types."""
    from standards import safe_xml, SOURCES
    folder = SOURCES / 'bpmn-2.0.2'
    from standards import Incomplete
    try:
        cmof_bytes = (folder / 'BPMN20.cmof').read_bytes()
        schema_bytes = (folder / 'Semantic.xsd').read_bytes()
    except OSError as exc:
        raise Incomplete('normative BPMN import type source material missing: ' + str(exc)) from exc
    if _sha(cmof_bytes) != '72f5bf035da7bea80dc53131a22e6ba466789abd7437532e64abd3a7cff20139' or _sha(schema_bytes) != 'c4318842f7d2bbc262d7954c9452c501db16f0868eac0b8732ec5d7fb384d9a7':
        raise Incomplete('normative BPMN import type source fingerprint mismatch')
    cmof, schema = safe_xml(cmof_bytes), safe_xml(schema_bytes)
    classes, parents, properties = {}, {}, {}
    for node in cmof.iter():
        declared = node.get('{'+XMI+'}type', '')
        prefix, sep, kind = declared.partition(':')
        if sep and kind == 'Class' and node.nsmap.get(prefix) == 'http://schema.omg.org/spec/MOF/2.0/cmof.xml':
            name = node.get('name')
            classes[name] = node
            parents[name] = node.get('superClass', '').split()
            for prop in node:
                if prop.tag.rsplit('}', 1)[-1] == 'ownedAttribute' and prop.get('type'):
                    properties[(name, prop.get('name'))] = prop.get('type')
    types = {node.get('name'): node.get('type', '').split(':')[-1]
             for node in schema if node.tag == '{'+XSD+'}element' and node.get('name')}
    return classes, parents, properties, types, {
        'cmof_sha256': _sha(cmof_bytes), 'semantic_xsd_sha256': _sha(schema_bytes)}


class ResourceContext:
    """Documents are indexed by path and namespaces, never by global raw ID."""

    def __init__(self, data, package_root=None, resources=None, source_path=None):
        from standards import safe_xml
        self.main_path = document_path(source_path)
        self.explicit_context = package_root is not None or resources is not None or source_path is not None
        if len(data) > MAX_TOTAL_BYTES:
            _invalid('BPMN root exceeds the supported byte budget')
        self.embedded_mode = resources is not None
        self.values = decode_resources(resources, len(data), self.main_path)
        self.package_root = resolved_path(package_root) if package_root is not None else None
        self.documents = {}
        self.errors, self.missing, self.unsupported = [], [], []
        self.imports = []
        self.reachable = defaultdict(set)
        self.references = {}
        self.total_bytes = len(data) + sum(len(v) for v in self.values.values())
        self._safe_xml = safe_xml
        self._classes, self._parents, self._properties, self._types, self.type_basis = _role_model()
        from bpmn_data_compensation import _metamodel, _exchange_types
        try:
            subtype, graph = _metamodel()
            self._model_class, type_audit = _exchange_types(subtype, graph)
        except (OSError, ValueError) as exc:
            self._model_class=lambda node:None
            self.missing.append('normative BPMN import exchange type mapping material missing or unusable: '+str(exc))
            self.type_basis['exchange_type_mapping_status']='unusable'
        else:
            self.type_basis['exchange_type_mapping'] = type_audit
            self.type_basis['exchange_type_mapping_status']='available'
        self.type_basis['reference_name_adaptations'] = REFERENCE_ADAPTATIONS
        self._visit(self.main_path, data, 0)
        for extra in sorted(set(self.values) - set(self.documents)):
            self.errors.append('native resource is outside the explicit BPMN import closure: ' + extra)
        # Transitive visibility, including cycles, has a finite least fixed point.
        for path in self.documents:
            seen, queue = {path}, [path]
            while queue:
                current = queue.pop()
                for target in self.reachable[current]:
                    if target not in seen:
                        seen.add(target)
                        queue.append(target)
            self.documents[path]['visible_paths'] = seen

    @classmethod
    def from_root(cls, data, package_root=None, resources=None, document_path=None):
        return cls(data, package_root, resources, document_path)

    def _load(self, path):
        if path == self.main_path:
            return self.documents[path]['data']
        check_path_hierarchy(path,set(self.values)|set(self.documents))
        if path in self.values:
            return self.values[path]
        if self.embedded_mode or self.package_root is None:
            return None
        if len(self.values) >= MAX_RESOURCES:
            _invalid('BPMN resource count exceeds the supported budget')
        target = resolved_path(self.package_root / path)
        if not target.is_relative_to(self.package_root):
            _invalid('BPMN resource symbolic link escapes the package: ' + path)
        if not target.is_file():
            return None
        if target.stat().st_size > MAX_TOTAL_BYTES - self.total_bytes:
            _invalid('BPMN resource decoded total exceeds the supported budget')
        value = _read_resource_bytes(target)
        if len(value) > MAX_TOTAL_BYTES - self.total_bytes:
            _invalid('BPMN resource decoded total exceeds the supported budget')
        self.total_bytes += len(value)
        self.values[path] = value
        return value

    def _visit(self, path, data, depth):
        if path in self.documents:
            return
        if depth > MAX_DEPTH or len(self.documents) >= MAX_DOCUMENTS:
            _invalid('BPMN resource graph exceeds the depth/document budget')
        root = self._safe_xml(data)
        if root.tag != '{'+BPMN+'}definitions':
            self.errors.append('imported BPMN document root is not normative definitions: ' + path)
        ids = defaultdict(list)
        for node in root.iter():
            if isinstance(node.tag, str) and node.get('id'):
                ids[node.get('id').strip()].append(node)
        self.documents[path] = {'data': data, 'root': root,
                                'namespace': root.get('targetNamespace'), 'ids': ids}
        for element in root.findall('{'+BPMN+'}import'):
            loc = element.get('location')
            row = {'document_path': path, 'owner_xpath': root.getroottree().getpath(element),
                   'location': loc, 'namespace': element.get('namespace'),
                   'importType': element.get('importType')}
            self.imports.append(row)
            if element.get('importType') != BPMN:
                row['status'] = 'unsupported-import-type'
                self.unsupported.append('BPMN importType unsupported and not fetched: ' + str(element.get('importType')) + ' at ' + path + ':' + row['owner_xpath'])
                continue
            if any(owner.get('{http://www.w3.org/XML/1998/namespace}base') is not None
                   for owner in [element,*element.iterancestors()]):
                row['status']='unsupported-xml-base'
                self.unsupported.append('BPMN import xml:base resolution is outside the bounded document-path profile and is not read: '+path+':'+row['owner_xpath'])
                continue
            try:
                target_path = relative_location(path, loc)
                row['target_document_path'] = target_path
                if target_path not in self.documents and (depth + 1 > MAX_DEPTH or len(self.documents) >= MAX_DOCUMENTS):
                    _invalid('BPMN resource graph exceeds the depth/document budget')
                target_data = self._load(target_path)
            except ValueError as exc:
                self.errors.append(str(exc))
                row['status'] = 'invalid-location'
                continue
            if target_data is None:
                row['status'] = 'missing-material'
                self.missing.append('BPMN imported resource missing: ' + target_path + ' declared by ' + path)
                continue
            self._visit(target_path, target_data, depth + 1)
            target = self.documents[target_path]
            self.reachable[path].add(target_path)
            if element.get('namespace') != target['namespace']:
                row['status'] = 'namespace-mismatch'
                self.errors.append('BPMN import namespace mismatch: ' + path + ' declares ' + str(element.get('namespace')) + ' for ' + target_path + ' with targetNamespace ' + str(target['namespace']))
            else:
                row['status'] = 'resolved-local-document'

    def _class(self, node):
        return self._model_class(node)

    def _is_type(self, actual, expected):
        if not actual:
            return False
        seen, queue = set(), [actual]
        while queue:
            current = queue.pop()
            if current == expected:
                return True
            if current not in seen:
                seen.add(current)
                queue.extend(self._parents.get(current, []))
        return False

    def _expected(self, owner, field, role):
        if role == 'element':
            owner = owner.getparent()
        actual = self._class(owner)
        seen, queue = set(), [actual] if actual else []
        while queue:
            current = queue.pop(0)
            native_field = field if (current, field) in self._properties else REFERENCE_ADAPTATIONS.get(field, field)
            if (current, native_field) in self._properties:
                expected = self._properties[(current, native_field)]
                return expected if expected in self._classes else None
            if current not in seen:
                seen.add(current)
                queue.extend(self._parents.get(current, []))
        return None

    def resolve(self, path, owner, field, value, role='attribute'):
        """A receipt is bound to the owner/field, not a reusable QName whitelist."""
        root = self.documents[path]['root']
        value = value.strip() if value else ''
        if len(value) > MAX_REFERENCE_CHARS:
            _invalid('BPMN reference lexical length exceeds the supported budget')
        owner_xpath = root.getroottree().getpath(owner)
        key = (path, owner_xpath, role, field, value)
        if key in self.references:
            return self.references[key]
        if len(self.references) >= MAX_REFERENCES:
            _invalid('BPMN reference count exceeds the supported budget')
        row = {'document_path': path, 'owner_xpath': owner_xpath, 'role': role,
               'field': field, 'lexical_reference': value,
               'expected_class': self._expected(owner, field, role), 'status': None}
        self.references[key] = row
        if ':' in value:
            prefix, identity = value.split(':', 1)
            ns = owner.nsmap.get(prefix)
            if not ns or not identity or ':' in identity:
                row.update(status='namespace-unbound', message='BPMN QName namespace is unbound: ' + value)
                return row
            paths = self.documents[path]['visible_paths']
        else:
            identity, ns, paths = value, self.documents[path]['namespace'], {path}
        row.update(namespace=ns, native_id=identity)
        matching_paths = [p for p in paths if self.documents[p]['namespace'] == ns]
        if not matching_paths:
            imports = [i for p in paths for i in self.imports if i['document_path'] == p and i['namespace'] == ns]
            if any(i['status'] == 'unsupported-import-type' for i in imports):
                row.update(status='unsupported-import-type', message='BPMN QName uses an unsupported importType: ' + value)
            elif any(i['status'] == 'unsupported-xml-base' for i in imports):
                row.update(status='unsupported-xml-base', message='BPMN QName import xml:base resolution remains uncovered: ' + value)
            elif any(i['status'] == 'missing-material' for i in imports):
                row.update(status='missing-material', message='BPMN QName imported resource missing: ' + value)
            else:
                if self.explicit_context or self.imports:
                    row.update(status='namespace-not-imported', message='BPMN QName namespace has no matching explicit reachable import: ' + value)
                else:
                    row.update(status='external-identity-uncovered', message='external QName binding unresolved: ' + value)
            return row
        found = [(p, node) for p in matching_paths for node in self.documents[p]['ids'].get(identity, [])]
        if not found:
            message=('dangling BPMN reference' + (' element' if role=='element' else '') + ': ' + value
                     if matching_paths==[path] else 'BPMN imported reference ID missing: ' + value)
            row.update(status='missing-id', message=message)
            return row
        if len(found) != 1:
            row.update(status='ambiguous-id', message='BPMN namespace/ID reference is ambiguous: ' + value)
            return row
        target_path, target = found[0]
        actual = self._class(target)
        row.update(target_document_path=target_path, target_xpath=target.getroottree().getpath(target),
                   target_sha256=_sha(self.documents[target_path]['data']), actual_class=actual)
        # Existing independent same-document semantics remain the authority.
        if target_path != path and row['expected_class'] and not self._is_type(actual, row['expected_class']):
            row.update(status='type-mismatch', message='BPMN reference target type mismatch for ' + path + ':' + owner_xpath + '/' + field + ': expected ' + row['expected_class'] + ', actual ' + str(actual))
        else:
            row['status'] = 'resolved-local-identity'
            if target_path != path:
                row['semantic_status'] = 'cross-document-role-uncovered'
                row['type_status'] = 'verified' if row['expected_class'] else 'role-type-uncovered'
                row['message'] = 'Cross-document BPMN semantic role remains uncovered: ' + path + ':' + owner_xpath + '/' + field + '=' + value
        return row

    def report(self):
        refs = list(self.references.values())
        invalid = [r for r in refs if r['status'] in {'namespace-unbound','namespace-not-imported','missing-id','ambiguous-id','type-mismatch'}]
        missing = [r for r in refs if r['status'] == 'missing-material']
        unsupported = [r for r in refs if r['status'] in {'unsupported-import-type','unsupported-xml-base'}]
        return {'status': 'invalid' if self.errors or invalid else 'incomplete' if self.missing or self.unsupported or missing or unsupported or any(r['status']=='external-identity-uncovered' for r in refs) else 'complete',
                'scope': 'bounded local BPMN document/resource and qualified identity closure only',
                'document_path': self.main_path, 'document_count': len(self.documents),
                'resource_count': len(self.values), 'total_bytes': self.total_bytes,
                'documents': [{'path': p, 'sha256': _sha(d['data']), 'bytes': len(d['data']), 'targetNamespace': d['namespace']}
                              for p,d in sorted(self.documents.items())],
                'imports': self.imports, 'references': refs,
                'validation_errors': self.errors + [r['message'] for r in invalid],
                'missing_material': self.missing + [r['message'] for r in missing],
                'capability_uncovered': self.unsupported + [r['message'] for r in unsupported] + [r['message'] for r in refs if r.get('semantic_status') or r['status']=='external-identity-uncovered'],
                'reference_type_basis': self.type_basis,
                'limits': {'resources':MAX_RESOURCES,'documents':MAX_DOCUMENTS,'total_bytes':MAX_TOTAL_BYTES,'depth':MAX_DEPTH,'references':MAX_REFERENCES,'path_chars':MAX_PATH_CHARS,'reference_chars':MAX_REFERENCE_CHARS},
                'full_standard_acceptance': False}


def materialize_bundle(package, out):
    """Verify the complete graph before creating an exclusive new output directory."""
    from standards import package_bytes, check_native, Invalid, Incomplete, write_new
    data = package_bytes(package, 'bpmn', '2.0.2')
    records = package.get('resources', [])
    main = document_path(package.get('document_path'))
    report = check_native(data, 'bpmn', '2.0.2', resources=records, document_path=main)
    if report['errors']:
        raise Invalid('; '.join(report['errors']))
    if report['resource_closure']['status'] != 'complete':
        raise Incomplete('BPMN resource closure is incomplete: ' + '; '.join(report['resource_closure']['missing_material'] + report['resource_closure']['capability_uncovered']))
    values = decode_resources(records, len(data), main)
    values[main] = data
    out = Path(out)
    if out.exists() or out.is_symlink():
        raise Invalid('Refusing to overwrite a BPMN bundle output: ' + str(out))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.mkdir(exist_ok=False)
    outputs = {}
    try:
        for path, value in sorted(values.items()):
            target = out / path
            write_new(target, value)
            outputs[path] = {'sha256':_sha(value),'bytes':len(value)}
    except Exception:
        import shutil
        shutil.rmtree(out)
        raise
    return {'document_path':main,'outputs':outputs,'resource_closure':report['resource_closure'],
            'exchange_status':'preserved','semantic_loss':False,'full_standard_acceptance':False}
