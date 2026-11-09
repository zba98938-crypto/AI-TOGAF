# 可持续ICT采购战略

`profile_id`: sustainable-procurement-strategy-default；`artifact_id`: sustainable-procurement-strategy；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G242 §3.7.1–3.7.3、§4.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "sustainable-procurement-strategy-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:sustainable_procurement。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 在岸、租赁、云或认证称号不能自动证明低足迹
- 抵消后的净零不能代替端到端排放透明度
- 不造权重或最低合格分；对外采购须实际授权

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainable-procurement-strategy-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainable-procurement-strategy-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
