#!/usr/bin/env python3
"""Write analysis and modification evidence records from real executions.

analysis      one record per executed method, citing the execution report and the
              model it ran against. Methods that were blocked get no record, because
              a blocked method has no result to attest.
modification  one aggregate record citing the baseline/target comparison output that
              actually contains the concept-level diffs.

Both records are hash-bound to files that exist. Nothing here claims business
acceptance; the reviewer field states AI-assisted review.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "examples/qianlin-synthetic/projection/model.json"
ANALYSIS = ROOT / "reviews/analysis-execution.json"
COMPARE = ROOT / "reviews/qianlin-baseline-target-comparison.json"
OUT = ROOT / "reviews/analysis-modification-records.json"
REVIEWER = {"id": "cursor-ai-reviewer",
            "role": "AI-assisted reviewer (not a human signatory)"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if not COMPARE.is_file():
        result = subprocess.run(
            [str(ROOT / ".venv/bin/python"), str(ROOT / "scripts/analyze.py"), str(MODEL),
             "--compare", "--baseline-state", "QL-baseline", "--target-state", "QL-target"],
            capture_output=True, text=True)
        if result.returncode != 0:
            sys.exit("比较失败：" + (result.stdout or "")[:400] + (result.stderr or "")[:400])
        COMPARE.write_text(result.stdout)

    comparison = json.loads(COMPARE.read_text())["comparison"]
    changed = [c for c in comparison["changes"] if c.get("attributes")]
    classified = [c for c in comparison["changes"] if c.get("kind")]
    execution = json.loads(ANALYSIS.read_text())

    analysis_records = {}
    for item in execution["executed"]:
        analysis_records[item["method_id"]] = {
            "method_id": item["method_id"],
            "calculator_id": item["calculator_id"],
            "inputs_sha256": item["inputs_sha256"],
            "result_sha256": item["result_sha256"],
            "evidence": [
                {"path": "reviews/analysis-execution.json",
                 "sha256": sha(ANALYSIS),
                 "locator": "executed:" + item["method_id"]},
                {"path": "examples/qianlin-synthetic/projection/model.json",
                 "sha256": sha(MODEL),
                 "locator": "entities/attributes"},
            ],
            "observations": [
                "在黔磷虚构模型上执行 " + item["calculator_id"]
                + "，结果摘要：" + item["result_summary"][:120],
                "结果只在该虚构输入下成立，不证明真实企业结论",
            ],
            "reviewer": REVIEWER,
        }

    modification = {
        "scope": "QL-enterprise",
        "baseline_state": "QL-baseline",
        "target_state": "QL-target",
        "changed_concepts": len(changed),
        "kind_classified": len(classified),
        "evidence": [{"path": "reviews/qianlin-baseline-target-comparison.json",
                      "sha256": sha(COMPARE)}],
        "sample": [
            {"concept_id": c["concept_id"], "baseline_id": c["baseline_id"],
             "target_id": c["target_id"],
             "changed_attributes": sorted(c["attributes"].keys())[:5]}
            for c in changed[:20]
        ],
        "observations": [
            "基线到目标共 " + str(len(changed)) + " 个概念有属性差异、"
            + str(len(classified)) + " 个增删候选",
            "差异由 analyze.py --compare 按 concept_id 配对产生，未经人工业务判断",
        ],
        "reviewer": REVIEWER,
    }

    payload = {
        "schema_version": "analysis-modification-records/1",
        "generated_at": "2026-11-04",
        "notice": ("分析记录来自真实计算器执行；修改记录来自真实基线目标比较。"
                   "两者都不构成业务验收。"),
        "analysis": {
            "executed_methods": analysis_records,
            "executed_count": len(analysis_records),
            "blocked_count": len(execution["blocked"]),
            "blocked": execution["blocked"],
        },
        "modification": modification,
    }
    if args.write:
        OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")

    print(json.dumps({
        "analysis_executed": len(analysis_records),
        "analysis_blocked": len(execution["blocked"]),
        "modification_changed_concepts": len(changed),
        "modification_kind_classified": len(classified),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
