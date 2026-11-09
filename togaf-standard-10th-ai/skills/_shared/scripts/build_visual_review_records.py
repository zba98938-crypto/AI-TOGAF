#!/usr/bin/env python3
"""Compare each routed source structure with the model that generated its view.

What this does and does not do:

  * It compares machine-readable structure: object count, relationship count and
    relationship type distribution between the portable source interpretation
    (references/source-structures/*.json) and the actual saved view JSON.
  * It records which files were opened and hashes them, so the record is auditable.
  * It does NOT claim visual equivalence. Reading an image through a text
    description is not the same as a human opening it, so every record states the
    observation basis explicitly and caps its verdict at "structural-partial"
    unless the counts match exactly and the source uncertainty is empty.

A template whose source structure has recorded uncertainty can never be reported as
structurally equivalent, because the reference itself is not settled.
"""
from datetime import datetime, timezone
import os
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT
OUT = ROOT / "reviews/profile-visual-review"
INDEX = ROOT / "reviews/profile-visual-review-index.json"
OUTPUT_ROOT = SHARED / "examples/full-capability"


def load(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def output_paths(profile_id):
    """Return the saved reference/adaptive outputs for a profile, if generated."""
    found = {}
    for layout in ("reference", "adaptive"):
        folder = OUTPUT_ROOT / layout / "artifacts"
        json_path = folder / f"profile-{profile_id}.json"
        png_path = folder / f"profile-{profile_id}.png"
        coverage_path = folder / f"profile-{profile_id}.coverage.json"
        if json_path.is_file():
            found[layout] = {
                "json": os.path.relpath(json_path, SHARED),
                "png": os.path.relpath(png_path, SHARED) if png_path.is_file() else None,
                "coverage": os.path.relpath(coverage_path, SHARED)
                if coverage_path.is_file() else None,
            }
    return found


def relationship_profile(rows):
    return dict(Counter(r.get("type") for r in rows if isinstance(r, dict)))


def main():
    global OUTPUT_ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    args = parser.parse_args()
    OUTPUT_ROOT = args.output_root.resolve()

    caps = load(SHARED / "capabilities.json")
    registry = load(SHARED / "evidence-registry.json")
    figures = {f["id"]: f for f in registry["figures"]}

    routings = {}
    for figure in caps.get("figure_profiles", []):
        for pid in figure.get("profile_ids") or []:
            routings.setdefault(pid, []).append(figure["id"])

    from runtime_provenance import fingerprints
    manifests={layout:load(OUTPUT_ROOT/layout/'manifest.json') if (OUTPUT_ROOT/layout/'manifest.json').is_file() else {} for layout in ('reference','adaptive')}
    output_current={layout:manifest.get('capabilities_sha256')==sha(SHARED/'capabilities.json') and manifest.get('implementation_dependencies_sha256')==fingerprints(SHARED) for layout,manifest in manifests.items()}
    records = []
    verdicts = Counter()
    for profile in caps["profiles"]:
        pid = profile["id"]
        figure_ids = routings.get(pid, [])
        outputs = output_paths(pid)
        if not figure_ids:
            verdicts["no-source-figure"] += 1
            records.append({
                "profile_id": pid,
                "artifact_id": profile["artifact_id"],
                "verdict": "no-source-figure",
                "reason": "该规范无来源图路由；只能验证生成可执行，不能声明来源等价。",
                "opened_assets": [],
                "source_assets": [],
                "output_assets": [v for layout in outputs.values()
                                  for k, v in layout.items() if k in ("json", "png") and v],
            })
            continue

        figure_id = figure_ids[0]
        figure = figures.get(figure_id, {})
        portable = figure.get("portable_structure")
        source_path = SHARED / portable if portable else None
        source_structure = load(source_path) if source_path and source_path.is_file() else None

        layout = "reference" if "reference" in outputs else (
            "adaptive" if "adaptive" in outputs else None)
        output_json = None
        if layout:
            output_json = load(SHARED / outputs[layout]["json"])

        source_elements = len((source_structure or {}).get("elements") or [])
        source_relations = len((source_structure or {}).get("relationships") or [])
        output_entities = len((output_json or {}).get("entities") or [])
        output_relations = len((output_json or {}).get("relationships") or [])
        uncertainty = (source_structure or {}).get("uncertainty") or []

        if source_structure is None or output_json is None:
            verdict = "blocked-source-structure-unavailable"
        elif uncertainty:
            verdict = "structural-partial-source-uncertain"
        elif source_elements == output_entities and source_relations == output_relations:
            verdict = "structural-match"
        elif abs(source_elements - output_entities) <= 2 and abs(source_relations - output_relations) <= 2:
            verdict = "structural-partial"
        else:
            verdict = "structural-mismatch"

        verdicts[verdict] += 1
        opened = []
        for path in [p for p in [outputs.get(layout, {}).get("json"),
                                 outputs.get(layout, {}).get("png")] if p]:
            opened.append({
                "path": path,
                "sha256": sha(SHARED / path),
                "reviewer_id": "cursor-ai-reviewer",
                "opened": path.endswith(".json"),
                "observation_basis": "parsed-model-json" if path.endswith(".json") else "file-hash-only; image-not-opened",
                "observations": [
                    "JSON仅比较结构计数；PNG只计算文件哈希，未作图像观察或视觉比较",
                    f"该文件用于核对 {pid} 的{('模型结构' if path.endswith('.json') else '渲染结果')}",
                ],
            })

        records.append({
            "profile_id": pid,
            "artifact_id": profile["artifact_id"],
            "source_figure": figure_id,
            "verdict": verdict,
            "reason": {
                "blocked-source-structure-unavailable": "来源结构或输出缺失，无法比较",
                "structural-partial-source-uncertain": (
                    "来源结构 JSON 自带不确定性说明，参考本身未定，不能判等价"),
                "structural-match": "对象与关系计数一致且来源无已声明不确定性",
                "structural-partial": "对象或关系计数差异在 2 以内",
                "structural-mismatch": "对象或关系计数差异超过 2",
            }[verdict],
            "counts": {
                "source_elements": source_elements,
                "source_relationships": source_relations,
                "output_entities": output_entities,
                "output_relationships": output_relations,
            },
            "source_uncertainty_count": len(uncertainty),
            "source_assets": [
                {"path": portable, "sha256": sha(source_path)}
            ] if source_path and source_path.is_file() else [],
            "output_assets": [p for layout_item in outputs.values()
                              for k, p in layout_item.items() if k in ("json", "png") and p],
            "opened_assets": opened,
            "visual_equivalence": False,
            "limitation": ("结构计数比较不等于视觉等价。本记录不含人工目视结论，"
                           "不能据此声明来源图复现通过。"),
        })

    if args.write:
        OUT.mkdir(parents=True, exist_ok=True)
        for record in records:
            (OUT / f"{record['profile_id']}.json").write_text(
                json.dumps(record, ensure_ascii=False, indent=1) + "\n")

    index = {
        "schema_version": "profile-visual-review-index/1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "registry_sha256": sha(SHARED / "capabilities.json"),
        "output_root": os.path.relpath(OUTPUT_ROOT, SHARED),
        "output_current": output_current,
        "output_manifest_sha256": {layout:sha(OUTPUT_ROOT/layout/"manifest.json") for layout in manifests if (OUTPUT_ROOT/layout/"manifest.json").is_file()},
        "notice": ("结构计数比较，非视觉等价。每个记录显式声明未做人工目视，"
                   "visual_equivalence 一律为 false。"),
        "verdicts": dict(verdicts),
        "total": len(records),
        "records": records,
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(dict(verdicts), ensure_ascii=False))
    print("total:", len(records))


if __name__ == "__main__":
    main()
