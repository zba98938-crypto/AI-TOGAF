# 能力与战略足迹

`profile_id`: capability-strategy-overlay；`artifact_id`: business-footprint-diagram；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G211 §4。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": null,
  "layout_notes": "战略贡献必须关联实际业务目标及理由",
  "review_status": "source-located-awaiting-template-validation"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, goal。关系类型：traces_to。

```json
{
  "entities": {
    "capability": [
      "definition",
      "strategic_contribution"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 战略贡献必须关联实际业务目标及理由

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
      "id": "capability-strategy-overlay-record",
      "type": "capability",
      "name": "能力与战略足迹：订单范围记录",
      "attributes": {
        "definition": "能力与战略足迹的虚构零售企业示例",
        "strategic_contribution": "缩短履约等待并提高客户通知可靠性"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-strategy-overlay-target",
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
      "id": "capability-strategy-overlay-supports",
      "type": "traces_to",
      "source": "capability-strategy-overlay-record",
      "target": "capability-strategy-overlay-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-capability-strategy-overlay",
    "artifact_id": "business-footprint-diagram",
    "profile_id": "capability-strategy-overlay",
    "title": "能力与战略足迹／虚构案例",
    "entity_ids": [
      "capability-strategy-overlay-record",
      "capability-strategy-overlay-target"
    ],
    "relationship_ids": [
      "capability-strategy-overlay-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-strategy-overlay --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-strategy-overlay --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
