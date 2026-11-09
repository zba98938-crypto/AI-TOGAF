# 项目语境图（兼容默认）

`profile_id`: compat-project-context-diagram；`artifact_id`: project-context-diagram；主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G248；G188；G186。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-project-context-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：project, actor, application, organization。关系类型：in_scope, external_dependency。

```json
{
  "entities": {
    "project": [],
    "actor": [
      "boundary",
      "owner"
    ],
    "application": [
      "boundary",
      "owner"
    ],
    "organization": [
      "boundary",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 外部依赖不自动纳入项目承诺
- 项目语境不是目标部署图

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
      "id": "org-partner",
      "type": "organization",
      "name": "示例物流伙伴",
      "attributes": {
        "category": "合作伙伴",
        "owner": "伙伴接口负责人",
        "boundary": "外部"
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
      "id": "project",
      "type": "project",
      "name": "订单履约改造",
      "attributes": {
        "boundary": "订单确认与仓储交接",
        "owner": "业务发起方"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "project-app",
      "type": "in_scope",
      "source": "project",
      "target": "app-oms",
      "label": "项目改变订单应用",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "project-external",
      "type": "external_dependency",
      "source": "project",
      "target": "org-partner",
      "label": "物流接口外部依赖",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-project-context-diagram",
    "artifact_id": "project-context-diagram",
    "title": "项目语境图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "context",
      "evolution": "target"
    },
    "entity_ids": [
      "project",
      "app-oms",
      "org-partner"
    ],
    "relationship_ids": [
      "project-app",
      "project-external"
    ],
    "analysis": "项目边界内外涉及哪些主体、系统与依赖？ 本视图限定订单履约改造范围，展示案例设定的项目语境图。明确项目目标及范围；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-project-context-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-project-context-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-project-context-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
