"""Independent annotation geometry audit of painted SVG, including repeated cards.

No renderer state or placement helper is imported. `inspect(svg, coverage=None)`
returns JSON-compatible findings. The CLI inspects every SVG in a directory.
Curve geometry is sampled conservatively; text ink uses the embedded TrueType
font without browser shaping, with additional padding for kerning/antialiasing.
Unsupported transforms or geometry are reported as failures, never skipped.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import math
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

NUMBER = r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?"
EPS = 1e-6
INK_PADDING = 1.5
FONT_CACHE = {}


def tag(e):
    return e.tag.rsplit("}", 1)[-1]


def painted_stroke_width(e):
    """A width property creates no painted stroke when stroke is none."""
    return 0. if e.get("stroke", "none") == "none" else float(e.get("stroke-width", "1"))


def expanded(box, pad):
    return (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)


def overlap(a, b):
    return max(a[0], b[0]) < min(a[2], b[2]) - EPS and max(a[1], b[1]) < min(a[3], b[3]) - EPS


def contains(box, point, strict=True):
    pad = EPS if strict else -EPS
    return box[0] + pad < point[0] < box[2] - pad and box[1] + pad < point[1] < box[3] - pad


def proper_contains_box(outer, inner):
    return (outer[0]+EPS < inner[0] and outer[1]+EPS < inner[1]
            and inner[2] < outer[2]-EPS and inner[3] < outer[3]-EPS)


def segment_box(p, q, box):
    """Liang-Barsky intersection, including the stroked edge of an obstacle."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    lo, hi = 0.0, 1.0
    for den, num in ((-dx, p[0] - box[0]), (dx, box[2] - p[0]),
                     (-dy, p[1] - box[1]), (dy, box[3] - p[1])):
        if abs(den) < EPS:
            if num < -EPS:
                return False
        else:
            t = num / den
            if den < 0:
                lo = max(lo, t)
            else:
                hi = min(hi, t)
            if lo > hi + EPS:
                return False
    return True


def point_segment_distance(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    ll = dx * dx + dy * dy
    t = max(0., min(1., ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / ll)) if ll else 0.
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def segment_distance(a, b, c, d):
    def cross(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    aa, bb, cc, dd = cross(a, b, c), cross(a, b, d), cross(c, d, a), cross(c, d, b)
    if aa * bb <= 0 and cc * dd <= 0 and segment_box(a, b, (min(c[0], d[0]), min(c[1], d[1]), max(c[0], d[0]), max(c[1], d[1]))):
        return 0.
    return min(point_segment_distance(a, c, d), point_segment_distance(b, c, d),
               point_segment_distance(c, a, b), point_segment_distance(d, a, b))


def trim_start(points, distance):
    points = list(points)
    while len(points) > 1 and distance > 0:
        a, b = points[:2]
        ll = math.hypot(b[0] - a[0], b[1] - a[1])
        if ll <= distance:
            distance -= ll
            points.pop(0)
        else:
            points[0] = (a[0] + (b[0] - a[0]) * distance / ll,
                         a[1] + (b[1] - a[1]) * distance / ll)
            break
    return points


class PathPoints(list):
    def __init__(self):
        super().__init__()
        self.breaks = set()


def path_segments(points):
    return [(a,b) for i,(a,b) in enumerate(zip(points,points[1:]),1) if i not in getattr(points,"breaks",set())]


def path_points(d):
    """Flatten emitted SVG commands and preserve separate subpaths."""
    toks = re.findall(r"[A-Za-z]|" + NUMBER, d)
    points, cur, start, cmd, i = PathPoints(), (0., 0.), (0., 0.), None, 0
    previous_op, previous_control = None, None
    arity = {"M": 2, "L": 2, "H": 1, "V": 1, "Q": 4, "C": 6, "T": 2, "S": 4, "A": 7}
    while i < len(toks):
        if toks[i].isalpha():
            cmd, i = toks[i], i + 1
            if cmd.upper() == "Z":
                points.append(start)
                cur, cmd, previous_op, previous_control = start, None, "Z", None
                continue
        if cmd is None or cmd.upper() not in arity:
            raise ValueError("unsupported path command: " + str(cmd))
        n = arity[cmd.upper()]
        if i + n > len(toks) or any(x.isalpha() for x in toks[i:i+n]):
            raise ValueError("incomplete path command")
        vs, i, relative = list(map(float, toks[i:i+n])), i + n, cmd.islower()
        op = cmd.upper()
        if op in {"M", "L"}:
            nxt = (vs[0] + (cur[0] if relative else 0), vs[1] + (cur[1] if relative else 0))
            if op == "M" and points:
                points.breaks.add(len(points))
            points.append(nxt)
            cur = nxt
            if op == "M":
                start, cmd = cur, "l" if relative else "L"
        elif op in {"H", "V"}:
            cur = (vs[0] + (cur[0] if relative else 0), cur[1]) if op == "H" else (cur[0], vs[0] + (cur[1] if relative else 0))
            points.append(cur)
        elif op == "A":
            rx, ry, rotation, large, sweep, xx, yy = vs
            end = (xx + (cur[0] if relative else 0), yy + (cur[1] if relative else 0))
            rx, ry, phi = abs(rx), abs(ry), math.radians(rotation % 360)
            if rx < EPS or ry < EPS or math.hypot(end[0]-cur[0],end[1]-cur[1]) < EPS:
                points.append(end)
            else:
                cp, sp = math.cos(phi), math.sin(phi)
                xp = cp*(cur[0]-end[0])/2 + sp*(cur[1]-end[1])/2
                yp = -sp*(cur[0]-end[0])/2 + cp*(cur[1]-end[1])/2
                ratio = xp*xp/(rx*rx) + yp*yp/(ry*ry)
                if ratio > 1:
                    rx, ry = rx*math.sqrt(ratio), ry*math.sqrt(ratio)
                numerator = max(0., rx*rx*ry*ry-rx*rx*yp*yp-ry*ry*xp*xp)
                denominator = rx*rx*yp*yp+ry*ry*xp*xp
                factor = (-1 if bool(large) == bool(sweep) else 1)*math.sqrt(numerator/denominator) if denominator else 0.
                cxp, cyp = factor*rx*yp/ry, -factor*ry*xp/rx
                cx, cy = cp*cxp-sp*cyp+(cur[0]+end[0])/2, sp*cxp+cp*cyp+(cur[1]+end[1])/2
                a1 = math.atan2((yp-cyp)/ry,(xp-cxp)/rx)
                a2 = math.atan2((-yp-cyp)/ry,(-xp-cxp)/rx)
                delta = (a2-a1) % (2*math.pi)
                if not sweep:
                    delta -= 2*math.pi
                steps = max(8,math.ceil(abs(delta)*math.sqrt(max(rx,ry)/1.6)))
                for k in range(1,steps+1):
                    a = a1+delta*k/steps
                    points.append((cx+cp*rx*math.cos(a)-sp*ry*math.sin(a),cy+sp*rx*math.cos(a)+cp*ry*math.sin(a)))
                points[-1] = end
            cur = end
        else:
            controls = [(vs[j] + (cur[0] if relative else 0), vs[j+1] + (cur[1] if relative else 0)) for j in range(0, n, 2)]
            if op in {"T","S"}:
                reflection = (2*cur[0]-previous_control[0],2*cur[1]-previous_control[1]) if previous_control is not None and previous_op in ({"Q","T"} if op=="T" else {"C","S"}) else cur
                controls.insert(0,reflection)
            poly = [cur] + controls
            length = sum(math.hypot(b[0]-a[0], b[1]-a[1]) for a, b in zip(poly, poly[1:]))
            steps = max(8, min(5000, math.ceil(length / 4)))
            for k in range(1, steps + 1):
                t, u = k / steps, 1 - k / steps
                if op in {"Q","T"}:
                    points.append((u*u*cur[0] + 2*u*t*controls[0][0] + t*t*controls[1][0],
                                   u*u*cur[1] + 2*u*t*controls[0][1] + t*t*controls[1][1]))
                else:
                    points.append((u**3*cur[0] + 3*u*u*t*controls[0][0] + 3*u*t*t*controls[1][0] + t**3*controls[2][0],
                                   u**3*cur[1] + 3*u*u*t*controls[0][1] + 3*u*t*t*controls[1][1] + t**3*controls[2][1]))
            cur = controls[-1]
            previous_control = controls[-2]
        if op not in {"Q","T","C","S"}:
            previous_control = None
        previous_op = op
    return points


def positioned(root):
    rows, unsupported = [], []
    def walk(e, offset=(0., 0.), owner=None, instance=None, in_defs=False):
        in_defs = in_defs or tag(e) == "defs"
        transform = e.get("transform", "")
        if transform:
            match = re.fullmatch(r"\s*translate\(\s*(" + NUMBER + r")(?:[\s,]+(" + NUMBER + r"))?\s*\)\s*", transform)
            if match:
                offset = (offset[0] + float(match[1]), offset[1] + float(match[2] or 0))
            else:
                unsupported.append({"kind": "transform", "value": transform})
        owner = e.get("data-annotation-owner", e.get("data-relationship-id", owner))
        index = len(rows)
        if e.get("data-entity-id"):
            instance = index
        rows.append({"e": e, "offset": offset, "owner": owner, "instance": instance, "index": index, "in_defs": in_defs})
        for child in e:
            walk(child, offset, owner, instance, in_defs)
    walk(root)
    return rows, unsupported


def font_metrics(root):
    style = " ".join((e.text or "") for e in root.iter() if tag(e) == "style")
    match = re.search(r"data:font/[^;]+;base64,([A-Za-z0-9+/=]+)", style)
    if not match:
        return None
    raw = base64.b64decode(match[1])
    key = hashlib.sha256(raw).hexdigest()
    if key not in FONT_CACHE:
        font = TTFont(io.BytesIO(raw))
        FONT_CACHE[key] = {"font": font, "glyphs": font.getGlyphSet(), "cmap": font.getBestCmap(),
                           "upm": font["head"].unitsPerEm, "bounds": {}, "hash": key}
    return FONT_CACHE[key]


def text_box(e, offset, font):
    x, y = float(e.get("x", "0")) + offset[0], float(e.get("y", "0")) + offset[1]
    size = float(e.get("font-size", "16"))
    content = "".join(e.itertext())
    if font:
        cursor, boxes = 0., []
        for char in content:
            name = font["cmap"].get(ord(char), ".notdef")
            if name not in font["bounds"]:
                pen = BoundsPen(font["glyphs"])
                font["glyphs"][name].draw(pen)
                font["bounds"][name] = pen.bounds
            bounds = font["bounds"][name]
            if bounds:
                boxes.append((cursor + bounds[0], -bounds[3], cursor + bounds[2], -bounds[1]))
            cursor += font["font"]["hmtx"].metrics[name][0]
        scale, advance = size / font["upm"], cursor * size / font["upm"]
        if not boxes:
            return None
        box = (min(b[0] for b in boxes)*scale, min(b[1] for b in boxes)*scale,
               max(b[2] for b in boxes)*scale, max(b[3] for b in boxes)*scale)
    else:
        advance = sum(size * (1.0 if ord(c) > 255 else .61) for c in content)
        box = (0., -size, advance, size*.25)
    anchor = e.get("text-anchor", "start")
    shift = advance / 2 if anchor == "middle" else advance if anchor == "end" else 0.
    return expanded((x + box[0] - shift, y + box[1], x + box[2] - shift, y + box[3]), INK_PADDING)


def inspect(svg, coverage=None):
    root = ET.fromstring(svg)
    rows, unsupported = positioned(root)
    font = font_metrics(root)
    cards, texts, rects, badges, leaders, paths, marker_paths = [], [], [], [], [], [], []
    groups = {r["index"]: r for r in rows if r["e"].get("data-entity-id")}
    by_element = {id(r["e"]): r for r in rows}
    label_owners = {}
    for r in ((coverage or {}).get("detail_ledger") or {}).get("relationships", []):
        if r.get("index") is not None:
            label_owners.setdefault(str(r["index"]), set()).add(r["id"])
    for row in rows:
        e = row["e"]
        if tag(e) == "g" and e.get("data-relationship-id"):
            number = re.match(r"\s*\[(\d+)\]", "".join(e.itertext()))
            if number:
                label_owners.setdefault(number[1], set()).add(e.get("data-relationship-id"))
    latest_owner = None
    pending_leader = None
    for i, row in enumerate(rows):
        e, off, owner = row["e"], row["offset"], row["owner"]
        if row["in_defs"]:
            continue
        kind = tag(e)
        if kind == "text":
            try:
                box = text_box(e, off, font)
                if box:
                    texts.append({"index": i, "box": box, "text": "".join(e.itertext()), "instance": row["instance"], "owner": owner})
            except (ValueError, KeyError) as exc:
                unsupported.append({"kind": "text", "index": i, "reason": str(exc)})
        if kind == "rect":
            if any("%" in e.get(k, "0") for k in ("x", "y", "width", "height")):
                continue  # Whole-canvas background; it carries no text or card ID.
            x, y, w, h = (float(e.get(k, "0")) for k in ("x", "y", "width", "height"))
            rec = {"index": i, "box": (x+off[0], y+off[1], x+w+off[0], y+h+off[1]), "instance": row["instance"], "owner": owner,
                   "stroke": e.get("stroke", "none"), "stroke_width": painted_stroke_width(e), "fill": e.get("fill", "black")}
            is_badge = e.get("data-annotation-badge") == "true" or (e.get("fill") == "white" and e.get("stroke") == "none" and abs(h-22) < EPS)
            if is_badge:
                next_text = rows[i+1]["e"] if i+1 < len(rows) and tag(rows[i+1]["e"]) == "text" else None
                text = "".join(next_text.itertext()) if next_text is not None else e.get("data-annotation-label", "")
                number = re.match(r"^\[(\d+)\]", text)
                candidates = label_owners.get(number[1], set()) if number else set()
                if owner is None:
                    owner = next(iter(candidates)) if len(candidates) == 1 else latest_owner
                rec.update({"owner": owner, "label": text, "text_index": i+1 if next_text is not None else None})
                badges.append(rec)
                if pending_leader is not None:
                    pending_leader["badge_index"] = i
                    pending_leader["label"] = text
                    pending_leader["owner"] = pending_leader["owner"] or owner
                    pending_leader = None
            else:
                rects.append(rec)
            if row["instance"] is not None:
                group = groups[row["instance"]]
                # Only direct painted rectangles define this card instance.
                if any(id(c) == id(e) for c in group["e"]):
                    cards.append({**rec, "entity_id": group["e"].get("data-entity-id"), "container": False})
        if kind in {"path", "line", "polyline", "polygon"}:
            try:
                if kind == "path":
                    pts = path_points(e.get("d", ""))
                elif kind == "line":
                    pts = [(float(e.get("x1", "0")), float(e.get("y1", "0"))), (float(e.get("x2", "0")), float(e.get("y2", "0")))]
                else:
                    vals = list(map(float, re.findall(NUMBER, e.get("points", ""))))
                    pts = list(zip(vals[::2], vals[1::2]))
                    if kind == "polygon" and pts:
                        pts.append(pts[0])
                raw_segments = path_segments(pts)
                pts = [(x+off[0], y+off[1]) for x, y in pts]
                segments = [((a[0]+off[0],a[1]+off[1]),(b[0]+off[0],b[1]+off[1])) for a,b in raw_segments]
                if len(pts) < 2:
                    continue
                rec = {"index": i, "kind": kind, "points": pts, "segments": segments, "owner": owner, "padding": painted_stroke_width(e)/2,
                       "d": e.get("d", ""), "marker": e.get("marker-end"), "fill": e.get("fill", "none")}
                if e.get("data-annotation-leader") == "true":
                    rec["owner"] = owner or latest_owner
                    rec["badge_index"] = None
                    rec["label"] = e.get("data-annotation-label")
                    leaders.append(rec)
                    pending_leader = rec
                else:
                    paths.append(rec)
                    if owner:
                        latest_owner = owner
                    if rec["marker"]:
                        marker_paths.append((rec, e, off))
            except ValueError as exc:
                unsupported.append({"kind": kind, "index": i, "d": e.get("d"), "reason": str(exc)})
    for card in cards:
        card["container"] = any(other["instance"] != card["instance"] and proper_contains_box(card["box"], other["box"]) for other in cards)
    card_rect_indexes = {c["index"] for c in cards}
    panel_records = []
    for rect in rects:
        nested = [c for c in cards if proper_contains_box(rect["box"], c["box"])] if rect["instance"] is None and rect["index"] not in card_rect_indexes else []
        rect["contained_card_instances"] = [{"entity_id":c["entity_id"],"instance":c["instance"],"index":c["index"],"box":c["box"]} for c in nested]
        rect["geometry_proven_nonentity_container"] = bool(nested)
        if nested:
            panel_records.append(rect)
    markers = {e.get("id"): e for e in root.iter() if tag(e) == "marker"}
    arrow_shapes = []
    for rec, e, off in marker_paths:
        match = re.fullmatch(r"url\(#([^)]*)\)", rec["marker"])
        marker = markers.get(match[1]) if match else None
        if marker is None:
            unsupported.append({"kind": "missing-marker", "index": rec["index"]})
            continue
        end, before = rec["points"][-1], rec["points"][-2]
        length = math.hypot(end[0]-before[0], end[1]-before[1])
        if length < EPS:
            unsupported.append({"kind": "zero-marker-tangent", "index": rec["index"]})
            continue
        ux, uy = (end[0]-before[0])/length, (end[1]-before[1])/length
        scale = float(e.get("stroke-width", "1")) if marker.get("markerUnits", "strokeWidth") == "strokeWidth" else 1.
        for shape in marker:
            if tag(shape) != "path":
                unsupported.append({"kind": "marker-shape", "tag": tag(shape)})
                continue
            try:
                local = path_points(shape.get("d", ""))
                pts = []
                for mx, my in local:
                    mx, my = (mx-float(marker.get("refX", "0")))*scale, (my-float(marker.get("refY", "0")))*scale
                    pts.append((end[0]+mx*ux-my*uy, end[1]+mx*uy+my*ux))
                arrow_shapes.append({"index": rec["index"], "owner": rec["owner"], "points": pts, "segments": [(pts[i],pts[i+1]) for i in range(len(pts)-1) if i+1 not in local.breaks],
                                     "padding": scale*painted_stroke_width(shape)/2 + .2})
            except ValueError as exc:
                unsupported.append({"kind": "marker-path", "reason": str(exc)})
    conflicts = []
    badge_by_index = {b["index"]: b for b in badges}
    def add(leader, category, obstacle, **extra):
        conflicts.append({"category": category, "leader_index": leader["index"], "owner": leader["owner"],
                          "label": leader.get("label"), "obstacle_index": obstacle.get("index"), **extra})
    def hits(pts, box, pad):
        return any(segment_box(a, b, expanded(box, pad)) for a, b in zip(pts, pts[1:]))
    for leader in leaders:
        pts, pad = leader["points"], leader["padding"]
        own_badge = badge_by_index.get(leader["badge_index"])
        if own_badge is None:
            # Explicit owner permits a matching nonadjacent badge.
            matches = [b for b in badges if b["owner"] == leader["owner"] and (not leader.get("label") or b["label"] == leader["label"])]
            if len(matches) == 1:
                own_badge = matches[0]
            else:
                add(leader, "unmapped-leader-badge", {})
        if own_badge:
            bx = own_badge["box"]
            corners = [(bx[0],bx[1]),(bx[2],bx[1]),(bx[2],bx[3]),(bx[0],bx[3]),(bx[0],bx[1])]
            if min(point_segment_distance(pts[-1], a, b) for a,b in zip(corners,corners[1:])) > .75:
                add(leader, "leader-not-attached-to-badge", own_badge)
            before_endpoint = trim_start(list(reversed(pts)), pad + .75)
            if hits(before_endpoint, bx, pad):
                add(leader, "leader-enters-own-badge-before-endpoint", own_badge)
        own_paths = [p for p in paths if p["owner"] == leader["owner"]]
        if not own_paths or not any(point_segment_distance(pts[0], a, b) <= 1.5 for p in own_paths for a, b in p["segments"]):
            add(leader, "leader-not-attached-to-relationship", {})
        for card in cards:
            box = card["box"]
            if card["container"] and contains(box, pts[0]):
                edges = [(box[0], box[1]), (box[2], box[1]), (box[2], box[3]), (box[0], box[3]), (box[0], box[1])]
                if any(segment_distance(a, b, c, d) <= pad+card["stroke_width"]/2 for a, b in zip(pts, pts[1:]) for c, d in zip(edges, edges[1:])):
                    add(leader, "leader-container-border", card, entity_id=card["entity_id"], instance=card["instance"], box=box)
            elif hits(pts, box, pad+card["stroke_width"]/2):
                add(leader, "leader-card", card, entity_id=card["entity_id"], instance=card["instance"], box=box)
        for text in texts:
            if own_badge and text["index"] == own_badge.get("text_index"):
                continue
            if hits(pts, text["box"], pad):
                add(leader, "leader-text", text, text=text["text"], box=text["box"], instance=text["instance"])
        for rect in rects:
            if rect["index"] in card_rect_indexes:
                continue
            bx = rect["box"]
            container_interior = rect["geometry_proven_nonentity_container"] and contains(bx, pts[0])
            if rect["fill"] == "none" or container_interior:
                corners = [(bx[0],bx[1]),(bx[2],bx[1]),(bx[2],bx[3]),(bx[0],bx[3]),(bx[0],bx[1])]
                conflict = rect["stroke"] != "none" and any(segment_distance(a,b,c,d) <= pad+rect["stroke_width"]/2 for a,b in zip(pts,pts[1:]) for c,d in zip(corners,corners[1:]))
            else:
                conflict = hits(pts, bx, pad+rect["stroke_width"]/2)
            if conflict:
                add(leader, "leader-other-rectangle", rect, box=rect["box"],
                    geometry_proven_nonentity_container=rect["geometry_proven_nonentity_container"],
                    container_anchor_inside=container_interior,
                    contained_card_instances=rect["contained_card_instances"])
        for badge in badges:
            if own_badge and badge["index"] == own_badge["index"]:
                continue
            if hits(pts, badge["box"], pad):
                add(leader, "leader-other-badge", badge, badge_owner=badge["owner"], box=badge["box"])
        for path in paths:
            line_pts = trim_start(pts, pad + path["padding"] + EPS) if path["owner"] == leader["owner"] else pts
            if any(segment_distance(a,b,c,d) <= pad+path["padding"] for a,b in zip(line_pts,line_pts[1:]) for c,d in path["segments"]):
                add(leader, "leader-relationship-or-other-path", path, path_owner=path["owner"])
        for arrow in arrow_shapes:
            if any(segment_distance(a,b,c,d) <= pad+arrow["padding"] for a,b in zip(pts,pts[1:]) for c,d in arrow["segments"]):
                add(leader, "leader-arrowhead", arrow, arrow_owner=arrow["owner"])
    for i, leader in enumerate(leaders):
        for other in leaders[i+1:]:
            if any(segment_distance(a,b,c,d) <= leader["padding"]+other["padding"]+.4 for a,b in zip(leader["points"],leader["points"][1:]) for c,d in zip(other["points"],other["points"][1:])):
                add(leader, "leader-other-leader", other, other_owner=other["owner"])
    badge_conflicts = []
    def badge_add(badge, category, obstacle, **extra):
        badge_conflicts.append({"category":category,"badge_index":badge["index"],"owner":badge["owner"],
                                "label":badge["label"],"badge_box":badge["box"],"obstacle_index":obstacle.get("index"),**extra})
    def border_hits_badge(badge, rect):
        bx = rect["box"]
        corners = [(bx[0],bx[1]),(bx[2],bx[1]),(bx[2],bx[3]),(bx[0],bx[3]),(bx[0],bx[1])]
        return rect["stroke"] != "none" and any(segment_box(a,b,expanded(badge["box"],rect["stroke_width"]/2)) for a,b in zip(corners,corners[1:]))
    for badge in badges:
        bx = badge["box"]
        center = ((bx[0]+bx[2])/2,(bx[1]+bx[3])/2)
        if font:
            own_text = next((t for t in texts if t["index"] == badge.get("text_index")),None)
            if own_text and not (bx[0]-EPS <= own_text["box"][0] and bx[1]-EPS <= own_text["box"][1]
                                 and own_text["box"][2] <= bx[2]+EPS and own_text["box"][3] <= bx[3]+EPS):
                badge_add(badge,"badge-own-text-outside-footprint",own_text,text=own_text["text"],ink_box=own_text["box"])
        for card in cards:
            container_interior = card["container"] and contains(card["box"],center)
            collision = border_hits_badge(badge,card) if container_interior else overlap(bx,expanded(card["box"],card["stroke_width"]/2))
            if collision:
                badge_add(badge,"badge-container-border" if container_interior else "badge-card",card,
                          entity_id=card["entity_id"],instance=card["instance"],box=card["box"])
        for text in texts:
            if text["index"] == badge.get("text_index"):
                continue
            if overlap(bx,text["box"]):
                badge_add(badge,"badge-text",text,text=text["text"],box=text["box"],instance=text["instance"])
        for rect in rects:
            if rect["index"] in card_rect_indexes:
                continue
            container_interior = rect["geometry_proven_nonentity_container"] and contains(rect["box"],center)
            collision = border_hits_badge(badge,rect) if rect["fill"] == "none" or container_interior else overlap(bx,expanded(rect["box"],rect["stroke_width"]/2))
            if collision:
                badge_add(badge,"badge-other-rectangle",rect,box=rect["box"],
                          geometry_proven_nonentity_container=rect["geometry_proven_nonentity_container"],
                          container_center_inside=container_interior,contained_card_instances=rect["contained_card_instances"])
        for path in paths:
            # Only its own unfilled relationship shaft may pass under a badge.
            # Filled polygons/glyphs and all marker arrowheads retain full checks.
            if badge["owner"] is not None and path["owner"] == badge["owner"] and path["fill"] == "none" and path["kind"] != "polygon":
                continue
            if any(segment_box(a,b,expanded(bx,path["padding"])) for a,b in path["segments"]):
                badge_add(badge,"badge-other-shaft-or-path",path,path_owner=path["owner"])
        for arrow in arrow_shapes:
            if any(segment_box(a,b,expanded(bx,arrow["padding"])) for a,b in arrow["segments"]):
                badge_add(badge,"badge-arrowhead",arrow,arrow_owner=arrow["owner"])
        for leader in leaders:
            if leader["badge_index"] == badge["index"]:
                continue
            if hits(leader["points"],bx,leader["padding"]):
                badge_add(badge,"badge-other-leader",leader,leader_owner=leader["owner"])
    for i,badge in enumerate(badges):
        for other in badges[i+1:]:
            if overlap(badge["box"],other["box"]):
                badge_add(badge,"badge-other-badge",other,other_owner=other["owner"],other_box=other["box"])
    duplicates = {}
    for card in cards:
        duplicates.setdefault(card["entity_id"], set()).add(card["instance"])
    return {"schema_version": "independent-annotation-geometry/1", "passed": not conflicts and not badge_conflicts and not unsupported,
            "cards": len(cards), "actual_entity_instances": len(groups), "duplicate_entity_instances": {k: len(v) for k,v in duplicates.items() if len(v)>1},
            "container_cards": sum(c["container"] for c in cards), "visible_texts": len(texts), "badges": len(badges),
            "annotation_leaders": len(leaders), "relationship_and_other_paths": len(paths), "checked_arrow_shapes": len(arrow_shapes),
            "font_sha256": font["hash"] if font else None,
            "text_measurement": "embedded-TTF glyph ink union, no browser shaping, 1.5px padding" if font else "conservative em-width fallback, 1.5px padding",
            "unsupported_geometry": unsupported, "conflicts": conflicts,
            "badge_conflicts": badge_conflicts, "badge_records": badges,
            "embedded_font_badge_footprints_checked": len(badges) if font else 0,
            "leader_records": [{k:v for k,v in p.items() if k != "padding"} for p in leaders],
            "card_instances": cards,
            "geometry_proven_nonentity_container_records": panel_records,
            "accepted": False, "human_acceptance": False, "business_acceptance": False,
            "professional_acceptance": False, "source_equivalence_acceptance": False, "full_diagram_acceptance": False}


def self_test():
    """Counterexamples prove repeated cards and every requested obstacle class."""
    prefix = '<svg xmlns="http://www.w3.org/2000/svg"><g data-relationship-id="r"><path d="M100 20 L140 20" stroke="black" stroke-width="1.8"/></g>'
    badge = '<rect data-annotation-owner="r" data-annotation-badge="true" x="110" y="190" width="30" height="22" fill="white" stroke="none"/><text x="125" y="206" font-size="13" text-anchor="middle">[8]</text>'
    leader = '<path data-annotation-owner="r" data-annotation-leader="true" d="M125 20 L125 190" stroke="black" stroke-width="1"/>'
    cases = []
    def test(name, body, categories=(), should_pass=False):
        result = inspect(prefix + body + leader + badge + '</svg>')
        actual = {c["category"] for c in result["conflicts"]}
        passed = result["passed"] if should_pass else set(categories).issubset(actual)
        cases.append({"name": name, "passed": passed, "categories": sorted(actual), "expected": list(categories)})
        return result
    test("clear-own-relationship-attachment", "", should_pass=True)
    repeated = ''.join('<g data-entity-id="reuse"><rect x="%s" y="50" width="40" height="40"/></g>' % x for x in (0,60,110))
    result = test("third-repeated-leaf-card-is-not-overwritten", repeated, ("leader-card",))
    cases[-1]["passed"] &= result["duplicate_entity_instances"].get("reuse") == 3 and any(c.get("instance") == result["card_instances"][2]["instance"] for c in result["conflicts"])
    test("visible-text", '<text x="100" y="110">ledger</text>', ("leader-text",))
    test("ledger-rectangle", '<rect x="110" y="90" width="40" height="30"/>', ("leader-other-rectangle",))
    test("transparent-context-interior-is-not-painted", '<rect x="90" y="0" width="80" height="230" fill="none" stroke="black"/>', should_pass=True)
    test("transparent-context-border-is-painted", '<rect x="90" y="0" width="80" height="100" fill="none" stroke="black"/>', ("leader-other-rectangle",))
    nested = '<g data-entity-id="nested"><rect x="95" y="30" width="15" height="20"/></g>'
    panel = '<rect x="90" y="0" width="80" height="230" fill="#eef" stroke="black"/>'
    test("filled-nonentity-panel-inside-anchor-clear-space", panel+nested, should_pass=True)
    test("filled-nonentity-panel-outside-anchor-is-solid", '<rect x="90" y="40" width="80" height="130" fill="#eef" stroke="black"/><g data-entity-id="nested"><rect x="95" y="60" width="15" height="20"/></g>', ("leader-other-rectangle",))
    test("filled-nonentity-panel-without-card-is-solid", panel, ("leader-other-rectangle",))
    test("filled-nonentity-panel-border-still-painted", '<rect x="90" y="0" width="80" height="100" fill="#eef" stroke="black"/>'+nested, ("leader-other-rectangle",))
    test("same-box-card-cannot-prove-panel-container", panel+'<g data-entity-id="same-box"><rect x="90" y="0" width="80" height="230"/></g>', ("leader-card","leader-other-rectangle"))
    test("filled-nonentity-panel-text-still-painted", panel+nested+'<text x="100" y="110">context</text>', ("leader-text",))
    test("other-badge", '<rect data-annotation-owner="q" data-annotation-badge="true" x="110" y="90" width="30" height="22" fill="white" stroke="none"/><text x="125" y="106">[9]</text>', ("leader-other-badge",))
    test("other-relationship", '<path data-relationship-id="q" d="M100 90 L140 90" stroke="black" stroke-width="1.8"/>', ("leader-relationship-or-other-path",))
    test("other-leader", '<path data-annotation-owner="q" data-annotation-leader="true" d="M100 90 L150 90" stroke="black"/>', ("leader-other-leader",))
    test("container-background-is-space-but-leaf-is-solid", '<g data-entity-id="container"><rect x="90" y="0" width="80" height="230"/></g><g data-entity-id="nested-leaf"><rect x="110" y="90" width="30" height="30"/></g>', ("leader-card",))
    test("container-border-remains-an-obstacle", '<g data-entity-id="container"><rect x="90" y="0" width="80" height="100" stroke="black"/></g><g data-entity-id="nested-leaf"><rect x="95" y="30" width="15" height="20"/></g>', ("leader-container-border",))
    arrow = '<defs><marker id="a" refX="8" refY="4"><path d="M0 0 L8 4 L0 8" fill="none" stroke="black"/></marker></defs><path data-relationship-id="q" d="M100 90 L130 90" stroke="black" stroke-width="1.8" marker-end="url(#a)"/>'
    test("arrowhead", arrow, ("leader-arrowhead",))
    def test_badge(name, body, expected=(), should_pass=False, badge_markup=None, font_defs=""):
        label = badge_markup or '<rect data-annotation-owner="r" data-annotation-badge="true" x="110" y="190" width="30" height="22" fill="white" stroke="none"/><text x="125" y="206" font-size="13" text-anchor="middle">[8]</text>'
        result = inspect(prefix+font_defs+body+label+'</svg>')
        actual = {c["category"] for c in result["badge_conflicts"]}
        passed = result["passed"] if should_pass else set(expected).issubset(actual)
        cases.append({"name":name,"passed":passed,"badge_categories":sorted(actual),"expected":list(expected)})
        return result
    test_badge("badge-own-adjacent-text-is-exempt", "", should_pass=True)
    test_badge("badge-third-repeated-card-not-overwritten", ''.join('<g data-entity-id="repeat"><rect x="%s" y="180" width="40" height="50"/></g>' % x for x in (0,60,110)), ("badge-card",))
    test_badge("badge-first-repeated-card-remains-obstacle", ''.join('<g data-entity-id="repeat"><rect x="%s" y="180" width="40" height="50"/></g>' % x for x in (110,170,230)), ("badge-card",))
    test_badge("badge-ledger-text-is-not-exempt", '<text x="100" y="206">ledger</text>', ("badge-text",))
    test_badge("badge-other-badge", '<rect data-annotation-owner="q" data-annotation-badge="true" x="120" y="195" width="30" height="22" fill="white" stroke="none"/><text x="135" y="211">[9]</text>', ("badge-other-badge",))
    test_badge("badge-other-shaft", '<path data-relationship-id="q" d="M100 200 L150 200" stroke="black" stroke-width="1.8" fill="none"/>', ("badge-other-shaft-or-path",))
    test_badge("badge-own-shaft-is-permitted", '<path data-relationship-id="r" d="M100 200 L150 200" stroke="black" stroke-width="1.8" fill="none"/>', should_pass=True)
    test_badge("badge-own-arrow-is-still-obstacle", '<defs><marker id="a" refX="8" refY="4"><path d="M0 0 L8 4 L0 8" fill="none" stroke="black"/></marker></defs><path data-relationship-id="r" d="M100 200 L140 200" stroke="black" stroke-width="1.8" fill="none" marker-end="url(#a)"/>', ("badge-arrowhead",))
    test_badge("badge-inside-filled-proven-panel", panel+nested, should_pass=True)
    test_badge("badge-filled-unrelated-panel-is-solid", panel, ("badge-other-rectangle",))
    test_badge("badge-filled-proven-panel-border-is-solid", '<rect x="90" y="0" width="80" height="200" fill="#eef" stroke="black"/>'+nested, ("badge-other-rectangle",))
    test_badge("badge-proven-panel-outside-center-is-solid", '<rect x="130" y="0" width="80" height="230" fill="#eef" stroke="black"/><g data-entity-id="nested"><rect x="135" y="30" width="15" height="20"/></g>', ("badge-other-rectangle",))
    test_badge("badge-entity-container-clear-interior", '<g data-entity-id="container"><rect x="90" y="0" width="80" height="230"/></g>'+nested, should_pass=True)
    test_badge("badge-entity-container-border-is-painted", '<g data-entity-id="container"><rect x="90" y="0" width="80" height="205" stroke="black"/></g>'+nested, ("badge-container-border",))
    location = '<g data-entity-id="loc-east"><rect x="30" y="933" width="1020" height="362" fill="#f4f7fb" stroke="#8298aa"/><text x="42" y="985" font-size="11">location / loc-east</text></g>'
    actual_badge = '<rect data-annotation-owner="r" data-annotation-badge="true" x="14" y="975.3" width="31" height="22" fill="white" stroke="none"/><text x="29.5" y="991.3" font-size="13" text-anchor="middle">[1]</text>'
    test_badge("confirmed-location-badge-covers-card-and-identity", location, ("badge-card","badge-text"), badge_markup=actual_badge)
    font_file = Path(__file__).with_name("annotation_test_font.ttf")
    if font_file.exists():
        font_defs = '<defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+base64.b64encode(font_file.read_bytes()).decode()+')}</style></defs>'
        compact = '<rect data-annotation-owner="r" data-annotation-badge="true" x="110" y="190" width="32" height="15.6" fill="white" stroke="none"/><text x="126" y="202" font-size="11" text-anchor="middle">[14]</text>'
        result = test_badge("compact-height-15p6-font11-complete-ink-fits", "", should_pass=True, badge_markup=compact, font_defs=font_defs)
        cases[-1]["passed"] &= result["badges"] == 1 and result["embedded_font_badge_footprints_checked"] == 1
        test_badge("compact-too-short-footprint-rejected", "", ("badge-own-text-outside-footprint",), badge_markup=compact.replace('height="15.6"','height="12"'),font_defs=font_defs)
    else:
        cases.append({"name":"compact-font-fixture-required","passed":False,"reason":"annotation_test_font.ttf is missing"})
    clear_rect = '<rect x="101.2" y="90" width="23.1" height="30" fill="#eef" stroke="none"/>'
    test("filled-no-stroke-rectangle-does-not-invent-half-pixel-margin", clear_rect, should_pass=True)
    test("filled-no-stroke-rectangle-ignores-unused-width-property", clear_rect.replace('stroke="none"','stroke="none" stroke-width="50"'), should_pass=True)
    test("filled-no-stroke-rectangle-fill-intersection-still-rejected", clear_rect.replace('width="23.1"','width="24"'), ("leader-other-rectangle",))
    test("filled-stroked-rectangle-painted-half-width-still-rejected", clear_rect.replace('stroke="none"','stroke="black"'), ("leader-other-rectangle",))
    clear_badge_rect = '<rect x="90" y="190" width="19.8" height="22" fill="#eef" stroke="none"/>'
    test_badge("badge-clear-of-no-stroke-fill-edge", clear_badge_rect, should_pass=True)
    test_badge("badge-real-fill-edge-intersection-rejected", clear_badge_rect.replace('width="19.8"','width="20.2"'), ("badge-other-rectangle",))
    test_badge("badge-real-stroked-edge-intersection-rejected", clear_badge_rect.replace('stroke="none"','stroke="black"'), ("badge-other-rectangle",))
    test_badge("badge-clear-of-no-stroke-leaf-edge", '<g data-entity-id="leaf">'+clear_badge_rect+'</g>', should_pass=True)
    test_badge("badge-real-stroked-leaf-edge-intersection-rejected", '<g data-entity-id="leaf">'+clear_badge_rect.replace('stroke="none"','stroke="black"')+'</g>', ("badge-card",))
    return {"schema_version": "independent-annotation-oracle-self-test/1", "passed": all(c["passed"] for c in cases), "cases": cases,
            "accepted": False, "human_acceptance": False, "business_acceptance": False, "professional_acceptance": False,
            "source_equivalence_acceptance": False, "full_diagram_acceptance": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        report = self_test()
    else:
        if args.input is None:
            parser.error("input SVG or directory is required")
        files = [args.input] if args.input.is_file() else sorted(args.input.glob("*.svg"))
        results = []
        for file in files:
            coverage_file = file.with_suffix(".coverage.json")
            coverage = json.loads(coverage_file.read_text()) if coverage_file.exists() else None
            data = file.read_bytes()
            results.append({"file": file.name, "svg_sha256": hashlib.sha256(data).hexdigest(), **inspect(data.decode(), coverage)})
        report = {"schema_version": "independent-annotation-geometry-campaign/1", "passed": bool(results) and all(r["passed"] for r in results),
                  "svg_count": len(results), "annotation_leaders": sum(r["annotation_leaders"] for r in results),
                  "conflicts": sum(len(r["conflicts"]) for r in results), "badges": sum(r["badges"] for r in results),
                  "badge_conflicts": sum(len(r["badge_conflicts"]) for r in results), "unsupported_geometry": sum(len(r["unsupported_geometry"]) for r in results),
                  "embedded_font_badge_footprints_checked": sum(r["embedded_font_badge_footprints_checked"] for r in results),
                  "results": results, "accepted": False, "human_acceptance": False, "business_acceptance": False,
                  "professional_acceptance": False, "source_equivalence_acceptance": False, "full_diagram_acceptance": False}
    report["oracle_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k:v for k,v in report.items() if k not in {"results", "cases"}}))
    return int(not report["passed"])


if __name__ == "__main__":
    raise SystemExit(main())
