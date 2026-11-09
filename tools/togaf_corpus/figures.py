"""Rebuild traceable figure records from the supplied PDFs and historical interpretations.

All paths stored in records are relative to the corpus root unless specified otherwise.
PDF indices are one-based; rectangles are unrotated PDF points, origin top-left.
"""
from __future__ import annotations
import argparse
import copy
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from concurrent.futures import ProcessPoolExecutor
import fitz
try:
    from .figure_supplements import enrich_image, DATA as VERIFIED_SUPPLEMENTS
except ImportError:
    from figure_supplements import enrich_image, DATA as VERIFIED_SUPPLEMENTS

VERSION = '1.0'
CAPTION = re.compile(r'^(Figure|Example)\s+([A-Z0-9]+-\d+)[:.]\s+(.+)', re.S)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def rect_list(rect):
    return [round(x, 3) for x in rect]


def json_text(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


def graph_issues(data, known_ids):
    errors = []
    elements = data.get('elements', [])
    ids = [e.get('id') for e in elements]
    if len(ids) != len(set(ids)):
        errors.append({'type': 'duplicate-element-id'})
    parents = {e['id']: e.get('parent') for e in elements if e.get('id')}
    for e in elements:
        parent = e.get('parent')
        if parent and parent not in parents:
            errors.append({'type': 'missing-parent', 'element': e.get('id'), 'parent': parent})
        visited = set()
        while parent and parent in parents:
            if parent in visited or parent == e.get('id'):
                errors.append({'type': 'parent-cycle', 'element': e.get('id')})
                break
            visited.add(parent)
            parent = parents[parent]
    for i, rel in enumerate(data.get('relationships', [])):
        for end in ['from', 'to']:
            if rel.get(end) not in parents:
                errors.append({'type': 'missing-relationship-endpoint', 'relationship_index': i, 'field': end, 'value': rel.get(end)})
    for rel in data.get('related_figures', []):
        if rel.get('target') not in known_ids:
            errors.append({'type': 'missing-related-figure', 'target': rel.get('target')})
    return errors


def transcript(page, clip, png_path, allow_ocr=True):
    """Keep digital and OCR text independently: neither implies a verified reading order."""
    digital = page.get_text('text', clip=clip, sort=True).strip()
    result = {'digital_text': digital, 'digital_words': [
        {'text': w[4], 'bbox_pdf_points': rect_list(w[:4])}
        for w in page.get_text('words', clip=clip, sort=True)], 'ocr': None}
    if not allow_ocr:
        return result
    # These documents embed raster diagrams; a few vector caption words must not
    # cause us to skip the image's labels. OCR is retained separately, never merged.
    if shutil.which('tesseract'):
        cache = png_path.with_suffix('.ocr.json')
        image_hash = sha(png_path)
        if cache.exists():
            cached = json.loads(cache.read_text())
            if cached.get('image_sha256') == image_hash:
                result['ocr'] = cached
                return result
        proc = subprocess.run(['tesseract', str(png_path), 'stdout', '-l', 'eng', '--psm', '11', 'tsv'],
                              capture_output=True, text=True, timeout=90)
        words = []
        lines = {}
        if proc.returncode == 0:
            for row in csv.DictReader(io.StringIO(proc.stdout), delimiter='\t'):
                if not row.get('text', '').strip():
                    continue
                try:
                    conf = float(row['conf'])
                    bbox = [int(row[k]) for k in ['left', 'top', 'width', 'height']]
                except (ValueError, KeyError):
                    continue
                words.append({'text': row['text'], 'confidence': conf, 'bbox_pixels_xywh': bbox})
                key = tuple(row.get(k) for k in ['page_num', 'block_num', 'par_num', 'line_num'])
                lines.setdefault(key, []).append(row['text'])
        ocr = {'engine': 'tesseract', 'language': 'eng', 'page_segmentation_mode': 11,
               'image_sha256': image_hash, 'status': 'extracted-unverified' if proc.returncode == 0 else 'failed',
               'text': '\n'.join(' '.join(v) for v in lines.values()), 'words': words,
               'mean_word_confidence': round(sum(w['confidence'] for w in words) / len(words), 2) if words else None,
               'coordinate_space': 'rendered crop pixels; sparse-text order is not diagram topology'}
        if proc.returncode:
            ocr['error'] = proc.stderr.strip()[:1000]
        dump(cache, ocr)
        result['ocr'] = ocr
    else:
        result['ocr'] = {'status': 'unavailable', 'engine': 'tesseract', 'text': ''}
    return result


def corrections(data):
    """Only corrections directly checked against rendered original PDF crops."""
    fid = data['id']
    if data.get('provenance', {}).get('pdf_sha256') != VERIFIED_SUPPLEMENTS['source_sha256'].get(fid.split('/')[0]):
        return []
    notes = []
    if fid == 'G234/fig4-4':
        notes.append({'scope': 'source-asset', 'finding_zh': '本次直接从英文 PDF 第 25 页提取的图显示 Technology、Data Model、Processes (Workflows) 三部分；消除了旧英文 PNG 错配问题。历史资产仍保留原有冲突。'})
    elif fid == 'G212/fig5-2':
        notes.append({'scope': 'quadrant-labels', 'finding_zh': '本次核对英文 PDF 第 40 页：左上 Avant-Garde，右上 Big-Bang，左下 Discreet，右下 Cohesive；横轴为普及度、纵轴为速度。旧中文重绘的 C/D 位置不可采用。'})
    elif fid == 'G234/fig5-1':
        old = copy.deepcopy(data['semantics']['key_points_zh'])
        data['semantics']['key_points_zh'] = [s.replace('五类文档化功能共 13 项', '五类文档化功能共 12 项') for s in old]
        notes.append({'scope': 'semantics.key_points_zh', 'finding_zh': '英文 PDF 第 31 页五类文档化分组为 2+3+3+2+2=12 项，修正历史摘要中的 13。10 个一级分组共有 30 个二级功能。', 'previous_value': old})
    elif fid == 'G242/fig3-14':
        old = copy.deepcopy(data['tables'][0])
        table = data['tables'][0]
        table['columns'] = ['项目', 'Total', 'Year 1 · Scope 2 KgCO2e', 'Year 1 · Scope 3 service kgCO2e',
                            'Year 1 · IT equipments build - Scope 3 KgCO2e', 'Year 2 · Scope 2 KgCO2e',
                            'Year 2 · Scope 3 service kgCO2e', 'Year 2 · IT equipments build - Scope 3 KgCO2e']
        table['rows'] = [row[:-1] for row in table['rows']]
        table['notes_zh'] = '直接核对英文 PDF 第 77 页。Total 只有一列，Year 1 和 Year 2 各有三项；不存在 Year 1 Total 列。原图数值不改：新增分项 69+224+590=883，与印刷总量884差1；Scope 2 的69−460=−391，与印刷平衡−390差1；未判定差异成因。深色 Increase 按钮与总平衡−103并存，保留原图状态。'
        data['semantics']['key_points_zh'] = [
            ('表格保留原图数值：新增总量884、分项和883差1；Scope 2 的69−460=−391，与原图−390差1；差异原因未确定。' if 'Total=69' in s else
             '本例业务影响中度量与培训选 YES，降低影响选 NO；IT 侧 Increase 按钮呈深色，同时表格总平衡为 −103，须保留这两个事实，不自动消解其含义。' if 'IT 侧承诺净减排' in s else s)
            for s in data['semantics']['key_points_zh']]
        data['semantics']['reading_guide_zh'] = data['semantics']['reading_guide_zh'].replace('第 1 年（Total/范围 2/范围 3 服务/IT 设备制造）', '第 1 年（范围 2/范围 3 服务/IT 设备制造）')
        prior_misreadings = copy.deepcopy(data['semantics']['misreadings_zh'])
        data['semantics']['misreadings_zh'] = [
            ('原图 Increase 按钮呈深色、Decrease 呈白色，同时表内总平衡为 −103。图中未解释两者关系，不推断其是否矛盾或各自统计口径。' if '两者并不矛盾' in t else
             '表格只有一个 Total 列（884/987/−103），之后是 Year 1 三列和 Year 2 三列；不存在 Year 1 Total 列。新增分项和883与Total884差1，Scope 2 计算−391与印刷−390差1，差异原因未确定。' if '疑为原表列错位' in t else
             '第 1 年 IT equipments build - Scope 3 三行分别为新增590、退役527、平衡63；第 2 年的三类分项均为0。不以这些示例值推断排放发生时点或业务原因。' if '本方案第 1 年没有新增设备制造' in t else t)
            for t in prior_misreadings]
        data['semantics']['key_points_zh'] = [
            ('碳足迹列按范围 2、范围 3 服务、IT 设备制造（范围 3）划分，Year 1 与 Year 2 各含三列。图中未说明各项排放发生频率。' if '制造排放一次发生' in t else
             '表格总量三行分别为新增资源884、退役资源987、平衡−103；这里保留原图值，不把它推导成已验证的目标架构结论。' if '说明目标架构通过退役旧资产抵消新增' in t else t)
            for t in data['semantics']['key_points_zh']]
        data['quality']['uncertainties_zh'] = [
            ('本次已核对原图列名并纠正历史解释：没有 Year 1 Total 列；原图两处1单位差异保留，未确定其成因。' if '第 1 年“Total”列' in t else t)
            for t in data['quality']['uncertainties_zh']]
        notes.append({'scope': 'tables.t_carbon_footprint-and-associated-semantics', 'finding_zh': table['notes_zh'], 'previous_value': old,
                      'previous_misreadings': prior_misreadings})
    return notes


def render_md(data):
    s = [f"# {data['id']} · {data.get('figure', {}).get('title_zh') or data.get('figure', {}).get('title_en') or 'Image'}", '',
         f"内容角色：`{data['provenance']['source_role']}`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。", '',
         f"原文：`{data['provenance']['pdf_path']}`；SHA-256：`{data['provenance']['pdf_sha256']}`。", '']
    for ext in data.get('source_extraction', []):
        if ext.get('image_path'):
            rel = os.path.relpath(ext['image_path'], str(Path('figures') / data['id'].split('/')[0]))
            s += [f"## 原图 · PDF 第 {ext['pdf_page']} 页", '', f"![英文原图]({rel})", '',
                  f"PDF 坐标：`{ext['bbox_pdf_points']}`；裁剪来源：`{ext['region_source']}`。", '',
                  '### 图内文字（数字提取）', '', ext['transcription']['digital_text'] or '原图该区域未提供可提取的数字文本。', '']
            ocr = ext['transcription'].get('ocr')
            if ocr:
                s += ['### 图内文字（OCR，待核对）', '', '```text', ocr.get('text', ''), '```', '']
    for note in data.get('current_visual_findings', []):
        s += ['## 本次原图核对', '', note['finding_zh'], '']
    sem = data.get('semantics', {})
    for key, title in [('one_line_zh', '概要'), ('purpose_zh', '目的'), ('reading_guide_zh', '阅读顺序'),
                       ('key_points_zh', '关键含义'), ('hierarchy_zh', '层级'), ('line_semantics_zh', '线条含义'), ('misreadings_zh', '易误读点')]:
        if sem.get(key):
            val = sem[key]
            s += ['## ' + title + '（历史解释；局部修正见上）', '', '\n'.join('- ' + str(x) for x in val) if isinstance(val, list) else str(val), '']
    # JSON blocks preserve every field, including nested tables and explicit/inferred relationships.
    for key, title in [('elements', '元素'), ('relationships', '关系'), ('flows', '有序流程'), ('tables', '转录表格'),
                       ('legend', '图例'), ('layout', '布局'), ('related_figures', '相关图'), ('quality', '历史不确定性'),
                       ('known_conflicts', '既有来源冲突'), ('validation', '结构校验')]:
        if data.get(key):
            s += ['## ' + title, '', '```json', json_text(data[key]), '```', '']
    return '\n'.join(s).rstrip() + '\n'


def process_document(args):
    root_s, output_s, pdf_s, known_ids, conflicts = args
    root, output, pdf = Path(root_s), Path(output_s), Path(pdf_s)
    code = pdf.stem[:-1]
    doc = fitz.open(pdf)
    pdf_hash = sha(pdf)
    historical = root / 'togaf-standard-10th-zh/figs/ai' / code
    records = [json.loads(p.read_text()) for p in sorted(historical.glob('*.json'))]
    historical_paths = {d['id']: historical / (d['id'].split('/')[1] + '.json') for d in records}
    # Require caption punctuation; ordinary prose references must not create figures.
    captions = {}
    for page in doc:
        for block in page.get_text('blocks'):
            m = CAPTION.match(block[4].strip())
            if m:
                key = ('fig' if m[1] == 'Figure' else 'ex') + m[2]
                captions.setdefault(key, []).append({'pdf_page': page.number + 1, 'text': re.sub(r'\s+', ' ', block[4]).strip(), 'bbox_pdf_points': rect_list(block[:4])})
    existing = {d['id'].split('/')[1] for d in records}
    for key, caps in captions.items():
        if key in existing:
            continue
        records.append({'id': code + '/' + key, 'figure': {'kind': 'figure', 'number': key.removeprefix('fig').removeprefix('ex'),
                         'title_en': caps[0]['text'], 'en_location': {'pages': [caps[0]['pdf_page']], 'bboxes': []}},
                         'doc': {'code': code}, 'elements': [], 'relationships': [], 'flows': [], 'tables': [],
                         'semantics': {'one_line_zh': '根据原文图题新增；数字文字和 OCR 见下，图形拓扑尚未人工校核。'},
                         'quality': {'confidence': 'unreviewed', 'uncertainties_zh': ['自动发现的图，未建立可靠语义拓扑。']}})
    figure_index, all_regions = [], []
    for data in records:
        fid = data['id']; key = fid.split('/')[1]
        data['schema_version'] = VERSION
        oldfile = historical_paths.get(fid)
        loc = data.get('figure', {}).get('en_location') or {}
        data['provenance'] = {'source_role': 'editorial-added' if not loc else 'source-figure-with-historical-interpretation' if oldfile else 'source-figure-auto-discovered',
                              'pdf_path': str(pdf.relative_to(root)), 'pdf_sha256': pdf_hash,
                              'interpretation_path': str(oldfile.relative_to(root)) if oldfile else None,
                              'interpretation_sha256': sha(oldfile) if oldfile else None,
                              'interpretation_status': 'historical-interpretation-not-fully-reverified',
                              'page_numbering': 'PDF physical page, one-based', 'bbox_coordinate_system': 'PDF points; origin top-left',
                              'title_matches': captions.get(key, [])}
        exts = []; pages = loc.get('pages', []); boxes = loc.get('bboxes', [])
        for i, n in enumerate(pages):
            if not 1 <= n <= len(doc):
                continue
            page = doc[n-1]
            if i < len(boxes):
                clip = fitz.Rect(boxes[i]) & page.rect
                source = 'historical-bbox-checked-within-original-page'
            else:
                clip = page.rect
                source = 'full-page-fallback-no-trusted-crop'
            region_suffix = f'-r{i+1:02}' if pages.count(n) > 1 else ''
            image_path = Path('figures/assets') / code / f'{key}-p{n:04}{region_suffix}.png'
            target = output / image_path; target.parent.mkdir(parents=True, exist_ok=True)
            page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip, alpha=False).save(target)
            trans = transcript(page, clip, target)
            exts.append({'pdf_page': n, 'printed_page': loc.get('printed_page'), 'bbox_pdf_points': rect_list(clip),
                         'page_size_points': [page.rect.width, page.rect.height], 'image_path': image_path.as_posix(),
                         'image_sha256': sha(target), 'render_dpi': 144, 'region_source': source, 'transcription': trans})
            all_regions.append((n, clip, fid, image_path.as_posix()))
        data['source_extraction'] = exts
        data['known_conflicts'] = [c for c in conflicts if c.get('figure_id') == fid]
        data['current_visual_findings'] = corrections(data)
        data['validation'] = {'graph_integrity_issues': graph_issues(data, set(known_ids) | {r['id'] for r in records}),
                              'location_available': bool(pages), 'caption_page_match': any(c['pdf_page'] in pages for c in captions.get(key, [])) if key in captions else None,
                              'visual_review_scope': 'specific-findings-only' if data['current_visual_findings'] else 'not-reverified-this-build',
                              'all_source_pages_valid': all(1 <= n <= len(doc) for n in pages)}
        path = Path('figures') / (fid + '.json'); dump(output / path, data)
        (output / path.with_suffix('.md')).write_text(render_md(data), encoding='utf-8')
        figure_index.append({'id': fid, 'document_id': code, 'title_en': data.get('figure', {}).get('title_en'),
                             'title_zh': data.get('figure', {}).get('title_zh'), 'pdf_pages': pages,
                             'json_path': path.as_posix(), 'markdown_path': path.with_suffix('.md').as_posix(),
                             'source_role': data['provenance']['source_role'], 'elements': len(data.get('elements', [])),
                             'relationships': len(data.get('relationships', [])), 'graph_issue_count': len(data['validation']['graph_integrity_issues']),
                             'ocr_word_count': sum(len((e['transcription'].get('ocr') or {}).get('words', [])) for e in exts)})
    # Enumerate every embedded-image occurrence, including covers, logos and icons.
    # Covered objects point at complete figure records; uncovered objects get their own text records.
    image_index = []
    for page in doc:
        for j, obj in enumerate(page.get_image_info(hashes=True, xrefs=True)):
            rect = fitz.Rect(obj['bbox']) & page.rect
            if rect.is_empty or rect.is_infinite:
                continue
            linked = []
            for n, box, fid, img in all_regions:
                if n == page.number + 1 and max(0, (rect & box).width) * max(0, (rect & box).height) / max(rect.width * rect.height, 0.01) >= .85:
                    linked.append(fid)
            asset_id = f'{code}/image-p{page.number+1:04}-{j+1:02}'
            item = {'id': asset_id, 'document_id': code, 'pdf_page': page.number + 1, 'bbox_pdf_points': rect_list(rect),
                    'pixel_dimensions': [obj['width'], obj['height']], 'pdf_xref': obj.get('xref'),
                    'decoded_image_digest_md5': obj['digest'].hex(), 'figure_ids': linked,
                    'content_role': 'embedded-image-occurrence-not-necessarily-a-logical-figure',
                    'provenance': {'pdf_path': str(pdf.relative_to(root)), 'pdf_sha256': pdf_hash,
                                   'page_numbering': 'PDF physical page, one-based',
                                   'bbox_coordinate_system': 'PDF points; origin top-left'}}
            if not linked:
                image_path = Path('figures/assets') / (asset_id + '.png')
                target = output / image_path; target.parent.mkdir(parents=True, exist_ok=True)
                page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect, alpha=False).save(target)
                item['image_path'] = image_path.as_posix()
                item['image_sha256'] = sha(target)
                item['transcription'] = transcript(page, rect, target)
                # Auto descriptions distinguish evidence from interpretations.
                item['description_zh'] = ('未单独编号的嵌入图像。其可提取文字见 transcription；未推断节点与箭头关系。')
                enrich_image(item, target)
                jp = Path('figures') / (asset_id + '.json'); dump(output / jp, item)
                ocr = item['transcription'].get('ocr') or {}
                text = f"# {asset_id}\n\n原文 PDF 第 {item['pdf_page']} 页，坐标 `{item['bbox_pdf_points']}`。\n\n{item['description_zh']}\n\n![原图](../assets/{asset_id}.png)\n\n## 数字文字\n\n{item['transcription']['digital_text']}\n\n## OCR（待核对）\n\n```text\n{ocr.get('text', '')}\n```\n"
                text += '\n## 结构化含义与表格\n\n```json\n' + json_text({k: item[k] for k in ['image_kind', 'visible_labels', 'notation_element_en', 'notation_variant', 'adm_phase', 'ordered_options', 'selected_option', 'tables', 'current_visual_review'] if k in item}) + '\n```\n'
                (output / jp.with_suffix('.md')).write_text(text, encoding='utf-8')
                item['json_path'] = jp.as_posix(); item['markdown_path'] = jp.with_suffix('.md').as_posix()
                item.pop('transcription')
                if 'tables' in item:
                    item['structured_table_count'] = len(item.pop('tables'))
            image_index.append(item)
    doc.close()
    print(f'{code}: {len(figure_index)} figure records, {len(image_index)} embedded image occurrences', flush=True)
    return figure_index, image_index


def build_figures(root: Path, output: Path, workers=4):
    root, output = Path(root).resolve(), Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    oldfiles = sorted((root / 'togaf-standard-10th-zh/figs/ai').glob('G*/*.json'))
    known_ids = [json.loads(p.read_text())['id'] for p in oldfiles]
    reg = root / 'togaf-standard-10th-ai/skills/_shared/evidence-registry.json'
    conflicts = json.loads(reg.read_text()).get('source_conflicts', []) if reg.exists() else []
    args = [(str(root), str(output), str(p), known_ids, conflicts) for p in sorted((root / 'togaf-standard-10th').glob('*.pdf'))]
    figures, images = [], []
    if workers == 1:
        batches = map(process_document, args)
        for fs, imgs in batches:
            figures.extend(fs); images.extend(imgs)
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for fs, imgs in pool.map(process_document, args):
                figures.extend(fs); images.extend(imgs)
    index = {'schema_version': VERSION, 'path_base': 'corpus-root',
             'notice_zh': '全部原图来自本地英文PDF；历史语义与当次原文提取分别保留。OCR不证明节点关系正确；页图、原图、原文优先于历史重绘。',
             'counts': {'figure_records': len(figures), 'original_figure_records': sum(f['source_role'] != 'editorial-added' for f in figures),
                        'editorial_added_records': sum(f['source_role'] == 'editorial-added' for f in figures),
                        'embedded_image_occurrences': len(images), 'embedded_images_linked_to_figures': sum(bool(i['figure_ids']) for i in images),
                        'standalone_embedded_images': sum(not i['figure_ids'] for i in images),
                        'graph_integrity_issues': sum(f['graph_issue_count'] for f in figures)},
             'figures': figures, 'embedded_images': images}
    dump(output / 'figures/index.json', index)
    lines = ['# 原图与图意入口', '', index['notice_zh'], '', '```json', json_text(index['counts']), '```', '',
             '| 图 ID | 标题 | 原文页 | 内容角色 |', '|---|---|---|---|']
    for f in figures:
        lines.append(f"| [{f['id']}]({f['id']}.md) | {f['title_zh'] or f['title_en'] or ''} | {', '.join(map(str, f['pdf_pages']))} | {f['source_role']} |")
    lines += ['', '所有嵌入图像（含标识、封面、截图内图像）另在 index.json 的 embedded_images 中逐个列出；已覆盖图像关联 figure_ids，其余另存 Markdown/JSON。', '']
    (output / 'figures/README.md').write_text('\n'.join(lines), encoding='utf-8')
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path, default=None)
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    result = build_figures(args.root, args.output or args.root / 'togaf-standard-10th-ai', args.workers)
    print(json_text(result['counts']))


if __name__ == '__main__':
    main()
