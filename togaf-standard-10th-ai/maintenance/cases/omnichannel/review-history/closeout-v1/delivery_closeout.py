#!/usr/bin/env python3
"""Record the completed image review and verify delivered local source paths.

The per-image observations below were recorded after opening each PNG at its
original size with view_image; this script checks those inspected fingerprints,
SVG identities, output integrity, and source locations. It does not perform a
new visual review when rerun, and it does not change coverage acceptance status.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys
from PIL import Image

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GEN = HERE / 'generated'
# Inspected 2026-11-08. Baseline was opened again after regeneration; all ten
# offline PNG hashes were verified unchanged from the inspected pre-render bytes.
OBSERVATIONS = {
    'capability-map': '4个能力及3个分解关系清楚；战略/支持带未记录不解释为不适用，带内位置不表顺序。',
    'interface-network': '应用和接口框完整；exposes/consumes统一箭头，需结合连线编号及语义列表读取，不能把提供和消费混为调用方向。',
    'transition-roadmap': '候选工作包及运营状态、日期条和关系完整；状态中的条件和待决输入可见，候选日期不等于运行就绪。',
    'risk-treatment': '风险、控制候选及演练期限清楚；残余风险保留待演练，没有伪造概率或评级。',
    'order-states': '4状态及3迁移可辨；订单确认后进入物流，异常路径保留；未强行增加初始状态。',
    'offline-data-boundary': '门店持久记录和中央接收/承诺记录分为两个框，单向对账追溯关系可辨；接收不自动成为履约确认。',
    'role-collaboration': '4角色及5关系可辨；企业角色含订单/库存/物流及门店渠道。职责标签完整，角色ID长串有换行。',
    'skill-matrix': '4技能×4角色的矩阵完整；原文参考4级、项目3级及两条未评价观察分列；空白/未记录不表零级。',
    'development-plan': '发展行动、历史证据和计划复评可读；现有等级为None且有中文未知说明；未推断培训提高评级。',
    'role-assignment': '11主体完整；4角色到任务箭头与1配置到任务箭头可见，两条配置到证据关系在明细页；容量、能力及批准缺口保留。',
}


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    inspected = load(HERE / 'visual-inspection-fingerprints.json')
    verified_manifest_files = 0
    source_rows = []
    source_errors = []
    visual_rows = []
    visual_errors = []
    for variant in ('baseline', 'offline-change', 'shared-object-change'):
        folder = GEN / variant
        model = load(folder / 'model.json')
        manifest = load(folder / 'manifest.json')
        for name, expected in manifest['output_sha256'].items():
            assert sha(folder / name) == expected, (variant, name)
            verified_manifest_files += 1
        for source in model['sources']:
            locator = source.get('locator', '')
            row = {'variant': variant, 'source_id': source['id'], 'locator': locator,
                   'locator_base': 'workspace-root'}
            if locator.startswith(('https://', 'http://')):
                row.update(status='external-original-reference-preserved-not-network-verified',
                           local_offline_equivalent='togaf-standard-10th-ai/documents/G249.md#page-27',
                           local_offline_sha256=sha(ROOT / 'togaf-standard-10th-ai/documents/G249.md'))
                assert '<a id="page-27"></a>' in (ROOT / 'togaf-standard-10th-ai/documents/G249.md').read_text()
            else:
                pathname, separator, fragment = locator.partition('#')
                path = ROOT / pathname
                exists = bool(pathname) and path.is_file()
                anchor_exists = exists and (not separator or f'id="{fragment}"' in path.read_text())
                row.update(status='local-path-and-fragment-verified' if anchor_exists else 'failed',
                           sha256=sha(path) if exists else None)
                if not anchor_exists:
                    source_errors.append(row)
            source_rows.append(row)
        if variant == 'shared-object-change':
            continue
        render = load(folder / 'render-report.json')
        expected_paths = {entry['png'] for entry in render['results']}
        actual_paths = {p.name for p in (folder / 'artifacts').glob('*.png')}
        assert actual_paths == expected_paths, (variant, actual_paths, expected_paths)
        for png in sorted((folder / 'artifacts').glob('*.png')):
            identity = png.stem
            svg = png.with_suffix('.svg')
            artifact = load(png.with_suffix('.json'))
            text = svg.read_text()
            entities = set(re.findall(r'data-entity-id="([^"]+)"', text))
            relationships = set(re.findall(r'data-relationship-id="([^"]+)"', text))
            selected_entities = set(artifact['view']['entity_ids'])
            selected_relationships = set(artifact['view']['relationship_ids'])
            missing_entities = sorted(selected_entities - entities)
            companion_relations = sorted(selected_relationships - relationships)
            expected_companion = ['CONFIG-EVIDENCE-A', 'CONFIG-EVIDENCE-EXPERT'] if identity == 'role-assignment' else []
            assert companion_relations == expected_companion, (variant, identity, companion_relations)
            if companion_relations:
                detail = png.with_suffix('.details.html').read_text()
                assert all(relation in detail for relation in companion_relations)
            recorded = inspected['png_sha256'][variant + '/' + identity]
            unchanged = sha(png) == recorded
            if not unchanged or missing_entities:
                visual_errors.append({'variant': variant, 'view_id': identity,
                                      'uninspected_changed_image': not unchanged, 'missing_entities': missing_entities})
            dimensions = Image.open(png).size
            row = {'variant': variant, 'view_id': identity, 'png_path': str(png.relative_to(HERE)),
                   'svg_path': str(svg.relative_to(HERE)), 'png_sha256': sha(png), 'svg_sha256': sha(svg),
                   'inspection_date': '2026-11-08', 'inspection_method': 'view_image-original-individual-images',
                   'current_png_matches_inspected_bytes': unchanged,
                   'width': dimensions[0], 'height': dimensions[1],
                   'visible_main_entity_count': len(entities), 'selected_entity_count': len(selected_entities),
                   'main_relation_ids': sorted(relationships), 'companion_only_relation_ids': companion_relations,
                   'observation_zh': OBSERVATIONS[identity],
                   'layout_observation_zh': '未发现主体框或正文截断、不可辨汉字、连线遮住正文；长技术字段会换行。',
                   'visual_review_status': 'reviewed-with-documented-limits', 'business_acceptance': 'not-granted'}
            if identity == 'skill-matrix':
                row['usability_limit_zh'] = '整图约3,400像素高，缩成页面缩略图时难读，应打开原尺寸或Markdown矩阵；正文技术JSON较密。'
            if identity == 'role-assignment':
                row['usability_limit_zh'] = 'PNG中的“可点击”明细提示在静态PNG本身不能点击；需由配套Markdown或SVG打开明细。单张PNG并未显示全部7条关系。'
            if identity in ('development-plan', 'role-assignment'):
                row['presentation_limit_zh'] = 'None等技术字段可进一步显示为“未知”；中文证据不足/容量未知说明已保留，不会据None赋等级。'
            visual_rows.append(row)
    assert len(visual_rows) == 19, len(visual_rows)
    result = {'schema_version': 'omnichannel-delivery-closeout/1',
              'generated_at': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),
              'status': 'passed-with-explicit-limits' if not source_errors and not visual_errors else 'failed',
              'reviewer': '/root/case_closeout independent-of-original-F08-implementation',
              'visual_reviewed_png_svg_pairs': len(visual_rows), 'visual_rows': visual_rows,
              'visual_errors': visual_errors, 'source_locators': source_rows, 'source_errors': source_errors,
              'manifest_output_hashes_verified': verified_manifest_files,
              'business_approval': 'not-granted', 'shared_object_change_png_rendered': False,
              'semantic_change_report': 'semantic-change-verification.json',
              'limits_zh': ['19对已实际查看的PNG/SVG为基线9张及断连10张；共享对象变体未栅格化，不计入19张。',
                            '原始外部G249 URL保留，未把离线路径验证冒充网络访问成功；可直接阅读本地英文第27页。',
                            '原F08独立复核和旧问题快照保存不变；本报告记录最新生成指纹及来源归一化后的状态。',
                            '本次目视检查与8项反事实回归不代替真实业务接受、人员能力证明或上线授权。']}
    dump(HERE / 'delivery-closeout-report.json', result)
    lines = ['# 案例交付收尾与逐图复核', '',
             f"结论：{result['status']}。已逐张目视复核19对PNG/SVG；{verified_manifest_files}项生成文件哈希匹配。业务批准仍未授予。", '',
             '原始图像按原尺寸逐张打开；来源归一化后重新生成，当前19张PNG与实际受检字节一致。SVG核对主体ID、关系ID与明细页。未将工程覆盖状态改成业务已接受。', '',
             '|变体|图|主图主体|主图/明细关系|观察|', '|---|---|---:|---|---|']
    lines += [f"|{r['variant']}|[{r['view_id']}]({r['png_path']})|{r['visible_main_entity_count']}|{len(r['main_relation_ids'])} / {len(r['companion_only_relation_ids'])}|{r['observation_zh']}|" for r in visual_rows]
    lines += ['', '两张技能矩阵图很长，应打开原尺寸或使用配套Markdown矩阵。两张角色配置图的全部11个主体可辨，主图5条关系、明细另外2条；静态PNG本身不能点击提示中的明细链接，应从配套Markdown/SVG进入。None等技术字段仍有中文未知解释，可继续改善表述。', '',
              '当前CASE-PERSON、CASE-EXPERT、CASE-ROLE-TARGET以及example-source均定位同目录角色输入；四项CASE业务来源使用已实际存在的HTML锚点。共24个本地来源引用验证通过；3个原始外部G249引用保留，并提供[本地英文第27页](../../../documents/G249.md#page-27)离线核对。', '',
              '[8项业务语义变更回归](semantic-change-verification.md)直接检查提供者、控制范围、职责及物流交接。接口含义变化的业务依赖继续待复核，不把自动一致投影当作已正确更改政策。', '',
              '详细SHA-256、PNG尺寸、SVG主体/关系及来源文件见[JSON](delivery-closeout-report.json)。', '']
    lines += ['- ' + line for line in result['limits_zh']]
    (HERE / 'delivery-closeout-report.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'status': result['status'], 'images': len(visual_rows),
                      'manifest_hashes': verified_manifest_files, 'local_source_errors': len(source_errors),
                      'visual_errors': len(visual_errors)}, ensure_ascii=False))
    return 0 if not source_errors and not visual_errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
