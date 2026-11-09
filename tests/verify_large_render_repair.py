#!/usr/bin/env python3
"""Reproduce repaired representative SVG rendering, not business acceptance."""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from enterprise.cases import SHARED
from enterprise.runtime import save, sha256
from enterprise.stress import shape_input, shape_worker
from registry import load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--sizes', type=int, nargs='+', default=[100, 1000])
    args = parser.parse_args()
    if any(n < 1 or n > 10000 for n in args.sizes):
        parser.error('sizes must be between 1 and 10000')
    args.out.mkdir(parents=True, exist_ok=False)
    from runtime_provenance import fingerprints
    before = fingerprints(SHARED)
    profiles = load()[2]
    rows = []
    for family, pid in [('network', 'trust-framework-default'),
                        ('matrix', 'architecture-maturity-model-default'),
                        ('roadmap', 'risk-mitigation-plan-default'),
                        ('catalogue', 'compat-application-portfolio-catalog')]:
        for size in args.sizes:
            directory = args.out / (family + '-' + str(size))
            directory.mkdir()
            model = directory / 'input.json'
            save(model, shape_input(profiles[pid], size))
            started = time.monotonic()
            try:
                shape_worker(model, directory / 'generated', render=True)
                detail = json.loads((directory / 'generated/shape-result.json').read_text())
                row = {'family': family, 'objects': size, 'status': detail['status'],
                       'seconds': time.monotonic() - started, 'detail': detail}
            except Exception as exc:
                row = {'family': family, 'objects': size, 'status': 'fail',
                       'seconds': time.monotonic() - started, 'error': str(exc)}
            rows.append(row)
            print(json.dumps({k: v for k, v in row.items() if k != 'detail'}), flush=True)
            stable = before == fingerprints(SHARED)
            save(args.out / 'summary.json', {
                'status': 'pass' if stable and all(r['status'] == 'pass' for r in rows) else 'partial',
                'complete': len(rows) == 4 * len(args.sizes), 'runtime_stable': stable,
                'runtime_sha256': before, 'rows': rows, 'human_visual_status': 'pending',
                'boundary': 'Actual SVG topology and native-resolution crops; not monolithic PNG capacity, Mermaid capacity, native sandbox acceptance, or professional approval.'})
    return 0 if stable and all(r['status'] == 'pass' for r in rows) else 1


if __name__ == '__main__':
    raise SystemExit(main())
