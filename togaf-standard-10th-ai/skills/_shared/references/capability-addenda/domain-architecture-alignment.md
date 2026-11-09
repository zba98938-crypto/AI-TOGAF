# 领域架构融入整体EA核对（Domain Architecture Alignment Check）

工作产品 `domain-architecture-alignment` · 视图 `domain-architecture-alignment-default` · 方法 `domain-architecture-alignment-review` · 主责 [togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md) · 常用ADM：B C D。

来源：G186 §12.2。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

各领域架构是否服务同一EA项目与目标、引用共享模型，安全是否作为关注点贯穿其他域？

## 字段

- `guide:domain-architecture` 必填：`kind`（领域类别）、`project_id`（所属EA项目ID）、`objective_ids`（服务的EA项目目标ID）
- `guide:ea-project-scope` 必填：`objective_ids`（服务的EA项目目标ID）、`model_id`（共享架构模型ID）
- 可选：`shared_entity_ids`（引用的共享模型对象ID）、`treated_as`（安全的处理方式：concern或其他）、`referenced_domain_ids`（安全关注点所引用的其他领域ID）

## 步骤

1. 登记EA项目及其目标与共享模型
2. 登记每个领域架构所属项目、服务目标及共享对象
3. 标出按另一个项目工作或目的不在EA目标内的领域
4. 把安全作为关注点并引用其所涉其他领域
5. 修正后再进入跨域评审

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 领域必须融入整体EA，整体EA也须契合领域
- 安全架构只在参照其他域时存在，按关注点处理
- 对齐核对不评价领域方案质量

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate domain-architecture-alignment-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile domain-architecture-alignment-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `DAA-R1`：虚构EA项目EA-2027：目标OBJ-1缩短履约时长、OBJ-2降低合规风险，共享模型M-1。
- `DAA-R2`：数据领域团队按自建“数据中台项目DP-9”推进，目标为“建设统一数据平台”；安全团队计划单独编写安全架构文档。

基线结果（实际执行计算器所得）：

```json
{
  "rows": [
    {
      "id": "DOM-BIZ",
      "kind": "business",
      "findings": [],
      "state": "aligned-awaiting-review",
      "gaps": []
    },
    {
      "id": "DOM-DATA",
      "kind": "data",
      "findings": [
        "separate-project: 领域架构按另一个项目工作，未融入整体EA",
        "divergent-purpose: 目的不在EA项目目标内：OBJ-DP"
      ],
      "state": "misaligned",
      "gaps": [
        {
          "id": "DOM-DATA:shared-model",
          "reason": "no-shared-model-reference",
          "action": "引用共享模型中的对象，避免平行架构"
        }
      ]
    },
    {
      "id": "DOM-SEC",
      "kind": "security",
      "findings": [
        "security-standalone: 安全架构只在参照其他域时存在，应作为关注点并引用相关域"
      ],
      "state": "misaligned",
      "gaps": []
    }
  ],
  "gaps": [
    {
      "id": "DOM-DATA:shared-model",
      "reason": "no-shared-model-reference",
      "action": "引用共享模型中的对象，避免平行架构"
    }
  ],
  "notice": "对齐只按声明的项目与目标核对；不评价领域方案质量。"
}
```

修改：数据领域改为服务EA-2027的OBJ-1并引用共享对象。分析结果变化：关闭缺口DOM-DATA:shared-model。修改后结果：

```json
{
  "rows": [
    {
      "id": "DOM-BIZ",
      "kind": "business",
      "findings": [],
      "state": "aligned-awaiting-review",
      "gaps": []
    },
    {
      "id": "DOM-DATA",
      "kind": "data",
      "findings": [],
      "state": "aligned-awaiting-review",
      "gaps": []
    },
    {
      "id": "DOM-SEC",
      "kind": "security",
      "findings": [
        "security-standalone: 安全架构只在参照其他域时存在，应作为关注点并引用相关域"
      ],
      "state": "misaligned",
      "gaps": []
    }
  ],
  "gaps": [],
  "notice": "对齐只按声明的项目与目标核对；不评价领域方案质量。"
}
```

反例：安全关注点引用不存在的领域。实际拒绝：`DAA-002 [DOM-SEC]: Security references unknown domain DOM-NONE`

完整模型片段见 [能力注册](../capabilities/domain-architecture-alignment.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
