# 微服务价值与资源目录

`profile_id`: microservice-value-catalog-default；`artifact_id`: microservice-value-catalog；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G21I §11.3。

## 构图与定义状态

表示族：`catalog`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：microservice。关系类型：。

```json
{
  "entities": {
    "microservice": [
      "business_function",
      "value",
      "planned_state",
      "development_resources",
      "operations_resources",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 计划服务不能标为已交付，服务数量不等于业务价值
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
      "id": "microservice-value-catalog-default-record",
      "type": "microservice",
      "name": "微服务价值与资源目录：订单范围记录",
      "attributes": {
        "business_function": "订单履约分析",
        "value": 2,
        "planned_state": "计划，尚未交付",
        "development_resources": "虚构跨职能团队一组",
        "operations_resources": "虚构运营责任人，容量待估算",
        "owner": "虚构业务负责人"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-microservice-value-catalog-default",
    "artifact_id": "microservice-value-catalog",
    "profile_id": "microservice-value-catalog-default",
    "title": "微服务价值与资源目录／虚构案例",
    "entity_ids": [
      "microservice-value-catalog-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile microservice-value-catalog-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile microservice-value-catalog-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
