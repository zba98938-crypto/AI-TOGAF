# 数据实体/业务功能矩阵（兼容默认）

`profile_id`: compat-data-entity-business-function-matrix；`artifact_id`: data-entity-business-function-matrix；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G234。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-data-entity-business-function-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_entity, function。关系类型：used_in_function。

```json
{
  "entities": {
    "data_entity": [],
    "function": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- CRUD 动作主体是列功能
- 不要求每个实体必须存在 D 操作

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
      "id": "data-order",
      "type": "data_entity",
      "name": "订单",
      "attributes": {
        "definition": "购买商品和履约承诺的数据记录",
        "owner": "销售负责人",
        "classification": "内部交易数据",
        "retention": "依据经确认的业务政策",
        "authority": "订单应用",
        "latency": "近实时",
        "delivery_mode": "业务事件",
        "purpose": "受控订单履约或已声明分析"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "data-function",
      "type": "used_in_function",
      "source": "data-order",
      "target": "fn-order",
      "label": "订单处理创建读取和更新订单",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "C",
        "R",
        "U"
      ]
    }
  ],
  "view": {
    "id": "v-data-entity-business-function-matrix",
    "artifact_id": "data-entity-business-function-matrix",
    "title": "数据实体/业务功能矩阵 · 星河零售虚构案例",
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
      "data-order",
      "fn-order"
    ],
    "relationship_ids": [
      "data-function"
    ],
    "analysis": "哪些功能创建、读取、更新或删除哪些数据？ 本视图限定订单履约改造范围，展示案例设定的数据实体/业务功能矩阵。确定业务数据实体与功能粒度；实际项目需由相关责任方核实。",
    "legend": "列功能对行数据实体执行的 CRUD；关系仍从行实体到列功能；单元代码：C,R,U,D；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-data-entity-business-function-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-entity-business-function-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-entity-business-function-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
