"""Merge explicit reviewed capability packages, without treating them as acceptance.

No heuristic candidate conversion: source review candidates remain unimplemented
until a package supplies real contracts and examples.
"""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def append_fields(target, additions, identity):
    """Merge explicitly additive contracts without silently replacing meanings."""
    for key,value in additions.items():
        if key not in target:target[key]=value
        elif isinstance(value,list) and isinstance(target[key],list):
            target[key].extend(x for x in value if x not in target[key])
        elif isinstance(value,dict) and isinstance(target[key],dict):append_fields(target[key],value,identity+'.'+key)
        elif target[key]!=value:raise ValueError('追加字段冲突：'+identity+'.'+key)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('packages',nargs='+');args=ap.parse_args()
    target=ROOT/'capabilities.json';cap=json.loads(target.read_text());meta=json.loads((ROOT/'metamodel.json').read_text());artifacts=json.loads((ROOT/'artifacts.json').read_text());records=[]
    for value in args.packages:
        path=Path(value).resolve();package=json.loads(path.read_text())
        for key in ['work_products','profiles','analysis_methods']:
            current={x['id']:x for x in cap[key]}
            for item in package.get(key,[]):
                if not item.get('id') or not item.get('owner') or not item.get('source_refs'):raise ValueError('缺少能力标识/主责/来源：'+str(item.get('id')))
                if key!='analysis_methods' and not item.get('example'):raise ValueError('缺少完整模型例：'+item['id'])
                current[item['id']]=item
            cap[key]=list(current.values())
        cap.setdefault('default_profiles',{}).update(package.get('default_profiles',{}))
        for patch in package.get('patches',[]):
            group=patch.get('group',patch.get('target_kind','work_products'));identity=patch.get('id',patch.get('target_id'))
            group={'work_product':'work_products','profile':'profiles','analysis_method':'analysis_methods','artifact':'artifacts'}.get(group,group)
            if group=='work_product_or_artifact':group='work_products' if any(x['id']==identity for x in cap['work_products']) else 'artifacts'
            item=next(x for x in (artifacts['artifacts'] if group=='artifacts' else cap[group]) if x['id']==identity)
            if 'add' in patch:
                append_fields(item,patch['add'],identity)
                continue
            updates=patch.get('set',patch.get('updates'))
            if not isinstance(updates,dict):raise ValueError('patch须显式set/updates，拒绝猜测字段：'+identity)
            item.update(updates)
        for name,definition in package.get('relationship_definitions',{}).items():
            if name in meta['relationships']:raise ValueError('禁止覆盖已有核心关系：'+name)
            if ':' not in name:raise ValueError('包新增关系须命名空间：'+name)
            vocabulary=cap.setdefault('extension_relationship_definitions',{})
            if name in vocabulary and vocabulary[name]!=definition:raise ValueError('扩展定义冲突：'+name)
            vocabulary[name]=definition
        for name,definition in package.get('entity_definitions',package.get('entity_type_definitions',{})).items():
            if name in meta['entity_types'] and meta['entity_types'][name]!=definition:raise ValueError('禁止覆盖核心类型：'+name)
            meta['entity_types'][name]=definition
        if package.get('candidate_resolutions'):
            resolutions=cap.setdefault('candidate_resolutions',[])
            raw=package['candidate_resolutions']
            if isinstance(raw,dict):raw=[dict(value,candidate_id=key) for key,value in raw.items()]
            for resolution in raw:
                record={**resolution,'package':str(path.relative_to(ROOT))}
                prior=next((i for i,x in enumerate(resolutions) if x.get('candidate_id',x.get('id'))==record.get('candidate_id',record.get('id'))),None)
                if prior is None:resolutions.append(record)
                else:resolutions[prior]=record
        records.append({'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'work_products':[x['id'] for x in package.get('work_products',[])],'profiles':[x['id'] for x in package.get('profiles',[])],'status':'registered-not-accepted'})
    from registry_consistency import canonicalize_resolutions
    known_ids={x['id'] for group in ['work_products','profiles','analysis_methods'] for x in cap[group]}
    cap['candidate_resolutions']=canonicalize_resolutions(cap.get('candidate_resolutions',[]),known_ids)
    for w in cap['work_products']:
        choices=[p for p in cap['profiles'] if p['artifact_id']==w['id']]
        if not choices:raise ValueError('工作产品无可达视图：'+w['id'])
        cap['default_profiles'].setdefault(w['id'],next((p['id'] for p in choices if p['id']==w['id']+'-default'),choices[0]['id']))
    known={p['id']:p for p in cap['profiles']}
    for aid,pid in cap['default_profiles'].items():
        if pid not in known or known[pid]['artifact_id']!=aid:raise ValueError('默认规范错误：'+aid)
    target.write_text(json.dumps(cap,ensure_ascii=False,indent=2)+'\n');(ROOT/'metamodel.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');(ROOT/'artifacts.json').write_text(json.dumps(artifacts,ensure_ascii=False,indent=2)+'\n')
    report=ROOT/'reviews/applied-capability-addenda.json';prior=json.loads(report.read_text()) if report.exists() else []
    entries={x['path']:x for x in prior};entries.update({x['path']:x for x in records});report.write_text(json.dumps(list(entries.values()),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'work_products':len(cap['work_products']),'profiles':len(cap['profiles']),'methods':len(cap['analysis_methods'])}))
if __name__=='__main__':main()
