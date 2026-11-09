# 云环境数据共享契约19字段

`profile_id`: cloud-environmental-data-contract-default；`artifact_id`: cloud-environmental-data-contract；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G242 §6表6-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "cloud-environmental-data-contract-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:cloud_environmental_field。关系类型：。

```json
{
  "entities": {
    "guide:cloud_environmental_field": [
      "sequence",
      "field_key",
      "value",
      "unit",
      "period",
      "service_boundary",
      "semantics",
      "evidence_refs",
      "quality"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- G242提出数据共享模型，不宣称已成为国际标准
- Period允许年/月而若干描述写完整年度，必须逐值声明期间，不自动年化
- 供应方scope标签与消费者组织范围归属不同
- 市场法和地点法不能相加，设备子集不与Scope3总量相加，抵消不抵掉报送原始值
- 复制后存储量不是逻辑原始数据；制造水未知不能记零

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。",
  "sources": [
    {
      "id": "src-cloud-environmental-data-contract-default",
      "kind": "example",
      "description": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。 材料组 cloud",
      "locator": "examples/addenda/sustainability/raw-business-materials.json#cloud"
    }
  ],
  "entities": [
    {
      "id": "cloud-environmental-data-contract-default-1",
      "type": "guide:cloud_environmental_field",
      "name": "提供方名称",
      "attributes": {
        "sequence": 1,
        "field_key": "provider_name",
        "value": "Atlas示例云",
        "unit": "text",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "supplier identifier",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-2",
      "type": "guide:cloud_environmental_field",
      "name": "被评估服务",
      "attributes": {
        "sequence": 2,
        "field_key": "provider_evaluated_service",
        "value": "工单SaaS",
        "unit": "text",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "specific service",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-3",
      "type": "guide:cloud_environmental_field",
      "name": "相关组织实体",
      "attributes": {
        "sequence": 3,
        "field_key": "concerned_organization_entities",
        "value": [
          "澄源客服部",
          "澄源运营部"
        ],
        "unit": "list",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "customer entities",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-4",
      "type": "guide:cloud_environmental_field",
      "name": "期间",
      "attributes": {
        "sequence": 4,
        "field_key": "period",
        "value": "2026",
        "unit": "year/month",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "reporting period; annual definitions remain explicit",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-5",
      "type": "guide:cloud_environmental_field",
      "name": "用电量",
      "attributes": {
        "sequence": 5,
        "field_key": "electricity_consumption_kwh",
        "value": 120000,
        "unit": "kWh",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "gross allocated service electricity",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-6",
      "type": "guide:cloud_environmental_field",
      "name": "采购可再生电力",
      "attributes": {
        "sequence": 6,
        "field_key": "renewable_electricity_purchased_kwh",
        "value": 80000,
        "unit": "kWh",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "purchase disclosure; not a subtraction",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-7",
      "type": "guide:cloud_environmental_field",
      "name": "Scope2市场法",
      "attributes": {
        "sequence": 7,
        "field_key": "scope2_market_based_kgco2e",
        "value": 18000,
        "unit": "kgCO2e",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "alternative accounting basis; do not add to location-based",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-8",
      "type": "guide:cloud_environmental_field",
      "name": "Scope2地点法",
      "attributes": {
        "sequence": 8,
        "field_key": "scope2_location_based_kgco2e",
        "value": 48000,
        "unit": "kgCO2e",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "alternative accounting basis; do not add to market-based",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-9",
      "type": "guide:cloud_environmental_field",
      "name": "PUE",
      "attributes": {
        "sequence": 9,
        "field_key": "pue",
        "value": 1.4,
        "unit": "ratio",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "hosting efficiency; included-allocation must be declared",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-10",
      "type": "guide:cloud_environmental_field",
      "name": "Scope2计算说明",
      "attributes": {
        "sequence": 10,
        "field_key": "scope2_calculation_comments",
        "value": "市场法按服务采购合同；地点法按设施区域；分配已包含PUE，不再次乘；原始排放未扣抵消",
        "unit": "text",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "optional comments; explicit missing allowed",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-11",
      "type": "guide:cloud_environmental_field",
      "name": "Scope3总量",
      "attributes": {
        "sequence": 11,
        "field_key": "total_scope3_kgco2e",
        "value": 9000,
        "unit": "kgCO2e",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "supplier total allocated to service",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-12",
      "type": "guide:cloud_environmental_field",
      "name": "数字设备Scope3子集",
      "attributes": {
        "sequence": 12,
        "field_key": "digital_equipment_scope3_kgco2e",
        "value": 6000,
        "unit": "kgCO2e",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "subset of total_scope3_kgco2e, not additive",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-13",
      "type": "guide:cloud_environmental_field",
      "name": "Scope3计算说明",
      "attributes": {
        "sequence": 13,
        "field_key": "scope3_calculation_comments",
        "value": "供应方范围3按客户实际服务分配，设备制造为子集；不自动等同客户GHG范围归属",
        "unit": "text",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "optional comments; explicit missing allowed",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-14",
      "type": "guide:cloud_environmental_field",
      "name": "碳信用与抵消",
      "attributes": {
        "sequence": 14,
        "field_key": "carbon_credits_offsets_kgco2e",
        "value": 5000,
        "unit": "kgCO2e",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "separate disclosure; do not net reported gross emissions",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-15",
      "type": "guide:cloud_environmental_field",
      "name": "数字废弃物重量",
      "attributes": {
        "sequence": 15,
        "field_key": "digital_waste_kg",
        "value": 120,
        "unit": "kg",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "disposed equipment in declared period/boundary",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-16",
      "type": "guide:cloud_environmental_field",
      "name": "回收数字废弃物",
      "attributes": {
        "sequence": 16,
        "field_key": "recycled_digital_waste_kg",
        "value": 100,
        "unit": "kg",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "collected for recycling; boundary/lot must be clear",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-17",
      "type": "guide:cloud_environmental_field",
      "name": "水消耗",
      "attributes": {
        "sequence": 17,
        "field_key": "water_consumption",
        "value": {
          "value": 300,
          "unit": "m3",
          "lifecycle_stage": "use-cooling",
          "manufacturing_value": null,
          "gap": "制造水未知；总生命周期水不可计算"
        },
        "unit": "m3",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "manufacturing/use phase split or explicit phase scope",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "manufacturing-water-missing"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-18",
      "type": "guide:cloud_environmental_field",
      "name": "存储数据量含复制",
      "attributes": {
        "sequence": 18,
        "field_key": "stored_data_gb_including_replication",
        "value": 6000,
        "unit": "GB",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "include all replicas, distinguish logical original；存储6000GB含3份复制，逻辑原始2000GB",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cloud-environmental-data-contract-default-19",
      "type": "guide:cloud_environmental_field",
      "name": "进出网络流量总量",
      "attributes": {
        "sequence": 19,
        "field_key": "network_traffic_gb",
        "value": 90000,
        "unit": "GB",
        "period": "2026",
        "service_boundary": "Atlas工单SaaS→澄源客服/运营；按实际服务用量分配；供应方报告范围不自动成为客户范围",
        "semantics": "inbound plus outbound over declared period",
        "evidence_refs": [
          "CL-01",
          "CL-02",
          "CL-03",
          "CL-04"
        ],
        "quality": "fictional-supplier-record"
      },
      "evidence": [
        "src-cloud-environmental-data-contract-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-cloud-environmental-data-contract-default",
    "artifact_id": "cloud-environmental-data-contract",
    "profile_id": "cloud-environmental-data-contract-default",
    "title": "云环境数据共享契约19字段",
    "entity_ids": [
      "cloud-environmental-data-contract-default-1",
      "cloud-environmental-data-contract-default-2",
      "cloud-environmental-data-contract-default-3",
      "cloud-environmental-data-contract-default-4",
      "cloud-environmental-data-contract-default-5",
      "cloud-environmental-data-contract-default-6",
      "cloud-environmental-data-contract-default-7",
      "cloud-environmental-data-contract-default-8",
      "cloud-environmental-data-contract-default-9",
      "cloud-environmental-data-contract-default-10",
      "cloud-environmental-data-contract-default-11",
      "cloud-environmental-data-contract-default-12",
      "cloud-environmental-data-contract-default-13",
      "cloud-environmental-data-contract-default-14",
      "cloud-environmental-data-contract-default-15",
      "cloud-environmental-data-contract-default-16",
      "cloud-environmental-data-contract-default-17",
      "cloud-environmental-data-contract-default-18",
      "cloud-environmental-data-contract-default-19"
    ],
    "relationship_ids": [],
    "analysis": "逐行保留G242表6-1拟议最小数据集：Scope2两法并行不相加；设备6000为Scope3总9000子集；抵消5000独列；存储6000含复制。制造水未知，不能宣称全生命周期数据完全。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "cloud"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile cloud-environmental-data-contract-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile cloud-environmental-data-contract-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
