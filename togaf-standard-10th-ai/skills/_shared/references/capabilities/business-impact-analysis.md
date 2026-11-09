# 业务影响分析

ID：`business-impact-analysis`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.1.4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

安全不足会使哪些业务结果受损？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 安全不足会使哪些业务结果受损？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_process
- loss_type
- impact

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：impact_scenario。

```json
{
  "impact_scenario": [
    "business_process",
    "loss_type",
    "impact",
    "criticality",
    "time_horizon"
  ],
  "risk_asset": [
    "asset_id",
    "criticality",
    "owner",
    "confidentiality_need",
    "integrity_need",
    "availability_need"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_process": {
    "meaning": "受影响的业务流程引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "loss_type": {
    "meaning": "业务损失或收益的类型",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "impact": {
    "meaning": "业务影响及其依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "criticality": {
    "meaning": "相对业务关键性及判据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "time_horizon": {
    "meaning": "分析覆盖的时间窗口",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从关键业务结果识别中断或损失场景
2. 记录影响类型与时间范围
3. 确认关键风险领域
4. 把结果交给风险评估

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 业务影响分析不定义事件发生的可能性
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 业务影响分析不定义事件发生的可能性


## 视图和交付物

- [业务影响分析](../profiles/business-impact-analysis-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务影响分析」给出：业务影响分析不定义事件发生的可能性",
    "expected": "missing-evidence",
    "why": "业务影响分析不定义事件发生的可能性"
  },
  "modification_example": {
    "change": "在「业务影响分析」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "business-impact-analysis-default-record",
      "type": "impact_scenario",
      "name": "业务影响分析：订单范围记录",
      "attributes": {
        "business_process": "订单确认与发运",
        "loss_type": "订单不可用造成履约中断",
        "impact": "高峰时段无法履约，影响当日发运承诺",
        "criticality": "关键：订单在一个工作日内发运",
        "time_horizon": "2026年度迁移期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-impact-analysis-default",
    "artifact_id": "business-impact-analysis",
    "profile_id": "business-impact-analysis-default",
    "title": "业务影响分析／虚构案例",
    "entity_ids": [
      "business-impact-analysis-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-impact-analysis --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
