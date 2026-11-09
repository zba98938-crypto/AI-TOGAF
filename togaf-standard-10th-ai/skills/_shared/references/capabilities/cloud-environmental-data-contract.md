# 云与外包环境数据共享契约

ID：`cloud-environmental-data-contract`。主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G242 §6表6-1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

服务提供方应以哪些边界和口径交付可审查环境数据？

- 业务负责人
- 企业架构师
- 环境核算负责人
- 采购及供应商负责人
- HR与治理负责人
- 服务提供方应以哪些边界和口径交付可审查环境数据？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 组织、服务、业务用途及所评估期间/生命周期边界
- 原始访谈、使用数据、供应商记录及稳定证据ID
- 适用目标、职责和组织自定决策规则；未知项显式登记

可选：

- 历史评估、环境数据目录、采购契约及角色技能资料

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:cloud_environmental_field。

```json
{
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
}
```

{
  "name": {
    "meaning": "数据项名",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "sequence": {
    "meaning": "G242拟议19字段顺序",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "field_key": {
    "meaning": "稳定字段key",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "value": {
    "meaning": "供应方原始值，未知显式保存",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "unit": {
    "meaning": "原始单位",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "period": {
    "meaning": "该值测量期间",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "service_boundary": {
    "meaning": "服务/组织实体/生命周期/分配边界",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "semantics": {
    "meaning": "互斥、包含、抵消、复制等含义",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "供应方报告/方法证据ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "quality": {
    "meaning": "完整/未知及口径待确认",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 确认提供方、服务、使用实体、期间与服务分配依据
2. 按拟议19字段逐项收集原始值和单位、测量期间
3. 同时保留市场/地点Scope2，设备Scope3包含关系及抵消独列
4. 检查年度/月度、制造/运行水、复制存储与进出流量口径
5. 给缺口/冲突清单后交给独立核算方法；不在数据契约中自动合计排放

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- G242提出数据共享模型，不宣称已成为国际标准
- Period允许年/月而若干描述写完整年度，必须逐值声明期间，不自动年化
- 供应方scope标签与消费者组织范围归属不同
- 市场法和地点法不能相加，设备子集不与Scope3总量相加，抵消不抵掉报送原始值
- 复制后存储量不是逻辑原始数据；制造水未知不能记零

- G242提出数据共享模型，不宣称已成为国际标准
- Period允许年/月而若干描述写完整年度，必须逐值声明期间，不自动年化
- 供应方scope标签与消费者组织范围归属不同
- 市场法和地点法不能相加，设备子集不与Scope3总量相加，抵消不抵掉报送原始值
- 复制后存储量不是逻辑原始数据；制造水未知不能记零


## 视图和交付物

- [云环境数据共享契约19字段](../profiles/cloud-environmental-data-contract-default.md)

- [architecture-contract](../deliverables/architecture-contract.md)
- [architecture-repository](../deliverables/architecture-repository.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "设备子集10000大于同边界Scope3总9000；或要求把两种Scope2相加",
    "expected": "scope3-subset-exceeds-total",
    "why": "scope3-subset-exceeds-total或scope2-bases-not-additive",
    "original_expected_text": "scope3-subset-exceeds-total或scope2-bases-not-additive"
  },
  "modification_example": {
    "change": "Scope3设备子集从6000更新为7000，总额仍9000",
    "expected": "子集更新且仍不相加；两种Scope2与抵消保持独立"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/cloud-environmental-data-contract.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact cloud-environmental-data-contract --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
