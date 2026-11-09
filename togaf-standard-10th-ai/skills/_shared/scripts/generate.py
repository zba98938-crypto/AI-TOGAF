#!/usr/bin/env python3
"""Derive Markdown, JSON and editable diagrams from a validated common model."""
import argparse
import base64
import html
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict
from validate import ARTS,DELS,ROOT,validate
from registry import load as load_registry, profile_for
from strict_json import load as load_json, dumps as strict_dumps

def dump(path,value):Path(path).write_text(strict_dumps(value,ensure_ascii=False,indent=2)+'\n')
def cell(value):return str(value).replace('|','\\|').replace('\n','<br>')
def table(headers,rows):return '| '+' | '.join(map(cell,headers))+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(map(cell,row))+' |\n' for row in rows)
def label(e):return e['name']+' ['+e['type']+']'
def mtext(text):return html.escape(str(text).replace('\n',' '),quote=True).replace('[','(').replace(']',')').replace('{','(').replace('}',')')

def diagram_source(view,contract,entities,relationships):
    """Compatibility helper: complete editable relation projection, never silent filtering."""
    renderer={"sequence":"sequence","state":"state","er":"er"}.get(contract.get("notation"),"network")
    return editable_mermaid(view,{"renderer":renderer},entities,relationships)

def subset_font(text,out):
    try:
        from fontTools import subset
        from fontTools.ttLib import TTFont
        from fontTools.varLib.instancer import instantiateVariableFont
    except ImportError:raise RuntimeError('渲染需要 fonttools；按 README 安装 requirements.txt。')
    font=TTFont(ROOT/'assets/fonts/NotoSansSC.ttf')
    if 'fvar' in font:font=instantiateVariableFont(font,{'wght':400},inplace=True)
    options=subset.Options();options.name_IDs=['*'];subsetter=subset.Subsetter(options=options)
    subsetter.populate(text=text+''.join(chr(i) for i in range(32,127))+'必填可选可选性待确认类型未知零至多恰一图例候选草案虚构示例→');subsetter.subset(font);font.save(out)
    return base64.b64encode(Path(out).read_bytes()).decode()

def artifact_markdown(model,v,a,ent,rel):
    if v.get('profile_id') == 'architecture-work-assignment-map':
        from assignment_projection import markdown
        return markdown(model,v)
    s=f'# {v["title"]}\n\n'+('**虚构验收案例，不代表真实企业事实。**\n\n' if model['project']['is_example'] else '')
    s+=f'制品：{a["name_zh"]}（{a["name_en"]}） · 模型 {model["project"]["version"]} · 视图 `{v["id"]}`\n\n'
    s+='语境：`'+json.dumps(v['context'],ensure_ascii=False)+'`\n\n'+v['analysis']+'\n\n'
    es=[ent[i] for i in v['entity_ids']];rs=[rel[i] for i in v['relationship_ids']]
    if v.get('_graphical') is False:
        s+='完整对象字段及关系见下方“模型表达”表；按视图规范选择记录式或行式布局。\n\n'
    elif a['kind']=='matrix' and a.get('matrix'):
        m=a['matrix'];rows=[e for e in es if e['type'] in m['row_types']];cols=[e for e in es if e['type'] in m['column_types']]
        cells=defaultdict(list)
        rowids={e['id'] for e in rows};colids={e['id'] for e in cols}
        for edge in rs:
            if edge['source'] in rowids and edge['target'] in colids:
                key=(edge['source'],edge['target']);direction='行→列'
            elif edge['target'] in rowids and edge['source'] in colids:
                key=(edge['target'],edge['source']);direction='列→行'
            else:continue
            cells[key].append(direction+' · '+(', '.join(edge.get('codes',[])) or edge['label'])+' ['+edge['id']+']')
        s+=table(['行对象 / 列对象']+[e['name']+' ['+e['id']+']' for e in cols],[[row['name']+' ['+row['id']+']']+[', '.join(cells[(row['id'],col['id'])]) or '未记录' for col in cols] for row in rows])
        s+='\n单元含义：'+m['cell_meaning']+'。空白含义：'+m['empty_meaning']+'。\n'
    elif a['kind']=='catalog':
        s+=table(['ID','类型','名称']+[f for f in a['fields'] if f!='name'],[[e['id'],e['type'],e['name']]+[json.dumps(e['attributes'].get(f,'待补'),ensure_ascii=False) for f in a['fields'] if f!='name'] for e in es if e['type'] in a['entity_types']])
    else:
        s+=table(['ID','类型','名称','属性'],[[e['id'],e['type'],e['name'],json.dumps(e['attributes'],ensure_ascii=False)] for e in es])
    if v.get('_graphical', a['kind']=='diagram' or bool(v.get('profile_id'))):
        s+=f'\n![{a["name_zh"]}]({v["id"]}.svg)\n\n独立图片：[{v["id"]}.png]({v["id"]}.png)。可编辑源与模型见同目录。\n'
    s+='\n图例／解释：'+v['legend']+'\n\n'
    if v.get('analysis_results'):
        s+='## 分析结果\n\n'
        for result in v['analysis_results']:
            s+='```json\n'+json.dumps(result,ensure_ascii=False,indent=2)+'\n```\n\n'
    if rs:s+=table(['关系 ID','起点','语义','终点','说明','属性／代码／端基数','证据／确定性'],[[r['id'],r['source'],r['type'],r['target'],r['label'],json.dumps({k:r[k] for k in ('attributes','codes','cardinality') if k in r},ensure_ascii=False),', '.join(r['evidence'])+' / '+r['certainty']] for r in rs])+'\n'
    s+='\n证据与缺口：\n\n'+table(['对象','来源','确定性'],[[e['id'],', '.join(e['evidence']),e['certainty']] for e in es])
    for gap in model['gaps']:s+=f'\n- {gap["description"]}；影响：{gap["impact"]}；需要：{gap["needed_input"]}。\n'
    s+='\n方法检查：\n\n'+''.join('- '+c+'。\n' for c in a['semantic_checks'])
    s+='\n这些检查是评审问题，生成文件不自动表示已通过业务评审。\n'
    return s

def generate(model,out,artifact_ids=None,deliverable_ids=None,all_items=False,render=False,
             view_ids=None,profile_ids=None,layout=None,strict=False):
    """Generate selected model views; all means all content present in this model."""
    from profile_render import render_profile
    from runtime_provenance import fingerprints
    started_at=datetime.now(timezone.utc).isoformat()
    runtime_before=fingerprints(ROOT)
    arts,dels,profiles,_=load_registry()
    issues=validate(model)
    errors=[i for i in issues if i['level']=='error']
    if errors:raise ValueError(json.dumps(errors,ensure_ascii=False,indent=2))
    requested=set(artifact_ids or []);drequested=set(deliverable_ids or [])
    vrequested=set(view_ids or []);prequested=set(profile_ids or [])
    for label,unknown in [('制品',requested-arts.keys()),('交付物',drequested-dels.keys()),('视图规范',prequested-profiles.keys())]:
        if unknown:raise ValueError('未知'+label+' ID：'+', '.join(sorted(unknown)))
    ent={e['id']:e for e in model['entities']};rel={r['id']:r for r in model['relationships']}
    views={v['id']:v for v in model['views']}
    if vrequested-views.keys():raise ValueError('缺少视图：'+', '.join(sorted(vrequested-views.keys())))
    def effective_profile(v):return v.get('profile_id') or arts[v['artifact_id']].get('default_profile_id')
    selected_views={v['id'] for v in model['views'] if all_items or v['artifact_id'] in requested or effective_profile(v) in prequested or v['id'] in vrequested}
    deliverables=[d for d in model['deliverables'] if all_items or d['deliverable_id'] in drequested]
    missing=drequested-{d['deliverable_id'] for d in deliverables}
    if missing:raise ValueError('缺少已分析的交付物内容：'+', '.join(sorted(missing)))
    for d in deliverables:selected_views.update(d['view_ids'])
    from deliverable_assembly import assemble,dependency_closure
    assembled={}
    for d in deliverables:
        if d.get('assembly'):
            result=assemble(model,d,dels[d['deliverable_id']])
            if result['status']=='blocked':raise ValueError(json.dumps(result['gaps'],ensure_ascii=False,indent=2))
            assembled[d['id']]=result;selected_views.update(result['required_view_ids'])
    chosen=[v for v in model['views'] if v['id'] in selected_views]
    missing=requested-{v['artifact_id'] for v in chosen}
    missing_profiles=prequested-{effective_profile(v) for v in chosen}
    if missing or missing_profiles:raise ValueError('缺少已分析的视图：'+', '.join(sorted(missing|missing_profiles)))
    if not chosen and not deliverables:raise ValueError('没有选择可输出的视图或交付物')
    # Safe names also prevent traversal when generate() is called directly.
    for obj in chosen+deliverables:
        if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_.-]*',obj['id']):raise ValueError('不安全的输出 ID：'+obj['id'])
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    ad=out/'artifacts';dd=out/'deliverables';ad.mkdir(exist_ok=True);dd.mkdir(exist_ok=True)
    def output_file(directory,identity,extension):return directory/(identity+'.'+extension)
    manifest={'schema_version':'2.0','model_schema_version':model['schema_version'],'project':model['project'],
              'run_id':uuid.uuid4().hex,'started_at':started_at,
              'model_version':model['project']['version'],
              'model_sha256':hashlib.sha256(json.dumps(model,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
              'artifacts':[],'deliverables':[],'rendered':False,'renderer_version':'profile-svg-'+__import__('profile_render').VERSION,
              'renderer_sha256':hashlib.sha256((ROOT/'scripts/profile_render.py').read_bytes()).hexdigest(),
              'implementation_dependencies_sha256':runtime_before,
              'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'table_renderer_sha256':hashlib.sha256((ROOT/'scripts/table_expression.py').read_bytes()).hexdigest(),
              'metamodel_sha256':hashlib.sha256((ROOT/'metamodel.json').read_bytes()).hexdigest(),
              'artifacts_sha256':hashlib.sha256((ROOT/'artifacts.json').read_bytes()).hexdigest(),
              'deliverables_sha256':hashlib.sha256((ROOT/'deliverables.json').read_bytes()).hexdigest(),
              'assembly_renderer_sha256':hashlib.sha256((ROOT/'scripts/deliverable_assembly.py').read_bytes()).hexdigest(),
              'assembly_rules_sha256':hashlib.sha256((ROOT/'capability-addenda/deliverable-assembly-rules.json').read_bytes()).hexdigest(),
              'capabilities_sha256':hashlib.sha256((ROOT/'capabilities.json').read_bytes()).hexdigest() if (ROOT/'capabilities.json').exists() else None,
              'notice':'生成与工程检查不等于业务评审通过或 TOGAF 全面等价认证。'}
    dump(out/'model.json',model);dump(out/'validation.json',{'issues':issues,'limit':'结构及已编码语义规则；业务结论仍需证据和评审。'})
    font_b64='';jobs=[];coverage=[];computed_analyses={}
    analyses={a['id']:a for a in model.get('analyses',[])}
    for result in assembled.values():
        for calculated in result['analysis_results']:
            computed_analyses[calculated['id']]=calculated
    for original in chosen:
        v=dict(original);v['_is_example']=model['project']['is_example']
        analysis_ids=v.get('attributes',{}).get('analysis_ids',[])
        if analysis_ids:
            from analyze import evaluate
            if set(analysis_ids)-analyses.keys():raise ValueError(v['id']+' 引用了不存在的分析 ID')
            for aid in analysis_ids:computed_analyses[aid]=evaluate(analyses[aid],model)
            v['analysis_results']=list(v.get('analysis_results',[]))+[computed_analyses[aid] for aid in analysis_ids]
        a=arts[v['artifact_id']];vid=v['id'];profile=profile_for(v,a,profiles)
        v['profile_id']=profile['id']
        graphical=profile.get('output_kind','diagram')=='diagram'
        v['_graphical']=graphical
        md=artifact_markdown(model,v,a,ent,rel)
        payload={'schema_version':model['schema_version'],'project':model['project'],'view':{**original,'profile_id':profile['id']},'computed_analyses':[computed_analyses[aid] for aid in analysis_ids],
                 'entities':[ent[i] for i in v['entity_ids']],'relationships':[rel[i] for i in v['relationship_ids']],
                 'sources':model['sources'],'gaps':model['gaps']}
        dump(output_file(ad,vid,'json'),payload)
        entry={'id':a['id'],'view_id':vid,'profile_id':profile['id'],
               'profile_version':profile.get('version','2.0'),'output_kind':'diagram' if graphical else 'table',
               'template_id':profile.get('template',{}).get('id',profile['id']),
               'template_version':profile.get('template',{}).get('version',profile.get('version','2.0')),
               'path':'artifacts/'+vid+'.md','json':'artifacts/'+vid+'.json'}
        if graphical:
            profile=profile_for(v,a,profiles);chosen_layout=layout or v.get('layout','adaptive')
            if chosen_layout=='reference' and not profile.get('template',{}).get('source_verified',False):
                v['legend']+='；来源结构模板尚未完成独立核实，不能据此声明与来源图等价。'
            svg,report=render_profile(model,v,profile,layout=chosen_layout)
            from view_semantics import check_view
            report.setdefault('errors',[]).extend(check_view(model,v,profile))
            report.update({'view_id':vid,'artifact_id':a['id'],'profile_id':profile['id'],'layout':chosen_layout})
            if report.get('companion_html'):
                output_file(ad,vid,'details.html').write_text(report['companion_html'])
                entry['details']='artifacts/'+vid+'.details.html'
                md+='\n[分组明细与完整关系记录]('+vid+'.details.html)\n'
            output_file(ad,vid,'svg').write_text(svg)
            if strict and report.get('errors'):raise ValueError(json.dumps(report['errors'],ensure_ascii=False))
            dump(output_file(ad,vid,'coverage.json'),report);coverage.append(report)
            dump(output_file(ad,vid,'layout.json'),{'view_id':vid,'profile_id':profile['id'],'layout':chosen_layout,
                 'template':profile.get('template',{}),'editable_source':vid+'.svg','model':'../model.json',
                 'profile_version':profile.get('version','2.0'),'source_refs':profile.get('source_refs',[])})
            # Preserve a complete editable relation source as well as the specialized SVG.
            source=editable_mermaid(v,profile,ent,rel)
            output_file(ad,vid,'mmd').write_text(source)
            jobs.append({'source':'artifacts/'+vid+'.svg','svg':'artifacts/'+vid+'.svg','png':'artifacts/'+vid+'.png',
                         'kind':'svg','id':vid,'title':v['title'],'legend':v['legend'],'is_example':model['project']['is_example']})
            entry.update({'profile_id':profile['id'],'layout':chosen_layout,'svg':'artifacts/'+vid+'.svg',
                          'png':'artifacts/'+vid+'.png' if render else None,'coverage':'artifacts/'+vid+'.coverage.json',
                          'render_status':'pending'})
            md+='\n表达完整性见 ['+vid+'.coverage.json]('+vid+'.coverage.json)。来源结构模板的核实状态见布局文件；生成不改变该状态。\n'
            if not render:
                md=re.sub(r'独立图片：.*?。可编辑源','PNG 尚未渲染；使用 --render。可编辑源',md)
            if report.get('errors') or report.get('unrepresented_entity_ids') or report.get('unrepresented_relationship_ids'):
                entry['status']='draft-with-gaps';md+='\n**草稿存在表达缺口，不能作为已验收视图。**\n'
            else:entry['status']='generated-awaiting-review'
        else:
            from table_expression import render_table_expression
            from view_semantics import check_view
            expression,report=render_table_expression(model,v,profile,table)
            report['errors'].extend(check_view(model,v,profile))
            if strict and report.get('errors'):raise ValueError(json.dumps(report['errors'],ensure_ascii=False))
            report.update({'view_id':vid,'artifact_id':a['id'],'profile_id':profile['id'],'layout':layout or v.get('layout','adaptive')})
            md+=expression+'\n表达位置见 ['+vid+'.coverage.json]('+vid+'.coverage.json)。\n'
            if strict and report.get('errors'):raise ValueError(json.dumps(report['errors'],ensure_ascii=False))
            dump(output_file(ad,vid,'coverage.json'),report);coverage.append(report)
            entry.update({'coverage':'artifacts/'+vid+'.coverage.json','status':'draft-with-gaps' if report['errors'] else 'generated-awaiting-review','render_status':'not-applicable'})
        output_file(ad,vid,'md').write_text(md);manifest['artifacts'].append(entry)
    for d in deliverables:
        contract=dels[d['deliverable_id']];did=d['id']
        # Keep established singleton filenames; distinct instances never overwrite one another.
        same=[x for x in deliverables if x['deliverable_id']==d['deliverable_id']]
        file_id=contract['id'] if len(same)==1 else did
        text='# '+d['title']+'\n\n'+('**虚构验收案例，不代表真实企业事实。**\n\n' if model['project']['is_example'] else '')
        text+='交付物：'+contract['name_en']+' · 模型 '+model['project']['version']+' · 兼容决策状态：'+d.get('decision_status','unspecified')+'\n\n'
        text+='批准状态：'+d.get('approval_status','unspecified')+' · 实现状态：'+d.get('implementation_status','unspecified')+'\n\n'
        assembly=assembled.get(did)
        appendix_path=None
        if assembly:
            text+='组装状态：'+assembly['status']+'；规则版本：'+d['assembly']['rules_version']+'。\n\n'
            text+='内容证据状态：'+assembly.get('content_status','not-assessed')+'。组装成功不代表各章节完整。\n\n'
            if assembly.get('unbound_section_titles'):text+='未绑定结构化章节证据：'+'、'.join(assembly['unbound_section_titles'])+'；这些章节不计内容已验收，是否阻断由项目适用性评审明确。\n\n'
            from deliverable_reader import reader_sections
            readable=reader_sections(model,assembly)
            if readable:
                appendix_path='appendices/'+file_id+'.md'
                (out/'appendices').mkdir(exist_ok=True)
                appendix='# 技术证据附录：'+d['title']+'\n\n保留全部原始组装字段、来源、分析结果与未决项；不是独立批准。\n\n'
                appendix+=''.join('## '+s['title']+'\n\n'+s['markdown']+'\n\n' for s in assembly['section_blocks'])
                (out/appendix_path).write_text(appendix)
                text+='本正文先呈现业务问题、结论、权衡与未知；[完整技术证据附录](../'+appendix_path+')保存所有模型字段和计算结果。\n\n'
            for section in readable or assembly['section_blocks']:text+='## '+section['title']+'\n\n'+section['markdown']+'\n\n'
        else:
            for section in contract['sections']:text+='## '+section['title']+'\n\n'+d['sections'][section['title']]+'\n\n'
        text+='## 支撑制品\n\n'
        for vid in assembly['required_view_ids'] if assembly else d['view_ids']:text+='- ['+views[vid]['title']+'](../artifacts/'+vid+'.md) · '+vid+'\n'
        if contract['id']=='architecture-repository':
            text+='\n## 实际资产索引\n\n'+table(['视图 ID','制品族','版本','路径'],[[v['id'],v['artifact_id'],model['project']['version'],'[视图](../artifacts/'+v['id']+'.md)'] for v in chosen])+'\n共享模型：[model.json](../model.json)。\n'
        text+='\n## 评审要求\n\n'+''.join('- '+c+'。\n' for c in contract['semantic_checks'])
        output_file(dd,file_id,'md').write_text(text)
        dump(output_file(dd,file_id,'json'),{'schema_version':model['schema_version'],'project':model['project'],'deliverable':d,'contract_id':contract['id'],'assembly':assembly})
        manifest['deliverables'].append({'id':contract['id'],'instance_id':did,'path':'deliverables/'+file_id+'.md','json':'deliverables/'+file_id+'.json','assembly_status':assembly['status'] if assembly else 'legacy-unassembled','content_status':assembly.get('content_status') if assembly else 'not-assessed','unbound_section_titles':assembly.get('unbound_section_titles',[]) if assembly else [],'view_ids':assembly['required_view_ids'] if assembly else d['view_ids']})
        if appendix_path:manifest['deliverables'][-1]['appendix']=appendix_path
    if render and jobs:
        # Subset the actual generated labels, including renderer-owned legends and diagnostics.
        generated_text=''.join((out/job['source']).read_text() for job in jobs)
        font_b64=subset_font(json.dumps(model,ensure_ascii=False)+html.unescape(re.sub(r'<[^>]+>',' ',generated_text)),out/'font-subset.ttf')
        for job in jobs:
            path=out/job['source'];svg=path.read_text()
            svg=svg.replace('>','><defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+font_b64+')}text{font-family:TogafCJK,sans-serif}</style></defs>',1)
            path.write_text(svg)
        dump(out/'render-jobs.json',{'font':'font-subset.ttf','oversized_policy':'tile','jobs':jobs})
        subprocess.run(['node',str(ROOT/'scripts/render.mjs'),str((out/'render-jobs.json').resolve())],check=True);manifest['rendered']=True
        rendered=load_json(out/'render-report.json')
        for result in rendered['results']:
            if result.get('mode')!='tiles':continue
            entry=next(e for e in manifest['artifacts'] if e['view_id']==result['id'])
            entry.update(png=None,raster_mode='tiles',monolithic_capacity_claimed=False,
                         tile_manifest='artifacts/'+result['tile_manifest'],
                         tile_viewer='artifacts/'+result['tile_viewer'])
            tiles=load_json(out/entry['tile_manifest'])
            entry['tile_pngs']=['artifacts/'+t['png'] for t in tiles['tiles']]
            path=out/entry['path']
            text=path.read_text()
            text=text.replace('独立图片：['+result['id']+'.png]('+result['id']+'.png)。',
                '原尺寸分块图片：['+result['tile_viewer']+']('+result['tile_viewer']+')；不是单张 PNG 容量通过。')
            path.write_text(text)
    dump(out/'analysis-results.json',{'analyses':list(computed_analyses.values()),'notice':'仅执行所选视图显式引用且已声明规则的分析。'})
    dump(out/'expression-coverage.json',{'views':coverage,'notice':'表达记录是工程证据；需结合语义断言及目视评审。'})
    index='# 架构成果索引\n\n'+('虚构验收案例。\n\n' if model['project']['is_example'] else '')
    for group,title in [('artifacts','制品'),('deliverables','交付物')]:
        index+='## '+title+'\n\n'+''.join('- ['+entry.get('view_id',entry['id'])+']('+entry['path']+')\n' for entry in manifest[group])+'\n'
    (out/'index.md').write_text(index)
    paths={'model.json','validation.json','analysis-results.json','expression-coverage.json','index.md'}
    for entry in manifest['artifacts']+manifest['deliverables']:
        paths.update(entry[k] for k in ('path','json','coverage','svg','png','appendix','details','tile_manifest','tile_viewer') if entry.get(k))
        paths.update(entry.get('tile_pngs',[]))
    if render and jobs:paths.update(('render-report.json','render-jobs.json'))
    for job in jobs:
        paths.update('artifacts/'+job['id']+'.'+suffix for suffix in ('mmd','layout.json'))
    manifest['output_sha256']={name:hashlib.sha256((out/name).read_bytes()).hexdigest() for name in sorted(paths)}
    manifest['finished_at']=datetime.now(timezone.utc).isoformat()
    manifest['runtime_after_sha256']=fingerprints(ROOT)
    manifest['runtime_stable']=manifest['runtime_after_sha256']==runtime_before
    dump(out/'manifest.json',manifest)
    if not manifest['runtime_stable']:raise RuntimeError('生成期间运行依赖变化；本次成果不能登记为当前稳定输出')
    if render and jobs:
        from finalize_render import finalize
        manifest=finalize(out)
    return manifest

def editable_mermaid(view,profile,entities,relationships):
    """Loss-aware Mermaid source; comments retain IDs and unsupported notation semantics."""
    es=[entities[i] for i in view['entity_ids']];rs=[relationships[i] for i in view['relationship_ids']]
    ids={e['id']:'n'+str(i) for i,e in enumerate(es)}
    if profile['renderer']=='sequence' and all('order' in r.get('attributes',{}) for r in rs):
        lines=['sequenceDiagram']+[f'  participant {ids[e["id"]]} as {mtext(e["name"])}' for e in es]
        for r in sorted(rs,key=lambda x:x['attributes']['order']):
            lines+=['  %% relationship-id: '+r['id'],f'  {ids[r["source"]]}->>{ids[r["target"]]}: {mtext(r["label"])}']
    elif profile['renderer']=='state' and all(r['type']=='transitions_to' for r in rs):
        lines=['stateDiagram-v2']+[f'  state "{mtext(e["name"])}" as {ids[e["id"]]}' for e in es]
        for r in rs:lines+=['  %% relationship-id: '+r['id'],f'  {ids[r["source"]]} --> {ids[r["target"]]}: {mtext(r["label"])}']
    else:
        lines=['flowchart LR','  %% Specialized notation is in the SVG; this source is the complete labelled relation projection.']
        for e in es:lines+=['  %% entity-id: '+e['id'],f'  {ids[e["id"]]}["{mtext(e["name"])}"]']
        for r in rs:
            detail=r['label']+(' / '+json.dumps(r['cardinality'],ensure_ascii=False) if r.get('cardinality') else '')
            lines+=['  %% relationship-id: '+r['id'],f'  {ids[r["source"]]} -->|"{mtext(detail)}"| {ids[r["target"]]}']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('model');p.add_argument('--out',required=True);p.add_argument('--artifact',action='append');p.add_argument('--deliverable',action='append');p.add_argument('--all',action='store_true');p.add_argument('--render',action='store_true');p.add_argument('--view',action='append');p.add_argument('--profile',action='append');p.add_argument('--layout',choices=['reference','adaptive']);p.add_argument('--strict',action='store_true',help='拒绝语义/表达错误；默认保留带缺口草稿');a=p.parse_args()
    if not a.all and not a.artifact and not a.deliverable and not a.view and not a.profile:p.error('至少选择一个 --artifact、--deliverable、--view、--profile 或 --all')
    try:
        result=staged_generate(load_json(a.model),a.out,a.artifact,a.deliverable,a.all,a.render,a.view,a.profile,a.layout,a.strict)
    except subprocess.CalledProcessError as e:p.exit(3 if e.returncode==3 else 1,str(e)+'\n')
    except (ValueError,OSError,RuntimeError) as e:p.exit(1,str(e)+'\n')
    print(f'Generated {len(result["artifacts"])} artifacts, {len(result["deliverables"])} deliverables; rendered={result["rendered"]}')

def staged_generate(model, out, *args):
    """Replace a CLI delivery only after generation succeeds; discard stale files."""
    destination=Path(out).absolute()
    if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
        raise ValueError('Output must be a directory, not a file or symlink')
    if Path.cwd().resolve().is_relative_to(destination.resolve()):
        raise ValueError('Output cannot contain the current working directory')
    if destination.exists():
        manifest=destination/'manifest.json'
        if not manifest.is_file() or json.loads(manifest.read_text()).get('schema_version')!='2.0':
            raise ValueError('Existing output is not a generated delivery; choose a dedicated directory')
    destination.parent.mkdir(parents=True,exist_ok=True)
    staging=Path(tempfile.mkdtemp(prefix='.'+destination.name+'.staging-',dir=destination.parent))
    backup=None
    try:
        result=generate(model,staging,*args)
        if destination.exists():
            backup=destination.with_name('.'+destination.name+'.previous-'+uuid.uuid4().hex)
            os.replace(destination,backup)
        try:
            os.replace(staging,destination)
        except BaseException:
            if backup is not None:os.replace(backup,destination)
            raise
        if backup is not None:shutil.rmtree(backup)
        return result
    finally:
        if staging.exists():shutil.rmtree(staging)
if __name__=='__main__':main()
