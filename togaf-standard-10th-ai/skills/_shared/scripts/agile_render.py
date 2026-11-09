# -*- coding: utf-8 -*-
"""Dedicated sprint/DORP collaboration layout; no generic graph fallback.

Spatial roles are explicit view data. Relation types separate forward handoff
from same-sprint, symmetric collaboration. Detail strips remain inside the SVG.
"""
import html,json,math
from collections import defaultdict

def agile_sprints(d,es,rs):
    esc=lambda x:html.escape(str(x),quote=True)
    fmt=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))if isinstance(x,(dict,list))else str(x)
    by={e['id']:e for e in es};config=d.view.get('attributes',{}).get('sprint_pattern',{})
    lanes=config.get('lanes',[]);laneids=[x['id']for x in lanes]
    sprintes=sorted((e for e in es if e['type']=='guide:agile_sprint'),key=lambda e:e['attributes']['order'])
    sprintids=[e['id']for e in sprintes]
    if not lanes or not sprintes:
        d.errors.append({'code':'agile-lanes-or-sprints-missing','id':d.view['id']});return
    activities=[e for e in es if e['type']=='guide:agile_activity'];gates=[e for e in es if e['type']=='guide:dorp_gate']
    contexts=[e for e in es if e['type']=='guide:agile_context']
    known={'guide:agile_sprint','guide:agile_activity','guide:dorp_gate','guide:agile_context'}
    for e in es:
        if e['type']not in known:d.errors.append({'code':'unsupported-agile-entity','id':e['id']})
        if e['type']in {'guide:agile_activity','guide:dorp_gate'}and e['attributes'].get('sprint_ref')not in sprintids:d.errors.append({'code':'agile-unknown-sprint','id':e['id']})
        if e['type']=='guide:agile_activity'and e['attributes'].get('lane')not in laneids:d.errors.append({'code':'agile-unknown-lane','id':e['id']})
    # More columns in source structure, fewer wider columns per adaptive panel.
    per=len(sprintes)if d.layout=='reference'else int(config.get('adaptive_columns',2))
    cw=420 if d.layout=='reference'else 510;left=175;gap=28;gatew=100;cardw=cw-gatew-34
    laneheight=max([d.card_height(e,cardw,fields=['team','capabilities','work'])for e in activities]+[d.card_height(e,cardw,fields=['business_change'])for e in contexts if e['attributes'].get('role')!='terminal']+[180])+100
    d.text(30,108,config.get('decision','协作模式按团队能力和业务需要选择；不是成熟度评分。'),14,units=145)
    y=155;placements={};panel_for={};gate_by={g['attributes']['sprint_ref']:g for g in gates}
    # Context exists once and retains a stable object ID; its temporal connection is explicit.
    for panel,start in enumerate(range(0,len(sprintes),per)):
        selected=sprintes[start:start+per];headerh=max(d.card_height(e,cw,fields=['timebox','goal'])for e in selected);bodytop=y+headerh+55;bodybottom=bodytop+laneheight*len(lanes)
        d.text(30,y+20,('来源结构片段'if d.layout=='reference'else'业务适配分图')+' '+str(panel+1)+' · '+config.get('pattern_label',''),17)
        for li,lane in enumerate(lanes):
            ly=bodytop+li*laneheight;d.rect(25,ly,left+len(selected)*(cw+gap)-40,laneheight-10,'#f5f8fb','#d9e3eb',3)
            d.text(40,ly+35,lane['label'],15,units=16)
        for ci,sprint in enumerate(selected):
            sid=sprint['id'];x=left+ci*(cw+gap);panel_for[sid]=panel
            d.card(sprint,x,y+35,cw,headerh,'#e2edf8',fields=['timebox','goal'])
            if start==0 and ci==0:
                for e in [z for z in contexts if z['attributes'].get('role')!='terminal']:
                    d.card(e,x+6,bodytop+54,cardw,None,'#edf4f8',fields=['business_change'])
            # Every sprint has one explicit DORP boundary; missing gates are gaps.
            gate=gate_by.get(sid)
            if not gate:d.errors.append({'code':'missing-dorp-gate','id':sid})
            else:
                gx=x+cw-gatew;d.parts.append('<g data-entity-id="'+esc(gate['id'])+'">')
                d.rect(gx,bodytop-4,gatew,bodybottom-bodytop+8,'#f4bb82','#b57943',2)
                d.text(gx+gatew/2,bodytop+23,gate['name'],14,anchor='middle',units=13)
                d.positions[gate['id']]=(gx,bodytop,gatew,bodybottom-bodytop);d.entity_ids.add(gate['id']);placements[gate['id']]=(panel,gx,bodytop,gatew,bodybottom-bodytop)
                # Output markers belong to DORP. They are not process vertices.
                for out in gate['attributes'].get('outputs',[]):
                    lane=out.get('lane',laneids[0]);li=laneids.index(lane)if lane in laneids else 0
                    cy=bodytop+li*laneheight+laneheight*.55;rx=43;ry=31
                    dash=' stroke-dasharray="5 3"'if out.get('necessity')=='optional'else''
                    d.parts.append(f'<ellipse cx="{gx+50}" cy="{cy}" rx="{rx}" ry="{ry}" fill="white" stroke="#4b657a"{dash}/>')
                    d.text(gx+50,cy+5,out.get('kind','?'),13,anchor='middle',units=10)
                    outid=str(out.get('id',''));shortid=outid if len(outid)<=18 else '…'+outid[-16:]
                    d.text(gx+50,cy+53,shortid,10,anchor='middle',units=18)
                d.parts.append('</g>')
            for activity in [e for e in activities if e['attributes'].get('sprint_ref')==sid]:
                a=activity['attributes'];li=laneids.index(a['lane'])if a['lane']in laneids else 0;cy=bodytop+li*laneheight+54
                h=d.card_height(activity,cardw,fields=['team','capabilities','work']);px=x+6
                count=a.get('parallel_teams',1)
                if isinstance(count,int)and count>1:
                    for layer in range(min(count-1,3),0,-1):
                        off=layer*5;d.rect(px+off,cy-off,cardw,h,'#ffffff','#91a5b4',4)
                    if count>4:d.text(px,cy-22,'并行团队数量：'+str(count),11)
                d.card(activity,px,cy,cardw,h,'#e6f0e9',fields=['team','capabilities','work'])
                placements[activity['id']]=(panel,px,cy,cardw,h)
        y=bodybottom+75;d.height=max(d.height,y)
    for e in [x for x in contexts if x['attributes'].get('role')=='terminal']:
        d.card(e,left+len(selected)*(cw+gap),bodytop+54,300,None,'#e2edf8')
    # Explicit route styles. Cross-panel relations use paired labelled ports.
    ports=defaultdict(int);routes=defaultdict(int)
    for i,r in enumerate(rs,1):
        typ=r['type'];a=by.get(r['source']);b=by.get(r['target']);ap=d.positions.get(r['source']);bp=d.positions.get(r['target'])
        if not ap or not bp:d.errors.append({'code':'agile-relation-endpoint-not-placed','id':r['id']});continue
        aa=a.get('attributes',{});bb=b.get('attributes',{});sa=aa.get('sprint_ref',a['id']if a['type']=='guide:agile_sprint'else None);sb=bb.get('sprint_ref',b['id']if b['type']=='guide:agile_sprint'else None)
        x1,y1,w1,h1=ap;x2,y2,w2,h2=bp;label='['+str(i)+']';color='#238b92'if typ=='guide:agile_collaborates'else'#365e82'
        if typ=='guide:agile_collaborates':
            if sa!=sb:d.errors.append({'code':'collaboration-crosses-sprint','id':r['id']})
            # One relation is symmetric; two arrowheads, no invented data flow.
            nonadjacent=abs(laneids.index(aa['lane'])-laneids.index(bb['lane']))>1
            xx=min(x1,x2)-12 if nonadjacent else min(x1,x2)+w1-18-(i%3)*18;sy=y1+h1;ty=y2
            if y1>y2:sy=y1;ty=y2+h2
            d.parts.append(f'<g data-relationship-id="{esc(r["id"])}"><path d="M{xx} {sy} L{xx} {ty}" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="6 4"/><path d="M{xx-5} {sy+8} L{xx} {sy} L{xx+5} {sy+8} M{xx-5} {ty-8} L{xx} {ty} L{xx+5} {ty-8}" fill="none" stroke="{color}" stroke-width="2"/></g>')
            d.text(xx-25 if nonadjacent else xx+7,(sy+ty)/2,label,12,color)
        elif typ in {'guide:agile_handoff','guide:agile_continues','guide:agile_finalizes'}:
            if sa in sprintids and sb in sprintids and sprintids.index(sb)<=sprintids.index(sa):d.errors.append({'code':'handoff-not-future-sprint','id':r['id']})
            if panel_for.get(sa)==panel_for.get(sb)or sa is None or typ=='guide:agile_finalizes':
                slot=routes[r['source']];routes[r['source']]+=1
                sx=x1+w1;sy=y1+h1-8-slot*5;tx=x2;ty=y2+h2-8;routey=y1+h1+30+slot*19
                source_sprint=sa or sprintids[0];gate=gate_by.get(source_sprint);gp=d.positions.get(gate['id'])if gate else None
                if gp:
                    li=laneids.index(aa.get('lane',laneids[0]));routey=max(routey,gp[1]+li*laneheight+laneheight*.55+80+slot*19)
                knee=tx-18-(slot%3)*6
                # Cross the DORP below output markers, then descend in the clear gutter.
                points=[(sx,sy),(sx+8,sy),(sx+8,routey),(knee,routey),(knee,ty),(tx,ty)]
                path='M'+' L'.join(str(x)+' '+str(yy)for x,yy in points)
                d.parts.append(f'<path data-relationship-id="{esc(r["id"])}" d="{path}" fill="none" stroke="{color}" stroke-width="1.5" marker-end="url(#arrow)"/>')
                d.text((sx+knee)/2,routey-5,label,12,color)
            else:
                for incoming,(x,yy,w,h),other in [(False,ap,r['target']),(True,bp,r['source'])]:
                    portkey=(r['target']if incoming else r['source']);slot=ports[portkey];ports[portkey]+=1
                    yy=yy+h+22+slot*22;start=x+12;end=x+w-12;arrow=' marker-end="url(#arrow)"'
                    d.parts.append(f'<path data-relationship-id="{esc(r["id"])}" d="M{start} {yy} L{end} {yy}" stroke="{color}" stroke-width="1.5"{arrow}/>')
                    d.text(start,yy-4,label+(' 来自 'if incoming else' 接续至 ')+other,10,color,units=max(28,int(w/6)))
        else:d.errors.append({'code':'unsupported-agile-relationship','id':r['id'],'type':typ});continue
        d.relation_ids.add(r['id']);d.edge_register.append(r)
    d.parts.insert(0,'<defs><marker id="agile-both" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0 L7 4 L0 8" fill="none" stroke="#238b92"/></marker></defs>')
    d.text(30,d.height+30,'橙色带＝DORP边界；圆/椭圆＝成果标记（不作为活动节点）；虚线圈＝可交付但未必每次必需。',14,units=150)
    d.text(30,d.height+16,'实线单向＝明确的后续冲刺交接/延续；青色虚线双向＝同冲刺协作、治理与支持。分图端口以同一关系ID对应。',14,units=150)
    # Complete visible field strips prevent compact source-shaped symbols hiding details.
    d.text(30,d.height+30,'对象字段与模型定位（与上图稳定ID对应）：',16)
    for e in es:
        missing=[k for k in e.get('attributes',{})if k not in d.attrs[e['id']]]
        if not missing:continue
        text=e['id']+' · '+'；'.join(k+'='+fmt(e['attributes'][k])for k in missing)
        d.text(30,d.height+12,text,12,units=170);d.attrs[e['id']].update(missing)
