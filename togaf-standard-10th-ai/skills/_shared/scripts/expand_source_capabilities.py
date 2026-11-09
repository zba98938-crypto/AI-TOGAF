"""Reviewed November 2026 source corrections. Never infer a source-verification pass.

Maintenance reads the original local text; normal generation reads only the
portable tables written inside skills. This script is not a runtime dependency.
"""
import copy, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parents[1]
def read(name):return json.loads((ROOT/name).read_text())
def write(name,data):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def table(gid,title):
    path=next((WORK/'togaf-standard-10th-zh').glob(gid+'*.md'));lines=path.read_text().splitlines()
    start=next(i for i,l in enumerate(lines) if l.replace(' ','').startswith('**'+title+'：'))
    i=next(j for j in range(start+1,len(lines)) if lines[j].startswith('|'))
    header=[x.strip() for x in lines[i].strip('|').split('|')];i+=2;rows=[]
    while i<len(lines) and lines[i].startswith('|'):
        rows.append({'line':i+1,'values':[x.strip() for x in lines[i].strip('|').split('|')]});i+=1
    return {'source':gid,'table':title,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'header':header,'rows':rows,'definition_status':'local-translation-read; official-definition-not-independently-verified'}
def entity(id,typ,name,attrs):return {'id':id,'type':typ,'name':name,'attributes':attrs,'evidence':['case-source'],'certainty':'assumed'}
def edge(id,typ,source,target,label,attrs=None):
    r={'id':id,'type':typ,'source':source,'target':target,'label':label,'evidence':['case-source'],'certainty':'assumed'}
    if attrs:r['attributes']=attrs
    return r
def example(pid,aid,name,entities,relations,analysis):
    return {'notice':'虚构业务案例；采用来源结构及术语，不代表真实实施或批准。','sources':[{'id':'case-source','kind':'example','description':'虚构社区服务机构的访谈、记录和项目约定'}],
        'entities':entities,'relationships':relations,'view':{'id':'v-'+pid,'artifact_id':aid,'profile_id':pid,'title':name,'entity_ids':[e['id'] for e in entities],'relationship_ids':[r['id'] for r in relations],'analysis':analysis,'legend':'同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。'}}
def profile(pid,aid,name,owner,refs,renderer,types,rels,required,ex,template=None,kind='diagram'):
    return {'id':pid,'artifact_id':aid,'name':name,'name_zh':name,'owner':owner,'version':'2.2','source_refs':refs,
        'renderer':renderer,'output_kind':kind,'entity_types':types,'relationship_types':rels,'required_attributes':required,
        'checks':['对象、关系、必要属性均可追溯并得到表达','参考内容不自动成为项目事实；未知项保持显式'],
        'definition_status':'source-derived-project-operational-contract','template':{'id':pid,'version':'2.2','source_verified':False,'layout_notes':'按已核查的来源结构参数化；参考图与业务实例的验收分别进行。',**(template or {})},'example':ex}
def product(id,name,owner,refs,typ,fields,decision,steps,checks,ex,deliverables):
    return {'id':id,'artifact_id':id,'name':name,'name_zh':name,'name_en':id,'owner':owner,'kind':'catalog','renderer':'catalog','notation':'table',
        'source_refs':refs,'definition_status':'guide-work-product-with-project-operational-contract','decision':decision,
        'stakeholders':['该范围业务负责人','架构师','评审及运营负责人'],'concerns':[decision,'来源、范围与适用性'],
        'required_inputs':['原始业务材料和来源','范围、状态和决策问题']+fields,'optional_inputs':['既有模型及历史结论'],
        'missing_input_policy':'缺少来源、责任、结果或决定时列缺口，不默认通过；未核实资料不能支撑批准。',
        'entity_types':[typ],'relationship_types':[],'fields':['name']+fields,'required_attributes':{typ:fields},
        'attribute_semantics':{k:{'meaning':k,'value_rule':'从来源或明确的项目约定记录，保留未知和不适用理由','definition_origin':'project-operational-convention'} for k in fields},
        'analysis':steps,'analysis_steps':steps,'checks':checks,'semantic_checks':checks,'misreadings':['名称、来源表格和成功输出不等于业务结论已核实']+checks,
        'output':['范围及依据','逐条结果与理由','缺口、下一步与责任','版本和来源引用'],'related_deliverables':deliverables,'example':ex,
        'implementation_status':{'definition':'source-located','model':'requires-validation','analysis':'case-specified','generation':'requires-execution','modification':'requires-execution','review':'requires-execution','visual':'not-applicable-table'}}

def main():
    cap=read('capabilities.json');meta=read('metamodel.json');ps={p['id']:p for p in cap['profiles']};ws={w['id']:w for w in cap['work_products']}
    # Correct locators, without laundering any definition status.
    correction={'customer-journey':['G20F §5.2.1、§5.3.1、§5.5'],'customer-persona':['G20F §5.5'],
      'interoperability-assessment':['G217 §4.4.4、附录C.4表C-5'],
      'mdm-integration-style':['G21B §6.1.1'],'mdm-exchange-pattern':['G21B §6.1.2'],
      'mdm-identity-analysis':['G21B 附录A.2'],
      'architecture-skill-matrix':['G249 §5表5-1、5-2','G198 §4.4、§5表5-1至5-7（已被G249取代）']}
    for aid,refs in correction.items():
        if aid in ws:ws[aid]['source_refs']=refs
        for p in ps.values():
            if p['artifact_id']==aid and p['id']==aid+'-default':p['source_refs']=refs
    # Portable reference tables: roles/levels remain versioned, never merged by name.
    skilltables=[table('G198','表4-1')]+[table('G198','表5-'+str(i)) for i in range(1,8)]+[table('G249','表5-1'),table('G249','表5-2')]
    write('references/source-tables/architecture-skills.json',{'notice':'历史参考矩阵，岗位需裁剪；总分/均值不作为合格线。','tables':skilltables})
    checks=[table('G248','表9-1'),table('G248','表11-1')]
    rows=[]
    for t in checks:
        for index,row in enumerate(t['rows'],1):
            step,phase,question,rapid,functional,robust,_=row['values']
            rows.append({'id':('planning' if t['table']=='表9-1' else 'implementation')+'-'+str(index).zfill(2),
              'step':int(step),'phase':phase,'question':question,'profiles':[p for p,v in [('rapid',rapid),('functional',functional),('robust',robust)] if v=='Y'],
              'source':'G248 '+t['table']+' L'+str(row['line'])})
    write('references/source-tables/change-profile-checks.json',{'notice':'Y表示源指南建议纳入，空白不是通过、不适用或禁止纳入；项目裁剪须记录理由。','rows':rows,'tables':checks})
    aid='change-profile-governance-checklist';owner='togaf-implementation-governance';typ='guide:governance-check'
    fields=['source_check_id','step','adm_phase','change_profile','applicability','response','evidence_locator','owner','action','transition_id']
    new=[]
    for group in ['planning','implementation']:
        pid='change-profile-'+group+'-checklist';entities=[]
        for row in [r for r in rows if r['id'].startswith(group)]:
            applicable='functional' in row['profiles']
            # Complete working example includes an explicit outcome for every row.
            # A pending row demonstrates honest evidence gaps; it is not a passed case.
            outcome='待证据' if applicable else '源指南未建议纳入，项目保留待裁剪'
            if row['id'] in ['planning-01','planning-06','implementation-03']:
                outcome='符合示例判据'
            attrs={'source_check_id':row['id'],'step':row['step'],'adm_phase':row['phase'],'change_profile':'functional','applicability':'纳入' if applicable else '待裁剪','response':outcome,
              'evidence_locator':{'planning-01':'虚构访谈INT-01：居民需线下/线上统一预约','planning-06':'项目规则KPI-01：预约冲突次数按周观察，目标由负责人另定','implementation-03':'虚构演练DEP-01：预约组件在过渡A环境运行'}.get(row['id'],'未提供对应证据'),
              'owner':'社区服务项目负责人','action':'核实结果证据并决定通过/返工/豁免；不自动批准','transition_id':'community-transition-a'}
            entities.append(entity('check-'+row['id'],typ,row['question'],attrs))
        ex=example(pid,aid,'变革画像'+('规划' if group=='planning' else '实施')+'检查',entities,[],
          '原料：社区服务预约上线采用Functional画像，只有访谈、KPI草案和部署演练记录。先按源表筛建议项，再逐项核对证据。可支持的三项仍只为示例，其他项保持待证据/待裁剪；不能据此批准上线。')
        new.append(profile(pid,aid,ex['view']['title'],owner,['G248 §9表9-1','G248 §11表11-1'],'catalog',[typ],[],{typ:fields},ex,kind='table'))
    ws[aid]=product(aid,'变革画像治理检查清单',owner,['G248 §3、§9表9-1、§11表11-1'],typ,fields,
        '按Rapid/Functional/Robust及具体过渡，哪些规格、实施和价值条件已有证据，哪些需要返工或裁剪？',
        ['识别变革范围、画像及具体过渡；保留选择理由','载入完整源表并记录项目纳入/排除决定','逐项核对证据，区分规格可实现性与实际实施效果','记录未决、负责人、措施及治理决定，变更后重审受影响项'],
        ['源表空格不代表通过','排除建议项需要明确裁剪理由','通过需要证据，已部署不证明价值已实现','安全X是源表标签，不是新增ADM阶段'],new[0]['example'],['compliance-assessment','architecture-contract','implementation-migration-plan'])
    for p in new:ps[p['id']]=p
    cap.setdefault('default_profiles',{})[aid]=new[0]['id']
    # Distinct information relations from G190 Appendix A.1, modeled as project vocabulary.
    meta['entity_types']['information_meaning']={'meaning':'某利益相关者在明确语境中对信息概念的解释，不替代概念自身'}
    for rel,src,tgt,meaning in [
        ('makes_explicit',['business_object'],['information'],'业务对象使信息概念显性化；不是存储或生成关系'),
        ('is_about',['information'],['business_object'],'信息概念作为元数据描述业务对象；不是组成关系'),
        ('interprets_information',['information_meaning'],['information'],'具名语境和利益相关者对信息的解释'),
        ('organization_value_exchange',['organization'],['organization'],'从交付方向接收方交付具体价值项；不自动逆推对价'),
        ('organization_information_exchange',['organization'],['organization'],'工作网络中的定向信息传递，需信息概念与派生证据')]:
        meta['relationships'][rel]={'source_types':src,'target_types':tgt,'meaning':meaning,'definition_origin':'project-vocabulary-guided-by-G190-A.1-or-G206-5'}
    pid='information-concept-object-meaning';aid='information-map'
    entities=[entity('customer-info','information','服务对象信息',{'definition':'用于理解居民服务需求的信息概念'}),
      entity('customer-record','business_object','服务对象记录',{'definition':'把服务对象信息显性记录的业务对象类型'}),
      entity('customer-person','business_object','服务对象',{'definition':'接受社区服务的居民主体类型'}),
      entity('meaning-ops','information_meaning','运营解释',{'stakeholder':'服务运营','context':'排班预约','interpretation':'按实际到场的人识别服务对象'}),
      entity('meaning-finance','information_meaning','财务解释',{'stakeholder':'结算管理','context':'补贴结算','interpretation':'按资格申请主体识别，可能与实际到场者不同'})]
    relations=[edge('record-explicit','makes_explicit','customer-record','customer-info','记录使服务对象信息显性化'),edge('info-about','is_about','customer-info','customer-person','信息关于服务对象'),edge('ops-meaning','interprets_information','meaning-ops','customer-info','运营解释：到场主体'),edge('finance-meaning','interprets_information','meaning-finance','customer-info','财务解释：申请主体')]
    ex=example(pid,aid,'信息概念、业务对象与解释语境',entities,relations,'原料：预约以到场人为单位，补贴以申请主体为单位。归一为同一信息主题并保留两个利益相关者解释；记录、主体、信息不能合并成一个同名节点。')
    ps[pid]=profile(pid,aid,ex['view']['title'],'togaf-information-data',['G190 §2、附录A.1'],'network',['information','business_object','information_meaning'],[r['type'] for r in relations],{'information':['definition'],'business_object':['definition'],'information_meaning':['stakeholder','context','interpretation']},ex)
    # Typed organization exchange in the existing network; preserve its identity.
    p=ps['organization-work-network'];p['relationship_types']=['collaborates_with','organization_value_exchange','organization_information_exchange'];p['version']='2.2'
    es=p['example']['entities'];prefix='organization-work-network-'
    es[0]['attributes']['boundary']='选定企业生态范围，不表示法律母公司或汇报上级'
    es[0]['attributes']['definition']='在线销售与履约的共同业务语境'
    rels=[edge(prefix+'works','collaborates_with',prefix+'ops',prefix+'carrier','共同处理履约例外；不是汇报'),
      edge(prefix+'info','organization_information_exchange',prefix+'ops',prefix+'carrier','订单交接信息：由订单处理能力使用订单概念推导',{'information_ref':'订单概念','derivation_path':'运营组织→订单处理能力→订单信息','condition':'确认订单后'}),
      edge(prefix+'value','organization_value_exchange',prefix+'carrier',prefix+'ops','履约服务：按委托完成交付',{'value_item':'配送履约服务','condition':'合同服务范围内；不推断付款方向'})]
    for e in es:e['evidence']=['case-source']
    p['example']=example(p['id'],p['artifact_id'],p['name'],es,rels,'识别运营与合作方的工作职责，从能力和信息使用关系推导订单交接；价值交付单独记录，不能从相邻布局推断汇报。')
    from repair_organization_example import repair
    repair(ps['organization-work-network'])
    cap['profiles']=list(ps.values());cap['work_products']=list(ws.values())
    write('capabilities.json',cap);write('metamodel.json',meta)
    print(json.dumps({'work_products':len(ws),'profiles':len(ps),'change_profile_source_checks':len(rows)},ensure_ascii=False))

if __name__=='__main__':main()
