"""Source-unit inventory covers raw leftovers and never promotes authored material."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('material_inventory', ROOT / 'togaf-standard-10th-ai/maintenance/build_material_review_inventory.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class MaterialSourceInventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='togaf-material-inventory-test-')
        self.root = Path(self.tmp.name).resolve()
        self.c = self.root / 'togaf-standard-10th-ai'
        self.c.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, relative, data):
        path = self.c / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
        return path

    def guide_fixture(self, stale=False):
        pdf = self.c / 'sources/fixture.pdf'; pdf.parent.mkdir(); pdf.write_bytes(b'local-only-source')
        source = {'path':'togaf-standard-10th-ai/sources/fixture.pdf','sha256':module.sha(pdf)}
        outline = [{'id':'G:s1','pdf_page':1,'y':0,'title':'Cover','number':None,'parent_id':None},
                   {'id':'G:s2','pdf_page':2,'y':0,'title':'Contents','number':None,'parent_id':None},
                   {'id':'G:s3','pdf_page':3,'y':0,'title':'1. Scope','number':'1','parent_id':None},
                   {'id':'G:s4','pdf_page':4,'y':0,'title':'References','number':None,'parent_id':None}]
        pages = []
        for page, text in enumerate(['Title','', 'Required body', 'Reference source'],1):
            raw = [{'id':f'G:p{page:04}:b1','text':text or 'Scope ........ 3','bbox':[20,50,200,70],'role':'body'},
                   {'id':f'G:p{page:04}:b2','text':'running header','bbox':[20,10,200,20],'role':'running-matter'}]
            if page == 3:
                raw.append({'id':'G:p0003:b3','text':'unmapped substantive content','bbox':[20,100,200,120],'role':'body'})
            pages.append({'pdf_page':page,'raw_text':text,'blocks':raw,
                          'content':[{'type':'text','text':text,'bbox':[20,50,200,70],'source_block_ids':[raw[0]['id']]}]})
        doc = self.write('documents/G.json',{'id':'G','source':source,'outline':outline,'pages':pages})
        self.write('chapters/G.json',{'source':source,'sections':[{'translation_zh':'必须的正文','source_units':[{'id':'G:p0003:c000','text_en':'stale' if stale else 'Required body'}]}]})
        return doc

    def test_context_classification_and_reference_model_are_distinct(self):
        self.assertEqual(module.classify('text',['Preface','The Open Group'])['classification'],'front-matter')
        self.assertEqual(module.classify('text',['1. Introduction'])['classification'],'body')
        self.assertEqual(module.classify('text',['2. Reference Model'])['classification'],'body')
        self.assertEqual(module.classify('text',['1.2 Recommended Reading'])['classification'],'reference')
        self.assertEqual(module.classify('text',['Contents'])['classification'],'navigation')
        self.assertEqual(module.classify('text',['1. Body'],role='running-matter')['classification'],'navigation')
        self.assertEqual(module.classify('unassigned')['classification_basis']['confidence'],'uncertain')

    def test_raw_blocks_not_mapped_to_content_are_inventoried(self):
        builder = module.Inventory(self.root); builder.guide(self.guide_fixture())
        self.assertEqual(len(builder.units),9)
        identities = {u['id'] for u in builder.units}
        self.assertIn('G:p0003:b3',identities)
        self.assertEqual(builder.documents[0]['raw_source_blocks'],9)
        self.assertEqual(builder.documents[0]['raw_blocks_represented'],4)
        self.assertTrue(builder.documents[0]['raw_block_closure_complete'])
        body = next(u for u in builder.units if u['id']=='G:p0003:c000')
        self.assertTrue(body['translation_candidates'])
        self.assertEqual(body['translation_candidates'][0]['alignment'],'section')
        self.assertFalse(body['independent_model_review'])
        self.assertEqual(body['review_status'],'not-executed')
        missing = next(u for u in builder.units if u['id']=='G:p0003:b3')
        self.assertEqual(missing['translation_status'],'body-translation-missing')
        navigation = next(u for u in builder.units if u['id']=='G:p0002:c000')
        self.assertEqual(navigation['classification'],'navigation')
        self.assertEqual(navigation['source_fragments'][0]['text'],'Scope ........ 3')

    def test_stale_candidate_text_and_source_bytes_fail_closed(self):
        builder=module.Inventory(self.root)
        with self.assertRaisesRegex(ValueError,'no longer matches'):
            builder.guide(self.guide_fixture(stale=True))
        path=self.c/'sources/fixture.pdf'
        with self.assertRaisesRegex(ValueError,'fingerprint conflict'):
            builder.reference(path,'0'*64)

    def test_foundation_all_blocks_navigation_and_footnotes_are_distinct(self):
        folder=self.c/'fundamental/web-2025/volumes/V';folder.mkdir(parents=True)
        (folder/'source.html').write_bytes(b'original html')
        mhtml=self.c/'fundamental/web-2025/V.mhtml';mhtml.write_bytes(b'original mhtml')
        blocks=[{'id':'V:b1','kind':'p','text_en':'copyright','section_path':[]},
                {'id':'V:b2','kind':'h2','text_en':'1. Body','section_path':[{'title_en':'1. Body'}]},
                {'id':'V:b3','kind':'p','text_en':'Required body','section_path':[{'title_en':'1. Body'}]}]
        doc={'id':'V','source':{'html_path':str((folder/'source.html').relative_to(self.c)),'html_sha256':module.sha(folder/'source.html'),
                              'mhtml_path':str(mhtml.relative_to(self.c)),'mhtml_sha256':module.sha(mhtml)},
             'blocks':blocks,'toc':[{'text_en':'Body','href':'#body'}],'footnotes':[{'id':'fn1','text_en':'Substantive qualification'}]}
        path=self.write('fundamental/web-2025/volumes/V/document.json',doc)
        self.write('fundamental/chinese-text/V.json',{'source_document_sha256':module.sha(path),'blocks':[{'source_block_id':'V:b3','text_en':'Required body','text_zh':'正文'}],
                                                    'footnotes':[{'id':'fn1','text_en':'Substantive qualification','text_zh':'实质限制'}]})
        builder=module.Inventory(self.root);builder.foundation(path)
        self.assertEqual(len(builder.units),5)
        footnote=next(u for u in builder.units if u['kind']=='footnote')
        self.assertTrue(footnote['translation_candidates'])
        self.assertEqual(footnote['classification_basis']['confidence'],'uncertain')
        self.assertEqual(builder.documents[0]['web_blocks'],3)

    def test_shards_preserve_every_unit_once_with_unique_translation_context(self):
        builder=module.Inventory(self.root);builder.guide(self.guide_fixture())
        inventory={'units':builder.units}
        shards=module.prepare_shards(inventory,builder.contexts,max_units=2,max_characters=1000)
        actual=[u['id'] for s in shards for u in s['units']]
        self.assertEqual(actual,[u['id'] for u in inventory['units']])
        self.assertEqual(len(actual),len(set(actual)))
        self.assertTrue(all(len(s['units'])<=2 for s in shards))
        self.assertTrue(all(s['review_status']=='not-executed' for s in shards))
        self.assertTrue(all('without overrides' in s['model_settings'] for s in shards))

    def test_path_escape_symlink_and_duplicate_unit_are_rejected(self):
        builder=module.Inventory(self.root)
        with self.assertRaisesRegex(ValueError,'escapes repository'):
            builder.reference(self.root.parent/'outside')
        target=self.c/'target';target.write_text('source')
        link=self.c/'link';link.symlink_to(target)
        with self.assertRaisesRegex(ValueError,'symlink forbidden'):
            builder.reference(link)
        builder.add({'id':'unit','text_en':'source'})
        with self.assertRaisesRegex(ValueError,'Duplicate source unit'):
            builder.add({'id':'unit','text_en':'source'})


if __name__=='__main__':
    unittest.main()
