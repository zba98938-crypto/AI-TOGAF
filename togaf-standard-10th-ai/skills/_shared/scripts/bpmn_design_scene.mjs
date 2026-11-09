// Fixed local browser function shared by public render and controlled renderer.
// No command, path, URL, browser flag, or executable model field is accepted.
export async function renderDesignScene({xml,spec,fontCSS}) {
    const NS = 'http://www.w3.org/2000/svg';
    const viewer = new window.BpmnJS({container:'#canvas',textRenderer:{defaultStyle:{fontFamily:'TogafCJK',fontSize:14},externalStyle:{fontFamily:'TogafCJK',fontSize:13}}});
    const parsed = await viewer.get('moddle').fromXML(spec.notation_xml);
    if (parsed.warnings.length) throw new Error('Native model parse warnings: '+parsed.warnings.map(w=>w.message).join('; '));
    const symbols = viewer.get('bpmnRenderer'), nodes = parsed.elementsById;
    const sourceGraphics=spec.graphics,raw=new Map(sourceGraphics.map(g=>[g.graphic_id,g]));
    const numeric=b=>b?Object.fromEntries(Object.entries(b).map(([k,v])=>[k,Number(v)])):b;
    spec={...spec,graphics:sourceGraphics.map(g=>({...g,bounds:numeric(g.bounds),label_bounds:numeric(g.label_bounds),waypoints:g.waypoints?.map(numeric)}))};
    const nativeBo=g=>g.type==='dataAssociationShortcut'?viewer.get('moddle').create('bpmn:Association',{id:g.view_identity,associationDirection:'None'}):nodes[g.semantic_id];
    const svg = document.createElementNS(NS,'svg');
    svg.setAttribute('xmlns',NS); svg.setAttribute('version','1.1');
    document.querySelector('#scene').append(svg);
    const add = (parent,name,attrs={}) => {
      const e = document.createElementNS(NS,name);
      for (const [k,v] of Object.entries(attrs)) if (v !== null && v !== undefined) e.setAttribute(k,String(v));
      parent.append(e); return e;
    };
    add(add(svg,'defs'),'style').textContent = fontCSS+'text{font-family:TogafCJK,sans-serif}';
    const scene = add(svg,'g',{'data-native-root':spec.root_id});
    const canvas = document.createElement('canvas').getContext('2d');
    const layouts = [], common = [], elements = new Map();
    const stroke = {stroke:'#111','stroke-width':2,fill:'white'};
    const localBox = b => ({x:0,y:0,width:b.width,height:b.height});
    function text(parent,name,b,{size=14,reserve=0,external=false}={}) {
      if (!name) return;
      canvas.font = `${size}px TogafCJK`;
      const available = Math.max(1,b.width-8), lines=[];
      for (const paragraph of name.split(/\r?\n/)) {
        let line='';
        for (const char of paragraph) {
          if (line && canvas.measureText(line+char).width > available) {lines.push(line);line='';}
          line += char;
        }
        lines.push(line);
      }
      const lineHeight=size*1.25, used=lines.length*lineHeight;
      if (!external && used > b.height-reserve-4) throw new Error('diagram-capacity: native label does not fit supplied DI bounds: '+name);
      const first=b.y+(b.height-reserve-used)/2+size;
      const label=add(parent,'text',{'font-size':size,'text-anchor':'middle',fill:'#111','data-native-label':name});
      lines.forEach((line,index) => {add(label,'tspan',{x:b.x+b.width/2,y:first+index*lineHeight}).textContent=line;});
      layouts.push({name,lines,box:b,origin:external?'derived label placement; node/edge DI unchanged':'source shape/name band'});
    }
    function plus(parent,x,y,size=12) {
      add(parent,'rect',{x:x-size/2,y:y-size/2,width:size,height:size,...stroke,'stroke-width':1,'data-marker':'sub-choreography'});
      add(parent,'path',{d:`M ${x-size/3} ${y} H ${x+size/3} M ${x} ${y-size/3} V ${y+size/3}`,stroke:'#111','stroke-width':1,fill:'none'});
    }
    function loop(parent,type,x,y) {
      if (type==='None') return;
      if (type==='Standard') {
        add(parent,'path',{d:`M ${x+5} ${y+4} A 6 6 0 1 1 ${x+5} ${y-4} M ${x+5} ${y-4} l -5 -1 M ${x+5} ${y-4} l -1 -5`,stroke:'#111','stroke-width':1.5,fill:'none','data-marker':'loop'});
      } else {
        const parallel=type==='MultiInstanceParallel';
        const p=add(parent,'g',{'data-marker':parallel?'parallel':'sequential'});
        for (const offset of [-4,0,4]) add(p,'line',parallel?{x1:x+offset,y1:y-6,x2:x+offset,y2:y+6,stroke:'#111','stroke-width':2}:{x1:x-6,y1:y+offset,x2:x+6,y2:y+offset,stroke:'#111','stroke-width':2});
      }
    }
    function envelope(parent,g) {
      const b=g.bounds, top=g.band_kind.startsWith('top_');
      const cx=b.width/2, y=top?-34:b.height+20, lineEnd=top?0:b.height;
      const filled=g.band_kind.endsWith('non_initiating');
      add(parent,'path',{d:`M ${cx} ${lineEnd} V ${top?y+14:y}`,stroke:'#111','stroke-width':1,'stroke-dasharray':'3 3',fill:'none','data-message-tether':g.semantic_id});
      add(parent,'rect',{x:cx-10,y,width:20,height:14,stroke:'#111','stroke-width':1,fill:filled?'#ddd':'white','data-message-envelope':filled?'return':'initiating'});
      add(parent,'path',{d:`M ${cx-10} ${y} L ${cx} ${y+8} L ${cx+10} ${y}`,stroke:'#111','stroke-width':1,fill:'none'});
    }
    function band(parent,g) {
      const b=g.bounds,w=b.width,h=b.height,r=Math.min(8,h/2),pos=g.band_kind.split('_')[0];
      const d=pos==='top'?`M 0 ${h} V ${r} Q 0 0 ${r} 0 H ${w-r} Q ${w} 0 ${w} ${r} V ${h} Z`:
        pos==='bottom'?`M 0 0 H ${w} V ${h-r} Q ${w} ${h} ${w-r} ${h} H ${r} Q 0 ${h} 0 ${h-r} Z`:`M 0 0 H ${w} V ${h} H 0 Z`;
      add(parent,'path',{d,...stroke,fill:g.band_kind.endsWith('non_initiating')?'#ddd':'white','data-band-kind':g.band_kind});
      text(parent,g.name,localBox(b),{size:12,reserve:g.participant_multiplicity?11:0});
      if (g.participant_multiplicity) loop(parent,'MultiInstanceParallel',w/2,h-7);
      if (['true','1'].includes(g.attributes.isMessageVisible)) envelope(parent,g);
    }
    function externalLabel(parent,g) {
      if (!g.name) return;
      const b=g.bounds, supplied=g.label_bounds;
      // BPMNLabel bounds are optional. This derives only typography positioning,
      // and never adds/replaces missing authoritative node or connector DI.
      const box=supplied?{...supplied,x:supplied.x-b.x,y:supplied.y-b.y}:
        {x:b.width/2-80,y:b.height+6,width:160,height:Math.max(24,Math.ceil(g.name.length/11)*17)};
      text(parent,g.name,box,{size:13,external:!supplied});
    }
    const shapeGraphics=spec.graphics.filter(g=>g.kind==='shape');
    // Container borders below children; participant bands above their activity.
    const order=[...shapeGraphics.filter(g=>!g.band_kind)].sort((a,b)=>b.bounds.width*b.bounds.height-a.bounds.width*a.bounds.height)
      .concat(shapeGraphics.filter(g=>g.band_kind));
    for (const g of order) {
      const b=g.bounds, bo=nativeBo(g);
      if (!bo) throw new Error('Native semantic object missing '+g.semantic_id);
      const group=add(scene,'g',{'data-element-id':g.semantic_id,'data-di-id':g.graphic_id,'data-native-type':g.type,
        transform:`translate(${b.x},${b.y})`,'data-di-x':raw.get(g.graphic_id).bounds.x,'data-di-y':raw.get(g.graphic_id).bounds.y,'data-di-width':raw.get(g.graphic_id).bounds.width,'data-di-height':raw.get(g.graphic_id).bounds.height});
      const di=nodes[g.graphic_id] || {$type:'bpmndi:BPMNShape',...g.attributes};
      const element={id:g.graphic_id,type:bo.$type,businessObject:bo,di,...b,parent:{businessObject:nodes[spec.root_id]}};
      elements.set(g.graphic_id,element);
      if (g.band_kind) band(group,g);
      else if (['conversation','subConversation','callConversation'].includes(g.type)) {
        add(group,'polygon',{points:`${b.width/4},0 ${b.width*3/4},0 ${b.width},${b.height/2} ${b.width*3/4},${b.height} ${b.width/4},${b.height} 0,${b.height/2}`,
          ...stroke,'stroke-width':g.type==='callConversation'?4:2,'data-notation':'conversation-hexagon'});
        if (g.type==='subConversation' || (g.type==='callConversation' && g.called_type==='collaboration')) plus(group,b.width/2,b.height-8,10);
        externalLabel(group,g);
      } else if (['choreographyTask','subChoreography','callChoreography'].includes(g.type)) {
        add(group,'rect',{x:0,y:0,width:b.width,height:b.height,rx:8,...stroke,'stroke-width':g.type==='callChoreography'?4:2,'data-notation':'choreography-activity'});
        const n=g.name_band, box={...n,x:n.x-b.x,y:n.y-b.y};
        const expanded=['true','1'].includes(g.attributes.isExpanded);
        const collapsed=(g.type==='subChoreography' || (g.type==='callChoreography' && g.called_type==='choreography')) && !['true','1'].includes(g.attributes.isExpanded);
        const hasLoop=g.loop_type!=='None';
        text(group,g.name,expanded?{...box,height:Math.min(40,box.height)}:box,{reserve:expanded?0:collapsed||hasLoop?22:0});
        const cx=b.width/2, y=box.y+box.height-10;
        if (collapsed) plus(group,cx+(hasLoop?9:0),y);
        if (hasLoop) loop(group,g.loop_type,cx-(collapsed?10:0),y);
      } else {
        // Resolve referenced event definitions in the in-memory display object.
        // Source XML and exported native bytes remain untouched.
        if (bo.eventDefinitionRef?.length) bo.eventDefinitions=[...(bo.eventDefinitions||[]),...bo.eventDefinitionRef];
        if (bo.eventDefinitionRefs?.length) bo.eventDefinitions=[...(bo.eventDefinitions||[]),...bo.eventDefinitionRefs];
        symbols.drawShape(group,element);
        if (g.type==='participant' && !g.participant_multiplicity) {
          group.querySelectorAll('[data-marker="participant-multiplicity"]').forEach(e=>e.remove());
        }
        common.push({graphic_id:g.graphic_id,semantic_id:g.semantic_id,type:bo.$type});
        if (/Event$|Gateway$/.test(bo.$type) || ['dataObjectReference','dataStoreReference','dataInput','dataOutput'].includes(g.type)) externalLabel(group,g);
      }
    }
    // Repaint thick call borders once bands are complete, preserving their fill.
    for (const g of shapeGraphics.filter(g=>g.type==='callChoreography')) {
      add(scene.querySelector(`[data-di-id="${g.graphic_id}"]`),'rect',{x:0,y:0,width:g.bounds.width,height:g.bounds.height,rx:8,stroke:'#111','stroke-width':4,fill:'none','pointer-events':'none','data-call-boundary':g.graphic_id});
    }
    function offsetPolyline(points,distance) {
      const normals=points.slice(1).map((p,i)=>{const a=points[i],dx=p.x-a.x,dy=p.y-a.y,l=Math.hypot(dx,dy);if(!l)throw new Error('ConversationLink has coincident consecutive waypoints');return {x:-dy/l,y:dx/l};});
      return points.map((p,i)=>{
        let n=normals[Math.min(i,normals.length-1)],scale=distance;
        if(i>0&&i<points.length-1){const a=normals[i-1],z=normals[i];n={x:a.x+z.x,y:a.y+z.y};const dot=n.x*z.x+n.y*z.y;if(Math.abs(dot)<1e-7)throw new Error('ConversationLink reverses direction at a waypoint');scale=distance/dot;}
        return {x:p.x+n.x*scale,y:p.y+n.y*scale};
      });
    }
    const pathOf=points=>points.map((p,i)=>`${i?'L':'M'} ${p.x} ${p.y}`).join(' ');
    const edgeGraphics=spec.graphics.filter(g=>g.kind==='edge');
    for (const g of edgeGraphics) {
      const bo=nativeBo(g);
      elements.set(g.graphic_id,{id:g.graphic_id,type:bo.$type,businessObject:bo,di:nodes[g.graphic_id]||{$type:'bpmndi:BPMNEdge',...g.attributes},waypoints:g.waypoints,parent:{businessObject:nodes[spec.root_id]}});
    }
    for (const g of edgeGraphics) {
      const bo=nativeBo(g),group=add(scene,'g',{'data-element-id':g.semantic_id,'data-di-id':g.graphic_id,'data-native-type':g.type,'data-source-waypoints':JSON.stringify(raw.get(g.graphic_id).waypoints),'data-source-di-endpoint':g.source_graphic_id,'data-target-di-endpoint':g.target_graphic_id,'data-normalized-native-associations':g.normalized_semantic_ids?JSON.stringify(g.normalized_semantic_ids):undefined});
      const connection=elements.get(g.graphic_id);
      connection.source=elements.get(g.source_graphic_id);connection.target=elements.get(g.target_graphic_id);
      if (g.type==='conversationLink') {
        for (const distance of [-1.5,1.5]) add(group,'path',{d:pathOf(offsetPolyline(g.waypoints,distance)),stroke:'#111','stroke-width':1,fill:'none','data-conversation-link-line':distance});
      } else {
        if (!connection.source || !connection.target) throw new Error('DI connection endpoint missing '+g.graphic_id);
        symbols.drawConnection(group,connection);common.push({graphic_id:g.graphic_id,semantic_id:g.semantic_id,type:bo.$type});
      }
      if (g.name) {
        const a=g.waypoints[Math.floor((g.waypoints.length-1)/2)],z=g.waypoints[Math.ceil((g.waypoints.length-1)/2)];
        text(group,g.name,g.label_bounds||{x:(a.x+z.x)/2-80,y:(a.y+z.y)/2-24,width:160,height:20},{size:13,external:!g.label_bounds});
      }
    }
    // Reattach whole graphic groups in the normative source-plane Z-order.
    // Preparing shapes/forward endpoints never defines painter ordering.
    const drawn=new Map([...scene.children].filter(e=>e.hasAttribute('data-di-id')).map(e=>[e.getAttribute('data-di-id'),e]));
    for(const g of sourceGraphics){const group=drawn.get(g.graphic_id);if(group){group.setAttribute('data-source-plane-index',g.source_plane_index);scene.append(group);}}
    const actual=[...svg.querySelectorAll('[data-di-id]')].map(e=>e.getAttribute('data-di-id'));
    const expected=sourceGraphics.map(g=>g.graphic_id);
    if (JSON.stringify(actual)!==JSON.stringify(expected)) throw new Error('Rendered DI graphic set differs from source plan');
    for (const [id,name] of Object.entries(spec.visible_names)) {
      if (!svg.textContent.replace(/\s+/g,'').includes(name.replace(/\s+/g,''))) throw new Error('SVG omitted native name '+id);
    }
    const box=scene.getBBox(),margin=12;
    const width=Math.ceil(box.width+2*margin),height=Math.ceil(box.height+2*margin);
    svg.setAttribute('viewBox',`${box.x-margin} ${box.y-margin} ${width} ${height}`);svg.setAttribute('width',width);svg.setAttribute('height',height);
    return {svg:new XMLSerializer().serializeToString(svg),graphicIds:actual,commonSymbols:common,labelLayouts:layouts,geometry:sourceGraphics.map(g=>({graphic_id:g.graphic_id,semantic_id:g.semantic_id,kind:g.kind,bounds:numeric(g.bounds),waypoints:g.waypoints})),sourceCoordinateGeometry:sourceGraphics.map(g=>({graphic_id:g.graphic_id,semantic_id:g.semantic_id,kind:g.kind,bounds:g.bounds,waypoints:g.waypoints,source_plane_index:g.source_plane_index}))};
}
