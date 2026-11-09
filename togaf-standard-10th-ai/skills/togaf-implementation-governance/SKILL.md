---
name: togaf-implementation-governance
description: 生成架构合同、合同度量、合规评估和治理决策，追踪实施偏离及补救。
---

# 实施治理

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 明确实施范围和适用架构版本。
2. 约定各方责任与验收证据。
3. 逐项比较实施与架构要求。
4. 分析偏离风险及补救选项。
5. 记录真实决策与后续验证。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接G 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [合同/度量目录 / Contract/Measure Catalog](../_shared/references/artifacts/contract-measure-catalog.md)

## 主责交付物

- [架构合同](../_shared/references/deliverables/architecture-contract.md)
- [合规评估](../_shared/references/deliverables/compliance-assessment.md)

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。每项结论可定位证据；未批准例外不写已接受；控制设计不等于运行有效；治理决策有决策者及日期来源。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 10 个视图规范、8 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 按Rapid/Functional/Robust及具体过渡，哪些规格、实施和价值条件已有证据，哪些需要返工或裁剪？ | `change-profile-planning-checklist`, `change-profile-implementation-checklist` | `change-profile-governance-checklist` |
| 服务提供方应以哪些边界和口径交付可审查环境数据？ | `cloud-environmental-data-contract-default` | `cloud-environmental-data-contract` |
| 合同/度量目录（兼容默认） | `compat-contract-measure-catalog` | `contract-measure-catalog` |
| 某类决策由谁、在何种边界内决定，何时需扩大参与或重新评审？ | `decision-delegation-register-default` | `decision-delegation-register` |
| 环境标准怎样进入架构决策？ | `environmental-decision-log-default` | `environmental-decision-log` |
| 架构定义了哪些产品、边界与产品负责人约束，哪些待办项与约束冲突，是否有阶段G豁免？ | `product-constraint-register-default` | `product-constraint-register` |
| 实现是否遵循安全政策与要求？ | `security-audit-record-default` | `security-audit-record` |
| 交付团队据以设计和测试的需求/规格、风险/控制配对、差距范围与目标架构摘要是什么？ | `solution-delivery-notebook-default` | `solution-delivery-notebook` |
| 如何在服务范围、地点、合同和全生命周期中形成可证实采购选择？ | `sustainable-procurement-strategy-default` | `sustainable-procurement-strategy` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-implementation-governance 能力包索引](../_shared/references/togaf-implementation-governance-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

契约、符合性、偏离与变更升级均须实际授权及评审证据。适用ADM入口：G,H。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
