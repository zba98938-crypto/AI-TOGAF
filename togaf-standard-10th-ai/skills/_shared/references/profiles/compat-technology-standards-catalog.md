# 技术标准目录（兼容默认）

`profile_id`: compat-technology-standards-catalog；`artifact_id`: technology-standards-catalog；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G184；G248；G152。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-technology-standards-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：standard。关系类型：governs。

```json
{
  "entities": {
    "standard": [
      "category",
      "version",
      "disposition",
      "rationale",
      "exception_process"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 标准状态不同于部署状态
- 标准不只厂商产品清单

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
      "id": "standard",
      "type": "standard",
      "name": "受支持运行时标准",
      "attributes": {
        "category": "技术运行时",
        "version": "项目草案 v1",
        "disposition": "候选推荐",
        "rationale": "降低运行及支持风险",
        "exception_process": "由平台和架构负责人评审例外"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-technology-standards-catalog",
    "artifact_id": "technology-standards-catalog",
    "title": "技术标准目录 · 星河零售虚构案例",
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
      "standard"
    ],
    "relationship_ids": [],
    "analysis": "哪些技术标准被允许、推荐、限制或退役？ 本视图限定订单履约改造范围，展示案例设定的技术标准目录。定义标准适用范围；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-technology-standards-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-technology-standards-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-technology-standards-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
