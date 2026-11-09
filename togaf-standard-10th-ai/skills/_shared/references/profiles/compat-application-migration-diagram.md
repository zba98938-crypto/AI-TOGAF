# 应用迁移图（兼容默认）

`profile_id`: compat-application-migration-diagram；`artifact_id`: application-migration-diagram；主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G248；G186；G248。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-application-migration-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, work_package。关系类型：replaced_by, migrated_by。

```json
{
  "entities": {
    "application": [
      "lifecycle"
    ],
    "work_package": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 目标不是已实现
- 应用更名不必然代表新系统

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
      "id": "app-old",
      "type": "application",
      "name": "现有订单应用",
      "attributes": {
        "owner": "应用负责人",
        "lifecycle": "现状在用",
        "criticality": "业务关键",
        "cost": "待估算",
        "jurisdiction": "示例境内",
        "automation": "辅助业务确认",
        "capacity": 100,
        "responsibility": "支持客户购买与订单履约",
        "boundary": "订单履约系统边界",
        "version": "候选或现状示例版本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "concept_id": "order-management-system",
      "evolution": "baseline"
    },
    {
      "id": "wp-app",
      "type": "work_package",
      "name": "迁移订单应用",
      "attributes": {
        "duration_days": 20,
        "owner": "实施负责人",
        "output": "可试运行订单服务",
        "cost": "示例估算待确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "app-replaced",
      "type": "replaced_by",
      "source": "app-old",
      "target": "app-oms",
      "label": "受控切换替换",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "app-migrated",
      "type": "migrated_by",
      "source": "app-oms",
      "target": "wp-app",
      "label": "工作包交付迁移",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-application-migration-diagram",
    "artifact_id": "application-migration-diagram",
    "title": "应用迁移图 · 星河零售虚构案例",
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
      "app-old",
      "app-oms",
      "wp-app"
    ],
    "relationship_ids": [
      "app-replaced",
      "app-migrated"
    ],
    "analysis": "现有单节点订单系统向目标订单应用演进。先完成数据与契约，再受控双运行、核对并切换；这是候选迁移设计。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": true,
    "profile_id": "compat-application-migration-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-migration-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-migration-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
