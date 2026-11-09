"""Read-only corpus/portable integrity ledger; never semantic or visual acceptance.

Original source checkout is optional. Missing original is unavailable, not a hash
pass. Explicit relationship flags are declarations in local interpretation JSON,
not independently observed physical arrows or confirmed enterprise relationships.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
READING_KEYS=['purpose_zh','reading_guide_zh','key_points_zh','hierarchy_zh','line_semantics_zh','misreadings_zh']

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path):return json.loads(path.read_text())
def safe_file(base,name):
    path=(base/name).resolve();base=base.resolve()
    return path if base in path.parents and path.is_file() else None

def check_hash(base,name,expected):
    path=safe_file(base,name)
    if path is None:return {'path':name,'status':'missing-or-unavailable','expected_sha256':expected,'actual_sha256':None}
    actual=digest(path)
    return {'path':name,'status':'hash-matches' if isinstance(expected,str) and expected==actual else 'hash-mismatch-or-unrecorded',
            'expected_sha256':expected,'actual_sha256':actual}

def flag(value):
    if value is True:return 'declared-explicit'
    if value is False:return 'declared-implicit'
    return 'unspecified' if value is None else 'invalid-explicit-declaration'

def graph_inventory(source):
    elements=source.get('elements');relationships=source.get('relationships');issues=[]
    if not isinstance(elements,list) or not isinstance(relationships,list):
        return {'status':'unrecognized-shape-not-semantic-rejection','findings':[]}
    ids=[e.get('id') for e in elements if isinstance(e,dict) and isinstance(e.get('id'),str)]
    counts=Counter(ids);idset=set(ids)
    duplicate_ids=sorted(i for i,n in counts.items() if n>1)
    parents=[]
    for e in elements:
        if not isinstance(e,dict):continue
        if e.get('parent') is not None:
            parents.append({'element_id':e.get('id'),'parent':e['parent'],'resolves_within_elements':isinstance(e['parent'],str) and e['parent'] in idset})
    flags=Counter();endpoints=[]
    for ordinal,rel in enumerate(relationships):
        if not isinstance(rel,dict):
            issues.append({'ordinal':ordinal,'code':'unrecognized-relationship-shape'});continue
        flags[flag(rel.get('explicit'))]+=1
        for key in ['from','to']:
            value=rel.get(key)
            if isinstance(value,str):
                status='local-element-reference' if value in idset else 'nonlocal-or-unresolved-reference-needs-context'
            else:status='unrecognized-endpoint-shape-needs-context'
            endpoints.append({'relationship_ordinal':ordinal,'relationship_id':rel.get('id'),
              'field':key,'value':value,'status':status})
    return {'status':'local-interpretation-inventory-only','element_count':len(elements),'duplicate_element_ids':duplicate_ids,
      'relationship_count':len(relationships),'relationship_explicit_declarations':dict(flags),'parent_references':parents,
      'endpoint_inventory':endpoints,'findings':issues,
      'limit':'Nonlocal references require context; an explicit flag is not independent physical-arrow or business truth verification.'}

def typed_equal(left,right):
    if type(left) is not type(right):return False
    if isinstance(left,dict):return left.keys()==right.keys() and all(typed_equal(left[k],right[k]) for k in left)
    if isinstance(left,list):return len(left)==len(right) and all(typed_equal(a,b) for a,b in zip(left,right))
    return left==right

def portable_differences(original,portable):
    expected={'id':original.get('id'),'title':original.get('figure',{}).get('title_zh'),
      'source_locator':original.get('figure',{}).get('zh_location',{}),
      'reading':{k:original.get('semantics',{}).get(k) for k in READING_KEYS},
      'elements':original.get('elements',[]),'relationships':original.get('relationships',[]),
      'flows':original.get('flows',[]),'tables':original.get('tables',[]),'legend':original.get('legend',{}),
      'uncertainty':original.get('quality',{})}
    return [key for key,value in expected.items() if key not in portable or not typed_equal(portable[key],value)]

def audit(root=ROOT,source=None):
    root=Path(root).resolve();source=Path(source).resolve() if source else root.parents[1]/'togaf-standard-10th-zh'
    index=load(root/'evidence-registry.json');cap=load(root/'capabilities.json')
    profiles={p['id'] for p in cap['profiles']};methods={m['id'] for m in cap['analysis_methods']}
    figures=[]
    for record in index['figures']:
        original_path=safe_file(source,record['json_path']);portable_path=safe_file(root,record['portable_structure'])
        original=load(original_path) if original_path else None;portable=load(portable_path) if portable_path else None
        original_hash=check_hash(source,record['json_path'],record.get('json_sha256'))
        differences=portable_differences(original,portable) if original is not None and portable is not None else None
        graph=graph_inventory(original) if original is not None else {'status':'original-unavailable-no-graph-inventory'}
        figure={'id':record['id'],'original':original_hash,'portable':{'path':record['portable_structure'],
          'actual_sha256':digest(portable_path) if portable_path else None,
          'comparison_status':'projection-matches' if differences==[] else 'projection-differs' if differences is not None else 'not-compared-missing-input',
          'differing_fields':differences},'graph_inventory':graph,
          'profile_ids':record.get('profile_ids',[]),'method_ids':record.get('method_ids',[]),
          'unresolved_profile_ids':sorted(set(record.get('profile_ids',[]))-profiles),
          'unresolved_method_ids':sorted(set(record.get('method_ids',[]))-methods),
          'disposition':record.get('disposition'),'source_status_retained':record.get('source_status'),
          'historical_semantic_status_retained':record.get('current_semantic_review'),
          'assets':[check_hash(source,a['path'],a.get('sha256')) for a in record.get('assets',[])],
          'historical_asset_observations':record.get('assets',[]),
          'registry_conflict_ids':record.get('conflict_ids',[]),'accepted':False,
          'visual_opened_this_audit':False,'semantic_review_performed_this_audit':False}
        figures.append(figure)
    guides=[check_hash(source,g['path'],g.get('sha256')) for g in index['guides']]
    assets=[check_hash(source,a['path'],a.get('sha256')) for a in index['image_assets']]
    relflags=Counter()
    for f in figures:relflags.update(f['graph_inventory'].get('relationship_explicit_declarations',{}))
    summary={'guides':len(guides),'guide_hash_matches':sum(g['status']=='hash-matches' for g in guides),
      'figure_records':len(figures),'figure_hash_matches':sum(f['original']['status']=='hash-matches' for f in figures),
      'portable_projection_matches':sum(f['portable']['comparison_status']=='projection-matches' for f in figures),
      'image_assets':len(assets),'image_hash_matches':sum(a['status']=='hash-matches' for a in assets),
      'registered_conflicts_retained':len(index.get('source_conflicts',[])),
      'relationship_explicit_declarations':dict(relflags),'visual_opened_this_audit':0,'semantic_accepted_this_audit':0,
      'figures_with_unresolved_routes':sum(bool(f['unresolved_profile_ids'] or f['unresolved_method_ids']) for f in figures)}
    return {'schema_version':'source-integrity-ledger/1','status':'mechanical-inventory-not-source-acceptance',
      'evidence_registry_sha256':digest(root/'evidence-registry.json'),'capabilities_sha256':digest(root/'capabilities.json'),
      'auditor_sha256':digest(Path(__file__)),'original_corpus_available':source.is_dir(),'summary':summary,
      'guides':guides,'figures':figures,'image_assets':assets,
      'registered_conflicts_retained':index.get('source_conflicts',[]),
      'supplemental_source_review_paths':['reviews/capability-diagram-source-audit.json','reviews/capability-diagram-render-audit.json'],
      'accepted':False,'limits':['Hash equality proves stored bytes unchanged, not correct translation, visual fidelity or official definition.',
        'Portable projection equality proves extraction consistency, not truth of the interpretation.',
        'Explicit/implicit are local JSON declarations; not a verified inventory of physical arrows.',
        'Missing originals remain unavailable; copying skills alone never fabricates original-source hash matches.',
        'Historical thumbnail/detailed observations are retained data, not this auditor opening images.']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path);parser.add_argument('--report',type=Path,default=ROOT/'reviews/source-integrity-ledger.json');args=parser.parse_args()
    report=audit(source=args.source);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report['summary'],ensure_ascii=False))
if __name__=='__main__':main()
