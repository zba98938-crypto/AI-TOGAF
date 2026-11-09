"""Source/coverage adversaries: missing inputs and test counts never certify UML/BPMN."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import Invalid
from standards_coverage import ledger, completeness, contained_file, verified_sources, attach_execution, KINDS


class StandardsCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.uml = ledger('uml', '2.5.1'); cls.bpmn = ledger('bpmn', '2.0.2')

    def test_stable_unique_source_items_and_all_six_dimensions(self):
        for language, version, report in [('uml','2.5.1',self.uml),('bpmn','2.0.2',self.bpmn)]:
            identities = [row['id'] for row in report['items']]
            self.assertEqual(len(identities), len(set(identities)))
            self.assertEqual(identities, [row['id'] for row in ledger(language,version)['items']])
            self.assertEqual(set(KINDS), {row['kind'] for row in report['items']})
            self.assertTrue(all(row['source']['locator'] and len(row['source']['sha256'])==64 for row in report['items']))

    def test_pdf_candidates_require_applicability_adjudication(self):
        for report in (self.uml,self.bpmn):
            candidates = [row for row in report['items'] if row['declaration_kind']=='prose-candidate']
            self.assertTrue(candidates)
            self.assertTrue(all(row['applicability']=='unadjudicated' for row in candidates))
            self.assertFalse(report['completeness']['applicability_adjudication_complete'])
            self.assertEqual('incomplete',report['completeness']['status'])

    def test_original_uml_duplicate_ids_remain_locatable_and_block_source_completion(self):
        duplicates = [row for row in self.uml['items']
                      if row['source'].get('ambiguous_native_id')=='State-isConsistentWith']
        self.assertEqual(2,len(duplicates))
        self.assertEqual(2,len({row['source']['locator'] for row in duplicates}))
        self.assertTrue(self.uml['source_defects'])
        self.assertFalse(self.uml['completeness']['source_scope_complete'])

    def test_all_425_declared_uml_invariants_are_source_covered(self):
        from uml_backend import official_rules
        identities = {row['source']['locator'].split(';')[0] for row in self.uml['items']
                      if row['kind']=='constraint' and row['source']['file'].endswith('/UML.xmi')}
        self.assertTrue({'xmi:id='+row['id'] for row in official_rules()[0]} <= identities)

    def test_standard_profile_extension_declarations_are_source_covered(self):
        from standards import SOURCES, safe_xml, XMI
        source=safe_xml((SOURCES/'uml-2.5.1/StandardProfile.xmi').read_bytes())
        extensions={e.get('{'+XMI+'}id') for e in source.iter()
                    if e.get('{'+XMI+'}type','').split(':')[-1]=='Extension'}
        self.assertEqual(34,len(extensions))
        covered={row['source']['locator'].removeprefix('xmi:id=') for row in self.uml['items']
                 if row['kind']=='construct' and row['source']['file'].endswith('/StandardProfile.xmi')}
        self.assertTrue(extensions <= covered)

    def test_unrelated_or_unexecuted_tests_cannot_complete_an_obligation(self):
        item = {'applicability':'design-time-declaration','implementation_status':'implemented',
                'verification_status':'not-executed','positive_tests':[{'name':'positive'}],
                'negative_tests':[{'name':'negative'}]}
        self.assertEqual('incomplete',completeness([item],True,True)['status'])
        item['verification_status']='passed'; self.assertEqual('complete',completeness([item],True,True)['status'])
        self.assertEqual('incomplete',completeness([item],False,True)['status'])
        self.assertEqual('incomplete',completeness([item],True,False)['status'])
        item['negative_tests']=[]; self.assertEqual('incomplete',completeness([item],True,True)['status'])

    def test_wrong_hash_missing_file_and_escape_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); (root/'uml-2.5.1').mkdir()
            model = root/'uml-2.5.1/UML.xmi'; model.write_text('<x/>')
            row = {'language':'uml-2.5.1','file':'uml-2.5.1/UML.xmi','sha256':'0'*64}
            (root/'manifest.json').write_text(json.dumps([row]))
            with self.assertRaisesRegex(Invalid,'fingerprint conflict'): verified_sources('uml','2.5.1',root)
            row['file']='uml-2.5.1/missing.xmi'; (root/'manifest.json').write_text(json.dumps([row]))
            with self.assertRaisesRegex(Invalid,'file missing'): verified_sources('uml','2.5.1',root)
            for path in ('../outside','/etc/passwd','https://example.com/model.xmi','folder\\file'):
                with self.subTest(path=path),self.assertRaises(Invalid): contained_file(root,path)

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary); inside=root/'inside';inside.mkdir();outside=root/'outside';outside.write_text('foreign')
            (inside/'source.xmi').symlink_to(outside)
            with self.assertRaisesRegex(Invalid,'symlink escape'):contained_file(inside,'source.xmi')

    def test_bindings_cannot_point_to_fictitious_implementation_symbols(self):
        binding={'obligation_id':self.uml['items'][0]['id'],
                 'implementation':[{'file':'tests/test_standards_coverage.py','symbol':'invented_function'}]}
        with self.assertRaisesRegex(Invalid,'symbol missing'):ledger('uml','2.5.1',bindings=[binding])

    def test_duplicate_execution_evidence_is_rejected(self):
        evidence={'schema_version':'native-standard-test-evidence/1',
                  'tests':[{'file':'test.py','symbol':'oracle','status':'passed'}]*2}
        with self.assertRaisesRegex(Invalid,'duplicate standard test evidence'):attach_execution([],evidence)

    def test_changed_normative_source_cannot_reuse_old_test_results(self):
        item={'source':{'file':'UML.xmi','sha256':'a'*64},
              'implementation':[{'file':'backend.py','sha256':'b'*64}],
              'positive_tests':[{'file':'test.py','symbol':'positive','sha256':'c'*64}],
              'negative_tests':[{'file':'test.py','symbol':'negative','sha256':'c'*64}]}
        evidence={'schema_version':'native-standard-test-evidence/1',
                  'source_hashes':{'backend.py':'b'*64,'test.py':'c'*64},
                  'normative_source_hashes':{'UML.xmi':'0'*64},
                  'tests':[{'file':'test.py','symbol':name,'status':'passed'} for name in ('positive','negative')]}
        attach_execution([item],evidence)
        self.assertEqual('stale-normative-source',item['verification_status'])
        evidence['normative_source_hashes']['UML.xmi']='a'*64
        attach_execution([item],evidence)
        self.assertEqual('passed-bounded-fixtures',item['verification_status'])
        evidence['source_hashes']['backend.py']='0'*64
        attach_execution([item],evidence)
        self.assertEqual('stale-source',item['verification_status'])


if __name__ == '__main__':unittest.main()
