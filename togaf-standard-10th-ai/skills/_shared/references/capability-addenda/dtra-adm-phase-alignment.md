# DTRA因素与ADM阶段对齐（DTRA Factor to ADM Phase Alignment）

工作产品 `dtra-adm-phase-alignment` · 视图 `dtra-adm-phase-alignment-default` · 方法 `dtra-adm-phase-alignment-review` · 主责 [togaf-ea-capability](../../../togaf-ea-capability/SKILL.md) · 常用ADM：Preliminary A B C D E F G H Requirements。

来源：G212 §6、表6-1、图6-1。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

DTRA结果在每个ADM阶段意味着什么，各阶段考虑了哪些因素，低分因素如何处理？

## 字段

- `guide:dtra-alignment-summary` 必填：`assessment_ref`（DTRA评估引用）、`initiated_in_phase`（DTRA启动阶段）、`factor_ratings`（15因素1-7评分（G212 表A-1））、`reassessment`（复评时点：end-of-cycle或next-vision）
- `guide:dtra-phase-record` 必填：`phase`（ADM阶段）、`implication`（该阶段对数字采用的含义（表6-1））、`actions`（行动及其针对的因素ID）
- 可选：`progression_note`（基础因素未满足时的递进安排）、`deferred_factors`（有理由延后处理的因素）、`considered_factor_ids`（本阶段考虑的DTRA因素）、`tailored_out`（被裁剪的区域因素及理由）、`governance_distinction`（阶段G治理与“治理与合规”因素的区别说明）、`requirement_changes`（由偏好变化引起的需求变更及影响评估引用）

## 步骤

1. 在阶段A启动DTRA并引用评估结果
2. 按表6-1记录各阶段含义与行动
3. 对照图6-1区域考虑各阶段因素，或记录裁剪
4. 评分低于“同意”的因素安排行动或有理由延后
5. 基础因素未满足时说明递进安排
6. 需求变更经影响评估在下一周期实施
7. 在周期结束或下一周期愿景阶段复评

## 来源要点

- DTRA应在架构愿景阶段启动，以了解组织现状（G212 §6 正文）
- 可在ADM周期结束或下一周期愿景阶段重新评估（G212 §6 正文）
- 复核评分不是“非常同意”或“同意”的因素（G212 §7、附录A）
- 未满足基础因素时评估影响与持续因素无意义，应逐步推进（G212 §5.4）
- 阶段G的治理指实施方法恰当性，不要与C/D的“治理与合规”因素混淆（G212 表6-1 注）

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 阶段-因素映射来自图6-1同区位置推断，不是原文逐条规定
- 阶段G治理指实施方法恰当性，不是“治理与合规”因素
- 评分低于“同意”只触发复核，不是不合格判定

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate dtra-adm-phase-alignment-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile dtra-adm-phase-alignment-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `DAP-R1`：虚构DTRA问卷汇总（DTRA-2026Q3）：文化4、IT能力5、生态系统5，其余因素6或7；评估在阶段A启动。
- `DAP-R2`：各阶段行动记录：B阶段安排文化变革工作坊；C/D阶段安排伙伴生态评审；D阶段安排平台能力补强；周期结束复评。

基线结果（实际执行计算器所得）：

```json
{
  "rows": [
    {
      "phase": "Preliminary",
      "id": "DAP-Preliminary",
      "considered_factor_ids": [
        "sponsorship-direction",
        "vision"
      ],
      "gaps": []
    },
    {
      "phase": "A",
      "id": "DAP-A",
      "considered_factor_ids": [
        "sponsorship-direction",
        "vision"
      ],
      "gaps": []
    },
    {
      "phase": "B",
      "id": "DAP-B",
      "considered_factor_ids": [
        "business-model-adaptability",
        "business-rationale",
        "culture",
        "funding-resources",
        "scope-scale"
      ],
      "gaps": []
    },
    {
      "phase": "C",
      "id": "DAP-C",
      "considered_factor_ids": [
        "ecosystem",
        "governance-compliance",
        "policy-regulations",
        "skills-competence",
        "value-realization"
      ],
      "gaps": []
    },
    {
      "phase": "D",
      "id": "DAP-D",
      "considered_factor_ids": [
        "ecosystem",
        "governance-compliance",
        "it-capability",
        "skills-competence",
        "technology-maturity"
      ],
      "gaps": []
    },
    {
      "phase": "E",
      "id": "DAP-E",
      "considered_factor_ids": [
        "implementation-approach"
      ],
      "gaps": []
    },
    {
      "phase": "F",
      "id": "DAP-F",
      "considered_factor_ids": [
        "implementation-approach"
      ],
      "gaps": []
    },
    {
      "phase": "G",
      "id": "DAP-G",
      "considered_factor_ids": [
        "implementation-approach"
      ],
      "gaps": []
    },
    {
      "phase": "H",
      "id": "DAP-H",
      "considered_factor_ids": [],
      "gaps": []
    },
    {
      "phase": "Requirements",
      "id": "DAP-Requirements",
      "considered_factor_ids": [],
      "gaps": []
    }
  ],
  "attention_factor_ids": [
    "culture",
    "ecosystem",
    "it-capability"
  ],
  "weak_foundational_factor_ids": [
    "culture",
    "it-capability"
  ],
  "gaps": [],
  "notice": "阶段-因素区域来自图6-1的同区位置推断；评分低于“同意”只触发复核，不是不合格判定。"
}
```

修改：删除阶段B的文化行动。分析结果变化：新增缺口attention:culture。修改后结果：

```json
{
  "rows": [
    {
      "phase": "Preliminary",
      "id": "DAP-Preliminary",
      "considered_factor_ids": [
        "sponsorship-direction",
        "vision"
      ],
      "gaps": []
    },
    {
      "phase": "A",
      "id": "DAP-A",
      "considered_factor_ids": [
        "sponsorship-direction",
        "vision"
      ],
      "gaps": []
    },
    {
      "phase": "B",
      "id": "DAP-B",
      "considered_factor_ids": [
        "business-model-adaptability",
        "business-rationale",
        "culture",
        "funding-resources",
        "scope-scale"
      ],
      "gaps": []
    },
    {
      "phase": "C",
      "id": "DAP-C",
      "considered_factor_ids": [
        "ecosystem",
        "governance-compliance",
        "policy-regulations",
        "skills-competence",
        "value-realization"
      ],
      "gaps": []
    },
    {
      "phase": "D",
      "id": "DAP-D",
      "considered_factor_ids": [
        "ecosystem",
        "governance-compliance",
        "it-capability",
        "skills-competence",
        "technology-maturity"
      ],
      "gaps": []
    },
    {
      "phase": "E",
      "id": "DAP-E",
      "considered_factor_ids": [
        "implementation-approach"
      ],
      "gaps": []
    },
    {
      "phase": "F",
      "id": "DAP-F",
      "considered_factor_ids": [
        "implementation-approach"
      ],
      "gaps": []
    },
    {
      "phase": "G",
      "id": "DAP-G",
      "considered_factor_ids": [
        "implementation-approach"
      ],
      "gaps": []
    },
    {
      "phase": "H",
      "id": "DAP-H",
      "considered_factor_ids": [],
      "gaps": []
    },
    {
      "phase": "Requirements",
      "id": "DAP-Requirements",
      "considered_factor_ids": [],
      "gaps": []
    }
  ],
  "attention_factor_ids": [
    "culture",
    "ecosystem",
    "it-capability"
  ],
  "weak_foundational_factor_ids": [
    "culture",
    "it-capability"
  ],
  "gaps": [
    {
      "id": "attention:culture",
      "reason": "low-rated-factor-unaddressed",
      "action": "评分低于“同意”需复核；安排行动或记录有理由的延后"
    }
  ],
  "notice": "阶段-因素区域来自图6-1的同区位置推断；评分低于“同意”只触发复核，不是不合格判定。"
}
```

反例：文化评分写为9。实际拒绝：`DAP-002 [culture]: Rating must be 1-7 (G212 Table A-1)`

完整模型片段见 [能力注册](../capabilities/dtra-adm-phase-alignment.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
