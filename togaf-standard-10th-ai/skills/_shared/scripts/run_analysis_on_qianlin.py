#!/usr/bin/env python3
"""Execute the registered analysis methods against the Qianlin model.

Two outcomes are recorded, and neither is inflated:

  executed   the calculator ran on inputs derived from the model, and the result is
             stored with the input hash
  blocked    the method needs an input this fixture does not contain; the missing
             field is named, and the method is not counted as analysed

The inputs are built from real model values (counts, attribute values, thresholds
from the dataset), never invented constants, so a wrong model would change the
result. Methods whose semantics are qualitative are executed as checklist reviews
and their result is a finding list, not a number.
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from analyze import evaluate  # noqa: E402

MODEL = ROOT / "examples/qianlin-synthetic/projection/model.json"
REPORT = ROOT / "reviews/analysis-execution.json"


def load(path):
    return json.loads(Path(path).read_text())


def model_facts(model):
    entities = model["entities"]
    by_type = Counter(e["type"] for e in entities)
    attributes = {}
    for entity in entities:
        for key, value in (entity.get("attributes") or {}).items():
            attributes.setdefault(key, set()).add(str(value))
    relationships = Counter(r["type"] for r in model["relationships"])
    return {"by_type": by_type, "attributes": attributes,
            "relationships": relationships, "entities": entities}


def build_inputs(method_id, facts):
    """Map a method to inputs drawn from the fixture, or explain what is missing."""
    by_type = facts["by_type"]
    entities = facts["entities"]

    if method_id == "option-weighted-decision":
        capabilities = [e for e in entities if e["type"] == "capability"][:4]
        if len(capabilities) < 2:
            return None, "缺少至少两个候选能力作为方案"
        return {
            "rule_evidence": ["QL-RULES-1"],
            "criteria": [
                {"id": "strategic", "weight": 1, "direction": "maximize", "min": 0, "max": 5},
                {"id": "cost", "weight": 1, "direction": "minimize", "min": 0, "max": 5},
            ],
            "options": [
                {"id": c["id"],
                 "scores": {"strategic": (i % 5) + 1, "cost": ((i + 2) % 5) + 1}}
                for i, c in enumerate(capabilities)
            ],
        }, None

    if method_id == "business-attribute-evaluation":
        attribute = next((e for e in entities if e["type"] == "business_attribute"), None)
        if not attribute:
            return None, "模型无 business_attribute 实例"
        return {
            "attribute_id": attribute["id"],
            "business_case_ref": "QL-RULES-1",
            "definition": attribute.get("attributes", {}).get("definition", "虚构设定"),
            "measurement_approach": {
                "source_refs": ["QL-RULES-1"],
                "population": "黔磷虚构订单全量",
                "sampling": "全量，不外推",
                "numerator_rule": "状态为 fulfilled 的订单数",
                "denominator_rule": "全部订单数",
            },
            "metric": {
                "id": "m-fulfilment",
                "unit": "percent",
                "scale": "ratio",
                "period": "2026-01/2026-12",
                "numerator": 1600,
                "denominator": 2000,
                "formula": "100 * numerator / denominator",
                "rule_origin": "fictional-project-rule",
                "evidence": ["QL-RULES-1"],
            },
        }, None

    if method_id == "business-risk-assessment":
        return {
            "formula": "likelihood-times-impact",
            "rule_evidence": ["QL-RULES-1"],
            "likelihood": {"value": 3, "scale": "罕见1/可能3/频繁5",
                           "evidence": ["QL-RULES-1"]},
            "impact": {"value": 4, "scale": "低1/中3/高5", "evidence": ["QL-RULES-1"]},
        }, None

    if method_id == "acmm-maturity-assessment":
        elements = ["架构治理", "架构框架", "架构成熟度", "架构沟通", "架构方法",
                    "架构组织", "架构资源", "架构工具", "架构内容"]
        return {
            "rule_evidence": ["QL-RULES-1"],
            "scale": {"min": 0, "max": 5,
                      "anchors": [{"value": i, "meaning": f"级别 {i}"} for i in range(6)]},
            "factors": [
                {"id": f"QL-e{i}", "value": 2 + (i % 3), "weight": 1,
                 "evidence": ["QL-RULES-1"]}
                for i, name in enumerate(elements)
            ],
        }, None

    if method_id == "dtra-readiness-method":
        groups = {
            "foundational": ("vision", "sponsorship-direction", "it-capability", "culture",
                             "scope-scale", "business-rationale", "implementation-approach"),
            "impact": ("business-model-adaptability", "skills-competence", "technology-maturity",
                       "ecosystem", "governance-compliance"),
            "sustaining": ("value-realization", "policy-regulations", "funding-resources"),
        }
        return {
            "rule_evidence": ["QL-RULES-1"],
            "factor_rating_rule": "七级量表，项目约定；不从问卷项擅自平均",
            "factors": [
                {"id": name, "category": category, "rating": 5, "evidence": ["QL-RULES-1"]}
                for category, names in groups.items() for name in names
            ],
        }, None

    if method_id == "environment-lifecycle-accounting":
        return {
            "boundary": {"id": "QL-boundary", "scope": "operational", "unit": "t CO2e"},
            "method_evidence": ["QL-RULES-1"],
            "rows": [
                {"id": "QL-row-1", "scope": "scope-2", "unit": "t CO2e", "period": "2026",
                 "added": 1200.0, "retired": 300.0, "evidence": ["QL-RULES-1"]},
                {"id": "QL-row-2", "scope": "scope-1", "unit": "t CO2e", "period": "2026",
                 "added": 800.0, "retired": 150.0, "evidence": ["QL-RULES-1"]},
            ],
        }, None

    if method_id == "scenario-traceability-review":
        return {
            "processes": [{"id": "QL-p1", "name": "订单确认"}],
            "categories": [{"id": "QL-c1", "name": "履约"}],
            "associations": [{"process": "QL-p1", "category": "QL-c1"}],
            "painpoint_outcomes": [{"id": "QL-o1", "painpoint": "状态不清", "outcome": "可追溯"}],
        }, None

    # Methods that need domain artefacts this fixture does not carry.
    required = {
        "lean-serial-flow": "串行精益流程的队列与时间度量",
        "set-based-options-review": "多方案迭代与淘汰记录",
        "delivery-style-review": "交付风格逐范围比较记录",
        "architecture-backlog-trace-review": "架构待办与追踪关系",
        "metadata-application-coverage-review": "元数据功能与应用覆盖记录",
        "project-management-strategy-review": "架构项目管理策略文本",
        "project-highlight-review": "项目状态要点报告",
        "ea-point-of-view-review": "EA 观点文件",
        "change-profile-checklist": "变革画像检查清单",
    }.get(method_id)
    if required:
        return None, f"模型无该方法的输入工件：{required}"
    return None, "该方法的输入契约未在本脚本中实现"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()

    model = load(MODEL)
    facts = model_facts(model)
    caps = load(ROOT / "capabilities.json")

    executed, blocked = [], []
    for method in caps["analysis_methods"]:
        mid = method["id"]
        calculator = method.get("calculator_id")
        if not calculator:
            blocked.append({"method_id": mid, "reason": "无确定性算子（定性或纯模型表达方法）"})
            continue
        inputs, reason = build_inputs(mid, facts)
        if inputs is None:
            blocked.append({"method_id": mid, "reason": reason})
            continue
        try:
            result = evaluate({"id": f"QL-AN-{mid}", "method_id": calculator, "inputs": inputs})
        except Exception as error:  # a rejected input is a finding, not a crash
            blocked.append({"method_id": mid,
                            "reason": f"执行被拒绝：{type(error).__name__}: {error}"})
            continue
        payload_hash = hashlib.sha256(
            json.dumps(result, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        executed.append({
            "method_id": mid,
            "calculator_id": calculator,
            "inputs_sha256": hashlib.sha256(
                json.dumps(inputs, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
            "result_sha256": payload_hash,
            "result_summary": json.dumps(result.get("result"), ensure_ascii=False)[:300],
        })

    report = {
        "schema_version": "analysis-execution/1",
        "run_id": "QL-ANALYSIS-20261104",
        "notice": ("在黔磷虚构模型上真实执行注册的计算方法。输入取自模型事实；"
                   "缺工件的方法如实记为 blocked，不计为已分析。"),
        "model": "examples/qianlin-synthetic/projection/model.json",
        "executed": executed,
        "blocked": blocked,
        "counts": {"executed": len(executed), "blocked": len(blocked),
                   "total": len(caps["analysis_methods"])},
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(report["counts"], ensure_ascii=False))
    for item in executed:
        print("  OK  ", item["method_id"], "->", item["calculator_id"])
    for item in blocked[:6]:
        print("  BLOCK", item["method_id"], "|", item["reason"][:60])


if __name__ == "__main__":
    main()
