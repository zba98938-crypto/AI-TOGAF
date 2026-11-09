"""A late white relationship label must leave SVG arrow strokes visible."""
import copy
import math
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from registry import load
from verify_artifact_profiles import inputs, substantive_change
from profile_render import render_profile


def intersects(p, q, box):
    left, top, right, bottom = box
    dx, dy = q[0] - p[0], q[1] - p[1]
    low, high = 0., 1.
    for denominator, numerator in ((-dx, p[0]-left), (dx, right-p[0]),
                                   (-dy, p[1]-top), (dy, bottom-p[1])):
        if abs(denominator) < 1e-9:
            if numerator < 0:return False
        else:
            ratio = numerator / denominator
            if denominator < 0:low = max(low, ratio)
            else:high = min(high, ratio)
            if low > high:return False
    return True


def covered_arrowheads(svg):
    root = ET.fromstring(svg)
    rows = list(root.iter())
    markers = {e.get('id'): e for e in rows if e.tag.endswith('}marker')}
    badges, arrows = [], []
    for index, e in enumerate(rows):
        if e.tag.endswith('}rect') and e.get('fill') == 'white' and e.get('stroke') == 'none':
            x,y,w,h = (float(e.get(k)) for k in ('x','y','width','height'))
            badges.append((index,(x,y,x+w,y+h)))
        if not e.tag.endswith('}path') or not e.get('marker-end'):continue
        marker = markers[e.get('marker-end')[5:-1]]
        coordinates = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', e.get('d'))]
        points = list(zip(coordinates[::2],coordinates[1::2]))
        endpoint, prior = points[-1], points[-2]
        vx,vy = endpoint[0]-prior[0],endpoint[1]-prior[1]
        length = math.hypot(vx,vy)
        ux,uy = vx/length,vy/length
        scale = float(e.get('stroke-width','1')) if marker.get('markerUnits','strokeWidth') == 'strokeWidth' else 1
        geometry = next(c for c in marker if c.tag.endswith('}path'))
        nums = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', geometry.get('d'))]
        vertices=[]
        for mx,my in zip(nums[::2],nums[1::2]):
            mx=(mx-float(marker.get('refX','0')))*scale
            my=(my-float(marker.get('refY','0')))*scale
            vertices.append((endpoint[0]+mx*ux-my*uy,endpoint[1]+mx*uy+my*ux))
        arrows.append((index,e.get('data-relationship-id'),vertices,scale*float(geometry.get('stroke-width','1'))/2))
    return [(rid,box) for index,rid,vertices,padding in arrows for later,box in badges
            if later > index and any(intersects(p,q,(box[0]-padding,box[1]-padding,box[2]+padding,box[3]+padding))
                                     for p,q in zip(vertices,vertices[1:]))]


class ArrowLabelClearanceTests(unittest.TestCase):
    def check_profiles(self, names):
        profiles=load()[2]
        for name in names:
            profile=profiles[name]
            for layout in ('reference','adaptive'):
                for modified in (False,True):
                    with self.subTest(profile=name,layout=layout,modified=modified):
                        model,view=inputs(profile)
                        if modified:substantive_change(model,view)
                        original=copy.deepcopy(model)
                        svg,coverage=render_profile(model,view,profile,layout)
                        self.assertEqual([],covered_arrowheads(svg))
                        self.assertEqual(original,model)
                        self.assertEqual([],coverage['errors'])
                        self.assertEqual([],coverage['unrepresented_relationship_ids'])

    def test_confirmed_short_upward_dependencies(self):
        self.check_profiles(('ea-team-capacity-plan-default','architecture-development-plan-default'))

    def test_later_labels_leave_earlier_arrowheads_visible(self):
        self.check_profiles(('metadata-inference-structure','value-stream-definition','value-stream-enabling-capabilities'))

    def test_geometric_oracle_rejects_the_original_occlusion(self):
        profile=load()[2]['ea-team-capacity-plan-default']
        model,view=inputs(profile)
        svg,_=render_profile(model,view,profile,'reference')
        self.assertEqual([],covered_arrowheads(svg))
        root=ET.fromstring(svg)
        badge=next(e for e in root.iter() if e.tag.endswith('}rect') and e.get('fill') == 'white' and e.get('stroke') == 'none')
        badge.set('x','177.5');badge.set('y','461.0')
        self.assertTrue(covered_arrowheads(ET.tostring(root,encoding='unicode')))


if __name__ == '__main__':unittest.main()
