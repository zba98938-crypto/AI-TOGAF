#!/usr/bin/env python3
"""Verify the six completion conditions for every skill package.

Exit code 0 means the in-scope package checks ran and passed. Dataset scale and
method execution are separate commands, never inferred from package contents.
`acceptance_granted` stays false by construction.

Conditions:
  1 files     eight files present, with byte floors on the five reference docs
  2 machine   positive/negative fixtures execute every actual WP machine check_spec
    legacy    historical prose counterexamples remain pending professional review
  3 calc      every calculation-policy method has a calculator or an explicit no-calculator status
  4 vocab     no entity or relationship type is missing from the accepted vocabulary
  5 data      run verify_scale_cases.py separately; not a package-content check
  6 negative  one constructed wrong model per skill is rejected by validate.py
"""
import argparse
import json
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT.parent
sys.path.insert(0, str(ROOT / "scripts"))
from field_contracts import apply_contract_overlay, validate_contracts, EXECUTORS
from field_counterexamples import run_explicit_counterexamples

FILE_FLOORS = {
    # A floor only catches empty or truncated files. Real quality is checked by
    # content completeness below: every owned work product, every required field
    # and every assertion code must actually appear. Byte floors alone invite
    # padding, so they are deliberately low.
    "SKILL.md": 2000,
    "references/method.md": 800,
    "references/contracts.md": 1000,
    "references/checks.md": 800,
    "references/counterexamples.md": 800,
    "references/decisions.md": 2000,
    "references/handoff.md": 800,
    "agents/openai.yaml": 250,
}


def read(path):
    return json.loads(Path(path).read_text())


def known_codes():
    """Collect every assertion code the validators can emit."""
    codes = set()
    for script in ("validate.py", "profile_render.py", "view_semantics.py",
                   "table_expression.py", "deliverable_assembly.py"):
        path = ROOT / "scripts" / script
        if not path.is_file():
            continue
        text = path.read_text()
        for token in ("issue('error','", "issue('warning','", '"code":"'):
            start = 0
            while True:
                index = text.find(token, start)
                if index < 0:
                    break
                begin = index + len(token)
                end = text.find("'", begin)
                alt = text.find('"', begin)
                if end < 0 or (0 <= alt < end):
                    end = alt
                if end > begin:
                    codes.add(text[begin:end])
                start = begin
    codes |= {"invalid-cardinality", "missing-evidence", "transition-operability-gap",
              "cycle", "measurement-evidence-gap", "dangling-reference", "duplicate-id",
              "undefined-entity-type", "undefined-relation"}
    return codes


def check_content(skill, caps):
    """Content completeness: every owned item and field must actually appear.

    This replaces byte-count proxies. A contracts.md that omits one work product's
    fields is incomplete no matter how long it is.
    """
    base = SKILLS / skill / "references"
    products = [w for w in caps["work_products"] if w["owner"] == skill]
    methods = [m for m in caps["analysis_methods"] if m["owner"] == skill]

    def text(name):
        path = base / name
        return path.read_text() if path.is_file() else ""

    contracts = text("contracts.md")
    checks = text("checks.md")
    counter = text("counterexamples.md")
    decisions = text("decisions.md")
    handoff = text("handoff.md")

    missing = []
    contract_problems = validate_contracts({'work_products': products, 'analysis_methods': methods})
    missing.extend(contract_problems)
    from build_skill_packages import render_contracts, render_checks
    if not contract_problems:
        if contracts != render_contracts(skill, products, caps):
            missing.append('contracts.md与显式类型字段契约不一致，须重新生成')
        if checks != render_checks(skill, products, methods):
            missing.append('checks.md与check_specs不一致，禁止关键词映射或假自动通过')
    for wp in products:
        if wp["id"] not in contracts:
            missing.append(f"contracts.md 缺工作产品 {wp['id']}")
        for entity_fields in (wp.get("required_attributes") or {}).values():
            for field in entity_fields:
                if f"`{field}`" not in contracts:
                    missing.append(f"contracts.md 缺字段 {wp['id']}.{field}")
        ce = wp.get("counterexample") or {}
        if wp["id"] not in counter:
            missing.append(f"counterexamples.md 缺工作产品 {wp['id']}")
        if ce.get("expected") and f"`{ce['expected']}`" not in counter:
            missing.append(f"counterexamples.md 缺断言码 {wp['id']}->{ce['expected']}")
    for method in methods:
        ce = method.get("counterexample") or {}
        if method["id"] not in counter:
            missing.append(f"counterexamples.md 缺方法 {method['id']}")
        if ce.get("expected") and f"`{ce['expected']}`" not in counter:
            missing.append(f"counterexamples.md 缺断言码 {method['id']}->{ce['expected']}")

    # decisions.md must carry at least five real judgements, each with all three parts.
    judgement_count = decisions.count("\n## 判断 ")
    todo_count = decisions.count("TODO")
    if judgement_count < 5:
        missing.append(f"decisions.md 只有 {judgement_count} 条判断，需 ≥5")
    if todo_count:
        missing.append(f"decisions.md 仍含 {todo_count} 个 TODO")
    for part in ("判据：", "反例：", "影响："):
        if decisions.count(part) < judgement_count:
            missing.append(f"decisions.md 缺少「{part}」（{decisions.count(part)}/{judgement_count}）")

    if "入向" not in handoff or "出向" not in handoff:
        missing.append("handoff.md 缺入向/出向之一")
    if products and "本技能产出的工作产品" not in handoff:
        missing.append("handoff.md 未列出本技能产出的工作产品")

    return {"status": "pass" if not missing else "fail",
            "work_products": len(products), "methods": len(methods),
            "judgements": judgement_count, "problems": missing[:25],
            "problem_count": len(missing)}


def check_files(skill):
    missing, undersized = [], []
    for relative, floor in FILE_FLOORS.items():
        path = SKILLS / skill / relative
        if not path.is_file():
            missing.append(relative)
            continue
        size = path.stat().st_size
        if size < floor:
            undersized.append((relative, size, floor))
    return {"status": "pass" if not missing and not undersized else "fail",
            "missing": missing, "undersized": undersized}


def check_codes(caps, codes, declared=None):
    """Inventory legacy prose without misclassifying review as engineering failure.

    Compatibility function name only: this does not execute these examples or
    grant machine coverage even if their historical code string is recognised.
    """
    declared = declared or {}
    enforced = {entry[0] for entry in EXECUTORS.values()}
    bad, absent, not_enforced = [], [], []
    records = [(wp["id"], (wp.get("counterexample") or {})) for wp in caps["work_products"]]
    records += [(m["id"], (m.get("counterexample") or {})) for m in caps["analysis_methods"]]
    for identity, ce in records:
        if not ce:
            absent.append(identity)
            continue
        code = ce.get("expected")
        # Historical narrative examples have no structured input adapter or
        # executable spec binding. A known string is not execution evidence.
        not_enforced.append((identity, code))
        if code not in codes and code not in enforced and code not in declared:
            bad.append((identity, code))
    return {"status": "pending-professional-review" if records else "not-applicable",
            "unknown_codes": bad,
            "without_counterexample": absent,
            "not_machine_enforced": not_enforced,
            "not_machine_enforced_count": len(not_enforced),
            "machine_coverage_claimed": False,
            "notice": "历史叙述反例全部待人工复核；码名存在不证明该反例被执行器拒绝。check_specs的真实执行与此分开。",
            "enforced_codes_found": len(enforced)}


def check_calculators(caps):
    problems = []
    for method in caps["analysis_methods"]:
        if not method.get("calculation_policy"):
            continue
        if method.get("calculator") or method.get("calculator_id"):
            continue
        if method.get("calculator_status") == "no-deterministic-calculator":
            if not method.get('professional_review') and not method.get('execution_mode'):
                problems.append(method['id'] + ': 无专业检查路径')
            continue
        problems.append(method["id"])
    return {"status": "pass" if not problems else "fail", "unresolved": problems}


def check_vocabulary(caps=None):
    from contract_vocabulary import audit_contracts
    caps = apply_contract_overlay(read(ROOT / "capabilities.json")) if caps is None else caps
    audited = audit_contracts(caps)
    missing_entities = sorted({name for row in audited for name in row['missing_entities']})
    missing_relations = sorted({name for row in audited for name in row['missing_relations']})
    problems = [row for row in audited if row['missing_entities'] or row['missing_relations'] or row['invalid_definitions']]
    return {"status": "pass" if not problems else "fail",
            "missing_entities": missing_entities[:20],
            "missing_entities_count": len(missing_entities),
            "missing_relations": missing_relations[:20],
            "missing_relations_count": len(missing_relations),
            "contract_problems": problems,
            "extension_policy": "Registered core types and explicit scoped definitions are checked separately; models must embed the extensions they use."}


def check_negative(caps, skill):
    """Construct one deliberately wrong model from this skill's first work product."""
    products = [w for w in caps["work_products"] if w["owner"] == skill]
    if not products:
        return {"status": "not-applicable", "reason": "no work product owned"}
    wp = products[0]
    example = wp.get("example")
    if not example:
        return {"status": "not-applicable", "reason": "no example to mutate"}

    model = {
        "schema_version": "2.0",
        "project": {"id": "negative-probe", "name": "反例探针", "version": "1",
                    "type": "probe", "is_example": True,
                    "context": {"domains": ["business"], "landscape": "capability",
                                "purpose": "project", "abstraction": "logical",
                                "evolution": "baseline"},
                    "approval_status": "candidate", "implementation_status": "not-started"},
        "sources": [{"id": "probe", "kind": "example", "description": "反例探针，非企业事实"}],
        "entities": [], "relationships": [], "views": [], "deliverables": [], "gaps": [],
    }
    for entity in example.get("entities", []):
        model["entities"].append({
            "id": entity["id"], "name": entity["name"], "type": entity["type"],
            "attributes": dict(entity.get("attributes") or {}),
            "evidence": ["probe"], "certainty": "assumed"})
    for relation in example.get("relationships", []):
        model["relationships"].append({
            "id": relation["id"], "type": relation["type"],
            "source": relation["source"], "target": relation["target"],
            "label": relation.get("label") or relation["id"],
            "attributes": dict(relation.get("attributes") or {}),
            "evidence": ["probe"], "certainty": "assumed"})
    # Mutation: point a relationship at a non-existent endpoint.
    mutated = False
    if model["relationships"]:
        model["relationships"][0]["target"] = "definitely-not-an-entity"
        mutated = True
    elif model["entities"]:
        model["entities"][0]["type"] = "undefined-probe-type"
        mutated = True
    if not mutated:
        return {"status": "not-applicable", "reason": "example has no entity or relationship to mutate"}

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "model.json"
        path.write_text(json.dumps(model, ensure_ascii=False))
        proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py"), str(path)],
                              capture_output=True, text=True)
    output = (proc.stdout or "") + (proc.stderr or "")
    rejected = proc.returncode != 0 or "dangling-reference" in output or "undefined" in output
    return {"status": "pass" if rejected else "fail",
            "work_product": wp["id"],
            "rejected": rejected,
            "exit_code": proc.returncode,
            "signal": "dangling-reference" if "dangling-reference" in output else output[:200]}


def check_duplication():
    """Real duplication means a method file repeats another method file's content.

    The single shared pointer line to method-common.md is intentional and excluded;
    so is the title line. What must not repeat is substantive guidance.
    """
    counts = Counter()
    files = sorted(SKILLS.glob("togaf-*/references/method.md"))
    for path in files:
        for block in path.read_text().split("\n\n"):
            block = block.strip()
            if len(block) < 80:
                continue
            if "method-common.md" in block:
                continue
            counts[block] += 1
    duplicates = [(block[:60], count) for block, count in counts.items() if count >= 2]
    return {"status": "pass" if not duplicates else "fail",
            "files": len(files),
            "duplicate_paragraphs": len(duplicates),
            "samples": duplicates[:3]}


def check_links():
    from package_links import broken_markdown_links
    # The release seal omits only the top-level runtime output directory.
    # Nested corpus/maintenance/work contains shipped source evidence.
    broken = broken_markdown_links(SKILLS, excluded_top_level={'work'})
    return {"status": "pass" if not broken else "fail", "broken": broken[:20],
            "broken_count": len(broken)}


def enforced_codes():
    """Codes emitted by an actual implementation, discovered from the source.

    Derived rather than declared so the verifier cannot be fooled by a registry that
    merely claims a code is enforced.
    """
    path = ROOT / "scripts/contract_semantics.py"
    if not path.is_file():
        return set()
    import re
    return set(re.findall(r'issue\(\s*"([a-z][a-z0-9-]+)"', path.read_text()))


def declared_codes():
    """Domain assertion codes registered by addenda but not yet emitted by validators."""
    path = ROOT / "capability-addenda/skill-contract-counterexamples.json"
    if not path.is_file():
        return {}
    return read(path).get("declared_assertion_codes") or {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(ROOT / "reviews/comparison/skill-package-verification.json"))
    parser.add_argument("--skip-negative", action="store_true")
    args = parser.parse_args()

    caps = apply_contract_overlay(read(ROOT / "capabilities.json"))
    codes = known_codes()
    skills = sorted({p["owner"] for p in caps["profiles"]}
                    | {w["owner"] for w in caps["work_products"]}
                    | {m["owner"] for m in caps["analysis_methods"]})

    results = {"files": {}, "content": {}, "negative": {}}
    for skill in skills:
        results["files"][skill] = check_files(skill)
        results["content"][skill] = check_content(skill, caps)
        if not args.skip_negative:
            results["negative"][skill] = check_negative(caps, skill)

    shared = {
        "field_contracts": {"status": "fail" if validate_contracts(caps) else "pass",
                            "problems": validate_contracts(caps)},
        "machine_counterexamples": run_explicit_counterexamples(caps),
        "legacy_narrative_review": check_codes(caps, codes, declared_codes()),
        "calculators": check_calculators(caps),
        "vocabulary": check_vocabulary(),
        "duplication": check_duplication(),
        "links": check_links(),
    }

    files_pass = sum(1 for r in results["files"].values() if r["status"] == "pass")
    content_pass = sum(1 for r in results["content"].values() if r["status"] == "pass")
    negative_pass = sum(1 for r in results["negative"].values() if r["status"] == "pass")
    conditions = {
        "1 files": f"{files_pass}/{len(skills)}",
        "1b content": f"{content_pass}/{len(skills)}",
        "2 machine-counterexamples": shared["machine_counterexamples"]["status"],
        "2b field-contracts": shared['field_contracts']['status'],
        "3 calculators": shared["calculators"]["status"],
        "4 vocabulary": shared["vocabulary"]["status"],
        "6 negative": "not-applicable" if args.skip_negative else f"{negative_pass}/{len(skills)}",
        "7 links": shared['links']['status'],
        "8 duplication": shared['duplication']['status'],
    }

    def ok(value):
        if value.startswith("deferred"):
            return True
        if "/" in value:
            left, right = value.split("/")
            return left == right
        return value in ("pass", "not-applicable")

    report = {
        "schema_version": "skill-package-verification/1",
        "audit_complete": True,
        "acceptance_granted": False,
        "conditions": conditions,
        "all_applicable_pass": all(ok(v) for v in conditions.values()),
        "engineering_scope": "Registered machine specs only; no method-calculator execution or narrative/professional acceptance claimed.",
        "pending_professional_reviews": {
            "legacy_narrative_review": shared['legacy_narrative_review']['status'],
            "legacy_narrative_count": shared['legacy_narrative_review']['not_machine_enforced_count'],
            "work_products_without_machine_spec": shared['machine_counterexamples']['not_applicable'],
        },
        "separate_checks": ["Dataset exists; execute verify_scale_cases.py for current T0/T1/T2 evidence.",
                            "Execute verify_methods.py for current bounded method routes."],
        "notice": ("Package checks alone do not claim a skill fully accepted. "
                   "Legacy narrative examples and non-machine professional reviews remain pending, not passed or machine-covered. "
                   "Passing engineering checks is not a seven-dimension acceptance."),
        "shared": shared,
        "per_skill": results,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")

    for name, value in conditions.items():
        print(f"  {name}: {value}")
    for name in ("machine_counterexamples", "legacy_narrative_review", "field_contracts", "calculators", "vocabulary", "duplication", "links"):
        item = shared[name]
        if item["status"] != "pass":
            print(f"  [{name}] {json.dumps({k: v for k, v in item.items() if k != 'status'}, ensure_ascii=False)[:400]}")
    for skill, item in results["files"].items():
        if item["status"] != "pass":
            print(f"  [{skill}] files: missing={item['missing']} undersized={item['undersized']}")
    print("all applicable pass:", report["all_applicable_pass"])
    print("wrote", out)
    sys.exit(0 if report["all_applicable_pass"] else 1)


if __name__ == "__main__":
    main()
