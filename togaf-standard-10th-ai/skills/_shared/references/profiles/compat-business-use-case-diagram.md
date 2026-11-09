# 业务用例图（兼容默认）

`profile_id`: compat-business-use-case-diagram；`artifact_id`: business-use-case-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G176；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-business-use-case-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：actor, business_use_case。关系类型：participates。

```json
{
  "entities": {
    "actor": [
      "boundary"
    ],
    "business_use_case": [
      "goal",
      "boundary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 用例不是内部功能分解
- 示意关系不宣称符合完整 UML 语义

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
      "id": "actor-customer",
      "type": "actor",
      "name": "客户参与者",
      "attributes": {
        "category": "外部主体",
        "owner": "客户服务负责人",
        "boundary": "外部",
        "jurisdiction": "示例境内"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-usecase",
      "type": "business_use_case",
      "name": "客户获得商品",
      "attributes": {
        "goal": "完成购买和交付",
        "boundary": "零售业务"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "business-participates",
      "type": "participates",
      "source": "actor-customer",
      "target": "business-usecase",
      "label": "客户获得商品",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-use-case-diagram",
    "artifact_id": "business-use-case-diagram",
    "title": "业务用例图 · 星河零售虚构案例",
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
      "actor-customer",
      "business-usecase"
    ],
    "relationship_ids": [
      "business-participates"
    ],
    "analysis": "外部参与者通过业务获得什么可观察结果？ 本视图限定订单履约改造范围，展示案例设定的业务用例图。定义业务系统边界；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-use-case-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-use-case-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-use-case-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
