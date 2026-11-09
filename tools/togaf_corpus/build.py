#!/usr/bin/env python3
"""Reproducible, source-first conversion of the local TOGAF Series Guides."""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[2]
VERSION = '1.0'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    # Some source PDF metadata contains lone UTF-16 surrogates. Escape those
    # code units in JSON to preserve the exact extraction without invalid UTF-8.
    path.write_bytes(serialized.encode('utf-8', errors='backslashreplace'))


def box(rect):
    return [round(float(v), 3) for v in rect]


def norm(text):
    text = re.sub('[\ud800-\udfff]', '', text)
    return re.sub(r'\s+', ' ', text.replace('\u00ad', '')).strip()


def number(title):
    m = re.match(r'^(?:Appendix\s+)?([A-Z]|\d+)((?:\.\d+)*)[.:：]?\s', title)
    return m[1] + m[2] if m else None


def table_md(rows):
    if not rows:
        return ''
    width = max(map(len, rows))
    cleaned = [[str(c or '').replace('|', '\\|').replace('\n', '<br>') for c in row] + [''] * (width-len(row)) for row in rows]
    return '\n'.join(['| ' + ' | '.join(cleaned[0]) + ' |', '| ' + ' | '.join(['---'] * width) + ' |'] + ['| ' + ' | '.join(r) + ' |' for r in cleaned[1:]])


def outlines(doc, code):
    result, stack = [], []
    for i, (level, title, page, dest) in enumerate(doc.get_toc(False), 1):
        if page < 1:
            continue
        while stack and stack[-1]['level'] >= level:
            stack.pop()
        entry = {'id': f'{code}:s{i:04}', 'level': level, 'title': norm(title), 'raw_title': title,
                 'number': number(title), 'pdf_page': page,
                 'y': round(float(dest.get('to', fitz.Point(0, 0)).y), 3),
                 'parent_id': stack[-1]['id'] if stack else None}
        result.append(entry)
        stack.append(entry)
    for i, entry in enumerate(result):
        stop = next((s for s in result[i+1:] if s['level'] <= entry['level']), None)
        entry['end_pdf_page'] = stop['pdf_page'] if stop else len(doc)
    return result


def paragraph_join(items):
    """Join wrapped prose only; coordinates/raw spans remain available separately."""
    result = []
    for item in items:
        text = item['text']
        prev = result[-1] if result else None
        bullet = bool(re.match(r'^(?:[•◦▪]|\d+\.|[a-z]\))\s', text))
        list_continuation = prev and re.match(r'^(?:[•◦▪]|\d+\.|[a-z]\))\s', prev['text']) and 0 <= item['bbox'][0]-prev['bbox'][0] <= 24
        if item['type'] == 'text' and prev and prev['type'] == 'text' and not bullet and \
                item['bbox'][1] - prev['bbox'][3] < 5 and \
                (abs(item['bbox'][0] - prev['bbox'][0]) < 8 or list_continuation):
            prev['text'] += ' ' + text
            prev['bbox'][2] = max(prev['bbox'][2], item['bbox'][2])
            prev['bbox'][3] = max(prev['bbox'][3], item['bbox'][3])
            prev['source_block_ids'].extend(item['source_block_ids'])
        else:
            result.append(dict(item))
    return result


def split_text(text, limit=6500):
    """Bound retrieval size while retaining every character and source locator."""
    parts = []
    while len(text) > limit:
        cut = text.rfind('\n', 0, limit)
        if cut < limit//2:
            cut = text.rfind(' ', 0, limit)
        if cut < limit//2:
            cut = limit
        else:
            cut += 1
        parts.append(text[:cut]); text = text[cut:]
    if text:
        parts.append(text)
    return parts


def parse_tables(page, code, page_number, blocks):
    # Restrict detection to actual stroked rectilinear borders. Filled glyph outlines,
    # watermarks, and figure paths otherwise produce false columns in these PDFs.
    paths = [d for d in page.get_drawings() if d['type'] == 's' and len(d['items']) <= 4
             and all(i[0] == 're' or i[0] == 'l' and
                     (abs(i[1].x-i[2].x) < .1 or abs(i[1].y-i[2].y) < .1) for i in d['items'])]
    if not paths:
        return []
    finder = page.find_tables(paths=paths, clip=fitz.Rect(30, 30, page.rect.width-30, page.rect.height-30),
                             snap_tolerance=1, join_tolerance=1)
    found = finder.tables
    result = []
    for t in found:
        if t.row_count < 2 or t.col_count < 1:
            continue
        rows = t.extract()
        if sum(bool(norm(c or '')) for row in rows for c in row) < 3:
            continue
        captions = [b for b in blocks if re.match(r'^Table\s+[A-Z\d]+[-.]\d+\s*:', b['text'])
                    and 0 <= t.bbox[1]-b['bbox'][3] < 70]
        caption = norm(captions[-1]['text']) if captions else None
        result.append({'id': f'{code}:p{page_number:04}:t{len(result)+1:02}',
                       'pdf_page': page_number, 'bbox': box(t.bbox), 'caption': caption,
                       'rows': rows, 'row_count': t.row_count, 'column_count': t.col_count,
                       'cell_bboxes': [[box(c) if c else None for c in row.cells] for row in t.rows],
                       'extraction': 'stroked-grid; merged-cell nulls preserved; page fragment',
                       'semantic_review': 'machine-extracted', 'markdown': table_md(rows)})
    # PyMuPDF deliberately omits single-column grids. Reconstruct only vertically
    # contiguous cells with identical borders and an explicit nearby table caption.
    orphan_cells = [c for c in finder.cells if not any((fitz.Rect(t['bbox'])+(-1,-1,1,1)).contains(fitz.Rect(c)) for t in result)]
    groups = collections.defaultdict(list)
    for c in orphan_cells:
        groups[(round(c[0],1), round(c[2],1))].append(c)
    for cells in groups.values():
        cells.sort(key=lambda c:c[1])
        if len(cells) < 2 or any(abs(cells[i][3]-cells[i+1][1]) > 2 for i in range(len(cells)-1)):
            continue
        rect = fitz.Rect(cells[0]) | fitz.Rect(cells[-1])
        caps = [b for b in blocks if re.match(r'^Table\s+[A-Z\d]+[-.]\d+\s*:', b['text']) and 0 <= rect.y0-b['bbox'][3] < 70]
        if not caps:
            continue
        rows = [[page.get_text('text', clip=fitz.Rect(c), sort=True).strip()] for c in cells]
        result.append({'id':f'{code}:p{page_number:04}:t{len(result)+1:02}', 'pdf_page':page_number,
                       'bbox':box(rect), 'caption':norm(caps[-1]['text']), 'rows':rows,
                       'row_count':len(rows), 'column_count':1, 'cell_bboxes':[[box(c)] for c in cells],
                       'extraction':'single-column-stroked-grid', 'semantic_review':'machine-extracted', 'markdown':table_md(rows)})
    return result


def text_blocks(page, code, page_number):
    blocks = []
    for i, b in enumerate(page.get_text('dict', flags=fitz.TEXTFLAGS_DICT & ~fitz.TEXT_PRESERVE_IMAGES)['blocks']):
        if b['type'] != 0:
            continue
        lines = []
        for line in b['lines']:
            spans = [{'text': s['text'], 'bbox': box(s['bbox']), 'font': s['font'],
                      'size': round(s['size'], 3), 'flags': s['flags']} for s in line['spans']]
            lines.append({'text': ''.join(s['text'] for s in spans), 'bbox': box(line['bbox']), 'spans': spans})
        text = '\n'.join(l['text'] for l in lines)
        role = 'body'
        if b['bbox'][3] < 30 or b['bbox'][1] > page.rect.height - 50:
            role = 'running-matter'
        blocks.append({'id': f'{code}:p{page_number:04}:b{i+1:03}', 'bbox': box(b['bbox']),
                       'text': text, 'role': role, 'lines': lines})
    return blocks


def make_items(blocks, tables, sections, page_number):
    items = []
    section_here = [s for s in sections if s['pdf_page'] == page_number]
    rows = []
    for b in blocks:
        if b['role'] != 'body':
            continue
        # Only suppress the text representation when the complete block lies in a table.
        # Any boundary straddling block is retained, favouring duplication over loss.
        r = fitz.Rect(b['bbox'])
        if any((fitz.Rect(t['bbox']) + (-1,-1,1,1)).contains(r) for t in tables):
            continue
        for line in b['lines']:
            rows.append({'bbox': line['bbox'].copy(), 'text': line['text'],
                         'sizes': [s['size'] for s in line['spans']], 'block_ids': [b['id']]})
    # Superscript trademark glyphs frequently split PDF text blocks and have a
    # slightly earlier y coordinate. Reconstruct shared baselines before sorting.
    assembled = []
    for line in sorted(rows, key=lambda r: (r['bbox'][1], r['bbox'][0])):
        match = next((r for r in reversed(assembled[-8:])
                      if abs(r['bbox'][3]-line['bbox'][3]) < 4
                      and min(r['bbox'][3],line['bbox'][3])-max(r['bbox'][1],line['bbox'][1]) >
                      .4*min(r['bbox'][3]-r['bbox'][1],line['bbox'][3]-line['bbox'][1])), None)
        if match:
            match['parts'].append(line)
            match['bbox'] = box(fitz.Rect(match['bbox']) | fitz.Rect(line['bbox']))
        else:
            assembled.append({'bbox': line['bbox'].copy(), 'parts': [line]})
    for row in assembled:
        parts = sorted(row['parts'], key=lambda p:p['bbox'][0])
        text = ''
        for i, part in enumerate(parts):
            gap = part['bbox'][0] - parts[i-1]['bbox'][2] if i else 0
            text += (' ' if i and gap > 1.5 else '') + part['text']
        text = norm(text)
        sizes = [s for p in parts for s in p['sizes']]
        b = {'bbox': row['bbox']}
        matched = next((s for s in section_here if norm(s['title']) == text), None)
        heading = max(sizes, default=0) >= 14 and b['bbox'][0] < 80
        kind = 'heading' if matched or heading else 'caption' if re.match(r'^(?:Figure|Table|Example) [A-Z\d]+[-.]\d+:', text) else 'text'
        item = {'type': kind, 'text': text, 'bbox': b['bbox'].copy(),
                'source_block_ids': list(dict.fromkeys(i for p in parts for i in p['block_ids']))}
        if matched:
            item.update(section_id=matched['id'], heading_level=min(6, matched['level']+1))
        elif heading:
            item['heading_level'] = 3
        items.append(item)
    for t in tables:
        items.append({'type': 'table', 'text': t['markdown'], 'bbox': t['bbox'], 'table_id': t['id'], 'source_block_ids': []})
    items.sort(key=lambda i: (round(i['bbox'][1], 1), i['bbox'][0]))
    return paragraph_join(items)


def active_section(sections, page_number, y):
    candidates = [s for s in sections if s['pdf_page'] < page_number or
                  s['pdf_page'] == page_number and s['y'] <= y+5]
    return candidates[-1] if candidates else None


def chunk_items(items, code, page_number, sections, source, figure_ids):
    chunks, pending, current, length = [], [], None, 0
    def flush():
        nonlocal pending, length
        if not pending:
            return
        sec = current or {}
        chunks.append({'id': f'{code}:p{page_number:04}:c{len(chunks)+1:02}',
                       'document_id': code, 'language': 'en', 'content_role': 'source',
                       'content_kind': 'navigation' if sec.get('title') in ['Table of Contents', 'Contents', 'Index'] else 'body',
                       'section_id': sec.get('id'), 'section_title': sec.get('title'),
                       'text': '\n\n'.join(i['text'] for i in pending), 'pdf_pages': [page_number],
                       'source_sha256': source['sha256'], 'source_path': source['path'],
                       'markdown_path': f'documents/{code}.md#page-{page_number}',
                       'figure_ids': figure_ids, 'table_ids': [i['table_id'] for i in pending if 'table_id' in i],
                       'quality': {'status': 'source-extracted', 'language': 'original', 'semantic_review': 'not-a-translation'},
                       'source_block_ids': [b for i in pending for b in i['source_block_ids']]})
        pending, length = [], 0
    for item in items:
        sec = active_section(sections, page_number, item['bbox'][1])
        if pending and ((sec or {}).get('id') != (current or {}).get('id') or length + len(item['text']) > 7000):
            flush()
        current = sec
        pending.append(item)
        length += len(item['text'])
    flush()
    return chunks


def convert_document(pdf, output, figure_records, embedded_records=()):
    code = pdf.stem[:-1]
    doc = fitz.open(pdf)
    source = {'path': str(pdf.relative_to(ROOT)), 'sha256': sha(pdf), 'bytes': pdf.stat().st_size,
              'page_count': len(doc), 'format': 'pdf'}
    sections = outlines(doc, code)
    title = norm(doc.metadata.get('title') or code)
    legacy = next((ROOT/'togaf-standard-10th-zh').glob(f'{code}e_*.md'), None)
    title_zh = legacy.stem.split('_', 1)[1] if legacy else None
    pages, tables, chunks, captions = [], [], [], []
    pending_caption = None
    markdown = [f'# {title}', '', f'文档：{code} · 英文原文全文 · PDF 共 {len(doc)} 页', '',
                f'来源：`{source["path"]}`；SHA-256：`{source["sha256"]}`。', '',
                '正文按原文提取，中文译文与图片解释另见索引。物理页码从封面起算。跨页表格按页保存，空合并单元格为 null。', '', '## 原文目录', '']
    markdown.extend(f'- [{s["title"]}](#page-{s["pdf_page"]})' for s in sections)
    for page in doc:
        pn = page.number+1
        blocks = text_blocks(page, code, pn)
        ts = parse_tables(page, code, pn, blocks)
        if pending_caption and ts and not ts[0]['caption'] and ts[0]['bbox'][1] < 100:
            ts[0]['caption'] = pending_caption['text']
            ts[0]['caption_pdf_page'] = pending_caption['pdf_page']
        pending_caption = None
        items = make_items(blocks, ts, sections, pn)
        page_figures = [f['id'] for f in figure_records if pn in (f.get('figure', {}).get('en_location') or {}).get('pages', [])]
        page_embedded = [e for e in embedded_records if e['pdf_page'] == pn]
        page_figures += [e['id'] for e in page_embedded if e.get('json_path')]
        for b in blocks:
            if b['role'] == 'body' and re.match(r'^(?:Table|Figure|Example) [A-Z\d]+[-.]\d+:', norm(b['text'])):
                captions.append({'text': norm(b['text']), 'pdf_page': pn, 'bbox': b['bbox']})
                if b['bbox'][1] > page.rect.height-110 and b['text'].startswith('Table '):
                    pending_caption = captions[-1]
        page_record = {'id': f'{code}:p{pn:04}', 'pdf_page': pn, 'printed_page_label': page.get_label(),
                       'width': page.rect.width, 'height': page.rect.height,
                       'raw_text': page.get_text(sort=False), 'reading_order_text': page.get_text(sort=True),
                       'blocks': blocks, 'content': items, 'tables': ts, 'figure_ids': page_figures,
                       'embedded_image_ids': [e['id'] for e in page_embedded],
                       'links': [{'kind': l['kind'], 'bbox': box(l['from']), 'uri': l.get('uri'),
                                  'target_pdf_page': l.get('page', -1)+1 if l.get('page', -1) >= 0 else None} for l in page.get_links()],
                       'images': [{'bbox': box(i['bbox']), 'width': i['width'], 'height': i['height'],
                                   'xref': i.get('xref'), 'digest': i['digest'].hex()} for i in page.get_image_info(hashes=True, xrefs=True)]}
        pages.append(page_record)
        tables.extend(ts)
        chunks.extend(chunk_items(items, code, pn, sections, source, page_figures))
        markdown += ['', f'<a id="page-{pn}"></a>', '', f'## PDF 第 {pn} 页', '']
        for item in items:
            if item['type'] == 'heading':
                markdown.append('#' * item.get('heading_level', 3) + ' ' + item['text'])
            else:
                markdown.append(re.sub(r'^•\s', '- ', item['text']))
            markdown.append('')
        if page_figures:
            markdown += ['本页图片结构：' + ' · '.join(f'[{fid}](../figures/{fid}.md)' for fid in page_figures), '']
        if not items:
            markdown += ['本页无可提取正文。请结合原文页与图片结构读取。', '']
    data = {'schema_version': VERSION, 'id': code, 'title_en': title, 'title_zh': title_zh,
            'content_role': 'source', 'language': 'en', 'source': source,
            'pdf_metadata': doc.metadata, 'outline': sections, 'pages': pages, 'captions': captions,
            'tables': tables, 'figure_ids': [f['id'] for f in figure_records],
            'quality': {'text': 'full-page-text-and-layout-preserved', 'tables': 'automatic-grid-extraction',
                        'interpretation': 'source-not-project-facts'},
            'statistics': {'pages': len(pages), 'sections': len(sections), 'table_fragments': len(tables),
                           'chunks': len(chunks), 'figures': len(figure_records),
                           'text_characters': sum(len(p['raw_text']) for p in pages)}}
    dump(output/'documents'/f'{code}.json', data)
    (output/'documents'/f'{code}.md').write_text('\n'.join(markdown), encoding='utf-8')
    dump(output/'tables'/f'{code}.json', {'document_id': code, 'source': source, 'tables': tables})
    return data, chunks


def convert_translation(path, data, output):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    code = data['id']
    headings = [(i+1, len(m[1]), m[2]) for i, line in enumerate(lines)
                if (m := re.match(r'^(#{1,6})\s+(.+)', line))]
    records, chunks = [], []
    numbered = collections.defaultdict(list)
    for sec in data['outline']:
        if sec['number']:
            numbered[sec['number']].append(sec)
    boundaries = [(1, 0, '前置内容')] + headings if not headings or headings[0][0] != 1 else headings
    for i, (line, level, title) in enumerate(boundaries):
        end = boundaries[i+1][0]-1 if i+1<len(boundaries) else len(lines)
        body = '\n'.join(lines[line-1:end])
        candidates = numbered.get(number(title), [])
        match = candidates[0] if len(candidates) == 1 else None
        rec = {'id': f'{code}:zh:L{line}', 'title': title, 'level': level, 'start_line': line,
               'end_line': end, 'markdown': body, 'source_section_id': match['id'] if match else None,
               'alignment_method': 'section-number-only' if match else 'unmatched',
               'translation_review': 'unverified-against-original'}
        records.append(rec)
        # Split at line boundaries; the full section remains in the document JSON.
        pieces, piece = [], []
        for line_text in body.splitlines():
            if sum(map(len, piece)) + len(line_text) > 6000 and piece:
                pieces.append('\n'.join(piece)); piece = []
            piece.append(line_text)
        if piece:
            pieces.append('\n'.join(piece))
        for j, part in enumerate(pieces, 1):
            chunks.append({'id': rec['id']+f':c{j:02}', 'document_id': code, 'language': 'zh',
                           'content_role': 'translation', 'section_id': rec['source_section_id'],
                           'section_title': title, 'text': part,
                           'pdf_pages': [match['pdf_page']] if match else [],
                           'source_sha256': sha(path), 'source_path': str(path.relative_to(ROOT)),
                           'markdown_path': f'translations/{code}.md', 'figure_ids': [],
                           'quality': {'status': 'translation-unverified', 'alignment': rec['alignment_method'],
                                       'pdf_pages_meaning': 'matched-heading-start-only'}})
    result = {'schema_version': VERSION, 'id': code, 'language': 'zh', 'content_role': 'translation',
              'source': {'path': str(path.relative_to(ROOT)), 'sha256': sha(path)},
              'quality': 'translation-unverified', 'sections': records, 'original_markdown': text}
    dump(output/'translations'/f'{code}.json', result)
    # Keep valid image and document links after relocating the old translation.
    def relocate(m):
        target = m[2]
        if re.match(r'\w+://|#|/', target):
            return m[0]
        return m[1] + '../../togaf-standard-10th-zh/' + target + m[3]
    relocated = re.sub(r'(\]\()([^\s)]+)(\))', relocate, text)
    (output/'translations'/f'{code}.md').write_text(
        '> 既有中文译文辅助层；未将历史译文标作本轮逐句核验结果。准确引用请回到英文原文。\n\n' + relocated, encoding='utf-8')
    return result, chunks


def build(output, only_docs=None, skip_figures=False, skip_architecture=False):
    output.mkdir(parents=True, exist_ok=True)
    if not skip_figures:
        from figures import build_figures
        build_figures(ROOT, output)
    figure_index_path = output/'figures/index.json'
    figure_index = json.loads(figure_index_path.read_text()) if figure_index_path.exists() else {}
    legacy_figures = [json.loads(p.read_text()) for p in sorted((ROOT/'togaf-standard-10th-zh/figs/ai').glob('G*/*.json'))]
    docs, all_chunks, alignments = [], [], []
    for pdf in sorted((ROOT/'togaf-standard-10th').glob('*.pdf')):
        code = pdf.stem[:-1]
        if only_docs and code not in only_docs:
            continue
        figs = [f for f in legacy_figures if f['doc']['code'] == code]
        embedded = [e for e in figure_index.get('embedded_images', []) if e['document_id'] == code]
        data, chunks = convert_document(pdf, output, figs, embedded)
        all_chunks.extend(chunks)
        legacy = next((ROOT/'togaf-standard-10th-zh').glob(f'{code}e_*.md'), None)
        if legacy:
            translation, zh_chunks = convert_translation(legacy, data, output)
            all_chunks.extend(zh_chunks)
            alignments.append({'id': code, 'sections': len(translation['sections']),
                               'number_aligned': sum(bool(s['source_section_id']) for s in translation['sections']),
                               'unmatched': [{'title': s['title'], 'line': s['start_line']} for s in translation['sections'] if not s['source_section_id']]})
        docs.append({'id': code, 'title_en': data['title_en'], 'title_zh': data['title_zh'],
                     'source': data['source'], 'statistics': data['statistics'],
                     'markdown': f'documents/{code}.md', 'json': f'documents/{code}.json',
                     'translation_markdown': f'translations/{code}.md' if legacy else None,
                     'translation_json': f'translations/{code}.json' if legacy else None})
        print(f'{code}: {data["statistics"]}', flush=True)
    for p in sorted((output/'figures').glob('G*/*.json')):
        f = json.loads(p.read_text())
        code = f.get('doc', {}).get('code', p.parent.name)
        if only_docs and code not in only_docs:
            continue
        editorial = f.get('provenance', {}).get('source_role') == 'editorial-added'
        embedded = 'transcription' in f
        semantic_text = '\n'.join(str(v) if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
                                  for k,v in f.get('semantics', {}).items())
        semantic_text += '\n' + json.dumps({k:f.get(k) for k in ['elements','relationships','flows','tables','quality','validation']}, ensure_ascii=False, indent=2)
        semantic_text += '\n' + json.dumps({k:f.get(k) for k in ['description_zh','known_conflicts','current_visual_review']}, ensure_ascii=False, indent=2)
        findings = [{k:v for k,v in finding.items() if not k.startswith('previous_')}
                    for finding in f.get('current_visual_findings', [])]
        semantic_text += '\n本次原图核对：\n' + json.dumps(findings, ensure_ascii=False, indent=2)
        transcriptions = [e['transcription'] for e in f.get('source_extraction', [])]
        if f.get('transcription'):
            transcriptions.append(f['transcription'])
        for trans in transcriptions:
            semantic_text += '\n数字文本：\n' + trans.get('digital_text', '')
            semantic_text += '\nOCR文本（待核对）：\n' + (trans.get('ocr') or {}).get('text', '')
        figure_source = ROOT / f['provenance']['interpretation_path'] if editorial else ROOT/'togaf-standard-10th'/f'{code}e.pdf'
        figure_chunk = {'id': f['id'], 'document_id': code, 'language': 'zh', 'content_role': 'figure',
                           'section_id': None, 'section_title': f.get('figure', {}).get('title_zh'),
                           'text': semantic_text, 'pdf_pages': [f['pdf_page']] if embedded else list(dict.fromkeys((f.get('figure', {}).get('en_location') or {}).get('pages', []))),
                           'source_sha256': sha(figure_source),
                           'source_path': str(figure_source.relative_to(ROOT)),
                           'markdown_path': f'figures/{f["id"]}.md', 'figure_ids': [f['id']],
                           'quality': {'status': 'zh-only-editorial' if editorial else 'embedded-image-extracted' if embedded else 'historical-interpretation-with-source-extraction', 'details': f.get('validation')}}
        parts = split_text(semantic_text)
        for i, part in enumerate(parts, 1):
            all_chunks.append({**figure_chunk, 'id': f'{f["id"]}:c{i:03}', 'text': part,
                               'parent_record_id': f['id'], 'part': i, 'part_count': len(parts)})
    dump(output/'index.json', {'schema_version': VERSION, 'title': 'TOGAF Series Guides · AI-readable corpus',
                              'scope': '26 local Series Guides; not the complete TOGAF 10th Edition Fundamental Content',
                              'extractor': {'name':'tools/togaf_corpus/build.py', 'sha256':sha(Path(__file__)), 'pymupdf_version':fitz.VersionBind},
                              'documents': docs, 'retrieval': 'retrieval/chunks.jsonl', 'figures': 'figures/index.json',
                              'reading_guide': 'reading-guide.json', 'validation_report': 'quality/validation.json',
                              'counts': {'documents':len(docs), 'pages':sum(d['statistics']['pages'] for d in docs),
                                         'sections':sum(d['statistics']['sections'] for d in docs),
                                         'chunks':len(all_chunks), 'table_fragments':sum(d['statistics']['table_fragments'] for d in docs),
                                         **figure_index.get('counts', {})}})
    dump(output/'quality'/'translation-alignment.json', {'method':'section-number alignment is navigation, not semantic equivalence', 'documents': alignments})
    (output/'retrieval').mkdir(exist_ok=True)
    (output/'retrieval/chunks.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in all_chunks), encoding='utf-8')
    write_readme(output, docs)
    if not only_docs and not skip_architecture:
        from architecture_analysis import build as analysis_build
        from roles import build_roles
        from architecture_diagrams import build as diagrams_build
        from build_architecture import integrate
        analysis_build(ROOT, output)
        build_roles(ROOT, output)
        diagrams_build(ROOT, output)
        integrate(ROOT, output)
        from chapter_reviews import build as chapters
        chapters(ROOT, output)


def write_readme(output, docs):
    for extension in ['md', 'json']:
        guide = Path(__file__).with_name('reading-guide.' + extension)
        if guide.exists():
            (output/guide.name).write_bytes(guide.read_bytes())
    text = '''# TOGAF 系列指南 AI 可读语料

以 `togaf-standard-10th/` 中全部 26 份英文 PDF 为源，保存完整正文、表格、图片语义和可追溯检索块。这里是系列指南集合，不等于第 10 版基础标准全集。

## 从这里读取

- [架构解析、图示关系与角色能力](architecture/README.md)：架构实体、方向、分类层级、角色职责及全部参考技能等级。
- [转换覆盖与视觉审校清单](quality/conversion-coverage.md)：全部文档和图像的输出位置、实际覆盖及剩余独立审校范围。
- [当前图片解析](figures/current-analysis.md)：已集成的当前解释与质量状态，关联原图及历史转录。
- [中文阅读导航](reading-guide.md)：各指南用途、核心概念、项目适用场景与原文页码；标记为派生阅读指南。
- `index.json`：文档目录、源文件 SHA-256、页数与路径。
- `documents/*.md`：英文全文；章节和物理页码；正文、列表、表格与图片解释入口。
- `documents/*.json`：全文、PDF 书签层级、原始逐页文本、字体/坐标、链接、表格和来源；`pages[].current_image_analysis` 直接指向当前图示解析。
- `tables/*.json`：真实边框提取的表格片段，保留合并单元格及坐标，跨页不臆测合并。
- `figures/index.json` 和 `figures/<文档>/*.{md,json}`：图片标签、元素、包含关系、箭头、流程、矩阵及解释；原图证据与历史解读分别记录。
- `translations/*.{md,json}`：既有中文全文与章节定位；标记 `translation-unverified`，不宣称已重新完整翻译。
- `retrieval/chunks.jsonl`：可直接供检索使用的内容块；每条带语言、来源角色、物理页码和证据指纹。
- [quality/validation.md](quality/validation.md)：转换覆盖、单元格和来源验证结果；同目录保存中英章节定位报告。

## 项目使用规则

1. 先按主题检索，再读取完整章节及相邻页；不要把目录条目当作正文证据。
2. 以英文 `source` 为引用依据；中文 `translation` 帮助阅读；`figure` 包括历史解释，需同时查看不确定性和冲突。
3. 页码均以 PDF 物理页为准，从封面计为第 1 页。中文章节映射仅通过编号，不证明译文语义等价。
4. 指南中的样例实体、关系和方案不自动构成当前项目事实。
5. 原始文本完整保存在 JSON 的 `pages[].raw_text`；页眉、页脚和水印从整理后正文移除但仍可追溯。
6. 图示的 `flows`、`tables`、`legend` 为当前内容；`source_flows`、`source_tables`、`source_legend` 是归档的历史记录，已从默认架构检索文本排除。按 `quality.visual_review` 读取独立审校范围。

## 构建和查询

在项目根目录执行：

```bash
python3 tools/togaf_corpus/build.py
python3 tools/togaf_corpus/validate.py
python3 tools/togaf_corpus/query.py '业务能力 价值流' --lang en --limit 5
```

依赖和数据模型见 [转换工具说明](../tools/togaf_corpus/README.md)。

## 文档

|编号|中文名称|英文全文|结构化 JSON|页数|
|---|---|---|---|---|
'''
    for d in docs:
        text += f'|{d["id"]}|{d["title_zh"]}|[Markdown]({d["markdown"]})|[JSON]({d["json"]})|{d["statistics"]["pages"]}|\n'
    (output/'README.md').write_text(text, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT/'togaf-standard-10th-ai')
    ap.add_argument('--doc', action='append', help='Convert one document for development; use a separate --output')
    ap.add_argument('--skip-figures', action='store_true', help='Reuse existing figure output')
    ap.add_argument('--skip-architecture', action='store_true', help='Only rebuild the document layer; run build_architecture.py before using existing semantic output')
    args = ap.parse_args()
    if args.doc and args.output.resolve() == (ROOT/'togaf-standard-10th-ai').resolve():
        ap.error('--doc 必须指定独立 --output，避免把正式全量索引覆盖为部分文档')
    build(args.output, args.doc, args.skip_figures, args.skip_architecture)


if __name__ == '__main__':
    main()
