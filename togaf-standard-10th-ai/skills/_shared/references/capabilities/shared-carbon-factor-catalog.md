# 共享碳单位数据与因子目录

ID：`shared-carbon-factor-catalog`。主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242 §3.6.3表3-4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些单位数据可在什么边界、版本和单位下复用于环境评估？

- 业务负责人
- 企业架构师
- 环境核算负责人
- 采购及供应商负责人
- HR与治理负责人
- 哪些单位数据可在什么边界、版本和单位下复用于环境评估？
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

对象类型：guide:carbon_reference_data。

```json
{
  "guide:carbon_reference_data": [
    "data_kind",
    "value",
    "unit",
    "period",
    "geography",
    "lifecycle_boundary",
    "applicability",
    "allocation_basis",
    "source_version",
    "source_locator",
    "quality",
    "reuse_limits"
  ]
}
```

{
  "name": {
    "meaning": "单位数据/因子",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "data_kind": {
    "meaning": "活动强度、设备足迹或电力因子等，不全部称排放因子",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "value": {
    "meaning": "原始值；不静默插值",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "unit": {
    "meaning": "原始单位与分母",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "period": {
    "meaning": "适用/观察期间",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "geography": {
    "meaning": "地区/设施/能源结构",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "lifecycle_boundary": {
    "meaning": "制造、运行或组合边界",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "applicability": {
    "meaning": "机型/服务/分配范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "allocation_basis": {
    "meaning": "是否含PUE及服务分配依据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "source_version": {
    "meaning": "来源版本和更新日期",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "source_locator": {
    "meaning": "原料/供应商/计算记录定位",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "quality": {
    "meaning": "测量/估算/未知及不确定性",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "reuse_limits": {
    "meaning": "不可跨何种范围/单位/期间复用",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 收集原始单位数据和来源，不把计算结果当原始因子
2. 声明机型/服务/地区/期间与生命周期边界
3. 核实单位分母、分配与PUE包含情况
4. 登记版本、质量和适用限制
5. 更新时保留旧版及引用该版的评估，禁止静默替换历史计算

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 表3-4非穷尽，不把五类当数量上限
- kWh/年、kgCO2e/台、kWh/vCPU、kgCO2e/币种、kgCO2e/kWh不可混用
- 已含PUE不再次乘PUE；单位数据没有实际服务分配则不得视为已验证
- 共享目录输入核算但本工作产品不产生排放总额

- 表3-4非穷尽，不把五类当数量上限
- kWh/年、kgCO2e/台、kWh/vCPU、kgCO2e/币种、kgCO2e/kWh不可混用
- 已含PUE不再次乘PUE；单位数据没有实际服务分配则不得视为已验证
- 共享目录输入核算但本工作产品不产生排放总额


## 视图和交付物

- [共享碳单位数据与因子目录](../profiles/shared-carbon-factor-catalog-default.md)

- [architecture-repository](../deliverables/architecture-repository.md)
- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "因子缺单位/期间/来源或把制造kgCO2e/台当年度值",
    "expected": "carbon-data-metadata-gap",
    "why": "carbon-data-metadata-gap或boundary-unit-conflict",
    "original_expected_text": "carbon-data-metadata-gap或boundary-unit-conflict"
  },
  "modification_example": {
    "change": "FC-03发布v2地点因子0.35，v1仍存在",
    "expected": "新增版本、适用期与变更理由；既有v1引用不被覆盖"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/shared-carbon-factor-catalog.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。",
  "sources": [
    {
      "id": "src-shared-carbon-factor-catalog-default",
      "kind": "example",
      "description": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。 材料组 factor-catalog",
      "locator": "examples/addenda/sustainability/raw-business-materials.json#factor-catalog"
    }
  ],
  "entities": [
    {
      "id": "shared-carbon-factor-catalog-default-1",
      "type": "guide:carbon_reference_data",
      "name": "平均机型M用电",
      "attributes": {
        "data_kind": "equipment-electricity",
        "value": 45,
        "unit": "kWh/device/year",
        "period": "2026",
        "geography": "企业机型M使用地点",
        "lifecycle_boundary": "operation-electricity",
        "applicability": "机型M，未覆盖其他机型",
        "allocation_basis": "制造商平均用电，不作公司实际电表值",
        "source_version": "FC-01/v1",
        "source_locator": "FC-01",
        "quality": "fictional-manufacturer-estimate",
        "reuse_limits": "不能当制造排放或其他机型因子"
      },
      "evidence": [
        "src-shared-carbon-factor-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "shared-carbon-factor-catalog-default-2",
      "type": "guide:carbon_reference_data",
      "name": "机型M制造足迹",
      "attributes": {
        "data_kind": "equipment-embodied",
        "value": 250,
        "unit": "kgCO2e/device",
        "period": "2026 product version",
        "geography": "机型M制造供应链",
        "lifecycle_boundary": "manufacturing",
        "applicability": "机型M一台的制造足迹",
        "allocation_basis": "整台制造额，未按年度摊销",
        "source_version": "FC-01/v1",
        "source_locator": "FC-01",
        "quality": "fictional-manufacturer-estimate",
        "reuse_limits": "不能当每年排放，也不能再加已含设备的Scope3总额"
      },
      "evidence": [
        "src-shared-carbon-factor-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "shared-carbon-factor-catalog-default-3",
      "type": "guide:carbon_reference_data",
      "name": "自营机房服务分配用电",
      "attributes": {
        "data_kind": "datacenter-activity-intensity",
        "value": 1.2,
        "unit": "kWh/vCPU",
        "period": "2026",
        "geography": "机房A",
        "lifecycle_boundary": "operation-electricity-including-PUE",
        "applicability": "ALLOC-2026中实际服务VM分配",
        "allocation_basis": "包含PUE分摊；VM使用及分配表ALLOC-2026",
        "source_version": "FC-02/v1",
        "source_locator": "FC-02 / ALLOC-2026",
        "quality": "fictional-allocated-measurement",
        "reuse_limits": "不得再次乘PUE；不同期间/vCPU-hour不可直接替换"
      },
      "evidence": [
        "src-shared-carbon-factor-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "shared-carbon-factor-catalog-default-4",
      "type": "guide:carbon_reference_data",
      "name": "云消费强度",
      "attributes": {
        "data_kind": "cloud-spend-intensity",
        "value": 0.02,
        "unit": "kgCO2e/CNY",
        "period": "2026",
        "geography": "供应商已评估服务范围",
        "lifecycle_boundary": "operation-and-manufacturing",
        "applicability": "指定服务及2026计价基准",
        "allocation_basis": "服务消费金额分配，仅本示例规则",
        "source_version": "FC-03/v1",
        "source_locator": "FC-03",
        "quality": "fictional-supplier-estimate",
        "reuse_limits": "货币口径依价格变化，不当通用技术因子"
      },
      "evidence": [
        "src-shared-carbon-factor-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "shared-carbon-factor-catalog-default-5",
      "type": "guide:carbon_reference_data",
      "name": "地点法电力因子",
      "attributes": {
        "data_kind": "grid-emission-factor",
        "value": 0.4,
        "unit": "kgCO2e/kWh",
        "period": "2026",
        "geography": "GRID-X虚构地区",
        "lifecycle_boundary": "location-based-electricity",
        "applicability": "GRID-X；无现实适用性",
        "allocation_basis": "地点法，不是供应商采购合同市场法",
        "source_version": "FC-03/v1",
        "source_locator": "FC-03",
        "quality": "fictional-scenario-factor",
        "reuse_limits": "仅用于示例，禁止默认为项目真实因子"
      },
      "evidence": [
        "src-shared-carbon-factor-catalog-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-shared-carbon-factor-catalog-default",
    "artifact_id": "shared-carbon-factor-catalog",
    "profile_id": "shared-carbon-factor-catalog-default",
    "title": "共享碳单位数据与因子目录",
    "entity_ids": [
      "shared-carbon-factor-catalog-default-1",
      "shared-carbon-factor-catalog-default-2",
      "shared-carbon-factor-catalog-default-3",
      "shared-carbon-factor-catalog-default-4",
      "shared-carbon-factor-catalog-default-5"
    ],
    "relationship_ids": [],
    "analysis": "保留表3-4五类原始单位数据及边界/分配/PUE信息；它们不是五个通用排放因子，不做新的环境总额计算。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "factor-catalog"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact shared-carbon-factor-catalog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
