"""Independent XML graph/selector oracle for the prose-derived Lifeline rule."""
import copy
import os
from pathlib import Path
import sys
import unittest
from lxml import etree

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
from uml_backend import validate_mapped, official_rules, execution_rules, LIFELINE_RULE
from standards import sha

XMI = '{http://www.omg.org/spec/XMI/20131001}'
UML = 'http://www.omg.org/spec/UML/20131001'


def fixtures():
    root = etree.Element('{'+UML+'}Model', nsmap={'uml': UML, 'xmi': XMI[1:-1]})
    root.set(XMI+'id', 'M'); root.set('name', 'Independent lifeline cases')
    def add(parent, tag, kind, identity, **attrs):
        child = etree.SubElement(parent, tag); child.set(XMI+'id', identity); child.set(XMI+'type', 'uml:'+kind)
        for key, value in attrs.items(): child.set(key, str(value))
        return child
    def selector(owner, identity, value):
        if value is not None: add(owner, 'selector', 'Literal'+value[0], identity, value=value[1])
    # Every row declares an enclosing, two referred interactions and their
    # lifelines. The expected answer is derived solely from XML containment and
    # declared represents/selector values by the oracle below.
    cases = [
        ('absent-match', None, None, None, 'same', True, False),
        ('absent-missing', None, None, None, 'same', False, False),
        ('different-represents', None, None, None, 'different', False, False),
        ('string-match', ('String', 'east'), ('String', 'east'), ('String', 'east'), 'same', True, False),
        ('string-wrong-outer', ('String', 'east'), ('String', 'east'), ('String', 'west'), 'same', True, False),
        ('string-different-peer', ('String', 'east'), ('String', 'west'), None, 'same', False, False),
        ('integer-match', ('Integer', '2'), ('Integer', '2'), ('Integer', '2'), 'same', True, False),
        ('integer-wrong-outer', ('Integer', '2'), ('Integer', '2'), ('Integer', '3'), 'same', True, False),
        ('selector-types-differ', ('String', '2'), ('Integer', '2'), None, 'same', False, False),
        ('wrong-outer-represents', None, None, None, 'outer-different', True, False),
        ('absent-vs-peer-selector', None, ('String', 'east'), None, 'same', False, False),
        ('absent-vs-outer-selector', None, None, ('String', 'east'), 'same', True, False),
        ('nested-match', ('Integer', '4'), ('Integer', '4'), ('Integer', '4'), 'same', True, True),
        ('nested-missing', ('Integer', '4'), ('Integer', '4'), None, 'same', False, True),
    ]
    for name, own_selector, peer_selector, outer_selector, mode, outer_present, nested in cases:
        prefix = name.replace('-', '_')
        owner = add(root, 'packagedElement', 'Class', prefix+'_OWNER', name=prefix)
        add(owner, 'ownedAttribute', 'Property', prefix+'_P', name='part')
        add(owner, 'ownedAttribute', 'Property', prefix+'_Q', name='other')
        first = add(owner, 'ownedBehavior', 'Interaction', prefix+'_FIRST', name='first')
        second = add(owner, 'ownedBehavior', 'Interaction', prefix+'_SECOND', name='second')
        outer = add(owner, 'ownedBehavior', 'Interaction', prefix+'_OUTER', name='outer')
        a = add(first, 'lifeline', 'Lifeline', prefix+'_A', name='a', represents=prefix+'_P')
        b = add(second, 'lifeline', 'Lifeline', prefix+'_B', name='b', represents=prefix+('_Q' if mode=='different' else '_P'))
        selector(a, prefix+'_SA', own_selector); selector(b, prefix+'_SB', peer_selector)
        if outer_present:
            enclosing = add(outer, 'lifeline', 'Lifeline', prefix+'_ENC', name='enclosing',
                            represents=prefix+('_Q' if mode=='outer-different' else '_P'))
            selector(enclosing, prefix+'_SE', outer_selector)
        container = outer
        if nested:
            fragment = add(outer, 'fragment', 'CombinedFragment', prefix+'_CF', interactionOperator='seq')
            container = add(fragment, 'operand', 'InteractionOperand', prefix+'_OP')
            nested_fragment = add(container, 'fragment', 'CombinedFragment', prefix+'_CF2', interactionOperator='seq')
            container = add(nested_fragment, 'operand', 'InteractionOperand', prefix+'_OP2')
        add(container, 'fragment', 'InteractionUse', prefix+'_USE_A', refersTo=prefix+'_FIRST')
        add(container, 'fragment', 'InteractionUse', prefix+'_USE_B', refersTo=prefix+'_SECOND')
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8')


def xml_oracle(data):
    """No OCL/metamodel queries: use XML ancestors and explicit value keys."""
    root = etree.fromstring(data)
    objects = {element.get(XMI+'id'): element for element in root.iter() if element.get(XMI+'id')}
    def kind(element): return element.get(XMI+'type', '').split(':')[-1]
    def interaction(element):
        while element is not None:
            if kind(element) == 'Interaction': return element
            element = element.getparent()
        return None
    def key(lifeline):
        selected = lifeline.find('selector')
        value = None if selected is None else (kind(selected), selected.get('value'))
        return lifeline.get('represents'), value
    uses = [element for element in root.iter() if kind(element) == 'InteractionUse']
    result = {}
    for identity, lifeline in objects.items():
        if kind(lifeline) != 'Lifeline': continue
        owner = interaction(lifeline); satisfied = True
        for use in uses:
            if use.get('refersTo') != owner.get(XMI+'id'): continue
            enclosing = interaction(use)
            for peer_use in uses:
                if peer_use is use or interaction(peer_use) is not enclosing: continue
                referred = objects[peer_use.get('refersTo')]
                peers = referred.findall('lifeline')
                if any(key(peer) == key(lifeline) for peer in peers):
                    satisfied &= any(key(candidate) == key(lifeline) for candidate in enclosing.findall('lifeline'))
        result[identity] = satisfied
    return result


class LifelineSourceTests(unittest.TestCase):
    def test_normative_body_is_retained_and_execution_basis_is_explicit(self):
        original, _ = official_rules(); before = copy.deepcopy(original)
        executed, adapters = execution_rules(original)
        self.assertEqual(before, original)
        adapter = next(item for item in adapters if item['id'] == LIFELINE_RULE)
        self.assertEqual('normative-prose-semantic-adapter', adapter['kind'])
        self.assertEqual([664,665], adapter['basis']['pdf_pages'])
        self.assertEqual([622,623], adapter['basis']['printed_pages'])
        self.assertEqual('pending', adapter['human_acceptance'])
        self.assertFalse(adapter['official_full_conformance'])
        self.assertEqual(sha(adapter['original_body'].encode()), adapter['original_body_sha256'])
        self.assertIn('->exists(enclosing : Lifeline', next(item['body'] for item in executed if item['id'] == LIFELINE_RULE))


@unittest.skipUnless(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME',''))/'bin/java').is_file(),
                     'set existing JAVA_HOME to execute Lifeline OCL')
class ActualLifelineOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = fixtures(); cls.expected = xml_oracle(cls.data); cls.report = validate_mapped(cls.data)
        cls.rule = next(row for row in cls.report['ocl_rules'] if row['id'] == LIFELINE_RULE)

    def test_every_lifeline_matches_independent_graph_and_selector_oracle(self):
        self.assertEqual('parsed', self.rule['parse_status'], self.rule['parse_error'])
        self.assertEqual(len(self.expected), self.rule['applicable'])
        self.assertEqual(0, self.rule['invalid_evaluations']); self.assertEqual(0, self.rule['null_evaluations'])
        self.assertEqual({identity for identity, satisfied in self.expected.items() if not satisfied},
                         set(self.rule['violation_ids']))

    def test_positive_negative_selector_and_represents_cases_are_present(self):
        outcomes = {row['id']: row['value_kind'] for row in self.rule['evaluation_outcomes']}
        for prefix in ('absent_match', 'string_match', 'integer_match', 'nested_match',
                       'different_represents', 'string_different_peer', 'selector_types_differ', 'absent_vs_peer_selector'):
            self.assertEqual('true', outcomes[prefix+'_A'])
        for prefix in ('absent_missing', 'string_wrong_outer', 'integer_wrong_outer',
                       'wrong_outer_represents', 'absent_vs_outer_selector', 'nested_missing'):
            self.assertEqual('false', outcomes[prefix+'_A'])


if __name__ == '__main__': unittest.main()
