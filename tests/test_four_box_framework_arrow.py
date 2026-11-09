"""Visible framework arrows must remain distinct from numbered model relations."""
import copy
import json
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from profile_examples import normalize_example
from profile_render import render_profile
from registry import load


def inspect_connector(svg):
    root = ET.fromstring(svg)
    cards, text_bottom, relations, polygons, extra_marker_lines = {}, {}, {}, [], []
    issues, leader_relationship_ids = [], set()
    for node in root.iter():
        tag = node.tag.rsplit('}', 1)[-1]
        if tag == 'g' and node.get('data-entity-id'):
            ident = node.get('data-entity-id')
            rect = next(child for child in node if child.tag.endswith('rect'))
            cards[ident] = tuple(float(rect.get(k)) for k in ('x', 'y', 'width', 'height'))
            text_bottom[ident] = max(float(child.get('y')) for child in node if child.tag.endswith('text'))
        if tag == 'path':
            leader = node.get('data-annotation-leader')
            ident = node.get('data-relationship-id')
            if leader not in (None, 'true'):
                issues.append('invalid-annotation-leader-value')
            if leader == 'true':
                if node.get('marker-start') or node.get('marker-end'):
                    issues.append('annotation-leader-has-business-arrow')
                if ident:
                    leader_relationship_ids.add(ident)
            elif ident:
                if ident in relations:
                    issues.append('duplicate-business-relationship-path')
                relations[ident] = node.attrib
                if node.get('marker-end') != 'url(#arrow)':
                    issues.append('missing-business-relationship-arrow')
        if tag == 'path' and node.get('marker-start') and not node.get('data-relationship-id'):
            extra_marker_lines.append(node.attrib)
        if tag == 'polygon':
            nums = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', node.get('points', ''))]
            polygons.append((node, list(zip(nums[::2], nums[1::2]))))
    rid, pid = 'four-box-business-model-default-2', 'four-box-business-model-default-3'
    resource, process = cards[rid], cards[pid]
    x1, x2, y = resource[0] + resource[2] - 30, process[0] + 30, resource[1] + resource[3] - 22
    near = lambda a, b: abs(a[0] - b[0]) < .11 and abs(a[1] - b[1]) < .11
    fixed = [(node, pts) for node, pts in polygons
             if any(near(p, (x1, y)) for p in pts) and any(near(p, (x2, y)) for p in pts)]
    if leader_relationship_ids - relations.keys():
        issues.append('annotation-leader-without-business-relationship')
    if extra_marker_lines:
        issues.append('unnumbered-model-marker-line')
    if len(fixed) != 1:
        issues.append('missing-distinct-framework-connector')
    else:
        node, points = fixed[0]
        if node.get('fill') != '#d3d6da' or node.get('stroke') != '#9aa0a6':
            issues.append('framework-legend-style-mismatch')
        for tip in [(x1, y), (x2, y)]:
            if sum(near(point, tip) for point in points) != 1:
                issues.append('missing-unique-outward-tip')
        if not all(x1 - .11 <= p[0] <= x2 + .11 for p in points):
            issues.append('tip-geometry-not-inward')
        if min(p[1] for p in points) <= max(text_bottom[rid], text_bottom[pid]) + 4:
            issues.append('framework-arrow-overlaps-text')
        if max(p[1] for p in points) >= min(resource[1] + resource[3], process[1] + process[3]):
            issues.append('framework-arrow-crosses-card-bottom')
    return issues, cards, relations, fixed, root


class FourBoxFrameworkArrowTests(unittest.TestCase):
    def test_framework_and_model_relations_in_all_four_variants(self):
        profile = load()[2]['four-box-business-model-default']
        for layout in ('reference', 'adaptive'):
            for modified in (False, True):
                with self.subTest(layout=layout, modified=modified):
                    model = normalize_example(profile)
                    if modified:
                        model['entities'][0]['attributes']['detail'] = 'VERIFY-four-box'
                    before = json.dumps(model, sort_keys=True)
                    svg, coverage = render_profile(model, model['views'][0], profile, layout)
                    issues, cards, relations, _, _ = inspect_connector(svg)
                    self.assertEqual([], issues)
                    self.assertEqual(before, json.dumps(model, sort_keys=True))
                    self.assertEqual({e['id'] for e in model['entities']}, set(cards))
                    self.assertEqual({r['id'] for r in model['relationships']}, set(relations))
                    self.assertEqual([], coverage['errors'])
                    self.assertEqual([], coverage['unrepresented_relationship_ids'])
                    self.assertTrue(all(r.get('marker-end') == 'url(#arrow)' for r in relations.values()))
                    self.assertEqual(int(modified), svg.count('VERIFY-four-box'))

    def test_oracle_rejects_blue_missing_and_one_sided_framework_arrows(self):
        profile = load()[2]['four-box-business-model-default']
        model = normalize_example(profile)
        svg, _ = render_profile(model, model['views'][0], profile, 'adaptive')
        issues, _, _, fixed, _ = inspect_connector(svg)
        self.assertEqual([], issues)
        for mutation in ('blue', 'missing', 'one-sided'):
            root = ET.fromstring(svg)
            original = fixed[0][0]
            target = next(n for n in root.iter() if n.tag.endswith('polygon') and n.get('points') == original.get('points'))
            if mutation == 'blue':
                target.set('fill', '#46647e')
            elif mutation == 'missing':
                next(n for n in root.iter() if target in list(n)).remove(target)
            else:
                points = target.get('points').split()
                points[0] = points[1]
                target.set('points', ' '.join(points))
            self.assertTrue(inspect_connector(ET.tostring(root, encoding='unicode'))[0], mutation)

    def test_same_id_annotation_leader_keeps_business_arrow_in_either_order(self):
        profile = load()[2]['four-box-business-model-default']
        model = normalize_example(profile)
        svg, _ = render_profile(model, model['views'][0], profile, 'adaptive')
        for leader_first in (False, True):
            with self.subTest(leader_first=leader_first):
                root = ET.fromstring(svg)
                leader = next(n for n in root.iter() if n.get('data-annotation-leader') == 'true')
                ident = leader.get('data-relationship-id')
                business = next(n for n in root.iter() if n.tag.endswith('path')
                                and n.get('data-relationship-id') == ident
                                and n.get('data-annotation-leader') is None)
                before = dict(business.attrib)
                parent = next(n for n in root.iter() if leader in list(n))
                parent.remove(leader)
                parent.insert(0 if leader_first else len(parent), leader)
                issues, _, relations, _, _ = inspect_connector(ET.tostring(root, encoding='unicode'))
                self.assertEqual([], issues)
                self.assertEqual(before, relations[ident])
                self.assertEqual({r['id'] for r in model['relationships']}, set(relations))
                self.assertTrue(all(r.get('marker-end') == 'url(#arrow)' for r in relations.values()))

    def test_oracle_rejects_missing_business_arrows_and_mislabeled_business_paths(self):
        profile = load()[2]['four-box-business-model-default']
        model = normalize_example(profile)
        svg, _ = render_profile(model, model['views'][0], profile, 'adaptive')
        for mutation, expected in (
                ('missing-arrow', 'missing-business-relationship-arrow'),
                ('business-marked-as-leader', 'annotation-leader-has-business-arrow'),
                ('missing-business-path', 'annotation-leader-without-business-relationship'),
                ('duplicate-business-path', 'duplicate-business-relationship-path')):
            with self.subTest(mutation=mutation):
                root = ET.fromstring(svg)
                leader = next(n for n in root.iter() if n.get('data-annotation-leader') == 'true')
                business = next(n for n in root.iter() if n.tag.endswith('path')
                                and n.get('data-relationship-id') == leader.get('data-relationship-id')
                                and n.get('data-annotation-leader') is None)
                parent = next(n for n in root.iter() if business in list(n))
                if mutation == 'missing-arrow':
                    del business.attrib['marker-end']
                elif mutation == 'business-marked-as-leader':
                    business.set('data-annotation-leader', 'true')
                elif mutation == 'missing-business-path':
                    parent.remove(business)
                else:
                    parent.append(copy.deepcopy(business))
                issues, _, relations, _, _ = inspect_connector(ET.tostring(root, encoding='unicode'))
                self.assertIn(expected, issues)
                if mutation in ('business-marked-as-leader', 'missing-business-path'):
                    self.assertNotEqual({r['id'] for r in model['relationships']}, set(relations))

    def test_oracle_rejects_illegal_annotation_leader_values(self):
        profile = load()[2]['four-box-business-model-default']
        model = normalize_example(profile)
        svg, _ = render_profile(model, model['views'][0], profile, 'adaptive')
        for value in ('false', 'TRUE', '', '1', 'null'):
            with self.subTest(value=value):
                root = ET.fromstring(svg)
                business = next(n for n in root.iter() if n.tag.endswith('path')
                                and n.get('data-relationship-id')
                                and n.get('data-annotation-leader') is None)
                business.set('data-annotation-leader', value)
                issues, _, relations, _, _ = inspect_connector(ET.tostring(root, encoding='unicode'))
                self.assertIn('invalid-annotation-leader-value', issues)
                self.assertEqual({r['id'] for r in model['relationships']}, set(relations))


if __name__ == '__main__':
    unittest.main()
