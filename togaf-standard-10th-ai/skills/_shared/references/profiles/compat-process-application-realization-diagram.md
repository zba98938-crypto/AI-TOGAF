# 流程/应用实现图（兼容默认）

`profile_id`: compat-process-application-realization-diagram；`artifact_id`: process-application-realization-diagram；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G233；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-process-application-realization-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：process, activity, application。关系类型：has_activity, automated_by。

```json
{
  "entities": {
    "process": [
      "owner",
      "automation"
    ],
    "activity": [
      "owner",
      "automation"
    ],
    "application": [
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 支撑不等于完全自动化
- 应用关系不能代替业务执行顺序

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
      "id": "process",
      "type": "process",
      "name": "订单履行流程",
      "attributes": {
        "definition": "从订单提交到送达的处理",
        "owner": "履约负责人",
        "lifecycle": "持续运营",
        "entry": "订单已提交",
        "exit": "交付确认",
        "automation": "部分自动"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "activity-confirm",
      "type": "activity",
      "name": "确认可售库存",
      "attributes": {
        "owner": "销售负责人",
        "entry": "收到订单",
        "exit": "库存校验完成",
        "automation": "应用辅助"
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
      "id": "process-activity",
      "type": "has_activity",
      "source": "process",
      "target": "activity-confirm",
      "label": "包含确认步骤",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "activity-app",
      "type": "automated_by",
      "source": "activity-confirm",
      "target": "app-oms",
      "label": "应用辅助确认",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-process-application-realization-diagram",
    "artifact_id": "process-application-realization-diagram",
    "title": "流程/应用实现图 · 星河零售虚构案例",
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
      "process",
      "activity-confirm",
      "app-oms"
    ],
    "relationship_ids": [
      "process-activity",
      "activity-app"
    ],
    "analysis": "流程步骤由哪些应用能力实现或辅助？ 本视图限定订单履约改造范围，展示案例设定的流程/应用实现图。保持业务步骤与应用边界；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-process-application-realization-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-process-application-realization-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-process-application-realization-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
