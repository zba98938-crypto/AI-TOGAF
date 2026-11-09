"""Source-bound preparation rejects changed/omitted/invented contexts and grants no review."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MAINT = ROOT / 'togaf-standard-10th-ai/maintenance'
SPEC = importlib.util.spec_from_file_location('material_preparation_inventory_target', MAINT / 'build_material_review_inventory.py')
inventory_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory_module)
adapter = inventory_module.preparation_dispositions

def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def signed_identity(unit):
    fields = ('id', 'document_id', 'family', 'kind', 'text_en', 'text_zh', 'source', 'source_document', 'source_locator', 'source_fragments')
    value = {key: unit[key] for key in fields if key in unit}
    return digest(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False))

class MaterialPreparationDispositionsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='togaf-material-preparation-test-')
        self.root = Path(self.tmp.name).resolve()
        self.c = self.root / 'togaf-standard-10th-ai'
        module_copy = self.root / adapter.MODULE_PATH
        module_copy.parent.mkdir(parents=True)
        shutil.copyfile(MAINT / 'material_preparation_dispositions.py', module_copy)
        self.source = self.c / 'sources/source.bin'
        self.source.parent.mkdir()
        self.source.write_bytes(b'original-local-source')
        self.image = self.c / 'figures/assets/source.png'
        self.image.parent.mkdir(parents=True)
        self.image.write_bytes(b'original-image-bytes')
        self.builder = inventory_module.Inventory(self.root)
        self.source_ref = self.builder.reference(self.source)
        self.image_ref = self.builder.reference(self.image)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, value):
        path = self.c / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False), encoding='utf-8')
        return path

    def add(self, identity, kind, original_path, pointer, text='', *, material='text', titles=(), source=None, **fields):
        unit = {'id': identity, 'document_id': 'G', 'family': 'series-guide', 'kind': kind, 'text_en': text,
                'source': source or self.source_ref, 'source_document': self.builder.reference(original_path),
                'source_locator': {'json_pointer': pointer}, 'source_material_form': material, **fields}
        self.builder.add(unit, titles=titles)
        return unit

    def profile(self, group, visual=None):
        rows = []
        for unit in self.builder.units:
            if unit['classification_basis']['confidence'] == 'uncertain':
                rows.append({'id': unit['id'], 'group': group,
                             'raw_binding_sha256': signed_identity(unit),
                             'original_classification_basis': copy.deepcopy(unit['classification_basis']),
                             'original_classification': unit['classification']})
        contexts = {}
        bindings = []
        if visual is not None:
            unit, path, strings = visual
            reference = self.builder.reference(path)
            for pointer, text in strings.items():
                contexts[reference['path'] + '#' + pointer] = {
                    'reference': reference, 'json_pointer': pointer, 'text_sha256': digest(text)}
            bindings.append({'id': unit['id'], 'raw_binding_sha256': signed_identity(unit), 'context_ids': sorted(contexts)})
        return {'schema_version': 'material-preparation-dispositions/1', 'baseline_inventory_sha256': 'a' * 64,
                'source_units': len(self.builder.units), 'dispositions': rows, 'visual_bindings': bindings, 'candidate_contexts': contexts}

    def apply(self, profile):
        path = self.write('maintenance/fixture-decisions.json', profile)
        return adapter.apply(self.builder, path)

    def caption(self, preceding=True, *, bad_order=False, bad_container=False):
        original = {'blocks': [
            {'id': 'G:image', 'kind': 'img' if preceding else 'p', 'text_en': '',
             'section_path': [{'title_en': '1. Source body'}], 'source_dom_order': 7 if bad_order else 4},
            {'id': 'G:caption', 'kind': 'p', 'text_en': 'Figure 1: Original caption', 'section_path': [],
             'parent_tag': 'p' if bad_container else 'div', 'parent_class': ['title'], 'source_dom_order': 5}]}
        path = self.write('documents/web.json', original)
        unit = self.add('G:caption', 'web-block', path, '/blocks/1', original['blocks'][1]['text_en'])
        return unit, self.profile('web-caption-context')

    def figure(self):
        detail = {'figure': {'title_en': None, 'title_zh': '历史图题'},
                  'elements': [{'label_zh': '相同候选'}], 'semantics': {'key_points_zh': ['历史解释']},
                  'unrelated': {'label_zh': '相同候选'}, 'historical_review': {'status': 'done'}}
        path = self.write('figures/G/source.json', detail)
        index = self.write('figures/index.json', {'figures': [
            {'id': 'G/figure', 'document_id': 'G', 'title_en': None, 'json_path': 'figures/G/source.json'}], 'embedded_images': []})
        unit = self.add('source-image:G/figure', 'figures', index, '/figures/0', material='image',
                        titles=['1. Body'], source_images=[self.image_ref])
        strings = {'/figure/title_zh': '历史图题', '/elements/0/label_zh': '相同候选', '/semantics/key_points_zh/0': '历史解释'}
        return unit, self.profile('guide-figure-no-title', (unit, path, strings))

    def test_caption_uses_exact_original_preceding_image_and_preserves_source(self):
        unit, profile = self.caption()
        before = adapter.immutable_binding(unit)
        result = self.apply(profile)
        self.assertEqual(result['supported_dispositions'], 1)
        self.assertEqual(result['pending_ids'], [])
        self.assertEqual(unit['classification_basis']['section_titles'], ['1. Source body'])
        self.assertEqual(unit['classification_basis']['confidence'], 'source-located-preparation')
        self.assertEqual(adapter.immutable_binding(unit), before)
        self.assertEqual(unit['review_status'], 'not-executed')
        self.assertFalse(unit['independent_model_review'])
        self.assertEqual(unit['human_professional_acceptance'], 'pending')
        self.assertEqual(unit['organizational_approval'], 'pending-signature')
        self.assertEqual(result['independent_semantic_reviews_executed'], 0)
        self.assertIn(adapter.MODULE_PATH, self.builder.inputs)

    def test_caption_missing_original_image_remains_pending_with_exact_id(self):
        unit, profile = self.caption(preceding=False)
        result = self.apply(profile)
        self.assertEqual(result['supported_dispositions'], 0)
        self.assertEqual(result['pending_ids'], [unit['id']])
        self.assertEqual(unit['classification_basis']['confidence'], 'uncertain')
        self.assertEqual(unit['classification_status'], 'pending-independent-adjudication')

    def test_caption_wrong_dom_order_remains_pending(self):
        unit, profile = self.caption(bad_order=True)
        self.assertEqual(self.apply(profile)['pending_ids'], [unit['id']])

    def test_caption_wrong_original_container_remains_pending(self):
        unit, profile = self.caption(bad_container=True)
        self.assertEqual(self.apply(profile)['pending_ids'], [unit['id']])

    def navigation(self, actual_href='#body'):
        self.source.write_text('<html><a href="' + actual_href + '"></a></html>')
        self.builder = inventory_module.Inventory(self.root)
        original = self.write('documents/navigation.json', {'toc': [{'text_en': '', 'href': '#body'}]})
        unit = self.add('G:navigation:00000', 'navigation-entry', original, '/toc/0', source=self.builder.reference(self.source))
        return unit, self.profile('empty-navigation')

    def test_empty_navigation_requires_exact_original_html_link(self):
        unit, profile = self.navigation()
        self.assertEqual(self.apply(profile)['supported_dispositions'], 1)
        self.assertEqual(unit['classification'], 'navigation')
        self.assertEqual(unit['text_en'], '')

    def test_empty_navigation_unrelated_original_link_does_not_prepare(self):
        unit, profile = self.navigation(actual_href='#other')
        self.assertEqual(self.apply(profile)['pending_ids'], [unit['id']])

    def blank_pdf(self, original_block_text):
        original = self.write('documents/blank.json', {'pages': [{'pdf_page': 1,
            'blocks': [{'id': 'b1', 'text': original_block_text, 'text_en': ''}],
            'content': [{'text': '', 'source_block_ids': ['b1']}]}]})
        unit = self.add('G:p0001:c000', 'pdf-content', original, '/pages/0/content/0')
        unit['source_locator'].update({'pdf_page': 1, 'source_block_ids': ['b1']})
        return unit, self.profile('empty-pdf-content')

    def test_pdf_whitespace_checks_actual_raw_text_not_text_en(self):
        unit, profile = self.blank_pdf(' \n\t')
        self.assertEqual(self.apply(profile)['supported_dispositions'], 1)
        self.assertEqual(unit['text_en'], '')

    def test_pdf_nonempty_raw_text_cannot_be_hidden_by_empty_text_en(self):
        unit, profile = self.blank_pdf('actual substantive source')
        self.assertEqual(self.apply(profile)['pending_ids'], [unit['id']])

    def test_missing_disposition_fails_without_partial_mutation(self):
        unit, profile = self.caption()
        before = copy.deepcopy(unit)
        profile['dispositions'] = []
        with self.assertRaisesRegex(ValueError, 'omits or replaces'):
            self.apply(profile)
        self.assertEqual(unit, before)

    def test_duplicate_disposition_fails_without_partial_mutation(self):
        unit, profile = self.caption()
        before = copy.deepcopy(unit)
        profile['dispositions'].append(copy.deepcopy(profile['dispositions'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate/unknown ID'):
            self.apply(profile)
        self.assertEqual(unit, before)

    def test_unknown_disposition_id_is_rejected(self):
        _, profile = self.caption()
        profile['dispositions'][0]['id'] = 'invented-source-unit'
        with self.assertRaisesRegex(ValueError, 'duplicate/unknown ID'):
            self.apply(profile)

    def test_changed_raw_text_binding_is_rejected(self):
        unit, profile = self.caption()
        unit['text_en'] = 'invented caption'
        with self.assertRaisesRegex(ValueError, 'changed raw source/ID/context binding'):
            self.apply(profile)

    def test_changed_source_locator_even_when_rehashed_is_rejected(self):
        unit, profile = self.caption()
        unit['source_locator']['json_pointer'] = '/blocks/0'
        profile['dispositions'][0]['raw_binding_sha256'] = signed_identity(unit)
        with self.assertRaises((ValueError, KeyError)):
            self.apply(profile)

    def test_changed_original_category_even_when_rehashed_is_rejected(self):
        _, profile = self.caption()
        profile['dispositions'][0]['original_classification'] = 'front-matter'
        with self.assertRaisesRegex(ValueError, 'changed raw source/ID/context binding'):
            self.apply(profile)

    def test_changed_original_basis_is_rejected(self):
        _, profile = self.caption()
        profile['dispositions'][0]['original_classification_basis']['section_titles'] = ['invented context']
        with self.assertRaisesRegex(ValueError, 'changed raw source/ID/context binding'):
            self.apply(profile)

    def test_wrong_kind_cannot_reuse_signed_disposition(self):
        unit, profile = self.caption()
        unit['kind'] = 'footnote'
        profile['dispositions'][0]['raw_binding_sha256'] = signed_identity(unit)
        with self.assertRaisesRegex(ValueError, 'changed raw source/ID/context binding'):
            self.apply(profile)

    def test_wrong_source_id_even_when_rehashed_is_rejected(self):
        unit, profile = self.caption()
        unit['id'] = 'G:invented'
        profile['dispositions'][0]['id'] = unit['id']
        profile['dispositions'][0]['raw_binding_sha256'] = signed_identity(unit)
        with self.assertRaisesRegex(ValueError, 'actual source unit ID/locator differs'):
            self.apply(profile)

    def test_wrong_source_fingerprint_even_when_rehashed_is_rejected(self):
        unit, profile = self.caption()
        unit['source'] = {**unit['source'], 'sha256': 'f' * 64}
        profile['dispositions'][0]['raw_binding_sha256'] = signed_identity(unit)
        with self.assertRaisesRegex(ValueError, 'outside acquired input closure'):
            self.apply(profile)

    def test_original_source_json_fingerprint_drift_is_rejected(self):
        unit, profile = self.caption()
        (self.root / unit['source_document']['path']).write_text('{"blocks":[]}')
        with self.assertRaisesRegex(ValueError, 'fingerprint conflict'):
            self.apply(profile)

    def test_original_binary_source_fingerprint_drift_is_rejected(self):
        _, profile = self.figure()
        self.source.write_bytes(b'changed-original-source')
        with self.assertRaisesRegex(ValueError, 'fingerprint conflict|Input changed'):
            self.apply(profile)

    def test_original_image_fingerprint_drift_is_rejected(self):
        _, profile = self.figure()
        self.image.write_bytes(b'changed-source-image')
        with self.assertRaisesRegex(ValueError, 'fingerprint conflict|Input changed'):
            self.apply(profile)

    def test_exact_historical_scalar_candidates_keep_null_and_unaccepted_status(self):
        unit, profile = self.figure()
        before = adapter.immutable_binding(unit)
        result = self.apply(profile)
        self.assertEqual(result['bound_English_body_visual_units'], 1)
        self.assertEqual(result['unique_historical_candidate_fields'], 3)
        self.assertEqual(adapter.immutable_binding(unit), before)
        original = json.loads((self.root / unit['source_document']['path']).read_text())['figures'][0]
        self.assertIsNone(original['title_en'])
        self.assertEqual(unit['text_en'], '')
        self.assertEqual(unit['translation_status'], 'original-visual-source-preserved-independent-review-pending')
        self.assertTrue(all(c['status'] == adapter.PENDING for c in unit['translation_candidates']))
        self.assertEqual(unit['historical_candidate_binding']['semantic_reliability'], 'not-certified')
        self.assertEqual(unit['review_status'], 'not-executed')
        self.assertFalse(unit['independent_model_review'])

    def test_missing_visual_binding_is_rejected(self):
        _, profile = self.figure()
        profile['visual_bindings'] = []
        with self.assertRaisesRegex(ValueError, 'omits or invents'):
            self.apply(profile)

    def test_duplicate_visual_binding_is_rejected(self):
        _, profile = self.figure()
        profile['visual_bindings'].append(copy.deepcopy(profile['visual_bindings'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate/unknown ID'):
            self.apply(profile)

    def test_duplicate_visual_candidate_field_is_rejected(self):
        _, profile = self.figure()
        profile['visual_bindings'][0]['context_ids'].append(profile['visual_bindings'][0]['context_ids'][0])
        with self.assertRaisesRegex(ValueError, 'field scope differs'):
            self.apply(profile)

    def test_omitted_related_visual_candidate_field_is_rejected(self):
        _, profile = self.figure()
        key = profile['visual_bindings'][0]['context_ids'].pop()
        profile['candidate_contexts'].pop(key)
        with self.assertRaisesRegex(ValueError, 'field scope differs'):
            self.apply(profile)

    def test_unrelated_equal_text_and_valid_hash_cannot_replace_source_field(self):
        _, profile = self.figure()
        old = next(key for key in profile['candidate_contexts'] if key.endswith('/elements/0/label_zh'))
        new = old.split('#')[0] + '#/unrelated/label_zh'
        entry = profile['candidate_contexts'].pop(old)
        entry['json_pointer'] = '/unrelated/label_zh'
        profile['candidate_contexts'][new] = entry
        contexts = profile['visual_bindings'][0]['context_ids']
        contexts[contexts.index(old)] = new
        with self.assertRaisesRegex(ValueError, 'field scope differs'):
            self.apply(profile)

    def test_rehashed_catalog_locator_cannot_invent_candidate_relation(self):
        _, profile = self.figure()
        key = next(iter(profile['candidate_contexts']))
        entry = profile['candidate_contexts'][key]
        entry['json_pointer'] = '/unrelated/label_zh'
        entry['text_sha256'] = digest('相同候选')
        with self.assertRaisesRegex(ValueError, 'omits or invents'):
            self.apply(profile)

    def test_non_chinese_field_cannot_be_added_as_a_historical_candidate(self):
        _, profile = self.figure()
        reference = next(iter(profile['candidate_contexts'].values()))['reference']
        key = reference['path'] + '#/figure/title_en'
        profile['candidate_contexts'][key] = {'reference': reference, 'json_pointer': '/figure/title_en', 'text_sha256': digest('')}
        profile['visual_bindings'][0]['context_ids'].append(key)
        with self.assertRaisesRegex(ValueError, 'field scope differs'):
            self.apply(profile)

    def test_original_candidate_source_bytes_drift_is_rejected(self):
        _, profile = self.figure()
        reference = next(iter(profile['candidate_contexts'].values()))['reference']
        (self.root / reference['path']).write_text('{"figure":{"title_zh":"changed"}}')
        with self.assertRaisesRegex(ValueError, 'fingerprint conflict|Input changed'):
            self.apply(profile)

    def footnote(self, conflicting=False):
        anchor = '_footnotedef_1'
        call = {'id': 'G:call', 'html': '<a id="_footnoteref_1"></a>', 'section_path': [{'title_en': '1. Body'}]}
        blocks = [call]
        if conflicting:
            blocks.append({**call, 'section_path': [{'title_en': 'References'}]})
        original = self.write('documents/footnote.json', {'blocks': blocks, 'footnotes': [{'id': anchor, 'text_en': 'Original qualification'}]})
        unit = self.add('G:footnote:' + anchor, 'footnote', original, '/footnotes/0', 'Original qualification')
        unit['source_locator']['anchor'] = anchor
        return unit, self.profile('footnote-context')

    def test_footnote_uses_original_body_callout_context(self):
        unit, profile = self.footnote()
        self.assertEqual(self.apply(profile)['supported_dispositions'], 1)
        self.assertEqual(unit['classification_basis']['section_titles'], ['1. Body'])
        self.assertEqual(unit['text_en'], 'Original qualification')

    def test_footnote_conflicting_callout_contexts_remain_pending(self):
        unit, profile = self.footnote(conflicting=True)
        self.assertEqual(self.apply(profile)['pending_ids'], [unit['id']])

    def author_continuation(self, prior_author_heading=True):
        pages = [{'pdf_page': index + 1, 'text': ''} for index in range(40)]
        pages[36]['text'] = '关于作者' if prior_author_heading else '正文'
        pages[37]['text'] = 'Chris Searle 与 Graham Neal'
        original = self.write('documents/W242C.json', {'pages': pages})
        unit = {'id': 'W242C:p0038', 'document_id': 'W242C', 'family': 'supplementary', 'kind': 'pdf-page',
                'text_zh': pages[37]['text'], 'source': self.source_ref, 'source_document': self.builder.reference(original),
                'source_locator': {'json_pointer': '/pages/37', 'pdf_page': 38}}
        self.builder.add(unit, chinese=True)
        return unit, self.profile('w242c-publication-pages')

    def test_publication_author_continuation_keeps_original_chinese_text(self):
        unit, profile = self.author_continuation()
        before = adapter.immutable_binding(unit)
        self.assertEqual(self.apply(profile)['supported_dispositions'], 1)
        self.assertEqual(unit['classification'], 'front-matter')
        self.assertEqual(adapter.immutable_binding(unit), before)
        self.assertEqual(unit['translation_status'], 'original-chinese-source-preserved')
        self.assertEqual(unit['translation_candidates'], [])

    def test_publication_author_continuation_without_prior_heading_stays_pending(self):
        unit, profile = self.author_continuation(prior_author_heading=False)
        self.assertEqual(self.apply(profile)['pending_ids'], [unit['id']])
        self.assertEqual(unit['classification'], 'body')

    def test_historical_done_flag_is_not_promoted_to_review(self):
        unit, profile = self.figure()
        self.apply(profile)
        self.assertEqual(unit['review_status'], 'not-executed')
        self.assertEqual(unit['classification_preparation']['independent_semantic_review'], 'not-executed')

    def test_profile_cannot_add_semantic_acceptance_fields(self):
        _, profile = self.figure()
        profile['dispositions'][0]['review_status'] = 'pass'
        with self.assertRaisesRegex(ValueError, 'row schema differs'):
            self.apply(profile)

    def test_profile_cannot_override_candidate_status(self):
        _, profile = self.figure()
        profile['visual_bindings'][0]['status'] = 'accepted'
        with self.assertRaisesRegex(ValueError, 'visual binding schema differs'):
            self.apply(profile)

    def test_preparation_cannot_inherit_claimed_independent_review(self):
        unit, profile = self.caption()
        unit['independent_model_review'] = True
        with self.assertRaisesRegex(ValueError, 'semantic acceptance'):
            self.apply(profile)

    def test_preparation_cannot_inherit_claimed_human_acceptance(self):
        unit, profile = self.caption()
        unit['human_professional_acceptance'] = 'accepted'
        with self.assertRaisesRegex(ValueError, 'semantic acceptance'):
            self.apply(profile)

    def test_preparation_cannot_inherit_claimed_organizational_approval(self):
        unit, profile = self.caption()
        unit['organizational_approval'] = 'approved'
        with self.assertRaisesRegex(ValueError, 'semantic acceptance'):
            self.apply(profile)

    def test_boolean_source_count_is_rejected(self):
        _, profile = self.caption()
        profile['source_units'] = True
        with self.assertRaisesRegex(ValueError, 'source unit scope differs'):
            self.apply(profile)

    def test_duplicate_json_key_is_rejected(self):
        _, profile = self.caption()
        path = self.write('maintenance/fixture-decisions.json', profile)
        raw = path.read_text()
        path.write_text(raw[:-1] + ',"source_units":1}')
        with self.assertRaisesRegex(ValueError, 'duplicate preparation decision JSON key'):
            adapter.apply(self.builder, path)

    def test_nonfinite_json_value_is_rejected(self):
        _, profile = self.caption()
        path = self.write('maintenance/fixture-decisions.json', profile)
        raw = path.read_text().replace('"source_units": 1', '"source_units": NaN')
        path.write_text(raw)
        with self.assertRaisesRegex(ValueError, 'nonfinite preparation decision JSON'):
            adapter.apply(self.builder, path)

    def test_preparation_manifest_path_escape_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'escapes repository'):
            inventory_module.Inventory(self.root, preparation_manifest=self.root.parent / 'outside.json')

    def test_preparation_manifest_symlink_is_rejected(self):
        _, profile = self.caption()
        path = self.write('maintenance/original.json', profile)
        link = self.c / 'maintenance/link.json'
        link.symlink_to(path)
        with self.assertRaisesRegex(ValueError, 'symlink forbidden'):
            adapter.apply(self.builder, link)

    def scope_build(self, builder):
        for index in range(26):
            self.write('documents/G' + str(index) + '.json', {})
        for index in range(6):
            self.write('fundamental/web-2025/volumes/V' + str(index) + '/document.json', {})
        def guide(path):
            builder.documents.append({'document_id': path.stem, 'family': 'series-guide'})
        def foundation(path):
            builder.documents.append({'document_id': path.parent.name, 'family': 'fundamental'})
        def supplement(path):
            builder.documents.append({'document_id': path.stem, 'family': 'supplementary'})
        with patch.object(builder, 'guide', guide), patch.object(builder, 'foundation', foundation), patch.object(builder, 'supplement', supplement):
            return builder.build()

    def empty_profile(self):
        return {'schema_version': 'material-preparation-dispositions/1', 'baseline_inventory_sha256': 'a' * 64,
                'source_units': 0, 'dispositions': [], 'visual_bindings': [], 'candidate_contexts': {}}

    def test_default_fixed_static_manifest_is_explicitly_recorded_in_inputs(self):
        path = self.root / adapter.DEFAULT_MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.empty_profile()))
        builder = inventory_module.Inventory(self.root)
        inventory = self.scope_build(builder)
        self.assertEqual(inventory['source_preparation']['application_mode'], 'default-static-source-manifest')
        self.assertEqual(inventory['source_preparation']['manifest']['path'], adapter.DEFAULT_MANIFEST)
        self.assertEqual(inventory['input_sha256'][adapter.DEFAULT_MANIFEST], inventory_module.sha(path))

    def test_explicit_manifest_mode_records_exact_selected_reference(self):
        path = self.write('maintenance/selected.json', self.empty_profile())
        builder = inventory_module.Inventory(self.root, preparation_manifest=path)
        inventory = self.scope_build(builder)
        self.assertEqual(inventory['source_preparation']['application_mode'], 'explicit-manifest')
        self.assertEqual(inventory['source_preparation']['manifest']['path'], path.relative_to(self.root).as_posix())

    def test_explicit_opt_out_does_not_read_static_decisions_or_add_inventory_metadata(self):
        path = self.root / adapter.DEFAULT_MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('malformed static decision JSON')
        builder = inventory_module.Inventory(self.root, preparation_manifest=False)
        inventory = self.scope_build(builder)
        self.assertEqual(builder.preparation_mode, 'explicit-disabled')
        self.assertIsNone(builder.preparation_result)
        self.assertNotIn('source_preparation', inventory)
        self.assertNotIn(adapter.DEFAULT_MANIFEST, inventory['input_sha256'])
        self.assertNotIn(adapter.MODULE_PATH, inventory['input_sha256'])

    def test_arbitrary_ignored_evidence_directory_cannot_enable_source_preparation(self):
        path = self.root / 'output/forged-r7/decisions.json'
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(self.empty_profile()))
        builder = inventory_module.Inventory(self.root)
        inventory = self.scope_build(builder)
        self.assertEqual(builder.preparation_mode, 'static-source-manifest-unavailable')
        self.assertIsNone(builder.preparation_result)
        self.assertNotIn('source_preparation', inventory)
        self.assertNotIn(path.relative_to(self.root).as_posix(), inventory['input_sha256'])

    def test_explicit_missing_manifest_fails_closed(self):
        builder = inventory_module.Inventory(self.root, preparation_manifest=self.c / 'maintenance/missing.json')
        with self.assertRaisesRegex(ValueError, 'Explicit material preparation manifest is missing'):
            self.scope_build(builder)

if __name__ == '__main__':
    unittest.main()
