#!/usr/bin/env python3
"""Maintainer audit: extract English text and figure crops for three-source review.

The English PDFs are evaluation copies ("Not for redistribution"). Extracted text,
crops and comparison sheets go only to an external scratch directory; the skill
collection keeps locators, hashes and review findings, never copies of the source.
Requires PyMuPDF and Pillow in the maintainer's Python; generated skills do not.
"""
import argparse
import json
import re
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont
from build_corpus_registry import guide_code, sha, text_inventory

ROOT = Path(__file__).resolve().parents[1]
FRONT_BACK = re.compile(r'^(前言|商标|索引|致谢|关于作者|尾注|版权声明|参考文档|参考文献)$')
FONT = ROOT / 'assets/fonts/NotoSansSC.ttf'

def raster(path, out, max_width=1600):
    """PNG copy or SVG rasterization of a local asset; failures are recorded, not hidden."""
    try:
        if path.suffix.lower() == '.svg':
            page = fitz.open(path)[0];zoom = min(2.0, max_width/max(1, page.rect.width))
            page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False).save(out)
        else:
            img = Image.open(path).convert('RGB')
            if img.width > max_width:img = img.resize((max_width, int(img.height*max_width/img.width)))
            img.save(out)
        return None
    except Exception as error:
        return type(error).__name__+': '+str(error)[:200]

def similarity(a, b, size=16):
    """Difference-hash agreement; a triage aid only, never proof of identity."""
    def bits(path):
        px = list(Image.open(path).convert('L').resize((size+1, size)).getdata())
        return [px[r*(size+1)+c] > px[r*(size+1)+c+1] for r in range(size) for c in range(size)]
    x, y = bits(a), bits(b);return round(sum(i == j for i, j in zip(x, y))/len(x), 3)

def sheet(panels, out, width=1400, max_height=4200):
    """Stack labelled panels, English PDF crop first, into one overview image."""
    font = ImageFont.truetype(str(FONT), 22);images = []
    for label, path in panels:
        img = Image.open(path).convert('RGB');scale = min(1.0, width/img.width, 1300/img.height)
        images.append((label, img.resize((max(1, int(img.width*scale)), max(1, int(img.height*scale))))))
    canvas = Image.new('RGB', (width, sum(img.height+44 for _, img in images)), 'white')
    draw = ImageDraw.Draw(canvas);y = 0
    for label, img in images:
        draw.rectangle([0, y, width, y+36], fill='#e6ecf2');draw.text((10, y+5), label, fill='#102030', font=font)
        canvas.paste(img, (0, y+40));y += img.height+44
    if canvas.height > max_height:canvas = canvas.resize((int(width*max_height/canvas.height), max_height))
    canvas.save(out)
def compact(items, render, limit):
    rows = [render(item) for item in items[:limit]]
    if len(items) > limit:rows.append('... 另有 %d 项，见完整 JSON' % (len(items)-limit))
    return rows

def element_row(e):
    return '|'.join(str(e.get(k) or '') for k in ['id', 'label_en', 'label_zh', 'type', 'parent'])

def relation_row(r):
    head = str(r.get('from'))+' -'+str(r.get('type'))+'-> '+str(r.get('to'))
    extra = [str(r[k]) for k in ['label_en', 'label_zh', 'cardinality', 'polarity'] if r.get(k)]
    return head+(' | '+' | '.join(extra) if extra else '')+(' [推断]' if r.get('explicit') is False else '')

def guide_brief(path, source, english_file, pdf_pages, figures=()):
    inv = text_inventory(path, source);code = guide_code(path)
    figures = [{'figure_id': f['id'], 'title': f.get('title'), 'zh_md_lines': (f.get('md_locator') or {}).get('md_lines'),
                'profile_ids': f.get('profile_ids', [])} for f in figures if f.get('guide') == code]
    sections = [{'id': s['id'], 'lines': [s['line'], s['end_line']], 'level': s['level'], 'title': s['title'],
                 **({'prehint': 'front-back-matter'} if FRONT_BACK.match(s['title'].strip()) else {})} for s in inv['sections']]
    tables = [{'id': t['id'], 'lines': t['lines'], 'rows': t['row_count'], 'header': t['header'][:120]} for t in inv['tables']]
    return {'guide': code, 'zh_md': str(path), 'zh_sha256': inv['sha256'], 'zh_line_count': inv['line_count'],
            'english_text': str(english_file), 'english_pages': pdf_pages, 'sections': sections, 'tables': tables,
            'figures': figures}
def figure_brief(f, d, pdf, zh, out, registry_row):
    fid = d['id'];stem = fid.replace('/', '-');loc = d.get('figure', {}).get('en_location') or {}
    crops, pages, panels, assets = [], [], [], []
    for i, (number, box) in enumerate(zip(loc.get('pages', []), loc.get('bboxes', []))):
        page = pdf[number-1];clip = fitz.Rect(box) & page.rect
        zoom = min(2.5, 1800/max(1, clip.width));crop = out/'crops'/(stem+'-p%d-%d.png' % (number, i))
        page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip, alpha=False).save(crop)
        full = out/'pages'/(d['doc']['code']+'-p%d.png' % number)
        if not full.exists():page.get_pixmap(dpi=110, alpha=False).save(full)
        crops.append(str(crop));pages.append(str(full));panels.append(('英文 PDF 原图 第%d页（基准）' % number, crop))
    for a in d.get('assets', []):
        rel = a.get('path', '').split('#')[0];path = zh/rel
        item = {'path': rel, 'kind': a.get('kind'), 'recorded_fidelity': a.get('fidelity'),
                'recorded_issues': a.get('issues_zh', []), 'referenced_in_zh_md': a.get('referenced_in_zh_md')}
        if path.suffix.lower() in ['.png', '.svg'] and path.is_file():
            target = out/'assets'/(stem+'--'+path.name+'.png');item['raster_error'] = raster(path, target)
            if not item['raster_error']:
                item['raster'] = str(target);panels.append(('本地资产 '+rel+' ['+str(a.get('kind'))+']', target))
                if crops:item['dhash_agreement_with_pdf'] = similarity(crops[0], target)
        elif path.suffix.lower() in ['.png', '.svg']:item['missing_file'] = True
        assets.append(item)
    overview = None
    if panels:overview = out/'sheets'/(stem+'.png');sheet(panels, overview)
    zh_lines = (d.get('figure', {}).get('zh_location') or {}).get('md_lines') or [1]
    return {'figure_id': fid, 'guide': d['doc']['code'], 'kind': d.get('figure', {}).get('kind'),
            'title_en': d.get('figure', {}).get('title_en'), 'title_zh': d.get('figure', {}).get('title_zh'),
            'zh_md': str(zh/d['doc']['zh_md']), 'zh_context_lines': [max(1, min(zh_lines)-40), max(zh_lines)+40],
            'label_table_lines': (d.get('figure', {}).get('zh_location') or {}).get('label_table_lines'),
            'en_pages': loc.get('pages', []), 'overview_sheet': str(overview) if overview else None,
            'pdf_crops': crops, 'pdf_full_pages': pages, 'assets': assets, 'full_json': str(f),
            'json_classification': d.get('classification', {}), 'json_purpose_zh': d.get('semantics', {}).get('purpose_zh'),
            'json_elements': compact(d.get('elements', []), element_row, 90),
            'json_relationships': compact(d.get('relationships', []), relation_row, 70),
            'json_flows': compact(d.get('flows', []), lambda x: json.dumps(x, ensure_ascii=False)[:200], 20),
            'json_legend': [str(x.get('symbol'))+' = '+str(x.get('meaning_zh')) for x in d.get('legend', [])],
            'json_tables': [json.dumps(t, ensure_ascii=False)[:300] for t in d.get('tables', [])][:5],
            'json_quality': d.get('quality', {}), 'current_registry': registry_row}
def inventory_tsv(path):
    arts = json.loads((ROOT/'artifacts.json').read_text())['artifacts']
    dels = json.loads((ROOT/'deliverables.json').read_text())['deliverables']
    cap = json.loads((ROOT/'capabilities.json').read_text())
    rows = ['kind\tid\tname\towner\tsources']
    rows += ['legacy-artifact\t%s\t%s / %s\t%s\t%s' % (a['id'], a['name_zh'], a['name_en'], a['owner'], ','.join(a.get('sources', []))) for a in arts]
    rows += ['deliverable\t%s\t%s / %s\t%s\t%s' % (d['id'], d['name_zh'], d['name_en'], d['owner'], ','.join(d.get('sources', []))) for d in dels]
    rows += ['work-product\t%s\t%s / %s\t%s\t%s' % (w['id'], w['name_zh'], w['name_en'], w['owner'], '；'.join(w['source_refs'])) for w in cap['work_products']]
    rows += ['view-profile\t%s\t%s [artifact=%s renderer=%s]\t%s\t%s' % (p['id'], p['name'], p['artifact_id'], p['renderer'], p['owner'], '；'.join(p['source_refs'])) for p in cap['profiles']]
    rows += ['analysis-method\t%s\t%s\t%s\t%s' % (m['id'], m['name'], m['owner'], '；'.join(m['source_refs'])) for m in cap['analysis_methods']]
    path.write_text('\n'.join(rows)+'\n')

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--zh', type=Path, default=ROOT.parents[1]/'togaf-standard-10th-zh')
    p.add_argument('--en', type=Path, required=True, help='目录内含 G152e.pdf 等英文原文')
    p.add_argument('--out', type=Path, required=True, help='外部临时目录；不得位于技能集合内')
    a = p.parse_args();out = a.out.resolve()
    if out == ROOT.parent.resolve() or ROOT.parent.resolve() in out.parents:p.error('输出不得写入技能集合')
    for name in ['text', 'crops', 'pages', 'assets', 'sheets', 'briefs/guides', 'briefs/figures']:(out/name).mkdir(parents=True, exist_ok=True)
    registry = {f['id']: f for f in json.loads((ROOT/'evidence-registry.json').read_text())['figures']}
    manifest = {'english_pdfs': {}, 'guides': [], 'figures': []};pdfs = {}
    for md in sorted(a.zh.glob('G*.md')):
        code = guide_code(md);pdf_path = a.en/(code+'e.pdf');pdf = fitz.open(pdf_path);pdfs[code] = pdf
        text = ''.join('\n=== PDF 第%d页 ===\n' % (i+1)+page.get_text() for i, page in enumerate(pdf))
        english = out/'text'/(code+'.txt');english.write_text(text)
        manifest['english_pdfs'][code] = {'file': pdf_path.name, 'sha256': sha(pdf_path), 'pages': len(pdf)}
        brief = guide_brief(md, a.zh, english, len(pdf), registry.values());target = out/'briefs/guides'/(code+'.json')
        target.write_text(json.dumps(brief, ensure_ascii=False, indent=1)+'\n')
        manifest['guides'].append({'guide': code, 'brief': str(target), 'sections': len(brief['sections']), 'tables': len(brief['tables'])})
    for f in sorted((a.zh/'figs/ai').glob('G*/*.json')):
        d = json.loads(f.read_text());row = registry.get(d['id'], {})
        current = {k: row.get(k) for k in ['disposition', 'profile_ids', 'method_ids', 'conflict_ids', 'source_status', 'current_semantic_review']}
        brief = figure_brief(f, d, pdfs[d['doc']['code']], a.zh, out, current)
        target = out/'briefs/figures'/(d['id'].replace('/', '-')+'.json')
        target.write_text(json.dumps(brief, ensure_ascii=False, indent=1)+'\n')
        manifest['figures'].append({'figure_id': d['id'], 'brief': str(target), 'crops': len(brief['pdf_crops']), 'sheet': brief['overview_sheet']})
    inventory_tsv(out/'capability-inventory.tsv')
    (out/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1)+'\n')
    print(json.dumps({'guides': len(manifest['guides']), 'figures': len(manifest['figures']),
                      'without_pdf_crop': [x['figure_id'] for x in manifest['figures'] if not x['crops']]}, ensure_ascii=False))

if __name__ == '__main__':main()
