# 数据迁移图（兼容默认）

`profile_id`: compat-data-migration-diagram；`artifact_id`: data-migration-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G21B；G234；G186。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-data-migration-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_component, migration_step。关系类型：migration_flow。

```json
{
  "entities": {
    "data_component": [],
    "migration_step": [
      "transformation",
      "reconciliation",
      "rollback"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- ETL 箭头不代表迁移成功
- 必须给出完整性核对和责任

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
    },
    {
      "id": "migration-clean",
      "type": "migration_step",
      "name": "清洗与客户标识映射",
      "attributes": {
        "transformation": "去重并生成客户标识映射",
        "reconciliation": "核对记录数和关键金额",
        "rollback": "保留源数据并回退映射版本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "migration-load",
      "type": "migration_step",
      "name": "加载与业务核对",
      "attributes": {
        "transformation": "转换为目标逻辑结构",
        "reconciliation": "核对记录数、金额及抽样订单",
        "rollback": "切换前撤销目标加载"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "migration-1",
      "type": "migration_flow",
      "source": "component-order",
      "target": "migration-clean",
      "label": "抽取与映射",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "migration-2",
      "type": "migration_flow",
      "source": "migration-clean",
      "target": "migration-load",
      "label": "清洗后加载",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "migration-3",
      "type": "migration_flow",
      "source": "migration-load",
      "target": "component-report",
      "label": "核对后提供分析副本",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-data-migration-diagram",
    "artifact_id": "data-migration-diagram",
    "title": "数据迁移图 · 星河零售虚构案例",
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
      "component-order",
      "migration-clean",
      "migration-load",
      "component-report"
    ],
    "relationship_ids": [
      "migration-1",
      "migration-2",
      "migration-3"
    ],
    "analysis": "数据如何完成抽取、转换、加载及切换？ 本视图限定订单履约改造范围，展示案例设定的数据迁移图。明确源目标和迁移范围；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-data-migration-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-migration-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-migration-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
