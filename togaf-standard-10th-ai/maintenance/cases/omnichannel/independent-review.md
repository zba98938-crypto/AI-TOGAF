# 全渠道案例独立来源与设计审阅

2026-11-08后续交付复核已补入[交付收尾报告](delivery-closeout-report.md)：19对PNG/SVG逐张查看，当前本地来源路径及锚点已归一化；另有[8项业务语义变更回归](semantic-change-verification.md)。下文保留原始独立观察及当时生成快照，其中“待逐张视觉复核”等范围说明按后续报告读取当前状态。原[独立F08复核](f08-independent-verification.md)的观察与指纹不被覆盖。

状态：F08主制品主体缺失已在本地案例修复，人员覆盖与专业证据缺口仍保留。首次独立审阅与修复作者自检分别记录；不是业务批准、人员认证或上线授权。

先独立审阅三份只读原教学材料和已生成制品。随后在togaf-standard-10th-ai本地案例内修复F08、重跑三组生成并自检；未修改skills目录。原独立观察与修复作者自检分开记录，schema/表达覆盖通过不作为业务内容充分性验收。

## 原始材料支持的结论

- **缺一致性输入时不能定优**：两候选均保留；纯同步仅被判为不能独自覆盖断连受理，未被全局退役；异步不被宣称避免超卖。
- **新增断连约束传播**：版本2新增恢复接口、门店与中央记录、离线需求、过渡和工作包；更新风险、解决方案任务目标、发展行动及复评，保留原人员观察。通用图影响的边界见F06。
- **物流只接受确认订单**：物流交接唯一状态迁移起点为ORDER-CONFIRMED；无待确认订单直接进入物流边。未提供物流系统时没有臆造物流应用，交接契约明确为缺口。
- **任务缺技能定义与目标**：TASK-SOL所需optimistic-pessimistic-patterns没有采用目标；当前分析明确source-definition-unresolved与missing-task-skill-requirement，不自动猜成并发控制，不宣布任务技能完备。
- **个人证据及容量未知**：甲proficiency=null而非自动降为2；所有任务workload_hours=null，40小时及8小时专家支持不能证明够用。实际分析保持needs-evidence、capacity unresolved和approval not-granted；另外期间缺口见F04。
- **共享ID与退役**：两个内存模型保留28个原实体ID，新增6个，没有退役任何实体。源材料未要求删除在线同步能力，保留IF-RESERVE用于在线场景合理；不凭新离线约束退役旧应用。
- **过渡是运营状态且需进入条件**：TRANS-ONLINE和TRANS-OFFLINE提供运营、数据一致性、依赖、控制和回退条件；WP为准备/演练工作。日期为候选计划，不等于进入批准；多个运营条件仍未知，不能标为已可运营。
- **技能发展不自动升级**：版本2保留历史观察并增加任务要求变更记录，更新实践与复评；输出rating_change=not-inferred。支持专家对新增离线行为也不自动视为满足。

## 原始问题与修订复核

F01–F07保留首次对只读原材料的观察；每项后附当前本地修订与生成结果，避免把已修订问题误报为仍未处理。F08–F09为本次生成结果复核新增。

### F01 · P1 · 专家4级只有同一条3级任务行为，未独立证实等级

OBS-EXPERT直接给4级，唯一行为与REQ-SKILL-SOL的3级条件相同；无相应更高层行为/组织认可内容。基线运行给evidence-contract-complete和expert-evidence-recorded，只说明声明结构完整；本独立审阅不能将它视为4级或专家支持资格已经证实。

影响：若把该记录用于认定指导/补足人员能力，会高估可用支持；目前assignment仍未批准，尚未造成自动配置批准。

建议：保留原4级为历史声明，将当前观察设为证据不足或补真实相应证据；不因不能证实4级自动降3。专家能力、组织认可和可用容量分别记录。

证据：[raw-business-materials.md:25](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/raw-business-materials.md:25)；[role-skill-inputs.json:251](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:251)；[role-skill-inputs.json:256](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:256)；[role-skill-inputs.json:241](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:241)

当前复核：**corrected-to-unknown-evidence-gap-remains**。本地修订将当前专家等级保留为null/evidence_insufficient，原4级仅作未证实的历史声明；生成分析为expert-evidence-unproven。未自动降为3级，也未认证专家支持能力。

当前证据：[skill-matrix.md:36](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:36)；[role-assessment.json:229](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/role-assessment.json:229)

### F02 · P2 · 企业架构师元数据遗漏物流分段

原始委托为订单、库存、物流；ROLE-EA.scope及TASK-EA.decision变为订单、库存、门店。构建器决策议程又写订单/库存/物流，形成不同视图责任口径不一致。

影响：物流确认交接与跨分段风险的协调责任可能只留在说明正文，而不进入角色任务定义。

建议：恢复订单/库存/物流主责任范围，门店作为受影响渠道一并列明；沿用同一个ROLE-EA及TASK-EA。

证据：[raw-business-materials.md:7](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/raw-business-materials.md:7)；[role-skill-inputs.json:34](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:34)；[role-skill-inputs.json:85](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:85)

当前复核：**corrected-in-local-copy**。ROLE-EA与TASK-EA已恢复订单、库存、物流分段责任，门店另列为渠道及运营参与者；生成的角色协作和技能矩阵保持同一ROLE-EA。

当前证据：[role-skill-inputs.json:35](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/role-skill-inputs.json:35)；[skill-matrix.md:18](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:18)

### F03 · P2 · 架构委员会被添加为决策主体但委托无此授权

MANDATE-STOCK将decision_owner写作架构委员会与库存业务负责人并引CASE-MANDATE；原文只说经营负责人委托分析，没有指定架构委员会或授予该组织审批权。

影响：候选治理建议可能被读成现有真实授权，形成证据来源错配。

建议：标记拟议治理责任待经营负责人确认，或补明确虚构授权材料；不以AI审阅代替确认。

证据：[raw-business-materials.md:7](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/raw-business-materials.md:7)；[role-skill-inputs.json:15](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:15)

当前复核：**authority-gap-explicitly-retained**。本地委托记录已写明经营负责人只委托分析，具体决定人、库存风险接受者和审批机制待确认；未凭架构委员会名称补造权限。

当前证据：[role-skill-inputs.json:15](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/role-skill-inputs.json:15)；[role-assignment.md:44](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:44)

### F04 · P1 · 人员有效期未覆盖离线试点后半段

ASSIGN-A有效期到2026-11-30，离线工作包/过渡计划到2026-12-04。工作量未知，40小时以及专家8小时不能说明整个期间覆盖。当前分析正确保留容量未知，但没有具体指出12月1日至4日覆盖未定。

影响：只按as_of核对有效性，会漏掉试点后半段人员与异常处理覆盖。

建议：在候选计划列为期间覆盖缺口，确认工作量、实际排期、续任/交接及专家容量；不能为通过检查直接延长有效期或补造估算。

证据：[role-skill-inputs.json:294](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:294)；[role-skill-inputs.json:295](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:295)；[build.py:81](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/build.py:81)

当前复核：**explicit-gap-remains-open**。GAP-ASSIGNMENT-PERIOD已进入所有相关生成制品。ASSIGN-A和DEV-A仍到11月30日，离线工作包到12月4日；这并不证明培训必须持续至交付最后一天，但尚无证据证明12月1日至4日的续任、交接、复评或替代覆盖。不得为消除日期差异而自动延长。

当前证据：[development-plan.json:112](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/development-plan.json:112)；[transition-roadmap.json:100](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/transition-roadmap.json:100)；[delivery-notebook.json:352](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/delivery-notebook.json:352)

### F05 · P2 · 门店持久化控制被单一中央库存控制范围吞并

断连版风险控制包括持久队列、检查点、冲突检测与人工补偿，但DELIVERY-NOTE的唯一CTRL-STOCK全部applies_to=APP-STOCK；APP-STORE和LOCAL-ORDER-RECORD的本地持久成功/掉电丢失风险没有对应控制范围。

影响：风险控制表可能误导为中央库存控制已覆盖本地断连数据丢失，即使详细恢复契约保留了未知。

建议：拆分门店持久记录控制与中央接收去重/对账控制；分别引用应用、记录边界、未决责任和验证场景，不虚构已通过。

证据：[raw-business-materials.md:25](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/raw-business-materials.md:25)；[build.py:124](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/build.py:124)

当前复核：**scope-corrected-verification-still-pending**。本地持久化与中央接收/重放已分为CTRL-LOCAL-DURABILITY、CTRL-CENTRAL-REPLAY，分别指向门店记录与中央恢复边界；控制仍为candidate，责任和故障验证仍未完成。

当前证据：[delivery-notebook.json:107](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/delivery-notebook.json:107)；[delivery-notebook.json:115](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/delivery-notebook.json:115)

### F06 · P2 · 角色技能传播来自案例分支，图影响尚未覆盖

REQ-OFFLINE的图可达结果有22个领域对象，不含DEV-A、DELIVERY-NOTE、任务技能目标或角色配置上下文；这些虽在本案例被显式分支更新，但影响引擎未给出相应依赖路径。

影响：本案例正确输出不能证明任意需求变化都能自动传递到技能目标和复评。

建议：补typed依赖或增加独立的任务/目标/发展引用影响分析；继续将图可达标为候选而非已证实全部影响。

证据：[build.py:172](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/build.py:172)；[build.py:302](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/build.py:302)

当前复核：**case-dependencies-added-general-capability-unproven**。新增CHANGE-DECISIONS、CHANGE-ROLE、CHANGE-DEVELOPMENT及配置关系后，图影响有39个候选，包括4角色、4任务、ASSIGN-A、两份证据状态、技能、DEV-A和DELIVERY-NOTE，全部待逐项确认。它证明本案例显式依赖可被遍历，尚不证明任意自然语言需求能自动发现或更新任务/技能/复评。

当前证据：[change-impact.json:50](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/change-impact.json:50)；[change-impact.json:318](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/change-impact.json:318)；[change-impact.json:32](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/change-impact.json:32)

### F07 · P2 · 四个角色均采用3级，裁剪依据仍过于通用

每条目标说明均为虚构主管采用3级，只有一条工作行为；已经正确区分原表参考与项目目标，但尚未解释任务复杂性、独立完成程度、所需复核和为何该级足够。

影响：可复用到真实项目时，容易退化为将等级字段填满而不是从工作要求推导目标。

建议：为每项任务补可观察的完成标准、预期独立性/支持条件和项目采用理由；如无决定保持拟议目标，不能让AI独立认可。

证据：[role-skill-inputs.json:166](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:166)；[role-skill-inputs.json:163](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/skills/_shared/examples/g249-omnichannel/role-skill-inputs.json:163)

当前复核：**tailoring-improved-project-adoption-not-business-approval**。四个3级目标已分别补投入取舍、跨分段互操作、库存运行数据、接口与恢复细节的采用理由，并说明困难情形仍需支持。adopted仅表示虚构教学场景中的目标状态；真实组织认可、行为证据与可用容量均未证实。

当前证据：[skill-matrix.md:30](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:30)；[skill-matrix.md:31](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:31)；[skill-matrix.md:33](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:33)；[skill-matrix.md:34](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:34)

### F08 · P1 · 角色分配主视图遗漏角色、任务与配置主体，空表仍获零覆盖错误

修复前，三组role-assignment视图只选择G249-ASSESSMENT-CONTEXT、0关系，Markdown主表为空；coverage仅检查所选上下文仍给零错误。该首次观察已归档，旧输出哈希只代表历史快照。当前修复结果见下方复核，不把旧问题描述当成当前状态。

影响：目录不能直接回答谁负责什么、需具备什么证据、配置何时有效；选错主体仍可获得形式覆盖通过，不能据此宣称已生成可用的角色配置制品。

建议：保持本地表达契约及缺主体拒绝机制；共享skills尚未采用该修复，不能推广为所有角色制品已解决。真实项目仍需确认任务、目标、能力、容量、期间及授权。

证据：[before-f08-fix.json:555](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/review-history/before-f08-fix.json:555)

当前复核：**local-case-fixed-regenerated-self-checked**。本地模型增加4任务、ASSIGN-A和2证据状态对象；主视图现含11个主体与7条关系，主Markdown显式呈现角色/任务/目标/配置/人员证据/发展/11项缺口。SVG和Mermaid可编辑，缺少任何必需主体时本地契约拒绝生成。ASSIGN-A仍至11月30日，12月1日至4日覆盖缺口和未批准状态保留。该复核包含修复作者自检，新增结果需由另一审阅者核验；不授予业务批准。

当前证据：[role-assignment.md:11](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:11)；[role-assignment.md:14](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:14)；[role-assignment.md:42](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:42)；[role-assignment.md:55](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:55)；[role-assignment.coverage.json:591](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.coverage.json:591)；[role-assignment.md:46](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:46)

### F09 · P2 · 共享对象变更验证只证明引用同步，未证明业务影响已分析

shared-object-change沿用CAP-RESERVE，只变名称和定义；实体、分析输入及上下文副本同步，目录/能力应用矩阵/路线图均引用同一ID。接口契约、风险、工作包、接受标准和批准仍维持原状态；该分支未运行图形渲染。

影响：名称与定义投影一致有助于避免多份对象分叉，但不能据此判定架构语义变化对接口和运营没有影响。

建议：先判断变更是编辑性重命名还是承诺/业务政策含义变化，再据显式依赖逐项复核接口、风险、工作包、接受条件及决定记录。此案例应标为稳定ID投影验证完成、业务语义影响待审，不把自动同步当业务接受。

证据：[shared-object-projections.json:23](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/shared-object-change/shared-object-projections.json:23)；[shared-object-projections.json:24](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/shared-object-change/shared-object-projections.json:24)；[shared-object-projections.json:25](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/shared-object-change/shared-object-projections.json:25)；[summary.json:28](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/summary.json:28)

## 生成结果复核

|输出|视图|实体|关系|schema错误|渲染状态|
|---|---:|---:|---:|---:|---|
|baseline|12|35|38|0|已运行|
|offline-change|13|41|53|0|已运行|
|shared-object-change|13|41|53|0|未运行|

上述数字是生成执行记录，不构成业务或内容充分性验收。

- **G01 · 人员证据、项目目标与配置批准分离**：两个人员观察均为证据不足，专家4级历史声明未转为现有能力。ASSIGN-A维持needs-evidence、capacity unresolved、approval not-granted；DEV-A未推断等级提升。
  证据：[role-assessment.json:210](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/role-assessment.json:210)；[role-assessment.json:211](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/role-assessment.json:211)；[role-assessment.json:238](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/role-assessment.json:238)
- **G02 · 离线约束已传播，通用自动分析能力仍有限**：断连版相较修复后基线新增6实体，保留35原实体与在线接口；离线行为进入TASK-SOL、REQ-SKILL-SOL、DEV-A。显式图依赖可达4角色、4任务、配置、证据、技能、发展与决策记录；所有候选待确认。
  证据：[skill-matrix.md:34](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/skill-matrix.md:34)；[change-impact.json:53](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/change-impact.json:53)；[change-impact.json:11](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/change-impact.json:11)
- **G03 · 角色分配主目录已修复为显式主体**：role-collaboration有4角色/5关系，skill-matrix有4角色+4技能/7关系。role-assignment有4角色+4任务+1配置+2证据状态/7关系；主表直接列出任务、目标、容量、期限与缺口，context只保留在分析执行模型。见F08。
  证据：[role-collaboration.json:46](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-collaboration.json:46)；[role-assignment.md:11](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:11)；[role-assignment.md:14](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.md:14)；[role-assignment.coverage.json:591](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/role-assignment.coverage.json:591)
- **G04 · 配置期间与发展计划覆盖**：发展和复评到11月30日，离线工作包到12月4日；日期差异本身不证明培训设计错误，但人员续任/交接与后续复评支持未证实。GAP-ASSIGNMENT-PERIOD已准确保留；见F04。
  证据：[development-plan.json:76](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/development-plan.json:76)；[transition-roadmap.json:100](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/transition-roadmap.json:100)；[delivery-notebook.json:352](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/delivery-notebook.json:352)
- **G05 · 共享对象多视图一致性**：CAP-RESERVE的名称和定义同步至catalog、capability_application_matrix和roadmap，应用仍APP-STOCK，工作包仍WP-ONLINE/WP-OFFLINE；这项检查仅证明稳定ID投影，语义影响未审，见F09。
  证据：[shared-object-projections.json:46](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/shared-object-change/shared-object-projections.json:46)；[shared-object-projections.json:78](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/shared-object-change/shared-object-projections.json:78)；[shared-object-projections.json:94](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/shared-object-change/shared-object-projections.json:94)
- **G06 · 物流与门店/中央数据边界**：生成状态迁移仍由ORDER-CONFIRMED进入ORDER-FULFIL；本地受理不自动承诺。门店持久化与中央去重/对账控制已分开，并保留责任、数据丢失和恢复指标的未知。
  证据：[order-states.md:28](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/order-states.md:28)；[delivery-notebook.json:107](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/delivery-notebook.json:107)；[delivery-notebook.json:115](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/offline-change/artifacts/delivery-notebook.json:115)
- **G07 · 缺主体反例与生成证据完整性**：删除任一必需角色、任务、人员配置、专家证据对象或配置证据关系时，本地表达契约拒绝生成。三分支共242项manifest输出哈希匹配；每份主目录4角色/4任务/1配置/2证据状态，11项分析缺口和未批准状态保持。
  证据：[assignment-verification.json:2](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/assignment-verification.json:2)；[assignment-verification.json:43](/Users/mac/Desktop/AI-TOGAF/togaf-standard-10th-ai/maintenance/cases/omnichannel/generated/assignment-verification.json:43)

## 审阅范围与未完成部分

已复核保存的模型、JSON、Markdown、覆盖登记、来源哈希和变更投影；F08本地修复后的主表、PNG与可编辑SVG/Mermaid由修复作者自检，另一审阅者复核待完成。未逐张目视验收其它视图，也未执行shared-object-change PNG渲染。角色分配主体缺失已修复，不等于真实任务、人员行为、容量或组织批准获证实；共享skills尚未采纳本地适配。

所有材料是虚构教学资料。独立AI审阅可识别逻辑和证据缺口，不授予真实业务批准、人员评级或上线权限。
