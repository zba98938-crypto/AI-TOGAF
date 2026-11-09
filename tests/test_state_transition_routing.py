"""Independent lifecycle edge tracing catches shared ports and T-junctions."""
import copy
import json
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from profile_render import render_profile


def lifecycle():
    entities = [
        {'id': 'data-active', 'type': 'data_state', 'name': '活动数据', 'attributes': {'retention': '业务处理中', 'owner': '数据负责人', 'entry': '订单创建', 'exit': '交易完成'}},
        {'id': 'data-archive', 'type': 'data_state', 'name': '归档数据', 'attributes': {'retention': '政策规定窗口', 'owner': '数据负责人', 'entry': '交易完成', 'exit': '允许销毁'}},
        {'id': 'data-destroyed', 'type': 'data_state', 'name': '已销毁', 'attributes': {'retention': '不再保留内容', 'owner': '数据负责人', 'entry': '到期且无法律保留', 'exit': '终态'}},
    ]
    relationships = [
        {'id': 'data-archive-edge', 'type': 'transitions_to', 'source': 'data-active', 'target': 'data-archive', 'label': '交易结束归档'},
        {'id': 'data-destroy-edge', 'type': 'transitions_to', 'source': 'data-archive', 'target': 'data-destroyed', 'label': '到期且无保留义务后销毁'},
    ]
    model = {'entities': entities, 'relationships': relationships}
    view = {'id': 'lifecycle', 'title': '生命周期', 'entity_ids': [e['id'] for e in entities], 'relationship_ids': [r['id'] for r in relationships]}
    return model, view, {'id': 'lifecycle', 'renderer': 'state'}


def traced_svg(svg):
    root = ET.fromstring(svg)
    boxes = {}
    paths = {}
    for node in root.iter():
        if node.get('data-entity-id'):
            rectangle = next(child for child in node if child.tag.endswith('rect'))
            boxes[node.get('data-entity-id')] = tuple(float(rectangle.get(k)) for k in ('x', 'y', 'width', 'height'))
        if node.tag.endswith('path') and node.get('data-relationship-id'):
            values = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', node.get('d'))]
            paths[node.get('data-relationship-id')] = list(zip(values[::2], values[1::2]))
            assert node.get('marker-end') == 'url(#arrow)'
    return root, boxes, paths


def on_boundary(point, box):
    x, y, w, h = box
    return ((point[0] in (x, x + w) and y <= point[1] <= y + h)
            or (point[1] in (y, y + h) and x <= point[0] <= x + w))


def intersects(segment_a, segment_b):
    """Inclusive intersection detects both shared segments and branch junctions."""
    a, b = segment_a
    c, d = segment_b
    if a[1] == b[1] and c[1] == d[1]:
        return a[1] == c[1] and max(min(a[0], b[0]), min(c[0], d[0])) <= min(max(a[0], b[0]), max(c[0], d[0]))
    if a[0] == b[0] and c[0] == d[0]:
        return a[0] == c[0] and max(min(a[1], b[1]), min(c[1], d[1])) <= min(max(a[1], b[1]), max(c[1], d[1]))
    if a[0] == b[0]:
        a, b, c, d = c, d, a, b
    return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(c[1], d[1]) <= a[1] <= max(c[1], d[1])


class StateTransitionRoutingTests(unittest.TestCase):
    def assert_independent_transitions(self, model, view, profile, layout):
        before = json.dumps(model, ensure_ascii=False, sort_keys=True)
        svg, coverage = render_profile(model, view, profile, layout)
        root, boxes, paths = traced_svg(svg)
        self.assertEqual(before, json.dumps(model, ensure_ascii=False, sort_keys=True))
        self.assertEqual([], coverage['errors'])
        self.assertEqual([], coverage['unrepresented_relationship_ids'])
        self.assertEqual({'data-active', 'data-archive', 'data-destroyed'}, set(boxes))
        self.assertEqual({'data-archive-edge', 'data-destroy-edge'}, set(paths))
        for relation in model['relationships']:
            points = paths[relation['id']]
            self.assertTrue(on_boundary(points[0], boxes[relation['source']]))
            self.assertTrue(on_boundary(points[-1], boxes[relation['target']]))
            self.assertTrue(all(a[0] == b[0] or a[1] == b[1] for a, b in zip(points, points[1:])))
        incoming = paths['data-archive-edge']
        outgoing = paths['data-destroy-edge']
        self.assertNotEqual(incoming[-1], outgoing[0], 'Archive entry and exit must have independent ports')
        self.assertFalse(any(intersects(a, b) for a in zip(incoming, incoming[1:]) for b in zip(outgoing, outgoing[1:])), 'Sequential transitions must not form a shared segment or T-junction')
        self.assertFalse(any(node.tag.endswith('circle') for node in root.iter()), 'No initial/final flags were declared')
        return svg, paths

    def test_original_and_modified_lifecycle_have_independent_ports(self):
        for layout in ('reference', 'adaptive'):
            for modified in (False, True):
                with self.subTest(layout=layout, modified=modified):
                    model, view, profile = lifecycle()
                    if modified:
                        model['entities'][0]['attributes']['owner'] = 'VERIFYfabd6af6'
                    svg, paths = self.assert_independent_transitions(model, view, profile, layout)
                    self.assertEqual(int(modified), svg.count('VERIFYfabd6af6'))
                    if layout == 'reference':
                        self.assertTrue(all(len(points) == 2 for points in paths.values()), 'Reference chain retains two direct horizontal arrows')

    def test_reversed_edge_registration_does_not_create_a_branch(self):
        model, view, profile = lifecycle()
        model['relationships'].reverse()
        view['relationship_ids'].reverse()
        self.assert_independent_transitions(model, view, profile, 'adaptive')


if __name__ == '__main__':
    unittest.main()
