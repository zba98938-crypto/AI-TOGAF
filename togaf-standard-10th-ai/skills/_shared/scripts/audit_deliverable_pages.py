#!/usr/bin/env python3
"""Check every rendered deliverable page for integrity and obvious PDF overflow.

This machine check complements, but cannot replace, actual page opening.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
REVIEW = ROOT / '_shared/reviews/deliverable-page-review'
LAYOUTS = ('baseline-reference', 'baseline-adaptive', 'modified-reference', 'modified-adaptive')


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    findings = []
    documents = 0
    pages = 0
    for layout in LAYOUTS:
        index = json.loads((REVIEW / layout / 'render-index.json').read_text())
        for doc in index['documents']:
            documents += 1
            source = ROOT / doc['source_path']
            pdf = REVIEW / layout / doc['deliverable_id'] / (doc['deliverable_id'] + '.pdf')
            problems = []
            if not source.is_file() or sha(source) != doc['source_sha256']:
                problems.append('source-missing-or-stale')
            if not pdf.is_file() or sha(pdf) != doc['pdf_sha256']:
                problems.append('pdf-missing-or-stale')
            markup = subprocess.run(['pdftotext', '-bbox-layout', str(pdf), '-'],
                                    check=True, capture_output=True, text=True).stdout
            root = ET.fromstring(markup)
            page_nodes = root.findall('.//{http://www.w3.org/1999/xhtml}page')
            if len(page_nodes) != len(doc['pages']):
                problems.append('page-count-mismatch')
            for position, item in enumerate(doc['pages']):
                pages += 1
                image = ROOT / item['path']
                if not image.is_file() or sha(image) != item['sha256']:
                    problems.append('page-image-missing-or-stale:' + item['page_id'])
                if position >= len(page_nodes): continue
                node = page_nodes[position]
                width, height = float(node.get('width')), float(node.get('height'))
                words = node.findall('.//{http://www.w3.org/1999/xhtml}word')
                if len(words) < 2:
                    problems.append('near-blank-page:' + item['page_id'])
                for word in words:
                    xmin, ymin = float(word.get('xMin')), float(word.get('yMin'))
                    xmax, ymax = float(word.get('xMax')), float(word.get('yMax'))
                    if xmin < -0.5 or ymin < -0.5 or xmax > width + 0.5 or ymax > height + 0.5:
                        problems.append('text-outside-page:' + item['page_id'])
                        break
            findings.append({'layout': layout, 'deliverable_id': doc['deliverable_id'],
                             'pages': len(doc['pages']), 'problems': sorted(set(problems)),
                             'visual_status': 'machine-check-only; actual-opening-required'})
    report = {'schema_version': 'deliverable-page-audit/1',
              'documents': documents, 'pages': pages,
              'problem_documents': sum(bool(x['problems']) for x in findings),
              'findings': findings, 'accepted_as_visual_review': False}
    (REVIEW / 'page-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('documents', 'pages', 'problem_documents')}, ensure_ascii=False))
    return int(report['problem_documents'] > 0)


if __name__ == '__main__': raise SystemExit(main())
