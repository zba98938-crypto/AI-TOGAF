# 应用通信图（兼容默认）

`profile_id`: compat-application-communication-diagram；`artifact_id`: application-communication-diagram；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G21I；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-application-communication-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, interface。关系类型：communicates_with, exposes, consumes。

```json
{
  "entities": {
    "application": [
      "version"
    ],
    "interface": [
      "protocol",
      "payload",
      "version"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 此图不是时间序列
- 通信方向不代表数据权威来源

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
      "id": "app-stock",
      "type": "application",
      "name": "库存应用",
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
      "id": "interface",
      "type": "interface",
      "name": "库存校验接口",
      "attributes": {
        "producer": "库存应用",
        "consumer": "订单应用",
        "protocol": "HTTPS",
        "payload": "商品和数量",
        "version": "v1",
        "owner": "库存应用负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "expose-stock",
      "type": "exposes",
      "source": "app-stock",
      "target": "interface",
      "label": "提供库存校验",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "consume-stock",
      "type": "consumes",
      "source": "app-oms",
      "target": "interface",
      "label": "消费库存校验",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "app-interaction",
      "type": "communicates_with",
      "source": "app-oms",
      "target": "app-stock",
      "label": "同步库存校验",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "sync"
      ],
      "attributes": {
        "interface_id": "interface",
        "payload": "商品和数量"
      }
    }
  ],
  "view": {
    "id": "v-application-communication-diagram",
    "artifact_id": "application-communication-diagram",
    "title": "应用通信图 · 星河零售虚构案例",
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
      "app-oms",
      "app-stock",
      "interface"
    ],
    "relationship_ids": [
      "expose-stock",
      "consume-stock",
      "app-interaction"
    ],
    "analysis": "应用通过哪些接口、模式和数据交换进行通信？ 本视图限定订单履约改造范围，展示案例设定的应用通信图。先画应用边界与接口；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-application-communication-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-communication-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-communication-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
