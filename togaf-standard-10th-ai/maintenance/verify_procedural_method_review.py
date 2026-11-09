#!/usr/bin/env python3
"""Read-only provenance/coverage verification for an authored procedural review.

This verifies current identities, step bindings and hashes. It never decides that
professional judgement, method behavior, or business acceptance has passed.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'maintenance/review-data/procedural-method-behavior-review-20261108.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def method_digest(method):
    return digest(json.dumps(method, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())


def verify(report, root=ROOT):
    registry = root / 'skills/_shared/capabilities.json'
    methods = {m['id']: m for m in json.loads(registry.read_text())['analysis_methods']
               if not (m.get('calculator_id') or m.get('calculator'))}
    rows = report.get('case_reviews', [])
    if not methods or len(rows) != len(methods) or {r.get('method_id') for r in rows} != set(methods):
        raise ValueError('review must cover every unique current procedural method')
    if report.get('accepted') is not False:
        raise ValueError('this candidate-output review cannot grant full acceptance')
    if report.get('reviewer_kind') != 'AI-implementation-agent':
        raise ValueError('reviewer provenance missing')
    for key in ('professional_author_review', 'standards_source_verification', 'business_acceptance'):
        if report.get('assurance_layers', {}).get(key, {}).get('status') not in ('pending', 'incomplete', 'not-accepted'):
            raise ValueError('unwarranted acceptance layer: ' + key)
    inputs = {}
    partial = 0
    supplemented = 0
    step_count = 0
    for row in rows:
        mid = row['method_id']
        method = methods[mid]
        expected = 'skills/_shared/references/method-cases/' + mid + '.md'
        if row.get('case_path') != expected or row.get('reviewer_kind') != 'AI-implementation-agent':
            raise ValueError('case/reviewer identity mismatch: ' + mid)
        path = root / expected
        if not path.is_file() or digest(path.read_bytes()) != row.get('case_sha256'):
            raise ValueError('stale or missing case: ' + mid)
        if method_digest(method) != row.get('method_sha256'):
            raise ValueError('stale registered method: ' + mid)
        if any(not isinstance(row.get(k), str) or not row[k].strip() for k in (
                'specific_basis', 'adverse_or_changed_input_review', 'limitations')):
            raise ValueError('specific observations required: ' + mid)
        steps = method.get('analysis_steps') or method.get('steps') or []
        actual = row.get('step_reviews', [])
        if not steps or len(steps) != len(actual):
            raise ValueError('every current declared step needs a review: ' + mid)
        for i, (text, observation) in enumerate(zip(steps, actual), 1):
            if observation.get('position') != i or observation.get('declared_step') != text:
                raise ValueError('declared step binding mismatch: ' + mid)
            if observation.get('case_scope') not in ('partial-or-explicitly-missing', 'candidate-walkthrough-reviewed',
                                                     'new-authored-candidate-supplement-reviewed'):
                raise ValueError('invalid scoped observation: ' + mid)
            if observation.get('runtime_execution') not in ('not-executed-by-this-review', 'model-to-artifact-generation-only'):
                raise ValueError('text review is not runtime execution: ' + mid)
            partial += observation['case_scope'] == 'partial-or-explicitly-missing'
            if observation['case_scope'] == 'new-authored-candidate-supplement-reviewed':
                supplemented += 1
                supplement = root / observation['supplement_path']
                if digest(supplement.read_bytes()) != observation.get('supplement_sha256'):
                    raise ValueError('stale new teaching supplement: ' + mid)
                material = json.loads(supplement.read_text())
                if not any(s['position'] == i and s['declared_step'] == text for s in material['steps']):
                    raise ValueError('supplement step identity mismatch: ' + mid)
                if material.get('accepted') is not False:
                    raise ValueError('supplement cannot grant business acceptance: ' + mid)
                inputs[observation['supplement_path']] = digest(supplement.read_bytes())
        if row.get('new_blind_agent_execution') != 'uncovered' or row.get('business_acceptance') != 'not-accepted':
            raise ValueError('this review contains no blind execution or business acceptance: ' + mid)
        inputs[expected] = digest(path.read_bytes())
        step_count += len(steps)
    for evidence in report.get('generated_output_evidence', []):
        output = Path(evidence['path'])
        if not output.is_absolute():
            output = root / output
        if digest(output.read_bytes()) != evidence.get('sha256') or evidence.get('accepted') is not False:
            raise ValueError('stale or unscoped model-to-artifact output evidence')
        run = json.loads(output.read_text())
        if run.get('passed') is not True or run.get('accepted') is not False:
            raise ValueError('generator output cannot grant business acceptance')
        for row in run['runs']:
            mid = row.get('method_id', 'agile-collaboration-selection-switch')
            source = root / ('skills/_shared/references/method-case-materials/procedural-supplements/' + mid + '.json')
            if digest(source.read_bytes()) != row['supplement_sha256']:
                raise ValueError('model-to-artifact output uses stale supplement: ' + mid)
    return {'procedural_methods': len(methods), 'candidate_outputs_reviewed': len(rows),
            'current_declared_steps_reviewed': step_count, 'partial_or_missing_steps': partial,
            'new_authored_candidate_supplement_steps': supplemented,
            'new_blind_agent_executions': 0, 'business_accepted': 0, 'inputs': inputs}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--review', type=Path, default=DEFAULT)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = {'scope': 'review provenance, current method identities, step coverage and evidence hashes',
              'semantic_approval': 'not-produced-by-this-verifier', 'accepted': False}
    try:
        report = json.loads(args.review.read_text())
        counts = verify(report)
        result.update(passed=True, counts={k: v for k, v in counts.items() if k != 'inputs'},
                      input_sha256={str(args.review.resolve().relative_to(ROOT.resolve())): digest(args.review.read_bytes()),
                                    'skills/_shared/capabilities.json': digest((ROOT / 'skills/_shared/capabilities.json').read_bytes()),
                                    **counts['inputs']})
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result.update(passed=False, error=str(exc))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, ensure_ascii=False))
    return int(not result['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
