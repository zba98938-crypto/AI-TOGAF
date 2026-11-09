# 组合主题工作包分组

ID：`portfolio-theme-work-package-register`。主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G186 §8.2表8-2、§8.3–8.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

如何把工作包按主题排序并识别依赖、投资和资源？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 如何把工作包按主题排序并识别依赖、投资和资源？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 范围、五维语境、所用目标与交付物版本
- 原始计划/访谈/验收/估算及来源ID
- 组织授权和容差规则；缺失时不代推

可选：

- 历史项目及组织模板

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:portfolio_assignment。

```json
{
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
}
```

{
  "name": {
    "meaning": "分组记录",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "theme": {
    "meaning": "组合主题及目标来源",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "work_package_id": {
    "meaning": "TOGAF变革工作包稳定ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "change_kind": {
    "meaning": "保持/改进/新差异化/新市场的项目分类",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "continuation": {
    "meaning": "新工作或本财年续作",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "required_work_packages": {
    "meaning": "前置工作包ID，方向本项依赖所列项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "importance": {
    "meaning": "继承战略重要性及依据，不发明权重",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "impact_start": {
    "meaning": "影响预计开始时间而非全部任务完成期",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "effort": {
    "meaning": "工作量/单位/估算依据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "investment": {
    "meaning": "金额/币种/估算范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "allocation_note": {
    "meaning": "多主题复用不重复计资，分组理由",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 从战略目标、当前路线和在建项目建立主题
2. 按稳定工作包ID区分新/续作与保持/改进分类
3. 记录战略重要性和前置依赖
4. 收集同口径工作量/投资/影响时点并标未齐字段
5. 检查循环、跨主题复用和资源争用后形成候选顺序

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 表8-2空格表示架构信息未完整，不用0替代
- TOGAF变革工作包与PM的WBS叶任务不是同一概念
- 一个工作包不同时承担保持和改进分类；共享ID不重复预算

- 表8-2空格表示架构信息未完整，不用0替代
- TOGAF变革工作包与PM的WBS叶任务不是同一概念
- 一个工作包不同时承担保持和改进分类；共享ID不重复预算


## 视图和交付物

- [组合主题工作包分组](../profiles/portfolio-theme-work-package-register-default.md)

- [architecture-roadmaps](../deliverables/architecture-roadmaps.md)
- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "WP-ID依赖WP-SIGN形成循环；或一包同时keep/improve",
    "expected": "dependency-cycle",
    "why": "dependency-cycle或ambiguous-change-kind",
    "original_expected_text": "dependency-cycle或ambiguous-change-kind"
  },
  "modification_example": {
    "change": "WP-SIGN新增等待数据责任批准的前置WP-GOV",
    "expected": "新增前置记录，签收不能沿旧依赖序列启动"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/portfolio-theme-work-package-register.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact portfolio-theme-work-package-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
