# BI 与分析演进架构

ID：`bi-transition-architecture`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G238 §3；图3-1–3-4；G238 §3.2.1–3.2.4；G238 表4-2价值链设计、表4-3存储/处理/监控；G238 表4-2高级分析模型工业化、运营平台；表4-3分析模型管理与监控。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

如何从现有数仓演进到目标分析平台？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 如何从现有数仓演进到目标分析平台？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- state_id
- role
- inbound

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：analytics_component, guide:bi_operating_state, ops:bi_value_chain, ops:bi_model_operations。

```json
{
  "analytics_component": [
    "role",
    "inbound",
    "outbound",
    "storage",
    "coexistence"
  ],
  "guide:bi_operating_state": [
    "state_ref",
    "evolution_kind",
    "data_flows",
    "raw_and_metadata",
    "consumers",
    "incremental_benefit",
    "known_gap",
    "operating_exit_gate",
    "legacy_requirement_coverage",
    "retirement_authorized",
    "cost_basis",
    "schedule_basis"
  ],
  "ops:bi_value_chain": [
    "layer_kind",
    "input_refs",
    "transformation_rule",
    "business_purpose",
    "owner",
    "quality_controls",
    "protection_controls",
    "metadata_lineage",
    "scope",
    "reference_identity",
    "evidence_detail"
  ],
  "ops:bi_model_operations": [
    "model_ref",
    "business_use",
    "lifecycle",
    "measure",
    "data_quality",
    "monitoring",
    "response",
    "lineage",
    "evidence_detail",
    "claim"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "state_id": {
    "meaning": "具体架构状态的稳定标识",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "role": {
    "meaning": "承担职责的角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "inbound": {
    "meaning": "入站信息流",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "outbound": {
    "meaning": "出站信息流",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "storage": {
    "meaning": "数据存储责任与位置",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "coexistence": {
    "meaning": "新旧状态共存条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `ops:data_derivation` | ops:bi_value_chain → ops:bi_value_chain | 数据派生/流转，源向目标，具体转换在目标transformation_rule |

## 分析步骤

1. 描述基线和目标
2. 设计多个可运营过渡
3. 区分入站出站和回写
4. 安排数据及应用迁移依赖
5. 识别旧系统已满足需求与新价值
6. 按可选过渡定义流向/数据语义和消费者
7. 记录每态收益、缺口和可运营条件
8. 退出前逐项验证旧需求与恢复、治理、元数据
9. 从业务决策反推数据和语义
10. 逐层区分原始、技术准备和业务信息转换
11. 记录输入输出及有向派生关系
12. 检查质量、安全、元数据和运营责任贯穿全链
13. 不因价值链存在就认定数据正确/及时
14. 由业务用途明确错误后果和运营责任
15. 选有项目依据的准确性/数据/技术/安全/使用观测
16. 给每指标单位、窗口、证据与阈值来源，未知保持未知
17. 按触发设计停止、人工回退、评审和新版本测试
18. 形成运行监控记录后再评审实际表现

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 不同状态是同一架构的演进视图，不机械当成独立制品种类
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 不同状态是同一架构的演进视图，不机械当成独立制品种类


## 视图和交付物

- [BI 与分析演进架构](../profiles/bi-transition-architecture-default.md)
- [BI 基线多过渡与目标](../profiles/bi-baseline-transition-target.md)
- [BI多阶段运营与退出条件](../profiles/bi-stage-operability-and-exit.md)
- [BI数据价值链、语义与控制](../profiles/bi-value-chain-controls.md)
- [BI分析模型运营监控与处置](../profiles/bi-model-operating-monitoring.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「BI 与分析演进架构」给出：不同状态是同一架构的演进视图，不机械当成独立制品种类",
    "expected": "mixed-evolution",
    "why": "不同状态是同一架构的演进视图，不机械当成独立制品种类"
  },
  "modification_example": {
    "change": "在「BI 与分析演进架构」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "bi-transition-architecture-default-baseline",
      "type": "analytics_component",
      "name": "基线分析平台",
      "attributes": {
        "state_id": "baseline",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-transition1",
      "type": "analytics_component",
      "name": "过渡1分析平台",
      "attributes": {
        "state_id": "transition1",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-transition2",
      "type": "analytics_component",
      "name": "过渡2分析平台",
      "attributes": {
        "state_id": "transition2",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-target",
      "type": "analytics_component",
      "name": "目标分析平台",
      "attributes": {
        "state_id": "target",
        "role": "数据处理与分析消费支持",
        "inbound": "交易应用提交已完成订单",
        "outbound": "向报表提供聚合数据，目标保留受控回写",
        "storage": "基线EDW；目标新平台内保留EDW职责",
        "coexistence": "新旧并行对账，按消费者分批切换",
        "operating_conditions": "运营责任、数据一致性、控制连续性及回退须经验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "bi-transition-architecture-default-bi-transition-architecture-default-baseline-next",
      "type": "traces_to",
      "source": "bi-transition-architecture-default-baseline",
      "target": "bi-transition-architecture-default-transition1",
      "label": "演进状态；不是强制替换厂商",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-bi-transition-architecture-default-transition1-next",
      "type": "traces_to",
      "source": "bi-transition-architecture-default-transition1",
      "target": "bi-transition-architecture-default-transition2",
      "label": "演进状态；不是强制替换厂商",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bi-transition-architecture-default-bi-transition-architecture-default-transition2-next",
      "type": "traces_to",
      "source": "bi-transition-architecture-default-transition2",
      "target": "bi-transition-architecture-default-target",
      "label": "演进状态；不是强制替换厂商",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-bi-transition-architecture-default",
    "artifact_id": "bi-transition-architecture",
    "profile_id": "bi-transition-architecture-default",
    "title": "BI 与分析演进架构／虚构案例",
    "entity_ids": [
      "bi-transition-architecture-default-baseline",
      "bi-transition-architecture-default-transition1",
      "bi-transition-architecture-default-transition2",
      "bi-transition-architecture-default-target"
    ],
    "relationship_ids": [
      "bi-transition-architecture-default-bi-transition-architecture-default-baseline-next",
      "bi-transition-architecture-default-bi-transition-architecture-default-transition1-next",
      "bi-transition-architecture-default-bi-transition-architecture-default-transition2-next"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact bi-transition-architecture --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
