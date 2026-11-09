"""Snapshot actual development inventory without promoting any acceptance claim."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import uuid

ROOT = Path(__file__).resolve().parents[1]


def inventory(root=ROOT):
    def read(name):
        return json.loads((root / name).read_text())
    caps = read('capabilities.json')
    arts = read('artifacts.json')['artifacts']
    deliverables = read('deliverables.json')['deliverables']
    records = []
    for category, group in [('artifact-family', arts + caps['work_products']),
                            ('view-template', caps['profiles']),
                            ('analysis-method', caps['analysis_methods']),
                            ('deliverable', deliverables)]:
        for item in group:
            records.append({'category': category, 'id': item['id'], 'owner': item['owner'],
                            'alias_of': item.get('alias_of'),
                            'development_status': 'registered-needs-behavioral-evidence',
                            'business_acceptance_status': 'not-granted'})
    files = [root / n for n in ('capabilities.json', 'artifacts.json', 'deliverables.json',
                                'metamodel.json', 'relationships.json')]
    files += list((root / 'scripts').glob('*.py')) + list((root / 'tests').glob('test_*.py'))
    files += list(root.parent.glob('togaf-*/SKILL.md'))
    issue_specs = [
        ('EVIDENCE-INTERNAL-HASH', 'evidence-stale', 'method-execution / method-cross-review',
         'test_evidence_integrity.py', 'Nested case/input/output hashes must match; re-execution or review is required.'),
        ('REVIEW-AUTO-CLAIMS', 'development-defect', 'scripts/build_method_case_records.py',
         'test_evidence_integrity.py', 'Generated observations never claim semantic review or execution.'),
        ('STATUS-GLOBAL-MODIFICATION', 'development-defect', 'scripts/evaluate_seven_dimensions.py',
         'test_dimension_status.py', 'Evidence scope must name the actual view/identity; gate computes acceptance.'),
        ('CONTRACT-FIELD-SEMANTICS', 'development-defect', 'capabilities.json and skill references',
         'contract tests', 'Every required field has domain-specific meaning, type, unknown and source policy.'),
        ('CHECK-KEYWORD-MAPPING', 'development-defect', 'scripts/build_skill_packages.py',
         'contract tests', 'Explicit checks reference actual executors; professional judgement remains separate.'),
        ('ARTIFACT-EXPRESSION', 'requires-current-reproduction', 'renderers / table_expression / view_semantics',
         'artifact verification', 'Per-profile semantic output and mutation checks, not file existence.'),
        ('CHAPTER-PLACEHOLDERS', 'development-defect', 'examples/qianlin-synthetic',
         'semantic chapter tests', 'Every selected chapter answers a concrete decision with scoped support.'),
        ('METHOD-CURRENT-RUN', 'evidence-stale', '64 methods',
         'bounded method replay', 'Calculator executions and qualitative reasoning are identified separately.'),
        ('SOURCE-SEMANTICS', 'professional-review-pending', '26 guides sections / tables / figures',
         'source comparison', 'No claim of equivalence without actual scoped source observations.'),
        ('C220-MISSING', 'external-dependency', 'C220 formal definitions',
         'source availability', 'Requires lawfully supplied text; does not block unrelated local guide development.'),
        ('BUSINESS-ACCEPTANCE', 'external-dependency', 'actual enterprise authority and operational evidence',
         'business review', 'Requires responsible party evidence, never synthetic approval.'),
        ('LINUX-EXECUTION', 'environment-dependent', 'portable renderer',
         'test_portable_v2.py', 'Requires an actual compatible Linux execution environment.')]
    issues = [{'id': i, 'classification': c, 'affected': a, 'verification': v,
               'closure_condition': condition, 'status': 'open'}
              for i, c, a, v, condition in issue_specs]
    return {'schema_version': 'development-baseline/1',
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'counts': {'skills': len(list(root.parent.glob('togaf-*/SKILL.md'))),
                       'base_artifacts': len(arts), 'base_artifact_kinds': dict(Counter(a['kind'] for a in arts)),
                       'guide_work_products': len(caps['work_products']),
                       'artifact_families': len(arts) + len(caps['work_products']),
                       'profile_entries': len(caps['profiles']),
                       'independent_profiles': sum(not p.get('alias_of') for p in caps['profiles']),
                       'methods': len(caps['analysis_methods']), 'deliverables': len(deliverables),
                       'chapters': sum(len(d['sections']) for d in deliverables)},
            'fingerprints': {str(p.relative_to(root.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(set(files))},
            'identities': records, 'issues': issues,
            'limit': 'Inventory snapshot, not source, semantic, visual or business acceptance.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out-dir', type=Path, default=ROOT / 'reviews/development')
    args = p.parse_args()
    run = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    directory = args.out_dir / run
    directory.mkdir(parents=True, exist_ok=False)
    report = inventory()
    report['run_id'] = run
    (directory / 'baseline.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'directory': str(directory), 'counts': report['counts']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
