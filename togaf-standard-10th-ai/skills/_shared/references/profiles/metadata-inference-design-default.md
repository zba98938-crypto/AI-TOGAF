# 技术元数据推断方案

`profile_id`: metadata-inference-design-default；`artifact_id`: metadata-inference-design；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-10。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：inference_source。关系类型：。

```json
{
  "entities": {
    "inference_source": [
      "data_structure",
      "schema_access",
      "content_access",
      "cost",
      "risk",
      "scope"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 采集模式不必然需要读取实际业务数据
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
      "id": "metadata-inference-design-default-structured",
      "type": "inference_source",
      "name": "结构化来源",
      "attributes": {
        "data_structure": "结构化",
        "schema_access": "可读字段模式",
        "content_access": "无需读取客户实际值",
        "cost": "需估算连接器维护与源系统负载",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-inference-design-default-semi",
      "type": "inference_source",
      "name": "半结构化来源",
      "attributes": {
        "data_structure": "半结构化",
        "schema_access": "有结构但需验证稳定性",
        "content_access": "仅在批准范围抽样",
        "cost": "需估算连接器维护与源系统负载",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-inference-design-default-unstructured",
      "type": "inference_source",
      "name": "非结构化来源",
      "attributes": {
        "data_structure": "非结构化",
        "schema_access": "无稳定字段模式",
        "content_access": "内容扫描需独立隐私与成本评估",
        "cost": "需估算连接器维护与源系统负载",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-metadata-inference-design-default",
    "artifact_id": "metadata-inference-design",
    "profile_id": "metadata-inference-design-default",
    "title": "技术元数据推断方案／虚构案例",
    "entity_ids": [
      "metadata-inference-design-default-structured",
      "metadata-inference-design-default-semi",
      "metadata-inference-design-default-unstructured"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-inference-design-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-inference-design-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
