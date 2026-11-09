"""Prove annotation geometry; repair blocked shared shafts with local doglegs."""
import math
import re
import heapq
import xml.etree.ElementTree as ET

NUM=r'-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

def overlap(a,b):
    return max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])

def expand(b,p):return (b[0]-p,b[1]-p,b[2]+p,b[3]+p)

def proper_contains(a,b):return a[0]<b[0] and a[1]<b[1] and a[2]>b[2] and a[3]>b[3]

def clipping(p,q,b):
    dx,dy=q[0]-p[0],q[1]-p[1];lo,hi=0.,1.
    for d,n in ((-dx,p[0]-b[0]),(dx,b[2]-p[0]),(-dy,p[1]-b[1]),(dy,b[3]-p[1])):
        if abs(d)<1e-9:
            if n<0:return None
        else:
            t=n/d
            if d<0:lo=max(lo,t)
            else:hi=min(hi,t)
            if lo>hi:return None
    return lo,hi

def departure_interval(a,b,step,box):
    """Project every box contact of a moving attachment segment onto its shaft.

    In (shaft parameter, departure parameter) coordinates the four rectangle
    constraints clip a unit square. Its exact projection gives all event
    boundaries; one midpoint per resulting open cell replaces blind sampling.
    """
    polygon=[(0.,0.),(1.,0.),(1.,1.),(0.,1.)]
    delta=(b[0]-a[0],b[1]-a[1])
    for axis,sign,bound in ((0,-1,-box[0]),(0,1,box[2]),(1,-1,-box[1]),(1,1,box[3])):
        coefficient=(sign*delta[axis],sign*step[axis]);limit=bound-sign*a[axis]
        if not polygon:return None
        output=[];previous=polygon[-1]
        prior=limit-coefficient[0]*previous[0]-coefficient[1]*previous[1]
        for current in polygon:
            value=limit-coefficient[0]*current[0]-coefficient[1]*current[1]
            if (prior>=0)!=(value>=0):
                t=prior/(prior-value)
                output.append((previous[0]+t*(current[0]-previous[0]),previous[1]+t*(current[1]-previous[1])))
            if value>=0:output.append(current)
            previous=current;prior=value
        polygon=output
    return (min(p[0] for p in polygon),max(p[0] for p in polygon)) if polygon else None

def geometry(parts):
    """Enumerate painted instances, never the entity-ID endpoint lookup map."""
    content=re.sub(r'__TOGAF_BADGE_\d+__','', ''.join(parts))
    root=ET.fromstring('<svg>'+content+'</svg>')
    cards=[];texts=[];segments=[];glyphs=[];unknown=[];rects=[];instances=[]
    def walk(e,offset=(0.,0.),rid=None,instance=None):
        transform=e.get('transform','')
        if transform:
            m=re.fullmatch(r'\s*translate\(\s*('+NUM+r')\s*[, ]\s*('+NUM+r')\s*\)\s*',transform)
            if not m:raise ValueError('annotation placement cannot prove transform: '+transform)
            offset=(offset[0]+float(m[1]),offset[1]+float(m[2]))
        rid=e.get('data-relationship-id',rid);tag=e.tag.rsplit('}',1)[-1]
        if tag=='g' and e.get('data-entity-id'):
            instance=len(instances);instances.append(e.get('data-entity-id'))
            for child in e:
                if child.tag.rsplit('}',1)[-1]=='rect' and all(child.get(k) is not None for k in ('x','y','width','height')):
                    x,y,w,h=(float(child.get(k)) for k in ('x','y','width','height'))
                    cards.append({'id':e.get('data-entity-id'),'instance':instance,'box':(x+offset[0],y+offset[1],x+w+offset[0],y+h+offset[1])})
        if tag=='rect' and all(e.get(k) is not None and '%' not in e.get(k) for k in ('x','y','width','height')):
            x,y,w,h=(float(e.get(k)) for k in ('x','y','width','height'))
            rects.append({'box':(x+offset[0],y+offset[1],x+w+offset[0],y+h+offset[1]),'instance':instance,'fill':e.get('fill','black'),'stroke':e.get('stroke','none'),'padding':float(e.get('stroke-width','1'))/2})
        if tag=='text' and e.get('x') is not None and e.get('y') is not None:
            value=''.join(e.itertext());size=float(e.get('font-size','16'));x=float(e.get('x'))+offset[0];y=float(e.get('y'))+offset[1]
            width=sum(size*(1.03 if ord(c)>255 else .66) for c in value)
            anchor=e.get('text-anchor','start');left=x-width/2 if anchor=='middle' else x-width if anchor=='end' else x
            texts.append((left-1,y-size-1,left+width+1,y+size*.28+1))
        if tag=='path' and e.get('stroke') not in (None,'none'):
            d=e.get('d','');commands=re.findall(r'[A-DF-Za-df-z]',d);v=[float(n) for n in re.findall(NUM,d)]
            points=[]
            if commands and all(c in ('M','L') for c in commands):points=list(zip(v[::2],v[1::2]))
            elif commands==['M','Q'] and len(v)==6:
                a,c,b=list(zip(v[::2],v[1::2]));points=[((1-t)**2*a[0]+2*t*(1-t)*c[0]+t*t*b[0],(1-t)**2*a[1]+2*t*(1-t)*c[1]+t*t*b[1]) for t in [i/32 for i in range(33)]]
            elif v:
                unknown.append({'d':d,'relationship_id':rid})
                # Conservative hull for an ornamental unsupported path. The
                # independent oracle records any unsupported computed case.
                points=list(zip(v[::2],v[1::2]))
            points=[(x+offset[0],y+offset[1]) for x,y in points]
            stroke=float(e.get('stroke-width','1'))/2
            for a,b in zip(points,points[1:]):segments.append({'id':rid,'points':(a,b),'box':expand((min(a[0],b[0]),min(a[1],b[1]),max(a[0],b[0]),max(a[1],b[1])),stroke)})
            if e.get('marker-end') and len(points)>1:
                p,q=points[-2:];length=math.dist(p,q)
                if length:
                    ux,uy=(q[0]-p[0])/length,(q[1]-p[1])/length;scale=stroke*2
                    verts=[(q[0]-8*scale*ux-4*scale*uy,q[1]-8*scale*uy+4*scale*ux),q,(q[0]-8*scale*ux+4*scale*uy,q[1]-8*scale*uy-4*scale*ux)]
                    glyphs.append(expand((min(x for x,y in verts),min(y for x,y in verts),max(x for x,y in verts),max(y for x,y in verts)),scale/2+.2))
        if tag=='polygon' and e.get('points'):
            v=[float(n) for n in re.findall(NUM,e.get('points'))];p=[(x+offset[0],y+offset[1]) for x,y in zip(v[::2],v[1::2])]
            if p:glyphs.append(expand((min(x for x,y in p),min(y for x,y in p),max(x for x,y in p),max(y for x,y in p)),float(e.get('stroke-width','1'))/2))
        for child in e:walk(child,offset,rid,instance)
    walk(root)
    for card in cards:
        a=card['box'];card['container']=any(card['instance']!=b['instance'] and proper_contains(a,b['box']) for b in cards)
    other_boxes=[]
    for rec in rects:
        b=rec['box'];pad=rec['padding']
        if any(b==c['box'] for c in cards):continue
        context=rec['instance'] is None and any(proper_contains(b,c['box']) for c in cards)
        if rec['fill']=='none' or context:
            if rec['stroke']!='none':other_boxes.extend((expand((b[0],b[1],b[2],b[1]),pad),expand((b[0],b[3],b[2],b[3]),pad),expand((b[0],b[1],b[0],b[3]),pad),expand((b[2],b[1],b[2],b[3]),pad)))
        else:other_boxes.append(expand(b,pad if rec['stroke']!='none' else 0))
    return {'cards':cards,'texts':texts,'segments':segments,'glyphs':glyphs,'other_boxes':other_boxes,'unknown_paths':unknown}

def card_obstacles(g,points):
    boxes=[]
    for card in g['cards']:
        b=card['box']
        inside=any(b[0]<p[0]<b[2] and b[1]<p[1]<b[3] for p in points)
        if card['container'] and inside:
            # A proved container has usable internal whitespace, but its
            # complete border and every text line remain obstacles.
            boxes.extend(((b[0]-.5,b[1]-.5,b[2]+.5,b[1]+.5),(b[0]-.5,b[3]-.5,b[2]+.5,b[3]+.5),(b[0]-.5,b[1],b[0]+.5,b[3]),(b[2]-.5,b[1],b[2]+.5,b[3])))
        else:boxes.append(expand(b,.5))
    return boxes

def badge_clear(d,box,rid,points):
    g=d.annotation_geometry;key=(rid,len(d.label_boxes))
    cache=getattr(d,'annotation_badge_index',None)
    if cache is None or cache[0]!=key:
        # Reserve a positive gap around every painted obstacle, including
        # actual container borders. Strict box overlap alone allows tangency.
        obstacles=[expand(ob,.1) for ob in card_obstacles(g,points)+g['other_boxes']+g['texts']+g['glyphs']+d.label_boxes+[s['box'] for s in g['segments'] if s['id']!=rid]]
        grid={}
        for i,b in enumerate(obstacles):
            for x in range(math.floor(b[0]/64),math.floor(b[2]/64)+1):
                for y in range(math.floor(b[1]/64),math.floor(b[3]/64)+1):grid.setdefault((x,y),set()).add(i)
        cache=(key,obstacles,grid);d.annotation_badge_index=cache
    _,obstacles,grid=cache;near=set()
    for x in range(math.floor(box[0]/64),math.floor(box[2]/64)+1):
        for y in range(math.floor(box[1]/64),math.floor(box[3]/64)+1):near.update(grid.get((x,y),()))
    if any(overlap(box,obstacles[i]) for i in near):return False
    return not any(any(clipping(a,b,expand(box,.5)) for a,b in zip(p,p[1:])) for p in d.annotation_leaders)

def leader_clear(d,path,rid,points,box):
    g=d.annotation_geometry;obstacles=card_obstacles(g,[path[0]])+g['other_boxes']+g['texts']+g['glyphs']+d.label_boxes
    anchor=path[0]
    if box is not None:
        # Only the final 1.25px may meet its badge border. Earlier segments
        # cannot enter or run along the white footprint before terminating.
        before=list(reversed(path));remaining=1.25
        while len(before)>1 and remaining>0:
            length=math.dist(before[0],before[1])
            if length<=remaining:remaining-=length;before.pop(0)
            else:
                a,b=before[:2];t=remaining/length
                before[0]=(a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]));remaining=0
        if any(clipping(a,b,expand(box,.5)) for a,b in zip(before,before[1:])):return False
    for i,(a,b) in enumerate(zip(path,path[1:])):
        if math.dist(a,b)<1e-8:continue
        if any(clipping(a,b,expand(ob,.5)) for ob in obstacles):return False
        for s in g['segments']:
            clip=clipping(a,b,expand(s['box'],.5))
            if clip is None:continue
            # The initial contact ends after the two actual stroke radii.
            # An anchor near a corner must not spend extra length following
            # its own shaft before departing; the independent audit trims
            # exactly this painted attachment radius.
            p,q=s['points'];ob=s['box']
            shaft_radius=max(min(p[0],q[0])-ob[0],min(p[1],q[1])-ob[1],ob[2]-max(p[0],q[0]),ob[3]-max(p[1],q[1]))
            if s['id']==rid and i==0 and clip[1]*math.dist(a,b)<=shaft_radius+.5+1e-7:continue
            return False
        for old in d.annotation_leaders:
            for p,q in zip(old,old[1:]):
                ob=expand((min(p[0],q[0]),min(p[1],q[1]),max(p[0],q[0]),max(p[1],q[1])),1.4)
                if clipping(a,b,ob):return False
    return True

def _badge_footprint(d,points,label,color,rid,compact=False,inline_only=False,repair_cache=None):
    """Prove a placement using the actual painted footprint and fixed paths."""
    width=len(label)*(6 if compact else 7)+(8 if compact else 10)
    height=15.6 if compact else 22;half_h=height/2
    font=11 if compact else 13;baseline=4 if compact else 5
    margin=.1 if compact else 1.1;g=d.annotation_geometry
    repair_cache={} if repair_cache is None else repair_cache
    footprint_results=repair_cache.setdefault(('badge',tuple(card_obstacles(g,points))),{})
    def clear_box(box):
        if box not in footprint_results:footprint_results[box]=badge_clear(d,box,rid,points)
        return footprint_results[box]
    segments=sorted(zip(points,points[1:]),key=lambda p:math.dist(*p),reverse=True)
    anchors=[]
    for a,b in segments:
        n=max(2,min(80,int(math.dist(a,b)/16)));ts={i/n for i in range(1,n)}|{.5,.35,.65,.2,.8}
        vertical=abs(a[0]-b[0])<1e-6;horizontal=abs(a[1]-b[1])<1e-6
        if vertical or horizontal:
            axis=1 if vertical else 0;lo,hi=sorted((a[axis],b[axis]));delta=b[axis]-a[axis]
            for ob in g['texts']+g['glyphs']+g['other_boxes']+[s['box'] for s in g['segments']]+card_obstacles(g,points):
                other=1-axis;reach=width/2+12 if vertical else 24
                if not ob[other]-reach<=a[other]<=ob[other+2]+reach:continue
                for bound in (ob[axis],ob[axis+2]):
                    for gap in (-.6,.6,-(half_h+.1),half_h+.1) if vertical else (-.6,.6,-(width/2+.1),width/2+.1):
                        v=bound+gap
                        if lo<v<hi:ts.add((v-a[axis])/delta)
        for t in sorted(ts,key=lambda t:abs(t-.5)):
            if 0<t<1:anchors.append((a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t,vertical,horizontal))
    # First preserve a direct, local reading on the actual connector.
    for ax,ay,vertical,horizontal in anchors:
        for shift in (0,3,-3,6,-6,9,-9):
            x=ax+(shift if vertical else 0);cy=ay+(shift if horizontal else 0)
            box=(x-width/2,cy-half_h,x+width/2,cy+half_h)
            if box[0]>=10 and box[1]>=78 and clear_box(box):
                return (x,cy+baseline,box,None,font)
    if inline_only:return None
    candidates=[]
    obstacles=card_obstacles(g,points)+g['other_boxes']+g['texts']+g['glyphs']+[s['box'] for s in g['segments']]+d.label_boxes
    leader_anchors=sorted(anchors,key=lambda p:(min(math.dist(p[:2],q) for q in points),p[0],p[1]))
    for ax,ay,vertical,horizontal in leader_anchors:
        point=(ax,ay)
        if any(clipping(point,point,expand(ob,.5)) for ob in card_obstacles(g,[point])+g['other_boxes']+g['texts']+g['glyphs']+d.label_boxes):continue
        if any(clipping(point,point,expand(ob['box'],.5)) for ob in g['segments'] if ob['id']!=rid):continue
        near_cards=[c['box'] for c in g['cards'] if c['box'][0]-180<=ax<=c['box'][2]+180 and c['box'][1]-180<=ay<=c['box'][3]+180]
        reach_x=max(360,max((b[2]-b[0] for b in near_cards),default=0)+width+40)
        route_budget=max(520,reach_x+80)
        xs={ax};ys={ay}
        for gap in (width/2+3,width/2+12,60,100,180,280):xs.update((ax-gap,ax+gap))
        for gap in (14,24,40,70,120,180):ys.update((ay-gap,ay+gap))
        for ob in obstacles:
            for x in (ob[0]-width/2-margin,ob[2]+width/2+margin):
                if abs(x-ax)<=reach_x:xs.add(x)
            for y in (ob[1]-half_h-margin,ob[3]+half_h+margin):
                if abs(y-ay)<=180:ys.add(y)
        # Use horizontal or vertical adjacency first. These are finite local
        # candidates derived from the actual obstacle boundaries, not page-end
        # placement that happens to look empty.
        centers={(x,ay) for x in xs}|{(ax,y) for y in ys}
        centers|={(x,y) for x in sorted(xs,key=lambda x:abs(x-ax))[:10] for y in sorted(ys,key=lambda y:abs(y-ay))[:10]}
        shifts=(width/2+3,width/2+12,60,100,180,280)
        centers|={(ax+side*shift,y) for y in ys for shift in shifts for side in (-1,1)}
        for ob in obstacles:
            for x in (ob[0]-width/2-margin,ob[2]+width/2+margin):
                for y in (ob[1]-half_h-margin,ob[3]+half_h+margin):
                    if abs(x-ax)<=reach_x and abs(y-ay)<=180:centers.add((x,y))
        for x,cy in sorted(centers,key=lambda p:(abs(p[0]-ax)+abs(p[1]-ay),p[0],p[1])):
            box=(x-width/2,cy-half_h,x+width/2,cy+half_h)
            if box[0]<10 or box[1]<78 or not clear_box(box):continue
            if abs(x-ax)>width/2:
                attach=(box[0] if x>ax else box[2],max(box[1],min(box[3],ay)))
            else:attach=(max(box[0],min(box[2],ax)),box[1] if cy>ay else box[3])
            target=attach;start=(ax,ay)
            routes=([start,(target[0],ay),target],[start,(ax,target[1]),target])
            for raw in routes:
                path=[raw[0]]
                for p in raw[1:]:
                    if p!=path[-1]:path.append(p)
                if len(path)<2:continue
                length=sum(math.dist(a,b) for a,b in zip(path,path[1:]))
                if length>route_budget:continue
                if leader_clear(d,path,rid,points,box):return (x,cy+baseline,box,path,font)
                candidates.append((length,len(path),abs(ay-segments[0][0][1]),x,cy,box,path))
    # If a corner needs another turn, try visibility rails at actual obstacle
    # boundaries. Every segment is rechecked, including the owner attachment.
    tried=set()
    for _,_,_,x,cy,box,path in sorted(candidates,key=lambda row:row[:5])[:1000]:
        start,end=path[0],path[-1];key=(start,end,box)
        if key in tried:continue
        tried.add(key)
        xs=set();ys=set()
        for ob in obstacles:
            for rail in (ob[0]-.6,ob[2]+.6):
                if min(start[0],end[0])-80<=rail<=max(start[0],end[0])+80:xs.add(rail)
            for rail in (ob[1]-.6,ob[3]+.6):
                if min(start[1],end[1])-80<=rail<=max(start[1],end[1])+80:ys.add(rail)
        routes=[[start,(rail,start[1]),(rail,end[1]),end] for rail in xs]+[[start,(start[0],rail),(end[0],rail),end] for rail in ys]
        for raw in sorted(routes,key=lambda row:sum(math.dist(a,b) for a,b in zip(row,row[1:]))):
            route=[raw[0]]
            for point in raw[1:]:
                if point!=route[-1]:route.append(point)
            if sum(math.dist(a,b) for a,b in zip(route,route[1:]))<=max(520,max((c['box'][2]-c['box'][0] for c in g['cards']),default=0)+width+120) and leader_clear(d,route,rid,points,box):return (x,cy+baseline,box,route,font)
    return None


def boundary_badge(d,points,label,color,rid,compact=False,repair_cache=None):
    """Search a finite deterministic arrangement from the painted obstacles.

    Local distance limits only rank the inexpensive first search. This fallback
    has no distance budget: its rails are actual obstacle edges, the footprint's
    supporting edges, and the finite exterior of the existing drawing. The
    Attachment events come from exact clipping and departure projections.
    Candidate rails and one shortest route per node bound the search; failure
    does not prove that no placement exists in the continuous drawing plane.
    """
    repair_cache={} if repair_cache is None else repair_cache
    g=d.annotation_geometry;width=len(label)*(6 if compact else 7)+(8 if compact else 10)
    height=15.6 if compact else 22;hh=height/2;font=11 if compact else 13
    baseline=4 if compact else 5;margin=.1
    fixed=g['other_boxes']+g['texts']+g['glyphs']+d.label_boxes
    other=[expand(s['box'],.5) for s in g['segments'] if s['id']!=rid]
    old=[expand((min(a[0],b[0]),min(a[1],b[1]),max(a[0],b[0]),max(a[1],b[1])),1.4)
         for leader in d.annotation_leaders for a,b in zip(leader,leader[1:])]
    sources=[]
    for a,b in zip(points,points[1:]):
        length=math.dist(a,b)
        if length<1e-8:continue
        source_obstacles=[expand(ob,.5) for ob in card_obstacles(g,points)+fixed]+other+old
        blocked=[clipping(a,b,ob) for ob in source_obstacles]
        merged=[]
        for lo,hi in sorted(c for c in blocked if c is not None):
            if merged and lo<=merged[-1][1]:merged[-1]=(merged[-1][0],max(hi,merged[-1][1]))
            else:merged.append((lo,hi))
        free=[];end=0.
        for lo,hi in merged:
            if lo>end:free.append((end,lo))
            end=max(end,hi)
        if end<1:free.append((end,1.))
        nx,ny=-(b[1]-a[1])/length,(b[0]-a[0])/length
        for lo,hi in free:
            if hi<=lo:continue
            for sign in (-1,1):
                step=(sign*nx*1.5,sign*ny*1.5);cuts={lo,hi}
                # Departure visibility, container status, and the free endpoint
                # of the attachment change only at these projected boundaries.
                events=source_obstacles+[expand(c['box'],1.) for c in g['cards']]
                for ob in events:
                    contact=departure_interval(a,b,step,ob)
                    if contact is not None:cuts.update(t for t in contact if lo<t<hi)
                shifted_a=(a[0]+step[0],a[1]+step[1]);shifted_b=(b[0]+step[0],b[1]+step[1])
                for s in g['segments']:
                    if s['id']!=rid:continue
                    contact=clipping(shifted_a,shifted_b,expand(s['box'],.5))
                    if contact is not None:cuts.update(t for t in contact if lo<t<hi)
                for card in g['cards']:
                    contact=clipping(a,b,card['box'])
                    if contact is not None:cuts.update(t for t in contact if lo<t<hi)
                ordered=sorted(cuts)
                samples=[]
                for begin,end in zip(ordered,ordered[1:]):
                    if end<=begin:continue
                    inset=min(.1/length,(end-begin)/4)
                    samples.extend((begin+inset,(begin+end)/2,end-inset))
                for t in samples:
                    anchor=(a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t)
                    depart=(anchor[0]+step[0],anchor[1]+step[1])
                    if depart[0]<10 or depart[1]<78:continue
                    if leader_clear(d,[anchor,depart],rid,points,None):sources.append((anchor,depart))
    if not sources:return None
    # Container exemptions are anchor-local. Distinct enclosing components
        # receive separate arrangements, retaining their complete borders.
    groups={}
    for anchor,depart in sources:
        cards=tuple(card_obstacles(g,[anchor]));groups.setdefault(cards,[]).append((anchor,depart))
    for cards,starts in groups.items():
        paint=list(cards)+fixed+[s['box'] for s in g['segments']]
        obstacles=[expand(ob,.5) for ob in paint]+old
        # Across a dogleg search only the owner's tiny segment overlay changes.
        # Keep the immutable other paint/index and its exact visibility results;
        # recheck every owner segment for every candidate and edge.
        base_key=('base',cards)
        base=repair_cache.get(base_key)
        if base is None:
            base_obstacles=[expand(ob,.5) for ob in list(cards)+fixed+[s['box'] for s in g['segments'] if s['id']!=rid]]+old
            index={}
            for i,ob in enumerate(base_obstacles):
                for ix in range(math.floor(ob[0]/64),math.floor(ob[2]/64)+1):
                    for iy in range(math.floor(ob[1]/64),math.floor(ob[3]/64)+1):index.setdefault((ix,iy),set()).add(i)
            base=(base_obstacles,index,{})
            repair_cache[base_key]=base
        base_obstacles,index,base_clear_cache=base
        owner_obstacles=[expand(s['box'],.5) for s in g['segments'] if s['id']==rid]
        edge_cache={}
        badge_key=('badge',tuple(card_obstacles(g,points)))
        box_cache=repair_cache.setdefault(badge_key,{})
        def clear(a,b):
            key=(a,b) if a<=b else (b,a)
            if key in edge_cache:return edge_cache[key]
            base_value=base_clear_cache.get(key)
            if base_value is None:
                nearby=set()
                for ix in range(math.floor(min(a[0],b[0])/64),math.floor(max(a[0],b[0])/64)+1):
                    for iy in range(math.floor(min(a[1],b[1])/64),math.floor(max(a[1],b[1])/64)+1):nearby.update(index.get((ix,iy),()))
                base_value=not any(clipping(a,b,base_obstacles[i]) for i in nearby)
                base_clear_cache[key]=base_value
            left,right=sorted((a[0],b[0]));top,bottom=sorted((a[1],b[1]))
            value=base_value and not any(clipping(a,b,ob) for ob in owner_obstacles if ob[0]<=right and ob[2]>=left and ob[1]<=bottom and ob[3]>=top)
            edge_cache[key]=value;return value
        def footprint_clear(box):
            if box not in box_cache:box_cache[box]=badge_clear(d,box,rid,points)
            return box_cache[box]
        xs={10.};ys={78.}
        right=max([getattr(d,'width',1100)]+[ob[2] for ob in obstacles])+width+20
        bottom=max([getattr(d,'height',180)]+[ob[3] for ob in obstacles])+height+20
        xs.add(right);ys.add(bottom)
        for anchor,depart in starts:xs.add(depart[0]);ys.add(depart[1])
        for ob in obstacles:
            xs.update((ob[0]-margin,ob[2]+margin));ys.update((ob[1]-margin,ob[3]+margin))
        # Supporting positions for all four badge attachment edges. A feasible
        # rectangle in an orthogonal free cell can be translated to a support
        # edge without crossing paint; these coordinates include supporting
        # candidates without claiming every continuous placement is searched.
        for ob in paint+d.label_boxes:
            for x in (ob[0]-margin,ob[2]+margin):xs.update((x,x-width,x+width,x-width/2,x+width/2))
            for y in (ob[1]-margin,ob[3]+margin):ys.update((y,y-height,y+height,y-hh,y+hh))
        xs=sorted(x for x in xs if 10<=x<=right);ys=sorted(y for y in ys if 78<=y<=bottom)
        xpos={x:i for i,x in enumerate(xs)};ypos={y:i for i,y in enumerate(ys)}
        heap=[];dist={};prev={};origin={};serial=0
        for anchor,depart in starts:
            if not clear(depart,depart):continue
            node=(xpos[depart[0]],ypos[depart[1]])
            if node in dist:continue
            dist[node]=math.dist(anchor,depart);prev[node]=None;origin[node]=anchor
            heapq.heappush(heap,(dist[node],serial,node));serial+=1
        while heap:
            cost,_,node=heapq.heappop(heap)
            if cost!=dist[node]:continue
            ix,iy=node;x,y=xs[ix],ys[iy]
            boxes=((x,y-hh,x+width,y+hh),(x-width,y-hh,x,y+hh),
                   (x-width/2,y,x+width/2,y+height),(x-width/2,y-height,x+width/2,y))
            for box in boxes:
                if box[0]<10 or box[1]<78 or not footprint_clear(box):continue
                path=[];cursor=node
                while cursor is not None:
                    path.append((xs[cursor[0]],ys[cursor[1]]));cursor=prev[cursor]
                path=[origin[node]]+list(reversed(path))
                simple=[]
                for p in path:
                    if simple and p==simple[-1]:continue
                    if len(simple)>1 and abs((simple[-1][0]-simple[-2][0])*(p[1]-simple[-1][1])-(simple[-1][1]-simple[-2][1])*(p[0]-simple[-1][0]))<1e-8:simple[-1]=p
                    else:simple.append(p)
                if leader_clear(d,simple,rid,points,box):
                    return ((box[0]+box[2])/2,(box[1]+box[3])/2+baseline,box,simple,font)
            for nxt in ((ix-1,iy),(ix+1,iy),(ix,iy-1),(ix,iy+1)):
                if not (0<=nxt[0]<len(xs) and 0<=nxt[1]<len(ys)):continue
                q=(xs[nxt[0]],ys[nxt[1]])
                new=cost+math.dist((x,y),q)
                if new>=dist.get(nxt,float('inf')) or not clear((x,y),q):continue
                dist[nxt]=new;prev[nxt]=node;origin[nxt]=origin[node]
                heapq.heappush(heap,(new,serial,nxt));serial+=1
    return None


def local_badge(d,points,label,color,rid):
    """Prefer standard placement before a compact annotation fallback.

    A compact footprint keeps the complete numbered relation label in a fixed
    16px channel without moving cards or business connectors. Its actual font
    and white badge dimensions are returned together for the SVG painter.
    """
    for compact in (False,True):
        result=_badge_footprint(d,points,label,color,rid,compact)
        if result is not None:return result
        result=boundary_badge(d,points,label,color,rid,compact)
        if result is not None:return result
    raise ValueError('no proved annotation placement for '+str(rid)+' '+label)


def repair_route(d,points,label,color,rid):
    """Create an attachment interval after both footprint candidate searches fail.

    The trigger is geometric collinear overlap with another painted shaft or
    context border. Finite dogleg rails and entry/return points are derived
    from those obstacles. Endpoints, first/last directions, and every SVG path
    attribute other than d are preserved. New business crossings are audited.
    """
    g=d.annotation_geometry;path_parts=[]
    for i,part in enumerate(d.parts):
        if part.startswith('<path ') and 'data-annotation-leader' not in part:
            e=ET.fromstring(part)
            if e.get('data-relationship-id')==rid:path_parts.append((i,e,part))
    if len(path_parts)!=1:raise ValueError('route repair requires one explicit owner path: '+str(rid))
    part_index,e,original_part=path_parts[0];stroke=float(e.get('stroke-width','1.8'))/2
    original=[tuple(p) for p in points];all_obstacles=card_obstacles(g,points)+g['texts']+g['other_boxes']+g['glyphs']+[s['box'] for s in g['segments']]+d.label_boxes
    options=[];seeds=[];overlaps=[]
    for segment_index,(a,b) in enumerate(zip(original,original[1:])):
        horizontal=abs(a[1]-b[1])<1e-8;vertical=abs(a[0]-b[0])<1e-8
        if not (horizontal or vertical):continue
        axis=0 if horizontal else 1;normal=1-axis;length=math.dist(a,b)
        if length<6:continue
        lo,hi=sorted((a[axis],b[axis]));direction=1 if b[axis]>a[axis] else -1
        shared=[]
        for s in g['segments']:
            p,q=s['points']
            if s['id']==rid or abs(p[normal]-q[normal])>1e-8 or abs(p[normal]-a[normal])>1e-8:continue
            overlap_length=min(hi,max(p[axis],q[axis]))-max(lo,min(p[axis],q[axis]))
            if overlap_length>1e-8:shared.append({'other_relationship_id':s['id'],'length':overlap_length})
        for ob in g['other_boxes']:
            if ob[normal]<=a[normal]<=ob[normal+2] and ob[normal+2]-ob[normal]<4:
                overlap_length=min(hi,ob[axis+2])-max(lo,ob[axis])
                if overlap_length>1e-8:shared.append({'context_border':ob,'length':overlap_length})
        if not shared:continue
        overlaps.append({'segment_index':segment_index,'overlaps':shared})
        rails=set();critical={a[axis]+direction*3,b[axis]-direction*3}
        blocked=[]
        for ob in [expand(ob,.5) for ob in card_obstacles(g,points)+g['texts']+g['glyphs']+g['other_boxes']+d.label_boxes]+[expand(s['box'],.5) for s in g['segments'] if s['id']!=rid]:
            hit=clipping(a,b,ob)
            if hit is not None:blocked.append(hit)
        merged=[]
        for begin,end in sorted(blocked):
            if merged and begin<=merged[-1][1]:merged[-1]=(merged[-1][0],max(end,merged[-1][1]))
            else:merged.append((begin,end))
        free=[];end=0.
        for begin,finish in merged:
            if begin>end:free.append((end,begin))
            end=max(end,finish)
        if end<1:free.append((end,1.))
        entries=[]
        for begin,end in free:
            if (end-begin)*length>.2:entries.append(a[axis]+(b[axis]-a[axis])*(begin+end)/2)
        for ob in all_obstacles:
            for bound in (ob[normal],ob[normal+2]):
                rails.update((bound,bound-stroke-.1,bound+stroke+.1,bound-1.5,bound+1.5))
            for bound in (ob[axis],ob[axis+2]):
                for gap in (0,-.1,.1,-1.5,1.5,-7.9,7.9,-11.1,11.1):
                    value=bound+gap
                    if lo+1.5<value<hi-1.5:critical.add(value)
        pairs={(a[axis]+direction*3,b[axis]-direction*3)}
        for entry in entries:
            for value in critical:
                p,q=(entry,value) if direction*(value-entry)>0 else (value,entry)
                if direction*(q-p)>.2:pairs.add((p,q))
        standard_normal=22 if horizontal else len(label)*7+10
        compact_normal=15.6 if horizontal else len(label)*6+8
        distances={40.,70.,120.}
        for footprint in (standard_normal,compact_normal):distances.update((footprint/2+stroke+2,footprint+stroke+2))
        for distance in sorted(distances):
            for sign in (-1,1):
                rail=a[normal]+sign*distance
                if rail<(10 if normal==0 else 78):continue
                p=a[axis]+direction*3;q=b[axis]-direction*3
                pa=list(a);pa[axis]=p;qa=list(a);qa[axis]=q
                pp=list(pa);pp[normal]=rail;qq=list(qa);qq[normal]=rail
                replacement=original[:segment_index+1]+[tuple(pa),tuple(pp),tuple(qq),tuple(qa)]+original[segment_index+1:]
                seeds.append((2*distance,abs(p-q),segment_index,replacement))
        for rail in rails:
            if rail<10 if normal==0 else rail<78:continue
            if abs(rail-a[normal])<.1:continue
            for p,q in pairs:
                pa=list(a);pa[axis]=p;qa=list(a);qa[axis]=q
                pp=list(pa);pp[normal]=rail;qq=list(qa);qq[normal]=rail
                replacement=original[:segment_index+1]+[tuple(pa),tuple(pp),tuple(qq),tuple(qa)]+original[segment_index+1:]
                options.append((2*abs(rail-a[normal]),abs(p-q),segment_index,replacement))
    if not overlaps:raise ValueError('unplaceable annotation has no collinear route-repair trigger: '+str(rid))
    old_segments=g['segments'];old_cache=getattr(d,'annotation_badge_index',None)
    checked=0;seen=set();repair_cache={}
    badge_index_cache={tuple(card_obstacles(g,points)):old_cache}
    protected=card_obstacles(g,points)+g['texts']+d.label_boxes
    # Markers at the same preserved endpoint retain exactly their old shape.
    protected+= [ob for ob in g['glyphs'] if not (ob[0]<=original[-1][0]<=ob[2] and ob[1]<=original[-1][1]<=ob[3])]
    old_pairs=set(zip(original,original[1:]));paint_cache={}
    def segment_paint_clear(a,b,first,last):
        key=(a,b,first,last)
        if key in paint_cache:return paint_cache[key]
        size=math.dist(a,b);clear=True
        for ob in protected:
            hit=clipping(a,b,expand(ob,stroke))
            if hit is None:continue
            if first and hit[1]*size<=1.5:continue
            if last and (1-hit[0])*size<=1.5:continue
            clear=False;break
        if clear:
            for old in d.annotation_leaders:
                for p,q in zip(old,old[1:]):
                    if clipping(a,b,expand((min(p[0],q[0]),min(p[1],q[1]),max(p[0],q[0]),max(p[1],q[1])),stroke+.5+.4)):
                        clear=False;break
                if not clear:break
        paint_cache[key]=clear;return clear
    def paint_clear(replacement):
        for i,(a,b) in enumerate(zip(replacement,replacement[1:])):
            if (a,b) in old_pairs:continue
            if not segment_paint_clear(a,b,i==0,i==len(replacement)-2):return False
        return True
    def candidate_rank(row):
        delta,span,index,replacement=row;a,b=original[index:index+2]
        normal_footprint=22 if abs(a[1]-b[1])<1e-8 else len(label)*7+10
        room=delta/2>=normal_footprint/2+1.1
        return (not room,delta,-span,index,replacement)
    fallback=[];fallback_limit=12
    def install(replacement):
        substitute=[{'id':rid,'points':(a,b),'box':expand((min(a[0],b[0]),min(a[1],b[1]),max(a[0],b[0]),max(a[1],b[1])),stroke)} for a,b in zip(replacement,replacement[1:]) if a!=b]
        d.annotation_geometry={**g,'segments':[s for s in old_segments if s['id']!=rid]+substitute}
        card_signature=tuple(card_obstacles(g,replacement))
        d.annotation_badge_index=badge_index_cache.get(card_signature)
        return card_signature
    def commit(delta,replacement,result,phase):
        before=e.get('d');after='M'+' L'.join(str(round(x,4))+' '+str(round(y,4)) for x,y in replacement)
        d.parts[part_index]=original_part.replace('d="'+before+'"','d="'+after+'"',1)
        repairs=getattr(d,'annotation_route_repairs',[])
        repairs.append({'relationship_id':rid,'label':label,'before':before,'after':after,'before_points':original,'after_points':replacement,'length_delta':delta,'trigger_overlaps':overlaps,'finite_candidates_checked':checked,'search_phase':phase,'visibility_candidate_limit':fallback_limit,'global_minimum_claimed':False,'endpoints_unchanged':True,'path_attributes_except_d_unchanged':True})
        d.annotation_route_repairs=repairs
        return replacement,result
    try:
        # Prefer rails with room for a standard footprint. Cheap checks visit
        # the deterministic dogleg set before any full visibility graph; this
        # bounds expensive fallback work without claiming a global minimum.
        representatives={}
        for row in options:
            delta,span,index,replacement=row
            rail=replacement[index+2]
            key=(index,rail[1] if abs(original[index][1]-original[index+1][1])<1e-8 else rail[0])
            previous=representatives.get(key)
            if previous is None or (-span,replacement)<(-previous[1],previous[3]):representatives[key]=row
        stages=(('seed-inline',seeds),('rail-representative-inline',list(representatives.values())),('remaining-inline',options))
        ordered=[(phase,row) for phase,rows in stages for row in sorted(rows,key=candidate_rank)]
        for phase,(delta,span,segment_index,replacement) in ordered:
            key=tuple(replacement)
            if key in seen:continue
            seen.add(key)
            if not paint_clear(replacement):continue
            checked+=1
            card_signature=install(replacement)
            result=None
            for compact in (False,True):
                result=_badge_footprint(d,replacement,label,color,rid,compact,inline_only=True,repair_cache=repair_cache)
                if result is not None:break
            badge_index_cache[card_signature]=d.annotation_badge_index
            if result is not None:return commit(delta,replacement,result,phase)
            if len(fallback)<fallback_limit:fallback.append((delta,replacement))
        for delta,replacement in fallback:
            card_signature=install(replacement);result=None
            for compact in (False,True):
                result=_badge_footprint(d,replacement,label,color,rid,compact,repair_cache=repair_cache)
                if result is None:result=boundary_badge(d,replacement,label,color,rid,compact,repair_cache=repair_cache)
                if result is not None:break
            badge_index_cache[card_signature]=d.annotation_badge_index
            if result is not None:return commit(delta,replacement,result,'bounded-visibility')
    finally:
        if d.parts[part_index]==original_part:d.annotation_geometry=g;d.annotation_badge_index=old_cache
    raise ValueError('no safe annotation in bounded collinear dogleg candidates: '+str(rid)+' '+label)
