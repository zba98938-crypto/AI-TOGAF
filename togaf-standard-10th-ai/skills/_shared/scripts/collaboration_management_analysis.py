"""Evidence-bounded G184/G188 operational reviews, without invented scores.

These checks are project contracts derived from guide purposes. They do not
claim full PRINCE2/PMBOK implementation, causal influence, or formal approval.
"""
from datetime import date
from evidence_analysis import require, unique, evidence, sources, number

def present(value):return value not in [None,'',[],{}]
def need_fields(record,fields,gaps):
    for field in fields:
        if not present(record.get(field)):gaps.append({'id':record['id']+':'+field,'field':field,'reason':'missing-input','action':'由责任人补充来源与值；不把未知填为通过或零'})
def checked_refs(refs,known,ident,gaps):
    if not refs:gaps.append({'id':ident+':evidence','reason':'missing-evidence','action':'补充事实或项目规则证据'})
    else:evidence(refs,known,'CM-EVIDENCE',ident)
def iso(value,ident):
    require(isinstance(value,str),'CM-DATE',ident,'ISO date required')
    try:return date.fromisoformat(value)
    except ValueError:raise ValueError('CM-DATE ['+ident+']: invalid ISO date')

def point_of_view_review(data):
    known=sources(data,'POV-001','point-of-view');points=unique(data.get('points',[]),'POV-001','points');rows=[];gaps=[]
    require(points,'POV-001','points','At least one explicit point-of-view document required')
    for p in points.values():
        ident=p['id'];local=[]
        need_fields(p,['charter_alignment','ecosystem_change','decision_question','position','rationale','alternatives','recommendation','adoption_timing','cost_risk_tradeoff','audience_ids','document_version','follow_up'],local)
        checked_refs(p.get('evidence'),known,ident,local)
        for option in unique(p.get('alternatives',[]),'POV-002',ident+':alternatives').values():
            require(isinstance(option,dict) and option.get('id'),'POV-002',ident,'Alternatives need stable IDs')
            need_fields(option,['description','impact','tradeoff'],local)
        events=unique(p.get('reading_events',[]),'POV-003',ident+':reading');readers=set();current_readers=set();stale=[]
        for event in events.values():
            need_fields(event,['reader_id','document_version','observed_at'],local)
            checked_refs(event.get('evidence'),known,event['id'],local)
            if event.get('observed_at'):iso(event['observed_at'],event['id'])
            if event.get('reader_id') and event.get('evidence'):readers.add(event['reader_id'])
            if event.get('document_version')!=p.get('document_version'):stale.append(event['id'])
            elif event.get('reader_id') and event.get('evidence'):current_readers.add(event['reader_id'])
        changes=unique(p.get('initiated_changes',[]),'POV-004',ident+':changes');associations=[]
        for change in changes.values():
            need_fields(change,['initiator_id','description'],local);checked_refs(change.get('evidence'),known,change['id'],local)
            if change.get('reading_event_id'):
                require(change['reading_event_id'] in events,'POV-004',change['id'],'Change links unknown reading event')
                event=events[change['reading_event_id']]
                require(change.get('initiator_id')==event.get('reader_id'),'POV-004',change['id'],'Change initiator differs from linked reader')
                associations.append({'change_id':change['id'],'reader_id':event.get('reader_id'),'reading_event_id':event['id'],'meaning':'observed-sequence-and-stakeholder-association; no causal inference'})
            require(not change.get('claims_causation'),'POV-005',change['id'],'Reading and subsequent change do not establish causation; record attribution as an evidenced statement instead')
        if not events:local.append({'id':ident+':reading-observation','reason':'no-reading-observation','action':'未观察到阅读，不将已分发计作已阅读；继续收集授权范围内的反馈'})
        elif not current_readers:local.append({'id':ident+':current-version-feedback','reason':'no-current-version-reading-observation','action':'历史阅读保留到旧版本，新版反馈待收集；不继承已阅读状态'})
        rows.append({'id':ident,'review_state':'needs-input' if local else 'document-and-observations-reviewable','unique_observed_readers':len(readers),'reader_ids':sorted(readers),'current_version_reader_ids':sorted(current_readers),'stale_version_reading_event_ids':stale,'change_associations':associations,'recommended_action':p.get('recommendation'),'gaps':local})
        gaps+=local
    return {'rows':rows,'gaps':gaps,'notice':'观点是面向变革决策的有理由主张及经营反馈，不是viewpoint规范库；阅读记录说明兴趣，不证明采纳、变革成效或因果贡献。'}

STRATEGY_FIELDS={
 'risk':['identification_classification','analysis_method','response_design','monitoring','risk_log_ref','project_vs_architecture_risk'],
 'quality':['quality_characteristics','documentation','assurance_process','organization_qms_alignment','acceptance_authority'],
 'stakeholder-communication':['stakeholder_map_ref','concerns','engagement_deliverables','audience','frequency','format','communication_plan_ref'],
 'project-controls':['reporting_levels','stage_boundaries','issue_change_capture','exception_path','delegated_tolerances','delegation_monitoring'],
 'configuration':['baseline_identification','change_approval','unapproved_change_rule','configuration_records_ref']}

def management_strategy_review(data):
    known=sources(data,'PMS-001','management-strategy');ident=data.get('id','management-strategy');gaps=[]
    need_fields({**data,'id':ident},['project_scope','selected_method','method_tailoring','project_governance','architecture_governance','confirmation_state'],gaps)
    checked_refs(data.get('evidence'),known,ident,gaps)
    topics=unique(data.get('topics',[]),'PMS-001','topics');bykind={};rows=[]
    for row in topics.values():
        kind=row.get('topic');require(kind in STRATEGY_FIELDS,'PMS-002',row['id'],'Unknown management strategy topic')
        require(kind not in bykind,'PMS-002',row['id'],'Duplicate topic; merge explicitly or define scope');bykind[kind]=row
        local=[];need_fields(row,STRATEGY_FIELDS[kind]+['owner'],local);checked_refs(row.get('evidence'),known,row['id'],local)
        if kind=='project-controls':
            for tolerance in unique(row.get('delegated_tolerances',[]),'PMS-003',row['id']+':tolerances').values():
                require(isinstance(tolerance,dict) and tolerance.get('id'),'PMS-003',row['id'],'Tolerance must be an explicit rule with stable ID')
                need_fields(tolerance,['metric','unit','operator','authority'],local)
                if tolerance.get('value') is None:local.append({'id':tolerance['id']+':value','reason':'tolerance-unknown','action':'负责人确认容差；不默认无限或零'})
                else:number(tolerance['value'],'PMS-003',tolerance['id'])
                checked_refs(tolerance.get('evidence'),known,tolerance['id'],local)
                require(tolerance.get('operator') in ['>','>=','<','<=','==',None],'PMS-003',tolerance['id'],'Unsupported explicit operator')
        if kind=='configuration':
            require(row.get('unapproved_change_rule')!='include-in-baseline','PMS-004',row['id'],'Unapproved changes cannot be incorporated into approved baseline')
        rows.append({'topic':kind,'id':row['id'],'state':'needs-input' if local else 'documented-awaiting-governance-confirmation','gaps':local});gaps+=local
    for kind in STRATEGY_FIELDS:
        if kind not in bykind:gaps.append({'id':ident+':'+kind,'reason':'missing-management-topic','action':'补齐主题或明确项目适用性与裁剪依据'})
    if data.get('confirmation_state')=='confirmed':checked_refs(data.get('confirmation_evidence'),known,ident+':confirmation',gaps)
    return {'strategy_id':ident,'topic_reviews':rows,'gaps':gaps,'state':'needs-input' if gaps else 'ready-for-governance-review','notice':'四个核心管理方面见G188§3.1.8；配置管理见§4.2.1。字段完备不代表批准；容差、频率与工具均来自项目规则，不是TOGAF默认值。'}

def highlight_report_review(data):
    known=sources(data,'HL-001','highlight');ident=data.get('id','highlight');gaps=[]
    need_fields({**data,'id':ident},['period','next_period','audience','communication_plan_ref','approved_plan_ref','previous_planned_task_ids','next_period_activities','risks_issues','corrective_actions','remaining_stage_forecast','remaining_project_forecast','decisions_required'],gaps)
    period=data.get('period',{});nextp=data.get('next_period',{})
    if period:
        require(iso(period.get('start'),ident)<=iso(period.get('end'),ident),'HL-002',ident,'Reporting period is inverted')
    if nextp:
        require(iso(nextp.get('start'),ident)<=iso(nextp.get('end'),ident),'HL-002',ident,'Next reporting period is inverted')
        if period:require(iso(nextp['start'],ident)>iso(period['end'],ident),'HL-002',ident,'Next period overlaps current report')
    checked_refs(data.get('evidence'),known,ident,gaps)
    tasks=unique(data.get('tasks',[]),'HL-003','tasks');rows=[]
    for tid in data.get('previous_planned_task_ids',[]):
        if tid not in tasks:gaps.append({'id':ident+':carry-forward:'+tid,'reason':'prior-planned-task-unreported','action':'按同一任务ID报告完成、继续、取消或变更状态与原因'})
    rule=data.get('schedule_tolerance');limit=None
    if rule:
        require(rule.get('unit')=='calendar-day' and rule.get('operator') in ['>','>='],'HL-004',ident,'Schedule rule requires calendar-day and > or >=')
        limit=number(rule.get('value'),'HL-004',ident,0);checked_refs(rule.get('evidence'),known,ident+':tolerance',gaps)
    else:gaps.append({'id':ident+':schedule-tolerance','reason':'missing-delegated-tolerance','action':'可报告日期差，无法自动判定是否超出项目经理权限'})
    for task in tasks.values():
        local=[];need_fields(task,['name','state','planned_finish','forecast_finish','owner'],local);checked_refs(task.get('evidence'),known,task['id'],local)
        require(task.get('state') in ['not-started','in-progress','submitted','accepted','cancelled',None],'HL-003',task['id'],'Unknown task state')
        accepted=task.get('state')=='accepted'
        if accepted:checked_refs(task.get('acceptance_evidence'),known,task['id']+':acceptance',local)
        delay=None
        if task.get('planned_finish') and task.get('forecast_finish'):delay=(iso(task['forecast_finish'],task['id'])-iso(task['planned_finish'],task['id'])).days
        escalation=None if delay is None or limit is None or not rule.get('evidence') else (delay>limit if rule['operator']=='>' else delay>=limit)
        rows.append({'id':task['id'],'state':task.get('state'),'completion_supported':bool(accepted and task.get('acceptance_evidence')),'forecast_variance_calendar_days':delay,'schedule_exception':escalation,'gaps':local});gaps+=local
    changes=unique(data.get('changes',[]),'HL-005','changes')
    for change in changes.values():
        require(change.get('status') in ['approved','pending','rejected'],'HL-005',change['id'],'Change approval state required')
        checked_refs(change.get('evidence'),known,change['id'],gaps)
        if change['status']=='approved':checked_refs(change.get('approval_evidence'),known,change['id']+':approval',gaps)
        if change.get('incorporated_into_approved_baseline'):
            require(change['status']=='approved' and change.get('approval_evidence'),'HL-005',change['id'],'Unapproved change incorporated into baseline')
            evidence(change['approval_evidence'],known,'HL-005',change['id'])
    return {'report_id':ident,'period':period,'task_reviews':rows,'schedule_exception_task_ids':[r['id'] for r in rows if r['schedule_exception'] is True],'approved_change_ids':[c['id'] for c in changes.values() if c['status']=='approved' and c.get('approval_evidence')],'pending_change_ids':[c['id'] for c in changes.values() if c['status']=='pending'],'gaps':gaps,'state':'needs-input' if gaps else 'reviewable-report','notice':'状态要点按报告期汇总实际、下一期计划、风险问题、纠偏和预测；预期完成不等于已验收。例外报告是另一个治理动作，本审查只标识显式项目容差越界。'}
