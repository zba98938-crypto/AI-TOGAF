"""Persist legacy default view contracts without changing their artifact IDs.

These are project compatibility specifications, not newly discovered TOGAF
definitions. Their source status must never be upgraded by successful rendering.
"""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tests'))
from example_model import build_model
from migrate import migrate
from registry import DEFAULT_RENDERERS

def main():
    artifacts = json.loads((ROOT / 'artifacts.json').read_text())
    cap = json.loads((ROOT / 'capabilities.json').read_text())
    model, _ = migrate(build_model())
    existing = {p['id']: p for p in cap['profiles']}
    for artifact in artifacts['artifacts']:
        aid = artifact['id']; pid = 'compat-' + aid
        artifact['default_profile_id'] = pid
        view = copy.deepcopy(next(v for v in model['views'] if v['artifact_id'] == aid))
        view['profile_id'] = pid
        graphical = artifact['kind'] == 'diagram'
        renderer = DEFAULT_RENDERERS.get(aid, {'er':'er','state':'state','sequence':'sequence'}.get(artifact['notation'], 'network')) if graphical else artifact['kind']
        selected = set(view['entity_ids']); edges = set(view['relationship_ids'])
        example = {'notice':'虚构兼容案例；不是正式定义或来源图复刻。',
                   'sources':copy.deepcopy(model['sources']),
                   'entities':[copy.deepcopy(e) for e in model['entities'] if e['id'] in selected],
                   'relationships':[copy.deepcopy(r) for r in model['relationships'] if r['id'] in edges],
                   'view':view}
        for e in example['entities']: e['certainty'] = 'assumed'
        for r in example['relationships']: r['certainty'] = 'assumed'
        existing[pid] = {'id':pid, 'artifact_id':aid, 'name':artifact['name_zh']+'（兼容默认）',
                         'owner':artifact['owner'], 'version':'2.1', 'renderer':renderer,
                         'output_kind':'diagram' if graphical else 'table',
                         'registration_class':'legacy-default',
                         'source_refs':artifact['sources'], 'source_locator':artifact.get('source_locator'),
                         'definition_status':'project-compatibility-template',
                         'template':{'id':pid, 'version':'2.1', 'source_verified':False,
                                     'layout_notes':'保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。'},
                         'entity_types':artifact['entity_types'], 'relationship_types':artifact['relationship_types'],
                         'required_attributes':artifact.get('required_attributes',{}),
                         'checks':artifact['semantic_checks'], 'example':example}
    cap['profiles'] = list(existing.values())
    cap['default_profiles'] = {a['id']:a['default_profile_id'] for a in artifacts['artifacts']}
    for w in cap['work_products']:
        candidates = [p for p in cap['profiles'] if p['artifact_id'] == w['id']]
        preferred = next((p for p in candidates if p['id'] == w['id']+'-default'), candidates[0] if candidates else None)
        if preferred: cap['default_profiles'][w['id']] = preferred['id']
    for name, data in [('artifacts.json',artifacts), ('capabilities.json',cap)]:
        (ROOT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'default_profiles':len(cap['default_profiles']), 'profiles':len(cap['profiles'])}))

if __name__ == '__main__': main()
