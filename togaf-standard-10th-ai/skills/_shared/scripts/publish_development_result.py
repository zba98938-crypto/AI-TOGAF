#!/usr/bin/env python3
"""Freeze identity-level results from actual current runs, not from target counts."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import uuid

from execution_batch import verify, digest, current
from evidence_integrity import verify_reference

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(Path(path).read_text())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, action='append', required=True)
    parser.add_argument('--method-review', type=Path, required=True)
    parser.add_argument('--out', type=Path, default=ROOT/'reviews/development')
    args=parser.parse_args()
    runs=[p.resolve() for p in args.run]
    failures={str(p.relative_to(ROOT)):verify(read(p/'execution.json'),ROOT) for p in runs}
    if any(failures.values()):raise ValueError(json.dumps(failures,ensure_ascii=False))
    def one(pattern):
        paths=[p for run in runs for p in run.glob(pattern)]
        if len(paths)!=1:raise ValueError('Expected one '+pattern+': '+str(paths))
        return paths[0]
    profiles_path=one('profiles/verification.json');profiles=read(profiles_path)
    methods_path=one('methods/*/methods.json');methods=read(methods_path)
    packages_path=one('skill-packages.json');packages=read(packages_path)
    acceptance_path=one('acceptance.json');acceptance=read(acceptance_path)
    source_path=one('source/run-summary.json');source=read(source_path)
    cases_index=next(read(p/'run-index.json') for p in runs
                     if 'external_runs' in read(p/'run-index.json')['locations'])
    external=cases_index['locations']['external_runs']
    qianlin=ROOT/external['qianlin'];assembly=read(qianlin/'assembly-development.json')
    scale=read(ROOT/external['scale']/'report.json')
    repeat=read(ROOT/external['scale_repeat']/'report.json')
    review=args.method_review.resolve()
    review_ref={'path':str(review.relative_to(ROOT)), 'sha256':digest(review)}
    from verify_method_reasoning import verify_review
    review_count=verify_review(review)
    if verify_reference(review_ref, ROOT):raise ValueError('Method review references are stale')
    caps=read(ROOT/'capabilities.json');arts=read(ROOT/'artifacts.json')['artifacts']
    byprofile={r['profile_id']:r for r in profiles['results']}
    bymethod={r['method_id']:r for r in methods['records']}
    identities=[]
    for a in arts+caps['work_products']:
        selected=[p for p in caps['profiles'] if p['artifact_id']==a['id'] and not p.get('alias_of')]
        checked=[byprofile.get(p['id']) for p in selected]
        identities.append({'category':'artifact-family','id':a['id'],'owner':a['owner'],
            'profile_ids':[p['id'] for p in selected],
            'engineering_verified':bool(checked) and all(c is not None and not c['failures'] for c in checked),
            'evidence':str(profiles_path.relative_to(ROOT)),
            'professional_acceptance':'not-granted', 'business_acceptance':'not-granted'})
    for p in caps['profiles']:
        case=byprofile[p.get('alias_of',p['id'])]
        identities.append({'category':'view-template','id':p['id'],'owner':p['owner'],
            'alias_of':p.get('alias_of'), 'independently_counted':not bool(p.get('alias_of')),
            'engineering_verified':not case['failures'], 'negative_applicability':case.get('negative_applicability'),
            'evidence':str(profiles_path.relative_to(ROOT)), 'professional_acceptance':'not-granted'})
    for m in caps['analysis_methods']:
        row=bymethod[m['id']]
        record=read(ROOT/row['record']['path'])
        identities.append({'category':'analysis-method','id':m['id'],'owner':m['owner'],
            'execution_kind':row['execution_kind'],'execution_status':row['status'],
            'calculator_id':m.get('calculator_id') or m.get('calculator'),
            'calculator_executions':record['calculator_executions'],
            'separate_cli_run':record['separate_cli_run'], 'record':row['record'],
            'reasoning_review':review_ref, 'review_scope':'64-case AI consistency review plus selected independent assertions',
            'professional_acceptance':'not-granted', 'business_acceptance':'not-granted'})
    for d in assembly['deliverables']:
        identities.append({'category':'deliverable','id':d['deliverable_id'],
            'draft_status':d['draft_status'],'strict_status':d['strict_status'],
            'chapters':d['section_coverage'],'evidence_gaps':d['gaps'],
            'evidence':str((qianlin/'assembly-development.json').relative_to(ROOT)),
            'business_acceptance':'not-granted'})
    for skill,data in packages['per_skill']['content'].items():
        identities.append({'category':'skill','id':skill,
            'package_files':packages['per_skill']['files'][skill], 'package_content':data,
            'machine_negative':packages['per_skill']['negative'].get(skill),
            'owned_artifacts':[x['id'] for x in identities if x.get('owner')==skill and x['category']=='artifact-family'],
            'business_acceptance':'not-granted'})
    tests=sum(int(match.group(1)) for r in acceptance['runs']
              if (match:=re.search(r'Ran (\d+) tests?',r.get('stderr',''))))
    output=args.out/('freeze-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8])
    output.mkdir(parents=True,exist_ok=False)
    result={'schema_version':'development-result/1','frozen_at':datetime.now(timezone.utc).isoformat(),
        'engineering':{'stable_batches':len(runs),'independent_profiles':profiles['independent_profiles_checked'],
            'artifact_families':profiles['artifact_families_checked'],'failed_profiles':profiles['failed_profiles'],
            'output_kinds':profiles['output_kinds_checked'],
            'png_exports':len(list(profiles_path.parent.glob('*.png'))),
            'method_routes':{k:methods[k] for k in ('registered_selected','calculator_methods_exercised','written_only','failed')},
            'method_reasoning_cases':review_count, 'package_conditions':packages['conditions'],
            'regression_checks':len(acceptance['runs']),'unittest_cases':tests,
            'regression_passed':acceptance['passed'],'skips':acceptance['skip_summary'],
            'portable_render_enabled':acceptance['portable_renderer_install_enabled'],
            'deliverables':len(assembly['deliverables']),
            'chapters':sum(len(d['section_coverage']) for d in assembly['deliverables']),
            'strict_deliverables':dict(Counter(d['strict_status'] for d in assembly['deliverables'])),
            'required_evidence_gaps':sum(len(d['gaps']) for d in assembly['deliverables']),
            'scale_tiers':scale['tiers'],'scale_repeat':repeat.get('persisted_repeat')},
        'local_source_alignment':source,
        'professional_quality':{'method_review':review_ref,
            'source_equivalence':'not-established',
            'visual_observations':'separate-asset-bound-records-required; geometry is not visual acceptance',
            'unreviewed_source_items':source['source']['by_review_status']},
        'business_acceptance':{'status':'not-granted','reason':'Synthetic scenarios do not provide actual authority, operations or benefits.'},
        'remaining_dependencies':[
            {'id':'C220','kind':'missing-source','close_with':'Lawfully supplied formal definition text and scoped source comparisons.'},
            {'id':'SOURCE-REVIEW','kind':'local-professional-work-remaining','close_with':'Review the 1819 pending and 91 insufficient source items; reconcile 18 historical figure anomalies. Not all are external blockers.'},
            {'id':'BUSINESS','kind':'external-evidence','close_with':'Responsible-party approval and actual operating/benefit evidence; retain the nine chapter evidence gaps.'},
            {'id':'LINUX','kind':'unexecuted-environment','close_with':'Run the opt-in portable rendering tests in an actual Linux environment.'},
            {'id':'VISUAL','kind':'limited-observation-scope','close_with':'Per-asset output and original-source review beyond the explicitly opened image sample.'}],
        'runtime_fingerprints':current(ROOT),
        'identity_counts':dict(Counter(r['category'] for r in identities)),
        'limit':'No aggregate completion percentage. Engineering checks, source alignment, professional quality and actual business acceptance are independent.'}
    (output/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (output/'identity-results.json').write_text(json.dumps(identities,ensure_ascii=False,indent=2)+'\n')
    baseline=read(ROOT/'reviews/development/20261104T050816Z-8f54376b/baseline.json')
    defects=[]
    engineering_ids={'EVIDENCE-INTERNAL-HASH','REVIEW-AUTO-CLAIMS','STATUS-GLOBAL-MODIFICATION',
                     'CONTRACT-FIELD-SEMANTICS','CHECK-KEYWORD-MAPPING','ARTIFACT-EXPRESSION','CHAPTER-PLACEHOLDERS'}
    for defect in baseline['issues']:
        status=('engineering-defect-closed' if defect['id'] in engineering_ids else
                'current-bounded-routes-and-written-review-recorded' if defect['id']=='METHOD-CURRENT-RUN' else
                'professional-review-pending' if defect['id']=='SOURCE-SEMANTICS' else 'external-dependency-unverified')
        defects.append({**defect,'status':status,'closing_evidence':str((output/'result.json').relative_to(ROOT)),
                        'caveat':'Historical stale records remain stale; no source or business approval granted.'})
    (output/'defects.json').write_text(json.dumps(defects,ensure_ascii=False,indent=2)+'\n')
    refs=[{'path':str((p/'execution.json').relative_to(ROOT)), 'sha256':digest(p/'execution.json')} for p in runs]
    refs += [review_ref]+[{'path':str((output/n).relative_to(ROOT)), 'sha256':digest(output/n)} for n in ('result.json','identity-results.json','defects.json')]
    (output/'evidence.json').write_text(json.dumps({'schema_version':'evidence-node/1','references':refs},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'freeze':str(output), 'engineering':{k:v for k,v in result['engineering'].items() if k!='scale_tiers'},
                      'identity_counts':result['identity_counts']},ensure_ascii=False))


if __name__=='__main__':main()
