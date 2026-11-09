"""Maintainer-only synchronization of reviewed source availability and G152 topology.

Source crops and source-content reviews do not confer generated-view acceptance.
The current corpus is required; a distributed runtime never invents these assets.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
MISSING_SOURCE = 'no-renderable-source-image'
CURRENT_AVAILABILITY = 'reviewed-source-crop-available-generated-review-pending'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def locate_corpus(source=None, shared=ROOT):
    candidates = [Path(shared).resolve().parents[1]]
    if source is not None:
        candidates += [Path(source).resolve(), *Path(source).resolve().parents]
    for candidate in candidates:
        if (candidate / 'maintenance/pipeline/architecture_diagrams.py').is_file() and (candidate / 'architecture/diagrams/index.json').is_file():
            return candidate
    raise ValueError('Current reviewed corpus required; archived figure JSON cannot replace reviewed source semantics')


def current_structure(corpus, figure_id):
    path = corpus / 'architecture/diagrams' / (figure_id + '.json')
    module_path = corpus / 'maintenance/pipeline/architecture_diagrams.py'
    spec = importlib.util.spec_from_file_location('reviewed_source_export', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.portable_source_structure(load(path), current_path=str(path.relative_to(corpus.parent)), current_sha256=sha(path))


def source_evidence(corpus, shared, figure_id, reviews):
    graph_path = corpus / 'architecture/diagrams' / (figure_id + '.json')
    graph = load(graph_path)
    review = reviews['figures'][figure_id]
    source = graph['source']
    if review.get('review_status') != 'source-content-audited':
        raise ValueError(figure_id + ': current source-content review required')
    mapping = load(corpus / 'sources/relocation-manifest.json')['logical_paths']
    pdf = corpus / mapping[source['pdf_path']]
    if sha(pdf) != source['pdf_sha256'] or sha(pdf) != review['source_pdf_sha256']:
        raise ValueError(figure_id + ': reviewed PDF fingerprint mismatch')
    crop_rows = []
    for item in source['images']:
        crop = corpus / item['image_path']
        if sha(crop) != item['image_sha256']:
            raise ValueError(figure_id + ': source crop fingerprint mismatch')
        crop_rows.append({'path': 'corpus/' + item['image_path'], 'sha256': sha(crop), 'pdf_page': item['pdf_page']})
    if not crop_rows or sorted(x['sha256'] for x in crop_rows) != sorted(review['source_crop_sha256']):
        raise ValueError(figure_id + ': reviewed crop set mismatch')
    portable_map = load(shared / 'corpus/source-map.json')['logical_paths']
    pdf_relative = 'corpus/' + portable_map[source['pdf_path']]
    # Validate distributed byte identities as well as the authoring corpus.
    for item in [{'path': pdf_relative, 'sha256': source['pdf_sha256']}, *crop_rows]:
        path = shared / item['path']
        if not path.is_file() or sha(path) != item['sha256']:
            raise ValueError(figure_id + ': portable source asset missing or changed: ' + item['path'])
    portable_review_path = shared / 'corpus/maintenance/pipeline/architecture-diagram-reviews.json'
    if not portable_review_path.is_file() or load(portable_review_path).get('figures', {}).get(figure_id) != review:
        raise ValueError(figure_id + ': portable source review missing or stale; refresh source closure')
    return {'source_pdf': {'path': pdf_relative, 'logical_path': source['pdf_path'], 'sha256': source['pdf_sha256']},
            'source_crops': crop_rows,
            'source_review': {'path': 'corpus/maintenance/pipeline/architecture-diagram-reviews.json',
                              'logical_path': 'maintenance/pipeline/architecture-diagram-reviews.json', 'record_id': figure_id,
                              'record_sha256': hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
                              'status': review['review_status']},
            'generated_view_acceptance': 'not-established-by-source-review'}


def sync(shared=ROOT, corpus=None):
    shared = Path(shared).resolve()
    corpus = Path(corpus).resolve() if corpus else locate_corpus(shared=shared)
    # Read current JSON at mutation time; preserve unrelated profile changes.
    cap_path, registry_path = shared / 'capabilities.json', shared / 'evidence-registry.json'
    cap, registry = load(cap_path), load(registry_path)
    reviews = load(corpus / 'maintenance/pipeline/architecture-diagram-reviews.json')
    targets = {row['id'] for row in cap['figure_profiles']
               if row.get('current_semantic_review') == MISSING_SOURCE or row.get('source_availability_sync')}
    targets.add('G152/fig3-1')
    evidence = {fid: source_evidence(corpus, shared, fid, reviews) for fid in sorted(targets)}
    portable = current_structure(corpus, 'G152/fig3-1')
    relationships = portable['relationships']
    if any(r['from'] == 'value_chains' and r['to'] == 'capabilities' for r in relationships):
        raise ValueError('G152: unsupported value-chain-to-capability edge remains')
    if sum(r['explicit'] is True for r in relationships) != 5:
        raise ValueError('G152: expected five source arrows')
    if portable['flows'][0]['steps'][0] != 'capabilities':
        raise ValueError('G152: inherited six-arrow flow remains')
    portable['generated_view_acceptance'] = 'not-established-by-source-review'
    for rows in (cap['figure_profiles'], registry['figures']):
        for row in rows:
            if row['id'] not in targets:
                continue
            row.setdefault('historical_source_availability', {k: copy.deepcopy(row.get(k)) for k in ('source_status', 'current_semantic_review', 'asset_limitation') if k in row})
            row.update(source_status='original-pdf-crop-available', current_semantic_review=CURRENT_AVAILABILITY,
                       source_availability_sync=evidence[row['id']], generated_view_acceptance='not-established-by-source-review')
            if 'asset_limitation' in row:
                row['asset_limitation'] = '原PDF与裁剪图已存在且匹配来源审阅指纹；生成视图语义和视觉验收仍须单独执行。'
            if row['id'] == 'G152/fig3-1':
                row.update(current_source=portable['current_source'], historical_source=portable['historical_source'])
                if rows is registry['figures']:
                    row.update(purpose_summary=portable['reading']['purpose_zh'], misreadings=portable['reading']['misreadings_zh'],
                               uncertainty=portable['uncertainty'], visual_structure_review=portable['visual_structure_review'])
    write(shared / 'references/source-structures/G152-fig3-1.json', portable)
    write(cap_path, cap)
    write(registry_path, registry)
    return {'updated_figure_ids': sorted(targets), 'source_assets_verified': True,
            'portable_structure_ids': ['G152/fig3-1'], 'source_arrow_count': 5,
            'generated_view_acceptance': False, 'source_evidence': evidence}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = sync(corpus=args.corpus)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        write(args.report, result)
    print(json.dumps({k:v for k,v in result.items() if k != 'source_evidence'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
