#!/usr/bin/env python3
"""Build source-linked architectural graphs, hierarchy views, and diagram analyses.

The source drawing, its semantic interpretation, a container tree, and an
organizational reporting tree are distinct data. This module never silently
converts one into another. All source elements, relations, and tables survive.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
import copy
import hashlib
import html
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
VERSION = 'architecture-diagrams/1.0'
DECORATIVE = {'cover-branding','factor-callout-icon','note-callout-icon','information-callout-icon'}
TYPE_ZH = {'group':'分组','function':'功能','process':'流程','concept':'概念','capability':'能力','service':'服务',
 'organization_unit':'组织单元','phase':'阶段','artifact':'制品','data':'信息/数据','note':'说明','application':'应用',
 'architecture':'架构','goal':'目标/成果','role':'角色','actor':'参与者','stakeholder':'利益相关者','metric':'度量',
 'requirement':'需求','principle':'原则','value_stream_stage':'价值流阶段','event':'事件','resource':'资源',
 'time':'时间','value_stream':'价值流','technology':'技术','building_block':'构建块','risk':'风险',
 'product':'产品','framework':'框架','location':'位置','skill':'技能','level':'等级','option':'选项','notation':'记法',
 'value':'价值','outcome':'成果','gap':'差距','other':'其他'}
REL_ZH = {'association':'关联','flow':'流动','sequence':'先于','composition':'包含组成','serving':'支撑/服务',
 'reports_to':'汇报于','produces':'产生/交付','influence':'影响','access':'访问','governs':'治理/监督',
 'maps_to':'映射','realization':'实现','dependency':'依赖','consumes':'消费','assignment':'参与/分配',
 'causal':'因果','iteration':'迭代','triggering':'触发','transitions_to':'过渡到','aggregation':'聚合',
 'specialization':'特化','contrast':'对比','equivalence':'等价','other':'相关','instantiates':'实例化',
 'organization_part_of':'组织组成属于','uses':'使用','modifies':'修改','enables':'使能','realizes':'实现',
 'implemented_by':'由…实现','implements':'实现','served_by':'由…支撑','performs':'执行',
 'requires_skill':'要求技能','applies_in_phase':'适用阶段','visual_contains':'视觉包含',
 'classified_under':'分组归属','skill_level':'熟练等级','option_order':'选项顺序',
 'governance_scope':'治理范围','visual_grouping':'版式分组','operationalizes':'落实为行为',
 'display_order':'图内排列次序',
 'delivers':'交付','provides_specifications':'提供规格并治理交付','provides_constraints':'提供潜在方案与约束',
 'value_item_for':'作为价值项用于','receives':'接收','participates_in':'参与',
 'covers_portion_of':'覆盖该层部分元素','encapsulates':'封装','accessed_through':'通过其访问/更新',
 'implemented_on':'实现在其平台上','provides_platform_for':'为其提供平台',
 'governed_by':'受治理于','bounded_by':'受约束于','supplies_or_consumes':'供应或消费',
 'cross_cuts':'横跨','measured_in':'以…度量','change_affects':'变化影响','depends_on':'依赖',
 'orchestrates_and_decomposes':'编排与分解','supports':'支持','motivated_by':'受驱动于',
 'provides_governed_interface':'提供受治理的访问接口','resolves':'解决'}


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def norm(text): return re.sub(r'\s+', ' ', str(text or '')).strip()
def gid(fid, local): return fid+'#'+local

def safe_label(text):
    return html.escape(norm(text), quote=True).replace('[','&#91;').replace(']','&#93;').replace('|','&#124;').replace('{','&#123;').replace('}','&#125;')

def compact_quote(text, limit=1100):
    text=norm(text)
    return text if len(text)<=limit else text[:limit]+'…'


def load_reviews(root):
    p = Path(__file__).with_name('architecture-diagram-reviews.json')
    return json.loads(p.read_text()) if p.exists() else {'figures':{}}


def reviewed_semantics(data, review):
    """A complete reviewed reading replaces inherited prose atomically.

    Partial reviews retain the existing explicit override contract. A full
    replacement must supply all reader-facing fields, so an omitted legacy
    explanation cannot silently survive beside a correction.
    """
    overrides = copy.deepcopy(review.get('semantics_overrides', {}))
    for key in ('hierarchy_zh', 'line_semantics_zh'):
        if key in review:
            overrides[key] = review[key]
    if review.get('semantics_mode') == 'replace':
        required = {'purpose_zh', 'reading_guide_zh', 'key_points_zh',
                    'hierarchy_zh', 'line_semantics_zh', 'misreadings_zh'}
        if missing := required - overrides.keys():
            raise ValueError(data['id'] + ': incomplete reviewed semantics: ' + ', '.join(sorted(missing)))
        return overrides, 'current-source-review-replacement', sorted(overrides)
    return {**data.get('semantics', {}), **overrides}, 'inherited-with-listed-current-overrides', sorted(overrides)


def portable_source_structure(diagram, *, current_path=None, current_sha256=None):
    """Project the active semantic record to the existing skills reference shape.

    Historical source payloads stay in the separately linked original figure
    record. They are never merged into this current, retrievable projection.
    """
    def local(value):
        return value.split('#', 1)[-1] if value else None
    a, source = diagram['analysis'], diagram['source']
    elements = []
    for node in diagram['nodes']:
        element = {k: copy.deepcopy(v) for k, v in node.items()
                   if k not in {'id', 'local_id', 'source_element', 'source_parent', 'source_position',
                                'group_parent', 'visual_parent', 'ancestors', 'children'}}
        element.update(id=node['local_id'], parent=local(node.get('group_parent')),
                       visual_parent=local(node.get('visual_parent')))
        elements.append(element)
    relationships = []
    for edge in diagram['edges']:
        item = {k: copy.deepcopy(v) for k, v in edge.items()
                if k not in {'id', 'from', 'to', 'predicate', 'source_relation', 'source_relation_index', 'visual'}}
        item.update(id=local(edge['id']), **{'from': local(edge['from']), 'to': local(edge['to'])},
                    type=edge['predicate'], explicit=edge['visual']['explicit_connection'],
                    visual={**edge['visual'], 'from': local(edge['visual']['from']), 'to': local(edge['visual']['to'])})
        relationships.append(item)
    return {
        'schema_version': '2.0', 'id': diagram['id'], 'title': diagram['title_zh'],
        'content_role': 'current-source-reviewed-reference-not-project-facts',
        'notice': '当前原图复核语义的便携投影；保留方向、端点基数、无标签线与视觉包含的区别。来源示例不是项目事实，历史解释单独定位。',
        'source_locator': {'pdf_path': source['pdf_path'], 'pdf_sha256': source['pdf_sha256'],
                           'pdf_pages': source['pdf_pages'], 'images': copy.deepcopy(source['images'])},
        'current_source': {'path': current_path or 'togaf-standard-10th-ai/architecture/diagrams/' + diagram['id'] + '.json',
                           'sha256': current_sha256, 'semantic_status': a['source_semantics_status']},
        'historical_source': {'path': 'togaf-standard-10th-ai/' + source['figure_record_path'],
                              'sha256': source['figure_record_sha256'], 'role': 'archived-interpretation-not-current-semantics'},
        'reading': {'purpose_zh': a['author_purpose_zh'], 'reading_guide_zh': a['reading_sequence_zh'],
                    'key_points_zh': copy.deepcopy(a['source_logic_zh']), 'hierarchy_zh': a['hierarchy_explanation_zh'],
                    'line_semantics_zh': a['line_explanation_zh'], 'misreadings_zh': copy.deepcopy(a['misreadings_zh'])},
        'elements': elements, 'relationships': relationships,
        'flows': copy.deepcopy(diagram['flows']), 'tables': copy.deepcopy(diagram['tables']),
        'legend': copy.deepcopy(diagram['legend']), 'uncertainty': copy.deepcopy(diagram['source_uncertainty']),
        'conflicts': copy.deepcopy(diagram['source_conflicts']),
        'detailed_observation': {'findings_zh': copy.deepcopy(a['current_findings_zh']),
                                 'status': diagram['quality']['visual_review']},
        'visual_structure_review': copy.deepcopy(diagram['current_visual_review']),
    }


def classify(data):
    if data.get('image_kind'):
        k=data['image_kind']
        if 'matrix' in k:return 'role-skill-matrix'
        if k=='likert-response-scale':return 'assessment-response-form'
        if 'legend' in k or 'notation' in k:return 'notation-or-legend'
        if k=='factor-label-in-adm-mapping-table':return 'architecture-phase-mapping'
        return 'architecture-context-symbol'
    types=data.get('classification',{}).get('diagram_types',[])
    if 'photo' in types:return 'illustrative-photo'
    if 'legend' in types:return 'notation-or-legend'
    if 'er_model' in types:return 'architecture-metamodel'
    if 'archimate' in types:return 'architecture-model'
    if 'causal_loop' in types:return 'causal-model'
    if any(t in types for t in ['matrix','table']):return 'mapping-or-assessment-matrix'
    if 'canvas' in types:return 'business-model-canvas'
    if 'hierarchy' in types:return 'decomposition-or-organization-model'
    if 'timeline' in types:return 'architecture-evolution-or-plan'
    node_types=Counter(e.get('type') for e in data.get('elements',[]))
    if node_types['application']+node_types['technology']>=3 and any(t in types for t in ['flow','network']):
        return 'system-or-data-reference-architecture'
    if 'flow' in types or 'cycle' in types:return 'process-or-method-model'
    if 'network' in types or 'layered' in types:return 'architecture-concept-or-system-model'
    return 'analytical-view'


def source_context(data, document, reviewed_pages=()):
    loc=data.get('figure',{}).get('en_location') or {}
    pns=list(dict.fromkeys(loc.get('pages', [data['pdf_page']] if 'pdf_page' in data else [])))
    targets=set(pns)|set(reviewed_pages)
    for e in data.get('semantics',{}).get('text_evidence',[]):
        m=re.search(r'en_pdf p(\d+)',e.get('source',''))
        if m: targets.add(int(m[1]))
    # Caption pages and explicitly cited evidence pages, without substituting a
    # bibliography or Chinese summary for original English evidence.
    evidence=[]
    figure_number=data.get('figure',{}).get('number')
    for n in sorted(targets):
        if not 1<=n<=len(document['pages']):continue
        page=document['pages'][n-1]
        blocks=[x for x in page['content'] if x['type'] not in ['table'] and len(x['text'])>70]
        if figure_number:
            relevant=[b for b in blocks if re.search(r'(?:Figure|Example|Table)\s+'+re.escape(figure_number)+r'\b',b['text'])]
        else:relevant=[]
        selected=relevant[:3] or [b for b in blocks if b['type']=='text'][:2]
        evidence.append({'id':f'pdf-p{n}', 'document_id':document['id'],'pdf_page':n,
                         'page_markdown':f'documents/{document["id"]}.md#page-{n}',
                         'quotes':[{'text':b['text'], 'source_block_ids':b.get('source_block_ids',[])} for b in selected],
                         'selection':'caption-reference-and-nearby-context' if relevant else 'same-page-context'})
    return pns,evidence


def transcriptions(data):
    ts=[e.get('transcription',{}) for e in data.get('source_extraction',[])]
    if data.get('transcription'):ts.append(data['transcription'])
    digital='\n'.join(t.get('digital_text','') for t in ts)
    ocr='\n'.join((t.get('ocr') or {}).get('text','') for t in ts)
    return digital,ocr


def label_match(label, digital, ocr):
    def key(s):return re.sub(r'[^a-z0-9]','',s.lower())
    k=key(label or '')
    if not k or len(k)<3:return 'not-tested-short-or-implicit-label'
    if k in key(digital):return 'digital-label-match'
    if k in key(ocr):return 'ocr-label-match'
    return 'not-found-in-machine-text'


def legacy_parent_semantics(fid, child, parent, data):
    """Classify the intended hierarchy without calling every parent a manager."""
    if child.get('hierarchy_kind'):
        return child['hierarchy_kind'], child.get('hierarchy_reason_zh') or '按当前原图审校显式区分分类、包含与其他层级语义。'
    ct,pt=child.get('type'),parent.get('type')
    position=norm(parent.get('position',''))
    if fid=='G190/fig4-1' or any(s in position for s in ['列标题','列头']):
        return 'classified_under','列标题用于分类；没有封闭容器，也不表示业务上下级。'
    if ct==pt=='organization_unit':
        return 'organization_partition','组织单元的组成/分区；此处不自动证明岗位直属汇报。'
    if ct==pt=='capability':
        return 'capability_decomposition','同类能力的包含分解；能力实例与能力类型另以实例化关系记录。'
    if ct==pt and ct in ['function','service','process']:
        return 'functional_decomposition','同类功能/过程/服务的嵌套分解；不推断执行顺序。'
    if pt=='value_stream' and ct=='value_stream_stage':
        return 'value_stream_decomposition','价值流包含阶段；具体先后另看sequence关系。'
    if ct==pt=='architecture':
        return 'architecture_scope_refinement','架构范围或细化关系；不等于人员汇报关系。'
    if pt=='application' and ct in ['data','process','application']:
        return 'application_encapsulation','应用组件包含其数据、行为或子组件。'
    if pt=='group':
        return 'visual_grouping','框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。'
    return 'visual_containment_only','保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。'


def predicate_for_relation(fid, r, i, review):
    s,t,k=r['from'],r['to'],r['type']
    label=norm(r.get('label_en')).lower()
    reason=None
    # No numbered source line is silently dropped. Corrections retain source_index.
    override=review.get('edge_overrides',{}).get(str(i))
    if override:
        return override.get('from',s),override.get('to',t),override.get('predicate',k),override.get('reason_zh'), 'current-source-review'
    if k=='reports_to' and not r['explicit']:
        return s,t,'organization_part_of','旧解释把隐式框嵌套/治理层次记为汇报；仅保留组成归属，不构造HR汇报线。','conservative-semantic-correction'
    if label=='instantiates':
        return s,t,'instantiates','实例化与子类型继承不同，按原文标签记录。','label-semantic-normalization'
    # These are unambiguous readings of the selected source relation's first label.
    # Ambiguous compound labels stay verbatim, not automatically inverted.
    if fid in ['G248/fig2-2','G248/fig2-3','G248/fig6-1','G249/fig4-2']:
        if label.startswith('implemented by'):
            return t,s,'implements','被动implemented by转为实现者→被实现对象；原图方向另外保存。','label-semantic-normalization'
        if label.startswith('performed by'):
            return t,s,'performs','performed by转为执行系统→服务。','label-semantic-normalization'
    if fid=='G248/fig3-1':
        if r.get('id') in ['r_goal_coa','r_capability_function','r_ldc_pdc','r_lac_pac','r_ltc_ptc']:
            return t,s,'realizes','Is realized by转为实现者→被实现对象。','label-semantic-normalization'
        if r.get('id')=='r_appservice_lac':
            return t,s,'implements','应用服务由逻辑应用组件实现。','label-semantic-normalization'
        if r.get('id') in ['r_data_lac','r_data_pac']:
            return t,s,'uses','数据实体Used by组件，故语义为组件使用数据。','label-semantic-normalization'
        if r.get('id') in ['r_appservice_techservice','r_lac_ltc','r_pac_ptc']:
            return t,s,'serving','Is served by转为提供服务者→使用者。','label-semantic-normalization'
    if label=='modifies':return s,t,'modifies',None,'source-label'
    return s,t,k,reason,'historical-interpretation'


def graph_components(node_ids, edges):
    adj={n:set() for n in node_ids}
    for e in edges:
        if e['from'] in adj and e['to'] in adj:
            adj[e['from']].add(e['to']);adj[e['to']].add(e['from'])
    unseen=set(node_ids); components=[]
    while unseen:
        start=min(unseen);todo=[start];unseen.remove(start);comp=[]
        while todo:
            n=todo.pop();comp.append(n)
            for nxt in sorted(adj[n]&unseen):unseen.remove(nxt);todo.append(nxt)
        components.append(sorted(comp))
    return components


def hierarchy_view(links):
    """Retain a directed hierarchy as a graph, including multiple parents/cycles."""
    parents=defaultdict(set);children=defaultdict(set);ids=set()
    for h in links:
        p,c=h['parent'],h['child'];ids.update([p,c])
        parents[c].add(p);children[p].add(c)
    roots=sorted(n for n in ids if not parents[n])
    depths={n:0 for n in roots};todo=deque(roots)
    while todo:
        p=todo.popleft()
        for c in sorted(children[p]):
            if c not in depths:
                depths[c]=depths[p]+1;todo.append(c)
    indegree={n:len(parents[n]) for n in ids};todo=deque(roots);ordered=[]
    while todo:
        p=todo.popleft();ordered.append(p)
        for c in sorted(children[p]):
            indegree[c]-=1
            if indegree[c]==0:todo.append(c)
    return {'links':links,'roots':roots,
      'nodes':[{'id':n,'parents':sorted(parents[n]),'children':sorted(children[n]),
                'shortest_root_depth':depths.get(n)} for n in sorted(ids)],
      'multiple_parent_nodes':sorted(n for n in ids if len(parents[n])>1),
      'cycle_or_cycle_dependent_nodes':sorted(ids-set(ordered)),
      'semantics_zh':'父项和子项按此视图的关系类型解释。多父项是有向图；最短根深度不等同统一业务等级。'}


def synthetic_embedded(data):
    """Materialize table semantics; an OCR string is not a role-skill graph."""
    f=copy.deepcopy(data);f.setdefault('elements',[]);f.setdefault('relationships',[])
    kind=f.get('image_kind')
    if kind=='skills-role-proficiency-matrix':
        for ti,table in enumerate(f.get('tables',[])):
            for ci,label in enumerate(table['columns'][1:],1):
                f['elements'].append({'id':f't{ti}-role-{ci}','type':'role','label_en':label,'label_zh':label,'parent':None})
            for ri,row in enumerate(table['rows']):
                skill=f't{ti}-skill-{ri+1}';f['elements'].append({'id':skill,'type':'skill','label_en':row[0],'label_zh':row[0],'parent':None})
                for ci,level in enumerate(row[1:],1):
                    f['relationships'].append({'from':f't{ti}-role-{ci}','to':skill,'type':'requires_skill','explicit':False,'line':'matrix-cell','arrow':'none',
                        'required_proficiency':level,'table_id':table['id'],'row':ri+1,'column':ci+1,'label_en':f'Level {level}',
                        'description_zh':f'该角色在该技能列要求等级{level}；这是能力要求，不是实际人员评级。'})
    elif kind=='factor-label-in-adm-mapping-table':
        label=', '.join(f.get('visible_labels',[]));phase=f.get('adm_phase')
        f['elements']=[{'id':'factor','type':'concept','label_en':label,'label_zh':label}]
        if phase:
            f['elements'].append({'id':'phase','type':'phase','label_en':phase,'label_zh':phase})
            f['relationships']=[{'from':'factor','to':'phase','type':'applies_in_phase','explicit':False,'line':'matrix-cell','arrow':'none',
                'description_zh':'依据表6-1实际所在行建立因素与阶段映射，不是流程箭头。'}]
    elif kind=='likert-response-scale':
        f['elements']=[{'id':f'option-{i+1}','type':'option','label_en':label,'label_zh':label,'order':i+1} for i,label in enumerate(f.get('ordered_options',[]))]
        f['relationships']=[{'from':f'option-{i+1}','to':f'option-{i+2}','type':'option_order','explicit':False,'line':'implicit','arrow':'none','description_zh':'问卷选项从左到右；没有受访者选择。'} for i in range(max(0,len(f['elements'])-1))]
    elif kind=='proficiency-level-legend':
        f['elements']=[{'id':f'level-{row[0]}','type':'level','label_en':f'{row[0]} {row[1]}','label_zh':str(row[2]),'description_zh':'熟练等级定义及颜色图例'} for row in f.get('tables',[{}])[0].get('rows',[])]
    else:
        label=f.get('notation_element_en') or f.get('context_label_en') or ' / '.join(f.get('visible_labels',[])) or f['id']
        f['elements']=[{'id':'symbol','type':'notation' if 'notation' in (kind or '') else 'concept','label_en':label,'label_zh':label,'description_zh':f.get('description_zh')}]
    f.setdefault('figure',{'title_en':f.get('notation_element_en') or f.get('image_kind'),'title_zh':f.get('description_zh'),
                          'en_location':{'pages':[f['pdf_page']]}})
    f.setdefault('classification',{'diagram_types':['matrix'] if 'matrix' in (kind or '') else ['legend'],'concepts':[]})
    f.setdefault('semantics',{'one_line_zh':f.get('description_zh'),'purpose_zh':f.get('description_zh')})
    return f


def analyse(data, document, input_path, root, output, reviews):
    fid=data['id'];code=fid.split('/')[0]
    original_data=data
    embedded='image_kind' in data
    if embedded:data=synthetic_embedded(data)
    review=reviews.get('figures',{}).get(fid,{})
    source_hash=data.get('provenance',{}).get('pdf_sha256')
    if review and review.get('source_pdf_sha256') != source_hash:
        raise ValueError(f'{fid}: source changed; manual review must be refreshed')
    if review:
        crops=data.get('source_extraction',[])
        recorded=[x['image_sha256'] for x in crops]
        actual=[sha(output/x['image_path']) for x in crops]
        if recorded!=actual or sorted(review.get('source_crop_sha256',[]))!=sorted(actual):
            raise ValueError(f'{fid}: reviewed crop changed; manual review must be refreshed')
    pages,evidence=source_context(data, document, review.get('inspected_pdf_pages',[]))
    digital,ocr=transcriptions(data)
    original_elements={e['id']:e for e in data.get('elements',[])}
    elements=copy.deepcopy(data.get('elements',[])+review.get('additional_nodes',[]))
    if len({e['id'] for e in elements})!=len(elements):raise ValueError(f'{fid}: duplicate original/added node ID')
    for e in elements:
        if e['id'] in review.get('node_overrides',{}):e.update(review['node_overrides'][e['id']])
    all_elements={e['id']:e for e in elements}
    rejected_nodes=[]
    for e in elements:
        if e.get('source_presence')!='rejected-not-in-source-figure':continue
        if e['id'] not in original_elements:raise ValueError(fid+': cannot reject an added node '+e['id'])
        if not e.get('rejection_reason_zh'):raise ValueError(fid+': rejected node needs reason '+e['id'])
        rejected_nodes.append({**e,'id':gid(fid,e['id']),'local_id':e['id'],
            'source_element':original_elements[e['id']],
            'semantic_state':'rejected-unobserved','evidence_refs':['source-interpretation','current-visual-review']})
    elements=[e for e in elements if e.get('source_presence')!='rejected-not-in-source-figure']
    byid={e['id']:e for e in elements}
    ids={gid(fid,e['id']) for e in elements}
    nodes=[];hierarchy=[]
    for e in elements:
        lid=e['id'];par=e.get('parent');seen=set();anc=[];cur=par
        while cur:
            if cur in seen or cur not in byid:raise ValueError(f'{fid}: invalid parent {cur}')
            seen.add(cur);anc.append(gid(fid,cur));cur=byid[cur].get('parent')
        parent_kind=parent_reason=None
        if par:
            parent_kind,parent_reason=legacy_parent_semantics(fid,e,byid[par],data)
            hierarchy.append({'id':gid(fid,'h-'+lid),'parent':gid(fid,par),'child':gid(fid,lid),
                'kind':parent_kind,'basis':'parent-field-plus-typed-semantic-analysis','reason_zh':parent_reason,
                'visual_enclosure_confirmed':False if parent_kind=='classified_under' else None,
                'evidence_refs':['source-interpretation']+(['current-visual-review'] if fid in reviews.get('figures',{}) else [])})
        nodes.append({**{key:value for key,value in e.items() if key not in {'id','parent'}},
            'id':gid(fid,lid),'local_id':lid,'label_en':e.get('label_en'),'label_zh':e.get('label_zh'),
            'type':e.get('type','other'),'meaning_zh':e.get('description_zh') or TYPE_ZH.get(e.get('type'),'图中元素')+'：'+str(e.get('label_zh') or e.get('label_en') or lid),
            'notation_type':e.get('notation_type'),'source_position':e.get('position'),'source_parent':original_elements.get(lid,{}).get('parent'),
            'visual_parent':gid(fid,par) if par and parent_kind!='classified_under' else None,
            'group_parent':gid(fid,par) if par else None,'hierarchy_kind':parent_kind,'depth':len(anc),'ancestors':list(reversed(anc)),
            'children':[gid(fid,x['id']) for x in elements if x.get('parent')==lid],
            'label_evidence':label_match(e.get('label_en'),digital,ocr),'source_element':original_elements.get(lid),
            'origin':'source-interpretation' if lid in original_elements else 'newly-transcribed-source-element',
            'evidence_refs':['source-interpretation'] if lid in original_elements else ['current-visual-review']})
    relations=[];corrections=[];rejected_edges=[]
    source_relations=data.get('relationships',[])
    for i,r in enumerate(source_relations+review.get('additional_edges',[])):
        added=i>=len(source_relations)
        s,t,k,reason,basis=predicate_for_relation(fid,r,i,review)
        if added:reason=r['description_zh'];basis='current-source-review'
        override=review.get('edge_overrides',{}).get(str(i),{})
        endpoints=all_elements if override.get('semantic_state')=='rejected-unobserved' else byid
        if s not in endpoints or t not in endpoints:raise ValueError(f'{fid}: bad endpoints {s} {t}')
        explicit=bool(r.get('explicit'))
        uncertain=any(x in norm(r.get('description_zh')) for x in ['推断','推测','不确定','可能','无法'])
        visual={'explicit_connection':explicit,'line_style':r.get('line'),'arrow':r.get('arrow'),
                'from':gid(fid,r['from']),'to':gid(fid,r['to']), 'direction_is_semantic_not_pixel_geometry':True}
        override=review.get('edge_overrides',{}).get(str(i),{})
        for key,value in override.get('visual',{}).items():
            visual[key]=gid(fid,value) if key in ['from','to'] else value
        for key,target in [('visual_arrow','arrow'),('visual_line_style','line_style'),('visual_explicit_connection','explicit_connection')]:
            if key in override:visual[target]=override[key]
        for key in ['from','to']:
            if 'visual_'+key in override:visual[key]=gid(fid,override['visual_'+key])
        label_en=override.get('label_en',r.get('label_en'))
        direction=override.get('direction') or ('bidirectional' if visual.get('arrow')=='both' else 'undirected' if k in ['association','equivalence','contrast','maps_to'] and visual.get('arrow')=='none' and not label_en else 'subject-to-object')
        if basis=='current-source-review':status='source-reviewed-correction'
        elif embedded and data.get('current_visual_review'):status='source-table-or-symbol-transcription'
        elif uncertain:status='historical-inference-requires-confirmation'
        elif not explicit:status='implicit-interpreted-relation'
        else:status='explicit-connection-historical-meaning'
        edge={'id':gid(fid,f'r{i+1:04}'),'source_relation_index':None if added else i,'source_relation_id':r.get('id'),
            'from':gid(fid,s),'to':gid(fid,t),'predicate':k,'predicate_zh':REL_ZH.get(k,k),
            'direction':direction,'label_en':label_en,'label_zh':override.get('label_zh',r.get('label_zh')),
            'description_zh':reason or r.get('description_zh') or REL_ZH.get(k,k),
            'visual':visual,'semantic_basis':basis,'status':status,'cardinality':override.get('cardinality',r.get('cardinality')),
            'polarity':override.get('polarity',r.get('polarity')),'required_proficiency':r.get('required_proficiency'),
            'source_relation':None if added else r,'evidence_refs':(['current-visual-review'] if added else ['source-interpretation']+(['current-visual-review'] if basis=='current-source-review' else []))}
        if override.get('scope_qualifier'):edge['scope_qualifier']=override['scope_qualifier']
        if override.get('source_statement'):edge['source_statement']=override['source_statement']
        for key in ['endpoint_cardinalities','source_conflict','semantic_interpretation','uncertainty']:
            if key in override:edge[key]=override[key]
            elif added and key in r:edge[key]=r[key]
        if override.get('semantic_state')=='rejected-unobserved':
            edge['semantic_state']='rejected-unobserved'
            edge['rejection_reason_zh']=override.get('reason_zh','本次原图复核未观察到该历史关系。')
            rejected_edges.append(edge)
            corrections.append({'edge_id':edge['id'],'old_type':r['type'],'new_predicate':None,'reason_zh':edge['rejection_reason_zh']})
            continue
        if added:edge['origin']='newly-transcribed-source-connection'
        if k=='reports_to':
            edge['reporting_scope']=byid[s].get('type','other')+'-to-'+byid[t].get('type','other')
            edge['reporting_scope_notice_zh']='该边的主体/客体类型决定是岗位汇报还是组织单元归属，不据此构造实际员工名册。'
        if embedded and r.get('table_id'):edge['table_cell']={k:r[k] for k in ['table_id','row','column']}
        if reason:corrections.append({'edge_id':edge['id'],'old_type':None if added else r['type'],'new_predicate':k,'reason_zh':reason})
        relations.append(edge)
    # Separate kind-specific hierarchies. Includes relation-based composition that
    # has no visual enclosure, and preserves organizational/reporting semantics.
    semantic_hierarchy=[];reporting=[];governance=[];instance=[]
    for edge in relations:
        k=edge['predicate']
        if k in ['composition','aggregation','encapsulates']:
            semantic_hierarchy.append({'id':edge['id'],'parent':edge['from'],'child':edge['to'],'kind':k,
               'basis':'relation-semantics-not-visual-containment','status':edge['status']})
        elif k=='specialization':
            semantic_hierarchy.append({'id':edge['id'],'parent':edge['to'],'child':edge['from'],'kind':'type_specialization','status':edge['status']})
        elif k=='organization_part_of':
            semantic_hierarchy.append({'id':edge['id'],'parent':edge['to'],'child':edge['from'],'kind':'organization_partition','status':edge['status']})
        elif k=='reports_to':reporting.append(edge['id'])
        elif k in ['governs','governance_scope']:governance.append(edge['id'])
        elif k=='instantiates':instance.append(edge['id'])
    adjacency=[{'from':e['from'],'to':e['to']} for e in relations]+[{'from':h['parent'],'to':h['child']} for h in hierarchy]
    comps=graph_components(ids,adjacency)
    degrees=Counter(x for e in relations for x in (e['from'],e['to']))
    node_map={n['id']:n for n in nodes}
    for n in nodes:
        n['incoming_relations']=[r['id'] for r in relations if r['to']==n['id']]
        n['outgoing_relations']=[r['id'] for r in relations if r['from']==n['id']]
        n['participating_relation_count']=degrees[n['id']]
    roles=[n['id'] for n in nodes if n['type'] in ['role','actor','stakeholder']]
    stats={'nodes':len(nodes),'source_relations':len(relations),'containment_or_grouping':len(hierarchy),
      'relation_types':dict(sorted(Counter(e['predicate'] for e in relations).items())),
      'node_types':dict(sorted(Counter(n['type'] for n in nodes).items())),
      'implicit_relations':sum(not r['visual']['explicit_connection'] for r in relations),
      'explicit_connections':sum(r['visual']['explicit_connection'] for r in relations),'reporting_relations':len(reporting),
      'reporting_subject_types':dict(sorted(Counter(node_map[r['from']]['type'] for r in relations if r['predicate']=='reports_to').items())),
      'governance_relations':len(governance),'instantiation_relations':len(instance),
      'max_group_depth':max((n['depth'] for n in nodes),default=0),'components':len(comps),
      'isolated_nodes':[c[0] for c in comps if len(c)==1], 'table_records':len(review.get('tables_override',data.get('tables',[]))),
      'corrections':len(corrections),'role_nodes':len(roles),'rejected_historical_relations':len(rejected_edges)}
    sem, semantics_status, overridden_fields = reviewed_semantics(data, review)
    observations=[f'本图有 {len(nodes)} 个具名或隐含元素、{len(relations)} 条关系和 {len(hierarchy)} 条包含/分组记录。']
    if hierarchy:observations.append(f'包含/分组树最大深度为 {stats["max_group_depth"]}；根节点为 '+ '、'.join(str(n['label_zh'] or n['label_en'] or n['local_id']) for n in nodes if not n['group_parent'])+'。')
    if reporting:observations.append(f'保留来源解释中的 {len(reporting)} 条汇报/组织归属关系，其主体类型为 {stats["reporting_subject_types"]}；组织单元不是具体员工，来源示例不能变成项目现行人事结构。')
    elif nodes:observations.append('本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。')
    if governance:observations.append('治理边回答谁提供约束、指导或监督；它们与岗位汇报边分别存储。')
    if instance:observations.append('能力实例→能力类型以 instantiates 记录，避免把特定实现当作子能力或继承子类。')
    if not relations and hierarchy:observations.append('原图靠嵌套表达结构，没有连线；新语义图将包含单独显式化，不补造流程、数据流或依赖。')
    if len(comps)>1:observations.append(f'包含分组后有 {len(comps)} 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。')
    applications=application_analysis(classify(data),stats,sem)
    source_imgs=[]
    for e in data.get('source_extraction',[]):
        source_imgs.append({k:e.get(k) for k in ['image_path','image_sha256','pdf_page','bbox_pdf_points','region_source']})
    if embedded:source_imgs=[{'image_path':data['image_path'],'image_sha256':data['image_sha256'],'pdf_page':data['pdf_page'],'bbox_pdf_points':data['bbox_pdf_points'],'region_source':'original-embedded-image-region'}]
    family_links={
      'visual_or_classification':hierarchy,
      'semantic_composition':semantic_hierarchy,
      'organizational_reporting':[{'id':e['id'],'parent':e['to'],'child':e['from'],'kind':'reports_to','status':e['status']} for e in relations if e['id'] in reporting],
      'governance_scope':[{'id':e['id'],'parent':e['from'],'child':e['to'],'kind':e['predicate'],'status':e['status']} for e in relations if e['id'] in governance],
      'type_and_instance':[{'id':e['id'],'parent':e['to'],'child':e['from'],'kind':'instantiates','status':e['status']} for e in relations if e['id'] in instance]}
    evidence.append({'id':'source-interpretation','kind':'inherited-interpretation-and-transcription',
      'record_path':str(input_path.relative_to(output)),'record_sha256':sha(input_path),
      'notice_zh':'既有解释加原文图像与转录。其历史语义不等于本轮视觉复核。'})
    if review:
        evidence.append({'id':'current-visual-review','kind':'selected-source-visual-review',
          'review_path':os.path.relpath(Path(__file__).with_name('architecture-diagram-reviews.json'),output),
          'review_record_id':fid,'scope':review['scope'],'pdf_sha256':source_hash,
          'crop_sha256':review['source_crop_sha256']})
    title=data.get('figure',{}).get('title_zh') or data.get('figure',{}).get('title_en') or fid
    result={'schema_version':VERSION,'id':fid,'document_id':code,'content_role':'derived-architecture-analysis',
       'title_zh':title,'title_en':data.get('figure',{}).get('title_en'),'category':classify(data),
       'diagram_types':data.get('classification',{}).get('diagram_types',[]),
       'concepts':data.get('classification',{}).get('concepts',[]),
       'source':{'pdf_path':data['provenance']['pdf_path'],'pdf_sha256':source_hash,'pdf_pages':pages,
           'figure_record_path':str(input_path.relative_to(output)), 'figure_record_sha256':sha(input_path),
           'source_role':data['provenance'].get('source_role','original-embedded-image'), 'images':source_imgs},
       'nodes':nodes,'edges':relations,'rejected_nodes':rejected_nodes,'rejected_edges':rejected_edges,'hierarchy':{'containment_and_grouping':hierarchy,'semantic_hierarchy':semantic_hierarchy,
           'organizational_reporting_edge_ids':reporting,'governance_edge_ids':governance,'instantiation_edge_ids':instance,
           'views':{k:hierarchy_view(v) for k,v in family_links.items()}},
       'role_node_ids':roles,'flows':review.get('flows_override',data.get('flows',[])),
       'source_flows':data.get('flows',[]),
       'source_flows_role':'archived-inherited-interpretation-see-current-flows',
       'tables':review.get('tables_override',data.get('tables',[])),
       'source_tables':data.get('tables',[]),
       'source_tables_role':'archived-source-symbol-transcription' if embedded else 'archived-inherited-transcription-see-current-tables',
       'legend':review.get('legend_override',data.get('legend',[])),
       'source_legend':data.get('legend',[]),
       'source_legend_role':'archived-source-symbol-transcription' if embedded else 'archived-inherited-interpretation-see-current-legend',
       'analysis':{'author_purpose_zh':sem.get('purpose_zh') or sem.get('one_line_zh'),
           'reading_sequence_zh':sem.get('reading_guide_zh'), 'source_logic_zh':sem.get('key_points_zh',[]),
           'structure_findings_zh':observations,'application_zh':applications,
           'hierarchy_explanation_zh':review.get('hierarchy_zh') or sem.get('hierarchy_zh'),
           'line_explanation_zh':review.get('line_semantics_zh') or sem.get('line_semantics_zh'),
           'misreadings_zh':sem.get('misreadings_zh',[])+review.get('misreadings_zh',[]),
           'current_findings_zh':review.get('findings_zh',[]), 'strongly_connected_note':'Cycles in process/feedback views are not automatically errors.',
           'source_semantics_status':semantics_status,
           'overridden_legacy_fields':overridden_fields,
           'components':comps, 'structural_hubs':[{'node_id':n,'incident_relation_count':c} for n,c in degrees.most_common(8)]},
       'evidence':evidence,'current_visual_review':review or None,'corrections':corrections,
       'source_uncertainty':review.get('uncertainty_override',data.get('quality')),
       'previous_source_semantics':data.get('semantics',{}),
       'previous_source_uncertainty':data.get('quality'),
       'source_conflicts':data.get('known_conflicts',[])+sem.get('source_conflicts',[]),
       'source_visual_transcription':data.get('current_visual_review') if embedded else None,
       'statistics':stats,'quality':{'graph_integrity':'checked','semantic_analysis':'typed-graph-and-context-analysis',
          'visual_review':('source-content-audited' if review.get('review_status')=='source-content-audited' else
                           'selected-facts-reviewed' if review else
                           'source-symbol-or-table-transcribed' if embedded and data.get('current_visual_review') else
                           'inherited-source-interpretation-with-new-normalization'),
          'notice_zh':'所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。'}}
    return result


def application_analysis(category,stats,sem):
    actions={
     'architecture-metamodel':['使用本图的实体类型作为建模词表，建立本地实体ID，再分别填入关系端点与证据。','核对主动/被动关系的语义方向和基数；实现、使能、使用、包含及实例化分别建模。'],
     'role-skill-matrix':['从角色出发读取全部技能及要求等级，以原等级定义评估具体人员的证据。','矩阵是要求，不是实测人员能力；不能把等级直接相加生成未定义的总分。'],
     'mapping-or-assessment-matrix':['先固定行、列所代表的维度及单元格含义，再登记有证据的映射或评分。','空白、无关系、未测量和不适用分别处理；颜色不自动等于优先级。'],
     'decomposition-or-organization-model':['按父项展开所有直接子项，检查同层粒度、重叠和缺项。','保留组成、分类、能力分解与组织汇报的区别；将示例名称替换为已确认的项目对象。'],
     'architecture-evolution-or-plan':['为每个演进状态/工作包登记前置条件、交付物、依赖和实际决策人。','时间轴表达计划顺序；架构范围、已批准计划和资源承诺须另有项目证据。'],
     'process-or-method-model':['按阶段/事件/行为关系读取入口、出口、责任和产物；检查循环与例外路径。','工作流先后不表示组织管理权；在项目中显式记录条件和完成标准。'],
     'system-or-data-reference-architecture':['先划定平台边界，登记应用、存储、数据来源及消费者，再逐条读取输入/输出流。','区分基线、过渡与目标架构，以及现有、保留与新增对象；范围包含不自动表示组件实现或组织管理。'],
     'architecture-model':['按节点类型建立业务、应用、数据、技术对象，并保留跨层服务、访问和实现关系。','交叉线不是连接点；角色分工、数据使用和组织汇报不得混用。'],
     'causal-model':['把因果方向、正负极性和回路分别录入模型，并记录来源适用范围。','示意因果关系没有自动提供数量、延迟或统计因果证明。'],
     'business-model-canvas':['先明确受益方和价值主张，再把各画布要素关联到能力、价值流及所需资源。','画布用于假设和共同理解；不能替代细化的实现架构或已验证经营数据。'],
     'assessment-response-form':['保留问题、等级顺序及用户真实选择，当前空白表单没有问卷结果。','不把图中选项顺序当成架构上下级，也不自造聚合阈值。'],
     'architecture-phase-mapping':['把因素与所在ADM阶段绑定，读取同一表格行中的活动说明。','单个标签来自表格上下文，不是完整阶段输入/输出合同。'],
     'notation-or-legend':['先用图例解释记法与颜色，再读取使用该符号的图。','记法符号是类型说明，不是实际项目实体。'],
    }
    result=actions.get(category,['围绕作者目的读取本图实体、分组与连线，并用对应原文限定其含义。','把参考模型与项目事实分开，实际范围、约束、值和责任须有项目证据。'])
    return result


def mermaid(data, mode='all'):
    ids={n['id']:f'n{i}' for i,n in enumerate(data['nodes'])}
    lines=['flowchart TB','  %% Semantic reconstruction; see original source image for exact layout.']
    for n in data['nodes']:
        label=safe_label(n['label_en'] or n['label_zh'] or n['local_id'])
        lines.append(f'  {ids[n["id"]]}["{label}"]')
    if mode in ['all','relations']:
        for edge in data['edges']:
            a,b=ids[edge['from']],ids[edge['to']]
            suffix=(f' L{edge["required_proficiency"]}' if edge.get('required_proficiency') is not None else '')
            if edge.get('polarity') is not None:suffix+=' ('+str(edge['polarity'])+')'
            if edge.get('source_conflict'):suffix+=' [图文冲突]'
            label=safe_label(edge['predicate_zh']+suffix)
            op='<-->' if edge['direction']=='bidirectional' else '---' if edge['direction']=='undirected' else '-->'
            if not edge['visual']['explicit_connection']:op='-.->' if op=='-->' else '-.-'
            lines.append(f'  {a} {op}|"{label}"| {b}')
    if mode in ['all','hierarchy']:
        for h in data['hierarchy']['containment_and_grouping']:
            label=safe_label('分组' if h['kind'] in ['visual_grouping','classified_under'] else h['kind'])
            lines.append(f'  {ids[h["parent"]]} -.->|"{label}"| {ids[h["child"]]}')
    if mode=='hierarchy':
        family_labels={'semantic_composition':'语义组成','organizational_reporting':'汇报归属',
                       'governance_scope':'治理范围','type_and_instance':'类型→实例'}
        for family,label in family_labels.items():
            for h in data['hierarchy']['views'][family]['links']:
                lines.append(f'  {ids[h["parent"]]} -->|"{safe_label(label+": "+h["kind"])}"| {ids[h["child"]]}')
    return '\n'.join(lines)+'\n'


def markdown(data, output):
    fid=data['id'];base=Path('architecture/diagrams')/fid
    links=lambda target:os.path.relpath(target,base.parent)
    a=data['analysis'];nodes={n['id']:n for n in data['nodes']+data.get('rejected_nodes',[])}
    label=lambda n:nodes[n].get('label_zh') or nodes[n].get('label_en') or nodes[n]['local_id']
    cell=lambda s:norm(s).replace('|','\\|')
    text=[f'# {fid} · {data["title_zh"]}', '',f'类型：`{data["category"]}`。{a.get("author_purpose_zh") or ""}', '',
      f'英文 PDF 物理页：{data["source"]["pdf_pages"]}。本页为架构语义分析，原文与原图分别保留。','',
      '## 原图与可编辑图','']
    for image in data['source']['images']:
        text += [f'![PDF 第 {image["pdf_page"]} 页原图]({links(image["image_path"])})','']
    key=fid.split('/')[1]
    text += [f'[完整 JSON]({key}.json) · [可编辑 Mermaid]({key}.mmd) · [仅关系图]({key}.relations.mmd) · [层级分解图]({key}.hierarchy.mmd)','',
      '图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。','',
      '```mermaid',mermaid(data).rstrip(),'```','','## 架构分析','']
    if a.get('reading_sequence_zh'):text += [a['reading_sequence_zh'],'']
    for item in a['structure_findings_zh']+a['current_findings_zh']:text += ['- '+item]
    text += ['','### 如何用于项目','']+['- '+x for x in a['application_zh']]
    if a.get('source_logic_zh'):text += ['','### 结构所表达的逻辑','']+['- '+x for x in a['source_logic_zh']]
    text += ['','## 上下级与包含','',a.get('hierarchy_explanation_zh') or '本图没有另行明确的层级说明。','',
      '|父项|子项|层级类型|依据与解释|','|---|---|---|---|']
    for h in data['hierarchy']['containment_and_grouping']:
        text.append('|'+ '|'.join(cell(x) for x in [label(h['parent']),label(h['child']),h['kind'],h['reason_zh']])+'|')
    if not data['hierarchy']['containment_and_grouping']:text.append('|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|')
    for family,title in [('semantic_composition','业务组成与特化'),('organizational_reporting','明确汇报关系'),('governance_scope','治理范围'),('type_and_instance','类型与实例')]:
        view=data['hierarchy']['views'][family]
        if not view['links']:continue
        text+=['','### '+title,'','|父项/范围/类型|子项/责任对象/实例|语义|','|---|---|---|']
        for h in view['links']:text.append('|'+ '|'.join(cell(x) for x in [label(h['parent']),label(h['child']),h['kind']])+'|')
        if view['multiple_parent_nodes']:text+=['','存在多个父项的节点：'+ '、'.join(label(n) for n in view['multiple_parent_nodes'])+'；保留多重关系，不强行转成单父项树。']
        if view['cycle_or_cycle_dependent_nodes']:text+=['','此层级含循环或依赖循环的节点，应结合关系类型与源图核查：'+ '、'.join(label(n) for n in view['cycle_or_cycle_dependent_nodes'])+'。']
    text += ['','## 全部元素与角色','', '|元素ID|原文名称|类型|含义|直接父项|深度|','|---|---|---|---|---|---|']
    for n in data['nodes']:
        text.append('|'+ '|'.join(cell(x) for x in [n['local_id'],n['label_en'] or n['label_zh'],n['type'],n['meaning_zh'],label(n['group_parent']) if n['group_parent'] else '—',n['depth']])+'|')
    for n in data['nodes']:
        if n.get('attributes'):
            text+=['', '### '+label(n['id'])+'：属性', '', '```json',
                   json.dumps(n['attributes'],ensure_ascii=False,indent=2),'```']
    text += ['','## 全部关系','',a.get('line_explanation_zh') or '', '', '|主体|语义关系|客体|显式线/隐式|原文标签|依据|','|---|---|---|---|---|---|']
    for edge in data['edges']:
        text.append('|'+ '|'.join(cell(x) for x in [label(edge['from']),edge['predicate_zh'],label(edge['to']),
           '显式连线' if edge['visual']['explicit_connection'] else edge['visual']['line_style'],edge['label_en'] or '',edge['description_zh']])+'|')
    constrained=[e for e in data['edges'] if any(e.get(k) is not None for k in ['polarity','cardinality','endpoint_cardinalities','source_conflict'])]
    if constrained:
        text+=['','### 极性、基数与图文冲突','','数值和符号按原图记录；业务解释与原图冲突时分别保存，不静默修正原文。','',
               '|关系ID|极性|基数/端点标记|冲突说明|','|---|---|---|---|']
        for e in constrained:
            text.append('|'+ '|'.join(cell(x) for x in [e['id'],e.get('polarity'),
                json.dumps(e.get('endpoint_cardinalities',e.get('cardinality')),ensure_ascii=False),
                json.dumps(e.get('source_conflict'),ensure_ascii=False) if e.get('source_conflict') else ''])+'|')
    if data.get('rejected_nodes'):
        text+=['','## 本轮否定的历史元素','','源图未出现的旧元素保留供追溯，不进入当前节点、关系或层级。','',
               '|旧元素|旧标签|否定依据|','|---|---|---|']
        for n in data['rejected_nodes']:
            text.append('|'+ '|'.join(cell(x) for x in [n['local_id'],n.get('label_en') or n.get('label_zh'),n['rejection_reason_zh']])+'|')
    if data.get('rejected_edges'):
        text += ['','## 本轮否定的历史关系','',
                 '以下旧解释保留用于追溯，不进入当前关系图、层级或知识图谱的有效边。','',
                 '|旧记录|主体|旧关系|客体|否定依据|','|---|---|---|---|---|']
        for edge in data['rejected_edges']:
            text.append('|'+ '|'.join(cell(x) for x in [edge['source_relation_index'],label(edge['from']),edge['source_relation'].get('type'),label(edge['to']),edge['rejection_reason_zh']])+'|')
    for table in data['tables']:
        text += ['','## '+(table.get('title_zh') or table.get('id') or '转录表格'),'','```json',json.dumps(table,ensure_ascii=False,indent=2),'```']
    if data['corrections']:
        text+=['','## 本轮语义修正','']+['- '+x['reason_zh'] for x in data['corrections']]
    if a['misreadings_zh']:text+=['','## 误读检查','']+['- '+x for x in a['misreadings_zh']]
    text+=['','## 原文证据','']
    for e in data['evidence']:
        if 'pdf_page' not in e:continue
        text += [f'### [PDF 第 {e["pdf_page"]} 页]({links(e["page_markdown"])})','']
        text += ['> '+q['text'].replace('\n',' ') for q in e['quotes']]
    text+=['','## 来源与分析状态','',data['quality']['notice_zh'],'',f'源 PDF SHA-256：`{data["source"]["pdf_sha256"]}`。', '',
           f'源图记录：[原始解释与转录]({links(data["source"]["figure_record_path"])})。', '',
           '```json',json.dumps({'quality':data['quality'],'source_uncertainty':data['source_uncertainty'],'source_conflicts':data['source_conflicts']},ensure_ascii=False,indent=2),'```','']
    return '\n'.join(text)


def build(root=ROOT, output=None):
    root=Path(root).resolve();output=Path(output or root/'togaf-standard-10th-ai').resolve()
    oldindex=json.loads((output/'figures/index.json').read_text());reviews=load_reviews(root)
    records=[];excluded=[]
    entries=list(oldindex['figures'])
    for e in oldindex['embedded_images']:
        if not e.get('json_path'):continue
        data=json.loads((output/e['json_path']).read_text())
        if data.get('image_kind') in DECORATIVE:
            excluded.append({'id':e['id'],'reason':'decorative-or-editorial-callout','image_kind':data['image_kind'],'source_record':e['json_path']})
        else:entries.append(e)
    docs={}
    for entry in entries:
        path=output/entry['json_path'];data=json.loads(path.read_text());code=entry['document_id']
        if code not in docs:docs[code]=json.loads((output/f'documents/{code}.json').read_text())
        result=analyse(data,docs[code],path,root,output,reviews)
        base=output/'architecture/diagrams'/result['id'];dump(base.with_suffix('.json'),result)
        base.with_suffix('.md').write_text(markdown(result,output),encoding='utf-8')
        for mode,suffix in [('all','.mmd'),('relations','.relations.mmd'),('hierarchy','.hierarchy.mmd')]:
            base.with_suffix(suffix).write_text(mermaid(result,mode),encoding='utf-8')
        records.append({'id':result['id'],'document_id':code,'title_zh':result['title_zh'],'category':result['category'],
          'json_path':str(base.with_suffix('.json').relative_to(output)),'markdown_path':str(base.with_suffix('.md').relative_to(output)),
          'mermaid_path':str(base.with_suffix('.mmd').relative_to(output)),'source_images':result['source']['images'],
          'pdf_pages':result['source']['pdf_pages'],'statistics':result['statistics'],'quality':result['quality']})
    counts={'diagrams':len(records),'source_logical_figures':len(oldindex['figures']),
      'supplementary_non_decorative_images':len(records)-len(oldindex['figures']),'decorative_images_disposed':len(excluded),
      'nodes':sum(r['statistics']['nodes'] for r in records),'relations':sum(r['statistics']['source_relations'] for r in records),
      'hierarchy_links':sum(r['statistics']['containment_or_grouping'] for r in records),
      'reviewed_figures':sum(r['quality']['visual_review'] in {'selected-facts-reviewed','source-content-audited'} for r in records),
      'content_audited_figures':sum(r['quality']['visual_review']=='source-content-audited' for r in records),
      'source_transcribed_embedded_images':sum(r['quality']['visual_review']=='source-symbol-or-table-transcribed' for r in records),
      'corrected_or_normalized_relations':sum(r['statistics']['corrections'] for r in records)}
    index={'schema_version':VERSION,'content_role':'derived-architecture-analysis','counts':counts,'diagrams':records,
      'excluded_decorative_images':excluded,'scope_zh':'243条既有逻辑图逐条分析，并补充独立非装饰图片；原文图242、中文编者图1分别保留。',
      'source_index_sha256':sha(output/'figures/index.json'),'pipeline_sha256':sha(Path(__file__)),
      'review_data_sha256':sha(Path(__file__).with_name('architecture-diagram-reviews.json'))}
    dump(output/'architecture/diagrams/index.json',index)
    lines=['# 架构图、关系与上下级分析','',index['scope_zh'],'','原图、完整节点关系、Mermaid及语义分析按图关联。所有节点保留，包含/分组、业务关系、组织汇报和治理范围分别记录。','',
      '```json',json.dumps(counts,ensure_ascii=False,indent=2),'```','','[可浏览原图目录](gallery.html) · [机器索引](index.json)','','|图|类型|元素|关系|包含/分组|PDF页|','|---|---|---:|---:|---:|---|']
    for r in records:
        s=r['statistics'];lines.append(f'|[{r["id"]} · {cell_title(r["title_zh"])}]({r["id"]}.md)|{r["category"]}|{s["nodes"]}|{s["source_relations"]}|{s["containment_or_grouping"]}|{r["pdf_pages"]}|')
    lines += ['','## 关系读取规则','','1. `nodes` 保存所有实体；`edges` 保存所有原始关系与本轮规范化后的方向。',
      '2. `hierarchy.containment_and_grouping` 是图中的包含或分组；业务组成在 `semantic_hierarchy`。',
      '3. `organizational_reporting_edge_ids` 只保存有明确汇报语义的边；`governance_edge_ids` 表示治理职责。',
      '4. `instantiation_edge_ids` 表示类型与实例，不等同子类型分解。',
      '5. `source_relation` 保留原字段，`corrections` 解释修改；不确定性沿用并显示，不凭空补齐。',
      '6. `hierarchy.views` 为五种层级分别计算根、直接父子、最短根深度、多父项及循环状态。',
      '7. 原图和可编辑语义图均保留；语义图的重排位置本身没有业务意义。','']
    (output/'architecture/diagrams/index.md').write_text('\n'.join(lines),encoding='utf-8')
    (output/'architecture/diagrams/gallery.html').write_text(gallery(index),encoding='utf-8')
    return index


def cell_title(s):return norm(s).replace('|','\\|')


def gallery(index):
    cards=[]
    for d in index['diagrams']:
        im=d['source_images'][0] if d['source_images'] else None
        image='<img loading="lazy" src="'+html.escape('../../'+im['image_path'],quote=True)+'" alt="原文图">' if im else '<div class="empty">中文编者图：原文没有对应插图</div>'
        title=html.escape(d['title_zh']);fid=html.escape(d['id']);key=html.escape((d['id']+' '+d['title_zh']+' '+d['category']).lower(),quote=True)
        cards.append(f'<article data-search="{key}"><a href="{fid}.md">{image}</a><h2>{fid} · {title}</h2><p>{html.escape(d["category"])} · {d["statistics"]["nodes"]} 实体 · {d["statistics"]["source_relations"]} 关系 · {d["statistics"]["containment_or_grouping"]} 包含/分组</p><p><a href="{fid}.md">架构分析</a> · <a href="{fid}.json">完整JSON</a> · <a href="{fid}.mmd">可编辑图</a></p></article>')
    return '''<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>架构图与语义分析</title><style>body{font:15px/1.6 system-ui;margin:32px;background:#f4f7fa;color:#172638}header{max-width:1000px;margin:auto auto 28px}input{padding:12px;width:min(90%,700px);font:inherit;border:1px solid #8ca0b2;border-radius:8px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(350px,1fr));gap:20px}article{background:white;padding:18px;border:1px solid #d2dee8;border-radius:12px}img{width:100%;height:270px;object-fit:contain;background:white}h2{font-size:17px}a{color:#075f9e}.empty{height:270px;display:grid;place-items:center;background:#eaf0f5}[hidden]{display:none!important}</style><header><h1>架构图、关系与上下级分析</h1><p>原图与语义图按来源逐张关联。搜索图号、主题或图类型；包含、管理、使能和流程关系分别解释。</p><input id="q" placeholder="例如 G249、业务能力、元数据、architecture-metamodel"><p id="count"></p></header><main>'''+''.join(cards)+'''</main><script>const q=document.getElementById('q'),cards=[...document.querySelectorAll('article')];function filter(){let n=0;for(const c of cards){c.hidden=!c.dataset.search.includes(q.value.toLowerCase());if(!c.hidden)n++;}document.getElementById('count').textContent=n+' / '+cards.length+' 条图形分析';}q.addEventListener('input',filter);filter();</script></html>'''


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'togaf-standard-10th-ai');a=p.parse_args()
    print(json.dumps(build(ROOT,a.output)['counts'],ensure_ascii=False,indent=2))

if __name__=='__main__':main()
