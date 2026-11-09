# 可持续性架构评审画布

ID：`sustainability-review-canvas`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G242 §3.8–3.9；图3-14。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

方案的环境贡献与措施是否一致？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 方案的环境贡献与措施是否一致？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_contribution
- year
- scope

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：sustainability_action。

```json
{
  "sustainability_action": [
    "business_contribution",
    "year",
    "scope",
    "increase",
    "decrease",
    "net",
    "selection",
    "rationale"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_contribution": {
    "meaning": "业务对环境目标的贡献类型",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "year": {
    "meaning": "环境核算年度",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "increase": {
    "meaning": "新增环境影响",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decrease": {
    "meaning": "退役或减少的环境影响",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "net": {
    "meaning": "同一边界下的净影响",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "selection": {
    "meaning": "措施或选项的选择状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rationale": {
    "meaning": "分析或选择的理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 说明三类业务环境贡献
2. 分别记录新增退役净值
3. 评价措施与选择理由
4. 核对印刷或计算差异

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 图3-14存在数值疑点，应保留来源值与差异，不能强行消解
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 图3-14存在数值疑点，应保留来源值与差异，不能强行消解


## 视图和交付物

- [可持续性架构评审画布](../profiles/sustainability-review-canvas-default.md)
- [环境架构评审画布](../profiles/sustainability-architecture-canvas.md)

- [compliance-assessment](../deliverables/compliance-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「可持续性架构评审画布」给出：图3-14存在数值疑点，应保留来源值与差异，不能强行消解",
    "expected": "missing-evidence",
    "why": "图3-14存在数值疑点，应保留来源值与差异，不能强行消解"
  },
  "modification_example": {
    "change": "在「可持续性架构评审画布」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "sustainability-review-canvas-default-0",
      "type": "sustainability_action",
      "name": "支持测量业务环境影响",
      "attributes": {
        "business_contribution": "支持测量业务环境影响",
        "year": 2026,
        "scope": "Scope 2，单一服务运营电力",
        "increase": 69,
        "decrease": 460,
        "net": -391,
        "selection": "候选；未批准",
        "rationale": "同边界比较新增与退役，印刷差异单独保存",
        "block": "业务贡献",
        "reported_net": -390
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-review-canvas-default-1",
      "type": "sustainability_action",
      "name": "核算使用阶段电力影响",
      "attributes": {
        "business_contribution": "核算使用阶段电力影响",
        "year": 2026,
        "scope": "Scope 2，单一服务运营电力",
        "increase": 69,
        "decrease": 460,
        "net": -391,
        "selection": "候选；未批准",
        "rationale": "同边界比较新增与退役，印刷差异单独保存",
        "block": "环境核算",
        "reported_net": -390
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-review-canvas-default-2",
      "type": "sustainability_action",
      "name": "减少重复报表任务",
      "attributes": {
        "business_contribution": "减少重复报表任务",
        "year": 2026,
        "scope": "Scope 2，单一服务运营电力",
        "increase": 69,
        "decrease": 460,
        "net": -391,
        "selection": "候选；未批准",
        "rationale": "同边界比较新增与退役，印刷差异单独保存",
        "block": "架构措施",
        "reported_net": -390
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-sustainability-review-canvas-default",
    "artifact_id": "sustainability-review-canvas",
    "profile_id": "sustainability-review-canvas-default",
    "title": "可持续性架构评审画布／虚构案例",
    "entity_ids": [
      "sustainability-review-canvas-default-0",
      "sustainability-review-canvas-default-1",
      "sustainability-review-canvas-default-2"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact sustainability-review-canvas --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
