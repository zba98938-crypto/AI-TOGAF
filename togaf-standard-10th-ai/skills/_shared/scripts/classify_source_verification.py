#!/usr/bin/env python3
"""Classify all registered view profiles into three source-verification tiers.

Tiers are decided by evidence that exists on disk, not by intent:

  verifiable      A source figure crops to a real English image and the profile
                  declares a source-derived definition status. Promoting to
                  source_verified=true requires a current substantive template
                  review. A file's existence or a matching source-image hash is
                  only provenance and cannot establish that review's conclusion.
  partial         A figure route exists but its best asset is a Chinese redraw, or
                  the English crop is missing for that specific figure number.
  unverifiable    No figure routes to the profile at all, or the definition status
                  says the artifact is a project convention with no source figure.
  blocked         The definition depends on material the project does not hold
                  (C220 body, external workbook).

This script only proposes tiers. It never flips source_verified itself; that is done
by apply in a separate step after the evidence files exist.
"""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT
OUT = ROOT / "reviews/source-verification"
INDEX = ROOT / "reviews/source-verification-index.json"

# Definition statuses that assert a source figure was the basis of the view.
SOURCE_DERIVED = {
    "source-derived-view-with-project-construction-rules",
    "source-derived-project-operational-contract",
    "source-semantics-with-project-operational-form",
    "source-guided-table-project-schema",
    "source-guided-project-choice; no-score",
    "body-reviewed-project-operational-table",
    "body-derived-project-table",
    "local-body-reference-plus-explicit-project-operational-contract",
    "local-body-table-reviewed; official-definition-separate",
}
# Statuses that explicitly say the source is unavailable or project-only.
BLOCKED_STATUS = {
    "local-body-pattern; original-figure-unavailable; historical-structure-not-certified",
}
PROJECT_ONLY = {
    "project-operational-view",
    "project-compatibility-template",
}


def load(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def english_crops():
    """Map figure id -> crop path for the bundled English PDF crops."""
    crops = SHARED / "reviews/source-package-2026-11-02-v2/original-crops"
    if not crops.is_dir():
        return {}
    found = defaultdict(list)
    for path in crops.iterdir():
        if not path.is_file():
            continue
        stem = path.name.split("-p")[0]
        figure_id = stem.replace("-", "/", 1)
        found[figure_id].append(str(path.relative_to(SHARED)))
    return found


def classify(profile, figures_for_profile, registry, crops):
    """Decide the tier from the figure's own source_status, not from crop presence.

    A bundled English crop means an original image exists, but the figure record may
    still say the local asset is a redraw awaiting verification. Promoting such a
    profile to verifiable would assert more than the evidence shows, so the tier is
    capped by source_status.
    """
    status = profile.get("definition_status")
    tier = "unverifiable"
    reason = ""
    evidence = []

    if status in BLOCKED_STATUS:
        if figures_for_profile and any(fid in crops for fid in figures_for_profile):
            return ("available-unverified",
                    "本机原图或裁图可用；文件可用不等于语义已核，source_verified 仍为 false",
                    [{"figure_id": fid, "crop": crops[fid][0], "source_status": "local-asset-present"}
                     for fid in figures_for_profile if fid in crops])
        return "blocked", "定义状态声明原图不可用", []

    if not figures_for_profile:
        reason = "无任何来源图路由到该规范"
        if status in PROJECT_ONLY:
            reason = "项目约定型规范，无来源图；不冒充来源核实"
        return "unverifiable", reason, []

    # Only a figure whose source_status says the original asset is usable may support
    # a verifiable tier. Redraws stay partial even when a PDF crop exists.
    usable_status = {"original-asset-available-unverified",
                     "english-pdf-available-candidate-reconstruction-opened"}
    strongest = None
    for fid in figures_for_profile:
        if fid not in crops:
            continue
        figures = [f for f in registry["figures"] if f["id"] == fid]
        if not figures:
            continue
        figure = figures[0]
        evidence.append({
            "figure_id": fid,
            "crop": crops[fid][0],
            "source_status": figure["source_status"],
        })
        if figure["source_status"] in usable_status:
            strongest = figure["source_status"]
        elif strongest is None:
            strongest = figure["source_status"]

    if not evidence:
        return "partial", "有图路由但缺该图号的英文原图裁图", []

    if strongest in usable_status and status in SOURCE_DERIVED:
        return "verifiable", "英文原图资产可用且定义状态声明来源派生", evidence
    if strongest in usable_status:
        return "partial", "英文原图可用但定义状态未声明来源派生", evidence
    return "partial", f"图源状态为 {strongest}，中文重绘或等价性未核，不判可核", evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-evidence", action="store_true",
                        help="写出每个规范一份证据记录（不置 source_verified）")
    args = parser.parse_args()

    caps = load(SHARED / "capabilities.json")
    registry = load(SHARED / "evidence-registry.json")
    crops = english_crops()

    routings = defaultdict(list)
    for figure in caps.get("figure_profiles", []):
        for pid in figure.get("profile_ids") or []:
            routings[pid].append(figure["id"])

    rows = []
    tier_counts = Counter()
    for profile in caps["profiles"]:
        pid = profile["id"]
        tier, reason, evidence = classify(profile, routings.get(pid, []), registry, crops)
        tier_counts[tier] += 1
        rows.append({
            "profile_id": pid,
            "artifact_id": profile["artifact_id"],
            "owner": profile["owner"],
            "definition_status": profile.get("definition_status"),
            "current_source_verified": (profile.get("template") or {}).get("source_verified"),
            "tier": tier,
            "reason": reason,
            "evidence": evidence,
            "source_refs": profile.get("source_refs") or [],
        })

    if args.write_evidence:
        OUT.mkdir(parents=True, exist_ok=True)
        for row in rows:
            record = {
                "schema_version": "source-verification-record/1",
                "profile_id": row["profile_id"],
                "tier": row["tier"],
                "reason": row["reason"],
                "definition_status": row["definition_status"],
                "source_refs": row["source_refs"],
                "source_comparisons": [
                    {
                        "source_path": item["crop"],
                        "source_sha256": sha(SHARED / item["crop"]),
                        "locator": item["figure_id"],
                        "conclusion": "英文原图裁图存在；结构与视觉等价仍须逐项对照",
                        "figure_source_status": item["source_status"],
                    }
                    for item in row["evidence"]
                ],
                "reviewer": {
                    "id": "cursor-ai-reviewer",
                    "role": "AI-assisted reviewer (not a human signatory)",
                },
                "limitation": ("AI 辅助分类，非人工签字；裁图存在不等于结构与视觉等价，"
                               "等价判定见 profile-visual-review 记录。"),
            }
            (OUT / f"{row['profile_id']}.json").write_text(
                json.dumps(record, ensure_ascii=False, indent=1) + "\n")

    index = {
        "schema_version": "source-verification-index/1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "registry_sha256": sha(SHARED / "capabilities.json"),
        "notice": ("三档为证据分类，不是验收。verifiable 仍需逐项对照与人工复核；"
                   "unverifiable 表示本项目无来源图，不等于规范错误。"),
        "tiers": dict(tier_counts),
        "total": len(rows),
        "records": rows,
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(dict(tier_counts), ensure_ascii=False))
    print("total:", len(rows))


if __name__ == "__main__":
    main()
