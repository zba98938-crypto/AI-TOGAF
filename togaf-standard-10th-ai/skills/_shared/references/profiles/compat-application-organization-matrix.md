# 应用/组织矩阵（兼容默认）

`profile_id`: compat-application-organization-matrix；`artifact_id`: application-organization-matrix；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G206；G248。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-application-organization-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, organization。关系类型：used_by。

```json
{
  "entities": {
    "application": [],
    "organization": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不能将应用负责人视为全部用户
- 代码表示不同关系类别

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
      "id": "org-sales",
      "type": "organization",
      "name": "销售团队",
      "attributes": {
        "category": "业务单元",
        "owner": "销售负责人",
        "boundary": "内部"
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
      "id": "app-org",
      "type": "used_by",
      "source": "app-oms",
      "target": "org-sales",
      "label": "销售使用订单应用",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "uses"
      ]
    }
  ],
  "view": {
    "id": "v-application-organization-matrix",
    "artifact_id": "application-organization-matrix",
    "title": "应用/组织矩阵 · 星河零售虚构案例",
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
      "org-sales"
    ],
    "relationship_ids": [
      "app-org"
    ],
    "analysis": "哪些组织使用或负责哪些应用？ 本视图限定订单履约改造范围，展示案例设定的应用/组织矩阵。确定组织边界；实际项目需由相关责任方核实。",
    "legend": "按单元代码区分组织使用、拥有、运营应用；单元代码：uses,owns,operates；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-application-organization-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-organization-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-organization-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
