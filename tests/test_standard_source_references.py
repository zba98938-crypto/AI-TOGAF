"""Independent exact-document/fragment/QName source-reference adversaries."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
from xml.sax.saxutils import quoteattr

from lxml import etree

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO/'togaf-standard-10th-ai/skills/_shared/scripts'
sys.path.insert(0, str(SCRIPTS))
from standards import Invalid
from standards_coverage import ledger, machine_reference_provenance

XMI = 'http://schema.omg.org/spec/XMI/2.1'
CMOF = 'http://schema.omg.org/spec/MOF/2.0/cmof.xml'
SOURCE_URI = 'https://example.invalid/20100501/Source.cmof'
PEER_URI = 'https://example.invalid/20100501/Peer.cmof'


def document(body, meta_uri=CMOF, meta_prefix='meta', xmi_uri=XMI, xmi_prefix='ids', package_uri='urn:fixture:abstract-model', default_uri=None):
    default = ' xmlns='+quoteattr(default_uri) if default_uri else ''
    return ('<'+xmi_prefix+':XMI xmlns:'+xmi_prefix+'='+quoteattr(xmi_uri)+
            ' xmlns:'+meta_prefix+'='+quoteattr(meta_uri)+default+'><'+meta_prefix+':Package '+
            xmi_prefix+':id="_0" name="Fixture" uri='+quoteattr(package_uri)+'>'+body+
            '</'+meta_prefix+':Package></'+xmi_prefix+':XMI>').encode()


class SourceReferenceAdversaries(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.temporary_root = Path(self.temporary.name)
        self.base = self.temporary_root/'sources'; self.base.mkdir()
        self.rows = []

    def put(self, file, raw, uri):
        path = self.base/file; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
        row = {'file': file, 'sha256': hashlib.sha256(raw).hexdigest(), 'url': uri}
        self.rows.append(row); return row

    def pair(self, href='Peer.cmof#Target', expected='meta:Class', peer_body=None,
             source_file='std/Source.cmof', peer_file='std/Peer.cmof',
             source_uri=SOURCE_URI, peer_uri=PEER_URI, source_options=None, peer_options=None):
        type_attr = ' ids:type='+quoteattr(expected) if expected is not None else ''
        source = '<ownedMember ids:type="meta:Class" ids:id="Source"><type'+type_attr+' href='+quoteattr(href)+'/></ownedMember>'
        self.put(source_file, document(source, **(source_options or {})), source_uri)
        if peer_body is None: peer_body='<ownedMember ids:type="meta:Class" ids:id="Target" name="Target"/>'
        self.put(peer_file, document(peer_body, **(peer_options or {})), peer_uri)
        return self.inspect()

    def inspect(self):
        return machine_reference_provenance(self.base, self.rows)

    def reference(self, report):
        self.assertEqual(1, len(report['references']))
        return report['references'][0]

    def with_source_xml_bases(self, element_base=None, ancestor_base=None, root_base=None):
        path=self.base/'std/Source.cmof';raw=path.read_bytes()
        for marker, value in ((b'<type ',element_base),(b'<ownedMember ',ancestor_base),(b'<ids:XMI ',root_base)):
            if value is not None:
                raw=raw.replace(marker,marker+b'xml:base='+quoteattr(value).encode()+b' ',1)
        path.write_bytes(raw);self.rows[0]['sha256']=hashlib.sha256(raw).hexdigest()
        return raw

    def assert_xml_base_unadjudicated(self, report):
        row=self.reference(report)
        self.assertEqual('base-chain-preserved',row['xml_base_context']['status'])
        self.assertEqual('relative-resolution-with-base-unadjudicated',row['xml_base_resolution_status'])
        self.assertEqual('xml-base-unadjudicated',row['logical_registration_status'])
        self.assertEqual('xml-base-unadjudicated',row['local_file_status'])
        self.assertIsNone(row['logical_document_uri']);self.assertIsNone(row['local_file'])
        self.assertIsNone(row['local_target']);self.assertIsNone(row['resolved_target'])
        self.assertFalse(row['qualified_identity_complete'])
        self.assertFalse(report['summary']['source_reference_identity_complete'])
        return row

    def test_element_xml_base_absolute_redirect_cannot_borrow_original_peer(self):
        self.pair();raw=self.with_source_xml_bases(element_base='https://other.invalid/')
        row=self.assert_xml_base_unadjudicated(self.inspect())
        entry=row['xml_base_context']['entries'][0]
        self.assertEqual('https://other.invalid/',entry['original_xml_base'])
        self.assertEqual(hashlib.sha256(raw).hexdigest(),entry['source_identity']['sha256'])
        self.assertTrue(entry['source_identity']['source_line'])
        self.assertIn('/type',entry['source_identity']['xml_path'])

    def test_ancestor_xml_base_parent_escape_is_not_resolved_in_source_directory(self):
        self.pair();self.with_source_xml_bases(ancestor_base='../../../')
        row=self.assert_xml_base_unadjudicated(self.inspect())
        self.assertEqual('../../../',row['xml_base_context']['entries'][0]['original_xml_base'])

    def test_empty_child_base_preserves_nonempty_ancestor_chain_without_acceptance(self):
        self.pair();self.with_source_xml_bases(root_base='https://other.invalid/',ancestor_base='../',element_base='')
        row=self.assert_xml_base_unadjudicated(self.inspect())
        self.assertEqual(['https://other.invalid/','../',''],[e['original_xml_base'] for e in row['xml_base_context']['entries']])
        self.assertEqual(3,len({e['source_identity']['key'] for e in row['xml_base_context']['entries']}))

    def test_same_document_fragment_with_nonempty_xml_base_is_not_source_identity(self):
        self.put('std/Source.cmof',document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'
                 '<type ids:type="meta:Class" href="#Target"/>'),SOURCE_URI)
        self.with_source_xml_bases(element_base='https://other.invalid/Source.cmof')
        row=self.assert_xml_base_unadjudicated(self.inspect());self.assertEqual('Target',row['fragment'])

    def test_absolute_registered_uri_is_not_overridden_by_dangerous_xml_base(self):
        for value in ('file:///etc/','javascript:alert(1)','../../../','https://[invalid'):
            with self.subTest(xml_base=value):
                self.rows=[];self.pair(href=PEER_URI+'#Target');self.with_source_xml_bases(ancestor_base=value)
                row=self.reference(self.inspect())
                self.assertEqual('not-required-for-absolute-reference',row['xml_base_resolution_status'])
                self.assertEqual(value,row['xml_base_context']['entries'][0]['original_xml_base'])
                self.assertEqual(PEER_URI,row['logical_document_uri']);self.assertTrue(row['qualified_identity_complete'])

    def test_nonempty_xml_base_does_not_read_unregistered_local_file(self):
        self.pair();self.with_source_xml_bases(element_base='../unregistered/')
        path=self.base/'unregistered/Peer.cmof';path.parent.mkdir();path.write_bytes(b'private arbitrary bytes')
        original=Path.read_bytes
        def guarded(candidate):
            if candidate==path:raise AssertionError('unregistered content must not be read')
            return original(candidate)
        with mock.patch.object(Path,'read_bytes',guarded):self.assert_xml_base_unadjudicated(self.inspect())

    def test_empty_only_xml_base_is_preserved_without_changing_relative_identity(self):
        self.pair();self.with_source_xml_bases(root_base='',element_base='')
        row=self.reference(self.inspect())
        self.assertEqual(['',''],[e['original_xml_base'] for e in row['xml_base_context']['entries']])
        self.assertEqual('no-nonempty-xml-base',row['xml_base_resolution_status'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_even_apparently_harmless_nonempty_base_requires_separate_adjudication(self):
        for value in ('./',' ','https://example.invalid/20100501/'):
            with self.subTest(xml_base=value):
                self.rows=[];self.pair();self.with_source_xml_bases(element_base=value)
                self.assert_xml_base_unadjudicated(self.inspect())

    def test_foreign_same_local_base_attribute_is_not_xml_base(self):
        self.pair();path=self.base/'std/Source.cmof';raw=path.read_bytes().replace(b'<type ',b'<type xmlns:foreign="urn:foreign" foreign:base="../../../" ',1)
        path.write_bytes(raw);self.rows[0]['sha256']=hashlib.sha256(raw).hexdigest()
        row=self.reference(self.inspect())
        self.assertEqual([],row['xml_base_context']['entries']);self.assertTrue(row['qualified_identity_complete'])

    def test_registered_relative_fragment_preserves_source_and_target_identities(self):
        report = self.pair(); row = self.reference(report)
        self.assertTrue(row['qualified_identity_complete'])
        self.assertEqual('Peer.cmof#Target', row['original_href'])
        self.assertEqual(PEER_URI, row['logical_document_uri'])
        self.assertEqual('std/Peer.cmof', row['resolved_target']['source_identity']['file'])
        self.assertEqual('Target', row['resolved_target']['native_id'])
        self.assertEqual(self.rows[0]['sha256'], row['source_identity']['sha256'])
        self.assertEqual(self.rows[1]['sha256'], row['resolved_target']['source_identity']['sha256'])
        self.assertTrue(row['source_identity']['source_line'])
        self.assertIn('ownedMember', row['source_identity']['xml_path'])
        self.assertTrue(report['summary']['source_reference_identity_complete'])

    def test_different_prefix_same_bound_qname_is_accepted(self):
        report = self.pair(peer_body='<ownedMember ids:type="renamed:Class" ids:id="Target"/>',
                           peer_options={'meta_prefix':'renamed'})
        row = self.reference(report)
        self.assertEqual('meta:Class', row['expected_qname']['lexical_value'])
        self.assertEqual('renamed:Class', row['local_target']['declared_qname']['lexical_value'])
        self.assertEqual('{'+CMOF+'}Class', row['type_comparison']['declared']['expanded_name'])
        self.assertEqual('matched-bound-qname', row['type_comparison']['status'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_default_namespace_binds_unprefixed_qname_value(self):
        row = self.reference(self.pair(expected='Class', source_options={'default_uri':CMOF}))
        self.assertEqual('{'+CMOF+'}Class', row['expected_qname']['expanded_name'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_xmi_prefix_spelling_does_not_change_identity(self):
        source = document('<ownedMember ids:type="meta:Class" ids:id="Source"><type ids:type="meta:Class" href="Peer.cmof#Target"/></ownedMember>')
        source = source.replace(b'xmlns:ids=', b'xmlns:otherIds=').replace(b'ids:', b'otherIds:')
        self.put('std/Source.cmof', source, SOURCE_URI)
        self.put('std/Peer.cmof', document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'), PEER_URI)
        self.assertTrue(self.reference(self.inspect())['qualified_identity_complete'])

    def test_exact_registered_absolute_uri_maps_to_registered_file_without_basename_guess(self):
        row = self.reference(self.pair(href=PEER_URI+'#Target', peer_file='other/Registered.cmof'))
        self.assertEqual('other/Registered.cmof', row['local_file'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_same_document_fragment_uses_registered_source_identity(self):
        self.put('std/Source.cmof', document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'
                 '<type ids:type="meta:Class" href="#Target"/>'), SOURCE_URI)
        row = self.reference(self.inspect())
        self.assertEqual(SOURCE_URI, row['logical_document_uri'])
        self.assertEqual('std/Source.cmof', row['local_file'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_contained_parent_relative_path_is_accepted_with_exact_route(self):
        row = self.reference(self.pair(href='../Peer.cmof#Target', source_file='std/folder/Source.cmof',
              source_uri='https://example.invalid/20100501/folder/Source.cmof'))
        self.assertEqual('std/Peer.cmof', row['local_file'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_qualified_declaration_element_provides_package_qname(self):
        row = self.reference(self.pair(href='Peer.cmof#_0', expected='meta:Package'))
        self.assertEqual('qualified-declaration-element', row['local_target']['declared_qname']['basis'])
        self.assertEqual('{'+CMOF+'}Package', row['local_target']['declared_qname']['expanded_name'])
        self.assertTrue(row['qualified_identity_complete'])

    def test_missing_original_semantic_file_stays_missing(self):
        row = self.reference(self.pair(href='Semantic.cmof#Core-Foundation-BaseElement'))
        self.assertEqual('missing-local-file', row['local_file_status'])
        self.assertEqual('unregistered-logical-uri', row['logical_registration_status'])
        self.assertIsNone(row['resolved_target'])
        self.assertFalse(row['identity_substitution_applied'])

    def test_filename_substitution_cannot_remove_original_foundation_fragment(self):
        for name in ('Extension','Relationship','RootElement','BaseElement'):
            with self.subTest(name=name):
                self.rows = []
                row = self.reference(self.pair(href='Peer.cmof#Core-Foundation-'+name,
                    peer_body='<ownedMember ids:type="meta:Class" ids:id='+quoteattr(name)+' name='+quoteattr(name)+'/>'))
                self.assertEqual('missing-fragment', row['fragment_status'])
                self.assertFalse(row['qualified_identity_complete'])
                self.assertEqual('Core-Foundation-'+name, row['fragment'])

    def test_existing_registered_file_missing_fragment_is_not_closed(self):
        report=self.pair(href='Peer.cmof#Absent'); row=self.reference(report)
        self.assertEqual('registered-local-machine-file', row['local_file_status'])
        self.assertEqual('registered-exact-logical-uri', row['logical_registration_status'])
        self.assertEqual('missing-fragment', row['fragment_status'])
        self.assertFalse(report['summary']['source_reference_identity_complete'])

    def test_duplicate_fragment_keeps_all_candidates_without_type_or_owner_disambiguation(self):
        row = self.reference(self.pair(peer_body='<ownedMember ids:type="meta:Class" ids:id="Target" name="First"/>'
            '<ownedMember ids:type="meta:DataType" ids:id="Target" name="Second"/>'))
        self.assertEqual('ambiguous-fragment', row['fragment_status'])
        self.assertEqual(2, len(row['local_target_candidates']))
        self.assertEqual(2,len({r['source_identity']['key'] for r in row['local_target_candidates']}))
        self.assertIsNone(row['local_target']); self.assertIsNone(row['resolved_target'])

    def test_unreferenced_duplicate_native_id_also_keeps_source_inventory_open(self):
        report=self.pair(peer_body='<ownedMember ids:type="meta:Class" ids:id="Target"/>'
            '<ownedMember ids:type="meta:Class" ids:id="Unused"/><ownedMember ids:type="meta:Class" ids:id="Unused"/>')
        self.assertTrue(self.reference(report)['qualified_identity_complete'])
        self.assertEqual(1,report['summary']['duplicate_native_id_group_count'])
        self.assertFalse(report['summary']['source_reference_identity_complete'])

    def test_same_local_type_name_different_namespace_is_explicitly_unresolved(self):
        row = self.reference(self.pair(peer_options={'meta_uri':'urn:other:metamodel'}))
        self.assertEqual('Class', row['type_comparison']['expected']['local_name'])
        self.assertEqual('Class', row['type_comparison']['declared']['local_name'])
        self.assertEqual('namespace-mismatch', row['namespace_status'])
        self.assertNotEqual(row['type_comparison']['expected']['expanded_name'],row['type_comparison']['declared']['expanded_name'])
        self.assertIsNone(row['resolved_target'])

    def test_different_metaclass_same_namespace_stays_unadjudicated(self):
        row = self.reference(self.pair(expected='meta:Package', peer_body='<ownedMember ids:type="meta:Model" ids:id="Target"/>'))
        self.assertEqual('type-difference-unadjudicated', row['type_comparison']['status'])
        self.assertEqual('matched-namespace-type-unadjudicated', row['namespace_status'])
        self.assertEqual('not-adjudicated',row['type_comparison']['metamodel_type_conformance'])
        self.assertFalse(row['qualified_identity_complete'])

    def test_missing_expected_type_does_not_infer_from_reference_role_or_target(self):
        row = self.reference(self.pair(expected=None))
        self.assertEqual('exact-unique-fragment', row['fragment_status'])
        self.assertEqual('unknown-type', row['type_comparison']['status'])
        self.assertIsNone(row['expected_qname']['expanded_name'])
        self.assertIsNone(row['resolved_target'])

    def test_unbound_type_prefix_is_unknown_without_prefix_string_comparison(self):
        row = self.reference(self.pair(expected='unbound:Class'))
        self.assertEqual('unbound-prefix',row['expected_qname']['binding_status'])
        self.assertEqual('unknown-type',row['type_comparison']['status'])
        self.assertFalse(row['qualified_identity_complete'])

    def test_invalid_type_qname_is_preserved_and_unknown(self):
        row=self.reference(self.pair(expected='meta:Class:Other'))
        self.assertEqual('meta:Class:Other',row['expected_qname']['lexical_value'])
        self.assertEqual('invalid-qname',row['expected_qname']['binding_status'])
        self.assertEqual('unknown-type',row['type_comparison']['status'])

    def test_untyped_unqualified_declaration_stays_unknown(self):
        row=self.reference(self.pair(peer_body='<ownedMember ids:id="Target" name="Class"/>'))
        self.assertEqual('unknown-type',row['local_target']['declared_qname']['binding_status'])
        self.assertEqual('unknown-type',row['type_comparison']['status'])

    def test_foreign_same_local_id_attribute_is_not_a_native_xmi_identity(self):
        row=self.reference(self.pair(peer_body='<ownedMember xmlns:foreign="urn:foreign" ids:type="meta:Class" foreign:id="Target"/>'))
        self.assertEqual('missing-fragment',row['fragment_status'])
        self.assertFalse(row['qualified_identity_complete'])

    def test_unknown_xmi_namespace_does_not_register_its_ids(self):
        report=self.pair(peer_options={'xmi_uri':'urn:unknown:xmi'})
        row=self.reference(report)
        self.assertEqual('missing-fragment',row['fragment_status'])
        peer=next(s for s in report['sources'] if s['file']=='std/Peer.cmof')
        self.assertEqual('unknown-xmi-namespace',peer['xmi_namespace_status'])
        self.assertFalse(report['summary']['machine_source_registration_complete'])

    def test_http_https_spelling_is_not_an_implicit_alias(self):
        row=self.reference(self.pair(href=PEER_URI.replace('https:','http:')+'#Target'))
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
        self.assertIsNone(row['local_file']); self.assertIsNone(row['resolved_target'])

    def test_unregistered_exact_fragment_inventory_matches_cannot_resolve_document(self):
        self.pair(href=PEER_URI.replace('https:','http:')+'#Target')
        self.put('unrelated/NotTheReferencedName.cmof',document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'),
                 'https://different.invalid/20991231/Unrelated.cmof')
        report=self.inspect();row=self.reference(report)
        candidates=row['unregistered_fragment_inventory_matches']
        self.assertEqual(2,len(candidates))
        self.assertEqual({'std/Peer.cmof','unrelated/NotTheReferencedName.cmof'},
                         {c['declaration']['source_identity']['file'] for c in candidates})
        self.assertTrue(all(c['candidate_qname_comparison']['status']=='matched-bound-qname' for c in candidates))
        self.assertTrue(all(not c['reference_identity_resolved'] and not c['reference_type_adjudicated'] for c in candidates))
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
        self.assertEqual('unknown-type',row['type_comparison']['status'])
        self.assertIsNone(row['local_target']);self.assertIsNone(row['resolved_target'])
        self.assertFalse(report['summary']['source_reference_identity_complete'])

    def test_absolute_uri_scheme_case_is_preserved_for_exact_registration(self):
        row=self.reference(self.pair(href=PEER_URI.replace('https:','HTTPS:')+'#Target'))
        self.assertEqual(PEER_URI.replace('https:','HTTPS:'),row['logical_document_uri'])
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])

    def test_different_date_logical_route_cannot_borrow_a_local_fragment(self):
        row=self.reference(self.pair(source_uri=SOURCE_URI.replace('20100501','20100502')))
        self.assertEqual('exact-unique-fragment',row['fragment_status'])
        self.assertEqual(PEER_URI.replace('20100501','20100502'),row['logical_document_uri'])
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
        self.assertIsNone(row['resolved_target'])

    def test_package_uri_is_not_a_registered_document_uri_alias(self):
        package_uri='https://example.invalid/20100524/ABSTRACT-MODEL'
        row=self.reference(self.pair(href=package_uri+'#Target',peer_options={'package_uri':package_uri}))
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
        self.assertIsNone(row['resolved_target'])

    def test_duplicate_registered_document_uri_stays_ambiguous(self):
        self.pair(href=PEER_URI+'#Target')
        self.put('other/Peer.cmof',document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'),PEER_URI)
        report=self.inspect();row=self.reference(report)
        self.assertEqual('ambiguous-logical-uri',row['logical_registration_status'])
        self.assertEqual(2,len(row['logical_registered_files']))
        self.assertIsNone(row['resolved_target'])
        self.assertFalse(report['summary']['machine_source_registration_complete'])

    def test_registered_route_and_local_file_conflict_is_explicit(self):
        self.pair(peer_uri='https://example.invalid/elsewhere/Peer.cmof')
        self.put('other/Registered.cmof',document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'),PEER_URI)
        row=self.reference(self.inspect())
        self.assertEqual('exact-unique-fragment',row['fragment_status'])
        self.assertEqual(['other/Registered.cmof'],row['logical_registered_files'])
        self.assertFalse(row['logical_local_file_consistent'])
        self.assertIsNone(row['resolved_target'])

    def test_missing_source_document_uri_does_not_guess_registration(self):
        row=self.reference(self.pair(source_uri=None))
        self.assertEqual('logical-uri-unavailable',row['logical_registration_status'])
        self.assertEqual('exact-unique-fragment',row['fragment_status'])
        self.assertFalse(row['qualified_identity_complete'])

    def test_unregistered_local_file_is_not_read_or_parsed(self):
        self.pair(href='Unregistered.cmof#Target')
        (self.base/'std/Unregistered.cmof').write_bytes(b'not XML; arbitrary unregistered local bytes')
        row=self.reference(self.inspect())
        self.assertEqual('unregistered-local-file',row['local_file_status'])
        self.assertIsNone(row['local_target']); self.assertIsNone(row['resolved_target'])

    def test_external_base_mof_reference_is_visible_and_not_accepted(self):
        row=self.reference(self.pair(href='http://schema.omg.org/spec/MOF/2.0/cmof.xml#String',expected='meta:PrimitiveType',
            peer_body='<ownedMember ids:type="meta:PrimitiveType" ids:id="String"/>'))
        self.assertEqual('cmof-base-metamodel',row['external_dependency'])
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
        self.assertIsNone(row['resolved_target'])
        self.assertEqual(1,len(row['unregistered_fragment_inventory_matches']))
        self.assertEqual('matched-bound-qname',row['unregistered_fragment_inventory_matches'][0]['candidate_qname_comparison']['status'])
        self.assertFalse(row['qualified_identity_complete'])

    def test_dangerous_uri_schemes_are_rejected_without_execution_or_read(self):
        for href in ('file:///etc/passwd#Target','javascript:alert(1)','data:text/xml,Target'):
            with self.subTest(href=href):
                self.rows=[];row=self.reference(self.pair(href=href))
                self.assertEqual('rejected-uri-scheme',row['local_file_status'])
                self.assertIsNone(row['local_target']); self.assertIsNone(row['resolved_target'])

    def test_relative_reference_cannot_inherit_a_dangerous_document_uri(self):
        self.put('std/Source.cmof',document('<ownedMember ids:type="meta:Class" ids:id="Target"/>'
                 '<type ids:type="meta:Class" href="#Target"/>'),'file:///unsafe/Source.cmof')
        report=self.inspect();row=self.reference(report)
        self.assertEqual('rejected-uri-scheme',row['local_file_status'])
        self.assertIsNone(row['resolved_target'])
        self.assertFalse(report['summary']['machine_source_registration_complete'])

    def test_absolute_and_parent_path_escape_are_rejected(self):
        for href in ('/etc/passwd#Target','../../outside.cmof#Target'):
            with self.subTest(href=href):
                self.rows=[];row=self.reference(self.pair(href=href))
                self.assertEqual('rejected-path-escape',row['local_file_status'])
                self.assertIsNone(row['resolved_target'])

    def test_symlink_escape_is_rejected_before_unregistered_file_access(self):
        self.pair(href='Escape.cmof#Target')
        outside=self.temporary_root/'outside.cmof';outside.write_bytes(b'secret unregistered bytes')
        (self.base/'std/Escape.cmof').symlink_to(outside)
        row=self.reference(self.inspect())
        self.assertEqual('rejected-path-escape',row['local_file_status'])
        self.assertIsNone(row['local_file'])

    def test_symlink_loop_records_a_diagnostic_without_aborting_inventory(self):
        self.pair(href='Loop.cmof#Target')
        (self.base/'std/Loop.cmof').symlink_to('Loop.cmof')
        row=self.reference(self.inspect())
        self.assertEqual('invalid-reference-uri',row['local_file_status'])
        self.assertIsNone(row['resolved_target']);self.assertTrue(row['diagnostic'])

    def test_percent_encoded_path_is_not_silently_decoded_to_an_alias(self):
        row=self.reference(self.pair(href='%50eer.cmof#Target'))
        self.assertEqual('unsupported-local-uri-component',row['local_file_status'])
        self.assertIsNone(row['resolved_target'])

    def test_control_characters_and_whitespace_do_not_normalize_to_a_registered_uri(self):
        for href in (PEER_URI+'\n#Target',' '+PEER_URI+'#Target',PEER_URI+'#Tar get'):
            with self.subTest(href=href):
                self.rows=[];row=self.reference(self.pair(href=href))
                self.assertEqual('invalid-reference-uri',row['local_file_status'])
                self.assertIsNone(row['resolved_target'])

    def test_malformed_uri_records_diagnostic_without_aborting_inventory(self):
        row=self.reference(self.pair(href='https://[invalid#Target'))
        self.assertEqual('invalid-reference-uri',row['local_file_status'])
        self.assertTrue(row['diagnostic']);self.assertFalse(row['qualified_identity_complete'])

    def test_missing_fragment_is_unadjudicated_not_root_inferred(self):
        for href in ('Peer.cmof','Peer.cmof#'):
            with self.subTest(href=href):
                self.rows=[];row=self.reference(self.pair(href=href))
                self.assertEqual('no-fragment-unadjudicated',row['fragment_status'])
                self.assertIsNone(row['resolved_target'])

    def test_changed_registered_source_hash_is_rejected(self):
        self.pair();(self.base/'std/Peer.cmof').write_bytes(b'changed source')
        with self.assertRaisesRegex(Invalid,'fingerprint conflict'):self.inspect()


class ActualNormativeReferenceRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bpmn=ledger('bpmn','2.0.2',bindings=[])
        cls.uml=ledger('uml','2.5.1',bindings=[])

    def test_bpmn_matches_independent_original_href_inventory(self):
        source=REPO/'togaf-standard-10th-ai/skills/_shared/standards/sources/bpmn-2.0.2'
        originals=[]
        for path in sorted(source.glob('*.cmof')):
            root=etree.fromstring(path.read_bytes())
            originals += [(path.name,e.sourceline,e.get('href')) for e in root.iter() if e.get('href') is not None]
        refs=self.bpmn['machine_reference_provenance']['references']
        reported=[(Path(r['source_identity']['file']).name,r['source_identity']['source_line'],r['original_href']) for r in refs]
        self.assertEqual(sorted(originals),sorted(reported))
        summary=self.bpmn['machine_reference_summary']
        self.assertEqual(163,summary['reference_count'])
        self.assertEqual(47,summary['local_exact_fragment_count'])
        self.assertEqual(46,summary['qualified_identity_complete_count'])
        self.assertEqual(4,summary['local_file_counts']['missing-local-file'])
        self.assertEqual(112,summary['external_dependency_counts']['cmof-base-metamodel'])
        self.assertFalse(summary['source_reference_identity_complete'])

    def test_original_semantic_fragments_are_preserved_without_bpmn20_substitution(self):
        refs=[r for r in self.bpmn['machine_reference_provenance']['references'] if r['original_href'].startswith('Semantic.cmof#')]
        self.assertEqual({'Core-Foundation-'+name for name in ('Extension','Relationship','RootElement','BaseElement')},{r['fragment'] for r in refs})
        for row in refs:
            self.assertIsNone(row['resolved_target']);self.assertIsNone(row['local_target'])
            self.assertEqual('https://www.omg.org/spec/BPMN/20100502/Semantic.cmof',row['logical_document_uri'])
        self.assertEqual(['Semantic.cmof'],self.bpmn['missing_machine_imports'])

    def test_actual_infrastructure_bpmndi_local_fragment_does_not_close_date_route(self):
        row=next(r for r in self.bpmn['machine_reference_provenance']['references'] if
            r['source_identity']['file'].endswith('/Infrastructure.cmof') and r['original_href']=='BPMNDI.cmof#BPMNDiagram')
        self.assertEqual('exact-unique-fragment',row['fragment_status'])
        self.assertEqual('matched-bound-qname',row['type_comparison']['status'])
        self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
        self.assertEqual('https://www.omg.org/spec/BPMN/20100502/BPMNDI.cmof',row['logical_document_uri'])
        self.assertIsNone(row['resolved_target'])

    def test_document_package_and_declaration_namespace_identities_are_separate(self):
        source=next(r for r in self.bpmn['machine_reference_provenance']['sources'] if r['file'].endswith('/BPMN20.cmof'))
        package=source['packages'][0]
        self.assertEqual('https://www.omg.org/spec/BPMN/20100501/BPMN20.cmof',source['logical_document_uri'])
        self.assertEqual('http://www.omg.org/spec/BPMN/20100524/MODEL-XMI',package['package_context'][0]['package_uri'])
        self.assertEqual('{'+CMOF+'}Package',package['declared_qname']['expanded_name'])

    def test_actual_standard_profile_namespace_difference_is_explicit(self):
        refs=[r for r in self.uml['machine_reference_provenance']['references'] if r['source_identity']['file'].endswith('/StandardProfile.xmi') and r['expected_qname']['lexical_value']=='uml:Class']
        self.assertEqual(34,len(refs))
        for row in refs:
            self.assertEqual('{http://www.omg.org/spec/UML/20161101}Class',row['expected_qname']['expanded_name'])
            self.assertEqual('unregistered-logical-uri',row['logical_registration_status'])
            self.assertIsNone(row['local_target']);self.assertIsNone(row['resolved_target'])
            target=[c for c in row['unregistered_fragment_inventory_matches']
                    if c['declaration']['source_identity']['file'].endswith('/UML.xmi')]
            self.assertEqual(1,len(target))
            self.assertEqual('{http://www.omg.org/spec/UML/20131001}Class',target[0]['declaration']['declared_qname']['expanded_name'])
            self.assertEqual('namespace-mismatch',target[0]['candidate_qname_comparison']['status'])
            self.assertFalse(target[0]['reference_identity_resolved'])
            self.assertEqual('unknown-type',row['type_comparison']['status'])
            self.assertFalse(row['qualified_identity_complete'])

    def test_actual_untyped_uml_references_are_not_expected_type_inferred(self):
        refs=self.uml['machine_reference_provenance']['references']
        untyped=[r for r in refs if r['expected_qname']['lexical_value'] is None]
        self.assertEqual(339,len(refs));self.assertEqual(237,len(untyped))
        self.assertTrue(all(r['type_comparison']['status']=='unknown-type' for r in untyped))
        self.assertTrue(all(r['resolved_target'] is None for r in untyped))


if __name__=='__main__':unittest.main()
