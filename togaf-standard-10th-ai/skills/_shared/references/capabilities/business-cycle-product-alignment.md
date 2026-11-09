# 业务周期与工作产品时点

ID：`business-cycle-product-alignment`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §4.3.2、§10.3、§11.4；G186 §4、§8.1、§11.2、§14。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构工作产品何时必须可用以影响业务决定？

- 授权业务利益相关者
- 架构师
- 相关SME与实施负责人
- 架构工作产品何时必须可用以影响业务决定？
- 依据完整、同口径、责任和未决项清晰


## 输入及缺口处理

必需：

- 范围和五维语境
- 原始访谈/计划/测量及定位
- 授权角色和适用目标版本

可选：

- 既有模型、视图、参考规范和组织规则

逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。

## 元素、属性与关系

对象类型：guide:cycle_product。

```json
{
  "guide:cycle_product": [
    "business_event",
    "decision",
    "consumer",
    "required_by",
    "planned",
    "actual",
    "product_view_refs",
    "dependency",
    "status",
    "recovery_action",
    "rule_source"
  ]
}
```

{
  "name": {
    "meaning": "交付时点安排",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "business_event": {
    "meaning": "业务/预算/发布/运营事件",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision": {
    "meaning": "该事件需要作出的决定",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "consumer": {
    "meaning": "消费架构成果的责任人",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "required_by": {
    "meaning": "消费方需要日期",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "planned": {
    "meaning": "计划提供日期",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "actual": {
    "meaning": "实际交付日期或未知",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "product_view_refs": {
    "meaning": "具体工作产品及view_id",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "dependency": {
    "meaning": "前置输入/工作",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "status": {
    "meaning": "准时/迟到/未知",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "recovery_action": {
    "meaning": "晚交付时如何修正或披露决策缺口",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "rule_source": {
    "meaning": "项目日历与日期依据",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 访谈消费方确认业务事件、决定和最迟输入日期
2. 将目的与所需工作产品/实际视图绑定
3. 以输入依赖倒排完成与评审
4. 比较计划/实际和消费期限，指出错过决策的后果
5. 重排范围资源或显式告知未满足条件，不改原业务事实

## 输出、检查与误读

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

- ADM阶段顺序不决定业务消费时点
- 30天/季度是G186的实践建议，项目日期必须由实际日历确认
- 计划早于期限不证明实际已按时交付

- ADM阶段顺序不决定业务消费时点
- 30天/季度是G186的实践建议，项目日期必须由实际日历确认
- 计划早于期限不证明实际已按时交付


## 视图和交付物

- [业务周期与工作产品时点](../profiles/business-cycle-product-alignment-default.md)

- [statement-of-work](../deliverables/statement-of-work.md)
- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "无消费方期限，只写“阶段F完成”",
    "expected": "missing-evidence",
    "why": "missing-consumer-deadline拒绝准时判定",
    "original_expected_text": "missing-consumer-deadline拒绝准时判定"
  },
  "modification_example": {
    "change": "组合选项计划从11月16改为11月12",
    "expected": "迟3天变提前1天；实际仍unknown"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/business-cycle-product-alignment.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-business-cycle-product-alignment-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：cycle",
      "locator": "examples/addenda/governance/raw-business-materials.json#cycle"
    }
  ],
  "entities": [
    {
      "id": "business-cycle-product-alignment-default-1",
      "type": "guide:cycle_product",
      "name": "2027预算选项",
      "attributes": {
        "business_event": "2026-11-20预算会",
        "decision": "T1拨款",
        "consumer": "财务负责人",
        "required_by": "2026-11-13",
        "planned": "2026-11-16",
        "actual": "unknown",
        "product_view_refs": [
          "v-budget-options-T1"
        ],
        "dependency": "成本估算、不确定性说明与主题工作包",
        "status": "late：计划比消费期限晚3日",
        "recovery_action": "安排11月12日候选评审；若未能提供则预算结论明确缺口",
        "rule_source": "CY-01财务约定；日期不是TOGAF规定"
      },
      "evidence": [
        "src-business-cycle-product-alignment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-cycle-product-alignment-default-2",
      "type": "guide:cycle_product",
      "name": "项目拨款准备",
      "attributes": {
        "business_event": "2026-12-04项目拨款会",
        "decision": "范围/契约批准",
        "consumer": "PMO与发起人",
        "required_by": "2026-12-03",
        "planned": "2026-12-02",
        "actual": "unknown",
        "product_view_refs": [
          "v-contract-T1"
        ],
        "dependency": "预算、范围、依赖与规格",
        "status": "timely：计划早于期限1日，尚无实际交付证据",
        "recovery_action": "维持计划，核实前置输入",
        "rule_source": "CY-02及项目确认的会前1日要求"
      },
      "evidence": [
        "src-business-cycle-product-alignment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-cycle-product-alignment-default-3",
      "type": "guide:cycle_product",
      "name": "首月价值回顾",
      "attributes": {
        "business_event": "2027-02-10运营价值回顾",
        "decision": "继续T2或调整路线",
        "consumer": "组合负责人",
        "required_by": "2027-02-10",
        "planned": "2027-02-08",
        "actual": "unknown",
        "product_view_refs": [
          "v-value-realization-assessment-default"
        ],
        "dependency": "T1首月运营测量与比较基线",
        "status": "timely：计划早2日",
        "recovery_action": "锁定数据口径与责任，不能以G合规报告替代",
        "rule_source": "CY-03运营约定"
      },
      "evidence": [
        "src-business-cycle-product-alignment-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-cycle-product-alignment-default",
    "artifact_id": "business-cycle-product-alignment",
    "profile_id": "business-cycle-product-alignment-default",
    "title": "业务周期与工作产品时点",
    "entity_ids": [
      "business-cycle-product-alignment-default-1",
      "business-cycle-product-alignment-default-2",
      "business-cycle-product-alignment-default-3"
    ],
    "relationship_ids": [],
    "analysis": "把预算/拨款/价值回顾倒排到消费日期；发现组合选项计划迟3天，已有项目表未表达这一消费缺口，需调整。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "cycle"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-cycle-product-alignment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
