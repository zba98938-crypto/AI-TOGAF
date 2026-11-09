#!/usr/bin/env python3
"""Independent source checks for role profiles; does not import the builder.

Mutation checks make omissions, wrong role columns, fabricated scores and broken
quotations fail even if generated summary counts still claim completeness.
"""
from collections import Counter
from copy import deepcopy
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import unittest
import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'togaf-standard-10th-ai'
ROLES=OUT/'architecture/roles'
COLUMNS={
 'G249':['enterprise-architect','business-domain-architect','data-domain-architect','application-domain-architect','technology-domain-architect','solution-architect'],
 'G198':['architecture-board-member','architecture-sponsor','enterprise-architecture-manager','technology-architect','data-architect','application-architect','business-architect','program-project-manager','it-designer','solution-architect']}
COUNTS={'G249':71,'G198':79}
CORE_PROFILE_IDS={
 'G249:role:'+key for key in ['chief-architect','enterprise-architect','segment-architect',*COLUMNS['G249'][1:]]
}|{'G198:role:'+key for key in [*COLUMNS['G198'],'enterprise-architect','segment-architect']}|{
 'G186:role:'+key for key in ['stakeholder','stakeholder-agent','subject-matter-expert','implementer','architect-governance','auditor','decision-maker']
}|{
 'G184:role:ea-governance-board','G188:role:executive','G20F:role:product-owner',
 'G152:role:security-architect','G21B:role:customer-data-owner','G234:role:data-steward'
}
PALETTE={(255,243,131):1,(176,203,31):2,(118,144,201):3,(234,85,111):4}

def read(path):return json.loads(path.read_text())
def norm(s):return re.sub(r'\s+',' ',str(s)).strip()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def walk(value):
 if isinstance(value,dict):
  yield value
  for v in value.values():yield from walk(v)
 elif isinstance(value,list):
  for v in value:yield from walk(v)

def check_profile(profile, expected):
 code=profile['source_guide'];key=profile['id'].split(':role:')[1]
 if key not in COLUMNS.get(code,[]):
  assert profile['skills']==[],profile['id']+' invented numeric skills'
  assert profile['matrix_status']=='not-specified-for-this-role'
  assert not profile.get('proficiency_scale')
  return
 assert profile['matrix_status']=='complete-source-column'
 actual={s['skill_id']:s for s in profile['skills']}
 assert len(actual)==len(profile['skills'])==COUNTS[code],profile['id']+' missing/duplicate skills'
 assert set(actual)==set(expected[code])
 col=COLUMNS[code].index(key)
 for sid,source in expected[code].items():
  s=actual[sid]
  assert s['reference_level']==source[col],(profile['id'],sid,'wrong source level')
  assert s['evidence']['role_column_index_zero_based']==col+(2 if code=='G249' else 1)
  assert s['requirement_kind']=='reference-desirable-proficiency-not-universal-mandate'

class RoleSourceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.index=read(ROLES/'index.json');cls.skills=read(ROLES/'skills.json')
  cls.profiles={x['id']:read(ROLES/x['json']) for x in cls.index['profiles']}
  cls.expected={'G249':{},'G198':{}};cls.pdfs={};cls.hashes={};cls.source_cells=Counter()
  cls.image_records={};cls.rendered_source_images={}
  for code,data in cls.skills.items():
   if code not in COLUMNS:continue
   for skill in data['skills']:
    e=skill['evidence'];path=ROOT/e['source_path']
    if str(path) not in cls.pdfs:cls.pdfs[str(path)]=fitz.open(path);cls.hashes[str(path)]=sha(path)
    assert e['source_sha256']==cls.hashes[str(path)]
    page=cls.pdfs[str(path)][e['pdf_page']-1]
    if code=='G249':
     b=e['cell_bboxes'];label=norm(page.get_text('text',clip=fitz.Rect(b[1])))
     assert label==skill['label_en'],(label,skill['label_en'])
     values=[int(norm(page.get_text('text',clip=fitz.Rect(box)))) for box in b[2:]]
    else:
     rid=e['image_record_id']
     if rid not in cls.image_records:
      rec=read(OUT/'figures'/(rid+'.json'));cls.image_records[rid]=rec
      png=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(rec['bbox_pdf_points']),alpha=False).tobytes('png')
      assert hashlib.sha256(png).hexdigest()==sha(OUT/rec['image_path'])
      cls.rendered_source_images[rid]=Image.open(BytesIO(png)).convert('RGB')
     rec=cls.image_records[rid];im=cls.rendered_source_images[rid];w,h=im.size
     table=next(t for t in rec['tables'] if t['id']==e['table_id'])
     row=e['row_index_zero_based'];assert table['rows'][row][0]==skill['label_en']
     colored=[y for y in range(h) if im.getpixel((int(w*.195),y)) in PALETTE]
     y0,y1=min(colored),max(colored)+1;cy=y0+(y1-y0)*(row+.5)/len(table['rows'])
     values=[]
     for col in range(10):
      cx=w*(.181+(col+.5)*.819/10)
      votes=Counter(PALETTE[p] for p in im.crop((int(cx-10),int(cy-4),int(cx+10),int(cy+4))).getdata() if p in PALETTE)
      assert votes and votes.most_common(1)[0][1]>20,(rid,row,col)
      values.append(votes.most_common(1)[0][0])
    assert values==skill['values'],(code,skill['id'],'matrix source mismatch')
    assert skill['id'] not in cls.expected[code]
    cls.expected[code][skill['id']]=values;cls.source_cells[code]+=len(values)
 @classmethod
 def tearDownClass(cls):
  for pdf in cls.pdfs.values():pdf.close()
 def quote_check(self,e):
  path=ROOT/e['source_path'];key=str(path)
  if key not in self.pdfs:self.pdfs[key]=fitz.open(path);self.hashes[key]=sha(path)
  self.assertEqual(e['source_sha256'],self.hashes[key])
  self.assertIn(norm(e['quote_en']),norm(self.pdfs[key][e['pdf_page']-1].get_text()))
 def test_01_all_core_and_supplemental_profiles_and_1216_values_against_source(self):
  specs=read(ROOT/'tools/togaf_corpus/role-additional-profiles.json')['profiles']
  supplemental={p['code']+':role:'+p['key'] for p in specs}
  self.assertEqual(len(supplemental),len(specs),'Duplicate supplemental role specification')
  self.assertFalse(CORE_PROFILE_IDS & supplemental)
  self.assertEqual(set(self.profiles),CORE_PROFILE_IDS | supplemental)
  self.assertEqual(self.index['counts']['roles'],len(self.profiles))
  self.assertEqual(self.source_cells,{'G249':426,'G198':790})
  self.assertEqual(sum(bool(p['skills']) for p in self.profiles.values()),16)
  for profile in self.profiles.values():
   with self.subTest(role=profile['id']):check_profile(profile,self.expected)
 def test_02_page_bottom_rows_and_original_role_columns(self):
  rows=self.skills['G249']['skills']
  for label,page in [('Integration and Sharing',27),('Oral Communication',28)]:
   matches=[s for s in rows if s['label_en']==label]
   self.assertEqual(len(matches),1);self.assertEqual(matches[0]['evidence']['pdf_page'],page)
  for code,columns in COLUMNS.items():
   self.assertEqual([x['id'] for x in self.skills[code]['role_columns']],[code+':role:'+c for c in columns])
 def test_03_all_quotes_and_fingerprints_directly_against_source_pdfs(self):
  evidence=[e for e in walk(list(self.profiles.values())) if all(k in e for k in ['quote_en','source_path','pdf_page'])]
  self.assertGreater(len(evidence),300)
  for e in evidence:
   with self.subTest(source=e['source_path'],page=e['pdf_page']):self.quote_check(e)
 def test_04_source_specific_scale_and_reference_requirements(self):
  for p in self.profiles.values():
   if not p['skills']:continue
   c=p['competency_analysis'];self.assertNotIn('expertise_required',c)
   self.assertEqual(c['expert_level_reference'],[s['label_en'] for s in p['skills'] if s['reference_level']==4])
   if p['source_guide']=='G198':
    self.assertNotIn('specialist_support_expected',c)
    self.assertEqual(c['optional_background'],[s['label_en'] for s in p['skills'] if s['reference_level']==1])
    requirements={x['skill_id']:x for x in p['requirements'] if x.get('assertion_type')=='source-matrix-reference-expectation'}
    wanted={s['skill_id']:s for s in p['skills'] if s['reference_level']>=3}
    self.assertEqual(set(requirements),set(wanted))
    for sid,x in requirements.items():self.assertEqual(x['evidence'],wanted[sid]['evidence'])
   else:self.assertEqual(c['specialist_support_expected'],[s['label_en'] for s in p['skills'] if s['reference_level']<=2])
  comp=read(ROLES/'comparison.json');self.assertEqual(comp['scale_comparability'],'different-ordinal-definitions-no-numeric-delta')
  self.assertFalse(any('difference' in x for x in walk(comp)))
 def test_05_no_unsupported_hr_or_role_architecture_equivalence(self):
  rels=read(ROLES/'relationships.json')['relationships']
  for rel in rels:
   self.assertFalse(rel['is_hr_reporting_line']);self.assertNotEqual(rel['predicate'],'reports_to')
   self.assertIn(rel['from'],self.profiles);self.assertIn(rel['to'],self.profiles)
   if rel['predicate']=='informed_by_higher_scope_architecture':
    self.assertEqual(rel['assertion_type'],'authored-semantic-mapping')
    self.assertIn('intermediary_architecture_scope',rel)
  self.assertIn('enforcement',json.dumps(self.profiles['G186:role:stakeholder'],ensure_ascii=False))
  self.assertIn('execution rights',json.dumps(self.profiles['G186:role:decision-maker'],ensure_ascii=False))
  caveat=self.profiles['G186:role:auditor']['source_caveats'][0]
  self.assertIn('vested with the implementer.',caveat['evidence']['quote_en'])
 def test_06_mutation_missing_source_skill_is_detected(self):
  p=deepcopy(self.profiles['G249:role:enterprise-architect']);p['skills']=[s for s in p['skills'] if s['label_en']!='Oral Communication']
  with self.assertRaises(AssertionError):check_profile(p,self.expected)
 def test_07_mutation_wrong_role_column_value_is_detected(self):
  p=deepcopy(self.profiles['G249:role:enterprise-architect']);p['skills'][0]['reference_level']=2
  with self.assertRaises(AssertionError):check_profile(p,self.expected)
 def test_08_mutation_fabricated_chief_scores_are_detected(self):
  p=deepcopy(self.profiles['G249:role:chief-architect']);p['skills']=deepcopy(self.profiles['G249:role:enterprise-architect']['skills'])
  with self.assertRaises(AssertionError):check_profile(p,self.expected)
 def test_09_mutation_corrupted_source_quote_is_detected(self):
  e=deepcopy(self.profiles['G249:role:chief-architect']['role_definition'][0]['evidence']);e['quote_en']+=' fabricated source claim'
  with self.assertRaises(AssertionError):self.quote_check(e)
 def test_10_generated_markdown_and_index_resolve(self):
  for entry in self.index['profiles']:
   self.assertTrue((ROLES/entry['json']).is_file());self.assertTrue((ROLES/entry['markdown']).is_file())
   self.assertEqual(entry['skill_count'],len(self.profiles[entry['id']]['skills']))
  for field in ['skills','relationships','comparison','mentions','validation']:self.assertTrue((ROLES/self.index[field]).is_file())

if __name__=='__main__':unittest.main(verbosity=2)
