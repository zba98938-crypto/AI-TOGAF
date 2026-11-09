"""Verify recorded evidence bytes and declared inputs without refreshing the ledger."""
from pathlib import Path
import argparse
import hashlib
import json
from report_outcome import engineering_complete, file_outcome, ledger_state

C = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def declared_inputs(root, report_path):
    """Only check published hash maps; absent maps are not proof of freshness."""
    if report_path.suffix != '.json':
        return []
    report = json.loads(report_path.read_text())
    if not isinstance(report, dict):
        return []
    rows = []
    for field in ('input_sha256', 'inputs', 'source_files'):
        mapping = report.get(field, {})
        if not isinstance(mapping, dict):
            continue
        for name, expected in mapping.items():
            if not isinstance(expected, str) or len(expected) != 64:
                continue
            candidates = [report_path.parent / name, root / name, root.parent / name]
            path = next((p for p in candidates if p.is_file()), candidates[0])
            actual = sha(path) if path.is_file() else None
            rows.append({'field': field, 'path': name, 'expected_sha256': expected,
                         'actual_sha256': actual, 'passed': actual == expected})
    # Hash the actual path set as well as existing bytes so newly added sources
    # cannot silently fall outside the scope of a previously passing release.
    for spec in report.get('input_file_sets', []):
        directory = root / spec['root']
        names = []
        if directory.is_dir():
            for path in directory.rglob('*'):
                relative = path.relative_to(directory)
                if not path.is_file() or (spec.get('exclude_symlinks') and path.is_symlink()):
                    continue
                if set(relative.parts) & set(spec.get('exclude_parts', [])):
                    continue
                if relative.parts[0] in spec.get('exclude_root_parts', []):
                    continue
                if relative.as_posix() in spec.get('exclude_files', []) or path.suffix in spec.get('exclude_suffixes', []):
                    continue
                names.append(relative.as_posix())
        actual = hashlib.sha256('\n'.join(sorted(names)).encode()).hexdigest() if directory.is_dir() else None
        rows.append({'field': 'input_file_sets', 'path': spec['root'],
                     'expected_sha256': spec['paths_sha256'], 'actual_sha256': actual,
                     'passed': actual == spec['paths_sha256']})
    return rows


def verify(root, ledger):
    rows = []
    issues = []
    items = ledger.get('items', [])
    if not items:
        issues.append({'code': 'empty-ledger'})
    for item in items:
        if not item.get('evidence'):
            issues.append({'id': item['id'], 'code': 'missing-evidence'})
        for evidence in item.get('evidence', []):
            path = root / evidence['path']
            actual = sha(path) if path.is_file() else None
            row = {'id': item['id'], 'path': evidence['path'],
                   'recorded_sha256': evidence.get('sha256'), 'actual_sha256': actual,
                   'fingerprint_current': actual is not None and actual == evidence.get('sha256')}
            if not row['fingerprint_current']:
                issues.append({'id': item['id'], 'path': evidence['path'],
                               'code': 'missing-evidence' if actual is None else 'stale-evidence'})
            try:
                row['declared_inputs'] = declared_inputs(root, path) if actual else []
                row['validation_outcome'] = file_outcome(path)
                row['explicit_validation_passed'] = row['validation_outcome']['passed']
                if item.get('state') == 'done' and ledger_state('done', [row['validation_outcome']]) != 'done':
                    issues.append({'id': item['id'], 'path': evidence['path'],
                                   'code': 'failed-evidence-for-complete-item',
                                   'outcome': row['validation_outcome']})
            except (ValueError, OSError) as exc:
                row['declared_inputs'] = []
                issues.append({'id': item['id'], 'path': evidence['path'],
                               'code': 'unreadable-evidence', 'detail': str(exc)})
            row['input_freshness'] = ('not-recorded' if not row['declared_inputs'] else
                                      'current' if all(x['passed'] for x in row['declared_inputs']) else 'stale')
            for dependency in row['declared_inputs']:
                if not dependency['passed']:
                    issues.append({'id': item['id'], 'path': evidence['path'],
                                   'code': 'stale-declared-input', 'input': dependency['path']})
            rows.append(row)
    if ledger.get('engineering_implementation_complete') is True and not engineering_complete(items, not issues):
        issues.append({'code': 'inconsistent-engineering-completion',
                       'detail': 'Stored completion is true but rows or evidence do not support completion.'})
    return {'schema_version': 'implementation-ledger-verification/1', 'passed': not issues,
            'counts': {'items': len(items), 'evidence_references': len(rows),
                       'stale_evidence_references': sum(not r['fingerprint_current'] for r in rows),
                       'issues': len(issues)},
            'issues': issues, 'evidence': rows,
            'scope_zh': '核对台账引用字节、明确登记的输入及done行是否引用显式失败报告；无输入指纹标记not-recorded，不补授测试、语义或业务验收。'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    ledger_path = C / 'quality/implementation-ledger.json'
    report = verify(C, json.loads(ledger_path.read_text()))
    report['input_sha256'] = {'quality/implementation-ledger.json': sha(ledger_path)}
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'passed': report['passed'], **report['counts'], 'issues': report['issues']}, ensure_ascii=False))
    return int(not report['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
