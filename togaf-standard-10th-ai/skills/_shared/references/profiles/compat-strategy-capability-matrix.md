# 战略/能力矩阵（兼容默认）

`profile_id`: compat-strategy-capability-matrix；`artifact_id`: strategy-capability-matrix；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G248；G211；G233。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-strategy-capability-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：goal, objective, capability。关系类型：requires_capability。

```json
{
  "entities": {
    "goal": [],
    "objective": [],
    "capability": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 相关性不自动代表因果或贡献权重
- 权重需业务确认

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
      "id": "cap-order",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "维护订单承诺及履行状态",
        "owner": "销售负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
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
    }
  ],
  "relationships": [
    {
      "id": "strategy-cap",
      "type": "requires_capability",
      "source": "goal",
      "target": "cap-order",
      "label": "体验目标需订单管理",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "supports"
      ]
    }
  ],
  "view": {
    "id": "v-strategy-capability-matrix",
    "artifact_id": "strategy-capability-matrix",
    "title": "战略/能力矩阵 · 星河零售虚构案例",
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
      "cap-order"
    ],
    "relationship_ids": [
      "strategy-cap"
    ],
    "analysis": "哪些能力支撑哪些战略目标？ 本视图限定订单履约改造范围，展示案例设定的战略/能力矩阵。把战略细化为可判定目标；实际项目需由相关责任方核实。",
    "legend": "战略目标需要列能力支撑；单元代码：supports；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-strategy-capability-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-strategy-capability-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-strategy-capability-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
