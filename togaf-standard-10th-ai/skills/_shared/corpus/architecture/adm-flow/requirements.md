# 持续需求管理（不是 Phase I）

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入


## 工作与治理门

1. 识别来源、利益相关者与目标
2. 澄清、优先排序、形成可验证需求并建立基线
3. 在每次阶段退出前复核需求与工作产品的追踪
4. 登记需求变更及候选影响范围，再逐项判断
5. 把接受、拒绝或待决处置反馈给受影响阶段并按需重开迭代


## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-requirements-specification|架构需求规格|phase-contract-output-candidate|requirements-catalog, constraints-catalog|
|requirements-impact-assessment|需求影响评估|phase-contract-output-candidate|requirements-impact-assessment|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|constraints-catalog|约束目录|catalog|project-owner-routing-candidate|compat-constraints-catalog|
|requirements-catalog|需求目录|catalog|source-artifact-phase-list|compat-requirements-catalog|
|requirements-impact-assessment|需求影响评估|assessment|project-owner-routing-candidate|compat-requirements-impact-assessment|
|bi-requirements-profile|BI 与分析需求规格|report|project-owner-routing-candidate|bi-requirements-profile-default, bi-requirement-origin-boundary, bi-usage-goal-measures, bi-business-function-coverage, bi-application-function-coverage|
|architecture-backlog|架构业务变革与冲刺待办|catalog|project-owner-routing-candidate|architecture-business-backlog, architecture-sprint-backlog, architecture-strategic-mva-trace|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method:b01083:step-01|Step 1|ADM Phase Steps|各阶段从业务目标、价值流、场景、用户体验或管理信息识别需求，记入架构需求规格及需求存储库。|
|C220-web-2025:02-architecture-development-method:b01083:step-02|Step 2|Requirements Management Steps|需求管理过程组织建立基线，记录优先级并确认利益相关者同意；结合13.5.1，实际处置和排序由相关ADM阶段承担，不能把过程列当独立决定权。|
|C220-web-2025:02-architecture-development-method:b01083:step-03|Step 3|Requirements Management Steps|需求管理持续监控已建立的需求基线。|
|C220-web-2025:02-architecture-development-method:b01083:step-04|Step 4|ADM Phase Steps|各阶段识别新增或变化：移除、重新评价优先级、增加需求或修改既有需求。|
|C220-web-2025:02-architecture-development-method:b01083:step-05|Step 5|Requirements Management Steps|需求管理确保当前阶段架构师和利益相关者确定并记录优先级，处理冲突并产生需求影响评估。变更可从任意渠道到来；记录决定，核对利益相关者满意度并推动问题解决。|
|C220-web-2025:02-architecture-development-method:b01083:step-06|Step 6|ADM Phase Steps|各阶段评价对当前及既往阶段的影响，决定本周期实施还是留待后续周期；实施时评价变更时间安排，并发布n+1版需求影响评估。|
|C220-web-2025:02-architecture-development-method:b01083:step-07|Step 7|ADM Phase Steps|各阶段实施来自H阶段的需求；需求管理过程确保这些新需求和变更得到管理。|
|C220-web-2025:02-architecture-development-method:b01083:step-08|Step 8|Requirements Management Steps|需求管理更新架构需求存储库，包括被请求的变更及受影响的利益相关者视图。|
|C220-web-2025:02-architecture-development-method:b01083:step-09|Step 9|ADM Phase Steps|各阶段在当前阶段实施已决定的变更。|
|C220-web-2025:02-architecture-development-method:b01083:step-10|Step 10|ADM Phase Steps|各阶段复核既往差距分析。这里gap requirement特指基线内容被意外移除而需修订目标架构的情况；须处置、记录入库并相应修订目标，不能把所有新目标差距都称为此类需求。|

来源摘要：G186 §§5.1.4, 6.1.1, 15.1；C220 ADM 13

具体原文节与定位保留在mapping.json及adm-phases.json。
