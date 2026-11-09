"""Purpose-specific fictional examples; no source diagram is treated as project fact."""
import copy

BMC=['关键伙伴','关键活动','关键资源','价值主张','客户关系','渠道','客户细分','成本结构','收入来源']

def specialize(p, products, base_example):
    from proficiency_contract import specialize as proficiency_example
    result = proficiency_example(p)
    if result is not None:
        return result
    # Keep the explicit comparison topology reproducible, including its contract.
    if p['id'] == 'application-gap-dependency':
        import json
        from pathlib import Path
        source = Path(__file__).resolve().parents[1] / 'capability-addenda/application-gap-profile.json'
        definition = json.loads(source.read_text())['profiles'][0]
        p.update(copy.deepcopy(definition))
        return p['example']
    w=next((w for w in products if w['id']==p['artifact_id']),None)
    original=copy.deepcopy(w['example']) if w else None
    pid=p['id'];aid=p['artifact_id'];renderer=p['renderer']
    def entity(identity,typ,name,**attrs):
        return {'id':pid+'-'+identity,'type':typ,'name':name,'attributes':attrs,'evidence':['example-source'],'certainty':'assumed'}
    es=[];rs=[]
    def E(identity,typ,name,**attrs):
        e=entity(identity,typ,name,**attrs);es.append(e);return e['id']
    def R(identity,typ,a,b,label,**attrs):
        r={'id':pid+'-'+identity,'type':typ,'source':a,'target':b,'label':label,'evidence':['example-source'],'certainty':'assumed'}
        if attrs:r['attributes']=attrs
        rs.append(r);return r
    primary=w['entity_types'][0] if w else {
        'business-capability-map':'capability','business-footprint-diagram':'capability','value-stream-map':'value_stage',
        'value-chain-diagram':'value_chain_activity','information-map':'information','conceptual-data-diagram':'data_entity',
        'logical-data-diagram':'logical_entity','organization-map':'organization','business-model-diagram':'business_model_element',
        'functional-decomposition-diagram':'function','application-migration-diagram':'application'}.get(aid,'information')
    required=p.get('required_attributes',{})
    if isinstance(required,list):
        required={primary:[a for a in required if a not in ['parent','state_id','polarity','loop_type','relationship_kind','operation']]}
    p['required_attributes']=required
    seed=(original or base_example(aid,p['name'],primary,[]))['entities'][0]['attributes']
    def attrs(typ,**overrides):
        data={k:copy.deepcopy(seed.get(k,{'definition':'在线零售订单范围内的明确业务含义','level':1,'category':'核心',
            'strategic_contribution':'缩短履约等待并提高客户通知可靠性','entry_condition':'已取得客户确认的有效订单',
            'exit_condition':'阶段结果已由责任人验证','value_item':'可继续履约的已确认订单',
            'order':1,'scale':'0未建立、1临时、2可重复、3受控、4优化；虚构项目量表','dimension':'履约支持充分性',
            'target':4,'attributes':[{'name':'订单标识','type':'string','key':'PK','optional':False}],
            'key':'订单标识','domain':'已确认、已发运或已取消','detail':'支持客户在承诺时间内收到订单'} .get(k,'本例'+k+'需由业务责任方验证')))
            for k in required.get(typ,[]) if k!='name'}
        data.update(overrides);return data
    if aid=='value-network':
        p['required_attributes']={'value_network_actor':['role','beneficiary']}
        customer=E('customer','value_network_actor','线上客户',role='价值需求与付款方',beneficiary='获得可用商品和可靠交付')
        retailer=E('retailer','value_network_actor','零售商',role='商品组合与履约承诺方',beneficiary='获得商品销售收入')
        carrier=E('carrier','value_network_actor','承运商',role='配送服务方',beneficiary='获得明确配送服务费')
        for n,a,b,value,condition in [('goods',retailer,customer,'商品和可跟踪交付','订单有效且承诺已确认'),('payment',customer,retailer,'商品对价','依已确认销售条款'),('delivery',carrier,retailer,'履行配送服务','受托订单范围内'),('fee',retailer,carrier,'配送服务费','依可验证服务成果结算')]:
            R(n,'exchanges_value',a,b,value,value_item=value,conditions=condition,tangible=True)
        p['structural_requirements']={'minimum_entity_types':{'value_network_actor':3},'relationship_types':['exchanges_value']}
    elif aid=='lean-value-stream':
        p['required_attributes']={'lean_process':['function','lead_time','processing_time','complete_accurate','unit','queue']}
        customer=E('customer','actor','线上客户',definition='提交已确认订单并接收履约状态')
        system=E('system','application','订单应用',definition='向仓库传递受控订单并接收发运结果')
        processes=[]
        for n,name,lt,pt,quality,queue in [('confirm','核对订单',480,10,0.95,12),('pick','拣配商品',960,30,0.98,35),('ship','交接发运',480,15,0.99,8)]:
            processes.append(E(n,'lean_process',name,function='虚构履约团队',lead_time=lt,processing_time=pt,complete_accurate=quality,unit='分钟',queue=queue,working_minutes_per_day=480,metric_evidence='虚构示例，非实测'))
        R('submit','information_flow',customer,system,'确认的购买需求')
        R('schedule','information_flow',system,processes[0],'经校验的订单信息')
        R('result','information_flow',processes[-1],system,'已交接商品及发运标识')
        R('notify','information_flow',system,customer,'可追踪发运状态')
        for i,(a,b) in enumerate(zip(processes,processes[1:])):R('work'+str(i),'work_flow',a,b,'推式工作流；队列记录在下游流程',queue_rule='待处理工作项数，不是人员数')
        p['template']['bands']=['信息流','工作流','时间与质量指标']
        p['structural_requirements']={'minimum_entity_types':{'lean_process':3},'relationship_types':['information_flow','work_flow']}
    elif aid=='four-box-business-model':
        p['required_attributes']={'business_model_component':['component','detail','assumptions']}
        components=[('客户价值主张','让线上客户按承诺获得可用商品','客户愿为可靠性选择本商店，需研究验证'),('利润公式','候选利润=销售收入−商品采购−履约变动成本−约定期间固定成本','本例未给财务值，不形成收益结论'),('关键资源','受控库存、仓库团队、订单信息及合作承运商','库存准确性及承运能力待核实'),('关键流程','确认购买承诺、拣配发运、处理例外','需业务责任方验证流程边界')]
        for i,(component,detail,assumptions) in enumerate(components):E(str(i),'business_model_component',component,component=component,detail=detail,assumptions=assumptions)
        for i in [1,2,3]:R('alignment'+str(i),'traces_to',es[i]['id'],es[0]['id'],'候选一致性：支持价值主张；不是原图箭头或已证实因果')
        p['structural_requirements']={'minimum_entity_types':{'business_model_component':4}}
    elif aid=='business-model-cube':
        p['required_attributes']={'business_model_dimension':['dimension','detail','local_mapping']}
        for i,(dimension,detail) in enumerate([('价值主张','可靠且透明的商品履约'),('客户','需要按承诺交付的线上客户'),('网络伙伴','承运商与商品供应方'),('活动','确认订单、拣配发运、处理例外'),('胜任力','履约协调与订单信息治理'),('价值公式','明确期间收入减采购履约和固定成本；尚无数值')]):
            E(str(i),'business_model_dimension',dimension,dimension=dimension,detail=detail,local_mapping='从参考维度映射到本例业务候选，待验证')
        R('customer-value','traces_to',es[0]['id'],es[1]['id'],'本例价值主张面向该客户；项目补充关系')
        R('partner-activity','traces_to',es[2]['id'],es[3]['id'],'承运商参与发运活动；项目补充关系')
        R('competence-activity','traces_to',es[4]['id'],es[3]['id'],'胜任力支撑活动；不是来源图流程箭头')
        p['structural_requirements']={'minimum_entity_types':{'business_model_dimension':6}}
    elif aid=='operating-model':
        p['required_attributes']={'operating_model':['integration','standardization','scope','rationale','quadrant']}
        p['template'].update({'x_axis':'业务流程标准化：低 → 高','y_axis':'业务流程集成：低 → 高'})
        for n,name,position,integration,standardization in [('coord','协调','top-left','高','低'),('unify','统一','top-right','高','高'),('diverse','多元化','bottom-left','低','低'),('replicate','复制','bottom-right','低','高')]:
            E(n,'operating_model',name,integration=integration,standardization=standardization,scope='参考候选模式，尚未选定本地适用范围',rationale='本例只展示两轴定义；实际范围与权衡需访谈取证',quadrant=position)
    elif aid=='stakeholder-influence-matrix':
        p['required_attributes']={'stakeholder':['influence','impact','engagement','concern','quadrant']}
        p['template'].update({'x_axis':'Impact 所受影响程度：低 → 高','y_axis':'Influence 影响力：低 → 高'})
        for n,name,position,influence,impact,engagement in [('sponsor','业务赞助人','top-right','高','高','重点管理'),('legal','法律顾问','top-left','高','低','令其满意'),('operator','仓库操作员','bottom-right','低','高','随时告知'),('observer','非试点地区观察者','bottom-left','低','低','监督')]:
            E(n,'stakeholder',name,influence=influence,impact=impact,engagement=engagement,concern='本例在线履约变更对职责或成果的影响',quadrant=position,evidence='虚构分级，待当事方核实；不代表决策授权')
    elif aid=='balanced-scorecard':
        p['required_attributes']={'goal':['perspective','definition'],'outcome':['perspective','metric','unit','baseline','target','period']}
        for i,(perspective,goal,outcome,metric,unit,baseline,target) in enumerate([('客户','提升重复购买','重复购买比例提高','期间重复购买客户占比','%',20,22),('学习与成长','提升人员稳定性','员工流失率降低','期间员工离职人数除期初人数','%',10,8.5),('内部流程','提高订单履约效率','平均确认时间下降','确认订单耗时算术平均','分钟',20,10),('财务','增加可持续销售','销售额增长','同口径期间商品销售额','万元',100,110)]):
            g=E('goal'+str(i),'goal',goal,perspective=perspective,definition='本例候选战略意图，需责任人确认')
            o=E('outcome'+str(i),'outcome',outcome,perspective=perspective,metric=metric,unit=unit,baseline=baseline,target=target,period='2026Q4 对2026Q3；虚构同口径期间')
            R('realize'+str(i),'realizes',o,g,'可度量成果实现目标；不是跨视角因果')
        p['structural_requirements']={'minimum_entity_types':{'goal':4,'outcome':4},'relationship_types':['realizes']}
    elif aid=='digital-business-reference-tailoring':
        p['required_attributes']={'dbrm_domain':['definition'],'dbrm_element':['definition','local_mapping','applicability']}
        for i,(domain,elements) in enumerate([('数字',['客户聚焦','数字企业']),('战略',['战略语境','业务动机','业务服务与产品']),('结构',['生态与业务模型','运营模式','业务能力模型']),('运营',['业务运营环境','数字使能'])]):
            d=E('domain'+str(i),'dbrm_domain',domain+'域',definition='DBRM参考域；不是TOGAF业务数据应用技术域',category=domain)
            for j,name in enumerate(elements):
                element=E('element'+str(i)+str(j),'dbrm_element',name,definition='DBRM十核心要素之一：'+name,local_mapping='本例在线履约需补充'+name+'的业务证据',applicability='候选适用，需裁剪责任人验证',category=domain,parent_id=d)
                R('contains'+str(i)+str(j),'contains',d,element,'DBRM域含核心要素；是参考结构，不是本地业务事实')
        p['structural_requirements']={'minimum_entity_types':{'dbrm_domain':4,'dbrm_element':10},'relationship_types':['contains']}
    elif aid=='business-capability-map':
        if 'heatmap' in pid:
            p['required_attributes']={'capability':['definition','dimension','score','scale','target']}
            p['template'].update({'score_field':'score','colors':{'1':'#f3c6c2','2':'#ffe5b1','3':'#bfe0c6','4':'#98cba8'}})
            for i,(name,score) in enumerate([('订单管理',2),('库存管理',3),('交付管理',1)]):
                E(str(i),'capability',name,definition='管理'+name.replace('管理','')+'相关结果',category='核心',dimension='履约支持充分性',score=score,scale='虚构1至4级：缺失、临时、受控、优化',target=4)
        else:
            p['required_attributes']={'capability':['definition','category','level']}
            root=E('fulfillment','capability','订单履约',definition='使已确认订单按承诺交付，排除市场获客',category='核心',level=1)
            c=E('order','capability','订单管理',definition='建立并维持准确订单状态',category='核心',level=2)
            d=E('delivery','capability','交付管理',definition='管理发运承诺和交付结果',category='核心',level=2)
            R('decomp-order','decomposes',root,c,'履约能力分解为订单管理')
            R('decomp-delivery','decomposes',root,d,'履约能力分解为交付管理')
            if 'classification' in pid:
                E('strategy','capability','业务规划',definition='确定企业方向和业务结果',category='战略',level=1)
                E('support','capability','人员发展',definition='发展履约所需人员能力',category='支持',level=1)
    elif aid in ['capability-instance-model','capability-increment-analysis']:
        p['required_attributes']={'capability':['definition'],'capability_instance':['definition','stage_id']}
        cap=E('type','capability','客户身份管理',definition='建立并校验履约所需客户身份，不限定某应用')
        stage1=E('select','value_stage','选择商品',order=1,entry_condition='客户进入商店',exit_condition='形成待结算商品',value_item='可购买的商品选择')
        stage2=E('buy','value_stage','购买商品',order=2,entry_condition='客户确认购物篮',exit_condition='付款和客户身份得到确认',value_item='有效订单')
        R('next','precedes',stage1,stage2,'选择后进入购买')
        for n,s,change in [('browse',stage1,'保留'),('payment',stage2,'改进')]:
            inst=E(n,'capability_instance','客户身份管理：'+('选择阶段' if n=='browse' else '购买阶段'),
                   definition='在该阶段按对应安全和体验要求实现客户身份管理',stage_id=s,change_kind=change,
                   baseline='人工确认或访客身份',target='按风险分级校验身份',rationale='避免不必要的登录摩擦并满足付款安全',gap='付款阶段需补充强校验')
            R(n+'-type','instance_of',inst,cap,'实例属于客户身份管理能力类型')
            R(n+'-stage','stage_uses_instance',s,inst,'阶段由该身份实例使能')
            for suffix,typ,name in [('role','role','客户服务角色'),('process','process','校验客户身份'),('app','application','客户身份服务'),('info','information','客户身份信息')]:
                c=E(n+'-'+suffix,typ,('选择阶段：' if n=='browse' else '购买阶段：')+name,definition='该阶段实例使用的'+name)
                R(n+'-'+suffix+'-composition','instance_comprises',inst,c,'实例组成：'+name)
        p['structural_requirements']={'minimum_entity_types':{'capability':1,'value_stage':2,'capability_instance':2},
                                      'relationship_types':['instance_of','stage_uses_instance','instance_comprises']}
    elif aid=='value-stream-map' or aid=='customer-journey':
        journey=aid=='customer-journey';typ='customer_journey_stage' if journey else 'value_stage'
        p['required_attributes']={typ:['order','entry_condition','exit_condition','value_item'] if not journey else ['order','actor','touchpoint','experience','pain_point','outcome']}
        stream=E('stream','value_stream','获取零售商品',beneficiary='线上客户',trigger='客户需要商品',outcome='客户按承诺获得商品')
        stages=[]
        for i,name in enumerate(['选择商品','确认订单','接收商品'],1):
            a={'order':i,'entry_condition':['客户确认需求','已选择商品','已确认并发运'][i-1],
               'exit_condition':['形成购物篮','有效订单已确认','客户确认收货'][i-1],
               'value_item':['适合需要的商品组合','可履行的购买承诺','可使用的商品'][i-1]}
            if journey:a.update(actor='线上客户',touchpoint=['商品页面','结算页面','配送通知'][i-1],experience='理解当前进展与下一步',pain_point='本例假设存在状态不清，需用户研究验证',outcome=a['value_item'])
            stages.append(E('stage'+str(i),typ,name,**a))
            R('stream-stage'+str(i),'has_journey_stage' if journey else 'traces_to',stream,stages[-1],'价值流包含该阶段；非流程控制线')
            if i>1:R('precedence'+str(i),'precedes',stages[-2],stages[-1],'客户体验阶段的先后' if journey else '客户价值阶段依次推进')
        if 'capabilit' in pid:
            cap=E('cap','capability','订单履约',definition='实现有效订单并按承诺交付',level=1,dimension='阶段支持充分性',score=2,scale='虚构1缺失2临时3受控4优化',target=4,category='核心')
            for i,s in enumerate(stages):R('enable'+str(i),'enabled_by',s,cap,'阶段由订单履约能力使能')
            if 'heatmap' in pid:
                p['required_attributes']['capability']=['dimension','score','scale','target'];p['template']['colors']={'1':'#f3c6c2','2':'#ffe5b1','3':'#bfe0c6','4':'#98cba8'}
    elif aid=='business-model-diagram':
        p['required_attributes']={'business_model_element':['block','detail']}
        p['template']['canvas_kind']='business-model'
        details=['商品供应商与承运商','订单确认与履约','库存与客户服务人员','可靠且可跟踪的商品交付','及时解释并处理例外','在线商店与通知渠道','需要透明履约的线上客户','库存、仓储、人员与配送成本','商品销售收入及明确服务收费']
        for i,(block,detail) in enumerate(zip(BMC,details)):
            E(str(i),'business_model_element',detail,block=block,detail=detail)
    elif aid=='customer-persona':
        p['required_attributes']={'persona':['segment','goals','behaviors','needs','evidence','assumptions']}
        p['template'].update({'canvas_kind':'persona','blocks':['客户群体','目标','行为','需求','研究证据','假设']})
        a=attrs('persona',segment='虚构线上常购客户',goals='按承诺收货并可追踪',behaviors='本例假设会在发货前查询状态',needs='准确状态及例外说明',evidence='虚构案例输入，不是真实用户研究',assumptions='行为频次和群体代表性尚待验证',block='客户群体')
        E('persona','persona','线上常购客户画像',**a)
    elif aid=='sustainability-review-canvas':
        p['renderer']='environmental-review'
        p['required_attributes']={'sustainability_action':['block']}
        p['template'].update({'canvas_kind':'sustainability','blocks':['业务贡献','环境核算','架构措施'],
                              'form_contract':'G242-fig3-14/1','source_verified':False})
        E('0','sustainability_action','业务环境正向影响',block='业务贡献',decisions=[
            {'id':'measure','selected':'YES','explanation':'候选系统记录仓配电力活动；需验证数据可得性'},
            {'id':'reduce','selected':'NO','explanation':'尚无可证实的客户侧减排因果结果'},
            {'id':'train','selected':'YES','explanation':'向运营人员展示候选环境指标口径'}])
        E('1','sustainability_action','IT 碳足迹候选核算',block='环境核算',carbon_footprint={
            'direction':'Decrease','unit':'kgCO2e','years':[2026,2027],
            'rows':[
                {'id':'in','total':120,'values':{'year1':{'scope2':30,'scope3_service':20,'equipment_scope3':70},'year2':{'scope2':0,'scope3_service':0,'equipment_scope3':0}}},
                {'id':'out','total':150,'values':{'year1':{'scope2':50,'scope3_service':20,'equipment_scope3':80},'year2':{'scope2':0,'scope3_service':0,'equipment_scope3':0}}},
                {'id':'balance','total':-30,'values':{'year1':{'scope2':-20,'scope3_service':0,'equipment_scope3':-10},'year2':{'scope2':0,'scope3_service':0,'equipment_scope3':0}}}],
            'comment':'虚构项目演练数据；边界、排放因子及真实测量尚未确认。原图印刷差异单列于来源解释，不套用为本项目数值。'})
        E('2','sustainability_action','架构环境措施',block='架构措施',measures=[
            {'id':'development','selected':'YES','explanation':'候选开发评审'},
            {'id':'equipment','selected':'YES','explanation':'候选寿命比较'},
            {'id':'procurement','selected':'NO','explanation':'采购准则未批准'},
            {'id':'data','selected':'YES','explanation':'候选保留策略'},
            {'id':'users','selected':'NO','explanation':'尚无用户研究'}])
    elif aid=='value-chain-diagram':
        p['required_attributes']={'value_chain_activity':['category','definition','contribution']}
        for i,name in enumerate(['基础设施','人力资源管理','技术开发','采购']):E('support'+str(i),'value_chain_activity',name,category='支持',definition='支撑价值创造的'+name,contribution='支撑主要活动并管理间接成本')
        for i,name in enumerate(['内部物流','运营','外部物流','市场与销售','服务']):E('primary'+str(i),'value_chain_activity',name,category='主要',definition='面向价值创造的'+name,contribution='形成客户价值并发生相应成本')
        p['template']['margin']='价值减成本所得的经济贡献；本例未提供金额，不能计算利润'
    elif pid=='information-capability-use-modify':
        p['required_attributes']={'capability':['definition'],'information':['definition']}
        c=E('cap','capability','订单管理',definition='建立并维护有效订单状态')
        i=E('order','information','订单',definition='客户与企业间的商品和履约承诺')
        R('read','uses_information',c,i,'使用订单信息进行确认')
        R('write','modifies_information',c,i,'修改订单状态；不等同于只读使用')
    elif aid in ['information-map','conceptual-data-diagram','logical-data-diagram','metadata-model','customer-mdm-model']:
        typ=primary
        if pid=='information-aggregation-generalization':
            p['required_attributes']={'information':['definition']}
            customer=E('customer','information','客户',definition='与企业形成业务关系的主体')
            person=E('person','information','自然人客户',definition='作为自然人参与的客户')
            order=E('order','information','订单',definition='包含商品和履约承诺的业务对象')
            line=E('line','information','订单明细',definition='只在所属订单中存在的商品条目')
            R('general','generalization',person,customer,'自然人客户是客户的特化')
            R('composition','composition',order,line,'订单独占组成订单明细')
            R('aggregation','aggregation',customer,order,'客户聚合与其关联的订单；订单有独立生命周期')
        else:
            if aid=='metadata-model':
                p['required_attributes']={'metadata_asset':['metadata_category','definition','identifier','domain','owner']}
                a=E('term','metadata_asset','订单业务术语',metadata_category='业务元数据',definition='客户的商品购买与交付承诺',identifier='TERM-ORDER',domain='订单业务语义',owner='订单业务所有者')
                b=E('field','metadata_asset','订单状态字段',metadata_category='技术元数据',definition='承载订单状态的字段描述',identifier='FIELD-ORDER-STATUS',domain='已确认、已发运、已取消',owner='订单应用维护团队')
                R('maps','traces_to',a,b,'业务术语映射技术字段；不是数据值副本')
            elif aid=='customer-mdm-model':
                p['required_attributes']={'master_data':['business_identity','identifier','source','matching','ownership','quality']}
                a=E('person','master_data','自然人客户内核',**attrs('master_data',business_identity='在订单关系中承担购买主体的自然人',identifier='候选客户主标识',source='经核实的客户源记录',matching='标识冲突人工核验；不按姓名直接合并',ownership='客户数据所有者',quality='身份唯一且可追溯'))
                b=E('org','master_data','组织客户内核',**attrs('master_data',business_identity='作为法律主体形成采购关系的组织',identifier='候选组织主标识',source='企业客户源记录',matching='按核实组织标识匹配',ownership='企业客户数据所有者',quality='组织身份及联系责任明确'))
                R('related','traces_to',a,b,'自然人可作为组织联系人；身份不自动合并')
            else:
                typ='logical_entity' if aid=='logical-data-diagram' else 'data_entity' if aid=='conceptual-data-diagram' else 'information'
                required={'logical_entity':['definition','attributes','identifier'],'data_entity':['definition'],'information':['definition','owner']}
                p['required_attributes']={typ:required[typ]}
                a=E('customer',typ,'客户',definition='形成购买关系且承担订单责任的主体',owner='客户业务所有者',identifier='客户业务标识',attributes=[{'name':'客户标识','type':'string','key':'PK','optional':False},{'name':'名称','type':'string','optional':False}])
                b=E('account',typ,'账户',definition='客户访问订单服务的授权身份',owner='身份业务所有者',identifier='账户标识',attributes=[{'name':'账户标识','type':'string','key':'PK','optional':False},{'name':'客户标识','type':'string','key':'FK','optional':False}])
                edge=R('association','logical_association' if typ=='logical_entity' else 'data_association' if typ=='data_entity' else 'traces_to',a,b,'客户持有账户；基数按本例约束')
                if typ in ['logical_entity','data_entity']:edge['cardinality']={'source':{'min':1,'max':2},'target':{'min':1,'max':None}}
    elif aid=='organization-map':
        p['required_attributes']={'organization':['category','boundary','definition']}
        org=E('enterprise','organization','星河零售',category='企业',boundary='本次架构范围内',definition='承担在线销售与履约责任')
        ops=E('ops','organization','在线运营',category='业务单元',boundary='内部',definition='管理在线订单和客户例外')
        ext=E('carrier','organization','承运合作方',category='外部伙伴',boundary='企业外部合同边界',definition='按合同交付商品')
        R('works','traces_to',ops,ext,'履约协作和例外交接；不是汇报关系')
        R('contains','traces_to',org,ops,'在线运营为本企业业务单元')
        if 'capability' in pid:
            cap=E('cap','capability','交付管理',definition='维持交付承诺并处理交付例外')
            R('cap-ops','traces_to',ops,cap,'在线运营承担该能力内部责任')
            R('cap-ext','traces_to',ext,cap,'伙伴参与该能力的配送实现')
    elif aid=='metadata-ingestion-options':
        p['required_attributes']={'metadata_component':['mechanism','responsibility','frequency','protocol','security','cost']}
        repo=E('repository','metadata_repository','元数据管理工具',scope='订单业务元数据与技术模式',authority='定义审核后发布')
        source=E('source','metadata_source','订单源应用',scope='提供模式与定义，不提供客户实际订单内容')
        for n,mechanism,resp,freq,protocol,cost in [('manual','手工','数据管家采集并提交','变更申请时','受控录入','人工维护与审核投入'),('push','推送','源应用主动通知变更','模式变更后','受控推送API','连接器维护及重试'),('pull','拉取','中央工具发起模式读取','每日一次','只读模式接口','轮询负载及访问控制')]:
            option=E(n,'metadata_component',mechanism+'采集候选',mechanism=mechanism,responsibility=resp,frequency=freq,protocol=protocol,security='最小授权、审计和敏感字段限制',cost=cost)
            R(n+'-source','traces_to',option,source,'方案适用订单源应用；三方案相互独立')
            R(n+'-repo','traces_to',option,repo,'方案向元数据工具提供受控元数据')
        R('push-flow','pushes_metadata',source,repo,'推送：源主动提交元数据')
        R('pull-control','pulls_metadata',repo,source,'拉取：目标主动发起读取请求')
    elif pid=='risk-security-traceability':
        p['required_attributes']={'risk':['likelihood','impact','owner','treatment']}
        threat=E('threat','threat_event','未授权修改订单',definition='假设攻击者利用管理访问薄弱点')
        vuln=E('vulnerability','vulnerability','高权限操作缺少复核',definition='候选脆弱性，待验证')
        loss=E('loss','loss_event','订单状态失真导致履约失败',definition='可能的业务损失场景')
        asset=E('asset','risk_asset','订单完整性',definition='与履约承诺有关的业务资产')
        risk=E('risk','risk','订单被篡改风险',likelihood='可能：虚构定性假设',impact='高履约影响：需责任方校准',owner='订单业务负责人',treatment='部署访问控制并验证')
        objective=E('objective','control_objective','高权限操作可追责',definition='异常订单修改可被预防或检测')
        req=E('requirement','security_requirement','订单修改必须通过授权并留审计证据',definition='候选可验证安全需求')
        control=E('control','control','权限复核与操作审计',definition='候选控制，效果未证实')
        app=E('app','application','订单应用',definition='候选控制实现载体')
        R('exploit','exploits',threat,vuln,'威胁利用脆弱性')
        R('loss-cause','causes_loss',threat,loss,'威胁事件可能造成损失')
        R('asset-impact','impacts_asset',loss,asset,'损失影响订单业务资产')
        R('risk-asset','impacts_asset',risk,asset,'风险作用于该资产')
        R('derive','derived_from',req,objective,'需求由控制目标导出')
        R('require','requires_control',req,control,'需求由候选控制实现')
        R('mitigation','risk_has_control',risk,control,'风险关联候选缓解控制')
        R('implementation','implements_control',app,control,'应用计划实现控制，未表示效果已验证')
    elif renderer=='matrix':
        p['required_attributes']={}
        if aid=='architecture-maturity-model':
            levels=[E('level'+str(i),'criterion','ACMM '+str(i)+'级',level=i,definition=d) for i,d in enumerate(['无','初始','开发中','已定义','已管理','已度量'])]
            for n,name in enumerate(['架构流程','架构开发','业务关联','高层管理参与','运营单元参与','架构沟通','IT安全','架构治理','投资与采购']):
                row=E('element'+str(n),'maturity_element',name,definition='评价该要素的实际过程证据')
                for i,level in enumerate(levels):R('cell'+str(n)+'-'+str(i),'traces_to',row,level,'按G203对应级别特征取证；本例未开展实测',evidence_rule='须有制度、执行或改进证据')
        elif aid in ['readiness-consequence-analysis']:
            f=E('factor','readiness_factor','赞助与方向',category='基础',rating=4,evidence='虚构访谈：发起人尚未承诺')
            c=E('consequence','consequence','决策和资源缺乏持续支持',definition='条件性主要后果；发生概率待分析')
            R('factor-consequence','has_consequence',f,c,'因素不足可能导致该后果')
        elif aid=='metadata-asset-coverage':
            rows=[E('row'+str(i),'metadata_asset',name,metadata_category=name,definition='元数据类别，不是数据保密等级') for i,name in enumerate(['业务','技术','运营'])]
            cols=[E('col'+str(i),'criterion',name,definition='本例所检查的管理维度') for i,name in enumerate(['数据质量','文档化','安全与隐私','治理'])]
            for i,row in enumerate(rows):
                for j,col in enumerate(cols):
                    if not (i==2 and j==1):R('coverage'+str(i)+str(j),'traces_to',row,col,'本例候选资产已识别；覆盖程度需核验',codes='candidate')
            p['template']['row_types']=['metadata_asset'];p['template']['column_types']=['criterion']
        elif aid=='options-decision-matrix':
            rows=[E('option'+str(i),'option',name,definition='待选择，未批准') for i,name in enumerate(['改善现有平台','整体替换平台'])]
            cols=[E('criterion'+str(i),'criterion',name,weight=1 if i!=2 else 2,scale='1最差至5最佳的偏好评分') for i,name in enumerate(['成本偏好','资源偏好','问题贡献','可行性'])]
            for i,row in enumerate(rows):
                for j,col in enumerate(cols):R('score'+str(i)+str(j),'evaluated_by',row,col,'偏好值 '+str(([4,4,3,5] if i==0 else [2,2,5,2])[j])+'；虚构评议证据',score=([4,4,3,5] if i==0 else [2,2,5,2])[j])
        elif aid=='scenario-traceability-matrix':
            rows=[E('process'+str(i),'process',name,definition='场景中的实际业务行为') for i,name in enumerate(['确认订单','发运商品'])]
            cols=[E('stakeholder','stakeholder','订单业务负责人',concern='可靠履约'),E('actor','actor','仓库操作员',definition='核对并发运'),E('computer','application','仓库应用',definition='提供发运支持'),E('problem','problem','发运状态不透明',definition='客户无法可靠获知状态'),E('goal','goal','一个工作日内发运',definition='虚构业务目标，需测量')]
            for i,row in enumerate(rows):
                for j,col in enumerate(cols):R('scenario'+str(i)+str(j),'traces_to',row,col,['受关注','参与','由计算机支持','解决问题','支撑目标'][j]+'；关联不等于控制流')
        else:
            row=E('row',primary,p['name']+'：业务范围',**attrs(primary))
            col=E('column','criterion','对应检查准则',definition=p['checks'][0])
            R('cell','evaluated_by',row,col,'本例候选评价：需核对原始证据')
    elif renderer=='nested-map':
        if aid=='functional-decomposition-diagram':typ='function'
        elif aid in ['government-reference-tailoring','digital-business-reference-tailoring']:typ=primary
        else:typ=primary
        p['required_attributes']={typ:[f for f in required.get(typ,[]) if f!='parent']}
        root=E('root',typ,p['name']+'：本次范围',**attrs(typ,definition='按本例业务职责分解，排除不适用参考项',level=1))
        for i,name in enumerate(['定义与规划','运营与治理']):
            child=E('child'+str(i),typ,name,**attrs(typ,definition='本例'+name+'的职责边界',level=2,parent_id=root))
            if typ in ['capability','function']:R('part'+str(i),'decomposes',root,child,'同类型职责分解')
            else:R('part'+str(i),'traces_to',root,child,'参考分类的从属项；不推断组织汇报')
    elif renderer=='quadrant':
        p['required_attributes']={primary:[f for f in required.get(primary,[]) if f not in ['polarity','loop_type']]}
        if aid=='digital-adoption-position':
            for n,name,q,u,v in [('A','先锋式','top-left','低','高'),('B','大爆炸式','top-right','高','高'),('C','凝聚式','bottom-right','高','低'),('D','谨慎式','bottom-left','低','低')]:
                E(n,primary,name,**attrs(primary,quadrant=q,ubiquity=u,velocity=v,rationale='按本企业范围速度与资源权衡；字母无优劣',scope='在线订单业务范围',tradeoffs='广度速度与风险资源之间的取舍'))
        else:
            for i,(name,q) in enumerate(zip(['组织管理与工作文化','技能教育','沟通','节制创新'],['top-left','top-right','bottom-left','bottom-right'])):
                E(str(i),primary,name,**attrs(primary,category=name,definition='数字节制文化的并列关注维度；无高低轴',quadrant=q))
    elif renderer=='sequence':
        p['required_attributes']={primary:required.get(primary,[])}
        a=E('producer',primary,'源方／提交活动',**attrs(primary,order=1,actor='源应用或数据管家',action='提交更新',input='已授权的变更',output='待校验内容',validation='校验身份和版本'))
        b=E('consumer',primary,'目标方／校验活动',**attrs(primary,order=2,actor='目标数据管理服务',action='校验并确认',input='待校验内容',output='受控确认',validation='按契约验证字段与一致性'))
        R('submit','traces_to',a,b,'提交有版本的更新请求',order=1)
        R('reply','traces_to',b,a,'返回受控结果或明确拒绝',order=2)
    elif renderer=='causal':
        p['required_attributes']={'measure':['definition']}
        a=E('usage','measure','数字使用量',definition='在既定边界内的数字服务使用量')
        b=E('infra','measure','基础设施投入',definition='为满足使用需求增加的计算与设备')
        c=E('cost','measure','单位数字服务成本',definition='在明确服务与期间内的成本')
        R('a-b','causal_influence',a,b,'使用增加推动基础设施需求',polarity='+')
        R('b-c','causal_influence',b,c,'规模效应可能降低单位成本，待本地验证',polarity='-')
        R('c-a','causal_influence',c,a,'成本降低可能促使更多使用',polarity='-')
        view_attributes={'loops':[{'id':'R1','type':'reinforcing','relationship_ids':[r['id'] for r in rs],'evidence':'本例假设；边极性乘积为正，不证明现实因果'}]}
    elif renderer=='roadmap':
        if aid in ['transition-architecture-model']:
            p['required_attributes']={'transition':['definition','operating_conditions']}
            previous=None
            for i,name in enumerate(['基线：旧平台','过渡1：只读副本','过渡2：分批写入','目标：统一履约']):
                n=E('state'+str(i),'transition',name,definition='本例具名运营状态，演进分类见标签',operating_conditions={'operations':'值班与服务责任明确','data_consistency':'逐笔对账后切换','dependencies':'身份与接口已就绪','controls':'授权与审计持续','rollback':'暂停新写并恢复旧平台'},ordinal=i)
                if previous:R('evolve'+str(i),'traces_to',previous,n,'达到进入退出条件后演进；不是仅有日期')
                previous=n
            wp=E('wp','work_package','接口及对账工作包',definition='实现第一过渡的候选工作包')
            R('impl','implements_transition',wp,es[1]['id'],'工作包实现可运营过渡')
        else:
            for i,name in enumerate([p['name']+'：准备',p['name']+'：验证'],1):
                ident=E('step'+str(i),primary,name,**attrs(primary,order=i,start='2026-11-02' if i==1 else '2026-11-16',end='2026-11-13' if i==1 else '2026-11-27'))
                if aid=='application-migration-diagram':
                    es[-1].update(concept_id=pid+'-application-concept',evolution='baseline' if i==1 else 'target')
            R('dependency','traces_to',es[1]['id'],es[0]['id'],'后项以准备结果为进入条件；工期是虚构演示')
    elif renderer=='deployment':
        if aid=='bi-transition-architecture':
            p['required_attributes']={'analytics_component':['state_id','role','inbound','outbound','storage','coexistence']}
            for n,name in [('baseline','基线'),('transition1','过渡1'),('transition2','过渡2'),('target','目标')]:
                E(n,'analytics_component',name+'分析平台',state_id=n,role='数据处理与分析消费支持',inbound='交易应用提交已完成订单',outbound='向报表提供聚合数据，目标保留受控回写',storage='基线EDW；目标新平台内保留EDW职责',coexistence='新旧并行对账，按消费者分批切换',operating_conditions='运营责任、数据一致性、控制连续性及回退须经验证')
            for a,b in zip(es,es[1:]):R(a['id']+'-next','traces_to',a['id'],b['id'],'演进状态；不是强制替换厂商')
        elif aid in ['metadata-integration-model','mdm-integration-style']:
            variants=['集中','混合','统一'] if aid=='metadata-integration-model' else ['整合','协作','集中']
            for n,name in enumerate(variants):E(str(n),primary,name+'候选方案',**attrs(primary,integration_style=name,style=name,authority='明确中央与源方的主记录责任；需逐项裁剪',collaboration='源方与中央团队按契约协作',consumers='订单与客户服务应用',synchronization='按权威和时效要求交换，非默认双向写'))
        elif aid=='metadata-inference-design':
            for n,name,schema,content in [('structured','结构化','可读字段模式','无需读取客户实际值'),('semi','半结构化','有结构但需验证稳定性','仅在批准范围抽样'),('unstructured','非结构化','无稳定字段模式','内容扫描需独立隐私与成本评估')]:E(n,primary,name+'来源',**attrs(primary,data_structure=name,schema_access=schema,content_access=content))
        elif pid=='metadata-three-part-solution':
            p['required_attributes']={'metadata_repository':['scope','model','governance']}
            for n,name in enumerate(['技术组件','数据模型','管理流程']):E(str(n),'metadata_repository',name,scope='支持订单元数据需求',model='定义术语、资产与关系',governance='职责、校验、变更与发布协作')
        else:
            E('domain',primary,p['name']+'：订单范围',**attrs(primary))
            app=E('application','application','订单应用',definition='本例待治理或支撑的实现应用')
            R('mapping','traces_to',es[0]['id'],app,'本工作产品所涉及的实现对象；不从邻近推断安全授权')
    else:
        E('record',primary,p['name']+'：订单范围记录',**attrs(primary))
        if renderer=='network':
            target=E('target','goal','可靠履约',definition='在承诺时间内交付且状态可追溯')
            R('supports','traces_to',es[0]['id'],target,'本工作产品的结论为该业务目标提供候选支撑')
    ex={'notice':'虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。',
        'sources':[{'id':'example-source','kind':'example','description':'虚构业务案例：在线订单、仓库发运及客户通知'}],
        'entities':es,'relationships':rs,
        'view':{'id':'v-'+pid,'artifact_id':aid,'profile_id':pid,'title':p['name']+'／虚构案例',
                'entity_ids':[e['id'] for e in es],'relationship_ids':[r['id'] for r in rs],
                'analysis':'依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。',
                'legend':'虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。'}}
    if renderer=='causal':ex['view']['attributes']=view_attributes
    if aid=='application-migration-diagram':ex['view']['allow_mixed_evolution']=True
    # Relationship fields and annotations are not mandatory entity attributes.
    p['required_attributes']={typ:[f for f in fs if f not in ['name','parent','state_id']] for typ,fs in p['required_attributes'].items()}
    p['entity_types']=sorted({e['type'] for e in es})
    p['relationship_types']=sorted({r['type'] for r in rs})
    p['example']=ex
    return ex
