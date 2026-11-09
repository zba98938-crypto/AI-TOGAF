#!/usr/bin/env python3
"""Preserve source-priority evidence without promoting historical notes to acceptance."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import uuid

ROOT = Path(__file__).resolve().parents[1]
REV = ROOT / "reviews"
PACKAGE = REV / "source-package-2026-11-02-v2"
OUT = REV / "source-priority-recheck-2026-11-03.json"

def read(path): return json.loads(path.read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    source = read(REV / "source-coverage-unified.json")
    inventory = read(REV / "actual-source-skill-comparison-2026-11-03.json")
    package = read(PACKAGE / "manifest.json")
    guides = {g["guide_id"]: g for g in package["guides"]}
    figures = {f["figure_id"]: f for f in package["figures"]}
    reviewed = {
        "G212:L523": "English PDF p41 §5.2 says the questionnaire is in Appendix A; the Chinese L527 adds an across-factor scoring/management-attention rule. This rule is not stated on p41. Treat it as translator/project interpretation until independently sourced.",
        "G212:L698": "English PDF p49 Appendix A.1 states the Likert terms have distinct meaning and explains neutral; Chinese L700 matches this sentence. Figure A-1 was opened: seven ordered categories and six colored layers are visible, but no 1–7 numbers or management-attention threshold.",
        "G212:T729": "English PDF p49 has Figure A-1 and no Table A-1. Figure A-1 was opened: seven ordered categories and six layers are visible, but no 1–7 numeric labels or 1–5 management-attention threshold. Chinese Table A-1 at L729 adds numeric anchors; do not treat them as directly printed source rules.",
        "G233:L300": "English PDF p25 §4.3.3 uses 'objectives and measurable goals' and says goals are realized by an objective. Chinese L302–304 reverses the words under its local 目标/目的 convention. Preserve both terms and do not transfer an unreviewed direction into a skill relationship.",
        "G242:L1016": "English PDF p61 §3.6.1 requires a yearly environmental assessment and management over two to three years. Chinese body L1018 conveys yearly assessment; the local Figure 3-10 label table L1038 says one yearly measure every 2–3 years, which changes frequency.",
        "G242:T1036": "Chinese Figure 3-10 label table L1038 reads '每 2–3 年一次年度度量'. English PDF p61 says yearly assessment managed over two to three years. The label interpretation is incorrect and cannot supply a period rule.",
    }
    deviations = []
    for entry in source["source_entries"]:
        check = entry.get("bilingual_check") or {}
        if check.get("result") != "deviation": continue
        guide = guides[entry["guide"]]
        chinese = PACKAGE / guide["chinese_text"]["path"]
        number = int(re.search(r":(?:L|T)(\d+)", entry["source_id"]).group(1))
        lines = chinese.read_text().splitlines()
        lo, hi = max(1, number-2), min(len(lines), number+3)
        english = []
        for page in check.get("en_pages", []):
            page_record = next((p for p in guide["english_page_text"] if p["page"] == page), None)
            if page_record:
                path = PACKAGE / page_record["path"]
                english.append({"page": page, "path": str(path.relative_to(ROOT)), "sha256": sha(path)})
        deviations.append({
            "source_id": entry["source_id"], "record_type": entry["record_type"],
            "capability_ids": entry.get("resolved_capability_refs", []),
            "historical_note": check.get("note"),
            "historical_status": "deviation; not automatically accepted",
            "chinese_asset": {"path": str(chinese.relative_to(ROOT)), "sha256": sha(chinese),
                "locator": f"L{number}",
                "excerpt": [f"L{i}: {lines[i-1]}" for i in range(lo, hi+1)]},
            "english_assets": english,
            "actual_opened_figure": ({"path": "reviews/source-package-2026-11-02-v2/original-crops/G212-figA-1-p49-0.png",
                "sha256": sha(PACKAGE / "original-crops/G212-figA-1-p49-0.png"),
                "observed": "Seven ordered categories and six layer rows; no numeric scoring labels or management threshold."}
                if entry["source_id"] in ("G212:L698", "G212:T729") else None),
            "current_semantic_observation": reviewed.get(entry["source_id"]),
            "current_semantic_status": "bounded-English-Chinese-comparison-recorded" if entry["source_id"] in reviewed else "historical-deviation-located-current-semantic-review-pending",
            "accepted": False,
        })
    route_problems = []
    for item in inventory["figures"]:
        if not item["route_problems"]: continue
        figure = figures[item["figure_id"]]
        route_problems.append({
            "figure_id": item["figure_id"], "title": figure["title"],
            "profile_ids": item["profile_ids"], "diagnostic": item["route_problems"],
            "source_json": figure["original_json"],
            "status": "needs-figure-specific-semantic-route-review",
            "note": "G21D shares a generic tailoring profile; Figure3-10 is named in a different spelling; neither is a proven missing capability or an accepted exact route.",
            "accepted": False,
        })
    unrouted = []
    for item in inventory["figures"]:
        if item["profile_ids"] or item["method_ids"]: continue
        figure = figures[item["figure_id"]]
        crops = [{"path": crop["path"], "sha256": crop["sha256"]}
                 for crop in figure["english_original_crops"]]
        unrouted.append({
            "figure_id": item["figure_id"], "title": figure["title"],
            "disposition": figure["source_route"]["disposition"],
            "reason": figure["source_route"]["disposition_reason"],
            "english_crop_assets": crops,
            "contact_sheet_opened": "reviews/source-repairs/no-route-english-contact-sheet.png",
            "status": "actual-English-crop-contact-sheet-triage; no-direct-skill-route-candidate",
            "capability_match": "not-individually-confirmed",
            "accepted": False,
        })
    result = {
        "schema_version": "source-priority-recheck/1", "run_id": uuid.uuid4().hex,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "inputs_sha256": {str(path.relative_to(ROOT)): sha(path) for path in
            (REV / "source-coverage-unified.json", REV / "actual-source-skill-comparison-2026-11-03.json",
             PACKAGE / "manifest.json", Path(__file__))},
        "counts": {"deviations": len(deviations), "current_bounded_semantic_observations": len(reviewed),
            "route_reference_diagnostics": len(route_problems), "no_direct_route_figures": len(unrouted)},
        "deviations": deviations, "route_reference_diagnostics": route_problems,
        "no_direct_route_figures": unrouted,
        "g211_repair": {
            "original_untouched": "reviews/source-package-2026-11-02-v2/original-assets/figs/g211_fig3-2.svg",
            "syntax_repair": {"svg": "reviews/source-repairs/G211-fig3-2-syntax-repair.svg",
                "png": "reviews/source-repairs/G211-fig3-2-syntax-repair.png"},
            "proposed_structural_transcription": {"svg": "reviews/source-repairs/G211-fig3-2-proposed-structure.svg",
                "png": "reviews/source-repairs/G211-fig3-2-proposed-structure.png"},
            "actual_opened": ["reviews/source-package-2026-11-02-v2/original-crops/G211-fig3-2-p20-0.png",
                "reviews/source-repairs/G211-fig3-2-syntax-repair.png",
                "reviews/source-repairs/G211-fig3-2-proposed-structure.png",
                "examples/full-capability/reference/artifacts/profile-capability-classification.png"],
            "result": "English original has 18 slots; syntax-repaired historical Chinese image has 15; new transcription has 18 visible slots, but translation and skill mapping await independent review.",
            "sha256": {str(path.relative_to(ROOT)): sha(path) for path in
                (REV / "source-repairs").glob("G211-fig3-2-*") if path.is_file()},
            "accepted": False,
        },
        "g186_fig6_1": {
            "original_json_kind": "zh_only", "english_pdf_page": 81,
            "english_page_status": "6.4 conclusion text followed by endnotes; no corresponding figure",
            "conclusion": "Chinese editorial figure, not an English source illustration; do not invent an original crop",
            "accepted": False,
        },
        "accepted": False,
        "limits": ["A historical deviation is a lead, not a current semantic pass.",
                   "The 11-figure contact sheet is actual visual triage but not a full source-equivalence review.",
                   "Route diagnostics check explicit identifiers, not whether a shared profile is semantically sufficient."]}
    assert len(deviations) == 26 and len(route_problems) == 18 and len(unrouted) == 11
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["counts"], ensure_ascii=False))

if __name__ == "__main__": main()
