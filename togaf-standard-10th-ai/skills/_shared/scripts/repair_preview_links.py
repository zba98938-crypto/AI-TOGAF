#!/usr/bin/env python3
"""Append clearly dated dependency supplements, never rewrite development previews.

Early scenario previews linked to artifacts before rendering. Generate their exact
saved model into a new run, and put explicit navigation pages at missing targets.
The supplements are new executions, not renewed historical review or acceptance.
"""
import json
import os
from pathlib import Path
import re
import sys

from execution_batch import Batch, digest

ROOT = Path(__file__).resolve().parents[1]


def main():
    models = sorted((ROOT / 'examples/qianlin-synthetic/runs').glob('semantic-closure-20261104-dev*/model.json'))
    models += sorted((ROOT / 'examples/library-delivery-validation/runs').glob('queue-closure-20261104-dev*/model.json'))
    batch = Batch('reviews/development/preview-link-supplements', inputs=models + [Path(__file__)],
                  purpose='Append missing navigation dependencies; retain original preview bytes and status')
    targets = {}
    records = []
    for model in models:
        original = model.parent
        docs = sorted((original / 'deliverables').glob('*.md')) or sorted(original.glob('*.md'))
        folder = batch.directory / original.name
        run, result = batch.run([sys.executable, ROOT / 'scripts/generate.py', model,
                                 '--all', '--out', folder])
        if result.returncode:
            folder.mkdir(parents=True, exist_ok=True)
            rejected = folder / 'generation-rejected.txt'
            rejected.write_text('该历史模型未通过当前校验；未生成制品，不修改旧输入以伪造通过。\n'+result.stderr)
            artifacts = {v['id']: rejected for v in json.loads(model.read_text())['views']}
        else:
            manifest = json.loads((folder / 'manifest.json').read_text())
            artifacts = {a['view_id']: folder / a['path'] for a in manifest['artifacts']}
        for doc in docs:
            for link in re.findall(r'\]\((\.\./artifacts/([A-Za-z0-9_.-]+)\.md)\)', doc.read_text()):
                target = (doc.parent / link[0]).resolve()
                if target.is_file():
                    continue
                if not target.is_relative_to(ROOT / 'examples') or link[1] not in artifacts:
                    raise ValueError('Unresolvable preview dependency: ' + str(target))
                targets.setdefault(target, []).append((model, artifacts[link[1]]))
        records.append({'original_model': str(model.relative_to(ROOT)), 'model_sha256': digest(model),
                        'new_manifest': str((folder / 'manifest.json').relative_to(ROOT)) if result.returncode == 0 else None,
                        'generation_exit': result.returncode,
                        'notice': 'Rendered later; historical preview and approval state unchanged.'})
    for target, dependencies in targets.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        lines = ['# 开发预览依赖补充导航', '',
                 '这是后续新执行的导航补充；不是原开发预览当时已经生成或通过的证明。',
                 '原预览、模型与失败记录未改写。请选择与原预览目录一致的版本：', '']
        for model, artifact in dependencies:
            label = '对应模型的新生成制品' if artifact.suffix == '.md' else '历史模型拒绝原因（未生成制品）'
            lines.append('- 原模型 `' + str(model.relative_to(ROOT)) + '`；['+label+'](' +
                         os.path.relpath(artifact, target.parent) + ')。')
        with target.open('x') as stream:
            stream.write('\n'.join(dict.fromkeys(lines)) + '\n')
    index = batch.directory / 'supplements.json'
    index.write_text(json.dumps({'records': records, 'navigation_pages_added': len(targets),
        'historical_files_overwritten': 0, 'accepted': False}, ensure_ascii=False, indent=2) + '\n')
    outputs = [p for p in batch.directory.rglob('*') if p.is_file()] + list(targets)
    path, report = batch.finish(outputs=outputs)
    print(json.dumps({'batch': str(path), 'passed': report['passed'], 'navigation_pages_added': len(targets)}, ensure_ascii=False))
    # A rejected historical model is retained, not disguised as successful replay.
    # Navigation repair is independent of the historical generation result.
    return int(bool(report['changed_runtime_paths'] or report['changed_input_paths']))


if __name__ == '__main__':
    raise SystemExit(main())
