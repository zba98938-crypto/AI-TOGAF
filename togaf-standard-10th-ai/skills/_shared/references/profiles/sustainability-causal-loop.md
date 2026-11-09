# 数字增长因果回路

`profile_id`: sustainability-causal-loop；`artifact_id`: environmental-is-assessment；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242/fig1-2。

## 构图与定义状态

表示族：`causal`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G242/fig1-2",
  "layout_notes": "正负号表示变化方向，强化与平衡回路不能混淆",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/sustainability-causal-loop.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：measure。关系类型：causal_influence。

```json
{
  "entities": {
    "measure": [
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 正负号表示变化方向，强化与平衡回路不能混淆

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
      "id": "sustainability-causal-loop-usage",
      "type": "measure",
      "name": "数字使用量",
      "attributes": {
        "definition": "在既定边界内的数字服务使用量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-causal-loop-infra",
      "type": "measure",
      "name": "基础设施投入",
      "attributes": {
        "definition": "为满足使用需求增加的计算与设备"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-causal-loop-cost",
      "type": "measure",
      "name": "单位数字服务成本",
      "attributes": {
        "definition": "在明确服务与期间内的成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "sustainability-causal-loop-a-b",
      "type": "causal_influence",
      "source": "sustainability-causal-loop-usage",
      "target": "sustainability-causal-loop-infra",
      "label": "使用增加推动基础设施需求",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "polarity": "+"
      }
    },
    {
      "id": "sustainability-causal-loop-b-c",
      "type": "causal_influence",
      "source": "sustainability-causal-loop-infra",
      "target": "sustainability-causal-loop-cost",
      "label": "规模效应可能降低单位成本，待本地验证",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "polarity": "-"
      }
    },
    {
      "id": "sustainability-causal-loop-c-a",
      "type": "causal_influence",
      "source": "sustainability-causal-loop-cost",
      "target": "sustainability-causal-loop-usage",
      "label": "成本降低可能促使更多使用",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "polarity": "-"
      }
    }
  ],
  "view": {
    "id": "v-sustainability-causal-loop",
    "artifact_id": "environmental-is-assessment",
    "profile_id": "sustainability-causal-loop",
    "title": "数字增长因果回路／虚构案例",
    "entity_ids": [
      "sustainability-causal-loop-usage",
      "sustainability-causal-loop-infra",
      "sustainability-causal-loop-cost"
    ],
    "relationship_ids": [
      "sustainability-causal-loop-a-b",
      "sustainability-causal-loop-b-c",
      "sustainability-causal-loop-c-a"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。",
    "attributes": {
      "loops": [
        {
          "id": "R1",
          "type": "reinforcing",
          "relationship_ids": [
            "sustainability-causal-loop-a-b",
            "sustainability-causal-loop-b-c",
            "sustainability-causal-loop-c-a"
          ],
          "evidence": "本例假设；边极性乘积为正，不证明现实因果"
        }
      ]
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-causal-loop --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-causal-loop --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
