#!/usr/bin/env python3
"""Build source-specific role, responsibility and competency analyses.

G249/G198 role vocabularies remain separate. Leadership/architecture scope is not
an HR reporting assertion. Numeric expectations are reference values, not hiring
thresholds, and no unprovided qualification is invented.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
CATEGORIES={'Application','Architecture','Business','Change','Data','Generic','Legal','Technology'}
ZH_CAT={'Application':'应用','Architecture':'架构','Business':'业务','Change':'变更','Data':'数据','Generic':'通用','Legal':'法律','Technology':'技术',
'Generic Skills':'通用技能','Business Skills & Methods':'业务技能与方法','Enterprise Architecture Skills':'企业架构技能',
'Program or Project Management Skills':'项目群/项目管理','IT General Knowledge Skills':'IT通用知识','Technical IT Skills':'IT技术','Legal Environment Skills':'法律环境'}


def norm(s):return re.sub(r'\s+',' ',str(s)).strip()
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def mdcell(v):return str(v).replace('|','\\|').replace('\n',' ')
def evidence(corpus,code,page,quote):
 d=json.loads((corpus/'documents'/f'{code}.json').read_text());text=norm(d['pages'][page-1]['raw_text'])
 if norm(quote) not in text:raise ValueError(f'Unsupported quote: {code} p{page} {quote}')
 return {'document_id':code,'pdf_page':page,'quote_en':quote,'source_path':d['source']['path'],'source_sha256':d['source']['sha256'],
         'markdown_path':f'documents/{code}.md#page-{page}'}
def assertion(corpus,code,page,quote,zh,kind='source-grounded-analysis'):
 return {'text_zh':zh,'evidence':evidence(corpus,code,page,quote),'assertion_type':kind}

CORE={
'chief-architect':{'label_en':'Chief Architect','label_zh':'首席架构师','section':'4.1. Chief Architect','scope':'企业整体与高层战略/运营上下文',
 'definition':(17,'responsible for communicating and gaining commitment','为企业重大业务与技术变革取得共识和承诺，将架构融入战略及运营上下文。'),
 'authority':[(18,'accountability for, and oversight of, the Architecture Landscape','对架构全景、其对业务服务交付的影响及治理承担最终责任。'),(18,'providing decisions about the overall landscape','领导并作出整体架构全景相关决定。')],
 'requirements':[(17,'very experienced and accomplished professional','具备丰富经验与已取得成就的专业能力。'),(17,'creating a consensus among executives and board members','能够在高管与董事会之间形成架构共识。'),(17,'dynamic, evolving, and/or novel','能够处理动态演进、新颖且复杂的情境。'),(18,'leadership, mentoring, and coaching','具备领导、辅导和教练能力，发展架构团队。')],
 'io':[(18,'Translating business and technology strategies, goals, and objectives','输入业务/技术战略、目标与当前能力；输出运营模型变化、能力变化及架构路线图。'),(18,'Identifying, documenting, and communicating the major constraints, principles, and policies','输出总体约束、原则与政策，为后续架构工作提供边界。')],
 'activities_zh':['支持并参与业务战略制定','将业务和技术战略/目标转为运营模型变更','评价当前能力并识别战略所需能力变化','与企业领导持续沟通架构路线图','塑造架构全景及未来状态模型','负责规模最大、最复杂和风险最高的架构全景变化','识别、记录和沟通主要约束/原则/政策','领导、辅导企业/分段/解决方案架构师','向企业传达变革驱动因素并监督架构治理'],
 'analysis':'首席角色着重高层共识、架构总体责任及跨域领导。它是 Enterprise Architect 的特殊情形，但表5-2没有Chief列，不能自动复制EA列或指定全4级。'},
'enterprise-architect':{'label_en':'Enterprise Architect','label_zh':'企业架构师','section':'4.2. Enterprise Architect','scope':'跨业务/技术分段的企业全景',
 'definition':(19,'creating, leading, and delivering significant technical and business change','发起、领导并交付跨企业的重大业务与技术变革，为跨分段架构提供一致性和治理。'),
 'authority':[(19,'accountability for overall business service delivery','通过信息系统对整体业务服务交付承担责任。'),(19,'define principles and policies','定义塑造架构全景的原则/政策，并监督架构变更治理。')],
 'requirements':[(19,'mastery in several key technical and/or business areas','在若干关键技术或业务领域具备熟练掌握能力。'),(19,'track record of significant delivery','具有重大交付经历以及与关键利益相关者合作的记录。'),(19,'not limited to any particular solution aspect or segment','工作范围不限于单一解决方案侧面或分段。'),(19,'coach and mentor others','能指导和辅导他人。')],
 'io':[(20,'Translating business and technology strategies and objectives','输入企业战略、目标、当前能力及变革驱动；输出运营模型变更、未来架构模型/视图及架构工作方式。'),(20,'constraints, principles, and policies necessary','输出约束、原则和政策，支持架构全景演进及治理。')],
 'activities_zh':['把业务/技术战略和目标转为运营模型变更','评价当前能力及所需能力变化','描述人员、组织、服务、流程、数据、信息、技术与环境的相互关系','创建和演进企业未来状态的架构模型与视图','定义、沟通并实施支持迭代与敏捷的架构工作实践','识别并沟通架构约束、原则和政策','领导、辅导分段与解决方案架构师','传达变革驱动因素并参与架构治理'],
 'analysis':'EA关注跨分段的一致性、互操作性、架构原则与治理；技能矩阵强调广度和架构判断，同时保留领域专家协作。'},
'segment-architect':{'label_en':'Segment Architect (Business and Technical)','label_zh':'分段架构师（业务与技术）','section':'4.3. Segment Architect (Business and Technical)','scope':'一个或多个业务/技术分段',
 'definition':(21,'responsible for the capabilities provided by one or more business or technical segments','负责一个或多个分段的能力、系统、子系统和构件，规划其演进并与其他分段协作。'),
 'authority':[(22,'They oversee all development','监督分段内系统/子系统/构件开发，确保适用、合法并遵循政策和标准。'),(22,'policies and standards','确定使分段构件有效、高效且合法的政策与标准。')],
 'requirements':[(21,'experienced and accomplished professionals','具有丰富经验并已取得专业成就。'),(22,'collaborate effectively and easily with other architects','能够与其他架构师有效协作，维持整体环境互联。'),(22,'technical/business specialists and Solution Architects are clear about their roles','能够明确专家及解决方案架构师角色，组织有效协作。')],
 'io':[(22,'relevant business and/or technical segment','输入企业战略/目标、分段能力现状及约束；输出分段能力变化、架构模型、政策标准与路线图。')],
 'activities_zh':['将战略目标落实到相关业务/技术分段','评价分段当前能力并识别所需变化','描述分段中人员/组织/服务/流程/数据/技术等关系','创建、迭代和维护分段未来架构模型与视图','实施适合分段的迭代敏捷架构实践','识别并沟通分段约束、政策和标准','领导、辅导相关专家和解决方案架构师'],
 'analysis':'分段是管理与控制所需的一致能力分组；业务、数据、应用、技术域是有用的分段视角。一般Segment角色没有单独数值列，不把四域列简单取均值。'},
'solution-architect':{'label_en':'Solution Architect','label_zh':'解决方案架构师','section':'4.4. Solution Architect','scope':'具体新建/变更解决方案及其过渡架构',
 'definition':(23,'responsible for the delivery of new and/or changed capabilities','围绕明确需求设计、治理并交付新增或变更能力，形成可实施的过渡架构。'),
 'authority':[(24,'development, and implementation of new and changing solutions','监督解决方案的规格、开发与实施，落实适用性、效率、合法性及相关标准。'),(24,'risk-based governance','提供风险驱动的实施治理，管理变更请求及必要的规格偏离。')],
 'requirements':[(23,'experienced and accomplished professionals','具备丰富经验与专业成就。'),(24,'fully engaging with all business/technology and other stakeholders','充分参与业务/技术及其他利益相关者沟通，理解关注点、需求和期望。'),(24,'security, privacy, and testing','能全面考虑安全、隐私及测试要求。')],
 'io':[(23,'specific requirements','输入具体需求、上位目标、战略政策及服务水平期望；输出系统/子系统/构件及互操作设计、方案路线图和过渡架构。'),(24,'planned operation, maintenance, and evolution','设计覆盖生产环境的运营、维护和演进安排。')],
 'activities_zh':['明确服务/流程/组织/运营模型及技术变化，并考虑生产运营维护演进','保证现有和计划构件兼容相关架构、战略、政策和标准','全面纳入安全、隐私与测试要求','说明不同部署拓扑和构件选项的收益与问题','创建并推动实施目标路线图及组成的过渡架构','以风险治理支持实施并管理变更与偏离','促进利益相关者沟通协作并达到目标服务水平'],
 'analysis':'解决方案角色把上位架构约束与具体需求转为可实现变更，负责协作、取舍与落地治理，不能缩减为代码或产品设计。'}
}

G249_MATRIX=[('enterprise-architect','Enterprise Architect','企业架构师'),('business-domain-architect','Business Domain Architect','业务域架构师'),('data-domain-architect','Data Domain Architect','数据域架构师'),('application-domain-architect','Application Domain Architect','应用域架构师'),('technology-domain-architect','Technology Domain Architect','技术域架构师'),('solution-architect','Solution Architect','解决方案架构师')]
G198_MATRIX=[('architecture-board-member','Architecture Board Member','架构委员会成员'),('architecture-sponsor','Architecture Sponsor','架构赞助人'),('enterprise-architecture-manager','Enterprise Architecture Manager','企业架构经理'),('technology-architect','Technology Architect','技术架构师'),('data-architect','Data Architect','数据架构师'),('application-architect','Application Architect','应用架构师'),('business-architect','Business Architect','业务架构师'),('program-project-manager','Program/Project Manager','项目群/项目经理'),('it-designer','IT Designer','IT设计师'),('solution-architect','Solution Architect','解决方案架构师')]


def section_material(doc,heading,next_heading):
 rows=[];active=False;state='definition'
 for p in doc['pages']:
  for item in p['content']:
   text=item['text']
   if text==heading:active=True;continue
   if active and text==next_heading:return rows
   if not active:continue
   if text.startswith('Activities may include'):state='activities';continue
   if text.startswith('Key Stakeholders may include'):state='stakeholders';continue
   if text.startswith('Potential') and 'KPIs' in text or text.startswith('Potential Key Performance Indicators'):state='potential_kpis';continue
   rows.append({'pdf_page':p['pdf_page'],'text_en':text.lstrip('• '),'kind':state,'source_block_ids':item.get('source_block_ids',[])})
 return rows


def grid_tables(pdf):
 result=[]
 for pn in [27,28,29]:
  p=pdf[pn-1]
  paths=[d for d in p.get_drawings() if d['type']=='s' and len(d['items'])<=4 and all(i[0]=='re' or i[0]=='l' and (abs(i[1].x-i[2].x)<.1 or abs(i[1].y-i[2].y)<.1) for i in d['items'])]
  for t in p.find_tables(paths=paths,clip=fitz.Rect(30,30,p.rect.width-30,p.rect.height-30),snap_tolerance=1,join_tolerance=1).tables:
   result.append({'pdf_page':pn,'rows':t.extract(),'bbox':list(t.bbox),'cell_bboxes':[[list(c) if c else None for c in row.cells] for row in t.rows]})
 return result


def extract_g249(root,corpus):
 d=json.loads((corpus/'documents/G249.json').read_text());pdf=fitz.open(root/d['source']['path']);tables=grid_tables(pdf)
 scale=[];skills=[];summary=[];checks=[]
 for ti,t in enumerate(tables):
  if len(t['rows'][0])==3:
   for ri,row in enumerate(t['rows'][1:],1):scale.append({'level':int(row[0]),'name_en':row[1],'description_en':norm(row[2]),'pdf_page':t['pdf_page'],'row':ri})
   continue
  for ri,row in enumerate(t['rows']):
   if row[0] not in CATEGORIES:
    if row[0]=='Skill Category':
     observed=[re.sub(r'\s+','',v) for v in row[2:]]
     if observed!=[re.sub(r'\s+','',r[1]) for r in G249_MATRIX]:raise ValueError('G249 role header mismatch')
    if row[0]!='Skill Category':summary.append({'label':norm(row[0]),'values':row[2:],'pdf_page':t['pdf_page'],'row':ri})
    continue
   entry={'id':'G249:skill:'+slug(row[0])+':'+slug(norm(row[1])),'category_en':row[0],'category_zh':ZH_CAT[row[0]],'label_en':norm(row[1]),'values':[int(v) for v in row[2:]],
          'evidence':{'document_id':'G249','pdf_page':t['pdf_page'],'table_label':'Table 5-2','row_index_zero_based':ri,'cell_bboxes':t['cell_bboxes'][ri],
                      'source_sha256':d['source']['sha256'],'source_path':d['source']['path'],'row_values_original':row}}
   for ci,value in enumerate(entry['values'],2):
    rect=fitz.Rect(t['cell_bboxes'][ri][ci]);observed=norm(pdf[t['pdf_page']-1].get_text('text',clip=rect))
    if observed!=str(value):raise ValueError(f'G249 numeric mismatch {t["pdf_page"]} {ri} {ci}: {observed}/{value}')
    checks.append([t['pdf_page'],ri,ci,value])
   skills.append(entry)
 pdf.close()
 if len(skills)!=71:raise ValueError(f'Expected source-visible 71 skills, got {len(skills)}')
 return scale,skills,summary,{'method':'independent extraction directly from source PDF; every role-level cell re-read by physical cell rectangle; rendered pages visually inspected',
                            'numeric_cells_checked':len(checks),'issues':[],'row_count':len(skills),'page_bottom_rows':['Integration and Sharing','Oral Communication']}


def extract_g198(corpus,root=ROOT):
 scale_record=json.loads((corpus/'figures/G198/image-p0015-01.json').read_text());scale=scale_record['tables'][0]['rows'];skills=[];checked=0
 for path in sorted((corpus/'figures/G198').glob('image-*.json')):
  rec=json.loads(path.read_text());pn=rec['pdf_page']
  for table in rec.get('tables',[]):
   if not table['id'].startswith('skills-matrix'):continue
   if table['columns'][1:]!=[r[1] for r in G198_MATRIX]:raise ValueError('G198 column mismatch')
   review=rec['current_visual_review'];check=review['numeric_cell_check']
   source=root/rec['provenance']['pdf_path']
   if sha(source)!=rec['provenance']['pdf_sha256']:raise ValueError('G198 source PDF fingerprint changed')
   with fitz.open(source) as pdf:
    source_png=pdf[pn-1].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(rec['bbox_pdf_points']),alpha=False).tobytes('png')
   if hashlib.sha256(source_png).hexdigest()!=sha(corpus/rec['image_path']):raise ValueError('G198 image differs from direct original PDF render')
   if check['mismatches']:raise ValueError('G198 source color mismatch')
   # Recompute directly from source crop, not merely trust the inherited result.
   image=Image.open(corpus/rec['image_path']).convert('RGB');w,h=image.size
   palette={(255,243,131):1,(176,203,31):2,(118,144,201):3,(234,85,111):4}
   ys=[y for y in range(h) if image.getpixel((int(w*.195),y)) in palette];a,b=min(ys),max(ys)+1
   for ri,row in enumerate(table['rows']):
    for ci,expected in enumerate(row[1:]):
     cy=a+(b-a)*(ri+.5)/len(table['rows']);cx=w*(.181+(ci+.5)*.819/10)
     pix=image.crop((int(cx-12),int(cy-5),int(cx+12),int(cy+5)));votes=Counter(palette[p] for p in pix.getdata() if p in palette)
     actual=votes.most_common(1)[0][0] if votes else None
     if actual!=expected:raise ValueError(f'G198 cell mismatch {rec["id"]} {ri} {ci}')
     checked+=1
    skills.append({'id':'G198:skill:'+slug(table['title_en'])+':'+slug(row[0]),'label_en':row[0],'category_en':table['title_en'],
                   'category_zh':ZH_CAT.get(table['title_en'],table['title_en']),'values':row[1:],
                   'evidence':{'document_id':'G198','pdf_page':pn,'image_record_id':rec['id'],'table_id':table['id'],
                               'row_index_zero_based':ri,'row_values_original':row,'source_sha256':rec['provenance']['pdf_sha256'],
                               'source_path':rec['provenance']['pdf_path'],'numeric_verification':'source-cell-background-color-rechecked'}})
 return [{'level':r[0],'name_en':r[1],'description_en':r[2],'color':r[3],'pdf_page':15} for r in scale],skills,{'numeric_cells_checked':checked,'issues':[],'method':'recomputed 790 source raster matrix cell colors against printed proficiency-level palette'}


def source_profile(code,key,en,zh,scope):
 return {'schema_version':'architecture-role/1','id':code+':role:'+key,'source_guide':code,'label_en':en,'label_zh':zh,'scope_zh':scope,
         'content_role':'source-grounded-role-analysis','role_definition':[],'responsibilities':[],'decision_authority':[],'requirements':[],'inputs_outputs':[],
         'collaboration':[],'potential_kpis':[],'source_material':[],'skills':[],'relationships':[],
         'hierarchy_notice_zh':'架构领导/治理、专业范围或协作关系不自动表示人事直属汇报；岗位、角色、任务分别建模。',
         'qualification_notice_zh':'学历、工作年限、认证、法定签字权等未在相应证据给出时保持未规定，不能从技能等级推造。',
         'matrix_status':'not-specified-for-this-role','assessment_status':'reference-expectation-not-an-assessment-of-any-person'}


def attach_skills(profile,code,ci,skills,scale):
 profile['skills']=[{'skill_id':s['id'],'label_en':s['label_en'],'category_en':s['category_en'],'category_zh':s['category_zh'],
                     'reference_level':s['values'][ci],'level_name_en':next(x['name_en'] for x in scale if x['level']==s['values'][ci]),
                     'requirement_kind':'reference-desirable-proficiency-not-universal-mandate',
                     'evidence':{**s['evidence'],'role_column_index_zero_based':ci+(2 if code=='G249' else 1),'role_header':profile['label_en']}}
                    for s in skills]
 profile['matrix_status']='complete-source-column';profile['proficiency_scale']=scale
 counts=Counter(s['reference_level'] for s in profile['skills'])
 profile['competency_analysis']={'method':'distribution and category comparison of the complete source column; ordinal levels are not a person score',
  'skill_count':len(profile['skills']),'levels':{str(i):counts[i] for i in range(1,5)},
  'expert_level_reference':[s['label_en'] for s in profile['skills'] if s['reference_level']==4],
  'category_profiles':[{'category':cat,'skills':len(ss),'levels':dict(sorted(Counter(str(s['reference_level']) for s in ss).items())),
                        'level_4_skills':[s['label_en'] for s in ss if s['reference_level']==4]}
                       for cat in dict.fromkeys(s['category_en'] for s in profile['skills'])
                       for ss in [[s for s in profile['skills'] if s['category_en']==cat]]],
  'application_zh':'以每项技能的参考等级与个人可核实经验逐项比较；不足项形成培训/专家支持/协作计划。不要把表中等级求和作为招聘或晋升合格线。'}
 if code=='G198':
  profile['competency_analysis']['optional_background']=[s['label_en'] for s in profile['skills'] if s['reference_level']==1]
  profile['competency_analysis']['awareness_reference']=[s['label_en'] for s in profile['skills'] if s['reference_level']==2]
  profile['requirements'] += [{'text_zh':f'参考技能要求：{s["label_en"]}（{s["category_zh"]}），原表期望等级{s["reference_level"]} / {s["level_name_en"]}；按G198量表解释，须结合实际角色裁剪。',
                               'assertion_type':'source-matrix-reference-expectation','skill_id':s['skill_id'],'reference_level':s['reference_level'],
                               'evidence':s['evidence']} for s in profile['skills'] if s['reference_level']>=3]
 else:
  profile['competency_analysis']['specialist_support_expected']=[s['label_en'] for s in profile['skills'] if s['reference_level']<=2]


def curated_profiles(corpus):
 d=json.loads((corpus/'documents/G249.json').read_text());profiles=[]
 keys=list(CORE)
 for k in keys:
  spec=CORE[k];r=source_profile('G249',k,spec['label_en'],spec['label_zh'],spec['scope'])
  page,quote,zh=spec['definition'];r['role_definition']=[assertion(corpus,'G249',page,quote,zh)]
  for field,specfield in [('decision_authority','authority'),('requirements','requirements'),('inputs_outputs','io')]:
   r[field]=[assertion(corpus,'G249',p,q,z) for p,q,z in spec[specfield]]
  end=CORE[keys[keys.index(k)+1]]['section'] if k!=keys[-1] else '5. Skills and Proficiency Levels'
  material=section_material(d,spec['section'],end);r['source_material']=material
  acts=[m for m in material if m['kind']=='activities' and not m['text_en'].startswith('In most cases')]
  if len(acts)!=len(spec['activities_zh']):raise ValueError(f'{k} activity count {len(acts)}')
  r['responsibilities']=[{'text_zh':zh,'text_en':m['text_en'],'evidence':evidence(corpus,'G249',m['pdf_page'],m['text_en'])} for m,zh in zip(acts,spec['activities_zh'])]
  for field,kind in [('collaboration','stakeholders'),('potential_kpis','potential_kpis')]:
   r[field]=[{'text_en':m['text_en'],'evidence':evidence(corpus,'G249',m['pdf_page'],m['text_en']),
              'status':'illustrative-potential-kpi-not-project-target' if kind=='potential_kpis' else 'source-stakeholder-list-not-reporting-line'} for m in material if m['kind']==kind]
  r['analysis_zh']=spec['analysis'];profiles.append(r)
 for key,en,zh in G249_MATRIX:
  if any(p['id']=='G249:role:'+key for p in profiles):continue
  r=source_profile('G249',key,en,zh,zh.replace('架构师','')+'的专业视角；属于分段角色适用语境')
  r['role_definition']=[assertion(corpus,'G249',21,'business, application, data, and technology domains','业务、应用、数据、技术是管理信息系统架构全景的四种域视角；角色数值要求由表5-2对应列给出。')]
  r['shared_responsibility_context']={'role_id':'G249:role:segment-architect','relationship':'domain-specific-context-of-segment-role','status':'contextual-reading-not-a-formal-HR-subtype',
                                    'evidence':evidence(corpus,'G249',21,'four particular segments are called')}
  r['responsibilities']=[assertion(corpus,'G249',22,'relevant business and/or technical segment','在所属域内适用分段架构的能力评价、关系建模、路线图、标准约束与协作治理活动；具体分工需按企业裁剪。')]
  r['requirements']=[assertion(corpus,'G249',22,'collaborate effectively and easily with other architects','专业判断同时需要跨域协作，不能只依据单一域技术方案工作。')]
  r['inputs_outputs']=[assertion(corpus,'G249',22,'Creating, iterating, and maintaining architectural models and views','将分段业务/技术目标转为域内模型、视图、约束与演进安排。')]
  r['decision_authority']=[assertion(corpus,'G249',22,'policies and standards','域相关架构政策和标准提供设计治理上下文；不在此推造岗位授权。')]
  r['analysis_zh']='按表5-2逐项读取该域角色的技能侧重；与其他域角色的区别见完整列比较，不以角色名推断全部知识深度。';profiles.append(r)
 # G198 contains 10 numeric columns; EA/Segment prose roles have no separate column.
 for key,en,zh in G198_MATRIX:
  r=source_profile('G198',key,en,zh,'G198架构团队角色与技能框架')
  r['role_definition']=[assertion(corpus,'G198',13,'competency levels for specific roles','该角色属于架构团队技能框架，表5-1至5-7逐技能给出期望熟练程度。')]
  r['proficiency_reference_notice']=assertion(corpus,'G198',14,'desirable level of proficiency in each skill','每项技能等级为框架的期望熟练程度；用于发现能力匹配与缺口，非当前人员已满足要求的证据。')
  r['analysis_zh']='本角色用完整79项技能列分析能力重点。G198没有为每个矩阵列分别写完整职位说明，明确职责只能由下列直接证据或注明来源的补充语境支持。'
  if key=='solution-architect':
   r['responsibilities']=[assertion(corpus,'G198',14,q,z) for q,z in [
    ('Conceptualize technical solutions','概念化复杂问题的技术方案，使IT投资收益最大化。'),('Verify stability, interoperability','核对稳定性、互操作性、可移植性、安全或扩展性。'),('Collaborate with stakeholders','与利益相关者协作取得组织承诺。'),('Communicate project information','通过演示、技术报告或白皮书传达项目信息。'),('Evaluate the existing operating environment','评价当前运营环境并识别冗余/无效系统和改进需要。'),('Evaluate and guide selection of technologies','评价并指导所需技术选择。')]]
   r['role_definition']+=[assertion(corpus,'G198',23,'at a system or subsystem level','负责系统或子系统级架构设计和文档，侧重应用、数据和技术，同时理解业务环境。')]
  elif key=='it-designer':
   r['responsibilities']=[assertion(corpus,'G198',14,'translate the architecture into deliverable components','将架构转为可交付构件，技能以技术为中心，与架构师互补。')]
   r['analysis_zh']+=' 设计师与架构师技能有交集，但把构件交付设计与企业架构完整性责任区分。'
  elif key=='architecture-sponsor':
   r['responsibilities']=[assertion(corpus,'G188',33,'provides the necessary resources','G188架构项目语境的Executive提供资源、代表需解决的需要，并任命项目经理；G188将Sponsor/Executive与技能框架Architecture Sponsor联系。')]
   r['decision_authority']=[assertion(corpus,'G188',40,'ultimate decision-maker','在G188所述项目治理语境，Executive是最终决策者；这不是架构委员会与所有赞助人的通用权限定义。')]
  elif key=='architecture-board-member':
   r['responsibilities']=[assertion(corpus,'G188',41,'Architecture Governance','架构委员会参与企业层架构治理；G188明确它与项目治理机构的治理类型不同。')]
   r['decision_authority']=[assertion(corpus,'G188',42,'rules and constraints imposed by the Architecture Board','架构委员会的规则与约束可作用于项目，即便项目经理向项目群管理汇报；不要据此把委员会当成项目经理直属上级。')]
  elif key=='program-project-manager':
   r['responsibilities']=[assertion(corpus,'G188',33,'tasks them with Architecture Project execution at the operational level','在G188架构项目语境承担运营层面的项目执行任务。'),assertion(corpus,'G188',71,'stage end should be reported by the Project Manager','阶段退出条件满足时向项目监督方报告成果、目标表现、影响和下一阶段计划。')]
  elif key=='enterprise-architecture-manager':
   r['responsibilities']=[assertion(corpus,'G198',13,'Ensuring that the right person does the right job','技能框架支持人员发展和工作匹配；本书没有给Architecture Manager完整职责清单，不能从等级表推导所有管理权限。')]
  else:
   r['responsibilities']=[assertion(corpus,'G198',13,'both business and IT professionals','在各自业务/数据/应用/技术专业范围参与企业架构工作，并与其他专业共同完成架构；详细职责未按矩阵列分别展开。')]
  if key in ['technology-architect','data-architect','application-architect','business-architect']:
   r['shared_responsibility_context']={'role_id':'G198:role:enterprise-architect','relationship':'shared-architect-duties-in-specialist-domain','status':'explicit-domain-independent-architect-duty-context','evidence':evidence(corpus,'G198',20,'whatever the particular architecture domain')}
   r['responsibilities'] += [assertion(corpus,'G198',p,q,z) for p,q,z in [(21,'Understand and interpret requirements','在本专业范围理解并解释需求。'),(21,'Create a useful model','在本专业范围创建有用模型并保持视图间一致。'),(22,'Validate, refine, and expand the model','与专家验证、细化和扩展模型。'),(22,'Manage the architecture','持续维护专业架构并支持跨专业沟通。')]]
   r['inputs_outputs']=[assertion(corpus,'G198',21,'requirements and develop well-formulated models','输入本域相关需求与上下文，输出可解释的模型、视图和构建块设计，供整体架构整合；专业边界须与团队约定。')]
  elif key=='it-designer':
   r['inputs_outputs']=[assertion(corpus,'G198',14,'translate the architecture into deliverable components','输入架构指引，输出可交付构件设计；设计师侧重技术实现。')]
  elif key=='solution-architect':
   r['inputs_outputs']=[assertion(corpus,'G198',14,'Conceptualize technical solutions','输入复杂问题、环境与组织要求；输出技术方案、技术选择评价及沟通材料。')]
   r['requirements']+=[assertion(corpus,'G198',23,'needs to understand the business environment','即使更以IT为中心，仍需理解交付方案所处的业务环境；原文不要求其成为业务建模/流程设计专家。')]
  elif key=='architecture-board-member':
   r['inputs_outputs']=[assertion(corpus,'G188',41,'Architecture Governance','输入架构及变更治理事项，输出架构治理约束/意见；具体委员会授权与项目治理分工由组织设计。')]
  elif key=='architecture-sponsor':
   r['inputs_outputs']=[assertion(corpus,'G188',33,'provides the necessary resources','输入需解决的业务需要，输出资源承诺与项目经理任命；此处采用明确标注的G188Executive语境。')]
  elif key=='program-project-manager':
   r['inputs_outputs']=[assertion(corpus,'G188',71,'summary of the completed stage','输入阶段目标、退出条件及执行证据，输出完成总结、项目影响和下一阶段计划。')]
  profiles.append(r)
 for key,en,zh in [('enterprise-architect','Enterprise Architect','企业架构师'),('segment-architect','Segment Architect','分段架构师')]:
  r=source_profile('G198',key,en,zh,'企业全景/技术参考模型' if key=='enterprise-architect' else '特定业务问题或组织/域')
  if key=='enterprise-architect':
   r['role_definition']=[assertion(corpus,'G198',20,'completeness (fitness-for-purpose)','确保架构完整性、适用性与视图整合，协调利益相关者冲突并呈现权衡。')]
   r['responsibilities']=[assertion(corpus,'G198',p,q,z) for p,q,z in [
    (21,'Understand and interpret requirements','理解并解释需求，区分真实需要与愿望，形成可行动要求。'),(21,'Create a useful model','创建可沟通的多视图模型，保持整体架构完整性并发现构建块复用。'),(22,'Validate, refine, and expand the model','验证假设，纳入领域专家，细化扩展模型。'),(22,'Manage the architecture','持续维护架构模型，在开发与决策节点表达架构问题。')]]
   r['decision_authority']=[assertion(corpus,'G198',20,'choice of which particular architecture views to develop','选择适用的架构视图，受可行性与适用性约束。')]
   r['requirements']=[assertion(corpus,'G198',p,q,z) for p,q,z in [
    (24,'requirements discovery and analysis','复杂系统设计能力：需求发现、上下文、方案替代与评价、技术选择、配置。'),(24,'extensive technical breadth','具备广泛技术经验，并至少在一个领域达到专家深度。'),(25,'working knowledge of more than one design method','掌握多个设计方法并有重复成功运用记录，能按情境裁剪。'),(25,'all aspects of a project','经历设计、开发、测试、实施与生产整个项目范围。'),(25,'Communication and team building','具备沟通、团队建设与领导力。'),(25,'Strong negotiation and problem-','具备沟通复杂信息、谈判和解决问题的能力，并及时与项目管理团队决策。'),(25,'Industry skill and experience','具备行业经验，理解业务流程、行业协作与关键趋势。')]]
   r['inputs_outputs']=[assertion(corpus,'G198',20,'strategic plan for realizing it','从高管收集并阐明技术愿景，形成与业务计划一致的战略实现计划。'),assertion(corpus,'G198',21,'documentation and rationale of high-level design decisions','输出高层设计决策及理由供分段/解决方案架构师和开发团队执行。')]
  else:
   r['role_definition']=[assertion(corpus,'G198',22,'specific business problems or organizations','负责特定业务问题或组织的架构设计与文档，把详细技术方案连接到整体架构全景。')]
   r['requirements']=[assertion(corpus,'G198',23,'do not have to understand the whole enterprise','技能与EA相近，但不要求理解整个企业全部业务和IT；通常仍需理解各架构域。')]
   r['responsibilities']=[assertion(corpus,'G198',22,'re-uses the output from all other architects','复用其他架构师输出，并在给定业务域内形成企业级业务解决方案。')]
  r['analysis_zh']='文本定义角色；G198数值矩阵没有这一名称的独立列。Enterprise Architecture Manager不能仅因名称相近而自动视为Enterprise Architect；也不生成合成数值列。'
  profiles.append(r)
 return profiles



def governance_profiles(corpus):
 """Explicit governance participants and specialist responsibilities across guides."""
 definitions=[
 ('G186','stakeholder','Stakeholder','利益相关者（本指南治理语境）','目标架构、豁免及强制遵守目标的架构批准权',
  [(139,'owner of the architecture','作为架构所有者提供优先级、偏好与方向，持有目标架构、豁免及强制遵守目标（enforcement）的决策权。'),(35,'someone who has approval rights','此指南实务语境将Stakeholder聚焦于对目标及实施适用性具有批准权的参与者；不得把该语境限制推广成所有标准的通用定义。')],
  [(141,'limitations in confidence','批准前理解价值、工作、风险及可信度限制。')],
  '输入关注点视图、需求权衡、目标及影响评估；输出批准/否决/豁免/强制遵守目标或修改架构的决定。',
  '有兴趣、被影响、提供信息与持有批准权不是同一事实；审批主体必须在项目中明确。'),
 ('G186','stakeholder-agent','Stakeholder Agent','利益相关者代理','利益相关者代表',
  [(139,'representative of the stakeholder','代表利益相关者参与架构工作。')],
  [(140,'role being performed needs to be clear','一人兼多角色时必须明确当前角色；代理资格不自动赋予架构所有者的全部批准权。')],
  '输入被代表者的关注点与授权范围，输出代表意见；具体授权边界需项目明确。',
  '原文没有单独给代理角色的技能等级或全面授权范围，不能把代理等同实际审批者。'),
 ('G186','subject-matter-expert','Subject Matter Expert','领域专家','企业或环境中的专业知识与解释验证',
  [(139,'possesses specialized knowledge','拥有企业或其环境某方面的专业知识，提供知识、建议和解释验证。'),(141,'facts and interpretation of the facts','核对架构事实及解释；意见分歧需转为对利益相关者的可信度限制说明。')],
  [(139,'specialized knowledge','能力要求是相应领域专业知识及对解释的验证能力；此处未规定数值等级或职业认证。')],
  '输入架构事实/模型/影响评估，输出专业确认、不同意见及证据限制。',
  '专家确认事实和解释不等于替代利益相关者批准目标架构。'),
 ('G186','implementer','Implementer','实施者','实施变更与实现选择',
  [(139,'responsible for performing all change activity','负责执行变更，既包括转型资本项目也包括增量运营变更。'),(140,'implementation choices, such as design, product selection, and change sequence','对提出的设计、产品选择及变更顺序等实施选择持有决策权。'),(37,'context, gap, architecture specification, and control','应收到明确上下文、差距、架构规格和控制，不能仅靠图片猜测责任。')],
  [(142,'reasonable interpretation','按要求/规格进行合理解释并提供符合性依据；未被架构限制的选择仍有设计创造空间。')],
  '输入Architecture Contract、Requirements Specification、工作包和差距；输出实现设计、变更成果及符合性证据。',
  '实现选择权不等于修改目标架构或给予永久豁免的权力。'),
 ('G186','architect-governance','Architect','架构师（治理职责）','目标架构开发、影响评估与建议',
  [(140,'developer of the Target Architecture','开发目标架构，在发现不符合时提供建议。'),(142,'impact assessment and recommendation','发现不符合后形成影响评估，并建议执行约束、临时豁免或修改目标架构。')],
  [(142,'same terms as the target was developed','影响评估应沿用形成目标时的评价口径；不能换一套口径替利益相关者决定。')],
  '输入利益相关者偏好、专家事实与不符合报告；输出目标模型/视图、影响评估及三类处置建议。',
  '架构师提出建议，利益相关者保留目标/豁免/强制遵守目标决策权；enforcement与decision-maker的execution rights（变更执行权）不同。'),
 ('G186','auditor','Auditor / Peer Reviewer','审计者/同行评审者','目标与实施的系统审查',
  [(140,'performs systematic reviews of both the target and implementation','对目标架构和实施开展系统性审查，应在多个阶段及早发现问题。'),(142,'Compliance assessment is an auditor role','符合性评价是审计角色，与架构师后续影响分析/建议角色区分。')],
  [(140,'peer reviewer','可由治理机构、同行评审者或自审承担；无论组织形式如何，必须明确当前审计角色。')],
  '输入目标架构、实现和控制证据；输出符合性评价、不符合发现及需要进一步评估的问题。',
  '原文p140在审计段内把compliance decision rights写给implementer；按字面保留该条，不能擅自改成审计者。p139明确目标、豁免与强制遵守目标的决策权属于stakeholder，二者对象不同，项目仍须澄清合规裁决流程。'),
 ('G186','decision-maker','Decision-Maker','变更决策者','变更执行权',
  [(34,'a decision-maker holds execution rights on change','在本指南沟通分类中持有变更执行权，与目标批准权和实施指导需要区分。'),(137,'decision-makers are validating','分配资金时确认项目经理、组合经理和实施架构师理解并同意按架构交付结果。')],
  [(137,'fully understand and agree to deliver the outcome','能够把资源分配与预期结果、架构符合性联系起来；具体任职技能等级未给出。')],
  '输入价值/预算/路线图/风险及实现承诺；输出资源和执行决策。',
  '不要仅凭职位名称假定审批权和执行权由同一人承担。'),
 ('G184','ea-governance-board','EA Governance Board','EA治理委员会','管理架构合规评价与发布流程',
  [(63,'manage the process of assessing compliance','管理符合性评价过程，按检查表核查证据和利益相关者的批准。'),(63,'approve the architecture for publication','当利益相关者已批准时，批准将架构发布到EA存储库。'),(64,'future compliance assessment and reporting','对临时豁免安排后续合规评价和报告。')],
  [(63,'there is no role for the EA governance board to debate','不把发布治理误作重新辩论或批准目标内容/约束的权力。')],
  '输入架构和不符合建议的检查证据、利益相关者批准；输出发布许可、补做指令及后续检查安排。',
  '治理机构的流程与发布职责不同于目标所有者的内容批准权。G188项目治理语境需另外读取。'),
 ('G188','executive','Executive / Project Sponsor','架构项目Executive/赞助人','项目业务目标、资源与收益责任',
  [(33,"owner of the project’s business goal",'拥有项目业务目标并对预期收益实现负责。'),(33,'provides the necessary resources','提供资源、代表需要，并任命项目经理负责运营层执行。'),(36,'responsibility of the Executive','对Business Case负责，但可委托业务分析师或项目经理编制。')],
  [(40,'ultimate decision-maker','在所述PRINCE2项目治理中作为最终决策者；这是方法语境内的角色。')],
  '输入商业论证、成本/风险/收益及项目报告；输出资源、可行性和继续/终止等战略决定。',
  '赞助人负责不等于亲自编制全部文档，且项目治理不能替代架构治理。'),
 ('G20F','product-owner','Product Owner','产品负责人','需求表达、优先级与敏捷交付',
  [(35,'single product owner','预备阶段确立单一产品负责人原则，确保需求被清楚表达和理解并设置开发优先级。'),(40,'prioritized by the product owner in consultation with the Agile team','与敏捷团队协商优先级；must-have故事集合形成最小可行架构。')],
  [(40,'in consultation with the Agile team','需要表达需求、区分价值优先级及与敏捷团队协作的能力；这是基于职责的分析，不是源文数值等级。')],
  '输入业务需求、用户故事与架构约束；输出有优先级的backlog和must-have选择。',
  '产品局部偏好不自动凌驾企业架构约束，角色也不等同架构师。'),
 ('G152','security-architect','Security Architect','安全架构师','跨域安全与风险架构',
  [(31,'expected role and mandate of the Security Architect','在架构团队定义时明确安全架构师预期角色与授权，把安全风险融入各域。'),(36,'must ensure that the required controls are included','确保所需控制进入技术架构并核对使用的有效性与效率。')],
  [(16,'Security Services Catalog','能够使用安全服务目录将保护构建块与所需安全控制联系起来。')],
  '输入风险/安全要求与前序控制；输出跨域安全设计、控制映射及有效性核对。',
  '授权须在企业治理中确定，安全架构师不自动拥有全部风险接受权。'),
 ('G21B','customer-data-owner','Customer Data Owner Executive','客户数据所有者高管','客户主数据能力责任',
  [(21,'under the responsibility of the customer data owner executive','客户主数据能力由客户数据所有者高管负责，并确保相关参与者贡献。'),(43,'Design a quality dashboard with executives, businesses, business data owners','与业务、数据管家等共同设计质量看板及其需求。')],
  [(21,'ensure the contribution of concerned actors','需要组织相关参与者贡献并明确共享客户数据目标；具体技能等级未给出。')],
  '输入业务客户数据需求、质量/价值信息；输出能力目标、参与者协调及质量度量需求。',
  '所有权/能力责任不是对所有操作的亲自执行，日常修正与治理职责需清楚分配。'),
 ('G234','data-steward','Data Steward','数据管家（元数据治理语境）','数据域元数据维护与治理',
  [(32,'Onboard and appoint data steward','按数据域明确数据管家、业务数据所有者和隐私负责人，识别维护/治理元数据存储库的关键参与者。')],
  [(32,'maintain and govern the metadata repository','需要在已分配角色范围内维护与治理元数据；源文未按这三个角色分别分配所有功能，也未给数值等级。')],
  '输入被分配的数据域、元数据要求与治理流程；输出维护/治理工作及协作证据，具体授权以角色分工为准。',
  '不要把元数据功能目录的全部功能自动全分配给data steward；所有者、管家、隐私负责人分别定义。')]
 out=[]
 for code,key,en,zh,scope,duties,requirements,io,note in definitions:
  r=source_profile(code,key,en,zh,scope)
  r['role_definition']=[assertion(corpus,code,*duties[0])]
  r['responsibilities']=[assertion(corpus,code,*x) for x in duties]
  r['requirements']=[assertion(corpus,code,*x,kind='source-grounded-or-derived-task-capability') for x in requirements]
  r['decision_authority']=[]
  r['inputs_outputs']=[{'text_zh':io,'assertion_type':'derived-input-output-analysis','evidence':evidence(corpus,code,duties[0][0],duties[0][1])}]
  r['analysis_zh']=note
  if key in ['stakeholder','decision-maker','implementer','ea-governance-board','executive']:
   r['decision_authority']=[assertion(corpus,code,*duties[0])]
  if key=='auditor':r['source_caveats']=[assertion(corpus,'G186',140,'All decision rights about compliance during the development of the architecture and implementation are vested with the implementer.','原文这句明确写implementer，保持字面证据；不由此推导审计者可改目标或给予豁免。')]
  out.append(r)
 return out


def supplemental_profiles(corpus):
 """Reviewed role contexts outside the two dedicated skills matrices."""
 path=Path(__file__).with_name('role-additional-profiles.json')
 result=[]
 for spec in json.loads(path.read_text())['profiles']:
  r=source_profile(spec['code'],spec['key'],spec['label_en'],spec['label_zh'],spec['scope_zh'])
  for field in ['role_definition','responsibilities','decision_authority','requirements','inputs_outputs']:
   r[field]=[assertion(corpus,c,p,q,z,kind=k) for c,p,q,z,k in spec[field]]
  r['analysis_zh']=spec['analysis_zh']
  r['qualification_status']='not-specified-no-degree-experience-year-certification-or-numeric-level'
  r['field_status']={f:'source-evidence-or-explicitly-marked-analysis' if r[f] else 'not-specified-in-cited-source' for f in ['responsibilities','decision_authority','requirements','inputs_outputs']}
  r['maintenance_source']=str(path.relative_to(ROOT));r['maintenance_sha256']=sha(path)
  result.append(r)
 return result

# Family membership is a retrieval aid, never an assertion of role equivalence.
ROLE_FAMILY_PROFILE_MAP={
 'chief-architect':['G249:role:chief-architect'],
 'enterprise-architect':['G249:role:enterprise-architect','G198:role:enterprise-architect'],
 'segment-architect':['G249:role:segment-architect','G198:role:segment-architect'],
 'solution-architect':['G249:role:solution-architect','G198:role:solution-architect'],
 'business-architect':['G249:role:business-domain-architect','G198:role:business-architect'],
 'data-architect':['G249:role:data-domain-architect','G198:role:data-architect'],
 'application-architect':['G249:role:application-domain-architect','G198:role:application-architect'],
 'technology-architect':['G249:role:technology-domain-architect','G198:role:technology-architect'],
 'security-architect':['G152:role:security-architect'],
 'architecture-board':['G198:role:architecture-board-member','G184:role:ea-governance-board'],
 'architecture-sponsor':['G198:role:architecture-sponsor'],
 'architecture-manager':['G198:role:enterprise-architecture-manager'],
 'project-manager':['G188:role:project-manager','G198:role:program-project-manager'],
 'program-manager':['G186:role:program-portfolio-manager','G198:role:program-project-manager'],
 'portfolio-manager':['G186:role:program-portfolio-manager'],
 'product-owner':['G20F:role:product-owner'],
 'product-manager':['G21H:role:product-manager'],
 'data-owner':['G21B:role:customer-data-owner','G234:role:business-data-owner'],
 'data-steward':['G234:role:data-steward'],
 'business-owner':['G242:role:business-owner'],
 'executive':['G188:role:executive','G184:role:ceo'],
 'business-leader':['G186:role:senior-leader'],
 'stakeholder':['G186:role:stakeholder'],
 'customer-user':['G186:role:customer','G217:role:information-user'],
 'subject-matter-expert':['G186:role:subject-matter-expert'],
 'implementer':['G186:role:implementer'],
 'operator':['G152:role:operator'],
 'designer':['G198:role:it-designer'],
 'practitioner':['G186:role:architecture-practitioner','G217:role:digital-practitioner'],
 'business-analyst':['G152:role:business-analyst'],
 'CIO':['G242:role:cio'], 'CEO':['G184:role:ceo'],
 'ea-capability-leader':['G184:role:ea-capability-leader'],
 'business-requirements-owner':['G186:role:business-requirements-owner'],
 'risk-owner':['G186:role:risk-owner'],
 'business-partner':['G186:role:business-partner'],
 'digital-practitioner':['G217:role:digital-practitioner'],
 'product-team':['G217:role:product-team'],
 'data-privacy-officer':['G234:role:data-privacy-officer'],
 'data-custodian':['G234:role:data-custodian'],
 'data-management-office':['G234:role:data-management-office'],
 'data-trustee':['G217:role:data-trustee'],
 'auditor':['G186:role:auditor'],
 'decision-maker':['G186:role:decision-maker'],
 'stakeholder-agent':['G186:role:stakeholder-agent'],
 'architect-governance':['G186:role:architect-governance'],
}

COVERAGE_CONTEXT={
 'change-manager':('context-only-no-independent-requirements', [('G212',28,'supporting teams, such as top-down champions and change managers')], 'G212把变更经理列为赞助人支持团队、G249列为协作方；这些上下文没有独立职责或任职能力定义，不能从Change Management职能推导岗位全部职责。'),
 'risk-manager':('non-role-match-only',[('G152',15,'Financial Risk Manager certification')], '唯一命中是FRM证书名称，不能作为风险经理岗位定义或所有角色必须持证的要求。'),
 'compliance-officer':('context-only-no-independent-requirements',[('G184',49,'Chief Compliance Officer'),('G184',116,'security or compliance officers or developers')], 'Chief Compliance Officer被列为EA服务利益相关者，另有观点平衡提及；High/Medium/Low描述EA服务相关性，不是该岗位技能等级。'),
 'chief-risk-officer':('context-only-no-independent-requirements',[('G184',49,'Chief Risk Officer')], '利益相关者表列出首席风险官及EA相关性；未提供其独立职位要求，不能等同Risk Manager或Risk Owner。'),
 'scrum-master':('context-only-no-independent-requirements',[('G186',109,'scrum master')], '源文要求架构交付的权衡和决策标准对Scrum Master等参与者明确；没有定义该角色完整职责或资格。'),
 'data-manager':('context-only-no-independent-requirements',[('G234',38,'data protection officer, data manager')], '数据经理在规则制定征询者中出现，未单独分配元数据功能或任职条件。'),
 'application-owner':('context-only-no-independent-requirements',[('G234',35,'application owner')], '应用所有者出现在元数据归属记录的角色清单；并非独立岗位职责标准。'),
 'internal-controller':('context-only-no-independent-requirements',[('G234',38,'internal controllers')], '内部控制人员属于数据规则需征询的参与者；未规定数值技能或签字权。'),
 'sustainability-expert':('specialty-training-context-not-job-specification',[('G242',92,'ICT low-carbon design experts (architects)'),('G242',92,'Skills need to be managed and trained according to different roles')], '原文列举碳度量、ICT低碳设计（架构师）、资产生命周期、低技术专家，要求按不同角色培训；不提供逐岗位职责或技能等级，保留专业方向和培训上下文。'),
}


def build_coverage(corpus,profiles,mentions):
 byid={p['id']:p for p in profiles};families=[]
 grouped=defaultdict(list)
 for m in mentions['mentions']:grouped[m['role_family']].append(m)
 for f in mentions['role_families']:
  key=f['id'];matches=grouped[key];pids=ROLE_FAMILY_PROFILE_MAP.get(key,[])
  if any(pid not in byid for pid in pids):raise ValueError('Unresolved role family profile '+key)
  ev=[]
  if pids:
   state='profiled-with-source-specific-scope'
   for pid in pids:
    for a in byid[pid]['role_definition']:ev.append(a['evidence'])
   note='读取所列档案中的来源特定定义、职责与要求；族关联用于检索，不把不同指南角色、岗位或量表视作等同。'
  elif key in COVERAGE_CONTEXT:
   state,quotes,note=COVERAGE_CONTEXT[key];ev=[evidence(corpus,*q) for q in quotes]
  elif not matches:
   state='not-found-in-controlled-body-scan';note='全26份已转换正文中未命中该受控名称；这是有限词表的阴性结果，不证明其他名称或外部标准不存在该角色。'
  else:raise ValueError('Role family lacks explicit disposition '+key)
  families.append({**f,'disposition':state,'profile_ids':pids,'mention_ids':[m['id'] for m in matches],
   'evidence':ev,'qualification_status':'see-source-specific-profiles' if pids else 'not-specified-in-reviewed-context',
   'responsibility_status':'see-source-specific-profiles' if pids else 'not-independently-defined-in-reviewed-context',
   'analysis_zh':note})
 # Every profile must have an explicit family route; otherwise it is invisible to the audit.
 linked={pid for f in families for pid in f['profile_ids']}
 if linked!=set(byid):raise ValueError('Unmapped profiles '+str(sorted(set(byid)-linked)))
 return {'schema_version':'role-family-coverage/1','content_role':'derived-role-coverage-disposition',
  'notice_zh':'逐族归集全26指南的命中上下文，再把有明确职责/要求的角色连接到来源特定档案。名称命中、作者经历、证书名称、图中示例和协作清单不自动成为岗位要求。未规定的资格/等级明确保持未规定。',
  'initial_controlled_family_count':39,'family_count':len(families),'document_count_scanned':26,'families':families,
  'counts':{'role_families':len(families),'profiled_role_families':sum(bool(f['profile_ids']) for f in families),
            'context_only_role_families':sum(f['disposition'] in ['context-only-no-independent-requirements','specialty-training-context-not-job-specification'] for f in families),
            'non_role_match_families':sum(f['disposition']=='non-role-match-only' for f in families),
            'unobserved_role_families':sum(f['disposition']=='not-found-in-controlled-body-scan' for f in families),
            'mapped_profiles':len(linked),'assigned_mentions':sum(len(f['mention_ids']) for f in families)}}


def render_coverage(coverage,profiles):
 byid={p['id']:p for p in profiles}
 lines=['# 角色族完整覆盖与未规定项','','覆盖最初39类受控角色，并补充正文中明确出现的重要治理、数据和数字交付角色。每个命中片段保留在mentions.json；每族都有明确处置，任职要求不得由名称或常识补造。','','|角色族|片段数|处置|来源特定档案|','|---|---:|---|---|']
 for f in coverage['families']:
  links='；'.join('['+byid[pid]['label_zh']+']('+pid.replace(':role:','-')+'.md)' for pid in f['profile_ids']) or '无独立档案；见下方理由'
  lines.append('|'+f['label_zh']+' (`'+f['id']+'`)|'+str(f['mentions'])+'|'+f['disposition']+'|'+links+'|')
 for f in coverage['families']:
  if f['profile_ids']:continue
  lines+=['','## '+f['label_zh'],'',f['analysis_zh'],'','职责：未在该上下文独立规定。任职资格与数值技能：未规定。']
  for e in f['evidence']:lines.append('- '+e['document_id']+' PDF '+str(e['pdf_page'])+'：'+e['quote_en'])
 return '\n'.join(lines)+'\n'


def role_relationships(corpus):
 rels=[]
 def add(code,a,b,predicate,page,quote,zh):
  rels.append({'id':f'role-rel-{len(rels)+1:03}','from':code+':role:'+a,'to':code+':role:'+b,'predicate':predicate,'assertion_type':'source-explicit',
               'is_hr_reporting_line':False,'meaning_zh':zh,'evidence':evidence(corpus,code,page,quote)})
 add('G249','chief-architect','enterprise-architect','special_case_of',17,'special case of an Enterprise Architect','首席架构师是企业架构师的特殊情形，属于角色概念关系。')
 for target in ['enterprise-architect','segment-architect','solution-architect']:
  add('G249','chief-architect',target,'leads_and_coaches',18,'They lead Enterprise Architects, Segment Architects, Solution Architects','首席提供领导与辅导，为架构全景演进建立条件。')
 for target in ['segment-architect','solution-architect']:
  add('G249','enterprise-architect',target,'leads_and_integrates',19,'leading Segment Architects, Solution Architects','企业层领导并整合分段/解决方案工作，形成互操作与治理条件。')
 add('G249','segment-architect','solution-architect','provides_context_and_guidance',22,'technical/business specialists and Solution Architects','分段层使解决方案架构师和专家明确角色并有效协作。')
 for a in ['enterprise-architect','segment-architect']:
  add('G249','solution-architect',a,'informed_by_higher_scope_architecture',17,'superior architectures identified at the Enterprise and Segment Levels','解决方案设计受企业/分段层架构指引；上位指架构范围，不证明雇佣汇报。')
  rels[-1]['assertion_type']='authored-semantic-mapping'
  rels[-1]['intermediary_architecture_scope']={'concept_id':'architecture-scope:'+a.removesuffix('-architect'),'label_en':a.removesuffix('-architect').title()+' Architecture',
    'source_statement_subject':'Solution Architect design','source_statement_object':'architecture at the Enterprise/Segment Level',
    'mapping_notice_zh':'原文对象是上位架构；此处关联相应范围角色便于检索，不将其误称为直接人对人指引。'}
 for key,en,zh in G249_MATRIX[1:5]:
  add('G249',key,'segment-architect','domain_context_of',21,'four particular segments are called','四个域是分段概念的专业视角；此关系不赋予直属领导身份。')
 for target in ['segment-architect','solution-architect']:
  add('G198','enterprise-architect',target,'may_lead_architecture_team',22,'often leads a group','特定项目群可由EA领导分段/解决方案架构团队，原文often不是通用组织定律。')
 add('G198','solution-architect','segment-architect','shields_implementation_detail',23,'shield the Enterprise/Segment Architect','解决方案角色屏蔽不必要实现细节，保持分层抽象。')
 add('G186','stakeholder-agent','stakeholder','represents',139,'representative of the stakeholder','代理代表利益相关者，具体授权不能超出已证实范围。')
 add('G186','subject-matter-expert','architect-governance','provides_knowledge_and_validation',139,'Provides knowledge, advice, and validation of interpretation','专业知识和验证支持架构工作，不替代目标批准。')
 add('G186','architect-governance','stakeholder','recommends_target_and_relief',142,'impact assessment and recommendation','架构师形成影响评估与处置建议，交利益相关者决定。')
 add('G186','auditor','implementer','reviews_implementation_work',140,'performs systematic reviews of both the target and implementation','对实施工作进行系统审查，不表达雇佣隶属。')
 add('G186','auditor','architect-governance','reviews_target_work',140,'performs systematic reviews of both the target and implementation','对目标架构工作进行系统审查，可由同行承担。')
 add('G186','stakeholder','implementer','holds_target_approval_not_implementation_choices',139,'All decision rights about the Target Architecture','利益相关者决定目标/豁免/强制遵守目标，实施者在约束内决定实现选择。')
 return rels


def comparison(profiles):
 byid={p['id']:p for p in profiles};pairs=[]
 for old,new in [('business-architect','business-domain-architect'),('data-architect','data-domain-architect'),('application-architect','application-domain-architect'),('technology-architect','technology-domain-architect'),('solution-architect','solution-architect')]:
  a=byid['G198:role:'+old];b=byid['G249:role:'+new]
  def key(s):return re.sub(r'[^a-z0-9]','',s['label_en'].lower()).replace('communications','communication')
  am=defaultdict(list);bm=defaultdict(list)
  for s in a['skills']:am[key(s)].append(s)
  for s in b['skills']:bm[key(s)].append(s)
  matches=[]
  for k in sorted(am.keys()&bm.keys()):
   if len(am[k])!=1 or len(bm[k])!=1:continue
   x,y=am[k][0],bm[k][0]
   matches.append({'g198_skill_id':x['skill_id'],'g249_skill_id':y['skill_id'],'label_g198':x['label_en'],'label_g249':y['label_en'],
                   'g198_level':x['reference_level'],'g249_level':y['reference_level'],'source_numeric_values_differ':y['reference_level']!=x['reference_level'],
                   'comparison_basis':'normalized-unambiguous-label; source scale definitions differ; numeric values juxtaposed without arithmetic delta; not an official crosswalk',
                   'evidence':[x['evidence'],y['evidence']]})
  pairs.append({'role_g198':a['id'],'role_g249':b['id'],'relationship':'related-role-not-identical','source_skill_counts':[len(a['skills']),len(b['skills'])],
                'compared_skills':matches,'different_source_values':[m for m in matches if m['source_numeric_values_differ']]})
 return {'content_role':'derived-comparison','scale_comparability':'different-ordinal-definitions-no-numeric-delta',
         'notice_zh':'两个指南的角色、技能类别、量表定义与版本上下文不同；同名词项只作原值对照，不能视为同标尺差值或能力升降，不合并为唯一等级。Chief/Segment无独立数值列，G198 EA Manager与EA文本角色不自动等同。','pairs':pairs}

MENTION_ROLES=[
('chief-architect','首席架构师',r'chief architects?'),('enterprise-architect','企业架构师',r'enterprise architects?'),('segment-architect','分段架构师',r'segment architects?'),
('solution-architect','解决方案架构师',r'solution architects?'),('business-architect','业务架构师',r'business (?:domain )?architects?'),('data-architect','数据架构师',r'data (?:domain )?architects?'),
('application-architect','应用架构师',r'application (?:domain )?architects?'),('technology-architect','技术架构师',r'technology (?:domain )?architects?'),('security-architect','安全架构师',r'security architects?'),
('architecture-board','架构委员会',r'architecture boards?'),('architecture-sponsor','架构赞助人',r'architecture sponsors?'),('architecture-manager','架构经理',r'(?:enterprise )?architecture managers?'),
('project-manager','项目经理',r'project managers?'),('program-manager','项目群经理',r'program managers?'),('portfolio-manager','组合经理',r'portfolio managers?'),('product-owner','产品负责人',r'product owners?'),
('product-manager','产品经理',r'product managers?'),('change-manager','变更经理',r'change managers?'),('data-owner','数据所有者',r'data owners?'),('data-steward','数据管家',r'data stewards?'),
('information-owner','信息所有者',r'information owners?'),('business-owner','业务所有者',r'business owners?'),('process-owner','流程所有者',r'process owners?'),('service-owner','服务所有者',r'service owners?'),
('executive','高管/Executive',r'(?:executives?|executive sponsors?)'),('business-leader','业务领导',r'business (?:segment )?leaders?'),('stakeholder','利益相关者',r'stakeholders?'),
('customer-user','客户与用户',r'(?:customers?|users?)'),('subject-matter-expert','领域专家',r'subject matter experts?'),('implementer','实施者',r'implementers?|implementors?'),
('operator','运营者',r'operators?'),('designer','设计师',r'(?:IT )?designers?'),('practitioner','架构实践者',r'(?:architecture |EA )?practitioners?'),('business-analyst','业务分析师',r'business analysts?'),
('risk-manager','风险经理',r'risk managers?'),('compliance-officer','合规人员',r'compliance officers?'),('CIO','首席信息官',r'CIO|Chief Information Officer'),
('CISO','首席信息安全官',r'CISO|Chief Information Security Officer'),('CEO','首席执行官',r'CEO|Chief Executive Officer'),
('ea-capability-leader','EA能力负责人',r'EA Capability Leaders?'),('business-requirements-owner','业务需求所有者',r'Business Requirements Owners?'),
('risk-owner','风险所有者',r'Risk Owners?'),('business-partner','业务伙伴',r'Business Partners?'),
('digital-practitioner','数字实践者',r'Digital Practitioners?'),('product-team','产品团队',r'product teams?'),
('data-privacy-officer','数据隐私负责人',r'data (?:privacy|protection) officers?'),('data-custodian','数据保管者',r'data custodians?'),
('data-management-office','数据管理办公室',r'Data Management Office'),('data-trustee','数据受托人',r'data trustee|trustee accountable for data quality'),
('auditor','审计者',r'auditors?|peer reviewers?'),('decision-maker','变更决策者',r'decision-makers?'),
('stakeholder-agent','利益相关者代理',r'stakeholder agents?|representative of the stakeholder'),('architect-governance','治理中的架构师角色',r'developer of the Target Architecture'),
('chief-risk-officer','首席风险官',r'Chief Risk Officer'),('scrum-master','Scrum Master',r'scrum masters?'),
('data-manager','数据经理',r'data managers?'),('application-owner','应用所有者',r'application owners?'),
('internal-controller','内部控制人员',r'internal controllers?'),('sustainability-expert','数字可持续专业方向',r'low-carbon design experts|digital carbon measure champions|low-tech experts')]



def build_mentions(corpus):
 out=[];summary=defaultdict(Counter)
 for path in sorted((corpus/'documents').glob('G*.json')):
  d=json.loads(path.read_text());code=d['id']
  for page in d['pages']:
   for item in page['content']:
    text=item['text']
    if item['type'] not in ['text','table'] or re.search(r'(?:\.\s*){5,}',text):continue
    pn=page['pdf_page'];active=[s for s in d['outline'] if s['pdf_page']<=pn]
    if active and active[-1]['title'] in ['Index','Table of Contents']:continue
    for key,zh,pattern in MENTION_ROLES:
     if re.search(r'\b(?:'+pattern+r')\b',text,re.I):
      isnorm=bool(re.search(r'\b(?:responsib|accountab|must|should|shall|requires?|ensures?|govern|approv|decision|lead|skill|competenc|appoint)',text,re.I))
      out.append({'id':f'role-mention-{len(out)+1:05}','role_family':key,'role_label_zh':zh,'document_id':code,'pdf_page':pn,
                  'source_path':d['source']['path'],'source_sha256':d['source']['sha256'],'quote_en':text,
                  'evidence_kind':'responsibility-or-requirement-candidate' if isnorm else 'contextual-mention',
                  'semantic_status':'context-evidence-not-a-normalized-role-requirement','block_ids':item.get('source_block_ids',[])})
      summary[key][code]+=1
 return {'content_role':'role-context-evidence-index','notice_zh':'全26指南按受控角色词表检索的正文上下文；出现名称不等于独立角色定义，must/should等候选词不代表已验证授权。角色详细分析见profiles。',
         'role_families':[{'id':k,'label_zh':z,'source_documents':dict(summary[k]),'mentions':sum(summary[k].values())} for k,z,_ in MENTION_ROLES],
         'mentions':out,'document_count_scanned':26}


def render_profile(r):
 lines=[f'# {r["label_zh"]} / {r["label_en"]}', '', f'记录：`{r["id"]}`；依据：{r["source_guide"]}；内容角色：`source-grounded-role-analysis`。', '',f'范围：{r["scope_zh"]}。', '',r['hierarchy_notice_zh'],'',r['qualification_notice_zh'],'']
 for field,title in [('role_definition','角色定位'),('responsibilities','职责'),('decision_authority','决策与治理权限'),('requirements','任职与能力要求'),('inputs_outputs','输入与输出')]:
  lines+=['## '+title,'']
  for a in r[field]:
   e=a['evidence'];detail='原文：'+e['quote_en'] if 'quote_en' in e else f'源矩阵行{e["row_index_zero_based"]+1} 列{e["role_column_index_zero_based"]+1}'
   lines.append(f'- {a["text_zh"]}（{e["document_id"]} PDF 第 {e["pdf_page"]} 页；{detail}）')
  if not r[field]:lines+=['该指南未独立规定此项。下方技能参考值不自动赋予职责或权限。']
  lines+=['']
 if r.get('shared_responsibility_context'):lines+=['共用角色语境：`'+r['shared_responsibility_context']['role_id']+'`；作为专业上下文读取，不视为雇佣汇报。','']
 lines+=['## 分析结论','',r.get('analysis_zh',''),'']
 if r.get('skills'):
  if r.get('proficiency_reference_notice'):lines += [r['proficiency_reference_notice']['text_zh'],'']
  c=r['competency_analysis'];lines += [f'完整技能：{c["skill_count"]} 项；等级分布：'+json.dumps(c['levels'],ensure_ascii=False)+'。', '',c['application_zh'],'','### 等级定义','']
  for s in r['proficiency_scale']:lines.append(f'- {s["level"]} / {s["name_en"]}：{s["description_en"]}')
  lines+=['','### 各类能力侧重','','|类别|技能数|专家级(4)技能|','|---|---:|---|']
  for s in c['category_profiles']:lines.append(f'|{mdcell(s["category"])}|{s["skills"]}|{mdcell("；".join(s["level_4_skills"]) or "无4级条目；其余等级见完整表")}|')
  lines+=['','### 全部技能要求','','|类别|技能|参考等级|等级含义|证据|','|---|---|---:|---|---|']
  for s in r['skills']:
   e=s['evidence'];lines.append(f'|{mdcell(s["category_zh"])}|{mdcell(s["label_en"])}|{s["reference_level"]}|{s["level_name_en"]}|{e["document_id"]} p{e["pdf_page"]} 行{e["row_index_zero_based"]+1} 列{e["role_column_index_zero_based"]+1}|')
 else:lines+=['本指南没有该角色的独立数值技能列。保留文本要求，不生成虚构等级或平均等级。','']
 if r.get('source_caveats'):
  lines+=['','## 原文中须保留的权限措辞','']
  for x in r['source_caveats']:lines.append('- '+x['text_zh']+' 原文：'+x['evidence']['quote_en'])
 for field,title in [('collaboration','协作对象（不等同直属上下级）'),('potential_kpis','原文候选 KPI（不是项目已采纳目标）')]:
  if r[field]:
   lines+=['','## '+title,'']
   for x in r[field]:lines.append(f'- {x["text_en"]}（PDF 第 {x["evidence"]["pdf_page"]} 页）')
 if r['relationships']:
  lines+=['','## 角色关系','','|关系|另一角色|含义|','|---|---|---|']
  for e in r['relationships']:lines.append(f'|{e["predicate"]}|{e["to"] if e["from"]==r["id"] else e["from"]}|{e["meaning_zh"]}|')
 lines+=['','## 可执行能力核对建议','','逐技能收集可核实的设计产物、决策理由、协作反馈及交付经历；按本项目选择的角色范围与参考等级逐项判断。原文未给出统一加权总分、合格阈值或自动认证规则。该建议为项目应用分析，不是原文强制流程。','']
 return '\n'.join(lines)



def verify_profile_evidence(profiles, relationships, root):
 cache={};hashes={};quotes=[];ids={p['id'] for p in profiles}
 def visit(value):
  if isinstance(value,dict):
   if 'quote_en' in value and 'source_path' in value and 'pdf_page' in value:
    path=value['source_path'];pn=value['pdf_page'];quote=norm(value['quote_en'])
    if path not in cache:
     cache[path]=fitz.open(root/path);hashes[path]=sha(root/path)
    if quote not in norm(cache[path][pn-1].get_text()):raise ValueError(f'Quote not in original PDF: {path} {pn} {quote}')
    if value.get('source_sha256')!=hashes[path]:raise ValueError('Quote source hash mismatch')
    quotes.append((path,pn,quote))
   for child in value.values():visit(child)
  elif isinstance(value,list):
   for child in value:visit(child)
 try:
  visit(profiles)
  for rel in relationships:
   if rel['from'] not in ids or rel['to'] not in ids:raise ValueError('Role relation endpoint missing')
   if rel['is_hr_reporting_line']:raise ValueError('Unsubstantiated HR reporting edge')
 finally:
  for doc in cache.values():doc.close()
 return {'quoted_evidence_instances_checked_against_source_pdf':len(quotes),'unique_quoted_evidence_checked':len(set(quotes)),'quoted_evidence_issues':[]}


def build_roles(root=ROOT,output=None):
 root=Path(root);corpus=Path(output) if output else root/'togaf-standard-10th-ai';dest=corpus/'architecture/roles';dest.mkdir(parents=True,exist_ok=True)
 scale249,skills249,summary249,check249=extract_g249(root,corpus);scale198,skills198,check198=extract_g198(corpus,root)
 profiles=curated_profiles(corpus)+governance_profiles(corpus)+supplemental_profiles(corpus)
 for code,matrix,skills,scale in [('G249',G249_MATRIX,skills249,scale249),('G198',G198_MATRIX,skills198,scale198)]:
  for ci,(key,en,zh) in enumerate(matrix):attach_skills(next(p for p in profiles if p['id']==code+':role:'+key),code,ci,skills,scale)
 rels=role_relationships(corpus)
 for r in profiles:r['relationships']=[x for x in rels if r['id'] in [x['from'],x['to']]]
 # All printed G249 summaries must be retained and compared with actual cells.
 arithmetic=[]
 for ci,(key,en,zh) in enumerate(G249_MATRIX):
  vals=[s['values'][ci] for s in skills249];counts=Counter(vals)
  expected={'Total':str(sum(vals)),'Number of Level 4s':str(counts[4]),'Number of Level 3s':str(counts[3]),'Number of Level 2s':str(counts[2]),'Number of Level 1s':str(counts[1]),'Total Number of Skills':str(len(vals))}
  printed={s['label']:s['values'][ci] for s in summary249};issues=[k for k,v in expected.items() if printed.get(k)!=v]
  mean_value=sum(vals)/len(vals); mean_text=printed.get('Mean',''); digits=len(mean_text.split('.')[1]) if '.' in mean_text else 0
  arithmetic.append({'role_id':'G249:role:'+key,'computed':expected,'printed':printed,'mismatched_fields':issues,'mean_computed':mean_value,
                     'mean_printed':mean_text,'mean_recomputed_at_printed_precision':round(mean_value,digits),
                     'mean_discrepancy':round(mean_value,digits)!=float(mean_text),'mean_note':'原文Technology Domain Architect Mean写2.6，189/71按一位小数应2.7；保留原值和算术差异，不把等级均值用作能力评分。'})
  if issues:raise ValueError(f'G249 summary mismatch {key}: {issues}')
 for r in profiles:
  key=r['id'].replace(':role:','-');write(dest/(key+'.json'),r);(dest/(key+'.md')).write_text(render_profile(r))
 comp=comparison(profiles);write(dest/'comparison.json',comp)
 lines=['# 角色与技能框架比较','','G198 和 G249 分别保留完整原始要求。G198 有79项技能×10角色；G249 有71项技能×6角色。两量表定义不同：G198 Level 1 是“Not a required skill, but could be useful”；G249 Level 1 是“Some understanding but reliant on specialists”。因此数字仅并列显示各源原值，不能视为同标尺差值、能力升降或要求变严/变松。','','|G198角色|G249相关角色|同名词项对照数|原值不同数|','|---|---|---:|---:|']
 for p in comp['pairs']:lines.append(f'|{p["role_g198"]}|{p["role_g249"]}|{len(p["compared_skills"])}|{len(p["different_source_values"])}|')
 lines+=['','## 不可直接合并的角色','','Chief Architect 在 G249 有完整职责，技能矩阵没有Chief列。Segment Architect 有通用职责，矩阵提供四个Domain角色列。G198 Enterprise Architecture Manager 是矩阵列，Enterprise Architect 是文本定义角色；不能把两个名称当成同一角色。','','## G249表5-2页底完整性','','原文p27最后一行Integration and Sharing、p28最后一行Oral Communication必须保留。独立直接抽取后实际71技能、426等级单元格与原文合计及等级计数一致；这些行不能因页脚裁剪被遗漏。原文技术域角色Mean=2.6，而189/71按一位小数为2.7；这是保留在原值与重算字段中的算术差异，不将任一均值当人员评价。','','## 同名技能的数值差异','']
 for p in comp['pairs']:
  lines+=['### '+p['role_g198']+' → '+p['role_g249'],'','|技能|G198|G249|','|---|---:|---:|']
  for s in p['different_source_values']:lines.append(f'|{s["label_g249"]}|{s["g198_level"]}|{s["g249_level"]}|')
 (dest/'comparison.md').write_text('\n'.join(lines)+'\n')
 write(dest/'skills.json',{'schema_version':'role-skills/1','content_role':'source-matrix-transcription','G249':{'role_columns':[{'id':'G249:role:'+r[0],'label':r[1],'column_index_zero_based':i+2} for i,r in enumerate(G249_MATRIX)],'scale':scale249,'skills':skills249,'printed_summary':summary249,'arithmetic_check':arithmetic},'G198':{'role_columns':[{'id':'G198:role:'+r[0],'label':r[1],'column_index_zero_based':i+1} for i,r in enumerate(G198_MATRIX)],'scale':scale198,'skills':skills198}})
 write(dest/'relationships.json',{'schema_version':'role-relations/1','relationships':rels,'notice_zh':'专业上下文、领导治理、范围和协作关系分别记录；未生成缺乏证据的人事直属汇报。'})
 mentions=build_mentions(corpus);write(dest/'mentions.json',mentions)
 coverage=build_coverage(corpus,profiles,mentions);write(dest/'coverage.json',coverage)
 (dest/'coverage.md').write_text(render_coverage(coverage,profiles))
 mlines=['# 全指南角色语境证据','','26份指南按受控角色词表定位。以下统计是证据出现数量，不是不同人员或正式岗位数量。完整正文片段见 mentions.json。','','|角色族|文档数|片段数|','|---|---:|---:|']
 for m in mentions['role_families']:mlines.append(f'|{m["label_zh"]} ({m["id"]})|{len(m["source_documents"])}|{m["mentions"]}|')
 (dest/'mentions.md').write_text('\n'.join(mlines)+'\n')
 validation={'passed':True,'numeric_cells_verified':check249['numeric_cells_checked']+check198['numeric_cells_checked'],'G249':check249,'G198':check198,
             'G249_source_sum_and_level_counts_match_all_six_columns':True,'G249_mean_discrepancies':[a for a in arithmetic if a['mean_discrepancy']],'role_count':len(profiles),'matrix_profile_count':sum(bool(p['skills']) for p in profiles),
             'source_matrix_value_count':sum(len(p['skills']) for p in profiles),'relationship_count':len(rels),'unsupported_hr_reporting_edges':0,
             'limits':['role evidence is not evidence about an actual employee','source-unprovided degrees, experience years, certifications and job reporting lines remain unspecified']}
 validation.update(verify_profile_evidence(profiles,rels,root))
 write(dest/'validation.json',validation)
 index={'schema_version':'role-analysis-index/1','content_role':'source-grounded-role-analysis','counts':{'roles':len(profiles),'matrix_roles':sum(bool(p['skills']) for p in profiles),
        'skill_expectations':validation['source_matrix_value_count'],'skills_G249':len(skills249),'skills_G198':len(skills198),'role_relationships':len(rels),'context_evidence_records':len(mentions['mentions']),'documents_scanned':26,**coverage['counts']},
        'profiles':[{'id':p['id'],'label_en':p['label_en'],'label_zh':p['label_zh'],'source_guide':p['source_guide'],'skill_count':len(p['skills']),
                     'json':p['id'].replace(':role:','-')+'.json','markdown':p['id'].replace(':role:','-')+'.md'} for p in profiles],
        'skills':'skills.json','relationships':'relationships.json','comparison':'comparison.json','mentions':'mentions.json','coverage':'coverage.json','validation':'validation.json'}
 write(dest/'index.json',index)
 lines=['# 架构角色、职责与能力分析','','明确回答每个角色负责什么、在哪个范围决策、与谁协作、输入输出是什么、需要哪些技能及多少深度。依据G249/G198及相关指南，保留原文页码和逐格证据。','','[框架差异](comparison.md) · [完整技能数据](skills.json) · [上下级与协作关系](relationships.json) · [全26指南角色证据](mentions.md) · [逐角色族覆盖](coverage.md) · [数值验证](validation.json)','','## 角色目录','','|角色|来源|完整技能数|JSON|','|---|---|---:|---|']
 for p in index['profiles']:lines.append(f'|[{p["label_zh"]}]({p["markdown"]})|{p["source_guide"]}|{p["skill_count"]}|[结构数据]({p["json"]})|')
 lines+=['','## 关系判读','','```mermaid','flowchart TD','  CA[首席架构师] -->|领导、治理与辅导| EA[企业架构师]','  EA -->|跨分段整合与领导| SA[分段架构师]','  SA -->|上下文、标准与协作指引| SO[解决方案架构师]','  SO -->|设计受其指引| HS[企业与分段层架构]','```','','图示依据G249 p17–24，表示架构责任范围与领导治理，不声明人事直属汇报。首席是企业架构师的特殊角色；业务/数据/应用/技术域与企业/分段/解决方案范围是不同分类轴。','','## 数值完整性','','G249逐PDF源格独立读出71技能×6列=426值；G198逐图色块独立重算79技能×10列=790值，共1216个参考等级。G249各列合计、等级数量及71项计数与印刷汇总一致。','','无数值列不等于无技能要求：Chief、Segment、G198文本EA等保存原文职责/要求，明确无对应独立列。没有个人能力数据时不生成能力达标结论，也不虚构学历、年限、认证或签字权。','']
 (dest/'index.md').write_text('\n'.join(lines));print(json.dumps(index['counts'],ensure_ascii=False));return index

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'togaf-standard-10th-ai');a=p.parse_args();build_roles(ROOT,a.output)
