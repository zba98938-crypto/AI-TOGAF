"""Schema-valid MI counterexamples and independent scoped exchange type audit."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
import bpmn_data_compensation as backend
from standards import safe_xml,check_native,make_package,package_bytes
from bpmn_data_compensation_fixtures import by_id,change,element,MODEL
from bpmn_role_type_fixtures import multi_instance_model,LOCAL_ROLE_ORACLE


class BPMNRoleTypeTests(unittest.TestCase):
    data=multi_instance_model()

    def resolver(self):
        subtype,graph=backend._metamodel()
        return backend._exchange_types(subtype,graph)

    def test_schema_valid_multi_instance_roles_and_implicit_event_are_native_valid(self):
        self.assertEqual([],check_native(self.data,'bpmn','2.0.2')['errors'])
        model_class,audit=self.resolver();root=safe_xml(self.data)
        for identity,expected in [('MI_INPUT','DataInput'),('MI_OUTPUT','DataOutput'),
                                  ('IMPLICIT_EVENT','ImplicitThrowEvent'),('CONDITION','FormalExpression'),
                                  ('COMPLETE','Expression')]:
            self.assertEqual(expected,model_class(by_id(root,identity)))
        self.assertGreater(audit['global_element_count'],100)
        self.assertEqual(backend.XSD_SHA256,audit['schema_sha256'])

    def test_all_analogous_role_declarations_match_independent_source_oracle(self):
        _,audit=self.resolver()
        actual={(r['owner_class'],r['role']):r['model_class'] for r in audit['local_roles']}
        self.assertEqual(LOCAL_ROLE_ORACLE,actual)
        for row in audit['local_roles']:
            self.assertTrue(row['cmof_native_id'] and row['cmof_locator'] and row['xsd_locator'])
            self.assertTrue(row['containment_cross_checked'])
        implicit=next(r for r in audit['local_roles'] if r['role']=='event')
        self.assertEqual('Event',implicit['global_class'])
        self.assertEqual('ImplicitThrowEvent',implicit['model_class'])

    def test_both_mi_data_roles_reject_existing_non_item_definition_without_schema_error(self):
        for identity in ['MI_INPUT','MI_OUTPUT']:
            with self.subTest(identity=identity):
                invalid=change(self.data,lambda r:by_id(r,identity).set('itemSubjectRef','tns:G'))
                report=check_native(invalid,'bpmn','2.0.2')
                self.assertTrue(any('data-item-subject-type:' in e for e in report['errors']),report['errors'])
                self.assertFalse(any('SCHEMAV_' in e for e in report['errors']),report['errors'])

    def test_both_mi_data_roles_enforce_collection_false_default_and_true_mismatch(self):
        for identity in ['MI_INPUT','MI_OUTPUT']:
            with self.subTest(identity=identity):
                invalid=change(self.data,lambda r:by_id(r,identity).set('isCollection','true'))
                report=check_native(invalid,'bpmn','2.0.2')
                self.assertTrue(any('data-item-collection:' in e for e in report['errors']),report['errors'])
                self.assertFalse(any('SCHEMAV_' in e for e in report['errors']))
        def matching(root):
            for identity in ['MI_INPUT','MI_OUTPUT']:
                e=by_id(root,identity);e.set('isCollection','true');e.set('itemSubjectRef','tns:COLLECTION')
        errors=check_native(change(self.data,matching),'bpmn','2.0.2')['errors']
        self.assertFalse(any('data-item-collection:' in e for e in errors))
        self.assertEqual(2,sum('mi-data-item-scalar:' in e for e in errors))

    def test_role_mapping_is_scoped_and_vendor_or_similar_tags_are_not_guessed(self):
        model_class,_=self.resolver()
        root=safe_xml(self.data);task=by_id(root,'A')
        wrong_owner=element(task,'inputDataItem',id='WRONG_OWNER')
        lookalike=element(by_id(root,'LOOP'),'inputDataItemExtra',id='LOOKALIKE')
        vendor=etree.SubElement(by_id(root,'LOOP'),'{urn:vendor}inputDataItem',id='VENDOR')
        self.assertIsNone(model_class(wrong_owner));self.assertIsNone(model_class(lookalike));self.assertIsNone(model_class(vendor))

    def test_declared_xsi_type_specialization_is_namespace_and_inheritance_checked(self):
        model_class,_=self.resolver();root=safe_xml(self.data)
        expression=by_id(root,'COMPLETE')
        expression.set('{http://www.w3.org/2001/XMLSchema-instance}type','tns:tFormalExpression')
        # tns identifies model targetNamespace, not the BPMN schema namespace.
        self.assertIsNone(model_class(expression))
        expression.set('{http://www.w3.org/2001/XMLSchema-instance}type','tFormalExpression')
        self.assertEqual('FormalExpression',model_class(expression))
        expression.set('{http://www.w3.org/2001/XMLSchema-instance}type','tDataInput')
        self.assertIsNone(model_class(expression))

    def test_missing_or_conflicting_schema_is_material_unusable_without_false_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing=Path(tmp)/'absent.xsd'
            with patch.object(backend,'SCHEMA_PATH',missing):
                report=backend.check(safe_xml(self.data))
                self.assertEqual('unusable',report['source_status']);self.assertEqual([],report['findings'])
            conflict=Path(tmp)/'conflicting.xsd';conflict.write_bytes(b'<schema/>')
            with patch.object(backend,'SCHEMA_PATH',conflict):
                report=backend.check(safe_xml(self.data))
                self.assertEqual('unusable',report['source_status'])
                self.assertTrue(any('Semantic.xsd fingerprint conflict' in e for e in report['capability_uncovered']))

    def test_matching_fingerprint_cannot_hide_a_role_type_or_composite_conflict(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'role-conflict.xsd'
            raw=backend.SCHEMA_PATH.read_bytes().replace(b'name="inputDataItem" type="tDataInput"',b'name="inputDataItem" type="tDataOutput"',1)
            path.write_bytes(raw)
            with patch.object(backend,'SCHEMA_PATH',path),patch.object(backend,'XSD_SHA256',hashlib.sha256(raw).hexdigest()):
                report=backend.check(safe_xml(self.data))
                self.assertEqual('unusable',report['source_status'])
                self.assertTrue(any('containment role/type conflict' in e for e in report['capability_uncovered']))
            path=Path(tmp)/'role-conflict.cmof'
            raw=backend.META_PATH.read_bytes().replace(b'id="MultiInstanceLoopCharacteristics-inputDataItem" name="inputDataItem" type="DataInput"',b'id="MultiInstanceLoopCharacteristics-inputDataItem" name="inputDataItem" type="DataOutput"',1)
            path.write_bytes(raw)
            with patch.object(backend,'META_PATH',path),patch.object(backend,'CMOF_SHA256',hashlib.sha256(raw).hexdigest()):
                report=backend.check(safe_xml(self.data))
                self.assertEqual('unusable',report['source_status'])
                self.assertTrue(any('containment role/type conflict' in e for e in report['capability_uncovered']))

    def test_missing_required_role_declaration_is_unusable_even_with_matching_fingerprint(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'missing-role.xsd'
            raw=backend.SCHEMA_PATH.read_bytes().replace(b'name="inputDataItem" type="tDataInput"',b'name="inputDataItem" type="xsd:QName"',1)
            path.write_bytes(raw)
            with patch.object(backend,'SCHEMA_PATH',path),patch.object(backend,'XSD_SHA256',hashlib.sha256(raw).hexdigest()):
                report=backend.check(safe_xml(self.data))
                self.assertEqual('unusable',report['source_status'])
                self.assertTrue(any('required MultiInstance data role declarations unavailable' in e for e in report['capability_uncovered']))

    def test_native_mi_source_and_expression_bytes_survive_validation_and_package_roundtrip(self):
        root=safe_xml(self.data);before=etree.tostring(root)
        self.assertEqual([],backend.check(root)['findings']);self.assertEqual(before,etree.tostring(root))
        self.assertEqual(self.data,package_bytes(make_package(self.data,'bpmn','2.0.2'),'bpmn','2.0.2'))


if __name__=='__main__':unittest.main()
