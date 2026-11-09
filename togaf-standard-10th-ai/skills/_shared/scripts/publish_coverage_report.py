#!/usr/bin/env python3
"""Publish the current, project-local evidence snapshot without promoting it."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = ROOT / "reviews"


def read(path):
    return json.loads(path.read_text())


def table(headers, rows):
    return "| " + " | ".join(headers) + " |\n| " + " | ".join("---" for _ in headers) + " |\n" + "".join(
        "| " + " | ".join(str(value) for value in row) + " |\n" for row in rows
    )


def main():
    status = read(REV / "capability-status.json")
    source = read(REV / "actual-source-skill-comparison-project-local-current.json")
    priority = read(REV / "source-priority-recheck-followup-2026-11-03.json")
    routes = read(REV / "figure-route-dispositions-followup-2026-11-03.json")
    methods = read(REV / "method-acceptance-assessment-2026-11-03.json")
    chapters = read(ROOT / "examples/xinghe-synthetic/deliverable-case-audit.json")
    pages = read(REV / "deliverable-page-review/page-audit.json")
    regression = read(ROOT / "tests/acceptance-v2-2026-11-03-followup-final.json")
    counts = status["registered_counts"]
    accepted = status["fully_accepted_counts"]
    dim = status["dimension_pass_counts"]
    categories = (("制品族", "artifact_families"), ("其中：指南工作产品", "guide_work_products"),
                  ("独立视图模板", "view_templates"), ("分析方法", "analysis_methods"), ("交付物", "deliverables"))
    rows = [(label, counts[key], *(dim[key][d] for d in ("definition", "model", "analysis", "generation", "modification", "review", "visual")), accepted[key]) for label, key in categories]
    source_summary = source["summary"]
    layout_rows = []
    for name, layout in chapters["layouts"].items():
        unbound = sum(len(d["unbound_section_titles"]) for d in layout["deliverables"])
        layout_rows.append((name, layout["deliverable_count"], layout["view_count"], unbound, len(layout["output_hash_mismatches"])))
    reg_passed = sum(run["exit_code"] == 0 for run in regression["runs"])
    reg_failed = len(regression["runs"]) - reg_passed
    lines = [
        "# TOGAF 全面能力对标与补齐",
        "",
        f"日期：{status['date']}。当前逐项状态见[七维状态清单](capability-status.json)，本轮操作与限制见[整体验收执行结果](TOGAF整体验收执行结果-2026-11-03.md)。历史报告和失败记录保留，不因本轮记录自动升级。",
        "",
        "## 两个独立结论",
        "",
        "- **本地中文套件匹配：未通过完整逐项验收。**中文材料用于定位和翻译，英文原件为冲突仲裁。26 条已登记偏差有逐条限定裁定，但 1,392 条节／表记录仍缺完整英文语义核对，330 表未逐字段闭合。",
        "- **按项目内 26 份英文原件界定的 TOGAF 来源匹配：未通过完整逐项验收。**本次分母只取项目内英文 PDF；C220 正文与 G238 外部工作簿不纳入本次分母。若某能力仍依赖未提供材料，只阻断该身份。来源图结构、266 模板和业务内容尚无逐项七维证据。",
        "",
        "## 五类身份与严格七维",
        "",
        table(["类别", "登记", "定义", "模型", "分析", "生成", "修改", "评审", "视觉", "完整通过"], rows).rstrip(),
        "",
        "106 个工作产品已包含于 176 个制品族，不重复相加。267 个规范入口含 1 个兼容别名，独立模板为 266。表中通过数来自[严格证据门](../references/acceptance-evidence.md)，工程运行不自动授予内容或视觉通过。",
        "",
        "## 来源与路由",
        "",
        f"[项目内英文来源对照](actual-source-skill-comparison-project-local-current.json)核对 26／26 PDF 哈希、1,337 节、330 表、243 图、406 图像资产；来源包 2,654 项资产完整性错误 {source_summary['package_integrity_errors']}。其中 {source_summary['english_semantic_check_pending_entries']} 条英文语义待核。[26 条偏差限定复核](source-priority-recheck-followup-2026-11-03.json)已有 26 条英文页锚点和处理结论，完整语义接受 0。",
        "",
        f"[18 条图路由逐图处置](figure-route-dispositions-followup-2026-11-03.json)：1 条图号格式诊断、2 条错误或部分结构绑定、15 条通用结构可复用但具体英文内容／视觉未核。另 [11 张无直达图初筛](no-direct-figure-route-dispositions-2026-11-03.json)已逐图定位用途，不授模板等价。[本轮实际打开](actual-visual-observations-followup-2026-11-03.json)只覆盖所列来源裁图和页面。",
        "",
        "G234 图 4-4 的可信英文裁图另存，旧错绑资产保留；图 3-1 现仅绑定业务半图。[G211 图 3-2 的 18 格转写](source-repairs/G211-fig3-2-18-cell-recheck-2026-11-03.json)已逐格核对英文原图，技能模板仍未等价验收。G242 图 3-14 仅有限结构观察；G186 图 6-1 是中文编辑附图，没有对应英文原图。旧 `faithful` 标签不自动继承。",
        "",
        "## 实际运行、内容与排版",
        "",
        f"[方法状态](method-acceptance-assessment-2026-11-03.json)：{methods['summary']['current_scoped_replay']}／60 有当前限定工程重放，12 种计算方法的 24 个变体与独立预期匹配，完整业务验收 {methods['summary']['complete_accepted']}／60。G212 数字阈值仅按显式虚构项目规则使用；旧过期索引未改写。",
        "",
        "全量 reference、adaptive 各生成 267 个入口（其中独立模板 266），但没有 266 个模板逐项的原图结构、实质修改、反例和目视通过。星河同一项目的章节候选绑定如下：",
        "",
        table(["状态／布局", "交付物", "视图", "未绑定章节", "输出哈希差异"], layout_rows).rstrip(),
        "",
        f"[交付物页面机器审计](deliverable-page-review/page-audit.json)为 {pages['documents']} 篇 PDF、{pages['pages']} 页、{pages['problem_documents']} 篇机器问题文档；只实际打开了[限定页面](actual-visual-observations-followup-2026-11-03.json)，没有 894 页逐页目视接受。章节绑定是候选结构，22 项业务内容仍待接受。",
        "",
        "[澄湾独立试用](../examples/independent-charge-trial/README.md)覆盖 4 视图、1 篇结构化草稿；可选业务规则契约拒绝同事件 ID 的电表号冲突自动覆盖。离线复制仅在本机操作系统执行；Linux QEMU 副本未运行。",
        "",
        f"[当前完整工程回归](../tests/acceptance-v2-2026-11-03-followup-final.json)已记录 {len(regression['runs'])} 项，{reg_passed} 通过、{reg_failed} 失败、{len(regression['skip_summary'])} 跳过；[系统 Python 缺依赖批次](../tests/acceptance-v2-2026-11-03-followup.json)与[未指定浏览器批次](../tests/acceptance-v2-2026-11-03-followup-venv.json)保留。",
        "",
        "**整体判定：可执行修复有当前记录，整体验收尚有明确缺口。**逐身份阻断见[剩余问题清单](剩余问题清单-2026-11-03.md)。",
        "",
    ]
    (REV / "TOGAF全面能力对标.md").write_text("\n".join(lines))
    print(json.dumps({"registered": counts, "fully_accepted": accepted, "source_pending": source_summary["english_semantic_check_pending_entries"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
