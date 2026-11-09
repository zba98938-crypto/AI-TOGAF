#!/usr/bin/env python3
"""Inventory every acquired unit and prepare local, unexecuted independent-review shards.

Source text, raw PDF fragments, images, front matter and navigation are retained.
Classification rules are provisional dispositions, never model or human acceptance.
"""
from collections import Counter, defaultdict
import argparse
import bisect
import hashlib
import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[2]
C = REPO / 'togaf-standard-10th-ai'
CATEGORIES = {'body', 'front-matter', 'navigation', 'reference'}
NAV = re.compile(r'^(?:table of contents|contents|list of (?:figures|tables)|index|目录|目次|索引)(?:\b|$)', re.I)
FRONT = re.compile(r'^(?:preface|foreword|acknowledg\w*|trademarks?|participants?|contributors?|about (?:the |this )?(?:author|document)|序言|前言|致谢|商标|版权)(?:\b|$)', re.I)
REFERENCE = re.compile(r'^(?:references|bibliography|recommended reading|referenced documents|acronyms\s*(?:&|and)\s*abbreviations|参考文献|参考资料|引用文献)(?:\b|$)', re.I)


def norm(text):
    return re.sub(r'\s+', ' ', text or '').strip()


def textsha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def stripped_title(text):
    return re.sub(r'^(?:\d+(?:\.\d+)*\.?|[A-Z][.:]?)\s+', '', norm(text))


def classify(text, titles=(), *, role=None, explicit_navigation=False, before_body=False, source_chinese=False):
    """Context matters: a Reference Model is substantive body, not bibliography."""
    rows = [stripped_title(t) for t in titles if t]
    if explicit_navigation or role == 'running-matter' or any(NAV.search(t) for t in rows):
        category, rule, confidence = 'navigation', 'explicit-navigation-or-running-matter', 'context-supported'
    elif any(REFERENCE.search(t) for t in reversed(rows)):
        category, rule, confidence = 'reference', 'bibliographic-section-context', 'context-supported'
    elif any(FRONT.search(t) for t in rows):
        category, rule, confidence = 'front-matter', 'front-matter-section-context', 'context-supported'
    elif before_body:
        category, rule, confidence = 'front-matter', 'before-first-substantive-heading', 'provisional'
    elif rows:
        category, rule, confidence = 'body', 'substantive-section-context', 'context-supported'
    else:
        category, rule, confidence = 'body', 'unassigned-source-requires-adjudication', 'uncertain'
    if not norm(text):
        confidence = 'uncertain'
    disposition = {'body': '核对正文及图表；缺少正文译写时补齐，原文与解释分别保留',
                   'front-matter': '保留出版、版权、前置说明；核对处理方式，不计作业务正文认证',
                   'navigation': '保留导航与版面定位；核对链接和文本，不计作正文译写覆盖',
                   'reference': '保留引文及书目信息；核对指向，不推定被引用材料已获取或获验收'}[category]
    if source_chinese:
        disposition += '；来源本身为中文，不虚构翻译行为'
    return {'classification': category, 'classification_basis': {'rule': rule, 'section_titles': rows,
            'raw_role': role, 'confidence': confidence}, 'disposition': disposition,
            'classification_status': 'pending-independent-adjudication'}


def outline_context(outline, page, y=0):
    ordered = sorted(enumerate(outline), key=lambda pair: (pair[1]['pdf_page'], pair[1].get('y', 0), pair[0]))
    candidates = [entry for _, entry in ordered if (entry['pdf_page'], entry.get('y', 0)) <= (page, y)]
    if not candidates:
        return []
    by_id = {item['id']: item for item in outline}
    entry = candidates[-1]
    result, seen = [], set()
    while entry and entry['id'] not in seen:
        seen.add(entry['id']); result.append(entry)
        entry = by_id.get(entry.get('parent_id'))
    return list(reversed(result))


def bounded(path, root=REPO):
    root = Path(root).resolve(); path = Path(path)
    if not path.is_absolute():
        path = root / path
    if not path.resolve().is_relative_to(root):
        raise ValueError('Source escapes repository: ' + str(path))
    cursor = root
    for part in path.relative_to(root).parts:
        cursor /= part
        if cursor.is_symlink():
            raise ValueError('Source symlink forbidden: ' + str(path))
    return path.resolve()


class Inventory:
    def __init__(self, root=REPO):
        self.root = Path(root).resolve()
        self.c = self.root / 'togaf-standard-10th-ai'
        self.inputs, self.units, self.documents, self.contexts, self.editorial = {}, [], [], {}, []
        self.ids = set()
        migration = self.c / 'sources/relocation-manifest.json'
        self.migration = self.read(migration).get('logical_paths', {}) if migration.is_file() else {}

    def reference(self, path, expected=None):
        path = bounded(path, self.root)
        fingerprint = sha(path)
        if expected is not None and fingerprint != expected:
            raise ValueError('Source fingerprint conflict: ' + str(path))
        relative = path.relative_to(self.root).as_posix()
        if relative in self.inputs and self.inputs[relative] != fingerprint:
            raise ValueError('Input changed while reading: ' + relative)
        self.inputs[relative] = fingerprint
        return {'path': relative, 'sha256': fingerprint}

    def source_ref(self, logical, expected):
        absolute = (self.c / logical).resolve() if logical.startswith('../') else self.root / logical
        original = absolute.relative_to(self.root).as_posix()
        target = self.c / self.migration[original] if original in self.migration else absolute
        return {**self.reference(target, expected), 'logical_path': logical}

    def read(self, path):
        ref = self.reference(path)
        return json.loads((self.root / ref['path']).read_text(encoding='utf-8'))

    def optional(self, path):
        return self.read(path) if path.is_file() else None

    def candidate(self, path, pointer, text, alignment, *, status='source-aligned-pending-independent-review'):
        ref = self.reference(path)
        key = ref['path'] + '#' + pointer
        self.contexts[key] = {'reference': ref, 'json_pointer': pointer, 'text_zh': text,
                              'alignment': alignment, 'status': status,
                              'independent_review_status': 'pending'}
        return {'context_id': key, 'reference': ref, 'json_pointer': pointer,
                'text_sha256': textsha(text), 'alignment': alignment, 'status': status}

    def add(self, unit, *, titles=(), role=None, before_body=False, navigation=False, chinese=False):
        if unit['id'] in self.ids:
            raise ValueError('Duplicate source unit: ' + unit['id'])
        self.ids.add(unit['id'])
        for field in ('text_en', 'text_zh'):
            if field in unit and unit[field] is None:
                unit[field] = ''
        unit.update(classify(unit.get('text_en', unit.get('text_zh', '')), titles,
                    role=role, explicit_navigation=navigation, before_body=before_body, source_chinese=chinese))
        unit['review_status'] = 'not-executed'
        unit['independent_model_review'] = False
        unit['human_professional_acceptance'] = 'pending'
        unit['organizational_approval'] = 'pending-signature'
        unit.setdefault('translation_candidates', [])
        unit.setdefault('source_material_form', 'text')
        candidates = unit['translation_candidates']
        if chinese:
            state = 'original-chinese-source-preserved'
        elif unit['source_material_form'] in {'image', 'visual-label'}:
            state = 'original-visual-source-preserved-independent-review-pending'
        elif candidates:
            state = 'candidate-translation-present-independent-review-pending'
        elif unit['classification'] != 'body':
            state = 'source-preserved-nonbody-disposition-pending'
        elif not norm(unit.get('text_en', '')):
            state = 'source-empty-or-unreadable-requires-adjudication'
        else:
            state = 'body-translation-missing'
        unit['translation_status'] = state
        self.units.append(unit)

    def guide(self, path):
        doc = self.read(path); code = doc['id']
        docref = self.reference(path)
        source = self.source_ref(doc['source']['path'], doc['source']['sha256'])
        review_path = self.c / 'chapters' / (code + '.json')
        review = self.optional(review_path)
        translated = defaultdict(list)
        if review:
            if review['source']['sha256'] != doc['source']['sha256']:
                raise ValueError('Guide review source fingerprint differs: ' + code)
            for si, section in enumerate(review['sections']):
                candidate_text = section.get('translation_zh', '')
                alignment, pointer = 'section', '/sections/' + str(si)
                if not candidate_text.strip() and section.get('status') == 'section-container' and all(u['type']=='heading' for u in section['source_units']):
                    candidate_text = section.get('title_zh', '')
                    alignment, pointer = 'section-title', pointer + '/title_zh'
                if not candidate_text.strip():
                    continue
                candidate = self.candidate(review_path, pointer, candidate_text, alignment)
                for unit in section.get('source_units', []):
                    translated[unit['id']].append((unit['text_en'], candidate))
        first_body = min((o['pdf_page'] for o in doc['outline'] if o.get('number')), default=10**9)
        all_blocks, mapped = {}, set()
        visual_regions = defaultdict(list)
        figure_index = self.optional(self.c / 'figures/index.json')
        if figure_index:
            for record in figure_index['figures']:
                if record['document_id'] != code:
                    continue
                figure = self.read(self.c / record['json_path'])
                for area in figure.get('source_extraction', []):
                    visual_regions[area['pdf_page']].append(area['bbox_pdf_points'])
        for pi, page in enumerate(doc['pages']):
            raw = {b['id']: b for b in page['blocks']}; all_blocks.update(raw)
            for ci, content in enumerate(page['content']):
                identity = f'{code}:p{page["pdf_page"]:04}:c{ci:03}'
                fragments = []
                for bid in content.get('source_block_ids', []):
                    if bid not in raw:
                        raise ValueError('Unknown raw PDF source block: ' + bid)
                    mapped.add(bid); b = raw[bid]
                    fragments.append({'id': bid, 'text': b['text'], 'text_sha256': textsha(b['text']),
                                      'bbox': b['bbox'], 'role': b.get('role')})
                context = outline_context(doc['outline'], page['pdf_page'], content.get('bbox', [0, 0])[1])
                unit = {'id': identity, 'document_id': code, 'family': 'series-guide', 'kind': 'pdf-content',
                        'text_en': content['text'], 'source_content_sha256': textsha(content['text']),
                        'source_document': docref, 'source': source,
                        'source_locator': {'json_pointer': f'/pages/{pi}/content/{ci}', 'pdf_page': page['pdf_page'],
                                           'content_index_zero_based': ci, 'bbox': content.get('bbox'),
                                           'source_block_ids': content.get('source_block_ids', [])},
                        'source_fragments': fragments, 'source_type': content['type'],
                        'translation_candidates': [ref for text, ref in translated[identity] if text == content['text']]}
                if translated[identity] and not unit['translation_candidates']:
                    raise ValueError('Guide candidate no longer matches source unit: ' + identity)
                self.add(unit, titles=[r['title'] for r in context], before_body=page['pdf_page'] < first_body)
            if not page['content'] and not page['blocks']:
                self.add({'id': code + f':p{page["pdf_page"]:04}:empty-source-page', 'document_id': code,
                          'family': 'series-guide', 'kind': 'pdf-page', 'text_en': page.get('raw_text', ''),
                          'source_document': docref, 'source': source,
                          'source_locator': {'json_pointer': f'/pages/{pi}', 'pdf_page': page['pdf_page']}},
                          before_body=page['pdf_page'] < first_body)
        raw_extras = 0
        for pi, page in enumerate(doc['pages']):
            for bi, block in enumerate(page['blocks']):
                if block['id'] in mapped:
                    continue
                raw_extras += 1
                context = outline_context(doc['outline'], page['pdf_page'], block['bbox'][1])
                box = block['bbox']; center = ((box[0] + box[2])/2, (box[1] + box[3])/2)
                visual = any(b[0] <= center[0] <= b[2] and b[1] <= center[1] <= b[3] for b in visual_regions[page['pdf_page']])
                table_candidates, table_units = [], []
                for ci, content in enumerate(page['content']):
                    if content['type'] != 'table':
                        continue
                    bbox = content['bbox']
                    if not (bbox[0] <= center[0] <= bbox[2] and bbox[1] <= center[1] <= bbox[3]):
                        continue
                    tabletext = norm(content['text'].replace('<br>', ' ').replace('|', ' '))
                    if not all(norm(line) in tabletext for line in block['text'].splitlines() if norm(line)):
                        continue
                    identity = f'{code}:p{page["pdf_page"]:04}:c{ci:03}'
                    table_units.append(identity)
                    table_candidates.extend(ref for text, ref in translated[identity] if text == content['text'])
                self.add({'id': block['id'], 'document_id': code, 'family': 'series-guide', 'kind': 'pdf-unmapped-raw-block',
                          'text_en': block['text'], 'source_content_sha256': textsha(block['text']),
                          'source_document': docref, 'source': source,
                          'source_material_form': 'visual-label' if visual else 'table-cell' if table_units else 'text',
                          'related_normalized_table_units':table_units,
                          'table_lineage_basis':'PDF center within table bounds and every nonempty raw line occurs in normalized table' if table_units else None,
                          'translation_candidates':table_candidates,
                          'raw_normalization_status': 'not-represented-by-content-unit',
                          'source_locator': {'json_pointer': f'/pages/{pi}/blocks/{bi}', 'pdf_page': page['pdf_page'], 'bbox': box}},
                          titles=[r['title'] for r in context], role=block.get('role'), before_body=page['pdf_page'] < first_body)
        figure_units = 0
        if figure_index:
            for collection in ('figures', 'embedded_images'):
                for fi, record in enumerate(figure_index[collection]):
                    if record['document_id'] != code:
                        continue
                    if collection == 'figures' and record.get('source_role') == 'editorial-added':
                        self.editorial.append({'id':record['id'],'reference':self.reference(self.c / record['json_path']),
                                               'disposition':'preserved historical editorial graph, not an original source unit'})
                        continue
                    figure_units += 1
                    assets = []
                    if collection == 'figures':
                        figure = self.read(self.c / record['json_path'])
                        assets = [self.reference(self.c / a['image_path'], a['image_sha256']) for a in figure.get('source_extraction', [])]
                    else:
                        if record.get('image_path'):
                            assets = [self.reference(self.c / record['image_path'], record['image_sha256'])]
                        else:
                            for identity in record.get('figure_ids', []):
                                linked = next(row for row in figure_index['figures'] if row['id'] == identity)
                                figure = self.read(self.c / linked['json_path'])
                                assets.extend(self.reference(self.c / a['image_path'], a['image_sha256']) for a in figure.get('source_extraction', []) if a['pdf_page'] == record['pdf_page'])
                            if not assets:
                                raise ValueError('Source image occurrence has no local original crop: ' + record['id'])
                    pages = record.get('pdf_pages') or ([record['pdf_page']] if record.get('pdf_page') else [])
                    page = min(pages) if pages else None
                    context = outline_context(doc['outline'], page, record.get('bbox_pdf_points', [0, 30])[1]) if page else []
                    self.add({'id': 'source-image:' + record['id'], 'document_id': code, 'family': 'series-guide', 'kind': collection,
                              'text_en': record.get('title_en', ''), 'source_material_form': 'image', 'source': source,
                              'source_document': self.reference(self.c / 'figures/index.json'), 'source_images': assets,
                              'source_locator': {'json_pointer': f'/{collection}/{fi}', 'pdf_page': page},
                              'historical_interpretation_status': 'separate-candidate-not-certified',
                              'source_location_status': 'located' if page else 'historical-record-source-locator-missing'},
                              titles=[r['title'] for r in context], before_body=page is not None and page < first_body)
        self.documents.append({'document_id': code, 'family': 'series-guide', 'source_document': docref,
                               'pdf_content_units': sum(len(p['content']) for p in doc['pages']),
                               'raw_source_blocks': len(all_blocks), 'raw_blocks_represented': len(mapped),
                               'unmapped_raw_block_units': raw_extras, 'image_units': figure_units,
                               'source_pages': len(doc['pages']), 'raw_block_closure_complete': len(mapped)+raw_extras == len(all_blocks)})

    def foundation(self, path):
        doc = self.read(path); volume = path.parent.name; code = doc['id']; docref = self.reference(path)
        source = self.reference(self.c / doc['source']['html_path'], doc['source']['html_sha256'])
        self.reference(self.c / doc['source']['mhtml_path'], doc['source']['mhtml_sha256'])
        translated = {}
        zhpath = self.c / 'fundamental/chinese-text' / (volume + '.json'); zh = self.optional(zhpath)
        if zh:
            if zh['source_document_sha256'] != docref['sha256']:
                raise ValueError('Foundation candidate source changed: ' + volume)
            for i, block in enumerate(zh.get('blocks', [])):
                translated[block['source_block_id']] = (block.get('text_en', ''), self.candidate(zhpath, f'/blocks/{i}', block.get('text_zh', ''), 'unit'))
        before = True
        for i, block in enumerate(doc['blocks']):
            titles = [p['title_en'] for p in block.get('section_path', [])]
            if any(re.match(r'^(?:\d+\.|[A-C][.:])', t) for t in titles):
                before = False
            candidates = []
            if block['id'] in translated:
                text, candidate = translated[block['id']]
                if text != block.get('text_en', ''):
                    raise ValueError('Foundation candidate text changed: ' + block['id'])
                if norm(self.contexts[candidate['context_id']]['text_zh']):
                    candidates.append(candidate)
            unit = {'id': block['id'], 'document_id': code, 'family': 'fundamental', 'kind': 'web-block',
                    'source_type': block['kind'], 'text_en': block.get('text_en', ''),
                    'source_content_sha256': textsha(block.get('text_en', '')),
                    'source_document': docref, 'source': source,
                    'source_locator': {'json_pointer': f'/blocks/{i}', 'anchor': block.get('anchor'),
                                       'source_dom_order': block.get('source_dom_order')}, 'translation_candidates': candidates}
            if block['kind'] == 'img':
                unit['source_material_form'] = 'image'
                if not block.get('local_asset'):
                    raise ValueError('Foundation image missing local asset: ' + block['id'])
                unit['source_images'] = [self.reference(path.parent / block['local_asset'])]
            self.add(unit, titles=titles, before_body=before)
        for i, link in enumerate(doc.get('toc', [])):
            self.add({'id': code + f':navigation:{i:05}', 'document_id': code, 'family': 'fundamental',
                      'kind': 'navigation-entry', 'text_en': link.get('text_en', ''), 'href_preserved_never_fetched': link['href'],
                      'source_document': docref, 'source': source, 'source_locator': {'json_pointer': f'/toc/{i}'}}, navigation=True)
        for i, footnote in enumerate(doc.get('footnotes', [])):
            candidates = []
            if zh:
                for zi, row in enumerate(zh.get('footnotes', [])):
                    if row['id'] == footnote['id']:
                        if row['text_en'] != footnote['text_en']:
                            raise ValueError('Foundation footnote candidate source differs: ' + footnote['id'])
                        candidates.append(self.candidate(zhpath, f'/footnotes/{zi}', row['text_zh'], 'footnote'))
            self.add({'id': code + ':footnote:' + footnote['id'], 'document_id': code, 'family': 'fundamental',
                      'kind': 'footnote', 'text_en': footnote['text_en'], 'source_document': docref, 'source': source,
                      'translation_candidates': candidates,
                      'source_locator': {'json_pointer': f'/footnotes/{i}', 'anchor': footnote['id']}})
        self.documents.append({'document_id': code, 'family': 'fundamental', 'source_document': docref,
                               'web_blocks': len(doc['blocks']), 'navigation_units': len(doc.get('toc', [])),
                               'footnote_units': len(doc.get('footnotes', [])), 'source_block_closure_complete': True})

    def supplement(self, path):
        review = self.read(path); code = review['document_id']; sourcepath = self.c / review['source_extraction_path']
        extracted = self.read(sourcepath); docref = self.reference(sourcepath, review['source_extraction_sha256'])
        source = self.source_ref(review['source_path'], review['source_pdf_sha256'])
        zhpath = self.c / ('supplementary/chinese-text/G226.json' if code == 'G226' else 'supplementary/chinese-text/W242C-source.json')
        zh = self.optional(zhpath)
        if zh and zh['source_extraction_sha256'] != docref['sha256']:
            raise ValueError('Supplementary candidate source changed: ' + code)
        if code == 'G226':
            translated, sections = {}, {}
            if zh:
                for i, section in enumerate(zh['sections']):
                    candidate = self.candidate(zhpath, f'/sections/{i}', section.get('text_zh', ''), 'section')
                    for b in section['source_blocks']:
                        translated[b['id']] = (b['text_en'], candidate)
            for section in extracted['sections']:
                for bid in section['source_block_ids']:
                    sections[bid] = section['title_en']
            first_body = min(s['pdf_page_start'] for s in extracted['sections'])
            unnumbered_title = None
            for i, block in enumerate(extracted['blocks']):
                candidate = translated.get(block['id'])
                if candidate and candidate[0] != block['text_en']:
                    raise ValueError('G226 candidate source text differs: ' + block['id'])
                box = block['bbox']; running = box[1] > 735 or box[3] < 30
                if REFERENCE.search(norm(block['text_en'])):
                    unnumbered_title = norm(block['text_en'])
                self.add({'id': block['id'], 'document_id': code, 'family': 'supplementary', 'kind': 'pdf-source-block',
                          'text_en': block['text_en'], 'source_content_sha256': textsha(block['text_en']),
                          'source_document': docref, 'source': source,
                          'source_locator': {'json_pointer': f'/blocks/{i}', 'pdf_page': block['pdf_page'], 'bbox': box},
                          'translation_candidates': [candidate[1]] if candidate and norm(self.contexts[candidate[1]['context_id']]['text_zh']) else []},
                          titles=[sections[block['id']]] if block['id'] in sections else [unnumbered_title] if unnumbered_title else [],
                          before_body=block['pdf_page'] < first_body, role='running-matter' if running else None)
            count = len(extracted['blocks'])
        else:
            page_sections = defaultdict(list)
            for section in review['sections']:
                for page in section.get('pdf_pages', []):
                    page_sections[page].append(section.get('title_zh', ''))
            for i, page in enumerate(extracted['pages']):
                candidate = []
                if zh:
                    original = next((p for p in zh['pages'] if p['pdf_page'] == page['pdf_page']), None)
                    if not original or original['text_zh'] != page['text']:
                        raise ValueError('W242C Chinese source differs: page ' + str(page['pdf_page']))
                    candidate = [self.candidate(zhpath, '/pages/' + str(i), original['text_zh'], 'source-page', status='original-Chinese-source-not-a-translation')]
                self.add({'id': code + f':p{page["pdf_page"]:04}', 'document_id': code, 'family': 'supplementary', 'kind': 'pdf-page',
                          'text_zh': page['text'], 'source_content_sha256': textsha(page['text']), 'source_document': docref, 'source': source,
                          'source_image_occurrences': page.get('image_count'),
                          'source_locator': {'json_pointer': f'/pages/{i}', 'pdf_page': page['pdf_page']}, 'translation_candidates': candidate},
                          titles=page_sections[page['pdf_page']], before_body=page['pdf_page'] < 6, chinese=True)
            count = len(extracted['pages'])
        for i, figure in enumerate(review.get('figures', [])):
            imagepath = figure.get('render_path') or figure.get('asset_path')
            fingerprint = figure.get('render_sha256') or figure.get('asset_sha256')
            images = [self.reference(self.c / imagepath, fingerprint)] if imagepath else []
            self.add({'id': figure.get('figure_id') or figure['id'], 'document_id': code, 'family': 'supplementary', 'kind': 'source-figure',
                      'text_en': figure.get('caption_en', ''), 'source_material_form': 'image', 'source_images': images,
                      'source_document': self.reference(path), 'source': source,
                      'source_locator': {'json_pointer': f'/figures/{i}', 'pdf_pages': figure.get('pdf_pages', [])}},
                      titles=['Substantive source figure'], chinese=code == 'W242C')
        self.documents.append({'document_id': code, 'family': 'supplementary', 'source_document': docref,
                               'source_units': count, 'source_figure_units': len(review.get('figures', [])),
                               'source_unit_closure_complete': True})

    def build(self):
        for path in sorted((self.c / 'documents').glob('*.json')):
            self.guide(path)
        for path in sorted((self.c / 'fundamental/web-2025/volumes').glob('*/document.json')):
            self.foundation(path)
        for code in ('G226', 'W242C'):
            self.supplement(self.c / 'supplementary' / (code + '.json'))
        actual = Counter(d['family'] for d in self.documents)
        if actual != Counter({'series-guide': 26, 'fundamental': 6, 'supplementary': 2}):
            raise ValueError('Required document scope differs: ' + repr(actual))
        self.units.sort(key=lambda u: (u['document_id'], u['id']))
        summary = {'documents': len(self.documents), 'document_families': dict(actual), 'units': len(self.units),
                   'classification': dict(Counter(u['classification'] for u in self.units)),
                   'uncertain_classifications': sum(u['classification_basis']['confidence'] == 'uncertain' for u in self.units),
                   'translation_status': dict(Counter(u['translation_status'] for u in self.units)),
                   'body_translation_missing': sum(u['translation_status'] == 'body-translation-missing' for u in self.units),
                   'raw_table_cell_units':sum(u['source_material_form']=='table-cell' for u in self.units),
                   'raw_visual_label_units':sum(u['source_material_form']=='visual-label' for u in self.units),
                   'independent_model_review_executed': 0, 'professional_acceptances': 0, 'organizational_approvals': 0}
        return {'schema_version': 'full-material-source-unit-inventory/1', 'scope': 'six fundamental volumes, 26 series guides, G226 and W242C',
                'source_unit_definition': 'All extracted PDF content units plus every raw block without a content mapping; all source images; every acquired fundamental block, navigation link and footnote; G226 raw blocks and W242C pages.',
                'input_sha256': self.inputs, 'documents': self.documents, 'summary': summary, 'units': self.units,
                'preserved_editorial_records_outside_source_units': self.editorial,
                'classification_acceptance': 'provisional deterministic dispositions; every unit awaits independent adjudication',
                'review_complete': False, 'model_launched': False,
                'limits': ['PDF text extraction and image records are acquired source representations, not proof that the pixel source has no unextracted content.',
                           'Section-aligned translation presence does not prove sentence/unit semantic equivalence.',
                           'Original Chinese W242C pages are not English-to-Chinese translation.',
                           'No prior authored review is renamed as independent model or human acceptance.']}


def prepare_shards(inventory, contexts, max_units=40, max_characters=24000):
    if max_units < 1 or max_characters < 100:
        raise ValueError('Positive shard unit/character budgets required')
    result, current, chars, doc, included_contexts = [], [], 0, None, set()
    for unit in inventory['units']:
        size = len(unit.get('text_en', unit.get('text_zh', ''))) + sum(len(f['text']) for f in unit.get('source_fragments', []))
        candidate_ids = {c['context_id'] for c in unit['translation_candidates']}
        added = sum(len(contexts[key]['text_zh']) for key in candidate_ids - included_contexts)
        if current and (unit['document_id'] != doc or len(current) >= max_units or chars + size + added > max_characters):
            result.append(current); current, chars, included_contexts = [], 0, set()
            added = sum(len(contexts[key]['text_zh']) for key in candidate_ids)
        current.append(unit); chars += size + added; doc = unit['document_id']; included_contexts.update(candidate_ids)
    if current:
        result.append(current)
    shards = []
    for index, units in enumerate(result):
        candidates = {c['context_id'] for u in units for c in u['translation_candidates']}
        characters = sum(len(u.get('text_en',u.get('text_zh',''))) + sum(len(f['text']) for f in u.get('source_fragments',[])) for u in units) + sum(len(contexts[key]['text_zh']) for key in candidates)
        shards.append({'schema_version': 'independent-material-review-shard/1', 'id': f'material-review-{index+1:04}',
                       'document_id': units[0]['document_id'], 'units': units,
                       'candidate_translation_context': {key: contexts[key] for key in sorted(candidates)},
                       'content_characters':characters,'character_budget':max_characters,
                       'oversized_single_unit':characters > max_characters,
                       'review_status': 'not-executed', 'model_settings': 'inherit existing configured service, model and inference settings without overrides',
                       'task': '逐项复核源定位、正文/前置/导航/参考分类及处理方式；对照原文和候选译文核对遗漏、语义、限定条件、图表文字与连线；每项给出发现、修订建议及复查状态。不将解释写成官方译文或真实批准。',
                       'required_result_fields': ['id', 'classification', 'disposition', 'source_locator', 'findings', 'revision', 'recheck', 'evidence', 'review_status'],
                       'acceptance_roles': {'independent_model': 'pending', 'human_professional': 'pending', 'organization': 'pending-signature'}})
    actual = [u['id'] for s in shards for u in s['units']]
    expected = [u['id'] for u in inventory['units']]
    if actual != expected or len(actual) != len(set(actual)):
        raise ValueError('Shards omit or duplicate source units')
    return shards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--max-units', type=int, default=40)
    parser.add_argument('--max-characters', type=int, default=24000)
    args = parser.parse_args()
    out = bounded(args.out)
    if not out.is_relative_to(REPO / 'output'):
        raise ValueError('Review inputs must be in repository output')
    out.mkdir()  # No overwriting an old preparation or review.
    builder = Inventory(); inventory = builder.build()
    shards = prepare_shards(inventory, builder.contexts, args.max_units, args.max_characters)
    changed = [name for name, fingerprint in inventory['input_sha256'].items() if sha(REPO / name) != fingerprint]
    if changed:
        raise ValueError('Inputs changed during preparation: ' + repr(changed))
    inventory_path = out / 'inventory.json'
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    pending = [u for u in inventory['units'] if not u['translation_candidates'] or u['classification_basis']['confidence'] == 'uncertain']
    (out / 'pending-units.json').write_text(json.dumps({'schema_version':'material-pending-unit-dispositions/1','units':pending},ensure_ascii=False,indent=2)+'\n')
    entries = []
    (out / 'shards').mkdir()
    for shard in shards:
        path = out / 'shards' / (shard['id'] + '.json')
        path.write_text(json.dumps(shard, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        entries.append({'id':shard['id'],'path':path.relative_to(REPO).as_posix(),'sha256':sha(path),
                        'document_id':shard['document_id'],'unit_ids':[u['id'] for u in shard['units']],
                        'review_status':'not-executed'})
    manifest = {'schema_version':'independent-material-review-inputs/1','source_unit_inventory':{'path':inventory_path.relative_to(REPO).as_posix(),'sha256':sha(inventory_path)},
                'shards':entries,'source_units':len(inventory['units']),'shard_count':len(shards),'complete_source_unit_assignment':True,
                'input_sha256':inventory['input_sha256'],'model_launched':False,'model_settings':'existing configuration unchanged',
                'oversized_single_unit_shards':[s['id'] for s in shards if s['oversized_single_unit']],
                'independent_review_complete':False,'human_professional_acceptance':'pending','organizational_approval':'pending-signature'}
    (out / 'review-input-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    lines = ['# 全量资料复核准备', '', '全部条目仅完成本地清点与暂定分类；独立模型尚未启动，人工专业验收及真实组织批准待签署。', '',
             '|范围|来源单元|正文译写缺项|不确定分类|', '|---|---:|---:|---:|']
    for document in inventory['documents']:
        units = [u for u in inventory['units'] if u['document_id'] == document['document_id']]
        lines.append(f'|{document["document_id"]}|{len(units)}|{sum(u["translation_status"]=="body-translation-missing" for u in units)}|{sum(u["classification_basis"]["confidence"]=="uncertain" for u in units)}|')
    lines += ['', '源文本、原始 PDF 片段、图片、定位和指纹在 inventory.json；pending-units.json 单列未写译文或分类不确定项。',
              'review-input-manifest.json 的全部分片恰好覆盖来源单元一次；候选译文按其实际 unit/section 对齐粒度提供，不把存在性当语义验收。',
              '原文可访问性、候选译文、独立复核、人工专业验收、组织批准分开记录。', '', json.dumps(inventory['summary'],ensure_ascii=False,indent=2)]
    (out / 'README.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'passed':True,'preparation_only':True,'summary':inventory['summary'],'shards':len(shards),'out':out.relative_to(REPO).as_posix()},ensure_ascii=False))


if __name__ == '__main__':
    main()
