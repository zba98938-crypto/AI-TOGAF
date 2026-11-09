# 驱动因素/目标/目的目录（兼容默认）

`profile_id`: compat-driver-goal-objective-catalog；`artifact_id`: driver-goal-objective-catalog；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G248；G176；G186。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-driver-goal-objective-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：driver, goal, objective。关系类型：motivates, refines。

```json
{
  "entities": {
    "driver": [
      "statement",
      "owner",
      "metric",
      "target",
      "deadline"
    ],
    "goal": [
      "statement",
      "owner",
      "metric",
      "target",
      "deadline"
    ],
    "objective": [
      "statement",
      "owner",
      "metric",
      "target",
      "deadline"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不能将手段当成业务目标
- 无期限数字不自动构成 SMART 目的

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
      "id": "driver",
      "type": "driver",
      "name": "跨渠道订单增长",
      "attributes": {
        "statement": "示例渠道订单增长导致人工协调压力",
        "owner": "业务发起方",
        "metric": "订单量",
        "target": "示例 20% 增长情景",
        "deadline": "下一季度"
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
      "id": "driver-goal",
      "type": "motivates",
      "source": "driver",
      "target": "goal",
      "label": "增长推动体验目标",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
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
    }
  ],
  "view": {
    "id": "v-driver-goal-objective-catalog",
    "artifact_id": "driver-goal-objective-catalog",
    "title": "驱动因素/目标/目的目录 · 星河零售虚构案例",
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
      "driver",
      "goal",
      "objective"
    ],
    "relationship_ids": [
      "driver-goal",
      "goal-objective"
    ],
    "analysis": "什么驱动因素促成哪些长期目标与可衡量目的？ 本视图限定订单履约改造范围，展示案例设定的驱动因素/目标/目的目录。区分外部驱动与期望结果；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-driver-goal-objective-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-driver-goal-objective-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-driver-goal-objective-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
