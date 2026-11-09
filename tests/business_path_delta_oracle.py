"""Independent SVG business-shaft delta audit; imports no renderer code."""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import annotation_geometry_oracle as geometry

EPS = 1e-7
FALSE_FLAGS = {name: False for name in ("accepted", "human_acceptance", "business_acceptance", "professional_acceptance", "source_equivalence_acceptance", "full_diagram_acceptance")}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def segments(row):
    e, off = row["e"], row["offset"]
    pts = geometry.path_points(e.get("d", ""))
    return [((a[0]+off[0], a[1]+off[1]), (b[0]+off[0], b[1]+off[1])) for a, b in geometry.path_segments(pts)]


def actual_paths(root):
    rows, unsupported = geometry.positioned(root)
    counts, paths = Counter(), {}
    for row in rows:
        e = row["e"]
        if row["in_defs"] or geometry.tag(e) != "path" or not row["owner"] or e.get("data-annotation-leader") == "true":
            continue
        owner = row["owner"]
        key = (owner, counts[owner])
        counts[owner] += 1
        paths[key] = {"owner": owner, "occurrence": key[1], "index": row["index"], "attrs": dict(e.attrib), "segments": segments(row), "offset": row["offset"]}
    return paths, unsupported


def exposed_segments(new_segments, old_segments):
    """Subtract all collinear old centerline intervals from every new segment."""
    exposed = []
    for a, b in new_segments:
        vx, vy = b[0]-a[0], b[1]-a[1]
        ll = vx*vx+vy*vy
        if ll < EPS:
            continue
        covered = []
        for c, d in old_segments:
            if abs(vx*(c[1]-a[1])-vy*(c[0]-a[0])) > EPS or abs(vx*(d[1]-a[1])-vy*(d[0]-a[0])) > EPS:
                continue
            lo, hi = sorted((((c[0]-a[0])*vx+(c[1]-a[1])*vy)/ll, ((d[0]-a[0])*vx+(d[1]-a[1])*vy)/ll))
            lo, hi = max(0., lo), min(1., hi)
            if hi-lo > EPS:
                covered.append((lo, hi))
        merged = []
        for lo, hi in sorted(covered):
            if merged and lo <= merged[-1][1]+EPS:
                merged[-1] = (merged[-1][0], max(hi, merged[-1][1]))
            else:
                merged.append((lo, hi))
        cursor = 0.
        intervals = []
        for lo, hi in merged:
            if lo-cursor > EPS:
                intervals.append((cursor, lo))
            cursor = max(cursor, hi)
        if 1.-cursor > EPS:
            intervals.append((cursor, 1.))
        exposed.extend(((a[0]+lo*vx, a[1]+lo*vy), (a[0]+hi*vx, a[1]+hi*vy)) for lo, hi in intervals)
    return exposed


def tangent(segment):
    a, b = segment
    length = math.dist(a, b)
    return ((b[0]-a[0])/length, (b[1]-a[1])/length) if length > EPS else None


def close(a, b):
    return a is not None and b is not None and math.dist(a, b) < EPS


def obstacle_records(root, report):
    rows, unsupported = geometry.positioned(root)
    font = geometry.font_metrics(root)
    card_indices = {c["index"] for c in report["card_instances"]}
    panel_indices = {p["index"] for p in report["geometry_proven_nonentity_container_records"]}
    obstacles = []
    markers = {e.get("id"): e for e in root.iter() if geometry.tag(e) == "marker"}
    def box_edges(box):
        x, y, xx, yy = box
        p = [(x,y),(xx,y),(xx,yy),(x,yy),(x,y)]
        return list(zip(p,p[1:]))
    for card in report["card_instances"]:
        obstacles.append({"category": "container-border" if card["container"] else "leaf-card", "index": card["index"], "entity_id": card["entity_id"], "instance": card["instance"], "box": card["box"], "segments": box_edges(card["box"]) if card["container"] else None, "padding": card["stroke_width"]/2})
    badge_indices = {b["index"]: b for b in report["badge_records"]}
    badge_text_indices = {b["text_index"]: b["owner"] for b in report["badge_records"]}
    for row in rows:
        if row["in_defs"]:
            continue
        e, off, owner, idx = row["e"], row["offset"], row["owner"], row["index"]
        kind = geometry.tag(e)
        rec = {"index": idx, "owner": owner}
        if kind == "text":
            box = geometry.text_box(e, off, font)
            if box:
                obstacles.append({**rec, "category": "text", "box": box, "text": "".join(e.itertext()), "own_badge_text_owner": badge_text_indices.get(idx), "padding": 0})
        elif kind == "rect" and idx not in card_indices and not any("%" in e.get(k, "0") for k in ("x","y","width","height")):
            x,y,w,h = (float(e.get(k,"0")) for k in ("x","y","width","height"))
            box = (x+off[0],y+off[1],x+w+off[0],y+h+off[1])
            if idx in badge_indices:
                obstacles.append({**rec, "owner": badge_indices[idx]["owner"], "category": "badge", "box": box, "padding": 0})
            elif e.get("fill") == "none" or idx in panel_indices:
                if idx in panel_indices and e.get("fill") != "none":
                    obstacles.append({**rec,"category":"proven-context-background","box":box,"padding":0,"geometry_proven_nonentity_container":True})
                if e.get("stroke", "none") != "none":
                    obstacles.append({**rec, "category": "proven-context-border" if idx in panel_indices else "other-context-border", "box": box, "segments": box_edges(box), "padding": geometry.painted_stroke_width(e)/2})
            else:
                obstacles.append({**rec,"category":"other-context-rectangle","box":box,"padding":geometry.painted_stroke_width(e)/2})
        elif kind == "path":
            ss = segments(row)
            obstacles.append({**rec, "category": "leader" if e.get("data-annotation-leader") == "true" else "shaft-or-other-path", "segments": ss, "padding": geometry.painted_stroke_width(e)/2,"fill":e.get("fill","none")})
            if e.get("marker-end") and ss:
                match = re.fullmatch(r"url\(#([^)]*)\)",e.get("marker-end"))
                marker = markers.get(match[1]) if match else None
                if marker is None:
                    unsupported.append({"kind":"missing-marker","index":idx})
                    continue
                before, end = ss[-1]
                ux,uy = tangent((before,end))
                scale = float(e.get("stroke-width","1")) if marker.get("markerUnits","strokeWidth") == "strokeWidth" else 1.
                for shape in marker:
                    if geometry.tag(shape) != "path":
                        unsupported.append({"kind":"marker-shape","index":idx})
                        continue
                    local = geometry.path_points(shape.get("d",""))
                    transformed = []
                    for mx,my in local:
                        mx,my = (mx-float(marker.get("refX","0")))*scale,(my-float(marker.get("refY","0")))*scale
                        transformed.append((end[0]+mx*ux-my*uy,end[1]+mx*uy+my*ux))
                    ss_marker = [(transformed[i],transformed[i+1]) for i in range(len(transformed)-1) if i+1 not in local.breaks]
                    obstacles.append({**rec,"category":"marker","segments":ss_marker,"padding":scale*geometry.painted_stroke_width(shape)/2+.2})
        elif kind in ("line","polyline","polygon"):
            if kind == "line":
                pts = [(float(e.get("x1","0")),float(e.get("y1","0"))),(float(e.get("x2","0")),float(e.get("y2","0")))]
            else:
                vals = list(map(float,re.findall(geometry.NUMBER,e.get("points",""))))
                pts = list(zip(vals[::2],vals[1::2]))
                if kind == "polygon" and pts:
                    pts.append(pts[0])
            pts = [(x+off[0],y+off[1]) for x,y in pts]
            obstacles.append({**rec,"category":"glyph-or-other-path","segments":list(zip(pts,pts[1:])),"padding":geometry.painted_stroke_width(e)/2})
    return obstacles, unsupported


def centerline_contact(a, b, c, d):
    vx,vy,wx,wy = b[0]-a[0],b[1]-a[1],d[0]-c[0],d[1]-c[1]
    den = vx*wy-vy*wx
    if abs(den) > EPS:
        t = ((c[0]-a[0])*wy-(c[1]-a[1])*wx)/den
        u = ((c[0]-a[0])*vy-(c[1]-a[1])*vx)/den
        if -EPS <= t <= 1+EPS and -EPS <= u <= 1+EPS:
            return {"kind":"point","point":(a[0]+t*vx,a[1]+t*vy)}
    elif abs(vx*(c[1]-a[1])-vy*(c[0]-a[0])) <= EPS:
        ll = vx*vx+vy*vy
        if ll > EPS:
            lo,hi = sorted((((c[0]-a[0])*vx+(c[1]-a[1])*vy)/ll,((d[0]-a[0])*vx+(d[1]-a[1])*vy)/ll))
            lo,hi = max(0.,lo),min(1.,hi)
            if hi >= lo-EPS:
                return {"kind":"collinear-overlap","overlap_segment":((a[0]+lo*vx,a[1]+lo*vy),(a[0]+hi*vx,a[1]+hi*vy))}
    return {"kind":"stroke-proximity","centerline_distance":geometry.segment_distance(a,b,c,d)}


def measure_added_segments(added, new_path, obstacles, old_segments=()):
    owner = new_path["owner"]
    pad = geometry.painted_stroke_width(new_path["attrs"])/2
    forbidden, permitted_delta = [], []
    for j,(a,b) in enumerate(added):
        for obstacle in obstacles:
            category = obstacle["category"]
            if category == "shaft-or-other-path" and obstacle.get("fill","none") != "none":
                category = "glyph-or-other-path"
                obstacle = {**obstacle,"category":category}
            if category == "proven-context-background" and geometry.contains(obstacle["box"],a):
                continue  # Same strict interior-anchor rule as annotation background exemption.
            if category == "badge" and obstacle.get("owner") == owner:
                continue
            if category == "shaft-or-other-path" and obstacle.get("owner") == owner and obstacle.get("fill","none") == "none":
                continue
            if category == "text" and obstacle.get("own_badge_text_owner") == owner:
                continue
            if obstacle.get("segments") is not None:
                contacts = []
                obstacle_segments = obstacle["segments"]
                if category == "leader" and obstacle.get("owner") == owner and obstacle_segments:
                    points = [obstacle_segments[0][0]]+[s[1] for s in obstacle_segments]
                    points = geometry.trim_start(points,pad+obstacle["padding"]+EPS)
                    obstacle_segments = list(zip(points,points[1:]))
                for k,(c,d) in enumerate(obstacle_segments):
                    if geometry.segment_distance(a,b,c,d) <= pad+obstacle["padding"]:
                        contact = centerline_contact(a,b,c,d)
                        if contact["kind"] == "point":
                            contact["point_on_original_owner_centerline"] = any(geometry.point_segment_distance(contact["point"],x,y) <= EPS for x,y in old_segments)
                        contacts.append({"obstacle_segment_index":k,"obstacle_segment":(c,d),**contact})
                hit = bool(contacts)
            else:
                hit = geometry.segment_box(a,b,geometry.expanded(obstacle["box"],pad+obstacle["padding"]))
                contacts = []
            if hit:
                item = {"added_segment_index":j, "added_segment":(a,b), "contact_details":contacts, **{k:v for k,v in obstacle.items() if k not in ("segments","padding")}}
                (permitted_delta if category in ("shaft-or-other-path","proven-context-border","proven-context-background") else forbidden).append(item)
    return forbidden, permitted_delta


def profile_variant(name):
    stem = Path(name).stem
    for variant in ("reference-modified","adaptive-modified","reference","adaptive"):
        if stem.endswith("-"+variant):
            return stem[:-len(variant)-1],variant
    return stem,"unknown"


def endpoint_cards(report, point):
    return [{k:c[k] for k in ("entity_id","instance","box","container")} for c in report["card_instances"] if geometry.contains(geometry.expanded(c["box"],1.5),point,strict=False)]


def ledger_records(svg_path, owner):
    path = svg_path.with_suffix(".coverage.json")
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return [r for r in (data.get("detail_ledger") or {}).get("relationships",[]) if r.get("id")==owner]


def audit(baseline_dir, candidate_dir, binding_report=None):
    old_files = {p.name:p for p in baseline_dir.glob("*.svg")}
    new_files = {p.name:p for p in candidate_dir.glob("*.svg")}
    expected = {r["file"]:r["svg_sha256"] for r in json.loads(binding_report.read_text())["results"]} if binding_report else {}
    errors, changes, inventory = [], [], []
    for name in sorted(old_files):
        if expected and expected.get(name) != sha(old_files[name]):
            errors.append({"file":name,"kind":"baseline-binding-mismatch"})
        if name not in new_files:
            continue
        old_root,new_root = ET.fromstring(old_files[name].read_text()),ET.fromstring(new_files[name].read_text())
        old_paths,u1 = actual_paths(old_root); new_paths,u2 = actual_paths(new_root)
        errors.extend({"file":name,**u} for u in u1+u2)
        if old_paths.keys() != new_paths.keys():
            errors.append({"file":name,"kind":"actual-business-path-instance-inventory-changed","removed":sorted(old_paths.keys()-new_paths.keys()),"added":sorted(new_paths.keys()-old_paths.keys())})
        before_report = after_report = obstacles = None
        for key in sorted(old_paths.keys() & new_paths.keys()):
            before,after = old_paths[key],new_paths[key]
            if before["attrs"] == after["attrs"] and before["offset"] == after["offset"]:
                continue
            before_attrs = {k:v for k,v in before["attrs"].items() if k != "d"}
            after_attrs = {k:v for k,v in after["attrs"].items() if k != "d"}
            bs,ns = before["segments"],after["segments"]
            identity_ok = before_attrs == after_attrs and before["offset"] == after["offset"]
            endpoints_ok = bool(bs and ns) and close(bs[0][0],ns[0][0]) and close(bs[-1][1],ns[-1][1])
            tangents_ok = bool(bs and ns) and close(tangent(bs[0]),tangent(ns[0])) and close(tangent(bs[-1]),tangent(ns[-1]))
            added = exposed_segments(ns,bs)
            old_length,new_length = sum(math.dist(*s) for s in bs),sum(math.dist(*s) for s in ns)
            if after_report is None:
                before_report = geometry.inspect(ET.tostring(old_root,encoding="unicode"))
                after_report = geometry.inspect(ET.tostring(new_root,encoding="unicode"))
                obstacles,unsupported = obstacle_records(new_root,after_report)
            forbidden,delta = measure_added_segments(added,after,obstacles,bs)
            profile,variant = profile_variant(name)
            old_ledger,new_ledger = ledger_records(old_files[name],key[0]),ledger_records(new_files[name],key[0])
            old_cards = {"source":endpoint_cards(before_report,bs[0][0]),"target":endpoint_cards(before_report,bs[-1][1])} if bs else None
            new_cards = {"source":endpoint_cards(after_report,ns[0][0]),"target":endpoint_cards(after_report,ns[-1][1])} if ns else None
            normalize_cards = lambda value: {k:[(c["entity_id"],c["box"],c["container"]) for c in v] for k,v in value.items()} if value else None
            change = {"file":name,"profile_id":profile,"variant":variant,"owner":key[0],"occurrence":key[1],"before_index":before["index"],"after_index":after["index"],"before_attrs":before["attrs"],"after_attrs":after["attrs"],"all_non_d_attributes_preserved":identity_ok,"endpoints_preserved":endpoints_ok,"endpoint_tangents_preserved":tangents_ok,"old_length":old_length,"new_length":new_length,"length_delta":new_length-old_length,"added_centerline_segments":added,"added_centerline_length":sum(math.dist(*s) for s in added),"removed_centerline_segments":exposed_segments(bs,ns),"forbidden_added_segment_conflicts":forbidden,"other_shaft_and_proven_context_border_geometry_delta":delta,"unsupported_geometry":unsupported,"annotation_oracle_passed_for_changed_svg":after_report["passed"],"actual_endpoint_card_instances_before":old_cards,"actual_endpoint_card_instances_after":new_cards,"endpoint_card_hierarchy_preserved":normalize_cards(old_cards)==normalize_cards(new_cards),"relationship_ledger_records_before":old_ledger,"relationship_ledger_records_after":new_ledger,"relationship_ledger_records_preserved":old_ledger==new_ledger if old_ledger is not None and new_ledger is not None else None,"source_target_semantics_note":"Endpoint card identity/hierarchy and relationship ledger are mechanical evidence only; semantic acceptance remains false.",**FALSE_FLAGS}
            for category,label in (("proven-context-border","new_proven_context_border_centerline_crossing_points"),("shaft-or-other-path","new_other_shaft_centerline_crossing_points")):
                contacts = []
                seen = set()
                for item in delta:
                    if item["category"] != category:
                        continue
                    for contact in item["contact_details"]:
                        if contact["kind"] == "point":
                            key_contact = (item["index"],tuple(round(x,7) for x in contact["point"]))
                            if key_contact not in seen:
                                original_kinds = []
                                c,d = contact["obstacle_segment"]
                                for x,y in bs:
                                    old_contact = centerline_contact(x,y,c,d)
                                    if old_contact["kind"] == "point" and close(old_contact["point"],contact["point"]):
                                        original_kinds.append("point")
                                    elif old_contact["kind"] == "collinear-overlap" and geometry.point_segment_distance(contact["point"],*old_contact["overlap_segment"]) <= EPS:
                                        original_kinds.append("collinear-overlap")
                                contacts.append({"obstacle_index":item["index"],"obstacle_owner":item.get("owner"),"point":contact["point"],"point_on_original_owner_centerline":contact["point_on_original_owner_centerline"],"original_owner_contact_kinds_at_point":sorted(set(original_kinds))})
                                seen.add(key_contact)
                change[label] = contacts
            change["geometry_delta_contacts_by_category"] = dict(Counter(item["category"] for item in delta))
            change["path_geometry_checks_passed"] = identity_ok and endpoints_ok and tangents_ok and new_length+EPS >= old_length and not forbidden and not unsupported
            changes.append(change)
        inventory.append({"file":name,"before_svg_sha256":sha(old_files[name]),"after_svg_sha256":sha(new_files[name]),"actual_business_path_instances_before":len(old_paths),"actual_business_path_instances_after":len(new_paths)})
    missing,extra = sorted(old_files.keys()-new_files.keys()),sorted(new_files.keys()-old_files.keys())
    return {"schema_version":"independent-business-path-delta/2","baseline_dir":str(baseline_dir),"candidate_dir":str(candidate_dir),"baseline_binding_report":str(binding_report) if binding_report else None,"baseline_binding_report_sha256":sha(binding_report) if binding_report else None,"baseline_svg_count":len(old_files),"candidate_svg_count":len(new_files),"missing_svg_files":missing,"extra_svg_files":extra,"errors":errors,"changed_path_instances":len(changes),"changed_svg_files":len({c["file"] for c in changes}),"forbidden_added_segment_conflicts":sum(len(c["forbidden_added_segment_conflicts"]) for c in changes),"geometry_delta_contacts_by_category":dict(Counter(item["category"] for c in changes for item in c["other_shaft_and_proven_context_border_geometry_delta"])),"new_proven_context_border_centerline_crossings":sum(len(c["new_proven_context_border_centerline_crossing_points"]) for c in changes),"new_other_shaft_centerline_crossings":sum(len(c["new_other_shaft_centerline_crossing_points"]) for c in changes),"passed":not missing and not extra and not errors and all(c["path_geometry_checks_passed"] for c in changes),"changes":changes,"svg_inventory_bindings":inventory,"audit_implementation_sha256":sha(Path(__file__)),"geometry_oracle_sha256":sha(Path(geometry.__file__)),"png_view_count":0,"interpretation":"Mechanical SVG geometry delta only; normal business-shaft container crossings and other-shaft crossings remain explicit deltas; annotation leaders receive no such border exemption. Crossings do not establish semantic or professional acceptance.",**FALSE_FLAGS}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("baseline_dir",type=Path)
    p.add_argument("candidate_dir",type=Path)
    p.add_argument("--baseline-binding-report",type=Path)
    p.add_argument("--out",type=Path,required=True)
    args = p.parse_args()
    if args.out.exists():
        raise SystemExit("Refusing to replace an existing evidence report")
    result = audit(args.baseline_dir,args.candidate_dir,args.baseline_binding_report)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("changes","svg_inventory_bindings")},ensure_ascii=False,indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
