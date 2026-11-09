# 产品生命周期图（兼容默认）

`profile_id`: compat-product-lifecycle-diagram；`artifact_id`: product-lifecycle-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G248；G176。

## 构图与定义状态

表示族：`state`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-product-lifecycle-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：product_state。关系类型：transitions_to。

```json
{
  "entities": {
    "product_state": [
      "entry",
      "exit",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 产品生命周期不是项目阶段
- 状态转换不表示价值流阶段

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
      "id": "product-draft",
      "type": "product_state",
      "name": "商品待发布",
      "attributes": {
        "entry": "商品定义完成",
        "exit": "获准发布",
        "owner": "商品负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "product-sale",
      "type": "product_state",
      "name": "商品在售",
      "attributes": {
        "entry": "发布批准",
        "exit": "决定下架",
        "owner": "商品负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "product-off",
      "type": "product_state",
      "name": "商品下架",
      "attributes": {
        "entry": "下架生效",
        "exit": "退役处理完成",
        "owner": "商品负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "product-publish",
      "type": "transitions_to",
      "source": "product-draft",
      "target": "product-sale",
      "label": "批准发布",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "product-retire",
      "type": "transitions_to",
      "source": "product-sale",
      "target": "product-off",
      "label": "下架生效",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-product-lifecycle-diagram",
    "artifact_id": "product-lifecycle-diagram",
    "title": "产品生命周期图 · 星河零售虚构案例",
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
      "product-draft",
      "product-sale",
      "product-off"
    ],
    "relationship_ids": [
      "product-publish",
      "product-retire"
    ],
    "analysis": "产品经历哪些状态，什么条件允许转换？ 本视图限定订单履约改造范围，展示案例设定的产品生命周期图。定义生命周期对象及状态；实际项目需由相关责任方核实。",
    "legend": "状态节点；箭头表示满足标签条件后的状态转换。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-product-lifecycle-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-product-lifecycle-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-product-lifecycle-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
