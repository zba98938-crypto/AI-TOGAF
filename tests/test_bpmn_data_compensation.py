"""Independent Data/IO and compensation positives, negatives and lossless exchange."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
import bpmn_data_compensation as backend
from standards import safe_xml,check_native,make_package,package_bytes,Invalid
from bpmn_data_compensation_fixtures import (data_model,event_data_model,compensation_model,
    by_id,change,element,io,association,add_flow_element,MODEL,definitions,bytes_xml)


class BPMNDataConstraintsTests(unittest.TestCase):
    def findings(self,data):
        return backend.check(safe_xml(data))['findings']

    def assert_rule(self,data,rule,native=True,schema_valid=True):
        rows=self.findings(data)
        self.assertIn(rule,{row['rule_id'] for row in rows},rows)
        matching=[row for row in rows if row['rule_id']==rule]
        self.assertTrue(all(row['source_locator'] and row['normative_source']['pdf_sha256']==backend.PDF_SHA256
                            and row['normative_source']['machine_source']['sha256']==backend.CMOF_SHA256 for row in matching))
        if native:
            report=check_native(data,'bpmn','2.0.2')
            self.assertTrue(any(rule+':' in message for message in report['errors']),report['errors'])
            if schema_valid:
                self.assertFalse(any('SCHEMAV_' in message for message in report['errors']),report['errors'])

    def test_positive_data_events_compensation_and_empty_specs_are_native_valid(self):
        root=definitions();p=element(root,'process',id='P');io(element(p,'task',id='T'),'EMPTY',inputs=0,outputs=0)
        for data in [data_model(),event_data_model(),compensation_model(),bytes_xml(root)]:
            with self.subTest(sha256=hashlib.sha256(data).hexdigest()):
                self.assertEqual([],self.findings(data));self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])

    def test_type_graph_is_derived_from_nested_official_package_and_complete_for_rules(self):
        subtype,graph=backend._metamodel()
        self.assertGreater(len(graph),100)
        for derived,base in [('Task','Activity'),('SubProcess','FlowElementsContainer'),
                             ('DataObject','ItemAwareElement'),('DataInput','ItemAwareElement'),
                             ('IntermediateThrowEvent','ThrowEvent'),('BoundaryEvent','CatchEvent')]:
            self.assertTrue(subtype(derived,base),(derived,base))
        self.assertFalse(subtype('Task','ItemAwareElement'))
        self.assertFalse(subtype('VendorProperty','ItemAwareElement'))
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'incomplete.cmof'
            raw=backend.META_PATH.read_bytes().replace(b'name="DataInput"',b'name="RemovedDataInput"',1)
            path.write_bytes(raw)
            with patch.object(backend,'META_PATH',path),patch.object(backend,'CMOF_SHA256',hashlib.sha256(raw).hexdigest()):
                report=backend.check(safe_xml(data_model()))
                self.assertEqual('unusable',report['source_status'])
                self.assertFalse(report['findings'])
                self.assertTrue(any('required classes unavailable: DataInput' in b for b in report['capability_uncovered']))

    def test_canonical_same_namespace_qnames_and_whitespace_remain_valid(self):
        original=data_model()
        for data in [original.replace(b'tns:',b''),original.replace(b'>DR<',b'> DR <')]:
            self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])

    def test_existing_task_gateway_and_flow_are_not_itemaware_references(self):
        model=change(data_model(),lambda r:add_flow_element(r,'sequenceFlow',id='F',sourceRef='A',targetRef='B'))
        for target in ['A','G','F']:
            with self.subTest(target=target):
                bad=change(model,lambda r:by_id(r,'DIN').find('{'+MODEL+'}sourceRef').__setattr__('text',target))
                self.assert_rule(bad,'data-association-type')

    def test_item_subject_ref_must_name_an_item_definition(self):
        self.assert_rule(change(data_model(),lambda r:by_id(r,'D').set('itemSubjectRef','tns:G')),'data-item-subject-type')

    def test_input_target_and_output_source_direction_and_owner_are_checked(self):
        cases=[('DIN','targetRef','A_OUT0'),('DIN','targetRef','B_IN0'),
               ('DOUT','sourceRef','A_IN0'),('DOUT','sourceRef','B_OUT0')]
        for sid,field,value in cases:
            with self.subTest(sid=sid,value=value):
                self.assert_rule(change(data_model(),lambda r:by_id(r,sid).find('{'+MODEL+'}'+field).__setattr__('text',value)),'data-association-direction')

    def test_event_catch_output_and_throw_input_associations_have_native_owners(self):
        for sid,field,value in [('CATCH_ASSOC','sourceRef','EVENT_IN'),('THROW_ASSOC','targetRef','EVENT_OUT')]:
            self.assert_rule(change(event_data_model(),lambda r:by_id(r,sid).find('{'+MODEL+'}'+field).__setattr__('text',value)),'data-association-direction')

    def test_without_transformation_exactly_one_source_is_required(self):
        def missing(r):
            child=by_id(r,'DIN').find('{'+MODEL+'}sourceRef');child.getparent().remove(child)
        def many(r):
            e=element(by_id(r,'DIN'),'sourceRef','P_PROP');p=e.getparent();p.remove(e);p.insert(0,e)
        for mutate in [missing,many]:self.assert_rule(change(data_model(),mutate),'data-association-source-cardinality')

    def test_transformation_allows_zero_or_multiple_sources_without_evaluating_text(self):
        def mutate(r,zero):
            e=by_id(r,'DIN')
            if zero:
                child=e.find('{'+MODEL+'}sourceRef');e.remove(child)
            else:
                child=element(e,'sourceRef','P_PROP');e.remove(child);e.insert(0,child)
            element(e,'transformation','literal(42)',language='urn:fixture-expression')
        for zero in [True,False]:
            data=change(data_model(),lambda r:mutate(r,zero))
            self.assertEqual([],self.findings(data));self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])

    def test_collection_matches_item_definition_and_false_defaults(self):
        for sid in ['D','A_IN0','A_OUT0']:
            self.assert_rule(change(data_model(),lambda r:by_id(r,sid).set('isCollection','true')),'data-item-collection')
        bad=change(data_model(),lambda r:by_id(r,'I').set('isCollection','true'))
        self.assert_rule(bad,'data-item-collection')
        def correct(r):
            by_id(r,'I').set('isCollection','true')
            for e in r.xpath('//*[local-name()="dataObject" or local-name()="dataInput" or local-name()="dataOutput"]'):
                e.set('isCollection','true')
        self.assertEqual([],self.findings(change(data_model(),correct)))

    def test_mismatched_identified_item_definitions_need_transformation(self):
        bad=change(data_model(),lambda r:by_id(r,'A_IN0').set('itemSubjectRef','tns:OTHER_I'))
        self.assert_rule(bad,'data-association-item-definition')
        corrected=change(bad,lambda r:element(by_id(r,'DIN'),'transformation','convert(source)',language='urn:fixture-expression'))
        self.assertEqual([],self.findings(corrected))

    def test_data_reference_effective_item_definition_is_derived_without_modifying_xml(self):
        data=data_model();root=safe_xml(data);before=etree.tostring(root)
        self.assertEqual([],backend.check(root)['findings']);self.assertEqual(before,etree.tostring(root))
        self.assertIsNone(by_id(root,'DR').get('itemSubjectRef'))
        self.assert_rule(change(data,lambda r:by_id(r,'DR').set('itemSubjectRef','tns:I')),'data-reference-item-definition')

    def test_reference_types_reject_existing_gateway_and_task(self):
        for sid,field,value in [('DR','dataObjectRef','G'),('DSR','dataStoreRef','A')]:
            lexical=value if field=='dataObjectRef' else 'tns:'+value
            self.assert_rule(change(data_model(),lambda r:by_id(r,sid).set(field,lexical)),'data-reference-type')

    def test_outer_and_sibling_scope_objects_and_properties_are_not_leaked(self):
        for value in ['INNER_D','FOREIGN_D','SUB_PROP','B_IN0']:
            self.assert_rule(change(data_model(),lambda r:by_id(r,'DIN').find('{'+MODEL+'}sourceRef').__setattr__('text',value)),'data-association-scope')
        self.assert_rule(change(data_model(),lambda r:by_id(r,'DR').set('dataObjectRef','INNER_D')),'data-association-scope')
        def task_property(r):
            element(by_id(r,'B'),'property',id='B_PROP',itemSubjectRef='tns:I')
            # Official Task property follows IOSpecification.
            by_id(r,'DIN').find('{'+MODEL+'}sourceRef').text='B_PROP'
        self.assert_rule(change(data_model(),task_property),'data-association-scope')

    def test_inner_activity_can_access_outer_data_and_its_own_property(self):
        for value in ['P_PROP','D','SUB_PROP']:
            data=change(data_model(),lambda r:by_id(r,'GRAND_IN').find('{'+MODEL+'}sourceRef').__setattr__('text',value))
            self.assertEqual([],self.findings(data))
        own=change(data_model(),lambda r:by_id(r,'DIN').find('{'+MODEL+'}sourceRef').__setattr__('text','A_PROP'))
        self.assertEqual([],self.findings(own))

    def test_data_object_and_property_containment_have_separate_rule_evidence(self):
        def move(r,sid):
            e=by_id(r,sid);e.getparent().remove(e);r.append(e)
        self.assert_rule(change(data_model(),lambda r:move(r,'D')),'data-object-containment',schema_valid=False)
        self.assert_rule(change(data_model(),lambda r:move(r,'A_PROP')),'property-containment',schema_valid=False)

    def test_embedded_subprocess_cannot_define_direct_data_io(self):
        def mutate(r):
            owner=by_id(r,'SUB');spec=io(owner,'SUB_IO');owner.remove(spec);owner.insert(0,spec)
        self.assert_rule(change(data_model(),mutate),'embedded-subprocess-io')

    def test_io_set_types_owner_and_pairing_are_independent_of_id_existence(self):
        for sid,field,value,rule in [('A_IS','dataInputRefs','A_OUT0','io-set-reference-type'),
                                   ('A_IS','dataInputRefs','B_IN0','io-set-reference-scope'),
                                   ('A_OS','dataOutputRefs','A_IN0','io-set-reference-type'),
                                   ('A_IS','outputSetRefs','B_OS','io-set-reference-scope')]:
            self.assert_rule(change(data_model(),lambda r:by_id(r,sid).find('{'+MODEL+'}'+field).__setattr__('text',value)),rule)

    def test_optional_and_while_executing_refs_are_main_set_subsets(self):
        for sid,field,value in [('A_IS','optionalInputRefs','B_IN0'),('A_IS','whileExecutingInputRefs','B_IN0'),
                               ('A_OS','optionalOutputRefs','B_OUT0'),('A_OS','whileExecutingOutputRefs','B_OUT0')]:
            def mutate(r):
                group=by_id(r,sid);child=element(group,field,value);group.remove(child);group.insert(1,child)
            self.assert_rule(change(data_model(),mutate),'io-set-subset')
        def valid_subset(r):
            group=by_id(r,'A_IS');child=element(group,'optionalInputRefs','A_IN0');group.remove(child);group.insert(1,child)
        good=change(data_model(),valid_subset)
        self.assertEqual([],self.findings(good))

    def test_every_declared_input_and_output_needs_corresponding_set_membership(self):
        for sid,field in [('A_IS','dataInputRefs'),('A_OS','dataOutputRefs')]:
            def mutate(r):
                child=by_id(r,sid).find('{'+MODEL+'}'+field);child.getparent().remove(child)
            self.assert_rule(change(data_model(),mutate),'io-set-membership')
        def second_set(r):
            spec=by_id(r,'A_IO');group=element(spec,'inputSet',id='SECOND_IS');element(group,'dataInputRefs','A_IN0')
            spec.remove(group);spec.insert(3,group)
            child=by_id(r,'A_IS').find('{'+MODEL+'}dataInputRefs');child.getparent().remove(child)
        self.assertEqual([],self.findings(change(data_model(),second_set)))

    def test_event_data_input_and_output_need_their_corresponding_set(self):
        for sid in ['EVENT_IS','EVENT_OS']:
            bad=change(event_data_model(),lambda r:by_id(r,sid).getparent().remove(by_id(r,sid)))
            self.assert_rule(bad,'io-set-membership')
        for sid,field in [('EVENT_IS','dataInputRefs'),('EVENT_OS','dataOutputRefs')]:
            def empty_set(r):
                group=by_id(r,sid);group.remove(group.find('{'+MODEL+'}'+field))
            self.assert_rule(change(event_data_model(),empty_set),'io-set-membership')

    def test_external_or_shadowed_qname_does_not_alias_local_reference(self):
        for sid,field in [('DSR','dataStoreRef'),('D','itemSubjectRef')]:
            bad=change(data_model(),lambda r:by_id(r,sid).set(field,'outside:'+by_id(r,sid).get(field).split(':')[-1]))
            report=check_native(bad,'bpmn','2.0.2');self.assertEqual([],report['errors']);self.assertTrue(any('outside:' in b for b in report['blockers']))
        # Preserve the lexical QName declaration. Tree replacement may drop an
        # unused namespace binding without knowing QName-valued attributes.
        shadow=data_model().replace(b'<dataObject id="D"',b'<dataObject xmlns:tns="urn:outside" id="D"')
        report=check_native(shadow,'bpmn','2.0.2')
        self.assertEqual([],report['errors']);self.assertTrue(any('tns:I' in b for b in report['blockers']))

    def test_idref_fields_reject_prefixed_values_at_schema_boundary(self):
        for sid,field,child in [('DR','dataObjectRef',False),('DIN','sourceRef',True),('A_IS','dataInputRefs',True)]:
            def mutate(r):
                e=by_id(r,sid)
                if child:
                    ref=e.find('{'+MODEL+'}'+field);ref.text='outside:'+ref.text
                else:e.set(field,'outside:'+e.get(field))
            bad=change(data_model(),mutate)
            self.assertTrue(check_native(bad,'bpmn','2.0.2')['errors'])
            self.assertFalse(backend.check(safe_xml(bad))['findings'])

    def test_vendor_item_reference_type_is_uncovered_and_material_loss_is_separate(self):
        def vendor(r):
            e=element(by_id(r,'P'),'extensionElements');etree.SubElement(e,'{urn:vendor}property',id='VENDOR_ITEM')
            by_id(r,'P').remove(e);by_id(r,'P').insert(0,e)
            by_id(r,'DIN').find('{'+MODEL+'}sourceRef').text='VENDOR_ITEM'
        report=check_native(change(data_model(),vendor),'bpmn','2.0.2')
        self.assertEqual([],report['errors']);self.assertTrue(any('reference type to vendor' in b for b in report['diagnostic_groups']['capability_uncovered']))
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(backend,'META_PATH',Path(tmp)/'missing.cmof'):
                missing=check_native(data_model(),'bpmn','2.0.2')
                self.assertEqual([],missing['errors']);self.assertTrue(missing['diagnostic_groups']['missing_material'])
                self.assertEqual('unusable',missing['design_time_semantics']['data_compensation_validation']['source_status'])
                self.assertEqual('incomplete',missing['conformance_status'])
            path=Path(tmp)/'wrong.cmof';path.write_text('<not-the-standard/>')
            with patch.object(backend,'META_PATH',path):
                conflict=check_native(data_model(),'bpmn','2.0.2')
                self.assertTrue(any('fingerprint conflict' in b for b in conflict['blockers']))


class BPMNCompensationConstraintsTests(unittest.TestCase):
    def assert_rule(self,data,rule):
        findings=backend.check(safe_xml(data))['findings']
        self.assertIn(rule,{f['rule_id'] for f in findings},findings)
        errors=check_native(data,'bpmn','2.0.2')['errors']
        self.assertTrue(any(rule+':' in e for e in errors))
        self.assertFalse(any('SCHEMAV_' in e for e in errors),errors)

    def test_top_level_and_non_event_subprocess_compensation_starts_are_rejected(self):
        def top(r):element(add_flow_element(r,'startEvent',id='BAD_START'),'compensateEventDefinition',id='BAD_COMP')
        self.assert_rule(change(compensation_model(),top),'compensation-start-scope')
        self.assert_rule(change(compensation_model(),lambda r:by_id(r,'EVENT_SUB').set('triggeredByEvent','false')),'compensation-start-scope')

    def test_catching_intermediate_compensation_is_boundary_only(self):
        def mutate(r):element(add_flow_element(r,'intermediateCatchEvent',id='BAD_CATCH'),'compensateEventDefinition',id='BAD_COMP')
        self.assert_rule(change(compensation_model(),mutate),'compensation-catch-placement')

    def test_boundary_compensation_outgoing_sequence_flow_is_rejected(self):
        for reference in ['BOUNDARY',' BOUNDARY ']:
            bad=change(compensation_model(),lambda r:add_flow_element(r,'sequenceFlow',id='F',sourceRef=reference,targetRef='B'))
            self.assert_rule(bad,'compensation-boundary-flow')

    def test_activity_reference_cannot_name_gateway_or_data_definition(self):
        self.assert_rule(change(compensation_model(),lambda r:by_id(r,'END_COMP').set('activityRef','tns:G')),'compensation-activity-reference-type')

    def test_child_and_other_process_activity_are_not_visible_from_throw_scope(self):
        self.assert_rule(change(compensation_model(),lambda r:by_id(r,'END_COMP').set('activityRef','tns:INNER')),'compensation-activity-visibility')
        def other(r):
            p=element(r,'process',id='Q');element(p,'task',id='OTHER');by_id(r,'END_COMP').set('activityRef','tns:OTHER')
        self.assert_rule(change(compensation_model(),other),'compensation-activity-visibility')
        self.assert_rule(change(compensation_model(),lambda r:by_id(r,'INNER_END_COMP').set('activityRef','tns:A')),'compensation-activity-visibility')

    def test_normal_same_scope_and_compensating_subprocess_parent_targets_are_valid(self):
        self.assertEqual([],backend.check(safe_xml(compensation_model()))['findings'])
        data=change(compensation_model(),lambda r:by_id(r,'COMP_END_DEF').attrib.pop('activityRef'))
        self.assertEqual([],check_native(data,'bpmn','2.0.2')['errors'])

    def test_referenced_event_definition_has_the_same_constraints_as_inline_definition(self):
        def mutate(r):
            definition=by_id(r,'BOUNDARY_COMP');definition.getparent().remove(definition);r.insert(0,definition)
            element(by_id(r,'BOUNDARY'),'eventDefinitionRef','tns:BOUNDARY_COMP')
            add_flow_element(r,'sequenceFlow',id='F',sourceRef='BOUNDARY',targetRef='B')
        self.assert_rule(change(compensation_model(),mutate),'compensation-boundary-flow')

    def test_external_activity_reference_is_material_blocked_without_local_alias(self):
        bad=change(compensation_model(),lambda r:by_id(r,'END_COMP').set('activityRef','outside:A'))
        report=check_native(bad,'bpmn','2.0.2');self.assertEqual([],report['errors'])
        self.assertTrue(any('outside:A' in b for b in report['blockers']))

    def test_compensation_handler_normal_flow_remains_rejected_by_legacy_rule(self):
        bad=change(compensation_model(),lambda r:add_flow_element(r,'sequenceFlow',id='F',sourceRef='B',targetRef='HANDLER'))
        report=check_native(bad,'bpmn','2.0.2');self.assertTrue(any('compensation-flow:' in e for e in report['errors']))

    def test_source_discrepancies_are_recorded_without_inventing_compensable_or_state_rejections(self):
        data=change(compensation_model(),lambda r:by_id(r,'BOUNDARY').getparent().remove(by_id(r,'BOUNDARY')))
        def no_handler_link(r):by_id(r,'HANDLER_LINK').getparent().remove(by_id(r,'HANDLER_LINK'))
        data=change(data,no_handler_link)
        report=backend.check(safe_xml(data))
        self.assertEqual([],report['findings']);self.assertTrue(any(a['element']=='SubProcess.compensable' for a in report['exchange_adaptations']))
        with_state=change(data_model(),lambda r:element(by_id(r,'D'),'dataState',id='STATE',name='审阅中'))
        self.assertEqual([],check_native(with_state,'bpmn','2.0.2')['errors'])
        invented=change(compensation_model(),lambda r:by_id(r,'SUB').set('compensable','true'))
        self.assertTrue(check_native(invented,'bpmn','2.0.2')['errors'])

    def test_native_import_export_roundtrip_preserves_data_compensation_and_explicit_source_bytes(self):
        for original in [data_model(),event_data_model(),compensation_model()]:
            package=make_package(original,'bpmn','2.0.2')
            self.assertEqual(original,package_bytes(package,'bpmn','2.0.2'))
            self.assertEqual(hashlib.sha256(original).hexdigest(),package['native_sha256'])
            self.assertFalse(package['report'].get('full_language_acceptance',False))
        invalid=change(compensation_model(),lambda r:by_id(r,'END_COMP').set('activityRef','tns:G'))
        with self.assertRaises(Invalid):make_package(invalid,'bpmn','2.0.2')


if __name__=='__main__':unittest.main()
