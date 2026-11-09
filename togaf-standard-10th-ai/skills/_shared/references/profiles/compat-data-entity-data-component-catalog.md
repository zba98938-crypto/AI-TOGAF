# 数据实体/数据组件目录（兼容默认）

`profile_id`: compat-data-entity-data-component-catalog；`artifact_id`: data-entity-data-component-catalog；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G234；G21B。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-data-entity-data-component-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_entity, data_component。关系类型：stored_in。

```json
{
  "entities": {
    "data_entity": [
      "definition",
      "owner",
      "classification",
      "retention"
    ],
    "data_component": [
      "definition",
      "owner",
      "classification",
      "retention"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 业务实体不是数据表
- 信息概念与数据组件保持独立身份

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
      "id": "data-customer",
      "type": "data_entity",
      "name": "客户",
      "attributes": {
        "definition": "可识别的购买主体数据",
        "owner": "客户数据负责人",
        "classification": "受限联系信息",
        "retention": "示例：合同完成后按已确认政策处置",
        "authority": "客户主数据服务",
        "latency": "待确认",
        "delivery_mode": "受控查询",
        "purpose": "受控订单履约或已声明分析"
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
    },
    {
      "id": "component-order",
      "type": "data_component",
      "name": "订单主存储",
      "attributes": {
        "definition": "订单逻辑存储组件",
        "owner": "应用负责人",
        "classification": "内部交易数据",
        "retention": "继承订单政策",
        "authority": "订单应用",
        "latency": "事务提交",
        "delivery_mode": "受控查询",
        "purpose": "受控订单履约或已声明分析"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "component-report",
      "type": "data_component",
      "name": "订单分析副本",
      "attributes": {
        "definition": "用于经营分析的只读副本",
        "owner": "数据团队",
        "classification": "脱敏内部数据",
        "retention": "按分析用途保留",
        "authority": "非权威副本",
        "latency": "示例每日",
        "delivery_mode": "批量复制",
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
      "id": "store-order",
      "type": "stored_in",
      "source": "data-order",
      "target": "component-order",
      "label": "订单由主存储管理",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-data-entity-data-component-catalog",
    "artifact_id": "data-entity-data-component-catalog",
    "title": "数据实体/数据组件目录 · 星河零售虚构案例",
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
      "data-customer",
      "data-order",
      "component-order",
      "component-report"
    ],
    "relationship_ids": [
      "store-order"
    ],
    "analysis": "哪些业务数据由哪些逻辑或物理组件管理？ 本视图限定订单履约改造范围，展示案例设定的数据实体/数据组件目录。先界定业务数据实体；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-data-entity-data-component-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-entity-data-component-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-entity-data-component-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
