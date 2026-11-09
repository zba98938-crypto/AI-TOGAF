# 应用与用户位置图（兼容默认）

`profile_id`: compat-application-and-user-location-diagram；`artifact_id`: application-and-user-location-diagram；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G206；G248。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-application-and-user-location-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：actor, application, location。关系类型：uses_application, located_at。

```json
{
  "entities": {
    "actor": [
      "jurisdiction"
    ],
    "application": [],
    "location": [
      "jurisdiction"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 用户所属组织不能代替地理位置
- 远程访问不等于同站点部署

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
      "id": "loc-east",
      "type": "location",
      "name": "东区配送中心",
      "attributes": {
        "category": "业务站点",
        "jurisdiction": "示例东区",
        "availability_zone": "不适用：业务地点"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "loc-cloud",
      "type": "location",
      "name": "示例云区域 A",
      "attributes": {
        "category": "云区域",
        "jurisdiction": "示例境内区域",
        "availability_zone": "A1/A2"
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
    }
  ],
  "relationships": [
    {
      "id": "loc-app",
      "type": "located_at",
      "source": "app-oms",
      "target": "loc-cloud",
      "label": "应用位于云区域",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "loc-user",
      "type": "located_at",
      "source": "actor-customer",
      "target": "loc-east",
      "label": "示例用户访问地点",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
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
    }
  ],
  "view": {
    "id": "v-application-and-user-location-diagram",
    "artifact_id": "application-and-user-location-diagram",
    "title": "应用与用户位置图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "actor-customer",
      "app-web",
      "app-oms",
      "loc-cloud",
      "loc-east"
    ],
    "relationship_ids": [
      "customer-web",
      "loc-app",
      "loc-user"
    ],
    "analysis": "用户从哪里访问部署在哪里的应用？ 本视图限定订单履约改造范围，展示案例设定的应用与用户位置图。区分用户位置与应用位置；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-application-and-user-location-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-and-user-location-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-and-user-location-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
