#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify actual inspection fingerprints and all five deliveries; never auto-review new bytes."""
from pathlib import Path
import json,hashlib,re,datetime,sys
from urllib.parse import urlparse
from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from source_paths import resolve as source_path
H=Path(__file__).resolve().parent;C=H.parents[2];PROJECT=C.parent
VARIANTS=('baseline','offline-change','shared-object-change','sufficient','sufficient-policy-change')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
NOTES={
'capability-map':'能力边界及3条分解关系可辨；空分类不表示不适用。政策版保留稳定CAP-RESERVE和明确版本。',
'development-plan':'发展动作与复评分别列示；未知为中文未知。课程记录不升级；充分版新增虚构行为观察，旧记录保留。',
'interface-network':'提供/消费关系按连线编号读；在线最终确认需中央原子预占。充分版实验只支持给定300ms目标下的候选建议。',
'order-states':'受理、确认、异常及物流交接分开；充分版确认条件明确为中央原子预占成功。',
'offline-data-boundary':'门店持久记录与中央接收/承诺记录分开；接收不自动成为履约确认。',
'risk-treatment':'控制、演练期间与剩余风险可读；政策版携带当前额度与期限，不虚构残余风险分数。',
'role-assignment':'全部选定主体和全部关系在主图直接表达；关系类型说明区分职责、配置和证据，不推断人事汇报。',
'role-collaboration':'首席角色的特例关系、跨分段指导、约束、协作和交接分别表达；政策版交接显示当前版本。',
'skill-matrix':'官方参考、项目目标与人员观察分开；Chief/通用Segment无伪造官方列。长图需按原尺寸或Markdown读取。',
'transition-roadmap':'工作包、运营状态与日期可读；政策版联动运营条件及恢复安排。候选计划不等于上线授权。'}
def main():
 inspected=load(H/'current-visual-inspections.json');known={x['png_sha256']:x for x in inspected['records']};rows=[];issues=[];sources=[];checked=0
 for variant in VARIANTS:
  folder=H/'generated'/variant;manifest=load(folder/'manifest.json');model=load(folder/'model.json')
  for rel,h in manifest['output_sha256'].items():
   p=folder/rel
   if not p.is_file() or sha(p)!=h:issues.append({'code':'output-hash','variant':variant,'path':rel})
   checked+=1
  for png in sorted((folder/'artifacts').glob('*.png')):
   h=sha(png);svg=png.with_suffix('.svg');art=load(png.with_suffix('.json'));text=svg.read_text()
   entities=set(re.findall(r'data-entity-id="([^"]+)"',text));relations=set(re.findall(r'data-relationship-id="([^"]+)"',text));v=art['view']
   missing_e=sorted(set(v['entity_ids'])-entities);missing_r=sorted(set(v['relationship_ids'])-relations)
   if h not in known:issues.append({'code':'image-not-actually-inspected','path':str(png.relative_to(H)),'sha256':h})
   if missing_e or missing_r:issues.append({'code':'missing-main-identity','variant':variant,'view':png.stem,'entities':missing_e,'relations':missing_r})
   rows.append({'variant':variant,'view_id':png.stem,'png_path':str(png.relative_to(H)),'svg_path':str(svg.relative_to(H)),'png_sha256':h,'svg_sha256':sha(svg),'inspection':known.get(h),'dimensions':list(Image.open(png).size),'visible_main_entity_count':len(entities),'visible_main_relation_count':len(relations),'selected_entities':v['entity_ids'],'selected_relations':v['relationship_ids'],'missing_main_entities':missing_e,'missing_main_relations':missing_r,'observation_zh':NOTES[png.stem],'layout_observation_zh':'文字和主体可辨，无框内截断；JSON较密处可读配套Markdown。正交线偶有交叉，按编号和关系清单核对，不把交叉当连接。'})
  for source in model['sources']:
   loc=source.get('locator','');path,_,anchor=loc.partition('#');candidate=None;status='missing'
   if path.startswith(('http://','https://')):status='external-citation-not-network-verified'
   else:
    for option in (PROJECT/path,H/path,C/'skills/_shared'/path):
     if source_path(option).is_file():candidate=source_path(option);break
    if candidate:
     status='file-verified'
     if anchor and not anchor.startswith('page=') and f'id="{anchor}"' not in candidate.read_text():status='anchor-missing'
     if anchor.startswith('page='):
      import fitz
      number=int(anchor.split('=',1)[1]);pdf=fitz.open(candidate)
      if not 1<=number<=len(pdf):status='pdf-page-missing'
      pdf.close()
   row={'variant':variant,'id':source['id'],'locator':loc,'status':status,'resolved':str(candidate.relative_to(C)) if candidate and C in candidate.parents else None,'sha256':sha(candidate) if candidate else None};sources.append(row)
   if status in ('missing','anchor-missing','pdf-page-missing'):issues.append({'code':'source-location',**row})
 if len(rows)!=49:issues.append({'code':'image-count','actual':len(rows),'expected':49})
 assignments=[r for r in rows if r['view_id']=='role-assignment']
 for r in assignments:
  expected=12 if r['variant'].startswith('sufficient') else 7
  if r['visible_main_relation_count']!=expected:issues.append({'code':'assignment-main-relations','variant':r['variant'],'actual':r['visible_main_relation_count'],'expected':expected})
 report={'schema_version':'omnichannel-current-delivery/2','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':not issues,'counts':{'variants':5,'png_svg_pairs':len(rows),'unique_inspected_png_hashes_in_current_delivery':len({r['png_sha256'] for r in rows}),'manifest_output_files_checked':checked,'source_references':len(sources)},'visual_rows':rows,'source_locations':sources,'issues':issues,'business_approval':'not-granted','review_independence':'same-task visual check and separate forward implementation; not different-reviewer final semantic acceptance','input_sha256':{'maintenance/cases/omnichannel/current-visual-inspections.json':sha(H/'current-visual-inspections.json')},'supersedes':'delivery-closeout-report.json; historical19-pair report archived in review-history/closeout-v1','limits_zh':['静态PNG不支持点击；配套Markdown和SVG含明细入口。技能矩阵应打开原尺寸。','字节相同重复图继承实际查看证据；SVG另核所选主体及关系全部出现。','图像可读、源路径存在和业务正确分别取证；本报告不授予组织批准。']}
 (H/'current-delivery-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# 当前五版案例交付与逐图复核','',f"结果：{'通过' if report['passed'] else '未通过'}。49对PNG/SVG、32种不同图像字节逐项对应实际目视证据；{checked}项生成文件指纹核对。",'','三版未知案例的配置图各显示11个主体和7条关系；充分虚构案例两版各显示16个主体和12条关系。能力、容量、期间和批准分别记录。','','|版本|图|主体/关系|说明|','|---|---|---|']
 for r in rows:lines.append(f"|{r['variant']}|[{r['view_id']}]({r['png_path']})|{r['visible_main_entity_count']} / {r['visible_main_relation_count']}|{r['observation_zh']}|")
 lines+=['','技能矩阵较高，建议打开原尺寸或配套Markdown。关系线按编号核对；静态PNG不能点击明细提示。','','[机器报告](current-delivery-review.json) · [固定目视指纹](current-visual-inspections.json) · [前向验证](forward-acceptance.json)','', '旧19对报告仅是历史版本证据，原件已保存到[历史目录](review-history/closeout-v1/delivery-closeout-report.md)。本报告是同一任务内的视觉复核，不冒充另一位评审人的最终语义验收。真实业务批准未授予。','']
 (H/'current-delivery-review.md').write_text('\n'.join(lines));print({'passed':report['passed'],'counts':report['counts'],'issues':issues});return int(not report['passed'])
if __name__=='__main__':raise SystemExit(main())
