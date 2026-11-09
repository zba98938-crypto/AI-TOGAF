#!/usr/bin/env python3
"""Synchronize the G242 form profile and full example after registry builds.

This is an idempotent late-stage registry specialization. It preserves existing
profile, entity, view and source IDs; historic generated outputs remain intact.
"""
import json
from pathlib import Path
from capability_examples import specialize
from build_capabilities import base_example

ROOT=Path(__file__).resolve().parents[1]
PROFILE='sustainability-architecture-canvas'

def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    cap_path=ROOT/'capabilities.json';cap=json.loads(cap_path.read_text())
    profile=next(p for p in cap['profiles'] if p['id']==PROFILE)
    profile['renderer']='environmental-review'
    profile['required_attributes']={'sustainability_action':['block']}
    profile['checks']=['逐项表达三项业务判断、两年Scope碳表和五项措施；缺字段必须报告ID化错误，不降级为通用画布。',
                       '印刷原图差异与虚构项目数值分开，不静默改数。']
    profile.setdefault('template',{}).update({'canvas_kind':'sustainability','blocks':['业务贡献','环境核算','架构措施'],
                                               'form_contract':'G242-fig3-14/1','source_verified':False})
    specialize(profile,cap['work_products'],base_example)
    dump(cap_path,cap)
    rules_path=ROOT/'capability-addenda/deliverable-assembly-rules.json'
    rules=json.loads(rules_path.read_text())
    contract=rules['profile_metadata'][PROFILE]
    contract['required_attributes']=profile['required_attributes']
    contract['template_version']='3.0'
    dump(rules_path,rules)
    model_path=ROOT/'tests/full-example.json'
    model=json.loads(model_path.read_text());byid={e['id']:e for e in model['entities']}
    for item in profile['example']['entities']:
        full_id=PROFILE+'--'+item['id']
        if full_id not in byid:raise ValueError('full-example missing stable G242 entity ID: '+full_id)
        byid[full_id]['attributes']=item['attributes']
    dump(model_path,model)
    print(json.dumps({'profile_id':PROFILE,'renderer':profile['renderer'],'example_entities':len(profile['example']['entities'])}))

if __name__=='__main__':main()
