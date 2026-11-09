"""Load versioned capability contracts without a machine-specific source path."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_RENDERERS = {
    "business-capability-map": "nested-map",
    "functional-decomposition-diagram": "nested-map",
    "organization-decomposition-diagram": "nested-map",
    "organization-map": "network", "information-map": "network",
    "business-model-diagram": "canvas", "value-chain-diagram": "value-chain",
    "value-stream-map": "stage-map", "platform-decomposition-diagram": "deployment",
    "software-distribution-diagram": "deployment",
    "environments-and-locations-diagram": "deployment",
    "application-and-user-location-diagram": "deployment",
    "data-security-diagram": "deployment",
    "network-and-communications-diagram": "deployment",
    "networked-computing-hardware-diagram": "deployment",
    "application-migration-diagram": "roadmap",
    "process-flow-diagram": "swimlane",
}

def load():
    arts = {a["id"]: a for a in json.loads((ROOT / "artifacts.json").read_text())["artifacts"]}
    dels = {d["id"]: d for d in json.loads((ROOT / "deliverables.json").read_text())["deliverables"]}
    path = ROOT / "capabilities.json"
    cap = json.loads(path.read_text()) if path.exists() else {}
    from field_contracts import apply_contract_overlay
    cap = apply_contract_overlay(cap)
    for w in cap.get("work_products", []):
        if w["id"] in arts:
            continue
        a = dict(w)
        a.setdefault("name_zh", a.get("name", a["id"]))
        a.setdefault("name_en", a.get("name", a["id"]))
        a.setdefault("kind", "report")
        a.setdefault("entity_types", a.get("elements", []) if isinstance(a.get("elements"), list) and all(isinstance(e, str) for e in a["elements"]) else [])
        a.setdefault("relationship_types", [])
        a.setdefault("fields", ["name"])
        a.setdefault("semantic_checks", a.get("checks", []))
        a.setdefault("analysis", a.get("analysis_steps", []))
        a.setdefault("notation", a.get("renderer", "network"))
        arts[a["id"]] = a
    profiles = {p["id"]: p for p in cap.get("profiles", [])}
    for aid, pid in cap.get('default_profiles', {}).items():
        if aid in arts: arts[aid]['default_profile_id'] = pid
    return arts, dels, profiles, cap.get("analysis_methods", [])

def profile_for(view, contract, profiles):
    pid = view.get('profile_id') or contract.get('default_profile_id')
    if pid:
        if pid not in profiles:
            raise ValueError("未知视图规范：" + pid)
        p = profiles[pid]
        if p["artifact_id"] != view["artifact_id"]:
            raise ValueError("profile 与制品族不匹配：" + view["id"])
        return p
    raise ValueError('制品缺少已登记的默认视图规范：' + contract['id'])
