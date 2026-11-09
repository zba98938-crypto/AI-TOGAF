# 构建块描述

`profile_id`: building-block-description-default；`artifact_id`: building-block-description；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G248 §2–3。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：abb, goal, sbb, requirement。关系类型：traces_to, realizes。

```json
{
  "entities": {
    "abb": [
      "definition",
      "abstraction",
      "service",
      "requirements",
      "realization",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现
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
      "id": "building-block-description-default-record",
      "type": "abb",
      "name": "构建块描述：订单范围记录",
      "attributes": {
        "definition": "构建块描述的虚构零售企业示例",
        "abstraction": "逻辑",
        "service": "虚构订单案例中需验证的服务对象引用",
        "requirements": "虚构订单案例中需验证的架构要求引用",
        "realization": "候选SBB方案，尚未选定",
        "owner": "虚构业务负责人"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "building-block-description-default-target",
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
      "id": "building-block-description-default-supports",
      "type": "traces_to",
      "source": "building-block-description-default-record",
      "target": "building-block-description-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-building-block-description-default",
    "artifact_id": "building-block-description",
    "profile_id": "building-block-description-default",
    "title": "构建块描述／虚构案例",
    "entity_ids": [
      "building-block-description-default-record",
      "building-block-description-default-target"
    ],
    "relationship_ids": [
      "building-block-description-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile building-block-description-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile building-block-description-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
