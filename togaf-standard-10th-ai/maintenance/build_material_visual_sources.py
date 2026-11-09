#!/usr/bin/env python3
"""Render or verify W242C source evidence using the installed local PDF tools."""
import argparse
import json
from pathlib import Path
from material_visual_sources import REPO, build, reference, verify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('build', 'verify'))
    parser.add_argument('--out', type=Path)
    parser.add_argument('--manifest', type=Path)
    args = parser.parse_args()
    if args.command == 'build':
        if args.out is None: parser.error('build requires --out')
        manifest = build(args.out); result = verify(manifest)
        result['manifest'] = manifest
    else:
        if args.manifest is None: parser.error('verify requires --manifest')
        path = args.manifest if args.manifest.is_absolute() else REPO / args.manifest
        result = verify(reference(path, REPO))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__': main()
