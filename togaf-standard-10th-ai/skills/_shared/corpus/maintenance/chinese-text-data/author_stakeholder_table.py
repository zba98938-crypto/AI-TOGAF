# -*- coding: utf-8 -*-
from pathlib import Path
import json,re
from bs4 import BeautifulSoup
C=Path(__file__).resolve().parents[2];base=C/'maintenance/chinese-text-data';d=json.loads((C/'fundamental/web-2025/volumes/03-adm-techniques/document.json').read_text());f=json.loads((C/'fundamental/chinese-text/05-architecture-content.json').read_text());key=lambda s:re.sub(r'[^a-z]','',s.lower());names={key(re.sub(r'^\d+[.\d]*\. ','',b['text_en'])):re.sub(r'^\d+[.\d]*\. ','',b['text_zh']) for b in f['blocks'] if b['kind'].startswith('h')};names[key('Business Capabilities catalog')]='业务能力目录'
people='''公司高管，如CEO、CFO、CIO、COO
公司项目群管理办公室，如项目组合经理
公司采购，如采购方
公司人力资源，如HR、培训发展经理
企业安全，如风险管理、安全官、IT安全经理
公司质量/标准群体，如数据所有者、流程所有者、技术标准机构
最终用户组织高管，如业务单元董事、高管、IT/架构负责人
最终用户组织一线管理，如高级业务经理、区域运营经理、IT经理
最终用户业务域专家，如流程专家、业务/流程分析师、流程架构师、设计者、职能经理
系统运营的IT服务管理，如服务交付经理
应用运营，如应用架构、系统与软件工程师
基础设施运营，如基础设施架构师、Wintel、中型机、运营DBA、服务台
数据/语音通信运营，如网络管理
项目组织高管，如赞助者、项目群经理
项目组织一线管理，如项目经理
项目业务流程/职能专家，如财务FICO及HR顾问
项目产品专家，如门户专家
项目技术专家，如应用架构师
外部监管机构，如金融、行业监管者
外部供应商，如联盟伙伴、关键供应商'''.splitlines()
concerns='''组织高层驱动、目标及具体目标如何转化为有效流程和IT架构，推进业务。
变革优先级、资助和对齐；理解项目内容及技术依赖，支持组合决策。
哪些构建块可采购、有哪些规则约束；向多供应商寻求最佳成本且符合标准等约束，作适配架构的采购决策。
支撑架构及变更所需角色、参与者；管理人员过渡。
确保只有获许可者访问组织信息、数据、系统，并防止未授权篡改。
确保业务、数据、应用、技术资产一致治理。
高层驱动、目标和具体目标如何转化为有效流程及架构，推进业务。
顶层职能流程及关键应用如何支持。
流程及系统功能方面，包括人员、用户流程、支撑功能和信息流。
确保服务达到业务成功所需水平。
开发途径、模块化复用、可迁移、迁移及互操作。
全部组件的位置、可修改、复用、可用，以及最优开发部署。
通信网络服务的位置、可修改、复用、可用，以及最优开发部署。
按时按预算交付、实现预期收益。
在商定范围按时按预算完成运营交付。
凭经验及与最终用户域专家交互细化功能需求。
产品设计满足需求及架构愿景；套装环境可识别可利用能力并指导定制战略。
技术产品设计满足需求及方案架构愿景。
获得监管所需信息并满足要求，关注报告流程及监管报送数据应用。
满足信息交换要求，以履行商定服务契约。'''.splitlines()
b=next(b for b in d['blocks'] if b['id'].endswith('b00290'));rs=BeautifulSoup(b['html'],'html.parser').select('tr')[1:];assert len(rs)==len(people)==len(concerns);out=[]
for r,p,c in zip(rs,people,concerns):
 cs=r.find_all('td',recursive=False);[br.replace_with('\n') for br in cs[3].find_all('br')];art=[' '.join(v.split()) for v in cs[3].get_text().splitlines() if v.strip()];artzh=[]
 for a in art:
  assert key(a) in names,a;artzh.append(names[key(a)])
 cl=' '.join(cs[2].stripped_strings);clzh={'KEEP SATISFIED':'保持满意','KEY PLAYERS':'关键参与者','KEEP INFORMED':'保持知情'}[cl]
 out.append('|'+p+'|'+c+'|'+clzh+'|'+ '；'.join(artzh)+'|')
p=base/'partial/03-adm-techniques.txt';s=p.read_text();assert '@@ b00290\n' not in s;s+='@@ b00290\n表3-2：利益相关者地图示例（组织采用时须裁剪）\n\n|利益相关者及示例|关键关注点|类别|目录、矩阵和图|\n|---|---|---|---|\n'+'\n'.join(out)+'\n';p.write_text(s)
