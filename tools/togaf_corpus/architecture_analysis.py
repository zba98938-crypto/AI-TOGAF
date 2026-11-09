"""Build source-grounded architectural meaning from the 26 local Series Guides.

This authored semantic layer supplements the full-text conversion.  It does not
claim to be the normative TOGAF metamodel.  Source paraphrases and project
recommendations are kept separate, and every quoted anchor is independently
verified against the physical page in the original, hash-bound PDF.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re

import fitz

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = Path(__file__).with_name("architecture-analysis-data.json")
RELATION_TYPES = {
    "specialization": {"label_zh": "类型特化", "meaning_zh": "源概念是目标概念的一种具体类型；不表示人事层级。"},
    "part_of": {"label_zh": "组成", "meaning_zh": "源对象构成目标模型或复合对象的一部分；不推断排他拥有。"},
    "enables": {"label_zh": "使能", "meaning_zh": "源对象为目标活动或能力提供必要作用；不同于组成或因果充分条件。"},
    "realization": {"label_zh": "实现或具体化", "meaning_zh": "源对象在明确上下文中实现或具体化目标的抽象意义。"},
    "instantiates": {"label_zh": "实例化", "meaning_zh": "源对象是目标类型在特定上下文中的具体实例；不是类型特化、子能力或人员汇报。"},
    "governance": {"label_zh": "治理", "meaning_zh": "源对象对目标承担所注明的决策、过程或符合性责任；权力不能扩大。"},
    "flow": {"label_zh": "信息输入或反馈", "meaning_zh": "所引用证据中的信息向目标传递；不默认是运行时数据流或固定执行顺序。"},
    "mapping": {"label_zh": "关联映射", "meaning_zh": "两个视角中的对象有关联；不表示等价、包含或未声明的基数。"},
    "depends_on": {"label_zh": "依赖", "meaning_zh": "源对象按所注明语义需要目标；不推断完整因果网络。"},
    "classification": {"label_zh": "分类", "meaning_zh": "按指定维度分类或分组；不等同父子分解或人事汇报。"},
    "constraint": {"label_zh": "约束", "meaning_zh": "源架构、目标或政策对目标工作施加已注明约束；不表示人员直属关系。"},
}


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u00ad", "")).strip()


def source_text(text: str) -> str:
    # Converted table cells preserve line breaks as HTML; these are layout, not
    # words inserted into the source quotation.
    return norm(re.sub(r"<br\s*/?>", " ", text, flags=re.I))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def md_text(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def link_from(target: str, relative_document: str) -> str:
    """Both arguments are corpus-root-relative POSIX paths (target may anchor)."""
    path, marker, anchor = target.partition("#")
    rel = Path(os.path.relpath(path, Path(relative_document).parent)).as_posix()
    return rel + (marker + anchor if marker else "")


def evidence_link(evidence, here):
    label = f"{evidence['document_id']} PDF {evidence['pdf_page']}"
    return f"[{label}]({link_from(evidence['source_markdown_path'], here)})"


def evidence_lines(items, here):
    result = []
    for e in items:
        printed = f"；书页 {e['printed_page_label']}" if e.get("printed_page_label") else ""
        result += [f"- {evidence_link(e, here)}{printed}，证据 `{e['finding_id']}`：{e['quote_en']}"]
        location = []
        if e.get('source_section'):
            location.append('章节：' + e['source_section']['title'])
        if e.get('source_block_ids'):
            location.append('正文块：' + '、'.join('`' + bid + '`' for bid in e['source_block_ids']))
        if e.get('source_table_ids'):
            location.append('表格：' + '、'.join('`' + tid + '`' for tid in e['source_table_ids']))
        if e.get('source_section_candidates'):
            location.append('短引在多个章节出现，未自动归属：' + '、'.join(e['source_section_candidates']))
        if location:
            result += ['  ' + '；'.join(location) + '。']
    return result


def source_location_for_quote(doc, page_number, quote):
    """Attribute a quote to its source blocks, not the last heading on its page.

    A page may finish one role and introduce the next. Inclusive outline page
    ranges cannot disambiguate those paragraphs; the ordered content headings
    and the blocks actually containing the quote can.
    """
    sections = {s["id"]: s for s in doc["outline"]}
    active = None
    spans, parts, cursor = [], [], 0
    for page in doc["pages"][:page_number]:
        # Some multi-line PDF headings have no section_id in converted content.
        # Keep the outline's actual start coordinates as a fallback, not its
        # inclusive page ranges. A later heading must not claim earlier blocks.
        starts = []
        for section in doc['outline']:
            if section.get('pdf_page') == page['pdf_page']:
                heading = next((b for b in page['content'] if b.get('section_id') == section['id']), None)
                y = heading['bbox'][1] if heading and heading.get('bbox') else section.get('y', 0)
                starts.append((y, section['level'], section))
        starts.sort(key=lambda item: (item[0], item[1]))
        next_start = 0
        for block in page["content"]:
            block_y = block.get('bbox', [0, 0])[1]
            while next_start < len(starts) and starts[next_start][0] <= block_y:
                active = starts[next_start][2]
                next_start += 1
            if block.get("type") == "heading" and block.get("section_id") in sections:
                active = sections[block["section_id"]]
            if page["pdf_page"] != page_number:
                continue
            text = source_text(block.get("text", ""))
            if not text:
                continue
            if parts:
                cursor += 1
            spans.append((cursor, cursor + len(text), block, active))
            parts.append(text)
            cursor += len(text)
    text, needle = " ".join(parts).casefold(), norm(quote).casefold()
    occurrences = [m.start() for m in re.finditer(re.escape(needle), text)]
    if not needle or not occurrences:
        raise ValueError(f"{doc['id']}: quote cannot be located in source blocks on page {page_number}")
    matches = []
    for start in occurrences:
        blocks = [(block, section) for low, high, block, section in spans
                  if low < start + len(needle) and high > start]
        identities = {section["id"] if section else None for _, section in blocks}
        if len(identities) != 1:
            raise ValueError(f"{doc['id']}: quote crosses source sections on page {page_number}")
        matches.append((blocks, next(iter(identities))))
    section_ids = {section_id for _, section_id in matches}
    ambiguous = len(section_ids) != 1
    blocks = [block for matched, _ in matches for block in matched]
    section_id = None if ambiguous else matches[0][1]
    return {
        "source_section": {k: sections[section_id][k] for k in ("id", "title", "level")} if section_id else None,
        "source_block_ids": list(dict.fromkeys(bid for block, _ in blocks for bid in block.get("source_block_ids", []))),
        "source_table_ids": list(dict.fromkeys(block['table_id'] for block, _ in blocks if block.get('table_id'))),
        "section_attribution": "ambiguous-multiple-source-sections" if ambiguous else "quote-containing-source-blocks-and-preceding-content-heading",
        **({"source_section_candidates": sorted(s for s in section_ids if s)} if ambiguous else {}),
    }


def verify_and_enrich(root: Path, output: Path, data):
    """Fail closed on stale maintenance evidence or an unresolvable source quote."""
    expected = {p.stem for p in (output / "documents").glob("*.json")}
    supplied = [g["id"] for g in data["guides"]]
    if len(set(supplied)) != len(supplied):
        raise ValueError("Duplicate guide identifiers in architecture maintenance data")
    if set(supplied) != expected:
        raise ValueError(f"Architecture guide coverage mismatch: missing={expected-set(supplied)}, extra={set(supplied)-expected}")
    findings = {}
    page_checks = set()
    source_bytes = 0
    for guide in data["guides"]:
        code = guide["id"]
        doc = json.loads((output / "documents" / f"{code}.json").read_text(encoding="utf-8"))
        source = doc["source"]
        source_file = root / source["path"]
        actual_hash = hashlib.sha256(source_file.read_bytes()).hexdigest()
        if actual_hash != source["sha256"] or guide["source"]["sha256"] != actual_hash:
            raise ValueError(f"{code}: original PDF, converted corpus, and maintenance hash do not match")
        guide["source"] = source
        source_bytes += source["bytes"]
        with fitz.open(source_file) as pdf:
            if len(pdf) != source["page_count"]:
                raise ValueError(f"{code}: source page count changed")
            for finding in guide["source_findings"]:
                fid = finding["id"]
                if fid in findings:
                    raise ValueError(f"Duplicate finding {fid}")
                if finding["source_sha256"] != actual_hash or finding["document_id"] != code:
                    raise ValueError(f"{fid}: incorrect finding source binding")
                page_number = finding["pdf_page"]
                page = doc["pages"][page_number - 1]
                quote = norm(finding["quote_en"])
                direct = norm(pdf[page_number - 1].get_text())
                if quote.casefold() not in direct.casefold():
                    raise ValueError(f"{fid}: exact normalized quote absent from original PDF page {page_number}")
                corpus_text = source_text(page["reading_order_text"])
                if quote.casefold() not in corpus_text.casefold():
                    corpus_text = source_text(" ".join(c["text"] for c in page["content"]))
                if quote.casefold() not in corpus_text.casefold():
                    raise ValueError(f"{fid}: quote absent from converted document page {page_number}")
                if finding["printed_page_label"] != page["printed_page_label"]:
                    raise ValueError(f"{fid}: printed page label changed")
                location = source_location_for_quote(doc, page_number, quote)
                # Use complete paragraph context from the source page when available.
                original_position = direct.casefold().index(quote.casefold())
                evidence = {
                    "finding_id": fid,
                    "document_id": code,
                    "pdf_page": page_number,
                    "printed_page_label": page["printed_page_label"],
                    "source_path": source["path"],
                    "source_sha256": actual_hash,
                    "quote_en": direct[original_position:original_position + len(quote)],
                    "context_en": direct[max(0, original_position - 200):min(len(direct), original_position + len(quote) + 350)],
                    **location,
                    "source_markdown_path": f"documents/{code}.md#page-{page_number}",
                    "source_json_path": f"documents/{code}.json",
                    "verification": "source-PDF-SHA256-and-normalized-quote-on-physical-page",
                }
                finding["evidence"] = evidence
                finding["assertion_status"] = "authored-source-grounded-paraphrase"
                findings[fid] = finding
                page_checks.add((code, page_number))
    return findings, {
        "source_pdf_hashes_verified": len(supplied),
        "source_pdf_bytes_verified": source_bytes,
        "source_quote_checks": len(findings),
        "distinct_evidence_pages": len(page_checks),
        "all_quotes_found_directly_in_source_pdfs": True,
        "semantic_review_status": "authored-paraphrases-and-synthesis-with-source-anchors",
        "notice_zh": "逐条验证原文短引存在及来源指纹；这不等于独立专家已复核全部中文释义，也不表示每页均已形成语义断言。",
    }


def assert_acyclic(relations, relation_type):
    adjacency = {}
    for edge in relations:
        if edge["type"] == relation_type:
            adjacency.setdefault(edge["source"], []).append(edge["target"])
    visiting, done = set(), set()
    def visit(node):
        if node in visiting:
            raise ValueError(f"Cycle in {relation_type}: {node}")
        if node in done:
            return
        visiting.add(node)
        for target in adjacency.get(node, []):
            visit(target)
        visiting.remove(node)
        done.add(node)
    for node in adjacency:
        visit(node)


def build(root: Path = ROOT, output: Path | None = None):
    root = Path(root).resolve()
    output = Path(output).resolve() if output is not None else root / "togaf-standard-10th-ai"
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    findings, verification = verify_and_enrich(root, output, data)
    concepts, relations = data["concepts"], data["relationships"]
    concept_by_id = {c["id"]: c for c in concepts}
    if len(concept_by_id) != len(concepts):
        raise ValueError("Duplicate architecture concept identifier")
    if len({r["id"] for r in relations}) != len(relations):
        raise ValueError("Duplicate relationship identifier")
    for record in concepts + relations:
        if not record["evidence_ids"]:
            raise ValueError(f"{record['id']}: missing evidence")
        record["evidence"] = [findings[fid]["evidence"] for fid in record["evidence_ids"]]
        record["source_documents"] = sorted({e["document_id"] for e in record["evidence"]})
        record["boundary_status"] = "authored-anti-misreading-guidance"
    for rel in relations:
        if rel["source"] not in concept_by_id or rel["target"] not in concept_by_id:
            raise ValueError(f"{rel['id']}: unresolved concept endpoint")
        if rel["type"] not in RELATION_TYPES:
            raise ValueError(f"{rel['id']}: unknown relationship type")
        rel["is_hr_reporting_line"] = False
        rel["assertion_status"] = "authored-source-grounded-semantic-normalization"
    for kind in ("part_of", "specialization"):
        assert_acyclic(relations, kind)
    base = output / "architecture"
    policy = data["semantic_policy"]
    shared = {
        "schema_version": "togaf-architecture-analysis/1.0",
        "path_base": "corpus-root",
        "content_role": "authored-source-grounded-architecture-analysis",
        "maintenance_source": DATA_PATH.relative_to(root).as_posix() if DATA_PATH.is_relative_to(root) else str(DATA_PATH),
        "maintenance_sha256": hashlib.sha256(DATA_PATH.read_bytes()).hexdigest(),
        "semantic_policy": policy,
    }
    figure_index_file = output / "figures/index.json"
    figure_index = json.loads(figure_index_file.read_text(encoding="utf-8")) if figure_index_file.exists() else {"figures": []}
    guide_index = []
    for guide in data["guides"]:
        code = guide["id"]
        guide.update(shared)
        guide["application_analysis_status"] = "derived-project-recommendations-not-source-mandates-or-project-facts"
        guide["application_evidence_ids"] = [f["id"] for f in guide["source_findings"]]
        interpretation = guide.get('operational_interpretation')
        if interpretation:
            if interpretation.get('assertion_status') != 'project-derived-operating-model-not-source-mandate':
                raise ValueError(code + ': operational interpretation must identify its project-derived status')
            unknown = set(interpretation['evidence_ids']) - set(guide['application_evidence_ids'])
            if unknown:
                raise ValueError(code + ': unresolved operational interpretation evidence: ' + ', '.join(sorted(unknown)))
        guide["concept_ids"] = [c["id"] for c in concepts if code in c["source_documents"]]
        guide["relationship_ids"] = [r["id"] for r in relations if code in r["source_documents"]]
        guide["figures"] = [f for f in figure_index["figures"] if f["document_id"] == code]
        guide["figure_notice_zh"] = "这里链接本指南的图记录供逐项核对，不把历史图示释义自动当作已验证原文关系；图记录的独立质量与视觉审查状态优先。"
        guide["full_text"] = {"json_path": f"documents/{code}.json", "markdown_path": f"documents/{code}.md"}
        write_json(base / "guides" / f"{code}.json", guide)
        here = f"architecture/guides/{code}.md"
        lines = [f"# {code} · {guide['title_zh']}", "", guide["title_en"], "",
                 f"架构问题：{guide['architecture_question_zh']}", "",
                 f"[逐页英文全文]({link_from(guide['full_text']['markdown_path'], here)}) · [本分析 JSON]({code}.json)", "",
                 f"原始 PDF：`{guide['source']['path']}`；{guide['source']['page_count']} 个实体页。", "",
                 f"SHA-256：`{guide['source']['sha256']}`", "",
                 "这份分析补充完整转换文本。下面的“原文发现”是中文释义，短引、PDF实体页和源文件指纹用于核对；“项目应用建议”是依据这些发现编写的分析，不是原文强制要求。", "",
                 "## 作用范围与易误读处", "", guide["scope_and_misreading_zh"], "", "## 原文发现与证据", ""]
        for f in guide["source_findings"]:
            lines += [f"<a id=\"{f['id'].split(':')[1].lower()}\"></a>", "", f"### {f['id']} · {f['topic']}", "", f["statement_zh"], ""]
            lines += evidence_lines([f["evidence"]], here) + [""]
        lines += ["## 项目应用建议", "", "以下内容是基于本指南证据的建议。输入、输出与步骤不表示本项目已经具备或已经完成；采用前需要结合实际范围、约束和治理权责。", ""]
        for field, title in [("application_inputs_zh", "需要收集的输入"), ("application_outputs_zh", "建议形成的输出"), ("application_steps_zh", "应用步骤"), ("decision_criteria_zh", "决策与验收问题")]:
            lines += [f"### {title}", ""]
            lines += [f"{i}. {s}" for i, s in enumerate(guide[field], 1)] + [""]
        if interpretation:
            lines += ['## 从官方方法到项目执行', '', interpretation['notice_zh'], '',
                      '原文依据：' + '、'.join(f"[{fid}](#{fid.split(':')[1].lower()})" for fid in interpretation['evidence_ids']) + '。', '']
            for stage in interpretation['chain']:
                lines += [f"### {stage['stage']} · {stage['question_zh']}", '',
                          '输入：' + '；'.join(stage['inputs_zh']) + '。', '',
                          '形成：' + '；'.join(stage['outputs_zh']) + '。', '',
                          '接受条件：' + stage['acceptance_zh'], '']
            lines += ['### 四类角色如何改变决策与产出', '',
                      '以下任务契约是项目推导；具体制品按真实决策问题选择，并非G249规定的固定交付物清单。', '']
            for contract in interpretation['role_decision_contracts']:
                lines += [f"#### {contract['role']}", '', '决策范围：' + contract['decision_scope_zh'] + '。', '',
                          '输入：' + '；'.join(contract['inputs_zh']) + '。', '',
                          '分析：' + contract['analysis_zh'], '',
                          '建议产出：' + '；'.join(contract['outputs_zh']) + '。', '',
                          '接受条件：' + contract['acceptance_zh'], '']
            example = interpretation['example']
            lines += ['### 虚构方法示例', '', example['scenario_zh'], '', example['trace_zh'], '', example['boundary_zh'], '']
        lines += ["## 概念与关系", "", "概念：" + "、".join(f"[{concept_by_id[c]['label_zh']}]({link_from('architecture/concepts.md#'+c, here)})" for c in guide["concept_ids"]) + "。", ""]
        for rel in [r for r in relations if r["id"] in guide["relationship_ids"]]:
            lines += [f"- [{rel['id']}]({link_from('architecture/relationships.md#'+rel['id'].lower(), here)})：{concept_by_id[rel['source']]['label_zh']} → `{rel['type']}` → {concept_by_id[rel['target']]['label_zh']}；{rel['label_zh']}。"]
        lines += ["", "## 关联图记录", "", guide["figure_notice_zh"], ""]
        if guide["figures"]:
            for f in guide["figures"]:
                pages = ", ".join(str(x) for x in f["pdf_pages"])
                lines += [f"- [{f['id']} · {md_text(f.get('title_zh') or f['title_en'])}]({link_from(f['markdown_path'], here)})（PDF {pages}）"]
        else:
            lines += ["本指南未发现编号图记录；所有嵌入图像仍可在完整文档页及图像索引中查阅。"]
        write_md(base / "guides" / f"{code}.md", lines)
        guide_index.append({"id": code, "title_zh": guide["title_zh"], "title_en": guide["title_en"],
                            "architecture_question_zh": guide["architecture_question_zh"],
                            "source": guide["source"], "finding_count": len(guide["source_findings"]),
                            "concept_count": len(guide["concept_ids"]), "relationship_count": len(guide["relationship_ids"]),
                            "figure_count": len(guide["figures"]),
                            "json_path": f"architecture/guides/{code}.json", "markdown_path": here})
    counts = {"guides": len(guide_index), "source_findings": len(findings), "concepts": len(concepts),
              "relationships": len(relations), "relationship_types": dict(sorted(Counter(r["type"] for r in relations).items())),
              "explicit_cardinality_relations": sum(r["cardinality"] is not None for r in relations),
              "hr_reporting_relations": sum(r["is_hr_reporting_line"] for r in relations)}
    verification.update({"graph_endpoints_resolved": True, "strict_part_of_acyclic": True, "specialization_acyclic": True,
                         "all_guides_have_evidence": True, "all_concepts_and_relations_have_evidence": True})
    evidence_records = [{"id": f["id"], "topic": f["topic"], "statement_zh": f["statement_zh"],
                         "assertion_status": f["assertion_status"], "evidence": f["evidence"]} for f in findings.values()]
    write_json(base / "evidence.json", {**shared, "verification": verification, "findings": evidence_records})
    write_json(base / "concepts.json", {**shared, "concepts": concepts})
    write_json(base / "relationships.json", {**shared, "relation_types": RELATION_TYPES, "relationships": relations})
    write_json(base / "guides/index.json", {**shared, "guides": guide_index})
    write_md(base / "guides/index.md", ["# 26份指南的架构分析", "", "每份分析将原文发现和项目建议分开，并链接逐页全文、关键概念、类型化关系及图记录。", "",
        "| 指南 | 架构问题 | 证据数 |", "|---|---|---:|"] + [f"| [{g['id']} · {md_text(g['title_zh'])}]({g['id']}.md) | {md_text(g['architecture_question_zh'])} | {g['finding_count']} |" for g in guide_index])
    here = "architecture/concepts.md"
    lines = ["# 架构概念词典", "", policy["evidence_policy_zh"], "", policy["hierarchy_policy_zh"], "", "概念边界说明是防止误读的分析提示；本词典不是TOGAF官方规范元模型。", ""]
    for concept in concepts:
        lines += [f"<a id=\"{concept['id']}\"></a>", "", f"## {concept['label_zh']} · {concept['label_en']}", "",
                  f"标识：`{concept['id']}`；类别：`{concept['category']}`。", "", concept["definition_zh"], "",
                  f"边界与误读提示：{concept['boundary_zh']}", ""]
        lines += evidence_lines(concept["evidence"], here) + [""]
    write_md(base / "concepts.md", lines)
    here = "architecture/relationships.md"
    lines = ["# 架构关系与层级语义", "", policy["hierarchy_policy_zh"], "", policy["cardinality_policy_zh"], "", "关系是依据正文证据建立的语义标准化分析；箭头按各关系的说明解释，并非把所有关系视作同一种流程。", "", "## 关系类型", "", "| 类型 | 含义 |", "|---|---|"]
    lines += [f"| `{key}` · {v['label_zh']} | {v['meaning_zh']} |" for key, v in RELATION_TYPES.items()]
    lines += ["", "## 关系明细", ""]
    for rel in relations:
        a, b = concept_by_id[rel["source"]], concept_by_id[rel["target"]]
        cardinality = json.dumps(rel["cardinality"], ensure_ascii=False) if rel["cardinality"] else "未在所引证据中规定"
        lines += [f"<a id=\"{rel['id'].lower()}\"></a>", "", f"### {rel['id']} · {rel['label_zh']}", "",
                  f"[{a['label_zh']}](concepts.md#{a['id']}) → `{rel['type']}` → [{b['label_zh']}](concepts.md#{b['id']})", "",
                  rel["meaning_zh"], "", f"关系方向语义：`{rel['direction']}`；基数：{cardinality}。", "",
                  f"不可推断：{rel['forbidden_inference_zh']}", ""]
        lines += evidence_lines(rel["evidence"], here) + [""]
    write_md(base / "relationships.md", lines)
    write_md(base / "evidence.md", ["# 架构分析证据索引", "", "以下短引已独立匹配原始PDF的实体页，并核对SHA-256；中文释义为人工编写分析。完整证据及上下文见 [JSON](evidence.json)。", "",
        "| 发现 | 中文释义 | 原文证据 |", "|---|---|---|"] +
        [f"| [{f['id']}](guides/{f['document_id']}.md#{f['id'].split(':')[1].lower()}) | {md_text(f['statement_zh'])} | {evidence_link(f['evidence'], 'architecture/evidence.md')} · {md_text(f['quote_en'])} |" for f in findings.values()])
    index = {**shared, "counts": counts, "verification": verification, "guides": guide_index,
             "outputs": {"guides_json": "architecture/guides/index.json", "guides_markdown": "architecture/guides/index.md",
                         "concepts_json": "architecture/concepts.json", "concepts_markdown": "architecture/concepts.md",
                         "relationships_json": "architecture/relationships.json", "relationships_markdown": "architecture/relationships.md",
                         "evidence_json": "architecture/evidence.json", "evidence_markdown": "architecture/evidence.md"}}
    write_json(base / "index.json", index)
    write_md(base / "index.md", ["# TOGAF架构语义分析", "",
        f"覆盖 {counts['guides']} 份本地指南，形成 {counts['source_findings']} 条原文发现、{counts['concepts']} 个概念和 {counts['relationships']} 条类型化关系。完整英文正文仍在逐页文档中保存；本层提炼关键架构知识并支持应用判断。", "",
        "- [逐指南分析](guides/index.md)：架构问题、原文发现、输入输出、步骤和决策条件。",
        "- [概念词典](concepts.md)：定义、上下文与容易混淆的边界。",
        "- [关系与层级](relationships.md)：组成、类型、使能、实现、治理、流、映射、依赖、分类和约束。",
        "- [原文证据](evidence.md)：PDF实体页、书页、短引、源文件指纹。", "",
        "## 使用约定", "", policy["evidence_policy_zh"], "", policy["recommendation_policy_zh"], "",
        policy["cardinality_policy_zh"], "", policy["hierarchy_policy_zh"], "", policy["source_scope_zh"], "",
        "## 校验范围", "",
        f"已核对 {verification['source_pdf_hashes_verified']} 份源PDF指纹及 {verification['source_quote_checks']} 条原文短引，证据涉及 {verification['distinct_evidence_pages']} 个不同实体页。图谱端点、证据引用、组成无环和特化无环检查通过。", "",
        verification["notice_zh"], "", "图记录中的历史语义与当次视觉校验保留各自状态；此分析不会把未知图形关系升级为确定事实。", ""])
    return index


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(args.root, args.output)
    print(json.dumps({"counts": result["counts"], "verification": result["verification"]}, ensure_ascii=False, indent=2))
