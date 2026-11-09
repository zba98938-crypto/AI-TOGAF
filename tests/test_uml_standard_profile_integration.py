"""Public catalog/exchange diagnostics for official versus opaque Profiles."""
import sys
import unittest
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import catalog, check_native, make_package, package_bytes, Invalid
from test_uml_standard_profile import fixture, URI
from uml_profiles import catalog as profile_catalog, check as check_profile
from standards import safe_xml


class StandardProfileIntegrationTests(unittest.TestCase):
    def test_invalid_profile_notation_is_rejected_before_svg_generation(self):
        from uml_render import diagram_model
        for stereotype,field,metaclass in (('Utility','base_Class','Class'),
                                           ('Create','base_BehavioralFeature','Operation'),
                                           ('Framework','base_Package','Package')):
            for data,rule in ((fixture(stereotype,field,metaclass,extra='invented="value"'),'StandardProfile-property-exists'),
                              (fixture(stereotype,field,'Generalization'),'StandardProfile-base-metaclass')):
                with self.subTest(stereotype=stereotype,rule=rule),self.assertRaisesRegex(Invalid,rule):diagram_model(data)

    def test_every_official_extension_rejects_incompatible_dangling_and_multiple_bases(self):
        for name, spec in profile_catalog()['stereotypes'].items():
            for field, base in spec['bases'].items():
                wrong=fixture(name,field,'Generalization')
                missing=fixture(name,field,base['type']).replace((field+'="B"').encode(),(field+'="MISSING"').encode())
                multiple=fixture(name,field,base['type']).replace((field+'="B"').encode(),(field+'="B OTHER"').encode())
                for raw, rule in ((wrong,'StandardProfile-base-metaclass'),
                                  (missing,'StandardProfile-base-exists'),
                                  (multiple,'Stereotype-one-base-instance')):
                    with self.subTest(stereotype=name,field=field,rule=rule):
                        result=check_profile(safe_xml(raw))
                        self.assertTrue(any(row['rule_id']==rule for row in result['findings']))
                        self.assertEqual([],result['applications'])

    def test_public_exchange_preserves_source_and_reports_verified_official_references(self):
        data=fixture();report=check_native(data,'uml','2.5.1')
        self.assertEqual([],report['errors'])
        self.assertEqual([],report['vendor_namespaces'])
        self.assertEqual([URI+'.xmi#_0'],report['standard_profile_validation']['verified_profile_references'])
        self.assertFalse(any(URI+'.xmi#_0' in row for row in report['blockers']))
        self.assertEqual('incomplete',report['conformance_status'])
        package=make_package(data,'uml','2.5.1')
        self.assertEqual(data,package_bytes(package,'uml','2.5.1'))
        result=catalog('uml','2.5.1')
        self.assertEqual(33,result['standard_profile']['stereotype_count'])
        self.assertFalse(result['standard_profile']['full_profile_design_time_conformance'])

    def test_official_profile_validation_errors_are_distinct_from_custom_capability(self):
        report=check_native(fixture(extra='invented="value"'),'uml','2.5.1')
        self.assertTrue(any('StandardProfile-property-exists' in row for row in report['diagnostic_groups']['validation_errors']))
        custom=fixture().replace(URI.encode(),b'http://example.invalid/custom')
        report=check_native(custom,'uml','2.5.1')
        self.assertEqual([],report['errors'])
        self.assertEqual(['http://example.invalid/custom'],report['vendor_namespaces'])
        self.assertTrue(report['diagnostic_groups']['capability_uncovered'])
        self.assertFalse(report['standard_profile_validation']['external_resources_loaded'])

    def test_unverified_remote_and_missing_local_profile_remain_blocked(self):
        unknown=fixture().replace((URI+'.xmi#_0').encode(),b'https://example.invalid/StandardProfile.xmi#_0')
        report=check_native(unknown,'uml','2.5.1')
        self.assertEqual([],report['standard_profile_validation']['verified_profile_references'])
        self.assertTrue(any('external reference is retained but never fetched' in row for row in report['blockers']))
        local=fixture().replace((URI+'.xmi#_0').encode(),b'StandardProfile.xmi#_0')
        report=check_native(local,'uml','2.5.1')
        self.assertTrue(report['diagnostic_groups']['missing_material'])
        self.assertFalse(report['standard_profile_validation']['external_resources_loaded'])


if __name__=='__main__':unittest.main()
