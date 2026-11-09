# 信任框架

`profile_id`: trust-framework-default；`artifact_id`: trust-framework；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.3。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：goal, trust_party。关系类型：traces_to。

```json
{
  "entities": {
    "trust_party": [
      "business_basis",
      "legal_basis",
      "direction",
      "conditions",
      "scope"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 数字证书可以传递既有信任，不能创造业务信任
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
      "id": "trust-framework-default-record",
      "type": "trust_party",
      "name": "信任框架：订单范围记录",
      "attributes": {
        "business_basis": "承运商受托履行配送合同",
        "legal_basis": "虚构配送与数据处理协议",
        "direction": "零售商向承运商传递受限订单数据",
        "conditions": "仅限有合同与明确用途的订单处理",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "trust-framework-default-target",
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
      "id": "trust-framework-default-supports",
      "type": "traces_to",
      "source": "trust-framework-default-record",
      "target": "trust-framework-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-trust-framework-default",
    "artifact_id": "trust-framework",
    "profile_id": "trust-framework-default",
    "title": "信任框架／虚构案例",
    "entity_ids": [
      "trust-framework-default-record",
      "trust-framework-default-target"
    ],
    "relationship_ids": [
      "trust-framework-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile trust-framework-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile trust-framework-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
