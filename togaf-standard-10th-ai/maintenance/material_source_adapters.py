"""Exact source binding adaptations; original text and semantic status stay intact."""
import hashlib
import json
from pathlib import Path
import re

DATA_PATH = Path(__file__).parent / 'material-source-adapters/g242-co2e-binding.json'
DATA = json.loads(DATA_PATH.read_text(encoding='utf-8'))


def text_sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def norm(text):
    return re.sub(r'\s+', ' ', text).strip()


def exact_cell_representation(cell):
    """Only a byte-exact acquired cell has a derived CO2e representation."""
    choices = {c['original']: c['derived_match_representation'] for table in DATA['tables'].values() for c in table['cells']}
    return choices.get(cell)


def g242_table_adaptation(document_id, source, document_ref, block, table_unit_id, table):
    """Return traceable matching evidence only for the 13 pinned raw blocks."""
    raw = DATA['raw_blocks'].get(block.get('id')); expected = DATA['tables'].get(table_unit_id)
    if (document_id != DATA['document_id'] or raw is None or expected is None
            or source.get('sha256') != DATA['source_pdf_sha256']
            or document_ref.get('sha256') != DATA['source_document_sha256']
            or raw['table_unit_id'] != table_unit_id or table.get('type') != 'table'
            or text_sha(block.get('text', '')) != raw['text_sha256'] or block.get('bbox') != raw['bbox']
            or text_sha(table.get('text', '')) != expected['content_sha256'] or table.get('bbox') != expected['bbox']):
        return None
    rows = table['text'].splitlines(); adaptations = []
    for cell in expected['cells']:
        row, column = cell['row_zero_based'], cell['column_zero_based']
        columns = rows[row].split('|')
        # The source is a Markdown table with one leading and trailing pipe.
        if columns[column + 1].strip() != cell['original']:
            return None
        updated = exact_cell_representation(cell['original'])
        if updated is None:
            return None
        columns[column + 1] = ' ' + updated + ' '; rows[row] = '|'.join(columns)
        adaptations.append({**cell, 'original_sha256': text_sha(cell['original']), 'derived_sha256': text_sha(updated)})
    derived = '\n'.join(rows)
    text = norm(derived.replace('<br>', ' ').replace('|', ' '))
    lines = [norm(line) for line in block['text'].splitlines() if norm(line)]
    if not lines or not all(line in text for line in lines):
        return None
    return {'schema_version': 'material-source-binding-adaptation/1', 'id': DATA['id'],
            'source_unit_id': block['id'], 'source': source, 'source_document': document_ref,
            'raw_text_sha256': raw['text_sha256'], 'raw_bbox_pdf_points': raw['bbox'],
            'table_unit_id': table_unit_id, 'table_source_content_sha256': expected['content_sha256'],
            'derived_match_content_sha256': text_sha(derived), 'cell_adaptations': adaptations,
            'raw_line_matches': lines, 'basis': DATA['basis'], 'semantic_review_status': 'pending',
            'source_text_changed': False}
