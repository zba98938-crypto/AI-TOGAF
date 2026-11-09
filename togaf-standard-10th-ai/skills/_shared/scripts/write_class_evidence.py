#!/usr/bin/env python3
"""Write the per-profile evidence that the class routing now requires.

Three kinds of record are produced, each matched to one evidence class:

  source-text        text_comparisons with a quote that must exist in the cited asset
  project-convention convention_basis with rule id, rationale, owner and date
  source-figure      nothing new: the existing source-verification record is used

The quote text is never composed here. It comes from probe_evidence_feasibility.py,
which located the heading in the English page text and copied an actual sentence.
A record whose quote cannot be re-found at write time is skipped and reported, so a
stale probe cannot silently produce a fabricated citation.
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from source_quote import navigation_quote

ROOT = Path(__file__).resolve().parents[1]
CLASS_INDEX = ROOT / "reviews/evidence-class-index.json"
FEASIBILITY = ROOT / "reviews/evidence-class-feasibility.json"
CAPS = ROOT / "capabilities.json"

# Convention rules for project-defined profiles. The rationale states what the
# project decided and what the source does not settle, which is the honest claim.
CONVENTION_RATIONALE = {
    "default": "本项目按自身运营与治理需要约定该规范的字段与检查；所引来源未给出该粒度的强制定义。",
    "compat": "兼容模板保留既有制品的生成结构；来源仅提供名称与用途，字段为本项目约定。",
}


def load(path):
    return json.loads(Path(path).read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="写入 capabilities.json；不加时只生成报告")
    args = parser.parse_args()

    class_index = {r["profile_id"]: r for r in load(CLASS_INDEX)["records"]}
    feasibility = {r["profile_id"]: r for r in load(FEASIBILITY)["records"]}
    caps = load(CAPS)

    written = Counter()
    skipped = []
    records = {}

    for profile in caps["profiles"]:
        pid = profile["id"]
        klass = class_index.get(pid, {}).get("evidence_class")

        if klass == "source-text":
            probe = feasibility.get(pid, {})
            if not probe.get("feasible"):
                skipped.append({"profile_id": pid, "class": klass,
                                "reason": "可行性探针未定位到可引正文"})
                continue
            source_path = probe["source_path"]
            quote = probe["quoted_clause"]
            # Re-check at write time: the asset must still contain the quote.
            body = (ROOT / source_path).read_text(encoding="utf-8", errors="ignore")
            if quote not in body or navigation_quote(quote):
                skipped.append({"profile_id": pid, "class": klass,
                                "reason": "写入时复核失败：引文不在资产中或仅为目录导航"})
                continue
            records[pid] = {
                "text_comparisons": [{
                    "source_path": source_path,
                    "locator": probe["locator"],
                    "quoted_clause": quote,
                    "conclusion": ("已定位该来源段落，语义对应仍待逐字段专业核对；"
                                   "仅找到正文摘录不等于本规范定义已通过，字段与检查为项目约定。"),
                }],
            }
            written["source-text"] += 1

        elif klass == "project-convention":
            is_compat = str(profile.get("definition_status")) == "project-compatibility-template"
            records[pid] = {
                "convention_basis": {
                    "rule_id": "QL-CONV-" + hashlib.sha256(pid.encode()).hexdigest()[:12],
                    "rationale": CONVENTION_RATIONALE["compat" if is_compat else "default"],
                    "owner": profile["owner"],
                    "decided_at": "2026-11-04",
                    "scope": "项目操作约定；不声称来源未提出该要求",
                },
            }
            written["project-convention"] += 1

    report = {
        "schema_version": "evidence-class-records/1",
        "generated_at": "2026-11-04",
        "notice": ("引文为英文原文摘录，写入前逐条复核；约定依据为项目规则。"
                   "本文件记录的是依据，不是验收。"),
        "written": dict(written),
        "skipped": skipped,
        "skipped_count": len(skipped),
        "records": records,
    }
    (ROOT / "reviews/evidence-class-records.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1) + "\n")

    if args.apply:
        for profile in caps["profiles"]:
            record = records.get(profile["id"])
            if not record:
                continue
            if "text_comparisons" in record:
                profile["text_comparisons"] = record["text_comparisons"]
            if "convention_basis" in record:
                profile["convention_basis"] = record["convention_basis"]
        CAPS.write_text(json.dumps(caps, ensure_ascii=False, indent=2) + "\n")

    print(json.dumps(dict(written), ensure_ascii=False))
    print("skipped:", len(skipped))
    for item in skipped[:6]:
        print(" ", item["profile_id"], "|", item["reason"])


if __name__ == "__main__":
    main()
