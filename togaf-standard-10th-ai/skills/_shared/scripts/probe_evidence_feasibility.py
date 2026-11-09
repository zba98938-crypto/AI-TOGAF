#!/usr/bin/env python3
"""Prove the source-text evidence path is actually feasible, per profile.

The proposal depends on one assumption: for a profile citing `G211 §4`, a real
sentence can be quoted from the English text. This script tests that assumption for
every source-text profile and reports, per profile, whether a quotable passage was
found. It does not write registry evidence; it only measures feasibility.

Locating rules, learned from the corpus:
  * A table-of-contents line contains dot leaders ("....") and must be rejected; the
    bare heading only appears on the body page.
  * Section headings look like "5.1.3. Risk Appetite" at line start.
  * A quotable passage is the longest prose line within the first N lines after the
    heading, at least MIN_QUOTE characters, containing at least two spaces.
"""
import argparse
import glob
import json
import re
from collections import Counter
from pathlib import Path
from source_quote import navigation_quote

ROOT = Path(__file__).resolve().parents[1]
TEXT_ROOT = ROOT / "reviews/source-package-2026-11-02-v2/english-text"
OUT = ROOT / "reviews/evidence-class-feasibility.json"
MIN_QUOTE = 40
HEADING_WINDOW = 40


def load(path):
    return json.loads(Path(path).read_text())


def guide_and_section(ref):
    """Parse either a section anchor (G211 §4) or a table anchor (G21H 表5-1)."""
    match = re.search(r"(G\d{2}[0-9A-Z])\s*§\s*([0-9]+(?:\.[0-9]+)*)", ref)
    if match:
        return match.group(1), match.group(2), "section"
    match = re.search(r"(G\d{2}[0-9A-Z])\s*(?:表|Table)\s*([0-9]+[-–][0-9]+)", ref)
    if match:
        return match.group(1), match.group(2).replace("–", "-"), "table"
    match = re.search(r"(G\d{2}[0-9A-Z])\s*附录\s*([A-Z](?:\.[0-9]+)?)", ref)
    if match:
        return match.group(1), match.group(2), "appendix"
    return None, None, None


def is_toc_line(line):
    return navigation_quote(line)


def find_heading_page(guide, section, kind):
    """Return ((page_path, line_index) | None, toc_hit_count)."""
    if kind == "section":
        pattern = re.compile(rf"^\s*{re.escape(section)}\.?\s+\S")
    elif kind == "table":
        pattern = re.compile(rf"^\s*(?:Table|表)\s*{re.escape(section)}\b", re.IGNORECASE)
    else:
        pattern = re.compile(rf"^\s*(?:Appendix|附录)\s*{re.escape(section)}\b", re.IGNORECASE)
    toc_hits, body_hits = [], []
    for path in sorted(glob.glob(str(TEXT_ROOT / guide / "page-*.txt"))):
        lines = Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()
        for index, line in enumerate(lines):
            if not pattern.search(line):
                continue
            if is_toc_line(line):
                toc_hits.append((path, index))
            else:
                body_hits.append((path, index))
    if body_hits:
        return body_hits[0], len(toc_hits)
    if toc_hits:
        return None, len(toc_hits)
    return None, 0


def extract_quote(page_path, line_index):
    lines = Path(page_path).read_text(encoding="utf-8", errors="ignore").splitlines()
    window = lines[line_index + 1: line_index + HEADING_WINDOW]
    candidates = []
    heading_words = set(re.findall(r'[a-z]{4,}', lines[line_index].lower())) - {'phase', 'architecture', 'the', 'and'}
    for line in window:
        text = line.strip()
        # Do not borrow a sentence from the next section merely because it is longer.
        if re.match(r'^\d+(?:\.\d+)*\.?\s+[A-Z]', text):
            break
        if len(text) < MIN_QUOTE:
            continue
        if text.count(" ") < 3:
            continue
        if is_toc_line(text):
            continue
        if text.startswith(('Location in the Architecture Framework:', '© ', 'Copyright ')):
            continue
        if re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)?\s*\.{2,}", text):
            continue
        candidates.append(text)
    if not candidates:
        return None
    # A heading-word match is a location aid only, never a semantic acceptance.
    return max(candidates, key=lambda s: len(heading_words & set(re.findall(r'[a-z]{4,}', s.lower()))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(OUT))
    args = parser.parse_args()

    # The review index is historical and may have fewer profiles than the live registry.
    text_profiles = [dict(p, profile_id=p['id']) for p in load(ROOT/'capabilities.json')['profiles']
                     if p.get('evidence_class') == 'source-text']

    results = []
    tally = Counter()
    for record in text_profiles:
        refs = record.get("source_refs") or []
        located = None
        toc_hits = 0
        for ref in refs:
            guide, section, kind = guide_and_section(ref)
            if not guide:
                continue
            (found, toc) = find_heading_page(guide, section, kind)
            toc_hits += toc
            if found:
                located = (guide, section, kind, found, ref)
                break
        if not located:
            tally["no-heading-located"] += 1
            results.append({
                "profile_id": record["profile_id"],
                "feasible": False,
                "reason": "未在英文文本中定位到该章节正文标题（仅目录命中或不存在）",
                "toc_hits": toc_hits,
            })
            continue
        guide, section, kind, (page_path, line_index), ref = located
        quote = extract_quote(page_path, line_index)
        if not quote:
            tally["heading-found-no-quote"] += 1
            results.append({
                "profile_id": record["profile_id"],
                "feasible": False,
                "reason": "找到正文标题，但后续窗口内没有足够长度的连续散文可引",
                "page": str(Path(page_path).relative_to(ROOT)),
                "section": f"{guide} §{section}",
            })
            continue
        tally["feasible"] += 1
        locator = f"{guide} §{section}" if kind == "section" else (
            f"{guide} 表{section}" if kind == "table" else f"{guide} 附录{section}")
        results.append({
            "profile_id": record["profile_id"],
            "feasible": True,
            "source_path": str(Path(page_path).relative_to(ROOT)),
            "locator": locator,
            "anchor_kind": kind,
            "quoted_clause": quote[:220],
            "quote_length": len(quote),
            "toc_hits": toc_hits,
        })

    payload = {
        "schema_version": "evidence-class-feasibility/1",
        "generated_at": "2026-11-04",
        "status": "feasibility probe; writes no registry evidence",
        "notice": ("本文件只测可行性：能否为每条 source-text 规范摘出一段可检索原文。"
                   "可行性通过不等于证据已提交，也不是验收。"),
        "counts": dict(tally),
        "probed": len(text_profiles),
        "records": results,
    }
    Path(args.out).write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(dict(tally), ensure_ascii=False))
    print("probed:", len(text_profiles))


if __name__ == "__main__":
    main()
