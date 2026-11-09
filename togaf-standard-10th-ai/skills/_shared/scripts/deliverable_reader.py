"""Readable projection of authored section evidence; raw ledgers remain appendices."""


def reader_sections(model, assembly):
    entities={e['id']:e for e in model.get('entities',[])}
    sources={s['id']:s for s in model.get('sources',[])}
    relationships={r['id']:r for r in model.get('relationships',[])}
    output=[]
    for block in assembly['section_blocks']:
        records=[entities[eid] for eid in block.get('direct_entity_ids',[])
                 if eid in entities and entities[eid].get('attributes',{}).get('record_contract')=='scenario-section/2']
        if not records:return None
        text='章节状态：'+block.get('coverage_status','not-assessed')+'；情景论证，不是实际签署。\n\n'
        for record in records:
            a=record['attributes']
            for label,key in [('决策问题','question'),('结论','conclusion'),('范围','scope'),
                              ('候选责任','owner'),('验收方法（尚未执行）','acceptance')]:
                text+='**'+label+'**：'+str(a.get(key,'未提供'))+'\n\n'
            if a.get('decision') and a['decision']!=a.get('conclusion'):
                text+='**候选决策**：'+str(a['decision'])+'\n\n'
            for label,key,empty in [('权衡','tradeoffs','尚未记录'),('未知／待核验','unknowns','此记录未声明；不表示实际验证完成'),
                                    ('必要证据缺口','evidence_gaps','无新增结构缺口；不表示业务接受')]:
                values=a.get(key,[])
                text+='**'+label+'**：'+('；'.join(map(str,values)) if isinstance(values,list) and values else str(values) if values else empty)+'\n\n'
            refs=a.get('model_refs',[])
            text+='**对象支撑**：'+'；'.join(entities.get(i,{}).get('name',i)+' `'+i+'`' for i in refs)+'\n\n'
            for rid in a.get('relationship_refs',[]):
                r=relationships.get(rid,{})
                text+='- 论证链 `'+rid+'`：`'+str(r.get('source','未知'))+'` → `'+str(r.get('target','未知'))+'`；'+str(r.get('label','未说明'))+'。\n'
            analyses=a.get('analysis_refs',[])
            if analyses:text+='\n**分析依据**：'+', '.join('`'+i+'`' for i in analyses)+'；计算结果及完整规则见技术附录。\n\n'
            for sid in record.get('evidence',[]):
                s=sources.get(sid,{})
                text+='- 来源 `'+sid+'`：'+str(s.get('description','未定位'))+'；定位：`'+str(s.get('locator','未提供'))+'`。\n'
        views=block.get('view_ids',[])+block.get('supplemental_view_ids',[])
        if views:text+='\n**关键制品**：'+'、'.join('[`'+v+'`](../artifacts/'+v+'.md)' for v in dict.fromkeys(views))+'。\n'
        output.append({'title':block['title'],'markdown':text})
    if assembly.get('gaps') and output:
        output[-1]['markdown']+='\n### 不可省略的组装缺口\n\n'+''.join(
            '- `'+g['id']+'`：'+g['message']+'；需要：'+str(g.get('needed_input','按缺口补证'))+'。\n' for g in assembly['gaps'])
    return output
