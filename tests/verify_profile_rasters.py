#!/usr/bin/env python3
"""Check every requested profile raster and tile at its declared native size.

This verifies file bytes and complete crop coverage, not professional semantics.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from PIL import Image

SHARED = Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/skills/_shared'
REPO = SHARED.parents[2]
sys.path.insert(0, str(SHARED / 'scripts'))
from registry import load


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(folder):
    folder = Path(folder).resolve()
    verification = json.loads((folder / 'verification.json').read_text())
    rendered = json.loads((folder / 'render-report.json').read_text())
    profiles = {p['id']: p for p in load()[2].values() if not p.get('alias_of')}
    expected = {identity + '-' + layout + variant for identity, p in profiles.items()
                if p.get('output_kind', 'diagram') == 'diagram'
                for layout in ('reference', 'adaptive') for variant in ('', '-modified')}
    rows, failures = [], []
    inputs = {name: digest(folder / name) for name in ('verification.json', 'render-report.json')}

    def ensure(condition, message):
        if not condition:
            raise AssertionError(message)

    def path(name):
        target = (folder / name).resolve()
        ensure(target.is_relative_to(folder) and target.is_file(), 'missing/escaping file: ' + name)
        inputs[name] = digest(target)
        return target

    def png(name, width, height, expected_hash):
        target = path(name)
        ensure(inputs[name] == expected_hash, 'raster checksum: ' + name)
        with Image.open(target) as bitmap:
            ensure(bitmap.format == 'PNG' and bitmap.size == (width, height), 'PNG format/size: ' + name)
            bitmap.verify()

    actual = [r['id'] for r in rendered['results']]
    if set(actual) != expected or len(actual) != len(expected):
        failures.append({'id': 'coverage', 'reason': 'missing/extra/duplicate raster jobs',
                         'missing': sorted(expected - set(actual)), 'extra': sorted(set(actual) - expected)})
    if verification['failed_profiles'] or rendered['status'] != 'passed':
        failures.append({'id': 'execution', 'reason': 'profile expression or raster execution did not pass'})
    for row in rendered['results']:
        try:
            svg = path(row['svg'])
            ensure(digest(svg) == row['svg_sha256'], 'SVG checksum')
            root = ET.parse(svg).getroot()
            width, height = [math.ceil(float(root.get(key).removesuffix('px'))) for key in ('width', 'height')]
            ensure((width, height) == (row['width'], row['height']), 'SVG/raster viewport differs')
            count = 1
            if row.get('mode') == 'tiles':
                manifest_path = path(row['tile_manifest'])
                ensure(digest(manifest_path) == row['tile_manifest_sha256'], 'tile manifest checksum')
                tiles = json.loads(manifest_path.read_text())
                ensure(tiles['source_sha256'] == digest(svg), 'tiles source differs from SVG')
                ensure(tiles['scale'] == 1 and tiles['monolithic_capacity_claimed'] is False, 'implicit scaling/monolithic claim')
                ensure((tiles['width'], tiles['height']) == (width, height), 'tile viewport differs')
                expected_crops = {(x, y, min(2048, width-x), min(2048, height-y))
                                  for y in range(0, height, 2048) for x in range(0, width, 2048)}
                crops = [(t['x'], t['y'], t['width'], t['height']) for t in tiles['tiles']]
                ensure(set(crops) == expected_crops and len(crops) == len(expected_crops), 'tile gaps/overlap/duplicates')
                ensure(len(crops) == row['tile_count'], 'tile count differs')
                for tile in tiles['tiles']:
                    png(tile['png'], tile['width'], tile['height'], tile['sha256'])
                path(row['tile_viewer'])
                count = len(crops)
            else:
                png(row['png'], width, height, row['png_sha256'])
            rows.append({'id': row['id'], 'passed': True, 'width': width, 'height': height,
                         'mode': row.get('mode', 'single'), 'png_files': count})
        except (AssertionError, OSError, ValueError, KeyError, ET.ParseError) as exc:
            failures.append({'id': row['id'], 'reason': str(exc)})
    return {'schema_version': 'profile-raster-integrity/1', 'passed': not failures,
            'counts': {'jobs': len(actual), 'checked': len(rows), 'tiled_jobs': sum(r['mode']=='tiles' for r in rows),
                       'png_files': sum(r['png_files'] for r in rows), 'failures': len(failures)},
            'results': rows, 'failures': failures,
            'input_sha256': {str((folder/name).relative_to(REPO)): value for name, value in inputs.items()},
            'input_base': str(folder), 'scope': 'actual PNG/SVG bytes, native dimensions and complete tile coverage; professional acceptance not granted'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profiles', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.profiles)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
    print(json.dumps(report['counts']))
    return int(not report['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
