# 能力/组织矩阵（兼容默认）

`profile_id`: compat-capability-organization-matrix；`artifact_id`: capability-organization-matrix；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G248；G206；G211。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-capability-organization-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, organization。关系类型：owned_by。

```json
{
  "entities": {
    "capability": [],
    "organization": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 能力不因组织调整而重命名
- 多个贡献者不自动等于多个最终责任人

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
      "id": "cap-stock",
      "type": "capability",
      "name": "库存管理",
      "attributes": {
        "definition": "掌握库存并分配可售数量",
        "owner": "仓储负责人",
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
      "id": "cap-org",
      "type": "owned_by",
      "source": "cap-stock",
      "target": "org-warehouse",
      "label": "负责库存能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "owner"
      ]
    }
  ],
  "view": {
    "id": "v-capability-organization-matrix",
    "artifact_id": "capability-organization-matrix",
    "title": "能力/组织矩阵 · 星河零售虚构案例",
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
      "cap-stock",
      "org-warehouse"
    ],
    "relationship_ids": [
      "cap-org"
    ],
    "analysis": "哪些组织拥有或贡献哪些能力？ 本视图限定订单履约改造范围，展示案例设定的能力/组织矩阵。统一能力分解层级；实际项目需由相关责任方核实。",
    "legend": "区分能力责任方与参与贡献方；单元代码：owner,contributor；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-capability-organization-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-capability-organization-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-capability-organization-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
