# 微服务业务价值与开发运营资源

`profile_id`: msa-value-resource-evidence；`artifact_id`: microservice-value-catalog；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G21I §11.3、§12.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "msa-value-resource-evidence",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "结构化表格，含完整属性、方向和证据；不是来源图模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:msa_value_resource。关系类型：。

```json
{
  "entities": {
    "ops:msa_value_resource": [
      "service_status",
      "ABF",
      "value",
      "development_resources",
      "operations_resources",
      "owner",
      "work_package_ref",
      "architecture_state_ref",
      "evidence_detail",
      "cost_and_return",
      "gap"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 四格都存在；unknown不等于0
- 人日与人时不无规则相加
- 未来计划不改为已分配
- 不自创成本率或ROI公式

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/msa-value-resource-evidence/raw-brief.md",
  "analysis_path": "examples/addenda/operations/msa-value-resource-evidence/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚维修容量表CAP-11：试点已实现预约时段判断，一个ABF；11月开发已分配12人日、运营16人时，12月计划开发5人日、运营20人时。备件可用判断尚计划，11月两类资源为零分配；12月计划9开发人日，运营工时未知。预约服务关联WP-appointment/T-pilot，备件关联WP-parts/T-expanded（外部引用，非本例已定义架构状态）。尚无成本单价或ROI口径。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MS-V1",
      "type": "ops:msa_value_resource",
      "name": "预约时段判断",
      "attributes": {
        "service_status": "realized-in-fictional-pilot",
        "ABF": "判断指定区域时段是否可预约",
        "value": "让客服在通话中得到可约结论",
        "development_resources": {
          "allocated": {
            "value": 12,
            "unit": "person-day",
            "period": "2026-11"
          },
          "planned": {
            "value": 5,
            "unit": "person-day",
            "period": "2026-12"
          }
        },
        "operations_resources": {
          "allocated": {
            "value": 16,
            "unit": "person-hour",
            "period": "2026-11"
          },
          "planned": {
            "value": 20,
            "unit": "person-hour",
            "period": "2026-12"
          }
        },
        "owner": "预约团队",
        "work_package_ref": "WP-appointment",
        "architecture_state_ref": "T-pilot",
        "evidence_detail": "虚构容量表CAP-11；非实际费用账单",
        "cost_and_return": {
          "cost": "unknown；无成本单价",
          "ROI": "not-calculated；无项目财务规则"
        },
        "gap": "12月均为计划，尚未分配"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MS-V2",
      "type": "ops:msa_value_resource",
      "name": "备件可用判断",
      "attributes": {
        "service_status": "planned",
        "ABF": "判断指定备件与站点在时间点可用数量",
        "value": "降低答应上门后无件的风险",
        "development_resources": {
          "allocated": {
            "value": 0,
            "unit": "person-day",
            "period": "2026-11"
          },
          "planned": {
            "value": 9,
            "unit": "person-day",
            "period": "2026-12"
          }
        },
        "operations_resources": {
          "allocated": {
            "value": 0,
            "unit": "person-hour",
            "period": "2026-11"
          },
          "planned": {
            "value": null,
            "unit": "person-hour",
            "period": "2026-12"
          }
        },
        "owner": "库存团队（提案）",
        "work_package_ref": "WP-parts",
        "architecture_state_ref": "T-expanded",
        "evidence_detail": "虚构容量表CAP-11；非实际费用账单",
        "cost_and_return": {
          "cost": "unknown；无成本单价",
          "ROI": "not-calculated；无项目财务规则"
        },
        "gap": "备件运营计划工时未知，不能视零成本"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [],
  "view": {
    "id": "v-msa-value-resource-evidence",
    "artifact_id": "microservice-value-catalog",
    "profile_id": "msa-value-resource-evidence",
    "title": "微服务业务价值与开发运营资源",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "MS-V1",
      "MS-V2"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-value-resource-evidence --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-value-resource-evidence --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
