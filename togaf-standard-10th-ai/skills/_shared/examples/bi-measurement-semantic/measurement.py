"""A fictional project's arithmetic, not a registered TOGAF method calculator.

Only summarize provided shadow samples; do not decide production adoption,
accuracy acceptance, causality, drift, release authority or business resolution.
"""
import math
import statistics

def measure_window(spec):
    version=spec.get('model_ref');window=spec.get('window');rows=spec.get('rows')
    if not isinstance(version,str) or not version or not isinstance(window,str) or not window or not isinstance(rows,list):
        raise ValueError('Explicit model version, window and rows required')
    known=[];missing=[];seen=set()
    for row in rows:
        identity=row.get('id')
        if not isinstance(identity,str) or not identity or identity in seen:raise ValueError('Missing/duplicate sample ID')
        seen.add(identity)
        if row.get('model_ref')!=version or row.get('window')!=window:raise ValueError('Mixed model version or observation window')
        predicted=row.get('predicted_minutes');actual=row.get('actual_minutes')
        for name,value in [('predicted',predicted),('actual',actual)]:
            if value is None and name=='actual':continue
            if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:raise ValueError('Invalid '+name+' minute value')
        if actual is None:missing.append(identity)
        else:known.append({'id':identity,'absolute_error_minutes':abs(predicted-actual)})
    count=len(known);total=len(rows)
    return {'model_ref':version,'window':window,'population':'provided-fictional-shadow-samples-only',
      'unit':'minute','sample_count':total,'paired_count':count,'missing_actual_ids':missing,
      'absolute_errors':known,'median_absolute_error_minutes':statistics.median([r['absolute_error_minutes'] for r in known]) if known else None,
      'paired_coverage':{'numerator':count,'denominator':total,'ratio':count/total if total else None},
      'acceptance_threshold':None,'acceptance_verdict':'unknown-no-project-threshold',
      'production_adoption_count':None,'business_resolution':'not-established',
      'limits':['Not an accuracy percentage or production adoption metric.',
                'Missing actuals remain listed; observed-pair median is not full-window error.',
                'Different versions/windows/samples do not establish comparative or causal improvement.']}
