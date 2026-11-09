#!/usr/bin/env python3
"""Publish authored, source-compared chapter revisions without certifying old translations.

Mechanical checks bind every reviewed content unit to the PDF extraction. They
prove coverage and provenance, not linguistic equivalence. Unreviewed content
remains explicitly inventoried, including front matter and unprocessed guides.
"""
from __future__ import annotations
import argparse
from collections import Counter
import copy
import json
from pathlib import Path
import re

from build_architecture import write, sha, pieces
from source_paths import resolve as source_path

ROOT=Path(__file__).resolve().parents[3]
MAINTENANCE=Path(__file__).resolve().parents[1]/'chapter-review-data'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def norm(value):
    return re.sub(r'\s+', ' ', value).strip()


def source_units(document):
    return {f'{document["id"]}:p{p["pdf_page"]:04}:c{i:03}':
            {'pdf_page':p['pdf_page'],'index':i,'content':c}
            for p in document['pages'] for i,c in enumerate(p['content'])}


def walk_evidence(value):
    if isinstance(value,dict):
        if 'source_unit_id' in value and 'quote_en' in value:
            yield value
        for item in value.values():yield from walk_evidence(item)
    elif isinstance(value,list):
        for item in value:yield from walk_evidence(item)


def validate_review(review,document,root):
    """Fail on missing, duplicated, stale or invented source coverage."""
    code=document['id'];errors=[];units=source_units(document)
    def check(condition, message):
        if not condition:errors.append(message)
    check(review['document_id']==code,'document ID mismatch')
    check(review['source']==document['source'],'source metadata changed')
    check(sha(source_path(root/document['source']['path']))==review['source']['sha256'],'PDF fingerprint changed')
    legacy=review.get('legacy_translation')
    if legacy:check(sha(source_path(root/legacy['path']))==legacy['sha256'],'legacy translation fingerprint changed')
    outlines={s['id']:s for s in document['outline']}
    dispositions=review['outline_coverage']
    check(Counter(s['source_section_id'] for s in dispositions)==Counter(outlines.keys()),'outline coverage missing or duplicate entries')
    sections=review['sections'];seen=Counter();sectionids=set();reviewed_outlines=set()
    for section in sections:
        sid=section['id'];check(sid not in sectionids,'duplicate section '+sid);sectionids.add(sid)
        check(section['source_section_id'] in outlines,'unknown outline '+sid)
        check(section['source_section_id'] not in reviewed_outlines,'duplicate reviewed outline '+sid)
        reviewed_outlines.add(section['source_section_id'])
        check(bool(section['source_units']),'empty evidence '+sid)
        if section['status']=='section-container':
            check(all(u['type']=='heading' for u in section['source_units']),'container hides body text '+sid)
        else:
            check(section['status']=='source-compared-revised','unknown review status '+sid)
            check(bool(section.get('translation_zh','').strip()),'missing revised translation '+sid)
        check(sorted(set(section['pdf_pages']))==sorted({u['pdf_page'] for u in section['source_units']}),'section page mismatch '+sid)
        for unit in section['source_units']:
            uid=unit['id'];seen[uid]+=1
            check(uid in units,'unknown unit '+uid)
            if uid not in units:continue
            source=units[uid];content=source['content']
            check(unit['pdf_page']==source['pdf_page'] and unit['content_index_zero_based']==source['index'],'unit locator mismatch '+uid)
            check(unit['text_en']==content['text'],'unit text mismatch '+uid)
            check(unit['source_block_ids']==content.get('source_block_ids',[]),'unit block IDs mismatch '+uid)
            check(unit['type']==content['type'],'unit type mismatch '+uid)
        for ref in section.get('structured_references',[]):
            path=root/ref['path'];check(path.is_file(),'missing structured reference '+ref['path'])
            if ref.get('json_pointer') and path.is_file():
                node=read(path)
                try:
                    for key in ref['json_pointer'].strip('/').split('/'):
                        key=key.replace('~1','/').replace('~0','~')
                        node=node[int(key)] if isinstance(node,list) else node[key]
                except (KeyError,IndexError,ValueError,TypeError):check(False,'invalid JSON pointer '+ref['path']+ref['json_pointer'])
    check(all(n==1 for n in seen.values()),'source content unit assigned more than once')
    numbered={s['id'] for s in document['outline'] if s.get('number')}
    missing_numbered=numbered-reviewed_outlines
    check(set(review['coverage'].get('unreviewed_substantive_sections',[]))==missing_numbered,
          'numbered substantive outline coverage claim mismatch: '+str(sorted(missing_numbered)))
    for e in walk_evidence(review):
        # A source issue can cite an unreviewed TOC/front-matter unit. Verify
        # its content without upgrading that whole unit to translated status.
        uid=e['source_unit_id'];check(uid in units,'unknown evidence unit '+uid)
        if uid not in units:continue
        check(norm(e['quote_en']) in norm(units[uid]['content']['text']),'quote not in source unit '+uid)
        check(e['pdf_page']==units[uid]['pdf_page'],'evidence page mismatch '+uid)
        check(e['source_block_ids']==units[uid]['content'].get('source_block_ids',[]),'evidence block IDs mismatch '+uid)
        check(e['source_sha256']==document['source']['sha256'],'evidence PDF fingerprint mismatch '+uid)
        check(e['source_path']==document['source']['path'],'evidence source path mismatch '+uid)
    declared=set(review['coverage']['reviewed_substantive_body_pages'])
    expected={uid for uid,u in units.items() if u['pdf_page'] in declared}
    check(expected<=set(seen),'declared body pages have unreviewed units: '+str(sorted(expected-set(seen))))
    check(review['coverage']['source_content_units']==len(seen),'declared unit count mismatch')
    if errors:raise ValueError(code+':\n'+'\n'.join(errors))
    return {'source_units_checked':len(seen),'source_quotes_checked':sum(1 for _ in walk_evidence(review)),
            'reviewed_section_ids':sorted(reviewed_outlines),'reviewed_source_unit_ids':sorted(seen),
            'all_source_units':len(units),'pending_source_units':[
                {'id':uid,'pdf_page':u['pdf_page'],'type':u['content']['type'],
                 'source_section_id':u['content'].get('section_id')}
                for uid,u in units.items() if uid not in seen]}


def section_anchor(section):
    return section['id'].split(':chapter-review:',1)[1]


def render_markdown(data):
    code=data['document_id'];lines=[f'# {code} · 中文正文校订与章节分析','',
        '[完整 JSON]('+code+'.json) · [英文全文](../documents/'+code+'.md) · [覆盖清单](index.md)','',
        data['review_scope']['method_zh'],'']
    lines += ['- '+x for x in data['review_scope']['limits_zh']]+['','## 章节目录','']
    for s in data['sections']:lines.append(f'- [{s["title_zh"]}](#{section_anchor(s)})')
    for s in data['sections']:
        lines += ['',f'<a id="{section_anchor(s)}"></a>',f'## {s["title_zh"]}','',
            f'原文：{s["title_en"]}。PDF 物理页：{s["pdf_pages"]}。状态：`{s["status"]}`。','',
            s['translation_zh'] or '本节仅为原文标题，正文见所属子节。','']
        for ref in s.get('structured_references',[]):
            rel=Path(ref['path']).relative_to('togaf-standard-10th-ai').as_posix()
            lines.append(f'相关结构化资料：[{ref["kind"]}](../{rel})。'+ref.get('review_scope_zh',''))
        if s.get('semantic_rules'):
            lines+=['','### 语义规则与适用边界','']
            for rule in s['semantic_rules']:
                lines+=['- '+rule['statement_zh']]
                if rule.get('boundary_zh'):lines+=['  - 适用边界：'+rule['boundary_zh']]
                for e in rule['evidence']:lines+=['  - PDF '+str(e['pdf_page'])+'：'+e['quote_en']]
        if s.get('corrections'):
            lines+=['','### 本节校订记录','','```json',json.dumps(s['corrections'],ensure_ascii=False,indent=2),'```']
        standard={'id','source_section_id','section_number','title_en','title_zh','status','translation_mode','pdf_pages',
                  'translation_zh','source_units','semantic_rules','corrections','structured_references'}
        extra={k:v for k,v in s.items() if k not in standard}
        if extra:lines+=['','### 本节结构化补充','','```json',json.dumps(extra,ensure_ascii=False,indent=2),'```']
        lines+=['','### 原文内容单元','','<details><summary>展开英文原文及文本块定位</summary>','']
        for u in s['source_units']:
            lines += [f'**{u["id"]} · PDF {u["pdf_page"]}**','',u['text_en'],'']
        lines+=['</details>']
    lines+=['','## 原文自身的歧义与冲突','','```json',json.dumps(data.get('source_issues',[]),ensure_ascii=False,indent=2),'```','',
            '## 本指南术语约定','','```json',json.dumps(data.get('terminology_zh',[]),ensure_ascii=False,indent=2),'```','']
    extra={k:v for k,v in data.items() if k in {'source_version','source_rights_notice'}}
    if extra:lines+=['## 版本与源文声明','','```json',json.dumps(extra,ensure_ascii=False,indent=2),'```','']
    return '\n'.join(lines)


def retrieval_value(section,review):
    """Current prose with linked context; historical wrong translations stay out."""
    value={k:v for k,v in section.items() if k!='corrections'}
    unit_ids={u['id'] for u in section['source_units']}
    value['source_issues']=[issue for issue in review.get('source_issues',[])
        if any(e['source_unit_id'] in unit_ids for e in walk_evidence(issue))]
    value['terminology_zh']=review.get('terminology_zh',[])
    value['document_context']={k:v for k,v in review.items() if k in {'source_version','source_rights_notice'}}
    return value


def build(root=ROOT,output=None,maintenance=MAINTENANCE):
    root=Path(root);output=Path(output or root/'togaf-standard-10th-ai');maintenance=Path(maintenance)
    catalog=read(output/'index.json');entries=[];chunks=[];checks=[]
    for entry in catalog['documents']:
        code=entry['id'];document=read(output/entry['json']);path=maintenance/(code+'.json')
        units=source_units(document)
        row={'document_id':code,'title_zh':entry['title_zh'],'source':entry['source'],
             'all_source_units':len(units),'all_outline_entries':len(document['outline'])}
        if not path.exists():
            row.update(status='pending-chapter-source-review',reviewed_source_units=0,reviewed_sections=0,
                       pending_source_units=len(units),pending_outline_entries=len(document['outline']))
            entries.append(row);continue
        review=read(path);checked=validate_review(review,document,root)
        payload=copy.deepcopy(review)
        payload['maintenance_source']=str(path.relative_to(root));payload['maintenance_sha256']=sha(path)
        payload['source_unit_coverage']=checked
        payload['verification']={'method':'exact-source-content-and-block-identity-check',
                                 'semantic_acceptance':'not-certified-by-coverage-check',
                                 'pipeline_sha256':sha(Path(__file__))}
        json_path=f'chapters/{code}.json';md_path=f'chapters/{code}.md'
        write(output/json_path,payload)
        (output/md_path).write_text(render_markdown(payload),encoding='utf-8')
        checks.append({'document_id':code,**{k:v for k,v in checked.items() if k.endswith('_checked')}})
        route={'json_path':json_path,'markdown_path':md_path,
               'reviewed_section_ids':checked['reviewed_section_ids'],
               'notice_zh':'中文正文按所列章节对照校订；其余章节及旧译保持原有状态。'}
        document['current_chapter_review']=route
        write(output/entry['json'],document)
        for rel in [entry['markdown'],f'translations/{code}.md']:
            target=output/rel
            if not target.exists():continue
            original=target.read_text(encoding='utf-8')
            original=re.sub(r'(?m)^> 当前章节校订：[^\n]*\n\n?', '',original)
            first,rest=original.split('\n',1)
            target.write_text(first+'\n\n'+f'> 当前章节校订：[MD](../{md_path}) · [JSON](../{json_path})。校订覆盖以记录为准；本文件原有来源状态保留。'+'\n\n'+rest.lstrip('\n'),encoding='utf-8')
        for section in payload['sections']:
            # Corrections stay in the full record as history. Retrieval contains
            # the revised prose, its evidence and current rules, not old errors.
            value=retrieval_value(section,payload)
            text=section['title_zh']+'\n'+json.dumps(value,ensure_ascii=False,indent=2)
            parts=list(pieces(text))
            for i,part in enumerate(parts,1):
                chunks.append({'id':section['id']+f':c{i:03}','parent_record_id':section['id'],
                    'part':i,'part_count':len(parts),'document_id':code,'document_ids':[code],
                    'language':'zh','content_role':'chapter-review','section_id':section['source_section_id'],
                    'section_title':section['title_zh'],'text':part,'pdf_pages':section['pdf_pages'],
                    'source_path':str((output/json_path).relative_to(root)),'source_sha256':sha(output/json_path),
                    'source_locators':[{'document_id':code,'pdf_pages':section['pdf_pages'],**document['source']}],
                    'markdown_path':md_path+'#'+section_anchor(section),'json_path':json_path,'figure_ids':[],
                    'quality':{'status':'authored-analysis-see-evidence','original_text':False,
                               'translation_review':section['status'],'alignment':'section-with-exact-source-content-units',
                               'notice_zh':'章节对照校订，非逐句对齐认证；图形审校见独立图示记录。'}})
        row.update(status=review['review_scope']['status'],json_path=json_path,markdown_path=md_path,
            reviewed_source_units=checked['source_units_checked'],reviewed_sections=len(payload['sections']),
            reviewed_section_ids=checked['reviewed_section_ids'],
            pending_source_units=len(checked['pending_source_units']),
            pending_outline_entries=len(document['outline'])-len(checked['reviewed_section_ids']),
            pending_source_units_path=json_path+'#/source_unit_coverage/pending_source_units')
        entries.append(row)
    counts={'documents':len(entries),'documents_with_chapter_review':sum(bool(e.get('json_path')) for e in entries),
            'reviewed_sections':sum(e['reviewed_sections'] for e in entries),
            'reviewed_source_units':sum(e['reviewed_source_units'] for e in entries),
            'pending_source_units':sum(e['pending_source_units'] for e in entries),
            'pending_outline_entries':sum(e['pending_outline_entries'] for e in entries),
            'retrieval_chunks':len(chunks)}
    report={'schema_version':'chapter-review-coverage/1','counts':counts,'documents':entries,
        'notice_zh':'正文校订与全部文档全译不同。待处理内容包括前置资料和未审指南；源单元覆盖只验证来源与遗漏，不证明译文语义无误。',
        'source_index':'index.json','pipeline_sha256':sha(Path(__file__))}
    write(output/'chapters/index.json',report)
    lines=['# 中文校订与逐章语义覆盖','',report['notice_zh'],'',
        '|指南|已有校订节|已覆盖原文单元|待处理单元|待处理书签|校订入口|','|---|---:|---:|---:|---:|---|']
    for e in entries:
        link=f'[MD]({e["document_id"]}.md) · [JSON]({e["document_id"]}.json)' if e.get('json_path') else '尚未完成'
        lines.append(f'|{e["document_id"]} {e["title_zh"]}|{e["reviewed_sections"]}|{e["reviewed_source_units"]}|{e["pending_source_units"]}|{e["pending_outline_entries"]}|{link}|')
    (output/'chapters/index.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (output/'retrieval/chapter-chunks.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in chunks),encoding='utf-8')
    write(output/'chapters/validation.json',{'passed':True,'scope':'source-unit-and-citation-integrity',
        'semantic_acceptance':'not-certified-by-mechanical-validation','counts':counts,'checks':checks,
        'pipeline_sha256':sha(Path(__file__)),'retrieval_sha256':sha(output/'retrieval/chapter-chunks.jsonl')})
    catalog['chapter_reviews']='chapters/index.json';catalog['chapter_retrieval']='retrieval/chapter-chunks.jsonl'
    write(output/'index.json',catalog)
    for rel in ['README.md','architecture/README.md']:
        p=output/rel
        if not p.exists():continue
        text=p.read_text(encoding='utf-8')
        text=re.sub(r'(?m)^中文章节校订入口：[^\n]*\n\n?', '', text)
        prefix='../' if rel.startswith('architecture/') else ''
        text+='\n中文章节校订入口：['+str(counts['documents_with_chapter_review'])+' 份指南的当前校订与剩余覆盖]('+prefix+'chapters/index.md)；机读记录见 [JSON]('+prefix+'chapters/index.json)。\n'
        p.write_text(text,encoding='utf-8')
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'togaf-standard-10th-ai')
    args=parser.parse_args()
    print(json.dumps(build(output=args.output)['counts'],ensure_ascii=False))
