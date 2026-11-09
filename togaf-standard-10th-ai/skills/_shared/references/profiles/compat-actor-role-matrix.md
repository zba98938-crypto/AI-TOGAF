# 参与者/角色矩阵（兼容默认）

`profile_id`: compat-actor-role-matrix；`artifact_id`: actor-role-matrix；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G248；G249；G198。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-actor-role-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：actor, role。关系类型：plays。

```json
{
  "entities": {
    "actor": [],
    "role": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 分配关系不是 RACI 责任类型
- 矩阵方向必须声明

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
      "id": "actor-picker",
      "type": "actor",
      "name": "仓储操作员",
      "attributes": {
        "category": "内部参与者",
        "owner": "仓储负责人",
        "boundary": "内部",
        "jurisdiction": "示例境内"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "role-picker",
      "type": "role",
      "name": "拣货角色",
      "attributes": {
        "responsibility": "按已确认订单备货",
        "authority": "查看必要的备货信息",
        "skill": "仓储拣配"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "actor-role",
      "type": "plays",
      "source": "actor-picker",
      "target": "role-picker",
      "label": "承担拣货角色",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "assigned"
      ]
    }
  ],
  "view": {
    "id": "v-actor-role-matrix",
    "artifact_id": "actor-role-matrix",
    "title": "参与者/角色矩阵 · 星河零售虚构案例",
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
      "actor-picker",
      "role-picker"
    ],
    "relationship_ids": [
      "actor-role"
    ],
    "analysis": "哪些参与者承担哪些角色？ 本视图限定订单履约改造范围，展示案例设定的参与者/角色矩阵。列出参与者与角色；实际项目需由相关责任方核实。",
    "legend": "参与者被分配到角色；单元代码：assigned；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-actor-role-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-actor-role-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-actor-role-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
