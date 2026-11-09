# 敏捷协作模式选择与切换

`profile_id`: agile-pattern-selection；`artifact_id`: options-decision-matrix；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G210 §3.3、§3.3.5–3.3.8。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-agile-1。

{
  "id": "agile-pattern-selection",
  "version": "1.0",
  "source_verified": false
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:agile_pattern_choice。关系类型：。

```json
{
  "entities": {
    "guide:agile_pattern_choice": [
      "pattern",
      "capability_evidence",
      "coordination",
      "feasibility",
      "selected",
      "reason",
      "constraints",
      "switch_trigger",
      "maturity_boundary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 能力容量授权证据
- 没有四级成熟度/权重
- 未来周期继承/退回条件

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "sources": [
    {
      "id": "raw-agile",
      "kind": "example",
      "description": "虚构云港城市图书馆预约服务，原业务材料在本包内，未声称真实批准。",
      "locator": "examples/addenda/agile-collaboration/raw-business-materials.json"
    },
    {
      "id": "guide-agile",
      "kind": "local-translation",
      "description": "G210本地正文§3.3–3.3.8；历史图JSON不证明本轮原图已核验。",
      "locator": "references/source-tables/agile-collaboration-patterns.json"
    }
  ],
  "scopes": [
    {
      "id": "scope-selection",
      "description": "候选选择"
    }
  ],
  "entities": [
    {
      "id": "choice-ea",
      "type": "guide:agile_pattern_choice",
      "name": "企业架构开发敏捷",
      "scope_id": "scope-selection",
      "attributes": {
        "pattern": "ea",
        "capability_evidence": "R01业务容量不足；R02独立EA/方案；R05逐队缺口",
        "coordination": "共享DORP、每周支持会；非每队三能力",
        "feasibility": "可行备选但延后方案反馈",
        "selected": false,
        "reason": "比较反馈时机、能力分布与业务参与；不打分",
        "constraints": [
          "隐私未决",
          "授权待审",
          "不自动上线"
        ],
        "switch_trigger": "每队三能力与授权均有证据才重选",
        "maturity_boundary": "不是四级成熟度/固定晋级路线"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "choice-solution",
      "type": "guide:agile_pattern_choice",
      "name": "解决方案协作",
      "scope_id": "scope-selection",
      "attributes": {
        "pattern": "solution",
        "capability_evidence": "R01业务容量不足；R02独立EA/方案；R05逐队缺口",
        "coordination": "共享DORP、每周支持会；非每队三能力",
        "feasibility": "当前候选采用",
        "selected": true,
        "reason": "比较反馈时机、能力分布与业务参与；不打分",
        "constraints": [
          "隐私未决",
          "授权待审",
          "不自动上线"
        ],
        "switch_trigger": "每队三能力与授权均有证据才重选",
        "maturity_boundary": "不是四级成熟度/固定晋级路线"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "choice-cross",
      "type": "guide:agile_pattern_choice",
      "name": "跨开发协作",
      "scope_id": "scope-selection",
      "attributes": {
        "pattern": "cross",
        "capability_evidence": "R01业务容量不足；R02独立EA/方案；R05逐队缺口",
        "coordination": "共享DORP、每周支持会；非每队三能力",
        "feasibility": "业务持续开发容量不足",
        "selected": false,
        "reason": "比较反馈时机、能力分布与业务参与；不打分",
        "constraints": [
          "隐私未决",
          "授权待审",
          "不自动上线"
        ],
        "switch_trigger": "每队三能力与授权均有证据才重选",
        "maturity_boundary": "不是四级成熟度/固定晋级路线"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "choice-functional",
      "type": "guide:agile_pattern_choice",
      "name": "跨职能敏捷",
      "scope_id": "scope-selection",
      "attributes": {
        "pattern": "functional",
        "capability_evidence": "R01业务容量不足；R02独立EA/方案；R05逐队缺口",
        "coordination": "共享DORP、每周支持会；非每队三能力",
        "feasibility": "每队三能力证据不足",
        "selected": false,
        "reason": "比较反馈时机、能力分布与业务参与；不打分",
        "constraints": [
          "隐私未决",
          "授权待审",
          "不自动上线"
        ],
        "switch_trigger": "每队三能力与授权均有证据才重选",
        "maturity_boundary": "不是四级成熟度/固定晋级路线"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-agile-pattern-selection",
    "artifact_id": "options-decision-matrix",
    "profile_id": "agile-pattern-selection",
    "title": "预约协作模式选择与切换",
    "scope_id": "scope-selection",
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
      "choice-ea",
      "choice-solution",
      "choice-cross",
      "choice-functional"
    ],
    "relationship_ids": [],
    "analysis": "选解决方案协作；业务容量/每队三能力不足，保留重选条件。",
    "legend": "并列选项；没有成熟度/加权总分。"
  },
  "raw_input": "examples/addenda/agile-collaboration/raw-business-materials.json",
  "analysis_path": "examples/addenda/agile-collaboration/analysis.md"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile agile-pattern-selection --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile agile-pattern-selection --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
