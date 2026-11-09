"""Returned profile exports must keep their local companion links usable."""
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from registry import load
from verify_artifact_profiles import verify_profile


class ProfileCompanionExportTests(unittest.TestCase):
    def test_returned_svg_links_resolve_to_exported_companions(self):
        profile = load()[2]['architecture-landscape-projection']
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            result, exports = verify_profile(profile, out)
            self.assertEqual([], result['failures'])
            self.assertEqual(4, len(exports))
            for identity, svg, coverage in exports:
                with self.subTest(variant=identity):
                    links = [node.get('href') for node in ET.fromstring(svg).iter()
                             if node.tag.endswith('}a') and node.get('href')]
                    self.assertTrue(links)
                    for target in links:
                        self.assertTrue((out / target).is_file(), target)
                        self.assertEqual(target, coverage['companion_file'])
                    self.assertEqual(svg, (out / (identity + '.svg')).read_text())


if __name__ == '__main__':
    unittest.main()
