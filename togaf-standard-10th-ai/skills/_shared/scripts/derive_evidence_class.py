#!/usr/bin/env python3
"""Derive an evidence class for every view profile, from registry facts only.

The class says what kind of proof a definition dimension can offer:

  source-figure      a usable English original figure exists and was structurally compared
  source-text        a section/table anchor exists in the guide text, but no usable figure
  project-convention no figure and no text anchor: the rule is this project's own
  unclassified       neither rule applies; a human must adjudicate

Precedence matters and is the anti-bypass mechanism:

  1 figure first  - if an original exists, figure comparison is required, so a
                    profile cannot escape visual review by claiming text or convention
  2 text second   - any § or 表 anchor in source_refs outranks a "project" label,
                    so citing the standard cannot be downgraded to "no basis"
  3 status third  - source-/body-/local-body-reference prefixes imply text derivation
  4 convention    - only project-operational-view / project-compatibility-template

This script is read-only with respect to the registry. It writes one index file and
reports discrepancies against the existing source-verification classification.
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviews/evidence-class-index.json"
SOURCE_INDEX = ROOT / "reviews/source-verification-index.json"

ANCHOR = re.compile(r"[§＃#]|表\s*[0-9A-Za-z]|Table\s*[0-9A-Za-z]|PDF\s*\d", re.IGNORECASE)
FIGURE_ANCHOR = re.compile(r"fig[0-9A-Za-z]|图\s*[0-9A-Za-z]", re.IGNORECASE)
TEXT_STATUS_PREFIXES = ("source-", "body-", "local-body-reference", "local-body-table")
CONVENTION_STATUSES = {"project-operational-view", "project-compatibility-template"}


def load(path):
    return json.loads(Path(path).read_text())


def classify(profile, source_record):
    """Return (class, reason). Order of checks is the safety property."""
    status = profile.get("definition_status")
    refs = [str(r) for r in (profile.get("source_refs") or [])]
    tier = (source_record or {}).get("tier")

    # 0. A blocked figure means the figure cannot be cited, but a profile that ALSO
    #    cites a section anchor still has a text basis. Only a blocked profile with
    #    no text anchor is unclassifiable.
    if tier == "blocked":
        text_anchors = [r for r in refs if ANCHOR.search(r)]
        if text_anchors:
            return "source-text", f"图为阻断，但仍有正文锚点：{text_anchors[0]}"
        return "unclassified", "来源三档为阻断且无正文锚点，需人工裁定或改标项目约定"

    # 1. A usable original figure forces source-figure.
    if tier == "verifiable":
        return "source-figure", "来源三档为可核，有可用英文原图"

    # 1b. A figure reference with no usable crop is a figure gap, not a text basis:
    #     the profile points at an image this project cannot inspect, so calling it
    #     source-text would invent a textual basis that does not exist.
    figure_anchors = [r for r in refs if FIGURE_ANCHOR.search(r)]
    if figure_anchors and not any(ANCHOR.search(r) for r in refs):
        return "unclassified", f"仅引用图号且该图不可用：{figure_anchors[0]}，需补正文锚点或改标项目约定"

    # 2. Any section/table anchor means the text supports the definition.
    anchors = [r for r in refs if ANCHOR.search(r)]
    if anchors:
        return "source-text", f"source_refs 含正文锚点：{anchors[0]}"

    # 3. A source-derived status without an explicit anchor still points at text.
    if status and any(str(status).startswith(p) for p in TEXT_STATUS_PREFIXES):
        return "source-text", f"definition_status 为 {status}，指向来源正文"

    # 4. Explicit project-only statuses.
    if status in CONVENTION_STATUSES:
        return "project-convention", f"definition_status 为 {status}，无来源引用"

    return "unclassified", "既无图也无正文锚点，且定义状态未声明项目约定"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(OUT))
    args = parser.parse_args()

    caps = load(ROOT / "capabilities.json")
    source_records = {r["profile_id"]: r for r in load(SOURCE_INDEX)["records"]}

    rows = []
    counts = Counter()
    mismatches = []
    pending_reviews = []
    for profile in caps["profiles"]:
        pid = profile["id"]
        record = source_records.get(pid, {})
        klass, reason = classify(profile, record)
        counts[klass] += 1
        row = {
            "profile_id": pid,
            "artifact_id": profile["artifact_id"],
            "owner": profile["owner"],
            "definition_status": profile.get("definition_status"),
            "evidence_class": klass,
            "reason": reason,
            "source_refs": profile.get("source_refs") or [],
            "source_tier": record.get("tier"),
            "current_source_verified": (profile.get("template") or {}).get("source_verified"),
        }
        rows.append(row)

        # Source availability and completed template review are independent.
        if klass == "source-figure" and not row["current_source_verified"]:
            pending_reviews.append({
                "profile_id": pid,
                "kind": "source-template-review-pending",
                "detail": "原图可用；模板尚待实质核查，保留 false 正确，不应仅凭原图存在升级",
            })
        # A promoted profile must be source-figure; otherwise the class rules disagree.
        if row["current_source_verified"] and klass != "source-figure":
            mismatches.append({
                "profile_id": pid,
                "kind": "promoted-but-class-disagrees",
                "detail": f"source_verified=true 但派生类别为 {klass}",
            })

    payload = {
        "schema_version": "evidence-class-index/1",
        "generated_at": "2026-11-04",
        "status": "design-derived; acceptance_gate.py unchanged",
        "notice": ("类别由注册表事实派生，不由调用方填写。本文件不改变任何 "
                   "source_verified 值，也不构成验收。"),
        "precedence": ["source-figure", "source-text", "project-convention", "unclassified"],
        "counts": dict(counts),
        "total": len(rows),
        "mismatches": mismatches,
        "pending_template_reviews": pending_reviews,
        "records": rows,
    }
    Path(args.out).write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")

    print(json.dumps(dict(counts), ensure_ascii=False))
    print("total:", len(rows), "| mismatches:", len(mismatches))
    for mismatch in mismatches[:8]:
        print(" ", mismatch["kind"], mismatch["profile_id"])


if __name__ == "__main__":
    main()
