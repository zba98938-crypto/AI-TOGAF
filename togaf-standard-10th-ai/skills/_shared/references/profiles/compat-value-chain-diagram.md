# 价值链图（兼容默认）

`profile_id`: compat-value-chain-diagram；`artifact_id`: value-chain-diagram；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G248；G178；G18A。

## 构图与定义状态

表示族：`value-chain`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-value-chain-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：value_chain_activity。关系类型：supports_activity。

```json
{
  "entities": {
    "value_chain_activity": [
      "category",
      "value_contribution"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 价值链不是面向触发方的价值流
- 分类不自动表示时间顺序

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
      "id": "chain-sales",
      "type": "value_chain_activity",
      "name": "销售与交付",
      "attributes": {
        "category": "主要活动",
        "value_contribution": "向客户交付商品"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "chain-tech",
      "type": "value_chain_activity",
      "name": "技术支持",
      "attributes": {
        "category": "支持活动",
        "value_contribution": "为销售和履约提供信息系统"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "chain-support",
      "type": "supports_activity",
      "source": "chain-tech",
      "target": "chain-sales",
      "label": "技术支持销售交付",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-value-chain-diagram",
    "artifact_id": "value-chain-diagram",
    "title": "价值链图 · 星河零售虚构案例",
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
      "chain-tech",
      "chain-sales"
    ],
    "relationship_ids": [
      "chain-support"
    ],
    "analysis": "企业有哪些主要及支持活动共同形成价值？ 本视图限定订单履约改造范围，展示案例设定的价值链图。声明采用的价值链分析框架；实际项目需由相关责任方核实。",
    "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-value-chain-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-chain-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-chain-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
