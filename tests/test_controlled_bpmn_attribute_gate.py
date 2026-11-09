"""Source-declared BPMN QName exception must not relax browser event rejection."""
import sys
from pathlib import Path
import unittest
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
from enterprise.local_render import validate_graphic

MODEL = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
XSD = 'http://www.w3.org/2001/XMLSchema'
SOURCES = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared/standards/sources/bpmn-2.0.2'


def graphic(attribute='oneBehaviorEventRef', tag='multiInstanceLoopCharacteristics', namespace=MODEL):
    root = ET.Element('{'+MODEL+'}definitions')
    ET.SubElement(root, '{'+namespace+'}'+tag, {attribute: 'localEvent'})
    return ET.tostring(root)


class ControlledBpmnAttributeGateTests(unittest.TestCase):
    def test_exact_exception_is_declared_by_official_local_schema(self):
        root = ET.parse(SOURCES / 'Semantic.xsd').getroot()
        role = root.find('./{'+XSD+'}complexType[@name="tMultiInstanceLoopCharacteristics"]')
        declaration = role.find('.//{'+XSD+'}attribute[@name="oneBehaviorEventRef"]')
        self.assertIsNotNone(declaration)
        self.assertEqual(declaration.attrib, {'name': 'oneBehaviorEventRef', 'type': 'xsd:QName', 'use': 'optional'})
        self.assertEqual(root.attrib.get('attributeFormDefault', 'unqualified'), 'unqualified')
        validate_graphic('bpmn', graphic())

    def test_case_namespace_and_lookalike_attributes_are_refused(self):
        for attribute in ('onebehavioreventref', 'OneBehaviorEventRef', 'oneBehaviorEventRefExtra',
                          '{'+MODEL+'}oneBehaviorEventRef', '{urn:foreign}oneBehaviorEventRef',
                          'onclick', 'onload', '{urn:foreign}onerror'):
            with self.subTest(attribute=attribute), self.assertRaisesRegex(ValueError, 'active attributes'):
                validate_graphic('bpmn', graphic(attribute))

    def test_exception_is_not_admitted_on_other_bpmn_or_foreign_elements(self):
        for tag, namespace in [('task', MODEL), ('definitions', MODEL),
                               ('multiInstanceLoopCharacteristics', 'urn:foreign')]:
            with self.subTest(tag=tag, namespace=namespace), self.assertRaisesRegex(ValueError, 'active attributes'):
                validate_graphic('bpmn', graphic(tag=tag, namespace=namespace))

    def test_svg_and_uml_keep_event_attribute_rejection(self):
        for kind, namespace, tag in [('svg', 'http://www.w3.org/2000/svg', 'svg'),
                                     ('uml-class-layout', 'http://www.omg.org/spec/UML/20131001', 'Model')]:
            root = ET.Element('{'+namespace+'}'+tag)
            ET.SubElement(root, '{'+MODEL+'}multiInstanceLoopCharacteristics', {'oneBehaviorEventRef': 'localEvent'})
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, 'active attributes'):
                validate_graphic(kind, ET.tostring(root))


if __name__ == '__main__':
    unittest.main()
