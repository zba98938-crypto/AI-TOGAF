# 运营模式

`profile_id`: operating-model-default；`artifact_id`: operating-model；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G184/fig4-1。

## 构图与定义状态

表示族：`quadrant`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "x_axis": "业务流程标准化：低 → 高",
  "y_axis": "业务流程集成：低 → 高"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：operating_model。关系类型：。

```json
{
  "entities": {
    "operating_model": [
      "integration",
      "standardization",
      "scope",
      "rationale",
      "quadrant"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序
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
      "id": "operating-model-default-coord",
      "type": "operating_model",
      "name": "协调",
      "attributes": {
        "integration": "高",
        "standardization": "低",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "top-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "operating-model-default-unify",
      "type": "operating_model",
      "name": "统一",
      "attributes": {
        "integration": "高",
        "standardization": "高",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "top-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "operating-model-default-diverse",
      "type": "operating_model",
      "name": "多元化",
      "attributes": {
        "integration": "低",
        "standardization": "低",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "bottom-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "operating-model-default-replicate",
      "type": "operating_model",
      "name": "复制",
      "attributes": {
        "integration": "低",
        "standardization": "高",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "bottom-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-operating-model-default",
    "artifact_id": "operating-model",
    "profile_id": "operating-model-default",
    "title": "运营模式／虚构案例",
    "entity_ids": [
      "operating-model-default-coord",
      "operating-model-default-unify",
      "operating-model-default-diverse",
      "operating-model-default-replicate"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile operating-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile operating-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
