#!/usr/bin/env python3
"""Classify every existing figure-route diagnostic without granting equivalence."""
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = ROOT / "reviews"
PACKAGE = REV / "source-package-2026-11-02-v2"
OUT = REV / "figure-route-dispositions-followup-2026-11-03.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    prior = json.loads((REV / "source-priority-recheck-2026-11-03.json").read_text())
    package = json.loads((PACKAGE / "manifest.json").read_text())
    profiles = {p["id"]: p for p in json.loads((ROOT / "capabilities.json").read_text())["profiles"]}
    figures = {f["figure_id"]: f for f in package["figures"]}
    records = []
    for diagnostic in prior["route_reference_diagnostics"]:
        fid = diagnostic["figure_id"]
        figure = figures[fid]
        crops = []
        for item in figure["english_original_crops"]:
            path = PACKAGE / item["path"]
            assert path.is_file() and sha(path) == item["sha256"]
            crops.append({"path": str(path.relative_to(ROOT)), "sha256": item["sha256"], "pdf_page": item["page"]})
        if fid == "G242/fig3-10":
            status = "identifier-format-diagnostic"
            decision = "Existing annual-environmental-accounting cites Figure3-10 in a different spelling; the route is explicit. Figure/table field and visual acceptance remain pending."
            next_action = "Normalize figure-id comparison in the inventory checker; do not infer source equivalence."
        elif fid == "G152/fig5-1":
            status = "incorrect-structure-route"
            decision = "English Figure 5-1 is a seven-category SABSA attribute taxonomy; business-attribute-profile-default is a selected-attribute measurement form. The form implements §5.10.1 but does not reproduce the taxonomy."
            next_action = "Keep profile form; add or bind an explicit taxonomy view only after all seven branches and attribute labels are checked."
        elif fid == "G234/fig3-1":
            status = "partial-structure-route"
            decision = "English Figure 3-1 contains ten business-function blocks plus six application-function blocks in separate colored containers. The present route points only to metadata-business-function-map, so its application half is not covered."
            next_action = "Bind both business and application function models with one shared figure structure; verify containers, row positions, function signs and labels against page 17."
        elif fid == "G21D/fig1-1":
            status = "reusable-semantics-visual-structure-gap"
            decision = "The existing reference taxonomy has sector/function/service IDs and classifies relations. English Figure 1-1 uses L1/L2/L3 blocks with composition diamonds; the current nested-map example does not demonstrate the same relation notation."
            next_action = "Verify classification versus composition semantics and render this three-level source example before marking structure equivalent."
        elif fid.startswith("G21D/appA-"):
            status = "shared-renderer-reusable-content-unverified"
            decision = "Appendix A shows multiple sector/function/service panels. The generic nested-map renderer can reuse the container pattern, but its current six-node sample and Chinese-derived 232-row catalog do not prove this panel's complete English labels or layout."
            next_action = "Compare every panel node and containment edge to its English crop, then render that panel from checked reference data."
        elif fid.startswith("G21D/"):
            status = "shared-renderer-reusable-content-unverified"
            decision = "This sector figure uses the L1/L2/L3 taxonomy container pattern, which the generic nested-map renderer can reuse. The current sample contains only two selected paths; full sector content and source layout have not been verified."
            next_action = "Transcribe and compare this sector's English function/service identities and containment, then run source-structure and visual review."
        else:
            raise AssertionError(fid)
        records.append({
            "figure_id": fid, "title": diagnostic["title"], "source_pdf_sha256": figure["source_pdf_sha256"],
            "source_crops": crops, "routed_profile_ids": diagnostic["profile_ids"],
            "profile_source_refs": {pid: profiles[pid].get("source_refs", []) for pid in diagnostic["profile_ids"]},
            "diagnostic": diagnostic["diagnostic"], "status": status,
            "reuse_or_gap_decision": decision, "next_action": next_action,
            "source_structure_equivalent": False, "business_layout_accepted": False,
        })
    assert len(records) == 18
    run_id = uuid.uuid4().hex
    result = {
        "schema_version": "figure-route-dispositions/1", "checked_at": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "scope": "18 route-reference diagnostics from project-local English PDF corpus",
        "inputs_sha256": {str(p.relative_to(ROOT)): sha(p) for p in (REV / "source-priority-recheck-2026-11-03.json", PACKAGE / "manifest.json", ROOT / "capabilities.json", Path(__file__))},
        "counts": {"diagnostics": 18, "format_only": 1, "partial_or_wrong_structure": 2, "shared_pattern_content_or_structure_unverified": 15,
                   "source_equivalence_passed": 0},
        "records": records, "accepted": False,
        "limit": "This is per-figure route disposition, not full node/edge/visual acceptance; no source reference was added solely to suppress a diagnostic.",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    (REV / "figure-route-dispositions-followup-2026-11-03-run.json").write_text(json.dumps({
        "run_id": run_id, "command": "python3 skills/_shared/scripts/dispose_figure_routes.py",
        "exit_code": 0, "inputs_sha256": result["inputs_sha256"],
        "output": str(OUT.relative_to(ROOT)), "output_sha256": sha(OUT),
    }, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
