"""UTF-8 native XML is authoritative; diagnostics and previews are derived."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

SCRIPTS = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared/scripts'
for path in (SCRIPTS, SCRIPTS.parent / 'vendor'):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

VERSIONS = {'bpmn': '2.0.2', 'uml': '2.5.1'}


def normalize(value):
    if value is None:
        return None
    if not isinstance(value, dict) or set(value) - {'language', 'version', 'xml', 'source_sha256'}:
        raise ValueError('native must contain language, version and UTF-8 xml only')
    language, version, text = value.get('language'), value.get('version'), value.get('xml')
    if language not in VERSIONS or version != VERSIONS[language]:
        raise ValueError('native requires explicit BPMN 2.0.2 or UML 2.5.1')
    if not isinstance(text, str):
        raise ValueError('native.xml must be a UTF-8 source string')
    data = text.encode('utf-8')
    if len(data) > 7 * 1024 * 1024:
        raise ValueError('native.xml exceeds the 7 MiB editor source limit')
    fingerprint = hashlib.sha256(data).hexdigest()
    if value.get('source_sha256') is not None and value['source_sha256'] != fingerprint:
        raise ValueError('native source fingerprint does not match xml')
    return {'language': language, 'version': version, 'xml': text, 'source_sha256': fingerprint}


def issue(category, message, code=None):
    return {'level': 'error' if category == 'validation_errors' else 'warning',
            'code': code or {'validation_errors': 'native-validation',
                             'missing_material': 'native-material-missing',
                             'capability_uncovered': 'native-capability-uncovered'}[category],
            'id': 'native', 'category': category, 'message': str(message)}


def blocker_category(message):
    return ('missing_material' if re.search(r'missing|not acquired|not obtained|not available|'
            r'package root required|XSD load failed|来源.*未|资料.*缺', str(message), re.I)
            else 'capability_uncovered')


def diagnose(native):
    from standards import check_native, safe_xml, Invalid, Incomplete
    groups = {'validation_errors': [], 'missing_material': [], 'capability_uncovered': []}
    report = {}
    try:
        declaration = re.match(r'\ufeff?\s*<\?xml\b[^?]*\bencoding\s*=\s*[\"\']([^\"\']+)', native['xml'], re.I)
        if declaration and declaration[1].lower().replace('_', '-') not in {'utf-8', 'utf8'}:
            raise Invalid('The source editor preserves UTF-8 XML; the declaration must use UTF-8')
        root = safe_xml(native['xml'].encode('utf-8'))
        for element in root.iter():
            for key, value in element.attrib.items():
                if key.rsplit('}', 1)[-1] != 'href':
                    continue
                resource = unquote(value.partition('#')[0])
                protocol = urlsplit(resource).scheme.lower()
                if (protocol and protocol not in {'http', 'https'}) or ('\\' in resource or resource.startswith(('/', '//'))
                        or '..' in resource.split('/')):
                    groups['validation_errors'].append(issue('validation_errors',
                        'Native editor resource reference is unsafe and will not be read: ' + value,
                        'native-unsafe-reference'))
        report = check_native(native['xml'].encode('utf-8'), native['language'], native['version'])
        explicit = report.get('diagnostic_groups')
        if isinstance(explicit, dict):
            for category in groups:
                groups[category].extend(issue(category, message) for message in explicit.get(category, []))
        else:
            groups['validation_errors'].extend(issue('validation_errors', message) for message in report.get('errors', []))
            for message in report.get('blockers', []):
                category = blocker_category(message)
                groups[category].append(issue(category, message))
    except Invalid as exc:
        groups['validation_errors'].append(issue('validation_errors', exc))
    except (Incomplete, FileNotFoundError) as exc:
        category = blocker_category(exc)
        groups[category].append(issue(category, exc))
    complete = report.get('full_language_acceptance') is True and not any(groups.values())
    if not complete and not groups['capability_uncovered']:
        groups['capability_uncovered'].append(issue('capability_uncovered',
            'Full applicable design-time obligations have not all been independently verified'))
    summary = {key: value for key, value in report.items() if key != 'native_inventory'}
    summary['native_inventory_count'] = len(report.get('native_inventory', []))
    return {**groups, 'valid': not groups['validation_errors'],
            'conformance_complete': complete, 'source_sha256': native['source_sha256'],
            'conformance_status': 'invalid' if groups['validation_errors'] else 'complete' if complete else 'incomplete',
            'authority': 'native.xml UTF-8 source bytes', 'standard_report': summary}


def generate(native, out, *, render=False, auto_layout=False):
    """Fixed local exchange and preview operation; no source normalization."""
    from standards import Invalid, Incomplete, make_package, safe_xml
    native = normalize(native)
    diagnostic = diagnose(native)
    if not diagnostic['valid']:
        raise Invalid('; '.join(i['message'] for i in diagnostic['validation_errors']))
    out = Path(out)
    data = native['xml'].encode('utf-8')
    extension = '.bpmn' if native['language'] == 'bpmn' else '.uml'
    (out / ('native' + extension)).write_bytes(data)
    (out / 'native-package.json').write_text(json.dumps(make_package(data, native['language'], native['version']), ensure_ascii=False, indent=2) + '\n')
    (out / 'native-diagnostics.json').write_text(json.dumps(diagnostic, ensure_ascii=False, indent=2) + '\n')
    preview = {'status': 'not-requested', 'auto_layout_requested': auto_layout,
               'source_sha256': native['source_sha256'], 'derived_layout': False}
    if render:
        try:
            if native['language'] == 'uml':
                root = safe_xml(data)
                if any(isinstance(e.tag, str) and 'UMLDI' in e.tag for e in root.iter()):
                    raise Incomplete('Preserving native UMLDI preview is not yet implemented; original DI remains in native.xml')
                if not auto_layout:
                    raise Incomplete('Native UML coordinates missing; explicitly select automatic layout to create a derived preview')
                from uml_render import render_native
                rendered = render_native(data, out / 'native-preview.svg')
                preview['derived_layout'] = True
            else:
                root = safe_xml(data)
                if not any(isinstance(e.tag, str) and e.tag == '{http://www.omg.org/spec/BPMN/20100524/DI}BPMNDiagram' for e in root.iter()):
                    raise Incomplete('Native BPMNDI coordinates missing; no derived BPMN auto-layout backend has been verified')
                from bpmn_render import render_native
                rendered = render_native(data, out / 'native-preview.svg')
            preview.update(status='succeeded', rendering=rendered,
                           full_language_acceptance=rendered.get('full_language_acceptance', False))
        except Incomplete as exc:
            category = blocker_category(exc)
            preview.update(status='blocked', category=category, issues=[issue(category, exc)])
    (out / 'native-preview.json').write_text(json.dumps(preview, ensure_ascii=False, indent=2) + '\n')
    hashes = {p.relative_to(out).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(out.rglob('*')) if p.is_file() and p.name != 'manifest.json'}
    manifest = {'schema_version': 'workbench-native-generation/1', 'runtime_stable': True,
                'job_status': 'blocked' if preview['status'] == 'blocked' else 'succeeded',
                'native_source_sha256': native['source_sha256'], 'source_authority': 'version native.xml',
                'exchange': 'native bytes preserved', 'preview': preview,
                'full_language_acceptance': diagnostic['conformance_complete'], 'output_sha256': hashes}
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return manifest
