#!/usr/bin/env python3
"""Build and connect the architectural meaning layer, graph, and retrieval corpus."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import os
import tempfile

ROOT=Path(__file__).resolve().parents[2]


def read(path):return json.loads(path.read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    # Preserve the source converter's escaping of lone UTF-16 code units.
    # Encode before opening and replace atomically so a failed write cannot
    # truncate an already published document.
    payload=(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode('utf-8',errors='backslashreplace')
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent,prefix='.'+path.name+'.',suffix='.tmp',delete=False) as handle:
            temporary=Path(handle.name);handle.write(payload)
        os.replace(temporary,path)
    finally:
        if temporary is not None and temporary.exists():temporary.unlink()
def serialize(obj):return json.dumps(obj,ensure_ascii=False,indent=2)


def pieces(text,limit=6000):
    while len(text)>limit:
        cut=text.rfind('\n',0,limit)
        if cut<limit//2:cut=limit
        else:cut+=1
        yield text[:cut];text=text[cut:]
    if text:yield text


def compact(obj):
    """Exclude preserved legacy payloads from current semantic retrieval."""
    if isinstance(obj,dict):
        return {k:compact(v) for k,v in obj.items() if k not in
                {'source_element','source_relation','source_flows','source_tables','source_legend','digital_words','source_material','source_position',
                 'cell_bboxes','row_values_original','source_sha256','source_path','source_json_path',
                 'source_markdown_path','markdown_path','context_en','figure_record_sha256',
                 'pdf_sha256','image_sha256','source_crop_sha256','source_pdf_sha256',
                 'maintenance_sha256','maintenance_source'}
                and not k.startswith('previous_')}
    if isinstance(obj,list):return [compact(v) for v in obj]
    return obj


def evidences(value):
    found={}
    def walk(x):
        if isinstance(x,dict):
            if x.get('document_id') and isinstance(x.get('pdf_page'),int):
                key=(x['document_id'],x['pdf_page'],x.get('quote_en',''))
                found[key]=x
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(value)
    return list(found.values())


def connect_diagram_reading_paths(output, diagrams):
    """Make current image meaning reachable when reading the original document."""
    byid={d['id']:d for d in diagrams}
    records=[]
    for d in diagrams:
        data=read(output/d['json_path'])
        records.append({'id':d['id'],'document_id':d['document_id'],
                        'source_record':data['source']['figure_record_path'],
                        'json_path':d['json_path'],'markdown_path':d['markdown_path'],
                        'pdf_pages':d['pdf_pages'],'quality':d['quality']})
        source_md=output/Path(data['source']['figure_record_path']).with_suffix('.md')
        if source_md.exists():
            text=source_md.read_text(encoding='utf-8')
            text=re.sub(r'(?m)^> 当前图示解析：[^\n]*\n\n?', '', text)
            first,rest=text.split('\n',1)
            md=os_relative(output/d['markdown_path'],source_md.parent)
            js=os_relative(output/d['json_path'],source_md.parent)
            entry=f'> 当前图示解析：[Markdown]({md}) · [JSON]({js})。包含本轮修正与证据状态；下方保留原图和历史转录。'
            source_md.write_text(first+'\n\n'+entry+'\n\n'+rest.lstrip('\n'),encoding='utf-8')
    for document in read(output/'index.json')['documents']:
        json_path=output/document['json'];source=read(json_path);changed=False
        for page in source['pages']:
            current=[{'id':fid,'json_path':byid[fid]['json_path'],
                      'markdown_path':byid[fid]['markdown_path'],
                      'content_role':'derived-architecture-analysis',
                      'quality':byid[fid]['quality']}
                     for fid in page['figure_ids'] if fid in byid]
            if page.get('current_image_analysis')!=current:
                page['current_image_analysis']=current;changed=True
        if source.get('current_figure_analysis')!='figures/current-analysis.json':
            source['current_figure_analysis']='figures/current-analysis.json';changed=True
        if changed:write(json_path,source)
        path=output/document['markdown'];text=path.read_text(encoding='utf-8')
        def replacement(match):
            ids=list(dict.fromkeys(re.findall(r'\.\./(?:figures|architecture/diagrams)/(G[A-Z0-9]+/[^)\s]+)\.md',match[0])))
            links=[]
            for fid in ids:
                raw=f'../figures/{fid}.md'
                if fid in byid:
                    links.append(f'[{fid}](../{byid[fid]["markdown_path"]})（[原图转录]({raw})）')
                else:
                    links.append(f'[{fid}]({raw})')
            return '本页图片解析：'+' · '.join(links) if links else match[0]
        updated=re.sub(r'(?m)^本页图片(?:结构|解析)：[^\n]+$',replacement,text)
        if updated!=text:path.write_text(updated,encoding='utf-8')
    write(output/'figures/current-analysis.json',{'schema_version':'current-figure-analysis-routing/1',
          'content_role':'current-image-analysis-index','records':records,'count':len(records),
          'notice_zh':'当前解释与原图历史转录逐条关联；质量状态按记录读取，不把局部复核外推至整图。'})
    lines=['# 当前图片解析入口','','全文中的图片链接优先到达这里的当前解析；原图及历史转录另有入口。','',
           '|图片|PDF页|当前解析|原图转录|复核状态|','|---|---|---|---|---|']
    for r in records:
        lines.append(f'|{r["id"]}|{r["pdf_pages"]}|[MD](../{r["markdown_path"]}) · [JSON](../{r["json_path"]})|[原图]({r["id"]}.md)|{r["quality"]["visual_review"]}|')
    (output/'figures/current-analysis.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    path=output/'figures/README.md';text=path.read_text(encoding='utf-8')
    link='当前解释从[图片解析目录](current-analysis.md)或[机器路由](current-analysis.json)读取。各记录保留具体修正与复核范围。\n\n'
    text=re.sub(r'(?m)^当前解释从[^\n]*\n\n?', '', text)
    first,rest=text.split('\n',1);path.write_text(first+'\n\n'+link+rest.lstrip('\n'),encoding='utf-8')


def os_relative(path, parent):
    import os
    return Path(os.path.relpath(path,parent)).as_posix()


def make_conversion_coverage(output, documents, diagrams):
    """Inventory every source document/image and expose remaining review scope."""
    figindex=read(output/'figures/index.json')
    byid={d['id']:d for d in diagrams}
    logical={f['id']:f for f in figindex['figures']}
    rows=[];image_rows=[];pending=[];missing=[]
    for code,entry in documents.items():
        data=read(output/entry['json'])
        for field in ['json','markdown']:
            if not (output/entry[field]).is_file():missing.append(entry[field])
        figs=[f for f in figindex['figures'] if f['document_id']==code]
        images=[im for im in figindex['embedded_images'] if im['document_id']==code]
        rows.append({'id':code,'title_zh':entry['title_zh'],'source':entry['source'],
                     'markdown_path':entry['markdown'],'json_path':entry['json'],
                     'pages':len(data['pages']),'table_fragments':len(data['tables']),
                     'logical_figures':len(figs),'embedded_image_occurrences':len(images),
                     'full_visual_reviews':sum(f['source_role']!='editorial-added' and byid[f['id']]['quality']['visual_review']=='source-content-audited' for f in figs),
                     'source_text_status':data['quality']['text']})
    for im in figindex['embedded_images']:
        fids=im.get('figure_ids',[])
        original_records=[logical[fid] for fid in fids] if fids else [im]
        representations=[]
        for record in original_records:
            for field in ['json_path','markdown_path']:
                if not (output/record[field]).is_file():missing.append(record[field])
            current=byid.get(record['id'])
            representations.append({'id':record['id'],'source_json_path':record['json_path'],
                                    'source_markdown_path':record['markdown_path'],
                                    'current_json_path':current['json_path'] if current else record['json_path'],
                                    'current_markdown_path':current['markdown_path'] if current else record['markdown_path'],
                                    'visual_review':current['quality']['visual_review'] if current else
                                      im.get('current_visual_review',{}).get('status','source-description-see-record')})
        evidence=[]
        if fids:
            for fid in fids:
                evidence.extend(crop for crop in byid[fid]['source_images'] if crop['pdf_page']==im['pdf_page'])
        else:
            evidence=[{k:im[k] for k in ['image_path','image_sha256','pdf_page','bbox_pdf_points']}]
        if not evidence:raise ValueError('Image occurrence has no rendered source evidence: '+im['id'])
        image_rows.append({'id':im['id'],'document_id':im['document_id'],'pdf_page':im['pdf_page'],
                           'source_pdf_sha256':im['provenance']['pdf_sha256'],
                           'source_bbox_pdf_points':im['bbox_pdf_points'],
                           'decoded_image_digest_md5':im['decoded_image_digest_md5'],
                           'image_evidence':evidence,'representations':representations})
    for fid,entry in logical.items():
        for field in ['json_path','markdown_path']:
            if not (output/entry[field]).is_file():missing.append(entry[field])
        tier=byid[fid]['quality']['visual_review']
        if entry['source_role']=='editorial-added' or tier=='source-content-audited':continue
        pending.append({'id':fid,'document_id':entry['document_id'],'title_en':entry.get('title_en'),
                        'pdf_pages':entry['pdf_pages'],'current_json_path':byid[fid]['json_path'],
                        'current_markdown_path':byid[fid]['markdown_path'],'current_review_status':tier,
                        'remaining_review':'independent-all-visible-labels-connectors-grouping-and-source-context'})
    counts={'documents':len(rows),'pages':sum(r['pages'] for r in rows),
            'table_fragments':sum(r['table_fragments'] for r in rows),'logical_figure_records':len(logical),
            'original_figure_records':sum(f['source_role']!='editorial-added' for f in logical.values()),
            'editorial_figure_records':sum(f['source_role']=='editorial-added' for f in logical.values()),
            'embedded_image_occurrences':len(image_rows),
            'images_with_md_and_json':sum(bool(r['representations']) for r in image_rows),
            'standalone_image_records':sum(not im.get('figure_ids') for im in figindex['embedded_images']),
            'full_visual_reviews':sum(r['full_visual_reviews'] for r in rows),
            'original_figures_pending_full_visual_review':len(pending),'missing_artifacts':len(set(missing))}
    report={'schema_version':'togaf-conversion-coverage/1','path_base':'corpus-root','counts':counts,
            'documents':rows,'images':image_rows,'missing_artifacts':sorted(set(missing)),
            'pending_full_visual_review':pending,
            'boundary_zh':'全文、表格和每个图像区域均有可追溯MD/JSON表示。转换覆盖与独立视觉审校分别计数；历史图意保留来源状态，未逐图完成独立审校的记录列在pending_full_visual_review。',
            'validation_reports':{'source':'quality/validation.json','architecture':'architecture/validation.json'}}
    write(output/'quality/conversion-coverage.json',report)
    lines=['# 转换覆盖与视觉审校清单','',report['boundary_zh'],'',
           '|转换对象|数量|','|---|---:|',
           f'|英文PDF / 页面|{counts["documents"]} / {counts["pages"]}|',
           f'|网格表格片段|{counts["table_fragments"]}|',
           f'|原文逻辑图 / 中文编者自绘图|{counts["original_figure_records"]} / {counts["editorial_figure_records"]}|',
           f'|嵌入图像区域 / 已关联MD与JSON表示|{counts["embedded_image_occurrences"]} / {counts["images_with_md_and_json"]}|',
           f'|独立图片记录|{counts["standalone_image_records"]}|',
           f'|完整可见内容已独立审校的原文图|{counts["full_visual_reviews"]}|',
           f'|原文图完整视觉审校待办|{counts["original_figures_pending_full_visual_review"]}|',
           f'|缺失输出文件|{counts["missing_artifacts"]}|','',
           f'机器清单见[conversion-coverage.json](conversion-coverage.json)，包括{counts["embedded_image_occurrences"]}个图像区域各自的原图、MD、JSON及当前解析入口。',
           '验证结果见[来源验证](validation.md)和[架构验证](../architecture/validation.md)。清单记录转换覆盖；验证报告分别检查来源一致性与集成完整性。','',
           '|文档|页数|表格片段|逻辑图|图像区域|完整视觉审校|全文|','|---|---:|---:|---:|---:|---:|---|']
    for r in rows:
        lines.append(f'|{r["id"]}|{r["pages"]}|{r["table_fragments"]}|{r["logical_figures"]}|{r["embedded_image_occurrences"]}|{r["full_visual_reviews"]}|[MD](../{r["markdown_path"]}) · [JSON](../{r["json_path"]})|')
    lines+=['','## 剩余独立视觉审校','',
            '下列图已转换，当前质量状态表示现有复核范围。后续独立审校应继续对照原PDF检查全部标签、实际连接端点、箭头、分组及相关正文。','',
            '|图片|PDF页|当前状态|当前解析|','|---|---|---|---|']
    for r in pending:
        lines.append(f'|{r["id"]}|{r["pdf_pages"]}|{r["current_review_status"]}|[MD](../{r["current_markdown_path"]}) · [JSON](../{r["current_json_path"]})|')
    (output/'quality/conversion-coverage.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return counts


def integrate(root,output):
    root=Path(root).resolve();output=Path(output).resolve();base=output/'architecture'
    ai=read(base/'index.json');ri=read(base/'roles/index.json');di=read(base/'diagrams/index.json')
    concepts=read(base/'concepts.json')['concepts'];relations=read(base/'relationships.json')['relationships']
    role_relations=read(base/'roles/relationships.json')['relationships']
    roles=[read(base/'roles'/p['json']) for p in ri['profiles']]
    diagrams=[read(output/d['json_path']) for d in di['diagrams']]
    docs={d['id']:d for d in read(output/'index.json')['documents']}
    nodes=[];edges=[];rejected_claims=[];rejected_node_claims=[];chunks=[];record_manifest=[]

    def add_record(record_id,kind,title,value,json_path,markdown_path,doc_ids=(),figure_ids=()):
        refs=evidences(value)
        codes=sorted(set(doc_ids)|{e['document_id'] for e in refs})
        locators=[]
        for code in codes:
            if code not in docs:raise ValueError('Unknown document '+code)
            pages=sorted({e['pdf_page'] for e in refs if e['document_id']==code})
            locators.append({'document_id':code,'pdf_pages':pages,**docs[code]['source']})
        # The record file is the direct source of authored analysis; original
        # documents remain multiple explicit locators, never a fabricated one.
        text=title+'\n'+serialize(compact(value))
        parts=list(pieces(text));record_manifest.append({'id':record_id,'kind':kind,'json_path':json_path,
                                                         'markdown_path':markdown_path,'chunk_count':len(parts)})
        for i,part in enumerate(parts,1):
            chunks.append({'id':f'architecture:{record_id}:c{i:03}','parent_record_id':record_id,
                           'part':i,'part_count':len(parts),'document_id':codes[0] if codes else None,
                           'document_ids':codes,'language':'zh','content_role':kind,'section_id':None,
                           'section_title':title,'text':part,
                           'pdf_pages':locators[0]['pdf_pages'] if len(locators)==1 else [],
                           'source_path':str((output/json_path).relative_to(root)),
                           'source_sha256':sha(output/json_path),'source_locators':locators,
                           'markdown_path':markdown_path,'json_path':json_path,'figure_ids':list(figure_ids),
                           'quality':{'status':'authored-analysis-see-evidence','original_text':False,
                                      'visual_review':value.get('quality',{}) if isinstance(value,dict) else None}})

    for guide in ai['guides']:
        code=guide['id'];data=read(base/'guides'/f'{code}.json')
        add_record('guide:'+code,'architecture',data['title_zh']+' · 架构分析',data,
                   f'architecture/guides/{code}.json',f'architecture/guides/{code}.md',[code])
    for c in concepts:
        nodes.append({**c,'id':'concept:'+c['id'],'kind':'concept'})
        add_record('concept:'+c['id'],'concept',c['label_zh']+' / '+c['label_en'],c,
                   'architecture/concepts.json','architecture/concepts.md',c['source_documents'])
    for r in relations:
        edges.append({**r,'id':'concept:'+r['id'],'from':'concept:'+r['source'],'to':'concept:'+r['target'],
                      'predicate':r['type'],'interpretation_status':r['assertion_status']})
        cs={c['id']:c for c in concepts}
        add_record('relation:'+r['id'],'relationship',cs[r['source']]['label_zh']+' '+r['label_zh']+' '+cs[r['target']]['label_zh'],r,
                   'architecture/relationships.json','architecture/relationships.md',r['source_documents'])
    for profile,entry in zip(roles,ri['profiles']):
        nodes.append({**profile,'kind':'role',
                      'source_documents':[profile['source_guide']],'profile_path':'architecture/roles/'+entry['json']})
        add_record(profile['id'],'role',profile['label_zh']+' / '+profile['label_en'],profile,
                   'architecture/roles/'+entry['json'],'architecture/roles/'+entry['markdown'],[profile['source_guide']])
        for skill in profile['skills']:
            edges.append({'id':profile['id']+'::'+skill['skill_id'],'from':profile['id'],'to':skill['skill_id'],
                          'predicate':'requires_skill','required_proficiency':skill['reference_level'],
                          'proficiency_scale':profile['source_guide'],'evidence':[skill['evidence']],
                          'requirement_kind':skill['requirement_kind'],'is_hr_reporting_line':False})
    skilldata=read(base/'roles/skills.json')
    for code in ['G249','G198']:
        for s in skilldata[code]['skills']:
            nodes.append({**s,'kind':'skill','evidence':[s['evidence']],'source_documents':[code]})
    for r in role_relations:
        edges.append({'id':'role:'+r['id'],**{k:v for k,v in r.items() if k!='id'}})
        add_record('role-relation:'+r['id'],'relationship',r['meaning_zh'],r,
                   'architecture/roles/relationships.json','architecture/roles/index.md')
    for data,entry in zip(diagrams,di['diagrams']):
        add_record('diagram:'+data['id'],'diagram',data['title_zh']+' · 架构图关系与上下级',data,
                   entry['json_path'],entry['markdown_path'],[data['document_id']],[data['id']])
        for n in data['nodes']:
            nodes.append({**n,'kind':'diagram-node','diagram_id':data['id'],
                          'record_path':entry['json_path']})
        for e in data['edges']:
            edges.append({**e,'diagram_id':data['id'],
                          'interpretation_status':e['semantic_basis'],
                          'record_path':entry['json_path']})
        for e in data.get('rejected_edges',[]):
            rejected_claims.append({**e,'diagram_id':data['id'],
                                    'record_path':entry['json_path']})
        for n in data.get('rejected_nodes',[]):
            rejected_node_claims.append({**n,'diagram_id':data['id'],'record_path':entry['json_path']})
        for h in data['hierarchy']['containment_and_grouping']:
            edges.append({**h,'from':h['parent'],'to':h['child'],'predicate':h['kind'],
                          'diagram_id':data['id'],'is_hr_reporting_line':False,'evidence_refs':h['evidence_refs'],
                          'interpretation_status':h['basis'],'record_path':entry['json_path']})
    ids={n['id'] for n in nodes}
    if len(ids)!=len(nodes):raise ValueError('Duplicate graph node ID')
    if len({e['id'] for e in edges})!=len(edges):raise ValueError('Duplicate graph edge ID')
    for e in edges:
        if e['from'] not in ids or e['to'] not in ids:raise ValueError('Graph endpoint missing '+e['id'])
    graph={'schema_version':'togaf-architecture-knowledge/1','content_role':'derived-architecture-knowledge',
           'notice_zh':'不同指南、图中实例、角色和概念分别保留身份；名称相似不自动合并。节点引用不表示当前项目事实。',
           'nodes':nodes,'edges':edges,'rejected_claims':rejected_claims,'rejected_node_claims':rejected_node_claims,
           'rejected_claims_notice_zh':'这些历史解释未得到原图支持，已从有效关系图与Mermaid中移除；仅保留供审计，不能作为架构事实。',
           'counts':{'nodes':len(nodes),'edges':len(edges),'rejected_claims':len(rejected_claims)},
           'layers':['concept','role','skill','diagram-node']}
    write(base/'knowledge-graph.json',graph)
    (output/'retrieval/architecture-chunks.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in chunks),encoding='utf-8')
    write(base/'retrieval-manifest.json',{'records':record_manifest,'counts':{'records':len(record_manifest),'chunks':len(chunks)},
                                       'retrieval_path':'retrieval/architecture-chunks.jsonl'})
    index={'schema_version':'architecture-workspace/1','content_role':'source-grounded-and-derived-analysis',
           'counts':{'guides':len(ai['guides']),'concepts':len(concepts),'concept_relationships':len(relations),
                     **ri['counts'],**di['counts'],'knowledge_nodes':len(nodes),'knowledge_edges':len(edges),
                     'rejected_historical_claims':len(rejected_claims),'retrieval_chunks':len(chunks)},
           'paths':{'guide_analysis':'architecture/index.json','diagrams':'architecture/diagrams/index.json',
                    'roles':'architecture/roles/index.json','concepts':'architecture/concepts.json',
                    'relationships':'architecture/relationships.json','knowledge_graph':'architecture/knowledge-graph.json',
                    'retrieval':'retrieval/architecture-chunks.jsonl','browser':'architecture/explorer.html'},
           'boundary_zh':'架构图原文、历史解读、当前关系校正、派生项目建议分别保留证据状态；本层不声称每张图所有箭头均已独立重新目视核验。'}
    write(base/'catalog.json',index)
    make_readme(base,index)
    make_explorer(base,di['diagrams'],roles,ri['profiles'],concepts,relations)
    connect_diagram_reading_paths(output,di['diagrams'])
    make_conversion_coverage(output,docs,di['diagrams'])
    corpusindex=read(output/'index.json');corpusindex['architecture']='architecture/catalog.json'
    corpusindex['architecture_retrieval']='retrieval/architecture-chunks.jsonl'
    corpusindex['current_figure_analysis']='figures/current-analysis.json'
    corpusindex['conversion_coverage']='quality/conversion-coverage.json'
    corpusindex['architecture_counts']=index['counts'];write(output/'index.json',corpusindex)
    return index


def make_readme(base,index):
    counts=index['counts']
    lines=['# 架构解析与角色能力入口','',
           '这里保存架构语义成果：图中是什么、关系如何读、上下级属于哪一种语义、角色负责什么，以及每项技能的参考要求。','',
           '- [可筛选浏览器](explorer.html)：按指南、图类型或角色查看原图和分析。',
           '- [全部图示解析](diagrams/index.md)：原图、完整实体/关系、包含树与可编辑 Mermaid。',
           '- [角色职责与能力](roles/index.md)：角色要求、输入输出、协作、完整技能等级、版本区别。',
           '- [26 份指南架构分析](index.md)：输入输出、方法、判断依据与应用步骤。',
           '- [概念定义](concepts.md) · [类型化关系](relationships.md) · [机器知识图谱](knowledge-graph.json)。',
           '- [架构验证](validation.md)；[底层文档转换验证](../quality/validation.md)。','',
           '转换覆盖及剩余独立视觉审校见[逐项清单](../quality/conversion-coverage.md)。','',
           '## 可以直接回答的问题','',
           '|问题|读取入口|','|---|---|',
           '|能力、能力实例、价值流阶段是什么关系？|[G233 元模型](diagrams/G233/fig3-1.md)、[关系说明](relationships.md)|',
           '|图中框中框是否是管理上下级？|各图“上下级与包含”及 hierarchy.views；组织汇报另列|',
           '|企业架构师需要哪些技能及等级？|[G249 企业架构师](roles/G249-enterprise-architect.md)|',
           '|首席架构师和分段架构师分别负责什么？|[首席](roles/G249-chief-architect.md)、[分段](roles/G249-segment-architect.md)|',
           '|两个技能框架可以直接互换吗？|[G198/G249 对比](roles/comparison.md)|','',
           '## 当前覆盖','',f'- {counts["guides"]} 份指南架构分析；{counts["concepts"]} 个概念、{counts["concept_relationships"]} 条跨指南关系。',
           f'- {counts["diagrams"]} 条图示分析（架构、流程、矩阵、图例和问卷等），{counts["nodes"]} 个图内节点、{counts["relations"]} 条关系、{counts["hierarchy_links"]} 条包含/分组。',
           f'- {counts["roles"]} 个角色档案；{counts["matrix_roles"]} 个角色具有原文技能矩阵列，共 {counts["skill_expectations"]} 项技能等级要求。',
           f'- {counts["reviewed_figures"]} 张有本轮视觉核对记录，其中 {counts.get("content_audited_figures",0)} 张核对了完整可见内容；{counts.get("source_transcribed_embedded_images",0)} 条独立图元已有原图文字/表格转录。复核范围和未知项逐条保存。','',
           '没有独立数值列的角色明确记录“原文未规定”，并分析其文字职责和能力要求。结构层级、业务组成、类型/实例、架构治理和人事汇报分别表示，未知关系不补造。','',
           '## 检索','', '```sh',
           'python3 tools/togaf_corpus/query.py "企业架构师 技能" --role role --doc G249 --limit 3',
           'python3 tools/togaf_corpus/query.py "能力实例 实例化" --role relationship --limit 5',
           'python3 tools/togaf_corpus/query.py "上下级 组织" --role diagram --limit 5',
           'python3 tools/togaf_corpus/build_architecture.py',
           'python3 tools/togaf_corpus/validate_architecture.py','```','']
    (base/'README.md').write_text('\n'.join(lines),encoding='utf-8')


def make_explorer(base,diagrams,roles,role_entries,concepts,relations):
    entries=[]
    for d in diagrams:
        entries.append({'kind':'图示','id':d['id'],'title':d['title_zh'],'subtitle':d['category'],
                        'doc':d['document_id'],'path':d['markdown_path'].removeprefix('architecture/'),
                        'json':d['json_path'].removeprefix('architecture/'),
                        'image':'../'+d['source_images'][0]['image_path'] if d['source_images'] else None,
                        'summary':f"{d['statistics']['nodes']} 节点 · {d['statistics']['source_relations']} 关系 · {d['statistics']['containment_or_grouping']} 包含/分组"})
    for r,e in zip(roles,role_entries):
        entries.append({'kind':'角色','id':r['id'],'title':r['label_zh']+' / '+r['label_en'],'subtitle':r['scope_zh'],
                        'doc':r['source_guide'],'path':'roles/'+e['markdown'],'json':'roles/'+e['json'],'image':None,
                        'summary':r.get('analysis_zh',''),'skills':r['skills'],
                        'responsibilities':r['responsibilities'],'requirements':r['requirements'],'scale':r.get('proficiency_scale',[])})
    payload=json.dumps(entries,ensure_ascii=False).replace('<','\\u003c')
    template='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TOGAF 架构解析</title>
<style>body{font:16px/1.6 system-ui,sans-serif;margin:0;color:#19304a;background:#f3f6fa}header,main{max-width:1280px;margin:auto;padding:24px}header{background:#fff}h1{margin:0}p{margin:8px 0}nav{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}input,select{font:inherit;padding:10px;border:1px solid #b8c7da;border-radius:6px}input{min-width:300px;flex:1}a{color:#075cb2}#cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:18px}article{background:white;padding:18px;border:1px solid #d7e0ec;border-radius:8px}article img{width:100%;height:220px;object-fit:contain;background:#fff}h2{font-size:19px;margin:8px 0}.meta{color:#53667b;font-size:14px}.pill{color:#23578e;font-weight:600}summary{cursor:pointer;color:#075cb2}table{border-collapse:collapse;font-size:14px;width:100%}td,th{padding:6px;border-bottom:1px solid #dde5ef;text-align:left}.scroll{max-height:450px;overflow:auto}button{font:inherit;padding:8px 14px;margin:20px 0}#count{margin-bottom:16px}</style>
<header><h1>架构解析 · 关系 · 角色能力</h1><p>按主题查看原图、结构化关系、上下级含义与角色要求。原文与解读各自保留证据状态。</p><p><a href="README.md">使用说明</a> · <a href="relationships.md">概念关系</a> · <a href="index.md">26 份指南分析</a> · <a href="roles/comparison.md">角色框架对比</a></p><nav><input id="query" placeholder="搜索：能力、元模型、企业架构师…" aria-label="搜索"><select id="kind" aria-label="类型"><option value="">全部类型</option><option>图示</option><option>角色</option></select><select id="doc" aria-label="指南"><option value="">全部指南</option></select></nav></header>
<main><div id="count"></div><div id="cards"></div><button id="more">显示更多</button></main><script>const data=__DATA__;const $=s=>document.querySelector(s);let limit=24;const docs=[...new Set(data.map(x=>x.doc))].sort();for(const d of docs){const o=document.createElement('option');o.value=d;o.textContent=d;$('#doc').append(o)}
function el(tag,text,cls){const x=document.createElement(tag);if(text!==undefined)x.textContent=text;if(cls)x.className=cls;return x}function link(text,url){const a=el('a',text);a.href=url;return a}function render(){const q=$('#query').value.trim().toLowerCase();const f=data.filter(x=>(!$('#kind').value||x.kind===$('#kind').value)&&(!$('#doc').value||x.doc===$('#doc').value)&&(!q||JSON.stringify(x).toLowerCase().includes(q)));$('#count').textContent=`匹配 ${f.length} 条，显示 ${Math.min(limit,f.length)} 条。图示包括架构模型、方法流程、矩阵和问卷，具体类型见卡片。`;$('#cards').replaceChildren();for(const x of f.slice(0,limit)){const a=el('article');a.append(el('div',x.kind+' · '+x.id,'pill'));if(x.image){const im=document.createElement('img');im.src=x.image;im.alt=x.title+' 原图';im.loading='lazy';a.append(im)}a.append(el('h2',x.title),el('div',x.subtitle,'meta'),el('p',x.summary));const p=el('p');p.append(link('完整分析',x.path),document.createTextNode(' · '),link('JSON',x.json));a.append(p);if(x.skills){const dt=el('details');dt.append(el('summary',`职责、要求和 ${x.skills.length} 项参考技能`));for(const k of ['responsibilities','requirements']){dt.append(el('h3',k==='responsibilities'?'职责':'能力要求'));for(const r of x[k])dt.append(el('p',r.text_zh||r.text_en||JSON.stringify(r)))}if(!x.skills.length)dt.append(el('p','原文没有该角色独立技能数值列。文字要求见上与完整分析。'));else{const wrap=el('div',undefined,'scroll'),t=el('table'),head=el('tr');for(const c of ['技能','类别','等级'])head.append(el('th',c));t.append(head);for(const s of x.skills){const tr=el('tr');tr.append(el('td',s.label_en),el('td',s.category_zh),el('td',s.reference_level+' · '+s.level_name_en));t.append(tr)}wrap.append(t);dt.append(wrap)}a.append(dt)}$('#cards').append(a)}$('#more').hidden=limit>=f.length}for(const s of ['#query','#kind','#doc'])$(s).addEventListener('input',()=>{limit=24;render()});$('#more').addEventListener('click',()=>{limit+=24;render()});render();</script></html>'''
    (base/'explorer.html').write_text(template.replace('__DATA__',payload),encoding='utf-8')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'togaf-standard-10th-ai')
    p.add_argument('--integrate-only',action='store_true');a=p.parse_args()
    if not a.integrate_only:
        from architecture_analysis import build as analysis
        from architecture_diagrams import build as diagrams
        from roles import build_roles
        analysis(ROOT,a.output);build_roles(ROOT,a.output);diagrams(ROOT,a.output)
    result=integrate(ROOT,a.output);print(serialize(result['counts']))
    from chapter_reviews import build as chapters
    print(serialize(chapters(ROOT,a.output)['counts']))

if __name__=='__main__':main()
