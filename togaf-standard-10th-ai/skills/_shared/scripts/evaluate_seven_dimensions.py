#!/usr/bin/env python3
"""Aggregate scoped, current observations separately from actual acceptance gates."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from acceptance_gate import DIMENSIONS, evaluate_acceptance
from evidence_integrity import verify_reference
from execution_batch import current as current_runtime

ROOT = Path(__file__).resolve().parents[1]


def load(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        return default


def summarise(entries, observations, gates, root, current):
    records = []
    for entry in entries:
        identity = (entry['category'], entry['id'])
        selected = [r for r in observations if (r.get('category'), r.get('id')) == identity]
        dimensions = {}
        for dimension in DIMENSIONS:
            instances = []
            for observation in selected:
                if observation.get('dimension') != dimension:
                    continue
                errors = list(observation.get('errors', []))
                if observation.get('runtime_fingerprints') != current:
                    errors.append('runtime-fingerprint-stale')
                refs = observation.get('evidence', [])
                if not refs:
                    errors.append('missing-scoped-evidence')
                for ref in refs:
                    errors.extend(verify_reference(ref, root,
                        {'method_id': entry['id']} if entry['category'] == 'analysis-method' else {}))
                scoped = {k: v for k, v in observation.items() if k != 'runtime_fingerprints'}
                scoped['runtime_fingerprints_sha256'] = hashlib.sha256(json.dumps(
                    observation.get('runtime_fingerprints'), sort_keys=True).encode()).hexdigest()
                instances.append({**scoped, 'evidence_current': not errors,
                                  'errors': sorted(set(errors))})
            current_instances = [r for r in instances if r['evidence_current']]
            dimensions[dimension] = {
                'has_evidence': bool(instances), 'evidence_current': bool(current_instances),
                'verification_status': ('scoped-observation' if current_instances else
                                        'stale' if instances else 'not-assessed'),
                'instances': instances,
                'coverage_note': 'Evidence applies only to the listed instances/scopes/states; not universal coverage.'}
        gate = gates.get(identity)
        outcome = evaluate_acceptance(entry, gate or {}, root, current)
        records.append({'category': identity[0], 'id': identity[1], 'dimensions': dimensions,
                        'dimensions_present': sum(d['has_evidence'] for d in dimensions.values()),
                        'accepted': outcome['accepted'],
                        'acceptance_status': outcome['status'] if gate else 'not-submitted',
                        'acceptance_reasons': outcome['reasons']})
    grouped = defaultdict(list)
    for record in records:
        grouped[record['category']].append(record)
    summary = {'categories': {}}
    for category, rows in grouped.items():
        summary['categories'][category] = {
            'identities': len(rows),
            'dimensions_with_evidence': {d: sum(r['dimensions'][d]['has_evidence'] for r in rows) for d in DIMENSIONS},
            'dimensions_with_current_scoped_evidence': {d: sum(r['dimensions'][d]['evidence_current'] for r in rows) for d in DIMENSIONS},
            'accepted': sum(r['accepted'] for r in rows)}
    return {'schema_version': 'seven-dimension-status/2',
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'summary': summary, 'records': records,
            'notice': 'Scoped observations, current integrity and gate acceptance are distinct. Missing gates are not submitted, not fabricated failures.'}


def registry_entries(root):
    caps = load(root / 'capabilities.json')
    groups = [('artifact-family', load(root / 'artifacts.json')['artifacts'] + caps['work_products']),
              ('guide-work-product', caps['work_products']),
              ('view-template', caps['profiles']), ('analysis-method', caps['analysis_methods']),
              ('deliverable', load(root / 'deliverables.json')['deliverables'])]
    return [{**item, 'category': category} for category, items in groups for item in items]


def manifest_observations(path, root, current):
    """Read the saved manifest, checking its original output hashes and runtime."""
    manifest = load(path, {})
    if not manifest:
        return []
    folder = path.parent
    errors = []
    if manifest.get('implementation_dependencies_sha256') != {
            k: v for k, v in current.items() if k not in
            ('capabilities.json', 'artifacts.json', 'deliverables.json', 'metamodel.json')}:
        errors.append('manifest-runtime-stale')
    for key, name in [('capabilities_sha256', 'capabilities.json'), ('artifacts_sha256', 'artifacts.json'),
                      ('deliverables_sha256', 'deliverables.json'), ('metamodel_sha256', 'metamodel.json')]:
        if manifest.get(key) != current[name]:
            errors.append('manifest-registry-stale:' + name)
    model = load(folder / 'model.json', {})
    digest = hashlib.sha256(json.dumps(model, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    if manifest.get('model_sha256') != digest:
        errors.append('manifest-model-stale')
    model_views = {v['id']: v for v in model.get('views', [])}
    output_hashes = manifest.get('output_sha256', {})
    records = []
    for kind, entries in [('artifact', manifest.get('artifacts', [])), ('deliverable', manifest.get('deliverables', []))]:
        for item in entries:
            paths = [item[k] for k in ('path', 'json', 'coverage', 'svg', 'png', 'appendix') if item.get(k)]
            refs = []
            local_errors = list(errors)
            for name in paths:
                refs.append({'path': str((folder / name).relative_to(root)), 'sha256': output_hashes.get(name)})
            view = model_views.get(item.get('view_id'), {})
            identities = ([('artifact-family', item['id']), ('view-template', item['profile_id'])]
                          if kind == 'artifact' else [('deliverable', item['id'])])
            for category, identity in identities:
                for dimension in ('model', 'generation'):
                    records.append({'category': category, 'id': identity, 'dimension': dimension,
                        'view_id': item.get('view_id'), 'instance_id': item.get('instance_id'),
                        'scope_id': view.get('scope_id'), 'state_id': view.get('state_id'),
                        'runtime_fingerprints': current, 'evidence': refs,
                        'errors': local_errors, 'note': 'Saved output; content and professional judgement remain separate.'})
    return records


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, default=ROOT / 'reviews/seven-dimension-status.json')
    p.add_argument('--observations', type=Path)
    p.add_argument('--gates', type=Path, default=ROOT / 'reviews/capability-acceptance.json')
    p.add_argument('--manifest', type=Path, action='append')
    args = p.parse_args()
    current = current_runtime(ROOT)
    observations = load(args.observations, {}).get('records', []) if args.observations else []
    manifests = args.manifest or [ROOT / 'examples/full-capability' / layout / 'manifest.json'
                                 for layout in ('reference', 'adaptive')]
    for path in manifests:
        observations.extend(manifest_observations(path, ROOT, current))
    gate_rows = load(args.gates, {}).get('capabilities', [])
    gates = {(r.get('category'), r.get('id')): r.get('gate', r) for r in gate_rows}
    report = summarise(registry_entries(ROOT), observations, gates, ROOT, current)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report['summary'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
