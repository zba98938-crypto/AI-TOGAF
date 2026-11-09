# 环境架构评审画布

`profile_id`: sustainability-architecture-canvas；`artifact_id`: sustainability-review-canvas；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G242/fig3-14。

## 构图与定义状态

表示族：`environmental-review`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G242/fig3-14",
  "layout_notes": "保留原始数值与舍入差异，不把误读列头写入规则",
  "review_status": "source-located-awaiting-template-validation",
  "blocks": [
    "业务贡献",
    "环境核算",
    "架构措施"
  ],
  "canvas_kind": "sustainability",
  "form_contract": "G242-fig3-14/1",
  "verification_evidence": "reviews/source-verification/sustainability-architecture-canvas.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：sustainability_action。关系类型：。

```json
{
  "entities": {
    "sustainability_action": [
      "block"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 逐项表达三项业务判断、两年Scope碳表和五项措施；缺字段必须报告ID化错误，不降级为通用画布。
- 印刷原图差异与虚构项目数值分开，不静默改数。

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
      "id": "sustainability-architecture-canvas-0",
      "type": "sustainability_action",
      "name": "业务环境正向影响",
      "attributes": {
        "block": "业务贡献",
        "decisions": [
          {
            "id": "measure",
            "selected": "YES",
            "explanation": "候选系统记录仓配电力活动；需验证数据可得性"
          },
          {
            "id": "reduce",
            "selected": "NO",
            "explanation": "尚无可证实的客户侧减排因果结果"
          },
          {
            "id": "train",
            "selected": "YES",
            "explanation": "向运营人员展示候选环境指标口径"
          }
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-architecture-canvas-1",
      "type": "sustainability_action",
      "name": "IT 碳足迹候选核算",
      "attributes": {
        "block": "环境核算",
        "carbon_footprint": {
          "direction": "Decrease",
          "unit": "kgCO2e",
          "years": [
            2026,
            2027
          ],
          "rows": [
            {
              "id": "in",
              "total": 120,
              "values": {
                "year1": {
                  "scope2": 30,
                  "scope3_service": 20,
                  "equipment_scope3": 70
                },
                "year2": {
                  "scope2": 0,
                  "scope3_service": 0,
                  "equipment_scope3": 0
                }
              }
            },
            {
              "id": "out",
              "total": 150,
              "values": {
                "year1": {
                  "scope2": 50,
                  "scope3_service": 20,
                  "equipment_scope3": 80
                },
                "year2": {
                  "scope2": 0,
                  "scope3_service": 0,
                  "equipment_scope3": 0
                }
              }
            },
            {
              "id": "balance",
              "total": -30,
              "values": {
                "year1": {
                  "scope2": -20,
                  "scope3_service": 0,
                  "equipment_scope3": -10
                },
                "year2": {
                  "scope2": 0,
                  "scope3_service": 0,
                  "equipment_scope3": 0
                }
              }
            }
          ],
          "comment": "虚构项目演练数据；边界、排放因子及真实测量尚未确认。原图印刷差异单列于来源解释，不套用为本项目数值。"
        }
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-architecture-canvas-2",
      "type": "sustainability_action",
      "name": "架构环境措施",
      "attributes": {
        "block": "架构措施",
        "measures": [
          {
            "id": "development",
            "selected": "YES",
            "explanation": "候选开发评审"
          },
          {
            "id": "equipment",
            "selected": "YES",
            "explanation": "候选寿命比较"
          },
          {
            "id": "procurement",
            "selected": "NO",
            "explanation": "采购准则未批准"
          },
          {
            "id": "data",
            "selected": "YES",
            "explanation": "候选保留策略"
          },
          {
            "id": "users",
            "selected": "NO",
            "explanation": "尚无用户研究"
          }
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-sustainability-architecture-canvas",
    "artifact_id": "sustainability-review-canvas",
    "profile_id": "sustainability-architecture-canvas",
    "title": "环境架构评审画布／虚构案例",
    "entity_ids": [
      "sustainability-architecture-canvas-0",
      "sustainability-architecture-canvas-1",
      "sustainability-architecture-canvas-2"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-architecture-canvas --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-architecture-canvas --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
