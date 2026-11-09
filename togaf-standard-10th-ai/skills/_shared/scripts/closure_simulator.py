#!/usr/bin/env python3
"""Symbolic guarded-flow replay only. NEVER executes enterprise operations."""
import argparse,json
from pathlib import Path
from closure_semantics import check

def replay(model,flow_id,observations):
    issues=check(model)
    if issues:raise ValueError('invalid closure flow model: '+str(issues))
    flow=next(f for f in model['extension_data']['enterprise:closure']['flows'] if f['id']==flow_id)
    edges=[e for e in model['relationships'] if e['id'] in flow['edge_ids']];entities={e['id']:e for e in model['entities']}
    cursor=flow['start_id'];events=[];steps=0
    while cursor not in flow['terminal_ids']:
        steps+=1
        if steps>flow.get('max_steps',100):raise ValueError('symbolic replay maximum steps reached; loop not silently accepted')
        selected=[]
        for e in edges:
            if e['source']!=cursor:continue
            g=e.get('attributes',{}).get('guard')
            if not g:selected.append(e)
            elif g['field'] not in observations:raise ValueError('missing guard observation: '+g['field'])
            elif type(observations[g['field']]) is type(g['value']) and observations[g['field']]==g['value']:selected.append(e)
        if len(selected)!=1:raise ValueError('no unique enabled exit: '+cursor)
        edge=selected[0];events.append({'node_id':cursor,'node_name':entities[cursor]['name'],'edge_id':edge['id'],'guard':edge.get('attributes',{}).get('guard'),'semantic':edge['type'],'actual_operation_executed':False});cursor=edge['target']
    return {'classification':'symbolic-synthetic-replay','production_proof':False,'events':events,'terminal_id':cursor,'status':'completed-replay','real_rollback_success':None}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--model',type=Path,required=True);p.add_argument('--flow',required=True);p.add_argument('--observations',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.write_text(json.dumps(replay(json.loads(a.model.read_text()),a.flow,json.loads(a.observations.read_text())),ensure_ascii=False,indent=2))
