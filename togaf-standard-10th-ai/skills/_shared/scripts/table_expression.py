"""Render selected table content and record exactly where its semantics appear.

Profiles may select extension types not present in a legacy artifact's columns.
The explicit field ledger prevents such objects or relationships disappearing.
"""
import json
from matrix_semantics import matrix_options, project_matrix, cell_label

VERSION = '1.2'

def value(item):
    return json.dumps(item,ensure_ascii=False,sort_keys=True) if not isinstance(item,str) else item

def render_table_expression(model,view,profile,table):
    entities={e['id']:e for e in model['entities']}
    relationships={r['id']:r for r in model['relationships']}
    es=[entities[i] for i in view['entity_ids']]
    rs=[relationships[i] for i in view['relationship_ids']]
    report={'renderer':'field-table','renderer_version':VERSION,'errors':[],'warnings':[],
            'represented_entity_ids':[],'represented_relationship_ids':[],
            'represented_attributes':{},'represented_relationship_attributes':{},
            'entity_field_locations':{},'relationship_field_locations':{},
            'unrepresented_entity_ids':[],'unrepresented_relationship_ids':[],
            'review_status':'generated-awaiting-review'}
    text='\n## 逐字段表达\n\n表格按所选对象类型分组；相邻行不表示依赖或包含。嵌套字段保持结构化原值。\n\n'
    if profile.get('renderer')=='matrix':
        options=matrix_options(profile)
        rows,cols,cells,outside=project_matrix(es,rs,options)
        if not rows or not cols:report['errors'].append({'code':'missing-matrix-axes','id':view.get('id')})
        else:
            text+='### 类型化行列矩阵\n\n'+table(['行对象／列对象']+[e['name']+' ['+e['id']+']' for e in cols],
                [[row['name']+' ['+row['id']+']']+['；'.join(cell_label(r,direction)+' {'+r['id']+'}' for r,direction in cells[(row['id'],col['id'])]) or '未记录' for col in cols] for row in rows])+'\n'
            text+='单元含义：'+str(options.get('cell_meaning','显式关系类型与代码；代码解释见图例，不默认解释为布尔关联'))+'。空白含义：'+str(options.get('empty_meaning','未记录≠不存在；不推断不适用或零分'))+'。\n\n'
        for identity in outside:report['errors'].append({'code':'relation-outside-matrix-axes','id':identity})
    for typ in dict.fromkeys(e['type'] for e in es):
        group=[e for e in es if e['type']==typ]
        requirement=profile.get('required_attributes',{})
        required=requirement.get(typ,[])+requirement.get('*',[]) if isinstance(requirement,dict) else requirement
        required=[k for k in required if k!='name']
        columns=list(dict.fromkeys(required+[key for e in group for key in e.get('attributes',{})]))
        extra=[k for k in ['state_id','concept_id','version','scope_id','approval_status','implementation_status','measurements'] if any(k in e for e in group)]
        headers=['ID','类型','名称']+columns+extra+['证据','确定性']
        orientation=profile.get('table_orientation','auto')
        if orientation not in ['auto','rows','records']:raise ValueError('未知表格方向：'+str(orientation))
        records=orientation=='records' or (orientation=='auto' and len(headers)>12)
        rows=[]
        for e in group:
            attrs=e.get('attributes',{})
            rows.append([e['id'],typ,e['name']]+[value(attrs[k]) if k in attrs else '未提供' for k in columns]+[value(e.get(k,'未提供')) for k in extra]+[value(e.get('evidence',[])),e.get('certainty','unknown')])
            report['represented_entity_ids'].append(e['id'])
            report['represented_attributes'][e['id']]=list(attrs)
            report['entity_field_locations'][e['id']]={k:{'table':e['id'] if records else typ,'row_id':k if records else e['id'],'column':'值' if records else k} for k in attrs}
            for key in required:
                if key not in attrs:report['errors'].append({'id':e['id'],'code':'missing-required-attribute','attribute':key})
        text+='### '+typ+'\n\n'
        if records:
            text+='字段较多或对象字段不同，逐对象显示字段／值；缺失项仍保留。\n\n'
            for e,row in zip(group,rows):
                text+='#### '+e['name']+' ['+e['id']+']\n\n'+table(['字段','值'],list(zip(headers,row)))+'\n'
        else:text+=table(headers,rows)+'\n'
    if rs:
        extra=[key for key in ['codes','cardinality','attributes','state_id','scope_id'] if any(key in r for r in rs)]
        text+='### 关系方向与条件\n\n'+table(['关系 ID','起点','语义','终点','说明']+extra+['证据','确定性'],
            [[r['id'],r['source'],r['type'],r['target'],r.get('label','')]+[value(r.get(k,'未提供')) for k in extra]+[value(r.get('evidence',[])),r.get('certainty','unknown')] for r in rs])+'\n'
        for r in rs:
            report['represented_relationship_ids'].append(r['id'])
            attrs=r.get('attributes',{})
            report['represented_relationship_attributes'][r['id']]=list(attrs)
            report['relationship_field_locations'][r['id']]={k:{'table':'关系方向与条件','row_id':r['id'],'column':'attributes','key':k} for k in attrs}
            for key in ['codes','cardinality']:
                if key in r:
                    fields=['cardinality.'+side for side in r[key]] if key=='cardinality' else ['codes']
                    report['represented_relationship_attributes'][r['id']].extend(fields)
                    for field in fields:report['relationship_field_locations'][r['id']][field]={'table':'关系方向与条件','row_id':r['id'],'column':key}
            required=profile.get('required_relationship_attributes',{})
            for key in required.get(r['type'],[])+required.get('*',[]):
                if key not in attrs:report['errors'].append({'id':r['id'],'code':'missing-required-relationship-attribute','attribute':key})
    return text,report
