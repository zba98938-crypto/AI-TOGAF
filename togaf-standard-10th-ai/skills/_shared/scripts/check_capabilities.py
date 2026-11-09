#!/usr/bin/env python3
"""Check registered capability entrypoints and actual output evidence separately."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from registry import ROOT,load

def check(examples=None,allow_drafts=False):
    arts,dels,profiles,methods=load();errors=[];rows=[]
    cap=json.loads((ROOT/"capabilities.json").read_text())
    def error(identity,message):errors.append({"id":identity,"message":message})
    for group in [cap.get("work_products",[]),list(profiles.values()),methods]:
        seen=set()
        for item in group:
            identity=item["id"]
            if identity in seen:error(identity,"重复注册 ID")
            seen.add(identity)
            if not item.get("source_refs"):error(identity,"缺少来源定位")
            if not (ROOT.parent/item.get("owner","")/"SKILL.md").is_file():error(identity,"主责技能不可达")
    if examples:
        for layout in ['reference','adaptive']:
            folder=Path(examples)/layout;path=folder/'manifest.json'
            manifest=json.loads(path.read_text()) if path.exists() else {}
            for key,local in [('capabilities_sha256','capabilities.json'),('renderer_sha256','scripts/profile_render.py'),('generator_sha256','scripts/generate.py'),('table_renderer_sha256','scripts/table_expression.py'),('metamodel_sha256','metamodel.json'),('artifacts_sha256','artifacts.json'),('deliverables_sha256','deliverables.json'),('assembly_renderer_sha256','scripts/deliverable_assembly.py'),('assembly_rules_sha256','capability-addenda/deliverable-assembly-rules.json')]:
                expected=hashlib.sha256((ROOT/local).read_bytes()).hexdigest()
                if manifest.get(key)!=expected:error(layout,'输出版本过期或缺少指纹：'+key)
            from runtime_provenance import fingerprints
            if manifest.get('implementation_dependencies_sha256')!=fingerprints(ROOT):
                error(layout,'执行依赖指纹过期或缺失：implementation_dependencies_sha256')
            identities=[entry.get('view_id') for entry in manifest.get('artifacts',[])]
            if len(identities)!=len(set(identities)):
                error(layout,'实际视图ID重复，可能发生同族多视图覆盖')
            for entry in manifest.get('artifacts',[]):
                registered=profiles.get(entry.get('profile_id'))
                if not registered:
                    error(entry.get('view_id',layout),'输出引用未注册的视图规范')
                    continue
                if entry.get('id')!=registered['artifact_id']:
                    error(entry.get('view_id',layout),'输出制品族与视图规范不一致')
                if entry.get('profile_version')!=registered.get('version','2.0'):
                    error(entry.get('view_id',layout),'输出视图规范版本与当前登记不一致')
            model_path=folder/'model.json'
            if model_path.exists():
                expected=hashlib.sha256(json.dumps(json.loads(model_path.read_text()),ensure_ascii=False,sort_keys=True).encode()).hexdigest()
                if manifest.get('model_sha256')!=expected:error(layout,'生成模型指纹不符')
    for profile in profiles.values():
        if profile["artifact_id"] not in arts:error(profile["id"],"制品族未注册")
        template=profile.get('template',{})
        if template.get('source_verified') and 'awaiting' in template.get('review_status',''):
            error(profile['id'],'来源模板仍待核查，不能同时声明 source_verified=true')
        row={"id":profile["id"],"artifact_id":profile["artifact_id"],"definition":"registered",
             "source_verification":profile.get("source_status",profile.get("template",{}).get("source_status","not-certified")),
             "outputs":[],"visual_acceptance":"not-implied-by-engineering-checks"}
        if examples:
            for layout in ["reference","adaptive"]:
                folder=Path(examples)/layout
                path=folder/"manifest.json"
                manifest=json.loads(path.read_text()) if path.exists() else {"artifacts":[]}
                entries=[a for a in manifest["artifacts"] if a.get("profile_id")==profile["id"]]
                evidence={"layout":layout,"generated":bool(entries),"views":[]}
                if not entries:error(profile["id"],layout+" 布局缺少实际输出")
                for entry in entries:
                    if profile.get('output_kind')=='table':
                        exists=all((folder/entry[k]).is_file() for k in ['path','json'])
                        if not exists:error(entry['view_id'],'表格输出或模型引用缺失')
                        cov_path=folder/entry.get('coverage','missing-coverage')
                        cov=json.loads(cov_path.read_text()) if cov_path.is_file() else {}
                        payload=json.loads((folder/entry['json']).read_text())
                        if set(payload['view']['entity_ids'])!=set(cov.get('represented_entity_ids',[])) or set(payload['view']['relationship_ids'])!=set(cov.get('represented_relationship_ids',[])):error(entry['view_id'],'表格所选对象/关系未完整表达')
                        if cov.get('errors'):error(entry['view_id'],'表格字段或语义存在缺口')
                        from table_expression import value
                        from generate import cell
                        md=(folder/entry['path']).read_text()
                        for key,group in [('represented_attributes','entities'),('represented_relationship_attributes','relationships')]:
                            for obj in payload[group]:
                                attrs=obj.get('attributes',{})
                                missing=set(attrs)-set(cov.get(key,{}).get(obj['id'],[]))
                                if missing:error(obj['id'],'表格属性遗漏：'+','.join(sorted(missing)))
                                if group=='entities' and any(cell(value(v)) not in md for v in attrs.values()):error(obj['id'],'表格属性值仅在模型中出现，正文未表达')
                                if group=='relationships' and attrs and cell(value(attrs)) not in md:error(obj['id'],'关系属性未在表格正文表达')
                        evidence['views'].append({'view_id':entry['view_id'],'table':exists,'coverage_record':entry.get('coverage'),'errors':cov.get('errors',[]),'status':entry.get('status')})
                        continue
                    cov=json.loads((folder/entry["coverage"]).read_text())
                    payload=json.loads((folder/entry["json"]).read_text())
                    svg=(folder/entry["svg"]).read_text()
                    from expression_details import identity_failures, location_failures
                    details=''
                    if cov.get('companion_file'):
                        dp=folder/entry.get('details','missing-details')
                        if not dp.is_file():error(entry['view_id'],'伴随明细文件缺失')
                        else:
                            details=dp.read_text()
                            if details!=cov.get('companion_html'):error(entry['view_id'],'实际明细与coverage记录不一致')
                    for failure in identity_failures(svg,details,set(payload['view']['entity_ids']),set(payload['view']['relationship_ids'])):
                        error(entry['view_id'],'实际图形/明细身份遗漏：'+str(failure))
                    if cov.get('coverage_contract')=='expression-locations/2':
                        for failure in location_failures(svg,details,cov.get('expression_locations'),cov.get('companion_file')):error(entry['view_id'],str(failure))
                    selected_e=set(payload["view"]["entity_ids"]);selected_r=set(payload["view"]["relationship_ids"])
                    represented_e=set(cov.get("represented_entity_ids",[]));represented_r=set(cov.get("represented_relationship_ids",[]))
                    missing_e=selected_e-represented_e;missing_r=selected_r-represented_r
                    png=bool(entry.get("png") and (folder/entry["png"]).is_file())
                    # Missing entities/relations must be explicit in the coverage record.
                    disclosed_e=set(cov.get("unrepresented_entity_ids",[]));disclosed_r=set(cov.get("unrepresented_relationship_ids",[]))
                    if missing_e-disclosed_e or missing_r-disclosed_r:error(entry["view_id"],"表达遗漏未披露")
                    if not allow_drafts and (missing_e or missing_r or cov.get("errors")):
                        error(entry["view_id"],layout+" 实际视图存在语义或表达缺口；披露缺口不等于通过验收")
                    if not png:error(entry["view_id"],"PNG 不存在")
                    evidence["views"].append({"view_id":entry["view_id"],"svg":bool(svg),"png":png,
                         "errors":cov.get("errors",[]),"missing_entity_ids":sorted(missing_e),"missing_relationship_ids":sorted(missing_r),
                         "status":entry.get("status"),"coverage_record":entry["coverage"]})
                row["outputs"].append(evidence)
        rows.append(row)
    return {"schema_version":"2.0","counts":{"artifact_families":len(arts),"legacy_artifact_families":len(json.loads((ROOT/"artifacts.json").read_text())["artifacts"]),
           "guide_work_products":len(cap.get("work_products",[])),"view_profiles":sum(not p.get('alias_of') for p in profiles.values()),"registered_profile_entries":len(profiles),"compatibility_aliases":sum(bool(p.get('alias_of')) for p in profiles.values()),
           "graphical_view_profiles":sum(p.get('output_kind')!='table' for p in profiles.values()),
           "legacy_default_profiles":sum(p.get('registration_class')=='legacy-default' for p in profiles.values()),
           "analysis_methods":len(methods),"deliverables":len(dels)},
           "errors":errors,"profiles":rows,"limit":"分类数量分别报告；来源定义、分析行为和目视验收不能从生成成功推定。"}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--examples");p.add_argument("--report")
    p.add_argument("--allow-drafts",action="store_true",help="仅检查输出存在及缺口披露，不将草稿计为完整能力验收")
    a=p.parse_args()
    report=check(a.examples,a.allow_drafts)
    if a.report:Path(a.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"counts":report["counts"],"errors":report["errors"]},ensure_ascii=False,indent=2))
    return int(bool(report["errors"]))
if __name__=="__main__":sys.exit(main())
