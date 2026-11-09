#!/usr/bin/env python3
"""Source-gated reference model mappings; never invent TRM/III-RM originals."""
import argparse,hashlib,json
from pathlib import Path
from acceptance_gate import evaluate_acceptance
from standards import Invalid,Incomplete,write_new
ROOT=Path(__file__).resolve().parents[1]

def catalog():return [{'id':n,'definition_status':'blocked','official_version':'not-acquired','gate':'authorized original + source locators + independent acceptance record','historical_reference_is_current_togaf_normative':False} for n in ('trm','iii-rm')]

def verified_definition(path,evidence_root,gate_path):
    d=json.loads(Path(path).read_text());identity=d.get('id')
    if identity not in ('trm','iii-rm'):raise Invalid('reference model must explicitly identify trm or iii-rm')
    for field in ('version','source_path','source_sha256','source_locator','nodes','relationships','normative_context'):
        if not d.get(field):raise Invalid('reference definition missing '+field)
    base=Path(evidence_root).resolve();source=(base/d['source_path']).resolve()
    if not source.is_relative_to(base) or not source.is_file():raise Invalid('reference source path escapes/missing')
    if hashlib.sha256(source.read_bytes()).hexdigest()!=d['source_sha256']:raise Invalid('reference source hash mismatch')
    if d['normative_context'] not in ('historical-reference','current-authorized-reference'):raise Invalid('explicit normative context required')
    ids=[n['id'] for n in d['nodes']]
    if len(ids)!=len(set(ids)):raise Invalid('duplicate reference IDs')
    for edge in d['relationships']:
        if edge.get('source') not in ids or edge.get('target') not in ids or not edge.get('meaning') or not edge.get('source_locator'):raise Invalid('reference edge needs valid endpoints, meaning and official locator')
    current={'reference_definition':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'script':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    gate=evaluate_acceptance({'category':'reference-model','id':identity,'evidence_class':'source-figure','visual_applicable':True},json.loads(Path(gate_path).read_text()),base,current)
    if not gate['accepted']:raise Incomplete('reference-model acceptance pending: '+ '; '.join(gate['reasons']))
    return d

def mapping_report(definition,model,mappings):
    nodes={n['id']:n for n in definition['nodes']};entities={e['id']:e for e in model['entities']};seen=set();rows=[];errors=[]
    for row in mappings:
        n=row.get('reference_id');e=row.get('entity_id');key=(n,e)
        if key in seen:errors.append('duplicate mapping '+str(key))
        seen.add(key)
        if n not in nodes or e not in entities:errors.append('unresolved mapping '+str(key));continue
        if entities[e]['type'] not in nodes[n].get('allowed_entity_types',[]):errors.append('mapping endpoint type mismatch '+str(key))
        if not row.get('rationale') or not row.get('evidence_ids') or not set(row['evidence_ids'])<=set(s['id'] for s in model['sources']):errors.append('mapping needs concrete rationale/source IDs '+str(key))
        rows.append({'reference_id':n,'entity_id':e,'entity_name':entities[e]['name'],'reference_version':definition['version'],'normative_context':definition['normative_context'],'source_locator':nodes[n].get('source_locator'),'rationale':row.get('rationale')})
    missing=[n for n in nodes if nodes[n].get('required') and n not in {r['reference_id'] for r in rows}]
    return {'status':'invalid' if errors else 'incomplete' if missing else 'mapped','errors':errors,'unmapped_required_nodes':missing,'mappings':rows,'source_equivalence_not_inferred_from_mapping':True}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['catalog','check','generate']);p.add_argument('--definition',type=Path);p.add_argument('--gate',type=Path);p.add_argument('--evidence-root',type=Path);p.add_argument('--model',type=Path);p.add_argument('--mappings',type=Path);p.add_argument('--out',type=Path);a=p.parse_args();code=0
    try:
        if a.command=='catalog':result=catalog();code=3
        else:
            if not all([a.definition,a.gate,a.evidence_root,a.model,a.mappings]):raise Incomplete('official gated definition/model/mappings required; no project diagram will masquerade as TRM or III-RM')
            d=verified_definition(a.definition,a.evidence_root,a.gate);result=mapping_report(d,json.loads(a.model.read_text()),json.loads(a.mappings.read_text()));code=1 if result['errors'] else 3 if result['unmapped_required_nodes'] else 0
            if a.command=='generate' and code==0:result.update(reference_nodes=d['nodes'],reference_relationships=d['relationships'],rendering='explicit reference graph with actual instance mapping, not standard certification')
        if a.out:write_new(a.out,json.dumps(result,ensure_ascii=False,indent=2).encode())
    except Incomplete as e:result={'status':'blocked','reason':str(e)};code=3
    except (Invalid,ValueError,OSError,KeyError) as e:result={'status':'error','reason':str(e)};code=1
    print(json.dumps(result,ensure_ascii=False,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
