# 功能分解图（兼容默认）

`profile_id`: compat-functional-decomposition-diagram；`artifact_id`: functional-decomposition-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G248；G233。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-functional-decomposition-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：function。关系类型：decomposes。

```json
{
  "entities": {
    "function": [
      "definition",
      "level"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 分解线不表示执行顺序
- 功能树不等于组织层级

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
      "id": "fn-order",
      "type": "function",
      "name": "订单处理",
      "attributes": {
        "definition": "记录、校验并确认订单",
        "owner": "销售负责人",
        "service_level": "由订单确认服务承诺约束",
        "level": 1
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "fn-validate",
      "type": "function",
      "name": "订单校验",
      "attributes": {
        "definition": "校验库存与客户输入",
        "owner": "销售负责人",
        "service_level": "继承确认服务承诺",
        "level": 2
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "fn-child",
      "type": "decomposes",
      "source": "fn-order",
      "target": "fn-validate",
      "label": "订单处理分解为校验职责",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-functional-decomposition-diagram",
    "artifact_id": "functional-decomposition-diagram",
    "title": "功能分解图 · 星河零售虚构案例",
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
      "fn-order",
      "fn-validate"
    ],
    "relationship_ids": [
      "fn-child"
    ],
    "analysis": "业务功能如何分解为一致边界的子功能？ 本视图限定订单履约改造范围，展示案例设定的功能分解图。确定功能分类依据；实际项目需由相关责任方核实。",
    "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-functional-decomposition-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-functional-decomposition-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-functional-decomposition-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
