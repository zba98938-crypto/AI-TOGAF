# 可持续性教育与角色技能计划

`profile_id`: sustainability-education-plan-default；`artifact_id`: sustainability-education-plan；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G242 §3.3.2、§4.3、§5.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "sustainability-education-plan-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:sustainability_learning。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不得仅覆盖ICT员工而漏业务及采购
- 重叠人群不重复计覆盖人数
- 课程/认证建议需核实可用性；本指南例子不代表当前认证有效
- 无评分依据不得自行给技能等级

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-education-plan-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-education-plan-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
