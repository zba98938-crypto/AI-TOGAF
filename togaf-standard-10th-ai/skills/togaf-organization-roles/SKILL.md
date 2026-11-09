---
name: togaf-organization-roles
description: 分析组织工作网络、组织分解、参与者、角色与职责，生成组织地图、能力叠加和角色技能矩阵。
---

# 组织与角色

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

建立架构实践、配置架构任务或评价架构师能力时，先读取 [G249 任务、角色与技能工作流](../_shared/references/g249-operational-workflow.md)。从工作依据与预期决策推导角色和技能要求；角色参考、企业目标、人员证据及实际任命分别保存。普通组织图继续使用下面的组织分析流程。

1. 确定内外部组织边界与有效时间。
2. 分别识别参与者和角色。
3. 核实正式汇报与协作关系。
4. 映射能力责任及业务交接。
5. 检查职责缺口与冲突。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接 Preliminary 的架构实践与角色能力配置，以及 B 阶段的业务组织分析。角色任命、技能证据和发展复评随实际任务贯穿周期。从利益相关者关注点选择相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [组织/参与者目录 / Organization/Actor Catalog](../_shared/references/artifacts/organization-actor-catalog.md)
- [角色目录 / Role Catalog](../_shared/references/artifacts/role-catalog.md)
- [参与者/角色矩阵 / Actor/Role Matrix](../_shared/references/artifacts/actor-role-matrix.md)
- [能力/组织矩阵 / Capability/Organization Matrix](../_shared/references/artifacts/capability-organization-matrix.md)
- [组织分解图 / Organization Decomposition Diagram](../_shared/references/artifacts/organization-decomposition-diagram.md)
- [组织地图 / Organization Map](../_shared/references/artifacts/organization-map.md)

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。汇报、协作、负责和参与使用不同关系；组织调整不引起无理由的能力重定义；不要推断未记录的授权。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 13 个视图规范、4 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 参与者/角色矩阵（兼容默认） | `compat-actor-role-matrix` | `actor-role-matrix` |
| 怎样弥补人员技能缺口？ | `architecture-development-plan-default` | `architecture-development-plan` |
| 架构实践需要哪些角色层级，各自职责、活动、关键利益相关者与KPI是什么，谁领导谁？ | `architecture-role-catalog-default` | `architecture-role-catalog` |
| 每种架构角色需要什么熟练度？ | `architecture-skill-matrix-default`, `ea-skill-role-proficiency` | `architecture-skill-matrix` |
| 能力/组织矩阵（兼容默认） | `compat-capability-organization-matrix` | `capability-organization-matrix` |
| 组织/参与者目录（兼容默认） | `compat-organization-actor-catalog` | `organization-actor-catalog` |
| 组织分解图（兼容默认） | `compat-organization-decomposition-diagram` | `organization-decomposition-diagram` |
| 组织工作网络 | `organization-work-network`, `organization-capability-overlay` | `organization-map` |
| 角色目录（兼容默认） | `compat-role-catalog` | `role-catalog` |
| 所有员工和关键专业角色怎样形成可应用的可持续ICT技能？ | `sustainability-education-plan-default` | `sustainability-education-plan` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



来源工作产品契约：[G206 organization-map](../_shared/references/capabilities/organization-map-source-contract.md)。按此契约核对输入、修改及反例，复用稳定基础制品ID。

## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-organization-roles 能力包索引](../_shared/references/togaf-organization-roles-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

任务和角色先于人员评价；目标、观察、容量、期间及批准分开。适用ADM入口：Preliminary。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
