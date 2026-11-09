"""Independent source-derived Standard Profile positives and application defects."""
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from standards import SOURCES, safe_xml
from uml_profiles import catalog, check

URI='http://www.omg.org/spec/UML/20161101/StandardProfile'


def fixture(stereotype='Auxiliary',field='base_Class',metaclass='Class',applied=True,extra=''):
    application=('<profileApplication xmi:type="uml:ProfileApplication" xmi:id="PA">'
                 '<appliedProfile href="'+URI+'.xmi#_0"/></profileApplication>') if applied else ''
    return ('<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001" '
            'xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:StandardProfile="'+URI+'">'
            '<uml:Model xmi:id="M" name="Model">'+application+
            '<packagedElement xmi:type="uml:'+metaclass+'" xmi:id="B" name="Base"/>'
            '<packagedElement xmi:type="uml:Class" xmi:id="OTHER" name="Other"/>'
            '</uml:Model><StandardProfile:'+stereotype+' xmi:id="ST" '+field+'="B" '+extra+'/></xmi:XMI>').encode()


class StandardProfileTests(unittest.TestCase):
    def test_all_official_stereotypes_and_each_extension_base_are_checked(self):
        source=catalog();self.assertEqual(33,source['stereotype_count'])
        for name,spec in source['stereotypes'].items():
            for field,base in spec['bases'].items():
                with self.subTest(stereotype=name,field=field):
                    result=check(safe_xml(fixture(name,field,base['type'])))
                    self.assertEqual([],result['findings'])
                    self.assertEqual(name,result['applications'][0]['stereotype'])
                    self.assertEqual(base['source_id'],result['applications'][0]['source']['id'])
                    self.assertFalse(result['full_profile_design_time_conformance'])
        self.assertIn('base_Artifact',source['stereotypes']['Document']['bases'])

    def test_extended_metaclass_subtype_is_valid(self):
        result=check(safe_xml(fixture('Create','base_BehavioralFeature','Operation')))
        self.assertEqual([],result['findings']);self.assertEqual('Operation',result['applications'][0]['base_metaclass'])

    def test_wrong_dangling_and_missing_base_are_invalid(self):
        variants=[(fixture(metaclass='PrimitiveType'),'StandardProfile-base-metaclass'),
                  (fixture().replace(b'base_Class="B"',b'base_Class="MISSING"'),'StandardProfile-base-exists'),
                  (fixture().replace(b'base_Class="B"',b''),'Stereotype-one-base-instance')]
        for raw,rule in variants:
            with self.subTest(rule=rule):
                result=check(safe_xml(raw))
                self.assertIn(rule,[f['rule_id'] for f in result['findings']]);self.assertFalse(result['applications'])

    def test_multiple_extended_metaclasses_cannot_attach_one_instance_twice(self):
        result=check(safe_xml(fixture('Create','base_Usage','Usage',extra='base_BehavioralFeature="OTHER"')))
        self.assertIn('Stereotype-one-base-instance',[f['rule_id'] for f in result['findings']])

    def test_standard_profile_must_be_applied_to_containing_package(self):
        result=check(safe_xml(fixture(applied=False)))
        self.assertIn('StandardProfile-applied-to-package',[f['rule_id'] for f in result['findings']])
        root=safe_xml(fixture());model=root[0];base=model.find('packagedElement')
        nested=etree.Element('packagedElement',{'{http://www.omg.org/spec/XMI/20131001}type':'uml:Package',
                                             '{http://www.omg.org/spec/XMI/20131001}id':'P','name':'Nested'})
        model.remove(base);nested.append(base);model.append(nested)
        self.assertEqual([],check(root)['findings'])

    def test_unknown_standard_stereotypes_properties_and_custom_profile_are_distinct(self):
        for raw,rule in [(fixture('NotAStandardStereotype'),'StandardProfile-stereotype-exists'),
                         (fixture(extra='invented="value"'),'StandardProfile-property-exists')]:
            self.assertIn(rule,[f['rule_id'] for f in check(safe_xml(raw))['findings']])
        raw=fixture().replace((URI+'.xmi#_0').encode(),b'custom.profile.uml#P')
        result=check(safe_xml(raw));self.assertTrue(result['capability_uncovered'])
        self.assertIn('StandardProfile-applied-to-package',[f['rule_id'] for f in result['findings']])

    def test_profile_references_are_package_local_and_fingerprint_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)/'package';base.mkdir();other=Path(tmp)/'other';other.mkdir()
            official=(SOURCES/'uml-2.5.1/StandardProfile.xmi').read_bytes()
            (base/'StandardProfile.xmi').write_bytes(official)
            raw=fixture().replace((URI+'.xmi#_0').encode(),b'StandardProfile.xmi#_0')
            self.assertEqual([],check(safe_xml(raw),base)['findings'])
            (base/'StandardProfile.xmi').write_bytes(official.replace(b'name="Auxiliary"',b'name="Altered"'))
            self.assertIn('StandardProfile-source-fingerprint',[f['rule_id'] for f in check(safe_xml(raw),base)['findings']])
            (other/'StandardProfile.xmi').write_bytes(official)
            escaped=raw.replace(b'href="StandardProfile.xmi#_0"',b'href="../other/StandardProfile.xmi#_0"')
            self.assertIn('StandardProfile-local-reference',[f['rule_id'] for f in check(safe_xml(escaped),base)['findings']])
            (base/'StandardProfile.xmi').unlink();(base/'StandardProfile.xmi').symlink_to(other/'StandardProfile.xmi')
            self.assertIn('StandardProfile-local-reference',[f['rule_id'] for f in check(safe_xml(raw),base)['findings']])

    def test_standard_application_payload_and_model_are_never_rewritten(self):
        root=safe_xml(fixture());before=etree.tostring(root)
        check(root);self.assertEqual(before,etree.tostring(root))
        self.assertFalse(check(root)['external_resources_loaded'])


if __name__=='__main__':unittest.main()
