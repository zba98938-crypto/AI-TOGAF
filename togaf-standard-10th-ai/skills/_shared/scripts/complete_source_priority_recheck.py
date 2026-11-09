#!/usr/bin/env python3
"""Record bounded comparisons for all known bilingual deviations.

This records what was checked against the project-local English extracts. It
does not turn a deviation check into full section, table, or capability review.
"""
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = ROOT / "reviews"
PACKAGE = REV / "source-package-2026-11-02-v2"
BASE = REV / "source-priority-recheck-2026-11-03.json"
OUT = REV / "source-priority-recheck-followup-2026-11-03.json"

# PDF page, exact phrase in extracted English page (empty for the image-only
# matrix), observed difference, and the capability consequence.
OBSERVATIONS = {
    "G152:L406": (39, "This is not explicitly addressed in the TOGAF ADM", "中文保留需求管理和运营绩效监控，但省略原文对运营监控不由 ADM 显式处理的限定。", "业务属性画像可用；不能声称运营监控是 ADM 显式步骤。"),
    "G186:L347": (38, "Timing speaks to when", "中文 L362 的“取自律图”是“路线图”的错字；原文列 Roadmap、Implementation & Migration Plan、Phase G。", "沟通计划中的时机来源应按英文三项解释。"),
    "G186:L1884": (135, "refurbish the résumé of the entire team", "中文 L1888 的“重塑整个团队的资历”弱化了原文让团队准备履历的警告语气。", "阶段 H 的预算时机和工作包要求另据原文核对；此语气不作为操作规则。"),
    "G186:L2080": (151, "", "英文 Table B-1 是利益相关者类别与关注点的交叉矩阵；中文 L2086 只有缺表占位，已打开英文裁图。", "viewpoint-library、stakeholder-catalog 不得从中文占位推定矩阵字段或视觉等价。"),
    "G186:L2149": (153, "Table D-1 shows the relationship between the stakeholder classes and concerns", "英文引导句与紧随的 Solution Delivery Notebook 表不符；中文 L2153 改成章节结构用途，是未标注的原文纠错。", "architecture-contract 按实际英文 Table D-1 各字段建模，保留原文冲突记录。"),
    "G212:L71": (15, "[Bucy et al., 2016]", "英文参考文献有 Bucy、Dasgupta & Wendler、G18A、Morgan、Tomaschek 五项，中文参考表未列。", "文献列表不直接生成能力；引用这五项时须返回英文页。"),
    "G212:L250": (26, "Table 4-1: Factor Categorization", "三类定义与 15 个因素可在原表核对；中文后续图标签和译者补写段不能自动当原文规则。", "dtra-readiness-method 的因素集合可沿用，图依赖和评分规则仍单独复核。"),
    "G212:L667": (46, "Table 6-1: Architectural Implications", "中文 6.1 明示为译者从表 6-1 归纳，部分阶段的因素分派是推论，不是英文逐句规则。", "DTRA 阶段映射应标为项目解释，并逐行引用原表。"),
    "G212:L747": (49, "The questionnaire is to be answered using the Likert scale provided in Figure A-1", "英文 A.2 问卷没有“1–7 分、1–5 列管理关注”的作答指令；中文 L749 为增补。", "问卷入口不得把数字和阈值标为英文规定。"),
    "G212:T73": (15, "[Dasgupta &", "中文参考表比英文少五项；不是可直接用于方法评分的来源表。", "只保留参考文献缺项，不影响既有项目计算规则的独立声明。"),
    "G21D:L11": (7, "The mission of The Open Group", "中文前言是节译，省略使命四条及关于系列指南的说明。", "政府参考模型能力定义以正文与英文表图为准，前言摘要不算定义核对。"),
    "G21D:L57": (9, "are registered trademarks", "英文明确 ArchiMate、TOGAF、The Open Group 为 The Open Group 注册商标；中文泛称归各自所有者。", "商标说明不授任何模板定义通过。"),
    "G21D:L63": (13, "ACCA, 2016: 50 Drivers of Change in the Public Sector", "英文 ACCA 条目的机构名称与中文 L69“英格兰及威尔士特许会计师协会”不符；其他 57 项未在此逐字段重核。", "参考文献名称按英文登记；本条不闭合其余参考表字段。"),
    "G233:L11": (8, "Intended Audience", "英文前言列业务规划者、企业架构师、业务架构师、业务分析师、系统分析师的用途；中文前言未列。", "能力规划使用角色不能从中文前言的省略推定。"),
    "G233:T378": (28, "Customer", "英文 Table 4-1 最后一行只显示 Customer 信息对象且源、目标格留空；中文补“同上”并增第四行，属解释。", "interface-catalog 不得自动继承上一行源应用或目标应用。"),
    "G242:L11": (8, "This Document", "中文前言只保留摘要，英文的 This Document、About、Terminology、Conventions 未完整翻译。", "数字可持续能力定义由具体正文和图表核，不用前言摘要代替。"),
    "G242:L161": (21, "181", "英文有 2%、3.5%、6%、181 ZB 和 5.5 times 等叙述；中文 L183 的“多 5.5 倍”有数量口径歧义，原文也有表述问题。", "背景统计不可当项目阈值或推导规则。"),
    "G242:L250": (25, "recycling rate above 50 per cent", "英文脚注为 recycling rate，中文 L254 写“可回收率”，混淆实际回收与技术可回收性。", "材料循环指标须区分实际回收率和可回收潜力。"),
    "G242:L310": (27, "sufficiency decisions", "英文 sufficiency 在此指足够性或需求约束判断，中文 L323 译“节制”，与 sobriety 概念混用。", "环境决策方法保留英文术语和业务判据，不能按译词自动合并。"),
    "G242:L1393": (77, "Figure 3-13 shows an example of a template", "英文正文将可持续评审模板误称 Figure 3-13，紧接图注实际为 Figure 3-14；中文沿用错误指号。", "sustainability-review-canvas 应绑定 Figure 3-14；表 3-5 混合单位另行核算，不自动修正原表。"),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    base = json.loads(BASE.read_text())
    assert len(base["deviations"]) == 26
    assert set(OBSERVATIONS) == {x["source_id"] for x in base["deviations"] if not x["current_semantic_observation"]}
    for row in base["deviations"]:
        sid = row["source_id"]
        if sid not in OBSERVATIONS:
            row["followup_status"] = "previous-bounded-observation-retained"
            continue
        page, phrase, observation, consequence = OBSERVATIONS[sid]
        matched = next((a for a in row["english_assets"] if a["page"] == page), None)
        assert matched, (sid, page)
        path = ROOT / matched["path"]
        assert sha(path) == matched["sha256"], sid
        if phrase:
            assert phrase.casefold() in path.read_text().casefold(), (sid, phrase)
        row["followup_english_locator"] = {"page": page, "asset": matched, "exact_anchor": phrase or "image-only English Table B-1"}
        if sid == "G186:L2080":
            crop = PACKAGE / "original-crops/G186-tabB-1-p151-0.png"
            row["followup_opened_image"] = {"path": str(crop.relative_to(ROOT)), "sha256": sha(crop)}
        row["current_semantic_observation"] = observation
        row["capability_consequence"] = consequence
        row["current_semantic_status"] = "bounded-deviation-rechecked-against-project-English"
        row["followup_status"] = "bounded-difference-disposition-recorded; full-source-and-capability-acceptance-pending"
    run_id = uuid.uuid4().hex
    result = {
        "schema_version": "source-priority-recheck/2",
        "run_id": run_id,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "scope": "26 recorded deviations only; English PDF page extracts are project-local; no full entry or table acceptance",
        "inputs_sha256": {str(p.relative_to(ROOT)): sha(p) for p in (BASE, PACKAGE / "manifest.json", Path(__file__))},
        "counts": {"deviations": 26, "bounded_rechecked": 26, "full_semantic_acceptance": 0},
        "deviations": base["deviations"],
        "route_reference_diagnostics": base["route_reference_diagnostics"],
        "no_direct_route_figures": base["no_direct_route_figures"],
        "accepted": False,
        "limit": "逐项偏差的限定裁定不等于 1,667 节表的全文、逐字段核对或七维通过；原来的六项观察和旧记录保留。",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    (REV / "source-priority-recheck-followup-2026-11-03-run.json").write_text(json.dumps({
        "run_id": run_id, "command": "python3 skills/_shared/scripts/complete_source_priority_recheck.py",
        "exit_code": 0, "inputs_sha256": result["inputs_sha256"],
        "output": str(OUT.relative_to(ROOT)), "output_sha256": sha(OUT),
    }, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
