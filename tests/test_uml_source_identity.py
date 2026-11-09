"""Independent source-identity preservation and unresolved-reference oracles."""
import hashlib
import json
from pathlib import Path
import sys
import unittest
from lxml import etree

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import safe_xml
from standards_coverage import ledger,source_identities,source_identity_provenance

SOURCE_SHA='e8166c91f51b8a0c015a90101b83d2249d03252e9f9a500a6511654347804f21'
UNCHANGED_IDS_SHA='1ebf53efcebfee41e3c905d21e44da2e8d0a33bc1d88f8f4aabd6cf45244aa24'


class UmlSourceIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=ledger('uml','2.5.1',bindings=[])
        cls.source=next(r for r in cls.report['source_identity_provenance'] if r['file']=='uml-2.5.1/UML.xmi')

    def fixture(self,text):
        return safe_xml(('<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmlns:u="http://www.omg.org/spec/UML/20131001">'+text+'</xmi:XMI>').encode())

    def test_all_5779_existing_obligation_ids_are_preserved(self):
        identities='\n'.join(row['id'] for row in self.report['items'])
        self.assertEqual(5779,len(self.report['items']))
        self.assertEqual(UNCHANGED_IDS_SHA,hashlib.sha256(identities.encode()).hexdigest())

    def test_all_eight_xml_duplicate_groups_and_sixteen_fragments_are_retained(self):
        summary=self.report['source_identity_summary']
        self.assertEqual((8,16,10),(summary['duplicate_xml_native_id_count'],summary['duplicate_xml_occurrence_count'],summary['ambiguous_reference_count']))
        self.assertEqual(5,len(self.report['source_defects']))
        keys=[]
        for group in self.source['duplicate_groups']:
            self.assertEqual(2,group['occurrence_count'])
            for node in group['occurrences']:
                text=node['canonical_xml_fragment'].encode()
                self.assertEqual(node['canonical_fragment_sha256'],hashlib.sha256(text).hexdigest())
                self.assertEqual(SOURCE_SHA,node['identity']['sha256'])
                self.assertIn('StateMachines',node['identity']['xml_path'])
                keys.append(node['identity']['key'])
        self.assertEqual(16,len(set(keys)))

    def test_rule_owner_full_identity_distinguishes_same_native_operation_id(self):
        rules=[row for row in self.report['items'] if row['source'].get('ambiguous_native_id')=='State-isConsistentWith-spec']
        self.assertEqual(2,len(rules))
        self.assertEqual({'State-isConsistentWith'},{row['owner_id'] for row in rules})
        self.assertEqual(2,len({row['owner_identity']['key'] for row in rules}))
        self.assertEqual(2,len({row['owner_identity']['xml_path'] for row in rules}))
        for row in rules:
            self.assertEqual('uml-2.5.1/UML.xmi',row['owner_identity']['file'])
            self.assertEqual(SOURCE_SHA,row['owner_identity']['sha256'])
            self.assertEqual(1,row['owner_identity']['occurrence'])
            self.assertTrue(row['source_identity']['xml_path'].startswith(row['owner_identity']['xml_path']+'/'))

    def test_bare_references_have_candidates_without_an_implicit_resolution(self):
        refs=self.source['ambiguous_references']
        self.assertEqual(10,len(refs))
        for row in refs:
            self.assertEqual('ambiguous-source-reference',row['status'])
            self.assertIsNone(row['resolved_target'])
            self.assertEqual(2,len(row['candidates']))
            self.assertEqual(1,len(row['context_candidates']))
            self.assertIn('separate normative type/ownership evidence',row['context_basis'])
            self.assertFalse(row['execution_adapter_applied'])
            self.assertFalse(row['semantic_correction_applied'])

    def test_same_owner_same_name_repeat_uses_occurrence(self):
        root=self.fixture('<packagedElement xmi:type="u:Class" xmi:id="C" name="C"><ownedOperation xmi:id="D" name="query"/><ownedOperation xmi:id="D" name="query"/></packagedElement>')
        index=source_identities({'file':'fixture.xmi','sha256':'a'*64},root)
        nodes=root.findall('packagedElement/ownedOperation');first,second=[index[node] for node in nodes]
        self.assertEqual(first['xml_path'],second['xml_path'])
        self.assertEqual((1,2),(first['occurrence'],second['occurrence']))
        self.assertNotEqual(first['key'],second['key'])

    def test_contextless_and_local_fragment_references_stay_ambiguous(self):
        root=self.fixture('<packagedElement xmi:type="u:Class" xmi:id="A" name="A"><ownedOperation xmi:id="D" name="query"/></packagedElement><packagedElement xmi:type="u:Class" xmi:id="B" name="B"><ownedOperation xmi:id="D" name="query"/></packagedElement><redefinedOperation xmi:idref="D"/><redefinedOperation href="#D"/>')
        result=source_identity_provenance({'file':'fixture.xmi','sha256':'a'*64},root)
        self.assertEqual(2,len(result['ambiguous_references']))
        for row in result['ambiguous_references']:
            self.assertEqual([],row['context_candidates'])
            self.assertIsNone(row['resolved_target'])
            self.assertEqual(2,len(row['candidates']))
        self.assertFalse(result['file_fingerprint_verified'])

    def test_namespace_prefix_and_file_hash_do_not_silently_migrate_identity_keys(self):
        raw=b'<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001"><ownedRule xmi:id="D" name="rule"/></xmi:XMI>'
        original=safe_xml(raw);renamed=safe_xml(raw.replace(b'xmlns:xmi=',b'xmlns:ids=').replace(b'xmi:',b'ids:'))
        first=source_identities({'file':'fixture.xmi','sha256':'a'*64},original)
        second=source_identities({'file':'fixture.xmi','sha256':'b'*64},renamed)
        a=first[original[0]];b=second[renamed[0]]
        self.assertEqual(a['key'],b['key']);self.assertEqual(a['xml_path'],b['xml_path'])
        self.assertNotEqual(a['sha256'],b['sha256'])
        # The separate changed fingerprint must still invalidate executed evidence.

    def test_state_vertex_semantics_and_equal_preconditions_are_not_merged(self):
        groups={r['native_id']:r for r in self.source['duplicate_groups']}
        specs=groups['State-isConsistentWith-spec']['occurrences'];pres=groups['State-isConsistentWith-pre']['occurrences']
        body=lambda row:etree.fromstring(row['canonical_xml_fragment'].encode()).findtext('specification/body')
        self.assertNotEqual(body(specs[0]),body(specs[1]))
        self.assertEqual(body(pres[0]),body(pres[1]))
        self.assertNotEqual(pres[0]['identity']['key'],pres[1]['identity']['key'])
        vertex=next(row for row in specs if 'packagedElement[name=Vertex]' in row['identity']['xml_path'])
        self.assertIn('redefinedElement.oclIsKindOf(Vertex)',body(vertex))
        self.assertNotIn('redefiningElement.oclIsKindOf(Vertex)',body(vertex))

    def test_available_verified_files_do_not_close_global_identity_or_semantic_scope(self):
        self.assertEqual('verified-local-files',self.report['source_availability']['status'])
        self.assertEqual(11,self.report['source_availability']['file_count'])
        self.assertTrue(all(r['file_available'] and r['file_fingerprint_verified'] and r['xml_well_formed'] for r in self.report['source_identity_provenance']))
        self.assertFalse(self.report['source_availability']['file_accessibility_establishes_semantic_acceptance'])
        self.assertFalse(self.source['global_native_id_unique'])
        self.assertFalse(self.report['source_identity_summary']['global_identity_repair_applied'])
        self.assertFalse(self.report['source_identity_summary']['semantic_correction_applied'])
        self.assertFalse(self.report['completeness']['source_scope_complete'])
        self.assertEqual(0,self.report['completeness']['verified_obligations'])
        self.assertEqual('incomplete',self.report['completeness']['status'])


if __name__=='__main__':unittest.main()
