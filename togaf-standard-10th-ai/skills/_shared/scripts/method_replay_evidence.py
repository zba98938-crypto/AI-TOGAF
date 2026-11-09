"""Scoped current execution evidence; never upgrades historical or semantic gates."""
import hashlib
from pathlib import Path

def replay_status(index,identity,root,current_fingerprints):
    root=Path(root).resolve();record=next((r for r in index.get('methods',[]) if r.get('method_id')==identity),None)
    if not record:return {'status':'no-current-replay','accepted':False}
    stale=[]
    def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
    if index.get('registry_sha256')!=digest(root/'capabilities.json'):stale.append('capabilities.json')
    if index.get('runtime_fingerprints')!=current_fingerprints:stale.append('runtime-fingerprints')
    evidence=record.get('evidence',[])
    if not evidence:stale.append('missing-evidence')
    for item in evidence:
        path=(root/item['path']).resolve()
        if root not in path.parents or not path.is_file() or digest(path)!=item.get('sha256'):stale.append(item['path'])
    for item in record.get('models',[]):
        path=(root/item['path']).resolve()
        if root not in path.parents or not path.is_file() or digest(path)!=item.get('sha256'):stale.append(item['path'])
    good=record.get('all_cli_exits_expected') is True and (record.get('model_cli_runs',0)>0 or record.get('direct_input_runs',0)>0)
    return {'status':'current-replay-evidence-stale' if stale else 'current-scoped-execution-recorded' if good else 'current-replay-execution-gap',
      'stale_paths':sorted(set(stale)),'accepted':False,'model_cli_runs':record.get('model_cli_runs',0),
      'direct_input_runs':record.get('direct_input_runs',0),'semantic_status':record.get('semantic_status'),
      'gaps':record.get('gaps',[]),'evidence':'reviews/method-current-replay-index.json#'+identity,
      'limit':'New scoped execution only; original method judgment, direct-call model binding, official/source/visual acceptance remain separate.'}
