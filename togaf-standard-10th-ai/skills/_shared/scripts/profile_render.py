"""Model-driven, loss-aware SVG views. Layout is separate from business semantics.

SVG remains editable and every represented business element/edge retains its ID.
Unknown source notation is reported; this module does not assert standards certification.
"""
import html
import json
import math
import heapq
from annotation_clearance import geometry as annotation_geometry, badge_clear as annotation_badge_clear, local_badge, repair_route
from collections import defaultdict
from datetime import date
from pathlib import Path
from evaluation_semantics import parse_evaluation, is_evaluation_field_satisfied, stage_capability_errors
from matrix_semantics import matrix_options, project_matrix, cell_label

VERSION = "2.6"
ROOT = Path(__file__).resolve().parents[1]
PALETTE = ["#e2edf8", "#e7f1e9", "#fff0d8", "#efe7f7", "#e3f1f2", "#f8e6e6"]
HIERARCHY = {"decomposes", "contains", "composed_of", "aggregates", "composition", "aggregation", "has_part", "visually_contains"}
STAGE_TYPES = {"value_stage", "value_stream_stage", "stage", "customer_journey_stage"}
# Realization keeps the ArchiMate hollow-triangle head; it is not a plain arrow.
HOLLOW_HEAD = {"generalization", "realizes", "realization", "realizes_abb"}

def esc(value):
    return html.escape(str(value), quote=True)

def fmt(value):
    if value is None:
        return '未知'
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return str(value)

def foreground(fill):
    value=str(fill).lstrip('#')
    if len(value)==3:value=''.join(c*2 for c in value)
    try:
        rgb=[int(value[i:i+2],16)/255 for i in [0,2,4]]
        linear=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
        luminance=sum(v*w for v,w in zip(linear,[.2126,.7152,.0722]))
        return '#ffffff' if luminance<.22 else '#19364d'
    except (ValueError,IndexError):return '#19364d'

def wrap(value, units=38):
    lines=[]; line=""; count=0
    for c in fmt(value):
        n=2 if ord(c)>255 else 1
        if c=="\n" or count+n>units:
            lines.append(line);line="";count=0
        if c!="\n":line+=c;count+=n
    if line:lines.append(line)
    return lines or [""]

def cardinality(value):
    """Do not conflate unknown with unbounded or map a bounded max to many."""
    if isinstance(value,str):
        return {"one":"1","zero-or-one":"0..1","many":"0..*","one-or-more":"1..*","unknown":"?"}.get(value,value)
    if not isinstance(value,dict) or value.get("unknown") or value.get("known") is False or value.get("status")=="unknown":return "?"
    low=value.get("min");high=value.get("max")
    if value.get("unbounded") or high in ["*","unbounded"]:high="*"
    elif 'max' in value and high is None:high='*'  # Explicit schema null is unbounded; omitted max is not.
    elif high is None:high="?"
    if low is None:return "?.."+str(high) if high!="?" else "?"
    return str(low) if low==high else str(low)+".."+str(high)

class Drawing:
    def __init__(self, view, profile, layout):
        self.view=view;self.profile=profile;self.layout=layout;self.parts=[];self.width=1100;self.height=180
        self.positions={};self.entity_ids=set();self.relation_ids=set();self.attrs=defaultdict(set);self.relationship_attrs=defaultdict(set)
        self.errors=[];self.warnings=[];self.groups=[]
        self.edge_register=[]
        self.network_routing=False
        self.occupied_segments=[]
        self.endpoint_port_offsets={}
        self.label_boxes=[]
        self.endpoint_glyph_boxes=[]
        self.badge_requests=[]
        self.planned_label_boxes=[]
        self.routed_relationships={}
    def text(self,x,y,value,size=16,fill="#19364d",anchor="start",units=None):
        lines=wrap(value,units or 10000)
        for i,line in enumerate(lines):
            self.parts.append(f'<text x="{x}" y="{y+i*(size+7)}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{esc(line)}</text>')
        self.height=max(self.height,y+len(lines)*(size+7));return len(lines)*(size+7)
    def rect(self,x,y,w,h,fill="#fff",stroke="#8298aa",radius=6,extra=""):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" {extra}/>')
        self.width=max(self.width,x+w+30);self.height=max(self.height,y+h+20)
    def reserve_arrowhead(self,points):
        # Default markerUnits scales the 8-by-8 open SVG head by the path's
        # 1.8 stroke width. Include its stroke, rather than just its endpoint.
        x2,y2=points[-1];vx=x2-points[-2][0];vy=y2-points[-2][1]
        length=max(1,math.hypot(vx,vy));ux,uy=vx/length,vy/length
        head=[(x2,y2),(x2-14.4*ux+7.2*uy,y2-14.4*uy-7.2*ux),
              (x2-14.4*ux-7.2*uy,y2-14.4*uy+7.2*ux)]
        self.endpoint_glyph_boxes.append((min(x for x,y in head)-1.5,min(y for x,y in head)-1.5,
                                          max(x for x,y in head)+1.5,max(y for x,y in head)+1.5))
    def queue_badge(self,points,label,color,relationship_id,placer=None):
        # Probe the original placement only for its layout dimensions. Keeping
        # those dimensions preserves the subsequently routed paths and captions.
        # Paint labels after all relationship paths and glyphs are registered.
        first=len(self.parts);warnings=len(self.warnings);actual_boxes=self.label_boxes
        self.label_boxes=self.planned_label_boxes
        if placer:placer(self,points,label,color,relationship_id,planning=True)
        else:self.badge(points,label,color,relationship_id,planning=True)
        self.planned_label_boxes=self.label_boxes;self.label_boxes=actual_boxes
        del self.parts[first:];del self.warnings[warnings:]
        token='__TOGAF_BADGE_'+str(len(self.badge_requests))+'__';self.parts.append(token)
        self.routed_relationships[relationship_id]=points
        self.badge_requests.append((points,label,color,relationship_id,placer,token))
    def badge_clear(self,box,obstacles,relationship_id=None,planning=False):
        def overlap(a,b):return max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])
        if any(overlap(box,b) for b in obstacles):return False
        if not planning:
            for rid,points in self.routed_relationships.items():
                if rid==relationship_id:continue
                for p,q in zip(points,points[1:]):
                    line=(min(p[0],q[0])-1.5,min(p[1],q[1])-1.5,max(p[0],q[0])+1.5,max(p[1],q[1])+1.5)
                    if overlap(box,line):return False
        return True
    def flush_badges(self):
        # Replay the unchanged baseline badge pass only to preserve its canvas
        # width, caption wrapping and companion-ledger selection. Restore all
        # paint before validating the actual annotations below.
        original_parts=list(self.parts);original_warnings=list(self.warnings)
        original_labels=list(self.label_boxes);original_width=self.width;original_height=self.height
        for points,label,color,rid,placer,token in self.badge_requests:
            first=len(self.parts)
            if placer:placer(self,points,label,color,rid)
            else:self.badge(points,label,color,rid)
            paint=self.parts[first:];del self.parts[first:]
            slot=self.parts.index(token);self.parts[slot:slot+1]=paint
        self.baseline_caption_width=self.width;self.baseline_figure_height=self.height
        self.parts=original_parts;self.warnings=original_warnings;self.label_boxes=original_labels
        self.width=max(original_width,self.baseline_caption_width);self.height=original_height
        # Collect actual painted rectangles/text before placing annotations.
        # Endpoint lookup intentionally remains unchanged for business routing.
        self.annotation_geometry=annotation_geometry(self.parts)
        # Final headers end at local y=70 after the body's caption translation;
        # reserve the complete header band with an additional 8px ink margin.
        self.annotation_geometry['other_boxes'].append((0,0,self.baseline_caption_width,78))
        self.annotation_leaders=[]
        for points,label,color,rid,placer,token in self.badge_requests:
            first=len(self.parts);old_height=self.height;old_width=self.width
            old_warnings=len(self.warnings);old_labels=len(self.label_boxes)
            if placer:placer(self,points,label,color,rid)
            else:self.badge(points,label,color,rid)
            paint=self.parts[first:];del self.parts[first:]
            box=self.label_boxes[-1]
            # Validate against every actual card instance and painted text, not
            # self.positions (which keeps only the last reused ID instance).
            has_leader=any('data-annotation-leader="true"' in part for part in paint)
            self.label_boxes=self.label_boxes[:old_labels]
            if not has_leader and annotation_badge_clear(self,box,rid,points):
                self.label_boxes.append(box)
            else:
                self.height=old_height;self.width=old_width
                del self.warnings[old_warnings:]
                try:x,y,box,leader,font=local_badge(self,points,label,color,rid)
                except ValueError:
                    replacement,result=repair_route(self,points,label,color,rid)
                    points=replacement;self.routed_relationships[rid]=points
                    x,y,box,leader,font=result
                if leader:
                    path='M'+' L'.join(str(round(px,4))+','+str(round(py,4)) for px,py in leader)
                    self.parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1" stroke-dasharray="2 4" data-annotation-leader="true" data-relationship-id="{esc(rid)}" data-annotation-label="{esc(label)}"/>')
                    self.annotation_leaders.append(leader)
                    self.warnings.append("连线标号置于局部空白区；点状引线仅关联标号、不表示业务关系："+label)
                self.label_boxes.append(box)
                badge_height=round(box[3]-box[1],4)
                if badge_height.is_integer():badge_height=int(badge_height)
                self.rect(box[0],box[1],box[2]-box[0],badge_height,"white","none",2,extra=f'data-annotation-badge="true" data-annotation-font-size="{font}" data-relationship-id="{esc(rid)}" data-annotation-label="{esc(label)}"')
                self.text(x,y,label,font,color,"middle")
                paint=self.parts[first:];del self.parts[first:]
            slot=self.parts.index(token);self.parts[slot:slot+1]=paint
        self.badge_requests=[]
    def badge(self,points,label,color="#46647e",relationship_id=None,planning=False):
        width=len(label)*7+10;height=22
        segments=sorted(zip(points,points[1:]),key=lambda pair:math.hypot(pair[1][0]-pair[0][0],pair[1][1]-pair[0][1]),reverse=True)
        def overlap(a,b):return max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])
        chosen=None
        # An ancestor region is permitted label space for edges from nested
        # cards. Treat its border/header as context, not a solid obstacle.
        def contains_endpoint(box):
            x,y,w,h=box
            return any(x<p[0]<x+w and y<p[1]<y+h for p in [points[0],points[-1]])
        node_boxes=[(x,y,x+w,y+h) for x,y,w,h in self.positions.values() if not contains_endpoint((x,y,w,h))]
        for p,q in segments:
            for t in [.5,.35,.65,.2,.8]:
                x=max(width/2+14,p[0]+(q[0]-p[0])*t);y=p[1]+(q[1]-p[1])*t-8
                box=(x-width/2,y-16,x+width/2,y+6)
                if self.badge_clear(box,self.label_boxes+node_boxes+self.endpoint_glyph_boxes,relationship_id,planning):chosen=(x,y,box);break
            if chosen:break
        if not chosen:
            # A short vertical gap can fit the badge beside its line while
            # leaving the complete arrowhead and both adjacent cards visible.
            # Retain existing placements whenever their glyph clearance is safe.
            for p,q in segments:
                vertical=abs(p[0]-q[0]) < 1e-6
                horizontal=abs(p[1]-q[1]) < 1e-6
                if not vertical and (planning or not horizontal):continue
                for t in [.5,.35,.65,.2,.8]:
                    for side in [1,-1]:
                        x=max(width/2+14,p[0]+(q[0]-p[0])*t+(side*(width/2+12) if vertical else 0))
                        y=p[1]+(q[1]-p[1])*t+5+(side*(height/2+12) if horizontal else 0)
                        box=(x-width/2,y-16,x+width/2,y+6)
                        if self.badge_clear(box,self.label_boxes+node_boxes+self.endpoint_glyph_boxes,relationship_id,planning):
                            chosen=(x,y,box);break
                    if chosen:break
                if chosen:break
        if not chosen:
            p,q=segments[0]
            anchor_x,anchor_y=(p[0]+q[0])/2,(p[1]+q[1])/2
            # Keep the badge readable instead of painting it over a title/card.
            # A non-arrow dotted leader associates this annotation with its edge.
            x=max(width/2+14,anchor_x);y=max(self.height+30,anchor_y+30)
            chosen=(x,y,(x-width/2,y-16,x+width/2,y+6))
            self.parts.append(f'<path d="M{anchor_x},{anchor_y} L{x},{y-16}" fill="none" stroke="{color}" stroke-dasharray="2 4" data-annotation-leader="true"/>')
            self.warnings.append("连线标号移至空白区，点状引线仅关联标号、不表示业务关系："+label)
        x,y,box=chosen;self.label_boxes.append(box);self.rect(box[0],box[1],width,height,"white","none",2);self.text(x,y,label,13,color,"middle")
    def line(self,x1,y1,x2,y2,label="",relation=None,dashed=False,color="#46647e",arrow=True,bend=0):
        rid=relation["id"] if relation else None
        extra=(f' data-relationship-id="{esc(rid)}"' if rid else "")
        if rid:self.relation_ids.add(rid)
        dash=' stroke-dasharray="7 4"' if dashed else ""
        marker=' marker-end="url(#arrow)"' if arrow else ""
        mx=(x1+x2)/2;my=(y1+y2)/2
        distance=max(1,math.hypot(x2-x1,y2-y1));cx=mx-(y2-y1)*bend/distance;cy=my+(x2-x1)*bend/distance
        path=f'M{x1} {y1} Q{cx} {cy} {x2} {y2}' if bend else f'M{x1} {y1} L{x2} {y2}'
        self.parts.append(f'<g{extra}><path d="{path}" fill="none" stroke="{color}" stroke-width="1.8"{dash}{marker}/></g>')
        if label:
            tx=mx+(cx-mx)/2;ty=my+(cy-my)/2-8
            self.text(tx,ty,label,13,color,"middle",34)
    def entity_lines(self,e,fields=None,width=270):
        attrs=e.get("attributes",{})
        keys=fields if fields is not None else [k for k in attrs if k not in {'reference_row','reference_column'}]
        result=[]
        for k in keys:
            if k in attrs:
                self.attrs[e["id"]].add(k)
                value=attrs[k]
                if k=="attributes" and isinstance(value,list):
                    primary=attrs.get("key",attrs.get("primary_key",[]));primary=primary if isinstance(primary,list) else [primary]
                    for item in value:
                        if isinstance(item,dict):
                            name=str(item.get("name",item.get("id","未命名属性")));line=("PK " if name in primary or item.get('key')=='PK' else 'FK ' if item.get('key')=='FK' else "")+name+" : "+str(item.get("datatype",item.get("type","类型待确认")))
                            required=item.get('required');optional=item.get('optional')
                            conflict=isinstance(required,bool) and isinstance(optional,bool) and required==optional
                            if conflict:
                                problem={'code':'attribute-optionality-conflict','id':e['id'],'attribute':name}
                                if problem not in self.errors:self.errors.append(problem)
                            elif not isinstance(required,bool) and isinstance(optional,bool):required=not optional
                            line+=" · "+('可选性冲突' if conflict else "必填" if required is True else "可选" if required is False else "可选性待确认")
                            other={kk:vv for kk,vv in item.items() if kk not in {"name","id","datatype","type","required"}}
                            if other:line+=" · "+fmt(other)
                        else:line=fmt(item)
                        result+=wrap(line,max(12,int((width-24)/6.5)))
                else:result+=wrap(k+": "+fmt(value),max(12,int((width-24)/6.5)))
        return result
    def card_height(self,e,width=270,fields=None):
        units=max(12,int((width-24)/8.5))
        return max(90,34+24*len(wrap(e["name"],units))+18*len(wrap(e["type"]+" / "+e["id"],units))+20*len(self.entity_lines(e,fields,width)))
    def card(self,e,x,y,w=270,h=None,fill="#e9f0f7",fields=None,radius=6):
        units=max(12,int((w-24)/8.5));name=wrap(e["name"],units);body=self.entity_lines(e,fields,w);identity=wrap(e["type"]+" / "+e["id"],units)
        h=h or max(90,34+24*len(name)+18*len(identity)+20*len(body))
        self.parts.append(f'<g data-entity-id="{esc(e["id"])}">')
        self.rect(x,y,w,h,fill,radius=radius);yy=y+28;ink=foreground(fill)
        for line in name:self.text(x+12,yy,line,17,ink);yy+=24
        for line in identity:self.text(x+12,yy,line,11,ink);yy+=18
        for line in body:self.text(x+12,yy,line,13,ink);yy+=20
        self.parts.append("</g>");self.positions[e["id"]]=(x,y,w,h);self.entity_ids.add(e["id"])
        return h
    def edge(self,r,entities,card=True):
        a=self.positions.get(r["source"]);b=self.positions.get(r["target"])
        if not a or not b:
            self.errors.append({"code":"edge-endpoint-not-placed","id":r["id"]});return
        ax,ay,aw,ah=a;bx,by,bw,bh=b
        if bx>=ax+aw:x1,y1,x2,y2=ax+aw,ay+ah/2,bx,by+bh/2
        elif ax>=bx+bw:x1,y1,x2,y2=ax,ay+ah/2,bx+bw,by+bh/2
        elif by>=ay+ah:x1,y1,x2,y2=ax+aw/2,ay+ah,bx+bw/2,by
        elif ay>=by+bh:x1,y1,x2,y2=ax+aw/2,ay,bx+bw/2,by+bh
        else:x1,y1,x2,y2=ax+aw/2,ay+ah,bx+bw/2,by
        relation_type=r.get("type","")
        label=r.get("label",relation_type)+" ["+relation_type+"]"
        if r.get("codes"):label+=" ["+",".join(r["codes"])+"]"
        if relation_type in {"uses_information","information_used_by","uses"}:color="#2869ad"
        elif relation_type in {"modifies_information","modifies"}:color="#b83f4b"
        else:color="#46647e"
        if r.get("attributes",{}).get("polarity"):label+=" ("+str(r["attributes"]["polarity"])+")"
        if len(label)>12:
            self.edge_register.append(r)
            label="["+str(len(self.edge_register))+"]"+(" "+str(r["attributes"]["polarity"]) if r.get("attributes",{}).get("polarity") else "")
        undirected={"association","information_association","data_association","logical_association","collaborates_with","aggregation","composition","generalization"}
        routed=False;points=[(x1,y1),(x2,y2)]
        if self.network_routing:
            points=orthogonal_route(self,r)
            if points:
                x1,y1=points[0];x2,y2=points[-1]
                path="M"+" L".join(str(round(x,2))+" "+str(round(y,2)) for x,y in points)
                dash=' stroke-dasharray="7 4"' if r.get("certainty")!="confirmed" else ""
                marker=' marker-end="url(#arrow)"' if relation_type not in undirected|HOLLOW_HEAD else ""
                self.parts.append(f'<path data-relationship-id="{esc(r["id"])}" d="{path}" fill="none" stroke="{color}" stroke-width="1.8"{dash}{marker}/>')
                if marker:self.reserve_arrowhead(points)
                segments=list(zip(points,points[1:]));self.queue_badge(points,label,color,r["id"])
                self.relation_ids.add(r["id"]);routed=True
                self.occupied_segments.extend(segments)
            else:self.errors.append({"code":"no-clear-edge-route","id":r["id"]})
        if not routed:
            points=[(x1,y1),(x2,y2)]
            self.line(x1,y1,x2,y2,label,r,r.get("certainty")!="confirmed",color,relation_type not in undirected|HOLLOW_HEAD,r.get("_render_bend",0))
        if relation_type in {"aggregation","composition"}:
            fill=color if relation_type=="composition" else "white"
            vx=points[1][0]-points[0][0];vy=points[1][1]-points[0][1];length=max(1,math.hypot(vx,vy));ux,uy=vx/length,vy/length
            diamond=[(x1,y1),(x1+9*ux-5*uy,y1+9*uy+5*ux),(x1+18*ux,y1+18*uy),(x1+9*ux+5*uy,y1+9*uy-5*ux)]
            self.parts.append('<polygon points="'+' '.join(str(x)+','+str(y) for x,y in diamond)+f'" fill="{fill}" stroke="{color}"/>')
            self.endpoint_glyph_boxes.append((min(x for x,y in diamond)-1,min(y for x,y in diamond)-1,
                                              max(x for x,y in diamond)+1,max(y for x,y in diamond)+1))
        elif relation_type in HOLLOW_HEAD:
            vx=points[-1][0]-points[-2][0];vy=points[-1][1]-points[-2][1];length=max(1,math.hypot(vx,vy));ux,uy=vx/length,vy/length
            triangle=[(x2,y2),(x2-14*ux+7*uy,y2-14*uy-7*ux),(x2-14*ux-7*uy,y2-14*uy+7*ux)]
            self.parts.append('<polygon points="'+' '.join(str(x)+','+str(y) for x,y in triangle)+f'" fill="white" stroke="{color}"/>')
            self.endpoint_glyph_boxes.append((min(x for x,y in triangle)-1,min(y for x,y in triangle)-1,
                                              max(x for x,y in triangle)+1,max(y for x,y in triangle)+1))
        if card and r.get("cardinality"):
            c=r["cardinality"]
            self.text(max(15,x1+(8 if x1>=ax+aw else -38 if x1<=ax else 8)),y1-9,cardinality(c.get("source")),13)
            self.text(max(15,x2+(8 if x2>=bx+bw else -38 if x2<=bx else 8)),y2-9,cardinality(c.get("target")),13)
    def finish(self,entities,relations):
        self.flush_badges()
        # Every selected relationship is inspectable even where a specialized spatial
        # view must leave its extra semantic projection to an explicitly labelled register.
        missing_e=[e["id"] for e in entities if e["id"] not in self.entity_ids]
        missing_r=[r["id"] for r in relations if r["id"] not in self.relation_ids]
        footer=self.height+30
        byid={e["id"]:e for e in entities}
        ledger={"entities":[],"relationships":[]}
        separate=bool(self.profile.get('template',{}).get('separate_detail_ledger') or self.profile.get('template',{}).get('source_topology') or getattr(self,'baseline_figure_height',self.height)>4200)
        for e in entities:
            remaining={k:v for k,v in e.get('attributes',{}).items() if k not in self.attrs[e['id']]}
            metadata={k:e[k] for k in ['measurements','state_id','concept_id','version','scope_id','approval_status','implementation_status'] if k in e}
            if remaining or metadata:
                payload={**remaining,**metadata}
                self.attrs[e['id']].update(remaining)
                self.attrs[e['id']].update(metadata)
                if separate:ledger["entities"].append({"id":e["id"],"fields":payload})
                else:footer+=self.text(30,footer,'补充对象字段（同一 ID；不替代主视图） '+e['id']+'：'+fmt(payload),13,units=140)+9
        if self.edge_register:
            if separate:
                footer+=self.text(30,footer,"连线编号、完整字段与分页见伴随明细（可点击）；主图保留结构。",16)+8
            else:
                footer+=self.text(30,footer,"连线标号与关系语义：",16)+8
            for i,r in enumerate(self.edge_register):
                arrow=" ⇄ " if r['type'] in self.profile.get('symmetric_relationship_types',[]) else " → "
                value="["+str(i+1)+"] "+byid.get(r["source"],{}).get("name",r["source"])+arrow+byid.get(r["target"],{}).get("name",r["target"])+"："+r["label"]+" ["+r["type"]+"]"
                if r.get("attributes"):value+=" · "+fmt(r["attributes"])
                if 'codes' in r:value+=" · 单元代码 "+fmt(r["codes"])
                if r.get("cardinality"):value+=" · 端点基数 "+fmt(r["cardinality"])
                self.relationship_attrs[r['id']].update(r.get('attributes',{}))
                if 'codes' in r:self.relationship_attrs[r['id']].add('codes')
                if r.get('cardinality'):self.relationship_attrs[r['id']].update('cardinality.'+k for k in r['cardinality'])
                if separate:
                    ledger["relationships"].append({"id":r["id"],"index":i+1,"text":value})
                else:
                    self.parts.append(f'<g data-relationship-id="{esc(r["id"])}">')
                    footer+=self.text(30,footer,value,13,units=140)+9
                    self.parts.append('</g>')
        registered={r['id'] for r in self.edge_register}
        for r in relations:
            if r['id'] not in registered and r['id'] in self.relation_ids and (r.get('attributes') or any(k in r for k in ['codes','cardinality'])):
                arrow=' ⇄ ' if r['type'] in self.profile.get('symmetric_relationship_types',[]) else ' → '
                value='关系属性 '+r['id']+' · '+r['source']+arrow+r['target']+' ['+r['type']+']：'+fmt({k:r[k] for k in ['attributes','codes','cardinality'] if k in r})
                self.relationship_attrs[r['id']].update(r.get('attributes',{}))
                if 'codes' in r:self.relationship_attrs[r['id']].add('codes')
                if r.get('cardinality'):self.relationship_attrs[r['id']].update('cardinality.'+k for k in r['cardinality'])
                if separate:ledger["relationships"].append({"id":r["id"],"text":value})
                else:footer+=self.text(30,footer,value,13,units=140)+9
        if separate:
            self.parts.append('<a href="'+esc(self.view['id']+'.details.html')+'"><text x="30" y="'+str(footer+20)+'" font-size="16" fill="#145a90">打开分组明细与完整关系记录</text></a>')
            footer+=52
        self.detail_ledger=ledger if separate else None
        if separate:
            for r in relations:self.relationship_attrs[r['id']].update(r.get('attributes',{}))
        for r in relations:
            required=self.profile.get('required_relationship_attributes',{})
            for field in required.get(r['type'],[])+required.get('*',[]):
                if field not in r.get('attributes',{}):self.errors.append({'code':'missing-relationship-attribute','id':r['id'],'attribute':field})
                elif field not in self.relationship_attrs[r['id']]:self.errors.append({'code':'relationship-attribute-not-expressed','id':r['id'],'attribute':field})
        footer+=self.text(30,footer,"图例："+self.view.get("legend","未提供"),14,units=140)+12
        if self.warnings:
            for warning in self.warnings:footer+=self.text(30,footer,"提示："+fmt(warning),13,units=145)+8
        self.height=max(self.height,footer+20)
        title=self.view.get("title",self.profile.get("name",self.profile.get("id","架构视图")))
        status="虚构示例 / 候选草案" if self.view.get("_is_example") else "项目视图 / 状态与证据见共享模型"
        caption_width=getattr(self,'baseline_caption_width',self.width)
        titles=wrap(title,max(20,int((caption_width-60)/12)));captions=wrap(status+" · "+self.layout+"（项目布局，非官方图等价认证） · "+str(self.profile.get("id","")),max(20,int((caption_width-60)/7)))
        header="".join(f'<text x="30" y="{34+i*30}" font-size="23">{esc(line)}</text>' for i,line in enumerate(titles))
        header+="".join(f'<text x="30" y="{34+len(titles)*30+i*22}" font-size="14">{esc(line)}</text>' for i,line in enumerate(captions))
        extra=max(0,(len(titles)-1)*30+(len(captions)-1)*22);self.height+=extra
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{int(self.width)}" height="{int(self.height)}" viewBox="0 0 {int(self.width)} {int(self.height)}" role="img"><title>{esc(title)}</title><desc>{esc(self.view.get("legend",""))}</desc><defs><style>text{{font-family:TogafCJK,"Noto Sans SC",sans-serif}}</style><marker id="arrow" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="none" stroke="#46647e"/></marker></defs><rect width="100%" height="100%" fill="white"/>{header}<g transform="translate(0,{extra})">'+"".join(self.parts)+"</g></svg>"
        report={"renderer_version":VERSION,"renderer":self.profile.get("renderer"),"errors":self.errors,"warnings":self.warnings,
                    "represented_entity_ids":sorted(self.entity_ids),"represented_relationship_ids":sorted(self.relation_ids),
                    "unrepresented_entity_ids":missing_e,"unrepresented_relationship_ids":missing_r,
                    "represented_attributes":{k:sorted(v) for k,v in self.attrs.items()},
                    "represented_relationship_attributes":{k:sorted(v) for k,v in self.relationship_attrs.items()},
                    "source_template_status":self.profile.get("definition_status","not-independently-verified"),
                    "review_status":"draft-with-gaps" if self.errors or missing_e or missing_r else "generated-awaiting-review"}
        if separate:
            report['detail_ledger']=self.detail_ledger
            report['main_figure_excludes_attribute_footer']=True
            from expression_details import companion, locations
            report['companion_file']=self.view['id']+'.details.html'
            report['companion_html']=companion(entities,relations,title)
            report['expression_locations']=locations(svg,report['companion_html'],report['companion_file'])
            report['coverage_contract']='expression-locations/2'
            report['represented_entity_ids']=sorted(report['expression_locations']['entities'])
            report['represented_relationship_ids']=sorted(report['expression_locations']['relationships'])
            report['unrepresented_entity_ids']=sorted(set(e['id'] for e in entities)-set(report['represented_entity_ids']))
            report['unrepresented_relationship_ids']=sorted(set(r['id'] for r in relations)-set(report['represented_relationship_ids']))
            report['review_status']='draft-with-gaps' if self.errors or report['unrepresented_entity_ids'] or report['unrepresented_relationship_ids'] else 'generated-awaiting-review'
        return svg,report

def orthogonal_route(d,r):
    """Visibility-grid routing around node rectangles, with a separate bidirectional lane."""
    rects=list(d.positions.values());a=d.positions[r["source"]];b=d.positions[r["target"]]
    if r["source"]==r["target"]:
        x,y,w,h=a;points=[(x+w,y+h*.3),(x+w+24,y+h*.3),(x+w+24,y+h*.7),(x+w,y+h*.7)]
        d.width=max(d.width,x+w+60);return points
    offset=r.get("_port_offset",12 if r["source"]<r["target"] else -12)
    def ports(box,endpoint):
        port_offset=getattr(d,"endpoint_port_offsets",{}).get((r.get("id"),endpoint),offset)
        x,y,w,h=box;cx=x+w/2+max(-w/3,min(w/3,port_offset));cy=y+h/2+max(-h/3,min(h/3,port_offset))
        return [((x,cy),(x-18,cy)),((x+w,cy),(x+w+18,cy)),((cx,y),(cx,y-18)),((cx,y+h),(cx,y+h+18))]
    # Containing regions are legitimate to cross when they contain an endpoint;
    # unrelated child cards remain obstacles. A nested endpoint must not be
    # trapped inside its ancestor rectangle.
    def contains(box,point):
        x,y,w,h=box;return x<point[0]<x+w and y<point[1]<y+h
    centers=[(box[0]+box[2]/2,box[1]+box[3]/2) for box in [a,b]]
    def encloses(outer,inner):
        return (outer!=inner and contains(outer,(inner[0],inner[1]))
                and contains(outer,(inner[0]+inner[2],inner[1]+inner[3])))
    # A container may itself be the target/source of an independent relation.
    # Its boundary is an endpoint, not a solid obstacle trapping its child.
    rects=[box for box in rects if not any(encloses(box,other) for other in (a,b))
           and (box in [a,b] or not any(contains(box,c) for c in centers))]
    starts=ports(a,"source");ends=ports(b,"target");obstacles=[(x-8,y-8,x+w+8,y+h+8) for x,y,w,h in rects]
    def clear(p,q):
        if p[1]==q[1]:return not any(top<p[1]<bottom and max(min(p[0],q[0]),left)<min(max(p[0],q[0]),right) for left,top,right,bottom in obstacles)
        return not any(left<p[0]<right and max(min(p[1],q[1]),top)<min(max(p[1],q[1]),bottom) for left,top,right,bottom in obstacles)
    if len(rects)>64:
        # Avoid the O(n^2) Cartesian grid (and O(n) obstacle scan per node)
        # when an exact rectilinear route already exists. Validate against ALL
        # obstacles; do not replace real connectors with a relationship ledger.
        candidates=[]
        for actual,p in starts:
            for target,q in ends:
                for middle in ([(p[0],q[1])],[(q[0],p[1])]):
                    route=[p]+middle+[q]
                    if all(clear(u,v) for u,v in zip(route,route[1:])):
                        points=[actual]+route+[target]
                        # Endpoint port stubs may cross only their own padded
                        # endpoint; unrelated obstacles must still be avoided.
                        unrelated=[box for box,rect in zip(obstacles,rects) if rect not in (a,b)]
                        def stub_free(u,v):
                            if u[1]==v[1]:return not any(t<u[1]<bt and max(min(u[0],v[0]),l)<min(max(u[0],v[0]),rt) for l,t,rt,bt in unrelated)
                            return not any(l<u[0]<rt and max(min(u[1],v[1]),t)<min(max(u[1],v[1]),bt) for l,t,rt,bt in unrelated)
                        if stub_free(actual,p) and stub_free(q,target):
                            overlap=sum(math.dist(u,v) for u,v in zip(route,route[1:])
                                        if any(u[0]==v[0]==s[0]==t[0] or u[1]==v[1]==s[1]==t[1] for s,t in d.occupied_segments))
                            candidates.append((sum(math.dist(u,v) for u,v in zip(points,points[1:]))+overlap*4,points))
        if candidates:
            points=min(candidates,key=lambda item:item[0])[1]
            for x,y in points:d.width=max(d.width,x+30);d.height=max(d.height,y+30)
            return points
    xs={12.,float(d.width+35)};ys={90.,float(d.height+35)}
    for left,top,right,bottom in obstacles:
        xs.update(x for x in [left-10,left-26,left-42,right+10,right+26,right+42] if x>=12)
        ys.update(y for y in [top-10,top-26,top-42,bottom+10,bottom+26,bottom+42] if y>=90)
    for actual,outside in starts+ends:xs.add(outside[0]);ys.add(outside[1])
    xs=sorted(xs);ys=sorted(ys);xindex={x:i for i,x in enumerate(xs)};yindex={y:i for i,y in enumerate(ys)}
    def free(p):return not any(left<p[0]<right and top<p[1]<bottom for left,top,right,bottom in obstacles)
    free_nodes={(ix,iy) for ix,x in enumerate(xs) for iy,y in enumerate(ys) if free((x,y))}
    def clear(p,q):
        if p[1]==q[1]:return not any(top<p[1]<bottom and max(min(p[0],q[0]),left)<min(max(p[0],q[0]),right) for left,top,right,bottom in obstacles)
        return not any(left<p[0]<right and max(min(p[1],q[1]),top)<min(max(p[1],q[1]),bottom) for left,top,right,bottom in obstacles)
    destinations={(xindex[out[0]],yindex[out[1]]):actual for actual,out in ends if free(out)}
    queue=[];costs={};previous={};origins={}
    for actual,out in starts:
        node=(xindex[out[0]],yindex[out[1]])
        if node not in free_nodes:continue
        state=(node,0);costs[state]=0;origins[state]=actual;heapq.heappush(queue,(0,state))
    final=None
    while queue:
        cost,state=heapq.heappop(queue)
        if cost!=costs.get(state):continue
        node,direction=state;ix,iy=node
        if node in destinations:final=state;break
        for nx,ny,nd in [(ix-1,iy,1),(ix+1,iy,1),(ix,iy-1,2),(ix,iy+1,2)]:
            target=(nx,ny)
            if target not in free_nodes:continue
            p=(xs[ix],ys[iy]);q=(xs[nx],ys[ny])
            if not clear(p,q):continue
            overlap=0
            for u,v in d.occupied_segments:
                if p[0]==q[0]==u[0]==v[0]:overlap+=max(0,min(max(p[1],q[1]),max(u[1],v[1]))-max(min(p[1],q[1]),min(u[1],v[1])))
                elif p[1]==q[1]==u[1]==v[1]:overlap+=max(0,min(max(p[0],q[0]),max(u[0],v[0]))-max(min(p[0],q[0]),min(u[0],v[0])))
            nc=cost+abs(p[0]-q[0])+abs(p[1]-q[1])+overlap*4+(30 if direction and nd!=direction else 0)
            ns=(target,nd)
            if nc<costs.get(ns,float("inf")):
                costs[ns]=nc;previous[ns]=state;origins[ns]=origins[state];heapq.heappush(queue,(nc,ns))
    if final is None:return None
    points=[];state=final
    while True:
        (ix,iy),_=state;points.append((xs[ix],ys[iy]))
        if state not in previous:break
        state=previous[state]
    points.reverse();points=[origins[final]]+points+[destinations[final[0]]]
    simplified=[]
    for p in points:
        if len(simplified)>1:
            a1,a2=simplified[-2:]
            if (a1[0]==a2[0]==p[0]) or (a1[1]==a2[1]==p[1]):simplified[-1]=p;continue
        simplified.append(p)
    for x,y in simplified:d.width=max(d.width,x+30);d.height=max(d.height,y+30)
    return simplified

def grid(d,es,columns=3,start_y=110,groups=False,gap=35,start_x=30):
    y=start_y;colw=320
    for start in range(0,len(es),columns):
        row=es[start:start+columns];heights=[d.card_height(e,colw) for e in row];rh=max(heights or [80])
        for i,e in enumerate(row):d.card(e,start_x+i*(colw+gap),y,colw,rh)
        y+=rh+gap
    return y

def nested(d,es,rs):
    byid={e["id"]:e for e in es};children=defaultdict(list);hierarchy=[];parents={}
    hierarchy_types=HIERARCHY|set(d.profile.get('hierarchy_relationship_types',[]))
    conflicts=[]
    for r in rs:
        if r["type"] in hierarchy_types and r["source"] in byid and r["target"] in byid:
            source,target=r['source'],r['target'];hierarchy.append(r)
            if target in parents and parents[target]!=source:
                conflicts.append({'code':'hierarchy-multiple-parents','id':target,
                    'parents':[parents[target],source],
                    'message':'此嵌套视图不能把同一ID画进多个父框；请分视图或使用显式引用，不据此禁止主模型DAG。'})
            parents[target]=source
            bands=d.profile.get('template',{}).get('bands',[])
            if bands and byid[source].get('attributes',{}).get('category')!=byid[target].get('attributes',{}).get('category'):
                conflicts.append({'code':'classification-parent-band-conflict','id':r['id'],
                                  'message':'子项分类与父框分类不一致；请拆分关注点视图，不能用嵌套隐去分类。'})
            if target not in children[source]:children[source].append(target)
            a=byid[source].get('attributes',{}).get('level');b=byid[target].get('attributes',{}).get('level')
            if d.profile.get('id')=='capability-decomposition' and type(a) is int and type(b) is int and b<=a:
                conflicts.append({'code':'hierarchy-level-order','id':r['id'],
                    'message':'能力分解子项层级须深于父项；允许视图跳级但不能以嵌套掩盖倒置/相同层级。'})
    # Inspect every component, including cycles disconnected from a valid root.
    state={}
    for start in byid:
        if state.get(start)==2:continue
        stack=[(start,False)]
        while stack:
            eid,exiting=stack.pop()
            if exiting:state[eid]=2;continue
            if state.get(eid)==1:
                conflicts.append({'code':'hierarchy-cycle','id':eid,'message':'嵌套关系存在循环，无法确定有限包含层级。'});continue
            if state.get(eid)==2:continue
            state[eid]=1;stack.append((eid,True))
            stack.extend((child,False) for child in reversed(children[eid]))
    if conflicts:
        d.errors.extend(conflicts)
        return
    for e in es:
        p=e.get("attributes",{}).get("parent_id")
        if p in byid and e["id"] not in children[p]:
            d.errors.append({'code':'parent-without-explicit-hierarchy','id':e['id'],'parent_id':p})
    childids={i for vals in children.values() for i in vals};roots=[e for e in es if e["id"] not in childids]
    if not roots and es:
        d.errors.append({"code":"hierarchy-cycle","message":"没有可定位的根节点"});roots=es;children.clear()
    active=set()
    def size(eid,w):
        if w<160:
            d.errors.append({"code":"hierarchy-too-deep","id":eid,"message":"需要分图，不能继续压缩层级"});return 120
        if eid in active:d.errors.append({"code":"hierarchy-cycle","id":eid});return 120
        active.add(eid);e=byid[eid];base=d.card_height(e,w);h=base
        for child in children[eid]:h+=size(child,w-36)+20
        active.remove(eid);return h+(20 if children[eid] else 0)
    def draw(eid,x,y,w):
        e=byid[eid];h=size(eid,w);d.card(e,x,y,w,h,PALETTE[min(len(active),len(PALETTE)-1)])
        active.add(eid);cy=y+d.card_height(e,w)+10
        for child in children[eid]:
            if child in active:continue
            ch=size(child,w-36);draw(child,x+18,cy,w-36);cy+=ch+20
        active.remove(eid)
    cats=defaultdict(list)
    for e in roots:cats[e.get("attributes",{}).get("category",d.profile.get("template",{}).get("default_group_label","未分类"))].append(e)
    bands=d.profile.get('template',{}).get('bands',[])
    for e in es:
        category=e.get('attributes',{}).get('category')
        if bands and category not in bands:
            d.errors.append({'code':'unknown-classification-band','id':e['id'],'category':category})
    ordered=list(dict.fromkeys(bands+list(cats)))
    y=110
    for cat in ordered:
        items=cats[cat]
        d.rect(25,y,1040,38,"#314f68");d.text(40,y+25,cat,17,"white");y+=55
        if not items:
            d.text(40,y+20,'未记录能力；缺失不表示不适用。带内位置不表示顺序。',14)
            d.warnings.append('分类带未记录能力：'+str(cat));y+=60;continue
        columns=min(len(items),int(d.profile.get("template",{}).get("columns",3 if d.layout=="reference" else 2)))
        w=(1005-22*(columns-1))/max(1,columns)
        for start in range(0,len(items),columns):
            row=items[start:start+columns];heights=[size(e["id"],w) for e in row]
            for i,e in enumerate(row):draw(e["id"],40+i*(w+22),y,w)
            y+=max(heights)+25
    if hierarchy:
        d.text(30,d.height+20,d.profile.get("template",{}).get("hierarchy_caption","嵌套表达所列包含／分解关系；关系类型分别保留，不相互替代："),14)
        for r in hierarchy:
            d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">')
            d.text(30,d.height+8,byid[r["source"]]["name"]+" → "+byid[r["target"]]["name"]+"："+r["label"]+" ["+r["type"]+"]",13,units=135)
            d.parts.append("</g>");d.relation_ids.add(r["id"])
    d.network_routing=True
    for r in rs:
        if r not in hierarchy:d.edge(r,byid)

def grouped_bands(d,es,rs):
    """Source-shaped rows of independent groups, each with nested child cards.

    Row/column placement is presentation data. Only explicit decomposition or
    visual-containment edges establish parentage. Business roles remain roles.
    """
    byid={e['id']:e for e in es};children=defaultdict(list);parent={};hierarchy=[]
    for r in rs:
        if r['type'] in {'decomposes','visually_contains'}:
            if r['target'] in parent:
                d.errors.append({'code':'multiple-band-parents','id':r['target']});continue
            parent[r['target']]=r['source'];children[r['source']].append(r['target']);hierarchy.append(r)
    roots=[e for e in es if e['id'] not in parent]
    if not roots and es:d.errors.append({'code':'band-hierarchy-cycle'});return
    rows=defaultdict(list)
    for i,e in enumerate(roots):
        key=e.get('attributes',{}).get('reference_row',i) if d.layout=='reference' else i//2
        rows[key].append(e)
    y=110
    def dimensions(e,w,path=()):
        if e['id'] in path:
            d.errors.append({'code':'band-hierarchy-cycle','id':e['id']});return 100,1
        cs=children[e['id']];cols=min(len(cs),3 if w>=900 else 2 if w>=550 else 1) or 1
        cw=(w-36-18*(cols-1))/cols;base=d.card_height(e,w)+18
        for start in range(0,len(cs),cols):
            base+=max(dimensions(byid[c],cw,path+(e['id'],))[0] for c in cs[start:start+cols])+18
        return base+12,cols
    def draw(e,x,y,w,path=()):
        if e['id'] in path:return
        h,cols=dimensions(e,w,path);d.card(e,x,y,w,h,'#f6f4cc' if e['type']=='function' else '#e7edf2')
        cs=children[e['id']];cw=(w-36-18*(cols-1))/cols;cy=y+d.card_height(e,w)+18
        if cs:d.positions['_band_header_'+e['id']]=(x,y,w,d.card_height(e,w))
        for start in range(0,len(cs),cols):
            chunk=cs[start:start+cols];heights=[dimensions(byid[c],cw,path+(e['id'],))[0] for c in chunk]
            for i,c in enumerate(chunk):draw(byid[c],x+18+i*(cw+18),cy,cw,path+(e['id'],))
            cy+=max(heights)+18
    for key,items in sorted(rows.items(),key=lambda kv:str(kv[0])):
        items.sort(key=lambda e:e.get('attributes',{}).get('reference_column',0))
        # Long labels increase group/card height; no semantic content is dropped.
        w=(1500-24*(len(items)-1))/len(items);hs=[dimensions(e,w)[0] for e in items]
        for i,e in enumerate(items):draw(e,30+i*(w+24),y,w)
        y+=max(hs)+40
    for r in hierarchy:
        d.relation_ids.add(r['id']);d.parts.append(f'<g data-relationship-id="{esc(r["id"])}"/>')
        d.edge_register.append(r)
    d.network_routing=True
    for r in rs:
        if r not in hierarchy:d.edge(r,byid)

    for key in list(d.positions):
        if key.startswith('_band_header_'):del d.positions[key]

def network(d,es,rs):
    if d.profile.get('template',{}).get('source_topology'):
        from source_topology_render import render_source_topology
        return render_source_topology(d,es,rs)
    positions=d.profile.get("template",{}).get("positions",{}) if d.layout=="reference" else {}
    if positions:
        used=set()
        for e in es:
            pos=positions.get(e["id"],positions.get(e["type"]))
            if pos:
                d.card(e,float(pos[0]),float(pos[1])+100,float(pos[2]) if len(pos)>2 else 300);used.add(e["id"])
        grid(d,[e for e in es if e["id"] not in used],3,d.height+30)
    elif d.layout=="adaptive" and len(es)>64:
        # A radius proportional to n wastes O(n^2) canvas area. A compact
        # grid keeps every node and explicit edge at its original font size.
        columns=math.ceil(math.sqrt(len(es)))
        grid(d,es,columns,gap=180,start_x=80)
    elif d.layout=="adaptive" and len(es)>2:
        w=320;maxh=max(d.card_height(e,w) for e in es);radius=max(330,len(es)*90)
        cx=radius+w/2+50;cy=radius+maxh/2+110
        for i,e in enumerate(es):
            angle=-math.pi/2+i*2*math.pi/len(es)
            x=cx+radius*math.cos(angle)-w/2;y=cy+radius*math.sin(angle)-maxh/2
            d.card(e,x,y,w,maxh)
    else:grid(d,es,2 if d.layout=="reference" else 3,gap=180,start_x=80)
    byid={e["id"]:e for e in es}
    d.network_routing=True
    pairs={(r["source"],r["target"]) for r in rs}
    for index,r in enumerate(rs):
        r={**r,"_port_offset":((index%7)-3)*9}
        if (r["target"],r["source"]) in pairs:r={**r,"_render_bend":55}
        d.edge(r,byid)

def evaluation(d,item):
    parsed=parse_evaluation(item,d.profile.get('template',{}),getattr(d,'scales',{}))
    d.errors.extend(parsed['errors']);d.warnings.extend(parsed['warnings'])
    return parsed

def evaluation_caption(parsed):
    return parsed['label']+' · 量表 '+fmt(parsed['scale'] or parsed['scale_id'] or '未定义')+' · 颜色 '+fmt(parsed['colors'])

def stage_capability_heatmap(d,es,rs):
    """Actual stage columns × capability rows. Missing links never imply zero."""
    stages=[e for e in es if e['type'] in STAGE_TYPES]
    caps=[e for e in es if e['type']=='capability']
    d.errors.extend(stage_capability_errors(es,rs))
    def order(e):
        value=e.get('attributes',{}).get('order',e.get('attributes',{}).get('ordinal'))
        return value if type(value) in {int,float} else float('inf')
    stages.sort(key=lambda e:(order(e),e['id']))
    if not stages or not caps:
        d.errors.append({'code':'missing-heatmap-axes'});grid(d,es);return
    if any(not any(k in e.get('attributes',{}) for k in ['order','ordinal']) for e in stages):
        d.warnings.append('阶段次序未完整记录；列位置只用于排版，不推断业务顺序。')
    d.text(30,110,'阶段 × 能力；空白／未记录使能关系≠不存在；共享评价不冒充阶段专属评价。',16,units=130)
    cw=300 if d.layout=='reference' else 370;left=360;top=155
    hh=max(d.card_height(e,cw) for e in stages)
    for i,e in enumerate(stages):d.card(e,left+i*cw,top,cw-8,hh)
    cells=defaultdict(list)
    byid={e['id']:e for e in es}
    for r in rs:
        if r['type']=='enabled_by' and r['source'] in {s['id'] for s in stages} and r['target'] in {c['id'] for c in caps}:
            cells[(r['source'],r['target'])].append(r)
    y=top+hh+15
    for cap in caps:
        base=evaluation(d,cap)
        evaluations={}
        for stage in stages:
            links=cells[(stage['id'],cap['id'])]
            evaluations[stage['id']]=[(r,evaluation(d,r)) for r in links]
        cell_heights=[sum(22*len(wrap(evaluation_caption(p if p['observed'] else base),40))+10 for _,p in entries) for entries in evaluations.values()]
        rh=max(d.card_height(cap,310),80+max(cell_heights or [0]))
        d.card(cap,30,y,310,rh)
        for i,stage in enumerate(stages):
            x=left+i*cw;entries=evaluations[stage['id']]
            specific=[p for _,p in entries if p['observed']]
            if len(specific)>1:d.warnings.append('同一阶段×能力存在多个评价；使用中性色并逐项标明，不合成总分，请按维度切片：'+stage['id']+' / '+cap['id'])
            fill=specific[0]['fill'] if len(specific)==1 else base['fill'] if entries and not specific else '#edf0f3'
            d.parts.append(f'<g data-stage-id="{esc(stage["id"])}" data-capability-id="{esc(cap["id"])}">')
            d.rect(x,y,cw-8,rh,fill);cy=y+25
            if not entries:d.text(x+10,cy,'未记录使能关系（不着热力色）',13,units=40)
            for r,p in entries:
                d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">')
                label=('阶段专属评价：' if p['observed'] else '能力共享评价：')+evaluation_caption(p if p['observed'] else base)
                cy+=d.text(x+10,cy,label,13,foreground(fill),units=40)+10
                d.parts.append('</g>');d.relation_ids.add(r['id']);d.edge_register.append(r)
            d.parts.append('</g>')
        y+=rh+20
    remaining=[e for e in es if e['id'] not in d.entity_ids]
    if remaining:grid(d,remaining,2,y+25)
    for r in rs:
        if r['id'] not in d.relation_ids:
            d.relation_ids.add(r['id']);d.edge_register.append(r)
    d.text(30,d.height+25,'阶段先后与其他追溯关系见下方关系登记；位置不代替显式关系。紫色=未来不存在，不是零分。',14,units=140)

def heatmap(d,es,rs):
    if d.profile.get('id')=='value-stream-capability-heatmap' or d.profile.get('template',{}).get('heatmap_axes')=='stage-capability':
        stage_capability_heatmap(d,es,rs);return
    y=110;groups=defaultdict(list)
    for e in es:groups[e.get('attributes',{}).get('category','未分类')].append(e)
    columns=3 if d.layout=='reference' else 2;cw=315 if columns==3 else 490
    for name,items in groups.items():
        d.text(30,y+20,name,18);y+=40
        for start in range(0,len(items),columns):
            row=items[start:start+columns]
            parsed=[evaluation(d,e) for e in row]
            h=max(d.card_height(e,cw)+25+20*len(wrap(evaluation_caption(p),int(cw/7))) for e,p in zip(row,parsed))
            for i,(e,p) in enumerate(zip(row,parsed)):
                x=30+i*(cw+35);d.card(e,x,y,cw,h,p['fill'])
                d.text(x+12,y+d.card_height(e,cw)+10,evaluation_caption(p),13,foreground(p['fill']),units=int(cw/7))
            y+=h+35
    d.network_routing=True
    for r in rs:d.edge(r,{e['id']:e for e in es})
    d.text(30,d.height+25,'紫色 future-absent 表示未来尚不存在；未知保持中性，不是成熟度最低或已退役。',14,units=140)

def stage_map(d,es,rs):
    stages=[e for e in es if e["type"] in STAGE_TYPES]
    stages.sort(key=lambda e:(e.get("attributes",{}).get("ordinal",e.get("attributes",{}).get("order",999)),e["id"]))
    if not stages:
        d.errors.append({"code":"missing-stages","message":"阶段地图缺少价值流阶段"});network(d,es,rs);return
    byid={e["id"]:e for e in es};used=set();width=355 if d.layout=="reference" else 430;y=110
    if any(not any(k in e.get("attributes",{}) for k in ["ordinal","order"]) for e in stages):
        d.warnings.append("部分阶段没有显式次序；横向位置仅用于排版，不能据此确认业务先后。")
    components=defaultdict(list);component_edges=[];edge_positions={};stage_positions={}
    component_types={"contains","has_component","composed_of","has_part","instance_comprises"}
    for r in rs:
        if r["source"] in byid and byid[r["source"]]["type"] in {"capability_instance","business_capability_instance"} and r["type"] in component_types:
            if r["target"] not in components[r["source"]]:components[r["source"]].append(r["target"])
            component_edges.append(r)
    for e in es:
        parent=e.get("attributes",{}).get("instance_id",e.get("attributes",{}).get("parent_id"))
        if parent in byid and byid[parent]["type"] in {"capability_instance","business_capability_instance"} and e["id"] not in components[parent]:components[parent].append(e["id"])
    def component_height(eid,w,path=None):
        path=path or set()
        if eid in path:d.errors.append({"code":"instance-composition-cycle","id":eid});return 90
        if w<150:d.errors.append({"code":"instance-composition-too-deep","id":eid});return 90
        title_safe={**byid[eid],"name":"复用引用："+byid[eid]["name"]}
        return d.card_height(title_safe,w)+sum(component_height(c,w-24,path|{eid})+15 for c in components[eid])+15
    def draw_component(eid,x,yy,w,path=None):
        path=path or set()
        if eid in path:return
        displayed={**byid[eid],"name":"复用引用："+byid[eid]["name"]} if eid in used else byid[eid]
        d.card(displayed,x,yy,w,component_height(eid,w),"#efe5d4" if components[eid] else "#e8edf7");used.add(eid)
        cy=yy+d.card_height({**byid[eid],"name":"复用引用："+byid[eid]["name"]},w)+10
        for child in components[eid]:
            draw_component(child,x+12,cy,w-24,path|{eid});cy+=component_height(child,w-24,path|{eid})+15
            for edge in [r for r in component_edges if r["source"]==eid and r["target"]==child]:
                d.relation_ids.add(edge["id"])
                d.parts.append(f'<metadata data-relationship-id="{esc(edge["id"])}">{esc(edge["label"])} / {esc(edge["type"])}</metadata>')
    stream=[e for e in es if e["type"]=="value_stream"]
    for e in stream:y+=d.card(e,30,y,max(1030,len(stages)*width-25))+25;used.add(e["id"])
    for i,e in enumerate(stages):
        x=30+i*width;yy=y;yy+=d.card(e,x,yy,320,fill="#dcebdd")+35;used.add(e["id"]);stage_positions[e["id"]]=d.positions[e["id"]]
        linked=[]
        for r in rs:
            if r["source"]==e["id"] and r["target"] in byid and byid[r["target"]]["type"] not in STAGE_TYPES|{"value_stream"}:linked.append(r["target"])
            if r["target"]==e["id"] and r["source"] in byid and byid[r["source"]]["type"] not in STAGE_TYPES|{"value_stream"}:linked.append(r["source"])
        linked+= [o["id"] for o in es if o.get("attributes",{}).get("stage_id")==e["id"]]
        for eid in dict.fromkeys(linked):
            if eid in used:
                repeated={**byid[eid],"name":"复用引用："+byid[eid]["name"]}
                yy+=d.card(repeated,x,yy,320,fill="#edf0f6")+25
            else:
                draw_component(eid,x,yy,320);yy+=component_height(eid,320)+25
            for r in rs:
                if (r["source"]==e["id"] and r["target"]==eid) or (r["target"]==e["id"] and r["source"]==eid):edge_positions[r["id"]]=(e["id"],eid,d.positions[eid])
    remaining=[e for e in es if e["id"] not in used]
    if remaining:
        yy=d.height+30;d.text(30,yy,"组成／语境对象",18);grid(d,remaining,3,yy+30)
    if component_edges:
        d.text(30,d.height+25,"实例组成关系：",16)
        for edge in component_edges:
            d.text(30,d.height+10,byid[edge["source"]]["name"]+" → "+byid[edge["target"]]["name"]+"："+edge["label"]+" ["+edge["type"]+"]",13,units=140)
    d.network_routing=True
    for r in rs:
        if r["id"] in d.relation_ids:continue
        if r["id"] in edge_positions:
            stage_id,eid,pos=edge_positions[r["id"]];old=d.positions[eid];d.positions[eid]=pos;d.positions[stage_id]=stage_positions[stage_id]
            d.edge(r,byid);d.positions[eid]=old
        else:d.edge(r,byid)

BMC={"伙伴":(0,0,1,2),"关键伙伴":(0,0,1,2),"key_partners":(0,0,1,2),
     "活动":(1,0,1,1),"关键活动":(1,0,1,1),"key_activities":(1,0,1,1),
     "资源":(1,1,1,1),"关键资源":(1,1,1,1),"key_resources":(1,1,1,1),
     "价值":(2,0,1,2),"价值主张":(2,0,1,2),"value_propositions":(2,0,1,2),
     "关系":(3,0,1,1),"客户关系":(3,0,1,1),"customer_relationships":(3,0,1,1),
     "渠道":(3,1,1,1),"channels":(3,1,1,1),"客户":(4,0,1,2),"客户细分":(4,0,1,2),"customer_segments":(4,0,1,2),
     "成本":(0,2,2.5,1),"成本结构":(0,2,2.5,1),"cost_structure":(0,2,2.5,1),
     "收入":(2.5,2,2.5,1),"收入来源":(2.5,2,2.5,1),"revenue_streams":(2.5,2,2.5,1)}
CANVASES={
    "four-box":{"客户价值主张":(0,0,1,1),"利润公式":(1,0,1,1),"关键资源":(0,1,1,1),"关键流程":(1,1,1,1)},
    "environment":{"业务贡献":(0,0,3,1),"环境核算":(0,1,3,1),"架构措施":(0,2,3,1)},
    "customer-portrait":{"画像主体":(0,0,1,2),"目标":(1,0,1,1),"痛点":(2,0,1,1),"任务":(1,1,1,1),"需求":(2,1,1,1),"约束":(0,2,3,1)}
}

PERSONA_REGIONS=[("客户群体","segment",0,0,1,2),("目标","goals",1,0,1,1),("需求","needs",2,0,1,1),
                 ("行为","behaviors",1,1,1,1),("研究证据","evidence",2,1,1,1),("假设","assumptions",0,2,3,1)]

def persona_canvas(d,es,rs):
    """One persona per canvas: each region shows one declared attribute of the same entity."""
    regions=d.profile.get("template",{}).get("persona_regions",PERSONA_REGIONS);w=330;gap=8;y0=110
    d.text(30,92,"画像结构：每个区块是同一画像对象的一个属性；研究证据与假设分开。",14)
    for e in es:
        attrs=e.get("attributes",{});rowh=150
        for label,field,col,row,span,rows in regions:
            if field in attrs:
                lines=len(wrap(fmt(attrs[field]),max(12,int((span*(w+gap)-44)/7.2))))
                if field=="segment":lines+=len(wrap(e["name"],int((w-24)/8)))+len(wrap(e["type"]+" / "+e["id"],int((w-24)/6.5)))+1
                rowh=max(rowh,math.ceil((lines*23+70)/rows))
        d.parts.append(f'<g data-entity-id="{esc(e["id"])}">')
        for label,field,col,row,span,rows in regions:
            x=30+col*(w+gap);y=y0+row*(rowh+gap);ww=span*(w+gap)-gap;hh=rows*(rowh+gap)-gap
            d.rect(x,y,ww,hh,"#f6f8fa");d.text(x+12,y+26,label,15);ty=y+52
            if field=="segment":ty+=d.text(x+12,ty,e["name"],17,units=int((ww-24)/8));ty+=d.text(x+12,ty,e["type"]+" / "+e["id"],11,units=int((ww-24)/6.5))+8
            if field in attrs:
                d.text(x+12,ty,attrs[field],13,units=int((ww-24)/7.2));d.attrs[e["id"]].add(field)
            else:d.text(x+12,y+52,"未记录；不能解释为该客户群体没有此特征",13,units=int((ww-24)/7.2))
        d.parts.append("</g>");d.entity_ids.add(e["id"]);d.positions[e["id"]]=(30,y0,3*(w+gap)-gap,3*(rowh+gap)-gap)
        y0=d.height+40
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})

def canvas(d,es,rs):
    template=d.profile.get("template",{})
    kind=template.get("canvas_type") or {"persona":"persona","sustainability":"environment","business-model":"bmc"}.get(template.get("canvas_kind"))
    if not kind:
        pid=d.profile.get("id","")
        kind="environment" if "sustainability" in pid else "persona" if "persona" in pid else "four-box" if "four-box" in pid else "bmc"
    if kind=="persona":persona_canvas(d,es,rs);return
    regions=template.get("regions",BMC if kind=="bmc" else CANVASES.get(kind,{}))
    regions={label:tuple(pos) for label,pos in regions.items()}
    if not regions:
        d.errors.append({"code":"undefined-canvas-structure","canvas_type":kind});network(d,es,rs);return
    if not template.get('_suppress_caption'):d.text(30,92,"画布结构："+kind+"；区块含义依本视点定义。",14)
    cells=defaultdict(list);unknown=[]
    for e in es:
        block=e.get("attributes",{}).get("block",e.get("attributes",{}).get("canvas_block",""))
        if not block and kind=="customer-portrait" and len(es)==1:block="画像主体"
        pos=regions.get(block)
        if pos is None:unknown.append(e)
        else:cells[pos].append(e)
    w=270 if kind=="bmc" else 360;gap=8;rowh=180
    # The row unit grows until every region can contain all of its items.
    for (col,row,span,rows),items in cells.items():rowh=max(rowh,math.ceil((sum(d.card_height(e,w*span-24) for e in items)+28*len(items)+25)/rows))
    for col,row,span,rows in sorted(set(regions.values())):
        items=cells.get((col,row,span,rows),[])
        x=30+col*(w+gap);y=110+row*(rowh+gap);ww=span*(w+gap)-gap;hh=rows*(rowh+gap)-gap
        d.rect(x,y,ww,hh,"#f6f8fa");cy=y+14
        for e in items:cy+=d.card(e,x+10,cy,ww-20)+15
        if not items:
            block=next(k for k,v in regions.items() if v==(col,row,span,rows))
            d.text(x+12,y+28,block+"：未记录",15)
    missing=set(regions.values())-set(cells)
    if missing:d.warnings.append("画布存在未填区块；缺失不能解释为业务上不需要。")
    if unknown:
        d.errors.append({"code":"unknown-canvas-block","ids":[e["id"] for e in unknown]});grid(d,unknown,3,d.height+35)
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})

def environmental_review(d,es,rs):
    """G242 fig3-14 form structure: decisions, year/scope table, and five measures.

    Project values are supplied by three distinct model entities. Missing form
    sections are errors, never silently converted into generic cards.
    """
    d.width=1540
    if rs:d.errors.append({'code':'environment-form-unexpected-relationships','ids':[r['id'] for r in rs]})
    blocks={};expected={'业务贡献','环境核算','架构措施'}
    for e in es:
        block=e.get('attributes',{}).get('block')
        if block not in expected:d.errors.append({'code':'environment-form-unknown-block','id':e['id'],'block':block});continue
        if block in blocks:d.errors.append({'code':'environment-form-duplicate-block','id':e['id'],'block':block})
        else:blocks[block]=e
    for block in sorted(expected-set(blocks)):d.errors.append({'code':'environment-form-missing-block','block':block})
    d.text(30,94,'支撑组织气候转型 · IT 贡献（项目数据；来源图结构对照另审）',19)
    def group(e,x,y,w,h):
        d.parts.append(f'<g data-entity-id="{esc(e["id"])}">')
        d.positions[e['id']]=(x,y,w,h);d.entity_ids.add(e['id']);d.attrs[e['id']].add('block')
    def end():d.parts.append('</g>')
    def selection(x,y,w,selected,options=('YES','NO')):
        for j,option in enumerate(options):
            px=x+j*w/len(options);active=selected==option
            d.rect(px,y,w/len(options)-5,29,'#33465f' if active else '#ffffff','#697c90',2)
            d.text(px+w/len(options)/2-2,y+20,option,13,'#ffffff' if active else '#19364d','middle')
    d.rect(30,115,1470,34,'#e8e8e8','#e8e8e8',0)
    d.text(765,138,'环境业务正向影响：目标架构将帮助业务',18,anchor='middle')
    business=blocks.get('业务贡献')
    decision_labels={'measure':'度量环境影响','reduce':'降低业务环境影响','train':'培训业务了解环境与气候变化'}
    if business:
        group(business,30,155,1470,215);attrs=business.get('attributes',{});items=attrs.get('decisions')
        if not isinstance(items,list) or {x.get('id') for x in items if isinstance(x,dict)}!=set(decision_labels) or len(items)!=3:
            d.errors.append({'code':'environment-form-decisions-incomplete','id':business['id']});items=[]
        byid={x['id']:x for x in items}
        for j,(key,label) in enumerate(decision_labels.items()):
            x=30+j*490;item=byid.get(key,{})
            d.rect(x,155,470,215,'#f6f8fa');d.rect(x+10,166,450,54,'#a0a4aa','#a0a4aa',2)
            d.text(x+235,190,label,16,'#ffffff','middle',units=24)
            selected=item.get('selected','unknown')
            if selected not in {'YES','NO'}:d.errors.append({'code':'environment-form-decision-unknown','id':business['id'],'decision':key})
            selection(x+130,229,210,selected)
            d.rect(x+10,269,450,86,'#ffffff','#7fb86f',2)
            d.text(x+20,292,'说明：'+str(item.get('explanation','未记录')),13,units=53)
        d.attrs[business['id']].add('decisions');end()
    d.rect(30,384,1470,34,'#e8e8e8','#e8e8e8',0)
    d.text(40,407,'IT 碳足迹：目标架构将',18)
    carbon=blocks.get('环境核算')
    if carbon:
        group(carbon,30,422,1470,360);attrs=carbon.get('attributes',{});foot=attrs.get('carbon_footprint')
        if not isinstance(foot,dict):d.errors.append({'code':'environment-form-carbon-missing','id':carbon['id']});foot={}
        direction=foot.get('direction','unknown')
        if direction not in {'Increase','Decrease'}:d.errors.append({'code':'environment-form-direction-unknown','id':carbon['id']})
        selection(600,390,260,direction,('Increase','Decrease'))
        unit=foot.get('unit');years=foot.get('years')
        if unit!='kgCO2e' or not isinstance(years,list) or len(years)!=2:
            d.errors.append({'code':'environment-form-unit-or-years-missing','id':carbon['id']})
        d.text(40,445,'单位：'+str(unit or '未记录')+'；期间：'+(' / '.join(map(str,years)) if isinstance(years,list) else '未记录'),13)
        widths=[265,110,160,160,180,160,160,275];xs=[30]
        for width in widths:xs.append(xs[-1]+width)
        for x,w,label,fill in [(xs[0],widths[0],'项目','#e8eee6'),
                               (xs[1],widths[1],'Total','#e8eee6'),
                               (xs[2],sum(widths[2:5]),'第 1 年','#e8eee6'),
                               (xs[5],sum(widths[5:8]),'第 2 年','#fff1ca')]:
            d.rect(x,459,w,30,fill,'#aab4b8',0);d.text(x+w/2,480,label,13,anchor='middle')
        labels=['行标签','整行合计','Scope 2','Scope 3 服务','设备制造 Scope 3','Scope 2','Scope 3 服务','设备制造 Scope 3']
        for j,label in enumerate(labels):
            d.rect(xs[j],489,widths[j],46,'#e8eee6' if j<5 else '#fff1ca','#aab4b8',0)
            d.text(xs[j]+6,507,label,12,units=max(10,int(widths[j]/8)))
        rows=foot.get('rows')
        row_ids={'in':'IN：新增资源','out':'OUT：退役资源','balance':'BALANCE（IN−OUT）'}
        if not isinstance(rows,list) or {x.get('id') for x in rows if isinstance(x,dict)}!=set(row_ids) or len(rows)!=3:
            d.errors.append({'code':'environment-form-carbon-rows-incomplete','id':carbon['id']});rows=[]
        byid={x['id']:x for x in rows}
        values=[]
        for i,(key,label) in enumerate(row_ids.items()):
            row=byid.get(key,{})
            nested=row.get('values',{})
            numbers=[row.get('total'),*[nested.get(y,{}).get(k) for y in ('year1','year2') for k in ('scope2','scope3_service','equipment_scope3')]]
            if any(x is None for x in numbers):d.errors.append({'code':'environment-form-carbon-cell-missing','id':carbon['id'],'row':key})
            values.append(numbers)
            for j,value in enumerate([label]+numbers):
                d.rect(xs[j],535+i*52,widths[j],52,'#f0f4f7' if j==0 else '#ffffff','#aab4b8',0)
                d.text(xs[j]+7,565+i*52,str(value if value is not None else '未知'),13,units=max(10,int(widths[j]/8)))
        d.rect(30,701,1470,78,'#ffffff','#7fb86f',2)
        d.text(42,725,'备注：'+str(foot.get('comment','未记录')),13,units=150)
        if foot.get('printed_discrepancy'):
            d.text(42,751,'原图印刷差异（单列保留）：'+str(foot['printed_discrepancy']),12,units=155)
        d.attrs[carbon['id']].add('carbon_footprint');end()
    d.rect(30,792,1470,34,'#e8e8e8','#e8e8e8',0)
    d.text(765,815,'为最小化 IT 环境影响，目标架构研究的措施',18,anchor='middle')
    measures=blocks.get('架构措施')
    measure_labels={'development':'开发考虑环境影响','equipment':'设备能效与寿命','procurement':'采购纳入环境准则','data':'数据最小化','users':'用户低碳使用'}
    if measures:
        group(measures,30,831,1470,195);attrs=measures.get('attributes',{});items=attrs.get('measures')
        if not isinstance(items,list) or {x.get('id') for x in items if isinstance(x,dict)}!=set(measure_labels) or len(items)!=5:
            d.errors.append({'code':'environment-form-measures-incomplete','id':measures['id']});items=[]
        byid={x['id']:x for x in items}
        for j,(key,label) in enumerate(measure_labels.items()):
            x=30+j*294;item=byid.get(key,{})
            d.rect(x,831,282,178,'#eef4fb')
            d.rect(x+5,837,272,91,'#4474c1','#4474c1',2)
            d.text(x+141,862,label,15,'#ffffff','middle',units=16)
            selected=item.get('selected','unknown')
            if selected not in {'YES','NO'}:d.errors.append({'code':'environment-form-measure-unknown','id':measures['id'],'measure':key})
            selection(x+30,938,222,selected)
            d.text(x+8,989,str(item.get('explanation','未记录')),11,units=30)
        d.attrs[measures['id']].add('measures');end()
    d.text(30,1050,'深色按钮为已选；白色按钮为未选。Total 为整行合计；IN/OUT 为资源增减，非现金流。',13)
    d.text(30,1075,'来源结构版本：G242 图 3-14；当前模型值为虚构候选，来源结构等价仍需独立目视审核。',13)

def canvas_compare(d,es,rs):
    """Keep a complete canvas per named state, then show block-level changes."""
    groups=defaultdict(list)
    for e in es:
        sid=e.get('state_id')
        if not sid:d.errors.append({'code':'canvas-comparison-state-missing','id':e['id']})
        groups[sid or 'unknown'].append(e)
    order=d.view.get('state_ids') or list(groups)
    order=list(dict.fromkeys([i for i in order if i in groups]+list(groups)))
    if len(order)<2:d.errors.append({'code':'canvas-comparison-needs-two-states','id':d.view['id']})
    offset=0;local_edges=set();state_names={s['id']:s.get('name',s['id']) for s in getattr(d,'states',[])}
    for sid in order:
        items=groups[sid];ids={e['id'] for e in items}
        inner=[r for r in rs if r['source'] in ids and r['target'] in ids]
        child=Drawing(d.view,{**d.profile,'template':{**d.profile.get('template',{}),'_suppress_caption':True}},d.layout)
        # Keep a single label sequence and semantic register across state canvases.
        child.edge_register=d.edge_register
        canvas(child,items,inner)
        d.text(30,offset+95,'架构状态：'+state_names.get(sid,sid),18)
        d.parts.append(f'<g data-state-id="{esc(sid)}" transform="translate(0 {offset})">'+''.join(child.parts)+'</g>')
        for eid,(x,y,w,h) in child.positions.items():d.positions[eid]=(x,y+offset,w,h)
        d.entity_ids.update(child.entity_ids);d.relation_ids.update(child.relation_ids)
        for eid,fields in child.attrs.items():d.attrs[eid].update(fields)
        d.errors.extend(child.errors);d.warnings.extend(child.warnings)
        d.width=max(d.width,child.width);local_edges.update(r['id'] for r in inner)
        offset+=child.height+50
    d.height=max(d.height,offset)
    d.text(30,d.height+25,'按区块比较（未记录不等于删除；批准与实现状态另行记录）',16)
    for before,after in zip(order,order[1:]):
        def values(sid):
            out=defaultdict(list)
            for e in groups[sid]:out[e.get('attributes',{}).get('block','未分区')].append(str(e.get('attributes',{}).get('detail',e['name'])))
            return {k:sorted(v) for k,v in out.items()}
        b,a=values(before),values(after)
        for block in sorted(b.keys()|a.keys()):
            status='未变' if b.get(block)==a.get(block) else '变化'
            d.text(30,d.height+20,f'{block} · {status} · {state_names.get(before,before)}: '+ ' / '.join(b.get(block,['未记录']))+' → '+state_names.get(after,after)+': '+' / '.join(a.get(block,['未记录'])),13,units=150)
    d.network_routing=True
    for r in rs:
        if r['id'] not in local_edges:d.edge(r,{e['id']:e for e in es})

def value_chain(d,es,rs):
    supports=[];primary=[];unknown=[]
    for e in es:
        cat=str(e.get("attributes",{}).get("category",""))
        if any(k in cat.lower() for k in ["支持","support"]):supports.append(e)
        elif any(k in cat.lower() for k in ["主要","primary"]):primary.append(e)
        else:unknown.append(e)
    width=max(1100,len(primary)*320);d.width=width+70;y=110
    d.text(30,y,"支持活动",18);y+=25
    for e in supports:y+=d.card(e,30,y,width,fill="#e8edf6")+12
    d.text(30,y+22,"主要活动（并列价值贡献；不自动表示流程先后）",18)
    # Captions occupy space too: route labels must not cover the activity band.
    d.label_boxes.append((30,y+3,660,y+30));y+=65
    for i,e in enumerate(primary):d.card(e,30+i*320,y,300,fill="#e5efe4")
    if unknown:
        d.warnings.append("未分类对象未放入主要或支持活动，需确认类别。 "+", ".join(e["id"] for e in unknown));grid(d,unknown,3,d.height+30)
    margin=d.view.get("margin",d.profile.get("template",{}).get("margin"))
    if margin is not None:d.text(30,d.height+25,"Margin／价值或利润说明："+fmt(margin),16,units=130)
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})

def deployment(d,es,rs):
    if d.profile.get('template',{}).get('source_topology'):
        from source_topology_render import render_source_topology
        return render_source_topology(d,es,rs)
    byid={e["id"]:e for e in es};containers={e["id"]:e for e in es if e["type"] in {"trust_zone","network_zone","location","environment","platform","boundary","security_domain"}}
    parent={};containment_ids=set();conflicts=[];assignments=defaultdict(list)
    def assign(child,container,origin):
        if child==container:
            conflicts.append({'code':'container-self-parent','id':child,'origin':origin});return
        assignments[child].append((container,origin))
    for r in rs:
        if r["type"] in {"located_at","member_of_zone","deployed_on","within_boundary","belongs_to_domain"} and r["target"] in containers:
            assign(r['source'],r['target'],r['id'])
        elif r["type"]=="contains" and r["source"] in containers:
            assign(r['target'],r['source'],r['id'])
    for e in es:
        p=e.get("attributes",{}).get("parent_id",e.get("attributes",{}).get("boundary_id"))
        if p in containers:assign(e['id'],p,'parent_id/boundary_id')
    for child,choices in assignments.items():
        targets=list(dict.fromkeys(container for container,_ in choices))
        if len(targets)>1:
            # Physical location and logical network/security membership are independent
            # dimensions. Drawing either as the sole parent hides the other fact;
            # drawing all as edges preserves both without inventing container hierarchy.
            kinds=[containers[target]['type'] for target in targets]
            if len(set(kinds))==len(kinds) and all(origin!='parent_id/boundary_id' for _,origin in choices):
                d.warnings.append('多维容器归属以独立连线表达，不推断容器间嵌套：'+child)
                continue
            conflicts.append({'code':'multiple-container-parents','id':child,
                'parents':targets,'origins':[origin for _,origin in choices],
                'message':'同一维度的绘制实例不能静默选择两个容器之一；请拆分部署实例或明确所选范围。'})
            continue
        parent[child]=targets[0]
        containment_ids.update(origin for _,origin in choices if origin!='parent_id/boundary_id')
    # Check the full parent graph, including rootless cycles, before drawing.
    for identity in parent:
        seen=set();current=identity
        while current in parent:
            if current in seen:
                conflicts.append({'code':'container-cycle','id':identity});break
            seen.add(current);current=parent[current]
    if conflicts:
        d.errors.extend(conflicts)
        return
    roots=[e for e in es if e["id"] not in parent];children=defaultdict(list)
    for child,p in parent.items():children[p].append(child)
    seen=set()
    def height(e,w,path):
        if e["id"] in path:return 100
        return d.card_height(e,w)+sum(height(byid[c],w-40,path|{e["id"]})+20 for c in children[e["id"]])+25
    def draw(e,x,y,w,path):
        if e["id"] in path:d.errors.append({"code":"container-cycle","id":e["id"]});return
        h=height(e,w,path);d.card(e,x,y,w,h,"#f4f7fb" if e["id"] in containers else "#e4edf6");seen.add(e["id"]);cy=y+d.card_height(e,w)+12
        for c in children[e["id"]]:draw(byid[c],x+20,cy,w-40,path|{e["id"]});cy+=height(byid[c],w-40,path|{e["id"]})+20
    y=110
    for e in roots:draw(e,30,y,1020,set());y+=height(e,1020,set())+30
    for e in es:
        if e["id"] not in seen:d.errors.append({"code":"unresolved-container","id":e["id"]})
    d.network_routing=True
    for r in rs:
        if r['id'] in containment_ids:
            d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">')
            d.text(30,d.height+12,byid[r["source"]]["name"]+" → "+byid[r["target"]]["name"]+"："+r["label"]+" ["+r["type"]+"]",13,units=135)
            d.parts.append("</g>");d.relation_ids.add(r["id"])
        else:d.edge(r,byid)

def matrix(d,es,rs):
    t=matrix_options(d.profile)
    rows,cols,cells,outside=project_matrix(es,rs,t)
    if not rows or not cols:
        d.errors.append({"code":"missing-matrix-axes"});grid(d,es);return
    cw=220;rh=max(110,max(len(wrap(e["name"]+" / "+e["id"],22))*22+48 for e in rows+cols),max([sum(len(wrap(cell_label(r,direction),22))*20+15 for r,direction in entries)+40 for entries in cells.values()]+[80]));y=110;labelw=300
    d.rect(30,y,labelw,rh,"#dae6f0");d.text(42,y+26,"行／列 · 未记录≠不存在",14,units=30)
    for i,e in enumerate(cols):d.card(e,30+labelw+i*cw,y,cw,rh,fields=[])
    for j,e in enumerate(rows):
        yy=y+(j+1)*rh;d.card(e,30,yy,labelw,rh,fields=[])
        for i,col in enumerate(cols):
            xx=30+labelw+i*cw;edges=cells.get((e["id"],col["id"]),[])
            d.rect(xx,yy,cw,rh,"#f6f9fb");cy=yy+25
            if not edges:d.text(xx+10,cy,"未记录",13)
            for r,direction in edges:
                d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">');cy+=d.text(xx+10,cy,cell_label(r,direction),13,units=22)+10;d.parts.append("</g>");d.relation_ids.add(r["id"])
                d.edge_register.append(r)
    remaining=[e for e in es if e["id"] not in d.entity_ids]
    if remaining:grid(d,remaining,3,d.height+30)
    detailed=[e for e in es if e.get("attributes")]
    if detailed:
        yy=d.height+30;d.text(30,yy,"行列对象的定义与必要属性（与矩阵内同一稳定 ID）：",16)
        grid(d,detailed,2,yy+35)
    for r in rs:
        if r["id"] not in d.relation_ids:d.errors.append({"code":"relation-outside-matrix-axes","id":r["id"]})
    d.text(30,d.height+25,'单元含义：'+str(t.get('cell_meaning','关系类型／代码含义见图例'))+'；空白含义：'+str(t.get('empty_meaning','未记录≠不存在；不推断不适用或零分')),14,units=140)

def sequence(d,es,rs):
    byid={e["id"]:e for e in es};w=300;top=110
    mh=max([d.card_height(e,w-25) for e in es]+[80])
    for i,e in enumerate(es):d.card(e,30+i*w,top,w-25,mh)
    yy=top+mh+65
    ordered=sorted(rs,key=lambda r:(r.get("attributes",{}).get("order",999999),r["id"]))
    for r in rs:
        if "order" not in r.get("attributes",{}):d.errors.append({"code":"missing-message-order","id":r["id"]})
    usedorders=[r.get("attributes",{}).get("order") for r in rs if "order" in r.get("attributes",{})]
    if len(usedorders)!=len(set(usedorders)):d.errors.append({"code":"duplicate-message-order"})
    for r in ordered:
        a=d.positions.get(r["source"]);b=d.positions.get(r["target"])
        if a and b:
            x1=a[0]+a[2]/2;x2=b[0]+b[2]/2
            if x1==x2:
                d.parts.append(f'<path data-relationship-id="{esc(r["id"])}" d="M{x1} {yy} h60 v35 h-60" fill="none" stroke="#46647e" marker-end="url(#arrow)"/>');d.text(x1+65,yy+15,r["label"],13,units=34);d.relation_ids.add(r["id"]);yy+=95
            else:d.line(x1,yy,x2,yy,str(r.get("attributes",{}).get("order","?"))+". "+r["label"]+" ["+r["type"]+"]",r);yy+=95
    for e in es:
        x,y,w1,h=d.positions[e["id"]];d.line(x+w1/2,y+h,x+w1/2,yy,dashed=True,arrow=False)
    d.height=max(d.height,yy+20)

def _schedule_span(e):
    from schedule_semantics import span
    return span(e)


def roadmap(d,es,rs):
    from schedule_semantics import hierarchy, check_schedule, is_milestone
    d.errors.extend(check_schedule(es))
    ordered,children,allspans=hierarchy(es)
    spans={k:v for k,v in allspans.items() if v}
    if not spans:
        d.warnings.append("未提供完整起止日期；显示状态／依赖视图，不推断排期。")
        network(d,sorted(es,key=lambda e:str(e.get("state_id",e.get("attributes",{}).get("ordinal",e["id"])))),rs);return
    earliest=min(s[0] for s in spans.values());latest=max(s[1] for s in spans.values())
    daywidth=8;axis_left=430;axis_top=148
    ticks=max(2,min(12,(latest-earliest)//14 or 1))
    step=max(1,(latest-earliest)//ticks)
    daywidth=max(daywidth,96/step)
    d.text(axis_left,108,"共享日期轴",14)
    d.parts.append(f'<path d="M{axis_left} {axis_top} L{axis_left+(latest-earliest)*daywidth+40} {axis_top}" fill="none" stroke="#46647e" stroke-width="1.6"/>')
    for i in range(ticks+1):
        day=earliest+i*step;x=axis_left+(day-earliest)*daywidth
        d.parts.append(f'<path d="M{x} {axis_top-6} L{x} {axis_top+6}" fill="none" stroke="#46647e"/>')
        d.text(x,axis_top-12,date.fromordinal(day).isoformat(),11,anchor="middle")
    scopes=[];seen=set()
    for e in es:
        a=e.get("attributes",{});scope=a.get("adm_scope");key=(scope,a.get("iteration_id"))
        if scope and key not in seen:
            seen.add(key);scopes.append(key)
    yy=185
    if scopes:
        d.text(30,yy,"ADM 迭代带（未声明 iteration_id 时为范围汇总）",15);yy+=24
        colors={"strategy":"#d9e8f6","portfolio":"#e4f0d9","project":"#fff0d2","delivery":"#f3e6f6"}
        for i,(scope,iteration) in enumerate(scopes):
            members=[e for e in es if (e.get("attributes",{}).get("adm_scope"),e.get("attributes",{}).get("iteration_id"))==(scope,iteration)]
            dates=[spans[e["id"]] for e in members if e["id"] in spans]
            if not dates:continue
            x=axis_left+(min(s[0] for s in dates)-earliest)*daywidth
            ww=max(24,(max(s[1] for s in dates)-min(s[0] for s in dates))*daywidth)
            d.rect(x,yy,ww,28,colors.get(scope,"#eee"));d.text(x+8,yy+18,scope+" ADM "+str(iteration or "范围汇总"),13)
            yy+=36
    for e,depth in ordered:
        a=e.get("attributes",{});indent=min(220,depth*40)
        d.card(e,30+indent,yy,350-indent)
        span=spans.get(e["id"])
        if not span:
            d.errors.append({"code":"missing-or-invalid-schedule","id":e["id"]});yy+=d.card_height(e,350-indent)+40;continue
        start,end,endraw=span
        x=axis_left+(start-earliest)*daywidth;ww=max(12,(end-start)*daywidth)
        if is_milestone(e):
            d.parts.append(f'<polygon points="{x+8},{yy+12} {x+20},{yy+28} {x+8},{yy+44} {x-4},{yy+28}" fill="#c45c26" stroke="#8a3d12"/>')
            d.text(x+26,yy+32,"里程碑 "+str(a.get("start",a.get("start_date"))),13)
            d.entity_ids.add(e["id"]);d.attrs[e["id"]].update(k for k in a if k in {"start","start_date","milestone","kind","adm_scope","parent_id"})
        else:
            fill="#9bb8c9" if a.get("parent_id") is None and children.get(e["id"]) else "#c8dece"
            d.rect(x,yy+20,ww,35,fill);d.text(x,yy+75,str(a.get("start",a.get("start_date")))+" → "+str(endraw or ("+"+str(a.get("duration_days",""))+"d")),13)
            if children.get(e["id"]):
                d.text(x,yy+12,"汇总",12,"#46647e")
        yy+=d.card_height(e,350-indent)+40
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})

def quadrant(d,es,rs):
    mapping={"top-left":(0,0),"top-right":(1,0),"bottom-left":(0,1),"bottom-right":(1,1),"左上":(0,0),"右上":(1,0),"左下":(0,1),"右下":(1,1)}
    cells=defaultdict(list);unknown=[]
    for e in es:
        q=e.get("attributes",{}).get("quadrant");p=mapping.get(q)
        if p is None:unknown.append(e)
        else:cells[p].append(e)
    # Axes are drawn only when the profile declares them; some sources have none.
    template=d.profile.get("template",{});xaxis=template.get("x_axis");yaxis=template.get("y_axis")
    quadrant_labels=template.get("quadrant_labels",{})
    left=95 if yaxis else 30;top=150 if yaxis else 110
    if yaxis:
        d.text(30,112,"纵轴 ↑ "+yaxis,15,units=150)
    label_height=45 if quadrant_labels else 0
    rh=max([sum(d.card_height(e,460)+20 for e in vals)+30+label_height for vals in cells.values()]+[220])
    if yaxis:
        d.parts.append(f'<path d="M{left-25} {top+2*rh+15} L{left-25} {top}" fill="none" stroke="#46647e" stroke-width="2" marker-end="url(#arrow)"/>')
        for row,word in [(0,"高"),(1,"低")]:d.text(left-50,top+row*(rh+15)+rh/2,word,15)
    positions=([(0,0),(1,0),(0,1),(1,1)] if quadrant_labels else list(cells))
    for col,row in positions:
        items=cells[(col,row)]
        x=left+col*530;y=top+row*(rh+15);d.rect(x,y,515,rh,PALETTE[col+row*2]);yy=y+15
        if quadrant_labels:
            name={ (0,0):"top-left",(1,0):"top-right",(0,1):"bottom-left",(1,1):"bottom-right"}[(col,row)]
            label=quadrant_labels.get(name)
            if not isinstance(label,str) or not label.strip():d.errors.append({"code":"missing-quadrant-label","id":name})
            else:d.text(x+15,y+28,label,17,units=45)
            yy+=40
        for e in items:yy+=d.card(e,x+15,yy,485)+15
    if xaxis:
        base=top+2*rh+30
        d.parts.append(f'<path d="M{left} {base} L{left+1045} {base}" fill="none" stroke="#46647e" stroke-width="2" marker-end="url(#arrow)"/>')
        for col,word in [(0,"低"),(1,"高")]:d.text(left+col*530+250,base+24,word,15)
        d.text(left,base+50,"横轴 → "+xaxis,15,units=150)
    if not xaxis and not yaxis:d.text(30,d.height+25,"本视图无坐标轴：四个区域是并列类别，位置不表示高低或评分。",14,units=140)
    if unknown:
        d.warnings.append("对象没有明确象限，不从数组次序推断象限或评分。")
        grid(d,unknown,3,d.height+30)
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})

def assessment(d,es,rs):
    """A labelled scorecard, never an invented aggregation or ranking."""
    fields=d.profile.get("template",{}).get("fields",[])
    fields=list(dict.fromkeys(fields+[k for e in es for k in e.get("attributes",{})]))
    if len(fields)>6:
        d.text(30,110,'多字段记录式表达；相邻记录不表示顺序或依赖。',16)
        grid(d,es,2 if d.layout=='reference' else 1,150)
        for r in rs:
            d.relation_ids.add(r['id']);d.edge_register.append(r)
        return
    widths=[300]+[245]*len(fields);xpositions=[30]
    for width in widths:xpositions.append(xpositions[-1]+width)
    labels=["评估对象 / ID"]+fields;y=110
    for i,label in enumerate(labels):
        d.rect(xpositions[i],y,widths[i],70,"#dfe9f3");d.text(xpositions[i]+10,y+25,label,14,units=26)
    y+=70
    for e in es:
        attrs=e.get("attributes",{});values=[e["name"]+" ["+e["id"]+"]"]+[fmt(attrs.get(field,"未记录")) for field in fields]
        h=max(65,max(len(wrap(v,26))*21+20 for v in values))
        d.parts.append(f'<g data-entity-id="{esc(e["id"])}">')
        for i,value in enumerate(values):
            d.rect(xpositions[i],y,widths[i],h,"#f4f7fa");d.text(xpositions[i]+10,y+25,value,13,units=26)
        d.parts.append("</g>");d.entity_ids.add(e["id"]);d.positions[e["id"]]=(30,y,sum(widths),h);d.attrs[e["id"]].update(k for k in fields if k in attrs);y+=h
    if rs:
        d.text(30,y+30,"评估追溯关系（独立于评分聚合）",16);y=d.height+15
        byid={e["id"]:e for e in es}
        for r in rs:
            d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">')
            y+=d.text(30,y,byid.get(r["source"],{}).get("name",r["source"])+" → "+byid.get(r["target"],{}).get("name",r["target"])+"："+r["label"]+" ["+r["type"]+"]",13,units=140)+10
            d.parts.append("</g>");d.relation_ids.add(r["id"])

def clip_to_box(box,toward):
    """Point where the segment from the box centre toward a point leaves the box."""
    x,y,w,h=box;cx,cy=x+w/2,y+h/2;dx=toward[0]-cx;dy=toward[1]-cy
    if not dx and not dy:return cx,cy
    t=min(w/2/abs(dx) if dx else float("inf"),h/2/abs(dy) if dy else float("inf"))
    return cx+dx*t,cy+dy*t

def framework_arrow(d,p,q,width=14,head=26):
    """A thick grey double-headed connector of the source framework, not a model relationship."""
    dx=q[0]-p[0];dy=q[1]-p[1];length=max(1,math.hypot(dx,dy));ux,uy=dx/length,dy/length;nx,ny=-uy,ux;h=width/2
    def at(t,off):return (p[0]+ux*t+nx*off,p[1]+uy*t+ny*off)
    e=length-head
    pts=[at(0,0),at(head,h*2.2),at(head,h),at(e,h),at(e,h*2.2),at(length,0),at(e,-h*2.2),at(e,-h),at(head,-h),at(head,-h*2.2)]
    d.parts.append('<polygon points="'+" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)+'" fill="#d3d6da" stroke="#9aa0a6" stroke-width="1"/>')

FOUR_BOX=[("value",["客户价值主张","价值主张","customer value proposition","cvp"]),("profit",["利润公式","profit formula"]),
          ("resources",["关键资源","key resources"]),("processes",["关键流程","key processes"])]

def four_box(d,es,rs):
    """Johnson four-box: CVP above, resources+processes grouped, profit formula beside them."""
    slots={};unknown=[]
    for e in es:
        label=str(e.get("attributes",{}).get("component",e["name"])).lower()
        slot=next((s for s,words in FOUR_BOX if any(w in label for w in words) and s not in slots),None)
        if slot:slots[slot]=e
        else:unknown.append(e)
    ref=d.layout=="reference";w=300 if ref else 330
    # Extra height keeps the resources-processes arrow below the card text.
    h=max([d.card_height(e,w) for e in slots.values()]+[110])+40
    box={"value":(380,130) if ref else (30,130),"resources":(30,h+330) if ref else (30,h+250),
         "processes":(345,h+330) if ref else (520,h+250),"profit":(760,h+330) if ref else (520,130)}
    for slot,(x,y) in box.items():
        if slot in slots:d.card(slots[slot],x,y,w,h,"#e6ecf2")
        else:d.rect(x,y,w,h,"#f4f5f6");d.text(x+12,y+30,dict(FOUR_BOX)[slot][0]+"：未记录",15);d.warnings.append("四框缺少区块："+dict(FOUR_BOX)[slot][0])
    gx,gy=box["resources"];d.rect(gx-12,gy-12,box["processes"][0]+w-gx+24,h+24,"none","#8a8f96",8,'stroke-dasharray="3 3"')
    v=box["value"];pr=box["profit"];group=(gx-12,gy-12,box["processes"][0]+w+12-gx+12,h+24)
    if ref:
        framework_arrow(d,(v[0]+40,v[1]+h+8),(group[0]+group[2]*0.55,group[1]-8))
        framework_arrow(d,(v[0]+w-40,v[1]+h+8),(pr[0]+w*0.3,pr[1]-8))
        framework_arrow(d,(group[0]+group[2]+8,pr[1]+h/2),(pr[0]-8,pr[1]+h/2))
    else:
        framework_arrow(d,(v[0]+w+8,v[1]+h/2),(pr[0]-8,pr[1]+h/2))
        framework_arrow(d,(v[0]+w/2,v[1]+h+8),(v[0]+w/2,group[1]-8))
        framework_arrow(d,(pr[0]+w/2,pr[1]+h+8),(pr[0]+w/2,group[1]-8))
    ry=box["resources"][1]+h-22;rx1=box["resources"][0]+w-30;rx2=box["processes"][0]+30
    framework_arrow(d,(rx1,ry),(rx2,ry))
    d.text(30,d.height+25,"灰色粗双向箭头与虚线分组是四框框架的固定结构（来源：G18A 图 2-2），表示四要素需相互一致，不是本模型的关系；模型关系另以编号连线表达。",14,units=140)
    if unknown:d.errors.append({"code":"unknown-four-box-component","ids":[e["id"] for e in unknown]});grid(d,unknown,3,d.height+35)
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})

CUBE=[("value_propositions",["价值主张","value proposition"]),("customers",["客户","customer"]),("network_partners",["网络伙伴","伙伴","partner"]),
      ("activities",["活动","activit"]),("competences",["胜任力","能力","competence"]),("value_formulas",["价值公式","value formula"])]

def cube(d,es,rs):
    """Lindgren-Rasmussen cube: six parallel dimensions around a Relations core, which is not a seventh dimension."""
    cells=defaultdict(list);unknown=[]
    for e in es:
        label=str(e.get("attributes",{}).get("dimension",e["name"])).lower()
        slot=next((s for s,words in CUBE if any(w in label for w in words)),None)
        (cells[slot] if slot else unknown).append(e)
    w=320;gap=40;rowh=max([sum(d.card_height(e,w-20)+12 for e in items)+20 for items in cells.values()]+[130])
    # reference: unfolded cube net; adaptive: core band above a 3x2 grid
    grid_pos={"value_propositions":(1,0),"customers":(0,0),"network_partners":(2,0),"activities":(0,1),"value_formulas":(2,1),"competences":(1,2)} if d.layout=="reference" else \
             {"value_propositions":(0,1),"customers":(1,1),"network_partners":(2,1),"activities":(0,2),"competences":(1,2),"value_formulas":(2,2)}
    core=(30+w+gap,110+rowh+gap,w,rowh) if d.layout=="reference" else (30,110,3*w+2*gap,110)
    d.rect(*core,"#3f86b4","#2c5f80",4);d.text(core[0]+core[2]/2,core[1]+core[3]/2,"Relations 关系（核心，不是第七维度）",17,"white","middle",60)
    for slot,(col,row) in grid_pos.items():
        x=30+col*(w+gap);y=110+row*(rowh+gap) if d.layout=="reference" else 110+core[3]+gap+(row-1)*(rowh+gap)
        d.rect(x,y,w,rowh,"#f3f6f9");cy=y+10
        for e in cells.get(slot,[]):cy+=d.card(e,x+10,cy,w-20)+12
        if not cells.get(slot):d.text(x+12,y+30,dict(CUBE)[slot][0]+"：未记录",15);d.warnings.append("立方体缺少维度："+dict(CUBE)[slot][0])
        if d.layout=="reference":
            p=clip_to_box((x,y,w,rowh),(core[0]+core[2]/2,core[1]+core[3]/2));q=clip_to_box(core,(x+w/2,y+rowh/2))
            d.parts.append(f'<path d="M{p[0]:.1f} {p[1]:.1f} L{q[0]:.1f} {q[1]:.1f}" stroke="#7d97ab" stroke-width="1.5" stroke-dasharray="2 4" fill="none"/>')
    d.positions["_relations_core"]=core
    d.text(30,d.height+25,"六个维度并列且都与 Relations 核心相关（来源：G18A 图 2-3）；位置不表示流程先后或层级。维度间关系只按模型中有依据的关系绘制。",14,units=140)
    if unknown:d.errors.append({"code":"unknown-cube-dimension","ids":[e["id"] for e in unknown]});grid(d,unknown,3,d.height+35)
    d.network_routing=True
    for r in rs:d.edge(r,{e["id"]:e for e in es})
    d.positions.pop("_relations_core",None)

BSC=["客户","学习与成长","内部流程","财务"]

def perspectives(d,es,rs):
    """Balanced scorecard: goals left, measurable outcomes right, joined only by realization; no cross-perspective causality."""
    order=d.profile.get("template",{}).get("perspectives",BSC);groups=defaultdict(list);unknown=[]
    for e in es:
        p=e.get("attributes",{}).get("perspective");(groups[p] if p in order else unknown).append(e)
    byid={e["id"]:e for e in es};realize=[r for r in rs if r["type"] in HOLLOW_HEAD and r["source"] in byid and r["target"] in byid]
    regw=560;cw=230;regions=[]
    for p in order:
        items=groups.get(p,[]);goals=[e for e in items if e["type"]=="goal"];outs=[e for e in items if e["type"]!="goal"];rows=[];placed=set()
        for g in goals:
            linked=[byid[r["source"]] for r in realize if r["target"]==g["id"] and byid[r["source"]] in outs and r["source"] not in placed]
            rows.append((g,linked));placed.update(o["id"] for o in linked)
        regions.append((p,rows+[(None,[o]) for o in outs if o["id"] not in placed]))
    def row_height(g,outs):
        # A single goal-outcome pair shares one height so the realization line stays level.
        own=[d.card_height(g,cw)] if g else []
        if len(outs)<=1:return max(own+[d.card_height(o,cw) for o in outs]+[90])
        return max(own+[sum(d.card_height(o,cw)+15 for o in outs)-15])
    y=110
    for start in range(0,len(regions),2):
        pair=regions[start:start+2];rh=max([sum(row_height(g,o)+25 for g,o in rows)+60 for _,rows in pair]+[130])
        for i,(p,rows) in enumerate(pair):
            x=30+i*(regw+20)
            d.rect(x,y+30,regw,rh-30,"none","#9aa0a6",0,'stroke-dasharray="6 4"');d.rect(x,y,290,30,"white","#9aa0a6",0,'stroke-dasharray="6 4"');d.text(x+10,y+21,p,16)
            yy=y+52
            if not rows:d.text(x+15,yy+20,"本视角未记录目标或成果；不能解释为不需要。",13,units=64)
            for g,outs in rows:
                h=row_height(g,outs)
                if g:d.card(g,x+15,yy,cw,h if len(outs)<=1 else None,"#dcd8f6")
                oy=yy
                for o in outs:oy+=d.card(o,x+regw-cw-15,oy,cw,h if len(outs)==1 else None,"#dcd8f6")+15
                yy+=h+25
        y+=rh+20
    d.text(30,d.height+25,"四个视角并列（来源：G233 图 4-3）；每个视角内左为目标、右为可度量成果，空心三角虚线表示成果实现目标。视角之间没有因果连线，不补造学习→财务的因果链。",14,units=140)
    if unknown:d.errors.append({"code":"unknown-scorecard-perspective","ids":[e["id"] for e in unknown]});grid(d,unknown,3,d.height+35)
    for r in realize:
        if byid[r["source"]].get("attributes",{}).get("perspective")==byid[r["target"]].get("attributes",{}).get("perspective"):d.edge(r,byid)
    d.network_routing=True
    for r in rs:
        if r["id"] not in d.relation_ids:d.edge(r,byid)

LEAN_FIELDS=[("lead_time","LT"),("processing_time","PT"),("complete_accurate","%C&A")]

def lean_flow(d,es,rs):
    """Lean VSM bands: information flow, push work flow with queues and step metrics, LT/PT timeline.
    Totals are shown only from an explicit lean-serial-flow analysis, never summed here."""
    byid={e["id"]:e for e in es};procs=[e for e in es if e["type"]=="lean_process"]
    if not procs:d.errors.append({"code":"missing-lean-processes"});network(d,es,rs);return
    work=[r for r in rs if r["type"]=="work_flow" and r["source"] in byid and r["target"] in byid]
    nxt={r["source"]:r["target"] for r in work};incoming={r["target"] for r in work}
    order=[];cur=next((p["id"] for p in procs if p["id"] not in incoming),procs[0]["id"])
    while cur and cur not in order and cur in byid:order.append(cur);cur=nxt.get(cur)
    order+=[p["id"] for p in procs if p["id"] not in order]
    if len(work)!=len(order)-1 or len(nxt)!=len(work):d.warnings.append("工作流不是单一串行链（存在并行、返工或断开）；时间线不能直接相加。")
    x0=240;colw=300;cw=220;col={pid:i for i,pid in enumerate(order)}
    info=[e for e in es if e["type"]!="lean_process"];flows=[r for r in rs if r["type"]=="information_flow"]
    def anchor(e):
        cols=[col[o] for r in flows for o in [r["source"],r["target"]] if e["id"] in (r["source"],r["target"]) and o in col]
        return sum(cols)/len(cols) if cols else 0
    rows=[[e for e in info if e["type"] in {"actor","customer","organization"}],[e for e in info if e["type"] not in {"actor","customer","organization"}]]
    y=125;used={}
    for row in rows:
        if not row:continue
        rh=max(d.card_height(e,cw) for e in row)
        for e in sorted(row,key=anchor):
            slot=round(anchor(e))
            while (y,slot) in used:slot+=1
            used[(y,slot)]=e["id"];d.card(e,x0+slot*colw,y,cw,rh,"#dbe7f5" if e["type"] in {"actor","customer"} else "#ffffff")
        y+=rh+70
    top_work=y;fields=d.profile.get("template",{}).get("card_fields",["function"])
    ph=max(d.card_height(byid[p],cw,[f for f in fields if f in byid[p].get("attributes",{})]) for p in order)
    for pid in order:
        e=byid[pid];x=x0+col[pid]*colw;a=e.get("attributes",{})
        d.card(e,x,top_work,cw,ph,"#dbe7f5",[f for f in fields if f in a]);my=top_work+ph+8;lines=[]
        for field,short in LEAN_FIELDS:
            if field in a:
                value=a[field];value=f"{value*100:g}%" if field=="complete_accurate" and isinstance(value,(int,float)) and value<=1 else fmt(value)+("" if field=="complete_accurate" else " "+fmt(a.get("unit","单位未记录")))
                lines.append(short+" = "+value);d.attrs[pid].add(field)
        for extra in ["unit","working_minutes_per_day","metric_evidence"]:
            if extra in a:lines.append({"unit":"单位","working_minutes_per_day":"每日工作分钟","metric_evidence":"度量依据"}[extra]+"："+fmt(a[extra]));d.attrs[pid].add(extra)
        d.parts.append(f'<g data-entity-id="{esc(pid)}">');d.rect(x,my,cw,len(lines)*20+14,"#ffffff","#46647e",0)
        for i,line in enumerate(lines):d.text(x+8,my+20+i*20,line,13,units=int((cw-16)/7))
        d.parts.append("</g>");d.positions["_metric_"+pid]=(x,my,cw,len(lines)*20+14)
        if "queue" in a:
            qx=x-70;qy=top_work+ph/2-14
            for k in range(3):d.parts.append(f'<line x1="{qx+8}" y1="{qy+k*5}" x2="{qx+48}" y2="{qy+k*5}" stroke="#46647e"/>')
            d.rect(qx+4,qy+16,44,14,"#ffffff","#46647e",0);d.text(qx+26,qy+48,fmt(a["queue"])+" 项排队",12,anchor="middle");d.attrs[pid].add("queue")
    metric_bottom=max(v[1]+v[3] for k,v in d.positions.items() if k.startswith("_metric_"))
    ty=metric_bottom+70;path=f"M{x0-40} {ty+30}"
    for pid in order:
        a=byid[pid].get("attributes",{});x=x0+col[pid]*colw
        path+=f" L{x} {ty+30} L{x} {ty} L{x+cw} {ty} L{x+cw} {ty+30}"
        unit=" "+fmt(a["unit"]) if "unit" in a else ""
        d.text(x+cw/2,ty-8,"LT "+fmt(a.get("lead_time","未记录"))+unit,13,anchor="middle");d.text(x+cw/2,ty+22,"PT "+fmt(a.get("processing_time","未记录"))+unit,13,anchor="middle")
    d.parts.append(f'<path d="{path} L{x0+len(order)*colw} {ty+30}" fill="none" stroke="#19364d" stroke-width="1.5"/>')
    for label,(y1,y2) in [("1 信息流",(115,top_work-20)),("2 工作流",(top_work,metric_bottom)),("3 时间线",(ty-25,ty+40))]:
        if y2-y1<40:continue
        d.parts.append(f'<path d="M58 {y1} Q46 {y1} 46 {y1+12} L46 {(y1+y2)/2-8} L36 {(y1+y2)/2} L46 {(y1+y2)/2+8} L46 {y2-12} Q46 {y2} 58 {y2}" fill="none" stroke="#46647e"/>')
        d.text(30,(y1+y2)/2+30,label,15,"#9b2d2d")
    summary=[res for res in d.view.get("analysis_results",[]) if res.get("method_id")=="lean-serial-flow"]
    sy=ty+70
    labels=[("total_lead_time_minutes","总 LT（分钟）"),("total_process_time_minutes","总 PT（分钟）"),("activity_ratio_percent","活动比 %"),
            ("cumulative_complete_accurate_percent","累积 %C&A"),("non_processing_time_minutes","非加工时间（分钟）"),("boundary","范围")]
    units=int((d.width-x0-40)/7.5)
    if summary:
        for res in summary:
            sy+=d.text(x0,sy,"串行汇总（lean-serial-flow 分析 "+res["id"]+"）",15,units=units)+6;result=res.get("result",{})
            for key,label in labels:
                if key in result:value=result[key];sy+=d.text(x0+16,sy,label+"："+(f"{value:.1f}" if isinstance(value,float) else fmt(value)),13,units=units)+4
            if result.get("notice"):sy+=d.text(x0+16,sy,"说明："+result["notice"],13,units=units)+4
    else:d.text(x0,sy,"未提供 lean-serial-flow 分析结果：总 LT、总 PT、活动比和累积 %C&A 未计算；须先声明单位换算与串行规则。",14,units=130)
    for r in work:
        a=d.positions[r["source"]];b=d.positions[r["target"]]
        if col[r["target"]]==col[r["source"]]+1:
            yy=top_work+ph/2;x1=a[0]+a[2]+4;x2=b[0]-(76 if "queue" in byid[r["target"]].get("attributes",{}) else 6)
            d.parts.append(f'<g data-relationship-id="{esc(r["id"])}"><path d="M{x1} {yy} L{x2-12} {yy}" stroke="#46647e" stroke-width="5" stroke-dasharray="6 5" fill="none"/><polygon points="{x2-14},{yy-9} {x2},{yy} {x2-14},{yy+9}" fill="#46647e"/></g>')
            d.relation_ids.add(r["id"]);d.edge_register.append(r);d.text((x1+x2)/2,yy-14,"["+str(len(d.edge_register))+"]",12,anchor="middle")
    d.network_routing=True
    for r in rs:
        if r["id"] not in d.relation_ids:d.edge(r,byid)
    for k in [k for k in d.positions if k.startswith("_metric_")]:d.positions.pop(k)
    d.text(30,d.height+25,"精益价值流（来源：G178 图 A-3）：细实线为信息流，粗点线为推式工作流，排队数记录在下游流程之前；精益流程不是业务架构价值阶段。",14,units=140)

FLOW_NODES={"process","activity","decision","event","business_process"}
LANE_TYPES={"role","actor","organization","organization_unit"}
FLOW_EDGES={"flows_to","triggers","branches","precedes","next"}

def swimlane(d,es,rs):
    """Process flow in role lanes; columns follow flow order. Lane comes from assigned_to, else declared owner."""
    byid={e["id"]:e for e in es};nodes=[e for e in es if e["type"] in FLOW_NODES]
    if not nodes:d.errors.append({"code":"missing-flow-nodes"});network(d,es,rs);return
    lane={};lanes=[e for e in es if e["type"] in LANE_TYPES];assign=[r for r in rs if r["type"]=="assigned_to"]
    for r in assign:
        if r["source"] in byid and r["target"] in byid:lane[r["target"]]=byid[r["source"]]["name"]
    fallback=False
    for e in nodes:
        if e["id"] not in lane:
            owner=e.get("attributes",{}).get("owner",e.get("attributes",{}).get("lane"))
            lane[e["id"]]=fmt(owner) if owner else "未分配泳道";fallback=fallback or bool(owner)
    if fallback:d.warnings.append("部分泳道按对象的 owner 属性划分（无 assigned_to 关系）；须确认 owner 是执行角色而非审批或数据所有者。")
    names=list(dict.fromkeys([e["name"] for e in lanes]+[lane[e["id"]] for e in nodes]))
    flow=[r for r in rs if r["type"] in FLOW_EDGES and r["source"] in lane and r["target"] in lane]
    out=defaultdict(list)
    for r in flow:out[r["source"]].append(r)
    layer={};back=set();state={}
    def visit(n,depth):
        if state.get(n)=="open":return
        layer[n]=max(layer.get(n,0),depth);state[n]="open"
        for r in out[n]:
            if state.get(r["target"])=="open":back.add(r["id"])
            elif layer.get(r["target"],-1)<depth+1:visit(r["target"],depth+1)
        state[n]="done"
    targets={r["target"] for r in flow}
    for e in nodes:
        if e["id"] not in targets and e["id"] not in layer:visit(e["id"],0)
    for e in nodes:
        if e["id"] not in layer:visit(e["id"],0)
    labelw=170;colw=290;cw=250;y=110
    width=labelw+(max(layer.values())+1)*colw+20
    for i,name in enumerate(names):
        members=[e for e in nodes if lane[e["id"]]==name];rh=max([d.card_height(e,cw)+40 for e in members]+[130])
        d.rect(30,y,width,rh,"#f7f9fb" if i%2==0 else "#eef2f6","#8298aa",0)
        header=next((e for e in lanes if e["name"]==name),None)
        if header:d.card(header,30,y,labelw,rh,"#dae6f0",fields=[],radius=0)
        else:d.rect(30,y,labelw,rh,"#dae6f0","#8298aa",0);d.text(42,y+30,name,15,units=int((labelw-24)/7.5))
        for e in members:
            shown=dict(e,name={"decision":"◇ 判断：","event":"○ 事件："}.get(e["type"],"")+e["name"])
            d.card(shown,30+labelw+layer[e["id"]]*colw+20,y+20,cw,None,{"decision":"#fff0d8","event":"#e7f1e9"}.get(e["type"],"#e2edf8"),radius=0 if e["type"]=="decision" else 10)
        y+=rh
    others=[e for e in es if e["id"] not in d.entity_ids]
    if others:d.text(30,d.height+30,"泳道外的关联对象",16);grid(d,others,3,d.height+20)
    d.network_routing=True
    for r in rs:
        if r in assign:
            d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">');d.text(30,d.height+12,"泳道归属："+byid[r["source"]]["name"]+" 执行 "+byid[r["target"]]["name"]+" ["+r["type"]+"]",13,units=140);d.parts.append("</g>");d.relation_ids.add(r["id"])
        else:d.edge(dict(r,label=r.get("label",r["type"])+("（回路／返工）" if r["id"] in back else "")),byid)
    d.text(30,d.height+25,"泳道按执行角色划分；列次序由流转关系推导，回路边单独标注。◇ 为判断，○ 为事件；连线编号见下方关系表。",14,units=140)

LIFECYCLE={"product_state","data_state","state","lifecycle_state"}

def state_diagram(d,es,rs):
    """States with labelled transitions. Initial/final pseudostates only when declared, never inferred."""
    byid={e["id"]:e for e in es};states=[e for e in es if e["type"] in LIFECYCLE]
    if not states:d.errors.append({"code":"missing-states"});network(d,es,rs);return
    ids={e["id"] for e in states};moves=[r for r in rs if r["type"]=="transitions_to" and r["source"] in ids and r["target"] in ids]
    flag=lambda e,k:e.get("attributes",{}).get(k) is True or e.get("attributes",{}).get("pseudostate")==k
    initial=[e["id"] for e in states if flag(e,"initial")];final=[e["id"] for e in states if flag(e,"final")]
    if not initial:d.warnings.append("模型未声明初始状态；不从拓扑推断起点，也不绘制初始伪状态。")
    roots=initial or [e["id"] for e in states if e["id"] not in {r["target"] for r in moves}] or [states[0]["id"]]
    order=[];queue=list(roots)
    while queue:
        n=queue.pop(0)
        if n in order:continue
        order.append(n);queue+=[r["target"] for r in moves if r["source"]==n]
    order+=[e["id"] for e in states if e["id"] not in order]
    cw=300;gapx=150;per=3 if d.layout=="reference" else 2;x0=110;y=150
    for start in range(0,len(order),per):
        row=order[start:start+per];rh=max(d.card_height(byid[i],cw) for i in row)
        for j,i in enumerate(row):
            d.card(byid[i],x0+j*(cw+gapx),y,cw,rh,"#e7f1e9",radius=24);x,yy,w,h=d.positions[i]
            if i in initial:
                d.parts.append(f'<circle cx="{x-60}" cy="{yy+h/2}" r="11" fill="#19364d"/><path d="M{x-49} {yy+h/2} L{x-4} {yy+h/2}" stroke="#19364d" stroke-width="1.8" marker-end="url(#arrow)" fill="none"/>')
            if i in final:
                d.parts.append(f'<path d="M{x+w/2} {yy+h+4} L{x+w/2} {yy+h+44}" stroke="#19364d" stroke-width="1.8" marker-end="url(#arrow)" fill="none"/><circle cx="{x+w/2}" cy="{yy+h+60}" r="14" fill="white" stroke="#19364d" stroke-width="2"/><circle cx="{x+w/2}" cy="{yy+h+60}" r="8" fill="#19364d"/>')
                d.height=max(d.height,yy+h+90)
        y+=rh+(130 if any(i in final for i in row) else 90)
    others=[e for e in es if e["id"] not in ids]
    if others:grid(d,others,3,d.height+30)
    if d.layout=="adaptive":
        # Incoming and outgoing transitions need independent attachment slots:
        # a folded lifecycle must not look like a branch of its preceding edge.
        incident=defaultdict(list)
        for r in moves:
            if r["source"]==r["target"]:continue
            incident[r["source"]].append((r["id"],"source"))
            incident[r["target"]].append((r["id"],"target"))
        for node,endpoints in incident.items():
            if len(endpoints)<2:continue
            _,_,w,h=d.positions[node]
            step=min(24,2*min(w,h)/3/(len(endpoints)-1))
            for index,endpoint in enumerate(sorted(endpoints)):
                d.endpoint_port_offsets[endpoint]=(index-(len(endpoints)-1)/2)*step
    d.network_routing=True
    for r in rs:d.edge(r,byid)
    d.text(30,d.height+25,"圆角框为状态；实心圆为声明的初始伪状态，靶心为声明的终止状态；转换的触发、条件与动作见编号关系表。",14,units=140)

def causal_loop(d,es,rs):
    """Variables on a circle; curved links carry +/- at the arrowhead; loops are verified, not assumed."""
    byid={e["id"]:e for e in es};n=len(es);cw=230;ch=max([d.card_height(e,cw) for e in es]+[90])
    radius=max(260,n*75);cx=radius+cw/2+60;cy=radius+ch/2+130
    for i,e in enumerate(es):
        angle=-math.pi/2+i*2*math.pi/max(1,n);d.card(e,cx+radius*math.cos(angle)-cw/2,cy+radius*math.sin(angle)-ch/2,cw,ch,"#fff7e8")
    pairs={(r["source"],r["target"]) for r in rs}
    for r in rs:
        if r["source"] not in d.positions or r["target"] not in d.positions:d.errors.append({"code":"edge-endpoint-not-placed","id":r["id"]});continue
        a=d.positions[r["source"]];b=d.positions[r["target"]];ac=(a[0]+a[2]/2,a[1]+a[3]/2);bc=(b[0]+b[2]/2,b[1]+b[3]/2)
        mx,my=(ac[0]+bc[0])/2,(ac[1]+bc[1])/2;ox,oy=mx-cx,my-cy;length=math.hypot(ox,oy)
        if length<1:dx,dy=bc[0]-ac[0],bc[1]-ac[1];l2=max(1,math.hypot(dx,dy));ox,oy,length=-dy/l2,dx/l2,1
        bend=70 if (r["target"],r["source"]) not in pairs or r["source"]<r["target"] else -70
        ctrl=(mx+ox/length*bend,my+oy/length*bend);p=clip_to_box(a,ctrl);q=clip_to_box(b,ctrl)
        q=(q[0]+(ctrl[0]-q[0])*0.04,q[1]+(ctrl[1]-q[1])*0.04)
        polarity=str(r.get("attributes",{}).get("polarity",""));sign="+" if polarity in {"+","positive"} else "−" if polarity in {"-","negative"} else "?"
        d.parts.append(f'<path data-relationship-id="{esc(r["id"])}" d="M{p[0]:.1f} {p[1]:.1f} Q{ctrl[0]:.1f} {ctrl[1]:.1f} {q[0]:.1f} {q[1]:.1f}" fill="none" stroke="#46647e" stroke-width="1.8" marker-end="url(#arrow)"/>')
        d.relation_ids.add(r["id"]);d.edge_register.append(r)
        sx,sy=q[0]+(ctrl[0]-q[0])*0.18,q[1]+(ctrl[1]-q[1])*0.18;tx,ty=(p[0]+2*ctrl[0]+q[0])/4,(p[1]+2*ctrl[1]+q[1])/4
        d.text(sx,sy-6,sign,22,"#b83f4b" if sign=="−" else "#2869ad","middle");d.text(tx,ty,"["+str(len(d.edge_register))+"]",12,anchor="middle")
    rbyid={r["id"]:r for r in rs}
    for loop in d.view.get("attributes",{}).get("loops",d.view.get("loops",d.profile.get("template",{}).get("loops",[]))):
        members=[rbyid[i] for i in loop.get("relationship_ids",[]) if i in rbyid]
        if not loop.get("relationship_ids"):d.warnings.append("回路 "+str(loop.get("id"))+" 未列出组成关系，类型无法核验。");continue
        if len(members)!=len(loop["relationship_ids"]):d.errors.append({"code":"loop-references-unknown-relationship","id":loop.get("id")});continue
        closed=sorted(r["source"] for r in members)==sorted(r["target"] for r in members) and len({r["source"] for r in members})==len(members)
        if not closed:d.errors.append({"code":"loop-not-closed","id":loop.get("id")});continue
        negatives=sum(str(r.get("attributes",{}).get("polarity")) in {"-","negative"} for r in members)
        derived="reinforcing" if negatives%2==0 else "balancing"
        if loop.get("type") and loop["type"]!=derived:d.errors.append({"code":"loop-type-contradicts-polarity","id":loop.get("id"),"declared":loop["type"],"derived":derived})
        nodes=[d.positions[r["source"]] for r in members];lx=sum(x+w/2 for x,_,w,_ in nodes)/len(nodes);ly=sum(y+h/2 for _,y,_,h in nodes)/len(nodes)
        d.parts.append(f'<path d="M{lx+22} {ly-10} A24 24 0 1 1 {lx+6} {ly-24}" fill="none" stroke="#9b2d2d" stroke-width="2" marker-end="url(#arrow)"/>')
        d.text(lx,ly+50,str(loop.get("id",""))+(" 强化" if derived=="reinforcing" else " 平衡"),15,"#9b2d2d","middle")
    d.text(30,d.height+25,"箭头端 + 表示同向变化，− 表示反向变化；回路中负号个数为偶数是强化回路，奇数是平衡回路（按所列关系计算并与声明比对）。",14,units=140)

def render_profile(model, view, profile, layout="adaptive"):
    if profile.get('id') == 'architecture-work-assignment-map':
        from assignment_projection import render_assignment
        return render_assignment(model, view, profile, layout)
    from metadata_render import metadata_map
    from agile_render import agile_sprints
    if layout not in {"reference","adaptive"}:raise ValueError("未知布局："+str(layout))
    profile=dict(profile)
    basefile=ROOT/"templates"/(profile.get("renderer","network")+".json")
    base=json.loads(basefile.read_text()) if basefile.exists() else {}
    profile["template"]={**base,**(profile.get("template") or {})}
    byid={e["id"]:e for e in model.get("entities",[])};rbyid={r["id"]:r for r in model.get("relationships",[])}
    es=[byid[i] for i in view.get("entity_ids",[]) if i in byid];rs=[rbyid[i] for i in view.get("relationship_ids",[]) if i in rbyid]
    d=Drawing(view,profile,layout)
    from organization_derivation import validate_organization_derivations
    for finding in validate_organization_derivations(model, view.get('relationship_ids',[])):
        (d.errors if finding['level']=='error' else d.warnings).append(finding)
    d.states=model.get('states',[])
    d.scales={s["id"]:s for s in model.get("scales",[])}
    for i in view.get("entity_ids",[]):
        if i not in byid:d.errors.append({"code":"unknown-entity","id":i})
    for i in view.get("relationship_ids",[]):
        if i not in rbyid:d.errors.append({"code":"unknown-relationship","id":i})
    template=profile.get("template",{})
    if layout=="reference" and not template.get("source_verified",False):d.warnings.append("来源结构模板尚未独立核实；不得标为原图复现通过。")
    required=profile.get("required_attributes",{})
    def required_fields(e):
        return required.get(e["type"],[])+required.get("*",[]) if isinstance(required,dict) else required
    for e in es:
        for field in required_fields(e):
            if field=="name":continue
            if field not in e.get("attributes",{}) and not (profile.get('renderer')=='heatmap' and is_evaluation_field_satisfied(e,field,template,d.scales)):d.errors.append({"code":"missing-profile-attribute","id":e["id"],"attribute":field})
    renderer=profile.get("renderer","network")
    methods={"nested-map":nested,"heatmap":heatmap,"stage-map":stage_map,"network":network,"canvas":canvas,"environmental-review":environmental_review,"value-chain":value_chain,"er":network,"state":state_diagram,"deployment":deployment,"roadmap":roadmap,"matrix":matrix,"sequence":sequence,"quadrant":quadrant,"assessment":assessment,"catalog":assessment,"causal":causal_loop,
             "four-box":four_box,"cube":cube,"perspectives":perspectives,"lean-flow":lean_flow,"swimlane":swimlane,"canvas-compare":canvas_compare,"grouped-bands":grouped_bands,"metadata-map":metadata_map}
    methods['agile-sprints']=agile_sprints
    if renderer not in methods:
        d.errors.append({"code":"unsupported-renderer","renderer":renderer})
    else:
        if renderer=="causal":
            for r in rs:
                if r.get("attributes",{}).get("polarity") not in {"+","-","positive","negative"}:d.errors.append({"code":"missing-causal-polarity","id":r["id"]})
        if renderer=="er":
            for r in rs:
                if r["type"] in {"data_association","logical_association","information_association"} and not r.get("cardinality"):
                    d.errors.append({"code":"missing-er-cardinality","id":r["id"]})
        from source_shape_render import RENDERERS as source_shapes
        source_shapes.get(template.get('semantic_layout'), methods[renderer])(d,es,rs)
    svg, report = d.finish(es,rs)
    # Required attributes must be visible in the actual main/companion output.
    for e in es:
        for field in required_fields(e):
            if field=="name":continue
            if field in e.get("attributes",{}) and field not in d.attrs[e["id"]]:d.errors.append({"code":"attribute-not-expressed","id":e["id"],"attribute":field})
    report["review_status"]="draft-with-gaps" if report["errors"] or report["unrepresented_entity_ids"] or report["unrepresented_relationship_ids"] else "generated-awaiting-review"
    return svg, report
