#!/usr/bin/env python3
"""Execute selected native-standard oracles and bind their actual results to source.

An explicit output directory is required. Outputs are exclusive, so previous
evidence is retained. A bounded passing test suite cannot certify all UML/BPMN.
"""
import argparse
import hashlib
import inspect
import json
from pathlib import Path
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO/'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(REPO/'tests'))
sys.path.insert(0, str(ROOT/'scripts'))


def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def serialize(value):
    if isinstance(value, (set, tuple)): return sorted(value)
    if isinstance(value, Path): return str(value)
    raise TypeError(type(value).__name__)


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = {}; self.classes = set()

    def record(self, test, status, detail=None):
        self.classes.add(type(test))
        path = Path(inspect.getfile(type(test))).resolve()
        symbol = type(test).__name__+'.'+getattr(test, '_testMethodName', test.id())
        row = {'file': str(path.relative_to(REPO)) if path.is_relative_to(REPO) else str(path), 'symbol': symbol,
               'id': test.id(), 'status': status}
        if detail: row['detail'] = detail
        self.rows[test.id()] = row

    def addSuccess(self, test):
        super().addSuccess(test); self.record(test, 'passed')

    def addFailure(self, test, err):
        super().addFailure(test, err); self.record(test, 'failed', self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err); self.record(test, 'error', self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason); self.record(test, 'skipped', reason)

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err); self.record(test, 'expected-failure', self._exc_info_to_string(err, test))

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test); self.record(test, 'unexpected-success')

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err: self.record(test, 'failed', self._exc_info_to_string(err, subtest))


def write(path, value):
    with path.open('x') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, default=serialize)
        stream.write('\n')


def source_snapshot():
    paths = {path for path in (REPO/'tests').rglob('*')
             if path.suffix in {'.py', '.java', '.js', '.mjs', '.json', '.svg', '.ttf'}
             and '__pycache__' not in path.parts}
    paths.update(path for path in (REPO/'workbench').rglob('*')
                 if path.suffix in {'.py', '.js', '.mjs', '.json', '.html', '.css', '.svg', '.ttf'}
                 and '__pycache__' not in path.parts)
    paths.update((ROOT/'scripts').glob('*.py'))
    paths.update((ROOT/'scripts').glob('*.java'))
    paths.update((ROOT/'scripts').glob('*.mjs'))
    paths.update((ROOT/'standards').glob('*.json'))
    paths.add(ROOT/'standards/java/manifest.json')
    paths.update((ROOT/'standards/java').glob('*.jar'))
    paths.add(ROOT/'standards/sources/manifest.json')
    return {str(path.relative_to(REPO)): digest(path) for path in sorted(paths) if path.is_file()}


def run(modules, out):
    from standards_coverage import ledger
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()): raise ValueError('native evidence output directory must be empty')
    sources = source_snapshot()
    suite = unittest.defaultTestLoader.loadTestsFromNames(modules)
    discovered = suite.countTestCases()
    with (out/'execution.log').open('x') as log:
        result = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=RecordedResult).run(suite)
    after = source_snapshot()
    changes = sorted(path for path in sources.keys() | after.keys() if sources.get(path) != after.get(path))
    manifest = json.loads((ROOT/'standards/sources/manifest.json').read_text())
    normative_hashes = {}
    for row in manifest:
        path = (ROOT/'standards/sources'/row['file']).resolve()
        if not path.is_relative_to((ROOT/'standards/sources').resolve()): raise ValueError('normative source path escape')
        actual = digest(path)
        if actual != row['sha256']: raise ValueError('normative source hash mismatch: '+row['file'])
        normative_hashes[row['file']] = actual
    evidence = {'schema_version': 'native-standard-test-evidence/1', 'modules': modules,
                'discovered': discovered, 'executed': result.testsRun,
                'failures': len(result.failures), 'errors': len(result.errors), 'skipped': len(result.skipped),
                'tests': list(result.rows.values()), 'source_hashes': sources,
                'normative_source_hashes': normative_hashes, 'source_changed_during_execution': changes,
                'passed': discovered > 0 and discovered == result.testsRun and result.wasSuccessful()
                          and len(result.rows) == result.testsRun and all(row['status']=='passed' for row in result.rows.values())
                          and not result.skipped and not changes,
                'full_design_time_conformance': False, 'human_acceptance':'pending',
                'organization_approval':'pending-signature'}
    write(out/'test-evidence.json', evidence)
    retained = out/'retained-fixtures'; retained.mkdir()
    for cls in sorted(result.classes, key=lambda c: c.__module__+'.'+c.__name__):
        prefix = cls.__module__+'.'+cls.__name__
        if isinstance(getattr(cls, 'data', None), bytes): (retained/(prefix+'.input.uml')).write_bytes(cls.data)
        for attr in ('expected', 'report', 'good', 'rule'):
            value = getattr(cls, attr, None)
            if isinstance(value, dict): write(retained/(prefix+'.'+attr+'.json'), value)
    for language, version in (('uml','2.5.1'), ('bpmn','2.0.2')):
        write(out/(language+'-coverage.json'), ledger(language, version, evidence=evidence))
    print(json.dumps({k:evidence[k] for k in ('discovered','executed','failures','errors','skipped','passed','source_changed_during_execution')}))
    return 0 if evidence['passed'] else 1


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('modules', nargs='+')
    args=parser.parse_args()
    raise SystemExit(run(args.modules, args.out))
