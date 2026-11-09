# 共享碳单位数据与因子目录

`profile_id`: shared-carbon-factor-catalog-default；`artifact_id`: shared-carbon-factor-catalog；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242 §3.6.3表3-4。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "shared-carbon-factor-catalog-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:carbon_reference_data。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 表3-4非穷尽，不把五类当数量上限
- kWh/年、kgCO2e/台、kWh/vCPU、kgCO2e/币种、kgCO2e/kWh不可混用
- 已含PUE不再次乘PUE；单位数据没有实际服务分配则不得视为已验证
- 共享目录输入核算但本工作产品不产生排放总额

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile shared-carbon-factor-catalog-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile shared-carbon-factor-catalog-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
