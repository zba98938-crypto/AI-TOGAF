---
name: togaf-security-risk
description: 跨业务、数据、应用、技术开展安全与风险分析，生成风险偏好、业务影响、安全域、信任、属性画像、风险登记、控制追溯及缓解与回退计划。
---

# 安全与风险

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

涉及安全域、信任、风险评估、属性画像、服务目录或过渡安全时，读取 [风险与安全手册](../_shared/references/security-risk-handbook.md)，据 ADM 阶段选择工作；区分业务影响与可能性、控制要求与实现服务、目标控制与过渡控制。

1. 从业务资产和价值识别风险情景。
2. 明确可能性、影响尺度及责任。
3. 将处理方案写为安全需求和控制。
4. 定位数据、身份及信任边界。
5. 验证控制证据和残余风险处置。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接贯穿 ADM 的风险与安全工作，并主责 D、G 的相关判据：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [数据安全图 / Data Security Diagram](../_shared/references/artifacts/data-security-diagram.md)

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。控制可追溯到风险与需求；未测不等于有效；不从角色使用矩阵推导访问许可；法规适用性有来源和日期。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 22 个视图规范、17 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 采用哪些控制框架来应对风险？ | `applicable-control-framework-register-default` | `applicable-control-framework-register` |
| 哪些法规适用于本次架构范围？ | `applicable-legislation-register-default` | `applicable-legislation-register` |
| 安全架构以什么业务价值衡量？ | `business-attribute-profile-default`, `business-attribute-profile-trace` | `business-attribute-profile` |
| 安全不足会使哪些业务结果受损？ | `business-impact-analysis-default` | `business-impact-analysis` |
| 哪些风险需要处置并由谁负责？ | `business-risk-register-default`, `risk-security-traceability` | `business-risk-register` |
| 数据安全图（兼容默认） | `compat-data-security-diagram` | `data-security-diagram` |
| 承担多大风险才能实现业务结果？ | `risk-appetite-default` | `risk-appetite` |
| 如何把风险降至可接受水平？ | `risk-mitigation-plan-default` | `risk-mitigation-plan` |
| 愿景如何使利益相关者确信风险可接受？ | `security-blueprint-default`, `security-cross-domain`, `security-adm-concept-map` | `security-blueprint` |
| 资产分类将触发哪些安全要求？ | `security-classification-scheme-default` | `security-classification-scheme` |
| 哪些资产受同一安全策略管辖？ | `security-domain-model-default` | `security-domain-model` |
| 架构变更怎样改变安全与风险？ | `security-impact-analysis-default` | `security-impact-analysis` |
| 安全政策如何分层及分配责任？ | `security-policy-architecture-default` | `security-policy-architecture` |
| 架构工作需要哪些安全与风险人员？ | `security-resource-plan-default` | `security-resource-plan` |
| 哪些安全服务实现安全目标？ | `security-services-catalog-default` | `security-services-catalog` |
| 哪些人员需要掌握控制的正确使用？ | `security-training-plan-default` | `security-training-plan` |
| 迁移过程本身会带来什么风险？ | `transition-risk-assessment-default` | `transition-risk-assessment` |
| 谁基于什么条件信任谁？ | `trust-framework-default` | `trust-framework` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-security-risk 能力包索引](../_shared/references/togaf-security-risk-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

按实际资产、威胁、控制与残余风险接受者持续评审。适用ADM入口：Preliminary,A,B,C,D,E,F,G,H。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
