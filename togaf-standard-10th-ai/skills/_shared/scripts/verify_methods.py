#!/usr/bin/env python3
"""Execute current registry calculators; keep professional method review separate.

Development fixtures are explicit input, not runtime package dependencies. Each CLI
execution is fresh and hash-bound. Expected outcomes are authored in tests, never
loaded from an old run. Exit 3 means required fixtures are unavailable.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
from execution_batch import Batch, digest

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(Path(path).read_text())


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')


def routes(root=ROOT):
    """Current examples, keyed by calculator identity; no historical review files."""
    result = {}
    for profile in read(root/'capabilities.json')['profiles']:
        for analysis in profile.get('example', {}).get('analyses', []):
            result.setdefault(analysis['method_id'], {'profile': profile, 'analysis_id': analysis['id']})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--method', action='append')
    parser.add_argument('--out', type=Path, default=ROOT.parents[1]/'output/method-runs')
    parser.add_argument('--fixtures', type=Path, default=ROOT.parents[1]/'tests/method_fixtures.py')
    parser.add_argument('--evaluate-input', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.evaluate_input:
        from analyze import evaluate
        try:
            result=evaluate(read(args.evaluate_input))
        except (ValueError, KeyError, TypeError) as exc:
            print(json.dumps({'status':'rejected','reason':str(exc)},ensure_ascii=False)); return 1
        print(json.dumps(result,ensure_ascii=False,indent=2)); return 0
    if not args.fixtures.is_file():
        save(args.out/'blocked.json', {'status':'blocked','reason':'authored-fixtures-missing','path':str(args.fixtures)})
        print(json.dumps({'status':'blocked','path':str(args.out/'blocked.json')})); return 3
    spec=importlib.util.spec_from_file_location('authored_method_fixtures',args.fixtures)
    fixture=importlib.util.module_from_spec(spec); spec.loader.exec_module(fixture)
    caps=read(ROOT/'capabilities.json')
    specs=[m for m in caps['analysis_methods'] if not args.method or m['id'] in args.method]
    if args.method and set(args.method)-{m['id'] for m in specs}: parser.error('unknown registered method')
    selected={m.get('calculator_id') or m.get('calculator') for m in specs}-{None}
    required=selected | ({'weighted-normalized-decision','environmental-delta','lean-serial-flow'} if not args.method else set())
    batch=Batch(args.out, inputs=[Path(__file__),args.fixtures,ROOT/'capabilities.json'],purpose='Current method calculator execution; professional review remains separate')
    records=[]
    exercised=set()
    from profile_examples import normalize_example
    mapping=routes()
    for mid in sorted(required & mapping.keys()):
        route=mapping[mid]; folder=batch.directory/mid; folder.mkdir()
        model=normalize_example(route['profile'])
        source=folder/'model.json'; save(source,model)
        run,completed=batch.run([sys.executable,ROOT/'scripts/analyze.py',source,'--evaluate',route['analysis_id']])
        row={'calculator_id':mid,'case':'registered-model-example','mode':'validated-model-binding','profile_id':route['profile']['id'], 'exit_code':completed.returncode}
        try:
            result=json.loads(completed.stdout)['analyses'][0]['result']
            row['oracle_passed']=completed.returncode==0 and bool(fixture.embedded_oracle(mid,result))
            save(folder/'result.json',result)
        except (ValueError,KeyError,TypeError) as exc:
            row['oracle_passed']=False;row['reason']=str(exc)
        records.append(row)
        if row['oracle_passed']:exercised.add(mid)
    for case in fixture.direct_cases():
        mid=case['method_id']
        if mid not in required: continue
        folder=batch.directory/mid; folder.mkdir(exist_ok=True)
        source=folder/(case['case']+'.input.json')
        save(source,{'id':case['case'],'method_id':mid,'inputs':case['inputs']})
        expected=1 if case['reject'] else 0
        run,completed=batch.run([sys.executable,Path(__file__),'--evaluate-input',source],expected=expected)
        row={'calculator_id':mid,'case':case['case'],'mode':'direct-call-no-model-binding','negative':case['reject'],'exit_code':completed.returncode}
        try:
            result=json.loads(completed.stdout)
            row['oracle_passed']=run['matches_expected'] and (result.get('status')=='rejected' if case['reject'] else bool(case['oracle'](result['result'])))
            save(folder/(case['case']+'.result.json'),result)
        except (ValueError,KeyError,TypeError) as exc:
            row['oracle_passed']=False;row['reason']=str(exc)
        records.append(row)
        if row['oracle_passed'] and not case['reject']:exercised.add(mid)
    missing=sorted(required-exercised)
    methods=[]
    for method in specs:
        calc=method.get('calculator_id') or method.get('calculator')
        methods.append({'method_id':method['id'],'calculator_id':calc,
            'status':'executed' if calc in exercised else 'failed' if calc else 'professional-review-required',
            'professional_acceptance':'not-granted'})
    summary={'schema_version':'method-verification/3','registered_selected':len(specs),'methods':methods,
        'registered_calculators':len(selected),'registered_calculators_exercised':len(selected & exercised),
        'extra_calculators_exercised':sorted(exercised-selected),'calculator_cases':len(records),'records':records,
        'professional_review_required':sum(not (m.get('calculator_id') or m.get('calculator')) for m in specs),
        'missing_calculators':missing,'failed':sum(not r['oracle_passed'] for r in records)+len(missing),
        'limit':'Direct calls are not model-binding proof; qualitative method reasoning needs professional review.'}
    output=batch.directory/'methods.json';save(output,summary)
    outputs=[p for p in batch.directory.rglob('*.json') if 'input-snapshots' not in p.parts]
    evidence,report=batch.finish(outputs=outputs)
    print(json.dumps({'report':str(output),'batch':str(evidence),'passed_execution_batch':report['passed'],
        'registered_calculators_exercised':summary['registered_calculators_exercised'], 'failed':summary['failed'],
        'professional_review_required':summary['professional_review_required']},ensure_ascii=False))
    return int(not report['passed'] or bool(summary['failed']))


if __name__=='__main__':raise SystemExit(main())
