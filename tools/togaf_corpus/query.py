#!/usr/bin/env python3
"""Search the local TOGAF JSONL corpus with auditable bilingual term expansion.

This is lexical retrieval, not answer generation. It preserves source locations
and quality labels and needs only Python's standard library.
"""
from __future__ import annotations

import argparse
import fileinput
import json
import math
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]

# Terminology and guide topics from togaf-standard-10th-zh/README.md, with
# explicit plural and abbreviation variants for retrieval, not definitions.
TERMS = (
    ("首席架构师", "Chief Architect"),
    ("企业架构师", "Enterprise Architect"),
    ("技能要求", "技能", "Skill", "Skills", "Competency"),
    ("能力实例", "Business Capability Instance", "Instantiates"),
    ("上下级", "层级", "Hierarchy", "Containment"),
    ("汇报", "Reports to", "Reporting"),
    ("业务场景", "Business Scenario", "Business Scenarios"),
    ("业务模型", "Business Model", "Business Models"),
    ("业务能力规划", "Business Capability Planning"),
    ("信息映射", "Information Mapping"),
    ("组织映射", "Organization Mapping"),
    ("架构项目管理", "Architecture Project Management"),
    ("架构技能框架", "Architecture Skills Framework"),
    ("架构成熟度模型", "Architecture Maturity Models", "Architecture Maturity Model"),
    ("企业敏捷性", "Enterprise Agility"),
    ("敏捷冲刺", "Agile Sprint", "Agile Sprints"),
    ("数字企业", "Digital Enterprise"),
    ("数字技术采用就绪度评估", "Digital Technology Adoption Readiness Assessment"),
    ("政府参考模型", "Government Reference Model", "GRM"),
    ("数字业务参考模型", "Digital Business Reference Model", "DBRM"),
    ("微服务架构", "Microservices Architecture", "MSA"),
    ("元数据管理", "Metadata Management"),
    ("元数据", "Metadata"),
    ("商业智能", "Business Intelligence", "BI"),
    ("环境可持续的信息系统", "Environmentally Sustainable Information Systems"),
    ("架构角色与技能", "Architecture Roles and Skills"),
    ("风险与安全", "Risk and Security"),
    ("架构开发方法", "Architecture Development Method", "ADM"),
    ("企业架构", "Enterprise Architecture"),
    ("架构能力", "Architecture Capability", "Architecture Capabilities"),
    ("架构治理", "Architecture Governance"),
    ("架构存储库", "Architecture Repository"),
    ("企业连续体", "Enterprise Continuum"),
    ("架构全景", "架构景观", "Architecture Landscape"),
    ("架构构建块", "Architecture Building Block", "Architecture Building Blocks", "ABB"),
    ("解决方案构建块", "Solution Building Block", "Solution Building Blocks", "SBB"),
    ("过渡架构", "Transition Architecture", "Transition Architectures"),
    ("架构愿景", "Architecture Vision"),
    ("基线架构", "Baseline Architecture"),
    ("目标架构", "Target Architecture"),
    ("利益相关者", "干系人", "Stakeholder", "Stakeholders"),
    ("关注点", "Concern", "Concerns"),
    ("视图", "View", "Views"),
    ("视角", "视点", "Viewpoint", "Viewpoints"),
    ("价值流", "Value Stream", "Value Streams"),
    ("价值流阶段", "Value Stream Stage", "Value Stream Stages"),
    ("价值项", "Value Item", "Value Items"),
    ("触发", "Trigger", "Triggers"),
    ("业务能力", "Business Capability", "Business Capabilities"),
    ("基于能力的规划", "Capability-Based Planning"),
    ("架构委员会", "Architecture Board"),
    ("架构合同", "Architecture Contract", "Architecture Contracts"),
    ("合规性审查", "Compliance Review"),
    ("架构工作请求", "Request for Architecture Work"),
    ("架构工作说明书", "Statement of Architecture Work"),
    ("成熟度级别", "Maturity Level", "Maturity Levels"),
    ("熟练等级", "Proficiency Level", "Proficiency Levels"),
    ("组织地图", "Organization Map", "Organization Mapping"),
    ("组织架构图", "Organization Chart"),
    ("组织单元", "Organization Unit", "Organization Units"),
    ("分段架构师", "Segment Architect"),
    ("解决方案架构师", "Solution Architect"),
    ("技术债务", "Technical Debt"),
    ("最小可行架构", "Minimum Viable Architecture", "MVA"),
    ("最小可行产品", "Minimum Viable Product", "MVP"),
    ("主数据管理", "Master Data Management", "MDM"),
    ("客户主数据", "Customer Master Data", "C-MDM"),
    ("内核客户数据", "Kernel Customer Data"),
    ("数字可持续性", "Digital Sustainability"),
    ("温室气体", "Greenhouse Gas", "GHG"),
    ("变革画像", "Change Profile"),
    ("构建块", "Building Block", "Building Blocks"),
)
STOP_EN = frozenset("a an and are as at be by can for from how in is it of on or that the this to what when where which with".split())
STOP_ZH = frozenset(("什么", "如何", "怎样", "为何", "为什么", "介绍", "解释", "有关", "关于", "以及", "中的", "是什", "么是", "什么是"))


def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).lower()
    value = re.sub(r"[‐‑‒–—−]", "-", value)
    return re.sub(r"\s+", " ", value).strip()


def pattern(term: str) -> re.Pattern:
    """English aliases respect word boundaries; Chinese matches substrings."""
    escaped = re.escape(term).replace(r"\ ", r"\s+")
    if re.search(r"[a-z0-9]", term) and not re.search(r"[\u3400-\u9fff]", term):
        escaped = r"(?<![a-z0-9])" + escaped + r"(?![a-z0-9])"
    return re.compile(escaped)


def expand_query(query: str) -> list[dict]:
    normalized = normalize(query)
    candidates: dict[str, dict] = {}

    def add(term: str, weight: float, reason: str) -> None:
        term = normalize(term)
        if term and (term not in candidates or candidates[term]["weight"] < weight):
            candidates[term] = {"term": term, "weight": weight, "reason": reason}

    add(normalized, 5.0, "query")
    for aliases in TERMS:
        if any(pattern(normalize(alias)).search(normalized) for alias in aliases):
            for alias in aliases:
                add(alias, 3.0, "bilingual-terminology")
    for word in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", normalized):
        if word not in STOP_EN and len(word) > 1:
            add(word, 1.0, "query-token")
    for run in re.findall(r"[\u3400-\u9fff]+", normalized):
        if len(run) > 1 and run not in STOP_ZH:
            add(run, 2.0, "query-token")
        for i in range(len(run) - 1):
            word = run[i:i + 2]
            if word not in STOP_ZH:
                add(word, 0.3, "chinese-bigram")
    return list(candidates.values())


def excerpt(text: str, terms: list[str], max_chars: int = 700) -> str:
    if len(text) <= max_chars:
        return text
    positions = [text.lower().find(t) for t in terms]
    positions = [p for p in positions if p >= 0]
    start = max(0, min(positions, default=0) - 160)
    end = min(len(text), start + max_chars)
    return ("…" if start else "") + text[start:end] + ("…" if end < len(text) else "")


def navigation_chunk(chunk: dict) -> bool:
    if chunk.get("content_kind") == "navigation":
        return True
    title = normalize(chunk.get("section_title") or "")
    if re.fullmatch(r"(?:table of )?contents|index|list of (?:figures|tables)|目录|索引|图目录|表目录", title):
        return True
    # PDF TOCs often place many dotted leaders in one extraction block.
    return len(re.findall(r"(?:\.\s*){4,}|…{2,}", chunk.get("text", ""))) >= 3


def search(query: str, corpus: Path, *, docs=(), languages=(), roles=(), limit=10, full_text=False, include_navigation=False, layer='all') -> dict:
    query = query.strip()
    if not query:
        raise ValueError("query must not be empty")
    chunk_path = Path(corpus) / "retrieval" / "chunks.jsonl"
    architecture_path = Path(corpus) / "retrieval" / "architecture-chunks.jsonl"
    chapter_path = Path(corpus) / "retrieval" / "chapter-chunks.jsonl"
    if layer not in {'all','source','architecture'}:
        raise ValueError('unknown layer '+layer)
    paths = [] if layer == 'architecture' else [chunk_path]
    if layer != 'source' and architecture_path.is_file():
        paths.append(architecture_path)
    if layer != 'source' and chapter_path.is_file():
        paths.append(chapter_path)
    if layer == 'architecture' and not paths:
        raise ValueError('Architecture retrieval is missing; run python3 tools/togaf_corpus/build_architecture.py')
    diagram_index = Path(corpus) / 'architecture/diagrams/index.json'
    current_diagrams = {}
    if diagram_index.is_file():
        current_diagrams = {d['id']:d for d in json.loads(diagram_index.read_text(encoding='utf-8'))['diagrams']}
    chapter_index = Path(corpus) / 'chapters/index.json'
    reviewed_sections = {}
    if chapter_index.is_file() and chapter_path.is_file():
        reviewed_sections = {d['document_id']:set(d.get('reviewed_section_ids',[]))
            for d in json.loads(chapter_index.read_text(encoding='utf-8'))['documents']}
    expanded = expand_query(query)
    matchers = [(term, pattern(term["term"])) for term in expanded]
    doc_filter = {d.upper().removesuffix("E") for d in docs}
    language_filter, role_filter = set(languages), set(roles)
    matches = []
    scanned = eligible = skipped_navigation = superseded_figures = superseded_translations = 0
    with fileinput.input(files=[str(p) for p in paths], openhook=fileinput.hook_encoded('utf-8')) as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                chunk = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at {fileinput.filename()}:{fileinput.filelineno()}: {exc.msg}") from exc
            if not isinstance(chunk, dict) or not isinstance(chunk.get("text"), str):
                raise ValueError(f"invalid chunk at {fileinput.filename()}:{fileinput.filelineno()}: expected an object with text")
            scanned += 1
            # Historical figure interpretations remain explicitly searchable,
            # but default results should use their current semantic record.
            if (layer == 'all' and not role_filter and architecture_path.is_file()
                    and chunk.get('content_role') == 'figure'
                    and any(fid in current_diagrams for fid in chunk.get('figure_ids', []))):
                superseded_figures += 1
                continue
            # Replace only an aligned, explicitly reviewed section. Old front
            # matter and sections not yet revised remain searchable as unverified.
            if (layer == 'all' and not role_filter and chunk.get('content_role') == 'translation'
                    and chunk.get('section_id') in reviewed_sections.get(chunk.get('document_id'),set())):
                superseded_translations += 1
                continue
            if not include_navigation and navigation_chunk(chunk):
                skipped_navigation += 1
                continue
            chunk_docs = set(chunk.get('document_ids') or [str(chunk.get('document_id', '')).upper()])
            if doc_filter and not doc_filter.intersection(chunk_docs):
                continue
            if language_filter and chunk.get("language") not in language_filter:
                continue
            if role_filter and chunk.get("content_role") not in role_filter:
                continue
            eligible += 1
            title = normalize(chunk.get("section_title") or "")
            body = normalize(chunk["text"])
            score, matched = 0.0, []
            for term, regex in matchers:
                title_count = len(regex.findall(title))
                body_count = len(regex.findall(body))
                if title_count or body_count:
                    matched.append(term["term"])
                    score += term["weight"] * (4 * min(title_count, 1) + math.log2(1 + min(body_count, 8)))
            if score:
                matches.append((score, chunk, matched))
    matches.sort(key=lambda item: (-item[0], str(item[1].get("id", ""))))
    results = []
    for score, chunk, matched in matches[:limit]:
        result = {k: chunk.get(k) for k in (
            "id", "document_id", "language", "content_role", "content_kind", "section_id", "section_title",
            "pdf_pages", "source_sha256", "source_path", "markdown_path", "figure_ids", "quality",
            "document_ids", "source_locators", "json_path", "parent_record_id", "part", "part_count",
        )}
        role = chunk.get("content_role")
        if role == 'figure':
            result['current_diagram_analysis'] = [
                {'id':fid,'json_path':current_diagrams[fid]['json_path'],
                 'markdown_path':current_diagrams[fid]['markdown_path'],
                 'notice_zh':'当前关系校正和撤销记录见此文件；本条保留历史图解释，不应覆盖当前解释。'}
                for fid in chunk.get('figure_ids', []) if fid in current_diagrams]
        result["retrieval_status"] = (
            "translation-unverified" if role == "translation" else
            "chapter-source-compared-revision-see-scope" if role == "chapter-review" else
            "figure-interpretation-see-quality" if role == "figure" else
            "authored-architecture-analysis-see-evidence" if role in {'architecture','role','diagram','concept','relationship'} else
            "source-extraction-see-quality"
        )
        result["score"] = round(score, 4)
        result["matched_terms"] = matched
        result["text"] = chunk["text"] if full_text else excerpt(chunk["text"], matched)
        result["text_truncated"] = result["text"] != chunk["text"]
        results.append(result)
    return {
        "schema_version": "togaf-corpus-query/1", "query": query,
        "search_mode": "lexical-with-bilingual-terminology",
        "corpus_path": str(Path(corpus).resolve()), "chunks_path": str(chunk_path.resolve()),
        "chunks_paths": [str(p.resolve()) for p in paths], "layer": layer,
        "filters": {"documents": sorted(doc_filter), "languages": sorted(language_filter), "roles": sorted(role_filter)},
        "expanded_terms": expanded, "scanned_chunks": scanned, "eligible_chunks": eligible,
        "include_navigation": include_navigation, "skipped_navigation_chunks": skipped_navigation,
        "superseded_historical_figure_chunks": superseded_figures,
        "superseded_translation_section_chunks": superseded_translations,
        "matched_chunks": len(matches), "returned_chunks": len(results), "results": results,
        "notice_zh": "结果为词项检索片段，不生成答案。translation为未验证旧译文，chapter-review为标明范围的章节对照校订及分析，二者均不冒充英文原文。默认查询仅替换已对齐且完成校订的旧译章节；显式--role translation仍可查历史。引用保留文档、PDF页码与来源指纹，派生内容的原PDF见source_locators。",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="Chinese or English search terms")
    parser.add_argument("--corpus", type=Path, default=ROOT / "togaf-standard-10th-ai")
    parser.add_argument("--doc", action="append", default=[], help="guide ID, e.g. G211; repeatable")
    parser.add_argument("--lang", choices=("en", "zh"), action="append", default=[])
    parser.add_argument("--role", choices=("source", "translation", "chapter-review", "figure", "architecture", "role", "diagram", "concept", "relationship"), action="append", default=[])
    parser.add_argument("--layer", choices=("all", "source", "architecture"), default="all", help="search full text, architecture semantics, or both")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--full-text", action="store_true", help="return complete chunk text instead of a 700-character excerpt")
    parser.add_argument("--include-navigation", action="store_true", help="include contents/index chunks; excluded by default")
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    try:
        result = search(" ".join(args.query), args.corpus, docs=args.doc, languages=args.lang,
                        roles=args.role, limit=args.limit, full_text=args.full_text, include_navigation=args.include_navigation, layer=args.layer)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "build_command": "python3 tools/togaf_corpus/build.py"}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
