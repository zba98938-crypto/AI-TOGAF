# 组织分解图（兼容默认）

`profile_id`: compat-organization-decomposition-diagram；`artifact_id`: organization-decomposition-diagram；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G248；G206。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-organization-decomposition-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：organization。关系类型：reports_to。

```json
{
  "entities": {
    "organization": [
      "boundary",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 合作关系不是汇报关系
- 组织地图比汇报树包含更多语义

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
    }
  ],
  "relationships": [
    {
      "id": "sales-reports",
      "type": "reports_to",
      "source": "org-sales",
      "target": "org-enterprise",
      "label": "正式汇报",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "warehouse-reports",
      "type": "reports_to",
      "source": "org-warehouse",
      "target": "org-enterprise",
      "label": "正式汇报",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-organization-decomposition-diagram",
    "artifact_id": "organization-decomposition-diagram",
    "title": "组织分解图 · 星河零售虚构案例",
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
      "org-warehouse"
    ],
    "relationship_ids": [
      "sales-reports",
      "warehouse-reports"
    ],
    "analysis": "正式组织的上下级或组成结构是什么？ 本视图限定订单履约改造范围，展示案例设定的组织分解图。确定组织范围和有效时间；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-organization-decomposition-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-organization-decomposition-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-organization-decomposition-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
