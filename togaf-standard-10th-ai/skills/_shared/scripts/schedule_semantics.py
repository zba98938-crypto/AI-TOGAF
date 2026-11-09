"""Date and hierarchy invariants shared by validation and rendering."""
from datetime import date

def is_milestone(e):
    a=e.get('attributes',{})
    return e['type']=='milestone' or a.get('milestone') is True or a.get('kind')=='milestone'

def span(e):
    a=e.get('attributes',{})
    try:
        start=date.fromisoformat(str(a.get('start',a.get('start_date')))).toordinal()
        raw=a.get('end',a.get('end_date'))
        end=date.fromisoformat(str(raw)).toordinal() if raw else start if is_milestone(e) else start+int(a['duration_days'])
        return (start,end,raw) if end>=start else None
    except (ValueError,TypeError,KeyError,OverflowError):
        return None

def hierarchy(es):
    byid={e['id']:e for e in es};children={};roots=[]
    for e in es:
        parent=e.get('attributes',{}).get('parent_id')
        if parent in byid:children.setdefault(parent,[]).append(e)
        else:roots.append(e)
    ordered=[];seen=set()
    def walk(e,depth):
        if e['id'] in seen:return
        seen.add(e['id']);ordered.append((e,depth))
        for child in children.get(e['id'],[]):walk(child,depth+1)
    for e in roots:walk(e,0)
    for e in es:walk(e,0)
    spans={e['id']:span(e) for e in es}
    for e,depth in reversed(ordered):
        kids=[spans[k['id']] for k in children.get(e['id'],[]) if spans[k['id']]]
        a=e.get('attributes',{})
        if kids and not any(k in a for k in ('start','start_date','end','end_date','duration_days')):
            spans[e['id']]=(min(s[0] for s in kids),max(s[1] for s in kids),None)
    return ordered,children,spans

def check_schedule(es):
    errors=[];byid={e['id']:e for e in es}
    def issue(code,e,message):errors.append({'code':code,'id':e['id'],'message':message})
    ordered,children,spans=hierarchy(es)
    # Undated status roadmaps are valid; partially dated schedules are not.
    dated=any(any(k in e.get('attributes',{}) for k in ('start','start_date','end','end_date')) for e in es)
    for e in es:
        parent=e.get('attributes',{}).get('parent_id');seen={e['id']};cursor=parent
        if parent and parent not in byid:issue('schedule-parent-missing',e,'父项不存在。')
        while cursor in byid:
            if cursor in seen:
                issue('schedule-parent-cycle',e,'父项构成循环。');break
            seen.add(cursor);cursor=byid[cursor].get('attributes',{}).get('parent_id')
        value=spans[e['id']]
        if dated and value is None:issue('missing-or-invalid-schedule',e,'排期需要有效起止日期或可汇总的子项。')
        if value and is_milestone(e) and value[0]!=value[1]:issue('schedule-milestone-duration',e,'里程碑必须为零工期，活动及其完成说明分别表达。')
        if value and parent in spans and spans[parent]:
            p=spans[parent]
            if value[0]<p[0] or value[1]>p[1]:issue('schedule-child-outside-parent',e,'子项日期超出父项范围。')
    return errors
