# 处理图（兼容默认）

`profile_id`: compat-processing-diagram；`artifact_id`: processing-diagram；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G248；G21I。

## 构图与定义状态

表示族：`sequence`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-processing-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, process, data_entity。关系类型：processing_step, accesses。

```json
{
  "entities": {
    "application": [],
    "process": [],
    "data_entity": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 序列只代表所选场景
- 不能从排列推断全部运行路径

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
    }
  ],
  "relationships": [
    {
      "id": "seq1",
      "type": "processing_step",
      "source": "app-web",
      "target": "app-oms",
      "label": "提交订单",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "attributes": {
        "order": 1
      }
    },
    {
      "id": "seq2",
      "type": "processing_step",
      "source": "app-oms",
      "target": "app-stock",
      "label": "请求库存确认",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "attributes": {
        "order": 2
      }
    },
    {
      "id": "seq3",
      "type": "processing_step",
      "source": "app-stock",
      "target": "app-oms",
      "label": "返回库存结果",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "attributes": {
        "order": 3
      }
    }
  ],
  "view": {
    "id": "v-processing-diagram",
    "artifact_id": "processing-diagram",
    "title": "处理图 · 星河零售虚构案例",
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
      "app-web",
      "app-oms",
      "app-stock"
    ],
    "relationship_ids": [
      "seq1",
      "seq2",
      "seq3"
    ],
    "analysis": "处理如何在应用组件间分配并完成一次交互？ 本视图限定订单履约改造范围，展示案例设定的处理图。选择典型处理场景；实际项目需由相关责任方核实。",
    "legend": "消息按 order 从上到下；实线箭头表示所选场景调用，不表达所有运行路径。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-processing-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-processing-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-processing-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
