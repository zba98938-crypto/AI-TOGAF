# ADM框架、架构制品与完整架构流程图

项目解释图；实线为常见信息流，虚线为需求反馈与迭代；阶段可并行、复用和裁剪。

[离线中文导航与图形预览](index.html)（SVG预览嵌入单页，原图与源码可打开／下载）。
从当前阶段合同、23项交付物和制品注册派生；完整目录和来源定位见[mapping.json](mapping.json)。

总览实线给出阅读顺序，实际退出依赖以周期`depends_on`为准。B/C/D可并行协调；C同时分析数据与应用。

阶段细图列出工作、制品示例和治理门；Markdown保留全部候选目录／矩阵／图。条件输出保留if any。

## 图形入口

|范围|SVG向量图|可编辑源码|PNG|
|---|---|---|---|
|adm-framework|[adm-framework.svg](adm-framework.svg)|[adm-framework.mmd](adm-framework.mmd)|[adm-framework.png](adm-framework.png)|
|content-chain|[content-chain.svg](content-chain.svg)|[content-chain.mmd](content-chain.mmd)|[content-chain.png](content-chain.png)|
|phase-Preliminary|[phase-Preliminary.svg](phase-Preliminary.svg)|[phase-Preliminary.mmd](phase-Preliminary.mmd)|[phase-Preliminary.png](phase-Preliminary.png)|
|phase-A|[phase-A.svg](phase-A.svg)|[phase-A.mmd](phase-A.mmd)|[phase-A.png](phase-A.png)|
|phase-B|[phase-B.svg](phase-B.svg)|[phase-B.mmd](phase-B.mmd)|[phase-B.png](phase-B.png)|
|phase-C|[phase-C.svg](phase-C.svg)|[phase-C.mmd](phase-C.mmd)|[phase-C.png](phase-C.png)|
|phase-D|[phase-D.svg](phase-D.svg)|[phase-D.mmd](phase-D.mmd)|[phase-D.png](phase-D.png)|
|phase-E|[phase-E.svg](phase-E.svg)|[phase-E.mmd](phase-E.mmd)|[phase-E.png](phase-E.png)|
|phase-F|[phase-F.svg](phase-F.svg)|[phase-F.mmd](phase-F.mmd)|[phase-F.png](phase-F.png)|
|phase-G|[phase-G.svg](phase-G.svg)|[phase-G.mmd](phase-G.mmd)|[phase-G.png](phase-G.png)|
|phase-H|[phase-H.svg](phase-H.svg)|[phase-H.mmd](phase-H.mmd)|[phase-H.png](phase-H.png)|
|requirements|[requirements.svg](requirements.svg)|[requirements.mmd](requirements.mmd)|[requirements.png](requirements.png)|
|cycle-iterations|[cycle-iterations.svg](cycle-iterations.svg)|[cycle-iterations.mmd](cycle-iterations.mmd)|[cycle-iterations.png](cycle-iterations.png)|

## 逐阶段资料

- [预备阶段 · 架构能力](phase-Preliminary.md)
- [A · 架构愿景](phase-A.md)
- [B · 业务架构](phase-B.md)
- [C · 信息系统架构（数据＋应用）](phase-C.md)
- [D · 技术架构](phase-D.md)
- [E · 机会与解决方案](phase-E.md)
- [F · 迁移规划](phase-F.md)
- [G · 实施治理](phase-G.md)
- [H · 架构变更管理](phase-H.md)
- [持续需求管理（不是 Phase I）](requirements.md)

## 交付物全表

|交付物ID|名称|阶段语境|制品ID|
|---|---|---|---|
|architecture-building-blocks|架构构建块|B C D E|requirements-catalog, solution-concept-diagram|
|architecture-contract|架构合同|G|contract-measure-catalog, requirements-catalog|
|architecture-definition-document|架构定义文档|B C D E|business-capability-map, conceptual-data-diagram, application-communication-diagram, platform-decomposition-diagram|
|architecture-requirements-specification|架构需求规格|A B C D|requirements-catalog, constraints-catalog|
|architecture-principles|架构原则|Preliminary|principles-catalog|
|architecture-repository|架构存储库|Preliminary H|principles-catalog, technology-standards-catalog, requirements-catalog|
|architecture-roadmaps|架构路线图|E F H|application-migration-diagram, data-migration-diagram, benefits-diagram|
|architecture-vision|架构愿景|A|stakeholder-catalog, project-context-diagram, solution-concept-diagram, benefits-diagram|
|business-goals-objectives|业务目标与目的|A B|driver-goal-objective-catalog, goal-objective-service-diagram|
|business-principles|业务原则|Preliminary A|principles-catalog|
|business-drivers|业务驱动因素|A|driver-goal-objective-catalog|
|capability-assessment|能力评估|A B E|business-capability-map, capability-organization-matrix|
|change-request|变更请求|G H|requirements-impact-assessment|
|communications-plan|沟通计划|A G H|stakeholder-catalog|
|compliance-assessment|合规评估|G|requirements-catalog, data-security-diagram|
|implementation-migration-plan|实施与迁移计划|F|application-migration-diagram, data-migration-diagram|
|organization-model|企业架构组织模型|Preliminary|organization-map, role-catalog, actor-role-matrix|
|request-for-architecture-work|架构工作请求|Preliminary H A|project-context-diagram, driver-goal-objective-catalog|
|requirements-impact-assessment|需求影响评估|Requirements|requirements-impact-assessment|
|solution-building-blocks|解决方案构建块|E G|application-portfolio-catalog, technology-portfolio-catalog|
|statement-of-work|架构工作说明书|A|project-context-diagram, stakeholder-catalog|
|tailored-architecture-framework|裁剪后的架构框架|Preliminary|principles-catalog, requirements-catalog|
|implementation-governance-model|实施治理模型|F G|role-catalog, actor-role-matrix|

## 贯穿阶段的制品评审

Review为贯穿阶段的工作路由，不是新增ADM阶段。

- 架构成果验收准则（architecture-acceptance-criteria）：architecture-acceptance-criteria-default
- 可持续性架构评审画布（sustainability-review-canvas）：sustainability-review-canvas-default, sustainability-architecture-canvas
- 视角库（viewpoint-library）：viewpoint-library-default
- 架构治理检查清单（architecture-governance-checklist）：architecture-governance-checklist-target, architecture-governance-checklist-implementation
- 不合规影响与处置登记（non-compliance-disposition）：non-compliance-disposition-default
- 架构描述充分性与正式度评审（architecture-description-formality-review）：architecture-description-formality-table
- 阶段边界与项目收尾记录（project-stage-closure-record）：project-stage-closure-record-stage, project-stage-closure-record-project
- 交付物章程与验收流程（project-deliverable-charter）：project-deliverable-charter-default

## 可复现生成

```sh
python3 -B /path/to/skills/_shared/scripts/adm.py flow --out /new/adm-flow --render
# 实际周期另加 --cycle /path/adm-cycle.json --model /path/model.json
```

输出目录必须不存在。生成操作只读当前合同和周期，不产生批准、业务事实或阶段退出。

[投影覆盖结果](coverage.json)核对阶段／来源步骤／交付物／制品路由；图形渲染和实际专业验收分别取证。

[实际周期的全部输入／输出、依赖及状态](cycle-records.md)。
