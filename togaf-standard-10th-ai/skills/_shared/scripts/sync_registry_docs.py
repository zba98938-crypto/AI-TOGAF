"""Publish reachable, relative-path contracts from the current registry.

Does not edit method-case narratives or change any verification status.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def dump(x):return json.dumps(x,ensure_ascii=False,indent=2)
def bullets(xs):return ''.join('- '+str(x)+'\n' for x in xs)
def section(title,body):return '\n## '+title+'\n\n'+body+'\n'
def save(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def main():
    cap=json.loads((ROOT/'capabilities.json').read_text());arts=json.loads((ROOT/'artifacts.json').read_text())['artifacts'];ds=json.loads((ROOT/'deliverables.json').read_text())['deliverables']
    rels=json.loads((ROOT/'relationships.json').read_text())['relationships']|json.loads((ROOT/'metamodel.json').read_text())['relationships']|cap.get('extension_relationship_definitions',{})
    for w in cap['work_products']:
        text='# '+w.get('name_zh',w.get('name',w['id']))+'\n\nID：`'+w['id']+'`。主责：['+w['owner']+'](../../../'+w['owner']+'/SKILL.md)。\n\n来源：'+'；'.join(w.get('source_refs',[]))+'。定义状态：`'+w.get('definition_status','未核实')+'`。字段与工具接口为项目操作约定，不自动成为官方强制规则。\n'
        text+=section('决策与受众',w['decision']+'\n\n'+bullets(w.get('stakeholders',[]))+bullets(w.get('concerns',[])))
        text+=section('输入及缺口处理','必需：\n\n'+bullets(w.get('required_inputs',[]))+'\n可选：\n\n'+bullets(w.get('optional_inputs',[]))+'\n'+w.get('missing_input_policy','缺输入列为未决，不默认通过。'))
        text+=section('元素、属性与关系','对象类型：'+', '.join(w['entity_types'])+'。\n\n```json\n'+dump(w.get('required_attributes',{}))+'\n```\n\n'+dump(w.get('attribute_semantics',{})))
        text+='\n| 关系 | 起点 → 终点 | 语义 |\n| --- | --- | --- |\n'
        for rid in w.get('relationship_types',[]):
            r=rels.get(rid,{});text+='| `'+rid+'` | '+','.join(r.get('source_types',[]))+' → '+','.join(r.get('target_types',[]))+' | '+r.get('meaning','见明确的项目扩展定义')+' |\n'
        text+=section('分析步骤','\n'.join(str(i)+'. '+s for i,s in enumerate(w['analysis_steps'],1)))
        text+=section('输出、检查与误读',bullets(w.get('output',[]))+'\n'+bullets(w.get('semantic_checks',w.get('checks',[])))+'\n'+bullets(w.get('misreadings',[])))
        profiles=[p for p in cap['profiles'] if p['artifact_id']==w['id']]
        text+=section('视图和交付物',bullets('['+p.get('name',p['id'])+'](../profiles/'+p['id']+'.md)' for p in profiles)+'\n'+bullets('['+d+'](../deliverables/'+d+'.md)' for d in w.get('related_deliverables',[])))
        addons=[]
        if (ROOT/'references/capability-addenda'/(w['id']+'.md')).exists():addons.append('[原料、分析、修改与反例能力包](../capability-addenda/'+w['id']+'.md)')
        if w.get('case_ref'):addons.append('[完整操作案例](../../'+w['case_ref']+')')
        text+=section('反例与修改示例','```json\n'+dump({'counterexample':w.get('counterexample'),'modification_example':w.get('modification_example')})+'\n```')
        text+=section('可编辑示例与调用','\n'.join(addons)+'\n\n以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。\n\n```json\n'+dump(w['example'])+'\n```\n\n```sh\npython "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact '+w['id']+' --layout adaptive --out output --render\n```\n\n单项请求只生成该选择；同族多视图用独立view_id。')
        save('references/capabilities/'+w['id']+'.md',text)
    for p in cap['profiles']:
        text='# '+p.get('name',p['id'])+'\n\n`profile_id`: '+p['id']+'；`artifact_id`: '+p['artifact_id']+'；主责：['+p['owner']+'](../../../'+p['owner']+'/SKILL.md)。\n\n来源：'+'；'.join(p.get('source_refs',[]))+'。\n'
        text+=section('构图与定义状态','表示族：`'+p.get('renderer','未确定')+'`；输出：`'+p.get('output_kind','diagram')+'`。规范版本：'+p.get('version','2.0')+'。\n\n'+dump(p.get('template',{}))+'\n\n来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。')
        text+=section('必需模型内容','对象类型：'+', '.join(p.get('entity_types',[]))+'。关系类型：'+', '.join(p.get('relationship_types',[]))+'。\n\n```json\n'+dump({'entities':p.get('required_attributes',{}),'relationships':p.get('required_relationship_attributes',{})})+'\n```\n\n缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。')
        text+=section('检查与追溯',bullets(p.get('checks',[]))+'\n每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。')
        text+=section('完整示例片段','```json\n'+dump(p['example'])+'\n```')
        text+=section('生成','```sh\npython "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile '+p['id']+' --layout reference --out output/reference --render\npython "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile '+p['id']+' --layout adaptive --out output/adaptive --render\n```\n\n用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。')
        save('references/profiles/'+p['id']+'.md',text)
    counts={'制品族':len(arts)+len(cap['work_products']),'指南工作产品':len(cap['work_products']),'视图模板':sum(not p.get('alias_of') for p in cap['profiles']),'分析方法':len(cap['analysis_methods']),'交付物':len(ds)}
    for method in cap['analysis_methods']:
        path=ROOT/'references/analysis-methods'/(method['id']+'.md')
        reference=method.get('reference_document') or method.get('method_reference')
        references=([reference] if reference else [])+method.get('reference_documents',[])
        if not path.exists() and references:
            for reference in references:
                if not (ROOT/reference).is_file():raise ValueError('方法文档不存在：'+reference)
            path.write_text('# '+method.get('name',method['id'])+'\n\n'+bullets('[完整方法、输入、分析、修改和反例](../'+str(Path(reference).relative_to('references'))+')' for reference in references)+'\n来源：'+'；'.join(method['source_refs'])+'。\n')
    text='# 能力与调用索引\n\n当前注册量：'+'；'.join(k+' '+str(v) for k,v in counts.items())+'。注册量不是通过验收量；状态与证据见逐项能力状态（历史材料已清理）。\n\n'
    for key,title,folder in [('work_products','指南工作产品','capabilities'),('profiles','视图模板','profiles'),('analysis_methods','分析方法','analysis-methods')]:
        text+=section(title,'| ID | 名称 | 主责 |\n| --- | --- | --- |\n'+''.join('| `'+i['id']+'` | ['+i.get('name_zh',i.get('name',i['id']))+']('+folder+'/'+i['id']+'.md) | '+i['owner']+' |\n' for i in cap[key]))
    text+='\n原制品与交付物：[兼容索引](coverage.md)。按 owner 或来源全文检索注册表，不依赖原工作区目录。\n';save('references/capability-index.md',text)
    save('references/view-profile-index.md','# 视图规范索引\n\n'+str(len(cap['profiles']))+'条注册规范；包含'+str(sum(p.get('registration_class')=='legacy-default' for p in cap['profiles']))+'条既有制品默认入口。\n\n| Profile | 制品族 | 构图 | 定义 |\n| --- | --- | --- | --- |\n'+''.join('| `'+p['id']+'` | `'+p['artifact_id']+'` | '+p.get('renderer','')+' | [规范](profiles/'+p['id']+'.md) |\n' for p in cap['profiles']))
    for owner in {p['owner'] for p in cap['profiles']}|{m['owner'] for m in cap['analysis_methods']}:
        text='# '+owner+' 按需能力包\n\n先根据实际决策问题选取规范，不强制生成全部清单。\n'
        for key,title,folder in [('work_products','工作产品','capabilities'),('profiles','视图','profiles'),('analysis_methods','分析方法','analysis-methods')]:
            text+=section(title,bullets('['+x.get('name_zh',x.get('name',x['id']))+']('+folder+'/'+x['id']+'.md)' for x in cap[key] if x['owner']==owner))
        save('references/'+owner+'-package.md',text)
        skill=ROOT.parent/owner/'SKILL.md';body=skill.read_text();link='../_shared/references/'+owner+'-package.md'
        if link not in body:skill.write_text(body+'\n按需入口：['+owner+' 能力包索引]('+link+')；只读取与本次任务相关的条目。\n')
    print(counts)
if __name__=='__main__':main()
