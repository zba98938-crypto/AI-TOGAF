# 应用/数据矩阵（兼容默认）

`profile_id`: compat-application-data-matrix；`artifact_id`: application-data-matrix；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G21B；G234。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-application-data-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, data_entity。关系类型：accesses。

```json
{
  "entities": {
    "application": [],
    "data_entity": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 复制数据不自动成为权威来源
- owner 与 CRUD 分开解释

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
    }
  ],
  "relationships": [
    {
      "id": "app-data",
      "type": "accesses",
      "source": "app-oms",
      "target": "data-order",
      "label": "订单应用管理订单",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "C",
        "R",
        "U",
        "owner"
      ]
    },
    {
      "id": "app-customer",
      "type": "accesses",
      "source": "app-oms",
      "target": "data-customer",
      "label": "读取必要客户信息",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "R"
      ]
    }
  ],
  "view": {
    "id": "v-application-data-matrix",
    "artifact_id": "application-data-matrix",
    "title": "应用/数据矩阵 · 星河零售虚构案例",
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
      "data-order",
      "data-customer"
    ],
    "relationship_ids": [
      "app-data",
      "app-customer"
    ],
    "analysis": "应用对数据实体承担什么操作及管理职责？ 本视图限定订单履约改造范围，展示案例设定的应用/数据矩阵。确认应用和数据粒度；实际项目需由相关责任方核实。",
    "legend": "行应用对列数据执行操作或承担管理职责；单元代码：C,R,U,D,owner；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-application-data-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-data-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-data-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
