# -*- coding: utf-8 -*-
"""Connect reviewed sources to reusable project execution contracts without inventing authority."""
from pathlib import Path
import json,hashlib
C=Path(__file__).resolve().parents[1];S=C/'skills/_shared'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 g=read(C/'architecture/source-method-graph.json');nodes={n['id']:n for n in g['nodes']};edges=g['edges']
 def node(i,kind,**attrs):
  if i not in nodes:nodes[i]={'id':i,'kind':kind,**attrs}
  return i
 def edge(a,b,r,**attrs):edges.append({'source':a,'target':b,'relation':r,**attrs})
 # Close guide/document reference endpoints using actual published IDs.
 for p in sorted((C/'chapters').glob('G*.json')):
  d=read(p);docid=d['document_id'];node(docid,'document',path=p.relative_to(C).as_posix(),sha256=sha(p))
  for s in d['sections']:
   sid=s['source_section_id'];node(sid,'source-section',document_id=docid,title=s.get('title_zh',s.get('title_en')),source_unit_ids=[u['id'] for u in s['source_units']]);edge(docid,sid,'contains-published-section',origin='publication-structure')
 for p in sorted((C/'architecture/roles').glob('G249-*.json')):
  d=read(p);rid=d['id'];node(rid,'role-responsibility',label_zh=d['label_zh'],scope_zh=d.get('scope_zh'),responsibilities=d.get('responsibilities',[]),path=p.relative_to(C).as_posix(),sha256=sha(p))
 registry=read(S/'capabilities.json');methods={r['id']:r for r in registry['analysis_methods']};artifacts={r['id']:r for r in registry['work_products']};artifacts.update({r['id']:r for r in read(S/'artifacts.json')['artifacts']})
 # Foundation-to-runtime bindings are distinct from guide-derived task routes.
 foundation=read(S/'references/foundation-execution-bindings.json')
 for binding in foundation['bindings']:
  prefix={'artifact':'artifact:','deliverable':'deliverable:','phase':'project:adm-source-contract:'}[binding['kind']]
  target=node(prefix+binding['id'],{'artifact':'artifact-type','deliverable':'deliverable-type','phase':'adm-phase-contract'}[binding['kind']],origin='project-operation',binding_path='skills/_shared/references/foundation-execution-bindings.json')
  for source in binding['refs']:
   assert source['section_id'] in nodes,source['section_id']
   edge(source['section_id'],target,'source-to-execution-binding',origin='project-operationalization',match_kind=binding['match_kind'],field_origin=binding['field_origin'],evidence_block_ids=[x['block_id'] for x in source['source_locators']])
 adm=read(S/'references/adm-phases.json')
 for definition in adm['phases']+[adm['requirements_management']]:
  phase=definition.get('id','Requirements');parent='project:adm-source-contract:'+phase
  for step in definition['source_step_records']:
   sid=node('project:source-step:'+step['id'],'source-bound-adm-step',origin='source-structure-with-project-explanation',phase=phase,title_en=step['name_en'],source_section_id=step['source_ref']['section_id'],responsibility_column=step.get('responsibility_column'))
   edge(parent,sid,'contains-source-step',origin='source-structure')
   edge(step['source_ref']['section_id'],sid,'source-step-localization',origin='source-structure',evidence_block_ids=[x['block_id'] for x in step['source_ref']['source_locators']])
 mapping=read(S/'references/g249/skill-task-map.json');source=read(C/'architecture/roles/skills.json')['G249'];matrix={s['id']:s for s in source['skills']};cols=[r['id'] for r in source['role_columns']]
 assert len(mapping['skills'])==len(matrix)==71
 basis=node('G249:work-basis:section3','work-basis',text_zh='先明确架构实践授权和待完成的工作，再匹配角色、技能及经验；发展评价有独立证据。',origin='source-grounded-interpretation',document_id='G249',source_pdf_pages=[14,15])
 assignment=node('project:assignment-contract:v1','assignment-contract',origin='project-operation',fields=['mandate','task_refs','role_ref','person_ref','authority','valid_from','valid_until','available_hours','assessment_refs'],missing_state='needs-input',approval='not-inferred')
 counts={'skills':0,'reference_cells':0,'task_chains':0};requirements=[]
 for row in mapping['skills']:
  sid=row['skill_id'];assert sid in matrix
  assert all(row['official']['reference_proficiencies'][r]==v for r,v in zip(cols,matrix[sid]['values']))
  node(sid,'human-skill',title_en=row['source_name_en'],definition_status=row['definition_status'],sources_needed=row['sources_needed'],source_evidence=row['official']['evidence'])
  task=node(sid+':project-task','task-prototype',origin='project-derived',text_zh=row['task_example_zh'],requires_tailoring=True)
  decision=node(sid+':decision-contract','decision-contract',origin='project-operation',required_fields=['question','alternatives','constraints','source_evidence','unknowns','decision_owner','rationale'],notice_zh='任务确定后填写具体待决问题；本记录不预先选择方案。')
  acceptance=node(sid+':acceptance-evidence','acceptance-evidence-requirement',origin='project-derived',text_zh=row['observable_evidence_zh'],approval='not-inferred')
  edge(basis,task,'grounds-task',origin='project-derived');edge(task,decision,'requires-decision',origin='project-operation');edge(task,assignment,'requires-scoped-assignment',origin='project-operation');edge(task,sid,'requires-skill-tailoring',origin='project-derived');edge(task,acceptance,'requires-review-evidence',origin='project-derived')
  for role,value in row['official']['reference_proficiencies'].items():
   node(role,'reference-role-column',document_id='G249');edge(role,sid,'reference-proficiency',value=value,scale_id='G249-table5-1',origin='source-transcription',evidence=row['official']['evidence']);counts['reference_cells']+=1
  for mid in row['method_ids']:
   assert mid in methods,mid
   node('method:'+mid,'analysis-method',title=methods[mid].get('name',methods[mid].get('title')),registry_path='skills/_shared/capabilities.json')
   edge(sid,'method:'+mid,'project-method-route',origin='project-derived');edge(decision,'method:'+mid,'analyzed-by',origin='project-derived')
   for aid in row['artifact_ids']:
    assert aid in artifacts,aid
    node('artifact:'+aid,'artifact-type',registry_path='skills/_shared/capabilities.json')
    edge('method:'+mid,'artifact:'+aid,'candidate-output',origin='project-derived',requires_task_selection=True);edge('artifact:'+aid,acceptance,'review-against',origin='project-derived')
  counts['skills']+=1;counts['task_chains']+=1
  if row['definition_status']=='source-name-unresolved':requirements.append({'skill_id':sid,'reason':'G249 only names skill; specialized meaning must be sourced before task adoption','sources_needed':row['sources_needed']})
 for rid in ['G249:role:chief-architect','G249:role:enterprise-architect','G249:role:segment-architect','G249:role:solution-architect']:
  assert rid in nodes,rid
  edge(assignment,rid,'role-responsibility-must-be-selected',origin='project-operation',notice_zh='候选角色类别，实际分配必须明确范围与期间；不自动分派。')
 # Preserve contextual differences: different frameworks remain separately versioned.
 node('G198','document',path='chapters/G198.json');edge('G198','G249','contextual-comparison',origin='project-interpretation',notice_zh='不同角色列与量表须分别记录；不据标题自行宣称全面取代。')
 for code in ['G226','W242C']:
  d=read(C/'supplementary'/f'{code}.json');node(code,'document',publication_role=d['publication_role'],source_version=d.get('source_version',d.get('version','unspecified-in-local-metadata')),path=f'supplementary/{code}.json')
  for section in d['sections']:
   sid=section.get('section_id',section.get('id'));edge(code,sid,'contains-published-section',origin='publication-structure')
   for ref in section.get('guide_refs',[]):
    target=ref.get('source_section_id',ref.get('section_id',ref.get('document_id'))) if isinstance(ref,dict) else ref
    if target in nodes:edge(sid,target,'contextual-refinement-candidate',origin='project-interpretation')
   for ref in section.get('fundamental_refs',[]):
    target='C220-web-2025:'+ref['volume_id']+'#'+ref['heading_id']
    assert target in nodes,target
    edge(sid,target,'contextual-foundation-reference',origin='project-interpretation',reason_zh=ref['relation'])
 if 'W242C:training' in nodes:
  edge('W242C:training','G249:skill:generic:training','contextual-difference',origin='project-interpretation',reason_zh='白皮书的训练为AI系统训练；G249 Training为人的技能名称，两者不合并。')
 unknown=sorted({x[k] for x in edges for k in ['source','target'] if x[k] not in nodes});assert not unknown,unknown
 unique={json.dumps(x,ensure_ascii=False,sort_keys=True):x for x in edges};g['nodes']=list(nodes.values());g['edges']=list(unique.values());g['schema_version']='source-method-graph/2';g['relation_contract']={'allowed_semantic_types':['definition','refinement','citation','example','replacement','conflict','project-operationalization'],'rule_zh':'只有源依据支持时才声明定义/引用/取代/冲突；一般关联保留解释性语境，不伪称官方关系。','unresolved_specialist_definitions':requirements,'assignment_semantics_zh':'工作任务、组织角色与实际人员配置分离；一人多角色与多人同角色通过不同配置记录表达。'}
 (C/'architecture/source-method-graph.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
 report={'schema_version':'execution-bridge-check/1','passed':True,'counts':{**counts,'foundation_bindings':len(foundation['bindings']),'foundation_source_steps':sum(len(p['source_step_records']) for p in adm['phases']+[adm['requirements_management']]),'nodes':len(nodes),'edges':len(g['edges']),'dangling_endpoints':0},'inputs':{p.relative_to(C).as_posix():sha(p) for p in [S/'references/g249/skill-task-map.json',S/'capabilities.json',S/'references/foundation-execution-bindings.json',S/'references/adm-phases.json',C/'architecture/roles/skills.json']},'unresolved_specialist_definitions':requirements,'limits_zh':['验证71个任务原型及方法/制品注册引用，不证明具体组织完成了这些工作。','原始矩阵426值保留；Chief/通用Segment没有伪造数值列。','关联是项目路由；真实任务、决策与分配仍须从业务材料实例化。']}
 (C/'quality/execution-bridge.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['counts'])
if __name__=='__main__':main()
