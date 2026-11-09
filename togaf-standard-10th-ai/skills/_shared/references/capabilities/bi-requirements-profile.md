# BI 与分析需求规格

ID：`bi-requirements-profile`。主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G238 §4；G238 §4.4（特别是本地补写示例说明）；G238 §3.1阶段B、表4-1、表4-2；G238 §2.2、表4-2；G238 §2.3、表4-3、§4.4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

分析平台需要满足什么可验证业务要求？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 分析平台需要满足什么可验证业务要求？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_function
- statement
- verification

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：analytics_requirement, guide:bi_requirement_provenance, ops:bi_usage, ops:functional_coverage。

```json
{
  "analytics_requirement": [
    "business_function",
    "statement",
    "verification",
    "priority",
    "source",
    "constraint"
  ],
  "guide:bi_requirement_provenance": [
    "statement",
    "function",
    "requirement_origin",
    "origin_locator",
    "official_requirement_id",
    "verification",
    "completeness_claim",
    "validation_criteria",
    "companion_sheet"
  ],
  "ops:bi_usage": [
    "user",
    "pain",
    "decision",
    "business_objects",
    "sponsor",
    "goal_reference",
    "metric",
    "priority_rationale",
    "priority_rule",
    "lifecycle",
    "data_access",
    "evidence_detail",
    "gap"
  ],
  "ops:functional_coverage": [
    "reference_id",
    "reference_kind",
    "reference_name",
    "reference_definition",
    "reference_group",
    "reference_level",
    "reference_scope",
    "source_locator",
    "reference_identity",
    "project_scope",
    "coverage_status",
    "implementation_ref",
    "evidence_detail",
    "gap_action",
    "source_uncertainty"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_function": {
    "meaning": "业务功能引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "statement": {
    "meaning": "原子陈述或问题",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "verification": {
    "meaning": "验证方法与验收证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "priority": {
    "meaning": "优先级及排序依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "source": {
    "meaning": "该条内容的输入来源",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "constraint": {
    "meaning": "适用约束",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从业务功能识别需求
2. 拆成原子独立陈述
3. 定义验证方式
4. 分离产品约束与业务要求
5. 记录来源身份再提炼需求
6. 按功能解释系统，检查原子/唯一/可验证
7. 区分项目需求和本地示例与官方配套记录
8. 未找到电子表格时只交付局部候选与缺口
9. 从用户痛点提炼决策及业务对象
10. 连接参考目标，但另设有来源的项目度量
11. 让赞助人提供价值/复杂性排序规则并保留理由
12. 定义从设计到持续维护的责任
13. 检查测量结果和目标/方向不同
14. 加载随技能携带的完整源表，保留参考分组/ID/出处
15. 限定项目范围和时点，逐项寻找组织活动或实际应用功能证据
16. 区分已见、计划、未知和有理由不适用
17. 不得以宏观组或产品名称推断子项覆盖
18. 对缺口形成具体补证/实现/复评行动，不合成成熟度分数

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 未取得外部完整需求电子表格时不能声称覆盖其全部条目
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 未取得外部完整需求电子表格时不能声称覆盖其全部条目


## 视图和交付物

- [BI 与分析需求规格](../profiles/bi-requirements-profile-default.md)
- [BI架构需求及来源边界](../profiles/bi-requirement-origin-boundary.md)
- [BI用途待办、目标与可追溯度量](../profiles/bi-usage-goal-measures.md)
- [BI业务功能参考覆盖](../profiles/bi-business-function-coverage.md)
- [BI应用功能参考覆盖](../profiles/bi-application-function-coverage.md)

- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「BI 与分析需求规格」给出：未取得外部完整需求电子表格时不能声称覆盖其全部条目",
    "expected": "core-vocabulary-override",
    "why": "未取得外部完整需求电子表格时不能声称覆盖其全部条目"
  },
  "modification_example": {
    "change": "在「BI 与分析需求规格」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "bi-requirements-profile-default-record",
      "type": "analytics_requirement",
      "name": "BI 与分析需求规格：订单范围记录",
      "attributes": {
        "business_function": "订单履约分析",
        "statement": "业务负责人明确承担数字采用的问责",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
        "priority": "高：支撑当前履约决策",
        "source": "虚构业务场景与需求材料",
        "constraint": "虚构订单案例中需验证的适用约束"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-bi-requirements-profile-default",
    "artifact_id": "bi-requirements-profile",
    "profile_id": "bi-requirements-profile-default",
    "title": "BI 与分析需求规格／虚构案例",
    "entity_ids": [
      "bi-requirements-profile-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact bi-requirements-profile --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
