# 组合主题工作包分组

`profile_id`: portfolio-theme-work-package-register-default；`artifact_id`: portfolio-theme-work-package-register；主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G186 §8.2表8-2、§8.3–8.5。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "portfolio-theme-work-package-register-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:portfolio_assignment。关系类型：。

```json
{
  "entities": {
    "guide:portfolio_assignment": [
      "theme",
      "work_package_id",
      "change_kind",
      "continuation",
      "required_work_packages",
      "importance",
      "impact_start",
      "effort",
      "investment",
      "evidence_refs",
      "allocation_note"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 表8-2空格表示架构信息未完整，不用0替代
- TOGAF变革工作包与PM的WBS叶任务不是同一概念
- 一个工作包不同时承担保持和改进分类；共享ID不重复预算

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-portfolio-theme-work-package-register-default",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 themes",
      "locator": "examples/addenda/project-management/raw-business-materials.json#themes"
    }
  ],
  "entities": [
    {
      "id": "portfolio-theme-work-package-register-default-1",
      "type": "guide:portfolio_assignment",
      "name": "单号唯一基础",
      "attributes": {
        "theme": "可靠交付",
        "work_package_id": "WP-ID",
        "change_kind": "improve",
        "continuation": "new",
        "required_work_packages": [],
        "importance": "战略强制（TH-01）",
        "impact_start": "2027-01",
        "effort": {
          "value": 20,
          "unit": "person-day",
          "basis": "TH-03项目估算"
        },
        "investment": {
          "value": 100000,
          "currency": "CNY",
          "basis": "TH-03项目估算"
        },
        "evidence_refs": [
          "TH-01",
          "TH-03"
        ],
        "allocation_note": "共享基础只记一次资金，其他主题可引用"
      },
      "evidence": [
        "src-portfolio-theme-work-package-register-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-theme-work-package-register-default-2",
      "type": "guide:portfolio_assignment",
      "name": "签收改进",
      "attributes": {
        "theme": "可靠交付",
        "work_package_id": "WP-SIGN",
        "change_kind": "improve",
        "continuation": "continuation",
        "required_work_packages": [
          "WP-ID"
        ],
        "importance": "支撑签收目标（TH-02）",
        "impact_start": "2027-03",
        "effort": {
          "value": 40,
          "unit": "person-day",
          "basis": "TH-03余工作估算"
        },
        "investment": {
          "value": 200000,
          "currency": "CNY",
          "basis": "TH-03待重新确认"
        },
        "evidence_refs": [
          "TH-02",
          "TH-03"
        ],
        "allocation_note": "续作不自动获得优先投资；仍需依据目标价值"
      },
      "evidence": [
        "src-portfolio-theme-work-package-register-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-theme-work-package-register-default-3",
      "type": "guide:portfolio_assignment",
      "name": "扫描设备维护",
      "attributes": {
        "theme": "运营优化",
        "work_package_id": "WP-KEEP",
        "change_kind": "keep",
        "continuation": "new",
        "required_work_packages": [],
        "importance": "保持现有运营（TH-02）",
        "impact_start": "2026-12",
        "effort": {
          "value": 5,
          "unit": "person-day",
          "basis": "TH-03"
        },
        "investment": {
          "value": 20000,
          "currency": "CNY",
          "basis": "TH-03"
        },
        "evidence_refs": [
          "TH-02",
          "TH-03"
        ],
        "allocation_note": "保持现状包不承担签收改进，避免一包混合不同价值分类"
      },
      "evidence": [
        "src-portfolio-theme-work-package-register-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-portfolio-theme-work-package-register-default",
    "artifact_id": "portfolio-theme-work-package-register",
    "profile_id": "portfolio-theme-work-package-register-default",
    "title": "组合主题工作包分组",
    "entity_ids": [
      "portfolio-theme-work-package-register-default-1",
      "portfolio-theme-work-package-register-default-2",
      "portfolio-theme-work-package-register-default-3"
    ],
    "relationship_ids": [],
    "analysis": "依表8-2列主题、名称、所需工作包、重要性、影响时点、工作量及投资；WP-SIGN依赖WP-ID，维护独立保持类，全部估算明确项目来源。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "themes"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile portfolio-theme-work-package-register-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile portfolio-theme-work-package-register-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
