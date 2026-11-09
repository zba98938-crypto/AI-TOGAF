#!/usr/bin/env python3
"""Self-contained static reader: overview, state detail, guarded flow, tables.
All diagrams are disclosed project projections, never strict standard notation.
"""
import argparse,html,json,unicodedata
from pathlib import Path
W,H=1920,1080

def wrap(text,width=29):
    lines=[];line='';size=0
    for c in text:
        n=2 if unicodedata.east_asian_width(c) in ('W','F') else 1
        if size+n>width:lines.append(line);line='';size=0
        line+=c;size+=n
    if line:lines.append(line)
    return lines

def text(x,y,value,size=24,fill='#172b4d',anchor='start',width=29):
    return ''.join(f'<text x="{x}" y="{y+i*(size+8)}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{html.escape(line)}</text>' for i,line in enumerate(wrap(value,width)))

def base(title,subtitle):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#506781"/></marker></defs><rect width="1920" height="1080" fill="#f6f9fc"/><g font-family="PingFang SC, Noto Sans CJK SC, Arial, sans-serif">',text(65,68,title,36,width=80),text(65,111,subtitle,22,width=130)]

def finish(svg):
    return ''.join(svg+[text(65,1051,'合成企业 / 项目简化关系图 / 不代表真实批准、实施或严格建模语言一致性',20,width=130),'</g></svg>'])

def box(svg,x,y,label,heading,width=490,height=145,color='#dbeafe'):
    svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="16" fill="white" stroke="#b8cbe1" stroke-width="2"/><rect x="{x}" y="{y}" width="{width}" height="35" rx="12" fill="{color}"/>')
    svg.append(text(x+20,y+25,heading,18,width=60));svg.append(text(x+20,y+70,label,24,width=36))

def arrow(svg,x1,y1,x2,y2,label,dashed=False):
    svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{ "#b45309" if dashed else "#506781"}" stroke-width="3" fill="none" marker-end="url(#arrow)"'+(' stroke-dasharray="8 6"' if dashed else '')+'/>')
    if y1==y2:x=(x1+x2)/2;y=y1-35
    else:x=x1+18;y=(y1+y2)/2-4
    svg.append(text(x,y,label,18,anchor='middle' if y1==y2 else 'start',width=14))

def overview(model):
    c=model['extension_data']['enterprise:closure'];ent={e['id']:e for e in model['entities']};stages=c['adm_chain']
    svg=base('订单履约与跨基地一致性：完整设计链','关注点 → 需求 → 四域架构 → 差距与方案 → 工作包与过渡 → 合规与价值；业务决定待独立复核')
    positions=[]
    for i,stage in enumerate(stages):
        row=i//3;column=i%3 if row%2==0 else 2-i%3;positions.append((65+column*630,155+row*217))
    for i in range(len(stages)-1):
        x,y=positions[i];nx,ny=positions[i+1];a=stages[i]['entity_ids'][0];b=stages[i+1]['entity_ids'][0]
        edge=next(e for e in model['relationships'] if e['source']==a and e['target']==b and e['type']!='traces_to')
        label=edge['label']
        if y==ny:arrow(svg,x+490 if nx>x else x,y+72,nx if nx>x else nx+490,ny+72,label)
        else:arrow(svg,x+245,y+145,nx+245,ny,label)
    for i,stage in enumerate(stages):box(svg,*positions[i],ent[stage['entity_ids'][0]]['name'],str(i+1).zfill(2)+' / '+stage['stage'])
    return finish(svg)

def states(model):
    svg=base('基线 / 可运营过渡 / 目标：同一概念的版本','领域分层、稳定 concept_id；每个状态都保留订单入口、对账责任与回退约束，不暗示已投产。')
    for row,(d,name,identity) in enumerate([('business','业务流程','order-fulfillment'),('data','信息与数据','order-event'),('application','应用与接口','order-hub'),('technology','技术平台','event-platform')]):
        y=166+row*210
        for col,state in enumerate(['baseline','transition','target']):
            x=65+col*630;entry=next(e for e in model['entities'] if e['id']=='closure-'+identity+'-'+state)
            box(svg,x,y,entry['name'],name+' / '+state,height=166)
            svg.append(text(x+20,y+116,entry['attributes'].get('architecture_detail',{}).get('summary','未提供状态机制'),20,width=42))
            if col<2:arrow(svg,x+490,y+72,x+630,y+72,'版本演进')
    return finish(svg)

def rollback(model):
    ent={e['id']:e for e in model['entities']};svg=base('回退控制：守卫、补偿与不可逆操作','蓝线为正常控制；黄虚线为补偿/异常；缺恢复点即中止。外部结算不得声称自动撤销。全部守卫与控制边另有静态明细。')
    pos={'start':(65,175),'check':(695,175),'restore':(1325,175),'verify':(1325,415),'settle':(695,415),'done':(65,415),'reconcile':(695,725),'abort':(1325,725)}
    flow=model['extension_data']['enterprise:closure']['flows'][0]
    for e in model['relationships']:
        if e['id'] not in flow['edge_ids']:continue
        a=e['source'].removeprefix('closure-flow-');b=e['target'].removeprefix('closure-flow-');x,y=pos[a];nx,ny=pos[b]
        if a=='check' and b=='abort':
            svg.append('<path d="M940 175 L940 150 L1840 150 L1840 797 L1815 797" stroke="#b45309" stroke-width="3" stroke-dasharray="8 6" fill="none" marker-end="url(#arrow)"/>');svg.append(text(1450,145,'恢复点无效 → 中止',18,width=60));continue
        if a=='restore' and b=='reconcile':
            svg.append('<path d="M1815 248 L1828 248 L1828 690 L940 690 L940 725" stroke="#b45309" stroke-width="3" stroke-dasharray="8 6" fill="none" marker-end="url(#arrow)"/>');svg.append(text(1390,678,'恢复失败 → 补偿与人工对账',18,width=55));continue
        if a=='verify' and b=='reconcile':
            svg.append('<path d="M1570 560 L1570 635 L940 635 L940 725" stroke="#b45309" stroke-width="3" stroke-dasharray="8 6" fill="none" marker-end="url(#arrow)"/>');svg.append(text(1360,620,'对账不一致',18,width=35));continue
        if a=='settle' and b=='reconcile':
            svg.append('<path d="M940 560 L940 725" stroke="#b45309" stroke-width="3" stroke-dasharray="8 6" fill="none" marker-end="url(#arrow)"/>')
            svg.append(text(963,597,'结算失败：禁止自动撤销，转人工对账',18,width=48));continue
        if y==ny:arrow(svg,x+490 if nx>x else x,y+72,nx if nx>x else nx+490,ny+72,({'restore_valid': '恢复点有效', 'consistent': '对账一致'}.get(e.get('attributes',{}).get('guard',{}).get('field'),e['label'])),e['type'].startswith('enterprise:'))
        else:arrow(svg,x+245,y+145,nx+245,ny,({'restore_valid': '恢复点有效', 'consistent': '对账一致'}.get(e.get('attributes',{}).get('guard',{}).get('field'),e['label'])),e['type'].startswith('enterprise:'))
    for n,(x,y) in pos.items():
        entry=ent['closure-flow-'+n];attrs=entry['attributes'];kind='终态' if attrs.get('terminal') else '守卫决策' if entry['type']=='decision' else '不可逆操作' if attrs.get('irreversible') else '控制步骤'
        box(svg,x,y,entry['name'],kind,color='#fff0ca' if attrs.get('irreversible') else '#dbeafe')
    return finish(svg)

def render(model,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);closure=model['extension_data']['enterprise:closure'];ent={e['id']:e for e in model['entities']}
    pages={'overview.svg':overview(model),'states.svg':states(model),'rollback.svg':rollback(model)}
    for n,s in pages.items():(out/n).write_text(s)
    def table(headers,rows):return '<table><thead><tr>'+''.join('<th>'+html.escape(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(c))+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table>'
    relationships=[e for e in model['relationships'] if e['id'].startswith('closure-edge')]
    rows=[[ent[e['source']]['name'],e['label'],ent[e['target']]['name'],e['type'],e.get('attributes',{}).get('guard','—')] for e in relationships]
    quality=[[e['dimension'],e['value'],e['unit'],str(e.get('numerator','—'))+'/'+str(e.get('denominator','—')),e.get('threshold',e.get('tolerance','—')),e['period_start']+' / '+e['period_end'],ent[e['owner_id']]['name'],'独立合成台账'] for e in closure['evidence_records']]
    content=''.join('<section class="diagram"><img src="'+n+'" alt="'+n+'"></section>' for n in pages)
    labels={'summary':'状态摘要','mechanism':'运作机制','sites':'基地数','max_latency_minutes':'最大延迟（分钟）','key':'业务键','contract':'契约版本','delivery':'交付保证','components':'组成','interface_mode':'接口方式','fault_domains':'故障域数','retention_hours':'保留（小时）','fallback':'回退路径','owner_id':'责任主体'}
    def state_detail(detail):
        return '\n'.join(labels.get(k,k)+'：'+(ent.get(v,{}).get('name',v) if k=='owner_id' else ' / '.join(map(str,v)) if isinstance(v,list) else str(v)) for k,v in detail.items() if k!='classification')
    state_rows=[[e.get('context',{}).get('evolution'),e['name'],state_detail(e['attributes']['architecture_detail']), '合成设计假设 / 未实施'] for e in model['entities'] if 'architecture_detail' in e.get('attributes',{})]
    for start in range(0,len(state_rows),6):content+='<section><h1>四域状态差异与运行约束 '+str(start//6+1)+'</h1>'+table(['状态','架构概念','具体机制、契约与责任','事实边界'],state_rows[start:start+6])+'</section>'
    content+='<section><h1>数据质量、风险与恢复：结构化决策表</h1><p>全部数值为独立模拟政策/观测，不能视为百万交易 SQL 审计统计或真实授权。</p>'+table(['维度','观测','单位','计数口径','阈值/容忍','期间','责任主体','分类'],quality)+'<h2>缺陷与处置</h2>'+table(['缺陷类别','数量','处置'],[['missing-master-key',10,'模拟隔离'],['duplicate-event',10,'模拟隔离']])+'</section>'
    for i in range(0,len(rows),9):content+='<section><h1>关系明细 '+str(i//9+1)+'</h1><p>静态页面直接给出端点、领域语义及控制守卫；无需点击节点才能理解。</p>'+table(['来源','实际含义','目标','关系类型','守卫'],rows[i:i+9])+'</section>'
    transition_state=next(s for s in model['states'] if s['evolution']=='transition')
    conditions=transition_state['operating_conditions']
    labels={'operations':'运营与责任','data_consistency':'数据一致性','dependencies':'运行依赖','controls':'控制与例外','rollback':'回退与不可逆操作'}
    content+='<section><h1>可运营过渡条件（合成设计）</h1><p>当前为候选设计，未实施、未取得真实批准；五项运行条件不从图可达性推断。</p>'+table(['运行维度','具体条件与责任'],[[label,conditions[key]] for key,label in labels.items()])+'</section>'
    content+='<section><h1>工程与验收附录</h1><pre>'+html.escape(json.dumps({'classification':'synthetic','acceptance':closure['acceptance'],'recovery_exercises':closure['recovery_exercises']},ensure_ascii=False,indent=2))+'</pre></section>'
    doc='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>合成企业架构设计闭环</title><style>@page{size:A3 landscape;margin:12mm}body{font:20px "PingFang SC",Arial,sans-serif;color:#172b4d;background:#f6f9fc;margin:0}section{padding:36px;max-width:1848px;margin:auto;break-after:page}.diagram{padding:0}.diagram img{width:100%;display:block}h1{font-size:32px}table{border-collapse:collapse;width:100%;font-size:19px;table-layout:fixed}th,td{border:1px solid #bccddd;padding:12px;overflow-wrap:anywhere;vertical-align:top;white-space:pre-line}th{background:#dbeafe}pre{white-space:pre-wrap;font-size:20px}@media print{body{background:white;font-size:12pt}section{padding:0;max-width:none}table{font-size:10.5pt}td,th{padding:6pt}h1{font-size:20pt}pre{font-size:11pt}.diagram img{height:267mm;object-fit:contain}}</style>'+content+'</html>'
    (out/'reader.html').write_text(doc)
    # Explicit coverage is limited to the selected decision scope; no transaction-record dump.
    selected=set(e for s in closure['adm_chain'] for e in s['entity_ids'])|set(e for f in closure['flows'] for e in f['node_ids'])|{e['id'] for e in model['entities'] if e.get('concept_id') in ['order-fulfillment','order-event','order-hub','event-platform']}
    (out/'coverage.json').write_text(json.dumps({'notation':'project-reading-projection','selected_entity_ids':sorted(selected),'selected_relationship_ids':[e['id'] for e in relationships],'relationship_static_pages':True,'transaction_projection_included':False,'body_font_px':24,'edge_font_px':18,'print_table_font_pt':10.5,'source_equivalence':False},indent=2))
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--model',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();render(json.loads(a.model.read_text()),a.out)
