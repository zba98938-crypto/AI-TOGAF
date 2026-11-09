#!/usr/bin/env python3
"""Formal discovery gate: zero tests, failures, errors and skips are not passes."""
import argparse
import contextlib
import hashlib
import json
import sys
import unittest
from pathlib import Path


class ActualResults(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs);self.actual_results=[]
    def addSuccess(self,test):
        super().addSuccess(test);self.actual_results.append({'id':test.id(),'status':'passed'})
    def addFailure(self,test,err):
        super().addFailure(test,err);self.actual_results.append({'id':test.id(),'status':'failed'})
    def addError(self,test,err):
        super().addError(test,err);self.actual_results.append({'id':test.id(),'status':'error'})
    def addSkip(self,test,reason):
        super().addSkip(test,reason);self.actual_results.append({'id':test.id(),'status':'skipped'})
    def addExpectedFailure(self,test,err):
        super().addExpectedFailure(test,err);self.actual_results.append({'id':test.id(),'status':'expected-failure'})
    def addUnexpectedSuccess(self,test):
        super().addUnexpectedSuccess(test);self.actual_results.append({'id':test.id(),'status':'unexpected-success'})


def run(directory,out=None):
    suite = unittest.defaultTestLoader.discover(directory, pattern='test_*.py')
    count = suite.countTestCases()
    def ids(node):
        for item in node:
            if isinstance(item,unittest.TestSuite):yield from ids(item)
            else:yield item.id()
    discovered_ids=list(ids(suite))
    source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path(directory).glob('test_*.py'))}
    if out:
        out=Path(out).resolve()
        if out.is_relative_to(Path(directory).resolve()):raise ValueError('unit evidence must be outside test source')
        out.mkdir(parents=True,exist_ok=False)
        with (out/'unit-regressions.log').open('x') as stream:
            with contextlib.redirect_stdout(stream),contextlib.redirect_stderr(stream):
                result=unittest.TextTestRunner(verbosity=2,stream=stream,resultclass=ActualResults).run(suite)
    else:result = unittest.TextTestRunner(verbosity=2,resultclass=ActualResults).run(suite)
    stable=source_hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path(directory).glob('test_*.py'))}
    report = {'schema_version':'formal-unit-regressions/1','discovered':count,'source_stable':stable,
              'executed':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
              'skipped':len(result.skipped),
              'passed':count>0 and result.testsRun==count and result.wasSuccessful() and not result.skipped
                       and stable and len(result.actual_results)==count and all(r['status']=='passed' for r in result.actual_results)}
    if out:
        detail={**report,'test_ids':discovered_ids,'actual_results':result.actual_results,'test_source_sha256':source_hashes,
                'failure_details':[(test.id(),trace) for test,trace in result.failures],
                'error_details':[(test.id(),trace) for test,trace in result.errors],
                'skipped_details':[(test.id(),reason) for test,reason in result.skipped]}
        (out/'summary.json').write_text(json.dumps(detail,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report),flush=True)
    return 0 if report['passed'] else 3 if count==0 else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory')
    parser.add_argument('--out',type=Path,help='New immutable directory containing actual test IDs, logs and results')
    args=parser.parse_args()
    raise SystemExit(run(args.directory,args.out))
