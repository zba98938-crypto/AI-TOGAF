"""Historical extraction must never reintroduce the rejected sixth G152 arrow."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
CORPUS = REPO / 'togaf-standard-10th-ai'
SHARED = CORPUS / 'skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
import build_corpus_registry
import corpus_query
from sync_reviewed_figure_sources import current_structure, source_evidence, CURRENT_AVAILABILITY


class ReviewedFigureSourcesTest(unittest.TestCase):
    def assert_five_arrows(self, portable):
        self.assertEqual(5, sum(r['explicit'] is True for r in portable['relationships']))
        self.assertNotIn(('value_chains', 'capabilities'), {(r['from'], r['to']) for r in portable['relationships']})
        self.assertEqual(['capabilities', 'processes', 'business_services', 'applications', 'ict_infrastructure', 'technical_components'], portable['flows'][0]['steps'])
        self.assertIn('五条', portable['flows'][0]['description_zh'])
        self.assertIn('没有', portable['reading']['line_semantics_zh'])

    def test_current_portable_graph_and_flow_use_five_source_arrows(self):
        self.assert_five_arrows(current_structure(CORPUS, 'G152/fig3-1'))
        self.assert_five_arrows(json.loads((SHARED / 'references/source-structures/G152-fig3-1.json').read_text()))

    def test_full_builder_does_not_restore_historical_sixth_arrow(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shared, source = root / 'shared', root / 'source'
            for relative in ['reviews', 'references/source-structures']:
                (shared / relative).mkdir(parents=True)
            (source / 'figs/ai/G152').mkdir(parents=True)
            original = CORPUS / 'sources/retained/togaf-standard-10th-zh/figs/ai/G152/fig3-1.json'
            shutil.copyfile(original, source / 'figs/ai/G152/fig3-1.json')
            history = json.loads(original.read_text())
            self.assertTrue(any(r['from'] == 'value_chains' and r['to'] == 'capabilities' for r in history['relationships']))
            (shared / 'capabilities.json').write_text(json.dumps({'profiles': [], 'analysis_methods': [], 'work_products': [], 'figure_profiles': []}))
            (shared / 'artifacts.json').write_text('{"artifacts": []}')
            (shared / 'reviews/tri-source-observations.json').write_text('{"observations": []}')
            (shared / 'reviews/source-visual-triage.json').write_text('{"reviewed": []}')
            (shared / 'corpus').symlink_to(SHARED / 'corpus', target_is_directory=True)
            with patch.object(build_corpus_registry, 'ROOT', shared), patch.object(build_corpus_registry, 'locate_corpus', return_value=CORPUS):
                build_corpus_registry.build(source)
            self.assert_five_arrows(json.loads((shared / 'references/source-structures/G152-fig3-1.json').read_text()))
            row = json.loads((shared / 'capabilities.json').read_text())['figure_profiles'][0]
            self.assertEqual(CURRENT_AVAILABILITY, row['current_semantic_review'])
            self.assertEqual('not-established-by-source-review', row['generated_view_acceptance'])

    def test_portable_crop_tampering_blocks_source_availability(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'corpus/figures/assets/G152').mkdir(parents=True)
            shutil.copyfile(SHARED / 'corpus/source-map.json', root / 'corpus/source-map.json')
            (root / 'corpus/sources').symlink_to(SHARED / 'corpus/sources', target_is_directory=True)
            (root / 'corpus/figures/assets/G152/fig3-1-p0022.png').write_bytes(b'changed crop')
            reviews = json.loads((CORPUS / 'maintenance/pipeline/architecture-diagram-reviews.json').read_text())
            with self.assertRaisesRegex(ValueError, 'portable source asset missing or changed'):
                source_evidence(CORPUS, root, 'G152/fig3-1', reviews)

    def test_nineteen_old_missing_sources_are_available_without_generated_acceptance(self):
        registry = json.loads((SHARED / 'capabilities.json').read_text())
        rows = [f for f in registry['figure_profiles'] if f.get('source_availability_sync')]
        self.assertEqual(19, len(rows))
        for row in rows:
            with self.subTest(figure=row['id']):
                self.assertEqual('no-renderable-source-image', row['historical_source_availability']['current_semantic_review'])
                self.assertEqual('original-pdf-crop-available', row['source_status'])
                self.assertEqual('not-established-by-source-review', row['generated_view_acceptance'])
                self.assertTrue(row['source_availability_sync']['source_crops'])
                review = row['source_availability_sync']['source_review']
                self.assertTrue((SHARED / review['path']).is_file())
                self.assertIn(row['id'], json.loads((SHARED / review['path']).read_text())['figures'])

    def test_package_query_excludes_superseded_figure_but_keeps_unreplaced_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'retrieval').mkdir()
            (root / 'architecture/diagrams').mkdir(parents=True)
            (root / 'architecture/diagrams/index.json').write_text(json.dumps({'diagrams': [{'id': 'G152/fig3-1'}]}))
            common = {'document_id': 'G152', 'source_path': 'source.json', 'source_sha256': None}
            historical = [dict(common, id='old', text='业务栈沿6个向下箭头', content_role='figure', figure_ids=['G152/fig3-1']),
                          dict(common, id='unreplaced', text='业务栈没有当前复核的来源', content_role='figure', figure_ids=['unreviewed'])]
            current = dict(common, id='new', text='业务栈五条向下箭头；价值链与能力之间没有线', content_role='diagram', figure_ids=['G152/fig3-1'])
            (root / 'retrieval/chunks.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in historical))
            (root / 'retrieval/architecture-chunks.jsonl').write_text(json.dumps(current, ensure_ascii=False) + '\n')
            with patch.object(corpus_query, 'CORPUS', root):
                results = corpus_query.query('业务栈', limit=10)
            self.assertEqual({'new', 'unreplaced'}, {r['id'] for r in results})


if __name__ == '__main__':
    unittest.main()
