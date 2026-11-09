"""Bounded-reader completeness; not diagram or standards conformance tests."""
import copy,json,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from large_view_reader import render
class ReaderTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
  self.model={'entities':[{'id':f'n{i}','type':'application','name':f'Node {i}','attributes':{'full':i}} for i in range(25)],'relationships':[{'id':f'e{i}','type':'supports','source':f'n{i}','target':f'n{i+1}','label':f'Edge {i}','attributes':{'guard':str(i)}} for i in range(24)],'views':[{'id':'v','title':'Reader','entity_ids':[f'n{i}' for i in range(25)],'relationship_ids':[f'e{i}' for i in range(24)]}]}
 def tearDown(self):self.tmp.cleanup()
 def run_reader(self):
  self.input=self.root/'model.json';self.input.write_text(json.dumps(self.model));self.out=self.root/'reader';return render(self.input,self.out,'v')
 def test_all_entities_edges_guards_and_original_bytes_retained(self):
  m=self.run_reader();self.assertEqual(json.loads((self.out/'entities.json').read_text()),self.model['entities']);self.assertEqual(json.loads((self.out/'relationships.json').read_text()),self.model['relationships']);self.assertEqual((self.out/'original-model.json').read_bytes(),self.input.read_bytes());self.assertEqual(m['cross_page_relationship_ids'],['e11','e23'])
 def test_pages_are_bounded_and_each_entity_appears_once(self):
  m=self.run_reader();self.assertEqual(len(m['entity_pages']),3);self.assertEqual([i for p in m['entity_pages'] for i in p['entity_ids']],self.model['views'][0]['entity_ids']);self.assertTrue(all(len(p['entity_ids'])<=12 and p['pixels']==2073600 for p in m['entity_pages']));self.assertFalse(m['monolithic_renderer_capacity_claimed']);self.assertFalse(m['strict_language_conformance'])
 def test_long_names_not_silently_truncated_or_injected(self):
  self.model['entities'][0]['name']='<script>alert(1)</script>'*80;m=self.run_reader();self.assertIn('n0',m['excerpts_explicitly_disclosed']);self.assertEqual(json.loads((self.out/'entities.json').read_text())[0]['name'],self.model['entities'][0]['name']);self.assertNotIn('<script>',(self.out/'reader.html').read_text())
 def test_existing_output_not_overwritten(self):
  self.run_reader()
  with self.assertRaisesRegex(ValueError,'new'):render(self.input,self.out,'v')
 def test_duplicate_view_membership_and_missing_refs_rejected(self):
  self.model['views'][0]['entity_ids'].append('n0')
  with self.assertRaisesRegex(ValueError,'duplicate'):self.run_reader()
 def test_external_view_endpoints_explicit(self):
  self.model['views'][0]['entity_ids'].remove('n24');self.run_reader();r=json.loads((self.out/'relationship-pages.json').read_text())[-1];self.assertIsNone(r['target_page']);self.assertTrue(r['cross_page'])
