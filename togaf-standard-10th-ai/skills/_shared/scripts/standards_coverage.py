#!/usr/bin/env python3
"""Source-derived design-time obligations; candidates never certify coverage.

Metamodel declarations and XSD particles have stable source locators. PDF modal
statements and figure captions remain candidates until their applicability and
meaning are adjudicated. Passing unrelated tests cannot close an obligation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
SOURCES = ROOT/'standards/sources'
KINDS = ('construct', 'attribute', 'reference', 'constraint', 'symbol', 'exchange')
XSD = 'http://www.w3.org/2001/XMLSchema'


def digest(data): return hashlib.sha256(data).hexdigest()
def local(tag): return tag.rsplit('}', 1)[-1] if isinstance(tag, str) else ''
def xml_attribute(element, name):
    return next((value for key, value in element.attrib.items() if local(key) == name), None)


def contained_file(base, relative):
    from standards import Invalid
    if not isinstance(relative, str) or not relative or urlsplit(relative).scheme:
        raise Invalid('coverage source requires a relative local path')
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts or '\\' in relative:
        raise Invalid('coverage path escape: '+relative)
    base = Path(base).resolve(); target = (base/path).resolve()
    if not target.is_relative_to(base): raise Invalid('coverage symlink escape: '+relative)
    if not target.is_file(): raise Invalid('coverage file missing: '+relative)
    return target


def verified_sources(language, version, sources_root=None):
    """Verify all selected normative and derived inputs before any extraction."""
    from standards import Invalid, Incomplete
    if (language, version) not in (('uml', '2.5.1'), ('bpmn', '2.0.2')):
        raise Invalid('coverage requires UML 2.5.1 or BPMN 2.0.2')
    base = Path(sources_root or SOURCES)
    rows = json.loads(contained_file(base, 'manifest.json').read_text())
    if not isinstance(rows, list): raise Invalid('standard source manifest must be a list')
    selected = [row for row in rows if row.get('language') == language+'-'+version or
                (language == 'uml' and row.get('language') == 'xmi-2.5.1')]
    found = {}; verified = []
    for row in selected:
        relative = row.get('file')
        if relative in found: raise Invalid('duplicate normative source: '+str(relative))
        path = contained_file(base, relative)
        actual = digest(path.read_bytes())
        if actual != row.get('sha256'): raise Invalid('normative source fingerprint conflict: '+relative)
        found[relative] = row
        verified.append({**row, 'verified_sha256': actual})
    main = language+'-'+version+'/'+('UML.xmi' if language == 'uml' else 'BPMN20.cmof')
    if main not in found: raise Incomplete('normative metamodel missing: '+main)
    for row in verified:
        if row.get('derived_from'):
            original = found.get(row['derived_from'])
            if not original or original['sha256'] != row.get('derived_from_sha256'):
                raise Invalid('derived normative source has no matching original: '+row['file'])
    return base, verified


def element_path(element):
    """Prefix-independent XML path; named particles survive sibling reordering."""
    segments = []
    while element is not None:
        segment = local(element.tag)
        if not segment: element = element.getparent(); continue
        name = element.get('name') or element.get('ref')
        if name: segment += '[name='+name+']'
        else:
            parent = element.getparent()
            if parent is not None:
                siblings = [child for child in parent if child.tag == element.tag]
                segment += '['+str(siblings.index(element)+1)+']'
        segments.append(segment); element = element.getparent()
    return '/'.join(reversed(segments))


def source_identities(row, root):
    """Logical tree identities supplement native IDs; official bytes stay intact.

    Source hashes remain evidence bindings rather than changing logical identity.
    Occurrence distinguishes repeated named nodes inside the same source owner.
    """
    identities = {}; occurrences = {}
    for element in root.iter():
        if not isinstance(element.tag, str): continue
        native_id = xml_attribute(element, 'id'); path = element_path(element)
        occurrence_key = (native_id, path)
        occurrences[occurrence_key] = occurrences.get(occurrence_key, 0)+1
        logical = {'file': row['file'], 'native_id': native_id, 'xml_path': path,
                   'occurrence': occurrences[occurrence_key]}
        identity_key = digest(json.dumps(logical, sort_keys=True, separators=(',', ':')).encode())
        identities[element] = {**logical, 'key': 'source-identity:'+identity_key,
                               'sha256': row['sha256'], 'source_line': element.sourceline}
    return identities


def source_identity_provenance(row, root):
    """Inventory all duplicate XML identities and leave bare references ambiguous.

    Context candidates describe syntactic containment only. They never resolve
    an XMI idref or supply a normative/semantic execution adaptation.
    """
    from collections import defaultdict
    from lxml import etree
    identities = source_identities(row, root); by_id = defaultdict(list)
    for element in identities:
        native_id = xml_attribute(element, 'id')
        if native_id: by_id[native_id].append(element)
    duplicate = {native_id: values for native_id, values in by_id.items() if len(values)>1}
    def record(element):
        owner = element.getparent()
        classifier = next((parent for parent in element.iterancestors()
                           if (xml_attribute(parent,'type') or '').split(':')[-1]
                           in {'Class','DataType','Enumeration','PrimitiveType','Stereotype'}), None)
        fragment = etree.tostring(element, method='c14n')
        return {'identity': identities[element], 'owner_identity': identities.get(owner),
                'classifier_identity': identities.get(classifier),
                'canonical_xml_fragment': fragment.decode(), 'canonical_fragment_sha256': digest(fragment),
                'fragment_serialization': 'c14n; original file bytes remain authoritative and unchanged'}
    groups = [{'native_id': native_id, 'occurrence_count': len(values),
               'occurrences': [record(element) for element in values]}
              for native_id, values in sorted(duplicate.items())]
    references = []
    for element in identities:
        for attribute, raw in element.attrib.items():
            if local(attribute)=='id': continue
            tokens = [raw[1:]] if local(attribute)=='href' and raw.startswith('#') else raw.split()
            for token_index, token in enumerate(tokens):
                if token not in duplicate: continue
                operation = next((parent for parent in (element, *element.iterancestors())
                                  if local(parent.tag)=='ownedOperation'), None)
                contextual = [candidate for candidate in duplicate[token]
                              if operation is not None and (candidate is operation or
                                  operation in candidate.iterancestors())]
                references.append({'source_identity': identities[element], 'attribute': attribute,
                    'raw_value': raw, 'token_index': token_index, 'native_idref': token,
                    'status': 'ambiguous-source-reference', 'resolved_target': None,
                    'candidates': [identities[candidate] for candidate in duplicate[token]],
                    'context_candidates': [identities[candidate] for candidate in contextual],
                    'context_basis': 'Same enclosing ownedOperation in the XML tree only; separate normative type/ownership evidence is required before any execution adaptation.',
                    'execution_adapter_applied': False, 'semantic_correction_applied': False})
    verified = row.get('verified_sha256')==row['sha256']
    return {'file': row['file'], 'sha256': row['sha256'], 'file_available': verified,
            'file_fingerprint_verified': verified, 'xml_well_formed': True,
            'identity_inventory_status': 'complete-with-known-duplicates' if duplicate else 'complete',
            'global_native_id_unique': not duplicate, 'native_id_count': len(by_id),
            'native_id_occurrences': sum(len(values) for values in by_id.values()),
            'duplicate_native_id_count': len(duplicate),
            'duplicate_occurrence_count': sum(len(values) for values in duplicate.values()),
            'duplicate_groups': groups, 'ambiguous_references': references,
            'global_identity_repair_applied': False, 'semantic_acceptance': 'not-established-by-source-provenance'}


def source_entry(language, version, row, element, kind, owner=None, identities=None):
    from lxml import etree
    native_id = xml_attribute(element, 'id')
    locator = 'xmi:id='+native_id if native_id else element_path(element)
    token = native_id or digest(locator.encode())[:24]
    body = element.findtext('specification/body') or element.findtext('body')
    result = {
        'id': ':'.join((language, version, kind, Path(row['file']).name, token)),
        'kind': kind, 'name': element.get('name') or local(element.tag),
        'declaration_kind': (xml_attribute(element, 'type') or local(element.tag)).split(':')[-1],
        'owner_id': owner, 'source': {'file': row['file'], 'sha256': row['sha256'],
                                    'locator': locator, 'xml_path': element_path(element),
                                    'fragment_sha256': digest(etree.tostring(element, method='c14n'))},
        'declaration': {'attributes': dict(element.attrib), 'body': body,
                        'type': element.get('type') or next((child.get('href') or child.get('idref')
                                for child in element if local(child.tag) == 'type'), None)},
        'applicability': 'design-time-declaration',
        'implementation_status': 'uncovered', 'implementation': [],
        'positive_tests': [], 'negative_tests': [], 'verification_status': 'not-executed',
    }
    if language=='uml':
        if identities is None: identities=source_identities(row,element.getroottree().getroot())
        result['source_identity']=identities[element]
        result['owner_identity']=identities.get(element.getparent())
    return result


def metamodel_entries(language, version, row, path, type_kinds=None):
    from standards import safe_xml
    root = safe_xml(path.read_bytes()); elements = list(root.iter())
    identities = source_identities(row,root) if language=='uml' else None
    scalar_ids = {xml_attribute(e, 'id') for e in elements if xml_attribute(e, 'id')
                  and (xml_attribute(e, 'type') or '').split(':')[-1]
                  in ('Enumeration', 'DataType', 'PrimitiveType')}
    result = []
    from collections import Counter
    native_counts = Counter(xml_attribute(element, 'id') for element in elements)
    for element in elements:
        if not isinstance(element.tag, str): continue
        tag = local(element.tag); declared = (xml_attribute(element, 'type') or '').split(':')[-1]
        native_id = xml_attribute(element, 'id')
        if not native_id: continue
        parent = element.getparent(); owner = xml_attribute(parent, 'id') if parent is not None else None
        if declared in ('Class', 'Association', 'Extension', 'Enumeration', 'DataType', 'PrimitiveType',
                        'Stereotype', 'Profile', 'Operation'):
            result.append(source_entry(language, version, row, element, 'construct', owner, identities))
            if 'DI' in Path(row['file']).stem or Path(row['file']).stem == 'DC':
                result.append(source_entry(language, version, row, element, 'symbol', owner, identities))
        elif tag in ('ownedAttribute', 'ownedEnd', 'ownedParameter'):
            target = element.get('type')
            type_child = next((child for child in element if local(child.tag) == 'type'), None)
            href = type_child.get('href') if type_child is not None else None
            imported_kind = None
            if href and '#' in href:
                source_path, fragment = href.rsplit('#',1)
                imported_kind = (type_kinds or {}).get((Path(urlsplit(source_path).path).name, fragment))
            primitive = target in scalar_ids or (type_child is not None and
                        (xml_attribute(type_child, 'type') or '').split(':')[-1] in ('PrimitiveType', 'DataType')) or \
                        imported_kind in ('Enumeration', 'DataType', 'PrimitiveType')
            kind = 'attribute' if primitive else 'reference'
            result.append(source_entry(language, version, row, element, kind, owner, identities))
        elif tag == 'ownedLiteral': result.append(source_entry(language, version, row, element, 'attribute', owner, identities))
        elif tag == 'ownedRule': result.append(source_entry(language, version, row, element, 'constraint', owner, identities))
        elif tag in ('generalization', 'packageImport', 'elementImport', 'profileApplication'):
            result.append(source_entry(language, version, row, element, 'reference', owner, identities))
    for item in result:
        identity = item['source']['locator'].removeprefix('xmi:id=')
        if native_counts[identity] > 1:
            path = item['source']['xml_path']
            item['id'] += '@'+digest(path.encode())[:16]
            item['source']['locator'] += ';path='+path
            item['source']['ambiguous_native_id'] = identity
    return result


def exchange_entries(language, version, row, path):
    from standards import safe_xml
    root = safe_xml(path.read_bytes()); result = []
    identities = source_identities(row,root) if language=='uml' else None
    for element in root.iter():
        if not isinstance(element.tag, str) or not element.tag.startswith('{'+XSD+'}'): continue
        if local(element.tag) in ('annotation', 'documentation', 'appinfo'): continue
        result.append(source_entry(language, version, row, element, 'exchange', identities=identities))
    return result


def prose_entries(language, version, row, path):
    """Retain line windows for every modal line and figure/table caption.

    This deliberately does not guess one obligation per sentence. Text windows
    may overlap and contain runtime/non-normative statements. Their explicit
    adjudication is a completeness prerequisite, rather than a test-count proxy.
    """
    from standards import Invalid
    extraction = json.loads(path.read_text())
    if extraction.get('pdf_sha256') != row.get('derived_from_sha256'):
        raise Invalid('PDF extraction fingerprint conflict')
    pages = extraction.get('pages', [])
    if extraction.get('page_count') != len(pages) or [p.get('pdf_page') for p in pages] != list(range(1, len(pages)+1)):
        raise Invalid('normative PDF page coverage gap')
    result = []
    modal = re.compile(r'\b(must|shall|required|prohibited)\b', re.I)
    caption = re.compile(r'^\s*(Figure|Table)\s+\d+(?:[.-]\d+)*\b')
    seen = set()
    for page in pages:
        lines = page['text'].splitlines()
        for i, line in enumerate(lines):
            if not modal.search(line) and not caption.match(line): continue
            first, last = max(0, i-2), min(len(lines), i+5)
            text = '\n'.join(lines[first:last]); token = digest(text.encode())[:24]
            key = (page['pdf_page'], token)
            if key in seen: continue
            seen.add(key)
            symbol = bool(caption.match(line)) or bool(re.search(r'notation|symbol|depict|draw|render', text, re.I))
            kind = 'symbol' if symbol else 'exchange' if re.search(r'XMI|XML|interchange|schema', text) else 'constraint'
            result.append({'id': ':'.join((language, version, kind, Path(row['derived_from']).name,
                                          'p'+str(page['pdf_page']), token)),
                           'kind': kind, 'name': 'PDF modal/caption candidate',
                           'declaration_kind': 'prose-candidate',
                           'source': {'file': row['derived_from'], 'sha256': row['derived_from_sha256'],
                                      'locator': 'pdf-page='+str(page['pdf_page'])+',extracted-lines='+str(first+1)+'-'+str(last),
                                      'text_file': row['file'], 'text_sha256': row['sha256'],
                                      'fragment_sha256': digest(text.encode())},
                           'declaration': {'text': text}, 'applicability': 'unadjudicated',
                           'implementation_status': 'uncovered', 'implementation': [],
                           'positive_tests': [], 'negative_tests': [], 'verification_status': 'not-executed'})
    return result


def attach_bindings(entries, bindings):
    """Bind reviewed implementation/test locations; never infer execution."""
    from standards import Invalid
    by_id = {entry['id']: entry for entry in entries}
    for binding in bindings:
        identity = binding.get('obligation_id')
        if identity not in by_id: raise Invalid('coverage binding refers to missing obligation: '+str(identity))
        item = by_id[identity]
        for field in ('implementation', 'positive_tests', 'negative_tests'):
            verified = []
            for record in binding.get(field, []):
                path = contained_file(REPO, record.get('file'))
                if not record.get('symbol'): raise Invalid('coverage binding requires a concrete symbol')
                symbol = record['symbol']
                if path.suffix == '.py':
                    import ast
                    tree = ast.parse(path.read_text()); available = set()
                    for node in tree.body:
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)): available.add(node.name)
                        if isinstance(node, ast.ClassDef):
                            available.add(node.name)
                            available.update(node.name+'.'+method.name for method in node.body
                                             if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)))
                    if symbol not in available: raise Invalid('coverage symbol missing: '+record['file']+':'+symbol)
                elif path.suffix == '.java':
                    if not re.search(r'\b'+re.escape(symbol.rsplit('.',1)[-1])+r'\s*\(', path.read_text()):
                        raise Invalid('coverage Java symbol missing: '+symbol)
                # Keep both file fingerprint and executable/test symbol location.
                verified.append({**record, 'sha256': digest(path.read_bytes())})
            item[field] = verified
        item['implementation_status'] = 'partial' if item['implementation'] else 'uncovered'
        item['binding_basis'] = binding.get('basis', '')
        item['limitations'] = binding.get('limitations', [])


def attach_execution(entries, evidence):
    """A test result must match its bound file, symbol and all implementation hashes."""
    from standards import Invalid
    if evidence is None: return
    if evidence.get('schema_version') != 'native-standard-test-evidence/1':
        raise Invalid('unsupported standard test evidence format')
    sources = evidence.get('source_hashes', {})
    normative_sources = evidence.get('normative_source_hashes', {})
    tests = {}
    for row in evidence.get('tests', []):
        key = (row['file'], row['symbol'])
        if key in tests: raise Invalid('duplicate standard test evidence: '+str(key))
        tests[key] = row
    for item in entries:
        bound = item['implementation']+item['positive_tests']+item['negative_tests']
        if not bound: continue
        if normative_sources.get(item['source']['file']) != item['source']['sha256']:
            item['verification_status'] = 'stale-normative-source'; continue
        if any(sources.get(row['file']) != row['sha256'] for row in bound):
            item['verification_status'] = 'stale-source'; continue
        required = item['positive_tests']+item['negative_tests']
        results = [tests.get((row['file'], row['symbol'])) for row in required]
        if not item['positive_tests'] or not item['negative_tests'] or not all(results): continue
        if any(row.get('status') != 'passed' for row in results):
            item['verification_status'] = 'failed-or-not-executed'; continue
        item['verification_status'] = 'passed-bounded-fixtures'
        item['verification_results'] = results
        # Bindings for this package are bounded subsets. An implementation and
        # sample test pair cannot assert the full normative obligation satisfied.


def completeness(entries, source_complete, applicability_complete=False):
    """Every applicable obligation needs implementation and both executed oracles."""
    applicable = [item for item in entries if item.get('applicability') != 'not-applicable-reviewed']
    closed = [item for item in applicable if item.get('implementation_status') == 'implemented' and
              item.get('verification_status') == 'passed' and item.get('positive_tests') and item.get('negative_tests')]
    return {'status': 'complete' if source_complete and applicability_complete and applicable and len(closed) == len(applicable) else 'incomplete',
            'applicable_obligations': len(applicable), 'verified_obligations': len(closed),
            'source_scope_complete': source_complete, 'applicability_adjudication_complete': applicability_complete,
            'criterion': 'All applicable normative design-time obligations; unrelated test counts cannot close obligations.'}


def ledger(language, version, sources_root=None, bindings=None, evidence=None):
    base, sources = verified_sources(language, version, sources_root)
    entries = []; identity_provenance = []
    from standards import safe_xml
    type_kinds = {}
    for row in sources:
        path = contained_file(base, row['file'])
        if path.suffix not in ('.xmi','.cmof'): continue
        for element in safe_xml(path.read_bytes()).iter():
            identity = xml_attribute(element,'id') if isinstance(element.tag,str) else None
            if identity: type_kinds[(path.name,identity)] = (xml_attribute(element,'type') or '').split(':')[-1]
    for row in sources:
        path = contained_file(base, row['file'])
        if path.suffix in ('.xmi', '.cmof'): entries += metamodel_entries(language, version, row, path, type_kinds)
        if language=='uml' and path.suffix=='.xmi':
            identity_provenance.append(source_identity_provenance(row,safe_xml(path.read_bytes())))
        if path.suffix == '.xsd': entries += exchange_entries(language, version, row, path)
        if path.name.endswith('.pages.json'): entries += prose_entries(language, version, row, path)
    ids = [item['id'] for item in entries]
    if len(ids) != len(set(ids)):
        from standards import Invalid
        raise Invalid('duplicate source-derived coverage item')
    if bindings is None:
        path = ROOT/'standards/coverage-bindings.json'
        bindings = json.loads(path.read_text()) if path.is_file() else []
    selected = [binding for binding in bindings if binding.get('obligation_id', '').startswith(language+':'+version+':')]
    attach_bindings(entries, selected)
    attach_execution(entries, evidence)
    entries.sort(key=lambda item: item['id'])
    body = any(row.get('source_class') == 'official-normative-publication' for row in sources)
    source_defects = sorted({(item['source']['file'], item['source']['ambiguous_native_id'])
                             for item in entries if item['source'].get('ambiguous_native_id')})
    available_names = {Path(row['file']).name for row in sources}
    imported_names = set()
    from standards import safe_xml
    for row in sources:
        if Path(row['file']).suffix not in ('.xmi', '.cmof'): continue
        for element in safe_xml(contained_file(base, row['file']).read_bytes()).iter():
            href = element.get('href') if isinstance(element.tag, str) else None
            if href and Path(urlsplit(href.partition('#')[0]).path).suffix in ('.xmi', '.cmof'):
                imported_names.add(Path(urlsplit(href.partition('#')[0]).path).name)
    missing_imports = sorted(imported_names-available_names)
    blockers = ['Normative prose/caption applicability and semantic obligations have not been fully adjudicated.',
                'Every applicable obligation needs implementation, independent positive and negative oracles, and current executed evidence.',
                'Metamodel/DI inventories do not by themselves implement standard notation or editing.']
    if not body: blockers.insert(0, 'Normative specification body is missing.')
    if source_defects: blockers.append('Normative machine source contains duplicate IDs; entries retain disambiguating XML paths.')
    if missing_imports: blockers.append('Normative machine imports not acquired: '+', '.join(missing_imports))
    result = {'schema_version': 'native-design-time-coverage/1', 'language': language, 'version': version,
            'sources': sources, 'items': entries, 'item_count': len(entries),
            'by_kind': {kind: sum(item['kind'] == kind for item in entries) for kind in KINDS},
            'unadjudicated_prose_candidates': sum(item['applicability'] == 'unadjudicated' for item in entries),
            'completeness': completeness(entries, body and not source_defects and not missing_imports),
            'source_defects': [{'file': file, 'duplicate_native_id': identity} for file, identity in source_defects],
            'missing_machine_imports': missing_imports, 'blockers': blockers,
            'human_acceptance': 'pending', 'organization_approval': 'pending-signature'}
    if language=='uml':
        result['source_availability']={'status':'verified-local-files','file_count':len(sources),
            'file_accessibility_establishes_semantic_acceptance':False}
        result['source_identity_provenance']=identity_provenance
        result['source_identity_summary']={
            'duplicate_xml_native_id_count':sum(row['duplicate_native_id_count'] for row in identity_provenance),
            'duplicate_xml_occurrence_count':sum(row['duplicate_occurrence_count'] for row in identity_provenance),
            'ambiguous_reference_count':sum(len(row['ambiguous_references']) for row in identity_provenance),
            'global_native_id_unique':all(row['global_native_id_unique'] for row in identity_provenance),
            'global_identity_repair_applied':False,'semantic_correction_applied':False,
            'availability_and_inventory_do_not_close_design_time_scope':True}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--language', choices=('uml', 'bpmn'), required=True)
    parser.add_argument('--version', required=True); parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--test-evidence', type=Path, help='Explicit current executed test manifest; no inferred execution')
    args = parser.parse_args()
    from standards import write_new, Invalid, Incomplete
    try:
        result = ledger(args.language, args.version, evidence=json.loads(args.test_evidence.read_text()) if args.test_evidence else None)
        write_new(args.out, (json.dumps(result, ensure_ascii=False, indent=2)+'\n').encode())
        print(json.dumps({key: result[key] for key in ('language', 'version', 'item_count', 'by_kind', 'completeness')}))
        return 3 if result['completeness']['status'] != 'complete' else 0
    except (Invalid, Incomplete, ValueError, OSError) as exc:
        print(json.dumps({'status': 'blocked', 'reason': str(exc)})); return 3


if __name__ == '__main__': raise SystemExit(main())
