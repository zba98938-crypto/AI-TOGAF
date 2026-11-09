#!/usr/bin/env python3
"""Derive a per-skill development backlog from the registry's own gaps.

Each skill is scored on facts the repository can prove, not on opinion:

  contract_gaps   work products without counterexample, methods without counterexample,
                  work products without modification example
  type_gaps       entity and relationship types the skill requires but the metamodel
                  does not define
  doc_thickness   bytes of SKILL.md and references/method.md, plus how much of
                  method.md is boilerplate shared verbatim with other skills
  profile_load    profiles owned, and how many still carry source_verified=false

The output is a work order. It does not modify anything and grants no acceptance.
"""
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT.parent
from audit_source_current import DEFAULT_DECISIONS, write_new
BOILERPLATE_MIN_REPEAT = 10


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def method_boilerplate():
    """Paragraphs that appear verbatim in many method.md files are scaffold, not method."""
    paragraphs = Counter()
    per_file = {}
    for path in sorted(SKILLS.glob("togaf-*/references/method.md")):
        blocks = [b.strip() for b in path.read_text().split("\n\n") if len(b.strip()) > 80]
        per_file[path.parent.parent.name] = blocks
        for block in blocks:
            paragraphs[block] += 1
    shared = {block for block, count in paragraphs.items() if count >= BOILERPLATE_MIN_REPEAT}
    return {
        "boilerplate_min_repeat": BOILERPLATE_MIN_REPEAT,
        "boilerplate_paragraphs": len(shared),
        "boilerplate_chars": sum(len(block) for block in shared),
        "per_skill": {
            name: {
                "blocks": len(blocks),
                "unique_blocks": sum(1 for block in blocks if paragraphs[block] == 1),
                "boilerplate_blocks": sum(1 for block in blocks if block in shared),
            }
            for name, blocks in per_file.items()
        },
    }


def accepted_vocabulary():
    """Return core types only; extensions require their own explicit definitions."""
    from contract_vocabulary import core_vocabulary
    return core_vocabulary()


def build():
    capabilities = read(ROOT / "capabilities.json")
    metamodel = read(ROOT / "metamodel.json")
    work_products = capabilities.get("work_products", [])
    methods = capabilities.get("analysis_methods", [])
    profiles = capabilities.get("profiles", [])

    from contract_vocabulary import audit_contracts
    vocabulary_audit = audit_contracts(capabilities)

    skills = sorted({p["owner"] for p in profiles}
                    | {w["owner"] for w in work_products}
                    | {m["owner"] for m in methods})

    boiler = method_boilerplate()

    rows = []
    for skill in skills:
        own_products = [w for w in work_products if w["owner"] == skill]
        own_methods = [m for m in methods if m["owner"] == skill]
        own_profiles = [p for p in profiles if p["owner"] == skill]

        wp_missing_counter = [w["id"] for w in own_products if not w.get("counterexample")]
        wp_missing_modification = [w["id"] for w in own_products if not w.get("modification_example")]
        method_missing_counter = [m["id"] for m in own_methods if not m.get("counterexample")]
        method_missing_calculator = [m["id"] for m in own_methods
                                     if m.get("calculation_policy") and not (m.get("calculator") or m.get('calculator_id'))
                                     and m.get('calculator_status') != 'no-deterministic-calculator']
        profiles_unverified = [p["id"] for p in own_profiles
                               if (p.get("template") or {}).get("source_verified") is False]

        entity_needs = set()
        relationship_needs = set()
        for product in own_products:
            entity_needs |= set(product.get("entity_types") or [])
            relationship_needs |= set(product.get("relationship_types") or [])
            for entity_type in (product.get("required_attributes") or {}):
                entity_needs.add(entity_type)
        for profile in own_profiles:
            entity_needs |= set(profile.get("entity_types") or [])
            relationship_needs |= set(profile.get("relationship_types") or [])

        own_vocabulary = [row for row in vocabulary_audit if row['owner'] == skill]
        entities_missing_metamodel = sorted({name for row in own_vocabulary for name in row['missing_entities']})
        relationships_missing_metamodel = sorted({name for row in own_vocabulary for name in row['missing_relations']})
        invalid_definitions = [dict(problem, contract=row['id']) for row in own_vocabulary for problem in row['invalid_definitions']]

        skill_md = SKILLS / skill / "SKILL.md"
        method_md = SKILLS / skill / "references" / "method.md"
        agents_yaml = SKILLS / skill / "agents" / "openai.yaml"
        package_files = [skill_md, agents_yaml] + [SKILLS/skill/'references'/name for name in
                         ('method.md','contracts.md','checks.md','counterexamples.md','decisions.md','handoff.md')]

        rows.append({
            "skill": skill,
            "files_present": [str(p.relative_to(SKILLS)) for p in
                              package_files if p.is_file()],
            "bytes": {str(p.relative_to(SKILLS/skill)): p.stat().st_size if p.is_file() else 0
                      for p in package_files},
            "method_md_shape": boiler["per_skill"].get(skill, {}),
            "counts": {
                "work_products": len(own_products),
                "profiles": len(own_profiles),
                "methods": len(own_methods),
                "entity_types": len(entity_needs),
                "relationship_types": len(relationship_needs),
            },
            "contract_gaps": {
                "work_products_missing_counterexample": wp_missing_counter,
                "work_products_missing_counterexample_count": len(wp_missing_counter),
                "work_products_missing_modification_example": wp_missing_modification,
                "methods_missing_counterexample": method_missing_counter,
                "methods_missing_counterexample_count": len(method_missing_counter),
                "methods_with_calculation_policy_but_no_calculator": method_missing_calculator,
            },
            "type_gaps": {
                "entities_not_in_project_metamodel": entities_missing_metamodel,
                "entities_not_in_project_metamodel_count": len(entities_missing_metamodel),
                "relationships_not_in_project_metamodel": relationships_missing_metamodel,
                "relationships_not_in_project_metamodel_count": len(relationships_missing_metamodel),
                "invalid_extension_definitions": invalid_definitions,
            },
            "profile_gaps": {
                "profiles_with_source_verified_false": profiles_unverified,
                "profiles_with_source_verified_false_count": len(profiles_unverified),
            },
        })

    missing_wp_ids = {w["id"] for w in work_products if not w.get("counterexample") or not w.get("modification_example")}
    totals = {
        "work_products_with_any_example_gap": len(missing_wp_ids),
        "skills": len(rows),
        "work_products": len(work_products),
        "work_products_missing_counterexample": sum(1 for w in work_products if not w.get("counterexample")),
        "work_products_missing_modification_example": sum(1 for w in work_products if not w.get("modification_example")),
        "methods": len(methods),
        "methods_missing_counterexample": sum(1 for m in methods if not m.get("counterexample")),
        "methods_with_calculator": sum(1 for m in methods if m.get("calculator") or m.get('calculator_id')),
        "methods_explicitly_non_calculating": sum(m.get('calculator_status')=='no-deterministic-calculator' for m in methods),
        "profiles": len(profiles),
        "profiles_with_source_verified_false": sum(
            1 for p in profiles if (p.get("template") or {}).get("source_verified") is False),
        "total_skill_bytes": sum(sum(r["bytes"].values()) for r in rows),
        "boilerplate_paragraphs_in_method_files": boiler["boilerplate_paragraphs"],
    }

    declared_entities = set()
    declared_relationships = set()
    for row in rows:
        declared_entities |= set(row["type_gaps"]["entities_not_in_project_metamodel"])
        declared_relationships |= set(row["type_gaps"]["relationships_not_in_project_metamodel"])
    totals["entity_types_missing_from_metamodel"] = len(declared_entities)
    totals["relationship_types_missing_from_metamodel"] = len(declared_relationships)

    workload = [
        {
            "work_package": "W1 契约补齐：工作产品的反例与修改示例",
            "unit": "work product",
            "count": len(missing_wp_ids),
            "affected_ids": sorted(missing_wp_ids),
            "missing_field_slots": totals["work_products_missing_counterexample"] + totals["work_products_missing_modification_example"],
            "owner_rule": "由 owner 技能负责，共享机制不代写领域反例",
        },
        {
            "work_package": "W2 方法补齐：分析方法的反例与可执行算子",
            "unit": "method",
            "count": totals["methods_missing_counterexample"],
            "owner_rule": "计算型必须给独立谓词；定性型必须给反例评语",
        },
        {
            "work_package": "W3 元模型补齐：规范声明但元模型未定义的类型",
            "unit": "type",
            "count": totals["entity_types_missing_from_metamodel"]
                     + totals["relationship_types_missing_from_metamodel"],
            "owner_rule": "先判定是否项目扩展类型，再决定入元模型或登记为视图局部类型",
        },
        {
            "work_package": "W4 来源核实：source_verified=false 的规范",
            "unit": "profile",
            "count": totals["profiles_with_source_verified_false"],
            "owner_rule": "逐条对照英文原图或正文；无法取得的登记 blocked，不改标记",
        },
        {
            "work_package": "W5 方法文档去模板化：存在共享样板段的技能",
            "unit": "skill",
            "count": sum(bool(r["method_md_shape"].get("boilerplate_blocks")) for r in rows),
            "owner_rule": "每个方法文档至少 4 个专属判断段，不得复制共用段落",
        },
    ]

    from build_routing_matrix import build as build_routes
    from build_artifact_bridge import build as build_bridge
    from audit_source_current import build as build_sources
    routes, bridge, source = build_routes(), build_bridge(), build_sources()
    insufficient_ids = [r["artifact_id"] for r in bridge["records"] if r["relation"] == "insufficient-material"]
    workload.extend([
        {"work_package": "W6 基本制品↔扩展WP定义比较资料不足", "unit": "basic artifact",
         "count": len(insufficient_ids), "affected_ids": insufficient_ids,
         "owner_rule": "补正式定义或明确blocked-definition-source；已有基本制品可合法复用，不为消零增建WP。"},
        {"work_package": "W7 可选择交付章节适用性确认", "unit": "guide", "count": len(routes["zero_rows"]["no_deliverables"]),
         "affected_ids": routes["zero_rows"]["no_deliverables"],
         "owner_rule": "按项目范围确认可选章节或不适用理由；不将所有指南变为mandatory。"},
        {"work_package": "W8 索引来源专业复核（非脚本签署）", "unit": "indexed source item",
         "count": source["counts"]["indexed_items"], "owner_rule": "逐条原文/定义/问题/差异核对；引文子串、读过及路由均非通过。"},
    ])
    return {
        "schema_version": "skill-development-backlog/2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "audit_complete": True,
        "acceptance_granted": False,
        "notice": (
            "A work order derived from registry state. Counts describe missing fields and "
            "undeclared types; they do not score skill quality, and closing one grants nothing."
        ),
        "inputs_sha256": {
            "capabilities.json": sha(ROOT / "capabilities.json"),
            "metamodel.json": sha(ROOT / "metamodel.json"),
            "source_route_decisions": sha(DEFAULT_DECISIONS),
            **{f"togaf*/SKILL.md+method.md ({r['skill']})": "" for r in []},
        },
        "totals": totals,
        "workload": workload,
        "source_route_status": {"source_counts": source["counts"], "routing_unique_counts": routes["totals"],
                                "guide_reference_counts": routes["guide_reference_counts"], "zero_rows": routes["zero_rows"],
                                "bridge_relations": bridge["relation_counts"]},
        "counting_rule": "count是该工作包单位的去重对象数；missing_field_slots单列缺失字段格数，指南引用次数不能算能力数。不同工作包交叉，不可相加。",
        "boilerplate": boiler,
        "skills": rows,
        "limits": [
            "Byte counts measure document size, not method quality.",
            "A work product may legitimately have no modification example; the backlog flags absence, an owner decides applicability.",
            "Types missing from the project metamodel may be intentional view-local types; the decision is recorded, not assumed.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = build()
    out = Path(args.out) if args.out else ROOT / f"reviews/source-current/run-backlog-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}.json"
    write_new(out, result)
    totals = result["totals"]
    print("skills:", totals["skills"], "total bytes:", totals["total_skill_bytes"])
    print("work products missing counterexample:", totals["work_products_missing_counterexample"],
          "/", totals["work_products"])
    print("work products missing modification example:", totals["work_products_missing_modification_example"])
    print("methods missing counterexample:", totals["methods_missing_counterexample"], "/", totals["methods"])
    print("methods with calculator:", totals["methods_with_calculator"])
    print("profiles with source_verified=false:", totals["profiles_with_source_verified_false"])
    print("entity types missing from metamodel:", totals["entity_types_missing_from_metamodel"])
    print("relationship types missing from metamodel:", totals["relationship_types_missing_from_metamodel"])
    print("boilerplate paragraphs in method.md files:", totals["boilerplate_paragraphs_in_method_files"])
    for item in result["workload"]:
        print(f"  {item['work_package']}: {item['count']} {item['unit']}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
