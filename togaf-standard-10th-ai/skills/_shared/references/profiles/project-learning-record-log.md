# 持续经验记录

`profile_id`: project-learning-record-log；`artifact_id`: project-learning-record；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G188 §3.1.3、§3.6.3示例3-37及注释2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "project-learning-record-log",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:project_learning。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 持续Lessons Log与最终Lessons Learned/Report不是同一个状态
- 参加复盘或提出建议不等于改进已验证
- 无原计划/实绩不能编造差异；未经验证原因不能写成确定事实

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-learning-record-log --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-learning-record-log --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
