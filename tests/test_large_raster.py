"""Large diagrams retain topology and native resolution without huge bitmaps."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from profile_render import orthogonal_route


class LargeRoutingTests(unittest.TestCase):
    def test_clear_large_route_does_not_build_global_visibility_grid(self):
        class Drawing:
            positions = {'a': (30, 120, 320, 120), 'b': (530, 120, 320, 120),
                         **{str(i): (30 + i * 500, 500, 320, 120) for i in range(1000)}}
            width = 501000
            height = 700
            occupied_segments = []
        with patch('profile_render.heapq.heappush', side_effect=AssertionError('global grid')):
            points = orthogonal_route(Drawing(), {'source': 'a', 'target': 'b'})
        self.assertIsNotNone(points)
        self.assertTrue(all(a[0] == b[0] or a[1] == b[1] for a, b in zip(points, points[1:])))


class LargeRasterTests(unittest.TestCase):
    def run_node(self, body):
        script = "import {rasterPlan} from './scripts/raster_tiles.mjs';\n" + body
        return subprocess.run(['node', '--input-type=module', '-e', script],
                              cwd=SHARED, capture_output=True, text=True, timeout=15)

    def test_tile_plan_covers_nonzero_viewbox_at_original_pixel_resolution(self):
        result = self.run_node("console.log(JSON.stringify(rasterPlan('<svg viewBox=\"10 20 20000 100\" width=\"20000\" height=\"100\"/>')));")
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        self.assertEqual(plan['mode'], 'tiles')
        self.assertEqual(sum(t['width'] * t['height'] for t in plan['tiles']), 2000000)
        self.assertEqual(plan['tiles'][0]['viewBox'][:2], [10, 20])
        self.assertTrue(all(t['width'] <= 2048 and t['height'] <= 2048 for t in plan['tiles']))
        self.assertEqual(plan['scale'], 1)

    def test_invalid_or_excessive_dimensions_rejected_before_allocation(self):
        for viewport in ('0 0 NaN 100', '0 0 1000000 1000000'):
            with self.subTest(viewport=viewport):
                result = self.run_node('rasterPlan(' + json.dumps('<svg viewBox="' + viewport + '"/>') + ');')
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('diagram-capacity:', result.stderr)

    def test_real_tiles_preserve_svg_and_are_not_a_monolithic_capacity_claim(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder)
            svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20000 100" width="20000" height="100"><rect x="19900" width="100" height="100" fill="#ff0000"/></svg>'
            (dest / 'large.svg').write_text(svg)
            (dest / 'jobs.json').write_text(json.dumps({'font': str(SHARED / 'assets/fonts/NotoSansSC.ttf'),
                'oversized_policy': 'tile', 'jobs': [{'id': 'large', 'kind': 'svg',
                'source': 'large.svg', 'svg': 'large.svg', 'png': 'large.png'}]}))
            result = subprocess.run(['node', str(SHARED / 'scripts/render.mjs'), str(dest / 'jobs.json')],
                                    capture_output=True, text=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((dest / 'large.svg').read_text(), svg)
            self.assertFalse((dest / 'large.png').exists())
            report = json.loads((dest / 'large.tiles.json').read_text())
            self.assertFalse(report['monolithic_capacity_claimed'])
            self.assertEqual(len(report['tiles']), 10)
            last = report['tiles'][-1]
            with Image.open(dest / last['png']) as image:
                self.assertEqual(image.size, (last['width'], last['height']))
                self.assertEqual(image.convert('RGB').getpixel((last['width'] - 50, 50)), (255, 0, 0))

    def test_tiled_generated_artifacts_are_hashed_and_tampering_rejected(self):
        from registry import load
        from profile_examples import normalize_example
        from generate import generate
        from architecture_delivery import output_check
        from profile_render import render_profile
        model = normalize_example(load()[2]['trust-framework-default'])
        real_render = render_profile

        def large(*args, **kwargs):
            svg, report = real_render(*args, **kwargs)
            import re
            svg = re.sub(r'(<svg\b[^>]*?)width="[^"]*" height="[^"]*" viewBox="[^"]*"',
                         r'\1width="20000" height="100" viewBox="0 0 20000 100"', svg, count=1)
            return svg, report

        with tempfile.TemporaryDirectory() as folder, patch('profile_render.render_profile', side_effect=large):
            dest = Path(folder)
            manifest = generate(model, dest, all_items=True, strict=True, render=True)
            entry = manifest['artifacts'][0]
            self.assertEqual(entry['raster_mode'], 'tiles')
            self.assertIsNone(entry['png'])
            self.assertEqual(output_check(dest, model)[1], [])
            tile = entry['tile_pngs'][0]
            (dest / tile).write_bytes(b'tampered')
            self.assertIn('output-file-stale:' + tile, output_check(dest, model)[1])
            del manifest['output_sha256'][tile]
            (dest / 'manifest.json').write_text(json.dumps(manifest))
            self.assertIn('output-hash-missing:' + tile, output_check(dest, model)[1])
            entry['tile_pngs'].remove(tile)
            (dest / 'manifest.json').write_text(json.dumps(manifest))
            errors = output_check(dest, model)[1]
            self.assertIn('output-tile-contract-invalid:' + entry['view_id'], errors)
            self.assertIn('output-hash-missing:' + tile, errors)
