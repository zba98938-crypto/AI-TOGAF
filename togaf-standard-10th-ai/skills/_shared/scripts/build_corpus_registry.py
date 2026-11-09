"""Inventory all local text, tables, figure interpretations and image assets.

Indexing proves enumeration and source integrity, not human/visual verification.
The script is a maintainer tool; copied skills run without the source corpus.
"""
import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path
from source_dispositions import disposition
from sync_reviewed_figure_sources import current_structure, locate_corpus, sync as sync_reviewed_sources

ROOT=Path(__file__).resolve().parents[1]
CONFLICTS=[
 {'id':'source-g212-fig5-2','figure_id':'G212/fig5-2','status':'observed-conflict',
  'description':'正文§5.1定义C为高普及低变化、D为低普及低变化；本地中文重绘将底部C/D左右位置互换。',
  'evidence':['G212 §5.1','figs/g212_fig5-2.svg','figs/ai/G212/fig5-2.json'],
  'resolution':'采用正文定义：A左上、B右上、C右下、D左下；保留重绘冲突，不将图中位置误植为架构规则。'},
 {'id':'source-g234-fig4-4','figure_id':'G234/fig4-4','status':'observed-conflict',
  'description':'实际英文 PNG 显示规范式／众包式两栏（图4-3内容），正文与JSON语义为技术、数据模型、流程三要素（图4-4）。已有faithful标签不能采信为本轮核验。',
  'evidence':['G234 §4.2.2–4.3','figs/g234e_fig4-4_en.png','figs/ai/G234/fig4-4.json'],
  'resolution':'保留正文可证实三要素与冲突，来源结构模板待取得可信图4-4；不修改原资料。'},
 {'id':'source-g242-fig3-14','figure_id':'G242/fig3-14','status':'observed-conflict',
  'description':'JSON把新增总量884和年度分项69、224、590误读；原图分项和883与总量884有1单位差异，Scope2净值也存在1单位差异。',
  'evidence':['G242 §3.8–3.9','figs/g242_fig3-14_en.png','figs/ai/G242/fig3-14.json'],
  'resolution':'保存原值、列头、算术差异及可能舍入；不得静默更正或认定选项矛盾已消解。'},
 {'id':'source-g234-fig5-1','figure_id':'G234/fig5-1','status':'observed-conflict',
  'description':'JSON摘要五类文档化功能共13项的分项相加为12；一级10组二级30项需按图逐组核对。',
  'evidence':['G234 §5.1','figs/g234e_fig5-1_en.png','figs/ai/G234/fig5-1.json'],
  'resolution':'使用实际分组与元素清单，不把错误摘要数量转为约束。'},
]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def current_g249_structure(source, figure_id):
    """Use the reviewed current graph; never republish a superseded interpretation.

    This is a maintainer-only dependency. The returned record is portable and the
    installed skill does not import the source corpus at runtime.
    """
    return current_structure(locate_corpus(source), figure_id)


def refresh_g249(source):
    """Refresh current G249 semantics without relying on archived review bundles."""
    cap_path = ROOT / 'capabilities.json'
    evidence_path = ROOT / 'evidence-registry.json'
    cap = json.loads(cap_path.read_text())
    evidence = json.loads(evidence_path.read_text())
    profiles = {p['id']: p for p in cap['profiles']}
    methods = {m['id'] for m in cap['analysis_methods']}
    targets = {'G249/fig4-1', 'G249/fig4-2'}
    portable_refs = {'references/source-structures/' + fid.replace('/', '-') + '.json' for fid in targets}
    for profile in profiles.values():
        profile['source_structure_refs'] = [r for r in profile.get('source_structure_refs', []) if r not in portable_refs]
    for fid in sorted(targets):
        portable = current_g249_structure(source, fid)
        ref = 'references/source-structures/' + fid.replace('/', '-') + '.json'
        write(ROOT / ref, portable)
        entry = next(f for f in evidence['figures'] if f['id'] == fid)
        selected = disposition(fid, entry.get('classification', []), set(profiles), methods)
        entry.update(current_source=portable['current_source'], historical_source=portable.get('historical_source'),
                     current_semantic_review='current-source-graph-with-traceable-revisions',
                     purpose_summary=portable['reading'].get('purpose_zh', ''),
                     misreadings=portable['reading'].get('misreadings_zh', []),
                     uncertainty=portable.get('uncertainty', {}),
                     profile_ids=selected['profile_ids'], method_ids=selected['method_ids'],
                     disposition=selected['disposition'], disposition_reason=selected['reason'],
                     implementation_gap=selected.get('implementation_gap'))
        for pid in selected['profile_ids']:
            profiles[pid].setdefault('source_structure_refs', []).append(ref)
        target = next((f for f in cap.get('figure_profiles', []) if f['id'] == fid), None)
        if target is not None:
            target.update({k:entry[k] for k in ['profile_ids','method_ids','disposition','disposition_reason','implementation_gap','current_semantic_review']})
    for p in profiles.values():
        if p['artifact_id'] == 'architecture-skill-matrix':
            p['source_table_refs']=['G249/table5-1','G249/table5-2']
    write(cap_path, cap)
    write(evidence_path, evidence)
    return {'refreshed': sorted(targets), 'historical_review_bundles_required': False}

def guide_code(path):
    """G18Ae_业务模型.md -> G18A; locators stay stable while the source hash is unchanged."""
    return Path(path).stem.split('_')[0][:-1]

def text_inventory(path,source):
    lines=path.read_text().splitlines();headings=[];tables=[];code=guide_code(path)
    for index,line in enumerate(lines):
        m=re.match(r'^(#{1,6})\s+(.+)',line)
        if m:headings.append({'line':index+1,'level':len(m[1]),'title':m[2]})
        # A table separator has cells; a bare --- is a horizontal rule, not a table.
        if index>0 and '|' in line and '|' in lines[index-1] and re.match(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$',line):
            start=index-1;end=index+1
            while end<len(lines) and '|' in lines[end] and lines[end].strip():end+=1
            tables.append({'id':code+':T'+str(start+1),'lines':[start+1,end],
                           'header':lines[start],'row_count':end-index-1,
                           'sha256':hashlib.sha256('\n'.join(lines[start:end]).encode()).hexdigest(),
                           'semantic_review':'not-evaluated'})
    sections=[]
    for i,h in enumerate(headings):
        next_line=headings[i+1]['line'] if i+1<len(headings) else len(lines)+1
        chunk='\n'.join(lines[h['line']-1:next_line-1])
        sections.append({'id':code+':L'+str(h['line']),**h,'end_line':next_line-1,'sha256':hashlib.sha256(chunk.encode()).hexdigest(),
                         'review_status':'indexed-not-equivalent-to-semantic-review'})
    return {'path':str(path.relative_to(source)),'sha256':sha(path),'line_count':len(lines),
            'sections':sections,'tables':tables,'scope':'guide-body-and-appendices-including-reference-front-matter'}

def build(source):
    source=Path(source).resolve();cap=json.loads((ROOT/'capabilities.json').read_text())
    prior_availability={f['id']:f.get('historical_source_availability') for f in cap.get('figure_profiles',[]) if f.get('historical_source_availability')}
    profiles=cap['profiles'];methods=cap['analysis_methods'];figures=[];used_assets=set()
    review_dir=ROOT/'reviews'
    observations={x['figure_id']:x for x in json.loads((review_dir/'tri-source-observations.json').read_text())['observations']}
    triage=json.loads((review_dir/'source-visual-triage.json').read_text())
    visual={x['id']:x for x in triage['reviewed']}
    structure_dir=ROOT/'references/source-structures'
    structure_dir.mkdir(parents=True,exist_ok=True)
    for f in sorted((source/'figs/ai').glob('G*/*.json')):
        d=json.loads(f.read_text());fid=d['id'];assets=[]
        opened=set(observations.get(fid,{}).get('assets_opened',[]))
        thumbnail_asset=visual.get(fid,{}).get('asset')
        for a in d.get('assets',[]):
            relative=a.get('path','').split('#')[0];asset=source/relative
            if asset.is_file():
                item={'path':relative,'kind':a.get('kind'),'exists':True,'sha256':sha(asset),
                      'historical_fidelity':a.get('fidelity'),'historical_issues':a.get('issues_zh',[]),
                      'current_visual_review':'opened-for-detailed-observation' if relative in opened else 'thumbnail-structure-reviewed' if relative==thumbnail_asset else 'not-evaluated'}
                if asset.suffix.lower() in ['.png','.svg'] :used_assets.add(relative)
                assets.append(item)
            else:assets.append({'path':relative,'exists':False,'kind':a.get('kind'),'current_visual_review':'not-evaluated'})
        matched=[p['id'] for p in profiles if fid in p.get('source_refs',[])]
        tags=d.get('classification',{}).get('diagram_types',[])
        code=f.parent.name
        guide_methods=[m['id'] for m in methods if any(s.startswith(code) for s in m['source_refs'])]
        role=disposition(fid,tags,{p['id'] for p in profiles},{m['id'] for m in methods})
        matched=sorted(set(matched+role['profile_ids']))
        guide_methods=role['method_ids']
        originals=[a for a in assets if a.get('kind')=='en_original' and a.get('exists')]
        redraw=[a for a in assets if a.get('kind') in ['zh_redraw_svg','zh_localized'] and a.get('exists')]
        source_status='original-asset-available-unverified' if originals else 'redraw-available-unverified' if redraw else 'json-only'
        portable={'schema_version':'2.0','id':fid,'title':d.get('figure',{}).get('title_zh'),
                  'content_role':'source-interpretation-reference-not-project-facts',
                  'notice':'以下为本地图表解释的便携摘录；不表示已核实官方定义。布局、推测箭头、示例名称和参考分类不能自动转为项目架构事实。',
                  'source_locator':d.get('figure',{}).get('zh_location',{}),
                  'reading':{k:d.get('semantics',{}).get(k) for k in ['purpose_zh','reading_guide_zh','key_points_zh','hierarchy_zh','line_semantics_zh','misreadings_zh']},
                  'elements':d.get('elements',[]),'relationships':d.get('relationships',[]),
                  'flows':d.get('flows',[]),'tables':d.get('tables',[]),'legend':d.get('legend',{}),
                  'uncertainty':d.get('quality',{}),'conflicts':[x for x in CONFLICTS if x['figure_id']==fid],
                  'detailed_observation':observations.get(fid),'visual_structure_review':visual.get(fid)}
        portable_path=structure_dir/(fid.replace('/','-')+'.json')
        if fid in {'G249/fig4-1', 'G249/fig4-2', 'G152/fig3-1'}:
            portable = current_g249_structure(source, fid)
        write(portable_path,portable)
        figures.append({'id':fid,'guide':code,'json_path':str(f.relative_to(source)),'json_sha256':sha(f),
                        'portable_structure':str(portable_path.relative_to(ROOT)),
                        'title':d.get('figure',{}).get('title_zh'),'md_locator':d.get('figure',{}).get('zh_location',{}),
                        'classification':tags,'purpose_summary':d.get('semantics',{}).get('purpose_zh',''),
                        'source_status':source_status,'current_semantic_review':observations.get(fid,{}).get('status','structure-triage-only' if fid in visual else 'no-renderable-source-image'),
                        'source_observation':observations.get(fid),'visual_structure_review':visual.get(fid),
                        'asset_limitation':None if fid in visual else '未提供独立图像或本地SVG不可渲染；正文/JSON记录保留，不能声称已目视核验。',
                        'assets':assets,'profile_ids':matched,'method_ids':guide_methods,'disposition':role['disposition'],
                        'disposition_reason':role['reason'],'implementation_gap':role.get('implementation_gap'),
                        'conflict_ids':[x['id'] for x in CONFLICTS if x['figure_id']==fid],
                        'uncertainty':portable.get('uncertainty',{}),'misreadings':portable.get('reading',{}).get('misreadings_zh',[])})
        if portable.get('current_source'):
            figures[-1]['current_source'] = portable['current_source']
            figures[-1]['historical_source'] = portable.get('historical_source')
            figures[-1]['purpose_summary'] = portable.get('reading',{}).get('purpose_zh','')
            figures[-1]['current_semantic_review'] = 'current-source-graph-with-traceable-revisions'
    images=[]
    opened_assets={a for o in observations.values() for a in o.get('assets_opened',[])}
    thumbnail_assets={v['asset'] for v in visual.values()}
    for p in sorted((source/'figs').rglob('*')):
        if p.is_file() and p.suffix.lower() in ['.png','.svg'] and 'ai' not in p.relative_to(source/'figs').parts:
            rel=str(p.relative_to(source));images.append({'path':rel,'sha256':sha(p),'referenced_by_figure_registry':rel in used_assets,
                                                        'current_visual_review':'opened-for-detailed-observation' if rel in opened_assets else 'thumbnail-structure-reviewed' if rel in thumbnail_assets else 'not-evaluated'})
    docs=[text_inventory(p,source) for p in sorted(source.glob('G*.md'))]
    base=json.loads((ROOT/'artifacts.json').read_text())['artifacts']
    official={'source':'https://publications.opengroup.org/c220','status':'product-page-located-formal-body-not-obtained',
              'notice':'产品页不提供全部正式制品定义；本地译文和图表解析不等于完整基础标准。'}
    result={'schema_version':'2.0','source_corpus':'togaf-standard-10th-zh',
            'verification_notice':'全量机器索引不等于全量三源语义核验或目视验收；历史faithful等标签保留为待复核元数据。',
            'guides':docs,'figures':figures,'image_assets':images,'source_conflicts':CONFLICTS,'official_supplement':[official],
            'counts':{'guides':len(docs),'sections':sum(len(d['sections']) for d in docs),'table_blocks':sum(len(d['tables']) for d in docs),
                      'figure_records':len(figures),'image_files':len(images),'base_artifact_names':len(base),
                      'guide_work_products':len(cap['work_products']),'view_profiles':len(profiles),'analysis_methods':len(methods),
                      'untriaged_figures':sum(f['disposition']=='explicit-source-review-gap' for f in figures),
                      'explicit_view_gaps':sum(f['disposition']=='explicit-view-capability-gap' for f in figures),
                      'detailed_three_source_observations':len(observations),'source_image_structure_reviews':len(visual)}}
    cap['figure_profiles']=[{k:f[k] for k in ['id','profile_ids','method_ids','disposition','disposition_reason','implementation_gap','source_status','current_semantic_review','conflict_ids']} for f in figures]
    for row in figures+cap['figure_profiles']:
        if row['id'] in prior_availability:row['historical_source_availability']=prior_availability[row['id']]
    for p in profiles:p['source_structure_refs']=[]
    for f in figures:
        for p in profiles:
            if p['id'] in f['profile_ids']:
                p['source_structure_refs'].append(f['portable_structure'])
    marker='## 便携来源结构与解释'
    for p in profiles:
        path=ROOT/'references/profiles'/(p['id']+'.md')
        body=path.read_text().split(marker)[0].rstrip()
        if p['source_structure_refs']:
            body+='\n\n'+marker+'\n\n以下保留来源图的元素、关系解释、图例、误读和不确定性。先核对其内容角色，再按本地范围重新建模；不能把参考实体或推测关系直接当作项目事实。\n\n'
            body+='\n'.join('- ['+Path(ref).stem+'](../source-structures/'+Path(ref).name+')' for ref in p['source_structure_refs'])
        path.write_text(body+'\n')
    write(ROOT/'capabilities.json',cap);write(ROOT/'evidence-registry.json',result)
    sync_reviewed_sources(ROOT, locate_corpus(source))
    cap=json.loads((ROOT/'capabilities.json').read_text())
    result=json.loads((ROOT/'evidence-registry.json').read_text())
    write_index(cap,result,base)
    return result

def write_index(cap,registry,base):
    text='# 全量来源与能力入口\n\n'
    text+='本索引将原70项制品名称、指南工作产品、视图模板、分析方法分开计数。存在条目不等于已完成生成、语义或视觉验收。\n\n'
    text+='机器索引统计：'+json.dumps(registry['counts'],ensure_ascii=False)+'。\n\n'
    text+='[既有70项与22项交付物](coverage.md) · [共享工作流](workflow-v2.md)\n\n'
    text+='## 指南新增工作产品\n\n|ID|工作产品|来源|主责技能|\n|---|---|---|---|\n'
    for w in cap['work_products']:
        text+='|'+w['id']+'|['+w['name_zh']+'](capabilities/'+w['id']+'.md)|'+'；'.join(w['source_refs'])+'|['+w['owner']+'](../../'+w['owner']+'/SKILL.md)|\n'
    text+='\n## 视图模板\n\n|ID|表达|制品族|构图|来源|\n|---|---|---|---|---|\n'
    for p in cap['profiles']:text+='|'+p['id']+'|['+p['name']+'](profiles/'+p['id']+'.md)|'+p['artifact_id']+'|'+p['renderer']+'|'+'；'.join(p['source_refs'])+'|\n'
    text+='\n## 分析方法\n\n|ID|方法|主责|来源|\n|---|---|---|---|\n'
    for m in cap['analysis_methods']:text+='|'+m['id']+'|['+m['name']+'](analysis-methods/'+m['id']+'.md)|'+m['owner']+'|'+'；'.join(m['source_refs'])+'|\n'
    text+='\n## 尚需核验的来源表达\n\n'
    text+='每张图已区分视图入口、方法证据、参考分类、记法/截图及明确缺口；这些处置不表示全面语义等价。完整清单、目视层级、缺图和来源冲突见 ../evidence-registry.json。\n'
    (ROOT/'references/capability-coverage.md').write_text(text)

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--source',type=Path,default=ROOT.parents[1]/'togaf-standard-10th-zh');parser.add_argument('--refresh-g249',action='store_true',help='Update current G249 records without archived review bundles');a=parser.parse_args()
    if not a.source.is_dir():parser.error('需要显式提供用于维护审计的源目录；技能正常生成不依赖该目录。')
    result=refresh_g249(a.source) if a.refresh_g249 else build(a.source);print(json.dumps(result if a.refresh_g249 else result['counts'],ensure_ascii=False))

if __name__=='__main__':main()
