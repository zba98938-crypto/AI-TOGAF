"""A substantive cold-chain design case, independent of profile example facts."""
import copy
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/'examples/independent-adm-delivery'
CTX={'domains':['business','data','application','technology'],'landscape':'segment','purpose':'project','abstraction':'logical','evolution':'target'}
STATES=['lg-now','lg-transition-1','lg-transition-2','lg-target']

def materials():
    spec=importlib.util.spec_from_file_location('lingang_chapters',CASE/'chapter_materials.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def specifications():
    return {
    'driver':('driver','温控断链投诉上升',{'statement':'改约缺少贯穿温控的预约身份，投诉原因需分别调查','owner':'运营','metric':'可解释的改约记录比例','target':'模拟20个预约完整可追溯'}),
    'goal':('goal','改约窗口内保持可追溯温控',{'statement':'每次接受或拒绝可还原温区和时标依据','owner':'运营','metric':'证据完整率','target':'模拟20/20；生产未知'}),
    'req':('requirement','改约须写回温控记录',{'statement':'保存预约ID、版本、温区、采集与接收时间；重复不得二次生效','owner':'履约','priority':'must','acceptance':'20个模拟预约逐项核对；温区边界2/8度，时差60秒，重复不新增生效版本'}),
    'stakeholder':('stakeholder','冷链运营负责人',{'concern':'改约、超温和承运责任能否还原','influence':'模拟业务裁决角色','impact':'错误生效影响仓位和交接','engagement':'每班异常复核','owner':'运营'}),
    'capability':('capability','预约改约能力',{'definition':'协调预约版本、温控依据和异常责任','level':2,'category':'履约','operating_mode':'客服手改；温控按车辆分离记录'}),
    'process':('business_process','改约编排',{'definition':'客服提出改单、运营裁决、仓库确认交接','trigger':'客户变更时间窗','outcome':'接受或拒绝有证据','operating_mode':'覆盖原时间窗，异常靠电话确认'}),
    'app':('application','预约编排服务',{'definition':'维护预约状态，不控制制冷机','owner':'平台','boundary':'预约接受/拒绝','responsibility':'版本化决策、收件箱及对账','version':'baseline-v1','lifecycle':'既有服务','event_mode':'最后一次写入覆盖旧版本'}),
    'data':('data_entity','预约温控记录',{'definition':'预约版本、货批、温区及采集和接收时标','owner':'运营数据责任人','classification':'内部履约数据','purpose':'关联改约与温控证据','identity_rule':'车辆号与接收日；没有预约版本'}),
    'tech':('technology','温控网关',{'definition':'采集与缓存温控观察，不接受预约控制冷机','owner':'采集运维','standard':'HTTPS事件；双时标','version':'既有，版本待盘点','lifecycle':'复用候选','responsibility':'独立采集、离线缓存、重新投递','retention':'覆盖式缓存，无消费偏移'}),
    'gap':('gap','改约未写回温控',{'description':'预约版本未贯穿温控观察，迟到可能覆盖新时间窗','owner':'架构负责人','resolution':'契约、收件箱及回放'}),
    'wp':('work_package','改约写回改造WP-2',{'definition':'影子收件箱、回放和对账','owner':'平台组','scope':'单仓20个模拟预约及影子验证','duration_days':15,'depends_on':['lg-wp1']}),
    'wp1':('work_package','WP-1预约与时标契约',{'owner':'运营与数据责任人','scope':'稳定预约版本、货批温区和双时标','duration_days':10,'depends_on':[]}),
    'wp3':('work_package','WP-3单仓受控切换',{'owner':'仓库负责人','scope':'门禁复核后申请单仓切换，保留人工回退','duration_days':10,'depends_on':['lg-wp']}),
    'transition':('transition','过渡一双写温控',{'definition':'人工系统权威，候选服务只做影子对账','operations':'禁止生产写入','data_consistency':'按预约版本逐条对账','rollback':'停消费者、冻结、核对偏移、回到人工'}),
    'abb':('abb','预约编排ABB',{'definition':'独立于产品的预约版本与温控证据协调能力','responsibility':'唯一生效、温区校验和异常接管','boundary':'不控制制冷机','interfaces':['改约请求','温控事件','决策查询'],'quality':'重放幂等、原时标不可覆盖','abstraction':'logical','owner':'架构负责人'}),
    'sbb':('sbb','改约写回组件',{'definition':'候选版本收件箱及校验器','implementation':'事件适配器和回放记录，未采购','responsibility':'实现预约版本幂等与双时标','lifecycle':'candidate；not-started'}),
    'interface':('interface','预约温控事件契约',{'protocol':'HTTPS事件投递','payload':'预约ID、版本、货批、温区、采集时标、接收时标','version':'1','idempotency':'预约ID+版本+事件键'}),
    'organization':('organization','单仓运营与平台协作组',{'boundary':'改约与交接证据，不含设备控制','owner':'候选仓库负责人','category':'模拟跨团队协作'}),
    'role':('role','温控异常裁决角色',{'responsibility':'裁决超温、时差和预约冲突','authority':'scenario-authority；无真实任命','skill':'时标、货批规则、异常回放'}),
    'actor':('actor','模拟客服与仓库操作员',{'boundary':'提出改约；不可改变货批温区','owner':'模拟运营'}),
    'constraint':('constraint','制冷控制范围禁入',{'rationale':'业务改约不能下发设备指令','category':'硬边界','owner':'运营与设备责任人','source':'模拟项目边界'}),
    'principle':('principle','原始温控证据不可覆盖',{'statement':'采集和接收时标分别保留，版本化裁决','rationale':'迟到与重试不能改写业务历史','implications':'更多存储及人工冲突处理','owner':'运营数据责任人'}),
    'standard':('standard','温控事件双时标约定',{'category':'项目事件约定','version':'scenario-v1','disposition':'candidate','rationale':'区分传感时间与网络延迟','exception_process':'运营和安全联合评审'}),
    'risk':('risk','乱序与超温记录误归属',{'impact':'旧观察可能被错误归到新预约','likelihood':'情景序数3，非概率','owner':'运营风险角色','treatment':'版本隔离、阈值拒绝、人工裁决','residual_risk':'生产未知，模拟不证明控制有效'}),
    'control':('control','版本幂等及异常隔离',{'purpose':'禁止重复生效和不可信温控自动使用','owner':'平台与运营','classification':'预防与恢复','effectiveness':'软件模拟可检查，生产未知'}),
    'change':('change_request','CR-01收紧时差容差',{'reason':'容差由60秒改30秒并保留拒绝原因','impact':'数据、网关、异常流程、回放与WP-2；温区和制冷控制不变','owner':'模拟运营','decision':'仅候选分析'}),
    'decision':('decision_record','事件适配候选决策',{'decision':'保留现有预约和网关，增加适配层','rationale':'减少设备运行扰动；报价未知','owner':'模拟架构角色'}),
    'project':('project','单仓改约证据架构研究',{'scope':'预约、温控写回与交接；排除设备控制','authorization':'scenario-authority，非真实预算或上线授权'}),
    'contract':('contract','预约温控交换候选条款',{'owner':'真实缔约方未知','target':'版本与时标可追溯','unit':'逐预约','measurement_window':'模拟20例','signature':'未签署'}),
    'benefit':('benefit','减少改约裁决等待的候选收益',{'owner':'运营','metric':'裁决前置时间','target':'模拟60降到35分钟；生产未观察','attribution':'减少证据查找，不证明制冷效果'}),
    'objective':('objective','20个预约完整回放',{'owner':'平台与运营','metric':'证据完整预约数','target':20,'deadline':'候选影子评审前'}),
    'measure':('measure','预约证据完整与裁决等待',{'owner':'运营','metric':'可追溯记录数及裁决分钟','target':'模拟20/20，35分钟','unit':'record；minute分列','measurement_window':'模拟20预约'}),
    'migration':('migration_step','影子至单仓受控写入',{'transformation':'先只读对账，后单仓版本提交','reconciliation':'逐预约版本核对，重复或漏写即停','rollback':'停消费者、冻结、核偏移、人工处理'}),
    'milestone':('milestone','单仓退出候选门禁',{'criterion':'边界、乱序、重复及断网重放通过后才提请评审','status':'仅模拟；非生产批准','owner':'模拟运营'}),
    'repository':('repository_asset','冷链模型与回放资产索引',{'versioning':'原始材料、模型、回执和输入哈希分别保留','owner':'模拟架构管理员','definition':'保存契约、四态模型与决策依据'}),
    'value_stream':('value_stream','取得可信改约决定',{'trigger':'客户变更时间窗','stakeholder':'客户与履约方','value':'得到有温控依据且可还原的改约决定'}),
    'value_stage':('value_stage','确认温控证据可用',{'entry':'预约版本和货批身份明确','exit':'时标可信且温区规则明确，可进入裁决','value':'避免基于旧观察接受新改约','enabling_capability':'预约改约能力'})}

VERSION_DELTAS={
'capability':[{'operating_mode':'影子预约按版本回放，人工权威不变'},{'operating_mode':'单仓版本化改约，异常由运营接管'},{'operating_mode':'预约与交接证据贯通，设备控制独立'}],
'process':[{'operating_mode':'影子异常队列，人工对照原始时标'},{'operating_mode':'客服提案、系统校验、运营裁决、仓库交接'},{'operating_mode':'跨班异常交接可回放并持续复核'}],
'data':[{'identity_rule':'预约ID+版本；原温区和双时标保留'},{'identity_rule':'货批温区版本与预约版本关联，冲突隔离'},{'identity_rule':'预约、货批、交接和温控完整事件血缘'}],
'app':[{'event_mode':'影子收件箱去重，只读对账','version':'scenario-v2'},{'event_mode':'单仓唯一版本提交，迟到隔离','version':'scenario-v3'},{'event_mode':'可回放决策和跨班异常交接','version':'scenario-v4'}],
'tech':[{'retention':'离线缓冲+消费偏移，保留原采集时标'},{'retention':'单仓校验时差并隔离不可信事件'},{'retention':'审计索引与容量保留期仍待实测'}],
'req':[{'acceptance':'20例影子验证幂等、边界温区和60秒时差；无生产执行'},{'acceptance':'单仓切换须无漏写、重复生效，异常有接管人'},{'acceptance':'端到端预约及交接可回放；运营批准独立'}]}

def build_case():
    mat=materials();specs=specifications();model={'schema_version':'2.0','project':{'id':'lingang-cold-chain','name':'全虚构临港冷链预约改约','version':'design-acceptance-2','context':CTX,'is_example':True,'approval_status':'candidate','implementation_status':'not-started'},
    'sources':[{'id':'lg-brief','kind':'example','description':'独立手写冷链场景，所有数值为模拟假设，非现场观察。','locator':'examples/independent-adm-delivery/chapter_materials.py'}],
    'entities':[],'relationships':[],'views':[],'deliverables':[],'analyses':[],'gaps':[],
    'extensions':{'entity_types':{'project:section_evidence':'项目章节候选证据，不是官方类型'},'relationship_types':{}}}
    versions={};ids={}
    for key,(typ,name,attrs) in specs.items():
        extra={
        'interface':{'producer':'温控网关','consumer':'预约编排收件箱'},
        'abb':{'service':'预约身份、温区校验、异常隔离','requirements':['版本幂等','双时标追溯'],'realization':'候选版本收件箱SBB；未实施'},
        'transition':{'operating_conditions':{'operations':'人工权威与影子只读','data_consistency':'逐版本对账','dependencies':'契约先行','controls':'重复或漏写即停','rollback':'冻结、核偏移、人工接管'}},
        'capability':{'score':'unknown：无现场成熟度量尺与观察'},
        'constraint':{'expiry':'范围变更须另行请求和真实授权'},
        'goal':{'perspective':'内部运营','definition':'可还原改约依据，独立于制冷效果','deadline':'模拟评审前；实际日期未知'},
        'driver':{'deadline':'候选单仓试点评审前，未承诺'},
        'objective':{'statement':'20个模拟预约均能回放版本与原始时标'},
        'stakeholder':{'quadrant':'unknown：未进行真实访谈与量化'},
        'risk':{'asset':'预约决策与温控观察','threat':'跨日迟到及重试','vulnerability':'未绑定预约版本、覆盖采集时标'},
        'change':{'severity':'追溯可信度与人工负担；模拟高优先级'},
        'app':{'criticality':'履约关键；未量化','cost':'unknown：无真实报价'},
        'tech':{'product':'既有网关，厂商未核实','support_end':'unknown：待采购和设备台账核实'}}
        attrs={**attrs,**extra.get(key,{})}
        identity='lg-'+key;ids[key]=identity;versions[key]=[]
        deltas=VERSION_DELTAS.get(key,[]);a=copy.deepcopy(attrs)
        for i in range(4 if deltas else 1):
            if i:a.update(deltas[i-1])
            eid=identity if i==0 else identity+'-v'+str(i+1)
            state=STATES[i] if deltas else STATES[-1]
            model['entities'].append({'id':eid,'concept_id':identity,'version':str(i+1),'type':typ,'name':name,'attributes':copy.deepcopy(a),'state_id':state,'evolution':['baseline','transition','transition','target'][i] if deltas else 'target','scope_id':'lg-fulfillment','evidence':['lg-brief'],'certainty':'assumed','approval_status':'candidate','implementation_status':'not-started'})
            versions[key].append(eid)
    model['states']=[{'id':sid,'name':name,'evolution':evo,'scope_id':'lg-fulfillment',**({'operating_conditions':{'operations':'人工权威，影子只读' if i==1 else '单仓版本化写入','data_consistency':'逐预约版本对账','dependencies':'WP-1契约→WP-2回放→WP-3受控切换','controls':'无漏写/重复生效才提请评审','rollback':'停消费者、冻结、核偏移、恢复人工'}} if evo=='transition' else {})} for i,(sid,name,evo) in enumerate(zip(STATES,['基线手改','过渡一影子对账','过渡二单仓写入','目标证据贯通'],['baseline','transition','transition','target']))]
    links=[('motivation','driver','req','motivates','投诉驱动温控写回需求'),('req-goal','req','goal','supports','追溯需求支撑履约目标'),('cap-proc','capability','process','realized_by','改约能力由职责分离过程实现'),('proc-app','process','app','supported_by','编排过程由预约服务支持'),('app-data','app','data','writes','编排写入版本化双时标记录'),('app-tech','app','tech','runs_on','编排依赖独立采集和传输平台'),('gap-req','gap','req','violates','基线缺口不能满足追溯需求'),('wp-gap','wp','gap','resolves','WP-2处理写回与回放缺口'),('tr-wp','transition','wp','includes','过渡包含影子回放工作包'),('sbb-abb','sbb','abb','realizes','收件箱实现编排逻辑契约'),('abb-req','abb','req','satisfies','编排契约满足预约追溯'),('change-req','change','req','changes','CR-01改变时差校验与验收'),('control-risk','control','risk','mitigates','隔离与幂等针对误归属'),('wp-wp1','wp','wp1','depends_on','回放依赖身份契约'),('wp3-wp','wp3','wp','depends_on','切换依赖影子门禁'),('wp-benefit','wp','benefit','contributes_to','回放减少查证等待但非已实现收益'),('interface-app','interface','app','delivers','事件输入编排收件箱'),('role-process','role','process','owns','运营裁决超温与冲突')]
    for suffix,a,b,typ,label in links:
        rt='lg:'+typ
        model['extensions']['relationship_types'][rt]={'source_types':['*'],'target_types':['*'],'meaning':label+'；模拟设计追溯，不表示批准'}
        model['relationships'].append({'id':'lg-'+suffix,'source':versions[a][-1],'target':versions[b][-1],'type':rt,'label':label,'attributes':{'meaning':label},'evidence':['lg-brief'],'certainty':'assumed'})
    # Independent hand inputs and hand-checkable arithmetic.
    for suffix,times in [('baseline',[20,30,10]),('target',[10,15,10])]:
        model['analyses'].append({'id':'lg-A-flow-'+suffix,'method_id':'lean-serial-flow','evidence':['lg-brief'],'inputs':{'boundary':'单条改约裁决串行流，模拟'+suffix,'aggregation_rule':'serial-conditional-first-pass','rule_evidence':['lg-brief'],'steps':[{'id':'lg-step-'+str(i),'lead_time':{'value':t,'unit':'minute'},'process_time':{'value':5,'unit':'minute'},'complete_accurate_percent':99,'evidence':['lg-brief']} for i,t in enumerate(times)]}})
    model['analyses'] += [{'id':'lg-A-options','method_id':'weighted-normalized-decision','evidence':['lg-brief'],'inputs':{'rule_evidence':['lg-brief'],'criteria':[{'id':'recoverability','direction':'maximize','weight':.6,'min':1,'max':5},{'id':'disruption','direction':'minimize','weight':.4,'min':1,'max':5}],'options':[{'id':'adapter','scores':{'recoverability':4,'disruption':2}},{'id':'replace-all','scores':{'recoverability':5,'disruption':5}}]}}, {'id':'lg-A-risk','method_id':'risk-explicit-rule','evidence':['lg-brief'],'inputs':{'formula':'likelihood-times-impact','rule_evidence':['lg-brief'],'likelihood':{'value':3,'scale':'模拟1至5序数','evidence':['lg-brief']},'impact':{'value':4,'scale':'模拟1至5序数','evidence':['lg-brief']}}}]
    rules=json.loads((ROOT/'capability-addenda/deliverable-assembly-rules.json').read_text());cap=json.loads((ROOT/'capabilities.json').read_text());profiles={p['id']:p for p in cap['profiles']};byid={e['id']:e for e in model['entities']}
    families={f for d in rules['deliverables'] for s in d['sections']+d.get('core_requirements',[]) for f in s.get('artifact_ids',[])}
    needed={p for d in rules['deliverables'] for s in d['sections'] for p in s.get('profile_ids',[])}
    needed.update(p['id'] for p in cap['profiles'] if p['id'].startswith('compat-') and p['artifact_id'] in families)
    # These alternative views require different questions/evidence (four BSC
    # perspectives, resource instances, customer journey or three MDM options).
    # This case selects its actual capability and version views instead.
    needed-={'balanced-scorecard-default','capability-increment-analysis-default','capability-instance-composition','customer-journey-default','mdm-consolidation-collaboration-central'}
    for pid in sorted(needed):
        p=profiles[pid];selected=[versions[k][-1] for k in specs if specs[k][0] in p.get('entity_types',[])]
        if not selected:continue
        rs=[r['id'] for r in model['relationships'] if {r['source'],r['target']}<=set(selected)]
        model['views'].append({'id':'lgv-'+pid,'artifact_id':p['artifact_id'],'profile_id':pid,'title':'临港／'+p['name'],'context':CTX,'scope_id':'lg-fulfillment','state_ids':STATES,'allow_mixed_evolution':True,'entity_ids':selected,'relationship_ids':rs,'analysis':'仅选取冷链手写对象；不混入内置profile事实。','legend':'虚构设计；生产验证与业务接受独立。'})
    # Four state domain views use their actual different versions.
    for key,family in [('capability','business-capability-map'),('data','conceptual-data-diagram'),('app','application-communication-diagram'),('tech','platform-decomposition-diagram')]:
        pid='compat-'+family
        for i,state in enumerate(STATES):
            model['views'].append({'id':'lg-state-'+key+'-'+str(i),'artifact_id':family,'profile_id':pid,'title':'临港四态／'+key+'/'+state,'context':{**CTX,'evolution':['baseline','transition','transition','target'][i]},'scope_id':'lg-fulfillment','state_ids':[state],'entity_ids':[versions[key][i]],'relationship_ids':[],'analysis':str(byid[versions[key][i]]['attributes']),'legend':'同一概念，不同命名状态与版本。'})
    for rule in rules['deliverables']:
        did=rule['id'];texts=mat.CHAPTER_TEXT[did];assert len(texts)==len(rule['sections']),did
        keys,analysis=mat.SUPPORT[did];refs=[versions[k][-1] for k in keys.split()]
        d={'id':'lg-d-'+did,'deliverable_id':did,'title':'临港／'+did,'entity_ids':[],'view_ids':[],'sections':{},'approval_status':'candidate','implementation_status':'not-started','assembly':{'mode':'draft','rules_version':rules['rules_version'],'scope_id':'lg-fulfillment','state_ids':STATES,'section_bindings':{}}}
        for i,(section,text) in enumerate(zip(rule['sections'],texts)):
            title=section['title'];eid='lg-ch-'+did+'-'+str(i)
            # A baseline argument must cite baseline objects, rather than merely
            # binding the latest versions to make chapter coverage green.
            chapter_refs=list(refs);chapter_analysis=analysis
            versioned=[k for k in keys.split() if len(versions[k])==4]
            if '基线' in title and '目标' not in title:
                chapter_refs=[versions[k][0] if k in versioned else versions[k][-1] for k in keys.split()]
                if analysis=='flow-target':chapter_analysis='flow-baseline'
            elif '过渡' in title or '现状' in title or ('基线' in title and '目标' in title):
                chapter_refs=list(dict.fromkeys(refs+[v for k in versioned for v in versions[k]]))
            tradeoff,criterion=mat.REVIEW[did]
            record={'id':eid,'type':'project:section_evidence','name':title+'／冷链论证','evidence':['lg-brief'],'certainty':'assumed','state_id':STATES[-1],'scope_id':'lg-fulfillment','attributes':{'record_contract':'scenario-section/2','authority':'scenario-authority','status':'scenario-proposal','deliverable_id':did,'section_title':title,'question':did+'／'+title+'：如何处理冷链预约版本、温控依据与责任？','conclusion':text,'decision':text,'scope':'单仓预约改约与温控交接','owner':'模拟运营及架构负责人','acceptance':'逐项复核本章主张与所引用对象，检查20例边界、乱序、重复和断网回放；现场测温及生产接受另行提供。','tradeoffs':['保留人工权威及设备独立控制增加对账和异常处理成本，但使'+title+'的候选判断可撤销。'],'model_refs':refs,'analysis_refs':['lg-A-'+analysis],'relationship_refs':[r['id'] for r in model['relationships'] if {r['source'],r['target']}<=set(refs)],'unknowns':['现场网关时钟、人员排班、真实报价及批准尚未取得'],'evidence_gaps':[]}}
            record['attributes'].update(model_refs=chapter_refs,analysis_refs=['lg-A-'+chapter_analysis],
                acceptance=criterion+' 本章逐项判据：'+text+' 现场与生产接受须另行取证。',tradeoffs=[tradeoff],
                relationship_refs=[r['id'] for r in model['relationships'] if {r['source'],r['target']}<=set(chapter_refs)])
            model['entities'].append(record);d['sections'][title]=text
            vs=[v['id'] for v in model['views'] if (v['profile_id'] in section.get('profile_ids',[]) if section.get('profile_ids') else v['artifact_id'] in section.get('artifact_ids',[]))]
            if did=='architecture-definition-document':
                vs+= [v['id'] for v in model['views'] if v['id'].startswith('lg-state-') and set(v['entity_ids'])<=set(chapter_refs)]
            d['assembly']['section_bindings'][title]={'entity_ids':[eid],'view_ids':vs};d['view_ids']+=vs
            if did=='architecture-definition-document' and any(v.startswith('lg-state-') for v in vs):
                d['assembly']['section_bindings'][title]['override']={
                    'reason':'本章以冷链单仓业务、数据、应用和技术四态回答“'+title+'”；不采用BI或MDM专题代替企业四域状态。所列状态与章节对象引用一致，保留原有适用专题视图作为补充。',
                    'owner':'模拟架构负责人；scenario-authority，无真实批准权',
                    'evidence':['lg-brief']}
        for req in rule.get('core_requirements',[]):
            v=next((v for v in model['views'] if v['artifact_id'] in req.get('artifact_ids',[]) or v['profile_id'] in req.get('profile_ids',[])),None)
            if v:d['view_ids'].append(v['id'])
        d['view_ids']=list(dict.fromkeys(d['view_ids']));model['deliverables'].append(d)
    model['scopes']=[{'id':'lg-fulfillment','description':'单仓预约改约与温控证据；不含制冷机控制','included_ids':[e['id'] for e in model['entities']]}]
    return model,{'versions':versions,'selected_ids':ids,'domain_keys':['capability','process','data','app','tech'],'external_evidence':['现场传感器校准与时钟实测','真实网络隔离和故障恢复回执','运营、承运及安全角色批准','真实排班、报价及采购信息']}
