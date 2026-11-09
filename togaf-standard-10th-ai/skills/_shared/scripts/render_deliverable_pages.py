#!/usr/bin/env python3
"""Render generated Markdown deliverables to PDFs and page PNGs for visual review.

This prepares review assets. It does not assert that anyone opened or approved
the pages. All inputs and outputs must remain within skills/.
"""
import argparse
import base64
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import subprocess
import uuid

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / '_shared'
FONT = SHARED / 'assets/fonts/NotoSansSC.ttf'
PRINT = SHARED / 'scripts/print_deliverable_pdf.mjs'


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(path):
    path = path.resolve()
    if path != ROOT and ROOT not in path.parents:
        raise ValueError('输入与输出必须位于 skills/ 内')
    return path


def render_one(source, out, browser, font_path):
    out.mkdir(parents=True, exist_ok=True)
    body = subprocess.run(['pandoc', '--from=gfm', '--to=html5', str(source)],
                          check=True, capture_output=True, text=True).stdout
    font = base64.b64encode(font_path.read_bytes()).decode('ascii')
    css = f'''<style>
@font-face {{font-family:TogafCJK;src:url(data:font/ttf;base64,{font})}}
html,body {{font-family:TogafCJK,sans-serif;color:#1d2f3d;font-size:10pt;line-height:1.5}}
h1 {{font-size:18pt;border-bottom:1px solid #b9c8d2;padding-bottom:3mm}}
h2 {{font-size:14pt;margin-top:7mm;break-after:avoid}}
h3 {{font-size:11pt;break-after:avoid}}
table {{width:100%;border-collapse:collapse;font-size:8.5pt;break-inside:auto}}
thead {{display:table-header-group}} tr {{break-inside:avoid}}
th,td {{border:1px solid #c4d0d8;padding:1.5mm 2mm;overflow-wrap:anywhere;vertical-align:top}}
pre,blockquote,figure {{break-inside:avoid;overflow-wrap:anywhere}}
code {{overflow-wrap:anywhere}} img,svg {{max-width:100%;height:auto}}
.wide-record {{border:1px solid #c4d0d8;padding:3mm;margin:3mm 0;break-inside:avoid;font-size:9pt}}
.wide-record div {{display:grid;grid-template-columns:34mm minmax(0,1fr);gap:3mm;padding:1mm 0;border-bottom:1px solid #e7edf1}}
.wide-record div:last-child {{border-bottom:0}}
.wide-record strong {{color:#34526a}}
.wide-record span {{overflow-wrap:anywhere;min-width:0}}
</style>'''
    html = out / (source.stem + '.html')
    base_href=os.path.relpath(source.parent, out).replace(os.sep, '/')+'/'
    html.write_text('<!doctype html><html lang="zh"><head><meta charset="utf-8"><base href="'+escape(base_href, quote=True)+'">'
                    + css + '</head><body>' + body + '</body></html>')
    pdf = out / (source.stem + '.pdf')
    env = os.environ.copy()
    if browser: env['TOGAF_BROWSER_PATH'] = str(browser)
    subprocess.run(['node', str(PRINT), str(html), str(pdf)], cwd=SHARED, env=env, check=True)
    prefix = out / source.stem
    subprocess.run(['pdftoppm', '-r', '110', '-png', str(pdf), str(prefix)],
                   check=True, capture_output=True)
    images = sorted(out.glob(source.stem + '-*.png'))
    info = subprocess.run(['pdfinfo', str(pdf)], check=True, capture_output=True, text=True).stdout
    match = re.search(r'^Pages:\s*(\d+)$', info, re.MULTILINE)
    pages = int(match.group(1)) if match else -1
    if len(images) != pages or pages < 1:
        raise RuntimeError(f'{source.name}: 页数与图像数不一致')
    return {'deliverable_id': source.stem, 'source_path': str(source.relative_to(ROOT)),
            'source_sha256': sha(source), 'html_sha256': sha(html), 'pdf_sha256': sha(pdf),
            'pages': [{'page_id': f'{source.stem}:p{i}', 'path': str(image.relative_to(ROOT)),
                       'sha256': sha(image)} for i, image in enumerate(images, 1)],
            'visual_status': 'rendered-awaiting-actual-page-opening'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--browser', type=Path)
    a = p.parse_args()
    input_dir, out = contained(a.input_dir), contained(a.out)
    if not input_dir.is_dir(): p.error('交付物目录不存在')
    files = sorted(input_dir.glob('*.md'))
    if not files: p.error('没有 Markdown 交付物')
    if out.exists(): p.error('输出必须是新目录；不覆盖历史页面或删除已有PNG')
    out.mkdir(parents=True, exist_ok=False)
    font_path = input_dir.parent / 'font-subset.ttf'
    if not font_path.is_file(): font_path = FONT
    records = [render_one(source, out / source.stem, a.browser, font_path) for source in files]
    report = {'schema_version': 'deliverable-page-render/1', 'run_id': uuid.uuid4().hex,
              'input_dir': str(input_dir.relative_to(ROOT)),
              'renderer_sha256': {str(x.relative_to(ROOT)): sha(x) for x in (Path(__file__), PRINT, font_path)},
              'documents': records, 'documents_rendered': len(records),
              'pages_rendered': sum(len(r['pages']) for r in records),
              'accepted': False,
              'notice': '逐页图像须实际打开并单独记录内容及排版结论；渲染成功不授予视觉通过。'}
    (out / 'render-index.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'documents': len(records), 'pages': report['pages_rendered']}, ensure_ascii=False))


if __name__ == '__main__': main()
