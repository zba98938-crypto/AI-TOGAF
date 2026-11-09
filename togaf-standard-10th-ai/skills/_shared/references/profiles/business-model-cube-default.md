# 业务模型立方体

`profile_id`: business-model-cube-default；`artifact_id`: business-model-cube；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G18A/fig2-3。

## 构图与定义状态

表示族：`cube`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_model_dimension。关系类型：traces_to。

```json
{
  "entities": {
    "business_model_dimension": [
      "dimension",
      "detail",
      "local_mapping"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级
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
      "id": "business-model-cube-default-0",
      "type": "business_model_dimension",
      "name": "价值主张",
      "attributes": {
        "dimension": "价值主张",
        "detail": "可靠且透明的商品履约",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-1",
      "type": "business_model_dimension",
      "name": "客户",
      "attributes": {
        "dimension": "客户",
        "detail": "需要按承诺交付的线上客户",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-2",
      "type": "business_model_dimension",
      "name": "网络伙伴",
      "attributes": {
        "dimension": "网络伙伴",
        "detail": "承运商与商品供应方",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-3",
      "type": "business_model_dimension",
      "name": "活动",
      "attributes": {
        "dimension": "活动",
        "detail": "确认订单、拣配发运、处理例外",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-4",
      "type": "business_model_dimension",
      "name": "胜任力",
      "attributes": {
        "dimension": "胜任力",
        "detail": "履约协调与订单信息治理",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-5",
      "type": "business_model_dimension",
      "name": "价值公式",
      "attributes": {
        "dimension": "价值公式",
        "detail": "明确期间收入减采购履约和固定成本；尚无数值",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "business-model-cube-default-customer-value",
      "type": "traces_to",
      "source": "business-model-cube-default-0",
      "target": "business-model-cube-default-1",
      "label": "本例价值主张面向该客户；项目补充关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-partner-activity",
      "type": "traces_to",
      "source": "business-model-cube-default-2",
      "target": "business-model-cube-default-3",
      "label": "承运商参与发运活动；项目补充关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-competence-activity",
      "type": "traces_to",
      "source": "business-model-cube-default-4",
      "target": "business-model-cube-default-3",
      "label": "胜任力支撑活动；不是来源图流程箭头",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-model-cube-default",
    "artifact_id": "business-model-cube",
    "profile_id": "business-model-cube-default",
    "title": "业务模型立方体／虚构案例",
    "entity_ids": [
      "business-model-cube-default-0",
      "business-model-cube-default-1",
      "business-model-cube-default-2",
      "business-model-cube-default-3",
      "business-model-cube-default-4",
      "business-model-cube-default-5"
    ],
    "relationship_ids": [
      "business-model-cube-default-customer-value",
      "business-model-cube-default-partner-activity",
      "business-model-cube-default-competence-activity"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-model-cube-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-model-cube-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
