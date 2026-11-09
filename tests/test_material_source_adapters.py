"""Pinned-source CO2e adaptation tests; these do not certify translation semantics."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MAINT = ROOT / 'togaf-standard-10th-ai/maintenance'
SPEC = importlib.util.spec_from_file_location('source_adapter_test_target', MAINT / 'material_source_adapters.py')
module = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(module)
SPEC2 = importlib.util.spec_from_file_location('source_inventory_adapter_test_target', MAINT / 'build_material_review_inventory.py')
builder_module = importlib.util.module_from_spec(SPEC2); SPEC2.loader.exec_module(builder_module)
EXPECTED = {'G242:p0066:b018','G242:p0066:b032','G242:p0066:b041','G242:p0080:b031','G242:p0093:b006',
    'G242:p0098:b023','G242:p0098:b024','G242:p0098:b028','G242:p0098:b029','G242:p0098:b036',
    'G242:p0098:b037','G242:p0098:b041','G242:p0098:b042'}


class ExactMaterialSourceAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document_path = ROOT / 'togaf-standard-10th-ai/documents/G242.json'
        cls.doc = json.loads(cls.document_path.read_text())
        cls.document_ref = {'path':'togaf-standard-10th-ai/documents/G242.json', 'sha256':builder_module.sha(cls.document_path)}
        cls.blocks = {b['id']: b for p in cls.doc['pages'] for b in p['blocks']}
        cls.tables = {f'G242:p{p["pdf_page"]:04}:c{i:03}':t for p in cls.doc['pages'] for i,t in enumerate(p['content']) if t['type']=='table'}

    def adapt(self, identity, *, block=None, table=None, source=None, document=None, table_id=None, code='G242'):
        table_id = table_id or module.DATA['raw_blocks'][identity]['table_unit_id']
        return module.g242_table_adaptation(code, source or self.doc['source'], document or self.document_ref,
            block or self.blocks[identity], table_id, table or self.tables[table_id])

    def test_all_thirteen_original_blocks_bind_four_existing_table_contexts(self):
        self.assertEqual(set(module.DATA['raw_blocks']), EXPECTED)
        before = copy.deepcopy(self.doc); bindings = [self.adapt(identity) for identity in sorted(EXPECTED)]
        self.assertTrue(all(bindings)); self.assertEqual(len({b['table_unit_id'] for b in bindings}), 4)
        for binding in bindings:
            self.assertFalse(binding['source_text_changed']); self.assertEqual(binding['semantic_review_status'], 'pending')
            self.assertTrue(any('CO2e' in line for line in binding['raw_line_matches']))
            self.assertTrue(all(c['original'] != c['derived_match_representation'] for c in binding['cell_adaptations']))
        self.assertEqual(self.doc, before)

    def test_exact_known_subscript_cells_only(self):
        self.assertEqual(module.exact_cell_representation('kgCOe/device<br>2'), 'kgCO2e/device')
        self.assertEqual(module.exact_cell_representation('kgCOe/<br>2<br>monetary unit'), 'kgCO2e/<br>monetary unit')
        for value in ('text<br>2','kgCOe/device<br>20','kgCOe/device<br>2<br>2','COe<br>2','COe<br>2|another cell',
                      'other text COe<br>2','kgCOe/device <br>2','kgCOe/device<br>3'):
            with self.subTest(value=value): self.assertIsNone(module.exact_cell_representation(value))

    def test_wrong_source_document_table_and_block_cannot_adapt(self):
        identity = 'G242:p0066:b018'; table = copy.deepcopy(self.tables['G242:p0066:c003'])
        for label in ('source', 'document', 'block-text', 'block-bbox', 'table-text', 'table-bbox', 'wrong-code', 'wrong-table'):
            kwargs = {}
            if label == 'source': kwargs['source'] = {**self.doc['source'], 'sha256':'a'*64}
            elif label == 'document': kwargs['document'] = {**self.document_ref, 'sha256':'a'*64}
            elif label.startswith('block'):
                block = copy.deepcopy(self.blocks[identity])
                if label == 'block-text': block['text'] += 'extra arbitrary body line'
                else: block['bbox'][0] += 1
                kwargs['block'] = block
            elif label.startswith('table'):
                changed = copy.deepcopy(table)
                if label == 'table-text': changed['text'] = changed['text'].replace('COe/device<br>2', 'text<br>2')
                else: changed['bbox'][0] += 1
                kwargs['table'] = changed
            elif label == 'wrong-code': kwargs['code'] = 'G249'
            else: kwargs['table_id'] = 'G242:p0098:c006'
            with self.subTest(label=label): self.assertIsNone(self.adapt(identity, **kwargs))

    def test_new_inventory_candidates_do_not_change_raw_text_locators_or_acceptance(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve(); c = root / 'togaf-standard-10th-ai'
            for relative in ('documents/G242.json','chapters/G242.json','maintenance/material-source-adapters/g242-co2e-binding.json'):
                path = c / relative; path.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ROOT/'togaf-standard-10th-ai'/relative, path)
            pdf = root / 'togaf-standard-10th/G242e.pdf'; pdf.parent.mkdir(); shutil.copyfile(ROOT/'togaf-standard-10th-ai/skills/_shared/corpus/sources/pdf/G242e.pdf', pdf)
            builder = builder_module.Inventory(root); builder.guide(c/'documents/G242.json')
            units = {u['id']:u for u in builder.units}; changed = [u for u in builder.units if u.get('source_binding_adaptations')]
            self.assertEqual({u['id'] for u in changed}, EXPECTED)
            sections = {'G242:p0066:c003':'/sections/47','G242:p0080:c001':'/sections/63',
                        'G242:p0093:c000':'/sections/79','G242:p0098:c006':'/sections/80'}
            for u in changed:
                raw = self.blocks[u['id']]; binding = u['source_binding_adaptations'][0]
                self.assertEqual(u['text_en'], raw['text']); self.assertEqual(u['source_locator']['bbox'], raw['bbox'])
                self.assertEqual(u['source_content_sha256'], module.text_sha(raw['text']))
                self.assertEqual(u['translation_candidates'], units[binding['table_unit_id']]['translation_candidates'])
                self.assertEqual(u['translation_candidates'][0]['json_pointer'], sections[binding['table_unit_id']])
                self.assertEqual(u['translation_status'], 'candidate-translation-present-independent-review-pending')
                self.assertFalse(u['independent_model_review']); self.assertEqual(u['review_status'], 'not-executed')
                self.assertEqual(u['human_professional_acceptance'], 'pending')


if __name__ == '__main__': unittest.main()
