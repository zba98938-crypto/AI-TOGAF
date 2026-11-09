#!/usr/bin/env python3
"""Build the 1,910-unit comparison skeleton from the existing source index.

Every unit arrives as `unknown`: the script never invents a requirement, never
guesses a capability target, and never writes `passed`. Each record carries the
seven check slots at `not-run` so that a later reviewer only fills them with
evidence, and the record's `result` stays `not-assessed` until the gate is run.

Units:
  1,337 sections + 330 tables from reviews/source-coverage-unified.json
  243 figures from evidence-registry.json
plus, as separate target-side units, 267 view profiles, 60 analysis methods,
22 deliverables x sections, 70 G248 artifacts, 78 metamodel entities and
48 metamodel relationships.
"""
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "reviews/comparison/comparison-ledger.json"
CHECK_SLOTS = ("definition", "source_available", "opened", "semantics", "execution", "business", "visual")


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def empty_checks(**overrides):
    checks = {slot: {"status": "not-run", "evidence": [], "rationale": None} for slot in CHECK_SLOTS}
    for slot, value in overrides.items():
        if isinstance(value, dict):
            checks[slot].update(value)
        else:
            checks[slot]["status"] = value
    return checks


def source_record(unit_id, unit_type, source_id, guide, requirement_explicit, assets, extra=None):
    record = {
        "comparison_id": unit_id,
        "unit_type": unit_type,
        "source_id": source_id,
        "guide": guide,
        "source_assets": assets,
        "requirement": {"explicit": requirement_explicit, "interpreted": None},
        "capability_targets": [],
        "applicability": None,
        "conflict": None,
        "checks": empty_checks(),
        "result": "not-assessed",
        "reason": "skeleton: requirement, targets, applicability and checks not yet supplied",
        "run_id": None,
        "review": None,
        "extensions": {},
    }
    if extra:
        record["extensions"].update(extra)
    return record


def build(english_root=None):
    coverage = read(ROOT / "reviews/source-coverage-unified.json")
    evidence = read(ROOT / "evidence-registry.json")
    capabilities = read(ROOT / "capabilities.json")
    artifacts = read(ROOT / "artifacts.json")["artifacts"]
    deliverables = read(ROOT / "deliverables.json")["deliverables"]
    rules = read(ROOT / "capability-addenda/deliverable-assembly-rules.json")
    metamodel = read(ROOT / "metamodel.json")

    records = []
    assets_by_figure = {f["id"]: f.get("assets", []) for f in evidence.get("figures", [])}
    conflicts_by_figure = {}
    for conflict in evidence.get("source_conflicts", []):
        conflicts_by_figure.setdefault(conflict.get("figure_id"), []).append(conflict["id"])

    for entry in coverage.get("source_entries", []):
        kind = entry.get("record_type")
        if kind not in ("section", "table"):
            continue
        guide = entry.get("guide")
        source_id = entry.get("source_id")
        assets = [{
            "path": f"reviews/source-coverage-unified.json#{source_id}",
            "sha256": None,
            "availability": "indexed-only",
            "note": "index row; the underlying guide text is not bundled as a hash-pinned asset here",
        }]
        records.append(source_record(
            unit_id=f"cmp-{guide}-{kind}-{source_id.split(':')[-1]}",
            unit_type=kind,
            source_id=source_id,
            guide=guide,
            requirement_explicit=entry.get("summary"),
            assets=assets,
            extra={
                "index_disposition": entry.get("disposition"),
                "index_status": entry.get("status"),
                "capability_refs": entry.get("resolved_capability_refs") or [],
                "bilingual_check": (entry.get("bilingual_check") or {}).get("result"),
                "table_rows": entry.get("rows"),
            },
        ))

    for figure in evidence.get("figures", []):
        figure_id = figure["id"]
        guide = figure.get("guide")
        assets = []
        for asset in assets_by_figure.get(figure_id, []):
            kind = asset.get("kind")
            availability = "available"
            if kind == "en_original":
                availability = "english-only"
            elif kind == "zh_redraw_svg":
                availability = "chinese-only"
            assets.append({
                "path": asset.get("path"),
                "sha256": asset.get("sha256"),
                "availability": availability,
                "kind": kind,
                "note": asset.get("fidelity") or asset.get("historical_fidelity"),
            })
        if not assets:
            assets.append({
                "path": figure.get("json_path"),
                "sha256": figure.get("json_sha256"),
                "availability": "figure-json-only",
                "note": "no image asset registered for this figure",
            })
        conflicts = conflicts_by_figure.get(figure_id)
        records.append(source_record(
            unit_id=f"cmp-{guide}-figure-{figure_id.split('/')[-1]}",
            unit_type="figure",
            source_id=figure_id,
            guide=guide,
            requirement_explicit=figure.get("purpose_summary"),
            assets=assets,
            extra={
                "conflict": conflicts[0] if conflicts else None,
                "index_disposition": figure.get("disposition"),
                "source_status": figure.get("source_status"),
                "semantic_review": figure.get("current_semantic_review"),
                "portable_structure": figure.get("portable_structure"),
                "method_refs": figure.get("method_ids") or [],
                "profile_refs": figure.get("profile_ids") or [],
            },
        ))

    for profile in capabilities.get("profiles", []):
        records.append({
            "comparison_id": f"cmp-profile-{profile['id']}",
            "unit_type": "profile",
            "source_id": profile["id"],
            "guide": None,
            "source_assets": [{
                "path": "capabilities.json",
                "sha256": sha(ROOT / "capabilities.json"),
                "availability": "registry",
                "note": f"profile artifact_id={profile.get('artifact_id')}",
            }],
            "requirement": {"explicit": None, "interpreted": None},
            "capability_targets": [{"category": "view-template", "id": profile["id"]}],
            "applicability": None,
            "conflict": None,
            "checks": empty_checks(visual="not-run"),
            "result": "not-assessed",
            "reason": "skeleton: source_refs recorded, definition and semantics not yet reviewed",
            "run_id": None,
            "review": None,
            "extensions": {
                "source_refs": profile.get("source_refs") or [],
                "definition_status": profile.get("definition_status"),
                "renderer": profile.get("renderer"),
            },
        })

    for method in capabilities.get("analysis_methods", []):
        records.append({
            "comparison_id": f"cmp-method-{method['id']}",
            "unit_type": "method",
            "source_id": method["id"],
            "guide": None,
            "source_assets": [{
                "path": "capabilities.json",
                "sha256": sha(ROOT / "capabilities.json"),
                "availability": "registry",
                "note": "method contract",
            }],
            "requirement": {"explicit": None, "interpreted": None},
            "capability_targets": [{"category": "analysis-method", "id": method["id"]}],
            "applicability": None,
            "conflict": None,
            "checks": empty_checks(),
            "result": "not-assessed",
            "reason": "skeleton: inputs/steps/checks recorded, business judgement not yet supplied",
            "run_id": None,
            "review": None,
            "extensions": {
                "source_refs": method.get("source_refs") or [],
                "required_inputs": method.get("required_inputs") or [],
                "implementation_status": method.get("implementation_status"),
            },
        })

    section_total = 0
    for deliverable in deliverables:
        for index, section in enumerate(deliverable.get("sections", []), 1):
            section_total += 1
            records.append({
                "comparison_id": f"cmp-deliverable-{deliverable['id']}-s{index}",
                "unit_type": "deliverable-section",
                "source_id": f"{deliverable['id']}#{section.get('title')}",
                "guide": None,
                "source_assets": [{
                    "path": "deliverables.json",
                    "sha256": sha(ROOT / "deliverables.json"),
                    "availability": "registry",
                    "note": "deliverable section contract",
                }],
                "requirement": {"explicit": section.get("instruction"), "interpreted": None},
                "capability_targets": [{"category": "deliverable", "id": deliverable["id"]}],
                "applicability": None,
                "conflict": None,
                "checks": empty_checks(),
                "result": "not-assessed",
                "reason": "skeleton: chapter binding and business review not yet supplied",
                "run_id": None,
                "review": None,
                "extensions": {
                    "deliverable_sources": deliverable.get("sources") or [],
                },
            })

    for artifact in artifacts:
        records.append({
            "comparison_id": f"cmp-g248-artifact-{artifact['id']}",
            "unit_type": "artifact",
            "source_id": artifact["id"],
            "guide": "G248",
            "source_assets": [{
                "path": "artifacts.json",
                "sha256": sha(ROOT / "artifacts.json"),
                "availability": "registry",
                "note": json.dumps(artifact.get("source_locator"), ensure_ascii=False),
            }],
            "requirement": {"explicit": artifact.get("question"), "interpreted": None},
            "capability_targets": [{"category": "artifact-family", "id": artifact["id"]}],
            "applicability": None,
            "conflict": None,
            "checks": empty_checks(),
            "result": "not-assessed",
            "reason": "skeleton: G248 appendix name located; definition and field semantics not yet reviewed",
            "run_id": None,
            "review": None,
            "extensions": {
                "definition_status": artifact.get("definition_status"),
                "default_profile_id": artifact.get("default_profile_id"),
            },
        })

    for name, definition in metamodel.get("entity_types", {}).items():
        meaning = definition.get("meaning") if isinstance(definition, dict) else definition
        records.append({
            "comparison_id": f"cmp-metamodel-entity-{name}",
            "unit_type": "metamodel-entity",
            "source_id": name,
            "guide": None,
            "source_assets": [{
                "path": "metamodel.json",
                "sha256": sha(ROOT / "metamodel.json"),
                "availability": "registry",
                "note": "project operational metamodel, not the official TOGAF metamodel",
            }],
            "requirement": {"explicit": meaning, "interpreted": None},
            "capability_targets": [],
            "applicability": None,
            "conflict": None,
            "checks": empty_checks(),
            "result": "not-assessed",
            "reason": "skeleton: entity meaning recorded, source anchoring not yet reviewed",
            "run_id": None,
            "review": None,
        })

    for name, definition in metamodel.get("relationships", {}).items():
        meaning = definition.get("meaning") if isinstance(definition, dict) else definition
        source_types = definition.get("source_types") if isinstance(definition, dict) else None
        target_types = definition.get("target_types") if isinstance(definition, dict) else None
        records.append({
            "comparison_id": f"cmp-metamodel-relation-{name}",
            "unit_type": "metamodel-relationship",
            "source_id": name,
            "guide": None,
            "source_assets": [{
                "path": "metamodel.json",
                "sha256": sha(ROOT / "metamodel.json"),
                "availability": "registry",
                "note": "project operational metamodel relationship",
            }],
            "requirement": {
                "explicit": meaning,
                "interpreted": None,
            },
            "capability_targets": [],
            "applicability": None,
            "conflict": None,
            "checks": empty_checks(),
            "result": "not-assessed",
            "reason": "skeleton: relationship meaning recorded, source anchoring not yet reviewed",
            "run_id": None,
            "review": None,
            "extensions": {
                "source_types": source_types,
                "target_types": target_types,
            },
        })

    by_type = Counter(record["unit_type"] for record in records)
    deliverable_rules = sum(len(d.get("sections", [])) for d in rules.get("deliverables", []))

    return {
        "schema_version": "comparison-ledger/1",
        "record_schema": "reviews/comparison/ledger-schema.json",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "audit_complete": True,
        "acceptance_granted": False,
        "notice": (
            "Skeleton ledger. Every record starts at result=not-assessed with all seven check slots "
            "at not-run. Populating a slot is not passing it; only acceptance_gate.py with matching "
            "runtime fingerprints and a review record can promote a record."
        ),
        "counting_rule": (
            "Source units (sections, tables, figures) are the primary denominator. Target units "
            "(profiles, methods, deliverable sections, G248 artifacts, metamodel entities and "
            "relationships) are listed separately and must not be summed into the source total."
        ),
        "source_unit_total": len([r for r in records if r["unit_type"] in ("section", "table", "figure")]),
        "counts": dict(sorted(by_type.items())),
        "target_side": {
            "profiles": len(capabilities.get("profiles", [])),
            "methods": len(capabilities.get("analysis_methods", [])),
            "deliverables": len(deliverables),
            "deliverable_sections_deliverables_json": section_total,
            "deliverable_sections_assembly_rules": deliverable_rules,
            "g248_artifacts": len(artifacts),
            "metamodel_entities": len(metamodel.get("entity_types", {})),
            "metamodel_relationships": len(metamodel.get("relationships", {})),
        },
        "inputs_sha256": {
            "reviews/source-coverage-unified.json": sha(ROOT / "reviews/source-coverage-unified.json"),
            "evidence-registry.json": sha(ROOT / "evidence-registry.json"),
            "capabilities.json": sha(ROOT / "capabilities.json"),
            "artifacts.json": sha(ROOT / "artifacts.json"),
            "deliverables.json": sha(ROOT / "deliverables.json"),
            "capability-addenda/deliverable-assembly-rules.json": sha(
                ROOT / "capability-addenda/deliverable-assembly-rules.json"),
            "metamodel.json": sha(ROOT / "metamodel.json"),
        },
        "english_root": english_root,
        "records": records,
        "limits": [
            "No requirement text is extracted here; requirement.explicit is copied from the index summary only.",
            "No capability_targets are inferred for source units; a reviewer must state the destination.",
            "result=not-assessed is never equivalent to matched, partial, or not-applicable.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--english-root", default=None,
                        help="informational only; no file is read from this path")
    args = parser.parse_args()
    result = build(args.english_root)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("source_unit_total:", result["source_unit_total"])
    for key, value in result["counts"].items():
        print(f"  {key}: {value}")
    print("target_side:", json.dumps(result["target_side"], ensure_ascii=False))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
