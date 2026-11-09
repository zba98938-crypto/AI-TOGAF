# 技术与架构债登记表

`profile_id`: technical-debt-register-default；`artifact_id`: technical-debt-register；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G217 §2.2–2.3、附录D.4。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addendum-1。

{
  "id": "technical-debt-register-default",
  "version": "1.0",
  "source_verified": false,
  "reference_identity": "正文操作化表格，不是来源图复刻",
  "layout_notes": "保留ID、字段、来源与关系表；长文可分节/分页，不能截断为摘要。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:technical_debt。关系类型：。

```json
{
  "entities": {
    "guide:technical_debt": [
      "kind",
      "affected_products",
      "cause",
      "consequence",
      "evidence_summary",
      "ea_involvement",
      "ea_rationale",
      "repayment_option",
      "backlog_refs",
      "owner",
      "review_date",
      "status",
      "closure_criteria",
      "verification_evidence",
      "closure_decision",
      "cost_or_interest"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 原因、后果、范围和负责人明确
- EA介入有跨产品或全局理由
- 偿还与待办可追溯
- 未知成本不填零、不自动算利息
- 关闭有验证及复核，原始观察保留

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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
      "id": "DEBT-01",
      "type": "guide:technical_debt",
      "name": "三馆重复身份匹配规则",
      "attributes": {
        "kind": "architecture-and-data-semantics",
        "affected_products": [
          "跨馆借阅",
          "身份管理"
        ],
        "cause": "三系统复制规则且责任不清",
        "consequence": "同名误关联与复核责任缺失",
        "evidence_summary": "BR-15虚构问题记录；未提供发生概率或损失金额",
        "ea_involvement": "cross-product-coordination",
        "ea_rationale": "需要跨两个产品与三馆统一语义/责任",
        "repayment_option": "统一最小身份规则及人工复核接口",
        "backlog_refs": [
          "BL-01"
        ],
        "owner": "借阅业务负责人和EA协调人",
        "review_date": "2026-11-09",
        "status": "selected",
        "closure_criteria": "修复交付引用、验证证据、责任人复核（BR-20项目规则）",
        "verification_evidence": [],
        "closure_decision": "not-closed",
        "cost_or_interest": "unknown；无货币公式/利率来源"
      },
      "evidence": [
        "BR-15"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "DEBT-02",
      "type": "guide:technical_debt",
      "name": "甲馆CSV转码重跑",
      "attributes": {
        "kind": "technical-local",
        "affected_products": [
          "甲馆报表"
        ],
        "cause": "过期转码脚本缺自动校验",
        "consequence": "每周需人工重跑一次",
        "evidence_summary": "BR-16虚构运营观察；工时和损失金额未知",
        "ea_involvement": "local-product-team",
        "ea_rationale": "暂无跨产品影响证据；不要求EA处理所有债务",
        "repayment_option": "补自动转码校验，估算待定",
        "backlog_refs": [],
        "owner": "甲馆报表负责人",
        "review_date": "2026-11-09",
        "status": "open",
        "closure_criteria": "修复交付引用、验证证据、责任人复核（BR-20项目规则）",
        "verification_evidence": [],
        "closure_decision": "not-closed",
        "cost_or_interest": "unknown；不能把重跑次数直接当金额"
      },
      "evidence": [
        "BR-16"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "DEBT-03",
      "type": "guide:technical_debt",
      "name": "预约状态接口词汇不一致",
      "attributes": {
        "kind": "architecture-interface",
        "affected_products": [
          "预约服务",
          "两馆消费者"
        ],
        "cause": "两份契约名称不同",
        "consequence": "消费者重复维护状态映射",
        "evidence_summary": "BR-17虚构接口观察；无财务折算",
        "ea_involvement": "cross-product-coordination",
        "ea_rationale": "业务、接口与两个消费者需共同采用词汇",
        "repayment_option": "统一状态词汇并验证两个消费者映射",
        "backlog_refs": [
          "BL-02"
        ],
        "owner": "接口负责人",
        "review_date": "2026-11-09",
        "status": "selected",
        "closure_criteria": "修复交付引用、验证证据、责任人复核（BR-20项目规则）",
        "verification_evidence": [],
        "closure_decision": "not-closed",
        "cost_or_interest": "unknown；未计算利息或折现"
      },
      "evidence": [
        "BR-17"
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
    "id": "v-technical-debt-register-default",
    "artifact_id": "technical-debt-register",
    "profile_id": "technical-debt-register-default",
    "title": "技术与架构债登记表／虚构跨馆案例",
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
      "DEBT-01",
      "DEBT-02",
      "DEBT-03"
    ],
    "relationship_ids": [],
    "analysis": "见analysis.md逐项原料→判断→结果；字段中的状态均是案例观察，不代表生产实施或批准。",
    "legend": "表格行以稳定ID区分；未知保留unknown，空列表表示明确没有该项；关系表按类型和端点解释。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile technical-debt-register-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile technical-debt-register-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
