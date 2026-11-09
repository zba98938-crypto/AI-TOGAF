#!/usr/bin/env python3
"""Independently validate architectural records, graph integration and retrieval.

Checks provenance and semantic-field preservation. A source quote match does
not certify the truth or completeness of an authored interpretation.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
import fitz
from PIL import Image
from jsonschema import Draft202012Validator
from validate import Report, markdown_links
from source_paths import resolve as source_path

ROOT = Path(__file__).resolve().parents[3]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm(text):
    text = unicodedata.normalize("NFKC", str(text)).replace("\u00ad", "")
    return re.sub(r"\s+", " ", re.sub(r"[‐‑‒–—−]", "-", text)).strip()


def walk(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


# Explicitly permit removal of duplicated source payload, coordinates and hashes.
# Definitions, labels, responsibilities, edge semantics, hierarchy, evidence IDs,
# cardinality, proficiency and uncertainty are deliberately not in this list.
RETRIEVAL_METADATA = {
    "source_element", "source_relation", "source_flows", "source_tables", "source_legend", "digital_words", "source_material", "source_position",
    "cell_bboxes", "row_values_original", "source_sha256", "source_path", "source_json_path",
    "source_markdown_path", "markdown_path", "context_en", "figure_record_sha256", "pdf_sha256",
    "image_sha256", "source_crop_sha256", "source_pdf_sha256", "maintenance_sha256", "maintenance_source",
}


def semantic_projection(value):
    if isinstance(value, dict):
        return {k: semantic_projection(v) for k, v in value.items()
                if k not in RETRIEVAL_METADATA and not k.startswith("previous_")}
    if isinstance(value, list):
        return [semantic_projection(v) for v in value]
    return value


def validate_relation_history(source_relations,active,rejected,report,figure):
    """Every inherited assertion survives, even when rejected as unobserved."""
    retained=[e for e in active+rejected if e.get("source_relation_index") is not None]
    indices=[e["source_relation_index"] for e in retained]
    valid_indices=all(isinstance(i,int) and not isinstance(i,bool) for i in indices)
    report.check(valid_indices and sorted(indices)==list(range(len(source_relations))),"diagram-source-edge-index-loss-or-duplicate",figure=figure)
    for e in retained:
        idx=e["source_relation_index"]
        report.check(isinstance(idx,int) and 0<=idx<len(source_relations) and e.get("source_relation")==source_relations[idx],"diagram-source-edge-loss",figure=figure,edge=e["id"])
    for e in active:
        if e.get("source_relation_index") is None:
            report.check(e.get("source_relation") is None and e.get("origin")=="newly-transcribed-source-connection" and "current-visual-review" in e.get("evidence_refs",[]),"diagram-additional-edge-origin-missing",figure=figure,edge=e["id"])


def validate_role_required_fields(role, supplemental_spec, report):
    """Keep source omissions explicit without accepting deleted requirements."""
    pid=role["id"]
    for key in ("role_definition", "qualification_notice_zh", "matrix_status", "assessment_status"):
        report.check(bool(role.get(key)), "role-required-analysis-missing", role=pid, field=key)
    for key in ("responsibilities", "requirements"):
        value=role.get(key)
        if isinstance(value,list) and value:
            continue
        declared_absent=(isinstance(value,list) and supplemental_spec is not None
                         and key in supplemental_spec and supplemental_spec[key]==[]
                         and role.get("field_status",{}).get(key)=="not-specified-in-cited-source"
                         and role.get("matrix_status")=="not-specified-for-this-role")
        report.check(declared_absent, "role-required-analysis-missing", role=pid, field=key)
        if declared_absent:
            report.counts["role_fields_explicitly_not_specified_checked"]+=1


class ArchitectureValidator:
    def __init__(self, corpus, root=ROOT):
        self.root, self.corpus = Path(root).resolve(), Path(corpus).resolve()
        self.base = self.corpus/"architecture"
        self.report = Report()
        self.documents = {d["id"]: d for d in read(self.corpus/"index.json")["documents"]}
        self.pdfs = {code: fitz.open(source_path(self.root/d["source"]["path"])) for code, d in self.documents.items()}
        self.hashes, self.page_text, self.quote_seen, self.source_seen = {}, {}, set(), set()
        self.source_documents = {}
        self.semantic_records, self.query_checks = {}, []

    def digest(self, path):
        path = Path(path).resolve()
        if path not in self.hashes:
            self.hashes[path] = sha(path)
        return self.hashes[path]

    def path(self, base, value, owner):
        if not isinstance(value, str) or not value:
            self.report.error("missing-path", owner=owner, path=value); return None
        path = source_path(base/value.split("#", 1)[0])
        if not path.is_relative_to(self.root) or not path.is_file():
            self.report.error("missing-or-outside-project-path", owner=owner, path=value); return None
        return path

    def pdf_text(self, code, page):
        key = code, page
        if key not in self.page_text:
            self.page_text[key] = norm(self.pdfs[code][page-1].get_text(sort=True))
        return self.page_text[key]

    def sources_and_evidence(self, value, owner):
        for obj in walk(value):
            for path_key, hash_key in (("source_path", "source_sha256"), ("pdf_path", "pdf_sha256"),
                                       ("maintenance_source", "maintenance_sha256")):
                if obj.get(path_key) and obj.get(hash_key):
                    key = obj[path_key], obj[hash_key]
                    if key not in self.source_seen:
                        self.source_seen.add(key)
                        path = self.path(self.root, obj[path_key], owner)
                        if path:
                            self.report.check(self.digest(path) == obj[hash_key], "source-hash-mismatch", owner=owner, path=obj[path_key])
                            self.report.counts["source_fingerprints_checked"] += 1
            for path_key, hash_key in (("figure_record_path", "figure_record_sha256"), ("image_path", "image_sha256"),
                                       ("record_path", "record_sha256")):
                if obj.get(path_key) and obj.get(hash_key):
                    path = self.path(self.corpus, obj[path_key], owner)
                    if path:
                        self.report.check(self.digest(path) == obj[hash_key], "artifact-hash-mismatch", owner=owner, path=obj[path_key])
            code, pn = obj.get("document_id"), obj.get("pdf_page")
            if code is not None and pn is not None:
                if not self.report.check(code in self.pdfs and isinstance(pn, int) and 1 <= pn <= len(self.pdfs[code]), "evidence-page-invalid", owner=owner, document=code, page=pn):
                    continue
                quote = obj.get("quote_en")
                key = code, pn, quote
                if quote and key not in self.quote_seen:
                    self.quote_seen.add(key)
                    if obj.get("semantic_status") == "context-evidence-not-a-normalized-role-requirement":
                        # Context indices include Markdown table serialization and
                        # joined source blocks, not literal contiguous PDF quotes.
                        if code not in self.source_documents:
                            self.source_documents[code] = read(self.corpus/"documents"/(code+".json"))
                        record = self.source_documents[code]["pages"][pn-1]
                        rtext = self.pdfs[code][pn-1].get_text(sort=False)
                        self.report.check(record["raw_text"] == rtext, "mention-source-page-changed", owner=owner, document=code, pdf_page=pn)
                        candidates = [norm(item["text"]) for item in record["content"]]
                        self.report.check(norm(quote) in candidates, "context-mention-not-in-extracted-page", owner=owner, document=code, pdf_page=pn)
                        block_ids = {b["id"] for b in record["blocks"]}
                        self.report.check(set(obj.get("block_ids",[])) <= block_ids, "context-mention-block-id-missing", owner=owner, document=code, pdf_page=pn)
                        self.report.counts["extracted_context_mentions_checked"] += 1
                    else:
                        original_order = norm(self.pdfs[code][pn-1].get_text(sort=False))
                        self.report.check(norm(quote) in self.pdf_text(code, pn) or norm(quote) in original_order, "source-quote-not-on-page", owner=owner, document=code, pdf_page=pn, quote=quote)
                        self.report.counts["distinct_source_quotes_checked"] += 1
                if "printed_page_label" in obj:
                    self.report.check(obj["printed_page_label"] == self.pdfs[code][pn-1].get_label(), "printed-page-label", owner=owner, document=code, pdf_page=pn)
            for key in ("source_json_path", "source_markdown_path", "page_markdown", "review_path"):
                if obj.get(key):
                    self.path(self.corpus, obj[key], owner)

    def guides_concepts_relationships(self):
        r = self.report
        self.analysis_index = read(self.base/"index.json")
        self.concepts = read(self.base/"concepts.json")["concepts"]
        relfile = read(self.base/"relationships.json")
        self.relations = relfile["relationships"]
        findings = read(self.base/"evidence.json")["findings"]
        finding_ids = {x["id"] for x in findings}
        r.check(len(finding_ids) == len(findings), "duplicate-finding-id")
        concept_ids = {c["id"] for c in self.concepts}
        relation_ids = {x["id"] for x in self.relations}
        r.check(len(concept_ids) == len(self.concepts), "duplicate-concept-id")
        r.check(len(relation_ids) == len(self.relations), "duplicate-relationship-id")
        r.check({g["id"] for g in self.analysis_index["guides"]} == set(self.documents), "architecture-guide-coverage")
        r.check(read(self.base/"guides/index.json")["guides"] == self.analysis_index["guides"], "guide-indices-disagree")
        for entry in self.analysis_index["guides"]:
            code = entry["id"]; guide = read(self.corpus/entry["json_path"])
            self.path(self.corpus, entry["markdown_path"], code)
            r.check(guide["source"] == self.documents[code]["source"], "guide-source-metadata", document=code)
            for key in ("architecture_question_zh", "application_inputs_zh", "application_outputs_zh", "application_steps_zh", "decision_criteria_zh", "source_findings"):
                r.check(bool(guide.get(key)), "guide-semantic-field-empty", document=code, field=key)
            r.check(set(guide["concept_ids"]) <= concept_ids and set(guide["relationship_ids"]) <= relation_ids, "guide-concept-or-relationship-id", document=code)
            self.semantic_records["guide:"+code] = guide
            r.counts["guides_checked"] += 1
        for c in self.concepts:
            r.check(bool(c.get("definition_zh")) and bool(c.get("evidence")), "concept-definition-or-evidence-missing", concept=c["id"])
            r.check(set(c["evidence_ids"]) <= finding_ids, "concept-finding-missing", concept=c["id"])
            self.semantic_records["concept:"+c["id"]] = c
        for rel in self.relations:
            r.check(rel["source"] in concept_ids and rel["target"] in concept_ids, "concept-relation-endpoint", relationship=rel["id"])
            r.check(rel["type"] in relfile["relation_types"], "relation-type-undefined", relationship=rel["id"])
            r.check(bool(rel.get("evidence")) and set(rel["evidence_ids"]) <= finding_ids, "relation-evidence-missing", relationship=rel["id"])
            r.check("cardinality" in rel and bool(rel.get("direction")) and "is_hr_reporting_line" in rel, "relation-semantics-incomplete", relationship=rel["id"])
            self.semantic_records["relation:"+rel["id"]] = rel
        r.counts.update(concepts_checked=len(self.concepts), concept_relationships_checked=len(self.relations), source_findings_checked=len(findings))

    def role_skills(self):
        r = self.report; index = read(self.base/"roles/index.json"); self.role_index = index
        self.roles = {p["id"]: read(self.base/"roles"/p["json"]) for p in index["profiles"]}
        self.skill_data = read(self.base/"roles/skills.json")
        self.role_relations = read(self.base/"roles/relationships.json")["relationships"]
        # Independently counted from G198 PDF pp16–19 and G249 pp26–29;
        # prevents a consistent omission from skills + every role going green.
        source_columns={
            "G198":["architecture-board-member","architecture-sponsor","enterprise-architecture-manager","technology-architect","data-architect","application-architect","business-architect","program-project-manager","it-designer","solution-architect"],
            "G249":["enterprise-architect","business-domain-architect","data-domain-architect","application-domain-architect","technology-domain-architect","solution-architect"],
        }
        for code in ("G198", "G249"):
            skills = self.skill_data[code]["skills"]
            columns = self.skill_data[code]["role_columns"]
            r.check(len(skills)=={"G198":79,"G249":71}[code],"source-skill-row-coverage",document=code)
            r.check([c["id"] for c in columns]==[code+":role:"+name for name in source_columns[code]],"source-role-column-coverage-and-order",document=code)
            self.report.check(len({s["id"] for s in skills}) == len(skills), "duplicate-skill-id", document=code)
            for skill in skills:
                e = skill["evidence"]; values = skill["values"]
                r.check(len(values) == len(columns) and all(v in (1,2,3,4) for v in values), "skill-column-or-level", skill=skill["id"])
                if code == "G249":
                    page = self.pdfs[code][e["pdf_page"]-1]
                    label=norm(page.get_text("text",clip=fitz.Rect(e["cell_bboxes"][1])))
                    r.check(label==norm(skill["label_en"]),"G249-skill-label-source-mismatch",skill=skill["id"],actual=label)
                    for ci, value in enumerate(values, 2):
                        rect = fitz.Rect(e["cell_bboxes"][ci])
                        actual = re.sub(r"\s+", "", page.get_text("text", clip=rect))
                        r.check(actual == str(value), "G249-skill-value-source-mismatch", skill=skill["id"], column=ci, expected=value, actual=actual)
                        r.counts["digital_skill_cells_rechecked"] += 1
                else:
                    record = read(self.corpus/"figures"/(e["image_record_id"]+".json"))
                    table = next(t for t in record["tables"] if t["id"] == e["table_id"])
                    row = table["rows"][e["row_index_zero_based"]]
                    r.check(skill["label_en"] == row[0] and values == row[1:], "G198-skill-value-source-record-mismatch", skill=skill["id"])
            for ci, col in enumerate(columns):
                profile = self.roles.get(col["id"])
                if not r.check(profile is not None, "matrix-role-profile-missing", role=col["id"]):
                    continue
                expected = {s["id"]: s["values"][ci] for s in skills}
                actual = {s["skill_id"]: s["reference_level"] for s in profile["skills"]}
                r.check(actual == expected and len(actual) == len(profile["skills"]), "role-skill-column-mismatch", role=col["id"])
                scale = {x["level"]: x["name_en"] for x in self.skill_data[code]["scale"]}
                for s in profile["skills"]:
                    r.check(s["level_name_en"] == scale[s["reference_level"]] and s["evidence"]["role_column_index_zero_based"] == col["column_index_zero_based"], "role-skill-scale-or-column", role=col["id"], skill=s["skill_id"])
                r.counts["role_skill_expectations_checked"] += len(actual)
        self.raster_skill_cells()
        matrix_ids = {c["id"] for code in ("G198", "G249") for c in self.skill_data[code]["role_columns"]}
        supplemental_path=self.root/"tools/togaf_corpus/role-additional-profiles.json"
        specs=read(supplemental_path)["profiles"]
        supplemental_specs={s["code"]+":role:"+s["key"]:s for s in specs}
        r.check(len(supplemental_specs)==len(specs),"duplicate-supplemental-role-specification")
        r.check(set(supplemental_specs)<=set(self.roles),"supplemental-role-profile-missing",missing=sorted(set(supplemental_specs)-set(self.roles)))
        for pid, role in self.roles.items():
            if pid not in matrix_ids:
                r.check(role["skills"] == [], "role-without-source-column-has-invented-levels", role=pid)
                r.check(role.get("matrix_status")=="not-specified-for-this-role" and not role.get("proficiency_scale"),"role-without-matrix-overclaim",role=pid)
            validate_role_required_fields(role,supplemental_specs.get(pid),r)
            self.semantic_records[pid] = role
        for rel in self.role_relations:
            r.check(rel["from"] in self.roles and rel["to"] in self.roles, "role-relationship-endpoint", relationship=rel["id"])
            self.semantic_records["role-relation:"+rel["id"]] = rel
        r.counts.update(roles_checked=len(self.roles), matrix_roles_checked=len(matrix_ids), role_relationships_checked=len(self.role_relations))

    def raster_skill_cells(self):
        from collections import Counter
        palette = {(255,243,131):1, (176,203,31):2, (118,144,201):3, (234,85,111):4}
        for path in sorted((self.corpus/"figures/G198").glob("image-*.json")):
            data = read(path)
            for table in data.get("tables", []):
                if not table["id"].startswith("skills-matrix"):
                    continue
                page = self.pdfs["G198"][data["pdf_page"]-1]
                png = page.get_pixmap(matrix=fitz.Matrix(2,2), clip=fitz.Rect(data["bbox_pdf_points"]), alpha=False).tobytes("png")
                self.report.check(hashlib.sha256(png).hexdigest() == self.digest(self.corpus/data["image_path"]), "G198-source-raster-render-mismatch", image=data["id"])
                image = Image.open(io.BytesIO(png)).convert("RGB"); w,h = image.size
                colored = [y for y in range(h) if image.getpixel((int(w*.195), y)) in palette]
                if not self.report.check(bool(colored), "G198-matrix-palette-missing", image=data["id"]):
                    continue
                top,bottom = min(colored),max(colored)+1
                for ri,row in enumerate(table["rows"]):
                    for ci,expected in enumerate(row[1:]):
                        x = w*(.181+(ci+.5)*.819/10); y = top+(bottom-top)*(ri+.5)/len(table["rows"])
                        patch = image.crop((int(x-12),int(y-5),int(x+12),int(y+5)))
                        votes = Counter(palette[p] for p in patch.getdata() if p in palette)
                        actual = votes.most_common(1)[0][0] if votes else None
                        self.report.check(expected == actual, "G198-matrix-cell-source-mismatch", image=data["id"], row=ri, column=ci, expected=expected, actual=actual)
                        self.report.counts["raster_skill_cells_rechecked"] += 1

    def diagrams_graph(self):
        r = self.report; self.diagram_index = read(self.base/"diagrams/index.json")
        self.diagrams = {e["id"]: read(self.corpus/e["json_path"]) for e in self.diagram_index["diagrams"]}
        source_index=read(self.corpus/"figures/index.json")
        source_ids={e["id"] for e in source_index["figures"]}|{e["id"] for e in source_index["embedded_images"] if e.get("json_path")}
        excluded={e["id"] for e in self.diagram_index["excluded_decorative_images"]}
        r.check(source_ids==set(self.diagrams)|excluded and not set(self.diagrams)&excluded,"architecture-image-coverage")
        r.check(self.diagram_index["source_index_sha256"]==self.digest(self.corpus/"figures/index.json"),"diagram-index-source-hash")
        r.check(self.diagram_index["pipeline_sha256"]==self.digest(self.root/"togaf-standard-10th-ai/maintenance/pipeline/architecture_diagrams.py"),"diagram-pipeline-hash")
        r.check(self.diagram_index["review_data_sha256"]==self.digest(self.root/"togaf-standard-10th-ai/maintenance/pipeline/architecture-diagram-reviews.json"),"diagram-review-data-hash")
        reviews=read(self.root/"togaf-standard-10th-ai/maintenance/pipeline/architecture-diagram-reviews.json")["figures"]
        r.check(set(reviews)<=set(self.diagrams),"diagram-review-record-missing",missing=sorted(set(reviews)-set(self.diagrams)))
        diagram_entries={e["id"]:e for e in self.diagram_index["diagrams"]}
        graph = read(self.base/"knowledge-graph.json")
        nodes = {n["id"]:n for n in graph["nodes"]}; edges = {e["id"]:e for e in graph["edges"]}
        rejected={e["id"]:e for e in graph.get("rejected_claims",[])}
        rejected_nodes={n["id"]:n for n in graph.get("rejected_node_claims",[])}
        expected_rejected_nodes=set()
        r.check(len(nodes) == len(graph["nodes"]) and len(edges) == len(graph["edges"]), "knowledge-graph-duplicate-id")
        r.check(len(rejected)==len(graph.get("rejected_claims",[])) and not set(rejected)&set(edges),"knowledge-rejected-claim-duplicate-or-active")
        for e in edges.values():
            r.check(e["from"] in nodes and e["to"] in nodes, "knowledge-graph-endpoint", edge=e["id"])
        expected_nodes = {"concept:"+c["id"] for c in self.concepts} | set(self.roles) | {s["id"] for code in ("G198","G249") for s in self.skill_data[code]["skills"]}
        expected_edges = {"concept:"+x["id"] for x in self.relations} | {"role:"+x["id"] for x in self.role_relations}
        expected_edges |= {pid+"::"+s["skill_id"] for pid,p in self.roles.items() for s in p["skills"]}
        expected_rejected=set()
        for c in self.concepts:
            actual = nodes.get("concept:"+c["id"], {})
            r.check(all(actual.get(k)==v for k,v in c.items() if k!="id"), "knowledge-concept-semantic-loss", concept=c["id"])
        for rel in self.relations:
            actual = edges.get("concept:"+rel["id"], {})
            r.check(all(actual.get(k)==v for k,v in rel.items() if k!="id") and actual.get("from")=="concept:"+rel["source"] and actual.get("to")=="concept:"+rel["target"], "knowledge-concept-relationship-semantic-loss", relationship=rel["id"])
        for pid,profile in self.roles.items():
            actual=nodes.get(pid,{})
            r.check(all(actual.get(k)==v for k,v in profile.items()),"knowledge-role-semantic-loss",role=pid)
        for code in ("G198","G249"):
            for skill in self.skill_data[code]["skills"]:
                actual=nodes.get(skill["id"],{})
                r.check(all(actual.get(k)==([v] if k=="evidence" else v) for k,v in skill.items()),"knowledge-skill-semantic-loss",skill=skill["id"])
        for rel in self.role_relations:
            actual=edges.get("role:"+rel["id"],{})
            r.check(all(actual.get(k)==v for k,v in rel.items() if k!="id"),"knowledge-role-relation-semantic-loss",relationship=rel["id"])
        for fid,d in self.diagrams.items():
            self.semantic_records["diagram:"+fid] = d
            source = read(self.corpus/d["source"]["figure_record_path"])
            review=d.get("current_visual_review")
            r.check(review==reviews.get(fid),"diagram-review-maintenance-record-mismatch",figure=fid)
            if review:
                r.check(review.get("source_pdf_sha256")==d["source"]["pdf_sha256"],"diagram-review-pdf-binding",figure=fid)
                r.check(sorted(review.get("source_crop_sha256",[]))==sorted(im["image_sha256"] for im in d["source"]["images"]),"diagram-review-image-binding",figure=fid)
                r.counts["visual_review_records_bound_to_source"]+=1
                reviewed_pages=review.get("inspected_pdf_pages",[])
                context_pages={e["pdf_page"] for e in d["evidence"] if isinstance(e.get("pdf_page"),int)}
                figure_code=d["document_id"]
                r.check(figure_code in self.pdfs and all(isinstance(p,int) and 1<=p<=len(self.pdfs[figure_code]) for p in reviewed_pages),"diagram-reviewed-source-page-invalid",figure=fid)
                r.check(set(reviewed_pages)<=context_pages,"diagram-reviewed-source-page-context-missing",figure=fid)
                if review.get("review_status")=="source-content-audited":
                    r.check(set(review.get("reviewed_components",[]))>={"visible-labels","connector-topology","grouping","table-content-or-absence","nearby-source-text"},"diagram-content-audit-scope-incomplete",figure=fid)
                    r.counts["content_audited_figures_checked"]+=1
            source_review=source.get("current_visual_review") if "image_kind" in source else None
            r.check(d.get("source_visual_transcription")==source_review,"diagram-source-visual-transcription-loss",figure=fid)
            if source_review:
                r.check(source_review.get("source_pdf_sha256")==d["source"]["pdf_sha256"],"diagram-source-transcription-binding",figure=fid)
                if not review:r.counts["source_transcribed_embedded_images_checked"]+=1
            r.check(d["source_flows"]==source.get("flows",[]),"diagram-source-flow-loss",figure=fid)
            r.check(d["flows"]==(review or {}).get("flows_override",source.get("flows",[])),"diagram-current-flow-mismatch",figure=fid)
            r.check(d["source_tables"]==source.get("tables",[]),"diagram-source-table-loss",figure=fid)
            r.check(d["tables"] == (review or {}).get("tables_override",source.get("tables",[])), "diagram-table-loss", figure=fid)
            r.check(d["source_legend"]==source.get("legend",[]),"diagram-source-legend-loss",figure=fid)
            r.check(d["legend"]==(review or {}).get("legend_override",source.get("legend",[])),"diagram-legend-loss",figure=fid)
            if "image_kind" not in source:
                retained={n['local_id']:n['source_element'] for n in d['nodes']+d.get('rejected_nodes',[]) if n.get('source_element') is not None}
                original={n['id']:n for n in source.get('elements',[])}
                r.check(retained==original and len(retained)==sum(n.get('source_element') is not None for n in d['nodes']+d.get('rejected_nodes',[])),"diagram-source-node-loss",figure=fid)
                for n in d["nodes"]:
                    if n.get("source_element") is None:
                        r.check(n.get("origin")=="newly-transcribed-source-element" and n.get("id") and "current-visual-review" in n.get("evidence_refs",[]),"diagram-additional-node-origin-missing",figure=fid,node=n.get("id"))
                validate_relation_history(source.get("relationships",[]),d["edges"],d.get("rejected_edges",[]),r,fid)
            local_ids = {n["id"] for n in d["nodes"]}
            evidence_ids = {e["id"] for e in d["evidence"]}
            for evidence in d["evidence"]:
                if not evidence.get("quotes"):continue
                code,pn=evidence.get("document_id"),evidence.get("pdf_page")
                if not r.check(code in self.documents and isinstance(pn,int) and 1<=pn<=len(self.pdfs[code]),"diagram-context-page-invalid",figure=fid):continue
                if code not in self.source_documents:
                    self.source_documents[code]=read(self.corpus/"documents"/(code+".json"))
                page=self.source_documents[code]["pages"][pn-1]
                r.check(page["raw_text"]==self.pdfs[code][pn-1].get_text(sort=False),"diagram-context-source-page-changed",figure=fid,page=pn)
                content={(item["text"],tuple(item.get("source_block_ids",[]))) for item in page["content"]}
                for quote in evidence["quotes"]:
                    r.check((quote["text"],tuple(quote.get("source_block_ids",[]))) in content,"diagram-context-quote-not-from-source-content",figure=fid,page=pn)
                    r.counts["diagram_context_quotes_checked"]+=1
            r.check(len(local_ids)==len(d["nodes"]),"diagram-duplicate-node",figure=fid)
            for view in d["hierarchy"]["views"].values():
                for link in view["links"]:
                    r.check(link["parent"] in local_ids and link["child"] in local_ids,"hierarchy-view-endpoint",figure=fid)
            for n in d["nodes"]:
                expected_nodes.add(n["id"])
                gn = nodes.get(n["id"], {})
                r.check(all(gn.get(k) == v for k,v in n.items()), "knowledge-node-semantic-loss", figure=fid, node=n["id"], fields=[k for k,v in n.items() if gn.get(k)!=v])
                r.check(n["depth"]==len(n["ancestors"]) and n["id"] not in n["ancestors"],"diagram-node-hierarchy-depth",figure=fid,node=n["id"])
            for n in d.get('rejected_nodes',[]):
                expected_rejected_nodes.add(n['id']);actual=rejected_nodes.get(n['id'],{})
                r.check(n['id'] not in nodes and all(actual.get(k)==v for k,v in n.items()),'rejected-node-active-or-lost',figure=fid,node=n['id'])
                r.check(n.get('source_presence')=='rejected-not-in-source-figure' and bool(n.get('rejection_reason_zh')),'rejected-node-reason-missing',figure=fid,node=n['id'])
            for e in d["edges"]:
                expected_edges.add(e["id"]); ge = edges.get(e["id"], {})
                r.check(all(ge.get(k) == v for k,v in e.items()), "knowledge-edge-semantic-loss", figure=fid, edge=e["id"], fields=[k for k,v in e.items() if ge.get(k)!=v])
                r.check(e["from"] in local_ids and e["to"] in local_ids, "diagram-local-edge-endpoint", figure=fid, edge=e["id"])
                r.check(e.get("semantic_state")!="rejected-unobserved","rejected-edge-still-active",figure=fid,edge=e["id"])
                for local in e.get("visual",{}).get("crosses_intermediate_region_local_ids",[]):
                    r.check(fid+"#"+local in local_ids,"diagram-crossed-region-endpoint-missing",figure=fid,edge=e["id"],region=local)
            for e in d.get("rejected_edges",[]):
                expected_rejected.add(e["id"]);actual=rejected.get(e["id"],{})
                r.check(e.get("semantic_state")=="rejected-unobserved" and bool(e.get("rejection_reason_zh")),"rejected-edge-reason-or-state-missing",figure=fid,edge=e["id"])
                r.check(e.get("source_relation_index") is not None and e.get("source_relation") is not None,"rejected-edge-source-history-missing",figure=fid,edge=e["id"])
                r.check(all(actual.get(k)==v for k,v in e.items()),"knowledge-rejected-claim-semantic-loss",figure=fid,edge=e["id"])
                r.check(e["id"] not in edges,"knowledge-rejected-claim-is-active",figure=fid,edge=e["id"])
                r.check(set(e.get("evidence_refs",[]))<=evidence_ids,"rejected-edge-evidence-missing",figure=fid,edge=e["id"])
                r.counts["rejected_diagram_claims_checked"]+=1
            for h in d["hierarchy"]["containment_and_grouping"]:
                expected_edges.add(h["id"]); ge = edges.get(h["id"], {})
                r.check(all(ge.get(k) == v for k,v in h.items()) and ge.get("from") == h["parent"] and ge.get("to") == h["child"], "knowledge-hierarchy-semantic-loss", figure=fid, hierarchy=h["id"])
            for item in d["nodes"]+d["edges"]+d["hierarchy"]["containment_and_grouping"]:
                r.check(set(item["evidence_refs"]) <= evidence_ids, "diagram-evidence-id-missing", figure=fid, id=item["id"])
            r.counts["diagram_nodes_checked"] += len(d["nodes"])
            r.counts["diagram_edges_checked"] += len(d["edges"])
            r.counts["diagram_hierarchy_links_checked"] += len(d["hierarchy"]["containment_and_grouping"])
            mpath=self.corpus/diagram_entries[fid]["mermaid_path"]
            for suffix,expected_count in ((".mmd",len(d["edges"])+len(d["hierarchy"]["containment_and_grouping"])),(".relations.mmd",len(d["edges"])),(".hierarchy.mmd",sum(len(v["links"]) for v in d["hierarchy"]["views"].values()))):
                text=mpath.with_suffix(suffix).read_text()
                declarations=re.findall(r"^  (n\d+)\[",text,re.M)
                medges=re.findall(r"^  (n\d+) (?:<-->|-->|---|-\.->|-\.-)\|.*\| (n\d+)$",text,re.M)
                r.check(len(declarations)==len(d["nodes"]) and len(medges)==expected_count,"mermaid-node-or-edge-loss",figure=fid,file=suffix)
                r.check(all(a in declarations and b in declarations for a,b in medges),"mermaid-dangling-node",figure=fid,file=suffix)
                r.counts["mermaid_files_checked"]+=1
        r.check(expected_nodes == set(nodes), "knowledge-node-coverage", missing=sorted(expected_nodes-set(nodes))[:20], extra=sorted(set(nodes)-expected_nodes)[:20])
        r.check(expected_edges == set(edges), "knowledge-edge-coverage", missing=sorted(expected_edges-set(edges))[:20], extra=sorted(set(edges)-expected_edges)[:20])
        r.check(expected_rejected==set(rejected),"knowledge-rejected-claim-coverage",missing=sorted(expected_rejected-set(rejected)),extra=sorted(set(rejected)-expected_rejected))
        r.check(expected_rejected_nodes==set(rejected_nodes),'knowledge-rejected-node-coverage')
        r.check(self.diagram_index["counts"]["reviewed_figures"]==r.counts["visual_review_records_bound_to_source"],"diagram-review-count-mismatch")
        r.check(self.diagram_index["counts"]["content_audited_figures"]==r.counts["content_audited_figures_checked"],"diagram-content-audit-count-mismatch")
        r.check(self.diagram_index["counts"]["source_transcribed_embedded_images"]==r.counts["source_transcribed_embedded_images_checked"],"diagram-source-transcription-count-mismatch")
        for pid,p in self.roles.items():
            for s in p["skills"]:
                edge = edges.get(pid+"::"+s["skill_id"], {})
                r.check(edge.get("required_proficiency") == s["reference_level"] and edge.get("to") == s["skill_id"] and edge.get("from") == pid, "knowledge-role-skill-mismatch", role=pid, skill=s["skill_id"])
                expected={"predicate":"requires_skill","proficiency_scale":p["source_guide"],"evidence":[s["evidence"]],"requirement_kind":s["requirement_kind"],"is_hr_reporting_line":False}
                r.check(all(edge.get(k)==v for k,v in expected.items()),"knowledge-role-skill-semantics-or-evidence-loss",role=pid,skill=s["skill_id"])
        r.counts.update(diagrams_checked=len(self.diagrams), knowledge_nodes_checked=len(nodes), knowledge_edges_checked=len(edges))

    def reading_routes(self):
        index=read(self.corpus/"index.json")
        r=self.report
        r.check(index.get("current_figure_analysis")=="figures/current-analysis.json","current-figure-router-entry-missing")
        path=self.path(self.corpus,index.get("current_figure_analysis"),"current-figure-router")
        if not path:return
        router=read(path);records={e["id"]:e for e in router["records"]}
        r.check(len(records)==len(router["records"])==router["count"],"current-figure-router-count-or-duplicate")
        r.check(set(records)==set(self.diagrams),"current-figure-router-coverage")
        entries={e["id"]:e for e in self.diagram_index["diagrams"]}
        for fid,d in self.diagrams.items():
            entry=records.get(fid,{})
            r.check(entry.get("source_record")==d["source"]["figure_record_path"] and
                    entry.get("json_path")==entries[fid]["json_path"] and
                    entry.get("markdown_path")==entries[fid]["markdown_path"] and
                    entry.get("quality")==d["quality"],"current-figure-route-mismatch",figure=fid)
            for key in ("source_record","json_path","markdown_path"):self.path(self.corpus,entry.get(key),fid)
            source_md=(self.corpus/d["source"]["figure_record_path"]).with_suffix(".md")
            text=source_md.read_text(encoding="utf-8")
            r.check("当前图示解析：" in text and "/"+fid+".md)" in text and "/"+fid+".json)" in text,"source-figure-current-analysis-link-missing",figure=fid)
            r.counts["current_image_routes_checked"]+=1
        for code,document in self.documents.items():
            source=read(self.corpus/document["json"])
            r.check(source.get("current_figure_analysis")=="figures/current-analysis.json","source-json-current-router-missing",document=code)
            text=(self.corpus/document["markdown"]).read_text(encoding="utf-8")
            for page in source["pages"]:
                ids=[fid for fid in page["figure_ids"] if fid in self.diagrams]
                expected_routes=[{"id":fid,"json_path":entries[fid]["json_path"],
                                  "markdown_path":entries[fid]["markdown_path"],
                                  "content_role":"derived-architecture-analysis",
                                  "quality":self.diagrams[fid]["quality"]} for fid in ids]
                r.check(page.get("current_image_analysis")==expected_routes,"source-json-current-image-route-mismatch",document=code,pdf_page=page["pdf_page"])
                r.counts["source_json_page_image_routes_checked"]+=1
                if not ids:continue
                match=re.search(r'<a id="page-'+str(page["pdf_page"])+r'"></a>(.*?)(?=<a id="page-\d+"></a>|\Z)',text,re.S)
                if not r.check(match is not None,"source-page-reading-anchor-missing",document=code,pdf_page=page["pdf_page"]):continue
                for fid in ids:
                    expected=f'[{fid}](../{entries[fid]["markdown_path"]})'
                    r.check(expected in match[1],"source-page-current-diagram-link-missing",document=code,pdf_page=page["pdf_page"],figure=fid)
                    r.counts["source_page_current_image_links_checked"]+=1

    def conversion_coverage(self):
        r=self.report;index=read(self.corpus/"index.json")
        r.check(index.get("conversion_coverage")=="quality/conversion-coverage.json","conversion-inventory-entry-missing")
        path=self.path(self.corpus,index.get("conversion_coverage"),"conversion-inventory")
        if not path:return
        inventory=read(path);source=read(self.corpus/"figures/index.json")
        documents={row["id"]:row for row in inventory["documents"]}
        images={row["id"]:row for row in inventory["images"]}
        r.check(set(documents)==set(self.documents) and len(documents)==len(inventory["documents"]),"conversion-inventory-document-coverage")
        source_images={im["id"]:im for im in source["embedded_images"]}
        source_figures={f["id"]:f for f in source["figures"]}
        r.check(set(images)==set(source_images) and len(images)==len(inventory["images"]),"conversion-inventory-image-coverage")
        tables=0
        for code,entry in self.documents.items():
            row=documents.get(code,{})
            data=read(self.corpus/entry["json"]);tables+=len(data["tables"])
            r.check(row.get("source")==entry["source"] and row.get("pages")==len(self.pdfs[code]) and
                    row.get("table_fragments")==len(data["tables"]),"conversion-inventory-document-mismatch",document=code)
            for key,target in (("json_path",entry["json"]),("markdown_path",entry["markdown"])):
                r.check(row.get(key)==target,"conversion-inventory-document-route-mismatch",document=code,field=key)
                self.path(self.corpus,row.get(key),code)
            r.counts["conversion_inventory_documents_checked"]+=1
        entries={d["id"]:d for d in self.diagram_index["diagrams"]}
        for iid,im in source_images.items():
            row=images.get(iid,{})
            expected_records=[source_figures[fid] for fid in im.get("figure_ids",[])] if im.get("figure_ids") else [im]
            actual_records={rep["id"]:rep for rep in row.get("representations",[])}
            r.check(set(actual_records)=={e["id"] for e in expected_records} and len(actual_records)==len(row.get("representations",[])),"conversion-inventory-image-representation-loss",image=iid)
            r.check(row.get("document_id")==im["document_id"] and row.get("pdf_page")==im["pdf_page"] and
                    row.get("source_pdf_sha256")==im["provenance"]["pdf_sha256"] and
                    row.get("source_bbox_pdf_points")==im["bbox_pdf_points"] and
                    row.get("decoded_image_digest_md5")==im["decoded_image_digest_md5"],"conversion-inventory-image-source-mismatch",image=iid)
            if im.get("figure_ids"):
                expected_evidence=[crop for fid in im["figure_ids"] for crop in entries[fid]["source_images"] if crop["pdf_page"]==im["pdf_page"]]
            else:
                expected_evidence=[{k:im[k] for k in ["image_path","image_sha256","pdf_page","bbox_pdf_points"]}]
            r.check(bool(expected_evidence) and row.get("image_evidence")==expected_evidence,"conversion-inventory-image-evidence-mismatch",image=iid)
            for crop in row.get("image_evidence",[]):
                rendered=self.path(self.corpus,crop.get("image_path"),iid)
                if rendered:r.check(self.digest(rendered)==crop.get("image_sha256"),"conversion-inventory-image-evidence-hash-mismatch",image=iid)
            for original in expected_records:
                rep=actual_records.get(original["id"],{});current=entries.get(original["id"],original)
                for key,target in (("source_json_path",original["json_path"]),("source_markdown_path",original["markdown_path"]),
                                   ("current_json_path",current["json_path"]),("current_markdown_path",current["markdown_path"])):
                    r.check(rep.get(key)==target,"conversion-inventory-image-route-mismatch",image=iid,field=key)
                    self.path(self.corpus,rep.get(key),iid)
            r.counts["conversion_inventory_images_checked"]+=1
        originals={fid for fid,f in source_figures.items() if f["source_role"]!="editorial-added"}
        fully_reviewed={fid for fid in originals if self.diagrams[fid]["quality"]["visual_review"]=="source-content-audited"}
        pending={e["id"]:e for e in inventory["pending_full_visual_review"]}
        r.check(set(pending)==originals-fully_reviewed and len(pending)==len(inventory["pending_full_visual_review"]),"conversion-inventory-remaining-review-mismatch")
        for fid,item in pending.items():
            r.check(item.get("current_review_status")==self.diagrams[fid]["quality"]["visual_review"],"conversion-inventory-review-status-mismatch",figure=fid)
        expected_counts={"documents":len(self.documents),"pages":sum(len(pdf) for pdf in self.pdfs.values()),
                         "table_fragments":tables,"logical_figure_records":len(source_figures),"original_figure_records":len(originals),
                         "editorial_figure_records":len(source_figures)-len(originals),"embedded_image_occurrences":len(source_images),
                         "images_with_md_and_json":len(source_images),"standalone_image_records":sum(not im.get("figure_ids") for im in source_images.values()),
                         "full_visual_reviews":len(fully_reviewed),"original_figures_pending_full_visual_review":len(pending),"missing_artifacts":0}
        r.check(inventory["counts"]==expected_counts and inventory["missing_artifacts"]==[],"conversion-inventory-count-or-missing-artifact-mismatch")
        r.counts["original_figures_pending_full_visual_review"]=len(pending)

    def retrieval(self):
        r = self.report; manifest = read(self.base/"retrieval-manifest.json")
        entries = {e["id"]:e for e in manifest["records"]}
        r.check(set(entries) == set(self.semantic_records), "retrieval-record-coverage", missing=sorted(set(self.semantic_records)-set(entries)), extra=sorted(set(entries)-set(self.semantic_records)))
        chunks = [json.loads(line) for line in (self.corpus/"retrieval/architecture-chunks.jsonl").read_text().splitlines() if line.strip()]
        ids = [c["id"] for c in chunks]; r.check(len(ids) == len(set(ids)), "architecture-chunk-duplicate-id")
        grouped = defaultdict(list)
        for c in chunks:
            owner = c["id"]; grouped[c["parent_record_id"]].append(c)
            path = self.path(self.root,c["source_path"],owner)
            if path:r.check(self.digest(path)==c["source_sha256"], "architecture-chunk-record-hash", chunk=owner)
            self.path(self.corpus,c["json_path"],owner);self.path(self.corpus,c["markdown_path"],owner)
            r.check(c["content_role"] in {"role","relationship","diagram","architecture","concept"}, "architecture-chunk-content-role", chunk=owner)
            locators = c.get("source_locators", [])
            r.check(bool(locators), "architecture-chunk-missing-source-locators", chunk=owner)
            for loc in locators:
                code=loc["document_id"]
                if not r.check(code in self.documents,"chunk-source-document-missing",chunk=owner,document=code):continue
                src=self.documents[code]["source"]
                r.check(all(loc.get(k)==v for k,v in src.items()),"chunk-source-locator-metadata",chunk=owner,document=code)
                pages=loc["pdf_pages"]
                r.check(len(pages)==len(set(pages)) and all(isinstance(p,int) and 1<=p<=len(self.pdfs[code]) for p in pages),"chunk-source-locator-pages",chunk=owner,document=code)
            r.check(set(c.get("document_ids",[]))=={x["document_id"] for x in locators},"chunk-document-ids",chunk=owner)
            r.check(c.get("document_id") in c.get("document_ids",[]),"chunk-primary-document-not-in-locators",chunk=owner)
            expected_pages=locators[0]["pdf_pages"] if len(locators)==1 else []
            r.check(c["pdf_pages"]==expected_pages,"chunk-ambiguous-top-level-pages",chunk=owner)
        for pid,record in self.semantic_records.items():
            parts=grouped.get(pid,[])
            if not r.check(bool(parts),"semantic-record-not-retrievable",record=pid):continue
            r.check([c["part"] for c in parts]==list(range(1,len(parts)+1)) and all(c["part_count"]==len(parts) for c in parts),"architecture-chunk-part-sequence",record=pid)
            r.check(entries[pid]["chunk_count"]==len(parts),"manifest-chunk-count",record=pid)
            content="".join(c["text"] for c in parts)
            try:
                decoded=json.loads(content.split("\n",1)[1])
            except (ValueError,IndexError):
                r.error("reassembled-semantic-record-invalid-json",record=pid);continue
            expected=semantic_projection(record)
            r.check(decoded==expected,"retrieval-semantic-fields-lost-or-altered",record=pid,
                    missing_top_level=sorted(set(expected)-set(decoded)) if isinstance(decoded,dict) else [])
            page_refs=defaultdict(set)
            for e in walk(record):
                if e.get("document_id") and isinstance(e.get("pdf_page"),int):page_refs[e["document_id"]].add(e["pdf_page"])
            if pid.startswith("diagram:"):
                page_refs[record["document_id"]].update(record["source"].get("pdf_pages",[]))
            locs={loc["document_id"]:set(loc["pdf_pages"]) for loc in parts[0]["source_locators"]}
            for code,pages in page_refs.items():r.check(pages<=locs.get(code,set()),"record-evidence-pages-lost-in-locator",record=pid,document=code,missing=sorted(pages-locs.get(code,set())))
        r.check(manifest["counts"]["chunks"]==len(chunks) and manifest["counts"]["records"]==len(self.semantic_records),"retrieval-manifest-counts")
        r.counts.update(semantic_records_retrievable=len(self.semantic_records),architecture_chunks_checked=len(chunks))

    def retrieval_schemas(self):
        """Use the published contract against both actual JSONL layers."""
        schema_path=self.root/"tools/togaf_corpus/schemas/chunk.schema.json"
        schema=read(schema_path)
        Draft202012Validator.check_schema(schema)
        validator=Draft202012Validator(schema)
        filenames=["chunks.jsonl", "architecture-chunks.jsonl"]
        if (self.corpus/'retrieval/chapter-chunks.jsonl').is_file():filenames.append('chapter-chunks.jsonl')
        for filename in filenames:
            path=self.corpus/"retrieval"/filename
            checked=0
            for line_number,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
                if not line.strip():continue
                try:
                    chunk=json.loads(line)
                except ValueError as exc:
                    self.report.error("retrieval-json-invalid",file=filename,line=line_number,detail=str(exc));continue
                for error in validator.iter_errors(chunk):
                    self.report.error("retrieval-schema-invalid",file=filename,line=line_number,
                                      chunk=chunk.get("id") if isinstance(chunk,dict) else None,
                                      field="/".join(map(str,error.absolute_path)),detail=error.message)
                checked+=1
            key={'chunks.jsonl':'source_chunks_schema_checked','architecture-chunks.jsonl':'architecture_chunks_schema_checked','chapter-chunks.jsonl':'chapter_chunks_schema_checked'}[filename]
            self.report.counts[key]=checked
        self.report.counts["retrieval_schemas_checked"]=1

    def chapter_reviews(self):
        from chapter_reviews import validate_review, retrieval_value
        r=self.report;index=read(self.corpus/'chapters/index.json')
        r.check(index['pipeline_sha256']==self.digest(self.root/'togaf-standard-10th-ai/maintenance/pipeline/chapter_reviews.py'),'chapter-pipeline-stale')
        chunks=[json.loads(line) for line in (self.corpus/'retrieval/chapter-chunks.jsonl').read_text().splitlines() if line.strip()]
        grouped=defaultdict(list)
        for chunk in chunks:grouped[chunk['parent_record_id']].append(chunk)
        expected=set()
        for entry in index['documents']:
            if not entry.get('json_path'):continue
            code=entry['document_id'];data=read(self.corpus/entry['json_path'])
            maintenance=self.root/data['maintenance_source'];authored=read(maintenance)
            r.check(data['maintenance_sha256']==self.digest(maintenance),'chapter-maintenance-stale',document=code)
            r.check(all(data.get(k)==v for k,v in authored.items()),'chapter-authored-content-loss',document=code)
            document=read(self.corpus/'documents'/(code+'.json'))
            try:
                checked=validate_review(authored,document,self.root)
                r.check(data['source_unit_coverage']==checked,'chapter-source-coverage-stale',document=code)
            except ValueError as exc:r.error('chapter-source-verification',document=code,detail=str(exc))
            for section in data['sections']:
                sid=section['id'];expected.add(sid);parts=sorted(grouped[sid],key=lambda c:c['part'])
                r.check([p['part'] for p in parts]==list(range(1,len(parts)+1)) and all(p['part_count']==len(parts) for p in parts),'chapter-retrieval-parts',section=sid)
                joined=''.join(p['text'] for p in parts)
                target=section['title_zh']+'\n'+json.dumps(retrieval_value(section,data),ensure_ascii=False,indent=2)
                r.check(joined==target,'chapter-retrieval-semantic-loss',section=sid)
                for part in parts:
                    r.check(part['source_sha256']==self.digest(self.corpus/entry['json_path']) and part['pdf_pages']==section['pdf_pages'],'chapter-retrieval-source-mismatch',section=sid)
            r.counts['chapter_documents_checked']+=1
            r.counts['chapter_sections_checked']+=len(data['sections'])
            r.counts['chapter_source_units_checked']+=entry['reviewed_source_units']
        r.check(expected==set(grouped),'chapter-retrieval-record-coverage')
        r.check(index['counts']['retrieval_chunks']==len(chunks),'chapter-retrieval-count')
        markdown_links(self.corpus/'chapters',self.root,r)

    def real_queries(self):
        cases=[("企业架构师 技能","role","G249"),("首席架构师 职责","role","G249"),
               ("能力实例 实例化","relationship","G233"),("上下级 组织","diagram","G206"),
               ("业务能力 价值流","diagram","G233"),("输入 输出 架构","architecture","G186")]
        for query,role,doc in cases:
            proc=subprocess.run([sys.executable,str(self.root/"tools/togaf_corpus/query.py"),query,"--corpus",str(self.corpus),"--role",role,"--doc",doc,"--limit","3"],capture_output=True,text=True)
            if not self.report.check(proc.returncode==0,"architecture-query-command-failed",query=query,stderr=proc.stderr[:500]):continue
            result=json.loads(proc.stdout);hits=result["results"]
            self.report.check(bool(hits),"architecture-query-no-hit",query=query,role=role)
            for hit in hits:
                self.report.check(hit["content_role"]==role and doc in hit.get("document_ids",[hit.get("document_id")]),"architecture-query-filter-mismatch",query=query,id=hit["id"])
                locs=hit.get("source_locators",[])
                self.report.check(bool(locs) and any(x["document_id"]==doc and x["pdf_pages"] for x in locs),"architecture-query-source-pages-missing",query=query,id=hit["id"])
            expected_record={"企业架构师 技能":"G249:role:enterprise-architect","首席架构师 职责":"G249:role:chief-architect","能力实例 实例化":"relation:R006","输入 输出 架构":"guide:G186"}.get(query)
            if expected_record:
                self.report.check(any(h.get("parent_record_id")==expected_record for h in hits),"architecture-query-expected-record-not-found",query=query,record=expected_record)
            self.query_checks.append({"query":query,"role":role,"document":doc,"returned_ids":[h["id"] for h in hits]})
        self.report.counts["real_cli_queries_checked"]=len(self.query_checks)

    def rendering_reports(self):
        """Reject successful UI checks that belong to older generated files."""
        mermaid_path=self.base/"diagrams/verification/mermaid-validation.json"
        explorer_path=self.base/"explorer-validation.json"
        for path in (mermaid_path,explorer_path):
            if not self.report.check(path.is_file(),"render-verification-report-missing",path=str(path.relative_to(self.corpus))):
                return
        mermaid=read(mermaid_path);explorer=read(explorer_path)
        self.report.check(mermaid.get("architecture_index_sha256")==self.digest(self.base/"diagrams/index.json"),"mermaid-render-report-stale")
        self.report.check(mermaid.get("verifier_sha256")==self.digest(self.corpus/"maintenance/pipeline/verify_architecture_mermaid.mjs"),"mermaid-verifier-changed")
        self.report.check(mermaid.get("parsed")==len(self.diagrams)*3 and not mermaid.get("errors"),"mermaid-parser-verification-incomplete")
        for item in mermaid.get("rendered",[]):
            self.path(self.base/"diagrams",item["svg"],"mermaid:"+item["id"])
            self.path(self.base/"diagrams",item["png"],"mermaid:"+item["id"])
        self.report.check(explorer.get("html_sha256")==self.digest(self.base/"explorer.html"),"explorer-render-report-stale")
        self.report.check(explorer.get("passed") and not explorer.get("errors") and len(explorer.get("checks",[]))>=3,"explorer-verification-incomplete")
        self.report.counts["mermaid_files_browser_parsed"]=mermaid.get("parsed",0)
        self.report.counts["representative_mermaid_graphs_rendered"]=len(mermaid.get("rendered",[]))
        self.report.counts["explorer_browser_checks"]=len(explorer.get("checks",[]))

    def run(self):
        try:
            self.guides_concepts_relationships(); self.role_skills(); self.diagrams_graph(); self.reading_routes(); self.conversion_coverage(); self.retrieval(); self.retrieval_schemas(); self.chapter_reviews()
            for path in sorted(self.base.rglob("*.json")):
                if path.name=="validation.json":continue
                obj=read(path);self.sources_and_evidence(obj,str(path.relative_to(self.corpus)))
                self.report.counts["architecture_json_files_checked"]+=1
            catalog=read(self.base/"catalog.json")
            for name,path in catalog["paths"].items():self.path(self.corpus,path,"catalog:"+name)
            comparisons={"guides":"guides_checked","concepts":"concepts_checked","concept_relationships":"concept_relationships_checked", "roles":"roles_checked","matrix_roles":"matrix_roles_checked","skill_expectations":"role_skill_expectations_checked","diagrams":"diagrams_checked","nodes":"diagram_nodes_checked","relations":"diagram_edges_checked","hierarchy_links":"diagram_hierarchy_links_checked","knowledge_nodes":"knowledge_nodes_checked","knowledge_edges":"knowledge_edges_checked","retrieval_chunks":"architecture_chunks_checked"}
            for ck,rk in comparisons.items():self.report.check(catalog["counts"][ck]==self.report.counts[rk],"catalog-count-mismatch",field=ck,actual=self.report.counts[rk])
            corpus_index=read(self.corpus/"index.json")
            self.report.check(corpus_index.get("architecture")=="architecture/catalog.json" and corpus_index.get("architecture_retrieval")=="retrieval/architecture-chunks.jsonl","corpus-architecture-entry-missing")
            self.report.check(corpus_index.get("architecture_counts")==catalog["counts"],"corpus-architecture-counts-stale")
            self.real_queries(); self.rendering_reports()
            markdown_links(self.base,self.root,self.report,pending_paths=(self.base/"validation.md",self.base/"validation.json"))
            return self.result()
        finally:
            for doc in self.pdfs.values():doc.close()

    def result(self):
        return {"schema_version":"architecture-validation/1","passed":not self.report.errors,
                "validator_sha256":sha(Path(__file__)),"counts":dict(self.report.counts),"errors":self.report.errors,"error_count":len(self.report.errors),
                "query_checks":self.query_checks,"semantic_acceptance":"not-asserted-by-integrity-validation",
                "limits_zh":["原文引用存在与指纹正确不等于全部中文释义经独立专业语义审校。", "图像历史解释与本轮选择性视觉复核保持不同状态；本验证不重新目视确认全部箭头。", "技能数值独立对照数字单元格或原图色阶，不把参考熟练度当作实际人员评分或通用岗位硬性门槛。", "原图、派生结构、完整知识图和检索记录分别检查；实际项目事实仍需项目证据。"]}


def write_report(base,result):
    (base/"validation.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=["# 架构解析验证","", "结果：**"+("通过" if result["passed"] else "存在错误")+"**；结构错误 "+str(result["error_count"])+" 项。", "", "本报告核验来源、数值、结构完整性与检索可达性，不宣称全部中文解释或图关系已通过独立语义审校。", "", "|检查项|数量|","|---|---:|"]
    labels={"guides_checked":"指南架构分析","concepts_checked":"概念","concept_relationships_checked":"概念关系","roles_checked":"角色档案","role_skill_expectations_checked":"角色技能要求","digital_skill_cells_rechecked":"原 PDF 数字技能单元格","raster_skill_cells_rechecked":"原图色阶技能单元格","diagrams_checked":"图示解析","diagram_nodes_checked":"图内节点","diagram_edges_checked":"图内关系","diagram_hierarchy_links_checked":"包含与分组","knowledge_nodes_checked":"知识图节点","knowledge_edges_checked":"知识图关系","semantic_records_retrievable":"可完整检索的语义记录","architecture_chunks_checked":"架构检索块","distinct_source_quotes_checked":"逐页原文短引","extracted_context_mentions_checked":"抽取正文或表格中的去重角色上下文","mermaid_files_checked":"可编辑 Mermaid 图文件","markdown_links_checked":"Markdown 本地链接","real_cli_queries_checked":"实际 CLI 查询"}
    labels.update(source_chunks_schema_checked="原文层检索块数据契约",architecture_chunks_schema_checked="架构层检索块数据契约")
    labels.update(current_image_routes_checked="当前图片解析路由",source_json_page_image_routes_checked="全文JSON逐页图片路由",
                  conversion_inventory_documents_checked="覆盖清单的文档",conversion_inventory_images_checked="覆盖清单的全部图像区域",
                  content_audited_figures_checked="已登记完整可见内容审校的图",source_transcribed_embedded_images_checked="独立图元文字/表格转录")
    lines += [f"|{label}|{result['counts'].get(key,0)}|" for key,label in labels.items()]
    lines += ["","## 查询验证",""]
    for q in result["query_checks"]:lines.append(f"- `{q['query']}` / `{q['role']}` / {q['document']}："+"、".join("`"+i+"`" for i in q["returned_ids"])+"。")
    lines += ["","## 验收边界",""]+["- "+x for x in result["limits_zh"]]
    if result["errors"]:lines += ["","## 错误","","```json",json.dumps(result["errors"],ensure_ascii=False,indent=2),"```"]
    lines += ["","[完整检查数据](validation.json)",""]
    (base/"validation.md").write_text("\n".join(lines),encoding="utf-8")


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--corpus",type=Path,default=ROOT/"togaf-standard-10th-ai");a=p.parse_args()
    result=ArchitectureValidator(a.corpus).run();base=a.corpus/"architecture";write_report(base,result)
    final=Report();markdown_links(base,ROOT,final)
    result["errors"].extend(e for e in final.errors if e not in result["errors"]);result["error_count"]=len(result["errors"]);result["passed"]=not result["errors"];result["counts"].update(final.counts);write_report(base,result)
    print(json.dumps({k:result[k] for k in ("passed","counts","error_count","query_checks")},ensure_ascii=False,indent=2))
    if result["errors"]:print(json.dumps(result["errors"][:15],ensure_ascii=False,indent=2),file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__=="__main__":raise SystemExit(main())
