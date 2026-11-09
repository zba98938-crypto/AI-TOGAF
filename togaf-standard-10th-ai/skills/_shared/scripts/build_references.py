# -*- coding: utf-8 -*-
"""Build navigable references from reviewed contracts and generated case model."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    arts=json.loads((ROOT/'artifacts.json').read_text())['artifacts'];ds=json.loads((ROOT/'deliverables.json').read_text())['deliverables']
    model=json.loads((ROOT/'tests/retail-example.json').read_text());views={v['artifact_id']:v for v in model['views']};delivs={d['deliverable_id']:d for d in model['deliverables']}
    registry=json.loads((ROOT/'relationships.json').read_text())['relationships'];names={a['id']:a['name_zh'] for a in arts}
    stakeholder={'ea-capability':'架构负责人、业务发起方、方法维护方','vision-scenarios':'发起方、受影响利益相关者、项目和架构负责人','strategy-capabilities':'战略及投资决策方、能力负责人','value-streams':'价值流负责人、触发方代表、跨职能能力负责人','organization-roles':'组织及人力负责人、业务责任方、合作伙伴','business-models-processes':'业务及流程负责人、服务消费者、执行与控制角色','information-data':'业务信息和数据负责人、数据及应用架构师','application-architecture':'应用和业务功能负责人、集成及数据团队','technology-architecture':'平台、运维、安全及标准负责人','security-risk':'业务风险责任方、数据责任方、控制验证方','gap-solutions':'架构、业务、采购和实施负责人','migration-roadmap':'组合及项目负责人、业务运营方、实施团队','requirements':'需求责任方、业务验收方、架构与实施团队','implementation-governance':'业务验收方、架构治理方、实施及风险责任方','change-value':'收益责任方、运营及业务决策方'}
    for a in arts:
        v=views[a['id']]
        t=f'# {a["name_zh"]}（{a["name_en"]}）\n\nID：`{a["id"]}` · 主责：[{a["owner"]}](../../../{a["owner"]}/SKILL.md) · 原文域：{"、".join(a["domains"])}。\n\n**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。\n\n## 决策与受众\n\n{a["question"]}\n\n主要受众：{stakeholder.get(a["owner"].removeprefix("togaf-"),"业务发起方及相关领域责任人")}。输出需回应已确认关注点，不因清单存在就强制生成。\n\n## 输入与属性\n\n必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：\n\n'
        for typ,attrs in a['required_attributes'].items():t+=f'- `{typ}`：'+('、'.join('`'+f+'`' for f in attrs) if attrs else '名称、边界、来源及对象类型')+'。\n'
        t+='\n可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。\n\n## 关系与表示语义\n\n'
        for rel in a['relationship_types']:
            rule=registry[rel];t+=f'- `{rel}`：{rule["meaning"]}。{", ".join(rule["source_types"])} → {", ".join(rule["target_types"])}。\n'
        if a.get('matrix'):
            x=a['matrix'];t+='\n行：'+', '.join(x['row_types'])+'；列：'+', '.join(x['column_types'])+'。模型关系从行到列。单元含义：'+x['cell_meaning']+'；允许代码：'+', '.join(x['codes'])+'；空白：'+x['empty_meaning']+'。同一单元可有多个有依据的代码。\n'
        for key in ['required_identity_fields','relationship_requirements']:
            if a.get(key):t+='\n附加要求：`'+json.dumps(a[key],ensure_ascii=False)+'`。\n'
        t+='\n## 分析与构造\n\n'+''.join(f'{i}. {step}。\n' for i,step in enumerate(a['analysis'],1))
        t+='\n按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。\n\n## 输出\n\nMarkdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`'+a['notation']+'`。'
        if a['kind']=='diagram':
            t+='提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。'
            if a['notation']=='er':t+='两端基数已确认才使用 ER 符号；未知时退为明确标注的关系图。'
            if a['notation'] in ['map','canvas']:t+='卡片位置只用于排版；分解或依赖由显式关系表示。热力颜色需量尺和实际评分依据。'
        t+='\n\n## 质量与常见误读\n\n'+''.join('- '+c+'。\n' for c in a['semantic_checks'])+'- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。\n- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。\n- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。\n'
        containing=[d for d in ds if a['id'] in d['artifact_ids']];related=[b for b in arts if b['id']!=a['id'] and set(b['entity_types'])&set(a['entity_types'])]
        t+='\n## 复用与追溯\n\n'+('支撑交付物：'+'、'.join(f'[{d["name_zh"]}](../deliverables/{d["id"]}.md)' for d in containing)+'。' if containing else '按视点需要被架构定义文档等交付物引用，不强制绑定。')+'\n\n相关制品：'+'、'.join(f'[{b["name_zh"]}]({b["id"]}.md)' for b in related[:6])+'。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。\n'
        t+='\n## 完整虚构示例\n\n[实际生成结果](../../examples/retail/artifacts/'+a['id']+'.md) 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 [完整案例模型](../../tests/retail-example.json) 按 ID 定位。\n\n```json\n'+json.dumps(v,ensure_ascii=False,indent=2)+'\n```\n\n生成单项：\n\n```sh\npython "$TOGAF_SKILLS/_shared/scripts/generate.py" "$TOGAF_SKILLS/_shared/tests/retail-example.json" --artifact '+a['id']+' --out ./architecture-output'+(' --render' if a['kind']=='diagram' else '')+'\n```\n\nTOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。\n'
        t+='\n## 来源\n\nG248 附录 A，源行 '+', '.join(map(str,a['source_locator']['lines']))+'；方法指南：'+', '.join(a['sources'])+'。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。\n'
        (ROOT/'references/artifacts'/(a['id']+'.md')).write_text(t)
    for d in ds:
        t=f'# {d["name_zh"]}（{d["name_en"]}）\n\nID：`{d["id"]}` · 主责：[{d["owner"]}](../../../{d["owner"]}/SKILL.md) · 常用 ADM：{d["adm"]}。\n\n名称来自 G248 附录 B；下列组装结构是项目约定，不替代 C220 正式定义。\n\n## 输入与内容\n\n输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。\n\n'
        for s in d['sections']:t+=f'- **{s["title"]}**：{s["instruction"]}。\n'
        t+='\n## 组装与引用\n\n'+''.join(f'- [{names[aid]}](../artifacts/{aid}.md)。\n' for aid in d['artifact_ids'])+'\n以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。\n'
        if d['id']=='architecture-repository':t+='\n额外建立实际资产清单：标识、路径、版本、状态和来源。生成器索引实际输出视图与共享模型，不能用空文件夹代替存储库。\n'
        if d['id'] in ['architecture-building-blocks','solution-building-blocks']:t+='\nABB 规定职责、接口、质量与约束；SBB 表达候选或实际实现及 ABB 映射。构建块作为交付内容不意味着与制品成为互斥类别。\n'
        if d['id']=='requirements-impact-assessment':t+='\n与同名制品共享同一次需求影响分析，交付物展开影响和处置，不重复创建需求事实。\n'
        t+='\n## 评审与不足\n\n'+''.join('- '+c+'。\n' for c in d['semantic_checks'])+'- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。\n- 所有引用可达，结论可回溯到模型、需求及来源。\n'
        t+='\n## 完整虚构示例\n\n[实际组装结果](../../examples/retail/deliverables/'+d['id']+'.md)。以下为完整案例中的组装输入，实体和视图见 [案例模型](../../tests/retail-example.json)。\n\n```json\n'+json.dumps(delivs[d['id']],ensure_ascii=False,indent=2)+'\n```\n\n```sh\npython "$TOGAF_SKILLS/_shared/scripts/generate.py" "$TOGAF_SKILLS/_shared/tests/retail-example.json" --deliverable '+d['id']+' --out ./architecture-output --render\n```\n\n## 来源\n\n'+', '.join(d['sources'])+'，详见 [来源分析](../source-analysis.md)。名称依据 G248 附录 B，生成结构为项目综合，正式定义缺口保留。\n'
        (ROOT/'references/deliverables'/(d['id']+'.md')).write_text(t)
    t='# 覆盖与调用索引\n\n70 种制品（20 目录、12 矩阵、37 图／地图、1 评估）和 22 项交付物。跨域同名条目只设一个主责定义，保留原域。候选清单不是每个项目的强制输出。\n\n## 制品\n\n| ID | 制品 | 类型 | 原域 | 主责技能 |\n| --- | --- | --- | --- | --- |\n'
    for a in arts:t+=f'| `{a["id"]}` | [{a["name_zh"]}](artifacts/{a["id"]}.md) | {a["kind"]} | {"、".join(a["domains"])} | [{a["owner"]}](../../{a["owner"]}/SKILL.md) |\n'
    t+='\n## 交付物\n\n| ID | 交付物 | 常用 ADM | 主责技能 |\n| --- | --- | --- | --- |\n'
    for d in ds:t+=f'| `{d["id"]}` | [{d["name_zh"]}](deliverables/{d["id"]}.md) | {d["adm"]} | [{d["owner"]}](../../{d["owner"]}/SKILL.md) |\n'
    (ROOT/'references/coverage.md').write_text(t)
if __name__=='__main__':main()
