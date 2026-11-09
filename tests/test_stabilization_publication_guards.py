"""Adversarial publication fixtures are not execution or model-review evidence.

Every attack has matching current-round identifiers and freshly computed file
digests. The gates must validate what those bytes establish, not trust labels.
"""
import importlib.util
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'stabilization_publication_guards_target',
    REPO / 'togaf-standard-10th-ai/maintenance/stabilization_evidence.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class StabilizationPublicationGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='togaf-publication-attack-')
        self.root = Path(self.temp.name).resolve()
        self.round = {'round_id': 'current', 'source_commit': 'a' * 40,
                      'prerequisites': {}}
        (self.root / 'source.py').write_text('def unrelated():\n    return True\n')
        (self.root / 'current.json').write_text('{"atlas":"unchanged"}\n')
        (self.root / 'catalogue.html').write_text('<!doctype html><p>Unchanged</p>\n')
        entry_inputs = {'schema_version': 'stabilization-entry-inputs/1',
                        'round_id': self.round['round_id'],
                        'entries': {key: module.reference(self.root / name, self.root)
                                    for key, name in (('current_map', 'current.json'),
                                                      ('catalogue', 'catalogue.html'))}}
        self.freeze = self.identity('stabilization-source-freeze/1', 'source_freeze',
                                    passed=True,
                                    files={name: module.sha(self.root / name) for name in
                                           ('source.py', 'current.json', 'catalogue.html')},
                                    entry_inputs=entry_inputs,
                                    excluded_generated_paths=[],
                                    excluded_generated_prefixes=[])
        self.round['prerequisites']['source_freeze'] = self.ref('freeze.json', self.freeze)

    def tearDown(self):
        self.temp.cleanup()

    def identity(self, schema, stage, **extra):
        return {'schema_version': schema, 'stage': stage,
                'round_id': self.round['round_id'],
                'source_commit': self.round['source_commit'], **extra}

    def ref(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('x') as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        return module.reference(path, self.root)

    def attack_execution_envelopes(self, raw=None):
        for stage in ('source_closure', 'package_verification',
                      'engineering_verification', 'model_evaluation'):
            envelope = self.identity('stabilization-execution-stage/1', stage, passed=True)
            if raw is not None:
                envelope['evidence'] = raw
            self.round['prerequisites'][stage] = self.ref(stage + '.json', envelope)

    def generated_report(self, name='actual-pending-report.json'):
        path = self.root / name
        result = module.report(self.round, path, self.root)
        return result, module.reference(path, self.root)

    def test_report_rejects_execution_envelopes_without_raw_evidence(self):
        self.attack_execution_envelopes()
        result, _ = self.generated_report()
        rows = {row['stage']: row for row in result['stages']}
        for stage in ('source_closure', 'package_verification',
                      'engineering_verification', 'model_evaluation'):
            with self.subTest(stage=stage):
                self.assertFalse(rows[stage]['passed'])
        self.assertFalse(result['engineering_stable'])
        self.assertFalse(result['technical_scope_complete'])

    def test_report_rejects_execution_envelopes_with_unrelated_raw_json(self):
        raw = self.ref('unrelated-json.json', {'passed': True, 'label': 'no execution'})
        self.attack_execution_envelopes(raw)
        result, _ = self.generated_report()
        rows = {row['stage']: row for row in result['stages']}
        for stage in ('source_closure', 'package_verification',
                      'engineering_verification', 'model_evaluation'):
            with self.subTest(stage=stage):
                self.assertFalse(rows[stage]['passed'])
        self.assertFalse(result['engineering_stable'])

    def test_single_fake_standard_item_cannot_certify_full_uml_and_bpmn(self):
        binding = {'file': 'source.py', 'sha256': module.sha(self.root / 'source.py'),
                   'symbol': 'unrelated'}
        refs = {}
        for language, version in (('uml', '2.5.1'), ('bpmn', '2.0.2')):
            item = {'id': language + ':only-invented-item',
                    'applicability': 'design-time-declaration',
                    'implementation_status': 'implemented',
                    'verification_status': 'passed',
                    'implementation': [dict(binding)], 'positive_tests': [dict(binding)],
                    'negative_tests': [dict(binding)], 'verification_results': [{}]}
            data = {'schema_version': 'native-design-time-coverage/1',
                    'language': language, 'version': version,
                    'completeness': {'source_scope_complete': True,
                                     'applicability_adjudication_complete': True},
                    'items': [item]}
            refs[language] = self.ref(language + '-invented-coverage.json', data)
        self.round['standard_capabilities'] = refs
        result, _ = self.generated_report()
        self.assertFalse(result['standard_capabilities_complete'])
        self.assertFalse(result['technical_scope_complete'])

    def test_single_fake_material_unit_and_independent_label_remain_incomplete(self):
        inventory = {'schema_version': 'full-material-source-unit-inventory/1',
                     'units': [{'id': 'only-invented-unit',
                                'classification': 'body',
                                'translation_status': 'body-translation-missing'}],
                     'input_sha256': {'source.py': module.sha(self.root / 'source.py')}}
        inventory_ref = self.ref('invented-inventory.json', inventory)
        arbitrary_evidence = self.ref('not-a-model-session.json', {})
        materials = {'schema_version': 'independent-material-review/1',
                     'round_id': self.round['round_id'],
                     'source_commit': self.round['source_commit'],
                     'source_unit_inventory': inventory_ref,
                     'items': [{'id': 'only-invented-unit', 'classification': 'body',
                                'disposition': 'pretend complete despite missing body',
                                'review_status': 'passed', 'independent_model_review': True,
                                'evidence': [arbitrary_evidence]}]}
        self.round['material_review'] = self.ref('invented-review.json', materials)
        result, _ = self.generated_report()
        self.assertFalse(result['source_material_review_complete'])
        self.assertFalse(result['material_review']['complete'])
        self.assertFalse(result['technical_scope_complete'])

    def forged_complete_report(self):
        return self.identity('stabilization-report/1', 'total_report',
                             stages=[], engineering_stable=True,
                             standard_capabilities_complete=True,
                             standard_checks={'uml': {'complete': True},
                                              'bpmn': {'complete': True}},
                             standard_capabilities={}, material_review={},
                             source_material_review_complete=True,
                             technical_scope_complete=True, all_work_complete=False)

    def test_ledger_rejects_complete_report_with_empty_stages(self):
        report_ref = self.ref('forged-report.json', self.forged_complete_report())
        self.round['prerequisites']['total_report'] = report_ref
        # Even a second matching downstream label must not authorize the report.
        pack = self.identity('business-acceptance-pack/1', 'business_acceptance_pack',
                             total_report=report_ref, ready_for_signature=True,
                             materials=[], missing_material_roles=[])
        self.round['acceptance_pack'] = self.ref('forged-pack.json', pack)
        with self.assertRaises(ValueError):
            module.ledger(self.round, self.root / 'ledger.json', self.root)

    def test_status_rejects_complete_ledger_with_empty_requirements(self):
        _, report_ref = self.generated_report()
        self.round['prerequisites']['total_report'] = report_ref
        forged = self.identity('stabilization-ledger/1', 'ledger',
                               total_report=report_ref, requirements=[],
                               engineering_stable=True, technical_delivery_complete=True)
        self.round['prerequisites']['ledger'] = self.ref('forged-ledger.json', forged)
        with self.assertRaises(ValueError):
            module.completion_status(self.round, self.root / 'status.json', self.root)

    def test_final_rejects_complete_labels_built_from_empty_publications(self):
        raw = self.ref('raw-label.json', {'passed': True})
        self.attack_execution_envelopes(raw)
        entries = self.freeze['entry_inputs']['entries']
        hashes = {key: record['sha256'] for key, record in entries.items()}
        activation = self.identity('current-output-activation/1', 'entrypoint_activation',
                                   applied=True, passed=True, before_sha256=hashes,
                                   after_sha256=hashes, proposed_sha256=hashes,
                                   entry_files={key: {'path': record['path'],
                                                      'before_sha256': record['sha256'],
                                                      'after_sha256': record['sha256']}
                                                for key, record in entries.items()})
        activation_ref = self.ref('activation-label.json', activation)
        self.round['prerequisites']['entrypoint_activation'] = self.ref(
            'activation-envelope.json', self.identity('stabilization-execution-stage/1',
                                                      'entrypoint_activation', passed=True,
                                                      evidence=activation_ref))
        report_ref = self.ref('empty-stage-report.json', self.forged_complete_report())
        ledger_ref = self.ref('empty-requirement-ledger.json', self.identity(
            'stabilization-ledger/1', 'ledger', total_report=report_ref,
            requirements=[], technical_delivery_complete=True))
        status_ref = self.ref('complete-status-label.json', self.identity(
            'stabilization-status/1', 'completion_status', ledger=ledger_ref,
            technical_delivery_complete=True, all_requested_delivery_complete=True))
        self.round['prerequisites'].update(total_report=report_ref, ledger=ledger_ref,
                                           completion_status=status_ref)
        with self.assertRaises(ValueError):
            module.final_readonly(self.round, self.root / 'final-readonly.json', self.root)

    def real_materials(self):
        """Nonempty local fixture inputs, never business or model acceptance."""
        roles = ('reproduction', 'sources', 'decisions', 'deliverables',
                 'exception_paths', 'evaluation_results')
        return [{'role': role, 'description': 'Synthetic retained ' + role,
                 'evidence': self.ref('materials/' + role + '.json',
                                      {'role': role, 'records': ['synthetic source fixture']})}
                for role in roles]

    def real_pack(self):
        _, report_ref = self.generated_report()
        self.round['prerequisites']['total_report'] = report_ref
        self.round['acceptance_materials'] = self.real_materials()
        path = self.root / 'actual-pack.json'
        data = module.acceptance_pack(self.round, path, self.root)
        self.round['acceptance_pack'] = module.reference(path, self.root)
        return data, path

    def altered_pack(self, data, name='altered-pack.json', sheet=None):
        ref = self.ref(name, data)
        if sheet is not None:
            (self.root / name).with_suffix('.md').write_bytes(sheet)
        return ref

    def test_real_six_materials_and_unsigned_sheet_are_read_only_and_incomplete(self):
        data, path = self.real_pack()
        before = {str(p.relative_to(self.root)): module.sha(p)
                  for p in self.root.rglob('*') if p.is_file()}
        verified = module.verified_acceptance_pack(self.round['acceptance_pack'],
                                                   self.round, self.root)
        self.assertEqual(verified, data)
        self.assertEqual(data['missing_material_roles'], [])
        self.assertFalse(data['technical_scope_complete'])
        self.assertFalse(data['ready_for_signature'])
        self.assertEqual(data['signatures'], {'professional_reviewer': None,
                                              'business_owner': None,
                                              'organization_authority': None})
        text = path.with_suffix('.md').read_text()
        for role in ('人工专业验收', '业务负责人验收', '真实组织批准'):
            self.assertIn('| ' + role + ' | 待填写 | 待填写 | 待填写 | 待签署 |', text)
        ledger = module.build_ledger(self.round, self.root)
        self.assertFalse(ledger['technical_delivery_complete'])
        after = {str(p.relative_to(self.root)): module.sha(p)
                 for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_pack_ready_relabel_is_rejected_with_real_six_materials(self):
        data, path = self.real_pack()
        forged = copy.deepcopy(data)
        forged['ready_for_signature'] = True
        self.round['acceptance_pack'] = self.altered_pack(
            forged, sheet=path.with_suffix('.md').read_bytes())
        with self.assertRaises(ValueError):
            module.build_ledger(self.round, self.root)

    def test_pack_cannot_omit_actual_materials_and_claim_no_missing_roles(self):
        data, path = self.real_pack()
        forged = copy.deepcopy(data)
        forged.update(materials=[], missing_material_roles=[], ready_for_signature=True)
        self.round['acceptance_pack'] = self.altered_pack(
            forged, sheet=path.with_suffix('.md').read_bytes())
        with self.assertRaises(ValueError):
            module.build_ledger(self.round, self.root)

    def test_pack_report_binding_cannot_change_with_matching_round_and_commit(self):
        data, path = self.real_pack()
        _, different_ref = self.generated_report('same-round-different-report-path.json')
        forged = copy.deepcopy(data)
        forged['total_report'] = different_ref
        self.round['acceptance_pack'] = self.altered_pack(
            forged, sheet=path.with_suffix('.md').read_bytes())
        with self.assertRaises(ValueError):
            module.build_ledger(self.round, self.root)

    def test_pack_rejects_missing_edited_or_escaping_unsigned_sheet(self):
        data, path = self.real_pack()
        original = path.with_suffix('.md').read_bytes()
        for case in ('missing', 'edited', 'symlink'):
            with self.subTest(case=case):
                ref = self.altered_pack(data, name=case + '-pack.json')
                sheet_path = (self.root / ref['path']).with_suffix('.md')
                if case == 'edited':
                    sheet_path.write_bytes(original.replace(
                        '| 真实组织批准 | 待填写 | 待填写 | 待填写 | 待签署 |'.encode(), b''))
                elif case == 'symlink':
                    sheet_path.symlink_to(path.with_suffix('.md'))
                with self.assertRaises(ValueError):
                    module.verified_acceptance_pack(ref, self.round, self.root)

    def test_pack_cannot_manufacture_professional_or_organization_signatures(self):
        data, path = self.real_pack()
        for role in data['signatures']:
            with self.subTest(role=role):
                forged = copy.deepcopy(data)
                forged['signatures'][role] = 'forged approval'
                ref = self.altered_pack(forged, name=role + '-pack.json',
                                        sheet=path.with_suffix('.md').read_bytes())
                with self.assertRaises(ValueError):
                    module.verified_acceptance_pack(ref, self.round, self.root)

    def test_pack_rechecks_actual_material_fingerprint(self):
        _, _ = self.real_pack()
        ref = self.round['acceptance_materials'][0]['evidence']
        (self.root / ref['path']).write_text('{"changed":"after package generation"}\n')
        with self.assertRaises(ValueError):
            module.verified_acceptance_pack(self.round['acceptance_pack'], self.round, self.root)

    def test_pack_rejects_unknown_empty_or_unreadable_materials_before_writing(self):
        _, report_ref = self.generated_report()
        self.round['prerequisites']['total_report'] = report_ref
        valid = self.ref('nonempty-material.json', {'records': ['synthetic source']})
        empty = self.ref('empty-material.json', {})
        bad_json = self.root / 'unreadable-material.json'
        bad_json.write_text('not JSON')
        unreadable = module.reference(bad_json, self.root)
        cases = ({'role': 'unknown', 'description': 'unknown role', 'evidence': valid},
                 {'role': 'sources', 'description': '', 'evidence': valid},
                 {'role': 'sources', 'description': 'empty source', 'evidence': empty},
                 {'role': 'sources', 'description': 'bad JSON', 'evidence': unreadable})
        for index, item in enumerate(cases):
            with self.subTest(index=index):
                self.round['acceptance_materials'] = [item]
                out = self.root / ('rejected-pack-%d.json' % index)
                with self.assertRaises(ValueError):
                    module.acceptance_pack(self.round, out, self.root)
                self.assertFalse(out.exists())
                self.assertFalse(out.with_suffix('.md').exists())

    def test_pack_generator_preserves_an_existing_unsigned_sheet(self):
        _, report_ref = self.generated_report()
        self.round['prerequisites']['total_report'] = report_ref
        out = self.root / 'new-pack.json'
        sheet = out.with_suffix('.md')
        sheet.write_bytes(b'preserved original sheet\n')
        with self.assertRaises(FileExistsError):
            module.acceptance_pack(self.round, out, self.root)
        self.assertFalse(out.exists())
        self.assertEqual(sheet.read_bytes(), b'preserved original sheet\n')

    def test_final_freeze_requires_its_schema_and_passing_execution_status(self):
        for case in ('schema', 'passed'):
            with self.subTest(case=case):
                frozen = copy.deepcopy(self.freeze)
                if case == 'schema':
                    frozen['schema_version'] = 'not-a-source-freeze/1'
                else:
                    frozen['passed'] = False
                self.round['prerequisites']['source_freeze'] = self.ref(case + '-freeze.json', frozen)
                result = module.final_readonly(self.round, self.root / (case + '-final.json'), self.root)
                check = next(row for row in result['checks'] if row['stage'] == 'source_freeze')
                self.assertFalse(check['passed'])
                self.assertFalse(result['graph_integrity_complete'])
                self.assertFalse(result['technical_delivery_complete'])
                self.assertFalse(result['all_requested_delivery_complete'])

    def test_integral_graph_does_not_promote_an_incomplete_delivery(self):
        """Stub already-validated upstream gates only to isolate final result semantics."""
        raw = self.ref('stubbed-upstream.json', {'test_fixture': True})
        self.attack_execution_envelopes(raw)
        entries = self.freeze['entry_inputs']['entries']
        hashes = {key: record['sha256'] for key, record in entries.items()}
        activation_ref = self.ref('stubbed-activation.json', self.identity(
            'current-output-activation/1', 'entrypoint_activation', applied=True, passed=True,
            before_sha256=hashes, after_sha256=hashes, proposed_sha256=hashes,
            entry_files={key: {'path': record['path'], 'before_sha256': record['sha256'],
                               'after_sha256': record['sha256']} for key, record in entries.items()}))
        self.round['prerequisites']['entrypoint_activation'] = self.ref(
            'stubbed-activation-envelope.json', self.identity('stabilization-execution-stage/1',
                'entrypoint_activation', passed=True, evidence=activation_ref))
        report = self.forged_complete_report()
        report.update(stages=[{'stage': stage, 'status': 'pass', 'passed': True,
                               'evidence': self.round['prerequisites'][stage]}
                              for stage in module.STAGES[:6]],
                      technical_scope_complete=False, standard_capabilities_complete=False,
                      source_material_review_complete=False)
        report_ref = self.ref('stubbed-canonical-report.json', report)
        unfinished = ['uml-complete-design-time', 'bpmn-complete-design-time',
                      'independent-source-material-review', 'pending-signature-business-acceptance-pack']
        requirements = [{'id': row['stage'], 'passed': True, 'evidence': row['evidence']}
                        for row in report['stages']] + [{'id': name, 'passed': False, 'evidence': None}
                                                       for name in unfinished]
        ledger = self.identity('stabilization-ledger/1', 'ledger', total_report=report_ref,
                               requirements=requirements, technical_delivery_complete=False)
        ledger_ref = self.ref('stubbed-canonical-ledger.json', ledger)
        status = self.identity('stabilization-status/1', 'completion_status', ledger=ledger_ref,
                               technical_delivery_complete=False, all_requested_delivery_complete=False,
                               unfinished_requirements=unfinished)
        status_ref = self.ref('stubbed-canonical-status.json', status)
        self.round['prerequisites'].update(total_report=report_ref, ledger=ledger_ref,
                                           completion_status=status_ref)
        original_gate = module.verified_stage
        def admitted(ref, stage, round_data, root, replacements=None):
            if stage == 'source_freeze':
                return original_gate(ref, stage, round_data, root, replacements)
            return module.read_ref(ref, root)[1]
        with patch.object(module, 'verified_stage', side_effect=admitted), \
                patch.object(module, 'assess_report', return_value=report), \
                patch.object(module, 'build_ledger', return_value=ledger), \
                patch.object(module, 'build_status', return_value=status):
            result = module.final_readonly(self.round, self.root / 'graph-only-final.json', self.root)
        self.assertTrue(result['passed'])
        self.assertTrue(result['graph_integrity_complete'])
        self.assertFalse(result['technical_scope_complete'])
        self.assertFalse(result['technical_delivery_complete'])
        self.assertFalse(result['all_requested_delivery_complete'])
        self.assertEqual(result['unfinished_requirements'], unfinished)


if __name__ == '__main__':
    unittest.main()
