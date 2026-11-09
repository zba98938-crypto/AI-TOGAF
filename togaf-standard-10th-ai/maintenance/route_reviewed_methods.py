# -*- coding: utf-8 -*-
"""Attach authored foundation/guide reading routes to the existing 17 skill owners."""
from pathlib import Path
import json,hashlib
C=Path(__file__).resolve().parents[1];P=C/'skills';S=P/'_shared'
ROWS='''
architecture-workbench|Preliminary,A,B,C,D,E,F,G,H,Requirements|01,02,03,04,05,06|G184,G186,G188,G249|先定目的、范围及关注点，再选阶段和制品；迭代及需求管理持续开展
vision-scenarios|A,Requirements|01,02,03,05|G176,G186|从利益相关者问题、目标与约束提出愿景和可验证需求
strategy-capabilities|A,B,E|01,02,04,05|G211,G233,G21H|核对战略—能力—实例—增量的身份与范围
business-models-processes|B|02,03,05|G18A,G206|用业务模型、组织和流程共同解释责任与价值
value-streams|B|02,05|G178,G211|区分价值阶段、能力使能及流程执行
information-data|C,Requirements|02,03,05|G190,G21B,G234,G238|区分业务信息、逻辑数据和物理实现；核对权威来源、生命周期、迁移及保护
application-architecture|C|02,03,05|G21I,G248|由需求和上位边界比较服务及应用方案，保留契约与失败场景
technology-architecture|D|02,03,05|G248,G242|在服务质量和产品约束下选择技术构建块；拓扑不能代替容量证据
security-risk|Preliminary,A,B,C,D,E,F,G,H|02,03,06|G152,G242|按实际资产、威胁、控制与残余风险接受者持续评审
organization-roles|Preliminary|01,02,06|G249,G198,G206|任务和角色先于人员评价；目标、观察、容量、期间及批准分开
requirements|Requirements,A,B,C,D,E,F,G,H|01,02,05|G176,G186|持续维护需求依据、冲突、变化及各域制品追溯
change-value|H,E,F|02,03,04,06|G20F,G210,G217|变更影响、收益归属和实际决策依据驱动迭代，不由渲染推断价值
migration-roadmap|E,F|02,03,05|G233,G188|按依赖、资源与过渡运营条件比较迁移次序
implementation-governance|G,H|02,05,06|G186,G188,G248|契约、符合性、偏离与变更升级均须实际授权及评审证据
gap-solutions|B,C,D,E|02,03,05|G248,G233|基线/目标差距到方案及构建块的选择必须保留约束和备选理由
ea-capability|Preliminary,H|01,02,04,06|G184,G203,G249|先明确架构实践授权、服务对象和工作需求，再配置能力与发展路径
artifact-review|Preliminary,A,B,C,D,E,F,G,H,Requirements|01,02,03,04,05,06|G186,G188,G249|从原始业务材料核对决定与制品，结构、语义、视觉和批准各自取证
'''
def main():
 vols={p.stem[:2]:p for p in (C/'fundamental/analysis').glob('*.json')};routes=[]
 for line in ROWS.strip().splitlines():
  name,phases,vs,gs,rule=line.split('|');skill='togaf-'+name;p=P/skill/'SKILL.md';assert p.is_file(),p
  refs=[]
  for num in vs.split(','):
   doc=json.loads(vols[num].read_text());refs.append({'document_id':doc['document_id'],'path':'corpus/fundamental/analysis/'+vols[num].name,'sha256':hashlib.sha256(vols[num].read_bytes()).hexdigest(),'source_kind':'web','translation_status':doc['translation_status']})
  for code in gs.split(','):refs.append({'document_id':code,'path':'corpus/chapters/'+code+'.json','sha256':hashlib.sha256((C/'chapters'/(code+'.json')).read_bytes()).hexdigest(),'source_kind':'pdf'})
  routes.append({'skill':skill,'adm_phases':phases.split(','),'method_rule_zh':rule,'required_reading':refs,'origin':'project-route-from-reviewed-local-sources','conditional_supplements':[{'document_id':'G226','when_zh':'需要敏捷架构实践时；保持2022 Playbook版本和作者经验边界'},{'document_id':'W242C','when_zh':'涉及AI投资、工作分配或系统能力时；保持2025中文白皮书范围，训练指AI训练，不是人员熟练度'}]})
  text=p.read_text().replace('承接A 阶段的领域工作','承接所选ADM阶段的相关工作');marker='## 本轮已审阅方法路由'
  if marker in text:text=text.split(marker)[0].rstrip()+'\n'
  text+='\n'+marker+'\n\n'+rule+'。适用ADM入口：'+phases+'。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。\n'
  p.write_text(text)
 report={'schema_version':'reviewed-skill-routing/1','routes':routes,'notice_zh':'这是项目方法路由，不是TOGAF规定的软件模块；资料存在和生成成功不构成业务批准。'}
 (S/'references/reviewed-method-routing.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');lines=['# 已审阅来源与技能入口','','从当前任务选关注点与ADM阶段；范围、决策问题和输出选择理由必须来自业务材料。','','|技能|ADM入口|本轮方法要求|读取卷/指南|','|---|---|---|---|']
 for row in routes:lines.append('|'+row['skill']+'|'+', '.join(row['adm_phases'])+'|'+row['method_rule_zh']+'|'+', '.join('['+r['document_id']+'](../'+r['path']+')' for r in row['required_reading'])+'|')
 lines+=['','网页来源使用卷/锚点/内容块；PDF使用物理页和内容块。完整中文译文尚未完成时，必须核对所引英文来源块。','','人员任务链：工作依据 → 任务 → 待决问题 → 角色责任 → 目标技能 → 方法 → 制品 → 验收证据。G249量表不决定AI自主权限；普通制图无需人员评价。','','敏捷情境可补读[G226](../corpus/supplementary/G226.md)；AI投资与系统工作可补读[W242C](../corpus/supplementary/W242C.md)。前者是2022 Playbook，后者是2025中文白皮书，不合并为基础标准。']
 (S/'references/reviewed-method-routing.md').write_text('\n'.join(lines)+'\n');print({'routed_skills':len(routes)})
if __name__=='__main__':main()
