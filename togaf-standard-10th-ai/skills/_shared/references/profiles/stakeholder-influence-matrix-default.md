# 利益相关者影响力与影响程度矩阵

`profile_id`: stakeholder-influence-matrix-default；`artifact_id`: stakeholder-influence-matrix；主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G184/fig4-3。

## 构图与定义状态

表示族：`quadrant`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "x_axis": "Impact 所受影响程度：低 → 高",
  "y_axis": "Influence 影响力：低 → 高",
  "quadrant_labels": {
    "top-left": "令其满意 Keep Satisfied",
    "top-right": "重点管理 Manage Closely",
    "bottom-left": "监督 Monitor",
    "bottom-right": "随时告知 Keep Informed"
  }
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：stakeholder。关系类型：。

```json
{
  "entities": {
    "stakeholder": [
      "influence",
      "impact",
      "engagement",
      "concern",
      "quadrant"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权
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
      "id": "stakeholder-influence-matrix-default-sponsor",
      "type": "stakeholder",
      "name": "业务赞助人",
      "attributes": {
        "influence": "高",
        "impact": "高",
        "engagement": "重点管理",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "top-right",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stakeholder-influence-matrix-default-legal",
      "type": "stakeholder",
      "name": "法律顾问",
      "attributes": {
        "influence": "高",
        "impact": "低",
        "engagement": "令其满意",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "top-left",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stakeholder-influence-matrix-default-operator",
      "type": "stakeholder",
      "name": "仓库操作员",
      "attributes": {
        "influence": "低",
        "impact": "高",
        "engagement": "随时告知",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "bottom-right",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stakeholder-influence-matrix-default-observer",
      "type": "stakeholder",
      "name": "非试点地区观察者",
      "attributes": {
        "influence": "低",
        "impact": "低",
        "engagement": "监督",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "bottom-left",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-stakeholder-influence-matrix-default",
    "artifact_id": "stakeholder-influence-matrix",
    "profile_id": "stakeholder-influence-matrix-default",
    "title": "利益相关者影响力与影响程度矩阵／虚构案例",
    "entity_ids": [
      "stakeholder-influence-matrix-default-sponsor",
      "stakeholder-influence-matrix-default-legal",
      "stakeholder-influence-matrix-default-operator",
      "stakeholder-influence-matrix-default-observer"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile stakeholder-influence-matrix-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile stakeholder-influence-matrix-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
