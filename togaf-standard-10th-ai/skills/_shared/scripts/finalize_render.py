#!/usr/bin/env python3
"""Validate saved renders and synchronise an unsealed delivery atomically per file.

This closes rendering only; it never changes source, visual or business acceptance.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def child(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute() or '..' in Path(name).parts:
        raise ValueError('unsafe delivery path: ' + str(name))
    target = (root / name).resolve()
    if not target.is_relative_to(root) or not target.is_file():
        raise ValueError('missing or escaped delivery file: ' + name)
    return target


def png_info(path, tile=False):
    from PIL import Image
    with Image.open(path) as image:
        if image.format != 'PNG':
            raise ValueError('render is not PNG: ' + str(path))
        width, height = image.size
        if width < (1 if tile else 80) or height < (1 if tile else 40):
            raise ValueError('empty render: ' + str(path))
        image.verify()
    with Image.open(path) as image:
        image.load()
    return width, height


def finalize(directory, report_name='render-report.json'):
    root = Path(directory).resolve()
    for ancestor in (root, *root.parents):
        if any((ancestor / marker).is_file() for marker in ('evidence-sha256.json', 'evidence-index.json')):
            raise ValueError('sealed evidence is immutable; create a new delivery revision')
    manifest_path = child(root, 'manifest.json')
    manifest = json.loads(manifest_path.read_text())
    model = json.loads(child(root, 'model.json').read_text())
    model_hash = hashlib.sha256(json.dumps(model, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    if model_hash != manifest.get('model_sha256'):
        raise ValueError('model fingerprint mismatch')
    for name, expected in manifest.get('output_sha256', {}).items():
        if digest(child(root, name)) != expected:
            raise ValueError('stale output hash: ' + name)
    report_path = child(root, report_name)
    report = json.loads(report_path.read_text())
    if report.get('status') != 'passed':
        raise ValueError('render report did not pass')
    results = report.get('results', [])
    by_id = {r['id']: r for r in results}
    if len(by_id) != len(results):
        raise ValueError('duplicate render result')
    graphics = [a for a in manifest['artifacts'] if a.get('svg')]
    if not graphics or set(by_id) != {a['view_id'] for a in graphics}:
        raise ValueError('render results must cover exactly all graphical artifacts')
    updated = copy.deepcopy(manifest)
    writes = {}
    paths = set(manifest.get('output_sha256', {})) | {report_name}
    for artifact in updated['artifacts']:
        if not artifact.get('svg'):
            artifact['render_status'] = 'not-applicable'
            continue
        result = by_id[artifact['view_id']]
        svg = child(root, artifact['svg'])
        if not result.get('svg_sha256') or digest(svg) != result['svg_sha256']:
            raise ValueError('render source hash missing or stale: ' + artifact['view_id'])
        folder = Path(artifact['svg']).parent
        if result.get('mode') == 'tiles':
            tile_name = str(folder / result['tile_manifest'])
            tile_path = child(root, tile_name)
            if digest(tile_path) != result.get('tile_manifest_sha256'):
                raise ValueError('stale tile manifest')
            tile_data = json.loads(tile_path.read_text())
            pngs = [str(folder / t['png']) for t in tile_data['tiles']]
            if not pngs:
                raise ValueError('empty tile set')
            expected_pngs = result.get('png_sha256', {})
            for name in pngs:
                path = child(root, name)
                if digest(path) != expected_pngs.get(path.name):
                    raise ValueError('stale tile PNG: ' + name)
                png_info(path, tile=True)
            viewer = str(folder / result['tile_viewer'])
            child(root, viewer)
            artifact.update(png=None, raster_mode='tiles', tile_manifest=tile_name,
                            tile_viewer=viewer, tile_pngs=pngs, monolithic_capacity_claimed=False)
            link = '原尺寸分块图片：[' + Path(viewer).name + '](' + Path(viewer).name + ')；不是单张 PNG 容量通过。'
            paths.update(pngs + [tile_name, viewer])
        else:
            name = str(folder / result['png'])
            png = child(root, name)
            if digest(png) != result.get('png_sha256'):
                raise ValueError('render PNG hash missing or stale: ' + name)
            width, height = png_info(png)
            if (width, height) != (result.get('width'), result.get('height')):
                raise ValueError('render dimensions mismatch')
            artifact.update(png=name, raster_mode='single')
            link = '独立图片：[' + png.name + '](' + png.name + ')。'
            paths.add(name)
        artifact['render_status'] = 'complete'
        artifact['render_evidence'] = {'path': report_name, 'sha256': digest(report_path),
                                       'source_sha256': digest(svg)}
        markdown = child(root, artifact['path']).read_text()
        import re
        markdown = re.sub(r'PNG 尚未渲染；使用 --render。|独立图片：\[[^\n]+?。|原尺寸分块图片：\[[^\n]+?不是单张 PNG 容量通过。', lambda _: link, markdown)
        writes[artifact['path']] = markdown
    index_path = child(root, 'index.md')
    index = index_path.read_text()
    import re
    index = re.sub(r'\n<!-- render-state -->.*?<!-- /render-state -->\n?', '', index, flags=re.S)
    index += '\n<!-- render-state -->\n图片已保存并通过文件与指纹检查；视觉及业务接受状态见独立评审。\n<!-- /render-state -->\n'
    writes['index.md'] = index
    updated['rendered'] = True
    updated['render_status'] = 'complete'
    updated['render_evidence'] = {'path': report_name, 'sha256': digest(report_path)}
    # Validate every reference before the first mutation. Repeated calls are stable.
    for name in paths:
        child(root, name)
    for name, content in writes.items():
        target = child(root, name)
        temp = target.with_name(target.name + '.finalizing')
        temp.write_text(content)
        os.replace(temp, target)
    updated['output_sha256'] = {name: digest(child(root, name)) for name in sorted(paths)}
    temp = manifest_path.with_name('manifest.json.finalizing')
    temp.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + '\n')
    os.replace(temp, manifest_path)
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--report', default='render-report.json')
    args = parser.parse_args()
    try:
        result = finalize(args.directory, args.report)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(json.dumps({'render_status': result['render_status'], 'business_acceptance': 'unchanged'}))


if __name__ == '__main__':
    main()
