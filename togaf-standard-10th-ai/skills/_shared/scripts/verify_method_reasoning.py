#!/usr/bin/env python3
"""Independent, bounded reasoning checks; not a TOGAF/business approval engine.

No calculator imports. Decimal/Fraction arithmetic and a Kahn graph implementation
are deliberately independent of the production calculators. Qualitative cases are
reviewed in a separately authored, hash-bound JSON record, not auto-rated here.
"""
import argparse
from datetime import date
from decimal import Decimal
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "references/method-cases"


def batches(nodes, edges):
    """Return deterministic hard-dependency levels; reject cycles/unknown nodes."""
    remaining = set(nodes)
    if len(remaining) != len(nodes):
        raise ValueError("duplicate-node")
    if any(a not in remaining or b not in remaining for a, b in edges):
        raise ValueError("unknown-endpoint")
    result = []
    while remaining:
        ready = sorted(n for n in remaining
                       if not any(b == n and a in remaining for a, b in edges))
        if not ready:
            raise ValueError("cycle")
        result.append(ready)
        remaining.difference_update(ready)
    return result


def order_valid(levels, edges):
    positions = {n: i for i, level in enumerate(levels) for n in level}
    return all(a in positions and b in positions and positions[a] < positions[b]
               for a, b in edges)


def benefit(target, baseline, observed):
    """Percent-number inputs; None observation is not zero or a plan."""
    if observed is None:
        return None
    t, b, o = map(Decimal, (target, baseline, observed))
    if t <= 0 or b <= 0:
        raise ValueError("non-positive-reference")
    return {"target_deviation": (o-t)/t*100,
            "baseline_improvement": (b-o)/b*100,
            "absolute_pp": o-t, "meets_target": o <= t,
            "trigger_gt_50": (o-t)/t*100 > 50}


def combined_rate(rates, volumes):
    """Use group transaction counts, never a growth percentage as a weight."""
    if (len(rates) != len(volumes) or not rates or
            any(v < 0 for v in volumes) or sum(volumes) <= 0):
        raise ValueError("missing-or-invalid-group-volumes")
    return sum(F(r)*v for r, v in zip(rates, volumes))/sum(volumes)


def score(values, weights):
    if len(values) != len(weights) or sum(weights) <= 0:
        raise ValueError("invalid-weights")
    return sum(F(v)*F(w) for v, w in zip(values, weights))/sum(map(F, weights))


def snapshot_usable(as_of_hours, ttl_hours, retention=24):
    """The clock is data as-of age, not export/query/cache insertion time."""
    return (0 <= as_of_hours <= retention and ttl_hours >= 0
            and ttl_hours <= retention-as_of_hours)


def operability_document_gate(conditions, rollback_fields):
    """Project conjunction gate only; existence of answers proves no runtime effect."""
    required = {"people", "systems", "data", "controls", "rollback"}
    return (set(conditions) == required and all(v is True for v in conditions.values())
            and set(rollback_fields) == {"trigger", "owner", "verification"}
            and all(v is True for v in rollback_fields.values()))


def read_case(name):
    return (CASES / (name + ".md")).read_text(encoding="utf-8")


def evidence_row(body, evidence_id):
    found = [line for line in body.splitlines()
             if re.match(r"\|\s*`?" + re.escape(evidence_id) + r"`?\s*\|", line)]
    if len(found) != 1:
        raise AssertionError("expected one evidence row: " + evidence_id)
    return found[0]


def engineering_assertions():
    checks = []

    def check(check_id, condition, detail):
        if not condition:
            raise AssertionError(check_id + ": " + detail)
        checks.append({"id": check_id, "status": "passed", "basis": detail})

    graph = read_case("dependency-topological-order")
    nodes, hard = [], []
    for i in range(1, 8):
        row = evidence_row(graph, "DEP-" + str(i))
        node = "W" + str(i)
        nodes.append(node)
        if "硬依赖" in row:
            hard.extend((p, node) for p in re.findall(r"`(W\d+)`", row)[1:])
    levels = batches(nodes, hard)
    stated = re.search(r"\[\[W1.*?\]\]", graph).group(0)
    rendered = "[" + ",".join("[" + ",".join(x) + "]" for x in levels) + "]"
    check("dependency-node-completeness", rendered == stated and
          set(sum(levels, [])) == set(nodes) and len(sum(levels, [])) == 7,
          "DEP-1..7 independently yield [[W1,W3,W7],[W2],[W4],[W5],[W6]].")
    check("dependency-soft-edge", order_valid(levels, [("W7", "W5")]) and
          batches(nodes, hard + [("W7", "W5")]) == levels and
          "crossed_soft_edges=[]" in graph,
          "W7 precedes W5; promoting this soft edge does not add a batch.")
    check("dependency-modification", len(batches(nodes, hard + [("W2", "W3")])) == 6,
          "Adding W2→W3 changes logical depth from five to six, not calendar duration.")
    try:
        batches(nodes, hard + [("W6", "W1")])
        cycle_rejected = False
    except ValueError as exc:
        cycle_rejected = str(exc) == "cycle"
    check("dependency-negative-semantics", cycle_rejected and
          not order_valid([["W1", "W3", "W7"], ["W2"], ["W4", "W5"], ["W6"]], hard),
          "A true directed cycle is rejected; same-batch W4/W5 is an order violation, not a cycle.")

    ben = read_case("benefit-realization-trigger")
    def percent(key):
        return re.search(r"\*\*([0-9.]+)%\*\*", evidence_row(ben, key)).group(1)
    t, b, o = percent("BEN-1"), percent("BEN-2"), percent("BEN-3")
    result = benefit(t, b, o)
    rounded = lambda x: str(x.quantize(Decimal("0.1")))
    check("benefit-deviations", rounded(result["target_deviation"]) == "83.3" and
          rounded(result["baseline_improvement"]) == "38.9" and
          result["absolute_pp"] == Decimal("0.5") and
          all(s in ben for s in ("83.3%", "38.9%", "+0.5")),
          "BEN-1/2/3 yield +83.3%, 38.9%, +0.5pp independently.")
    old = re.search(r"\*\*([0-9.]+)%\*\*", evidence_row(ben, "BEN-6")).group(1)
    check("benefit-not-achieved", not result["meets_target"] and
          not benefit(t, b, old)["meets_target"] and "均未达目标" in ben,
          "Both observed 1.1% and old-business 0.7% exceed the 0.6% target.")
    check("benefit-trigger-boundary", result["trigger_gt_50"] and
          not benefit("0.6", "1.8", "0.9")["trigger_gt_50"] and
          benefit("0.6", "1.8", None) is None,
          "Deviation must be strictly >50%; no observation yields no computation.")
    check("benefit-weighting-not-causation",
          combined_rate(["0.7", "2.1"], [100, 40]) == F("1.1") and
          combined_rate(["0.7", "1.7"], [100, 40]) != F("1.1") and
          "不能直接与估算 0.4pp 相加" in ben,
          "100 old +40 new transactions would require 2.1% new-group rate; growth alone proves neither weights nor causation.")

    a, c, bb = [F(4), F(3), F(7, 3)], [F(4), F(5), F(0)], [F(3), F(2), F(11, 3)]
    weights = [F(2, 5), F(2, 5), F(1, 5)]
    check("work-package-scores", [score(v, weights) for v in (a, bb, c)] ==
          [F(49, 15), F(41, 15), F(18, 5)],
          "Declared 0–5 cost transform gives A=3.2667,B=2.7333,C=3.6; anchors remain unconfirmed.")
    stable = True
    for i in range(3):
        for factor in (F(4, 5), F(6, 5)):
            w = weights[:]
            w[i] *= factor
            stable &= score(c, w) > score(a, w) > score(bb, w)
    w = [F(3, 10), F(7, 20), F(7, 20)]
    check("work-package-sensitivity", stable and score(a, w) > score(c, w) > score(bb, w)
          and score(a, [F(17, 30), F(7, 30), F(1, 5)]) ==
          score(c, [F(17, 30), F(7, 30), F(1, 5)]),
          "Six single-weight ±20% normalized endpoints keep C>A>B; joint change gives A>C>B; fixed-cost tie is 7/30.")
    wp = read_case("work-package-prioritization")
    check("work-package-narrative", "W-B` 仍为第三" in wp and "0–5" in wp and "±20%" in wp,
          "Case does not report B rising to second or label a zero score as a 1–5 scale.")
    check("option-weighted-sensitivity",
          score([4, 4, 3, 5], [1, 1, 2, 1]) == F(19, 5) and
          score([2, 2, 5, 2], [1, 1, 2, 1]) == F(16, 5) and
          score([4, 4, 3, 5], [1, 1, 5, 1]) < score([2, 2, 5, 2], [1, 1, 5, 1]),
          "Independent preference arithmetic reproduces A-first and sensitivity B-first.")
    check("scheduling-and-capacity", 2+max(3, 4)+1+2 == 9 and
          2+3+4+1+2 == 12 and 2+3 > 4 and 2+1 <= 4 and
          "同样在 day9" in read_case("architecture-project-scheduling") and
          "仍为 2+3=5 > 4" in read_case("architecture-backlog-method"),
          "Serial B/C order cannot change day12; removing only 1-day audit leaves 5>4.")
    check("business-attribute-boundaries", F(996, 10) == F("99.6") and
          F(992, 10) < F("99.3") and not F("99.3") < F("99.3") and
          F(99200, 996) > F("99.5") and F(99200, 996) != 100,
          "Fixed-denominator 99.2% triggers; 99.3 does not; deleting bad samples gives 99.5984%, not 100%.")
    check("environment-and-lifecycle", Decimal("172.5")*Decimal("0.4")-460 == -391
          and 215*Decimal("0.4")-460 == -374
          and 1200+3*69 == 1407 and 50+3*300 == 950
          and F(1200-50, 300-69) == F(1150, 231),
          "Operational deltas -391/-374; three-year scenario 1407/950; crossing 1150/231 years, conditional on lifecycle assumptions.")
    check("snapshot-age-and-ttl", snapshot_usable(22, 2) and
          not snapshot_usable(22, 3) and not snapshot_usable(25, 0) and
          "as-of" in read_case("msa-data-distribution-conditions-method"),
          "A fresh export does not reset source data age; cache cannot outlive remaining validity.")
    check("project-tolerance", (date(2026, 10, 18)-date(2026, 10, 16)).days == 2 and
          not 2 > 2 and (date(2026, 10, 20)-date(2026, 10, 16)).days > 2,
          "Two calendar days is in tolerance; four triggers; approved baseline stays fixed.")
    com = read_case("digital-enablement-competency-mapping-method")
    rows = [line.split("|") for line in com.splitlines()
            if re.match(r"\| (团队|团队之团队) \| `", line)]
    check("competency-counts", len(rows) == 10 and len({r[1].strip() for r in rows}) == 2
          and sum("具备" in r[4] for r in rows) == 3 and
          sum("部分" in r[4] for r in rows) == 7 and "3 具备 / 7 部分" in com,
          "The actual role table has ten rows, two represented contexts, three evidenced and seven partial.")
    acmm = read_case("acmm-maturity-assessment")
    factors = list(map(int, re.search(r"形成分值\[([0-9,]+)\]", acmm).group(1).split(",")))
    changed = factors[:-1] + [3]
    check("acmm-ordinal-summary", len(factors) == 9 and sum(factors) == 20 and
          sum(changed) == 22 and [sum(x >= n for x in factors) for n in (1, 2, 3, 4, 5)] ==
          [9, 8, 3, 0, 0] and sum(x >= 3 for x in changed) == 4,
          "Explicit project factors produce 20/9→22/9 and 3→4 at level3; arithmetic confers no certification or feature evidence.")
    conditions = dict.fromkeys(("people", "systems", "data", "controls", "rollback"), True)
    rollback = dict.fromkeys(("trigger", "owner", "verification"), True)
    baseline = dict(conditions, rollback=False)
    transition = read_case("transition-operability-check")
    check("transition-project-conjunction", not operability_document_gate(baseline, {})
          and operability_document_gate(conditions, rollback)
          and not operability_document_gate(conditions, dict(rollback, verification=False))
          and not operability_document_gate(dict(conditions, data=None), rollback)
          and "工程清单" in transition and "财务凭证" in transition,
          "Four of five is not a score or probability; complete rollback text passes only the document gate, not business acceptance or runtime verification.")
    debt = read_case("technical-debt-register-method")
    check("debt-new-evidence-estimate", 1*2*300 == 600 and 52*600 == 31200
          and "600元" in debt and "31200元" in debt and "52周" in debt,
          "New duration/rate evidence permits 600/week; 31200/year requires the explicit constant 52-week scenario, not a claim of actual loss.")
    readiness = read_case("msa-readiness-evidence-method")
    table = readiness.split("| 条件 | 判定 | 依据 |", 1)[1].split("## 输出与追溯", 1)[0]
    answers = [line.split("|")[2].strip().replace("**", "") for line in table.splitlines()
               if line.startswith("|") and "---" not in line]
    check("msa-readiness-state-counts", len(answers) == 8 and answers.count("是") == 4
          and answers.count("否") == 2 and sum(a.startswith("部分") for a in answers) == 2,
          "Actual eight-row readiness table yields four yes, two partial, two no; requirement existence is not attainment.")
    ten = read_case("mdm-operational-ten-questions-method")
    qa_rows = [line.split("|") for line in ten.splitlines() if re.match(r"\| \d+ \|", line)]
    qa = [r[3].strip() for r in qa_rows[:10]]
    check("mdm-ten-question-states", len(qa) == 10 and
          {state: qa.count(state) for state in ("是", "部分", "否", "未知")} ==
          {"是": 2, "部分": 3, "否": 2, "未知": 3},
          "The ten answers remain four-state; absent evidence is unknown, not no; appointment alone changes no governance mechanism.")
    check("operating-model-capacity", max(24-16, 0) == 8 and max(24-26, 0) == 0
          and "24-26" in read_case("operating-model-submodel-analysis-method"),
          "Eight-hour shortage closes under the explicit unchanged 24-hour demand; it does not prove authority or service quality.")
    return checks


def verify_review(path, cases_dir=CASES):
    """Check review provenance/completeness, not whether its judgments are true."""
    report = json.loads(Path(path).read_text(encoding="utf-8"))
    files = {p.stem: p for p in cases_dir.glob("*.md")}
    records = report["case_reviews"]
    if not files or len(records) != len(files) or len({r["case_id"] for r in records}) != len(files):
        raise ValueError("review-must-cover-all-unique-cases")
    if {r["case_id"] for r in records} != set(files):
        raise ValueError("review-case-set-mismatch")
    input_root = ROOT if cases_dir.resolve() == (ROOT / 'references/method-cases').resolve() else cases_dir
    case_paths = {str(p.relative_to(input_root)) for p in files.values()}
    for record in records:
        if (record.get("method_id") != record["case_id"] or
                record.get("case_path") != str(files[record["case_id"]].relative_to(input_root))):
            raise ValueError("review-method-or-case-path-mismatch")
        digest = hashlib.sha256(files[record["case_id"]].read_bytes()).hexdigest()
        if digest != record["case_sha256"]:
            raise ValueError("stale-review-hash: " + record["case_id"])
        if not record.get("specific_basis") or not record.get("limitations"):
            raise ValueError("missing-specific-review-basis")
        if record.get("reviewer_kind") != "AI-implementation-agent":
            raise ValueError("reviewer-provenance-not-declared")
    inputs = report.get("inputs_sha256", {})
    if not case_paths.issubset(inputs):
        raise ValueError("missing-case-input-fingerprints")
    for name, expected in inputs.items():
        source = (input_root / name).resolve()
        if (Path(name).is_absolute() or ".." in Path(name).parts or
                not source.is_relative_to(input_root.resolve()) or not source.is_file()):
            raise ValueError("unsafe-review-input: " + name)
        if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
            raise ValueError("stale-review-input: " + name)
    for key in ("professional_author_review", "standards_source_verification", "business_acceptance"):
        if report["assurance_layers"][key]["status"] not in ("pending", "incomplete", "not-accepted"):
            raise ValueError("unwarranted-assurance: " + key)
    return len(records)


def main():
    global CASES
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--review", type=Path, help="Hash-bound separately authored review JSON")
    parser.add_argument("--cases-dir", "--cases", dest="cases_dir", type=Path, default=CASES)
    args = parser.parse_args()
    CASES = args.cases_dir.resolve()
    output = {"semantic_approval": "not-produced-by-this-program"}
    code = 0
    if not any(CASES.glob("*.md")):
        output.update(status="blocked", engineering_status="blocked", engineering_assertions=[],
                      reason="no-teaching-cases-found", cases_dir=str(CASES))
        code = 3
    else:
        try:
            checks = engineering_assertions()
            output.update(status="passed", engineering_assertions=checks, engineering_status="passed")
            if args.review:
                output["hash_bound_review_records"] = verify_review(args.review, CASES)
        except FileNotFoundError as exc:
            output.update(status="blocked", engineering_status="blocked", reason="required-case-or-review-missing", detail=str(exc))
            code = 3
        except (AssertionError, ValueError, KeyError, TypeError) as exc:
            output.update(status="failed", engineering_status="failed", reason=str(exc))
            code = 1
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
