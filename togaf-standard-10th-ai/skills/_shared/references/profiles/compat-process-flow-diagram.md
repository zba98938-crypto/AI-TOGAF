# 流程图（兼容默认）

`profile_id`: compat-process-flow-diagram；`artifact_id`: process-flow-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G176；G233；G152。

## 构图与定义状态

表示族：`swimlane`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-process-flow-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：process, activity, decision, event, role。关系类型：triggers, flows_to, branches, assigned_to。

```json
{
  "entities": {
    "process": [
      "owner",
      "entry",
      "exit"
    ],
    "activity": [
      "owner",
      "entry",
      "exit"
    ],
    "decision": [
      "owner",
      "entry",
      "exit"
    ],
    "event": [
      "owner"
    ],
    "role": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 标明简化流程表示法，非严格 BPMN
- 箭头不能混用控制流和信息流

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
      "id": "event-submit",
      "type": "event",
      "name": "订单已提交",
      "attributes": {
        "definition": "客户完成订单提交",
        "owner": "销售负责人",
        "lifecycle": "业务事件",
        "trigger": "客户提交",
        "outcome": "启动确认"
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
      "id": "activity-pack",
      "type": "activity",
      "name": "拣货打包",
      "attributes": {
        "owner": "仓储负责人",
        "entry": "库存已分配",
        "exit": "包裹待发运",
        "automation": "人工与应用辅助"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "decision-stock",
      "type": "decision",
      "name": "库存是否充足",
      "attributes": {
        "owner": "履约负责人",
        "entry": "库存核对完成",
        "exit": "选择处理路径"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "event-activity",
      "type": "triggers",
      "source": "event-submit",
      "target": "activity-confirm",
      "label": "开始库存确认",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "activity-decision",
      "type": "flows_to",
      "source": "activity-confirm",
      "target": "decision-stock",
      "label": "校验后判断",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "decision-pack",
      "type": "branches",
      "source": "decision-stock",
      "target": "activity-pack",
      "label": "库存充足",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "decision-confirm",
      "type": "branches",
      "source": "decision-stock",
      "target": "activity-confirm",
      "label": "不充足：等待后复核",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-process-flow-diagram",
    "artifact_id": "process-flow-diagram",
    "title": "流程图 · 星河零售虚构案例",
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
      "event-submit",
      "activity-confirm",
      "decision-stock",
      "activity-pack"
    ],
    "relationship_ids": [
      "event-activity",
      "activity-decision",
      "decision-pack",
      "decision-confirm"
    ],
    "analysis": "业务活动如何在参与者之间流转并处理例外？ 本视图限定订单履约改造范围，展示案例设定的流程图。从触发到结果安排活动；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-process-flow-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-process-flow-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-process-flow-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
