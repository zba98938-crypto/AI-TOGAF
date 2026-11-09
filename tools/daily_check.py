#!/usr/bin/env python3
"""Small, non-rendering local check; formal evidence uses tests/verify_core.py."""
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TESTS = ('test_disk_growth_controls.py', 'test_package_links.py', 'test_profile_examples.py')


def main():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    checks = []
    for pattern in TESTS:
        result = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                                 '-s', 'tests', '-p', pattern], cwd=ROOT, env=env,
                                capture_output=True, text=True)
        checks.append({'check': pattern, 'passed': result.returncode == 0,
                       'detail': (result.stdout + result.stderr).strip().splitlines()[-1:] if result.returncode == 0
                                 else (result.stdout + result.stderr).strip().splitlines()[-12:]})
    query = subprocess.run([sys.executable, '-B', str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts/local_tool.py'),
                            'query', '业务能力', '--limit', '1'], cwd=ROOT, env=env,
                           capture_output=True, text=True)
    checks.append({'check': 'source-bound-query', 'passed': query.returncode == 0,
                   'detail': [] if query.returncode == 0 else query.stderr.strip().splitlines()[-3:]})
    report = {'mode': 'daily-smoke', 'rendered': False, 'saved_evidence': False,
              'passed': all(row['passed'] for row in checks), 'checks': checks}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
