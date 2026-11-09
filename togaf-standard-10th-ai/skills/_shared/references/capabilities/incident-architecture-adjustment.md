# 事件后的架构调整记录

ID：`incident-architecture-adjustment`。主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G186 §12.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

事件如何改变了利益相关者的风险偏好与需求，有哪些目标变更、取消目标或取消变更的选项？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 事件如何改变了利益相关者的风险偏好与需求，有哪些目标变更、取消目标或取消变更的选项？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'incident', 'meaning': '事件事实、日期与证据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'objectives', 'meaning': '受影响目标', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'risk_appetite_before', 'meaning': '事件前风险偏好及权限方', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'risk_appetite_after', 'meaning': '事件后风险偏好及权限方', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'risk_tolerance', 'meaning': '风险容忍度及权限方', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'requirement_changes', 'meaning': '由偏好变化引起的需求变更及影响评估引用', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'options', 'meaning': '变更目标/取消目标/取消变更三类选项及其成本、确定性与后果', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'decision', 'meaning': '利益相关者决定状态、所选选项、权限与证据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'summary', 'meaning': '调整事项摘要', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:incident-adjustment。

```json
{
  "guide:incident-adjustment": [
    "incident",
    "objectives",
    "risk_appetite_before",
    "risk_appetite_after",
    "risk_tolerance",
    "requirement_changes",
    "options",
    "decision"
  ]
}
```

{
  "incident": {
    "meaning": "事件事实、日期与证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "objectives": {
    "meaning": "受影响目标",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "risk_appetite_before": {
    "meaning": "事件前风险偏好及权限方",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "risk_appetite_after": {
    "meaning": "事件后风险偏好及权限方",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "risk_tolerance": {
    "meaning": "风险容忍度及权限方",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "requirement_changes": {
    "meaning": "由偏好变化引起的需求变更及影响评估引用",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "options": {
    "meaning": "变更目标/取消目标/取消变更三类选项及其成本、确定性与后果",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "decision": {
    "meaning": "利益相关者决定状态、所选选项、权限与证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "summary": {
    "meaning": "调整事项摘要",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 记录事件事实与证据
2. 记录事件前后的风险偏好与风险容忍度及权限方
3. 把偏好变化登记为需求变更并做影响评估
4. 提出目标与工作变更方案，说明成本、确定性与残余风险
5. 同时评估取消目标与取消变更的后果
6. 由利益相关者决定并留存证据

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 事件改变风险偏好即需求变更，架构须调整
- 超出风险偏好的风险常用转移或规避
- 可接受成本的变更可能很少；取消目标或取消变更是正常选项
- 不推断事件原因，不代替利益相关者决定

- 名称、来源表格和成功输出不等于业务结论已核实
- 事件改变风险偏好即需求变更，架构须调整
- 超出风险偏好的风险常用转移或规避
- 可接受成本的变更可能很少；取消目标或取消变更是正常选项
- 不推断事件原因，不代替利益相关者决定


## 视图和交付物

- [事件后的架构调整记录](../profiles/incident-architecture-adjustment-default.md)

- [change-request](../deliverables/change-request.md)
- [requirements-impact-assessment](../deliverables/requirements-impact-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "需求变更引用不存在的目标",
    "expected": "IAA-003",
    "why": "IAA-003 [RC-1]: Requirement change must name an affected objective"
  },
  "modification_example": {
    "change": "只保留变更目标一种选项",
    "expected": "分析结果变化：新增缺口options:cancellation；option_kinds：[\"cancel-change\", \"cancel-objective\", \"change-target\"]→[\"change-target\"]"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/incident-architecture-adjustment.md)
[完整操作案例](../../references/capability-addenda/incident-architecture-adjustment.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "IAA-R1",
      "kind": "example",
      "description": "虚构事件INC-31：2026-10-18周末订单服务中断6小时，客服记录与监控截图已归档。",
      "locator": "raw-materials.json#IAA-R1"
    },
    {
      "id": "IAA-R2",
      "kind": "example",
      "description": "事件前风险委员会接受单次中断<4小时；事件后改为大促期间零中断容忍。目标OBJ-AV：大促期间订单可用。",
      "locator": "raw-materials.json#IAA-R2"
    },
    {
      "id": "IAA-R3",
      "kind": "example",
      "description": "方案X：双活改造，估算120万元、9个月，压测与供应商SLA支持其确定性，残余风险仍高于新偏好需购买业务中断保险。",
      "locator": "raw-materials.json#IAA-R3"
    }
  ],
  "entities": [
    {
      "id": "INC-31-ADJ",
      "type": "guide:incident-adjustment",
      "name": "事件后的架构调整：订单中断",
      "attributes": {
        "summary": "订单中断后按新风险偏好复议大促可用性目标与相关工作",
        "incident": {
          "id": "INC-31",
          "description": "订单服务中断6小时",
          "occurred_on": "2026-10-18",
          "evidence": [
            "IAA-R1"
          ]
        },
        "objectives": [
          {
            "id": "OBJ-AV",
            "statement": "大促期间订单可用"
          }
        ],
        "risk_appetite_before": {
          "statement": "接受单次中断<4小时",
          "authority": "风险委员会"
        },
        "risk_appetite_after": {
          "statement": "大促期间零中断容忍",
          "authority": "风险委员会"
        },
        "risk_tolerance": {
          "statement": "大促期间中断>15分钟即启动目标复议",
          "authority": "风险委员会"
        },
        "requirement_changes": [
          {
            "id": "RC-1",
            "objective_id": "OBJ-AV",
            "change": "大促期间可用性要求提高到99.95%",
            "impact_assessment_ref": "RIA-12"
          }
        ],
        "options": [
          {
            "id": "OPT-X",
            "kind": "change-target",
            "target_change": "订单服务双活",
            "work": "双活改造与切换演练",
            "cost": "估算120万元、9个月",
            "certainty_basis": "压测与供应商SLA",
            "residual_vs_appetite": "exceeds",
            "excess_strategy": "转移：购买业务中断保险"
          },
          {
            "id": "OPT-Y",
            "kind": "cancel-objective",
            "consequence": "放弃大促零中断目标，维持事件前偏好"
          },
          {
            "id": "OPT-Z",
            "kind": "cancel-change",
            "consequence": "不改造，接受与新偏好不一致的风险并上报"
          }
        ],
        "decision": {
          "status": "pending"
        }
      },
      "evidence": [
        "IAA-R1",
        "IAA-R2",
        "IAA-R3"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "incident-architecture-adjustment-baseline",
    "artifact_id": "incident-architecture-adjustment",
    "profile_id": "incident-architecture-adjustment-default",
    "title": "事件后的架构调整记录／虚构星河零售",
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
      "INC-31-ADJ"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行incident-architecture-adjustment-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "incident-architecture-adjustment-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "incident-architecture-adjustment-analysis",
      "method_id": "incident-architecture-adjustment-review",
      "inputs": {
        "summary": "订单中断后按新风险偏好复议大促可用性目标与相关工作",
        "incident": {
          "id": "INC-31",
          "description": "订单服务中断6小时",
          "occurred_on": "2026-10-18",
          "evidence": [
            "IAA-R1"
          ]
        },
        "objectives": [
          {
            "id": "OBJ-AV",
            "statement": "大促期间订单可用"
          }
        ],
        "risk_appetite_before": {
          "statement": "接受单次中断<4小时",
          "authority": "风险委员会"
        },
        "risk_appetite_after": {
          "statement": "大促期间零中断容忍",
          "authority": "风险委员会"
        },
        "risk_tolerance": {
          "statement": "大促期间中断>15分钟即启动目标复议",
          "authority": "风险委员会"
        },
        "requirement_changes": [
          {
            "id": "RC-1",
            "objective_id": "OBJ-AV",
            "change": "大促期间可用性要求提高到99.95%",
            "impact_assessment_ref": "RIA-12"
          }
        ],
        "options": [
          {
            "id": "OPT-X",
            "kind": "change-target",
            "target_change": "订单服务双活",
            "work": "双活改造与切换演练",
            "cost": "估算120万元、9个月",
            "certainty_basis": "压测与供应商SLA",
            "residual_vs_appetite": "exceeds",
            "excess_strategy": "转移：购买业务中断保险"
          },
          {
            "id": "OPT-Y",
            "kind": "cancel-objective",
            "consequence": "放弃大促零中断目标，维持事件前偏好"
          },
          {
            "id": "OPT-Z",
            "kind": "cancel-change",
            "consequence": "不改造，接受与新偏好不一致的风险并上报"
          }
        ],
        "decision": {
          "status": "pending"
        },
        "source_ids": [
          "IAA-R1",
          "IAA-R2",
          "IAA-R3"
        ]
      }
    }
  ]
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact incident-architecture-adjustment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
