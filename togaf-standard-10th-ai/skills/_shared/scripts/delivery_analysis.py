"""G20F qualitative style comparison and iterative option review.

These functions check explicit project judgments; they do not infer judgments,
scores, or approval from prose or from the number of source-table matches.
"""
import json
from pathlib import Path
from numeric_contracts import stable_id, unique_records
ROOT=Path(__file__).resolve().parents[1]

def review_styles(inputs):
    guidance=json.loads((ROOT/'references/source-tables/delivery-styles.json').read_text())['features']
    expected={x['id'] for x in guidance};rows=inputs.get('features',[])
    if len(rows)!=len(expected) or {x['feature_id'] for x in rows}!=expected:raise ValueError('style-feature-coverage: 逐项评估来源24特征，未确定须写unknown')
    for row in rows:
        if row.get('applies') not in ['yes','no','unknown'] or not row.get('observation') or not row.get('evidence_refs'):raise ValueError('style-observation-evidence-gap')
    decisions=inputs.get('decisions',[])
    if not decisions:raise ValueError('style-decision-missing')
    unique_records(decisions,'decisions',key='scope_id')
    for d in decisions:
        if not d.get('styles') or set(d['styles'])-{'rapid','agile','robust'} or not d.get('rationale') or not d.get('evidence_refs') or not d.get('owner'):raise ValueError('style-decision-evidence-gap')
        if not d.get('conflicting_features') or not d.get('tailoring'):raise ValueError('style-conflict-and-tailoring-required')
        if set(d['conflicting_features'])-expected:raise ValueError('style-unknown-feature-reference')
    return {'decisions':decisions,'unknown_features':[r['feature_id'] for r in rows if r['applies']=='unknown'],
      'source_feature_count':len(guidance),'weighted_score':None,'automatic_approval':False,
      'notice':'来源是一般画像；按范围解释冲突，可嵌套三种风格。不能以匹配项多数决定交付风格。'}

def review_options(inputs):
    rows=inputs.get('iterations',[]);constraints=inputs.get('constraints',[])
    if not rows:raise ValueError('sbce-no-iterations')
    unique_records(constraints,'constraints')
    for row in rows:
        stable_id(row.get('option_id'),'iterations.option_id')
        if type(row.get('iteration')) is not int or row['iteration']<1:raise ValueError('sbce-iteration-order')
    if not inputs.get('constraint_review',{}).get('evidence_refs'):raise ValueError('sbce-constraint-review-missing')
    if len({(r['option_id'],r['iteration']) for r in rows})!=len(rows):raise ValueError('sbce-duplicate-iteration')
    history={};eliminated=set()
    for row in sorted(rows,key=lambda x:x['iteration']):
        if type(row.get('iteration')) is not int or row['iteration']<1:raise ValueError('sbce-iteration-order')
        if not all(row.get(k) for k in ['subsystem','goal','hypothesis','evidence_refs','decision_owner','assessment']):raise ValueError('sbce-evidence-gap')
        if row.get('status') not in ['retain','eliminate','selected','reopen']:raise ValueError('sbce-status')
        oid=row['option_id'];previous=history.get(oid)
        if previous and previous['subsystem']!=row['subsystem']:raise ValueError('sbce-option-identity-conflict')
        if oid in eliminated and row['status'] in ['retain','selected']:raise ValueError('sbce-reopen-evidence-required')
        if row['status'] in ['eliminate','reopen'] and (not row.get('decision_reason') or not row.get('new_evidence_refs')):raise ValueError('sbce-elimination-or-reopen-evidence')
        if row['status']=='eliminate':eliminated.add(oid)
        if row['status']=='reopen':eliminated.discard(oid)
        history[oid]=row
    known=set(history);selected={key for key,row in history.items() if row['status']=='selected'}
    subsystems=[history[key]['subsystem'] for key in selected]
    if len(subsystems)!=len(set(subsystems)):raise ValueError('sbce-multiple-selected-per-subsystem')
    unresolved=[]
    for c in constraints:
        if c.get('source_option_id') not in known or c.get('target_option_id') not in known:raise ValueError('sbce-dangling-constraint')
        if c.get('status') not in ['satisfied','violated','unknown'] or not c.get('evidence_refs'):raise ValueError('sbce-constraint-evidence')
        if c['source_option_id'] in selected and c['target_option_id'] in selected and c['status']!='satisfied':unresolved.append(c['id'])
    if unresolved:raise ValueError('sbce-selected-set-not-compatible: '+','.join(unresolved))
    return {'latest_options':list(history.values()),'selected_ids':sorted(selected),'eliminated_ids':sorted(eliminated),
      'iteration_count':len({r['iteration'] for r in rows}),'automatic_approval':False,
      'notice':'保留逐轮评估与淘汰/重开证据；selected是项目分析选择，不是正式批准。未建模的子系统耦合仍须评审。'}
