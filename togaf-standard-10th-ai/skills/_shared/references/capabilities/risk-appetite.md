# 风险偏好

ID：`risk-appetite`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.1.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

承担多大风险才能实现业务结果？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 承担多大风险才能实现业务结果？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- scope
- impact_scale
- likelihood_scale

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：risk_appetite。

```json
{
  "risk_appetite": [
    "scope",
    "impact_scale",
    "likelihood_scale",
    "acceptance_boundary",
    "approval_authority"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "impact_scale": {
    "meaning": "影响评价尺度及锚点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "likelihood_scale": {
    "meaning": "可能性评价尺度及锚点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "acceptance_boundary": {
    "meaning": "风险可接受范围及超限判据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "approval_authority": {
    "meaning": "拥有批准权限的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 界定风险范围和风险所有者
2. 记录影响与可能性尺度
3. 定义可接受边界及超限处置
4. 用真实业务场景检验边界

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 风险偏好不是一条任意高低分线，批准状态需要证据
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 风险偏好不是一条任意高低分线，批准状态需要证据


## 视图和交付物

- [风险偏好](../profiles/risk-appetite-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「风险偏好」给出：风险偏好不是一条任意高低分线，批准状态需要证据",
    "expected": "approval-without-evidence",
    "why": "风险偏好不是一条任意高低分线，批准状态需要证据"
  },
  "modification_example": {
    "change": "在「风险偏好」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "risk-appetite-default-record",
      "type": "risk_appetite",
      "name": "风险偏好：订单范围记录",
      "attributes": {
        "scope": "虚构星河零售：在线下单至仓库发运",
        "impact_scale": "低／中／高，按履约中断与合同影响判断",
        "likelihood_scale": "罕见／可能／频繁，需事故与测试证据支持",
        "acceptance_boundary": "不接受无责任归属且无恢复方案的高履约影响风险",
        "approval_authority": "虚构风险委员会，当前未批准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-risk-appetite-default",
    "artifact_id": "risk-appetite",
    "profile_id": "risk-appetite-default",
    "title": "风险偏好／虚构案例",
    "entity_ids": [
      "risk-appetite-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact risk-appetite --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
