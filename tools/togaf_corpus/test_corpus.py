#!/usr/bin/env python3
"""Regression checks for source loss, swapped cells and bilingual retrieval."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import fitz
from PIL import Image

import build
from query import search
from validate import Report, validate_document, validate_table, validate_chunks, validate_grid_coverage, validate_source_crop


class CorpusRegression(unittest.TestCase):
    def test_current_diagram_replaces_historical_default_but_history_is_accessible(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);(folder/'retrieval').mkdir();(folder/'architecture/diagrams').mkdir(parents=True)
            old={'id':'old','document_id':'G152','language':'zh','content_role':'figure',
                 'text':'Loss event triggers Risk','figure_ids':['G152/fig5-2']}
            current={'id':'new','document_id':'G152','language':'zh','content_role':'diagram',
                     'text':'Loss event association Risk; no arrow','figure_ids':['G152/fig5-2']}
            (folder/'retrieval/chunks.jsonl').write_text(json.dumps(old)+'\n')
            (folder/'retrieval/architecture-chunks.jsonl').write_text(json.dumps(current)+'\n')
            (folder/'architecture/diagrams/index.json').write_text(json.dumps({'diagrams':[{
                'id':'G152/fig5-2','json_path':'architecture/diagrams/G152/fig5-2.json',
                'markdown_path':'architecture/diagrams/G152/fig5-2.md'}]}))
            result=search('Loss event',folder)
            self.assertEqual([x['id'] for x in result['results']],['new'])
            self.assertEqual(result['superseded_historical_figure_chunks'],1)
            history=search('Loss event',folder,roles=['figure'])
            self.assertEqual(history['results'][0]['id'],'old')
            self.assertEqual(history['results'][0]['current_diagram_analysis'][0]['id'],'G152/fig5-2')
            self.assertEqual(search('Loss event',folder,layer='source')['results'][0]['id'],'old')

    def test_source_bottom_rows_are_structured_and_missing_row_detected(self):
        root = Path(__file__).resolve().parents[2]
        with fitz.open(root/'togaf-standard-10th/G249e.pdf') as doc:
            for pn, expected_rows, label in [(27, 20, 'Integration and Sharing'), (28, 33, 'Oral Communication')]:
                p = doc[pn-1]
                tables = build.parse_tables(p, 'G249', pn, build.text_blocks(p, 'G249', pn))
                table = next(t for t in tables if t['column_count'] == 8)
                self.assertEqual(table['row_count'], expected_rows)
                self.assertEqual(table['rows'][-1][1], label)
                report = Report(); validate_grid_coverage(p, tables, report, 'G249')
                self.assertEqual(report.errors, [])
                broken = copy.deepcopy(tables)
                for t in broken:
                    if t['column_count'] == 8:
                        t['bbox'][3] = t['cell_bboxes'][-2][0][3]
                        t['rows'].pop(); t['cell_bboxes'].pop(); t['row_count'] -= 1
                report = Report(); validate_grid_coverage(p, broken, report, 'G249')
                self.assertIn('source-grid-clipped-or-missing', {e['type'] for e in report.errors})

    def test_real_tables_do_not_duplicate_cells_and_keep_one_column(self):
        root = Path(__file__).resolve().parents[2]
        with fitz.open(root/"togaf-standard-10th/G178e.pdf") as doc:
            page = doc[17]
            blocks = build.text_blocks(page, "G178", 18)
            tables = build.parse_tables(page, "G178", 18, blocks)
            self.assertEqual(sorted((t["row_count"], t["column_count"]) for t in tables), [(3, 6), (4, 2)])
        with fitz.open(root/"togaf-standard-10th/G248e.pdf") as doc:
            page = doc[42]
            blocks = build.text_blocks(page, "G248", 43)
            tables = build.parse_tables(page, "G248", 43, blocks)
            self.assertEqual([(t["row_count"], t["column_count"]) for t in tables], [(23, 1)])
            report = Report(); validate_table(page, tables[0], report)
            self.assertEqual(report.errors, [])

    def make_pdf(self, folder):
        path = folder/"GTESTe.pdf"
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((50, 60), "Business Capability", fontsize=16)
        page.insert_text((50, 90), "A capability describes what an enterprise can do.")
        for x in (50, 200, 350):
            page.draw_line((x, 120), (x, 210))
        for y in (120, 150, 180, 210):
            page.draw_line((50, y), (350, y))
        for text, x, y in [("Name", 60, 140), ("Value", 210, 140), ("Alpha", 60, 170), ("123", 210, 170), ("Beta", 60, 200), ("456", 210, 200)]:
            page.insert_text((x, y), text)
        doc.new_page().insert_text((50, 60), "Second page must survive extraction.")
        doc.set_toc([[1, "Business Capability", 1], [2, "Details", 2]])
        doc.save(path); doc.close()
        return path

    def convert(self, folder):
        pdf = self.make_pdf(folder)
        output = folder/"corpus"
        output.mkdir()
        previous_root = build.ROOT
        build.ROOT = folder
        try:
            data, chunks = build.convert_document(pdf, output, [])
        finally:
            build.ROOT = previous_root
        return pdf, output, data, chunks

    def test_lost_page_and_lost_body_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); pdf, output, data, chunks = self.convert(folder)
            report = Report()
            validate_document(data, pdf, output/"documents/GTEST.md", report)
            self.assertEqual(report.errors, [])
            broken = copy.deepcopy(data); broken["pages"].pop()
            report = Report(); validate_document(broken, pdf, output/"documents/GTEST.md", report)
            self.assertIn("lost-or-added-pages", {e["type"] for e in report.errors})
            broken = copy.deepcopy(data); broken["pages"][0]["raw_text"] = ""
            report = Report(); validate_document(broken, pdf, output/"documents/GTEST.md", report)
            self.assertIn("raw-page-text-mismatch", {e["type"] for e in report.errors})

    def test_swapped_table_cells_detected_against_pdf_geometry(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf, output, data, chunks = self.convert(Path(tmp))
            table = copy.deepcopy(data["pages"][0]["tables"][0])
            table["rows"][1][0], table["rows"][1][1] = table["rows"][1][1], table["rows"][1][0]
            with fitz.open(pdf) as doc:
                report = Report(); validate_table(doc[0], table, report)
            self.assertIn("table-cell-content-mismatch", {e["type"] for e in report.errors})

    def test_changed_image_pixels_detected_even_when_saved_image_has_a_valid_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);pdf=self.make_pdf(folder);image_path=folder/'crop.png'
            with fitz.open(pdf) as doc:
                rect=fitz.Rect(45,40,400,105)
                doc[0].get_pixmap(matrix=fitz.Matrix(2,2),clip=rect,alpha=False).save(image_path)
                report=Report();self.assertTrue(validate_source_crop(doc[0],rect,image_path,report,'test'))
                with Image.open(image_path) as image:altered=image.convert('RGB')
                altered.putpixel((5,5),(255,0,255));altered.save(image_path)
                report=Report();self.assertFalse(validate_source_crop(doc[0],rect,image_path,report,'test'))
                self.assertIn('image-pixels-differ-from-original-pdf-crop',{e['type'] for e in report.errors})

    def test_outline_parent_and_missing_retrieval_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); pdf, output, data, chunks = self.convert(folder)
            broken = copy.deepcopy(data); broken["outline"][1]["parent_id"] = None
            report = Report(); validate_document(broken, pdf, output/"documents/GTEST.md", report)
            self.assertIn("outline-parent", {e["type"] for e in report.errors})
            report = Report(); validate_chunks(chunks[:-1], {"GTEST": data}, {}, {}, folder, output, report)
            self.assertIn("source-content-not-fully-retrievable", {e["type"] for e in report.errors})

    def test_chinese_query_finds_english_and_preserves_translation_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); (folder/"retrieval").mkdir()
            rows = [
                {"id": "en", "document_id": "G211", "language": "en", "content_role": "source", "section_title": "Business Capabilities", "text": "Business Capabilities describe what an enterprise does.", "pdf_pages": [10], "source_sha256": "abc"},
                {"id": "zh", "document_id": "G211", "language": "zh", "content_role": "translation", "section_title": "业务能力", "text": "业务能力译文。", "quality": {"status": "translation-unverified"}},
                {"id": "md", "document_id": "G234", "language": "en", "content_role": "source", "section_title": "Metadata", "text": "Metadata management."},
                {"id": "toc", "document_id": "G211", "language": "en", "content_role": "source", "content_kind": "navigation", "section_title": "Contents", "text": "Business Capability ............ 10"},
            ]
            (folder/"retrieval/chunks.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows))
            found = search("业务能力", folder, languages=["en"], roles=["source"])
            self.assertEqual([r["id"] for r in found["results"]], ["en"])
            self.assertEqual(found["results"][0]["pdf_pages"], [10])
            found = search("Business Capability", folder, languages=["zh"])
            self.assertEqual(found["results"][0]["retrieval_status"], "translation-unverified")
            self.assertEqual(search("元数据", folder, docs=["G234"], languages=["en"])["results"][0]["id"], "md")
            self.assertEqual(search("missing-zzxx", folder)["matched_chunks"], 0)
            self.assertIn("toc", [r["id"] for r in search("业务能力", folder, include_navigation=True)["results"]])

    def test_figure_table_missing_from_retrieval_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); pdf, output, data, chunks = self.convert(folder)
            image_json = output/"figure.json"
            table = {"columns": ["Role", "Level"], "rows": [["Architect", 4]]}
            image_json.write_text(json.dumps({"tables": [table]}))
            image_md = output/"figure.md"; image_md.write_text("# Figure")
            figures = {"GTEST/image-1": {"json_path": "figure.json"}}
            figure_chunk = {
                "id": "figure-chunk", "document_id": "GTEST", "language": "zh", "content_role": "figure",
                "source_path": pdf.name, "source_sha256": data["source"]["sha256"], "markdown_path": "figure.md",
                "pdf_pages": [1], "figure_ids": ["GTEST/image-1"], "text": "OCR labels without structured values",
            }
            report = Report(); validate_chunks(chunks+[figure_chunk], {"GTEST": data}, {}, figures, folder, output, report)
            self.assertIn("figure-structure-not-retrievable", {e["type"] for e in report.errors})
            figure_chunk["text"] = json.dumps({"tables": [table]})
            report = Report(); validate_chunks(chunks+[figure_chunk], {"GTEST": data}, {}, figures, folder, output, report)
            self.assertEqual(report.errors, [])


if __name__ == "__main__":
    unittest.main()
