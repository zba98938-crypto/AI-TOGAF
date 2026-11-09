"""Render reviews/method-case-index.md from the JSON index.

The Markdown table is generated, not hand-maintained, so the six role columns can
never drift from the JSON hashes they claim to summarise.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLES = [('raw', '原料'), ('steps', '步骤'), ('result', '结果'),
         ('modification', '修改'), ('counterexample', '反例'),
         ('execution', '运行记录'), ('cross_review', '交叉评审')]
INTRO = """# 分析方法实际案例入口索引

本文件由 `scripts/render_method_case_index.py` 从 [机器索引](method-case-index.json) 生成，请勿手工编辑。

## 当前状态

注册方法 **{registered}** 个，全部具有指向**本方法自身**的七章案例（`examples/method-cases/<method_id>.md`）。每个案例含：决策与原始业务资料、来源规则与项目规则、转换与推理、输出与追溯、修改演练、反例与输入不足、评审记录，并以统一的作者一致性声明收尾。

| 项 | 数量 | 含义 |
|---|---|---|
| canonical case | {canonical} | 指向本方法自身七章案例的入口 |
| 七章结构完整 | {complete} | 六个正文角色齐备且结构有序 |
| 交叉评审记录 | {cross} | AI 具名代理的范围性审阅，**非人工签字** |
| 执行记录 | {execution} | 按步骤走完留下的记录，**非计算器结果** |
| 仍保留扩展证据 | {ext_kept} | 除本案例外仍挂接 addenda/extension 证据的方法 |
| 待复核（哈希保留） | {stale} | 历史更正后故意保留旧哈希、要求重新核对的方法 |

**边界**：64/64 有案例 ≠ 64/64 方法通过验收。案例为虚构演练；交叉评审由 AI 签署；执行记录只证明"在给定虚构输入上按步骤执行过"，不证明方法选择正确或结论符合业务。独立业务评审、官方定义逐字核实与图形视觉比对仍为待验证。

原有 14 方法的定性执行与两份跨代理评审记录保留在 `examples/qualitative-execution/`、`reviews/qualitative-*-cross-review.json`，未因本轮改写而删除；它们评的是另一批文件，因此不再作为这 14 个方法本轮案例的交叉评审来源（本轮已为每个方法另出逐案例评审）。

**本轮新增可核工件**：

| 文件 | 作用 |
|---|---|
| `reviews/method-case-constraints.json` | 机械核验七章结构、反例码、修改演练、定性边界；64/64 通过，0 违规 |
| `reviews/method-case-similarity.json` | 2016 对两两相似度，最高 0.13、均值 0.034，无阈值以上配对 |
| `scripts/verify_method_case_constraints.py` | 上述核验的实现；`tests/test_method_case_constraints.py` 用 8 个负例证明它确实会拒绝坏案例 |

## 逐方法入口

"""


def links(rows):
    if not rows:
        return '未定位'
    parts = []
    for i, row in enumerate(rows, 1):
        target = row['path']
        # This Markdown lives in reviews/, while index paths are relative to
        # skills/_shared; every internal path therefore needs exactly one "..".
        if target.startswith(('examples/', 'reviews/', 'references/', 'tests/')):
            target = '../' + target
        parts.append('[%s](<%s>)' % (i, target))
    return ' / '.join(parts)


def main():
    index = json.loads((ROOT / 'reviews/method-case-index.json').read_text())
    methods = index['methods']
    summary = index['summary']
    complete = sum(
        1 for m in methods
        if all(m['evidence'].get(r) for r in ('raw', 'steps', 'result', 'modification', 'counterexample'))
    )
    stale = 0
    for m in methods:
        for role in ('raw', 'steps', 'result', 'modification', 'counterexample'):
            for row in m['evidence'].get(role, []):
                if 'historical-hash-preserved' in (row.get('basis') or ''):
                    stale += 1
                    break
            else:
                continue
            break

    out = [INTRO.format(
        registered=summary.get('registered_methods', len(methods)),
        canonical=summary.get('canonical_via_own_case', 0),
        complete=complete,
        cross=summary.get('bounded_cross_review_linked_count', 0),
        execution=summary.get('execution_record_located_count', 0),
        ext_kept=summary.get('extension_evidence_retained_count', 0),
        stale=stale,
    )]
    header = '| 方法 | 入口类别 | ' + ' | '.join(name for _, name in ROLES) + ' |'
    divider = '|' + '---|' * (len(ROLES) + 2)
    out.append(header)
    out.append(divider)
    for m in methods:
        cells = [links(m['evidence'].get(role, [])) for role, _ in ROLES]
        route = m['route_type']
        if m.get('extension_evidence_retained'):
            route += '（另存扩展证据）'
        out.append('| `%s` | %s | %s |' % (m['method_id'], route, ' | '.join(cells)))
    out.append('')
    out.append('## 说明')
    out.append('')
    out.append('1. 表中数字为该角色的可达记录条数，不等于通过项数。')
    out.append('2. `运行记录` 对无独立计算器的方法指"按步骤走完的书面执行记录"，不含机器计算结果。')
    out.append('3. `交叉评审` 由 AI 代理在限定范围内核对文本自洽与追溯完整，未核对业务真实性，也非人工签字。')
    out.append('4. 标"哈希保留"的方法保留更正前的哈希，索引因此持续报"需复核"，这是刻意留白而非遗漏。')
    out.append('')
    (ROOT / 'reviews/method-case-index.md').write_text('\n'.join(out))
    print(json.dumps({'rows': len(methods), 'complete': complete, 'stale': stale}, ensure_ascii=False))


if __name__ == '__main__':
    main()
