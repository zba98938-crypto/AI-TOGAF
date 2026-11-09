# 项目经验记录与教训报告

ID：`project-learning-record`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G188 §3.1.3、§3.6.3示例3-37及注释2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些观察应成为后续项目和EA能力改进的输入？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 哪些观察应成为后续项目和EA能力改进的输入？
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

对象类型：guide:project_learning。

```json
{
  "guide:project_learning": [
    "record_kind",
    "expected",
    "actual",
    "difference",
    "cause_hypothesis",
    "evidence_refs",
    "impact",
    "recommendation",
    "owner",
    "verification",
    "status",
    "follow_up_reference"
  ]
}
```

{
  "name": {
    "meaning": "经验事项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "record_kind": {
    "meaning": "ongoing-log或final-lessons-report",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "expected": {
    "meaning": "当初计划或假设",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "actual": {
    "meaning": "实际观察",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "difference": {
    "meaning": "具体差异，不把因果当事实",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "cause_hypothesis": {
    "meaning": "已证实原因或待验证假设",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID/访谈/记录",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "impact": {
    "meaning": "对项目的实际影响",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "recommendation": {
    "meaning": "下一项目可执行改进",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "owner": {
    "meaning": "负责采取改进的人",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "verification": {
    "meaning": "如何验证建议有效",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "status": {
    "meaning": "观察/原因待证/建议待试点等",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "follow_up_reference": {
    "meaning": "能力变更请求或后续项目引用",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 持续日志从以往经验和本项目观察开始
2. AAR分别记录预期/实际/原因/改进
3. 区别证据支持原因与待验证假设
4. 收尾筛选关键教训并指定改进责任与验证
5. 将可执行能力改进形成H变更请求并向后续项目传递

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 持续Lessons Log与最终Lessons Learned/Report不是同一个状态
- 参加复盘或提出建议不等于改进已验证
- 无原计划/实绩不能编造差异；未经验证原因不能写成确定事实

- 持续Lessons Log与最终Lessons Learned/Report不是同一个状态
- 参加复盘或提出建议不等于改进已验证
- 无原计划/实绩不能编造差异；未经验证原因不能写成确定事实


## 视图和交付物

- [持续经验记录](../profiles/project-learning-record-log.md)
- [项目最终经验教训](../profiles/project-learning-record-report.md)

- [change-request](../deliverables/change-request.md)
- [architecture-repository](../deliverables/architecture-repository.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "仅写“沟通不好，要加强沟通”无预期实际和证据",
    "expected": "learning-evidence-gap"
  },
  "modification_example": {
    "change": "下一项目采用模板后同范围清单确认8天、返工1次",
    "expected": "记录试点结果和可比性，改进证据增强但不能由单例证明普遍因果"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/project-learning-record.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-project-learning-record-log",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 lessons",
      "locator": "examples/addenda/project-management/raw-business-materials.json#lessons"
    }
  ],
  "entities": [
    {
      "id": "project-learning-record-log-1",
      "type": "guide:project_learning",
      "name": "应用边界导致返工",
      "attributes": {
        "record_kind": "ongoing-log",
        "expected": "10天确认应用清单",
        "actual": "22天，3次返工",
        "difference": "多12天",
        "cause_hypothesis": "各部门应用边界不同；访谈尚未完成，因果待确认",
        "evidence_refs": [
          "LS-01"
        ],
        "impact": "增派两人追赶；具体额外工时尚未收集",
        "recommendation": "启动时定义应用边界并用统一模板试填",
        "owner": "架构方法负责人",
        "verification": "下一项目记录确认用时与返工次数，保持范围可比",
        "status": "observed; cause-pending; action-proposed",
        "follow_up_reference": "CR-EA-TEMPLATE（候选）"
      },
      "evidence": [
        "src-project-learning-record-log"
      ],
      "certainty": "assumed"
    },
    {
      "id": "project-learning-record-log-2",
      "type": "guide:project_learning",
      "name": "CFO成本关注缺失",
      "attributes": {
        "record_kind": "ongoing-log",
        "expected": "阶段评审可支持成本决策",
        "actual": "许可/维护成本未采集，补录延迟3天",
        "difference": "关注点覆盖不足",
        "cause_hypothesis": "初始视角只覆盖功能技术；LS-02可验证资料缺项，尚不推断个人动机",
        "evidence_refs": [
          "LS-02",
          "LS-03"
        ],
        "impact": "CFO视图返工，决策延迟3天",
        "recommendation": "需求确认时加入CFO并将许可/维护成本纳入选定视角",
        "owner": "项目经理/财务代表",
        "verification": "下一项目启动评审检查全部关注点信息覆盖",
        "status": "ongoing-observation",
        "follow_up_reference": "CR-EA-VIEWPOINT（候选）"
      },
      "evidence": [
        "src-project-learning-record-log"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-learning-record-log",
    "artifact_id": "project-learning-record",
    "profile_id": "project-learning-record-log",
    "title": "持续经验记录",
    "entity_ids": [
      "project-learning-record-log-1",
      "project-learning-record-log-2"
    ],
    "relationship_ids": [],
    "analysis": "按AAR比较预期、实际、差异原因和改进；日志连续保留事实，最终报告筛选可行动教训。建议尚未经过试点，不宣称已消除延期。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "lessons"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact project-learning-record --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
