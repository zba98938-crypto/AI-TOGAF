# 冲刺DORP记录

ID：`dorp-record`。主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G210 §3.3.2、§5.5。定义状态：`guide-body-located-with-explicit-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

本冲刺是否达成目标、学到什么、哪些工作需要回流或进入下一次规划？

- 业务负责人
- 架构/产品团队
- 相关评审与治理人员
- 本冲刺是否达成目标、学到什么、哪些工作需要回流或进入下一次规划？
- 来源、边界与待决项


## 输入及缺口处理

必需：

- 明确冲刺目标与所选待办
- 演示观察及成果证据
- 未完成项/新需求
- 回顾及下一步行动责任

可选：

- 已有模型/待办/历史决策
- 组织特定规则及证据

缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。

## 元素、属性与关系

对象类型：guide:dorp_record。

```json
{
  "guide:dorp_record": [
    "sprint_ref",
    "goal",
    "demo",
    "outcomes",
    "retrospective",
    "next_plan",
    "returned_to_business_backlog",
    "new_backlog_requests",
    "review_at",
    "history"
  ]
}
```

{
  "sprint_ref": {
    "meaning": "DORP所审阅冲刺稳定ID；在独立调用时作为明确外部引用",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "goal": {
    "meaning": "整个冲刺的可验证目标；不能由选中事项标题自动代替",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "demo": {
    "meaning": "逐项实际展示内容、证据和未展示/失败观察，不是完成自报",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "outcomes": {
    "meaning": "相对于原目标的结论、完成/未完成集合及理由",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "retrospective": {
    "meaning": "对做法及结果的回顾，区分观察与推测根因",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "next_plan": {
    "meaning": "下一步建议的ID、行动、责任、时间和状态，不能冒充已批准承诺",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "returned_to_business_backlog": {
    "meaning": "未完成项回流业务待办的原始ID列表",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "new_backlog_requests": {
    "meaning": "新提出但可能尚未澄清/估算的需求，不默认承诺",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "review_at": {
    "meaning": "DORP的评审时点，用于保留历史目标判断",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "history": {
    "meaning": "按观察时间保留状态/结论与证据的历史，不由后续结果覆盖",
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

## 分析步骤

1. 先固定本次冲刺目标和评审时点，不因结果不好而改写目标。
2. 按Demo记录实际展示和未展示内容；按Outcome核对目标与成果。
3. 按Retrospective解释偏差与可改进做法，不将推测当根因事实。
4. 按Planning形成有责任人与依据的下一步建议；未完成项回到业务待办。
5. 新需求先登记澄清，不自动承诺下一冲刺；保留历史与后续补充。

## 输出、检查与误读

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

- Demo/Outcome/Retrospective/Planning四项分别存在
- 有强制冲刺目标，结论对应同一目标
- 完成和未完成集不交叉，未完成集全部回流
- 未展示或缺证据的成果不标完成
- 后续完成不能倒改原冲刺历史失败

- DORP不是只写会议纪要或四个空标题
- 不能把演示次数代替价值
- 下次计划是建议，非批准或实际已完成


## 视图和交付物

- [DORP四活动记录](../profiles/dorp-record-default.md)

- [change-request](../deliverables/change-request.md)
- [compliance-assessment](../deliverables/compliance-assessment.md)
- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「冲刺DORP记录」给出：DORP不是只写会议纪要或四个空标题",
    "expected": "empty-view",
    "why": "DORP不是只写会议纪要或四个空标题"
  },
  "modification_example": {
    "change": "在「冲刺DORP记录」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/dorp-record.md)

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
      "id": "DORP-01",
      "type": "guide:dorp_record",
      "name": "SP-01结束DORP记录",
      "attributes": {
        "sprint_ref": "SP-01",
        "goal": "形成可供两馆审阅的身份与预约契约包，包含审计事件",
        "demo": [
          {
            "item": "BL-01",
            "evidence": "DEMO-01 / BR-07",
            "observation": "同名异证分开且有人工复核分支"
          },
          {
            "item": "BL-03",
            "evidence": "AUD-01 / BR-07",
            "observation": "审计清单已形成"
          },
          {
            "item": "BL-02",
            "evidence": "BR-07",
            "observation": "取消后重约约束缺失，未完成"
          }
        ],
        "outcomes": {
          "goal_result": "not-achieved",
          "completed": [
            "BL-01",
            "BL-03"
          ],
          "incomplete": [
            "BL-02"
          ],
          "reason": "API契约关键状态缺失，整体包不满足目标"
        },
        "retrospective": "乙馆接口负责人介入过晚，状态语义直到最后一天才暴露",
        "next_plan": [
          {
            "id": "ACT-01",
            "action": "邀请乙馆负责人澄清取消规则并评审取值",
            "owner": "接口负责人",
            "target_date": "2026-11-09",
            "status": "proposed"
          }
        ],
        "returned_to_business_backlog": [
          "BL-02"
        ],
        "new_backlog_requests": [
          {
            "id": "REQ-SMS",
            "description": "短信通知模板",
            "status": "needs-clarification",
            "estimate": null
          }
        ],
        "review_at": "2026-11-06",
        "history": [
          {
            "at": "2026-11-06",
            "goal_result": "not-achieved",
            "evidence": "BR-07"
          }
        ]
      },
      "evidence": [
        "BR-06",
        "BR-07",
        "BR-08"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "view": {
    "id": "v-dorp-record-default",
    "artifact_id": "dorp-record",
    "profile_id": "dorp-record-default",
    "title": "冲刺DORP记录／虚构跨馆案例",
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
      "DORP-01"
    ],
    "relationship_ids": [],
    "analysis": "见analysis.md逐项原料→判断→结果；字段中的状态均是案例观察，不代表生产实施或批准。",
    "legend": "表格行以稳定ID区分；未知保留unknown，空列表表示明确没有该项；关系表按类型和端点解释。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact dorp-record --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
