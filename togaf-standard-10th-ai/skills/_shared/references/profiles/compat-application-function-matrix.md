# 应用/功能矩阵（兼容默认）

`profile_id`: compat-application-function-matrix；`artifact_id`: application-function-matrix；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G248；G233。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-application-function-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, function。关系类型：supports_function。

```json
{
  "entities": {
    "application": [],
    "function": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 支撑关系不自动等于唯一实现
- 不能用流程名称替换功能而不说明

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
      "id": "app-function",
      "type": "supports_function",
      "source": "app-oms",
      "target": "fn-order",
      "label": "支撑订单处理",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "supports"
      ]
    }
  ],
  "view": {
    "id": "v-application-function-matrix",
    "artifact_id": "application-function-matrix",
    "title": "应用/功能矩阵 · 星河零售虚构案例",
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
      "fn-order"
    ],
    "relationship_ids": [
      "app-function"
    ],
    "analysis": "哪些应用支撑哪些业务功能？ 本视图限定订单履约改造范围，展示案例设定的应用/功能矩阵。统一功能边界；实际项目需由相关责任方核实。",
    "legend": "应用为业务功能提供支撑；单元代码：supports；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-application-function-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-function-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-function-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
