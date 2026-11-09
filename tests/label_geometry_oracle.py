"""Independent SVG clipping checks; no renderer placement state is consulted."""
import math
import re
import xml.etree.ElementTree as ET

NUMBER = r'-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'


def intersects(p, q, box):
    left,top,right,bottom=box
    dx,dy=q[0]-p[0],q[1]-p[1]
    low,high=0.,1.
    for divisor,numerator in ((-dx,p[0]-left),(dx,right-p[0]),(-dy,p[1]-top),(dy,bottom-p[1])):
        if abs(divisor)<1e-9:
            if numerator<0:return False
        else:
            ratio=numerator/divisor
            if divisor<0:low=max(low,ratio)
            else:high=min(high,ratio)
            if low>high:return False
    return True


def positioned(root):
    rows=[];unsupported=[]
    def walk(e,offset=(0.,0.),rid=None):
        transform=e.get('transform','')
        if transform:
            match=re.fullmatch(r'\s*translate\(\s*('+NUMBER+r')\s*[, ]\s*('+NUMBER+r')\s*\)\s*',transform)
            if not match:unsupported.append(transform);return
            offset=(offset[0]+float(match[1]),offset[1]+float(match[2]))
        rid=e.get('data-relationship-id',rid)
        rows.append((e,offset,rid))
        for child in e:walk(child,offset,rid)
    walk(root)
    return rows,unsupported


def inspect(svg,coverage=None):
    root=ET.fromstring(svg);rows,transforms=positioned(root)
    markers={e.get('id'):e for e in root.iter() if e.tag.endswith('}marker')}
    label_candidates={};badges=[];shafts=[];arrows=[];unsupported=[];paths={};leaders=[];unmapped=[];ambiguous=[];contradictions=[]
    def register_label(number,owner):
        label_candidates.setdefault(number,set()).add(owner)
    for e in root.iter():
        if not e.tag.endswith('}g') or not e.get('data-relationship-id'):continue
        match=re.match(r'^\s*\[(\d+)\]', ''.join(e.itertext()))
        if match:register_label(match[1],e.get('data-relationship-id'))
    for row in ((coverage or {}).get('detail_ledger') or {}).get('relationships',[]):
        if row.get('index') is not None:register_label(str(row['index']),row['id'])
    latest_relationship_path=None
    for index,(e,offset,rid) in enumerate(rows):
        tag=e.tag.rsplit('}',1)[-1]
        if tag=='path' and rid and e.get('data-annotation-leader')!='true':latest_relationship_path=rid
        if tag=='rect' and e.get('fill')=='white' and e.get('stroke')=='none' and e.get('height')=='22':
            x,y,w,h=(float(e.get(k)) for k in ('x','y','width','height'))
            text=rows[index+1][0].text if index+1<len(rows) and rows[index+1][0].tag.endswith('}text') else ''
            number=re.match(r'^\[(\d+)\]',text or '')
            candidates=label_candidates.get(number[1],set()) if number else set()
            owner=next(iter(candidates)) if len(candidates)==1 else None
            method='SVG/companion numbered ledger' if owner else 'immediately preceding relationship path'
            if len(candidates)>1:
                ambiguous.append({'index':index,'text':text,'candidate_relationship_ids':sorted(candidates)})
            elif owner is None:owner=latest_relationship_path
            elif latest_relationship_path is not None and owner!=latest_relationship_path:
                contradictions.append({'index':index,'text':text,'ledger_relationship_id':owner,'preceding_relationship_id':latest_relationship_path})
            if owner is None:unmapped.append({'index':index,'text':text})
            badges.append({'id':owner,'index':index,'box':(x+offset[0],y+offset[1],x+w+offset[0],y+h+offset[1]),'owner_mapping':method})
        if tag!='path':continue
        if e.get('data-annotation-leader')=='true':leaders.append({**e.attrib,'owner_relationship_id':latest_relationship_path});continue
        d=e.get('d','');commands=re.findall(r'[A-DF-Za-df-z]',d)
        values=[float(n) for n in re.findall(NUMBER,d)]
        if rid:paths[rid]=dict(e.attrib)
        if rid and commands and all(c in ('M','L') for c in commands) and len(values)>=4:
            points=[(x+offset[0],y+offset[1]) for x,y in zip(values[::2],values[1::2])]
            shafts.append({'id':rid,'index':index,'points':points,'padding':float(e.get('stroke-width','1'))/2})
        if not e.get('marker-end'):continue
        if not commands or any(c not in ('M','L','Q') for c in commands) or len(values)<4:
            unsupported.append({'id':rid,'d':d,'kind':'marker'});continue
        points=list(zip(values[::2],values[1::2]));endpoint,prior=points[-1],points[-2]
        vx,vy=endpoint[0]-prior[0],endpoint[1]-prior[1];length=math.hypot(vx,vy)
        if not length:unsupported.append({'id':rid,'d':d,'kind':'zero-tangent'});continue
        ux,uy=vx/length,vy/length
        match=re.fullmatch(r'url\(#([^)]*)\)',e.get('marker-end'));marker=markers.get(match[1]) if match else None
        shape=next((c for c in marker if c.tag.endswith('}path')),None) if marker is not None else None
        if shape is None or shape.get('d')!='M0 0 L8 4 L0 8':
            unsupported.append({'id':rid,'d':d,'kind':'unsupported-marker-shape'});continue
        scale=float(e.get('stroke-width','1')) if marker.get('markerUnits','strokeWidth')=='strokeWidth' else 1.
        vertices=[]
        for mx,my in ((0.,0.),(8.,4.),(0.,8.)):
            mx=(mx-float(marker.get('refX','0')))*scale;my=(my-float(marker.get('refY','0')))*scale
            vertices.append((endpoint[0]+offset[0]+mx*ux-my*uy,endpoint[1]+offset[1]+mx*uy+my*ux))
        arrows.append({'id':rid,'index':index,'points':vertices,'padding':scale*float(shape.get('stroke-width','1'))/2})
    arrow_conflicts=[];shaft_conflicts=[]
    for kind,items,destination in (('arrow',arrows,arrow_conflicts),('shaft',shafts,shaft_conflicts)):
        for path in items:
            for badge in badges:
                if kind=='shaft' and badge['id']==path['id']:continue
                if kind=='arrow' and badge['index']<=path['index']:continue
                box=badge['box'];padding=path['padding'];expanded=(box[0]-padding,box[1]-padding,box[2]+padding,box[3]+padding)
                if any(intersects(p,q,expanded) for p,q in zip(path['points'],path['points'][1:])):
                    destination.append({'relationship_id':path['id'],'badge_owner':badge['id'],'box':box,'path_index':path['index'],'badge_index':badge['index']})
    return {'badges':len(badges),'checked_marker_paths':len(arrows),'checked_relationship_polyline_paths':len(shafts),
            'unsupported_marker_paths':unsupported,'unsupported_transforms':transforms,
            'arrow_conflicts':arrow_conflicts,'other_shaft_conflicts':shaft_conflicts,
            'annotation_leaders':leaders,'relationship_paths':paths,'unmapped_badge_owners':unmapped,'badge_records':badges,
            'ambiguous_badge_owners':ambiguous,'contradictory_badge_owners':contradictions}
