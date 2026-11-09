# EA 与企业价值地图

`profile_id`: ea-value-map-default；`artifact_id`: ea-value-map；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §13。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ea_value, goal。关系类型：traces_to。

```json
{
  "entities": {
    "ea_value": [
      "service",
      "consumer",
      "business_outcome",
      "measure",
      "contribution",
      "evidence"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 相关性或贡献假设不能直接断言为确定收益因果
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
      "id": "ea-value-map-default-record",
      "type": "ea_value",
      "name": "EA 与企业价值地图：订单范围记录",
      "attributes": {
        "service": "虚构订单案例中需验证的服务对象引用",
        "consumer": "虚构订单应用",
        "business_outcome": "提高履约可靠性",
        "measure": "虚构订单案例中需验证的衡量贡献的指标",
        "contribution": "架构通过明确信息责任和迁移约束提供贡献，因果待验证",
        "evidence": "虚构场景说明，非实测证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ea-value-map-default-target",
      "type": "goal",
      "name": "可靠履约",
      "attributes": {
        "definition": "在承诺时间内交付且状态可追溯"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "ea-value-map-default-supports",
      "type": "traces_to",
      "source": "ea-value-map-default-record",
      "target": "ea-value-map-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-ea-value-map-default",
    "artifact_id": "ea-value-map",
    "profile_id": "ea-value-map-default",
    "title": "EA 与企业价值地图／虚构案例",
    "entity_ids": [
      "ea-value-map-default-record",
      "ea-value-map-default-target"
    ],
    "relationship_ids": [
      "ea-value-map-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-value-map-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-value-map-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
