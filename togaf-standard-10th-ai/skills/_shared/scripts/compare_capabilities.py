#!/usr/bin/env python3
"""Build a figure-by-figure evidence ledger; counts never imply source equivalence."""
import argparse,collections,json
from pathlib import Path
from registry import ROOT,load

def read(path,default=None):
    return json.loads(path.read_text()) if path.exists() else default

def build(examples=None):
    cap=read(ROOT/'capabilities.json',{});evidence=read(ROOT/'evidence-registry.json',{})
    detailed=read(ROOT/'reviews/tri-source-observations.json',{}).get('observations',[])
    triage=read(ROOT/'reviews/source-visual-triage.json',{}).get('reviewed',[])
    _,_,profiles,methods=load();observed=collections.defaultdict(list)
    for o in detailed:observed[o['figure_id']].append(o)
    triage={r['id']:r for r in triage};mapping={r.get('figure_id',r.get('id')):r for r in cap.get('figure_profiles',[])}
    outputs=collections.defaultdict(list)
    if examples:
        for layout in ['reference','adaptive']:
            folder=Path(examples)/layout
            for a in read(folder/'manifest.json',{}).get('artifacts',[]):
                coverage=read(folder/a['coverage'],{}) if a.get('coverage') else {}
                outputs[a.get('profile_id')].append({'layout':layout,'view_id':a['view_id'],
                    'status':a.get('status'),'svg_exists':bool(a.get('svg') and (folder/a['svg']).exists()),
                    'png_exists':bool(a.get('png') and (folder/a['png']).exists()),
                    'errors':coverage.get('errors',[]),'unrepresented_entities':coverage.get('unrepresented_entity_ids',[]),
                    'unrepresented_relationships':coverage.get('unrepresented_relationship_ids',[])})
    rows=[]
    for f in evidence.get('figures',[]):
        binding=mapping.get(f['id'],{})
        pids=binding.get('profile_ids',f.get('profile_ids',[]))
        mids=binding.get('method_ids',f.get('method_ids',[]))
        row={'figure_id':f['id'],'guide':f['guide'],'title':f.get('title'),'decision_purpose':f.get('purpose_summary'),
             'md_locator':f.get('md_locator'),'json_path':f.get('json_path'),'json_sha256':f.get('json_sha256'),
             'assets':[{'path':a['path'],'kind':a['kind'],'exists':a.get('exists'),
                        'historical_fidelity':a.get('historical_fidelity')} for a in f.get('assets',[])],
             'misreadings':f.get('misreadings',[]),'source_uncertainty':f.get('uncertainty'),
             'disposition':binding.get('disposition',f.get('disposition')),
             'disposition_reason':binding.get('disposition_reason',binding.get('reason',binding.get('rationale',binding.get('reason_zh')))),
             'implementation_gap':binding.get('implementation_gap'),
             'profile_ids':pids,'method_ids':mids,'detailed_tri_source_observations':observed[f['id']],
             'visual_structure_triage':triage.get(f['id']),
             'implementation_outputs':[{'profile_id':p,'definition_exists':p in profiles,
                                         'source_verified':profiles.get(p,{}).get('template',{}).get('source_verified',False),
                                         'actual_outputs':outputs.get(p,[])} for p in pids],
             'equivalence_verdict':'not-established'}
        rows.append(row)
    return {'schema_version':'2.0','review_date':'2026-11-01',
            'notice':'逐图去向、来源核实、实际生成和视觉证据独立登记。not-established不表示功能失败，也不能改称已等价。',
            'counts':{'source_figures':len(rows),'registered_profiles':len(profiles),'analysis_methods':len(methods),
                      'dispositions':dict(collections.Counter(r['disposition'] for r in rows)),
                      'figures_with_detailed_observations':sum(bool(r['detailed_tri_source_observations']) for r in rows),
                      'figures_with_thumbnail_triage':sum(bool(r['visual_structure_triage']) for r in rows)},
            'official_supplement':evidence.get('official_supplement',[]),'figures':rows}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--examples');p.add_argument('--out',default=str(ROOT/'reviews/capability-comparison.json'));a=p.parse_args()
    result=build(a.examples);Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result['counts'],ensure_ascii=False,indent=2))

if __name__=='__main__':main()
