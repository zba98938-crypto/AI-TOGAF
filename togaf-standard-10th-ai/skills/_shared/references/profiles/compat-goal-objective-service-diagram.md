# 目标/目的/服务图（兼容默认）

`profile_id`: compat-goal-objective-service-diagram；`artifact_id`: goal-objective-service-diagram；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G248；G176；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-goal-objective-service-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：goal, objective, business_service。关系类型：refines, served_by。

```json
{
  "entities": {
    "goal": [
      "statement",
      "metric"
    ],
    "objective": [
      "statement",
      "metric"
    ],
    "business_service": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 服务实现不是目标达成证据
- 层间关系不是简单包含

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
      "id": "service-order",
      "type": "business_service",
      "name": "订单确认服务",
      "attributes": {
        "definition": "向客户提供可履行的订单确认",
        "owner": "销售负责人",
        "service_level": "示例服务承诺由业务方确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "goal",
      "type": "goal",
      "name": "改善客户履约体验",
      "attributes": {
        "statement": "客户获得可靠及时的交付",
        "owner": "业务发起方",
        "metric": "按承诺送达比例",
        "target": "提升",
        "deadline": "下一季度"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "objective",
      "type": "objective",
      "name": "缩短订单确认时间",
      "attributes": {
        "statement": "示例目标：确认时间中位数由 20 分钟降低至 5 分钟",
        "owner": "履约负责人",
        "metric": "确认时长中位数",
        "target": 5,
        "unit": "分钟",
        "baseline": 20,
        "deadline": "试运行结束"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "goal-objective",
      "type": "refines",
      "source": "goal",
      "target": "objective",
      "label": "细化为确认时长目的",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "objective-service",
      "type": "served_by",
      "source": "objective",
      "target": "service-order",
      "label": "确认服务支撑时长目标",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-goal-objective-service-diagram",
    "artifact_id": "goal-objective-service-diagram",
    "title": "目标/目的/服务图 · 星河零售虚构案例",
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
      "goal",
      "objective",
      "service-order"
    ],
    "relationship_ids": [
      "goal-objective",
      "objective-service"
    ],
    "analysis": "服务如何支撑目的和更高层目标？ 本视图限定订单履约改造范围，展示案例设定的目标/目的/服务图。区分长期目标和可度量目的；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-goal-objective-service-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-goal-objective-service-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-goal-objective-service-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
