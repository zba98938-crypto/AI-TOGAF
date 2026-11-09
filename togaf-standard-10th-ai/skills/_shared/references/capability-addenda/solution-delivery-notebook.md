# 解决方案交付笔记本（Solution Delivery Notebook (Architecture Contract Template)）

工作产品 `solution-delivery-notebook` · 视图 `solution-delivery-notebook-default` · 方法 `solution-delivery-notebook-review` · 主责 [togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md) · 常用ADM：G。

来源：G186 附录D 表D-1。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

交付团队据以设计和测试的需求/规格、风险/控制配对、差距范围与目标架构摘要是什么？

## 字段

- `guide:solution-delivery-notebook` 必填：`work_package_id`（笔记本所对应的工作包）、`solution_concept_ref`（解决方案概念图视图ID）、`implementation_strategy`（处理差距或工作包的首选方法）、`stakeholders`（利益相关者及其需求ID）、`requirements`（入向需求及利益相关者ID）、`specifications`（架构规格；每条追溯到一项需求）、`risks`（适用风险；无控制时记录有证据的处理决定）、`controls`（控制；每条追溯到一项风险）、`gaps`（差距及in_scope真假）、`architecture_summary`（各域目标架构视图引用或不适用理由（仅供参考））

## 步骤

1. 写解决方案摘要：概念图、利益相关者目录、风险目录、差距目录
2. 写规格摘要：实施策略、架构规格、控制
3. 每条规格追溯到需求，每个控制追溯到风险
4. 标出本工作包处理与不处理的差距
5. 用视图引用概述各域目标架构（仅供参考）
6. 用需求/规格与风险/控制两类配对作为合规评估依据

## 来源要点

- 规格可适用于架构任何事物，但始终追溯到某项需求（G186 表D-1 架构规格）
- 控制可适用于架构任何事物，但始终追溯到某项风险（G186 表D-1 控制）
- 规格符合性按需求/规格配对与风险/控制配对测试（G186 表D-1 规格摘要）
- 差距目录标明本工作包处理范围；未处理的差距要明确标出（G186 表D-1 差距目录）
- 架构描述摘要仅供参考，用图、目录、矩阵概述目标架构（G186 表D-1 架构描述摘要）

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 规格总追溯到某项需求
- 控制总追溯到某项风险
- 架构描述摘要仅供参考，不替代规格
- 笔记本是交付沟通模板，不代表合同已签署

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate solution-delivery-notebook-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile solution-delivery-notebook-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `SDN-R1`：虚构工作包WP-7“门店自提”：处理差距G-1（无自提预约）；G-2（退货流程）不在本工作包。
- `SDN-R2`：门店运营要求自提预约准确率≥99%（R-ACC），法务要求只显示脱敏手机号（R-PRIV）；风险RK-1为预约超卖。
- `SDN-R3`：规格S-1：预约须通过库存服务锁定；S-2：前台仅读取脱敏视图。控制C-1：锁定失败时禁止确认预约。

基线结果（实际执行计算器所得）：

```json
{
  "id": "SDN-WP7",
  "pairs": {
    "requirement_specification": [
      {
        "requirement_id": "R-ACC",
        "specification_ids": [
          "S-1"
        ]
      },
      {
        "requirement_id": "R-PRIV",
        "specification_ids": [
          "S-2"
        ]
      }
    ],
    "risk_control": [
      {
        "risk_id": "RK-1",
        "control_ids": [
          "C-1"
        ]
      }
    ]
  },
  "gaps": [],
  "in_scope_gap_ids": [
    "G-1"
  ],
  "out_of_scope_gap_ids": [
    "G-2"
  ],
  "notice": "配对只证明可追溯结构；规格是否充分、控制是否有效、合同是否签署由治理责任方评审。"
}
```

修改：删除控制C-1。分析结果变化：新增缺口RK-1:control。修改后结果：

```json
{
  "id": "SDN-WP7",
  "pairs": {
    "requirement_specification": [
      {
        "requirement_id": "R-ACC",
        "specification_ids": [
          "S-1"
        ]
      },
      {
        "requirement_id": "R-PRIV",
        "specification_ids": [
          "S-2"
        ]
      }
    ],
    "risk_control": [
      {
        "risk_id": "RK-1",
        "control_ids": []
      }
    ]
  },
  "gaps": [
    {
      "id": "RK-1:control",
      "reason": "uncontrolled-risk",
      "action": "补充缓解控制，或记录有证据的接受/转移/规避决定"
    }
  ],
  "in_scope_gap_ids": [
    "G-1"
  ],
  "out_of_scope_gap_ids": [
    "G-2"
  ],
  "notice": "配对只证明可追溯结构；规格是否充分、控制是否有效、合同是否签署由治理责任方评审。"
}
```

反例：规格S-1追溯到不存在的需求R-NONE。实际拒绝：`SDN-004 [S-1]: Every specification must trace to a requirement`

完整模型片段见 [能力注册](../capabilities/solution-delivery-notebook.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
