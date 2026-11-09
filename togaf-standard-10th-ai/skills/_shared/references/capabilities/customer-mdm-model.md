# 客户主数据模型

ID：`customer-mdm-model`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §4–5；G21B 附录A.1–A.2；G21B §4.4、§6.1.1–6.1.2；G21B §3、§5.2.2；G21B §5.2.1表5-3；G21B §5.2.2表5-4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

怎样形成可复用的客户主数据？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 怎样形成可复用的客户主数据？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_identity
- identifier
- source

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：master_data, guide:mdm_diagnostic_answer, guide:mdm_plateau, guide:mdm_match_case, ops:functional_coverage。

```json
{
  "master_data": [
    "business_identity",
    "identifier",
    "source",
    "matching",
    "ownership",
    "quality"
  ],
  "guide:mdm_diagnostic_answer": [
    "question_number",
    "question",
    "answer",
    "evidence_detail",
    "consequence",
    "action",
    "owner",
    "scope",
    "scoring"
  ],
  "guide:mdm_plateau": [
    "state_ref",
    "evolution_kind",
    "mastership",
    "golden_record",
    "CRUD_ownership",
    "propagation",
    "use_cases",
    "operating_gate",
    "next_trigger",
    "rollback",
    "scope",
    "source_mapping"
  ],
  "guide:mdm_match_case": [
    "rule",
    "record_refs",
    "key_comparison",
    "proposal",
    "matching_basis",
    "manual_arbitration",
    "decision_status",
    "merge_lineage",
    "unmerge_plan",
    "historical_policy"
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
  "business_identity": {
    "meaning": "业务身份定义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "identifier": {
    "meaning": "对象标识与唯一性规则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "source": {
    "meaning": "该条内容的输入来源",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "matching": {
    "meaning": "匹配与合并规则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "ownership": {
    "meaning": "数据所有权及责任",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "quality": {
    "meaning": "所需或观察到的数据质量",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 确定客户内核与业务语境
2. 分析源记录身份匹配
3. 定义质量和责任
4. 建立模型与分发关系
5. 保持十问题ID与原问题含义
6. 逐项取证，区分否定、未知、部分和不适用
7. 将缺口映射行动、责任、影响；不得按yes比例冒充成熟度
8. 识别当前主控和可用业务能力
9. 分开分析黄金记录与运营主控
10. 逐状态验证用例/质量/授权/恢复/支持条件
11. 选择演进触发，不强制固定四期
12. 区分业务键、技术键与姓名属性
13. 按给定规则提出候选，不直接自动合并
14. 人工判定并保留来源/版本/证据
15. 执行前验证可取消合并与历史语义
16. 加载随技能携带的完整源表，保留参考分组/ID/出处
17. 限定项目范围和时点，逐项寻找组织活动或实际应用功能证据
18. 区分已见、计划、未知和有理由不适用
19. 不得以宏观组或产品名称推断子项覆盖
20. 对缺口形成具体补证/实现/复评行动，不合成成熟度分数

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 统一客户标识不等于无条件合并不同业务语境
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 统一客户标识不等于无条件合并不同业务语境


## 视图和交付物

- [客户主数据模型](../profiles/customer-mdm-model-default.md)
- [C-MDM十问运营诊断](../profiles/mdm-operational-ten-questions.md)
- [C-MDM四平台态运营计划](../profiles/mdm-four-plateau-operations.md)
- [C-MDM匹配、合并与人工仲裁](../profiles/mdm-match-merge-arbitration.md)
- [C-MDM业务功能参考覆盖](../profiles/mdm-business-function-coverage.md)
- [C-MDM应用功能参考覆盖](../profiles/mdm-application-function-coverage.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「客户主数据模型」给出：统一客户标识不等于无条件合并不同业务语境",
    "expected": "missing-evidence",
    "why": "统一客户标识不等于无条件合并不同业务语境"
  },
  "modification_example": {
    "change": "在「客户主数据模型」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "customer-mdm-model-default-person",
      "type": "master_data",
      "name": "自然人客户内核",
      "attributes": {
        "business_identity": "在订单关系中承担购买主体的自然人",
        "identifier": "候选客户主标识",
        "source": "经核实的客户源记录",
        "matching": "标识冲突人工核验；不按姓名直接合并",
        "ownership": "客户数据所有者",
        "quality": "身份唯一且可追溯"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-mdm-model-default-org",
      "type": "master_data",
      "name": "组织客户内核",
      "attributes": {
        "business_identity": "作为法律主体形成采购关系的组织",
        "identifier": "候选组织主标识",
        "source": "企业客户源记录",
        "matching": "按核实组织标识匹配",
        "ownership": "企业客户数据所有者",
        "quality": "组织身份及联系责任明确"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "customer-mdm-model-default-related",
      "type": "traces_to",
      "source": "customer-mdm-model-default-person",
      "target": "customer-mdm-model-default-org",
      "label": "自然人可作为组织联系人；身份不自动合并",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-customer-mdm-model-default",
    "artifact_id": "customer-mdm-model",
    "profile_id": "customer-mdm-model-default",
    "title": "客户主数据模型／虚构案例",
    "entity_ids": [
      "customer-mdm-model-default-person",
      "customer-mdm-model-default-org"
    ],
    "relationship_ids": [
      "customer-mdm-model-default-related"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact customer-mdm-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
