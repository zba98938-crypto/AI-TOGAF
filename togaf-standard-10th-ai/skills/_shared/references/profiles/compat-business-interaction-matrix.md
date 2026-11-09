# 业务交互矩阵（兼容默认）

`profile_id`: compat-business-interaction-matrix；`artifact_id`: business-interaction-matrix；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G206；G248。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-business-interaction-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：organization, organization。关系类型：business_interaction。

```json
{
  "entities": {
    "organization": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对角线需按业务边界解释
- 方向不可由相邻位置推断

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
      "id": "org-sales",
      "type": "organization",
      "name": "销售团队",
      "attributes": {
        "category": "业务单元",
        "owner": "销售负责人",
        "boundary": "内部"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "org-warehouse",
      "type": "organization",
      "name": "仓储团队",
      "attributes": {
        "category": "业务单元",
        "owner": "仓储负责人",
        "boundary": "内部"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "business-interaction",
      "type": "business_interaction",
      "source": "org-sales",
      "target": "org-warehouse",
      "label": "提供已确认订单",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "exchange"
      ]
    }
  ],
  "view": {
    "id": "v-business-interaction-matrix",
    "artifact_id": "business-interaction-matrix",
    "title": "业务交互矩阵 · 星河零售虚构案例",
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
      "org-sales",
      "org-warehouse"
    ],
    "relationship_ids": [
      "business-interaction"
    ],
    "analysis": "哪些组织向哪些组织提供什么业务交互？ 本视图限定订单履约改造范围，展示案例设定的业务交互矩阵。统一交互边界；实际项目需由相关责任方核实。",
    "legend": "行组织向列组织提供的产品或服务；单元代码：exchange；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-interaction-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-interaction-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-interaction-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
