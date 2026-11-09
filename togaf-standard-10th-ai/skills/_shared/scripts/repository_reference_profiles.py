"""Operational views for G186 reference trees, version comparison and concern mapping.
The local source interpretations are examples, never imported enterprise facts.
"""
import json
from pathlib import Path
from specialized_view_profiles import entity,edge,profile
ROOT=Path(__file__).resolve().parents[1]

def source(fig):return json.loads((ROOT/'references/source-structures'/('G186-'+fig+'.json')).read_text())

def extensions(types,rels):
    return {'entity_types':{},
            'relationship_types':{r:{'source_types':list(types),'target_types':list(types),'meaning':'显式包含或职责映射，不表示流程或批准'} for r in rels}}

def make(pid,name,fig,kind,es,rs,artifact=None):
    types={e['type'] for e in es};rels={r['type'] for r in rs}
    return profile(pid,artifact or pid,name,'togaf-ea-capability',['G186/'+fig],kind,es,rs,extensions(types,rels),
       ['按显式关系与状态读取；来源解释不代表本地组织事实。','折叠不等于空；选中不等于差异；不从布局推断语义。'])

def tree(fig,pid,name):
    d=source(fig);es=[];rs=[]
    for e in d['elements']:
        es.append(entity(e['id'],'g186:repository_node',e.get('label_en') or e.get('label_zh') or e['id'],
            definition=e.get('description_zh',e.get('label_zh',e['id'])),parent_id=e.get('parent'),
            node_kind='view-folder' if e['type']=='group' else 'state-container',
            disclosure='visible-source-excerpt; folded contents unknown'))
        if e.get('parent'):rs.append(edge('contains-'+e['id'],e['parent'],e['id'],'g186:contains','包含（不表示时间或依赖）'))
    return make(pid,name,fig,'repository-tree',es,rs)

def comparison(reverse=False):
    d=source('fig13-1');es=[];rs=[]
    from_state,to_state=('Baseline','Target') if reverse else ('Target','Baseline')
    es=[entity('snapshot-from','g186:repository_snapshot',from_state,definition='比较起点，方向必须先于差异解释',snapshot=from_state),
        entity('snapshot-to','g186:repository_snapshot',to_state,definition='比较终点，导航到同ID明细',snapshot=to_state)]
    rows=d['tables'][0]['rows']
    for i,row in enumerate(rows):
        changed=row[2]=='浅蓝'
        baseline={'definition':row[0]+' / baseline'};target={'definition':row[0]+(' / revised' if changed else ' / baseline')}
        a,b=(baseline,target) if reverse else (target,baseline)
        es.append(entity('diff-'+str(i),'g186:comparison_item',row[0],definition=row[1],from_values=a,to_values=b,from_children=[],to_children=[]))
        rs.extend([edge('from-'+str(i),'snapshot-from','diff-'+str(i),'g186:compares_from','源架构导航'),edge('to-'+str(i),'diff-'+str(i),'snapshot-to','g186:compares_to','目标架构导航')])
    pid='repository-baseline-target-comparison' if reverse else 'repository-target-baseline-comparison'
    return make(pid,'存储库版本比较 '+from_state+' → '+to_state,'fig13-2' if reverse else 'fig13-1','repository-comparison',es,rs,'repository-target-baseline-comparison')

def continuum():
    labels=['维持：与他人持平','维持：保持相同优势','改进：创造竞争优势','改进：创造新收入流']
    es=[entity('continuum','g186:continuum','能力与项目连续谱',definition='0–10无单位；标签仅有阅读顺序，无精确分段值、时间或成熟度含义',scale_min=0,scale_max=10,unit='unitless')]
    es += [entity('position-'+str(i),'g186:continuum_label',s,definition=s,order=i+1) for i,s in enumerate(labels)]
    return make('capability-project-continuum','能力与项目连续谱','fig8-1','capability-continuum',es,[])

def concern_matrix():
    d=source('tabB-1');rows=d['tables'][0]['rows'];sh=[e for e in d['elements'] if e['type']=='stakeholder'];cn=[e for e in d['elements'] if e['type']=='requirement']
    es=[entity(e['id'],'g186:stakeholder' if e['type']=='stakeholder' else 'g186:concern',e['label_zh'],definition=e['label_en'],order=e['order'],purpose='portfolio') for e in sh+cn]
    rs=[edge('responsibility-'+str(i)+'-'+str(j),sh[i]['id'],cn[j]['id'],'g186:responsibility','X：来源表已标注对应职责（非RACI）') for i,row in enumerate(rows) for j,value in enumerate(row[1:]) if value=='X']
    p=make('portfolio-stakeholder-concern-matrix','组合利益相关者×关注点矩阵','tabB-1','stakeholder-concern-matrix',es,rs)
    p['example']['view']['legend']='X=已标注职责；空白=来源表未标注，不能据此断言无关注；非RACI，仅适用于组合目的。'
    return p

def build():
    return [tree('fig5-2','repository-state-view-tree','存储库状态与视图树'),tree('fig5-3','repository-parallel-candidates','存储库并行候选容器'),comparison(),comparison(True),continuum(),concern_matrix()]

def difference(e):
    a=e['attributes'];before=a.get('from_values');after=a.get('to_values')
    if before is None:return 'added'
    if after is None:return 'deleted'
    if a.get('from_children')!=a.get('to_children'):return 'different-children'
    return 'different-attributes' if before!=after else 'unchanged'

def check(es,rs,kind):
    errors=[];byid={e['id']:e for e in es}
    def need(ok,code,identity):
        if not ok:errors.append({'code':code,'id':identity})
    if kind=='repository-tree':
        for e in es:
            parent=e['attributes'].get('parent_id');seen={e['id']};cursor=parent
            need(not parent or any(r['source']==parent and r['target']==e['id'] and r['type']=='g186:contains' for r in rs),'repository-tree-parent-link',e['id'])
            while cursor in byid:
                if cursor in seen:need(False,'repository-tree-cycle',e['id']);break
                seen.add(cursor);cursor=byid[cursor]['attributes'].get('parent_id')
    elif kind=='repository-comparison':
        snapshots=[e for e in es if e['type']=='g186:repository_snapshot']
        need(len(snapshots)==2,'comparison-snapshots',kind)
        for e in es:
            if e['type']!='g186:comparison_item':continue
            a=e['attributes'];need(all(k in a for k in ['from_values','to_values','from_children','to_children']),'comparison-missing-snapshot-values',e['id'])
            for typ in ['g186:compares_from','g186:compares_to']:
                matches=[r for r in rs if r['type']==typ and (r['target']==e['id'] if typ.endswith('from') else r['source']==e['id'])]
                need(len(matches)==1 and byid.get(matches[0]['source'] if typ.endswith('from') else matches[0]['target'],{}).get('type')=='g186:repository_snapshot','comparison-navigation-missing',e['id'])
    elif kind=='capability-continuum':
        axes=[e for e in es if e['type']=='g186:continuum'];need(len(axes)==1,'continuum-axis',kind)
        if axes:need(tuple(axes[0]['attributes'].get(k) for k in ['scale_min','scale_max','unit'])==(0,10,'unitless'),'continuum-fabricated-unit',axes[0]['id'])
    elif kind=='stakeholder-concern-matrix':
        for r in rs:need(byid[r['source']]['type']=='g186:stakeholder' and byid[r['target']]['type']=='g186:concern','concern-matrix-endpoints',r['id'])
        need(all(e['attributes'].get('purpose')=='portfolio' for e in es),'concern-matrix-purpose',kind)
    return errors

def render(d,es,rs,kind):
    from html import escape
    if kind=='repository-tree':
        byid={e['id']:e for e in es};children={};roots=[]
        for e in es:
            parent=e['attributes'].get('parent_id')
            if parent in byid:children.setdefault(parent,[]).append(e)
            else:roots.append(e)
        seen=set();y=170
        def visit(e,depth):
            nonlocal y
            if e['id'] in seen:return
            seen.add(e['id']);d.card(e,30+depth*65,y,850,None,fields=['node_kind','disclosure']);y+=d.positions[e['id']][3]+32
            for c in children.get(e['id'],[]):visit(c,depth+1)
        for e in roots+es:visit(e,0)
        # Indentation gives the tree; link records explicitly state containment.
        d.text(30,125,'缩进=显式包含；折叠内容未知；并列容器独立，视图文件夹不是ADM阶段。',16,units=130)
    elif kind=='repository-comparison':
        snapshots=[e for e in es if e['type']=='g186:repository_snapshot'];y=170
        for i,e in enumerate(snapshots):d.card(e,30+i*800,y,680,None,fields=['snapshot'])
        y+=max([d.positions[e['id']][3] for e in snapshots]+[100])+50
        colors={'added':'#d5edd7','deleted':'#f3d3d3','different-children':'#fff0af','different-attributes':'#d9edfa','unchanged':'#f4f4f4'}
        d.text(30,y,'绿色=新增；红色=删除；黄色=子项差异；浅蓝=属性差异；灰色=无变化。导航至伴随明细的源/目标值。',16,units=155);y+=45
        for e in es:
            if e['type']!='g186:comparison_item':continue
            d.card(dict(e,name=e['name']+' / '+difference(e)),30,y,1450,None,colors[difference(e)],fields=['from_values','to_values','from_children','to_children']);y+=d.positions[e['id']][3]+30
    elif kind=='capability-continuum':
        axis=next((e for e in es if e['type']=='g186:continuum'),None)
        if axis:d.card(axis,30,160,1400,None,fields=['scale_min','scale_max','unit'])
        y=d.height+65;d.rect(30,y,1400,28,'#3a7eae')
        for n in range(11):d.text(30+n*140,y-15,str(n),15,anchor='middle')
        y+=70
        for i,e in enumerate(sorted([e for e in es if e!=axis],key=lambda e:e['attributes'].get('order',0))):d.card(e,30+i*370,y,330,None,fields=['order'])
        d.text(30,d.height+45,'等距标签只表达阅读顺序；没有分段数值、箭头、日期、阶段门或成熟度等级。',16,units=150)
    elif kind=='stakeholder-concern-matrix':
        rows=sorted([e for e in es if e['type']=='g186:stakeholder'],key=lambda e:e['attributes']['order']);cols=sorted([e for e in es if e['type']=='g186:concern'],key=lambda e:e['attributes']['order'])
        w=120;x0=300
        header_h=max([d.card_height(e,w-4,fields=[]) for e in cols]+[120])
        for j,e in enumerate(cols):d.card(e,x0+j*w,150,w-4,header_h,fields=[])
        y=150+header_h+25
        for e in rows:
            row_h=max(80,d.card_height(e,250,fields=[]))
            d.card(e,30,y,250,row_h,fields=[])
            for j,c in enumerate(cols):
                x=x0+j*w;d.rect(x,y,w-4,row_h,'#f7f9fc')
                for r in rs:
                    if (r['source'],r['target'])==(e['id'],c['id']):
                        d.parts.append('<g data-relationship-id="'+escape(r['id'])+'">');d.text(x+w/2,y+row_h/2+7,'X',22,anchor='middle');d.parts.append('</g>');d.relation_ids.add(r['id'])
            y+=row_h+15
        d.text(30,d.height+45,'X：来源已标注对应职责；空白：未标注。非RACI；仅适用于组合目的。',16,units=170)
