# 组织/参与者目录（兼容默认）

`profile_id`: compat-organization-actor-catalog；`artifact_id`: organization-actor-catalog；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G248；G206；G249。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-organization-actor-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：organization, actor。关系类型：member_of。

```json
{
  "entities": {
    "organization": [
      "category",
      "owner",
      "boundary"
    ],
    "actor": [
      "category",
      "owner",
      "boundary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 角色不等于具体人员
- 供应商也可能位于业务范围内

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
      "id": "org-enterprise",
      "type": "organization",
      "name": "星河零售",
      "attributes": {
        "category": "企业",
        "owner": "业务发起方",
        "boundary": "内部"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
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
    },
    {
      "id": "org-partner",
      "type": "organization",
      "name": "示例物流伙伴",
      "attributes": {
        "category": "合作伙伴",
        "owner": "伙伴接口负责人",
        "boundary": "外部"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
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
    }
  ],
  "relationships": [
    {
      "id": "actor-member",
      "type": "member_of",
      "source": "actor-picker",
      "target": "org-warehouse",
      "label": "操作员属于仓储团队",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-organization-actor-catalog",
    "artifact_id": "organization-actor-catalog",
    "title": "组织/参与者目录 · 星河零售虚构案例",
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
      "org-enterprise",
      "org-sales",
      "org-warehouse",
      "org-partner",
      "actor-customer",
      "actor-picker"
    ],
    "relationship_ids": [
      "actor-member"
    ],
    "analysis": "谁参与业务，哪些组织对结果负责？ 本视图限定订单履约改造范围，展示案例设定的组织/参与者目录。标识内外部组织及具体参与者类型；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-organization-actor-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-organization-actor-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-organization-actor-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
