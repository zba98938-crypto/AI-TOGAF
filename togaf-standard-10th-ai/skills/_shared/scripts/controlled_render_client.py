#!/usr/bin/env python3
"""Submit one fixed-format graphic task to the local test controller."""
import argparse
import json
import os
import time
import uuid
from pathlib import Path


def submit(task, root=None, timeout=180):
    root = Path(root or Path.cwd()).resolve()
    if not isinstance(task, dict) or set(task) != {'kind', 'source'}:
        raise ValueError('task must contain exactly kind and source')
    if task['kind'] not in {'svg', 'mmd', 'bpmn','uml-class-layout'} or not isinstance(task['source'], str):
        raise ValueError('unsupported graphic task')
    queue = root / '.render'
    for folder in (queue, queue/'inbox', queue/'outbox', queue/'results'):
        if folder.is_symlink() or not folder.is_dir():
            raise ValueError('no registered local rendering controller in this session')
    identity = uuid.uuid4().hex
    request = queue/'inbox'/(identity+'.json')
    with request.open('x') as stream:
        json.dump(task, stream, ensure_ascii=False)
    deadline = time.monotonic() + timeout
    response = queue/'outbox'/(identity+'.json')
    while time.monotonic() < deadline:
        if response.is_symlink():
            raise ValueError('invalid rendering response')
        if response.is_file():
            result = json.loads(response.read_text())
            if result.get('status') != 'pass':
                raise ValueError(result.get('reason', 'rendering refused'))
            return result
        time.sleep(.1)
    raise TimeoutError('local rendering controller timed out')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task', type=Path)
    args = parser.parse_args()
    try:
        result = submit(json.loads(args.task.read_text()))
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TimeoutError) as exc:
        print(json.dumps({'status': 'refused', 'reason': str(exc)}, ensure_ascii=False))
        return 3


if __name__ == '__main__':
    raise SystemExit(main())
