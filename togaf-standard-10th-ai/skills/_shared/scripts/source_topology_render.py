"""Dedicated source topology layouts. Explicit relationships drive every connector."""
from collections import defaultdict
from html import escape
from source_topology_semantics import check_source_topology
import math

def _card(d,e,x,y,w=300,fill='#e9f0f7',fields=None,h=None):
    return d.card(e,x,y,w,h,fill,fields=fields or ['definition'])

def _badge(d,points,label,color,relationship_id=None,planning=False):
    """Keep dense topology labels on their connector, avoiding long leaders."""
    width=len(label)*7+10;height=22
    def overlap(a,b):return max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])
    def containing_endpoint(box):
        x,y,w,h=box
        return any(x<p[0]<x+w and y<p[1]<y+h for p in (points[0],points[-1]))
    obstacles=d.label_boxes+d.endpoint_glyph_boxes+[(x,y,x+w,y+h) for x,y,w,h in d.positions.values() if not containing_endpoint((x,y,w,h))]
    segments=sorted(zip(points,points[1:]),key=lambda pair:math.dist(*pair),reverse=True)
    for a,b in segments:
        length=math.dist(a,b)
        steps=max(2,int(length/16))
        fractions=sorted((i/steps for i in range(1,steps)),key=lambda t:abs(t-.5))
        for t in fractions:
            px=a[0]+(b[0]-a[0])*t;py=a[1]+(b[1]-a[1])*t
            for shift in (0,3,-3,6,-6,9,-9):
                # The white label still crosses its actual connector; this small
                # perpendicular offset fits narrow channels without a leader.
                x=px+(shift if a[0]==b[0] else 0);y=py+(shift if a[1]==b[1] else 0)
                box=(x-width/2,y-height/2,x+width/2,y+height/2)
                if box[0]<10 or not d.badge_clear(box,obstacles,relationship_id,planning):continue
                d.label_boxes.append(box);d.rect(box[0],box[1],width,height,'white','none',2);d.text(x,y+4,label,13,color,'middle');return
    d.badge(points,label,color,relationship_id,planning)

def _edge(d,r,arrow=True,dashed=False,color='#46647e'):
    from profile_render import orthogonal_route
    if r['source'] not in d.positions or r['target'] not in d.positions:
        d.errors.append({'code':'topology-endpoint-not-placed','id':r['id']});return
    if r['source']==r['target']:
        x,y,w,h=d.positions[r['source']]
        points=[(x+w*.35,y),(x+w*.35,y-35),(x+w*.65,y-35),(x+w*.65,y)]
    else:points=orthogonal_route(d,r)
    if not points:
        d.errors.append({'code':'no-clear-topology-edge-route','id':r['id']});return
    path='M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in points)
    dash=' stroke-dasharray="7 4"' if dashed else ''
    marker=' marker-end="url(#arrow)"' if arrow else ''
    d.parts.append(f'<path data-relationship-id="{escape(r["id"])}" d="{path}" fill="none" stroke="{color}" stroke-width="1.8"{dash}{marker}/>')
    if arrow:d.reserve_arrowhead(points)
    d.relation_ids.add(r['id']);d.edge_register.append(r);d.queue_badge(points,'['+str(len(d.edge_register))+']',color,r['id'],_badge)
    d.occupied_segments.extend(zip(points,points[1:]))

def integration(d,es,rs,kind):
    mdm=kind=='mdm-integration'
    patterns=('consolidation','cooperation','centralized') if mdm else ('consolidation','hybrid','unified')
    labels={'consolidation':'整合式：来源汇入中央' if mdm else '集中式：中央只保留副本','cooperation':'协作式：更新与规范版本双向交换','centralized':'集中式：MDM向消费方分发','hybrid':'混合式：选定主记录与工作流进入中央','unified':'统一式：全部主记录与工作流进入中央'}
    grouped=defaultdict(list)
    for e in es:grouped[e.get('attributes',{}).get('integration_style')].append(e)
    panelw=1150;start=150
    for i,pattern in enumerate(patterns):
        x=30+i*(panelw+25);nodes=grouped[pattern];central=[e for e in nodes if e.get('attributes',{}).get('topology_role')=='central'];others=[e for e in nodes if e not in central]
        if not central:continue
        width=330;rowh=max([d.card_height(e,width,fields=['definition','authority']) for e in others]+[170])+55
        rows=(len(others)+1)//2;panelh=max(650,rows*rowh+90)
        d.rect(x,start,panelw,panelh,'#f8fafc','#a8b5c0');d.text(x+18,start+30,labels[pattern],20)
        for j,e in enumerate(others):
            col=j%2;row=j//2;xx=x+20 if col==0 else x+panelw-width-20;yy=start+65+row*rowh
            _card(d,e,xx,yy,width,fields=['definition','authority'])
            if not mdm and e.get('attributes',{}).get('repository_location')=='external':
                d.text(xx+8,yy+d.positions[e['id']][3]+22,'外部主库存储（保留）',13,'#59646b')
        for c in central:_card(d,c,x+425,start+80+(panelh-250)/2,300,'#d8f1f4',fields=['definition','authority','workflow_owner'])
    for r in rs:_edge(d,r)
    d.text(30,d.height+35,'三栏为并列可组合方案；箭头仅按显式交换方向读取。候选示例的确定度不使用虚线编码。',16,units=200)

def security(d,es,rs):
    from source_topology_semantics import DOMAINS
    byid={e['id']:e for e in es};domains={e.get('attributes',{}).get('architecture_domain'):e for e in es if e['type']=='guide:architecture_domain'};concerns=[e for e in es if e['type']=='security_component']
    rowh=max([d.card_height(e,720,fields=['definition']) for e in domains.values()]+[150])+55;top=260
    labels={'business':'业务 Business','data':'数据 Data','application':'应用 Application','technology':'技术 Technology'}
    fullw=790+len(concerns)*380
    for i,key in enumerate(DOMAINS):
        y=top+i*rowh;d.rect(30,y,fullw,rowh-12,'#edf0f2','#a8b5c0')
        if key in domains:_card(d,domains[key],50,y+20,720,'#e4edf6',fields=['definition'])
        d.text(55,y+rowh-25,labels[key],16)
    for j,e in enumerate(concerns):
        x=840+j*380;h=top+4*rowh-120
        _card(d,e,x,110,340,'#ffffff',fields=['definition'],h=h)
        for i,key in enumerate(DOMAINS):
            domain=domains.get(key)
            if domain is None:continue
            matches=[r for r in rs if r['source']==e['id'] and r['target']==domain['id']]
            for r in matches:
                y=top+i*rowh+65;d.parts.append(f'<g data-relationship-id="{escape(r["id"])}">')
                d.text(x+18,y,r['label'],15,units=30);d.parts.append('</g>');d.relation_ids.add(r['id']);d.edge_register.append(r)
    d.text(30,d.height+30,'纵列覆盖四域；覆盖表示横切关注，不是第五域、流程先后或数据流。图中不绘制业务箭头。',16,units=180)

def bi(d,es,rs):
    stages=('baseline','transition1','transition2','target');labels={'baseline':'基线：企业数据仓库','transition1':'过渡一：并存与双供数','transition2':'过渡二：原始数据与交换','target':'目标：覆盖EDW职责的统一平台'}
    grouped=defaultdict(list)
    for e in es:grouped[e.get('attributes',{}).get('stage')].append(e)
    panelw=1540;panelh=1100;top=160;stagebounds={}
    for index,stage in enumerate(stages):
        x=30+(index%2)*(panelw+45);y=top+(index//2)*(panelh+65);nodes=grouped[stage];roles=defaultdict(list)
        for e in nodes:roles[e.get('attributes',{}).get('component_role')].append(e)
        d.rect(x,y,panelw,panelh,'#fff','#b4c4cc');d.text(x+18,y+30,labels[stage],22)
        d.rect(x+380,y+65,panelw-405,panelh-90,'#f6fafb','#277181',extra='stroke-dasharray="5 5"');d.text(x+395,y+92,'BI与分析数据平台范围',16)
        stagebounds[stage]=(x,y)
        sources=roles['transaction']+roles['external']
        for j,e in enumerate(sources):_card(d,e,x+18,y+130+j*220,320,'#e2edf6',fields=['definition','storage'])
        for j,e in enumerate(roles['consumer']):
            fill='#e2edf6' if e.get('attributes',{}).get('asset_status')=='existing' else '#fff0d8'
            _card(d,e,x+1020+(j%2)*250,y+130+(j//2)*290,230,fill,fields=['definition','storage'])
        central=roles['edw']+roles['platform']
        if stage=='target' and roles['platform']:
            p=roles['platform'][0];_card(d,p,x+480,y+270,430,'#fff0d8',fields=['definition','storage'],h=620)
            for e in roles['edw']:_card(d,e,x+510,y+600,370,'#e7e9ed',fields=['definition','storage'])
        else:
            for j,e in enumerate(central):_card(d,e,x+500,y+180+j*470,400,'#e2edf6' if e.get('attributes',{}).get('component_role')=='edw' else '#fff0d8',fields=['definition','storage'])
    for r in rs:
        attrs=r.get('attributes',{});_edge(d,r,dashed=attrs.get('flow_role')=='inbound',color='#cb7d27' if attrs.get('change_status')=='new' else '#52798b')
    d.text(30,d.height+30,'线型：虚线＝入站与应用回写，实线＝出站供数。填色：蓝色＝保留资产，浅橙＝新增平台或消费方；不表示已批准。目标嵌套只表示EDW职责被覆盖。',16,units=220)

def metamodel(d,es,rs):
    grouped=defaultdict(list)
    for e in es:grouped[e.get('attributes',{}).get('domain')].append(e)
    width=2430;y=140;common=[e for e in grouped['general'] if e.get('attributes',{}).get('associated_with_all')];other=[e for e in grouped['general'] if e not in common]
    d.rect(30,y,width,310,'#ffe8c5');d.text(45,y+28,'通用实体 General Entities',20)
    d.rect(45,y+48,2050,240,'#f0f0f0');d.text(60,y+75,'可与所有对象关联的七类实体',16)
    for i,e in enumerate(common):_card(d,e,60+i*289,y+90,270,fields=['definition'])
    for e in other:_card(d,e,2120,y+90,310,'#fff2dc',fields=['definition'])
    y+=345;business=grouped['business'];service=[e for e in business if e.get('attributes',{}).get('source_concept')=='business_service'];business=[e for e in business if e not in service]
    rowh=max([d.card_height(e,440,fields=['definition']) for e in business]+[150])+95;rows=(len(business)+4)//5
    d.rect(30,y,width,rows*rowh+270,'#ffffdb');d.text(45,y+30,'业务架构 BUSINESS ARCHITECTURE',20)
    for i,e in enumerate(business):_card(d,e,55+(i%5)*480,y+65+(i//5)*rowh,440,'#fffde8',fields=['definition'])
    sy=y+65+rows*rowh
    for e in service:_card(d,e,55,sy,width-50,'#fffde8',fields=['definition'])
    y+=rows*rowh+305
    colors={'data':'#fbe4f5','application':'#e1f8ea','technology':'#e3effc'};labels={'data':'数据架构 DATA','application':'应用架构 APPLICATION','technology':'技术架构 TECHNOLOGY'}
    for index,key in enumerate(('data','application','technology')):
        x=30+index*815;d.rect(x,y,800,740,colors[key]);d.text(x+15,y+30,labels[key],20)
        for j,e in enumerate(grouped[key]):_card(d,e,x+45,y+85+j*215,700,'#ffffff',fields=['definition','abstraction'])
    for r in rs:_edge(d,r,arrow=False)
    d.text(30,d.height+30,'所有节点表示实体类型，不是企业实例。所有连线均无箭头：正反向读法见编号关系表；源图端点推断保留为待核实解释。逻辑—物理关系不等于组成嵌套。',16,units=220)

def _frame(d,e,x,y,w,h,label):
    d.parts.append('<g data-entity-id="'+escape(e['id'])+'">')
    d.rect(x,y,w,h,'#f1f5fa','#8193a7')
    d.text(x+16,y+28,label,18)
    d.parts.append('</g>');d.positions[e['id']]=(x,y,w,h);d.entity_ids.add(e['id'])

def repository(d,es,rs):
    containers={e.get('attributes',{}).get('container_role'):e for e in es if e['type']=='repository_container'}
    arch=containers.get('architecture');enterprise=containers.get('enterprise')
    contained={(r['source'],r['target']):r for r in rs if r['type']=='project:contains'}
    partitions=[e for e in es if e['type']=='repository_partition']
    assets=[e for e in es if e['type']=='repository_asset']
    connected=[e for e in partitions if arch and (arch['id'],e['id']) in contained]
    detached=[e for e in partitions if e not in connected]
    cw=420;cols=4;top=250;rows=max(1,(len(connected)+cols-1)//cols)
    heights={e['id']:d.card_height(e,cw,fields=['definition'])+sum(d.card_height(a,cw-30,fields=['definition'])+20 for a in assets if (e['id'],a['id']) in contained) for e in connected}
    rowheights=[max([heights[e['id']] for e in connected[i:i+cols]]+[150])+65 for i in range(0,len(connected),cols)]
    archh=sum(rowheights)+100;archw=cols*(cw+30)+30
    if enterprise:_frame(d,enterprise,30,130,archw+90,archh+130,enterprise['name'])
    if arch:_frame(d,arch,65,190,archw,archh,arch['name'])
    placed=set(containers[e]['id'] for e in containers)
    for i,e in enumerate(connected):
        x=90+(i%cols)*(cw+30);y=top+sum(rowheights[:i//cols])
        kids=[a for a in assets if (e['id'],a['id']) in contained]
        h=d.card_height(e,cw,fields=['definition'])+sum(d.card_height(a,cw-30,fields=['definition'])+20 for a in kids)
        _card(d,e,x,y,cw,fields=['definition'],h=h);placed.add(e['id'])
        yy=y+d.card_height(e,cw,fields=['definition'])
        for a in kids:
            ah=_card(d,a,x+15,yy,cw-30,fields=['definition']);yy+=ah+20;placed.add(a['id'])
    yy=180
    for e in es:
        if e['id'] in placed:continue
        h=_card(d,e,archw+200,yy,400,'#fff4df',fields=['definition']);yy+=h+55
    for r in rs:
        if r['type']=='project:contains':
            a=d.positions.get(r['source']);b=d.positions.get(r['target'])
            if a and b and a[0]<=b[0] and a[1]<=b[1] and b[0]+b[2]<=a[0]+a[2] and b[1]+b[3]<=a[1]+a[3]:
                x,y,w,h=b
                d.parts.append('<rect data-relationship-id="'+escape(r['id'])+'" x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'" fill="none" stroke="#627e96"/>')
                d.relation_ids.add(r['id']);d.edge_register.append(r)
            else:d.errors.append({'code':'repository-containment-not-expressed','id':r['id']})
        else:_edge(d,r,arrow=r['type'] not in {'project:visibility_escalation','project:delivers_outcomes'})
    d.text(30,d.height+35,'边界嵌套仅来自 contains；外部标准与参考材料分别采纳到对应分区。完整语义见伴随明细。',16,units=200)

def landscape(d,es,rs):
    from source_topology_semantics import landscape_members
    volume=next((e for e in es if e['type']=='landscape_projection'),None)
    axes=[e for e in es if e['type']=='landscape_dimension']
    slices=[e for e in es if e['type']=='landscape_slice']
    objects=[e for e in es if e not in ([volume] if volume else [])+axes+slices]
    sy=340;slice_layout=[]
    for e in slices:
        members=landscape_members(es,e)
        h=d.card_height(e,800,fields=['definition','breadth','abstraction','time'])+sum(d.card_height(o,760,fields=['definition','breadth','abstraction','time'])+25 for o in objects if o['id'] in members)+35
        slice_layout.append((e,sy,h,members));sy+=h+35
    if volume:
        _frame(d,volume,50,140,920,max(400,sy-120),'EA 全景：三轴坐标交集')
        d.text(80,210,volume.get('attributes',{}).get('definition',''),15,units=95)
    placed=set()
    for e,y,h,members in slice_layout:
        _card(d,e,100,y,800,'#fff0dc',fields=['definition','breadth','abstraction','time'],h=h)
        yy=y+d.card_height(e,800,fields=['definition','breadth','abstraction','time'])+15
        for o in objects:
            if o['id'] in members and o['id'] not in placed:
                yy+=_card(d,o,120,yy,760,fields=['definition','breadth','abstraction','time'])+25;placed.add(o['id'])
    yy=160
    for e in axes+[o for o in objects if o['id'] not in placed]:
        yy+=_card(d,e,1080,yy,400,'#e5eef8',fields=['definition','axis','breadth','abstraction','time'])+40
    for r in rs:
        if r['type']=='project:contains' or (r['type']=='project:projects_to' and r['target'] in {e['id'] for e in slices}):
            x,y,w,h=d.positions[r['target'] if r['type']=='project:contains' else r['source']]
            d.parts.append('<rect data-relationship-id="'+escape(r['id'])+'" x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'" fill="none" stroke="#b78954"/>')
            d.relation_ids.add(r['id']);d.edge_register.append(r)
        else:_edge(d,r)
    d.text(30,d.height+35,'三轴为范围维度；切片与成员位置由显式包含关系及坐标交集共同校验。',16,units=200)

def security_adm(d,es,rs):
    from source_topology_semantics import ADM_PHASES
    phases={e.get('attributes',{}).get('phase_code'):e for e in es if e['type']=='adm_phase'}
    concepts=[e for e in es if e['type']=='security_risk_concept']
    grouped=defaultdict(list)
    for e in concepts:grouped[e.get('attributes',{}).get('phase_code')].append(e)
    y=160
    for code in ADM_PHASES:
        items=grouped[code];rows=[items[i:i+4] for i in range(0,len(items),4)]
        heights=[max(d.card_height(e,360,fields=['definition']) for e in row)+30 for row in rows]
        phase=phases.get(code);rh=max(d.card_height(phase,260,fields=['definition']) if phase else 0,sum(heights))+60
        if phase:_card(d,phase,30,y,260,fields=['definition'])
        yy=y
        for row,h in zip(rows,heights):
            for j,e in enumerate(row):
                fill='#fff3c4' if e.get('attributes',{}).get('ism_erm_addition') else '#ffffff'
                _card(d,e,400+j*400,yy,360,fill,fields=['definition'])
            yy+=h
        y+=rh
    others=[e for e in es if e['type'] not in {'adm_phase','security_risk_concept'}]
    for i,e in enumerate(others):_card(d,e,400+(i%4)*400,y+(i//4)*250,360,'#e8f6f2',fields=['definition'])
    for r in rs:_edge(d,r,arrow=r['type']!='project:associates',dashed=r['type']=='project:continues')
    d.text(30,d.height+35,'阶段—概念组无方向；P/A共享首组，RM关联业务属性与控制目标。浅黄为15个ISM/ERM新增概念。E/F曲线端点仍保留来源判读限制。',16,units=200)

def inference(d,es,rs):
    zones={e.get('attributes',{}).get('zone'):e for e in es if e['type']=='metadata_zone'}
    mgmt=next((e for e in es if e['type']=='metadata_management'),None)
    profiling=next((e for e in es if e['type']=='data_profiling'),None)
    sources=sorted([e for e in es if e['type']=='inference_source'],key=lambda e:{'structured':0,'semi-structured':1,'unstructured':2}.get(e.get('attributes',{}).get('data_structure'),0))
    fields=['definition','data_structure','schema_access','content_access','governance_claim']
    heights=[d.card_height(e,640,fields=fields)+40 for e in sources]
    datah=max(400,sum(heights)+80)
    d.rect(30,140,1500,290,'#e7f0e4','#6d8a6f');d.text(48,168,'METADATA',18)
    d.rect(30,470,1500,datah,'#e8eef6','#6a7d93');d.text(48,498,'DATA',18)
    if 'METADATA' in zones:_card(d,zones['METADATA'],80,200,280,fields=['definition'])
    if mgmt:_card(d,mgmt,420,200,420,fields=['definition','access_condition','cost'])
    if 'DATA' in zones:_card(d,zones['DATA'],80,540,280,fields=['definition'])
    if profiling:_card(d,profiling,420,540,360,fields=['definition','access_condition','cost'])
    y=540
    for e,h in zip(sources,heights):_card(d,e,820,y,640,fields=fields);y+=h
    for r in rs:_edge(d,r)
    d.text(30,d.height+35,'DATA来源经读取、剖析、结构上推与上行进入METADATA；访问条件与成本来自模型。',16,units=200)

def soa(d,es,rs):
    from source_topology_semantics import SOA_LAYERS,SOA_CONCERNS
    layers={e.get('attributes',{}).get('layer'):e for e in es if e['type']=='soa_layer'}
    concerns={e.get('attributes',{}).get('concern'):e for e in es if e['type']=='soa_concern'}
    colors={'consumer-interface':'#e9f3ff','business-process':'#e7f6ea','services':'#fff4d6','service-component':'#f3e9ff','operational-systems':'#f0f0f0'}
    for i,name in enumerate(SOA_LAYERS):
        y=150+i*150;d.rect(30,y,1100,135,colors[name],'#8aa0b3')
        if name in layers:_card(d,layers[name],50,y+18,1060,colors[name],fields=['definition'],h=100)
    for j,name in enumerate(SOA_CONCERNS):
        if name in concerns:_card(d,concerns[name],1180,150+j*188,360,'#ffffff',fields=['definition'])
    for r in rs:_edge(d,r,arrow=r['type']=='project:maps_to',dashed=r['type']=='project:cross_cuts_soa')
    d.text(30,d.height+28,'五层自上而下。虚线是跨层关注，不是第六层或调用顺序。参考层可按项目裁剪。',16,units=200)

def ea_adm_matrix(d,es,rs):
    from source_topology_semantics import ADM_PHASES
    from profile_render import wrap
    services=list(dict.fromkeys(e.get('attributes',{}).get('service') for e in es))
    left=400;top=200;cw=180;y=top
    for i,phase in enumerate(ADM_PHASES):d.text(left+i*cw+15,top-35,phase,18)
    labels={'no-relation':'明确无关系','not-applicable':'不适用','unknown':'未知','source-mapped':'× 来源映射','source-unmarked':'来源未标注'}
    for service in services:
        rh=max(120,len(wrap(service,30))*24+30);d.text(30,y+35,service,17,units=30)
        for col,phase in enumerate(ADM_PHASES):
            x=left+col*cw
            records=[e for e in es if e.get('attributes',{}).get('service')==service and (e['attributes'].get('ADM_phase')==phase or phase in e['attributes'].get('phase_map',{}))]
            d.rect(x,y,cw-8,rh-8,'#e7f2e6' if records else '#f3f4f6')
            if not records:d.text(x+12,y+35,'未知',15)
            for i,e in enumerate(records):
                d.parts.append('<g data-entity-id="'+escape(e['id'])+'">')
                state=e['attributes'].get('phase_map',{}).get(phase,e['attributes'].get('mapping_status','project-mapping'))
                d.text(x+10,y+27+i*34,labels.get(state,'项目映射'),14)
                d.text(x+10,y+55+i*34,e['id'],11,units=22);d.parts.append('</g>')
                d.positions[e['id']]=(x,y,cw-8,rh-8);d.entity_ids.add(e['id'])
        y+=rh
    for r in rs:_edge(d,r)
    d.text(30,d.height+40,'RM为持续需求管理。未知、明确无关系、不适用、来源未标注分别记录；参考映射不强制企业照搬。',16,units=180)

def msa_execution(d,es,rs):
    kinds=('source','library','deployment','execution')
    for col,kind in enumerate(kinds):
        x=30+col*520;d.text(x,145,kind,20);y=190
        for e in es:
            if e.get('attributes',{}).get('unit_kind')==kind:
                y+=_card(d,e,x,y,430,fields=['function','service_id','environment','instances','operating_condition'])+65
    for r in rs:_edge(d,r)

def msa_governance(d,es,rs):
    from companion_profiles import ASPECTS
    owner=next((e for e in es if e.get('attributes',{}).get('process_aspects')),None)
    if owner:
        aspects=owner['attributes']['process_aspects'];cw=530
        h=max(d.card_height(dict(owner,name=label,attributes={'definition':aspects.get(key,'缺失')}),cw,fields=['definition']) for key,label in ASPECTS.items())
        y=180
        for i,(key,label) in enumerate(ASPECTS.items()):
            row=0 if i<3 else 1;col=i if i<3 else 5-i
            shown=dict(owner,name=label,attributes={'definition':aspects.get(key,'缺失')})
            d.card(shown,30+col*660,y+row*(h+120),cw,h,'#e4f0f7',fields=['definition'])
        # Continuous cycle is source notation for the six aspects of this one
        # governance process, not an invented dependency between governance tiers.
        d.text(30,d.height+50,'六类治理要素持续复核、度量、纠偏并更新；没有一次性项目终点。上区共用MSA治理对象ID，具体值为项目候选。',16,units=180)
    y=d.height+100
    d.text(30,y,'四层治理关系（G21I图5-1）及本项目控制；与上方图5-2六要素分开读取。',18,units=170);y+=50
    for row in range(0,len(es),2):
        nodes=es[row:row+2]
        h=max(d.card_height(e,680,fields=['authority','decision','decision_status','waiver','controls','feedback']) for e in nodes)
        for col,e in enumerate(nodes):_card(d,e,30+col*940,y,680,fields=['authority','decision','decision_status','waiver','controls','feedback'],h=h)
        y+=h+180
    for r in rs:_edge(d,r,dashed=r['type']=='ops:governance_constrains')
    d.text(30,d.height+40,'支持、对齐、扩展、约束分别保留类型；豁免申请不是批准。控制执行与持续反馈见卡片及明细。',16,units=180)

def render_source_topology(d,es,rs):
    kind=d.profile.get('template',{}).get('source_topology')
    findings=check_source_topology(es,rs,d.profile,d.view);d.errors.extend(findings)
    if kind in {'repository-tree','repository-comparison','capability-continuum','stakeholder-concern-matrix'}:
        from repository_reference_profiles import render
        render(d,es,rs,kind)
    elif kind in {'mdm-integration','metadata-integration'}:integration(d,es,rs,kind)
    elif kind=='security-crosscut':security(d,es,rs)
    elif kind=='bi-evolution':bi(d,es,rs)
    elif kind=='content-metamodel':metamodel(d,es,rs)
    elif kind=='architecture-repository':repository(d,es,rs)
    elif kind=='architecture-landscape':landscape(d,es,rs)
    elif kind=='security-adm-map':security_adm(d,es,rs)
    elif kind=='metadata-inference':inference(d,es,rs)
    elif kind=='soa-layered':soa(d,es,rs)
    elif kind=='ea-adm-matrix':ea_adm_matrix(d,es,rs)
    elif kind=='msa-governance':msa_governance(d,es,rs)
    elif kind=='msa-execution':msa_execution(d,es,rs)
