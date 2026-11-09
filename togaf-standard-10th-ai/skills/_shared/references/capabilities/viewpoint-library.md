# 视角库

ID：`viewpoint-library`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G184 §8.2–8.4；G186 §6.3.1、§9.1.3、附录C表C-1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

为完整利益相关者关注点选择哪些可复用构图规范？

- 授权业务利益相关者
- 架构师
- 相关SME与实施负责人
- 为完整利益相关者关注点选择哪些可复用构图规范？
- 依据完整、同口径、责任和未决项清晰


## 输入及缺口处理

必需：

- 范围和五维语境
- 原始访谈/计划/测量及定位
- 授权角色和适用目标版本

可选：

- 既有模型、视图、参考规范和组织规则

逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。

## 元素、属性与关系

对象类型：guide:viewpoint。

```json
{
  "guide:viewpoint": [
    "concern",
    "stakeholders",
    "decision",
    "construction",
    "required_information",
    "source_models",
    "view_ids",
    "gaps",
    "selection_reason"
  ]
}
```

{
  "name": {
    "meaning": "视角名",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "concern": {
    "meaning": "标准关注点",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "stakeholders": {
    "meaning": "拥有架构决策权的利益相关者",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision": {
    "meaning": "待支持的业务决定",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "construction": {
    "meaning": "可重复构造视图的方法和筛选规则",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "required_information": {
    "meaning": "必需对象、关系、属性、单位等",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "source_models": {
    "meaning": "模型/版本引用",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "view_ids": {
    "meaning": "实际视图实例ID；视角不是视图",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "gaps": {
    "meaning": "缺信息及其影响",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "selection_reason": {
    "meaning": "为何覆盖这组关注点",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 从业务原话区分关注点、决策与角色
2. 明确每组问题需要哪些信息并查模型缺口
3. 定义构造规则、筛选范围与状态
4. 关联profile_id和多个实际view_id，检查关注点覆盖
5. 缺信息单列，不以已有图名代替分析

## 输出、检查与误读

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

- 视角定义构造规范，view_id标识具体实例，两者不混同
- 每项授权关注点都有所需信息及构造规则
- 附录C是空白参考库，填入内容是项目分析而非原指南答案

- 视角定义构造规范，view_id标识具体实例，两者不混同
- 每项授权关注点都有所需信息及构造规则
- 附录C是空白参考库，填入内容是项目分析而非原指南答案


## 视图和交付物

- [云帆物流视角库](../profiles/viewpoint-library-default.md)

- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [architecture-repository](../deliverables/architecture-repository.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "只有图名“数据流图”，无关注点/所需信息",
    "expected": "missing-evidence",
    "why": "报告viewpoint-information-gap，不计完成视角",
    "original_expected_text": "报告viewpoint-information-gap，不计完成视角"
  },
  "modification_example": {
    "change": "新增客户负责人关注签收争议处理",
    "expected": "增加争议关注点、证据链信息和专门视角；旧三项不自动覆盖"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/viewpoint-library.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-viewpoint-library-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：viewpoints",
      "locator": "examples/addenda/governance/raw-business-materials.json#viewpoints"
    }
  ],
  "entities": [
    {
      "id": "viewpoint-library-default-1",
      "type": "guide:viewpoint",
      "name": "组合成本与价值",
      "attributes": {
        "concern": "价值、变更成本、信心",
        "stakeholders": [
          "财务负责人"
        ],
        "decision": "是否为T1拨款",
        "construction": "按工作包列三年成本和同单位月节省，单列区间与假设，不把成本直接当效用评分",
        "required_information": [
          "工作包/差距",
          "成本币种与期间",
          "工时单位、期间、范围",
          "不确定性来源"
        ],
        "source_models": [
          "model-budget-v2"
        ],
        "view_ids": [
          "v-budget-options-T1"
        ],
        "gaps": [
          "measure.uncertainty尚缺，不能形成确定投资结论"
        ],
        "selection_reason": "VP-01需要同口径预算比较"
      },
      "evidence": [
        "src-viewpoint-library-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "viewpoint-library-default-2",
      "type": "guide:viewpoint",
      "name": "过渡可运营",
      "attributes": {
        "concern": "可行性、可靠性、控制",
        "stakeholders": [
          "运营负责人"
        ],
        "decision": "T1是否可独立上线",
        "construction": "逐T1业务场景映射人员/流程/应用/数据、依赖和回退证据",
        "required_information": [
          "T1范围",
          "进入退出条件",
          "恢复/回退演练",
          "关键外部依赖"
        ],
        "source_models": [
          "model-transition-v2"
        ],
        "view_ids": [
          "v-operability-T1"
        ],
        "gaps": [],
        "selection_reason": "VP-02明确暂停T2仍须发运"
      },
      "evidence": [
        "src-viewpoint-library-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "viewpoint-library-default-3",
      "type": "guide:viewpoint",
      "name": "签收信息用途与控制",
      "attributes": {
        "concern": "安全、控制、规格",
        "stakeholders": [
          "数据负责人"
        ],
        "decision": "签收信息用途是否被控制",
        "construction": "按信息用途关联使用服务、约束、控制和验证证据；使用/修改分别标明",
        "required_information": [
          "information.purpose",
          "uses/modifies",
          "control.test_evidence"
        ],
        "source_models": [
          "model-data-v2"
        ],
        "view_ids": [
          "v-data-purpose-T1"
        ],
        "gaps": [],
        "selection_reason": "VP-03要求可追溯使用范围"
      },
      "evidence": [
        "src-viewpoint-library-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-viewpoint-library-default",
    "artifact_id": "viewpoint-library",
    "profile_id": "viewpoint-library-default",
    "title": "云帆物流视角库",
    "entity_ids": [
      "viewpoint-library-default-1",
      "viewpoint-library-default-2",
      "viewpoint-library-default-3"
    ],
    "relationship_ids": [],
    "analysis": "从VP-01/02/03提取三组决策与关注点，复用成本/过渡/信息模型；成本缺少不确定性资料，预算视图只能作为待补草稿。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "viewpoints"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact viewpoint-library --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
