# 数字可持续教育与技能计划

ID：`sustainability-education-plan`。主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G242 §3.3.2、§4.3、§5.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

所有员工和关键专业角色怎样形成可应用的可持续ICT技能？

- 业务负责人
- 企业架构师
- 环境核算负责人
- 采购及供应商负责人
- HR与治理负责人
- 所有员工和关键专业角色怎样形成可应用的可持续ICT技能？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 组织、服务、业务用途及所评估期间/生命周期边界
- 原始访谈、使用数据、供应商记录及稳定证据ID
- 适用目标、职责和组织自定决策规则；未知项显式登记

可选：

- 历史评估、环境数据目录、采购契约及角色技能资料

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:sustainability_learning。

```json
{
  "guide:sustainability_learning": [
    "audience",
    "population",
    "current_evidence",
    "skill_need",
    "learning_activity",
    "resources",
    "application_check",
    "hr_change",
    "owner",
    "status",
    "evidence_refs"
  ]
}
```

{
  "name": {
    "meaning": "教育项目",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "audience": {
    "meaning": "全员或具体角色",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "population": {
    "meaning": "覆盖人数及范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "current_evidence": {
    "meaning": "现有知识/培训/实操证据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "skill_need": {
    "meaning": "需补知识与技能",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "learning_activity": {
    "meaning": "可执行活动",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "resources": {
    "meaning": "已选资源及可用性",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "application_check": {
    "meaning": "实际应用能力的验证方式",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "hr_change": {
    "meaning": "职位/招聘要求变更",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "owner": {
    "meaning": "责任人",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "status": {
    "meaning": "覆盖与验证状态",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "原料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 列全员与重叠专业角色，查当前证据
2. 将普遍意识与角色技能分开
3. 为采购、核算、架构等设计实操任务
4. 安排资源、责任、时间与HR职位/招聘变更
5. 验证理解/实践效果；参加课程不自动提熟练度

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 不得仅覆盖ICT员工而漏业务及采购
- 重叠人群不重复计覆盖人数
- 课程/认证建议需核实可用性；本指南例子不代表当前认证有效
- 无评分依据不得自行给技能等级

- 不得仅覆盖ICT员工而漏业务及采购
- 重叠人群不重复计覆盖人数
- 课程/认证建议需核实可用性；本指南例子不代表当前认证有效
- 无评分依据不得自行给技能等级


## 视图和交付物

- [可持续性教育与角色技能计划](../profiles/sustainability-education-plan-default.md)

- [organization-model](../deliverables/organization-model.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "仅20名ICT人员被标全员覆盖",
    "expected": "all-staff-coverage-gap"
  },
  "modification_example": {
    "change": "采购4人完成报告识别和合同练习，但全员理解验证仍未完成",
    "expected": "采购能力证据更新，不能把全员状态标完成"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/sustainability-education-plan.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。",
  "sources": [
    {
      "id": "src-sustainability-education-plan-default",
      "kind": "example",
      "description": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。 材料组 education",
      "locator": "examples/addenda/sustainability/raw-business-materials.json#education"
    }
  ],
  "entities": [
    {
      "id": "sustainability-education-plan-default-1",
      "type": "guide:sustainability_learning",
      "name": "全员基础",
      "attributes": {
        "audience": "全部员工",
        "population": 100,
        "current_evidence": "45人仅参加，未测理解",
        "skill_need": "能源/气候/资源与自身ICT使用影响",
        "learning_activity": "同伴工作坊与使用场景练习",
        "resources": "内部同伴工作坊/项目选定课程；可用日期待排",
        "application_check": "解释个人使用选择的影响与替代方式",
        "hr_change": "入职教育加入相同基础",
        "owner": "HR与对应职能负责人",
        "status": "planned; competence-not-verified",
        "evidence_refs": [
          "ED-01",
          "ED-02",
          "ED-03"
        ]
      },
      "evidence": [
        "src-sustainability-education-plan-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-education-plan-default-2",
      "type": "guide:sustainability_learning",
      "name": "采购专项",
      "attributes": {
        "audience": "采购人员",
        "population": 4,
        "current_evidence": "无专项训练",
        "skill_need": "全生命周期数据、条款、手段/结果义务",
        "learning_activity": "评审虚构供应商报告并起草条款",
        "resources": "内部同伴工作坊/项目选定课程；可用日期待排",
        "application_check": "识别净零宣传中的范围/抵消缺口",
        "hr_change": "采购岗位与面试加入数据契约能力",
        "owner": "HR与对应职能负责人",
        "status": "planned; competence-not-verified",
        "evidence_refs": [
          "ED-01",
          "ED-02",
          "ED-03"
        ]
      },
      "evidence": [
        "src-sustainability-education-plan-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-education-plan-default-3",
      "type": "guide:sustainability_learning",
      "name": "碳核算专项",
      "attributes": {
        "audience": "核算人员",
        "population": 2,
        "current_evidence": "无边界实操证据",
        "skill_need": "边界、单位、Scope2两法与Scope3子集",
        "learning_activity": "复核一份云19字段记录",
        "resources": "内部同伴工作坊/项目选定课程；可用日期待排",
        "application_check": "发现市场/地点法相加与子集重复计量",
        "hr_change": "核算岗位加入边界复核",
        "owner": "HR与对应职能负责人",
        "status": "planned; competence-not-verified",
        "evidence_refs": [
          "ED-01",
          "ED-02",
          "ED-03"
        ]
      },
      "evidence": [
        "src-sustainability-education-plan-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-education-plan-default-4",
      "type": "guide:sustainability_learning",
      "name": "架构专项",
      "attributes": {
        "audience": "架构师",
        "population": 6,
        "current_evidence": "缺生态设计实操",
        "skill_need": "生态设计、低技术替代、双入口分析",
        "learning_activity": "从用途与设备提出方案并评审",
        "resources": "内部同伴工作坊/项目选定课程；可用日期待排",
        "application_check": "业务可接受性、全生命周期比较与约束完整",
        "hr_change": "架构岗位加入生态设计技能",
        "owner": "HR与对应职能负责人",
        "status": "planned; competence-not-verified",
        "evidence_refs": [
          "ED-01",
          "ED-02",
          "ED-03"
        ]
      },
      "evidence": [
        "src-sustainability-education-plan-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-sustainability-education-plan-default",
    "artifact_id": "sustainability-education-plan",
    "profile_id": "sustainability-education-plan-default",
    "title": "可持续性教育与角色技能计划",
    "entity_ids": [
      "sustainability-education-plan-default-1",
      "sustainability-education-plan-default-2",
      "sustainability-education-plan-default-3",
      "sustainability-education-plan-default-4"
    ],
    "relationship_ids": [],
    "analysis": "全员100与专项采购4/核算2/架构6是重叠人群，不相加成112。45人参训不代表已理解；专项技能通过实际任务检验。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "education"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact sustainability-education-plan --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
