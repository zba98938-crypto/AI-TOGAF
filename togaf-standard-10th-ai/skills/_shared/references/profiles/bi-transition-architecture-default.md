# BI 与分析演进架构

`profile_id`: bi-transition-architecture-default；`artifact_id`: bi-transition-architecture；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G238 §3；图3-1–3-4。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：analytics_component。关系类型：traces_to。

```json
{
  "entities": {
    "analytics_component": [
      "role",
      "inbound",
      "outbound",
      "storage",
      "coexistence"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不同状态是同一架构的演进视图，不机械当成独立制品种类
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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
      "id": "bi-transition-architecture-default-baseline",
      "type": "analytics_component",
      "name": "基线分析平台",
      "attributes": {
        "state_id": "baseline",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-transition1",
      "type": "analytics_component",
      "name": "过渡1分析平台",
      "attributes": {
        "state_id": "transition1",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-transition2",
      "type": "analytics_component",
      "name": "过渡2分析平台",
      "attributes": {
        "state_id": "transition2",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-target",
      "type": "analytics_component",
      "name": "目标分析平台",
      "attributes": {
        "state_id": "target",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "bi-transition-architecture-default-bi-transition-architecture-default-baseline-next",
      "type": "traces_to",
      "source": "bi-transition-architecture-default-baseline",
      "target": "bi-transition-architecture-default-transition1",
      "label": "演进状态；不是强制替换厂商",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-bi-transition-architecture-default-transition1-next",
      "type": "traces_to",
      "source": "bi-transition-architecture-default-transition1",
      "target": "bi-transition-architecture-default-transition2",
      "label": "演进状态；不是强制替换厂商",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-bi-transition-architecture-default-transition2-next",
      "type": "traces_to",
      "source": "bi-transition-architecture-default-transition2",
      "target": "bi-transition-architecture-default-target",
      "label": "演进状态；不是强制替换厂商",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-bi-transition-architecture-default",
    "artifact_id": "bi-transition-architecture",
    "profile_id": "bi-transition-architecture-default",
    "title": "BI 与分析演进架构／虚构案例",
    "entity_ids": [
      "bi-transition-architecture-default-baseline",
      "bi-transition-architecture-default-transition1",
      "bi-transition-architecture-default-transition2",
      "bi-transition-architecture-default-target"
    ],
    "relationship_ids": [
      "bi-transition-architecture-default-bi-transition-architecture-default-baseline-next",
      "bi-transition-architecture-default-bi-transition-architecture-default-transition1-next",
      "bi-transition-architecture-default-bi-transition-architecture-default-transition2-next"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-transition-architecture-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-transition-architecture-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
