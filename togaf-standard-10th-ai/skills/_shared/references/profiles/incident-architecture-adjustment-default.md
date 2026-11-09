# 事件后的架构调整记录

`profile_id`: incident-architecture-adjustment-default；`artifact_id`: incident-architecture-adjustment；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G186 §12.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "incident-architecture-adjustment-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:incident-adjustment。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 事件改变风险偏好即需求变更，架构须调整
- 超出风险偏好的风险常用转移或规避
- 可接受成本的变更可能很少；取消目标或取消变更是正常选项
- 不推断事件原因，不代替利益相关者决定

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile incident-architecture-adjustment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile incident-architecture-adjustment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
