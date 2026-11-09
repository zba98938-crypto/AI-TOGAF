#!/usr/bin/env python3
"""Run current skills regression checks without historical reports or datasets."""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import traceback
from pathlib import Path

from core_cases import (REPO, SHARED, delivery_cases, integrity_and_adm, production_profiles,
                        require, save, scale_cases, source_hashes, syntax_check)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--render', action='store_true', help='Export PNGs and run browser text geometry checks')
    parser.add_argument('--orders', type=int, default=1000)
    args = parser.parse_args()
    if args.orders <= 0:
        parser.error('--orders must be positive')
    out = args.out.resolve()
    if out.exists():
        parser.error('--out must be a new directory; previous evidence is immutable')
    if out.is_relative_to(REPO / 'togaf-standard-10th-ai/skills') or out.is_relative_to(REPO / 'tests'):
        parser.error('--out must be outside source directories')
    out.mkdir(parents=True)
    (out / 'logs').mkdir()
    before = source_hashes()
    save(out / 'source-before.json', before)
    rows = []
    def record(name, fn):
        started = time.monotonic()
        try:
            detail = fn()
            row = {'name': name, 'status': detail.pop('_status', 'pass'), 'detail': detail}
        except Exception as exc:
            row = {'name': name, 'status': 'fail', 'error': str(exc), 'traceback': traceback.format_exc()}
        row['seconds'] = round(time.monotonic() - started, 3)
        rows.append(row)
        save(out / 'progress.json', rows)
        print(json.dumps({k: v for k, v in row.items() if k not in ('detail', 'traceback')}, ensure_ascii=False), flush=True)
    def command(name, argv, expected=0, timeout=1800):
        result = subprocess.run([str(x) for x in argv], cwd='/tmp', capture_output=True, text=True, timeout=timeout)
        (out / 'logs' / (name + '.log')).write_text(result.stdout + result.stderr)
        detail = {'argv': [str(x) for x in argv], 'exit_code': result.returncode, 'expected_exit_code': expected}
        if result.returncode == 3 and expected == 0:
            return {**detail, '_status': 'blocked', 'reason': 'requested prerequisite unavailable'}
        require(result.returncode == expected, name + ': exit ' + str(result.returncode) + '\n' + (result.stdout + result.stderr)[-3000:])
        return detail
    py = sys.executable
    scripts = SHARED / 'scripts'
    record('syntax', lambda: syntax_check(out))
    record('unit-regressions', lambda: command('unit-regressions', [py, REPO/'tests/run_unit_regressions.py', REPO/'tests','--out',out/'unit-regressions']))
    for name, script, destination in (
        ('skill-packages', 'verify_skill_packages.py', out / 'packages.json'),
        ('method-case-constraints', 'verify_method_case_constraints.py', out / 'method-cases.json'),
        ('method-reasoning', 'verify_method_reasoning.py', out / 'method-reasoning.json'),
        ('methods', 'verify_methods.py', out / 'methods')):
        record(name, lambda n=name, s=script, d=destination: command(n, [py, scripts / s, '--out', d]))
    record('registry-consistency', lambda: command('registry-consistency', [py, scripts / 'registry_consistency.py']))
    record('production-profiles', lambda: production_profiles(out))
    record('deliverables', lambda: delivery_cases(out))
    record('integrity-adm', lambda: integrity_and_adm(out))
    profile_argv = [py, scripts / 'verify_artifact_profiles.py', '--all', '--out', out / 'profiles']
    if args.render:
        profile_argv.extend(['--render', '--oversized-policy', 'tile'])
    record('profile-expression', lambda: command('profile-expression', profile_argv))
    if args.render:
        record('text-geometry', lambda: command('text-geometry', [py, scripts / 'verify_profile_geometry.py', out / 'profiles', '--out', out / 'geometry']))
        record('mermaid-chinese', lambda: mermaid_smoke(out, command))
        record('visual-samples', lambda: visual_samples(out))
    else:
        rows.append({'name': 'browser-rendering', 'status': 'skipped', 'reason': 'enable --render to request PNG/browser stages'})
    record('scale-sql', lambda: scale_cases(out, args.orders))
    record('missing-historical-data', lambda: command('missing-historical-data', [py, scripts / 'verify_scale_cases.py', '--dataset-dir', out / 'missing-dataset', '--out', out / 'missing-scale'], expected=3))
    empty = out / 'empty-cases'
    empty.mkdir()
    for script in ('verify_method_case_constraints.py', 'verify_method_reasoning.py'):
        name = 'empty-' + script[:-3]
        record(name, lambda n=name, s=script: command(n, [py, scripts / s, '--cases-dir', empty, '--out', out / (n + '.json')], expected=3))
    after = source_hashes()
    save(out / 'source-after.json', after)
    changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
    record('source-integrity', lambda: {'unchanged': True} if not changed else require(False, changed))
    failures = [r['name'] for r in rows if r['status'] == 'fail']
    blocked = [r['name'] for r in rows if r['status'] == 'blocked']
    summary = {'schema_version': 'skills-core-regression/1', 'status': 'fail' if failures else 'blocked' if blocked else 'pass',
               'orders': args.orders, 'render_requested': args.render, 'results': rows, 'failures': failures,
               'blocked': blocked, 'source_changed': changed,
               'limits': ['Engineering checks do not grant professional/source-equivalence/business approval.',
                          'Text geometry does not verify edge routing or all visual semantics.',
                          'Missing historical architecture data is separate from synthetic SQL reconciliation.']}
    summary['evidence_sha256']={p.relative_to(out).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(out.rglob('*')) if p.is_file() and not p.is_symlink()
        and p not in (out/'summary.json',out/'progress.json')}
    save(out / 'summary.json', summary)
    print(json.dumps({'status': summary['status'], 'report': str(out / 'summary.json'), 'failures': failures, 'blocked': blocked}, ensure_ascii=False))
    return 1 if failures else 3 if blocked else 0


def mermaid_smoke(out, command):
    import shutil
    directory = out / 'mermaid'
    directory.mkdir()
    shutil.copyfile(SHARED / 'assets/fonts/NotoSansSC.ttf', directory / 'font.ttf')
    (directory / 'diagram.mmd').write_text('flowchart LR\n A[业务需求] --> B[架构评审]\n B --> C[证据与交付]\n')
    save(directory / 'jobs.json', {'font': 'font.ttf', 'jobs': [{
        'id': 'chinese', 'kind': 'mmd', 'source': 'diagram.mmd', 'svg': 'diagram.svg', 'png': 'diagram.png',
        'title': '中文渲染回归', 'legend': '显式流程关系；虚构示例', 'is_example': True}]})
    result = command('mermaid', ['node', SHARED / 'scripts/render.mjs', directory / 'jobs.json'])
    if result.get('_status') != 'blocked':
        require((directory / 'diagram.svg').is_file() and (directory / 'diagram.png').is_file(), 'Mermaid exports missing')
    return result


def visual_samples(out):
    import shutil
    sys.path.insert(0, str(SHARED / 'scripts'))
    from registry import load
    selected = {}
    for p in load()[2].values():
        if not p.get('alias_of') and p.get('output_kind', 'diagram') == 'diagram':
            selected.setdefault(p['renderer'], p['id'])
    dest = out / 'visual-samples'
    dest.mkdir()
    for renderer, pid in selected.items():
        source = out / 'profiles' / (pid + '-reference.png')
        require(source.is_file(), str(source))
        shutil.copyfile(source, dest / (renderer + '.png'))
    save(dest / 'index.json', selected)
    return {'renderer_families': len(selected), 'status': 'samples-retained-for-review'}


if __name__ == '__main__':
    raise SystemExit(main())
