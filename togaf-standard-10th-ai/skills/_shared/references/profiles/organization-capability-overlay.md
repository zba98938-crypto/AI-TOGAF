# 组织能力叠加地图

`profile_id`: organization-capability-overlay；`artifact_id`: organization-map；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G206/fig7-2。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G206/fig7-2",
  "layout_notes": "能力不参与组织汇报层级，映射线不表示弱汇报",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/organization-capability-overlay.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, organization。关系类型：traces_to。

```json
{
  "entities": {
    "organization": [
      "category",
      "boundary",
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 能力不参与组织汇报层级，映射线不表示弱汇报

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
      "id": "organization-capability-overlay-enterprise",
      "type": "organization",
      "name": "星河零售",
      "attributes": {
        "category": "企业",
        "boundary": "本次架构范围内",
        "definition": "承担在线销售与履约责任"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization-capability-overlay-ops",
      "type": "organization",
      "name": "在线运营",
      "attributes": {
        "category": "业务单元",
        "boundary": "内部",
        "definition": "管理在线订单和客户例外"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization-capability-overlay-carrier",
      "type": "organization",
      "name": "承运合作方",
      "attributes": {
        "category": "外部伙伴",
        "boundary": "企业外部合同边界",
        "definition": "按合同交付商品"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization-capability-overlay-cap",
      "type": "capability",
      "name": "交付管理",
      "attributes": {
        "definition": "维持交付承诺并处理交付例外"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "organization-capability-overlay-works",
      "type": "traces_to",
      "source": "organization-capability-overlay-ops",
      "target": "organization-capability-overlay-carrier",
      "label": "履约协作和例外交接；不是汇报关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization-capability-overlay-contains",
      "type": "traces_to",
      "source": "organization-capability-overlay-enterprise",
      "target": "organization-capability-overlay-ops",
      "label": "在线运营为本企业业务单元",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization-capability-overlay-cap-ops",
      "type": "traces_to",
      "source": "organization-capability-overlay-ops",
      "target": "organization-capability-overlay-cap",
      "label": "在线运营承担该能力内部责任",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization-capability-overlay-cap-ext",
      "type": "traces_to",
      "source": "organization-capability-overlay-carrier",
      "target": "organization-capability-overlay-cap",
      "label": "伙伴参与该能力的配送实现",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-organization-capability-overlay",
    "artifact_id": "organization-map",
    "profile_id": "organization-capability-overlay",
    "title": "组织能力叠加地图／虚构案例",
    "entity_ids": [
      "organization-capability-overlay-enterprise",
      "organization-capability-overlay-ops",
      "organization-capability-overlay-carrier",
      "organization-capability-overlay-cap"
    ],
    "relationship_ids": [
      "organization-capability-overlay-works",
      "organization-capability-overlay-contains",
      "organization-capability-overlay-cap-ops",
      "organization-capability-overlay-cap-ext"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile organization-capability-overlay --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile organization-capability-overlay --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
