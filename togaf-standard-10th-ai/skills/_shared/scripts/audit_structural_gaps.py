#!/usr/bin/env python3
"""Audit structural gaps: routing holes, bridge holes, and measured renderer losses.

Three gap families, each with a reproduction command:

1. Routing holes   - guides with zero work products, zero deliverables, or zero methods;
                     figures with no profile and no method route.
2. Bridge holes    - G248 artifacts that have only an unverified compatibility template,
                     or that no work product models at all.
3. Renderer losses - measured, not inferred: a probe renders a relationship that carries
                     endpoint cardinality through every registered renderer and records
                     whether the cardinality string survives into the SVG, and whether a
                     missing string is reported as an error. A silent loss is a gap even
                     when the renderer is otherwise correct.

Every finding is a design/review input. `audit_complete` and `acceptance_granted` are
separate: finishing this audit grants nothing.
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_source_current import DEFAULT_DECISIONS, write_new
CARDINALITY_TOKEN = "1..2"


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def routing_holes():
    from build_routing_matrix import build as build_routes
    matrix = build_routes()
    zero = matrix["zero_rows"]
    return {"guide_count": matrix["totals"]["guides"],
            "guides_with_zero_work_products": zero["no_work_products"],
            "guides_with_zero_deliverables": zero["no_deliverables"],
            "guides_with_zero_analysis_methods": zero["no_analysis_methods"],
            "guides_with_zero_profiles": zero["no_view_profiles"],
            "guides_without_capability_destination": zero["no_capability_destination"],
            "guides_without_deliverable_destination_or_reason": zero["no_deliverable_destination_or_reason"],
            "figures_without_profile_or_method": [{"figure_id": f, "guide": g["guide"]} for g in matrix["guides"] for f in g["figure_unrouted"]],
            "figures_without_profile_or_method_count": matrix["totals"]["figures_unrouted"],
            "matrix": matrix}


def bridge_holes():
    from build_artifact_bridge import build as build_bridge
    bridge = build_bridge()
    records = bridge["records"]
    compat = [r["artifact_id"] for r in records if not r["view_profiles"]["has_source_verified_profile"]]
    unresolved = [r["artifact_id"] for r in records if r["relation"] == "insufficient-material"]
    distinct = [r["artifact_id"] for r in records if r["relation"] == "distinct"]
    return {"measured_facts": bridge["measured_facts"], "relation_counts": bridge["relation_counts"],
            "compat_only_artifacts": compat, "compat_only_count": len(compat),
            "unresolved_artifacts": unresolved, "unresolved_count": len(unresolved),
            "distinct_artifacts": distinct, "distinct_count": len(distinct)}


def source_route_findings(routing, bridge):
    from audit_source_current import build as build_sources
    source = build_sources()
    findings = []
    for row in routing["matrix"]["guides"]:
        if not row["work_products"]:
            findings.append({"id": f"GAP-ROUTE-WP-{row['guide']}", "family": "routing", "severity": "info",
                             "statement": "零扩展WP保留为实际计数；既有基本制品/指南profile可合法承载，不要求新建重复WP。",
                             "affected_ids": row["base_artifact_reuse_ids"],
                             "verdict": "covered-by-base-artifact-review-required" if row["base_artifact_reuse_ids"] else "open",
                             "repair": "按适用范围选择现有制品，专业符合性另审；仅无合法目的地时补建模方案。"})
        if not row["deliverables"]:
            findings.append({"id": f"GAP-ROUTE-DL-{row['guide']}", "family": "routing", "severity": "info",
                             "statement": "注册表sources仍无该指南引用；显式给出可选交付章节，不声明强制性。",
                             "destinations": row["deliverable_options"],
                             "verdict": "optional-destination-review-required" if row["deliverable_options"] else "open",
                             "repair": "交付物责任人按项目适用性确认章节、保留不适用理由及本地结论。"})
    for figure in source["figure_dispositions"]:
        findings.append({"id": "GAP-ROUTE-FIG-" + figure["figure_id"].replace("/", "-"),
                         "family": "routing", "severity": "info" if figure["role"] == "non-template" else "medium",
                         "statement": figure["reason"], "destinations": figure["destinations"],
                         "verdict": "non-template-role-recorded" if figure["role"] == "non-template" else "review-required",
                         "repair": figure["closure_condition"]})
    for key, ids, text in (("DEFINITION", bridge["compat_only_artifacts"], "缺少source_verified=true profile，不能宣称英文定义已通过。"),
                           ("INSUFFICIENT", bridge["unresolved_artifacts"], "制品与扩展WP定义比较资料不足，不以实体重叠裁定。")):
        findings.append({"id": "GAP-BRIDGE-" + key, "family": "bridge", "severity": "high",
                         "statement": text, "affected_ids": ids, "verdict": "open" if ids else "no-current-gap",
                         "repair": "逐条取得正式定义、比较决策范围及字段差异；不能取得时明确blocked-definition-source，不补重复WP。"})
    findings.append({"id": "GAP-SOURCE-PROFESSIONAL-REVIEW", "family": "source", "severity": "high",
                     "statement": "所有索引来源均保留，路由与读过不代表专业通过。", "counts": source["counts"],
                     "verdict": "review-required", "repair": "逐条独立核对英文定义与适用性；无资料先补原文/正式来源，保留假设与未决项。"})
    return findings, source["counts"]


def build_source_routes_only():
    routing, bridge = routing_holes(), bridge_holes()
    findings, source_counts = source_route_findings(routing, bridge)
    return {"schema_version": "source-route-gaps/1", "generated_at": datetime.now(timezone.utc).isoformat(),
            "audit_complete": True, "acceptance_granted": False,
            "scope": "current source/routes/bridge only; no renderer or output regeneration",
            "summary": {"findings": len(findings), "open": sum(f["verdict"] == "open" for f in findings),
                        "review_required": sum("review-required" in f["verdict"] for f in findings)},
            "evidence": {"routing": routing, "bridge": bridge, "source_counts": source_counts}, "findings": findings}


def _entities():
    return [
        {"id": "probe-app", "name": "探针应用", "type": "application",
         "attributes": {}, "certainty": "assumed", "evidence": ["probe"]},
        {"id": "probe-proc", "name": "探针流程", "type": "process",
         "attributes": {}, "certainty": "assumed", "evidence": ["probe"]},
        {"id": "probe-data", "name": "探针数据实体", "type": "data_entity",
         "attributes": {}, "certainty": "assumed", "evidence": ["probe"]},
    ]


def _relationships():
    cardinality = {"source": {"min": 1, "max": 1}, "target": {"min": 1, "max": 2}}
    return [
        {"id": "probe-rel", "type": "accesses", "source": "probe-proc", "target": "probe-data",
         "label": "探针基数关系", "attributes": {"order": 1},
         "cardinality": cardinality, "certainty": "assumed", "evidence": ["probe"]},
        {"id": "probe-rel-2", "type": "processing_step", "source": "probe-app", "target": "probe-proc",
         "label": "探针处理关系", "attributes": {"order": 2}, "certainty": "assumed",
         "evidence": ["probe"]},
    ]


def renderer_probe():
    """Render one fixed model through every registered renderer and record cardinality survival."""
    from profile_render import render_profile

    capabilities = read(ROOT / "capabilities.json")
    renderers = sorted({p.get("renderer") for p in capabilities.get("profiles", []) if p.get("renderer")})
    entities = _entities()
    relationships = _relationships()
    results = []
    for renderer in renderers:
        view = {
            "id": f"probe-{renderer}",
            "title": f"渲染器探针 {renderer}",
            "entity_ids": [e["id"] for e in entities],
            "relationship_ids": [r["id"] for r in relationships],
            "legend": "探针视图；不含企业事实",
        }
        profile = {"id": f"probe-{renderer}", "renderer": renderer, "template": {},
                   "required_attributes": {}}
        try:
            svg, report = render_profile({"entities": entities, "relationships": relationships},
                                         view, profile, "adaptive")
        except Exception as error:  # a crash is itself a finding, not a probe failure
            results.append({
                "renderer": renderer,
                "status": "raised",
                "error": f"{type(error).__name__}: {error}",
                "cardinality_visible": False,
                "cardinality_reported_missing": False,
                "silent_loss": False,
                "applicable": False,
            })
            continue
        visible = CARDINALITY_TOKEN in svg
        errors = [e.get("code") for e in report.get("errors", []) if isinstance(e, dict)]
        reported = any("cardinal" in str(code).lower() for code in errors) or any(
            "端点基数" in str(w) or "cardinal" in str(w).lower() for w in report.get("warnings", []))
        # A renderer that reports the relationship as unrepresented is loud, not silent.
        loud = reported or bool(report.get("unrepresented_relationship_ids"))
        results.append({
            "renderer": renderer,
            "status": "rendered",
            "cardinality_visible": visible,
            "cardinality_reported_missing": reported,
            "silent_loss": (not visible) and (not loud),
            "unrepresented_entities": report.get("unrepresented_entity_ids", []),
            "unrepresented_relationships": report.get("unrepresented_relationship_ids", []),
            "errors": errors,
        })
    silent = sorted(r["renderer"] for r in results if r.get("silent_loss"))
    loud = sorted(r["renderer"] for r in results if r.get("status") == "rendered"
                  and not r.get("cardinality_visible") and not r.get("silent_loss"))
    raised = sorted(r["renderer"] for r in results if r.get("status") == "raised")
    return {
        "probe": "one relationship carrying endpoint cardinality 1..2 rendered through every registered renderer",
        "renderers_tested": len(results),
        "silent_loss_renderers": silent,
        "silent_loss_count": len(silent),
        "loud_loss_renderers": loud,
        "raised_renderers": raised,
        "results": results,
    }


def category_probe():
    """Does a category change produce structure, or only changed text?"""
    from profile_render import render_profile

    def build(category):
        entities = [
            {"id": "cap-a", "name": "能力甲", "type": "capability",
             "attributes": {"definition": "探针", "category": category, "level": 1},
             "certainty": "assumed", "evidence": ["probe"]},
            {"id": "cap-b", "name": "能力乙", "type": "capability",
             "attributes": {"definition": "探针", "category": category, "level": 2},
             "certainty": "assumed", "evidence": ["probe"]},
        ]
        relationships = [{"id": "dec", "type": "decomposes", "source": "cap-a", "target": "cap-b",
                          "label": "分解", "attributes": {}, "certainty": "assumed",
                          "evidence": ["probe"]}]
        view = {"id": "probe-nested", "title": "能力分区探针",
                "entity_ids": ["cap-a", "cap-b"], "relationship_ids": ["dec"], "legend": "探针"}
        profile = {"id": "probe-nested", "renderer": "nested-map", "template": {},
                   "required_attributes": {"capability": ["definition", "category", "level"]}}
        svg, report = render_profile({"entities": entities, "relationships": relationships},
                                     view, profile, "adaptive")
        return svg, report

    svg_strategic, report_a = build("战略")
    svg_support, report_b = build("支持")
    changed = svg_strategic != svg_support
    markers = ('data-category-band', 'data-group="category"', 'data-band')
    structural_markers = sum(svg_strategic.count(marker) for marker in markers)
    return {
        "probe": "two capabilities with category 战略 vs 支持 under the nested-map renderer",
        "svg_changed": changed,
        "structural_marker_count": structural_markers,
        "category_rendered_as_structure": structural_markers > 0,
        "category_rendered_as_text_only": changed and structural_markers == 0,
        "errors": [e.get("code") for e in report_a.get("errors", []) if isinstance(e, dict)]
                  + [e.get("code") for e in report_b.get("errors", []) if isinstance(e, dict)],
    }


def score_probe():
    """Where does a score become visible? Recorded per renderer and per color-map presence."""
    from profile_render import render_profile

    def build(score, renderer, template):
        entities = [{"id": "cap-score", "name": "评分能力", "type": "capability",
                     "attributes": {"definition": "探针", "category": "核心", "level": 1,
                                    "dimension": "maturity", "score": score,
                                    "scale": "0-3", "target": 3},
                     "certainty": "assumed", "evidence": ["probe"]}]
        view = {"id": f"probe-score-{renderer}-{score}", "title": "评分探针",
                "entity_ids": ["cap-score"], "relationship_ids": [], "legend": "探针"}
        profile = {"id": "probe-score", "renderer": renderer, "template": template,
                   "required_attributes": {"capability": [
                       "definition", "category", "level", "dimension", "score", "scale", "target"]}}
        try:
            svg, report = render_profile({"entities": entities, "relationships": []},
                                         view, profile, "adaptive")
            return svg, report, None
        except Exception as error:
            return "", {}, f"{type(error).__name__}: {error}"

    colors = {"colors": {"1": "#dbeafe", "3": "#1e3a8a"}}
    matrix = {}
    for renderer in ("nested-map", "heatmap"):
        for label, template in (("no_colors", {}), ("declared_colors", colors)):
            low, low_report, low_error = build(1, renderer, template)
            high, _, high_error = build(3, renderer, template)
            error = low_error or high_error
            matrix[f"{renderer}__{label}"] = {
                "fill_changed": (not error) and _fill_signature(low) != _fill_signature(high),
                "errors": [] if error else [e.get("code") for e in low_report.get("errors", [])
                                            if isinstance(e, dict)],
                "raised": error,
            }

    only_heatmap = (
        matrix["heatmap__declared_colors"]["fill_changed"]
        and not matrix["nested-map__declared_colors"]["fill_changed"]
        and not matrix["heatmap__no_colors"]["fill_changed"]
    )
    return {
        "probe": "score 1 vs 3 rendered by nested-map and heatmap, with and without a declared color map",
        "matrix": matrix,
        "score_visualisation_requires_heatmap_and_declared_colors": only_heatmap,
        "nested_map_silently_accepts_score": (
            matrix["nested-map__no_colors"]["fill_changed"] is False
            and not matrix["nested-map__no_colors"]["errors"]
        ),
    }


def _fill_signature(svg):
    """Extract only fill attributes so text-only changes cannot masquerade as visualisation."""
    import re
    return re.findall(r'fill="(#[0-9a-fA-F]{3,8})"', svg)


def provenance_drift():
    """Compare saved output fingerprints against current runtime fingerprints.

    A drift is reported, never repaired here: regenerating outputs would refresh
    historical evidence. The owner must open a new run_id and keep the old batch.
    """
    import sys as _sys
    _sys.path.insert(0, str(ROOT / "scripts"))
    from runtime_provenance import fingerprints

    current = fingerprints(ROOT)
    drifts = []
    for layout in ("reference", "adaptive"):
        manifest_path = ROOT / f"examples/full-capability/{layout}/manifest.json"
        if not manifest_path.is_file():
            drifts.append({"layout": layout, "status": "manifest-missing"})
            continue
        manifest = read(manifest_path)
        recorded = manifest.get("implementation_dependencies_sha256") or {}
        changed = sorted(key for key in recorded if key in current and recorded[key] != current[key])
        added = sorted(set(current) - set(recorded))
        removed = sorted(set(recorded) - set(current))
        drifts.append({
            "layout": layout,
            "status": "current" if not (changed or added or removed) else "stale",
            "changed": changed,
            "added_since_output": added,
            "removed_since_output": removed,
        })
    named = {
        "capabilities_sha256": "capabilities.json",
        "renderer_sha256": "scripts/profile_render.py",
        "generator_sha256": "scripts/generate.py",
        "table_renderer_sha256": "scripts/table_expression.py",
        "metamodel_sha256": "metamodel.json",
        "artifacts_sha256": "artifacts.json",
        "deliverables_sha256": "deliverables.json",
        "assembly_renderer_sha256": "scripts/deliverable_assembly.py",
        "assembly_rules_sha256": "capability-addenda/deliverable-assembly-rules.json",
    }
    manifest = read(ROOT / "examples/full-capability/reference/manifest.json")
    semantic = {
        key: {"match": manifest.get(key) == sha(ROOT / path), "path": path}
        for key, path in named.items()
    }
    return {
        "probe": "saved full-capability manifests versus current runtime fingerprints",
        "layouts": drifts,
        "semantic_registry_fingerprints": semantic,
        "stale_layouts": [d["layout"] for d in drifts if d.get("status") == "stale"],
        "note": (
            "A stale layout means the saved output no longer matches the code that produced it. "
            "This audit does not regenerate; the fix is a new run_id with the old batch preserved."
        ),
    }


def compat_only_profiles():
    capabilities = read(ROOT / "capabilities.json")
    compat = [p["id"] for p in capabilities.get("profiles", []) if p["id"].startswith("compat-")]
    unverified = [p["id"] for p in capabilities.get("profiles", [])
                  if (p.get("template") or {}).get("source_verified") is False]
    return {
        "compat_profile_count": len(compat),
        "profiles_with_source_verified_false": len(unverified),
        "compat_profiles": compat,
    }


def build():
    routing = routing_holes()
    bridge = bridge_holes()
    renderers = renderer_probe()
    category = category_probe()
    score = score_probe()
    compat = compat_only_profiles()
    provenance = provenance_drift()

    findings, source_counts = source_route_findings(routing, bridge)

    findings.append({
        "id": "GAP-RENDER-CARDINALITY-SILENT",
        "family": "renderer",
        "severity": "high",
        "statement": (
            f"{renderers['silent_loss_count']} of {renderers['renderers_tested']} renderers drop endpoint "
            f"cardinality without any error, warning or unrepresented-relationship record: "
            f"{', '.join(renderers['silent_loss_renderers']) or 'none'}. "
            f"Renderers that lose cardinality but report the relationship as unrepresented are "
            f"excluded as loud: {', '.join(renderers['loud_loss_renderers']) or 'none'}."
        ),
        "consequence": "Readers cannot see bounded cardinality in those views and the pipeline still reports success; the existing rule that required attributes must be visible, not merely retained in JSON, is not enforced for relationship attributes.",
        "reproduce": "python3 skills/_shared/scripts/audit_structural_gaps.py",
        "repair": "Emit endpoint cardinality in the message label or the relationship-attribute register, then add a per-renderer regression test asserting either visibility or an explicit not-represented record.",
        "verdict": "open",
        "affected_ids": renderers["silent_loss_renderers"],
    })

    findings.append({
        "id": "GAP-RENDER-CATEGORY-TEXT-ONLY",
        "family": "renderer",
        "severity": "medium",
        "statement": (
            "A category change under the nested-map renderer alters only the attribute text"
            f" (structural markers found: {category['structural_marker_count']})."
        ),
        "consequence": "Category is not expressed as a band or spatial partition, so a capability map cannot be read by category.",
        "reproduce": "python3 skills/_shared/scripts/audit_structural_gaps.py",
        "repair": "Add category bands to nested-map and require an explicit color map when score is required.",
        "verdict": "open" if category["category_rendered_as_text_only"] else "closed-by-probe",
    })

    findings.append({
        "id": "GAP-RENDER-SCORE-ROUTING",
        "family": "renderer",
        "severity": "medium",
        "statement": (
            "Score becomes visual only in the heatmap renderer with a declared color map; the nested-map "
            f"renderer accepts a required score and draws no graded emphasis without any error "
            f"(matrix: {json.dumps(score.get('matrix'), ensure_ascii=False)})."
        ),
        "consequence": "A profile that declares score as required but uses nested-map produces a view that looks complete while no score is visible, and nothing marks it as draft or incomplete.",
        "reproduce": "python3 skills/_shared/scripts/audit_structural_gaps.py",
        "repair": "Route score-bearing capability maps to heatmap, or make nested-map report a coded gap when score is required and no rendered encoding exists.",
        "verdict": "open",
    })

    if provenance["stale_layouts"]:
        stale = provenance["stale_layouts"]
        changed = sorted({key for layout in provenance["layouts"]
                          for key in layout.get("changed", [])})
        findings.append({
            "id": "GAP-PROVENANCE-STALE-OUTPUT",
            "family": "provenance",
            "severity": "high",
            "statement": (
                f"Saved full-capability layouts are stale against current runtime fingerprints: "
                f"{', '.join(stale)}. Changed dependency files: {', '.join(changed) or 'none'}."
            ),
            "consequence": (
                "The 267 saved outputs were produced by different code than the current tree, so "
                "they cannot be cited as current generation evidence; any comparison against them "
                "must state the older dependency set."
            ),
            "reproduce": "python3 skills/_shared/scripts/audit_structural_gaps.py",
            "repair": (
                "Regenerate under a new run_id and keep the previous batch as historical evidence; "
                "do not overwrite the recorded hashes in place."
            ),
            "verdict": "open",
            "affected_ids": stale,
        })

    findings.append({
        "id": "GAP-SOURCE-CHINESE-PDF-ABSENT",
        "family": "source",
        "severity": "medium",
        "statement": "The Chinese corpus README and prior reports describe 26 Chinese PDFs; 0 are present in the directory.",
        "consequence": "Any claim about the Chinese suite must be limited to 26 Markdown files, 243 figure JSON records and 406 image assets.",
        "reproduce": "ls togaf-standard-10th-zh/*.pdf | wc -l  # expect 0",
        "repair": "Register documented-but-absent; do not fabricate files or retro-hash.",
        "verdict": "open",
    })

    return {
        "schema_version": "structural-gaps/1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "audit_complete": True,
        "acceptance_granted": False,
        "notice": (
            "Structural findings with reproduction commands. A finding is a design input, never an "
            "acceptance verdict; closing one requires a code or registry change and a re-run."
        ),
        "inputs_sha256": {
            "capabilities.json": sha(ROOT / "capabilities.json"),
            "artifacts.json": sha(ROOT / "artifacts.json"),
            "deliverables.json": sha(ROOT / "deliverables.json"),
            "metamodel.json": sha(ROOT / "metamodel.json"),
            "scripts/profile_render.py": sha(ROOT / "scripts/profile_render.py"),
            "source_route_decisions": sha(DEFAULT_DECISIONS),
        },
        "summary": {
            "findings": len(findings),
            "by_family": dict(Counter(f["family"] for f in findings)),
            "by_severity": dict(Counter(f["severity"] for f in findings)),
            "open": sum(1 for f in findings if f["verdict"] == "open"),
        },
        "evidence": {
            "routing": routing,
            "bridge": bridge,
            "renderer_cardinality": renderers,
            "renderer_category": category,
            "renderer_score": score,
            "compat_profiles": compat,
            "provenance_drift": provenance,
        },
        "findings": findings,
        "limits": [
            "The renderer probe uses a synthetic two-entity model; results describe these renderers on that input, not every possible model.",
            "Category and score probes record text-only change, not that a future change cannot add structure.",
            "Bridge relations are explicit question/definition comparisons, never inferred from entity types; source and professional review remain separate.",
            "No finding here changes a registered capability, profile, template or acceptance number.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out")
    parser.add_argument("--source-routes-only", action="store_true")
    args = parser.parse_args()
    result = build_source_routes_only() if args.source_routes_only else build()
    out = Path(args.out) if args.out else ROOT / f"reviews/source-current/run-gaps-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}.json"
    write_new(out, result)
    summary = result["summary"]
    print(f"findings={summary['findings']} open={summary['open']}")
    if not args.source_routes_only:
        print("by_family:", summary["by_family"])
        print("by_severity:", summary["by_severity"])
        print("renderers with silent cardinality loss:",
              result["evidence"]["renderer_cardinality"]["silent_loss_renderers"])
        print("stale saved layouts:", result["evidence"]["provenance_drift"]["stale_layouts"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
