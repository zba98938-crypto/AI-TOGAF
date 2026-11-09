#!/usr/bin/env python3
"""Prove the modification dimension with a real mutation, not a claim.

For each sampled view, the script generates the view, changes one attribute of an
entity the view actually selects, regenerates, and checks that the saved output
differs and that the new value literally appears in it.

A view whose output does not change is a real defect: it would mean the rendered
artifact is decoupled from the model. Those views are reported, not hidden.
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "examples/qianlin-synthetic/projection/model.json"
PYTHON = str(ROOT / ".venv/bin/python")
GENERATE = str(ROOT / "scripts/generate.py")
OUT = ROOT / "reviews/modification-mutation-probe.json"
SENTINEL = "变更探测值-修改维验证"


def generate(model_path, view_id, out_dir):
    return subprocess.run(
        [PYTHON, GENERATE, str(model_path), "--view", view_id,
         "--layout", "adaptive", "--out", str(out_dir)],
        capture_output=True, text=True)


def output_files(out_dir, view_id):
    folder = Path(out_dir) / "artifacts"
    return sorted(p for p in folder.glob(f"{view_id}.*")
                  if p.suffix in (".json", ".md", ".svg"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=6,
                        help="抽样视图数；0 表示全部")
    args = parser.parse_args()

    model = json.loads(MODEL.read_text())
    views = model["views"]
    chosen = views if args.samples == 0 else views[: args.samples]

    results = []
    for view in chosen:
        view_id = view["id"]
        entity_ids = view.get("entity_ids") or []
        if not entity_ids:
            results.append({"view_id": view_id, "status": "no-entities"})
            continue

        with tempfile.TemporaryDirectory() as base_tmp, \
                tempfile.TemporaryDirectory() as mut_tmp:
            first = generate(MODEL, view_id, base_tmp)
            if first.returncode != 0:
                results.append({"view_id": view_id, "status": "generation-failed",
                                "detail": (first.stdout or first.stderr)[:160]})
                continue

            mutated = json.loads(MODEL.read_text())
            target_id = entity_ids[0]
            target = next(e for e in mutated["entities"] if e["id"] == target_id)
            if target.get("attributes"):
                key = sorted(target["attributes"])[0]
                target["attributes"][key] = SENTINEL
                changed_field = f"attributes.{key}"
            else:
                target["name"] = SENTINEL
                changed_field = "name"
            mutated_path = Path(base_tmp) / "mutated.json"
            mutated_path.write_text(json.dumps(mutated, ensure_ascii=False))

            second = generate(mutated_path, view_id, mut_tmp)
            if second.returncode != 0:
                results.append({"view_id": view_id, "status": "regeneration-failed",
                                "detail": (second.stdout or second.stderr)[:160]})
                continue

            before = {p.suffix: p.read_text(errors="ignore")
                      for p in output_files(base_tmp, view_id)}
            after = {p.suffix: p.read_text(errors="ignore")
                     for p in output_files(mut_tmp, view_id)}
            shared = set(before) & set(after)
            changed = [s for s in shared if before[s] != after[s]]
            carries = [s for s in shared if SENTINEL in after[s]]
            status = ("output-changed-and-carries-value"
                      if changed and carries else
                      "output-changed-without-value" if changed else
                      "output-unchanged")
            results.append({
                "view_id": view_id,
                "status": status,
                "mutated_entity": target_id,
                "changed_field": changed_field,
                "suffixes_compared": sorted(shared),
                "suffixes_changed": sorted(changed),
                "suffixes_carrying_value": sorted(carries),
            })

    tally = {}
    for row in results:
        tally[row["status"]] = tally.get(row["status"], 0) + 1

    payload = {
        "schema_version": "modification-mutation-probe/1",
        "generated_at": "2026-11-04",
        "notice": ("对每个抽样视图改动一个属性后重新生成，比对保存输出。"
                   "输出未变即为真实缺陷，不掩盖。"),
        "probe_value": SENTINEL,
        "sampled": len(chosen),
        "tally": tally,
        "results": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(tally, ensure_ascii=False))
    for row in results:
        if row["status"] not in ("output-changed-and-carries-value",):
            print("  ATTENTION", row["view_id"], "|", row["status"])


if __name__ == "__main__":
    main()
