#!/usr/bin/env python3
"""Run browser geometry checks on current profile exports; flags require review."""
import argparse
import copy
import json
import os
from pathlib import Path

from execution_batch import Batch, digest

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profiles', type=Path)
    parser.add_argument('--out', default=str(ROOT.parents[1] / 'output/profile-geometry'))
    args = parser.parse_args()
    source = args.profiles.resolve()
    if not (source / 'verification.json').is_file():
        destination = Path(args.out); destination.mkdir(parents=True, exist_ok=True)
        result = {'status': 'blocked', 'reason': 'profile-verification-missing', 'path': str(source / 'verification.json')}
        (destination / 'blocked.json').write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(result)); return 3
    verification = json.loads((source / 'verification.json').read_text())
    cases = [source / (r['profile_id'] + '.case.json') for r in verification['results']
             if r.get('output_kind') == 'diagram']
    svgs = [source / (r['profile_id'] + '-' + layout + variant + '.svg')
            for r in verification['results'] if r.get('output_kind') == 'diagram'
            for layout in ('reference', 'adaptive') for variant in ('', '-modified')]
    missing = [str(p) for p in [*cases, *svgs] if not p.is_file()]
    if not cases or missing:
        destination = Path(args.out); destination.mkdir(parents=True, exist_ok=True)
        result = {'status': 'blocked', 'reason': 'diagram-inputs-missing', 'missing': missing}
        (destination / 'blocked.json').write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(result)); return 3
    batch = Batch(args.out, inputs=[Path(__file__), source / 'verification.json', *cases, *svgs],
                  purpose='Browser text bounding boxes for each independent diagram, original and modified inputs, both layouts')
    folder = batch.directory
    (folder / 'inputs').mkdir()
    artifacts = []
    snapshots = {entry['original_path']: batch.directory / reference.removeprefix('run:')
                 for reference, entry in batch.external_inputs.items()}
    for case in cases:
        data = json.loads(case.read_text())
        pid = data['result']['profile_id']
        from verify_artifact_profiles import substantive_change
        for variant in ('', '-modified'):
            model = copy.deepcopy(data['input'])
            if variant:
                substantive_change(model, data['view'])
            payload = folder / 'inputs' / (pid + variant + '.json')
            payload.write_text(json.dumps(model, ensure_ascii=False, indent=2) + '\n')
            for layout in ('reference', 'adaptive'):
                artifacts.append({'view_id': pid + '-' + layout + variant,
                                  'json': str(payload.relative_to(folder)),
                                  'svg': str(snapshots[str(source / (pid + '-' + layout + variant + '.svg'))].relative_to(folder))})
    manifest = folder / 'manifest.json'
    manifest.write_text(json.dumps({'artifacts': artifacts, 'model_sha256': digest(source / 'verification.json'),
        'renderer_sha256': digest(ROOT / 'scripts/profile_render.py')}, ensure_ascii=False, indent=2) + '\n')
    batch.run(['node', ROOT / 'scripts/check_geometry.mjs', folder])
    geometry = folder / 'geometry-check.json'
    evidence, report = batch.finish(outputs=[manifest, geometry, *sorted((folder / 'inputs').glob('*.json'))],
                                   observations=['Observable geometry flags are not visual or semantic acceptance.'])
    result = json.loads(geometry.read_text())
    print(json.dumps({'batch': str(evidence), 'passed_execution': report['passed'],
                      'status': result['status'], 'checked': result['checked'], 'flagged': result['flagged']}, ensure_ascii=False))
    return 3 if result.get('status') == 'blocked' else int(not report['passed'] or result.get('status') != 'passed')


if __name__ == '__main__':
    raise SystemExit(main())
