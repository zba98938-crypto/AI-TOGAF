#!/usr/bin/env python3
"""Review each of the 86 deliverable sections against its own assembly contract.

Three judgements per section, each answerable from files:

  bound         did the assembled body actually receive a view/object/analysis?
  content       does the body contain concrete model-derived text, or only the
                generator's empty-section notice?
  honesty       does the section carry its gaps and unknowns as IDs rather than
                silently reading as complete?

The review reads the generated deliverable Markdown and the assembly rules. It does
not judge whether a business reader would agree, and says so in every record.
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviews/deliverable-chapter-review"
INDEX = ROOT / "reviews/deliverable-chapter-review-index.json"
CASE = ROOT / "examples/qianlin-synthetic/output/adaptive"
RULES = ROOT / "capability-addenda/deliverable-assembly-rules.json"

EMPTY_MARKERS = [
    "本章未绑定", "无绑定", "narrative-only", "未提供", "本章无",
]


def load(path):
    return json.loads(Path(path).read_text())


def split_sections(text):
    """Split a deliverable Markdown file on level-2 headings."""
    parts = re.split(r"\n## ", text)
    out = {}
    for part in parts[1:]:
        title, _, body = part.partition("\n")
        out[title.strip()] = body.strip("\n")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rules = load(RULES)["deliverables"]
    rules_by_id = {r["id"]: r for r in rules}

    records = []
    verdict_counts = Counter()
    by_deliverable = {}
    for path in sorted((CASE / "deliverables").glob("*.md")):
        deliverable_id = path.stem
        text = path.read_text()
        sections = split_sections(text)
        rule = rules_by_id.get(deliverable_id, {})
        chapter_records = []
        for section_rule in rule.get("sections", []):
            title = section_rule["title"]
            body = sections.get(title)
            if body is None:
                verdict = "unbound"
                finding = "生成文件中没有该章节"
            else:
                view_refs = re.findall(r"view[_ ]?id[^\n]*", body)
                has_ids = bool(re.findall(r"\b(QL-|v-)[A-Za-z0-9_-]+", body))
                empty = any(marker in body for marker in EMPTY_MARKERS)
                if empty and not has_ids:
                    verdict = "narrative-only-unverified"
                    finding = "章节只有说明性文字，没有可追溯的模型对象或视图"
                elif has_ids:
                    id_count = len(set(re.findall(r"\b(QL-|v-)[A-Za-z0-9_-]+", body)))
                    # Placeholder text is machine-generated filler, not a business
                    # statement. A chapter carrying only filler is structurally bound
                    # but has no reviewable content, and must say so.
                    placeholder = body.count("虚构设定：") + body.count("虚构责任人")
                    if placeholder >= 3:
                        verdict = "bound-placeholder-content"
                        finding = (f"含 {id_count} 个模型标识，但正文为合成占位值"
                                   f"（{placeholder} 处）；结构可核，内容不可接受")
                    else:
                        verdict = "bound-not-business-accepted"
                        finding = f"含 {id_count} 个模型标识，未做业务判断"
                else:
                    verdict = "narrative-only-unverified"
                    finding = "无模型标识，判为说明性文字"
            verdict_counts[verdict] += 1
            chapter_records.append({
                "deliverable_id": deliverable_id,
                "section_title": title,
                "bound": verdict,
                "verdict": verdict,
                "findings": [finding],
                "content_focus": section_rule.get("content_focus") or [],
                "declared_profiles": section_rule.get("profile_ids") or [],
                "declared_artifacts": section_rule.get("artifact_ids") or [],
                "reviewer": {
                    "id": "cursor-ai-reviewer",
                    "role": "AI-assisted reviewer (not a human signatory)",
                },
                "limitation": ("AI 辅助结构判断，非业务接受；未做行业专家复核，"
                               "不代表责任方已确认该章内容。"),
            })
        by_deliverable[deliverable_id] = chapter_records
        records.extend(chapter_records)

    if args.write:
        OUT.mkdir(parents=True, exist_ok=True)
        for deliverable_id, chapter_records in by_deliverable.items():
            payload = {
                "schema_version": "deliverable-chapter-review/1",
                "deliverable_id": deliverable_id,
                "source": f"examples/qianlin-synthetic/output/adaptive/deliverables/{deliverable_id}.md",
                "chapters": chapter_records,
                "verdicts": dict(Counter(r["verdict"] for r in chapter_records)),
                "notice": "结构判断，不是业务接受。",
            }
            (OUT / f"{deliverable_id}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=1) + "\n")

    index = {
        "schema_version": "deliverable-chapter-review-index/1",
        "generated_at": "2026-11-04",
        "notice": ("逐章结构判断。bound-not-business-accepted 表示该章有可追溯对象，"
                   "但业务内容未被责任方接受。"),
        "deliverables": len(by_deliverable),
        "chapters": len(records),
        "verdicts": dict(verdict_counts),
        "records": records,
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"deliverables": len(by_deliverable), "chapters": len(records),
                      "verdicts": dict(verdict_counts)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
