# -*- coding: utf-8 -*-
"""Copy editable fictional examples and bind all local source locators to package paths."""
from pathlib import Path
import json,shutil
import sys,copy,hashlib,argparse
C=Path(__file__).resolve().parents[1];P=C/'skills';H=C/'maintenance/cases/omnichannel';D=P/'_shared/examples/omnichannel'
def export_adm_delivery(source):
 source=Path(source).resolve();target=D/'adm-delivery'
 manifest=json.loads((source/'summary.json').read_text())
 if manifest.get('structured_deliverables')!=23 or manifest.get('independent_business_accepted') is not False:
  raise ValueError('expected current 23-deliverable fictional case with explicit acceptance boundary')
 target.mkdir(parents=True,exist_ok=True);(target/'cycles').mkdir(exist_ok=True)
 (target/'materials').mkdir(exist_ok=True)
 for path in (source/'materials').iterdir():
  if path.is_file():shutil.copy2(path,target/'materials'/path.name)
 shutil.copy2(source/'stage-deliverable-map.json',target/'stage-deliverable-map.json')
 from adm import iteration_fingerprint,requirements_fingerprint,requirements_context,check_cycle
 from validate import validate
 models={};rewrites=[]
 for name,origin in [('model',source/'model.json'),('model-policy-v2',source/'counterexamples/policy-v2-model.json')]:
  model=json.loads(origin.read_text())
  for entry in model['sources']:
   before=entry.get('locator','');fragment='#'+before.split('#',1)[1] if '#' in before else ''
   for basename in ['adm-delivery-materials.json','adm-business-materials.md','sufficient-business-materials.md']:
    if basename in before:
     entry['locator']='_shared/examples/omnichannel/adm-delivery/materials/'+basename+fragment;break
   else:
    if 'role-skill-inputs.json' in before:entry['locator']='_shared/examples/omnichannel/sufficient-role-skill-inputs.json'
    elif 'raw-business-materials.md' in before:entry['locator']='_shared/examples/omnichannel/raw-business-materials.md'+fragment
    elif entry['id']=='g249-table-source':entry['locator']='_shared/corpus/sources/pdf/G249e.pdf#page=27'
   if entry.get('locator')!=before:rewrites.append({'model':name,'source_id':entry['id'],'before':before,'after':entry['locator']})
  errors=[x for x in validate(model) if x['level']=='error']
  if errors:raise ValueError(errors)
  models[name]=model;(target/(name+'.json')).write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
 cycle=json.loads((source/'cycles/cycle.json').read_text());model=models['model']
 for phase in cycle['phases']:
  it=phase['iterations'][-1];current=iteration_fingerprint(model,it,cycle['scope']);it['model_sha256']=current
  for step in it['source_step_coverage']:step['context_sha256']=current
  for review in cycle['requirements']['reviews']:
   if review['iteration_id']==it['id']:review['model_sha256']=requirements_fingerprint(model,cycle,phase['phase'])
 for step in cycle['requirements']['source_step_coverage']:step['context_sha256']=requirements_context(model,cycle)
 (target/'cycles/cycle.json').write_text(json.dumps(cycle,ensure_ascii=False,indent=2)+'\n')
 checked=check_cycle(cycle,model,target/'cycles');changed=check_cycle(cycle,models['model-policy-v2'],target/'cycles')
 assert not checked['errors'] and checked['recorded_cycle_complete'] and checked['foundation_source_coverage_complete'],checked
 assert not changed['recorded_cycle_complete'] and not changed['foundation_source_coverage_complete'],changed
 record={'schema_version':'adm-delivery-relocation/1','passed':True,'structured_deliverables':23,'chapters':90,
  'source_model_sha256':hashlib.sha256((source/'model.json').read_bytes()).hexdigest(),
  'source_cycle_sha256':hashlib.sha256((source/'cycles/cycle.json').read_bytes()).hexdigest(),
  'source_material_sha256':hashlib.sha256((source/'materials/adm-delivery-materials.json').read_bytes()).hexdigest(),
  'source_locator_rewrites':rewrites,'only_source_locators_and_context_fingerprints_changed':True,
  'baseline_cycle_recorded_complete':True,'policy_v2_old_cycle_recorded_complete':False,
  'independent_business_accepted':False,'real_business_approval':'not-granted'}
 (target/'relocation-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 (target/'README.md').write_text('''# 同一情景的ADM与正式交付物\n\n模型含23种候选正式交付物、90章具体论证、33视图，与9阶段/94来源步骤在同一模型及周期中关联。原始材料和本轮新增的交付物材料补充位于materials/；新增计划是作者提案，未冒称旧情景已审批新文档。全部候选，真实批准及全范围独立业务接受未授予。\n\n从skills包根目录执行：\n\n```sh\npython3 -B _shared/scripts/local_tool.py validate _shared/examples/omnichannel/adm-delivery/model.json --report work/adm-delivery-validation.json\npython3 -B _shared/scripts/local_tool.py adm check --model _shared/examples/omnichannel/adm-delivery/model.json --cycle _shared/examples/omnichannel/adm-delivery/cycles/cycle.json --require-complete --require-source-coverage\npython3 -B _shared/scripts/local_tool.py generate _shared/examples/omnichannel/adm-delivery/model.json --out work/adm-delivery --all --strict\npython3 -B _shared/scripts/local_tool.py adm report --model _shared/examples/omnichannel/adm-delivery/model-policy-v2.json --cycle _shared/examples/omnichannel/adm-delivery/cycles/cycle.json\n```\n\n最后一项应显示政策2→1件、24→8小时改变后旧记录需要重审。文本/JSON/适用SVG实际生成不代替PNG目视或专业语义验收。应用迁移排期只选有给定窗口的工作包，生产应用迁移日期未知。\n\n[输入材料](materials/adm-delivery-materials.json) · [阶段映射](stage-deliverable-map.json) · [仅路径重定位记录](relocation-record.json)\n''')
 return target

def main(adm_delivery_case=None):
 D.mkdir(parents=True,exist_ok=True)
 for name in ['raw-business-materials.md','role-skill-inputs.json','sufficient-business-materials.md','sufficient-role-skill-inputs.json','shared-policy-contract.json']:
  shutil.copy2(H/name,D/name)
 for name in ['baseline','offline-change','shared-object-change','sufficient','sufficient-policy-change']:
  m=json.loads((H/'generated'/name/'model.json').read_text())
  for src in m['sources']:
   loc=src.get('locator','');frag='#'+loc.split('#',1)[1] if '#' in loc else ''
   if 'raw-business-materials.md' in loc:src['locator']='_shared/examples/omnichannel/raw-business-materials.md'+frag
   elif 'role-skill-inputs.json' in loc:src['locator']='_shared/examples/omnichannel/'+('sufficient-role-skill-inputs.json' if name.startswith('sufficient') else 'role-skill-inputs.json')
   elif 'sufficient-business-materials.md' in loc:src['locator']='_shared/examples/omnichannel/sufficient-business-materials.md'+frag
   elif src['id']=='g249-table-source':src['locator']='_shared/corpus/sources/pdf/G249e.pdf#page=27'
  (D/(name+'.json')).write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
 # Preserve the ADM example as an explicit fictional record. Only relocate
 # source locators/fingerprints; no decision or evidence wording is upgraded.
 sys.path[:0]=[str(P/'_shared/scripts'),str(P/'_shared/vendor')]
 from adm import iteration_fingerprint,requirements_fingerprint,requirements_context,check_cycle
 raw=H/'adm-business-materials.md';shutil.copy2(raw,D/raw.name)
 target=D/'adm';(target/'cycles').mkdir(parents=True,exist_ok=True)
 models={}
 for name in ['model','model-policy-v2']:
  model=json.loads((H/'generated-adm'/(name+'.json')).read_text())
  for source in model['sources']:
   loc=source.get('locator','');fragment='#'+loc.split('#',1)[1] if '#' in loc else ''
   for basename in ['adm-business-materials.md','sufficient-business-materials.md','raw-business-materials.md']:
    if basename in loc:source['locator']='_shared/examples/omnichannel/'+basename+fragment;break
   else:
    if 'role-skill-inputs.json' in loc:source['locator']='_shared/examples/omnichannel/sufficient-role-skill-inputs.json'
    elif source['id']=='g249-table-source':source['locator']='_shared/corpus/sources/pdf/G249e.pdf#page=27'
  models[name]=model;(target/(name+'.json')).write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
 cycle=json.loads((H/'generated-adm/cycles/cycle.json').read_text());model=models['model']
 for phase in cycle['phases']:
  current=phase['iterations'][-1];fingerprint=iteration_fingerprint(model,current,cycle['scope']);current['model_sha256']=fingerprint
  for record in current['source_step_coverage']:record['context_sha256']=fingerprint
  review=next(r for r in cycle['requirements']['reviews'] if r['iteration_id']==current['id']);review['model_sha256']=requirements_fingerprint(model,cycle,phase['phase'])
 for record in cycle['requirements']['source_step_coverage']:record['context_sha256']=requirements_context(model,cycle)
 (target/'cycles/cycle.json').write_text(json.dumps(cycle,ensure_ascii=False,indent=2)+'\n')
 report=check_cycle(cycle,model,target/'cycles');assert report['recorded_cycle_complete'] and report['foundation_source_coverage_complete'],report
 changed=copy.deepcopy(cycle);original=json.loads((H/'generated-adm/cycles/cycle-policy-v2-needs-review.json').read_text());changed['requirements']['changes']=original['requirements']['changes']
 (target/'cycles/cycle-policy-v2-needs-review.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2)+'\n')
 report2=check_cycle(changed,models['model-policy-v2'],target/'cycles');assert not report2['recorded_cycle_complete'] and not report2['foundation_source_coverage_complete']
 (target/'relocation-record.json').write_text(json.dumps({'origin':'fictional-source-locator-relocation','source_cycle_sha256':hashlib.sha256((H/'generated-adm/cycles/cycle.json').read_bytes()).hexdigest(),'source_locator_rewrites':True,'evidence_content_or_decisions_changed':False,'real_business_approval':'not-granted','legacy_policy_evidence_retained_as_stale':True},ensure_ascii=False,indent=2)+'\n')
 (D/'README.md').write_text('''# 虚构全渠道履约示例

从skills包根目录执行。baseline、offline-change、shared-object-change保留未定业务、能力及容量；sufficient与sufficient-policy-change只在声明的虚构证据范围内完成方案比较、角色配置和复评。实际业务批准始终未授予。

```bash
python3 -B _shared/scripts/local_tool.py validate _shared/examples/omnichannel/sufficient.json --report work/validation.json
python3 -B _shared/scripts/local_tool.py generate _shared/examples/omnichannel/sufficient.json --out work/example --all --render --strict
python3 -B _shared/scripts/local_tool.py policy _shared/examples/omnichannel/sufficient-policy-change.json --contract _shared/examples/omnichannel/shared-policy-contract.json --before _shared/examples/omnichannel/sufficient.json --out work/policy-check.json
```

业务原料与人员证据同目录保存。所有时间、人员、评级、测量和政策均为教学数据；输出不代表生产测量或组织已签认。包内来源定位相对skills包根目录。
''')
 print({'variants':5,'local_example_directory':D.relative_to(P).as_posix()})
 with (D/'README.md').open('a') as f:f.write('''\n## ADM全周期演练\n\n[原始材料](adm-business-materials.md)及[共享模型](adm/model.json)关联Preliminary、A—H和持续需求管理94项来源步骤。所有签署、测量与交付均是给定虚构情景，非实际批准。重定位仅改写来源路径及相应输入指纹，见[迁移记录](adm/relocation-record.json)。\n\n```bash\npython3 -B _shared/scripts/local_tool.py adm check --model _shared/examples/omnichannel/adm/model.json --cycle _shared/examples/omnichannel/adm/cycles/cycle.json --require-complete --require-source-coverage\npython3 -B _shared/scripts/local_tool.py adm report --model _shared/examples/omnichannel/adm/model-policy-v2.json --cycle _shared/examples/omnichannel/adm/cycles/cycle-policy-v2-needs-review.json\n```\n\n第二条命令显示政策变化后需要复核的旧记录，不会自动重新批准。\n''')
 if adm_delivery_case:export_adm_delivery(adm_delivery_case)
 if (D/'adm-delivery/model.json').is_file():
  with (D/'README.md').open('a') as f:f.write('\n## ADM到正式交付物\n\n[新增同一情景贯通案例](adm-delivery/README.md)将阶段工作关联到23种结构化正式交付物、90章正文及实际生成接口；候选状态和独立业务接受边界保留。此前adm/中的阶段案例与0正式交付物历史仍保留。\n')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--adm-delivery-case',type=Path)
 main(parser.parse_args().adm_delivery_case)
