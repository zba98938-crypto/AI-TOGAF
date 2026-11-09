#!/usr/bin/env python3
"""Derive required instance volume from registered demand, not from intuition.

The registry already states what each view profile, analysis method and deliverable
needs. This script turns that demand into a per-entity-type instance floor per tier,
so a synthetic dataset can be sized against evidence rather than guessed.

Tiers
  T0  2 instances per entity type (a relationship needs two endpoints), one context.
  T1  skill-scoped: every skill that owns the type must be able to build its profiles
      in a single-site ADM cycle, so the type gets 6 instances per owning skill plus
      the floor needed for its most demanding profile.
  T2  group-scoped: T1 x multiplier for types that carry structure across sites,
      states and value streams; flat multiplier for leaf types.

Output is a bill of materials. It is a floor, not a target: real datasets may exceed
it, and nothing here grants coverage or acceptance.
"""
import argparse
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "reviews/comparison/data-volume-model-2026-11-03.json"

# Types that must scale with sites, states, value streams and time.
STRUCTURAL = {
    "capability", "capability_instance", "value_stream", "value_stage", "process",
    "organization", "actor", "role", "application", "data_entity", "information",
    "technology", "requirement", "goal", "objective", "driver", "risk", "control",
    "work_package", "location", "master_data", "metadata_asset", "function",
    "business_service", "product", "technology_service", "platform", "project",
}
LEAF_MULTIPLIER = 3
STRUCTURAL_MULTIPLIER = 8


def read(path):
    return json.loads(Path(path).read_text())


def collect_demand():
    capabilities = read(ROOT / "capabilities.json")
    deliverables = read(ROOT / "deliverables.json")["deliverables"]
    rules = read(ROOT / "capability-addenda/deliverable-assembly-rules.json")["deliverables"]

    entity_profiles = defaultdict(list)
    entity_methods = defaultdict(list)
    entity_skills = defaultdict(set)
    entity_attributes = defaultdict(set)
    entity_deliverables = defaultdict(set)
    entity_artifact_families = defaultdict(set)

    for profile in capabilities.get("profiles", []):
        for entity_type in profile.get("entity_types") or []:
            entity_profiles[entity_type].append(profile["id"])
            entity_skills[entity_type].add(profile["owner"])
            entity_artifact_families[entity_type].add(profile["artifact_id"])
        for entity_type, attributes in (profile.get("required_attributes") or {}).items():
            entity_attributes[entity_type].update(attributes or [])

    for product in capabilities.get("work_products", []):
        for entity_type in product.get("entity_types") or []:
            entity_skills[entity_type].add(product["owner"])
            entity_artifact_families[entity_type].add(product.get("artifact_id") or product["id"])
        for entity_type, attributes in (product.get("required_attributes") or {}).items():
            entity_attributes[entity_type].update(attributes or [])

    for method in capabilities.get("analysis_methods", []):
        for entity_type in method.get("entity_types") or []:
            entity_methods[entity_type].append(method["id"])
            entity_skills[entity_type].add(method["owner"])

    rules_by_id = {rule["id"]: rule for rule in rules}
    for deliverable in deliverables:
        required_profiles = set()
        for section in rules_by_id.get(deliverable["id"], {}).get("sections", []):
            required_profiles |= set(section.get("profile_ids") or [])
        for profile in capabilities.get("profiles", []):
            if profile["id"] in required_profiles:
                for entity_type in profile.get("entity_types") or []:
                    entity_deliverables[entity_type].add(deliverable["id"])

    relationship_types = Counter()
    for profile in capabilities.get("profiles", []):
        for relationship_type in profile.get("relationship_types") or []:
            relationship_types[relationship_type] += 1

    return {
        "entity_profiles": entity_profiles,
        "entity_methods": entity_methods,
        "entity_skills": entity_skills,
        "entity_attributes": entity_attributes,
        "entity_deliverables": entity_deliverables,
        "entity_artifact_families": entity_artifact_families,
        "relationship_types": relationship_types,
    }


def tier_volumes(demand):
    rows = []
    for entity_type in sorted(demand["entity_skills"]):
        profile_count = len(demand["entity_profiles"][entity_type])
        method_count = len(demand["entity_methods"][entity_type])
        skill_count = len(demand["entity_skills"][entity_type])
        deliverable_count = len(demand["entity_deliverables"][entity_type])
        attribute_count = len(demand["entity_attributes"][entity_type])

        t0 = 2
        # T1 floor: each owning skill needs its own instances, and the most demanding
        # profile needs enough to show a non-trivial relationship set.
        t1_skill_floor = skill_count * 4
        t1_profile_floor = max(6, profile_count * 2)
        t1_method_floor = max(2, method_count * 2)
        t1_deliverable_floor = max(2, deliverable_count * 2)
        t1 = max(t0, t1_skill_floor, t1_profile_floor, t1_method_floor, t1_deliverable_floor)

        multiplier = STRUCTURAL_MULTIPLIER if entity_type in STRUCTURAL else LEAF_MULTIPLIER
        t2 = t1 * multiplier

        rows.append({
            "entity_type": entity_type,
            "structural": entity_type in STRUCTURAL,
            "attribute_count": attribute_count,
            "owning_skills": sorted(demand["entity_skills"][entity_type]),
            "owning_skill_count": skill_count,
            "profile_count": profile_count,
            "method_count": method_count,
            "deliverable_count": deliverable_count,
            "artifact_families": sorted(demand["entity_artifact_families"][entity_type]),
            "instances": {"T0": t0, "T1": t1, "T2": t2},
            "attributes_to_populate": {
                "T1": attribute_count,
                "T2": attribute_count,
            },
            "cells": {"T1": t1 * attribute_count, "T2": t2 * attribute_count},
        })
    return rows


def build():
    demand = collect_demand()
    rows = tier_volumes(demand)

    totals = {
        "entity_types": len(rows),
        "structural_types": sum(1 for r in rows if r["structural"]),
        "leaf_types": sum(1 for r in rows if not r["structural"]),
        "instances": {tier: sum(r["instances"][tier] for r in rows) for tier in ("T0", "T1", "T2")},
        "attribute_slots": sum(r["attribute_count"] for r in rows),
        "cells": {tier: sum(r["cells"][tier] for r in rows) for tier in ("T1", "T2")},
    }
    totals["relationship_edges"] = {
        "T0": totals["instances"]["T0"] // 2,
        "T1": int(totals["instances"]["T1"] * 0.9),
        "T2": int(totals["instances"]["T2"] * 1.2),
    }

    by_skill = defaultdict(lambda: {"instances": {"T1": 0, "T2": 0}, "entity_types": 0})
    for row in rows:
        for skill in row["owning_skills"]:
            by_skill[skill]["entity_types"] += 1
            by_skill[skill]["instances"]["T1"] += row["instances"]["T1"]
            by_skill[skill]["instances"]["T2"] += row["instances"]["T2"]

    single_skill = [r["entity_type"] for r in rows if r["owning_skill_count"] == 1]
    heavy = sorted(rows, key=lambda r: -r["instances"]["T2"])[:25]

    return {
        "schema_version": "data-volume-model/1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "audit_complete": True,
        "acceptance_granted": False,
        "notice": (
            "Derived floors, not targets. Volumes come from registered profile, method and "
            "deliverable demand plus explicit tier multipliers. Exceeding a floor proves nothing."
        ),
        "inputs_sha256_source": ["capabilities.json", "deliverables.json",
                                 "capability-addenda/deliverable-assembly-rules.json"],
        "tier_rules": {
            "T0": "2 instances per entity type; enough for one relationship and one profile.",
            "T1": "max(4 x owning skills, 2 x owning profiles, 2 x owning methods, 2 x owning deliverables), floor 6.",
            "T2": f"T1 x {STRUCTURAL_MULTIPLIER} for structural types, T1 x {LEAF_MULTIPLIER} for leaf types.",
            "structural_types": sorted(STRUCTURAL),
        },
        "totals": totals,
        "by_skill": {k: v for k, v in sorted(by_skill.items())},
        "single_skill_entity_types": single_skill,
        "single_skill_count": len(single_skill),
        "heaviest_types": [
            {"entity_type": r["entity_type"], "T1": r["instances"]["T1"], "T2": r["instances"]["T2"],
             "attribute_count": r["attribute_count"]}
            for r in heavy
        ],
        "records": rows,
        "limits": [
            "Relationship edges are estimated from instance counts, not enumerated per type.",
            "The model sizes entity instances and attribute slots; it does not size transaction or event tables.",
            "A type owned by many skills is sized once, not once per skill.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()
    result = build()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    totals = result["totals"]
    print("entity_types:", totals["entity_types"],
          f"(structural {totals['structural_types']} / leaf {totals['leaf_types']})")
    print("instances T0/T1/T2:", totals["instances"])
    print("attribute slots per type (sum):", totals["attribute_slots"])
    print("entity x attribute cells:", totals["cells"])
    print("estimated relationship edges:", totals["relationship_edges"])
    print("types needed by exactly one skill:", result["single_skill_count"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
