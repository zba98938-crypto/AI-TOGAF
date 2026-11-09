#!/usr/bin/env python3
"""Compare the current local guide corpus with registered skill routes and outputs.

This is an inventory and trace comparison. It never grants source semantic or
visual equivalence from filenames, hashes, generated files, or old fidelity tags.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import uuid

from source_package import verify_package
from runtime_provenance import fingerprints

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parents[1]
REV = ROOT / 'reviews'
PACKAGE = REV / 'source-package-2026-11-02-v2'
ROUTE_REVIEW = REV / 'no-direct-figure-route-dispositions-2026-11-03.json'


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def locate(base, item):
    path = base / item['path']
    return path.is_file() and sha(path) == item['sha256']


def compare(english_root):
    package = read(PACKAGE / 'manifest.json')
    source_index = read(REV / 'source-coverage-unified.json')
    registry = read(ROOT / 'capabilities.json')
    evidence_registry = read(ROOT / 'evidence-registry.json')
    figure_evidence = {f['id']: f for f in evidence_registry['figures']}
    route_reviews = {r['figure_id']: r for r in read(ROUTE_REVIEW)['records']} if ROUTE_REVIEW.is_file() else {}
    profiles = {p['id']: p for p in registry['profiles']}
    methods = {m['id']: m for m in registry['analysis_methods']}
    manifests = {layout: read(ROOT / 'examples/full-capability' / layout / 'manifest.json')
                 for layout in ('reference', 'adaptive')}
    by_profile = {layout: defaultdict(list) for layout in manifests}
    for layout, manifest in manifests.items():
        for artifact in manifest['artifacts']:
            by_profile[layout][artifact['profile_id']].append(artifact)

    guide_records = []
    for guide in package['guides']:
        original = english_root / guide['source_pdf_name']
        chinese = WORK / 'togaf-standard-10th-zh' / Path(guide['chinese_text']['path']).name
        guide_records.append({
            'guide_id': guide['guide_id'], 'english_pdf_name': guide['source_pdf_name'],
            'english_pdf_sha256': guide['source_pdf_sha256'],
            'english_pdf_present': original.is_file(),
            'english_pdf_hash_match': original.is_file() and sha(original) == guide['source_pdf_sha256'],
            'chinese_markdown_name': chinese.name, 'chinese_markdown_present': chinese.is_file(),
            'chinese_markdown_hash_match': chinese.is_file() and sha(chinese) == guide['chinese_text']['sha256'],
            'english_extracted_pages': len(guide['english_page_text']),
            'definition_status': 'not-reviewed-by-this-inventory-comparison',
        })

    entries = []
    for entry in source_index['source_entries']:
        if entry['record_type'] == 'figure-json-and-assets':
            continue
        bilingual = (entry.get('bilingual_check') or {}).get('result')
        entries.append({
            'source_id': entry['source_id'], 'guide_id': entry['guide'],
            'record_type': entry['record_type'], 'disposition': entry.get('disposition'),
            'resolved_capability_refs': entry.get('resolved_capability_refs', []),
            'unresolved_refs': entry.get('candidate_or_unresolved_refs', []),
            'bilingual_result': bilingual or 'not-recorded',
            'comparison_status': 'recorded-deviation-requires-resolution' if bilingual == 'deviation'
                else 'bilingual-consistent-only' if bilingual == 'consistent'
                else 'english-semantic-check-pending',
        })

    figures = []
    for figure in package['figures']:
        route = figure['source_route']
        profile_ids = route.get('profile_ids', [])
        method_ids = route.get('method_ids', [])
        output = {}
        for layout, manifest in manifests.items():
            items = [item for pid in profile_ids for item in by_profile[layout].get(pid, [])]
            output[layout] = [{
                'profile_id': item['profile_id'], 'view_id': item['view_id'],
                'path': item['path'], 'json': item['json'],
                'saved_output_hash_match': all(
                    (ROOT / 'examples/full-capability' / layout / item[key]).is_file()
                    and sha(ROOT / 'examples/full-capability' / layout / item[key]) == manifest['output_sha256'].get(item[key])
                    for key in ('path', 'json', 'coverage') if item.get(key)),
            } for item in items]
        route_problems = []
        for pid in profile_ids:
            if pid not in profiles:
                route_problems.append('unregistered-profile:' + pid)
            else:
                p = profiles[pid]
                refs = p.get('source_refs', [])
                structures = p.get('source_structure_refs', [])
                normalized = figure['figure_id'].replace('/', '-')
                if figure['figure_id'] not in ' '.join(refs) and normalized not in ' '.join(structures):
                    route_problems.append('profile-source-reference-not-explicit:' + pid)
            for layout in manifests:
                if not by_profile[layout].get(pid):
                    route_problems.append('generated-profile-missing:' + layout + ':' + pid)
        for mid in method_ids:
            if mid not in methods:
                route_problems.append('unregistered-method:' + mid)
        crops = figure.get('english_original_crops', [])
        route_review = route_reviews.get(figure['figure_id'])
        route_review_asset_hash_match = bool(route_review and
            locate(ROOT, route_review['opened_asset']))
        source_status = figure_evidence.get(figure['figure_id'], {}).get('source_status')
        figures.append({
            'figure_id': figure['figure_id'], 'guide_id': figure['figure_id'].split('/')[0],
            'source_pdf_sha256': figure['source_pdf_sha256'],
            'source_json_hash_match': locate(PACKAGE, figure['original_json']),
            'interpretation_hash_match': locate(PACKAGE, figure['interpretation']),
            'english_crop_count': len(crops),
            'english_crops_hash_match': all(locate(PACKAGE, crop) for crop in crops),
            'historical_assets': [{
                'kind': a['kind'], 'historical_fidelity': a.get('historical_fidelity'),
                'portable_asset_hash_match': locate(PACKAGE, a['portable_asset']),
            } for a in figure['historical_assets'] if a.get('portable_asset')],
            'disposition': route['disposition'], 'profile_ids': profile_ids,
            'method_ids': method_ids, 'route_problems': route_problems,
            'source_status': source_status,
            'route_review': route_review['route_decision'] if route_review else None,
            'route_review_asset_hash_match': route_review_asset_hash_match,
            'outputs': output,
            'semantic_status': 'english-original-vs-interpretation-not-verified-by-machine',
            'visual_status': 'actual-original-and-output-opening-required',
        })

    all_output_mismatches = []
    for layout, manifest in manifests.items():
        folder = ROOT / 'examples/full-capability' / layout
        for rel, digest in manifest['output_sha256'].items():
            path = folder / rel
            if not path.is_file() or sha(path) != digest:
                all_output_mismatches.append(layout + ':' + rel)
    verification = verify_package(PACKAGE)
    findings = {
        'english_pdfs_hash_matched': sum(g['english_pdf_hash_match'] for g in guide_records),
        'chinese_markdown_hash_matched': sum(g['chinese_markdown_hash_match'] for g in guide_records),
        'chinese_pdfs_in_current_corpus': len(list((WORK / 'togaf-standard-10th-zh').rglob('*.pdf'))),
        'source_entries_by_type': dict(Counter(e['record_type'] for e in source_index['source_entries'])),
        'bilingual_consistent_entries': sum(e['bilingual_result'] == 'consistent' for e in entries),
        'bilingual_deviation_entries': sum(e['bilingual_result'] == 'deviation' for e in entries),
        'english_semantic_check_pending_entries': sum(e['comparison_status'] == 'english-semantic-check-pending' for e in entries),
        'figures_with_english_crop': sum(bool(f['english_crop_count']) for f in figures),
        'figures_without_english_crop': [f['figure_id'] for f in figures if not f['english_crop_count']],
        'direct_profile_routes': sum(bool(f['profile_ids']) for f in figures),
        'figure_route_problems': sum(bool(f['route_problems']) for f in figures),
        'no_direct_route_figures': sum(not f['profile_ids'] and not f['method_ids'] for f in figures),
        'no_direct_route_reviewed': sum(not f['profile_ids'] and not f['method_ids'] and
                                        f['route_review'] == 'no-direct-template-required' and
                                        f['route_review_asset_hash_match'] for f in figures),
        'saved_output_hash_mismatches': len(all_output_mismatches),
        'package_assets_checked': verification['assets_checked'],
        'package_integrity_errors': len(verification['errors']),
    }
    report = {
        'schema_version': 'source-skill-comparison/1', 'run_id': uuid.uuid4().hex,
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'scope': '26 project-local English PDFs, 1,910 source entries, 243 figure routes, 406 image assets, current dual-layout output',
        'english_source_root': str(english_root.resolve().relative_to(WORK)),
        'inputs_sha256': {str(path.relative_to(ROOT)): sha(path) for path in (
            PACKAGE / 'manifest.json', REV / 'source-coverage-unified.json',
            ROOT / 'capabilities.json', ROOT / 'evidence-registry.json', ROUTE_REVIEW,
            ROOT / 'examples/full-capability/reference/manifest.json',
            ROOT / 'examples/full-capability/adaptive/manifest.json')},
        'runtime_fingerprints': fingerprints(ROOT), 'summary': findings,
        'guide_records': guide_records, 'source_entries': entries, 'figures': figures,
        'output_hash_mismatches': all_output_mismatches,
        'source_package_verification': verification,
        'accepted': False,
        'limits': [
            'This audit checks inventory, routes, and actual saved output hashes; it does not validate English-Chinese meaning or diagram visual equivalence.',
            'A direct profile route is an implementation destination, not proof that the source figure structure is reproduced.',
            'Historical fidelity labels, including faithful, are never promoted to current acceptance.',
            'No-direct-route dispositions classify the role of source illustrations; they do not grant source-structure equivalence to reused templates.',
            'The source corpus README claims 26 Chinese PDFs, but none exist in its present directory.',
        ],
    }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--english-root', type=Path, default=WORK / 'togaf-standard-10th',
                        help='项目内英文原件目录；默认 togaf-standard-10th。')
    parser.add_argument('--out', type=Path, default=REV / 'actual-source-skill-comparison-2026-11-03.json')
    args = parser.parse_args()
    if args.english_root.resolve() != (WORK / 'togaf-standard-10th').resolve():
        parser.error('英文来源必须是当前项目只读目录 togaf-standard-10th')
    if ROOT not in args.out.resolve().parents:
        parser.error('output must stay inside skills/_shared')
    report = compare(args.english_root)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report['summary'], ensure_ascii=False, indent=2))
    return int(report['summary']['english_pdfs_hash_matched'] != 26
               or report['summary']['package_integrity_errors'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
