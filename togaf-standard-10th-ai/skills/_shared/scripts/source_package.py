#!/usr/bin/env python3
"""Build and verify a portable source audit package, without upgrading reviews.

PDF coordinate/page declarations are inherited from source JSON, not independently
certified here. Only named review records can claim an actual image opening.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import uuid

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def safe_child(base, relative):
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('unsafe relative path: ' + str(relative))
    path = (Path(base) / relative).resolve()
    if not path.is_relative_to(Path(base).resolve()):
        raise ValueError('path escapes package: ' + str(relative))
    return path


def build_package(english_dir, corpus, out, registry=ROOT / 'evidence-registry.json'):
    import fitz
    english_dir, corpus, out = map(lambda p: Path(p).resolve(), (english_dir, corpus, out))
    if not out.is_relative_to(ROOT):
        raise ValueError('source package writes must remain under skills/_shared')
    if out.exists() and any(out.iterdir()):
        raise ValueError('use a new empty output directory; historical runs are immutable')
    out.mkdir(parents=True, exist_ok=True)
    data = read(registry)
    before = {}
    assets = {}
    def source(path):
        path = Path(path).resolve()
        before[str(path)] = sha(path)
        return before[str(path)]
    def record(path):
        path = Path(path)
        key = str(path.relative_to(out))
        assets[key] = {'path': key, 'sha256': sha(path), 'bytes': path.stat().st_size}
        return assets[key]
    def copy(path, dest):
        digest = source(path)
        target = safe_child(out, dest)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        item = record(target)
        if item['sha256'] != digest:
            raise ValueError('copy hash mismatch: ' + str(path))
        return item
    documents = {}
    guides = []
    for guide in data['guides']:
        gid = guide['path'][:4]
        pdf = english_dir / (gid + 'e.pdf')
        pdf_hash = source(pdf)
        doc = fitz.open(pdf)
        documents[gid] = doc
        page_records = []
        for page in doc:
            path = out / 'english-text' / gid / ('page-%03d.txt' % (page.number + 1))
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(page.get_text(sort=True))
            page_records.append({'page': page.number + 1, **record(path)})
        zh = copy(corpus / guide['path'], 'chinese-text/' + guide['path'])
        guides.append({'guide_id': gid, 'source_pdf_name': pdf.name,
                       'source_pdf_sha256': pdf_hash, 'pages': len(doc),
                       'source_pdf_archived_in_package': False,
                       'english_page_text': page_records, 'chinese_text': zh,
                       'text_extraction': 'PyMuPDF sort=True; page text is not a visual equivalent',
                       'definition_review': 'pending-per-capability-source-comparison'})
    copied_images = {}
    for asset in data['image_assets']:
        copied_images[asset['path']] = copy(corpus / asset['path'], 'original-assets/' + asset['path'])
    figures = []
    for figure in data['figures']:
        original = corpus / figure['json_path']
        raw = read(original)
        raw_copy = copy(original, 'original-json/' + figure['json_path'])
        portable = copy(ROOT / figure['portable_structure'], 'interpretations/' + Path(figure['portable_structure']).name)
        loc = raw.get('figure', {}).get('en_location') or {}
        pages, bboxes = loc.get('pages') or [], loc.get('bboxes') or []
        crops = []
        gid = figure.get('guide', figure['id'].split('/')[0])
        if len(pages) != len(bboxes):
            raise ValueError('page/bbox arity mismatch: ' + figure['id'])
        for index, (page_number, bbox) in enumerate(zip(pages, bboxes)):
            doc = documents[gid]
            if not isinstance(page_number, int) or not 1 <= page_number <= len(doc):
                raise ValueError('invalid PDF page: ' + figure['id'])
            page = doc[page_number - 1]
            rect = fitz.Rect(bbox)
            if rect.is_empty or not page.rect.contains(rect):
                raise ValueError('crop outside source page: ' + figure['id'])
            path = out / 'original-crops' / (figure['id'].replace('/', '-') + '-p%d-%d.png' % (page_number, index))
            path.parent.mkdir(parents=True, exist_ok=True)
            page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False).save(path)
            crops.append({'page': page_number, 'bbox': bbox, 'coordinate_basis': 'inherited-source-json-pdf-points', **record(path)})
        entries = []
        for asset in figure.get('assets', []):
            original_path = asset['path'].split('#')[0]
            entry = {'original_path': asset['path'], 'kind': asset.get('kind'),
                     'historical_fidelity': asset.get('historical_fidelity'),
                     'review_status': 'historical-claim-not-upgraded',
                     'historical_independent_verification': asset.get('independent_verification')}
            if original_path in copied_images:
                entry['portable_asset'] = copied_images[original_path]
            elif original_path.endswith('.md'):
                guide = next(g for g in guides if g['guide_id'] == gid)
                entry['portable_asset'] = guide['chinese_text']
                entry['locator'] = figure.get('md_locator')
            else:
                entry['missing_asset'] = original_path
            entries.append(entry)
        figures.append({'figure_id': figure['id'], 'title': figure.get('title'),
                        'original_json': raw_copy, 'interpretation': portable,
                        'source_pdf_sha256': next(g['source_pdf_sha256'] for g in guides if g['guide_id'] == gid),
                        'english_original_crops': crops,
                        'original_availability': 'pdf-coordinate-renditions-bundled' if crops else 'english-location-missing',
                        'actual_opening_this_build': False, 'semantic_review': 'not-performed-by-packaging',
                        'source_route': {k: figure.get(k) for k in ['disposition', 'disposition_reason', 'profile_ids', 'method_ids', 'conflict_ids']},
                        'historical_assets': entries})
    for doc in documents.values():
        doc.close()
    old_rows = read(ROOT / 'reviews/source-audit-assets-2026-11-01/missing-local-originals.json')
    by_id = {x['figure_id']: x for x in figures}
    relocations = []
    for row in old_rows:
        figure = by_id.get(row['id'], {})
        possible = [x for x in figure.get('english_original_crops', []) if x['page'] in row.get('en_pages', [])]
        relocations.append({'figure_id': row['id'], 'historical_path': row['crop'],
                            'replacement_assets': possible,
                            'status': 'portable-source-rendition-located' if possible else 'unresolved',
                            'same_bytes_as_historical_crop': any(x['sha256'] == row.get('pdf_crop_sha256') for x in possible),
                            'limit': 'new rendering at declared coordinates; historical crop hash/opening is not inherited'})
    candidates = read(ROOT / 'reviews/source-coverage-unified.json').get('candidates', [])
    caps = read(ROOT / 'capabilities.json')
    known = {x['id'] for key in ['work_products', 'profiles', 'analysis_methods'] for x in caps[key]}
    # Candidate resolutions also contain artifact family IDs. A valid family
    # route must not be reported as an unregistered profile or method.
    known.update(x['id'] for x in read(ROOT / 'artifacts.json')['artifacts'])
    route_audit = []
    for item in candidates:
        resolution = item.get('resolution') or {}
        ids = []
        for key in ['work_product_ids', 'profile_ids', 'method_ids', 'analysis_method_ids']:
            ids.extend(resolution.get(key, []))
        route_audit.append({'candidate_id': item['id'], 'registered_routes': list(dict.fromkeys(ids)),
                            'unknown_routes': sorted(set(ids) - known),
                            'semantic_equivalence': 'not-asserted-by-route-inventory',
                            'observations': item.get('observations', [])})
    changed = [name for name, digest in before.items() if sha(name) != digest]
    if changed:
        raise ValueError('original inputs changed during packaging: ' + str(changed))
    report = {'schema_version': 'portable-source-package/1', 'run_id': str(uuid.uuid4()),
              'created_at': datetime.now(timezone.utc).isoformat(),
              'builder_sha256': sha(__file__), 'evidence_registry_sha256': source(registry),
              'guides': guides, 'figures': figures,
              'image_assets': list(copied_images.values()), 'historical_relocations': relocations,
              'candidate_route_audit': route_audit,
              'original_inputs_unchanged': not changed,
              'summary': {'guides': len(guides), 'english_text_pages': sum(g['pages'] for g in guides),
                          'figure_records': len(figures), 'figures_with_original_crop': sum(bool(f['english_original_crops']) for f in figures),
                          'original_crop_assets': sum(len(f['english_original_crops']) for f in figures),
                          'original_image_assets': len(copied_images), 'candidate_records': len(route_audit),
                          'actual_image_openings': 0, 'definition_acceptances': 0},
              'assets': list(assets.values()),
              'limits': ['Mechanical portable inventory, not source authority certification or semantic acceptance.',
                         'PDF crop coordinates are inherited; captions/actual figure identity require visual comparison.',
                         'English text preserves page positions only; full PDF bytes remain at the original archive.',
                         'Historical fidelity, image openings and independent verdicts are not upgraded.']}
    write(out / 'manifest.json', report)
    return report


def verify_package(package):
    package = Path(package).resolve()
    manifest = read(package / 'manifest.json')
    errors = []
    seen = set()
    for asset in manifest.get('assets', []):
        try:
            path = safe_child(package, asset['path'])
            if asset['path'] in seen:
                errors.append('duplicate-asset:' + asset['path'])
            seen.add(asset['path'])
            if not path.is_file() or sha(path) != asset['sha256']:
                errors.append('missing-or-changed-asset:' + asset['path'])
        except (ValueError, KeyError):
            errors.append('unsafe-or-malformed-asset')
    for figure in manifest.get('figures', []):
        if not figure.get('source_route', {}).get('disposition'):
            errors.append('missing-source-disposition:' + figure['figure_id'])
    return {'schema_version': 'portable-source-package-verification/1',
            'run_id': manifest.get('run_id'), 'assets_checked': len(seen),
            'errors': errors, 'passed': not errors,
            'accepted': False, 'limit': 'Integrity and reachability only; not semantic or visual acceptance.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    build = sub.add_parser('build')
    build.add_argument('--english-dir', required=True)
    build.add_argument('--corpus', required=True)
    build.add_argument('--out', required=True)
    verify = sub.add_parser('verify')
    verify.add_argument('package')
    args = parser.parse_args()
    result = build_package(args.english_dir, args.corpus, args.out) if args.action == 'build' else verify_package(args.package)
    print(json.dumps(result.get('summary', result), ensure_ascii=False, indent=2))
    return int(result.get('passed') is False)


if __name__ == '__main__':
    raise SystemExit(main())
