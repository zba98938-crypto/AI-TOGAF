#!/usr/bin/env python3
"""Independently verify exported TOGAF data against the local source PDFs.

Structural failures fail the command. Extraction limitations are recorded as
quality findings and never promoted to translation or visual acceptance.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from source_paths import resolve as source_path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

import fitz
from PIL import Image
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
CAPTION = re.compile(r"^(Figure|Example|Table)\s+([A-Z0-9]+[-.]\d+)\s*[:.]\s*(.+)", re.S)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalized(text):
    return re.sub(r"\s+", " ", str(text).replace("\u00ad", "")).strip()


def characters(text):
    text = unicodedata.normalize("NFKC", str(text)).replace("\u00ad", "")
    return Counter(c for c in text if not c.isspace())


class Report:
    def __init__(self):
        self.errors = []
        self.quality_findings = []
        self.counts = Counter()

    def error(self, kind, **details):
        self.errors.append({"type": kind, **details})

    def quality(self, kind, **details):
        self.quality_findings.append({"type": kind, **details})

    def check(self, condition, kind, **details):
        if not condition:
            self.error(kind, **details)
        return bool(condition)


def read_json(path, report):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        report.error("unreadable-json", path=str(path), detail=str(exc))
        return {}


def within(path, base):
    return Path(path).resolve().is_relative_to(Path(base).resolve())


def require_path(base, value, report, owner, *, allow_parent=False):
    if not isinstance(value, str) or not value:
        report.error("missing-path", owner=owner, path=value)
        return None
    relative = unquote(value.split("#", 1)[0])
    p = (base / relative).resolve()
    if not allow_parent and not within(p, base):
        report.error("path-outside-root", owner=owner, path=value)
        return None
    if not p.is_file():
        report.error("missing-referenced-file", owner=owner, path=str(p))
        return None
    return p


def validate_source_crop(page, rect, image_path, report, owner):
    """Compare actual pixels with a fresh PDF render, not just a stored hash."""
    expected=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=rect,alpha=False)
    with Image.open(image_path) as image:
        actual=image.convert("RGB")
        identical=actual.size==(expected.width,expected.height) and actual.tobytes()==expected.samples
    report.check(identical,"image-pixels-differ-from-original-pdf-crop",image=owner,pdf_page=page.number+1)
    report.counts["image_crops_rendered_against_original_pdf"]+=1
    return identical


def validate_document_contract(data, report):
    schema=json.loads(Path(__file__).with_name("schemas").joinpath("document.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    for error in Draft202012Validator(schema).iter_errors(data):
        report.error("document-schema-invalid",document=data.get("id"),
                     field="/".join(map(str,error.absolute_path)),detail=error.message)
    report.counts["source_document_schemas_checked"]+=1


def validate_table(page, table, report):
    tid = table.get("id")
    rows, boxes = table.get("rows", []), table.get("cell_bboxes", [])
    height, width = table.get("row_count"), table.get("column_count")
    report.counts["table_fragments_checked"] += 1
    if not report.check(len(rows) == height and len(boxes) == height, "table-row-count", table=tid):
        return
    chars = []
    raw = page.get_text("rawdict", flags=fitz.TEXTFLAGS_RAWDICT & ~fitz.TEXT_PRESERVE_IMAGES)
    for block in raw["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                for char in span["chars"]:
                    b = char["bbox"]
                    chars.append(((b[0] + b[2]) / 2, (b[1] + b[3]) / 2, char["c"]))
    for ri, (row, cells) in enumerate(zip(rows, boxes)):
        if not report.check(len(row) == width and len(cells) == width, "table-column-count", table=tid, row=ri):
            continue
        for ci, (value, bbox) in enumerate(zip(row, cells)):
            report.counts["table_cells_checked"] += 1
            if bbox is None:
                report.check(value is None, "merged-cell-lost-null", table=tid, row=ri, column=ci)
                continue
            rect = fitz.Rect(bbox)
            if not report.check(not rect.is_empty and page.rect.contains(rect), "invalid-cell-bbox", table=tid, row=ri, column=ci):
                continue
            observed = "".join(c for x, y, c in chars if rect.x0 <= x < rect.x1 and rect.y0 <= y < rect.y1)
            # Character multisets ignore word wrapping but detect missing content and
            # values assigned to a different physical column. Raw source retains order.
            wanted, actual = characters(value or ""), characters(observed)
            report.check(wanted == actual, "table-cell-content-mismatch", table=tid, row=ri, column=ci,
                         exported=str(value)[:180], source=observed[:180],
                         missing_characters=dict(actual-wanted), extra_characters=dict(wanted-actual))


def validate_grid_coverage(page, tables, report, code):
    """Find source grids without the exporter's page clip to detect omitted rows.

    Checking only exported cells misses a final row that was clipped before
    export. This independently enumerates complete stroked grids on the page.
    """
    paths = []
    for drawing in page.get_drawings():
        if drawing['type'] != 's' or len(drawing['items']) > 4:
            continue
        if all(item[0] == 're' or item[0] == 'l' and
               (abs(item[1].x-item[2].x) < .1 or abs(item[1].y-item[2].y) < .1)
               for item in drawing['items']):
            paths.append(drawing)
    if not paths:
        return
    finder = page.find_tables(paths=paths, snap_tolerance=1, join_tolerance=1)
    for source_table in finder.tables:
        if source_table.row_count < 2 or source_table.col_count < 2:
            continue
        values = source_table.extract()
        if sum(bool(normalized(c or '')) for r in values for c in r) < 3:
            continue
        report.counts['unclipped_source_grids_checked'] += 1
        source_rect = fitz.Rect(source_table.bbox)
        exported = [t for t in tables if
                    (fitz.Rect(t['bbox'])+(-1,-1,1,1)).contains(source_rect)]
        report.check(bool(exported), 'source-grid-clipped-or-missing', document=code,
                     pdf_page=page.number+1, source_bbox=list(source_rect),
                     source_rows=source_table.row_count, source_columns=source_table.col_count)
        if exported:
            report.check(any(t['row_count'] == source_table.row_count and
                             t['column_count'] == source_table.col_count for t in exported),
                         'source-grid-dimensions-mismatch', document=code, pdf_page=page.number+1,
                         source_rows=source_table.row_count, source_columns=source_table.col_count)


def validate_document(data, pdf_path, markdown_path, report):
    code = data.get("id", pdf_path.stem[:-1])
    with fitz.open(pdf_path) as pdf:
        pages = data.get("pages", [])
        report.counts["documents_checked"] += 1
        report.check(data.get("source", {}).get("sha256") == sha(pdf_path), "source-pdf-hash", document=code)
        report.check(data.get("source", {}).get("page_count") == len(pdf), "declared-page-count", document=code)
        report.check(len(pages) == len(pdf), "lost-or-added-pages", document=code, expected=len(pdf), actual=len(pages))
        page_numbers = [p.get("pdf_page") for p in pages]
        report.check(page_numbers == list(range(1, len(pdf)+1)), "page-sequence", document=code, actual=page_numbers)
        md = markdown_path.read_text(encoding="utf-8") if markdown_path.is_file() else ""
        outline = data.get("outline", [])
        pdf_outline = [(x[0], x[1], x[2]) for x in pdf.get_toc(False) if x[2] >= 1]
        exported_outline = [(x.get("level"), x.get("raw_title", x.get("title")), x.get("pdf_page")) for x in outline]
        report.check(pdf_outline == exported_outline, "outline-source-mismatch", document=code)
        stack, ids = [], set()
        for sec in outline:
            while stack and stack[-1]["level"] >= sec["level"]:
                stack.pop()
            expected = stack[-1]["id"] if stack else None
            report.check(sec.get("parent_id") == expected, "outline-parent", document=code, section=sec.get("id"), expected=expected)
            report.check(sec.get("id") not in ids, "duplicate-section-id", document=code, section=sec.get("id"))
            report.check(1 <= sec.get("pdf_page", 0) <= sec.get("end_pdf_page", 0) <= len(pdf), "outline-page-range", document=code, section=sec.get("id"))
            ids.add(sec.get("id")); stack.append(sec)
        all_tables = []
        for record in pages:
            pn = record.get("pdf_page", 0)
            if not 1 <= pn <= len(pdf):
                continue
            page = pdf[pn-1]
            report.counts["pages_checked_against_pdf"] += 1
            report.check(record.get("raw_text") == page.get_text(sort=False), "raw-page-text-mismatch", document=code, pdf_page=pn)
            report.check(record.get("reading_order_text") == page.get_text(sort=True), "reading-order-text-mismatch", document=code, pdf_page=pn)
            report.check(f'id="page-{pn}"' in md, "missing-markdown-page", document=code, pdf_page=pn)
            source_blocks = [b for b in page.get_text("dict", flags=fitz.TEXTFLAGS_DICT & ~fitz.TEXT_PRESERVE_IMAGES)["blocks"] if b["type"] == 0]
            source_texts = ["\n".join("".join(s["text"] for s in line["spans"]) for line in b["lines"]) for b in source_blocks]
            report.check(source_texts == [b.get("text") for b in record.get("blocks", [])], "text-block-loss", document=code, pdf_page=pn)
            content = record.get("content", [])
            covered = {bid for item in content for bid in item.get("source_block_ids", [])}
            tables = record.get("tables", [])
            all_tables.extend(tables)
            for block in record.get("blocks", []):
                if block.get("role") != "body":
                    continue
                rect = fitz.Rect(block["bbox"])
                table_covered = any((fitz.Rect(t["bbox"])+(-1, -1, 1, 1)).contains(rect) for t in tables)
                report.check(block["id"] in covered or table_covered, "body-block-not-exported", document=code, pdf_page=pn, block=block["id"])
            for item in content:
                # The Markdown writer normalizes leading bullet symbols only.
                emitted = re.sub(r"^•\s", "- ", item.get("text", ""))
                report.check(emitted in md, "content-missing-from-markdown", document=code, pdf_page=pn, text=emitted[:120])
            for table in tables:
                validate_table(page, table, report)
                report.check(table.get("markdown", "") in md, "table-missing-from-markdown", table=table.get("id"))
            validate_grid_coverage(page, tables, report, code)
            if not record.get("raw_text", "").strip():
                report.quality("page-without-digital-text", document=code, pdf_page=pn)
            for block in page.get_text("blocks"):
                match = CAPTION.match(block[4].strip())
                if match and match[1] == "Table":
                    near = [t for t in tables if 0 <= t["bbox"][1]-block[3] < 200]
                    if not near:
                        report.quality("table-caption-without-nearby-grid", document=code, pdf_page=pn,
                                       caption=normalized(block[4]), bbox=list(block[:4]), explanation="原始文本保留；该图题附近未识别出结构化边框表格，需结合原页核对。")
        report.check(data.get("tables") == all_tables, "document-table-index-mismatch", document=code)


def validate_chunks(chunks, documents, translations, figures, root, corpus, report):
    seen, source_chunks, translation_chunks, hashes = set(), defaultdict(list), defaultdict(list), {}
    figure_chunks = defaultdict(list)
    for chunk in chunks:
        cid, code = chunk.get("id"), chunk.get("document_id")
        report.counts["chunks_checked"] += 1
        report.check(cid and cid not in seen, "duplicate-or-empty-chunk-id", chunk=cid)
        seen.add(cid)
        if not report.check(code in documents, "chunk-document-missing", chunk=cid, document=code):
            continue
        data = documents[code]
        report.check(chunk.get("language") in {"en", "zh"}, "chunk-language", chunk=cid)
        role = chunk.get("content_role")
        report.check(role in {"source", "translation", "figure"}, "chunk-role", chunk=cid)
        path = require_path(root, chunk.get("source_path"), report, cid)
        if path:
            if path not in hashes:
                hashes[path] = sha(path)
            report.check(chunk.get("source_sha256") == hashes[path], "chunk-source-hash", chunk=cid)
        require_path(corpus, chunk.get("markdown_path"), report, cid)
        pages = chunk.get("pdf_pages", [])
        report.check(isinstance(pages, list) and all(isinstance(p, int) and 1 <= p <= data["source"]["page_count"] for p in pages), "chunk-page-range", chunk=cid)
        report.check(isinstance(pages, list) and len(pages) == len(set(pages)), "chunk-pages-not-unique", chunk=cid)
        section_ids = {s["id"] for s in data.get("outline", [])}
        report.check(chunk.get("section_id") is None or chunk["section_id"] in section_ids, "chunk-section-missing", chunk=cid)
        for fid in chunk.get("figure_ids", []):
            report.check(fid in figures, "chunk-figure-missing", chunk=cid, figure=fid)
        if role == "source":
            report.check(chunk.get("language") == "en" and len(pages) == 1, "source-chunk-language-or-page", chunk=cid)
            report.check(chunk.get("source_path") == data["source"]["path"], "source-chunk-wrong-document", chunk=cid)
            if len(pages) == 1:
                source_chunks[(code, pages[0])].append(chunk)
        elif role == "translation":
            report.check((chunk.get("quality") or {}).get("status") == "translation-unverified", "translation-overclaims-review", chunk=cid)
            report.check(chunk.get("source_path") == translations.get(code, {}).get("source", {}).get("path"), "translation-chunk-source", chunk=cid)
            translation_chunks[code].append(chunk)
        elif role == "figure":
            for fid in chunk.get("figure_ids", []):
                figure_chunks[fid].append(chunk)
    for code, doc in documents.items():
        for page in doc["pages"]:
            exported = source_chunks[(code, page["pdf_page"])]
            expected = normalized("\n\n".join(i["text"] for i in page["content"]))
            actual = normalized("\n\n".join(c["text"] for c in exported))
            report.check(actual == expected, "source-content-not-fully-retrievable", document=code, pdf_page=page["pdf_page"])
            expected_ids = Counter(b for i in page["content"] for b in i.get("source_block_ids", []))
            actual_ids = Counter(b for c in exported for b in c.get("source_block_ids", []))
            report.check(expected_ids == actual_ids, "chunk-block-provenance", document=code, pdf_page=page["pdf_page"])
        if code in translations:
            expected = normalized(translations[code]["original_markdown"])
            actual = normalized("\n".join(c["text"] for c in translation_chunks[code]))
            report.check(expected == actual, "translation-content-not-fully-retrievable", document=code)
    for fid, entry in figures.items():
        parts = figure_chunks[fid]
        if not report.check(bool(parts), "figure-not-retrievable", figure=fid):
            continue
        if any("part_count" in c for c in parts):
            report.check([c.get("part") for c in parts] == list(range(1, len(parts)+1)) and
                         all(c.get("part_count") == len(parts) for c in parts), "figure-chunk-sequence", figure=fid)
        path = corpus/entry["json_path"]
        if not path.is_file():
            continue
        record = read_json(path, report)
        text = ("" if any("part_count" in c for c in parts) else "\n").join(c["text"] for c in parts)
        # Structure fields must survive retrieval serialization, including raster
        # tables and numeric matrix cells; OCR alone is not a substitute.
        for field in ("tables", "elements", "relationships"):
            value = record.get(field)
            if value:
                found = []
                for match in re.finditer('"' + field + r'"\s*:\s*', text):
                    try:
                        decoded, _ = json.JSONDecoder().raw_decode(text[match.end():])
                        found.append(decoded)
                    except ValueError:
                        continue
                report.check(value in found, "figure-structure-not-retrievable", figure=fid, field=field)
        if entry.get("source_role") == "editorial-added":
            report.check(all(c.get("quality", {}).get("status") == "zh-only-editorial" and not c.get("pdf_pages") for c in parts), "editorial-chunk-source-overclaim", figure=fid)


def markdown_links(corpus, root, report, pending_paths=()):
    pending = {Path(p).resolve() for p in pending_paths}
    for path in sorted(corpus.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"(?ms)^```.*?^```[^\n]*", "", text)
        report.counts["markdown_files_checked"] += 1
        for match in re.finditer(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
            target = match[1].strip("<>")
            if urlsplit(target).scheme:
                continue
            relative, _, anchor = target.partition("#")
            resolved = source_path(path.parent/unquote(relative)) if relative else path
            report.counts["markdown_links_checked"] += 1
            if not within(resolved, root):
                report.error("markdown-link-outside-project", file=str(path), target=target)
            elif not resolved.is_file() and resolved not in pending:
                report.error("broken-markdown-link", file=str(path), target=target)
            elif anchor and resolved.suffix == ".md" and anchor.startswith("page-"):
                report.check(f'id="{anchor}"' in resolved.read_text(encoding="utf-8"), "broken-markdown-page-anchor", file=str(path), target=target)


def validate_figures(corpus, root, documents, report):
    index = read_json(corpus/"figures/index.json", report)
    figures = {f["id"]: f for f in index.get("figures", [])}
    report.check(len(figures) == len(index.get("figures", [])), "duplicate-figure-id")
    images = index.get("embedded_images", [])
    image_ids = {i["id"] for i in images}
    report.check(len(image_ids) == len(images), "duplicate-image-id")
    pdfs = {code: fitz.open(root/data["source"]["path"]) for code, data in documents.items()}
    try:
        for fid, entry in figures.items():
            report.counts["figure_records_checked"] += 1
            path = require_path(corpus, entry.get("json_path"), report, fid)
            require_path(corpus, entry.get("markdown_path"), report, fid)
            if not path:
                continue
            data = read_json(path, report)
            provenance = data.get("provenance", {})
            code = entry["document_id"]
            pdf = pdfs.get(code)
            if not pdf:
                report.error("figure-document-missing", figure=fid); continue
            report.check(provenance.get("pdf_sha256") == documents[code]["source"]["sha256"], "figure-source-hash", figure=fid)
            if provenance.get("interpretation_path"):
                old = require_path(root, provenance["interpretation_path"], report, fid)
                if old:
                    report.check(sha(old) == provenance.get("interpretation_sha256"), "historical-figure-hash", figure=fid)
            elements = data.get("elements", [])
            element_ids = {e.get("id") for e in elements}
            report.check(len(elements) == len(element_ids), "duplicate-figure-element", figure=fid)
            parents = {e.get("id"): e.get("parent") for e in elements}
            for eid, parent in parents.items():
                seen = {eid}
                while parent:
                    if not report.check(parent in parents and parent not in seen, "invalid-figure-parent", figure=fid, element=eid, parent=parent):
                        break
                    seen.add(parent); parent = parents[parent]
            for rel in data.get("relationships", []):
                report.check(rel.get("from") in element_ids and rel.get("to") in element_ids, "figure-edge-endpoint", figure=fid, relationship=rel.get("id"))
            for rel in data.get("related_figures", []):
                report.check(rel.get("target") in figures, "figure-related-target", figure=fid, target=rel.get("target"))
            loc = data.get("figure", {}).get("en_location") or {}
            if provenance.get("source_role") == "editorial-added":
                report.check(not loc and not data.get("source_extraction"), "editorial-figure-mislabeled-as-original", figure=fid)
                report.quality("editorial-added-figure", figure=fid)
            for ext in data.get("source_extraction", []):
                pn = ext.get("pdf_page", 0)
                if not report.check(1 <= pn <= len(pdf), "figure-page-range", figure=fid):
                    continue
                page, rect = pdf[pn-1], fitz.Rect(ext["bbox_pdf_points"])
                report.check(not rect.is_empty and page.rect.contains(rect), "figure-crop-bounds", figure=fid, pdf_page=pn)
                image = require_path(corpus, ext.get("image_path"), report, fid)
                if image:
                    report.check(sha(image) == ext.get("image_sha256"), "figure-image-hash", figure=fid, pdf_page=pn)
                    validate_source_crop(page,rect,image,report,fid)
                digital = page.get_text("text", clip=rect, sort=True).strip()
                report.check(digital == ext.get("transcription", {}).get("digital_text"), "figure-digital-transcription", figure=fid, pdf_page=pn)
                report.counts["figure_crops_checked"] += 1
            if data.get("validation", {}).get("visual_review_scope") != "specific-findings-only":
                report.counts["figures_with_inherited_semantics"] += 1
        indexed_images = {i["id"]: i for i in images}
        for code, pdf in pdfs.items():
            for page in pdf:
                for block in page.get_text("blocks"):
                    match = CAPTION.match(block[4].strip())
                    if match and match[1] in {"Figure", "Example"}:
                        fid = code + "/" + ("fig" if match[1] == "Figure" else "ex") + match[2]
                        report.check(fid in figures, "source-caption-without-figure", figure=fid, pdf_page=page.number+1)
                for i, obj in enumerate(page.get_image_info(hashes=True, xrefs=True), 1):
                    rect = fitz.Rect(obj["bbox"]) & page.rect
                    if rect.is_empty or rect.is_infinite:
                        continue
                    key = f"{code}/image-p{page.number+1:04}-{i:02}"
                    entry = indexed_images.get(key)
                    report.counts["embedded_images_checked"] += 1
                    if not report.check(entry is not None, "embedded-image-not-indexed", image=key):
                        continue
                    report.check(entry.get("decoded_image_digest_md5") == obj["digest"].hex(), "embedded-image-digest", image=key)
                    for fid in entry.get("figure_ids", []):
                        report.check(fid in figures, "embedded-image-figure-missing", image=key, figure=fid)
                    if not entry.get("figure_ids"):
                        for field in ("json_path", "markdown_path", "image_path"):
                            require_path(corpus, entry.get(field), report, key)
                        image = corpus/entry.get("image_path", "")
                        if image.is_file():
                            report.check(sha(image) == entry.get("image_sha256"), "standalone-image-hash", image=key)
                            validate_source_crop(page,rect,image,report,key)
                        record_path = corpus/entry.get("json_path", "")
                        if record_path.is_file():
                            data = read_json(record_path, report)
                            report.check(data.get("provenance", {}).get("pdf_sha256") == documents[code]["source"]["sha256"], "standalone-image-source-hash", image=key)
                            for table in data.get("tables", []):
                                width = len(table.get("columns", []))
                                report.check(all(len(row) == width for row in table.get("rows", [])), "raster-table-column-count", image=key, table=table.get("id"))
                            review = data.get("current_visual_review", {})
                            if review:
                                report.check(review.get("source_pdf_sha256") == documents[code]["source"]["sha256"], "raster-table-review-source-hash", image=key)
                                if "numeric_cell_check" in review:
                                    check = review["numeric_cell_check"]
                                    report.check(not check.get("mismatches"), "raster-table-recorded-numeric-mismatch", image=key)
                                    report.counts["raster_table_numeric_cells_recorded"] += check.get("checked_cells", 0)
        # Standalone image records are also valid retrievable figure IDs.
        return {**figures, **{k: v for k, v in indexed_images.items() if v.get("json_path")}}
    finally:
        for pdf in pdfs.values():
            pdf.close()


def resolve_table_caption_findings(report, corpus, documents):
    """Find text tables on following pages or raster-table records for captions."""
    index = read_json(corpus/"figures/index.json", report)
    records = []
    for entry in index.get("figures", []) + index.get("embedded_images", []):
        if not entry.get("json_path"):
            continue
        path = corpus/entry["json_path"]
        if not path.is_file():
            continue
        data = read_json(path, report)
        if not data.get("tables"):
            continue
        pages = entry.get("pdf_pages") or [entry.get("pdf_page")]
        for page in pages:
            records.append((entry["document_id"], page, entry["id"], entry.get("bbox_pdf_points")))
    unresolved = []
    for finding in report.quality_findings:
        if finding["type"] != "table-caption-without-nearby-grid":
            unresolved.append(finding); continue
        code, pn = finding["document"], finding["pdf_page"]
        bbox = finding.get("bbox")
        candidates = []
        for doc, page, fid, image_bbox in records:
            if doc != code or page != pn:
                continue
            if not image_bbox or not bbox:
                candidates.append((0, fid)); continue
            below = image_bbox[1] - bbox[3]
            above = bbox[1] - image_bbox[3]
            distances = [gap for gap in (below, above) if -2 <= gap < 100]
            if distances:
                candidates.append((min(distances), fid))
        raster = [min(candidates)[1]] if candidates else []
        next_page = documents[code]["pages"][pn] if pn < len(documents[code]["pages"]) else {}
        tables_next = next_page.get("tables", [])
        near_bottom = bbox and bbox[1] > documents[code]["pages"][pn-1]["height"] * .65
        if raster:
            finding.update(type="raster-table-caption-covered", related_records=raster,
                           explanation="表格以栅格图存于原文，结构化转录见关联图记录；未把它计入网格自动提取。")
        elif near_bottom and tables_next:
            finding.update(type="table-caption-precedes-next-page-grid", related_records=[t["id"] for t in tables_next],
                           explanation="图题位于页末，结构化表格在下一页；保留分页关系。")
        elif re.search(r"\b(?:shows|describes|illustrates|provides)\b", finding["caption"]):
            finding.update(type="table-reference-in-prose", explanation="检测到正文表题引用，实际表格在后续页；不认定此处有缺失表格。")
        unresolved.append(finding)
    report.quality_findings = unresolved


def validate_reading_guide(corpus, root, documents, report):
    """Check derived reading-guide locators without asserting Chinese equivalence."""
    corpus, root = Path(corpus), Path(root)
    data = read_json(corpus/"reading-guide.json", report)
    report.check(data.get("content_role") == "derived-reading-guide", "reading-guide-role")
    guides = data.get("guides", [])
    ids = [g.get("id") for g in guides]
    report.check(set(ids) == set(documents) and len(ids) == len(set(ids)), "reading-guide-document-coverage")
    for suffix in ("json", "md"):
        template = root/"tools/togaf_corpus"/f"reading-guide.{suffix}"
        generated = corpus/f"reading-guide.{suffix}"
        report.check(template.is_file() and generated.is_file() and template.read_bytes() == generated.read_bytes(), "reading-guide-template-mismatch", file=f"reading-guide.{suffix}")
    markdown_path = corpus/"reading-guide.md"
    if markdown_path.is_file():
        page_links = re.findall(r"\]\(documents/(G[A-Z0-9]{3})\.md#page-(\d+)\)", markdown_path.read_text(encoding="utf-8"))
        expected_links = Counter((g["id"], str(p["evidence"]["pdf_page"])) for g in guides for p in g.get("key_points", []))
        actual_links = Counter(page_links)
        report.check(not (expected_links - actual_links), "reading-guide-evidence-markdown-links", missing_links=list((expected_links-actual_links).elements()))
    def quote_norm(text):
        text = unicodedata.normalize("NFKC", text).replace("\u00ad", "")
        text = re.sub(r"[‐‑‒–—−]", "-", text)
        return re.sub(r"\s+", " ", text).strip()
    for guide in guides:
        code = guide.get("id")
        if code not in documents:
            continue
        report.counts["reading_guides_checked"] += 1
        report.check(guide.get("content_role") == "derived-reading-guide", "reading-guide-entry-role", document=code)
        source = guide.get("source_pdf", {})
        report.check(source == documents[code]["source"], "reading-guide-source-metadata", document=code)
        path = require_path(root, source.get("path"), report, code)
        if not path:
            continue
        report.check(source.get("sha256") == sha(path), "reading-guide-source-hash", document=code)
        with fitz.open(path) as pdf:
            for point in guide.get("key_points", []):
                evidence = point.get("evidence", {})
                pn, quote = evidence.get("pdf_page", 0), evidence.get("quote_en", "")
                report.check(evidence.get("document_id") == code, "reading-guide-evidence-document", document=code)
                if not report.check(isinstance(pn, int) and 1 <= pn <= len(pdf), "reading-guide-evidence-page", document=code, pdf_page=pn):
                    continue
                report.counts["reading_guide_quotes_checked"] += 1
                page = pdf[pn-1]
                report.check(bool(quote) and quote_norm(quote) in quote_norm(page.get_text(sort=True)), "reading-guide-quote-not-on-source-page", document=code, pdf_page=pn, quote=quote)
                report.check(evidence.get("printed_page_label") == page.get_label(), "reading-guide-printed-page-label", document=code, pdf_page=pn)
        for related in guide.get("related_guides", []):
            report.check(related.get("id") in documents, "reading-guide-related-id", document=code, target=related.get("id"))


def validate(corpus, root=ROOT):
    corpus, root = Path(corpus).resolve(), Path(root).resolve()
    report = Report()
    index = read_json(corpus/"index.json", report)
    source_paths = {p.stem[:-1]: p for p in sorted((root/"togaf-standard-10th").glob("*.pdf"))}
    report.check(bool(source_paths), "source-pdfs-empty")
    entries = index.get("documents", [])
    report.check({d["id"] for d in entries} == set(source_paths), "document-coverage", expected=sorted(source_paths), actual=sorted(d["id"] for d in entries))
    report.check(len(entries) == len({d["id"] for d in entries}), "duplicate-document-id")
    documents, translations = {}, {}
    for entry in entries:
        code = entry["id"]
        path = require_path(corpus, entry.get("json"), report, code)
        md = require_path(corpus, entry.get("markdown"), report, code)
        if not path or not md or code not in source_paths:
            continue
        data = read_json(path, report); documents[code] = data
        validate_document_contract(data,report)
        validate_document(data, source_paths[code], md, report)
        tables = read_json(corpus/"tables"/f"{code}.json", report)
        report.check(tables.get("tables") == data.get("tables"), "table-sidecar-mismatch", document=code)
        if entry.get("translation_json"):
            path = require_path(corpus, entry["translation_json"], report, code)
            require_path(corpus, entry.get("translation_markdown"), report, code)
            if path:
                trans = read_json(path, report); translations[code] = trans
                original = require_path(root, trans.get("source", {}).get("path"), report, code)
                if original:
                    report.check(trans.get("source", {}).get("sha256") == sha(original), "translation-source-hash", document=code)
                    report.check(trans.get("original_markdown") == original.read_text(encoding="utf-8"), "translation-source-content", document=code)
                report.check(trans.get("quality") == "translation-unverified", "translation-document-overclaims-review", document=code)
                report.check(normalized("\n".join(s.get("markdown", "") for s in trans.get("sections", []))) == normalized(trans.get("original_markdown", "")), "translation-section-loss", document=code)
    figures = validate_figures(corpus, root, documents, report)
    resolve_table_caption_findings(report, corpus, documents)
    validate_reading_guide(corpus, root, documents, report)
    chunk_path = require_path(corpus, index.get("retrieval"), report, "index")
    chunks = []
    if chunk_path:
        for line_no, line in enumerate(chunk_path.read_text(encoding="utf-8").splitlines(), 1):
            try:
                chunks.append(json.loads(line))
            except ValueError:
                report.error("invalid-jsonl", line=line_no)
    validate_chunks(chunks, documents, translations, figures, root, corpus, report)
    report.check(index.get("counts", {}).get("documents") == len(documents), "index-document-count")
    report.check(index.get("counts", {}).get("pages") == report.counts["pages_checked_against_pdf"], "index-page-count")
    report.check(index.get("counts", {}).get("chunks") == len(chunks), "index-chunk-count")
    # These two files are the validator's own outputs. main() checks all links
    # again after writing them, so the first successful run is self-contained.
    markdown_links(corpus, root, report, pending_paths=(corpus/"quality/validation.json", corpus/"quality/validation.md"))
    for path in corpus.rglob("*.json"):
        if path == corpus/"quality/validation.json":
            continue
        read_json(path, report); report.counts["json_files_checked"] += 1
    if chunk_path:
        from query import search
        checks = []
        for term, code in [("业务能力", "G211"), ("value stream", "G178"), ("元数据", "G234")]:
            if code not in documents:
                continue
            found = search(term, corpus, docs=[code], languages=["en"], roles=["source"], limit=3)
            report.check(bool(found["results"]), "real-corpus-query-empty", query=term, document=code)
            checks.append({"query": term, "document": code, "returned_ids": [r["id"] for r in found["results"]]})
        report.query_checks = checks
    return {"schema_version": "togaf-corpus-validation/1", "passed": not report.errors,
            "corpus": str(corpus), "validator_sha256": sha(Path(__file__)),
            "counts": dict(report.counts), "error_count": len(report.errors), "errors": report.errors,
            "quality_finding_count": len(report.quality_findings), "quality_findings": report.quality_findings,
            "query_checks": getattr(report, "query_checks", []),
            "scope": "Source integrity, every PDF page text, table-cell geometry/content, outline, retrieval provenance and file references.",
            "limits": ["Does not certify translation equivalence or all historical figure semantics.", "Unstructured table captions are explicitly reported; raw PDF page text remains available."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=ROOT/"togaf-standard-10th-ai")
    parser.add_argument("--output", type=Path, help="validation JSON; default <corpus>/quality/validation.json")
    args = parser.parse_args(argv)
    try:
        result = validate(args.corpus)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(json.dumps({"passed": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    output = args.output or args.corpus/"quality/validation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    write_markdown_report(output.with_suffix(".md"), result)
    final_links = Report()
    markdown_links(args.corpus.resolve(), ROOT, final_links)
    if final_links.errors:
        result["errors"].extend(e for e in final_links.errors if e not in result["errors"])
        result["error_count"] = len(result["errors"])
        result["passed"] = False
    result["counts"].update(final_links.counts)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    write_markdown_report(output.with_suffix(".md"), result)
    print(json.dumps({k: result[k] for k in ("passed", "counts", "error_count", "quality_finding_count", "query_checks")}, ensure_ascii=False, indent=2))
    if result["errors"]:
        print(json.dumps(result["errors"][:12], ensure_ascii=False, indent=2), file=sys.stderr)
    return 0 if result["passed"] else 1


def write_markdown_report(path, result):
    counts = result["counts"]
    lines = ["# TOGAF 语料转换验证", "", "结果：**" + ("通过" if result["passed"] else "存在结构错误") + "**。", "",
             f"结构错误 {result['error_count']} 项；质量说明 {result['quality_finding_count']} 项。完整逐项记录见 [validation.json](validation.json)。", "",
             "| 验证对象 | 数量 |", "|---|---:|"]
    labels = {"documents_checked": "英文源文档", "pages_checked_against_pdf": "逐页对照原 PDF 的页面",
              "table_fragments_checked": "网格表格片段", "table_cells_checked": "按原 PDF 坐标核对的单元格",
              "unclipped_source_grids_checked": "不裁剪页面的原始表格完整性复核",
              "raster_table_numeric_cells_recorded": "图像转录记录中的独立数值检查",
              "figure_records_checked": "逻辑图记录", "figure_crops_checked": "图区域及数字文字",
              "image_crops_rendered_against_original_pdf": "重新渲染原 PDF 并逐像素核对的图片区域",
              "source_document_schemas_checked": "英文全文 JSON 数据契约",
              "embedded_images_checked": "嵌入图片对象", "chunks_checked": "检索块",
              "markdown_links_checked": "Markdown 本地引用", "json_files_checked": "JSON 文件",
              "reading_guides_checked": "中文导读的文档来源", "reading_guide_quotes_checked": "导读中逐页核对的英文证据短语"}
    for key, label in labels.items():
        lines.append(f"| {label} | {counts.get(key, 0)} |")
    lines += ["", "## 验证范围", "",
              "验证器独立打开原 PDF，核对每页 raw_text 与阅读顺序文本、文档指纹、页序及书签父子关系。表格按原 PDF 字符的物理位置核对每个单元格，检查内容遗失或错列；正文内容与检索块逐页对应。图区域指纹、数字文字、嵌入图像清单、结构引用及 Markdown 链接分别检查。", "",
              "## 质量说明", ""]
    finding_counts = Counter(f["type"] for f in result["quality_findings"])
    explanations = {
        "raster-table-caption-covered": "栅格表格已通过图像转录记录关联；与自动网格提取分开计数。",
        "table-caption-precedes-next-page-grid": "页末表题的表格位于下一页，保留跨页定位。",
        "table-reference-in-prose": "正文引用表题，未误认为本页缺少表格。",
        "editorial-added-figure": "中文编者自绘图，未标记为英文原图。",
        "table-caption-without-nearby-grid": "表题附近未找到结构化表格，需要按 JSON 中页码继续核对。",
        "page-without-digital-text": "原页缺少数字文本，需要结合图片和 OCR。",
    }
    for kind, count in sorted(finding_counts.items()):
        lines.append(f"- {count} 项：{explanations.get(kind, kind)}")
    if not finding_counts:
        lines.append("本轮未登记额外质量说明。")
    lines += ["", "## 检索抽查", ""]
    for check in result["query_checks"]:
        lines.append(f"- `{check['query']}` / {check['document']}：" + "、".join(f"`{x}`" for x in check["returned_ids"]) + "。")
    lines += ["", "## 验收边界", "",
              "本报告证明文件完整性、抽取结果与原始数字文本的一致性、结构和检索可达性。既有中文译文仍为 translation-unverified；历史图语义、OCR 字符以及所有箭头含义没有因自动检查通过而获得新的独立确认。",
              "", "表格字符核对忽略换行和空白，不等价于语义审校。图像矩阵的数值检查计数来自绑定原 PDF 指纹的独立转录检查记录，不属于普通数字文本抽取。", ""]
    lines += ["中文导读属于派生阅读辅助材料。验证仅确认其来源指纹、页码、英文证据短语、相关文档 ID 和模板一致性，不声称中文归纳与英文逐句等价。", ""]
    if result["errors"]:
        lines += ["## 结构错误", "", "```json", json.dumps(result["errors"], ensure_ascii=False, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
