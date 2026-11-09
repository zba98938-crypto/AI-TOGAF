// Fixed browser-side renderer for source-DI process views with data depictions.
// All graphic ordering and geometry comes from the verified source plan.
export async function renderDataScene({spec,fontCSS}) {
  const NS='http://www.w3.org/2000/svg';
  const viewer=new window.BpmnJS({container:'#canvas',textRenderer:{defaultStyle:{fontFamily:'TogafCJK',fontSize:14},externalStyle:{fontFamily:'TogafCJK',fontSize:13}}});
  const parsed=await viewer.get('moddle').fromXML(spec.notation_xml);
  if(parsed.warnings.length)throw new Error('Native model parse warnings: '+parsed.warnings.map(w=>w.message).join('; '));
  const nodes=parsed.elementsById,symbols=viewer.get('bpmnRenderer');
  const add=(parent,tag,attrs={})=>{const e=document.createElementNS(NS,tag);for(const [k,v] of Object.entries(attrs))if(v!==null&&v!==undefined)e.setAttribute(k,String(v));parent.append(e);return e;};
  const svg=add(document.querySelector('#scene'),'svg',{xmlns:NS,version:'1.1'});
  add(add(svg,'defs'),'style').textContent=fontCSS+'text{font-family:TogafCJK,sans-serif}';
  const scene=add(svg,'g',{'data-native-root':spec.root_id}),elements=new Map(),common=[],labels=[];
  const numberBox=b=>Object.fromEntries(Object.entries(b).map(([k,v])=>[k,Number(v)]));
  const geometry=spec.graphics.map(g=>({graphic_id:g.graphic_id,semantic_id:g.semantic_id,kind:g.kind,bounds:g.bounds,waypoints:g.waypoints,source_plane_index:g.source_plane_index}));
  // Prepare endpoint objects before drawing. Their references may point forward
  // in source plane order, which is a z-order and not a construction order.
  for(const g of spec.graphics){
    const bo=nodes[g.semantic_id];if(!bo)throw new Error('Native semantic object missing '+g.semantic_id);
    const element={id:g.graphic_id,type:bo.$type,businessObject:bo,di:nodes[g.graphic_id]||{$type:g.kind==='shape'?'bpmndi:BPMNShape':'bpmndi:BPMNEdge',...g.attributes},parent:{businessObject:nodes[spec.root_id]}};
    if(g.kind==='shape')Object.assign(element,numberBox(g.bounds));
    else element.waypoints=g.waypoints.map(numberBox);
    elements.set(g.graphic_id,element);
  }
  function label(parent,name,g,edge=false){
    if(!name)return;
    const supplied=g.label_bounds;
    let b;
    if(supplied){b=numberBox(supplied);if(!edge){b.x-=Number(g.bounds.x);b.y-=Number(g.bounds.y);}}
    else if(edge){const p=g.waypoints[Math.floor(g.waypoints.length/2)];b={x:Number(p.x)-80,y:Number(p.y)-24,width:160,height:22};}
    else b={x:Number(g.bounds.width)/2-80,y:Number(g.bounds.height)+6,width:160,height:Math.max(22,Math.ceil(name.length/11)*17)};
    const ctx=document.createElement('canvas').getContext('2d');ctx.font='13px TogafCJK';
    const lines=[];let line='';
    for(const ch of name){if(ch==='\n'||line&&ctx.measureText(line+ch).width>b.width-8){lines.push(line);line='';}if(ch!=='\n')line+=ch;}
    lines.push(line);
    if(supplied&&lines.length*16.25>b.height)throw new Error('diagram-capacity: data label exceeds source BPMNLabel Bounds: '+name);
    const t=add(parent,'text',{'font-size':13,'text-anchor':'middle',fill:'#111','data-native-label':name});
    lines.forEach((value,i)=>{add(t,'tspan',{x:b.x+b.width/2,y:b.y+13+i*16.25}).textContent=value;});
    labels.push({semantic_id:g.semantic_id,name,lines,source_bounds:supplied||null,origin:supplied?'source BPMNLabel':'derived typography placement; source node/edge geometry unchanged'});
  }
  for(const g of spec.graphics){
    const bo=nodes[g.semantic_id],element=elements.get(g.graphic_id);
    const attrs={'data-element-id':g.semantic_id,'data-di-id':g.graphic_id,'data-native-type':g.type,'data-source-plane-index':g.source_plane_index};
    if(g.kind==='shape'){
      Object.assign(attrs,{transform:`translate(${g.bounds.x},${g.bounds.y})`,'data-di-x':g.bounds.x,'data-di-y':g.bounds.y,'data-di-width':g.bounds.width,'data-di-height':g.bounds.height});
      const group=add(scene,'g',attrs);
      if(bo.eventDefinitionRef?.length)bo.eventDefinitions=[...(bo.eventDefinitions||[]),...bo.eventDefinitionRef];
      if(bo.eventDefinitionRefs?.length)bo.eventDefinitions=[...(bo.eventDefinitions||[]),...bo.eventDefinitionRefs];
      symbols.drawShape(group,element);
      if(['dataInput','dataOutput','dataObjectReference','dataStoreReference'].includes(g.type)||/Event$|Gateway$/.test(bo.$type)){
        const state=g.type==='dataObjectReference'&&bo.dataState?.name;
        label(group,g.name+(state?' ['+state+']':''),g);
      }
    }else{
      attrs['data-source-waypoints']=JSON.stringify(g.waypoints);
      attrs['data-source-di-endpoint']=g.source_graphic_id;attrs['data-target-di-endpoint']=g.target_graphic_id;
      const group=add(scene,'g',attrs);
      element.source=elements.get(g.source_graphic_id);element.target=elements.get(g.target_graphic_id);
      if(!element.source||!element.target)throw new Error('Data DI connection endpoint missing '+g.graphic_id);
      symbols.drawConnection(group,element);label(group,g.name,g,true);
    }
    common.push({graphic_id:g.graphic_id,semantic_id:g.semantic_id,type:bo.$type});
  }
  const actual=[...scene.children].filter(e=>e.hasAttribute('data-di-id')).map(e=>e.getAttribute('data-di-id'));
  if(JSON.stringify(actual)!==JSON.stringify(spec.graphics.map(g=>g.graphic_id)))throw new Error('Data DI plane order differs from source');
  for(const [id,name] of Object.entries(spec.visible_names))if(!svg.textContent.replace(/\s+/g,'').includes(name.replace(/\s+/g,'')))throw new Error('Data DI omitted visible name '+id);
  const box=scene.getBBox(),margin=12,width=Math.ceil(box.width+margin*2),height=Math.ceil(box.height+margin*2);
  svg.setAttribute('viewBox',`${box.x-margin} ${box.y-margin} ${width} ${height}`);svg.setAttribute('width',width);svg.setAttribute('height',height);
  return {svg:new XMLSerializer().serializeToString(svg),graphicIds:actual,commonSymbols:common,labelLayouts:labels,geometry};
}
