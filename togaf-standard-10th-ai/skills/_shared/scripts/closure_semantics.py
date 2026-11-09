"""Opt-in executable enterprise contracts. Project conventions, not TOGAF clauses."""
from datetime import date
import math

def check(model):
    contract=model.get('extension_data',{}).get('enterprise:closure')
    if not contract:return []
    issues=[]
    def fail(code,identity,message):issues.append({'level':'error','code':code,'id':identity,'message':message})
    entities={e['id']:e for e in model.get('entities',[])}
    edges=model.get('relationships',[])
    source_index={s['id']:s for s in model.get('sources',[])}
    for group in ('project','entities','relationships','states','views'):
        records=[model['project']] if group=='project' else model.get(group,[])
        for record in records:
            if model['project'].get('is_example') and (record.get('approval_status')=='approved' or record.get('implementation_status')=='realized' or record.get('decision_status') in ('approved','realized')):
                fail('synthetic-authority',record.get('id',group),'合成输入不能被转换成真实批准或实施证据。')
    for record in contract.get('evidence_records',[]):
        identity=record.get('id','evidence')
        for key in ('period_start','period_end','unit','method','owner_id','source_id','classification'):
            if not record.get(key):fail('evidence-required',identity,'缺少 '+key)
        if record.get('classification')!='synthetic':fail('evidence-authority',identity,'独立模拟台账须明确 synthetic，不得升级为真实授权。')
        if record.get('owner_id') not in entities:fail('evidence-owner',identity,'责任主体不存在。')
        if record.get('source_id') not in source_index:fail('evidence-source',identity,'台账来源不存在。')
        try:
            start=date.fromisoformat(record['period_start']);end=date.fromisoformat(record['period_end'])
            asof=date.fromisoformat(contract['as_of'])
            if start>end or end>asof:fail('evidence-period',identity,'观察期间无效或在评估日期之后。')
            if (asof-end).days>record.get('max_age_days',90):fail('evidence-stale',identity,'证据超出适用时效。')
        except (KeyError,TypeError,ValueError):fail('evidence-period',identity,'观察期间须为合法 ISO 日期。')
        for key in ('value','numerator','denominator','threshold'):
            value=record.get(key)
            if value is not None and (not isinstance(value,(int,float)) or isinstance(value,bool) or not math.isfinite(value)):
                fail('evidence-number',identity,'非有限或非数值 '+key)
        if 'numerator' in record and 'denominator' in record:
            n=record['numerator'];d=record['denominator']
            if not isinstance(n,(int,float)) or not isinstance(d,(int,float)) or d<=0 or n<0 or n>d:
                fail('evidence-denominator',identity,'计数口径无效。')
            elif record.get('unit')=='ratio' and abs(record.get('value',-1)-n/d)>1e-9:
                fail('evidence-calculation',identity,'比例与独立计数不符。')
    rules={}
    for rule in contract.get('rules',[]):
        identity=rule.get('id','rule');key=(rule.get('dimension'),rule.get('period_start'),rule.get('period_end'))
        if key in rules and rules[key].get('threshold')!=rule.get('threshold'):fail('conflicting-rule',identity,'同口径同期间规则冲突。')
        rules[key]=rule
        if rule.get('authority')!='simulation-policy' or rule.get('owner_id') not in entities:
            fail('rule-authority',identity,'规则必须有模拟政策来源和明确责任。')
    for flow in contract.get('flows',[]):
        fid=flow.get('id','flow');nodes=set(flow.get('node_ids',[]));start=flow.get('start_id');terminals=set(flow.get('terminal_ids',[]))
        if not nodes or not terminals<=nodes or start not in nodes or not terminals:
            fail('flow-contract',fid,'流程需包含起点及明确终态。');continue
        if not nodes<=set(entities):fail('flow-reference',fid,'控制节点不存在。');continue
        selected=[e for e in edges if e.get('id') in flow.get('edge_ids',[])]
        if len(selected)!=len(set(flow.get('edge_ids',[]))):fail('flow-reference',fid,'控制边不存在或重复。')
        adjacency={n:[] for n in nodes};reverse={n:[] for n in nodes}
        for e in selected:
            if e['source'] not in nodes or e['target'] not in nodes:fail('flow-endpoint',e['id'],'流程边端点越界。');continue
            adjacency[e['source']].append(e);reverse[e['target']].append(e['source'])
            if e['type'] not in ('flows_to','branches','enterprise:failure_exit','enterprise:compensates'):
                fail('flow-semantic',e['id'],'控制流不能用通用追踪关系替代。')
            if e['type']=='branches':
                guard=e.get('attributes',{}).get('guard',{})
                if not isinstance(guard,dict) or guard.get('operator')!='eq' or not guard.get('field') or 'value' not in guard:
                    fail('branch-guard',e['id'],'分支缺少可判定 eq 守卫。')
        def closure(seed,neighbors):
            seen=set(seed);pending=list(seed)
            while pending:
                for child in neighbors(pending.pop()):
                    if child not in seen:seen.add(child);pending.append(child)
            return seen
        reachable=closure({start},lambda n:[e['target'] for e in adjacency[n]])
        ends=closure(terminals,lambda n:reverse[n])
        for n in nodes:
            attrs=entities[n].get('attributes',{})
            if n not in reachable:fail('flow-unreachable',n,'控制节点不可达。')
            if n not in ends:fail('flow-no-exit',n,'控制节点没有终态退出路径。')
            if n in terminals and adjacency[n]:fail('flow-terminal',n,'终态不得继续流出。')
            if entities[n]['type']=='decision':
                outgoing=adjacency[n];guards=[e.get('attributes',{}).get('guard',{}) for e in outgoing]
                expected=attrs.get('guard_values');field=attrs.get('guard_field')
                actual=[g.get('value') for g in guards]
                if expected is None or not field or len(set(map(str,actual)))!=len(actual) or set(map(str,actual))!=set(map(str,expected)) or any(g.get('field')!=field for g in guards):
                    fail('branch-partition',n,'守卫需互斥、覆盖声明的有限域，字段一致。')
            if len(adjacency[n])>1 and entities[n]['type']!='decision':
                field=attrs.get('outcome_field');values=attrs.get('outcome_values',[])
                guards=[e.get('attributes',{}).get('guard',{}) for e in adjacency[n]]
                if not field or not values or any(g.get('operator')!='eq' or g.get('field')!=field for g in guards) or sorted(map(str,[g.get('value') for g in guards]))!=sorted(map(str,values)):
                    fail('operation-outcomes',n,'多出口操作必须明确成功/失败/补偿的互斥守卫。')
            if attrs.get('writes_state') and not attrs.get('irreversible') and not attrs.get('compensation_id'):
                fail('compensation-missing',n,'可逆写操作缺少补偿控制。')
            if attrs.get('compensation_id'):
                target=attrs['compensation_id']
                if target not in nodes or not any(e['type']=='enterprise:compensates' and e['target']==target for e in adjacency[n]):
                    fail('compensation-link',n,'补偿标识与控制边不一致。')
            if attrs.get('irreversible') and not any(e['type']=='enterprise:failure_exit' for e in adjacency[n]):
                fail('irreversible-exit',n,'不可逆操作须有异常退出及人工对账，不得声称自动回退。')
    stages=contract.get('adm_chain',[])
    required=['concern','requirement','business','data','application','technology','gap','option','work_package','transition','compliance','value_review']
    if [s.get('stage') for s in stages]!=required:fail('adm-chain-stages','closure','完整示范链缺少阶段或次序。')
    for stage in stages:
        for identity in stage.get('entity_ids',[]):
            if identity not in entities:fail('adm-chain-reference',identity,'闭环对象不存在。')
        if not stage.get('entity_ids'):fail('adm-chain-empty',stage.get('stage','stage'),'闭环阶段为空。')
    for a,b in zip(stages,stages[1:]):
        if not any(e['source'] in a['entity_ids'] and e['target'] in b['entity_ids'] and e['type']!='traces_to' for e in edges):
            fail('adm-chain-link',a['stage'],'缺少到下一阶段的明确领域关系。')
    for state in model.get('states',[]):
        if state.get('evolution')=='transition':
            conditions=state.get('operating_conditions',{})
            required=('operations','data_consistency','dependencies','controls','rollback')
            if any(not isinstance(conditions.get(k),str) or not conditions[k].strip() for k in required):
                fail('transition-operability',state['id'],'过渡状态必须明确运营、数据一致性、依赖、控制和回退；不能只用状态名称或实体叙述代替。')
            if conditions.get('order_intake')!='enabled':
                fail('transition-order-intake',state['id'],'模拟双写过渡必须保留订单入口，不能称停机状态为可运营过渡。')
    if contract.get('state_detail_contract'):
        for concept in ('order-fulfillment','order-event','order-hub','event-platform'):
            versions=[e for e in entities.values() if e.get('concept_id')==concept]
            if {e.get('context',{}).get('evolution') for e in versions}!={'baseline','transition','target'}:
                fail('architecture-state-versions',concept,'四域每个概念必须具有三种明确演进状态。')
            summaries=[]
            for e in versions:
                detail=e.get('attributes',{}).get('architecture_detail',{})
                if not detail.get('summary') or detail.get('owner_id') not in entities or detail.get('classification')!='synthetic-design-assumption':
                    fail('architecture-state-detail',e['id'],'状态差异必须有具体机制、责任和合成设计假设分类。')
                summaries.append(detail.get('summary'))
            if len(set(summaries))!=3:fail('architecture-state-difference',concept,'仅复制状态名称不足以证明架构差异。')
        for state in ('baseline','transition','target'):
            data=entities.get('closure-order-event-'+state,{}).get('attributes',{}).get('architecture_detail',{})
            interface=entities.get('closure-interface-'+state,{}).get('attributes',{})
            if interface.get('schema_id')!=data.get('contract') or interface.get('identity')!=data.get('key') or interface.get('delivery_semantics')!=data.get('delivery'):
                fail('architecture-interface-contract',state,'同状态数据契约、键和投递语义必须与接口一致。')
    for recovery in contract.get('recovery_exercises',[]):
        if recovery.get('classification')!='synthetic' or recovery.get('production_proof') is not False:fail('recovery-authority',recovery.get('id','recovery'),'演练仅为模拟，不是生产恢复证明。')
        if recovery.get('restore_point_id') not in entities:fail('recovery-restore-point',recovery.get('id','recovery'),'缺少明确恢复点。')
        if recovery.get('result') not in ('pass','fail') or not recovery.get('observations'):fail('recovery-evidence',recovery.get('id','recovery'),'缺少演练结果/观察。')
    return issues
