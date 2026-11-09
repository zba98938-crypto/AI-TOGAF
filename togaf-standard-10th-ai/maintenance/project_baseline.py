#!/usr/bin/env python3
"""Record locally retained material without modifying it or following symlinks."""
import argparse
import hashlib
import json
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRUNE = {'.git', 'node_modules', '.venv', '__pycache__', 'output', 'tmp', 'work', '.vscode'}
MATERIAL = {'.pdf', '.mhtml', '.png', '.ttf', '.woff', '.woff2', '.jar', '.class', '.zip'}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def inventory(root):
    root = root.resolve()
    rows, links = [], []
    for base, dirs, files in os.walk(root, followlinks=False):
        kept = []
        for name in sorted(dirs):
            path = Path(base) / name
            if path.is_symlink():
                links.append({'path': path.relative_to(root).as_posix(), 'target': os.readlink(path)})
            elif name not in PRUNE:
                kept.append(name)
        dirs[:] = kept
        for name in sorted(files):
            path = Path(base) / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                links.append({'path': relative, 'target': os.readlink(path)})
                continue
            size = path.stat().st_size
            retained = (path.suffix.lower() in MATERIAL or name.endswith('.tar.gz')
                        or relative.startswith(('08_磷化工行业知识库/', 'togaf-standard-10th-ai/sources/retained/'))
                        or size > 5 * 1024 * 1024)
            if retained:
                rows.append({'path': relative, 'bytes': size, 'sha256': digest(path),
                             'kind': 'large-data' if size > 5 * 1024 * 1024 else 'retained-material'})
    return {'schema_version': 'project-local-material-baseline/1', 'repo_root': str(root),
            'files': sorted(rows, key=lambda row: row['path']), 'symlinks': links,
            'excluded_runtime_directory_names': sorted(PRUNE),
            'meaning': 'Local byte preservation and location inventory; no semantic acceptance.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        parser.error('--out must be new; historical inventories are immutable')
    data = inventory(REPO)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'files': len(data['files']), 'bytes': sum(r['bytes'] for r in data['files']),
                      'manifest': str(args.out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
