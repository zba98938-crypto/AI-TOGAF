# 元数据模型

`profile_id`: metadata-model-default；`artifact_id`: metadata-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-5、4-6。

## 构图与定义状态

表示族：`er`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：metadata_asset。关系类型：traces_to。

```json
{
  "entities": {
    "metadata_asset": [
      "metadata_category",
      "definition",
      "identifier",
      "domain",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 图4-5的参考资产不是每个项目必须全选的模型
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
      "id": "metadata-model-default-term",
      "type": "metadata_asset",
      "name": "订单业务术语",
      "attributes": {
        "metadata_category": "业务元数据",
        "definition": "客户的商品购买与交付承诺",
        "identifier": "TERM-ORDER",
        "domain": "订单业务语义",
        "owner": "订单业务所有者"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-model-default-field",
      "type": "metadata_asset",
      "name": "订单状态字段",
      "attributes": {
        "metadata_category": "技术元数据",
        "definition": "承载订单状态的字段描述",
        "identifier": "FIELD-ORDER-STATUS",
        "domain": "已确认、已发运、已取消",
        "owner": "订单应用维护团队"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "metadata-model-default-maps",
      "type": "traces_to",
      "source": "metadata-model-default-term",
      "target": "metadata-model-default-field",
      "label": "业务术语映射技术字段；不是数据值副本",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-metadata-model-default",
    "artifact_id": "metadata-model",
    "profile_id": "metadata-model-default",
    "title": "元数据模型／虚构案例",
    "entity_ids": [
      "metadata-model-default-term",
      "metadata-model-default-field"
    ],
    "relationship_ids": [
      "metadata-model-default-maps"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
