"""Graphic projections of existing EA/MSA records; table IDs remain stable."""
import copy

SPECS=[('ea-service-adm-evidence-map','ea-service-adm-matrix','ea-adm-matrix','G217/figC-1'),
       ('msa-federated-governance-process','msa-federated-governance-diagram','msa-governance','G21I/fig5-2'),
       ('msa-source-deployment-execution','msa-source-deployment-diagram','msa-execution','G21I/fig9-1')]

def build(cap):
    profiles={p['id']:p for p in cap['profiles']};result=[]
    for base,identity,kind,figure in SPECS:
        p=copy.deepcopy(profiles[base]);
        if base=='msa-federated-governance-process':enrich_governance(p)
        p.update(id=identity,renderer='deployment',output_kind='diagram',version='2.4',notation='source-topology')
        p['name']=p['name_zh']=profiles[base]['name']+'／图形'
        p['source_refs']=list(dict.fromkeys(p['source_refs']+[figure]))
        p['template']={'id':identity,'version':'2.4','source_verified':False,'source_topology':kind,
                       'separate_detail_ledger':True,'review_status':'awaiting-source-and-business-review',
                       'companion_table_profile_id':base}
        p['example']['view'].update(id='v-'+identity,profile_id=identity,title=p['name'])
        p['example']['view']['legend']='图形与表格复用同一ID；未知不等于无关系或不适用；项目映射不是原图逐格验收。'
        result.append(p)
    return result + reference_matrix_profiles()

ASPECTS={'principles':'指导原则','governing':'治理流程','governed':'受治理的MSA流程','artifacts':'制品','roles':'角色与职责','technology':'技术'}

def enrich_governance(profile):
    for e in profile['example']['entities']:
        if e['id']=='GOV-MSA':
            e['attributes']['process_aspects']={
             'principles':'保持自治边界，豁免须由EA委员会决定；EX-1待决',
             'governing':'每次发布前四眼复核，监测偏离并纠偏',
             'governed':'预约服务的设计、构建、测试、发布和运行流程',
             'artifacts':'候选契约、EX-1申请、测试及监控回执；真实签署缺失',
             'roles':'项目/领域架构师、开发运维执行；架构委员会审定豁免',
             'technology':'受控管道、最小权限、自动测试、运行监控'}
    return profile

def reference_matrix_profiles():
    import json
    from specialized_view_profiles import ROOT,entity,profile
    d=json.loads((ROOT/'references/source-structures/G217-figC-1.json').read_text())
    elements=[e for e in d['elements'] if e['type'] in {'group','service'}]
    rows=d['tables'][0]['rows'];phases=['P','A','B','C','D','E','F','G','H','RM'];es=[]
    for e,row in zip(elements,rows):
        es.append(entity(e['id'],'guide:ea_adm_mapping',e.get('label_zh') or e['label_en'],definition=e['label_en'],service=e['label_en'],column_kind='category' if e['type']=='group' else 'service',phase_map={phase:'source-mapped' if cell else 'source-unmarked' for phase,cell in zip(phases,row[1:])},mapping_origin='local-source-transcription; not business facts'))
    p=profile('ea-service-adm-reference-matrix','ea-service-catalog','EA服务×ADM来源参考矩阵','togaf-ea-capability',['G217/figC-1'],'ea-adm-matrix',es,[],{},['24列=6分类+18服务；10阶段。空白是来源未标注，不表示禁止。','开发支持分类G格按来源转录但语义存疑，需原文专业复核。'])
    p['example']['view']['legend']='来源解释参考；24列/10行的转置表达。开发支持分类G格为不确定项，不能据此推断该分类所有服务适用。'
    q=copy.deepcopy(p);q.update(id='ea-service-adm-reference-table',renderer='assessment',output_kind='table');q['example']['view'].update(id='v-'+q['id'],profile_id=q['id']);q['columns']=['name','definition','service','column_kind','phase_map','mapping_origin'];q['template']['columns']=q['columns'];q['template'].pop('source_topology',None)
    return [p,q]
