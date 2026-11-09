# 业务风险模型／风险登记册

ID：`business-risk-register`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.4–5.3.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些风险需要处置并由谁负责？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些风险需要处置并由谁负责？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- asset
- threat
- vulnerability

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：application, control, control_objective, loss_event, risk, risk_asset, security_requirement, threat_event, vulnerability。

```json
{
  "risk": [
    "asset",
    "threat",
    "vulnerability",
    "likelihood",
    "impact",
    "owner",
    "treatment",
    "residual_risk"
  ],
  "threat_event": [
    "threat_actor_ref",
    "event_time",
    "likelihood_scale",
    "evidence"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "asset": {
    "meaning": "风险资产引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "threat": {
    "meaning": "威胁主体或事件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "vulnerability": {
    "meaning": "可被利用的脆弱性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "likelihood": {
    "meaning": "已声明尺度下的事件可能性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "impact": {
    "meaning": "业务影响及其依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "treatment": {
    "meaning": "选定风险处置及理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "residual_risk": {
    "meaning": "处置后的剩余风险及评价依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `causes_loss` | threat_event,vulnerability → loss_event | 有证据或待验证的损失因果 |
| `derived_from` | security_requirement,requirement → business_attribute,control_objective,goal,legal_requirement | 要求由业务属性或目标导出 |
| `exploits` | threat_event,threat_actor → vulnerability | 威胁利用脆弱性 |
| `impacts_asset` | loss_event,risk → risk_asset | 损失或风险影响资产 |
| `implements_control` | sbb,application,technology,process → control | 实现控制措施 |
| `requires_control` | control_objective,security_requirement → control | 要求由控制措施实现 |
| `risk_has_control` | risk,risk_register_entry → control | 风险关联候选或已实施控制 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 识别资产与失败场景
2. 关联威胁脆弱性和损失
3. 按声明方法评估
4. 比较风险偏好
5. 记录处置和剩余风险

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 业务风险模型和风险登记册是同一工作产品的表达，不重复计数
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 业务风险模型和风险登记册是同一工作产品的表达，不重复计数


## 视图和交付物

- [业务风险模型／风险登记册](../profiles/business-risk-register-default.md)
- [风险与安全追溯模型](../profiles/risk-security-traceability.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务风险模型／风险登记册」给出：业务风险模型和风险登记册是同一工作产品的表达，不重复计数",
    "expected": "duplicate-id",
    "why": "业务风险模型和风险登记册是同一工作产品的表达，不重复计数"
  },
  "modification_example": {
    "change": "在「业务风险模型／风险登记册」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "business-risk-register-default-record",
      "type": "risk",
      "name": "业务风险模型／风险登记册：订单范围记录",
      "attributes": {
        "asset": "客户订单信息",
        "threat": "未授权访问导致订单被修改",
        "vulnerability": "管理访问缺少独立复核",
        "likelihood": "可能（本例假设）",
        "impact": "高峰时段无法履约，影响当日发运承诺",
        "owner": "虚构业务负责人",
        "treatment": "采用多因素认证与高权限操作复核",
        "residual_risk": "需在控制验证后复评，当前未知"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-risk-register-default",
    "artifact_id": "business-risk-register",
    "profile_id": "business-risk-register-default",
    "title": "业务风险模型／风险登记册／虚构案例",
    "entity_ids": [
      "business-risk-register-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-risk-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
