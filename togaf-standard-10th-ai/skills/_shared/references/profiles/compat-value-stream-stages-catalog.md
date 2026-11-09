# 价值流阶段目录（兼容默认）

`profile_id`: compat-value-stream-stages-catalog；`artifact_id`: value-stream-stages-catalog；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G248；G178；G233。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-value-stream-stages-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：value_stage。关系类型：precedes。

```json
{
  "entities": {
    "value_stage": [
      "entry",
      "exit",
      "value_item",
      "stakeholder",
      "ordinal",
      "description"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 阶段不等于详细作业步骤
- 横向顺序与能力层级分别记录

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
      "id": "stage-order",
      "type": "value_stage",
      "name": "确认购买",
      "attributes": {
        "entry": "客户已选择商品",
        "exit": "订单和可售库存已确认",
        "value_item": "可靠购买承诺",
        "stakeholder": "客户",
        "ordinal": 1,
        "description": "按进入退出条件交付该阶段增量价值"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stage-deliver",
      "type": "value_stage",
      "name": "收到商品",
      "attributes": {
        "entry": "订单已确认",
        "exit": "客户确认送达",
        "value_item": "商品可使用",
        "stakeholder": "客户",
        "ordinal": 2,
        "description": "按进入退出条件交付该阶段增量价值"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "stage-ordering",
      "type": "precedes",
      "source": "stage-order",
      "target": "stage-deliver",
      "label": "确认后交付",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-value-stream-stages-catalog",
    "artifact_id": "value-stream-stages-catalog",
    "title": "价值流阶段目录 · 星河零售虚构案例",
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
      "stage-order",
      "stage-deliver"
    ],
    "relationship_ids": [
      "stage-ordering"
    ],
    "analysis": "每个阶段何时开始和结束，增加什么价值？ 本视图限定订单履约改造范围，展示案例设定的价值流阶段目录。按利益相关者价值增量分阶段；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-value-stream-stages-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-stream-stages-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-stream-stages-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
