# 解决方案概念图（兼容默认）

`profile_id`: compat-solution-concept-diagram；`artifact_id`: solution-concept-diagram；主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G248；G186；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-solution-concept-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, application, technology, actor。关系类型：uses_application, supports_capability, runs_on, supports_capability。

```json
{
  "entities": {
    "capability": [],
    "application": [
      "responsibility"
    ],
    "technology": [
      "responsibility"
    ],
    "actor": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 概念方案不是产品采购决定
- 不要在高层图埋入未经确认的物理设计

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构兼容案例；不是正式定义或来源图复刻。",
  "sources": [
    {
      "id": "case",
      "kind": "example",
      "description": "全量验收使用的虚构业务情景；数字、主体和架构均非真实项目事实。"
    },
    {
      "id": "assumption",
      "kind": "assumption",
      "description": "方案和收益因果假设，需在真实项目中验证。"
    }
  ],
  "entities": [
    {
      "id": "cap-order",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "维护订单承诺及履行状态",
        "owner": "销售负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "actor-customer",
      "type": "actor",
      "name": "客户参与者",
      "attributes": {
        "category": "外部主体",
        "owner": "客户服务负责人",
        "boundary": "外部",
        "jurisdiction": "示例境内"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "app-web",
      "type": "application",
      "name": "线上商城",
      "attributes": {
        "owner": "应用负责人",
        "lifecycle": "候选目标",
        "criticality": "业务关键",
        "cost": "待估算",
        "jurisdiction": "示例境内",
        "automation": "辅助业务确认",
        "responsibility": "支持客户购买与订单履约",
        "boundary": "订单履约系统边界",
        "version": "候选或现状示例版本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "app-oms",
      "type": "application",
      "name": "目标订单应用",
      "attributes": {
        "owner": "应用负责人",
        "lifecycle": "候选目标",
        "criticality": "业务关键",
        "cost": "待估算",
        "jurisdiction": "示例境内",
        "automation": "辅助业务确认",
        "capacity": 250,
        "responsibility": "支持客户购买与订单履约",
        "boundary": "订单履约系统边界",
        "version": "候选或现状示例版本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "concept_id": "order-management-system",
      "evolution": "target"
    },
    {
      "id": "tech-platform",
      "type": "technology",
      "name": "应用运行节点",
      "attributes": {
        "product": "示例通用平台产品",
        "version": "候选版本",
        "owner": "平台负责人",
        "lifecycle": "候选",
        "support_end": "待厂商确认",
        "capacity": "待压测",
        "redundancy": "跨两个示例故障域",
        "protocol": "TLS",
        "ports": "443",
        "trust": "业务服务区",
        "responsibility": "承载运行服务",
        "standard": "受支持运行时"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "customer-web",
      "type": "uses_application",
      "source": "actor-customer",
      "target": "app-web",
      "label": "通过商城购买",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "app-tech",
      "type": "runs_on",
      "source": "app-oms",
      "target": "tech-platform",
      "label": "部署于目标运行节点",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "runs_on"
      ]
    },
    {
      "id": "app-cap",
      "type": "supports_capability",
      "source": "app-oms",
      "target": "cap-order",
      "label": "应用支撑订单能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-solution-concept-diagram",
    "artifact_id": "solution-concept-diagram",
    "title": "解决方案概念图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "context",
      "evolution": "target"
    },
    "entity_ids": [
      "actor-customer",
      "app-web",
      "app-oms",
      "tech-platform",
      "cap-order"
    ],
    "relationship_ids": [
      "customer-web",
      "app-tech",
      "app-cap"
    ],
    "analysis": "哪些主要构件以何种总体方案解决业务问题？ 本视图限定订单履约改造范围，展示案例设定的解决方案概念图。从业务问题和关键需求出发；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-solution-concept-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-solution-concept-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-solution-concept-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
