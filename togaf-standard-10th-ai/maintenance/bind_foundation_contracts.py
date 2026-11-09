# -*- coding: utf-8 -*-
"""Bind reviewed C220 source blocks to executable registries; preserve project status."""
from pathlib import Path
import json,re,hashlib,shutil,copy,sys
C=Path(__file__).resolve().parents[1];S=C/'skills/_shared';V='05-architecture-content'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def save(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def normalized(t):return re.sub(r'[^a-z0-9]','',re.sub(r'^\d+(?:\.\d+)*\.\s*','',t).lower())
def main():
 history=C/'maintenance/foundation-contract-history';history.mkdir(exist_ok=True)
 for rel in ['artifacts.json','deliverables.json','capabilities.json','references/adm-phases.json','schemas/model.schema.json','schemas/model-v1.schema.json']:
  target=history/rel
  if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/rel,target)
 docs={v:load(C/'fundamental/analysis'/f'{v}.json') for v in ['02-architecture-development-method',V]}
 def ref(vol,anchor,descendants=False):
  doc=docs[vol];sec=next(s for s in doc['sections'] if s['heading_id']==anchor);selected=[sec]
  number=re.match(r'^([\d.]+)\s',sec['title_en'])[1].rstrip('.')
  if descendants:selected += [s for s in doc['sections'] if s is not sec and s['title_en'].startswith(number+'.')]
  locs={l['block_id']:l for s in selected for l in s['source_locators']}
  return {'document_id':doc['document_id'],'volume_id':vol,'anchor':anchor,'section_id':sec['id'],'title_en':sec['title_en'],'path':'fundamental/analysis/'+vol+'.json','source_document_path':doc['source_document_path'],'source_document_sha256':doc['source_document_sha256'],'source_locators':list(locs.values()),'source_quotes_en':[e for s in selected for e in s['source_evidence'] if e['text_en'].strip()]}
 arts=load(S/'artifacts.json');dels=load(S/'deliverables.json');caps=load(S/'capabilities.json');adm=load(S/'references/adm-phases.json')
 added=[
 ('implementation-factor-catalog','实施因素目录','Implementation Factor Catalog','catalog',['implementation_factor'],['category','description','deduction','action_or_constraint'],'E','_implementation_factor_catalog','哪些风险、问题、假设、依赖、行动和影响改变实施与迁移计划？'),
 ('consolidated-gaps-solutions-dependencies-matrix','合并差距、方案和依赖矩阵','Consolidated Gaps, Solutions, and Dependencies Matrix','matrix',['gap','work_package'],['solution_refs','dependency_refs'],'E','_consolidated_gaps_solutions_and_dependencies_matrix','跨域差距由哪些候选方案覆盖，哪些依赖影响工作包？'),
 ('architecture-definition-increments-table','架构定义增量表','Architecture Definition Increments Table','matrix',['work_package','transition'],['increment_description'],'E','_architecture_definition_increments_table','每个项目的增量交付分配到哪个过渡架构？'),
 ('transition-architecture-state-evolution-table','过渡架构状态演进表','Transition Architecture State Evolution Table','matrix',['business_service','transition','sbb'],['service_taxonomy','proposed_state','sbb_refs'],'F','_transition_architecture_state_evolution_table','采用企业分类法时，各过渡架构中的服务及SBB怎样变化？'),
 ('business-value-risk-matrix','业务价值与风险矩阵','Business Value and Risk Matrix','matrix',['work_package'],['value_index','risk_index','criteria_basis'],'F','_business_value_and_risk_matrix','依据预先制定的价值和风险准则，怎样评价项目？')]
 for aid,zh,en,kind,types,fields,phase,anchor,question in added:
  if not any(x['id']==aid for x in arts['artifacts']):
   a={'id':aid,'name_zh':zh,'name_en':en,'kind':kind,'domains':['通用'],'owner':'togaf-migration-roadmap','question':question,'entity_types':types,'relationship_types':['traces_to','depends_on','implements_transition'],'fields':['name']+fields,'analysis':[question,'逐项记录来源与未知；结合企业裁剪决定使用范围'],'semantic_checks':['字段与关系均为项目操作表达，未提供值保留未知','候选工作包、状态和指数不自动成为已批准事实'],'sources':['C220'],'source_locator':{'volume':V,'anchor':anchor},'definition_status':'project-operational-contract','notation':'table','required_attributes':{t:[] for t in types},'default_profile_id':'c220-'+aid}
   if aid=='architecture-definition-increments-table':a['matrix']={'row_types':['work_package'],'column_types':['transition'],'relationship':'implements_transition','direction':'row-to-column','codes':[],'cell_meaning':'项目在过渡架构中的增量交付，细节须显式记录','empty_meaning':'未记录，不表示没有交付'}
   arts['artifacts'].append(a)
  pid='c220-'+aid
  if not any(p['id']==pid for p in caps['profiles']):
   # Record layouts reuse the existing table engine; tables are not source figures.
   caps['profiles'].append({'id':pid,'artifact_id':aid,'name':zh,'name_zh':zh,'owner':'togaf-migration-roadmap','renderer':'matrix' if aid=='architecture-definition-increments-table' else 'catalog','output_kind':'table','version':'1.0','entity_types':types,'relationship_types':['traces_to','depends_on','implements_transition'],'required_attributes':{t:[] for t in types},'checks':['以来源定义核对用途，组织字段和评审结论分别记录'],'source_refs':['C220 '+V+'#'+anchor],'definition_status':'project-operational-view','template':{'source_verified':False,'layout_notes':'项目表格布局；来源图另存，不声称视觉等价。'}})
  caps['default_profiles'][aid]=pid
  details={
   'implementation-factor-catalog':['为每项因素记录描述、推论及行动或约束；常见风险、问题、假设、依赖、行动和影响。','仅列风险名称而无推论时不能认为规划分析充分。'],
   'consolidated-gaps-solutions-dependencies-matrix':['把各域差距合并分组，比较覆盖一个或多个差距的候选方案及依赖，支持E/F工作包和迁移。','未评价的候选方案或依赖不默认空集合；有依据的无依赖判断需要说明。'],
   'architecture-definition-increments-table':['按指定时点的过渡架构分配项目增量交付；项目/工作包与过渡状态关系含increment_description。','连接工作包与过渡状态不等于已说明交付内容或实施完成。'],
   'transition-architecture-state-evolution-table':['采用企业服务分类法描述过渡架构及拟议转换，保留所有相关SBB对服务的交付或影响。','来源颜色和状态为示例，不能强制所有组织采用；缺服务、状态或过渡引用保持缺口。'],
   'business-value-risk-matrix':['价值和风险分别建立指数；由高层在方案已知前制定并批准准则及权重。','未评价指数保持未知；不补0、等权或批准。项目assessed状态须有先验准则日期、权重、原始评分与来源，可复算后仍需实际评审。']}
  current=next(x for x in arts['artifacts'] if x['id']==aid)
  current['analysis']=[question,details[aid][0]]
  current['semantic_checks']=[details[aid][1],'候选设计、指数和生成结果不自动构成组织接受或实际批准。']
 if not any(d['id']=='implementation-governance-model' for d in dels['deliverables']):
  dels['deliverables'].append({'id':'implementation-governance-model','name_zh':'实施治理模型','name_en':'Implementation Governance Model','owner':'togaf-implementation-governance','adm':'E F G','entity_types':['role','actor','milestone','decision'],'artifact_ids':['role-catalog','actor-role-matrix'],'sections':[{'title':'治理过程','instruction':'明确实施期间的评审、问题升级、偏离与变更流程。'},{'title':'治理组织结构','instruction':'记录适用的既有机构与项目治理接口。'},{'title':'治理角色与责任','instruction':'记录决策权、执行责任与授权依据。'},{'title':'治理检查点与成功失败准则','instruction':'为检查点规定可验证条件及证据；未知或候选状态保留。'}],'semantic_checks':['治理组织或检查点存在不表示已授权或已符合架构','采用已有治理框架时仍需核对项目适用性'],'sources':['C220'],'definition_status':'project-operational-contract'})
 titles={}
 for s in docs[V]['sections']:
  if re.match(r'^3\.6\.\d+\.\d+\.',s['title_en']):titles.setdefault(normalized(s['title_en']),[]).append(s['heading_id'])
 aliases={'goal-objective-service-diagram':'goalobjectivebusinessservicediagram'}
 supporting={'constraints-catalog':('02-architecture-development-method','tag_03_03_04'),'requirements-impact-assessment':(V,'tag_04_02_18')}
 bindings=[]
 for a in arts['artifacts']:
  if a['id'] in supporting:
   vol,anchor=supporting[a['id']];refs=[ref(vol,anchor,True)];match='supporting-concept-not-same-named-artifact'
  else:
   key=aliases.get(a['id'],normalized(a['name_en']));anchors=titles.get(key,[]);assert anchors,(a['id'],key)
   refs=[ref(V,i,True) for i in anchors];match='direct-purpose-title' if a['id'] not in aliases else 'explicit-name-alias'
  a['foundation_binding']={'match_kind':match,'refs':refs,'field_origin':'project-operationalization','source_visual_equivalence':False}
  phase_groups={'2':'Preliminary','3':'A','4':'B','5':'C','6':'C','7':'D','8':'E','9':'F','10':'Requirements'}
  a['foundation_phase_suggestions']=list(dict.fromkeys(phase_groups[m[1]] for r in refs if r['volume_id']==V for m in [re.match(r'^3\.6\.(\d+)\.',r['title_en'])] if m and m[1] in phase_groups))
  a['sources']=list(dict.fromkeys(a['sources']+['C220']));bindings.append({'kind':'artifact','id':a['id'],**a['foundation_binding']})
 da={'architecture-building-blocks':'01','architecture-contract':'02','architecture-definition-document':'03','architecture-principles':'04','architecture-repository':'05','architecture-requirements-specification':'06','architecture-roadmaps':'07','architecture-vision':'08','business-principles':'09','business-goals-objectives':'09','business-drivers':'09','capability-assessment':'10','change-request':'11','communications-plan':'12','compliance-assessment':'13','implementation-migration-plan':'14','implementation-governance-model':'15','organization-model':'16','request-for-architecture-work':'17','requirements-impact-assessment':'18','solution-building-blocks':'19','statement-of-work':'20','tailored-architecture-framework':'21'}
 for d in dels['deliverables']:
  d['foundation_binding']={'match_kind':'split-source-description' if da[d['id']]=='09' else 'direct-source-description','refs':[ref(V,'tag_04_02_'+da[d['id']],True)],'field_origin':'project-assembly-convention','source_visual_equivalence':False};d['sources']=list(dict.fromkeys(d['sources']+['C220']));bindings.append({'kind':'deliverable','id':d['id'],**d['foundation_binding']})
 phase_chapters={'Preliminary':[2],'A':[3],'B':[4],'C':[5,6,7],'D':[8],'E':[9],'F':[10],'G':[11],'H':[12],'Requirements':[13]}
 # The Requirements steps are table rows, with distinct responsibility columns.
 source=load(C/'fundamental/web-2025/volumes/02-architecture-development-method/document.json')
 rm_table=next(b for b in source['blocks'] if b['id'].endswith(':b01083'))
 rm_zh=[
 '各阶段从业务目标、价值流、场景、用户体验或管理信息识别需求，记入架构需求规格及需求存储库。',
 '需求管理过程组织建立基线，记录优先级并确认利益相关者同意；结合13.5.1，实际处置和排序由相关ADM阶段承担，不能把过程列当独立决定权。',
 '需求管理持续监控已建立的需求基线。',
 '各阶段识别新增或变化：移除、重新评价优先级、增加需求或修改既有需求。',
 '需求管理确保当前阶段架构师和利益相关者确定并记录优先级，处理冲突并产生需求影响评估。变更可从任意渠道到来；记录决定，核对利益相关者满意度并推动问题解决。',
 '各阶段评价对当前及既往阶段的影响，决定本周期实施还是留待后续周期；实施时评价变更时间安排，并发布n+1版需求影响评估。',
 '各阶段实施来自H阶段的需求；需求管理过程确保这些新需求和变更得到管理。',
 '需求管理更新架构需求存储库，包括被请求的变更及受影响的利益相关者视图。',
 '各阶段在当前阶段实施已决定的变更。',
 '各阶段复核既往差距分析。这里gap requirement特指基线内容被意外移除而需修订目标架构的情况；须处置、记录入库并相应修订目标，不能把所有新目标差距都称为此类需求。']
 for p in adm['phases']+[adm['requirements_management']]:
  phase=p.get('id','Requirements');chapters=phase_chapters[phase];p['foundation_binding']={'match_kind':'phase-source-contract','refs':[ref('02-architecture-development-method','chap%02d'%n,True) for n in chapters],'field_origin':'project-execution-contract'}
  step_records=[]
  for n in chapters:
   prefix='%d.3.'%n
   for section in docs['02-architecture-development-method']['sections']:
    if section['title_en'].startswith(prefix):
     number=re.match(r'^([\d.]+)\s',section['title_en'])[1].rstrip('.')
     if len(number.split('.'))!=3:continue
     step_records.append({'id':section['id'],'name_en':section['title_en'],'explanation_zh':section['concepts_zh'],'decisions_zh':section['decisions_zh'],'source_ref':ref('02-architecture-development-method',section['heading_id'],True)})
  if phase=='Requirements':
   p['interpretation_issues']=[{'id':'C220-RM-PRIORITIZATION','kind':'cross-section-qualification','source_refs':[ref('02-architecture-development-method','tag_13_03'),ref('02-architecture-development-method','tag_13_05_01')],'explanation_zh':'13.3表把建立基线与记录优先级列为Requirements Management Steps；13.5.1明确过程本身不处置、解决或排序需求，由相关ADM阶段执行。按过程组织/记录与阶段实际决定区分责任，不由表列推断独立批准权。','operation_origin':'project-interpretation-with-source-qualification'}]
   for i,row in enumerate(rm_table['cells'][1:],1):
    occupied=[n for n in (1,2) if row[n]['text_en'].strip()];assert len(occupied)==1
    col=occupied[0];sr=ref('02-architecture-development-method','tag_13_03')
    sr['source_locators']=[x for x in sr['source_locators'] if x['block_id']==rm_table['id']]
    sr['source_quotes_en']=[{'block_id':rm_table['id'],'text_en':row[col]['text_en']}]
    step_records.append({'id':rm_table['id']+':step-%02d'%i,'name_en':row[0]['text_en'],'source_row':i,'responsibility_column':rm_table['cells'][0][col]['text_en'],'responsibility_column_index':col,'text_en':row[col]['text_en'],'explanation_zh':[rm_zh[i-1]],'interpretation_kind':'source-bound-project-explanation','source_ref':sr})
  p['source_step_records']=step_records;p['source_refs']=list(dict.fromkeys(p.get('source_refs',[])+['C220 ADM '+','.join(str(n) for n in chapters)]));bindings.append({'kind':'phase','id':phase,**p['foundation_binding'],'source_step_count':len(step_records)})
 # F lists the governance model conditionally; G uses the applicable governance.
 governance=next(d for d in dels['deliverables'] if d['id']=='implementation-governance-model')
 governance['adm']='F G'
 governance['phase_applicability']=[{'phase':'F','role':'conditional-output','condition_en':'Implementation Governance Model (if any)','source_ref':ref('02-architecture-development-method','tag_10_04')},{'phase':'G','role':'governance-context','origin':'project-routing','condition_zh':'采用适用治理模型指导实施监督；不宣称G重复制定F输出。'}]
 f=next(p for p in adm['phases'] if p['id']=='F')
 if governance['id'] not in f['deliverables']:f['deliverables'].append(governance['id'])
 f['conditional_deliverables']=[{'id':governance['id'],'condition_en':'if any','source_anchor':'tag_10_04'}]
 for aid,*_ in added:
  a=next(x for x in arts['artifacts'] if x['id']==aid)
  lines=['# '+a['name_zh'],'',a['question'],'','这是依据C220用途形成的项目操作契约。字段、布局及判据不声称为官方规定。','','## 来源','']
  for r in a['foundation_binding']['refs']:lines.append('- C220 '+r['volume_id']+' §'+r['title_en']+'；来源块：'+', '.join(x['block_id'] for x in r['source_locators']))
  lines+=['','## 分析与证据','']+['- '+x for x in a['analysis']+a['semantic_checks']]
  lines+=['','字段：'+', '.join(a['fields'])+'。未提供字段保持未知。','']
  (S/'references/artifacts'/f'{aid}.md').write_text('\n'.join(lines))
 # Refresh the existing entry definitions instead of leaving stale 'C220 missing' claims.
 for kind,records in [('artifacts',arts['artifacts']),('deliverables',dels['deliverables'])]:
  for item in records:
   path=S/'references'/kind/(item['id']+'.md')
   if not path.exists():path.write_text('# '+item['name_zh']+'\n\n'+item['name_en']+'。内容与字段按下列基础标准用途组织。\n')
   text=path.read_text().split('<!-- foundation-binding:start -->')[0].rstrip()
   text=text.replace('名称来自 G248 附录 B；下列组装结构是项目约定，不替代 C220 正式定义。','名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。')
   text=text.replace('名称依据 G248 附录 B，生成结构为项目综合，正式定义缺口保留。','基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。')
   lines=['','<!-- foundation-binding:start -->','## 当前基础标准依据','',
          '匹配性质：`'+item['foundation_binding']['match_kind']+'`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。','']
   for rr in item['foundation_binding']['refs']:
    lines.append('- [C220 '+rr['title_en']+'](../../corpus/fundamental/analysis/'+rr['volume_id']+'.md#'+rr['anchor']+')')
    sec=next(s for s in docs[rr['volume_id']]['sections'] if s['heading_id']==rr['anchor'])
    for label,key in [('概念','concepts_zh'),('逻辑','logic_zh'),('决策','decisions_zh'),('边界','limits_zh')]:
     lines+=['  - '+label+'：'+t for t in sec.get(key,[])]
   if item['id']=='implementation-governance-model':lines+=['','F阶段输出保留“if any”；可采用适用的既有治理框架。项目治理组织、过程、责任及检查点需要有依据；生成文本不授予权力。']
   path.write_text(text+'\n'+'\n'.join(lines)+'\n')
 rules=load(S/'capability-addenda/deliverable-assembly-rules.json')
 if not any(x['id']==governance['id'] for x in rules['deliverables']):
  rules['deliverables'].append({'id':governance['id'],'sections':[{'title':s['title'],'entity_types':['role','actor','decision','milestone'],'applicability':'项目采用的实施治理范围','content_focus':[s['instruction']]} for s in governance['sections']],'core_requirements':[],'conditional_groups':[],'source_origin':'C220 4.2.15 defines content; selectors are project conventions'})
 save(S/'capability-addenda/deliverable-assembly-rules.json',rules)
 # Preserve abbreviated project actions, with full official step records alongside them.
 adm['notice']='依据本地C220基础标准及系列指南的项目执行契约。source_step_records逐项定位基础标准步骤；steps/criteria为项目操作规则，须按具体任务裁剪，不自动构成官方符合性或批准。'
 arts['definition_notice']='制品用途逐项绑定本地C220；名称差异和支持概念明确标记。字段、代码及布局是项目操作规则，不声称官方图等价。'
 dels['notice']='交付物逐项绑定C220内容卷定义；业务原则/目标/驱动保留拆分的项目ID，组装结构属于项目约定。'
 sys.path.insert(0,str(S/'scripts'))
 from planning_case_examples import install as install_planning_examples
 from registry_consistency import apply_delivery_links
 install_planning_examples(caps)
 apply_delivery_links(caps)
 save(S/'artifacts.json',arts);save(S/'deliverables.json',dels);save(S/'capabilities.json',caps);save(S/'references/adm-phases.json',adm)
 for rel in ['schemas/model.schema.json','schemas/model-v1.schema.json']:
  schema=load(S/rel);enum=schema['properties']['deliverables']['items']['properties']['deliverable_id']['enum']
  if 'implementation-governance-model' not in enum:enum.append('implementation-governance-model')
  save(S/rel,schema)
 report={'schema_version':'foundation-execution-bindings/1','bindings':bindings,'counts':{'artifacts':len(arts['artifacts']),'deliverables':len(dels['deliverables']),'phase_contracts':len(phase_chapters),'source_step_records':sum(len(p['source_step_records']) for p in adm['phases']+[adm['requirements_management']]),'new_artifacts':len(added),'new_deliverables':1},'interpretation_zh':'绑定证明用途和来源对应；来源只定义概念的字段不能冒充官方字段，非同名关系单列。'}
 save(S/'references/foundation-execution-bindings.json',report)
 save(C/'quality/foundation-contract-coverage.json',{'passed':True,'counts':report['counts'],'source_files':{str((S/r).relative_to(C)):sha(S/r) for r in ['artifacts.json','deliverables.json','references/adm-phases.json']},'limits_zh':['来源记录全量绑定，不等于真实项目执行或独立语义认证。']});print(report['counts'])
if __name__=='__main__':main()
