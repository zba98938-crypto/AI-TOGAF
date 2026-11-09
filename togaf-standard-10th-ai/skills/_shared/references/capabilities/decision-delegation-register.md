# 决策授权与可逆性登记

ID：`decision-delegation-register`。主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G210 §5.4（转引Management 3.0及Bezos）。定义状态：`guide-body-located-with-explicit-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

某类决策由谁、在何种边界内决定，何时需扩大参与或重新评审？

- 业务负责人
- 架构/产品团队
- 相关评审与治理人员
- 某类决策由谁、在何种边界内决定，何时需扩大参与或重新评审？
- 来源、边界与待决项


## 输入及缺口处理

必需：

- 决策范围和影响对象
- 参与人、权限与企业护栏
- 可逆性证据和回滚条件
- 组织采用的授权规则及批准状态

可选：

- 已有模型/待办/历史决策
- 组织特定规则及证据

缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。

## 元素、属性与关系

对象类型：guide:delegation_decision。

```json
{
  "guide:delegation_decision": [
    "decision_scope",
    "delegation_level",
    "framework_origin",
    "authority",
    "participants",
    "reversibility",
    "reversibility_evidence",
    "rollback_plan",
    "guardrails",
    "authorization_status",
    "review_trigger",
    "decision_result",
    "source_refs"
  ],
  "decision_record": [
    "question",
    "options_considered",
    "decision",
    "authority",
    "rationale",
    "date"
  ]
}
```

{
  "decision_scope": {
    "meaning": "授权适用的具体决定、对象和影响边界",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "delegation_level": {
    "meaning": "G210引用的Management3.0名称之一；只作词汇，具体权责另列",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "framework_origin": {
    "meaning": "外部方法归属与项目操作化说明，防止冒充TOGAF独创",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "authority": {
    "meaning": "谁在听取谁意见后做何种决定的项目明文约定",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "participants": {
    "meaning": "需要参与当前决策的团队或角色，不仅列被通知人",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "reversibility": {
    "meaning": "reversible/irreversible/unknown；对整个决定结果而非单一技术动作判断",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "reversibility_evidence": {
    "meaning": "支持可逆性判断的业务与技术证据或明确缺口",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "rollback_plan": {
    "meaning": "回滚方式、条件与未覆盖部分；不可回滚明确not-available",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "guardrails": {
    "meaning": "授权不能突破的企业/项目约束及范围",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "authorization_status": {
    "meaning": "授权安排本身的proposed/approved等状态；批准需要真实证据",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "review_trigger": {
    "meaning": "哪些范围、消费者、规则或恢复条件变化要求复评",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "decision_result": {
    "meaning": "当前决定或建议及未决条件，不由授权级别自动推导",
    "value_rule": "必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。",
    "definition_origin": "project-operational-contract-guided-by-cited-body"
  },
  "source_refs": {
    "meaning": "支持本条业务内容的来源ID列表，区别指南定义来源",
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

1. 为具体决策划清范围、受影响方及护栏。
2. 记录reversible/irreversible/unknown及依据；未知不能默认为可逆。
3. 可选引用七授权名称tell/sell/consult/agree/advise/inquire/delegate，逐条用项目语言明确定谁决定、谁参与。
4. 不可逆或可逆性不明时明确更广群体及需补证据；不从数值等级自动推导批准。
5. 记录提案、批准证据与复评触发，授权状态与架构实现状态独立。

## 输出、检查与误读

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

- 七名称来自外部方法；权责描述与组织约定一致
- 可逆有回滚条件与证据；unknown不当作reversible
- 不可逆决策有跨相关团队参与安排
- 无批准证据只能proposed，不实际执行
- 决策影响变化触发复评

- 七级不是TOGAF成熟度评分
- “高授权级”不代表更好
- 来源转引不等于已核实完整Management3.0规则
- 用户使用本技能不构成外部业务授权


## 视图和交付物

- [决策授权与可逆性登记](../profiles/decision-delegation-register-default.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [compliance-assessment](../deliverables/compliance-assessment.md)


- [implementation-governance-model](../deliverables/implementation-governance-model.md)

项目路由：F阶段在适用时（if any）准备实施治理模型；G阶段使用其检查点、决策权和升级规则进行实施治理。关联工作产品不自动创建必需交付物、不代替适用性裁剪或真实授权。

## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「决策授权与可逆性登记」给出：七级不是TOGAF成熟度评分",
    "expected": "missing-evidence",
    "why": "七级不是TOGAF成熟度评分"
  },
  "modification_example": {
    "change": "在「决策授权与可逆性登记」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/decision-delegation-register.md)

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
      "id": "DEC-01",
      "type": "guide:delegation_decision",
      "name": "试点API内部命名权限",
      "attributes": {
        "decision_scope": "仅无外部消费者的试点API内部命名",
        "delegation_level": "consult",
        "framework_origin": "Management 3.0，G210 §5.4转引；具体权责为本例项目规则",
        "authority": "架构负责人听取开发团队意见后决定",
        "participants": [
          "架构负责人",
          "开发团队"
        ],
        "reversibility": "reversible",
        "reversibility_evidence": "无外部消费者；保留旧别名且可恢复路由（BR-09）",
        "rollback_plan": "恢复旧别名与路由；一旦增加外部消费者重新评估",
        "guardrails": [
          "不改变契约业务语义",
          "不涉及读者证据删除"
        ],
        "authorization_status": "proposed",
        "review_trigger": "新增外部消费者或无法恢复路由",
        "decision_result": "拟采用consult，待正式授权",
        "source_refs": [
          "BR-09"
        ]
      },
      "evidence": [
        "BR-09"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "DEC-02",
      "type": "guide:delegation_decision",
      "name": "读者关联证据保留期限变更",
      "attributes": {
        "decision_scope": "读者关联历史证据的保留期限",
        "delegation_level": "agree",
        "framework_origin": "Management 3.0及可逆性区分由G210 §5.4转引；本例约定共同决策",
        "authority": "数据治理、借阅业务与安全负责人共同决策",
        "participants": [
          "数据治理负责人",
          "借阅业务负责人",
          "安全负责人"
        ],
        "reversibility": "irreversible",
        "reversibility_evidence": "删除历史证据后普通回滚不可恢复（BR-10）",
        "rollback_plan": "not-available；决策完成前不得执行删除",
        "guardrails": [
          "不得凭技术团队单方决定",
          "先补保留依据与影响"
        ],
        "authorization_status": "proposed",
        "review_trigger": "法律/业务依据或数据范围变化",
        "decision_result": "需更广群体共同评审；依据未齐保持草稿",
        "source_refs": [
          "BR-10"
        ]
      },
      "evidence": [
        "BR-10"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "DEC-03",
      "type": "guide:delegation_decision",
      "name": "脱敏日志展示样式权限",
      "attributes": {
        "decision_scope": "既有脱敏/访问护栏内的展示样式",
        "delegation_level": "delegate",
        "framework_origin": "Management 3.0，G210 §5.4转引；本例拟委派规则",
        "authority": "拟由开发团队决定并留存变更记录",
        "participants": [
          "开发团队",
          "日志使用者"
        ],
        "reversibility": "reversible",
        "reversibility_evidence": "可切回旧模板，保留期限/字段不变（BR-11）",
        "rollback_plan": "切回旧展示模板并检查脱敏",
        "guardrails": [
          "不改保留期限",
          "不改审计字段",
          "保持访问与脱敏规则"
        ],
        "authorization_status": "proposed",
        "review_trigger": "涉及保留期限、字段或脱敏规则",
        "decision_result": "授权仅为提案，未实施",
        "source_refs": [
          "BR-11"
        ]
      },
      "evidence": [
        "BR-11"
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
    "id": "v-decision-delegation-register-default",
    "artifact_id": "decision-delegation-register",
    "profile_id": "decision-delegation-register-default",
    "title": "决策授权与可逆性登记／虚构跨馆案例",
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
      "DEC-01",
      "DEC-02",
      "DEC-03"
    ],
    "relationship_ids": [],
    "analysis": "见analysis.md逐项原料→判断→结果；字段中的状态均是案例观察，不代表生产实施或批准。",
    "legend": "表格行以稳定ID区分；未知保留unknown，空列表表示明确没有该项；关系表按类型和端点解释。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact decision-delegation-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
