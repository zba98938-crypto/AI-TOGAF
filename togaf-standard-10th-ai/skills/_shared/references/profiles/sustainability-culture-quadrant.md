# 数字节制文化四维图

`profile_id`: sustainability-culture-quadrant；`artifact_id`: environmental-decision-log；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242/fig3-2。

## 构图与定义状态

表示族：`quadrant`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G242/fig3-2",
  "layout_notes": "无坐标轴、无高低，无序并列四维围绕共同目标",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/sustainability-culture-quadrant.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：environmental_decision。关系类型：。

```json
{
  "entities": {
    "environmental_decision": [
      "category",
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 无坐标轴、无高低，无序并列四维围绕共同目标

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
      "id": "sustainability-culture-quadrant-0",
      "type": "environmental_decision",
      "name": "组织管理与工作文化",
      "attributes": {
        "category": "组织管理与工作文化",
        "definition": "数字节制文化的并列关注维度；无高低轴",
        "quadrant": "top-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-culture-quadrant-1",
      "type": "environmental_decision",
      "name": "技能教育",
      "attributes": {
        "category": "技能教育",
        "definition": "数字节制文化的并列关注维度；无高低轴",
        "quadrant": "top-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-culture-quadrant-2",
      "type": "environmental_decision",
      "name": "沟通",
      "attributes": {
        "category": "沟通",
        "definition": "数字节制文化的并列关注维度；无高低轴",
        "quadrant": "bottom-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-culture-quadrant-3",
      "type": "environmental_decision",
      "name": "节制创新",
      "attributes": {
        "category": "节制创新",
        "definition": "数字节制文化的并列关注维度；无高低轴",
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
    "id": "v-sustainability-culture-quadrant",
    "artifact_id": "environmental-decision-log",
    "profile_id": "sustainability-culture-quadrant",
    "title": "数字节制文化四维图／虚构案例",
    "entity_ids": [
      "sustainability-culture-quadrant-0",
      "sustainability-culture-quadrant-1",
      "sustainability-culture-quadrant-2",
      "sustainability-culture-quadrant-3"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-culture-quadrant --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-culture-quadrant --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
