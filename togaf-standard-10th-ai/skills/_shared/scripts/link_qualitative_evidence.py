"""Append actual qualitative case routes without relabelling their judgments as calculations.

Keeps previously indexed evidence and requires explicit per-method report fields.
Run after independent authors finish their reports; never fabricate missing roles.
"""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROLES={'raw_materials':'raw','analysis_steps':'steps','analysis_baseline':'result',
       'analysis_modified':'modification','counterexamples':'counterexample','execution_record':'execution'}

def add_reports(index, reports, root=ROOT):
    methods={m['method_id']:m for m in index['methods']}
    for report_path in reports:
        report=json.loads((root/report_path).read_text())
        for case in report.get('methods',[]):
            method=methods[case['method_id']]
            for field,role in ROLES.items():
                if field not in case:
                    if field=='analysis_steps':
                        candidate=str(Path(case['baseline_model']).parent/'analysis.md')
                        if (root/candidate).is_file():case[field]=candidate
                        else:continue
                    else:continue
                paths=case[field] if isinstance(case[field],list) else [case[field]]
                for path in paths:
                    file=root/path
                    if not file.is_file():raise ValueError('Missing evidence '+path)
                    record={'path':path,'exists':True,'basis':'executed qualitative case; not a calculator acceptance',
                            'selector':'method_id='+case['method_id'],'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
                    rows=method['evidence'].setdefault(role,[])
                    rows[:]=[r for r in rows if r['path']!=path];rows.append(record)
            method.setdefault('qualitative_execution_routes',[])
            route={'report':report_path,'profile_id':case['profile_id'],
                   'baseline_model':case['baseline_model'],'modified_model':case['modified_model'],
                   'review':case.get('qualitative_review',{}),
                   'limit':'人工定性判断已记录；CLI验证模型/表达，不等于方法计算、业务批准或目视通过。'}
            method['qualitative_execution_routes']=[r for r in method['qualitative_execution_routes'] if r['report']!=report_path]+[route]
            method['execution_status']='qualitative-case-and-standard-cli-records-linked; acceptance-separate'
            method['missing_evidence_roles']=[r for r in ROLES.values() if not method['evidence'].get(r)]
    # Attach the legacy qualitative cross reviews only to methods this call actually
    # touched. Attaching them unconditionally made an empty report set mutate the index,
    # and it also overrode the per-case reviews with rows about a different set of files.
    touched={case['method_id'] for report_path in reports
             for case in json.loads((root/report_path).read_text()).get('methods',[])} if reports else set()
    for path in ['reviews/qualitative-business-cross-review.json','reviews/qualitative-information-cross-review.json']:
        file=root/path
        if not file.is_file():continue
        cross=json.loads(file.read_text())
        for result in cross.get('methods',[]):
            if result['method_id'] not in touched:
                continue
            method=methods[result['method_id']]
            record={'path':path,'exists':True,'basis':'other-agent bounded semantic review; not official, business approval or visual acceptance',
              'selector':'method_id='+result['method_id'],'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
              'reported_status':result.get('status',result.get('qualitative_review'))}
            rows=method['evidence'].setdefault('cross_review',[])
            rows[:]=[r for r in rows if r['path']!=path];rows.append(record)
            method['independent_status']='bounded-cross-agent-semantic-review-recorded; visual-and-official-acceptance-pending'
    summary=index['summary'];summary['execution_record_located_count']=sum(bool(m['evidence'].get('execution')) for m in methods.values())
    summary['missing_role_counts']={role:sum(not m['evidence'].get(role) for m in methods.values()) for role in set(ROLES.values()) if any(not m['evidence'].get(role) for m in methods.values())}
    summary['qualitative_execution_linked_count']=sum(bool(m.get('qualitative_execution_routes')) for m in methods.values())
    summary['bounded_cross_review_linked_count']=sum(bool(m['evidence'].get('cross_review')) for m in methods.values())
    return index

def main():
    path=ROOT/'reviews/method-case-index.json';index=json.loads(path.read_text())
    reports=['reviews/qualitative-business-execution.json','reviews/qualitative-information-execution.json']
    add_reports(index,reports)
    path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(index['summary'],ensure_ascii=False))
if __name__=='__main__':main()
