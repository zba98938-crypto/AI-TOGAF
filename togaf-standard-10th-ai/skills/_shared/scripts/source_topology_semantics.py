"""Source-specific topology invariants; never grants source or business acceptance."""
from collections import defaultdict

KINDS={'repository-tree','repository-comparison','capability-continuum','stakeholder-concern-matrix','mdm-integration','metadata-integration','security-crosscut','bi-evolution','content-metamodel',
       'ea-adm-matrix','msa-governance','msa-execution','architecture-repository','architecture-landscape','security-adm-map','metadata-inference','soa-layered'}
REPO_PARTITIONS=('metamodel','landscape','solutions','reference','standards','requirements','governance','capability')
LANDSCAPE_AXES=('breadth','abstraction','time')
ADM_PHASES=('P','A','B','C','D','E','F','G','H','RM')
SOA_LAYERS=('consumer-interface','business-process','services','service-component','operational-systems')
SOA_CONCERNS=('integration','qos','information','governance')
DOMAINS=('business','data','application','technology')

SECURITY_GROUPS = {
 'business_drivers': {'P','A'}, 'security_principles': {'P','A'},
 'risk_appetite': {'P','A'}, 'key_risk_areas': {'P','A'}, 'security_resource_plan': {'P','A'},
 'security_policy_architecture': {'B'}, 'security_domain_model': {'B'}, 'trust_framework': {'B'},
 'risk_assessment': {'B'}, 'business_risk_model': {'B'}, 'law_register': {'B'},
 'control_framework_register': {'B'}, 'security_services_catalog': {'C'},
 'security_classification': {'C'}, 'data_quality': {'C'}, 'security_standards': {'D'},
 'business_attribute_profile': {'E','RM'}, 'control_objectives': {'E','RM'},
 'risk_mitigation_plan': {'F'}, 'security_audit': {'G'}, 'security_training': {'G'}}
SECURITY_ADDITIONS = {'risk_appetite','key_risk_areas','security_policy_architecture','trust_framework',
 'risk_assessment','business_risk_model','law_register','control_framework_register','security_services_catalog',
 'security_classification','data_quality','business_attribute_profile','control_objectives','security_audit','security_training'}

def landscape_members(es, slice_entity):
    """Categorical coordinate intersection; no membership inferred from adjacency."""
    bounds=slice_entity.get('attributes',{})
    def matches(value,bound):
        return value in bound if isinstance(bound,list) else value==bound
    return {e['id'] for e in es if e['type'] not in {'landscape_projection','landscape_dimension','landscape_slice'}
            and all(matches(e.get('attributes',{}).get(k),bounds.get(k)) for k in LANDSCAPE_AXES)}

def check_source_topology(es,rs,profile,view=None):
    kind=profile.get('template',{}).get('source_topology')
    if kind not in KINDS:return []
    errors=[];byid={e['id']:e for e in es}
    def need(ok,code,identity,message):
        if not ok:errors.append({'code':code,'id':identity,'message':message})
    def attrs(e):return e.get('attributes',{})
    def edges(a,b):return [r for r in rs if r['source']==a and r['target']==b]
    for r in rs:
        need(r['source'] in byid and r['target'] in byid,'topology-endpoint-missing',r['id'],'拓扑关系的两端必须在同一视图中。')
    if errors:return errors
    if kind in {'repository-tree','repository-comparison','capability-continuum','stakeholder-concern-matrix'}:
        from repository_reference_profiles import check
        return check(es,rs,kind)
    if kind in {'mdm-integration','metadata-integration'}:
        patterns=('consolidation','cooperation','centralized') if kind=='mdm-integration' else ('consolidation','hybrid','unified')
        grouped=defaultdict(list)
        for e in es:grouped[attrs(e).get('integration_style')].append(e)
        need(set(grouped)==set(patterns),'integration-alternatives-missing',profile['id'],'比较视图必须明确三种并列风格，不能视作时间阶段。')
        for r in rs:
            need(attrs(byid[r['source']]).get('integration_style')==attrs(byid[r['target']]).get('integration_style'),'integration-cross-alternative-flow',r['id'],'不能在不同候选风格之间画数据流。')
        for pattern in patterns:
            nodes=grouped[pattern];centers=[e for e in nodes if attrs(e).get('topology_role')=='central']
            need(len(centers)==1,'integration-central-count',pattern,'每种风格需且仅需一个中央库。')
            if len(centers)!=1:continue
            center=centers[0];others=[e for e in nodes if e!=center]
            need(bool(others),'integration-periphery-missing',pattern,'中央库需要显式外围系统或社区，文字方案卡不能表达拓扑。')
            if kind=='mdm-integration':
                authority={'consolidation':'external-master','cooperation':'central-canonical','centralized':'central-master'}[pattern]
                need(attrs(center).get('authority')==authority,'mdm-central-authority',center['id'],'中央库主控责任与风格不符。')
                for e in others:
                    incoming=bool(edges(e['id'],center['id']));outgoing=bool(edges(center['id'],e['id']))
                    expected={'consolidation':(True,False),'cooperation':(True,True),'centralized':(False,True)}[pattern]
                    need((incoming,outgoing)==expected,'mdm-flow-direction',e['id'],'整合：源→MDM；协作：源↔MDM；集中：MDM→消费方。')
                    expected_authority='consumer-only' if pattern=='centralized' else 'operational-master'
                    need(attrs(e).get('authority')==expected_authority,'mdm-peripheral-authority',e['id'],'集中式外围不保有独立主记录；其他风格须声明运营源职责。')
            else:
                expected={'consolidation':('copy-only','external'),'hybrid':('selected-scopes','mixed'),'unified':('all-scopes','central')}[pattern]
                need((attrs(center).get('authority'),attrs(center).get('workflow_owner'))==expected,'metadata-central-authority',center['id'],'集中只保存副本；混合选定范围主记录入中央；统一全部主记录与工作流入中央。')
                scopes={attrs(e).get('domain_key') for e in others}
                expected_scopes={'governance','glossary','processes','reference','application','technical','privacy','risk','security'}
                need(scopes==expected_scopes,'metadata-domain-coverage',pattern,'参考比较需覆盖九个社区；社区不是九个独立存储库。')
                need(len(others)==len(scopes),'metadata-community-duplicate',pattern,'比较模式中每个社区只出现一次；同域多个企业实例应使用项目拓扑视图。')
                for e in others:
                    a=attrs(e);domain=a.get('domain_key');location=a.get('repository_location')
                    central=domain=='governance' or pattern=='unified' or (pattern=='hybrid' and domain in {'glossary','processes','reference'})
                    expected_location='none' if domain=='governance' else 'central' if central else 'external'
                    need(location==expected_location,'metadata-repository-location',e['id'],'是否保留外围主库必须与所选风格和范围相符。')
                    both=central and not (pattern=='unified' and domain=='security')
                    incoming=bool(edges(e['id'],center['id']));outgoing=bool(edges(center['id'],e['id']))
                    need((incoming,outgoing)==(True,both),'metadata-flow-direction',e['id'],'供数、社区读写和治理交换的箭头必须显式；统一式安全社区保留原图单向供数例外。')
    elif kind=='security-crosscut':
        domains={attrs(e).get('architecture_domain'):e for e in es if e['type']=='guide:architecture_domain'}
        concerns=[e for e in es if e['type']=='security_component']
        need(set(domains)==set(DOMAINS),'security-four-domains',profile['id'],'安全需横贯业务、数据、应用、技术四域，不能新增第五域或只连应用。')
        need(sum(e['type']=='guide:architecture_domain' for e in es)==4,'security-domain-duplicate',profile['id'],'四个架构域是类别，不能以同域实例复制冒充第五域。')
        need(bool(concerns),'security-concern-missing',profile['id'],'需有跨域安全关注点。')
        for e in concerns:
            targets={r['target'] for r in rs if r['source']==e['id'] and r['type']=='project:cross_cuts'}
            need(targets=={d['id'] for d in domains.values()},'security-crosscut-incomplete',e['id'],'每一安全关注点必须显式覆盖四域；交叠表示覆盖而非流程箭头。')
    elif kind=='bi-evolution':
        stages=('baseline','transition1','transition2','target');grouped=defaultdict(list)
        for e in es:grouped[attrs(e).get('stage')].append(e)
        need(set(grouped)==set(stages),'bi-states-missing',profile['id'],'需分别表达基线、两个过渡态与目标的实际组件。')
        for r in rs:
            a=attrs(byid[r['source']]);b=attrs(byid[r['target']]);flow=r.get('attributes',{}).get('flow_role')
            need(a.get('stage')==b.get('stage'),'bi-flow-crosses-state',r['id'],'跨状态对应不应被画为运营数据流。')
            need(flow in {'inbound','outbound'},'bi-flow-role',r['id'],'入站虚线和出站实线是源图角色，不表示确定度。')
            if flow=='inbound':need(b.get('component_role') in {'edw','platform'},'bi-inbound-direction',r['id'],'入站与回写均指向接收历史数据的平台。')
            if flow=='outbound':need(a.get('component_role') in {'edw','platform'} and b.get('component_role') in {'edw','platform','consumer'},'bi-outbound-direction',r['id'],'出站供数必须来自数仓或平台，交付另一平台或消费方。')
        for stage in stages:
            nodes=grouped[stage];roles=defaultdict(list)
            for e in nodes:roles[attrs(e).get('component_role')].append(e)
            need(bool(roles['transaction']) and bool(roles['consumer']),'bi-operating-components',stage,'每个状态需有真实供数方与消费方，不是状态文本卡。')
            need(len(roles['edw'])==1,'bi-edw-role',stage,'每个状态应明确数仓或被目标覆盖的数仓职责。')
            need(len(roles['platform'])==(0 if stage=='baseline' else 1),'bi-platform-role',stage,'基线没有新平台，过渡与目标各有一个新平台。')
            for e in roles['edw']+roles['platform']:need(attrs(e).get('boundary')=='inside','bi-platform-boundary',e['id'],'数仓和分析平台须处于图示平台范围内。')
            for e in roles['transaction']+roles['external']:
                need(attrs(e).get('boundary')=='outside','bi-source-boundary',e['id'],'事务与外部数据源须在分析平台范围外。')
                need(any(r['source']==e['id'] for r in rs),'bi-source-flow-missing',e['id'],'供数方需有显式入站流。')
            for e in roles['consumer']:
                need(attrs(e).get('boundary')=='inside','bi-consumer-boundary',e['id'],'图示消费方属于分析平台范围。')
                need(any(r['target']==e['id'] for r in rs),'bi-consumer-flow-missing',e['id'],'消费方需有显式出站供数流。')
            if not roles['edw']:continue
            edw=roles['edw'][0]
            if stage=='target' and roles['platform']:
                platform=roles['platform'][0]
                need(attrs(edw).get('covered_by_id')==platform['id'],'bi-target-edw-not-covered',edw['id'],'目标须覆盖EDW职责，不保留并列历史主库。')
                need(not any(edw['id'] in (r['source'],r['target']) for r in rs),'bi-target-independent-edw-flow',edw['id'],'被覆盖的数仓职责不能仍独立接收或发送数据。')
            elif stage in {'transition1','transition2'} and roles['platform']:
                platform=roles['platform'][0]
                need(not attrs(edw).get('covered_by_id'),'bi-premature-edw-absorption',edw['id'],'过渡期两个平台并存，不能提前吸收数仓。')
                need(bool(edges(edw['id'],platform['id'])),'bi-transition-edw-feed',stage,'过渡期数仓须向新平台提供数据。')
                if stage=='transition2':need(bool(edges(platform['id'],edw['id'])),'bi-transition-exchange-missing',stage,'第二过渡态需显式保留平台反哺数仓的交换。')
                need(any(edges(edw['id'],e['id']) and edges(platform['id'],e['id']) for e in roles['consumer']),'bi-dual-fed-consumer-missing',stage,'过渡图应能表达双平台供数消费方。')
    elif kind=='content-metamodel':
        domains={attrs(e).get('domain') for e in es}
        need(domains=={'general',*DOMAINS},'metamodel-domains-missing',profile['id'],'内容元模型应分通用、业务、数据、应用、技术五区。')
        concepts=[attrs(e).get('source_concept') for e in es]
        need(len(set(concepts))==len(concepts),'metamodel-concept-duplicate',profile['id'],'同一元模型类型不能重复为多个实例。')
        if profile.get('template',{}).get('full_source_concepts'):
            need(set(concepts)==set(profile['template']['full_source_concepts']),'metamodel-concepts-missing',profile['id'],'完整参考模式需覆盖声明的36种类型；企业实例应另选项目视图。')
        common={'principle','constraint','assumption','requirement','location','gap','work_package'}
        for e in es:
            a=attrs(e);c=a.get('source_concept','')
            need(a.get('model_kind')=='entity-type','metamodel-instance-confusion',e['id'],'此图元素是实体类型，不能把单一ABB实例当作完整内容元模型。')
            need(a.get('associated_with_all')==(c in common),'metamodel-universal-scope',e['id'],'通用7类可关联所有对象；Capability不属于该集合。')
            if c.startswith('logical_'):need(a.get('abstraction')=='logical','metamodel-abstraction-conflict',e['id'],'逻辑组件不能标为物理实现。')
            if c.startswith('physical_'):need(a.get('abstraction')=='physical','metamodel-abstraction-conflict',e['id'],'物理组件不能标为逻辑要求。')
        need(bool(rs),'metamodel-relations-missing',profile['id'],'类型清单必须带明确关系语义。')
        for r in rs:
            a=r.get('attributes',{})
            need(bool(a.get('forward_label')) and bool(a.get('inverse_label')),'metamodel-paired-labels',r['id'],'无箭头关联需声明正向与反向读法；来源未给出时应明确未知。')
            need(a.get('notation')=='unarrowed','metamodel-arrow-invention',r['id'],'原图无箭头，不能用线走向推断语义方向。')
    elif kind=='architecture-repository':
        containers={attrs(e).get('container_role'):e for e in es if e['type']=='repository_container'}
        partitions=[e for e in es if e['type']=='repository_partition']
        externals=[e for e in es if e['type']=='repository_external']
        need(set(containers)>= {'enterprise','architecture'},'repository-containment',profile['id'],'须显式区分企业库与其内的架构库。')
        roles={attrs(e).get('partition_role') for e in partitions}
        need(set(REPO_PARTITIONS)<=roles,'repository-partitions-missing',profile['id'],'架构库须含七分区加架构能力；全景只是分区之一。')
        need(len([e for e in partitions if attrs(e).get('partition_role')=='landscape'])==1,'repository-landscape-not-whole',profile['id'],'Architecture Landscape 不是整个存储库。')
        if 'architecture' in containers:
            arch=containers['architecture']['id']
            if 'enterprise' in containers:
                need(any(r['type']=='project:contains' for r in edges(containers['enterprise']['id'],arch)),
                     'repository-enterprise-link',arch,'企业库必须显式包含架构库。')
            for e in partitions:
                need(any(r['type']=='project:contains' for r in edges(arch,e['id'])),
                     'repository-partition-disconnected',e['id'],'分区的嵌套须由显式 contains 关系支撑。')
            for e in externals:
                need(not any(r['type']=='project:contains' and r['source']==arch and r['target']==e['id'] for r in rs),
                     'repository-external-inside',e['id'],'外部参考/标准/架构委员会在架构库外侧。')
        for e in es:
            if e['type']=='repository_asset':
                need(any(r['type']=='project:contains' and r['target']==e['id'] and byid[r['source']]['type']=='repository_partition' for r in rs),'repository-asset-disconnected',e['id'],'资产须由分区显式包含。')
        typed={r['type'] for r in rs}
        for rel in ('project:contains','project:governs','project:enables','project:adopts'):
            need(rel in typed,'repository-relation-missing',rel,'治理、使能、采纳与组成须为类型化关系，不能只靠相邻。')
        for e in externals:
            role=attrs(e).get('external_role')
            target='standards' if role=='standard' else 'reference' if role=='reference-model' else None
            if target:
                need(any(r['type']=='project:adopts' and r['source']==e['id'] and
                         attrs(byid[r['target']]).get('partition_role')==target for r in rs),
                     'repository-adoption-missing',e['id'],'外部材料须关联到对应标准库或参考库。')
    elif kind=='architecture-landscape':
        axes=[e for e in es if e['type']=='landscape_dimension']
        names={attrs(e).get('axis') for e in axes}
        need(names==set(LANDSCAPE_AXES),'landscape-axes-missing',profile['id'],'全景投影只有广度、抽象/细节、时间三轴。')
        need(not any(attrs(e).get('axis')=='recency' for e in axes),'landscape-fourth-axis',profile['id'],'时效性可作属性，不能伪造第四轴。')
        landscapes=[e for e in es if e['type']=='landscape_projection']
        slices=[e for e in es if e['type']=='landscape_slice']
        need(bool(landscapes),'landscape-volume-missing',profile['id'],'须有可投影的全景对象，不能把全景画成存储库。')
        need(not any(e['type']=='repository_container' for e in es),'landscape-not-repository',profile['id'],'fig3-2 是全景内的项目切片，不是第二个存储库。')
        if slices:
            for e in slices:
                a=attrs(e)
                need(all(a.get(k) for k in LANDSCAPE_AXES),'landscape-slice-bounds',e['id'],'项目切片须声明广度、抽象与时间范围。')
                need(any(r['type']=='project:contains' and r['source'] in {v['id'] for v in landscapes}
                         and r['target']==e['id'] for r in rs),'landscape-slice-outside',e['id'],'切片须显式位于全景内。')
                projected={r['source'] for r in rs if r['type']=='project:projects_to' and r['target']==e['id']}
                need(projected==landscape_members(es,e),'landscape-coordinate-mismatch',e['id'],'投影成员须与三轴坐标交集一致。')
    elif kind=='security-adm-map':
        phases={attrs(e).get('phase_code'):e for e in es if e['type']=='adm_phase'}
        need(set(phases)==set(ADM_PHASES),'security-adm-phases',profile['id'],'须覆盖 Preliminary 至 H 及需求管理，阶段 H 无概念组。')
        concepts=[e for e in es if e['type']=='security_risk_concept']
        keyed={attrs(e).get('concept_key',e['id'].removeprefix('c-')):e for e in concepts}
        tailoring=(view or {}).get('topology_tailoring',{})
        omitted=set(tailoring.get('omitted_concepts',[]))
        tailored=tailoring.get('mode')=='project'
        need(not tailored or bool(tailoring.get('reason')),'security-tailoring-reason',profile['id'],'企业裁剪须说明适用范围与理由。')
        expected=set(SECURITY_GROUPS)-omitted if tailored else set(SECURITY_GROUPS)
        need(set(keyed)==expected and len(keyed)==len(concepts),'security-adm-concept-count',profile['id'],'参考概念身份须齐；企业裁剪逐项列明省略项。')
        need(not omitted-set(SECURITY_GROUPS),'security-tailoring-unknown',profile['id'],'裁剪不能引用未知概念。')
        for key,e in keyed.items():
            allowed=SECURITY_GROUPS.get(key,set())
            actual={attrs(byid[r['source']]).get('phase_code') for r in rs
                    if r['type']=='project:associates' and r['target']==e['id']}
            need(actual==allowed,'security-adm-phase-association',e['id'],'阶段关联须符合来源概念组，P/A共享且RM关联业务属性和控制目标。')
            need(attrs(e).get('phase_code') in allowed,'security-adm-primary-phase',e['id'],'概念的主阶段与关联组不一致。')
            need(attrs(e).get('ism_erm_addition') is (key in SECURITY_ADDITIONS),
                 'security-adm-addition',e['id'],'ISM/ERM新增标记须与来源下划线一致。')
        for r in rs:
            if r['type']=='project:associates':
                need(r.get('attributes',{}).get('notation')=='unarrowed','security-adm-arrow',r['id'],'阶段与概念组是无方向关联。')
                src,tgt=byid[r['source']],byid[r['target']]
                phase=src if src['type']=='adm_phase' else tgt
                need(attrs(phase).get('phase_code')!='H','security-adm-phase-h-link',r['id'],'阶段 H 无概念组是原图语义，禁止补线。')
        need(any(e['type']=='ism_process' for e in es) and any(e['type']=='erm_process' for e in es),
             'security-adm-cycles',profile['id'],'须有 ISM/ERM 持续过程。')
        for e in es:
            if e['type'] in {'ism_process','erm_process'}:
                need(any(r['source']==e['id'] and r['target']==e['id'] and r['type']=='project:continues' for r in rs),
                     'security-adm-cycle-missing',e['id'],'ISM/ERM 须显式环形持续，不是一次活动。')
        additions=[e for e in concepts if attrs(e).get('ism_erm_addition')]
        need(bool(additions),'security-adm-underlined',profile['id'],'下划线概念须标记为 ISM/ERM 新增，可检查。')
    elif kind=='metadata-inference':
        sources={attrs(e).get('data_structure'):e for e in es if e['type']=='inference_source'}
        need(set(sources)=={'structured','semi-structured','unstructured'},'inference-sources-missing',profile['id'],'须区分结构化、半结构化、非结构化来源。')
        need(any(e['type']=='data_profiling' for e in es) and any(e['type']=='metadata_management' for e in es),
             'inference-actors-missing',profile['id'],'须有数据剖析与元数据管理，不只是来源卡片。')
        zones={attrs(e).get('zone'):e for e in es if e['type']=='metadata_zone'}
        need(set(zones)=={'METADATA','DATA'},'inference-zones-missing',profile['id'],'须保留 METADATA/DATA 分区。')
        uplinks=[r for r in rs if r['type']=='project:metadata_uplinks']
        need(bool(uplinks),'inference-uplink-missing',profile['id'],'剖析或结构化来源须有元数据上行。')
        for r in uplinks:
            src=byid[r['source']];role=src['type']
            structure=attrs(src).get('data_structure')
            need(role=='data_profiling' or structure=='structured','inference-illegal-uplink',r['id'],'仅剖析与结构化来源可跨 DATA→METADATA。')
            need(byid[r['target']]['type']=='metadata_management','inference-uplink-target',r['id'],'元数据上行须进入元数据管理。')
        profs=[e for e in es if e['type']=='data_profiling']
        managers=[e for e in es if e['type']=='metadata_management']
        for p in profs:
            for s in sources.values():
                need(any(r['type']=='project:profiling_reads' for r in edges(p['id'],s['id'])),
                     'inference-read-missing',s['id'],'三种来源须显式连接到读取剖析链。')
            need(any(r['type']=='project:metadata_uplinks' and r['source']==p['id'] and
                     r['target'] in {m['id'] for m in managers} for r in rs),
                 'inference-profile-uplink',p['id'],'剖析结果须上行元数据管理。')
        for a,b in [('unstructured','semi-structured'),('semi-structured','structured')]:
            if a in sources and b in sources:
                need(any(r['type']=='project:structure_lifts' for r in edges(sources[a]['id'],sources[b]['id'])),
                     'inference-lift-missing',a,'结构上推链不能被删除。')
        for s in sources.values():
            if attrs(s).get('data_structure')=='structured':
                need(any(r['type']=='project:metadata_uplinks' and r['source']==s['id'] and byid[r['target']]['type']=='metadata_management' for r in rs),'inference-structured-uplink',s['id'],'结构化来源的直接元数据上行链不可删除。')
        for r in rs:
            if r['type']=='project:structure_lifts':
                a,b=attrs(byid[r['source']]).get('data_structure'),attrs(byid[r['target']]).get('data_structure')
                need((a,b) in {('unstructured','semi-structured'),('semi-structured','structured')},
                     'inference-reverse-lift',r['id'],'结构上推不可反向。')
        for e in es:
            if e['type']=='inference_source' and attrs(e).get('data_structure')=='unstructured':
                if attrs(e).get('governance_claim')=='governed':
                    need(attrs(e).get('content_access') not in {None,'none','无需读取'},
                         'inference-unstructured-ungoverned',e['id'],'非结构化无内容访问却声称已治理。')
            if e['type'] in {'data_profiling','inference_source'} and (attrs(e).get('access_condition') or attrs(e).get('cost')):
                need(e.get('evidence'),'inference-restriction-evidence',e['id'],'访问条件与成本限制必须带来源，不靠渲染器发明。')
    elif kind=='ea-adm-matrix':
        for e in es:
            a=attrs(e)
            need(a.get('ADM_phase') in ADM_PHASES or set(a.get('phase_map',{}))==set(ADM_PHASES),'ea-adm-phase',e['id'],'映射阶段须为P/A-H/RM。')
            need(a.get('mapping_status','project-mapping') in {'project-mapping','unknown','no-relation','not-applicable'},'ea-adm-cell-status',e['id'],'未知、无关系与不适用须分别表达。')
    elif kind=='msa-execution':
        roles={e['id']:attrs(e).get('unit_kind') for e in es}
        pairs={'guide:uses_neutral_library':('source','library'),'guide:builds_deployment':('source','deployment'),'guide:deploys_instance':('deployment','execution')}
        for r in rs:
            if r['type'] in pairs:
                need((roles[r['source']],roles[r['target']])==pairs[r['type']],'msa-unit-direction',r['id'],'源码、共享库、构建包和实例的角色/方向不符。')
        for e in es:
            role=roles[e['id']];a=attrs(e)
            need(role in {'source','library','deployment','execution'},'msa-unit-kind',e['id'],'单元角色未定义。')
            if role=='library':need(not a.get('included_business_services') and a.get('service_id')=='business-neutral','msa-library-business-logic',e['id'],'共享库不能包含业务服务。')
            if role=='deployment':need(len(a.get('included_business_services',[]))==1,'msa-mixed-package',e['id'],'部署包只能包含一个微服务。')
            required='guide:builds_deployment' if role=='deployment' else 'guide:deploys_instance' if role=='execution' else None
            if required:need(any(r['target']==e['id'] and r['type']==required for r in rs),'msa-unit-disconnected',e['id'],'构建/部署追溯链不可删除。')
    elif kind=='msa-governance':
        required={'ops:governance_supports','ops:governance_aligns','ops:governance_extends','ops:governance_constrains'}
        need(required<={r['type'] for r in rs},'msa-governance-relations',profile['id'],'四种治理关系须显式表达。')
        from companion_profiles import ASPECTS
        need(any(set(attrs(e).get('process_aspects',{}))==set(ASPECTS) for e in es),'msa-governance-six-aspects',profile['id'],'须区分六个循环治理要素，四层治理不是图5-2六要素。')
        for e in es:
            need(bool(attrs(e).get('controls')) and bool(attrs(e).get('feedback')),'msa-governance-feedback',e['id'],'治理须有执行控制和持续反馈。')
    elif kind=='soa-layered':
        layers={attrs(e).get('layer'):e for e in es if e['type']=='soa_layer'}
        concerns={attrs(e).get('concern'):e for e in es if e['type']=='soa_concern'}
        need(set(layers)==set(SOA_LAYERS),'soa-layers-missing',profile['id'],'须有消费者接口到运营系统的五层。')
        need(set(concerns)==set(SOA_CONCERNS),'soa-concerns-missing',profile['id'],'须有 Integration/QoS/Information/Governance 四种跨层关注点。')
        order={name:i for i,name in enumerate(SOA_LAYERS)}
        for r in rs:
            if r['type']=='project:maps_to':
                a,b=attrs(byid[r['source']]),attrs(byid[r['target']])
                if a.get('layer') and b.get('layer'):
                    need(order[a['layer']]+1==order[b['layer']],'soa-layer-direction',r['id'],'层间映射须保持自上而下，不能跳层或反向充数。')
            if r['type']=='project:cross_cuts_soa':
                need(byid[r['source']]['type']=='soa_concern','soa-crosscut-source',r['id'],'跨层关注点横切各层，不是第五层。')
        for e in concerns.values():
            targets={r['target'] for r in rs if r['source']==e['id'] and r['type']=='project:cross_cuts_soa'}
            need(targets=={n['id'] for n in layers.values()},'soa-crosscut-incomplete',e['id'],'每一跨层关注点须覆盖五层。')
    return errors
