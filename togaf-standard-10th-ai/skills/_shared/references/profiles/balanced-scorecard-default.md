# 平衡计分卡目标与成果

`profile_id`: balanced-scorecard-default；`artifact_id`: balanced-scorecard；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G233/fig4-3。

## 构图与定义状态

表示族：`perspectives`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：goal, outcome。关系类型：realizes。

```json
{
  "entities": {
    "goal": [
      "perspective",
      "definition"
    ],
    "outcome": [
      "perspective",
      "metric",
      "unit",
      "baseline",
      "target",
      "period"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链
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
      "id": "balanced-scorecard-default-goal0",
      "type": "goal",
      "name": "提升重复购买",
      "attributes": {
        "perspective": "客户",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome0",
      "type": "outcome",
      "name": "重复购买比例提高",
      "attributes": {
        "perspective": "客户",
        "metric": "期间重复购买客户占比",
        "unit": "%",
        "baseline": 20,
        "target": 22,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-goal1",
      "type": "goal",
      "name": "提升人员稳定性",
      "attributes": {
        "perspective": "学习与成长",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome1",
      "type": "outcome",
      "name": "员工流失率降低",
      "attributes": {
        "perspective": "学习与成长",
        "metric": "期间员工离职人数除期初人数",
        "unit": "%",
        "baseline": 10,
        "target": 8.5,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-goal2",
      "type": "goal",
      "name": "提高订单履约效率",
      "attributes": {
        "perspective": "内部流程",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome2",
      "type": "outcome",
      "name": "平均确认时间下降",
      "attributes": {
        "perspective": "内部流程",
        "metric": "确认订单耗时算术平均",
        "unit": "分钟",
        "baseline": 20,
        "target": 10,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-goal3",
      "type": "goal",
      "name": "增加可持续销售",
      "attributes": {
        "perspective": "财务",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome3",
      "type": "outcome",
      "name": "销售额增长",
      "attributes": {
        "perspective": "财务",
        "metric": "同口径期间商品销售额",
        "unit": "万元",
        "baseline": 100,
        "target": 110,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "balanced-scorecard-default-realize0",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome0",
      "target": "balanced-scorecard-default-goal0",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-realize1",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome1",
      "target": "balanced-scorecard-default-goal1",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-realize2",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome2",
      "target": "balanced-scorecard-default-goal2",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-realize3",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome3",
      "target": "balanced-scorecard-default-goal3",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-balanced-scorecard-default",
    "artifact_id": "balanced-scorecard",
    "profile_id": "balanced-scorecard-default",
    "title": "平衡计分卡目标与成果／虚构案例",
    "entity_ids": [
      "balanced-scorecard-default-goal0",
      "balanced-scorecard-default-outcome0",
      "balanced-scorecard-default-goal1",
      "balanced-scorecard-default-outcome1",
      "balanced-scorecard-default-goal2",
      "balanced-scorecard-default-outcome2",
      "balanced-scorecard-default-goal3",
      "balanced-scorecard-default-outcome3"
    ],
    "relationship_ids": [
      "balanced-scorecard-default-realize0",
      "balanced-scorecard-default-realize1",
      "balanced-scorecard-default-realize2",
      "balanced-scorecard-default-realize3"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile balanced-scorecard-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile balanced-scorecard-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
