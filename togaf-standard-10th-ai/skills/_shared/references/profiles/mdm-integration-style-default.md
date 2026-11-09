# 主数据集成风格

`profile_id`: mdm-integration-style-default；`artifact_id`: mdm-integration-style；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §6.1.1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：master_repository。关系类型：。

```json
{
  "entities": {
    "master_repository": [
      "style",
      "authority",
      "collaboration",
      "consumers",
      "synchronization"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 参考集成风格不是指定厂商产品
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
      "id": "mdm-integration-style-default-0",
      "type": "master_repository",
      "name": "整合候选方案",
      "attributes": {
        "style": "整合",
        "authority": "明确中央与源方的主记录责任；需逐项裁剪",
        "collaboration": "源方与中央团队按契约协作",
        "consumers": "订单与客户服务应用",
        "synchronization": "按权威和时效要求交换，非默认双向写",
        "integration_style": "整合"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "mdm-integration-style-default-1",
      "type": "master_repository",
      "name": "协作候选方案",
      "attributes": {
        "style": "协作",
        "authority": "明确中央与源方的主记录责任；需逐项裁剪",
        "collaboration": "源方与中央团队按契约协作",
        "consumers": "订单与客户服务应用",
        "synchronization": "按权威和时效要求交换，非默认双向写",
        "integration_style": "协作"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "mdm-integration-style-default-2",
      "type": "master_repository",
      "name": "集中候选方案",
      "attributes": {
        "style": "集中",
        "authority": "明确中央与源方的主记录责任；需逐项裁剪",
        "collaboration": "源方与中央团队按契约协作",
        "consumers": "订单与客户服务应用",
        "synchronization": "按权威和时效要求交换，非默认双向写",
        "integration_style": "集中"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-mdm-integration-style-default",
    "artifact_id": "mdm-integration-style",
    "profile_id": "mdm-integration-style-default",
    "title": "主数据集成风格／虚构案例",
    "entity_ids": [
      "mdm-integration-style-default-0",
      "mdm-integration-style-default-1",
      "mdm-integration-style-default-2"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-integration-style-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-integration-style-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
