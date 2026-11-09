#!/usr/bin/env python3
"""Publish local-only authored reviews; all writes are confined to this corpus."""
from pathlib import Path
import argparse
import json
import os
import sys

sys.dont_write_bytecode = True
CORPUS = Path(__file__).resolve().parents[1]
ROOT = CORPUS.parent
sys.path.insert(0, str(ROOT / 'tools/togaf_corpus'))
sys.path.insert(0, str(CORPUS / 'maintenance/pipeline'))


def check_write(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if resolved != CORPUS and CORPUS not in resolved.parents:
        raise PermissionError('This task only writes inside ' + str(CORPUS) + ': ' + str(resolved))


def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if (mode and any(ch in mode for ch in 'wax+')) or flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            check_write(path)
    elif event in {'os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.utime'}:
        check_write(args[0])
    elif event in {'os.rename', 'os.link', 'os.symlink'}:
        check_write(args[0]); check_write(args[1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapters-only', action='store_true')
    args = parser.parse_args()
    sys.addaudithook(guard)
    import chapter_reviews
    import architecture_diagrams
    import build_architecture
    chapter_result = chapter_reviews.build(ROOT, CORPUS)
    if not args.chapters_only:
        diagrams = architecture_diagrams.build(ROOT, CORPUS)
        integrated = build_architecture.integrate(ROOT, CORPUS)
        print(json.dumps({'diagrams': diagrams['counts'], 'architecture': integrated['counts']}, ensure_ascii=False))
        import publish_extended
        publish_extended.main()
    print(json.dumps({'chapters': chapter_result['counts']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
