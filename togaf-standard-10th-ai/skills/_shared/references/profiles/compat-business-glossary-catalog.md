# 业务术语表目录（兼容默认）

`profile_id`: compat-business-glossary-catalog；`artifact_id`: business-glossary-catalog；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G234；G21B。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-business-glossary-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：term。关系类型：defines, synonym_of。

```json
{
  "entities": {
    "term": [
      "definition",
      "owner",
      "synonyms"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 同名不自动合并
- 术语定义不等于数据库字段说明

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
      "id": "term-customer",
      "type": "term",
      "name": "客户",
      "attributes": {
        "definition": "向企业购买产品或服务的主体",
        "owner": "客户数据负责人",
        "synonyms": [
          "购买方"
        ]
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-glossary-catalog",
    "artifact_id": "business-glossary-catalog",
    "title": "业务术语表目录 · 星河零售虚构案例",
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
      "term-customer"
    ],
    "relationship_ids": [],
    "analysis": "关键业务术语是否有统一含义及负责方？ 本视图限定订单履约改造范围，展示案例设定的业务术语表目录。收集领域术语及语境；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-glossary-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-glossary-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-glossary-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
