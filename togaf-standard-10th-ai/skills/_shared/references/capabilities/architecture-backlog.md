# 架构业务变革与冲刺待办

ID：`architecture-backlog`。主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G210 §2、§3.3.2–3.3.4；G20F §4.5、§5.2.3、§5.3.2；G20F §4.5 L304–327；G20F §5.2.3 L529–547；G20F §5.3.2 L601–632。定义状态：`guide-body-located-with-explicit-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

先处理哪些业务变革，当前团队冲刺承诺哪些架构结果？

- 业务负责人
- 架构/产品团队
- 相关评审与治理人员
- 先处理哪些业务变革，当前团队冲刺承诺哪些架构结果？
- 来源、边界与待决项


## 输入及缺口处理

必需：

- 原始目标/需求/变更及来源
- 业务优先级及理由
- 依赖与验收条件
- 团队时间盒、目标、可用容量及估算依据

可选：

- 已有模型/待办/历史决策
- 组织特定规则及证据

缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。

## 元素、属性与关系

对象类型：guide:backlog_item, guide:sprint, goal, requirement, abb, sbb, guide:mva_scope。

```json
{
  "guide:backlog_item": [
    "backlog_scope",
    "business_value",
    "priority",
    "priority_basis",
    "owner",
    "status",
    "acceptance_criteria",
    "estimate",
    "sprint_id",
    "dependencies",
    "source_refs",
    "history"
  ],
  "guide:sprint": [
    "goal",
    "timebox",
    "team",
    "capacity",
    "selected_item_ids",
    "planning_status",
    "outcome",
    "snapshot_at"
  ]
}
```

{
  "backlog_scope": {
    "meaning": "需求所属的业务变革待办范围；冲刺选择以关系和sprint_id表达",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "business_value": {
    "meaning": "需求对相关利益人的预期增量价值，允许定性且需来源",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "priority": {
    "meaning": "利益相关者明确给定的相对顺序；不是量化价值评分",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "priority_basis": {
    "meaning": "排序依据及提出该判断的来源，不由行号推断",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "owner": {
    "meaning": "负责澄清、交付或处理该项的角色；不是隐含审批人",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "status": {
    "meaning": "该工作产品自身的业务流程状态，独立于模型批准/实现状态",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "acceptance_criteria": {
    "meaning": "判断待办成果达成的可检查条件，须符合原始目标",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "estimate": {
    "meaning": "带数值或null、单位、依据与estimated/unknown状态的项目估算",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "sprint_id": {
    "meaning": "所选冲刺稳定ID，未分配为unassigned；多次选择保留history",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "dependencies": {
    "meaning": "前置待办ID，与guide:backlog_depends_on关系逐项一致",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "source_refs": {
    "meaning": "支持本条业务内容的来源ID列表，区别指南定义来源",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "history": {
    "meaning": "按观察时间保留状态/结论与证据的历史，不由后续结果覆盖",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "goal": {
    "meaning": "整个冲刺的可验证目标；不能由选中事项标题自动代替",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "timebox": {
    "meaning": "项目声明的开始、结束日期及来源；不是TOGAF固定周期",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "team": {
    "meaning": "本冲刺共同负责交付的团队范围",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "capacity": {
    "meaning": "含value、unit、basis的可用投入；未知不能按零处理",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "selected_item_ids": {
    "meaning": "冲刺选择的待办稳定ID；与选择关系一致",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "planning_status": {
    "meaning": "该时间点的冲刺规划状态，不代替结果",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "outcome": {
    "meaning": "冲刺规划时点是否已有成果观察；未观察需明示",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "snapshot_at": {
    "meaning": "当前规划记录所对应的观察时点",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "name": {
    "meaning": "工作产品对象的业务名称",
    "value_rule": "使用范围内可识别的业务名称；身份由稳定ID确定，不以同名合并对象",
    "definition_origin": "project-operational-convention",
    "value_schema": {
      "type": "string",
      "minLength": 1,
      "pattern": "\\S"
    }
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `guide:backlog_depends_on` | guide:backlog_item → guide:backlog_item | 源待办以目标待办成果作为前置；不是优先级关系 |
| `guide:scheduled_in` | guide:backlog_item → guide:sprint | 某日期将待办选入冲刺；不表示完成或投产 |
| `g20f:refines` | goal,requirement → requirement | 本项目声明的战略意图到epic/feature/story逐层细化，不是流程先后 |
| `g20f:constrains-story` | abb → requirement | ABB对故事给出功能/非功能护栏 |
| `g20f:allocated-to-sbb` | requirement → sbb | 故事分配到候选SBB实现，不表示已实现 |
| `g20f:included-in-mva` | requirement → guide:mva_scope | 显式必须项纳入命名MVA边界，非已验收或完整MVP |
| `g20f:story-depends-on` | requirement → requirement | 依赖方故事指向前置故事，非优先级或完成顺序断言 |
| `realizes` | function,outcome,sbb,technology → abb,business_service,goal,technology_service | 实现规定的服务、构建块或目标；成果到目标表示达成，不表示目标导致成果。 |

## 分析步骤

1. 将每项业务需求归一为稳定ID，保留来源、价值、责任人与验收条件；未知不填零。
2. 依据利益相关者给定排序及依赖确定候选顺序；没有权重时不计算分数。
3. 区分业务变革范围与团队冲刺范围；以相同ID选择近期工作，记录目标与容量。
4. 核对前置工作及所选估算是否在声明容量内；未知估算不能给出容量通过。
5. 以演示证据更新状态；未完成项回流业务待办，保存历史且不自动承诺下一冲刺。

## 输出、检查与误读

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

- 业务优先级有证据；编号顺序不等同关系方向
- 每个选中项能关联冲刺目标、估算依据和验收条件
- 依赖无环；依赖可在冲刺内先完成或有既成证据
- 容量单位一致；未知不能计零
- 未完成工作保留原ID并回流；历史冲刺记录不重写

- 不把速率当项目完成度
- 不固定1–4周为所有组织规则
- 业务待办与冲刺待办是同族两视图，不复制身份或双计制品
- 本例优先级和人日是项目规则，不是TOGAF权重


## 视图和交付物

- [业务变革待办](../profiles/architecture-business-backlog.md)
- [团队冲刺待办](../profiles/architecture-sprint-backlog.md)
- [战略—MVA—产品待办追溯](../profiles/architecture-strategic-mva-trace.md)

- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)
- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)
- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构业务变革与冲刺待办」给出：不把速率当项目完成度",
    "expected": "missing-evidence",
    "why": "不把速率当项目完成度"
  },
  "modification_example": {
    "change": "在「架构业务变革与冲刺待办」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/architecture-backlog.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构跨城图书互借案例；不代表真实批准、实现或原图复刻。",
  "raw_input": "examples/addenda/new-work-products/raw-brief.md",
  "analysis_path": "examples/addenda/new-work-products/analysis.md",
  "sources": [
    {
      "id": "BR-01",
      "kind": "example",
      "description": "甲、乙、丙三个图书馆计划允许读者跨馆预约并在常用馆取书。三套目录系统使用不同读者标识，同名读者不能直接合并。业务负责人关心错误关联和等待解释。",
      "locator": "raw-brief.md#BR-01"
    },
    {
      "id": "BR-02",
      "kind": "example",
      "description": "试点首先需要一份跨馆读者身份核对规则；验收条件是区分姓名相同但证件信息不同的两名测试读者，记录无法判定的情形并交人工复核。责任人是借阅业务负责人。",
      "locator": "raw-brief.md#BR-02"
    },
    {
      "id": "BR-03",
      "kind": "example",
      "description": "第二项需要提供跨馆预约 API 契约。它依赖身份核对规则；需明确读者标识、预约状态、失败返回和消费者。接口负责人估计需 1 人日。",
      "locator": "raw-brief.md#BR-03"
    },
    {
      "id": "BR-04",
      "kind": "example",
      "description": "第三项需要试点审计事件清单，记录谁在何时因何理由关联读者，并区分原值与修改值。数据治理负责人估计需 1 人日。",
      "locator": "raw-brief.md#BR-04"
    },
    {
      "id": "BR-05",
      "kind": "example",
      "description": "架构团队在 2026-11-02 至 2026-11-06 的冲刺 SP-01 可投入 4 人日，已经扣除例会和日常支持。身份规则估计需 2 人日；预约页面配色提案估计需 0.5 人日。该工时与日期是本例项目规则。业务负责人按“身份正确性 → 对外预约契约 → 审计可解释性 → 配色探索”排序，未采用加权分数。",
      "locator": "raw-brief.md#BR-05"
    },
    {
      "id": "BR-06",
      "kind": "example",
      "description": "SP-01 的目标是“形成可供两馆审阅的身份与预约契约包，包含审计事件”；这些是待评审设计结果，不能声称已投产。页面配色与此目标关系较弱，未选入本冲刺。团队在 11 月 2 日选择了身份规则、API 契约和审计清单。",
      "locator": "raw-brief.md#BR-06"
    },
    {
      "id": "BR-07",
      "kind": "example",
      "description": "11 月 6 日演示中，身份规则正确分开两名同名测试读者，材料 DEMO-01 记录了人工复核分支；审计清单 AUD-01 已形成。预约契约仍缺乙馆“取消后重新预约”的状态约束，未完成。总体冲刺目标未达成。未完成项应回到业务变革待办，不能直接宣称顺延已获准。",
      "locator": "raw-brief.md#BR-07"
    },
    {
      "id": "BR-08",
      "kind": "example",
      "description": "回顾发现乙馆接口负责人直到最后一天才参与。下一次先邀请该负责人澄清取消规则，并评审旧系统状态取值；记录行动 ACT-01，负责人接口负责人，目标日期 11 月 9 日。11 月 6 日还收到“短信通知模板”的新需求，记为待澄清，尚无估算，不自动承诺下个冲刺。",
      "locator": "raw-brief.md#BR-08"
    },
    {
      "id": "BR-09",
      "kind": "example",
      "description": "对试点 API 的内部命名，项目提出采用 consult：架构负责人先听取开发团队意见，再由架构负责人做出记录化决策。可逆性依据是当前无外部消费者，保留旧别名并能恢复路由；一旦有外部消费者即重新评估。此为拟定授权安排，尚未获正式批准。",
      "locator": "raw-brief.md#BR-09"
    },
    {
      "id": "BR-10",
      "kind": "example",
      "description": "删除读者关联的历史证据无法以普通回滚恢复。因此保留期限变更应由数据治理、借阅业务与安全负责人共同达成一致（agree）；在依据和共同决策完成前不执行。其他例中的 tell/sell/advise/inquire/delegate 仅为 G210 引用的外部 Management 3.0 名称，本项目并未默认授权所有事项。",
      "locator": "raw-brief.md#BR-10"
    },
    {
      "id": "BR-11",
      "kind": "example",
      "description": "试点日志展示样式由开发团队在既定脱敏与访问护栏内提出 delegate；更改不触及保留期限或审计字段，能切回旧模板。没有正式授权证明，因此仍为 proposed。",
      "locator": "raw-brief.md#BR-11"
    },
    {
      "id": "BR-12",
      "kind": "example",
      "description": "评审材料 DESC-01 是一张版本化、通过语法检查的“统一读者”图；它遗漏乙馆与丙馆的身份冲突和人工复核责任。当前决策是能否开始接口契约评审，故它内容不足，即使已经使用正式模型表示。",
      "locator": "raw-brief.md#BR-12"
    },
    {
      "id": "BR-13",
      "kind": "example",
      "description": "DESC-02 是给内部访谈的临时预约页面草图，只用于判断读者是否理解跨馆取书。已有访谈目的、对象和问题，尚无需求可行性证据；此时要求完整生产部署与容灾模型会增加与当前决策无关的工作。项目只要求标明假设、边界与版本。",
      "locator": "raw-brief.md#BR-13"
    },
    {
      "id": "BR-14",
      "kind": "example",
      "description": "DESC-03 是准备进入契约审阅的预约接口说明，已有输入输出、错误码、消费者、范围、版本和待决问题；它仍缺 BR-07 的取消状态。因此在该问题补齐前只能作为审阅草稿，不能宣称足够支持发布，也不能把 approved 当成正式度。",
      "locator": "raw-brief.md#BR-14"
    },
    {
      "id": "BR-15",
      "kind": "example",
      "description": "债务 DEBT-01：三系统各自复制姓名匹配规则且责任不清；同名读者有被误关联的风险。影响跨馆借阅与身份管理两个产品范围，需要 EA 协调语义与责任；偿还候选是统一最小规则和人工复核接口，对应身份规则待办。",
      "locator": "raw-brief.md#BR-15"
    },
    {
      "id": "BR-16",
      "kind": "example",
      "description": "债务 DEBT-02：单馆报表仍使用过期的 CSV 转码脚本；运行人员每周手工重跑一次。影响仅甲馆报表，暂无跨产品影响证据，由该产品团队处理即可；候选改动是补自动转码校验，估算未知。",
      "locator": "raw-brief.md#BR-16"
    },
    {
      "id": "BR-17",
      "kind": "example",
      "description": "债务 DEBT-03：预约状态接口在两份文档中命名不一致，令消费者重复编写映射。需接口团队与业务共同统一词汇；候选偿还对应 API 契约待办。未提供损失金额、利率或任何货币折算规则。",
      "locator": "raw-brief.md#BR-17"
    },
    {
      "id": "BR-18",
      "kind": "example",
      "description": "修改试验材料：11 月 9 日乙馆给出取消规则，并在 DEMO-02 中验证 API 的取消和重新预约，API 项可标为设计完成（不是投产）；DESC-03 加入该证据后足以支持契约审阅。DEBT-03 的两个消费者回归结果 TEST-03 表明映射一致，可按本例关闭规则关闭该债项。新证据不改变原冲刺目标未达成的历史记录。",
      "locator": "raw-brief.md#BR-18"
    },
    {
      "id": "BR-19",
      "kind": "example",
      "description": "第二个修改试验：API 命名现在已有一名外部消费者，旧别名不能完全恢复其缓存状态；把 BR-09 的可逆性改为 unknown，原自治安排必须保持 proposed 并补更广利益相关者评审，不能把未知当可逆。",
      "locator": "raw-brief.md#BR-19"
    },
    {
      "id": "BR-20",
      "kind": "example",
      "description": "本例关闭债务的项目规则：需记录修复交付引用、验证证据和责任人复核结论；仅“已排计划”或“工时已消耗”不能关闭。描述评审使用“是否足够支持指定决策”和“当前正式控制是否适合目的”两独立判断，采用文字理由，不使用数值等级或总分。",
      "locator": "raw-brief.md#BR-20"
    }
  ],
  "entities": [
    {
      "id": "BL-01",
      "type": "guide:backlog_item",
      "name": "跨馆身份核对规则",
      "attributes": {
        "backlog_scope": "business-change",
        "business_value": "避免同名读者误关联，明确人工复核责任",
        "priority": 1,
        "priority_basis": "BR-05业务负责人显式排序；无权重",
        "owner": "借阅业务负责人",
        "status": "selected",
        "acceptance_criteria": "区分同名异证测试读者，并保留未知情形的人工复核分支",
        "estimate": {
          "value": 2,
          "unit": "person-day",
          "basis": "BR-05",
          "status": "estimated"
        },
        "sprint_id": "SP-01",
        "dependencies": [],
        "source_refs": [
          "BR-02"
        ],
        "history": [
          {
            "at": "2026-11-02",
            "status": "selected",
            "evidence": "BR-06"
          }
        ]
      },
      "evidence": [
        "BR-01",
        "BR-02",
        "BR-05",
        "BR-06"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "BL-02",
      "type": "guide:backlog_item",
      "name": "预约API契约",
      "attributes": {
        "backlog_scope": "business-change",
        "business_value": "使两馆能按共同标识及状态开展契约审阅",
        "priority": 2,
        "priority_basis": "BR-05显式排序；先解决身份前置",
        "owner": "接口负责人",
        "status": "selected",
        "acceptance_criteria": "明确读者标识、预约状态、失败返回与消费者，包括取消后重约约束",
        "estimate": {
          "value": 1,
          "unit": "person-day",
          "basis": "BR-03",
          "status": "estimated"
        },
        "sprint_id": "SP-01",
        "dependencies": [
          "BL-01"
        ],
        "source_refs": [
          "BR-03"
        ],
        "history": [
          {
            "at": "2026-11-02",
            "status": "selected",
            "evidence": "BR-06"
          }
        ]
      },
      "evidence": [
        "BR-03",
        "BR-05",
        "BR-06"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "BL-03",
      "type": "guide:backlog_item",
      "name": "试点审计事件清单",
      "attributes": {
        "backlog_scope": "business-change",
        "business_value": "支持关联读者操作的责任和修改解释",
        "priority": 3,
        "priority_basis": "BR-05显式排序；与冲刺目标直接相关",
        "owner": "数据治理负责人",
        "status": "selected",
        "acceptance_criteria": "列谁/何时/理由/原值/修改值，并关联身份复核过程",
        "estimate": {
          "value": 1,
          "unit": "person-day",
          "basis": "BR-04",
          "status": "estimated"
        },
        "sprint_id": "SP-01",
        "dependencies": [],
        "source_refs": [
          "BR-04"
        ],
        "history": [
          {
            "at": "2026-11-02",
            "status": "selected",
            "evidence": "BR-06"
          }
        ]
      },
      "evidence": [
        "BR-04",
        "BR-05",
        "BR-06"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "BL-04",
      "type": "guide:backlog_item",
      "name": "预约页面配色探索",
      "attributes": {
        "backlog_scope": "business-change",
        "business_value": "待访谈确认是否改善理解；不是当前冲刺的必要输出",
        "priority": 4,
        "priority_basis": "BR-05显式排序；与本冲刺目标关系较弱",
        "owner": "业务负责人",
        "status": "open",
        "acceptance_criteria": "需补访谈问题与期望改善；当前待澄清",
        "estimate": {
          "value": 0.5,
          "unit": "person-day",
          "basis": "BR-05",
          "status": "estimated"
        },
        "sprint_id": "unassigned",
        "dependencies": [],
        "source_refs": [
          "BR-05"
        ],
        "history": [
          {
            "at": "2026-11-02",
            "status": "open",
            "evidence": "BR-06"
          }
        ]
      },
      "evidence": [
        "BR-05",
        "BR-06"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "SP-01",
      "type": "guide:sprint",
      "name": "两馆身份与预约契约包冲刺",
      "attributes": {
        "goal": "形成可供两馆审阅的身份与预约契约包，包含审计事件",
        "timebox": {
          "start": "2026-11-02",
          "end": "2026-11-06",
          "source": "BR-05"
        },
        "team": "跨馆架构团队",
        "capacity": {
          "value": 4,
          "unit": "person-day",
          "basis": "BR-05；已扣日常支持"
        },
        "selected_item_ids": [
          "BL-01",
          "BL-02",
          "BL-03"
        ],
        "planning_status": "planned",
        "outcome": "not-yet-observed-at-planning",
        "snapshot_at": "2026-11-02"
      },
      "evidence": [
        "BR-05",
        "BR-06"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [
    {
      "id": "REL-BL-02-01",
      "type": "guide:backlog_depends_on",
      "source": "BL-02",
      "target": "BL-01",
      "label": "预约契约以身份核对规则为前置",
      "evidence": [
        "BR-03"
      ],
      "certainty": "assumed"
    },
    {
      "id": "REL-BL-01-SP",
      "type": "guide:scheduled_in",
      "source": "BL-01",
      "target": "SP-01",
      "label": "2026-11-02选择进入本冲刺；不代表完成",
      "evidence": [
        "BR-06"
      ],
      "certainty": "assumed"
    },
    {
      "id": "REL-BL-02-SP",
      "type": "guide:scheduled_in",
      "source": "BL-02",
      "target": "SP-01",
      "label": "2026-11-02选择进入本冲刺；不代表完成",
      "evidence": [
        "BR-06"
      ],
      "certainty": "assumed"
    },
    {
      "id": "REL-BL-03-SP",
      "type": "guide:scheduled_in",
      "source": "BL-03",
      "target": "SP-01",
      "label": "2026-11-02选择进入本冲刺；不代表完成",
      "evidence": [
        "BR-06"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "guide:backlog_depends_on": {
        "source_types": [
          "guide:backlog_item"
        ],
        "target_types": [
          "guide:backlog_item"
        ],
        "meaning": "源待办以目标待办成果作为前置；不是优先级关系"
      },
      "guide:scheduled_in": {
        "source_types": [
          "guide:backlog_item"
        ],
        "target_types": [
          "guide:sprint"
        ],
        "meaning": "某日期将待办选入冲刺；不表示完成或投产"
      }
    }
  },
  "view": {
    "id": "v-architecture-business-backlog",
    "artifact_id": "architecture-backlog",
    "profile_id": "architecture-business-backlog",
    "title": "架构业务变革与冲刺待办／虚构跨馆案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "BL-01",
      "BL-02",
      "BL-03",
      "BL-04",
      "SP-01"
    ],
    "relationship_ids": [
      "REL-BL-02-01",
      "REL-BL-01-SP",
      "REL-BL-02-SP",
      "REL-BL-03-SP"
    ],
    "analysis": "见analysis.md逐项原料→判断→结果；字段中的状态均是案例观察，不代表生产实施或批准。",
    "legend": "表格行以稳定ID区分；未知保留unknown，空列表表示明确没有该项；关系表按类型和端点解释。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-backlog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
