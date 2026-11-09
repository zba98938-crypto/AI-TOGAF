#!/usr/bin/env python3
"""Current source inventory: traceability and applicability, never semantic approval."""
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DECISIONS = ROOT / "reviews/source-current/run-route-decisions-v1.json"


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def registries():
    caps = read(ROOT / "capabilities.json")
    return {
        "artifact": {a["id"]: a for a in read(ROOT / "artifacts.json")["artifacts"]},
        "work-product": {w["id"]: w for w in caps.get("work_products", []) + caps.get("base_work_product_bindings", [])},
        "profile": {p["id"]: p for p in caps.get("profiles", [])},
        "method": {m["id"]: m for m in caps.get("analysis_methods", [])},
        "deliverable": {d["id"]: d for d in read(ROOT / "deliverables.json")["deliverables"]},
    }


def validate_destination(destination, registry):
    kind, ident = destination.get("kind"), destination.get("id")
    if ident not in registry.get(kind, {}):
        raise ValueError(f"unknown destination: {kind}:{ident}")
    if "chapter" in destination:
        chapters = {s["title"] for s in registry[kind][ident].get("sections", [])}
        if destination["chapter"] not in chapters:
            raise ValueError(f"unknown destination chapter: {ident}/{destination['chapter']}")


def validate_decisions(data, registry):
    ids = [r["artifact_id"] for r in data["bridge"]]
    if len(ids) != len(set(ids)) or set(ids) != set(registry["artifact"]):
        raise ValueError("bridge must retain every artifact exactly once")
    figures = {f["id"] for f in read(ROOT / "evidence-registry.json")["figures"]}
    guides = {e.get("guide") for e in read(ROOT / "reviews/source-coverage-unified.json")["source_entries"]}
    for group in ("bridge", "guide_routes", "figure_dispositions", "legacy_reference_aliases", "source_role_rules"):
        seen = set()
        for row in data[group]:
            key = row.get("artifact_id") or row.get("guide") or row.get("figure_id") or row.get("legacy_ref") or row.get("disposition")
            if key in seen:
                raise ValueError(f"duplicate decision: {key}")
            seen.add(key)
            if not str(row.get("reason", "")).strip():
                raise ValueError(f"empty reason: {key}")
            if not row.get("source_refs") or not row.get("closure_condition"):
                raise ValueError(f"missing provenance or closure condition: {key}")
            if group == "guide_routes" and key not in guides:
                raise ValueError(f"unknown guide: {key}")
            if group == "figure_dispositions" and key not in figures:
                raise ValueError(f"unknown figure: {key}")
            for dest in row.get("destinations", []):
                validate_destination(dest, registry)
                if dest.get("kind") == "deliverable" and dest.get("mandatory") is not False:
                    raise ValueError("guide chapter options must be explicitly non-mandatory")
            for wid in row.get("work_product_ids", []):
                validate_destination({"kind": "work-product", "id": wid}, registry)
            if group == "bridge":
                if row["relation"] not in {"reuse", "extension", "distinct", "insufficient-material", "same-concept"}:
                    raise ValueError(f"unknown bridge relation: {key}")
                if row["relation"] in {"reuse", "extension", "same-concept"} and not row.get("work_product_ids"):
                    raise ValueError(f"relation requires a work product: {key}")
                if row["relation"] == "same-concept":
                    comp = row.get("definition_comparison", {})
                    if any(not comp.get(k) for k in ("artifact_definition", "work_product_definition", "decision_scope", "field_comparison", "differences", "reviewer_evidence")):
                        raise ValueError(f"same-concept lacks definition comparison: {key}")
    return data


def load_decisions(path=None, registry=None):
    return validate_decisions(read(path or DEFAULT_DECISIONS), registry or registries())


def validate_counts(matrix, registry):
    names = {"work_products": "work-product", "artifacts": "artifact", "analysis_methods": "method", "view_profiles": "profile", "deliverables": "deliverable"}
    for column, kind in names.items():
        if matrix["totals"][column] != len(registry[kind]):
            raise ValueError(f"incorrect unique count: {column}")


def resolve_ref(ref, registry):
    return [{"kind": k, "id": ref} for k, rows in registry.items() if ref in rows]


def build(decisions_path=None):
    registry = registries()
    decisions = load_decisions(decisions_path, registry)
    coverage = read(ROOT / "reviews/source-coverage-unified.json")
    figures = {f["id"]: f for f in read(ROOT / "evidence-registry.json")["figures"]}
    caps = read(ROOT / "capabilities.json")
    current_figures = {f["id"]: f for f in caps.get("figure_profiles", [])}
    explicit = {f["figure_id"]: f for f in decisions["figure_dispositions"]}
    guides = {g["guide"]: g for g in decisions["guide_routes"]}
    aliases = {a["legacy_ref"]: a for a in decisions["legacy_reference_aliases"]}
    role_rules = {r["disposition"]: r for r in decisions["source_role_rules"]}
    records, seen = [], set()
    for entry in coverage["source_entries"]:
        sid = entry["source_id"]
        if sid in seen:
            raise ValueError(f"duplicate indexed source_id: {sid}")
        seen.add(sid)
        gid = entry.get("guide") or sid.split("/")[0]
        destinations, unresolved, applied_aliases = [], [], []
        refs = set(entry.get("capability_refs", []) + entry.get("resolved_capability_refs", []))
        for ref in sorted(refs):
            found = resolve_ref(ref, registry)
            if not found and ref in aliases:
                found = aliases[ref]["destinations"]
                applied_aliases.append(aliases[ref])
            destinations.extend(found)
            if not found:
                unresolved.append(ref)
        disposition = explicit.get(sid)
        role_rule = role_rules.get(entry.get("disposition"))
        if sid in figures:
            figure = current_figures.get(sid, {})
            for field, kind in (("profile_ids", "profile"), ("method_ids", "method")):
                for ident in figure.get(field, []):
                    dest = {"kind": kind, "id": ident}
                    validate_destination(dest, registry)
                    destinations.append(dest)
        if disposition:
            destinations.extend(disposition.get("destinations", []))
        # Conditional guide options are not section-level definition claims.
        options = [] if role_rule else guides.get(gid, {}).get("destinations", [])
        destinations = list({(d["kind"], d["id"], d.get("chapter")): d for d in destinations}.values())
        status = "review-required" if destinations or options or role_rule or (disposition and disposition.get("role") == "non-template") else "insufficient-material"
        records.append({"source_id": sid, "guide": gid, "record_type": entry["record_type"],
                        "original_index_entry": entry, "destinations": destinations,
                        "conditional_guide_options": options, "unresolved_legacy_refs": unresolved,
                        "applied_legacy_aliases": applied_aliases,
                        "applicability_rule": role_rule,
                        "figure_disposition": disposition, "review_status": status, "semantic_acceptance": False,
                        "observation": (disposition or {}).get("reason") or entry.get("summary") or entry.get("reason") or "索引保留；尚无逐条定义观察。",
                        "closure_condition": (disposition or role_rule or {}).get("closure_condition") or "责任人逐条核对英文定义、决策问题、范围与字段；补原文定位和差异处置。读过/引用命中/存在路由均不构成通过。"})
    if {r["source_id"] for r in records if r["record_type"] == "figure-json-and-assets"} != set(figures):
        raise ValueError("indexed figures differ from evidence registry")
    return {"schema_version": "source-current/1", "generated_at": datetime.now(timezone.utc).isoformat(),
            "audit_complete": True, "acceptance_granted": False,
            "notice": "逐条保留历史来源与当前路由；仅适用性/最小证据约束，不自动签署专业符合性。条件性章节不是mandatory要求。",
            "inputs_sha256": {p: sha(ROOT / p) for p in ("capabilities.json", "artifacts.json", "deliverables.json", "evidence-registry.json", "reviews/source-coverage-unified.json")},
            "decisions_sha256": sha(decisions_path or DEFAULT_DECISIONS),
            "counts": {"indexed_items": len(records), "by_kind": dict(Counter(r["record_type"] for r in records)),
                       "by_review_status": dict(Counter(r["review_status"] for r in records)), "semantic_passes": 0,
                       "items_with_unresolved_legacy_refs": sum(bool(r["unresolved_legacy_refs"]) for r in records),
                       "items_with_explicit_legacy_aliases": sum(bool(r["applied_legacy_aliases"]) for r in records),
                       "items_with_non_template_role_rule": sum(bool(r["applicability_rule"]) for r in records)},
            "figure_disposition_counts": {"historical_unrouted": sum(r["cohort"] == "historical-unrouted" for r in decisions["figure_dispositions"]),
                                          "historical_anomalies": sum(r["cohort"] == "historical-anomaly" for r in decisions["figure_dispositions"]),
                                          "non_template_roles": sum(r.get("role") == "non-template" for r in decisions["figure_dispositions"]), "semantic_passes": 0},
            "figure_dispositions": decisions["figure_dispositions"], "records": records}


def write_new(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def write_bundle(directory):
    """One reproducible, append-only run; no renderer or full regression execution."""
    from build_artifact_bridge import build as build_bridge
    from build_routing_matrix import build as build_routes
    from audit_structural_gaps import build_source_routes_only
    from build_skill_backlog import build as build_backlog

    inputs = [ROOT / p for p in ("capabilities.json", "artifacts.json", "deliverables.json", "evidence-registry.json", "reviews/source-coverage-unified.json", "metamodel.json")]
    inputs += [DEFAULT_DECISIONS]
    scripts = ["audit_source_current.py", "build_artifact_bridge.py", "build_routing_matrix.py", "audit_structural_gaps.py", "build_skill_backlog.py"]
    inputs += [ROOT / "scripts" / p for p in scripts]
    before = {str(p.relative_to(ROOT)): sha(p) for p in inputs}
    results = {"source-current": build(), "artifact-bridge": build_bridge(), "routing-matrix": build_routes(),
               "source-route-gaps": build_source_routes_only(), "skill-backlog": build_backlog()}
    if before != {str(p.relative_to(ROOT)): sha(p) for p in inputs}:
        raise RuntimeError("source/registry changed during audit; retry under a new run directory")
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    for name, value in results.items():
        write_new(directory / (name + ".json"), value)
    source, bridge, routes = (results[k] for k in ("source-current", "artifact-bridge", "routing-matrix"))
    summary = {"schema_version": "source-route-run/1", "run_dir": str(directory), "acceptance_granted": False,
               "inputs_sha256": before, "source": source["counts"], "figures": source["figure_disposition_counts"],
               "bridge": bridge["relation_counts"], "bridge_facts": bridge["measured_facts"],
               "routes": routes["totals"], "guide_reference_counts": routes["guide_reference_counts"],
               "zero_rows": routes["zero_rows"], "structural": results["source-route-gaps"]["summary"],
               "remaining_conditions": ["1910项均未获自动专业通过；逐条正式定义/适用性与字段差异需责任人独立评审。",
                                        "基本制品资料不足及扩展WP无比较项须补定义或明确blocked；不能为消零新建重复WP。",
                                        "18异常图保留原处置和目标，按closure_condition核对英文节点、关系/标签及视觉结构。",
                                        "12指南章节仅可选，交付物责任人须按范围确认；11非模板图保留说明角色，不要求UI/照片复刻。"],
               "outputs_sha256": {p.name: sha(p) for p in directory.glob("*.json")}}
    write_new(directory / "run-summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out")
    parser.add_argument("--bundle", action="store_true", help="write all five current audits under a new --out directory")
    parser.add_argument("--decisions", default=str(DEFAULT_DECISIONS))
    args = parser.parse_args()
    if args.bundle:
        if Path(args.decisions) != DEFAULT_DECISIONS:
            parser.error("--bundle currently requires the default explicit decisions file")
        directory = args.out or ROOT / f"reviews/source-current/run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}"
        print(json.dumps(write_bundle(directory), ensure_ascii=False, indent=2))
        return
    result = build(args.decisions)
    out = args.out or ROOT / f"reviews/source-current/run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}/source-current.json"
    write_new(out, result)
    print(json.dumps({"out": str(out), **result["counts"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
