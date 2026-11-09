# 四框业务模型

`profile_id`: four-box-business-model-default；`artifact_id`: four-box-business-model；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G18A/fig2-2。

## 构图与定义状态

表示族：`four-box`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_model_component。关系类型：traces_to。

```json
{
  "entities": {
    "business_model_component": [
      "component",
      "detail",
      "assumptions"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 四框不能用九块画布或六维立方体的字段替代，利润公式需要明确变量而非捏造收益
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
      "id": "four-box-business-model-default-0",
      "type": "business_model_component",
      "name": "客户价值主张",
      "attributes": {
        "component": "客户价值主张",
        "detail": "让线上客户按承诺获得可用商品",
        "assumptions": "客户愿为可靠性选择本商店，需研究验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "four-box-business-model-default-1",
      "type": "business_model_component",
      "name": "利润公式",
      "attributes": {
        "component": "利润公式",
        "detail": "候选利润=销售收入−商品采购−履约变动成本−约定期间固定成本",
        "assumptions": "本例未给财务值，不形成收益结论"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "four-box-business-model-default-2",
      "type": "business_model_component",
      "name": "关键资源",
      "attributes": {
        "component": "关键资源",
        "detail": "受控库存、仓库团队、订单信息及合作承运商",
        "assumptions": "库存准确性及承运能力待核实"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "four-box-business-model-default-3",
      "type": "business_model_component",
      "name": "关键流程",
      "attributes": {
        "component": "关键流程",
        "detail": "确认购买承诺、拣配发运、处理例外",
        "assumptions": "需业务责任方验证流程边界"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "four-box-business-model-default-alignment1",
      "type": "traces_to",
      "source": "four-box-business-model-default-1",
      "target": "four-box-business-model-default-0",
      "label": "候选一致性：支持价值主张；不是原图箭头或已证实因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "four-box-business-model-default-alignment2",
      "type": "traces_to",
      "source": "four-box-business-model-default-2",
      "target": "four-box-business-model-default-0",
      "label": "候选一致性：支持价值主张；不是原图箭头或已证实因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "four-box-business-model-default-alignment3",
      "type": "traces_to",
      "source": "four-box-business-model-default-3",
      "target": "four-box-business-model-default-0",
      "label": "候选一致性：支持价值主张；不是原图箭头或已证实因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-four-box-business-model-default",
    "artifact_id": "four-box-business-model",
    "profile_id": "four-box-business-model-default",
    "title": "四框业务模型／虚构案例",
    "entity_ids": [
      "four-box-business-model-default-0",
      "four-box-business-model-default-1",
      "four-box-business-model-default-2",
      "four-box-business-model-default-3"
    ],
    "relationship_ids": [
      "four-box-business-model-default-alignment1",
      "four-box-business-model-default-alignment2",
      "four-box-business-model-default-alignment3"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile four-box-business-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile four-box-business-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
