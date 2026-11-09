"""G234 spatial maps plus complete, visible semantic detail by stable object ID.

Slots determine layout only. All containment is taken from model relationships.
"""
def metadata_map(d, es, rs):
    from profile_render import esc, wrap, fmt
    byid={e['id']:e for e in es};children={e['id']:[] for e in es}
    hierarchy=[r for r in rs if r['type'] in {'decomposes','visually_contains'}]
    for r in hierarchy:
        if r['source'] in children and r['target'] in byid:children[r['source']].append(byid[r['target']])
    def slot(value):return next((e for e in es if e.get('attributes',{}).get('g234:slot')==value),None)
    def header(e,w):return 30+len(wrap(e['name'],max(10,int((w-32)/9))))*25
    if d.layout=='reference':
        for items in children.values():items.sort(key=lambda e:e.get('attributes',{}).get('g234:reference-order',0))
    def compact_height(e,w):return 24+len(wrap(e['name'],max(10,int((w-24)/8.5))))*24+(28 if e.get('attributes',{}).get('concerns') else 0)
    def compact(e,x,y,w,h=None,fill='#ffffff'):
        h=h or compact_height(e,w)
        d.parts.append('<g data-entity-id="'+esc(e['id'])+'">');d.rect(x,y,w,h,fill)
        d.text(x+12,y+26,e['name'],16,units=max(10,int((w-24)/8.5)))
        for i,c in enumerate([c for c in d.profile.get('template',{}).get('concern_legend',[]) if c['label'] in e.get('attributes',{}).get('concerns',[])]):d.rect(x+14+i*30,y+h-26,20,15,c['color'],radius=2)
        d.parts.append('</g>')
        d.positions[e['id']]=(x,y,w,h);d.entity_ids.add(e['id']);return h
    def group_height(e,w,cols=3):
        items=children.get(e['id'],[]);cw=(w-32-14*(cols-1))/cols
        heights=[max(compact_height(c,cw) for c in items[i:i+cols]) for i in range(0,len(items),cols)]
        return header(e,w)+sum(h+14 for h in heights)+8
    def frame(e,x,y,w,h,fill):
        d.parts.append('<g data-entity-id="'+esc(e['id'])+'">');d.rect(x,y,w,h,fill)
        d.text(x+14,y+27,e['name'],18,units=max(10,int((w-32)/9)));d.parts.append('</g>')
        d.positions[e['id']]=(x,y,w,h);d.entity_ids.add(e['id'])
    def group(e,x,y,w,cols=3,h=None,fill='#d9eeee'):
        height=h or group_height(e,w,cols);frame(e,x,y,w,height,fill)
        items=children.get(e['id'],[]);cw=(w-32-14*(cols-1))/cols;yy=y+header(e,w)
        for i in range(0,len(items),cols):
            row=items[i:i+cols];rh=max(compact_height(c,cw) for c in row)
            for j,c in enumerate(row):compact(c,x+16+j*(cw+14),yy,cw,rh)
            yy+=rh+14
        return height
    structure=d.profile.get('template',{}).get('structure');width=1740;left=30;yy=110;d.width=width+60
    if structure in {'business','application'}:
        outer=slot('functions');team=slot('team')
        if not outer:
            d.errors.append({'code':'metadata-missing-outer-container','id':d.view['id']});return
        groups=children[outer['id']]
        if team:yy+=group(team,left,yy,width,4,fill='#edf0f4')+22
        outer_y=yy;inner_y=yy+header(outer,width);inner_x=left+18;inner_w=width-36;placements=[]
        if structure=='business' and d.layout=='reference':
            rows={}
            for e in groups:rows.setdefault(e.get('attributes',{}).get('reference_row',99),[]).append(e)
            for _,row in sorted(rows.items()):
                row.sort(key=lambda e:e.get('attributes',{}).get('reference_column',99))
                gw=(inner_w-18*(len(row)-1))/len(row)
                def cols(e):return {'1':5,'2':3,'3':1,'4':1,'5':1,'6':2,'7':2,'8':2,'9':2,'10':3}.get(e.get('attributes',{}).get('g234:slot'),3)
                rh=max(group_height(e,gw,cols(e)) for e in row)
                for j,e in enumerate(row):placements.append((e,inner_x+j*(gw+18),inner_y,gw,cols(e),rh))
                inner_y+=rh+18
        elif structure=='application' and d.layout=='reference':
            lookup={e.get('attributes',{}).get('g234:slot'):e for e in groups};needed=['acquisition','governance','reporting','reference-data','administration','integration']
            if any(s not in lookup for s in needed):d.errors.append({'code':'metadata-reference-slot-missing','id':outer['id'],'slots':[s for s in needed if s not in lookup]})
            rightw=310;mainw=inner_w-rightw-18;acq=lookup.get('acquisition');top=inner_y
            acqh=group_height(acq,mainw,5) if acq else 0
            if acq:placements.append((acq,inner_x,top,mainw,5,acqh))
            middle=top+acqh+18;govw=mainw*.42;reportw=mainw-govw-18
            gov=lookup.get('governance');ref=lookup.get('reference-data');rep=lookup.get('reporting')
            gh=group_height(gov,govw,2) if gov else 0;refh=group_height(ref,govw,1) if ref else 0
            rh=group_height(rep,reportw,2) if rep else 0;middleh=max(gh+18+refh,rh)
            if gov:placements.append((gov,inner_x,middle,govw,2,gh))
            if ref:placements.append((ref,inner_x,middle+gh+18,govw,1,refh))
            if rep:placements.append((rep,inner_x+govw+18,middle,reportw,2,middleh))
            integration=lookup.get('integration');span=acqh+18+middleh
            if integration:
                span=max(span,group_height(integration,rightw,1));placements.append((integration,inner_x+mainw+18,top,rightw,1,span))
            inner_y=top+span+18;admin=lookup.get('administration')
            if admin:
                ah=group_height(admin,inner_w,5);placements.append((admin,inner_x,inner_y,inner_w,5,ah));inner_y+=ah+18
            for e in groups:
                if e.get('attributes',{}).get('g234:slot') not in needed:
                    h=group_height(e,inner_w,4);placements.append((e,inner_x,inner_y,inner_w,4,h));inner_y+=h+18;d.warnings.append('新增参考槽位在扩展区显示：'+e['id'])
        else:
            for i in range(0,len(groups),2):
                row=groups[i:i+2];gw=(inner_w-18)/2;rh=max(group_height(e,gw,3) for e in row)
                for j,e in enumerate(row):placements.append((e,inner_x+j*(gw+18),inner_y,gw,3,rh))
                inner_y+=rh+18
        frame(outer,left,outer_y,width,inner_y-outer_y,'#fff7dc' if structure=='business' else '#eef7fc')
        for e,x,y,w,cols,h in placements:group(e,x,y,w,cols,h)
    elif structure=='solution':
        needs=slot('requirements');solution=slot('solution')
        if not needs or not solution:d.errors.append({'code':'metadata-solution-container-missing','id':d.view['id']});return
        gap=44;mainw=1390 if d.layout=='reference' else width;nx=left
        nh=group_height(needs,mainw,3);group(needs,nx,yy,mainw,3,nh,fill='#fff7dc');ny=yy;yy+=nh+120
        parts=children[solution['id']];cols=min(3,max(1,len(parts)));cw=(mainw-40-gap*(cols-1))/cols
        sh=header(solution,mainw)+sum(max(compact_height(c,cw) for c in parts[i:i+cols])+18 for i in range(0,len(parts),cols))+10
        frame(solution,nx,yy,mainw,sh,'#e3f2fa');py=yy+header(solution,mainw)
        for i in range(0,len(parts),cols):
            row=parts[i:i+cols];rh=max(compact_height(c,cw) for c in row)
            for j,c in enumerate(row):
                compact(c,nx+20+j*(cw+gap),py,cw,rh,'#d5f0f0')
                if j:d.text(nx+20+j*(cw+gap)-gap/2,py+rh/2+10,'+',32,anchor='middle')
            py+=rh+18
        for r in [r for r in rs if r['type']=='g234:supports-requirements']:
            if r['source']==solution['id'] and r['target']==needs['id']:d.line(nx+mainw/2,yy,nx+mainw/2,ny+nh,'整体方案支撑业务需求',r)
            else:d.edge(r,byid)
            d.edge_register.append(r)
        ly=ny if d.layout=='reference' else yy+sh+30;lx=nx+mainw+20 if d.layout=='reference' else nx
        d.text(lx,ly+20,'关注点图例（不表示人数）',16,units=34);ly+=65
        for concern in d.profile['template'].get('concern_legend',[]):
            d.rect(lx,ly,24,24,concern['color']);d.text(lx+34,ly+18,concern['label'],15,units=32);ly+=60
        d.text(lx,ly,'部门和关注点无来源规定的一一对应；示例需求另行声明。',13,units=36)
        project=[r for r in rs if r['type']=='supports_metadata_requirement'];ty=max(d.height,yy+sh)+35
        if project:
            ty+=d.text(left,ty,'虚构项目设计追溯（源图未规定；待实现验证）',17)+15
            for r in project:
                d.text(left,ty,byid[r['source']]['name'],16,units=40);d.text(left+660,ty,byid[r['target']]['name'],16,units=42)
                d.line(left+390,ty-6,left+620,ty-6,'',r,dashed=True);ty+=50;d.edge_register.append(r)
    else:d.errors.append({'code':'unknown-metadata-structure','id':d.view['id'],'structure':structure});return
    for r in hierarchy:
        a=d.positions.get(r['source']);b=d.positions.get(r['target'])
        if a and b and a[0]<=b[0] and a[1]<=b[1] and b[0]+b[2]<=a[0]+a[2]+.1 and b[1]+b[3]<=a[1]+a[3]+.1:
            d.relation_ids.add(r['id']);d.edge_register.append(r)
        else:d.errors.append({'code':'metadata-containment-not-expressed','id':r['id']})
    for e in es:
        if e['id'] not in d.entity_ids:
            d.warnings.append('对象未匹配来源槽位，在扩展区显示：'+e['id']);compact(e,left,d.height+20,width)
    for r in rs:
        if r['id'] not in d.relation_ids and r not in hierarchy:d.network_routing=True;d.edge(r,byid)
    # Full definitions are actual readable, anchored companion pages. Keep the
    # source-band overview compact instead of appending a many-screen ledger.
    d.profile = dict(d.profile, template={**d.profile.get('template',{}), 'separate_detail_ledger': True})
