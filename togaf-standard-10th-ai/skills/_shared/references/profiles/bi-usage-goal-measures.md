# BI用途待办、目标与可追溯度量

`profile_id`: bi-usage-goal-measures；`artifact_id`: bi-requirements-profile；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G238 §3.1阶段B、表4-1、表4-2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "bi-usage-goal-measures",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "结构化表格，含完整属性、方向和证据；不是来源图模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:bi_usage。关系类型：。

```json
{
  "entities": {
    "ops:bi_usage": [
      "user",
      "pain",
      "decision",
      "business_objects",
      "sponsor",
      "goal_reference",
      "metric",
      "priority_rationale",
      "priority_rule",
      "lifecycle",
      "data_access",
      "evidence_detail",
      "gap"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 参考方向不是目标或达标
- 每指标有单位/时间/依据
- 无ROI公式则不计算
- 数据民主化不放开机密数据

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/bi-usage-goal-measures/raw-brief.md",
  "analysis_path": "examples/addenda/operations/bi-usage-goal-measures/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚运营总监赞助两用例：U1缺件预警辅助调度主管上门前复核与调拨，使用预约/库存/站点。项目11月目标一个已在生产采用、有负责人证据的自动化检查功能，基线零，尚未测量。U2预测维修时长辅助服务经理选窗口，故障标签质量未知，价值尚定性。赞助人按重复决策价值与数据可得性先做U1后做U2，没有数字权重/ROI公式。业务分析师和数据工程师设计、平台部署、运营产品负责人维护。客户联系方式不进看板。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "BI-U1",
      "type": "ops:bi_usage",
      "name": "备件缺货预警",
      "attributes": {
        "user": "调度主管",
        "pain": "到站缺件导致二次上门",
        "decision": "上门前复核并调拨备件",
        "business_objects": [
          "维修预约",
          "备件库存",
          "站点"
        ],
        "sponsor": "运营总监",
        "goal_reference": {
          "id": "G238-T4-1-10",
          "kind": "goal",
          "name": "提升运营效率",
          "definition": "旨在提升组织从创新到运营之敏捷性的用例与服务。",
          "indicator_direction": "↑ 自动化功能数量",
          "locator": "G238 表4-1 L405"
        },
        "metric": {
          "name": "自动化缺件检查功能数",
          "unit": "function-count",
          "period": "2026-11月末",
          "baseline": 0,
          "target": 1,
          "rule": "项目仅计生产采用且有负责人证据的功能",
          "basis": "虚构赞助人记录B-01",
          "observed": null
        },
        "priority_rationale": "先做：每天重复决策且已找到三类数据，技术复杂度较低",
        "priority_rule": "项目赞助人按重复决策价值与数据可得性顺序讨论，无数值权重",
        "lifecycle": {
          "design": "业务分析师+数据工程师",
          "deploy": "平台团队",
          "maintain": "运营产品负责人",
          "current": "candidate"
        },
        "data_access": "需按角色授权；预约客户联系方式不进入预警看板",
        "evidence_detail": "虚构B-01/B-02，目标值仅项目声明",
        "gap": "测量尚未运行；不得用参考指标方向宣称结果"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "BI-U2",
      "type": "ops:bi_usage",
      "name": "维修时长预测",
      "attributes": {
        "user": "服务经理",
        "pain": "不能说明复杂故障耗时",
        "decision": "为客户选择预约窗口",
        "business_objects": [
          "故障类型",
          "历史工单"
        ],
        "sponsor": "运营总监",
        "goal_reference": {
          "id": "G238-T4-1-15",
          "kind": "goal",
          "name": "借助新数据能力（如数据科学）创造业务价值",
          "definition": "新数据能力承诺创造新业务价值与新市场；组织须能借助新数据能力参与国际竞争。CDO 岗位正为此设立。",
          "indicator_direction": "↑ 数据用例产生的价值",
          "locator": "G238 表4-1 L410"
        },
        "metric": {
          "name": "降低二次沟通的业务价值",
          "unit": "qualitative",
          "period": "2026-12试点复盘",
          "baseline": "unknown",
          "target": "unknown",
          "rule": "先收集用户反馈，不计算ROI",
          "basis": "虚构业务访谈B-02",
          "observed": null
        },
        "priority_rationale": "后做：价值假设明确，但历史故障标签质量未知",
        "priority_rule": "项目赞助人按重复决策价值与数据可得性顺序讨论，无数值权重",
        "lifecycle": {
          "design": "业务分析师+数据工程师",
          "deploy": "平台团队",
          "maintain": "运营产品负责人",
          "current": "candidate"
        },
        "data_access": "需按角色授权；预约客户联系方式不进入预警看板",
        "evidence_detail": "虚构B-01/B-02，目标值仅项目声明",
        "gap": "测量尚未运行；不得用参考指标方向宣称结果"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [],
  "view": {
    "id": "v-bi-usage-goal-measures",
    "artifact_id": "bi-requirements-profile",
    "profile_id": "bi-usage-goal-measures",
    "title": "BI用途待办、目标与可追溯度量",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "BI-U1",
      "BI-U2"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-usage-goal-measures --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-usage-goal-measures --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
