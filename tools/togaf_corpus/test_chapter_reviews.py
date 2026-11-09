"""Catch lost source paragraphs, fabricated quotations and stale translations."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from chapter_reviews import validate_review
from query import search

ROOT=Path(__file__).resolve().parents[2]


class ChapterReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review=json.loads((ROOT/'tools/togaf_corpus/chapter-review-data/G249.json').read_text())
        cls.document=json.loads((ROOT/'togaf-standard-10th-ai/documents/G249.json').read_text())

    def test_dropped_body_paragraph_is_detected_even_when_declared_count_is_updated(self):
        changed=copy.deepcopy(self.review)
        section=next(s for s in changed['sections'] if s['section_number']=='1')
        section['source_units'].pop()
        changed['coverage']['source_content_units']-=1
        with self.assertRaisesRegex(ValueError,'declared body pages have unreviewed units'):
            validate_review(changed,self.document,ROOT)

    def test_heading_container_cannot_hide_untranslated_body(self):
        changed=copy.deepcopy(self.review)
        changed['sections'][0]['status']='section-container'
        changed['sections'][0]['translation_zh']=''
        with self.assertRaisesRegex(ValueError,'container hides body text'):
            validate_review(changed,self.document,ROOT)

    def test_fabricated_quote_is_detected(self):
        changed=copy.deepcopy(self.review)
        changed['sections'][0]['semantic_rules'][0]['evidence'][0]['quote_en']='All architects must report to this person.'
        with self.assertRaisesRegex(ValueError,'quote not in source unit'):
            validate_review(changed,self.document,ROOT)

    def test_only_reviewed_aligned_translation_sections_are_replaced_in_default_query(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder);(p/'retrieval').mkdir();(p/'chapters').mkdir()
            old={'id':'old-reviewed','document_id':'G249','content_role':'translation','section_id':'G249:s0013','text':'architect old mistake'}
            pending={**old,'id':'old-pending','section_id':'G249:s0001','text':'architect pending front matter'}
            new={**old,'id':'new','content_role':'chapter-review','text':'architect revised source'}
            (p/'retrieval/chunks.jsonl').write_text('\n'.join(json.dumps(c) for c in [old,pending]))
            (p/'retrieval/chapter-chunks.jsonl').write_text(json.dumps(new)+'\n')
            (p/'chapters/index.json').write_text(json.dumps({'documents':[{'document_id':'G249','reviewed_section_ids':['G249:s0013']}]}))
            result=search('architect',p)
            self.assertEqual({r['id'] for r in result['results']},{'new','old-pending'})
            self.assertEqual(result['superseded_translation_section_chunks'],1)
            history=search('architect',p,roles=['translation'])
            self.assertEqual({r['id'] for r in history['results']},{'old-reviewed','old-pending'})
            self.assertTrue(all(r['retrieval_status']=='translation-unverified' for r in history['results']))


if __name__=='__main__':unittest.main()
