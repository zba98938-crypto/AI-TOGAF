# 回退计划

ID：`rollback-plan`。主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G152 §5.7。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

迁移失败时如何恢复可运营状态？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 迁移失败时如何恢复可运营状态？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- trigger
- decision_owner
- prerequisite

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：rollback_step。

```json
{
  "rollback_step": [
    "trigger",
    "decision_owner",
    "prerequisite",
    "data_recovery",
    "sequence",
    "verification"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "trigger": {
    "meaning": "触发事件或判据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decision_owner": {
    "meaning": "有权作出该决策的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "prerequisite": {
    "meaning": "可执行该项的前置条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "data_recovery": {
    "meaning": "数据恢复与一致性规则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "sequence": {
    "meaning": "执行次序及其依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "verification": {
    "meaning": "验证方法与验收证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 确定回退触发与授权
2. 分析可逆点和数据一致性
3. 排列步骤与依赖
4. 定义恢复验证和演练证据

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 回退不是仅写恢复备份，应说明业务与数据恢复条件
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 回退不是仅写恢复备份，应说明业务与数据恢复条件


## 视图和交付物

- [回退计划](../profiles/rollback-plan-default.md)

- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「回退计划」给出：回退不是仅写恢复备份，应说明业务与数据恢复条件",
    "expected": "missing-evidence",
    "why": "回退不是仅写恢复备份，应说明业务与数据恢复条件"
  },
  "modification_example": {
    "change": "在「回退计划」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "rollback-plan-default-step1",
      "type": "rollback_step",
      "name": "回退计划：准备",
      "attributes": {
        "trigger": "订单一致性校验失败时暂停切换",
        "decision_owner": "虚构发布经理",
        "prerequisite": "保留旧平台可写能力并完成对账",
        "data_recovery": "核对切换窗口内订单与付款记录后恢复",
        "sequence": "停止新写入→订单对账→恢复旧平台→验证订单履约",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
        "order": 1,
        "start": "2026-11-02",
        "end": "2026-11-13"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "rollback-plan-default-step2",
      "type": "rollback_step",
      "name": "回退计划：验证",
      "attributes": {
        "trigger": "订单一致性校验失败时暂停切换",
        "decision_owner": "虚构发布经理",
        "prerequisite": "保留旧平台可写能力并完成对账",
        "data_recovery": "核对切换窗口内订单与付款记录后恢复",
        "sequence": "停止新写入→订单对账→恢复旧平台→验证订单履约",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
        "order": 2,
        "start": "2026-11-16",
        "end": "2026-11-27"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "rollback-plan-default-dependency",
      "type": "traces_to",
      "source": "rollback-plan-default-step2",
      "target": "rollback-plan-default-step1",
      "label": "后项以准备结果为进入条件；工期是虚构演示",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-rollback-plan-default",
    "artifact_id": "rollback-plan",
    "profile_id": "rollback-plan-default",
    "title": "回退计划／虚构案例",
    "entity_ids": [
      "rollback-plan-default-step1",
      "rollback-plan-default-step2"
    ],
    "relationship_ids": [
      "rollback-plan-default-dependency"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact rollback-plan --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
