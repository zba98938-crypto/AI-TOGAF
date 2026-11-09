"""Regressions for G249 paragraph attribution and current diagram meaning."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from architecture_analysis import source_location_for_quote
from architecture_diagrams import analyse, load_reviews, portable_source_structure, reviewed_semantics
from build_architecture import compact
from query import search

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / 'togaf-standard-10th-ai'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


class SourceSectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = read(CORPUS / 'documents/G249.json')

    def test_same_page_paragraphs_keep_their_own_role_section(self):
        cases = [
            (14, 'Have a clear mandate', '3. Architecture Roles and Skills: The Basis of an Enterprise Architecture Practice'),
            (17, 'The Chief Architect is a special case', '4. Architecture Roles'),
            (19, 'Stakeholder satisfaction score', '4.1. Chief Architect'),
            (19, 'Enterprise Architects are very experienced', '4.2. Enterprise Architect'),
            (21, 'Services delivering and accepted', '4.2. Enterprise Architect'),
            (21, 'A segment is a coherent grouping', '4.3. Segment Architect (Business and Technical)'),
            (23, 'Services (related to the elements overseen', '4.3. Segment Architect (Business and Technical)'),
            (23, 'Solution Architects are experienced', '4.4. Solution Architect'),
        ]
        for page, quote, section in cases:
            with self.subTest(page=page, quote=quote):
                result = source_location_for_quote(self.document, page, quote)
                self.assertEqual(result['source_section']['title'], section)
                self.assertTrue(result['source_block_ids'])
                self.assertTrue(all(f':p{page:04}:' in bid for bid in result['source_block_ids']))

    def test_table_line_breaks_preserve_quote_and_table_identity(self):
        result = source_location_for_quote(self.document, 27, 'Solution Architect')
        self.assertEqual(result['source_section']['title'], '5. Skills and Proficiency Levels')
        self.assertEqual(result['source_table_ids'], ['G249:p0027:t02'])

    def test_unknown_quote_is_rejected_instead_of_page_guess(self):
        with self.assertRaisesRegex(ValueError, 'cannot be located'):
            source_location_for_quote(self.document, 21, 'invented source quote')

    def test_repeated_quote_across_headings_is_explicitly_ambiguous(self):
        doc = {'id': 'test', 'outline': [{'id': 'a', 'title': 'A', 'level': 1}, {'id': 'b', 'title': 'B', 'level': 1}],
               'pages': [{'pdf_page': 1, 'content': [
                   {'type': 'heading', 'text': 'A', 'section_id': 'a'},
                   {'type': 'text', 'text': 'same claim', 'source_block_ids': ['a1']},
                   {'type': 'heading', 'text': 'B', 'section_id': 'b'},
                   {'type': 'text', 'text': 'same claim', 'source_block_ids': ['b1']}]}]}
        result = source_location_for_quote(doc, 1, 'same claim')
        self.assertIsNone(result['source_section'])
        self.assertEqual(result['source_section_candidates'], ['a', 'b'])
        self.assertEqual(result['source_block_ids'], ['a1', 'b1'])


class CurrentG249SemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        document = read(CORPUS / 'documents/G249.json')
        reviews = load_reviews(ROOT)
        cls.records = {}
        for number in ('fig4-1', 'fig4-2'):
            path = CORPUS / f'figures/G249/{number}.json'
            cls.records[number] = analyse(read(path), document, path, ROOT, CORPUS, reviews)

    def test_review_replaces_prose_without_retrieving_archived_claims(self):
        forbidden = ['两个灰色 Domain 框', 'System 1..* contains Building Block 1..*',
                     'System 到 Building Block 的连线表示组成', 'System–Building Block 的连线两端有']
        for record in self.records.values():
            self.assertEqual(record['analysis']['source_semantics_status'], 'current-source-review-replacement')
            self.assertIn('previous_source_semantics', record)
            active = json.dumps(compact(record), ensure_ascii=False)
            for phrase in forbidden:
                self.assertNotIn(phrase, active)
            self.assertEqual(record['analysis']['line_explanation_zh'], record['current_visual_review']['semantics_overrides']['line_semantics_zh'])

    def test_complete_review_cannot_fall_back_to_a_missing_legacy_field(self):
        source = read(CORPUS / 'figures/G249/fig4-1.json')
        review = deepcopy(load_reviews(ROOT)['figures'][source['id']])
        del review['semantics_overrides']['key_points_zh']
        with self.assertRaisesRegex(ValueError, 'incomplete reviewed semantics'):
            reviewed_semantics(source, review)

    def test_vertical_interactions_have_no_borrowed_labels(self):
        record = self.records['fig4-1']
        edges = {edge['source_relation_index']: edge for edge in record['edges']}
        for index in (6, 8):
            self.assertEqual(edges[index]['direction'], 'bidirectional')
            self.assertIsNone(edges[index]['label_en'])
            self.assertIsNone(edges[index]['label_zh'])
        self.assertEqual({e['source_relation_index'] for e in record['rejected_edges']}, {7, 9})
        for local_id in ('business_domain', 'tech_domain'):
            node = next(n for n in record['nodes'] if n['local_id'] == local_id)
            self.assertEqual(node['group_parent'], 'G249/fig4-1#domain_scope')

    def test_nesting_does_not_invent_connector_or_system_cardinality(self):
        record = self.records['fig4-2']
        edge = next(e for e in record['edges'] if e['source_relation_index'] == 4)
        self.assertFalse(edge['visual']['explicit_connection'])
        self.assertEqual(edge['visual']['line_style'], 'implicit')
        self.assertEqual(edge['visual']['arrow'], 'none')
        self.assertEqual(edge['cardinality'], 'unspecified:1..*')
        self.assertIsNone(edge['endpoint_cardinalities']['from'])
        self.assertEqual(edge['endpoint_cardinalities']['to'], '1..*')
        service = next(n for n in record['nodes'] if n['local_id'] == 'service')
        self.assertIsNone(service['group_parent'])

    def test_historical_aggregate_nodes_do_not_duplicate_visible_objects(self):
        for number, aggregate in [('fig4-1', 'deliverables'), ('fig4-2', 'business_subdomains')]:
            record = self.records[number]
            self.assertNotIn(aggregate, {n['local_id'] for n in record['nodes']})
            rejected = next(n for n in record['rejected_nodes'] if n['local_id'] == aggregate)
            self.assertTrue(rejected['source_element'])
            self.assertTrue(rejected['rejection_reason_zh'])
        self.assertEqual({'business_xx_left', 'business_xx_center', 'business_ellipsis'},
                         {n['local_id'] for n in self.records['fig4-2']['nodes']
                          if n['label_en'] in ('XX', '..')})

    def test_portable_skills_reference_uses_current_edges_and_separate_history(self):
        for record in self.records.values():
            portable = portable_source_structure(record)
            self.assertEqual(len(portable['relationships']), len(record['edges']))
            self.assertEqual({r['id'] for r in portable['elements']}, {n['local_id'] for n in record['nodes']})
            self.assertEqual(portable['reading']['key_points_zh'], record['analysis']['source_logic_zh'])
            self.assertIn('/figures/G249/', portable['historical_source']['path'])
            self.assertNotIn('previous_source_semantics', portable)


class PublishedG249RetrievalTests(unittest.TestCase):
    def test_default_query_does_not_return_superseded_readings(self):
        for phrase in ('两个灰色 Domain 框', 'System 1..* contains Building Block 1..*',
                       'System 到 Building Block 的连线表示组成'):
            result = search(phrase, CORPUS, docs=['G249'], full_text=True, limit=1000)
            self.assertTrue(result['superseded_historical_figure_chunks'])
            self.assertTrue(result['results'])
            for row in result['results']:
                self.assertNotIn(phrase, row['text'], row['id'])

    def test_published_portable_reference_is_exact_current_projection(self):
        from architecture_diagrams import sha
        for number in ('fig4-1', 'fig4-2'):
            path = CORPUS / f'architecture/diagrams/G249/{number}.json'
            portable = read(ROOT / f'togaf-standard-10th-ai/skills/_shared/references/source-structures/G249-{number}.json')
            expected = portable_source_structure(read(path), current_sha256=sha(path))
            self.assertEqual(portable, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
