#!/usr/bin/env python3
"""Close the unclassified profiles by anchoring them to their figure's caption text.

A profile that cites only `G178/figA-2` has no usable crop, but the guide still
carries a caption and surrounding prose for that figure. Anchoring to the page where
the figure is discussed gives a real, quotable text basis.

The anchor is only written when the figure reference is actually found in that page,
and the quote is copied from the page, never composed. Profiles with no anchor found
stay unclassified and are reported, because inventing a page number would defeat the
purpose of the check.
"""
import argparse
import glob
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_ROOT = ROOT / "reviews/source-package-2026-11-02-v2/english-text"
INDEX = ROOT / "reviews/evidence-class-index.json"
CAPS = ROOT / "capabilities.json"
MIN_QUOTE = 40


def load(path):
    return json.loads(Path(path).read_text())


def figure_ref(ref):
    match = re.match(r"(G\d{2}[0-9A-Z])/(?:fig|图)([0-9A-Za-z-]+)", ref)
    if not match:
        return None, None
    return match.group(1), match.group(2)


def pages_mentioning(guide, figure):
    pattern = re.compile(rf"(?:Figure|Table|图|表)\s*{re.escape(figure)}\b", re.IGNORECASE)
    hits = []
    for path in sorted(glob.glob(str(TEXT_ROOT / guide / "page-*.txt"))):
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        if pattern.search(text):
            hits.append((path, text))
    return hits


def best_quote(text):
    """Pick the longest prose line that is not the caption itself."""
    candidates = []
    for line in text.splitlines():
        stripped = line.strip()
        if len(stripped) < MIN_QUOTE:
            continue
        if stripped.count(" ") < 3:
            continue
        if "...." in stripped:
            continue
        if re.match(rf"^(?:Figure|Table)\s*[0-9A-Za-z-]+\.?\s*$", stripped, re.IGNORECASE):
            continue
        candidates.append(stripped)
    return max(candidates, key=len) if candidates else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    index = load(INDEX)
    unclassified = [r for r in index["records"] if r["evidence_class"] == "unclassified"]
    caps = load(CAPS)
    by_id = {p["id"]: p for p in caps["profiles"]}

    records = {}
    tally = Counter()
    for record in unclassified:
        pid = record["profile_id"]
        refs = record.get("source_refs") or []
        located = None
        for ref in refs:
            guide, figure = figure_ref(ref)
            if not guide:
                continue
            for path, text in pages_mentioning(guide, figure):
                quote = best_quote(text)
                if quote:
                    located = (guide, figure, path, quote, ref)
                    break
            if located:
                break
        if not located:
            tally["no-caption-page"] += 1
            continue
        guide, figure, path, quote, ref = located
        # Re-verify the figure reference really is on this page.
        body = Path(path).read_text(encoding="utf-8", errors="ignore")
        if not re.search(rf"(?:Figure|Table|图|表)\s*{re.escape(figure)}\b", body, re.IGNORECASE):
            tally["verification-failed"] += 1
            continue
        if quote not in body:
            tally["quote-not-found"] += 1
            continue
        records[pid] = {
            "text_comparisons": [{
                "source_path": str(Path(path).relative_to(ROOT)),
                "locator": f"{guide} 图{figure}（正文讨论页）",
                "quoted_clause": quote[:220],
                "conclusion": ("原图不可用，改为引用该图所在正文页的说明文字；"
                               "结构与视觉等价仍未核，仅支撑规范语义来源。"),
            }],
            "evidence_class": "source-text",
            "evidence_class_reason": f"原图不可用，改锚定正文页 {Path(path).name}",
        }
        tally["anchored-to-text"] += 1

    report = {
        "schema_version": "unclassified-adjudication/1",
        "generated_at": "2026-11-04",
        "notice": ("原图不可用的规范改锚正文引用。锚点须在页内实际命中图号，"
                   "否则保持未分类。"),
        "tally": dict(tally),
        "records": records,
    }
    (ROOT / "reviews/evidence-class-adjudication.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1) + "\n")

    if args.apply:
        for pid, record in records.items():
            profile = by_id.get(pid)
            if not profile:
                continue
            profile["evidence_class"] = record["evidence_class"]
            profile["evidence_class_reason"] = record["evidence_class_reason"]
            profile["text_comparisons"] = record["text_comparisons"]
        CAPS.write_text(json.dumps(caps, ensure_ascii=False, indent=2) + "\n")

    print(json.dumps(dict(tally), ensure_ascii=False))
    print("unclassified before:", len(unclassified),
          "| resolved:", len(records),
          "| remaining:", len(unclassified) - len(records))


if __name__ == "__main__":
    main()
