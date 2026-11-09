# 可持续ICT采购战略

ID：`sustainable-procurement-strategy`。主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G242 §3.7.1–3.7.3、§4.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

如何在服务范围、地点、合同和全生命周期中形成可证实采购选择？

- 业务负责人
- 企业架构师
- 环境核算负责人
- 采购及供应商负责人
- HR与治理负责人
- 如何在服务范围、地点、合同和全生命周期中形成可证实采购选择？
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

对象类型：guide:sustainable_procurement。

```json
{
  "guide:sustainable_procurement": [
    "option",
    "sourcing",
    "location",
    "lifecycle_evidence",
    "whole_life_tco",
    "means_obligations",
    "result_obligations",
    "end_of_use",
    "supply_chain_access",
    "gaps",
    "decision_rule",
    "recommendation",
    "authority"
  ]
}
```

{
  "name": {
    "meaning": "采购方案",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "option": {
    "meaning": "候选方案/范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "sourcing": {
    "meaning": "内包/外包/采购/服务获取",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "location": {
    "meaning": "在岸/近岸/离岸及实际地区证据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "lifecycle_evidence": {
    "meaning": "端到端足迹、可再生采购和抵消分列",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "whole_life_tco": {
    "meaning": "购置、运行、维护、退出等范围和缺项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "means_obligations": {
    "meaning": "证明培训/方法/度量等手段",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "result_obligations": {
    "meaning": "可验证成果承诺",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "end_of_use": {
    "meaning": "翻新/回收/拆解去向与证据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "supply_chain_access": {
    "meaning": "中间环节/供应链访问和演进参与",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "gaps": {
    "meaning": "影响比较和选择的数据缺口",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision_rule": {
    "meaning": "组织自定准则，不默认权重",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "recommendation": {
    "meaning": "候选处理，不自动选商",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "authority": {
    "meaning": "发起人决定、法务审查等",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 明确业务用途寿命及采购/外包/所在地方案
2. 要求端到端数据、抵消与可再生采购分别公开
3. 与法务将手段义务和结果义务分别写成可验证条款
4. 比较全生命周期成本、修理能力、退出及供应链访问
5. 按有来源的组织准则权衡；缺资料时给补证/不选择结论

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 在岸、租赁、云或认证称号不能自动证明低足迹
- 抵消后的净零不能代替端到端排放透明度
- 不造权重或最低合格分；对外采购须实际授权

- 在岸、租赁、云或认证称号不能自动证明低足迹
- 抵消后的净零不能代替端到端排放透明度
- 不造权重或最低合格分；对外采购须实际授权


## 视图和交付物

- [可持续ICT采购战略](../profiles/sustainable-procurement-strategy-default.md)

- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)
- [architecture-contract](../deliverables/architecture-contract.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "将“零碳”宣传单独作为完整足迹证据",
    "expected": "procurement-transparency-gap"
  },
  "modification_example": {
    "change": "B提交排放/抵消独列和设备去向，但仍无五年TCO",
    "expected": "仅关闭已补资料缺口，仍不能完整比较或自动选B"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/sustainable-procurement-strategy.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。",
  "sources": [
    {
      "id": "src-sustainable-procurement-strategy-default",
      "kind": "example",
      "description": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。 材料组 procurement",
      "locator": "examples/addenda/sustainability/raw-business-materials.json#procurement"
    }
  ],
  "entities": [
    {
      "id": "sustainable-procurement-strategy-default-1",
      "type": "guide:sustainable_procurement",
      "name": "A本地翻新",
      "attributes": {
        "option": "A本地翻新 / 100终端5年业务用途",
        "sourcing": "purchase-refurbished",
        "location": "onshore；具体地区待核实",
        "lifecycle_evidence": "愿供制造/维修/退出数据；尚未收齐",
        "whole_life_tco": "5年TCO待补；不只比较购置价",
        "means_obligations": "维修人员培训记录、环境数据报告方法与审查权",
        "result_obligations": "项目要求5年备件可得性、退出设备逐台追踪；由法务/发起人确认",
        "end_of_use": "愿提供维修及设备回收去向",
        "supply_chain_access": "直接与供方协作，需核实制造中间环节",
        "gaps": [
          "完整足迹",
          "五年TCO",
          "退出合同"
        ],
        "decision_rule": "PR-03：先证据透明和可验证维修支持；无评分权重",
        "recommendation": "补证后比较；当前不选择供应商",
        "authority": "法务审查条款，采购准备，发起人决定"
      },
      "evidence": [
        "src-sustainable-procurement-strategy-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainable-procurement-strategy-default-2",
      "type": "guide:sustainable_procurement",
      "name": "B远程租赁",
      "attributes": {
        "option": "B远程租赁 / 100终端5年业务用途",
        "sourcing": "outsource-lease",
        "location": "offshore；电力结构待核实",
        "lifecycle_evidence": "只报抵消后零碳，缺总额与抵消拆分",
        "whole_life_tco": "2年换机与5年服务成本未统一",
        "means_obligations": "维修人员培训记录、环境数据报告方法与审查权",
        "result_obligations": "项目要求5年备件可得性、退出设备逐台追踪；由法务/发起人确认",
        "end_of_use": "设备退还后去向不明",
        "supply_chain_access": "需供应方演进参与机制",
        "gaps": [
          "制造足迹",
          "Scope2两法",
          "抵消拆分",
          "服务分配",
          "五年TCO",
          "退出去向"
        ],
        "decision_rule": "PR-03：先证据透明和可验证维修支持；无评分权重",
        "recommendation": "补证后比较；当前不选择供应商",
        "authority": "法务审查条款，采购准备，发起人决定"
      },
      "evidence": [
        "src-sustainable-procurement-strategy-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-sustainable-procurement-strategy-default",
    "artifact_id": "sustainable-procurement-strategy",
    "profile_id": "sustainable-procurement-strategy-default",
    "title": "可持续ICT采购战略",
    "entity_ids": [
      "sustainable-procurement-strategy-default-1",
      "sustainable-procurement-strategy-default-2"
    ],
    "relationship_ids": [],
    "analysis": "比较A/B内外获取方式、位置、生命周期TCO、手段与结果义务、退出去向；资料不足不排名，不因租赁/在岸或零碳宣传直接作可持续结论。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "procurement"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact sustainable-procurement-strategy --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
