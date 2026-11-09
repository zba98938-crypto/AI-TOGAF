"""Source-bound authoring helpers; never infer review findings from headings."""
from pathlib import Path
import hashlib, json, re

C = Path(__file__).resolve().parents[1]
DATA = C / 'maintenance/fundamental-review-data'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def source(volume):
    p = C / 'fundamental/web-2025/volumes' / volume / 'document.json'
    return p, json.loads(p.read_text())

def numbered_sections(doc):
    """Assign unwrapped figure captions by DOM order, retaining their provenance."""
    current = None
    result = []
    for b in doc['blocks']:
        if re.fullmatch(r'h[2-6]', b['kind']):
            current = None
            if re.match(r'^(?:\d+\.|[A-C][.:])', b['text_en']):
                current = {'heading_id': b['anchor'], 'title_en': b['text_en'], 'blocks': []}
                result.append(current)
        if current is not None:
            current['blocks'].append(b)
    return result

def make_review(volume, notes, figure_notes, table_notes, guide_map, issues=()):
    p, doc = source(volume)
    rows = numbered_sections(doc)
    result = {'schema_version': 'fundamental-semantic-review/1', 'volume_id': volume,
              'source_document_sha256': sha(p), 'source': doc['source'],
              'review_status': 'source-read-section-analysis-authored',
              'review_method_zh': '阅读每个编号标题下的直接正文；中文分析为项目解释，英文原文保持独立。图表读取原图/HTML单元格；图中文字、连线与正文矛盾另记。',
              'sections': [], 'figures': [], 'tables': [], 'source_issues': list(issues)}
    fields = ['concepts_zh','applicability_zh','logic_zh','decisions_zh','artifacts_evidence_zh','limits_zh']
    actual_numbers = {r['title_en'].split(' ', 1)[0].rstrip('.') for r in rows}
    if set(notes) != actual_numbers:
        raise ValueError({'missing': sorted(actual_numbers-set(notes)), 'extra': sorted(set(notes)-actual_numbers)})
    for r in rows:
        n = r['title_en'].split(' ', 1)[0].rstrip('.')
        parts = notes[n].split('|')
        if len(parts) != len(fields):
            raise ValueError((n, len(parts)))
        refs = guide_map.get(n, guide_map.get(n.split('.')[0], []))
        row = {k:r[k] for k in ('heading_id','title_en')}
        row.update({k:[v] if v else [] for k,v in zip(fields,parts)})
        row.update(source_block_ids=[b['id'] for b in r['blocks']],
                   source_content_sha256=hashlib.sha256('\n'.join(b.get('text_en','') for b in r['blocks']).encode()).hexdigest(),
                   source_url=doc['source']['url']+'#'+r['heading_id'],
                   guide_refs=refs, status='authored-source-bound-analysis')
        result['sections'].append(row)
    for kind, supplied in [('img',figure_notes),('table',table_notes)]:
        blocks = [b for b in doc['blocks'] if b['kind']==kind]
        expected = {b['id'].rsplit(':',1)[-1] for b in blocks}
        if expected != set(supplied):
            raise ValueError((kind, expected-set(supplied), set(supplied)-expected))
        for b in blocks:
            local = b['id'].rsplit(':',1)[-1]
            sn = supplied[local]
            parts = sn.split('|')
            if len(parts)!=3:
                raise ValueError((local,len(parts)))
            row = {'block_id': b['id'], 'caption_en': b.get('alt',b.get('text_en','').split('\n')[0]),
                   'semantic_review_zh': parts[0], 'labels_connections_zh': parts[1], 'limits_zh': [parts[2]],
                   'guide_refs': guide_map.get('figure:'+local, guide_map.get(b.get('section_path',[{'title_en':'0'}])[0]['title_en'].split('.')[0],[])),
                   'source_block_sha256':hashlib.sha256(b['html'].encode()).hexdigest(), 'review_status':'source-visual-or-cells-reviewed'}
            if kind=='img':
                row.update(asset_path=str((p.parent/b['local_asset']).relative_to(C)), asset_sha256=sha(p.parent/b['local_asset']))
            else:
                from bs4 import BeautifulSoup
                soup=BeautifulSoup(b['html'],'html.parser')
                row['source_cells']=[[{'text_en':c.get_text(' ',strip=True),'rowspan':int(c.get('rowspan',1)),'colspan':int(c.get('colspan',1))} for c in tr.find_all(['td','th'],recursive=False)] for tr in soup.find_all('tr')]
            result['figures' if kind=='img' else 'tables'].append(row)
    DATA.mkdir(exist_ok=True)
    dest = DATA / (volume+'.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    lines=['# '+doc['title_zh']+'：逐节语义解析','', '来源：本地保存的2025数字版；分析不是官方译文或组织批准。','',
           f"编号标题 {len(rows)}；图片引用 {len(result['figures'])}；提取表 {len(result['tables'])}。源JSON SHA-256：`{sha(p)}`。",'']
    for r in result['sections']:
        lines.extend(['## '+r['title_en'],'',f"[离线原文](../../fundamental/web-2025/volumes/{volume}/index.html#{r['heading_id']})；源块："+', '.join(x.rsplit(':',1)[-1] for x in r['source_block_ids']), ''])
        for field,label in zip(fields,['概念','适用条件','逻辑关系','决策方法','制品与证据','边界']):
            if r[field]: lines.extend([label+'：'+'；'.join(r[field]),''])
        if r['guide_refs']: lines.extend(['指南关联：'+', '.join(r['guide_refs']),''])
    for kind,label in [('figures','原图审查'),('tables','表格审查')]:
        lines.extend(['## '+label,''])
        for r in result[kind]:
            lines.extend(['### '+r['block_id'].rsplit(':',1)[-1]+' '+r['caption_en'],'',r['semantic_review_zh'],'',r['labels_connections_zh'],'','边界：'+'；'.join(r['limits_zh']),''])
    lines.extend(['## 源文问题',''])
    for issue in result['source_issues']:lines.extend([json.dumps(issue,ensure_ascii=False),''])
    dest.with_suffix('.md').write_text('\n'.join(lines)+'\n')
    return result
