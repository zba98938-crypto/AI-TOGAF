#!/usr/bin/env python3
"""Current routes with explicit basic-artifact reuse and optional chapter choices.

Unique registered IDs are not guide-reference edges and neither is a count of
independent business capabilities. Route presence never grants acceptance.
"""
import argparse
import re
from datetime import datetime, timezone

from audit_source_current import ROOT, DEFAULT_DECISIONS, load_decisions, read, registries, sha, validate_counts, write_new

GUIDE_RE = re.compile(r"(G[0-9]{2}[0-9A-Z])")


def guides_of(refs):
    return {m.group(1) for ref in refs or [] for m in GUIDE_RE.finditer(str(ref))}


def guide_ids():
    coverage = read(ROOT / "reviews/source-coverage-unified.json")
    return sorted({e.get("guide") or e["source_id"].split("/")[0] for e in coverage["source_entries"]})


def build(decisions_path=None):
    registry = registries()
    decisions = load_decisions(decisions_path, registry)
    coverage = read(ROOT / "reviews/source-coverage-unified.json")
    caps = read(ROOT / "capabilities.json")
    evidence = read(ROOT / "evidence-registry.json")
    ids = guide_ids()
    index = {gid: {"guide": gid, "sections": 0, "tables": 0, "figures": 0,
                   "figure_routes": 0, "figure_unrouted": [], "figure_non_template": [], "figure_unresolved": [],
                   "work_products": [], "analysis_methods": [], "view_profile_ids": [],
                   "view_profiles_guide_specific": 0, "view_profiles_compat": 0,
                   "deliverables": [], "artifact_ids": [], "base_artifact_reuse_ids": [],
                   "deliverable_options": [], "applicability_decision": None} for gid in ids}
    for entry in coverage["source_entries"]:
        gid = entry.get("guide")
        if gid in index and entry["record_type"] in ("section", "table"):
            index[gid][entry["record_type"] + "s"] += 1
    route_by_figure = {f["id"]: f for f in caps.get("figure_profiles", [])}
    disposition_by_figure = {f["figure_id"]: f for f in decisions["figure_dispositions"]}
    for figure in evidence["figures"]:
        row = index[figure["guide"]]
        row["figures"] += 1
        route = route_by_figure.get(figure["id"], {})
        if route.get("profile_ids") or route.get("method_ids"):
            row["figure_routes"] += 1
        else:
            row["figure_unrouted"].append(figure["id"])
            disposition = disposition_by_figure.get(figure["id"], {})
            field = "figure_non_template" if disposition.get("role") == "non-template" else "figure_unresolved"
            row[field].append(figure["id"])
    for kind, field, refs in (("work-product", "work_products", "source_refs"),
                              ("method", "analysis_methods", "source_refs"),
                              ("profile", "view_profile_ids", "source_refs"),
                              ("deliverable", "deliverables", "sources"),
                              ("artifact", "artifact_ids", "sources")):
        for ident, record in registry[kind].items():
            source_refs = list(record.get(refs) or [])
            if kind == "artifact":
                source_refs += list(record.get("source_refs") or [])
            for gid in guides_of(source_refs):
                if gid in index:
                    index[gid][field].append(ident)
    for decision in decisions["guide_routes"]:
        row = index[decision["guide"]]
        row["applicability_decision"] = decision
        row["base_artifact_reuse_ids"] = sorted({d["id"] for d in decision["destinations"] if d["kind"] == "artifact"})
        row["deliverable_options"] = [d for d in decision["destinations"] if d["kind"] == "deliverable"]
    for row in index.values():
        for field in ("work_products", "analysis_methods", "view_profile_ids", "deliverables", "artifact_ids"):
            row[field] = sorted(set(row[field]))
        row["work_products_count"] = len(row["work_products"])
        row["analysis_methods_count"] = len(row["analysis_methods"])
        row["deliverables_count"] = len(row["deliverables"])
        row["artifacts"] = len(row["artifact_ids"])
        row["view_profiles"] = len(row["view_profile_ids"])
        row["view_profiles_compat"] = sum(p.startswith("compat-") for p in row["view_profile_ids"])
        row["view_profiles_guide_specific"] = row["view_profiles"] - row["view_profiles_compat"]
        row["figures_unrouted_count"] = len(row["figure_unrouted"])
        # A registered basic artifact with guide-specific profiles is a valid
        # destination, not a reason to create a duplicate extension WP.
        guide_profile_families = {registry["profile"][pid]["artifact_id"] for pid in row["view_profile_ids"] if not pid.startswith("compat-")}
        row["effective_capability_destination_ids"] = sorted(set(row["work_products"]) | set(row["base_artifact_reuse_ids"]) | guide_profile_families)
        row["route_review_status"] = "review-required"
    zero = {"no_work_products": [g for g in ids if not index[g]["work_products"]],
            "no_deliverables": [g for g in ids if not index[g]["deliverables"]],
            "no_analysis_methods": [g for g in ids if not index[g]["analysis_methods"]],
            "no_view_profiles": [g for g in ids if not index[g]["view_profile_ids"]],
            "no_capability_destination": [g for g in ids if not index[g]["effective_capability_destination_ids"]],
            "no_deliverable_destination_or_reason": [g for g in ids if not index[g]["deliverables"] and not index[g]["deliverable_options"]]}
    totals = {"guides": len(ids), "sections": sum(r["sections"] for r in index.values()),
              "tables": sum(r["tables"] for r in index.values()), "figures": len(evidence["figures"]),
              "figure_routes": sum(r["figure_routes"] for r in index.values()),
              "figures_unrouted": sum(len(r["figure_unrouted"]) for r in index.values()),
              "figures_non_template": sum(len(r["figure_non_template"]) for r in index.values()),
              "figures_unresolved": sum(len(r["figure_unresolved"]) for r in index.values()),
              **{k: len(registry[v]) for k, v in {"work_products": "work-product", "analysis_methods": "method", "view_profiles": "profile", "deliverables": "deliverable", "artifacts": "artifact"}.items()}}
    reference_counts = {col: sum(len(r[field]) for r in index.values()) for col, field in {"work_products": "work_products", "analysis_methods": "analysis_methods", "view_profiles": "view_profile_ids", "deliverables": "deliverables", "artifacts": "artifact_ids"}.items()}
    result = {"schema_version": "guide-routing-matrix/2", "generated_at": datetime.now(timezone.utc).isoformat(),
              "audit_complete": True, "acceptance_granted": False,
              "notice": "条件性章节建议/基本制品复用不改变注册表，零扩展WP不等于零能力。无路由图按非模板角色逐项说明；不自动签署专业符合性。",
              "counting_rule": "totals为注册表唯一ID数；guide_reference_counts为去重的指南→ID边数，不能当能力数或相加。",
              "inputs_sha256": {p: sha(ROOT / p) for p in ("capabilities.json", "artifacts.json", "deliverables.json", "reviews/source-coverage-unified.json", "evidence-registry.json")},
              "decisions_sha256": sha(decisions_path or DEFAULT_DECISIONS),
              "totals": totals, "extension_work_products": len(caps["work_products"]), "base_work_product_bindings": len(caps.get("base_work_product_bindings", [])), "guide_reference_counts": reference_counts, "zero_rows": zero,
              "guides": [index[g] for g in ids],
              "limits": ["引用/路由存在不表示定义、图形或项目专业通过。", "no_deliverables仍保留注册表sources的实际零行；条件性章节另列，不伪造source_ref。"]}
    validate_counts(result, registry)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out")
    parser.add_argument("--decisions", default=str(DEFAULT_DECISIONS))
    args = parser.parse_args()
    result = build(args.decisions)
    out = args.out or ROOT / f"reviews/source-current/run-routing-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}.json"
    write_new(out, result)
    print(result["totals"], result["zero_rows"], str(out))


if __name__ == "__main__":
    main()
