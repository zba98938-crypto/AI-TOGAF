#!/usr/bin/env python3
"""Explicit, non-destructive migration of v1 project models to v2."""
import argparse
import copy
import json
from pathlib import Path
import re
from validate import validate,ROOT,NAMESPACE

LEGACY_CARDINALITY = {
    "one": {"min": 1, "max": 1}, "zero-or-one": {"min": 0, "max": 1},
    "many": {"min": 0, "max": None}, "one-or-more": {"min": 1, "max": None},
    "unknown": {"unknown": True, "min": None, "max": None},
}

def migrate(model):
    if model.get("schema_version") == "2.0":
        return copy.deepcopy(model), {"changed": False, "warnings": [], "notice": "已为 v2；未修改输入。"}
    if model.get("schema_version") != "1.0":
        raise ValueError("只支持 schema_version 1.0 或 2.0")
    result = copy.deepcopy(model)
    unknown=[]
    schema=json.loads((ROOT/"schemas/model-v1.schema.json").read_text())
    def preserve_unrecognized(value,rule,path):
        if isinstance(value,dict):
            properties=rule.get("properties",{})
            if rule.get("additionalProperties") is False:
                for key in list(value):
                    if key not in properties:
                        unknown.append({"path":path,"field":key,"value":value.pop(key)})
            for key,child in value.items():
                child_rule=properties.get(key,rule.get("additionalProperties",{}))
                if isinstance(child_rule,dict):preserve_unrecognized(child,child_rule,path+[key])
        elif isinstance(value,list) and isinstance(rule.get("items"),dict):
            for index,child in enumerate(value):preserve_unrecognized(child,rule["items"],path+[index])
    preserve_unrecognized(result,schema,[])
    errors = [i for i in validate(result) if i["level"] == "error"]
    if errors:
        raise ValueError("输入 v1 未通过验证：" + json.dumps(errors, ensure_ascii=False))
    result["schema_version"] = "2.0"
    warnings = []
    if unknown:
        result["extension_data"]={"legacy_unrecognized_fields":unknown}
        warnings.append({"code":"unrecognized-preserved","message":"未识别字段按原路径保存在 extension_data.legacy_unrecognized_fields；未推断其架构含义。","count":len(unknown)})
    for rel in result["relationships"]:
        if "cardinality" in rel:
            rel["cardinality"] = {end: copy.deepcopy(LEGACY_CARDINALITY[value]) for end, value in rel["cardinality"].items()}
    # Namespace declarations and their references as one operation. An auditable
    # mapping preserves every old vocabulary value; stable object IDs and the
    # arbitrary payloads themselves are never rewritten by string replacement.
    renames=[]
    extension=result.get('extensions',{})
    maps={}
    for kind in ['entity_types','relationship_types','data']:
        values=extension.get(kind,{})
        occupied=set(values)
        mapping={}
        for name in list(values):
            if NAMESPACE.fullmatch(name):continue
            stem=re.sub(r'[^A-Za-z0-9_.:-]','_',name)
            if not stem or not stem[0].isalnum():stem='value_'+stem
            base='legacy:'+stem;new=base;suffix=2
            while new in occupied:
                new=base+'_'+str(suffix);suffix+=1
            occupied.add(new);mapping[name]=new
            values[new]=values.pop(name)
            renames.append({'kind':kind,'from':name,'to':new})
        maps[kind]=mapping
    for entity in result['entities']:
        entity['type']=maps['entity_types'].get(entity['type'],entity['type'])
    for relationship in result['relationships']:
        relationship['type']=maps['relationship_types'].get(relationship['type'],relationship['type'])
    for rule in extension.get('relationship_types',{}).values():
        for end in ['source_types','target_types']:
            rule[end]=[maps['entity_types'].get(value,value) for value in rule[end]]
    if renames:
        result.setdefault('extension_data',{})['togaf:migration']={'vocabulary_renames':renames}
        warnings.append({'code':'legacy-extension-namespaced','message':'旧扩展词汇已改为无冲突命名空间，并同步更新类型引用；原名称与新名称见映射。','mappings':renames})
    pending=[]
    for obj in [result['project']]+result['entities']+result['deliverables']:
        if 'decision_status' in obj:
            pending.append({'id':obj['id'],'legacy_status':obj['decision_status'],
                            'fields':['approval_status','implementation_status'],
                            'reason':'旧单一状态不足以分别证明批准决定与实现进度；未自动推断。'})
    for obj in result['entities']:
        if obj.get('evolution',obj.get('context',{}).get('evolution'))=='transition':
            pending.append({'id':obj['id'],'fields':['state_id'],'reason':'需人工确认命名过渡状态及其可运营条件。'})
    # Preserve identity, facts, arbitrary attribute payloads and source evidence exactly.
    return result, {"changed": True, "from": "1.0", "to": "2.0", "warnings": warnings,
                    "pending_confirmations":pending,
                    "notice": "转换版本、基数与旧扩展命名空间；不会推断命名过渡状态、profile、批准、实现或项目事实。"}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model");parser.add_argument("--out",required=True);parser.add_argument("--report")
    args=parser.parse_args();source=Path(args.model);out=Path(args.out);report_path=Path(args.report) if args.report else None
    if source.resolve()==out.resolve():parser.error("迁移不得写回输入；请选择新的 --out 文件")
    if report_path and report_path.resolve() in [source.resolve(),out.resolve()]:parser.error("--report 必须与输入和 --out 使用不同文件")
    for destination in [out]+([report_path] if report_path else []):
        if destination.exists():parser.error('迁移输出必须是新文件，拒绝覆盖：'+str(destination))
    try:
        result,report=migrate(json.loads(source.read_text()))
        report["validation"] = validate(result)
        if any(i["level"]=="error" for i in report["validation"]):raise ValueError(json.dumps(report,ensure_ascii=False))
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('x') as handle:handle.write(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
        if report_path:
            report_path.parent.mkdir(parents=True,exist_ok=True)
            with report_path.open('x') as handle:handle.write(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
        print(json.dumps(report,ensure_ascii=False,indent=2))
    except (OSError,ValueError) as exc:parser.exit(1,str(exc)+"\n")
if __name__=="__main__":main()
