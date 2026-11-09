# 数据使用文档

`profile_id`: data-usage-documentation-default；`artifact_id`: data-usage-documentation；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §3、§5.1。

## 构图与定义状态

表示族：`catalog`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_usage。关系类型：。

```json
{
  "entities": {
    "data_usage": [
      "dataset",
      "user_role",
      "purpose",
      "access_condition",
      "retention",
      "lawful_basis"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 存在使用关系不等于已获访问授权
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
      "id": "data-usage-documentation-default-record",
      "type": "data_usage",
      "name": "数据使用文档：订单范围记录",
      "attributes": {
        "dataset": "虚构在线订单集",
        "user_role": "虚构订单案例中需验证的使用数据的角色",
        "purpose": "履行客户订单",
        "access_condition": "角色授权且仅访问其职责所需订单",
        "retention": "由本地业务与法规责任方确定，本例未批准",
        "lawful_basis": "虚构订单案例中需验证的数据使用的法规或政策依据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-data-usage-documentation-default",
    "artifact_id": "data-usage-documentation",
    "profile_id": "data-usage-documentation-default",
    "title": "数据使用文档／虚构案例",
    "entity_ids": [
      "data-usage-documentation-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile data-usage-documentation-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile data-usage-documentation-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
