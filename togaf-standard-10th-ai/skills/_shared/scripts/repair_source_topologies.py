"""Author five complete source-topology fixtures; rerun only in the source workspace."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]

def entity(identity,typ,name,**attrs):
    return {'id':identity,'type':typ,'name':name,'attributes':attrs,'evidence':['example-source'],'certainty':'assumed'}
def edge(identity,source,target,typ,label,**attrs):
    return {'id':identity,'source':source,'target':target,'type':typ,'label':label,'attributes':attrs,'evidence':['example-source'],'certainty':'assumed'}

def build(profile,kind,entities,relations,extensions,refs):
    p=copy.deepcopy(profile);p['version']='2.3';p['renderer']='network' if kind=='content-metamodel' else 'deployment'
    p['template'].update({'source_topology':kind,'source_verified':False,'review_status':'source-topology-repaired-awaiting-independent-review','version':'2.3'})
    p['template'].pop('verification_evidence',None);p['source_refs']=refs;p['source_structure_refs']=['references/source-structures/'+r.replace('/','-')+'.json' for r in refs]
    p['entity_types']=sorted({e['type'] for e in entities});p['relationship_types']=sorted({r['type'] for r in relations})
    p['required_attributes']={'*':['definition']};p['required_relationship_attributes']={'*':['meaning']}
    for r in relations:r['attributes'].setdefault('meaning',r['label'])
    p['example']={'notice':'来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。',
        'sources':[{'id':'example-source','kind':'example','description':'专用拓扑验收示例：'+', '.join(refs)+'；来源图解释与候选企业场景分开。'}],
        'entities':entities,'relationships':relations,'extensions':extensions,
        'view':{'id':'v-'+p['id'],'artifact_id':p['artifact_id'],'profile_id':p['id'],'title':p['name']+'／来源结构专用示例',
        'entity_ids':[e['id'] for e in entities],'relationship_ids':[r['id'] for r in relations],
        'analysis':'明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。',
        'legend':'虚构候选或来源解释；相同ID表示同一对象。按专用线型、区域与编号语义读取；工程生成不授予来源等价或业务验收。'}}
    return p

def mdm(p):
    es=[];rs=[];typ='project:master_data_transfer'
    for short,pattern,label in [('con','consolidation','整合'),('coo','cooperation','协作'),('cen','centralized','集中')]:
        center=short+'-mdm';authority={'consolidation':'external-master','cooperation':'central-canonical','centralized':'central-master'}[pattern]
        es.append(entity(center,'master_repository',label+'式 MDM',definition={'consolidation':'整合来源副本，供分析使用','cooperation':'整合并形成规范客户版本','centralized':'唯一主数据存储与创建维护入口'}[pattern],integration_style=pattern,topology_role='central',authority=authority,scope='客户主数据',style=label,collaboration='项目候选职责；需所有者确认'))
        for n,name in enumerate(['客户服务系统','销售系统','账务系统'],1):
            identity=short+'-sys'+str(n);es.append(entity(identity,'application',name,definition='客户主记录的运营来源' if pattern!='centralized' else '消费MDM主记录，不保有独立主控权',integration_style=pattern,topology_role='peripheral',authority='consumer-only' if pattern=='centralized' else 'operational-master',scope='客户主数据'))
            if pattern!='centralized':rs.append(edge(short+'-in'+str(n),identity,center,typ,'源系统提交客户更新',flow_role='source-update',data_scope='客户主数据'))
            if pattern!='consolidation':rs.append(edge(short+'-out'+str(n),center,identity,typ,'MDM分发规范客户版本',flow_role='canonical-distribution',data_scope='客户主数据'))
    return build(p,'mdm-integration',es,rs,{'relationship_types':{typ:{'source_types':['master_repository','application'],'target_types':['master_repository','application'],'meaning':'项目明确的客户主数据传输；箭头指向接收方，不自动表示主控权或同步一致性。'}}},['G21B/fig6-1'])

def metadata(p):
    es=[];rs=[];typ='project:metadata_exchange'
    domains=[('glossary','词汇表、政策与质量'),('processes','业务流程'),('application','应用存储库'),('technical','技术与运营元数据'),('privacy','数据隐私'),('risk','风险管理'),('security','安全管理'),('reference','参考数据'),('governance','数据治理')]
    for short,pattern,label in [('con','consolidation','集中'),('hyb','hybrid','混合'),('uni','unified','统一')]:
        center=short+'-central';authority,workflow={'consolidation':('copy-only','external'),'hybrid':('selected-scopes','mixed'),'unified':('all-scopes','central')}[pattern]
        es.append(entity(center,'metadata_repository',label+'式中央库',definition={'consolidation':'统一访问副本；不迁移源方维护流程','hybrid':'选定域主记录及工作流迁入中央','unified':'全范围主记录与维护工作流统一'}[pattern],integration_style=pattern,topology_role='central',authority=authority,workflow_owner=workflow,scope='九个元数据域社区'))
        for key,name in domains:
            identity=short+'-'+key;central=key=='governance' or pattern=='unified' or (pattern=='hybrid' and key in {'glossary','processes','reference'})
            location='none' if key=='governance' else 'central' if central else 'external'
            es.append(entity(identity,'metadata_component',name+'社区',definition='治理监督，不是独立存储库' if key=='governance' else '直接在中央维护本域元数据' if central else '外部保留本域主记录与维护流程',integration_style=pattern,topology_role='community',domain_key=key,repository_location=location,authority='governance' if key=='governance' else 'central-master' if central else 'external-master'))
            rs.append(edge(short+'-'+key+'-in',identity,center,typ,'治理输入' if key=='governance' else '中央直接维护' if central else '来源向中央供副本',flow_role='governance' if key=='governance' else 'write' if central else 'copy',data_scope=key))
            if central and not(pattern=='unified' and key=='security'):
                rs.append(edge(short+'-'+key+'-out',center,identity,typ,'治理反馈' if key=='governance' else '社区读取中央元数据',flow_role='governance' if key=='governance' else 'read',data_scope=key))
    return build(p,'metadata-integration',es,rs,{'relationship_types':{typ:{'source_types':['metadata_repository','metadata_component'],'target_types':['metadata_repository','metadata_component'],'meaning':'指定元数据范围的供副本、读写或治理交换；关系角色在flow_role中明示。'}}},['G234/fig4-6','G234/fig4-7','G234/fig4-8'])

def security(p):
    es=[entity('security-concern','security_component','安全、隐私与运营风险',definition='同一组跨域安全关注点',concern='授权、机密性、完整性、可用性',principle='最小权限与可追溯职责',risk='未授权操作与履约中断',scope='业务、数据、应用和技术')];rs=[];typ='project:cross_cuts'
    for domain,name,definition,concern in [('business','业务域','交易职责与履约规则','职责分离与授权审批'),('data','数据域','客户、订单及生产数据','分类、保留与用途限制'),('application','应用域','应用与接口实现','身份、访问控制与审计'),('technology','技术域','运行平台与基础设施','网络隔离、恢复与监控')]:
        es.append(entity('domain-'+domain,'guide:architecture_domain',name,definition=definition,architecture_domain=domain))
        rs.append(edge('cross-'+domain,'security-concern','domain-'+domain,typ,concern,domain=domain))
    return build(p,'security-crosscut',es,rs,{'entity_types':{'guide:architecture_domain':'指南中的架构域类别，不是企业组织或部署容器'},'relationship_types':{typ:{'source_types':['security_component'],'target_types':['guide:architecture_domain'],'meaning':'关注点横切指定架构域；覆盖关系，不表示流程、包含或数据流。'}}},['G152/fig4-1'])

def bi(p):
    es=[];rs=[];typ='project:analytics_flow'
    names={'tx1':'事务应用1','tx2':'事务应用2','tx3':'含嵌入BI的事务应用','ext':'设备、开放数据与日志','edw':'企业数据仓库 EDW','ng':'新一代分析平台','dm1':'数据集市1','dm2':'数据集市2','app1':'既有应用1','dm3':'新数据集市3','app2':'新分析应用2','app3':'新分析应用3'}
    for short,stage in [('b','baseline'),('t1','transition1'),('t2','transition2'),('t','target')]:
        keys=['tx1','tx2','tx3','edw','dm1','dm2','app1']+([] if stage=='baseline' else ['ext','ng','dm3','app2','app3'])
        for key in keys:
            role='transaction' if key.startswith('tx') else 'external' if key=='ext' else 'edw' if key=='edw' else 'platform' if key=='ng' else 'consumer'
            storage='RDBMS' if key not in {'ext','ng','app2','app3'} else 'RDBMS / NoSQL' if key.startswith('app') else '源方存储' if key=='ext' else '清洗数据副本' if stage=='transition1' else '原始、集成与加工数据'
            if key=='tx3':storage='RDBMS / Other'
            if stage=='transition1' and key=='app2':storage='RDBMS'
            if stage=='target' and key=='app1':storage='Other'
            if stage=='target' and key=='dm3':storage='RDBMS / NoSQL'
            definition='事务数据供数' if role=='transaction' else '新增数据源' if role=='external' else '分析或应用消费' if role=='consumer' else '历史关系数据' if role=='edw' and stage!='target' else '数仓范围与职责被覆盖' if role=='edw' else '新增分析能力与历史数据存储'
            a=dict(definition=definition,stage=stage,component_role=role,boundary='outside' if role in {'transaction','external'} else 'inside',storage=storage,asset_status='new' if key in {'ng','ext','dm3','app2','app3'} else 'existing',role=role,inbound='见显式入站关系',outbound='见显式出站关系',coexistence='并行运营，独立维护' if stage in {'transition1','transition2'} else '唯一现有历史库' if stage=='baseline' else '统一历史职责，退役须独立验收')
            if stage=='target' and key=='edw':a['covered_by_id']=short+'-ng'
            if stage in {'transition2','target'} and key=='app1':a['asset_status']='modified'
            es.append(entity(short+'-'+key,'analytics_component',names[key],**a))
        def flow(a,b,role,change='new'):
            rs.append(edge(short+'-'+a+'-'+b,short+'-'+a,short+'-'+b,typ,'入站摄取／应用回写' if role=='inbound' else '出站数据供给',flow_role=role,change_status=change))
            if stage=='transition2' and a in {'tx2','tx3'} and b=='edw':
                rs[-1]['attributes']['source_notation_note']='G238 fig3-3将这两条保留摄取线画为实线；此解释性视图按入站虚线图例统一，差异明确保留，不宣称逐线同形。'
        if stage=='baseline':
            for key in ['tx1','tx2','tx3']:flow(key,'edw','inbound','existing')
            for key in ['dm1','dm2','app1']:flow('edw',key,'outbound','existing')
        elif stage=='transition1':
            for key in ['tx1','tx2','tx3']:flow(key,'edw','inbound','existing')
            for key in ['dm1','dm2','app1']:flow('edw',key,'outbound','existing')
            flow('edw','ng','outbound');flow('edw','dm3','outbound');flow('ext','ng','inbound')
            for key in ['dm3','app2','app3']:flow('ng',key,'outbound')
            flow('app3','ng','inbound')
        elif stage=='transition2':
            for key in ['tx2','tx3']:flow(key,'edw','inbound','existing')
            for key in ['tx1','tx2','tx3','ext']:flow(key,'ng','inbound')
            for key in ['dm1','dm2']:flow('edw',key,'outbound','existing')
            flow('edw','app1','outbound');flow('edw','ng','outbound');flow('ng','edw','outbound')
            for key in ['app1','dm3','app2','app3']:flow('ng',key,'outbound')
            for key in ['app2','app3']:flow(key,'ng','inbound')
        else:
            for key in ['tx1','tx2','tx3','ext']:flow(key,'ng','inbound')
            for key in ['dm1','dm2','app1','dm3','app2','app3']:flow('ng',key,'outbound','existing' if key in ['dm1','dm2','app1'] else 'new')
            for key in ['dm3','app2','app3']:flow(key,'ng','inbound')
    return build(p,'bi-evolution',es,rs,{'relationship_types':{typ:{'source_types':['analytics_component'],'target_types':['analytics_component'],'meaning':'指定运营状态中的分析数据传输，箭头指向接收者。入站、出站、回写和变更状态显式声明。'}}},['G238/fig3-1','G238/fig3-2','G238/fig3-3','G238/fig3-4'])

def content(p):
    source=json.loads((PROJECT/'togaf-standard-10th-zh/figs/ai/G248/fig3-1.json').read_text());es=[];rs=[];typ='guide:metamodel_relation'
    elements=[e for e in source['elements'] if e['type']!='group'];common={'principle','constraint','assumption','requirement','location','gap','work_package'}
    for e in elements:
        c=e['id'];parent=e.get('parent');domain='general' if parent in {'all_objects_group','general_group'} else parent.removesuffix('_group')
        abstraction='logical' if c.startswith('logical_') else 'physical' if c.startswith('physical_') else 'type'
        es.append(entity(c,'guide:metamodel_entity',e['label_zh']+' / '+e['label_en'],definition='实体类型：'+e['label_zh'],source_concept=c,domain=domain,abstraction=abstraction,model_kind='entity-type',associated_with_all=c in common))
    ids={e['id'] for e in es}
    for r in source['relationships']:
        if r.get('from') not in ids or r.get('to') not in ids:continue
        pair=r.get('label_en','').split(' / ',1);forward=pair[0];inverse=pair[1] if len(pair)>1 else '来源未单列反向标签（不推断）'
        rs.append(edge(r['id'],r['from'],r['to'],typ,r.get('label_zh',r['label_en']),forward_label=forward,inverse_label=inverse,notation='unarrowed',interpretation_status='endpoint-inferred-awaiting-review' if '推断' in r.get('description_zh','') else 'source-label-interpreted',source_relation_kind=r['type']))
    result=build(p,'content-metamodel',es,rs,{'entity_types':{'guide:metamodel_entity':'来源元模型的实体类型，非企业实例；原类型名称保存在source_concept'},'relationship_types':{typ:{'source_types':['guide:metamodel_entity'],'target_types':['guide:metamodel_entity'],'meaning':'无箭头的来源元模型关联；正反读法与解释状态显式保留，不将几何方向当作业务方向。'}}},['G248/fig3-1'])
    result['template']['full_source_concepts']=sorted(ids);result['required_relationship_attributes']={'*':['meaning','forward_label','inverse_label','notation']}
    return result

def main():
    path=ROOT/'capabilities.json';registry=json.loads(path.read_text());builders={'mdm-consolidation-collaboration-central':mdm,'metadata-central-hybrid-unified':metadata,'security-cross-domain':security,'bi-baseline-transition-target':bi,'building-block-content-model':content};updated={}
    for p in registry['profiles']:
        if p['id'] in builders:updated[p['id']]=builders[p['id']](p)
    # Re-read immediately before the narrow profile replacement to preserve other agents' changes.
    current=json.loads(path.read_text());current['profiles']=[updated.get(p['id'],p) for p in current['profiles']];path.write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:{'entities':len(v['example']['entities']),'relationships':len(v['example']['relationships'])} for k,v in updated.items()}))

if __name__=='__main__':main()
