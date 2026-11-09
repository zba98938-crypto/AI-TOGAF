# 分段架构师（业务与技术） / Segment Architect (Business and Technical)

记录：`G249:role:segment-architect`；依据：G249；内容角色：`source-grounded-role-analysis`。

范围：一个或多个业务/技术分段。

架构领导/治理、专业范围或协作关系不自动表示人事直属汇报；岗位、角色、任务分别建模。

学历、工作年限、认证、法定签字权等未在相应证据给出时保持未规定，不能从技能等级推造。

## 角色定位

- 负责一个或多个分段的能力、系统、子系统和构件，规划其演进并与其他分段协作。（G249 PDF 第 21 页；原文：responsible for the capabilities provided by one or more business or technical segments）

## 职责

- 将战略目标落实到相关业务/技术分段（G249 PDF 第 22 页；原文：Translating business and technology strategies and objectives into related changes in the relevant business and/or technical segment）
- 评价分段当前能力并识别所需变化（G249 PDF 第 22 页；原文：Assessing current capabilities and identifying required changes in capabilities to achieve business and technology strategies and objectives in the relevant business and/or technical segment）
- 描述分段中人员/组织/服务/流程/数据/技术等关系（G249 PDF 第 22 页；原文：Describing the interrelationships (between people, organization, service, process, data, information, technology, and the external environment) needed to enable the delivery of effective products and services in the relevant business and/or technical segment）
- 创建、迭代和维护分段未来架构模型与视图（G249 PDF 第 22 页；原文：Creating, iterating, and maintaining architectural models and views embodying the key principles that describe the organization’s future state, and that enable its successful evolution in the relevant business and/or technical segment）
- 实施适合分段的迭代敏捷架构实践（G249 PDF 第 22 页；原文：Implementing architecture working practices to support and enable iterative and Agile working in the relevant business and/or technical segment）
- 识别并沟通分段约束、政策和标准（G249 PDF 第 22 页；原文：Identifying, documenting, and communicating the constraints, policies, and standards necessary to define, assure, and govern the effective evolution of an Architecture Landscape (its environment of services implemented in its various building blocks) in the relevant business and/or technical segment）
- 领导、辅导相关专家和解决方案架构师（G249 PDF 第 22 页；原文：Developing, leading, enabling, and supporting the technical/business specialists and Solution Architects working within the architecture team in the relevant business and/or technical segment through leadership, mentoring, and coaching）

## 决策与治理权限

- 监督分段内系统/子系统/构件开发，确保适用、合法并遵循政策和标准。（G249 PDF 第 22 页；原文：They oversee all development）
- 确定使分段构件有效、高效且合法的政策与标准。（G249 PDF 第 22 页；原文：policies and standards）

## 任职与能力要求

- 具有丰富经验并已取得专业成就。（G249 PDF 第 21 页；原文：experienced and accomplished professionals）
- 能够与其他架构师有效协作，维持整体环境互联。（G249 PDF 第 22 页；原文：collaborate effectively and easily with other architects）
- 能够明确专家及解决方案架构师角色，组织有效协作。（G249 PDF 第 22 页；原文：technical/business specialists and Solution Architects are clear about their roles）

## 输入与输出

- 输入企业战略/目标、分段能力现状及约束；输出分段能力变化、架构模型、政策标准与路线图。（G249 PDF 第 22 页；原文：relevant business and/or technical segment）

## 分析结论

分段是管理与控制所需的一致能力分组；业务、数据、应用、技术域是有用的分段视角。一般Segment角色没有单独数值列，不把四域列简单取均值。

本指南没有该角色的独立数值技能列。保留文本要求，不生成虚构等级或平均等级。


## 协作对象（不等同直属上下级）

- Chief Architect（PDF 第 22 页）
- Relevant business segment leaders（PDF 第 22 页）
- Customer/user representatives（PDF 第 22 页）
- Relevant business operators（PDF 第 23 页）
- Relevant product owners and managers（PDF 第 23 页）
- Change managers（PDF 第 23 页）
- Program and project managers（PDF 第 23 页）
- Portfolio managers（PDF 第 23 页）
- Enterprise Architects（PDF 第 23 页）
- Segment Architects（PDF 第 23 页）
- Solution Architects（PDF 第 23 页）
- Relevant business and technical specialists（PDF 第 23 页）
- Relevant segment industry leaders（PDF 第 23 页）
- Any other stakeholders with an interest in the Enterprise Architecture and the delivery of effective solutions and services (including all relevant user types)（PDF 第 23 页）

## 原文候选 KPI（不是项目已采纳目标）

- Stakeholder satisfaction score ⇒ 3 out of 5 (scale 1 = poor; 5 = excellent, target score average or above)（PDF 第 23 页）
- Services (related to the elements overseen by a segment(s)) delivering and accepted at or better than planned service levels（PDF 第 23 页）
- The segment(s) is externally benchmarked as in the (xxx) quartile for business/technology capability and architecture in the relevant market segment（PDF 第 23 页）
- New and changed solutions are delivered and signed off within agreed time, resource, and cost boundaries (boundaries must be properly set to reflect the potential variation relevant to a specific change)（PDF 第 23 页）

## 角色关系

|关系|另一角色|含义|
|---|---|---|
|leads_and_coaches|G249:role:chief-architect|首席提供领导与辅导，为架构全景演进建立条件。|
|leads_and_integrates|G249:role:enterprise-architect|企业层领导并整合分段/解决方案工作，形成互操作与治理条件。|
|provides_context_and_guidance|G249:role:solution-architect|分段层使解决方案架构师和专家明确角色并有效协作。|
|informed_by_higher_scope_architecture|G249:role:solution-architect|解决方案设计受企业/分段层架构指引；上位指架构范围，不证明雇佣汇报。|
|domain_context_of|G249:role:business-domain-architect|四个域是分段概念的专业视角；此关系不赋予直属领导身份。|
|domain_context_of|G249:role:data-domain-architect|四个域是分段概念的专业视角；此关系不赋予直属领导身份。|
|domain_context_of|G249:role:application-domain-architect|四个域是分段概念的专业视角；此关系不赋予直属领导身份。|
|domain_context_of|G249:role:technology-domain-architect|四个域是分段概念的专业视角；此关系不赋予直属领导身份。|

## 可执行能力核对建议

逐技能收集可核实的设计产物、决策理由、协作反馈及交付经历；按本项目选择的角色范围与参考等级逐项判断。原文未给出统一加权总分、合格阈值或自动认证规则。该建议为项目应用分析，不是原文强制流程。
