# 信息地图（兼容默认）

`profile_id`: compat-information-map；`artifact_id`: information-map；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G234。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-information-map",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：information。关系类型：information_association。

```json
{
  "entities": {
    "information": [
      "definition",
      "category",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 信息地图不是 ER 表结构
- 主题分组不能臆造继承关系

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
      "id": "information-customer",
      "type": "information",
      "name": "客户信息",
      "attributes": {
        "definition": "描述交易客户的业务信息",
        "category": "客户主题",
        "owner": "客户数据负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-order",
      "type": "information",
      "name": "订单信息",
      "attributes": {
        "definition": "描述客户购买承诺的业务信息",
        "category": "交易主题",
        "owner": "销售负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "info-assoc",
      "type": "information_association",
      "source": "information-customer",
      "target": "information-order",
      "label": "客户关联购买订单",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-information-map",
    "artifact_id": "information-map",
    "title": "信息地图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "conceptual",
      "evolution": "target"
    },
    "entity_ids": [
      "information-customer",
      "information-order"
    ],
    "relationship_ids": [
      "info-assoc"
    ],
    "analysis": "哪些业务信息概念需要共同理解及管理？ 本视图限定订单履约改造范围，展示案例设定的信息地图。从业务语言构造信息主题；实际项目需由相关责任方核实。",
    "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-information-map"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-information-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-information-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
