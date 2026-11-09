#!/usr/bin/env python3
"""Reproduce current engineering evidence in new directories; never grant acceptance."""
import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import sys

from execution_batch import Batch

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=['artifacts', 'cases', 'regression', 'all'], default='all')
    parser.add_argument('--method-review', type=Path)
    parser.add_argument('--out', default='reviews/development/current-runs')
    args = parser.parse_args()
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    os.environ['TOGAF_TEST_PORTABLE_RENDER'] = '1'
    chrome = Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    if 'TOGAF_BROWSER_PATH' not in os.environ and chrome.is_file():
        os.environ['TOGAF_BROWSER_PATH'] = str(chrome)
    inputs = [Path(__file__), ROOT/'capabilities.json', ROOT/'artifacts.json', ROOT/'deliverables.json']
    inputs += list((ROOT/'examples/method-cases').glob('*.md'))
    inputs += list((ROOT/'scripts').glob('*.py')) + list((ROOT/'scripts').glob('*.mjs'))
    inputs += list((ROOT/'tests').glob('test_*.py'))
    inputs += list((ROOT/'capability-addenda').glob('*.json'))
    inputs += list((ROOT/'examples/qianlin-synthetic').glob('*.py'))
    inputs += list((ROOT/'examples/qianlin-synthetic/dataset').rglob('*.json'))
    inputs += list((ROOT/'examples/library-delivery-validation').glob('*.py'))
    inputs += [ROOT/'examples/library-delivery-validation/raw-materials.json']
    if args.method_review:inputs.append(args.method_review.resolve())
    batch = Batch(args.out, inputs=inputs, purpose='Current stable development verification: '+args.phase)
    folder = batch.directory
    extra_outputs = []
    locations = {}

    def run(name, script, *arguments, required=False):
        row, result = batch.run([sys.executable, ROOT/script, *arguments])
        print(name, 'exit', result.returncode, flush=True)
        locations[name] = {'exit_code': result.returncode, 'stdout': row['stdout'], 'stderr': row['stderr']}
        if required and result.returncode:
            raise RuntimeError(name + ' failed; dependent generation stopped; original logs retained')
        return result

    failure = None
    try:
        if args.phase in ('artifacts', 'all'):
            run('profiles', 'scripts/verify_artifact_profiles.py', '--all', '--out', folder/'profiles', '--render', required=True)
            run('profile-geometry', 'scripts/verify_profile_geometry.py', folder/'profiles', '--out', folder/'geometry')
            run('machine-contracts', 'scripts/field_counterexamples.py', '--out', folder/'machine-counterexamples.json')
            run('skill-packages', 'scripts/verify_skill_packages.py', '--out', folder/'skill-packages.json')
            run('source-bundle', 'scripts/audit_source_current.py', '--bundle', '--out', folder/'source')
        if args.phase in ('cases', 'all'):
            qianlin = ROOT/'examples/qianlin-synthetic/runs'/batch.run_id
            library = ROOT/'examples/library-delivery-validation/runs'/batch.run_id
            run('qianlin-input', 'examples/qianlin-synthetic/build_model.py', '--out', qianlin, required=True)
            run('library-input', 'examples/library-delivery-validation/build_case.py', '--out', library, required=True)
            for layout in ('reference', 'adaptive'):
                run('qianlin-'+layout, 'scripts/generate.py', qianlin/'model.json', '--all', '--layout', layout,
                    '--out', folder/('qianlin-'+layout), '--render', required=True)
            run('library-generated', 'scripts/generate.py', library/'model.json', '--all',
                '--out', folder/'library-generated', '--render', required=True)
            run('deliverable-pages', 'scripts/render_deliverable_pages.py', '--input-dir',
                folder/'qianlin-reference/deliverables', '--out', folder/'pages')
            run('method-routes', 'scripts/verify_methods.py', '--out', folder/'methods')
            review_args = ['--review', args.method_review.resolve()] if args.method_review else []
            run('method-reasoning', 'scripts/verify_method_reasoning.py', *review_args)
            scale = ROOT/'examples/qianlin-synthetic/scale-runs'/batch.run_id
            repeat = scale.with_name(scale.name+'-repeat')
            run('scale', 'scripts/verify_scale_cases.py', '--out', scale, required=True)
            run('scale-repeat', 'scripts/verify_scale_cases.py', '--out', repeat, '--repeat-of', scale)
            extra_outputs += [p for directory in (qianlin, library, scale, repeat)
                              for p in directory.rglob('*') if p.is_file()]
            locations['external_runs'] = {k: str(v.relative_to(ROOT)) for k, v in
                [('qianlin',qianlin),('library',library),('scale',scale),('scale_repeat',repeat)]}
            run('seven-dimensions', 'scripts/evaluate_seven_dimensions.py',
                '--manifest', folder/'qianlin-reference/manifest.json',
                '--manifest', folder/'qianlin-adaptive/manifest.json',
                '--manifest', folder/'library-generated/manifest.json', '--out', folder/'seven-dimensions.json')
        if args.phase in ('regression', 'all'):
            run('full-regression', 'tests/run_acceptance_v2.py', '--report', folder/'acceptance.json')
    except Exception as error:
        failure = str(error)
    index = folder/'run-index.json'
    index.write_text(json.dumps({'schema_version':'development-run-index/1', 'run_id':batch.run_id,
        'phase':args.phase, 'locations':locations, 'interrupted_by':failure,
        'environment':{'system':platform.system(), 'machine':platform.machine(), 'python':platform.python_version(),
                       'browser':os.environ.get('TOGAF_BROWSER_PATH'),
                       'container_runtime':shutil.which('docker') or shutil.which('podman'),
                       'linux_execution':'performed' if platform.system()=='Linux' else 'not-performed'},
        'business_acceptance':'not-granted', 'source_semantic_acceptance':'not-granted-by-runner',
        'professional_review':'separate-from-execution'}, ensure_ascii=False, indent=2)+'\n')
    outputs = [p for p in folder.rglob('*') if p.is_file()] + extra_outputs
    evidence, report = batch.finish(outputs=outputs, observations=[
        'No historical run overwritten. Expected external evidence gaps remain explicit in each deliverable.',
        'A passing command batch proves the listed checks only, not universal source, visual or business acceptance.'])
    print(json.dumps({'run':str(folder), 'batch':str(evidence), 'passed':report['passed'] and failure is None,
                      'changed_runtime_paths':report['changed_runtime_paths'],
                      'changed_input_paths':report['changed_input_paths'], 'failure':failure}, ensure_ascii=False))
    return int(not report['passed'] or failure is not None)


if __name__=='__main__':raise SystemExit(main())
