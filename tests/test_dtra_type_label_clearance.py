"""Actual glyph ink of DTRA captions must clear its trend indicator."""
import copy
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from annotation_geometry_oracle import expanded, path_points, segment_box, tag, text_box
from registry import load
from verify_artifact_profiles import inputs, express, substantive_change

class DtraTypeLabelClearanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = load()[2]['dtra-factor-progression']
        font = TTFont(SHARED / 'assets/fonts/NotoSansSC.ttf')
        cls.font = {'font': font, 'glyphs': font.getGlyphSet(), 'cmap': font.getBestCmap(),
                    'upm': font['head'].unitsPerEm, 'bounds': {}}

    def conflicts(self, root):
        indicator = [e for e in root.iter() if tag(e) == 'path' and e.get('stroke') == '#607986']
        self.assertEqual(1, len(indicator))
        points = path_points(indicator[0].get('d'))
        captions = [e for e in root.iter() if tag(e) == 'text'
                    and re.fullmatch(r'类型 [123] / Type [123]', e.text or '')]
        self.assertEqual(3, len(captions))
        return [e.text for e in captions if any(segment_box(a, b,
            expanded(text_box(e, (0., 0.), self.font), .9)) for a, b in zip(points, points[1:]))]

    def test_all_caption_ink_clears_trend_in_both_layouts_and_field_changes(self):
        model, view = inputs(self.profile)
        changed = copy.deepcopy(model)
        self.assertIsNotNone(substantive_change(changed, view))
        for layout in ('reference', 'adaptive'):
            for data in (model, changed):
                with self.subTest(layout=layout, modified=data is changed):
                    svg, report = express(data, view, self.profile, layout)
                    self.assertEqual([], report['errors'])
                    self.assertEqual([], self.conflicts(ET.fromstring(svg)))

    def test_counterexample_original_outer_caption_crossing_is_rejected(self):
        model, view = inputs(self.profile)
        svg, _ = express(model, view, self.profile, 'reference')
        root = ET.fromstring(svg)
        caption = next(e for e in root.iter() if tag(e) == 'text' and e.text == '类型 3 / Type 3')
        caption.attrib.update(x='534.4464653313012', y='369.03183235208765', **{'text-anchor': 'end'})
        self.assertIn('类型 3 / Type 3', self.conflicts(root))
