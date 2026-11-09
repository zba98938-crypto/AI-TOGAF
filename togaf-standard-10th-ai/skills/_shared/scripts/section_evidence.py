"""Validate an opt-in project chapter record, not an official TOGAF entity type.

Only project:section_evidence has this operational contract. Other existing
entities keep their established rules. Structural checks cannot judge whether
business reasoning or a cited source is true; independent review is required.
"""
import re

TYPE='project:section_evidence'
SCENARIO_CONTRACT='scenario-section/2'
PLACEHOLDER=re.compile(r'虚构设定：.+的第\s*\d+\s*条说明|合成占位|目标态修订|待补正文|\b(?:TODO|TBD|placeholder)\b',re.I)

def check_section_record(entity, deliverable, title, sources, model=None):
    if entity.get('type')!=TYPE:return []
    errors=[];attrs=entity.get('attributes',{})
    def fail(code,message):errors.append({'code':code,'object_id':entity.get('id'),'message':message})
    if attrs.get('deliverable_id')!=deliverable.get('deliverable_id') or attrs.get('section_title')!=title:
        fail('assembly-section-record-identity','项目章节事实必须明确匹配当前交付物族及章节，不得跨章复用充数。')
    for field in ['decision','scope','owner','acceptance','status']:
        value=attrs.get(field)
        if not isinstance(value,str) or not value.strip():fail('assembly-section-record-field','项目章节事实缺少非空文本：'+field)
    for field in ['decision','acceptance','question','conclusion']:
        if isinstance(attrs.get(field),str) and PLACEHOLDER.search(attrs[field]):
            fail('assembly-section-placeholder','占位/批量属性修订不是章节推理或证据：'+field)
    # Unknowns can be an empty list only when the author explicitly asserts no
    # unknowns in this bounded record; absence is not equivalent to none.
    unknowns=attrs.get('unknowns')
    if not isinstance(unknowns,list) or not all(isinstance(x,str) and x.strip() for x in unknowns):
        fail('assembly-section-record-unknowns','项目章节事实必须显式列unknowns数组，未知不是0或默认已解决。')
    evidence=entity.get('evidence')
    if not isinstance(evidence,list) or not evidence:fail('assembly-section-record-evidence','项目章节事实没有来源依据ID。')
    else:
        for identity in evidence:
            if not isinstance(identity,str) or identity not in sources:fail('assembly-section-record-source','项目章节事实来源ID不存在：'+str(identity))
    if attrs.get('record_contract') not in [None,SCENARIO_CONTRACT]:
        fail('assembly-section-record-contract','未识别的章节契约版本，不能静默退回旧结构。')
    if attrs.get('record_contract')==SCENARIO_CONTRACT:
        for field in ['question','conclusion']:
            if not isinstance(attrs.get(field),str) or not attrs[field].strip():
                fail('assembly-section-reasoning','情景章节须有针对性问题与可读结论：'+field)
        for field in ['tradeoffs','model_refs','analysis_refs','evidence_gaps']:
            value=attrs.get(field)
            if not isinstance(value,list) or not all(isinstance(x,str) and x.strip() for x in value) or (field!='evidence_gaps' and not value):
                fail('assembly-section-support','情景章节须显式声明非空权衡、模型和分析支撑；evidence_gaps可为空：'+field)
        if attrs.get('authority')!='scenario-authority' or attrs.get('status')!='scenario-proposal':
            fail('assembly-section-authority','全虚构材料仅有scenario-authority；无未知项也不构成业务批准、接受或签署。')
        for missing in attrs.get('evidence_gaps',[]) if isinstance(attrs.get('evidence_gaps'),list) else []:
            fail('assembly-section-evidence-gap','章节必要证据未提供：'+str(missing))
        if model is not None:
            for field,collection,code in [('model_refs','entities','assembly-section-model-ref'),('analysis_refs','analyses','assembly-section-analysis-ref')]:
                known={obj['id'] for obj in model.get(collection,[])}
                for identity in attrs.get(field,[]) if isinstance(attrs.get(field),list) else []:
                    if not isinstance(identity,str) or identity not in known or identity==entity.get('id'):
                        fail(code,'章节支撑不存在或自我引用：'+str(identity))
            if 'relationship_refs' in attrs:
                refs=attrs['relationship_refs']
                if not isinstance(refs,list) or not all(isinstance(x,str) and x.strip() for x in refs):
                    fail('assembly-section-support','relationship_refs必须是关系ID数组。')
                else:
                    relations={r['id']:r for r in model.get('relationships',[])}
                    selected=attrs.get('model_refs',[])
                    selected={x for x in selected if isinstance(x,str)} if isinstance(selected,list) else set()
                    for rid in refs:
                        if rid not in relations or not {relations[rid].get('source'),relations[rid].get('target')}<=selected:
                            fail('assembly-section-relationship-ref','章节关系不存在或未显式选择两端：'+rid)
    return errors
