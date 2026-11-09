#!/usr/bin/env python3
"""Bind every project profile to existing locators, expression and honest gates."""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def ledger():
    from registry import load
    from runtime_provenance import fingerprints
    from acceptance_gate import evaluate_acceptance
    _,_,profiles,_=load();rows=[]
    runtime=hashlib.sha256(json.dumps(fingerprints(ROOT),sort_keys=True).encode()).hexdigest()
    documents={}
    for path in (ROOT.parents[1]/'togaf-standard-10th').glob('G*e.pdf'):
        documents[path.stem[:-1]]={'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'authority':'local-original-pdf-not-independently-accepted'}
    for identity,p in profiles.items():
        evidence=p.get('evidence_class','unspecified')
        definition_hash=hashlib.sha256(json.dumps(p,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        gate_path=ROOT/'reviews/source-acceptance'/(identity+'.json')
        acceptance={'accepted':False,'status':'pending','reasons':['current named source review not supplied']}
        if gate_path.is_file():
            try:acceptance=evaluate_acceptance({'category':'profile','id':identity,'evidence_class':evidence,'output_kind':p.get('output_kind','diagram')},json.loads(gate_path.read_text()),ROOT,{'definition':definition_hash,'runtime':runtime})
            except (ValueError,OSError):acceptance={'accepted':False,'status':'pending','reasons':['invalid source acceptance record']}
        assets=[]
        for ref in p.get('source_refs',[]):
            match=re.match(r'^(G[0-9A-Z]+)(?=[\s/§]|$)',ref)
            item={'locator':ref,'document':documents.get(match.group(1)) if match else None,'semantic_review':'pending'}
            structure=ROOT/'references/source-structures'/(ref.replace('/','-')+'.json')
            if structure.is_file():item['interpretation']={'path':str(structure.relative_to(ROOT)),'sha256':hashlib.sha256(structure.read_bytes()).hexdigest(),'official_equivalence':False}
            assets.append(item)
        rows.append({'profile_id':identity,'source_refs':p.get('source_refs',[]),'source_structure_refs':p.get('source_structure_refs',[]),'source_class':evidence,'source_evidence':assets,'actual_expression':{'renderer':p.get('renderer'),'artifact_id':p.get('artifact_id'),'entity_types':p.get('entity_types',[]),'relationship_types':p.get('relationship_types',[])},'project_convention':evidence=='project-convention','source_verified':p.get('template',{}).get('source_verified') is True,'acceptance_status':'project-contract-review-pending' if evidence=='project-convention' and not acceptance['accepted'] else acceptance['status'],'current_acceptance':acceptance,'discrepancies':p.get('blocked_source',{}),'definition_sha256':definition_hash,'bulk_verification_permitted':False})
    for row in rows:
        row['source_structure_evidence']=[]
        for name in row['source_structure_refs']:
            path=(ROOT/name).resolve()
            if path.is_relative_to(ROOT) and path.is_file():
                row['source_structure_evidence'].append({'path':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'official_equivalence':False})
        row['implementation_difference_review']='pending; empty discrepancy metadata is not acceptance'
    from collections import Counter
    return {'schema_version':'source-coverage-ledger/2','profile_count':len(rows),'source_classes':dict(Counter(r['source_class'] for r in rows)),'profiles':rows,'external_gates':[{'id':'togaf-c220','version':'10th Edition / C220','url':'https://publications.opengroup.org/c220','status':'blocked','reason':'authorized complete foundation original and acceptance record not supplied'},{'id':'archimate-4','version':'4 / C260','url':'https://publications.opengroup.org/c260','status':'blocked','reason':'authorized original and exchange applicability missing'},{'id':'trm-iii-rm','version':'TOGAF 9.1 historical reference','normative_context':'historical-reference','status':'blocked','reason':'authorized historical reference original and current acceptance record not supplied'}],'automatic_source_equivalence':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.write_text(json.dumps(ledger(),ensure_ascii=False,indent=2))
