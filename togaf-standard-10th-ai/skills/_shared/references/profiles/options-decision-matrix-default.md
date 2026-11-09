# 备选方案决策矩阵

`profile_id`: options-decision-matrix-default；`artifact_id`: options-decision-matrix；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G176 §12.8。

## 构图与定义状态

表示族：`matrix`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：criterion, option。关系类型：evaluated_by。

```json
{
  "entities": {},
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 成本原值不能直接当越高越好的评分，权重必须显式
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
      "id": "options-decision-matrix-default-option0",
      "type": "option",
      "name": "改善现有平台",
      "attributes": {
        "definition": "待选择，未批准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-option1",
      "type": "option",
      "name": "整体替换平台",
      "attributes": {
        "definition": "待选择，未批准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion0",
      "type": "criterion",
      "name": "成本偏好",
      "attributes": {
        "weight": 1,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion1",
      "type": "criterion",
      "name": "资源偏好",
      "attributes": {
        "weight": 1,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion2",
      "type": "criterion",
      "name": "问题贡献",
      "attributes": {
        "weight": 2,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion3",
      "type": "criterion",
      "name": "可行性",
      "attributes": {
        "weight": 1,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "options-decision-matrix-default-score00",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion0",
      "label": "偏好值 4；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 4
      }
    },
    {
      "id": "options-decision-matrix-default-score01",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion1",
      "label": "偏好值 4；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 4
      }
    },
    {
      "id": "options-decision-matrix-default-score02",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion2",
      "label": "偏好值 3；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 3
      }
    },
    {
      "id": "options-decision-matrix-default-score03",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion3",
      "label": "偏好值 5；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 5
      }
    },
    {
      "id": "options-decision-matrix-default-score10",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion0",
      "label": "偏好值 2；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 2
      }
    },
    {
      "id": "options-decision-matrix-default-score11",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion1",
      "label": "偏好值 2；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 2
      }
    },
    {
      "id": "options-decision-matrix-default-score12",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion2",
      "label": "偏好值 5；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 5
      }
    },
    {
      "id": "options-decision-matrix-default-score13",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion3",
      "label": "偏好值 2；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 2
      }
    }
  ],
  "view": {
    "id": "v-options-decision-matrix-default",
    "artifact_id": "options-decision-matrix",
    "profile_id": "options-decision-matrix-default",
    "title": "备选方案决策矩阵／虚构案例",
    "entity_ids": [
      "options-decision-matrix-default-option0",
      "options-decision-matrix-default-option1",
      "options-decision-matrix-default-criterion0",
      "options-decision-matrix-default-criterion1",
      "options-decision-matrix-default-criterion2",
      "options-decision-matrix-default-criterion3"
    ],
    "relationship_ids": [
      "options-decision-matrix-default-score00",
      "options-decision-matrix-default-score01",
      "options-decision-matrix-default-score02",
      "options-decision-matrix-default-score03",
      "options-decision-matrix-default-score10",
      "options-decision-matrix-default-score11",
      "options-decision-matrix-default-score12",
      "options-decision-matrix-default-score13"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile options-decision-matrix-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile options-decision-matrix-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
