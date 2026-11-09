#!/usr/bin/env python3
"""Explicit definition/question bridge; never infer identity from entity types."""
import argparse
from collections import Counter
from datetime import datetime, timezone

from audit_source_current import ROOT, DEFAULT_DECISIONS, load_decisions, registries, sha, write_new


def build(decisions_path=None):
    registry = registries()
    decisions = load_decisions(decisions_path, registry)
    rows = []
    for decision in decisions["bridge"]:
        artifact = registry["artifact"][decision["artifact_id"]]
        profiles = [p for p in registry["profile"].values() if p["artifact_id"] == artifact["id"]]
        guide = [p["id"] for p in profiles if not p["id"].startswith("compat-")]
        verified = [p["id"] for p in profiles if (p.get("template") or {}).get("source_verified") is True]
        rows.append({**decision, "g248_artifact_id": artifact["id"],
                     "g248_artifact_name_en": artifact.get("name_en"), "g248_artifact_name_zh": artifact.get("name_zh"),
                     "artifact_question": artifact.get("question"), "g248_source_locator": artifact.get("source_locator"),
                     "definition_status": artifact.get("definition_status"),
                     "work_product_questions": {wid: registry["work-product"][wid].get("decision") for wid in decision["work_product_ids"]},
                     "view_profiles": {"guide_specific": guide, "compat_only": [p["id"] for p in profiles if p["id"].startswith("compat-")],
                                       "has_guide_specific_profile": bool(guide), "has_source_verified_profile": bool(verified)},
                     "review_status": "review-required" if decision["relation"] != "insufficient-material" else "insufficient-material",
                     "semantic_acceptance": False})
    inverse = []
    for wid, product in registry["work-product"].items():
        linked = [r for r in rows if wid in r["work_product_ids"]]
        inverse.append({"work_product_id": wid, "decision": product.get("decision"), "source_refs": product.get("source_refs"),
                        "artifact_ids": [r["artifact_id"] for r in linked], "relations": {r["artifact_id"]: r["relation"] for r in linked},
                        "reuse_or_extension_artifact_ids": [r["artifact_id"] for r in linked if r["relation"] in ("reuse", "extension", "same-concept")],
                        "review_status": "review-required" if linked else "insufficient-material",
                        "closure_condition": "没有基本制品配对不等于缺少能力；需按指南定义决定是否独立扩展，不能靠实体类型补配对。"})
    return {"schema_version": "artifact-bridge/2", "generated_at": datetime.now(timezone.utc).isoformat(),
            "audit_complete": True, "acceptance_granted": False,
            "notice": "显式项目阅读桥接；reuse/extension/distinct均非英文定义符合性或专业通过。无资料不推断distinct。",
            "relation_definitions": {
                "reuse": "可复用同一操作概念/ID，但仍须逐字段专业复核；未断言注册制品与工作产品完全复用。",
                "extension": "特定范围、字段或视角的条件性扩展；不声称WP完整实现基本制品，差异与不覆盖项见reason。",
                "distinct": "只裁定列出的具体候选对解决不同问题；可作为彼此输入，不推断全部工作产品均无关。",
                "insufficient-material": "缺少可裁定的正式定义比较；未配对仍可复用基本制品，不要求补WP。",
                "same-concept": "需正式定义、问题范围及字段差异的比较材料；通过结构验证也不是语义通过，本轮未断言。",
            },
            "counting_rule": f"{len(registry['artifact'])}基本制品与{len(registry['work-product'])}扩展WP为{len(set(registry['artifact']) | set(registry['work-product']))}个唯一注册family，不等于同数量的独立业务能力；配对边与指南引用次数另计，交付物不相加。",
            "inputs_sha256": {p: sha(ROOT / p) for p in ("artifacts.json", "capabilities.json", "deliverables.json")},
            "decisions_sha256": sha(decisions_path or DEFAULT_DECISIONS),
            "measured_facts": {"g248_artifacts": len(registry["artifact"]), "work_products": len(registry["work-product"]),
                               "artifact_families": len(set(registry["artifact"]) | set(registry["work-product"])),
                               "appendix_b_deliverables": len(registry["deliverable"]),
                               "explicit_comparison_edges": sum(len(r["work_product_ids"]) for r in rows),
                               "reuse_or_extension_edges": sum(len(r["work_product_ids"]) for r in rows if r["relation"] in ("reuse", "extension", "same-concept")),
                               "work_products_with_explicit_comparison": sum(bool(r["artifact_ids"]) for r in inverse),
                               "work_products_with_reuse_or_extension": sum(bool(r["reuse_or_extension_artifact_ids"]) for r in inverse),
                               "work_products_without_comparison": sum(not r["artifact_ids"] for r in inverse), "semantic_passes": 0},
            "relation_counts": dict(Counter(r["relation"] for r in rows)), "records": rows, "work_product_records": inverse,
            "limits": ["G248附录A列名不提供完整正式字段定义；当前字段是项目操作契约，不能冒充标准条款。", "结构验证仅检查ID、理由及最小比较证据，不批准映射语义。"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out")
    parser.add_argument("--decisions", default=str(DEFAULT_DECISIONS))
    args = parser.parse_args()
    result = build(args.decisions)
    out = args.out or ROOT / f"reviews/source-current/run-bridge-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}.json"
    write_new(out, result)
    print(result["measured_facts"], result["relation_counts"], str(out))


if __name__ == "__main__":
    main()
