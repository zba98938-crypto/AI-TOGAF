# 企业架构服务目录

`profile_id`: ea-service-catalog-default；`artifact_id`: ea-service-catalog；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G217 附录B–C。

## 构图与定义状态

表示族：`catalog`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ea_service。关系类型：。

```json
{
  "entities": {
    "ea_service": [
      "consumer",
      "decision",
      "output",
      "adm_phase",
      "owner",
      "service_level"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 候选服务不是每个 EA 团队必须提供的服务清单
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
      "id": "ea-service-catalog-default-record",
      "type": "ea_service",
      "name": "企业架构服务目录：订单范围记录",
      "attributes": {
        "consumer": "虚构订单应用",
        "decision": "虚构订单案例中需验证的决策结果、理由和状态",
        "output": "经过校验并发布的新定义",
        "adm_phase": "B、C、E",
        "owner": "虚构业务负责人",
        "service_level": "在决策节点前提供足够架构证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-ea-service-catalog-default",
    "artifact_id": "ea-service-catalog",
    "profile_id": "ea-service-catalog-default",
    "title": "企业架构服务目录／虚构案例",
    "entity_ids": [
      "ea-service-catalog-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-catalog-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-catalog-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
