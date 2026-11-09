# 企业框架接触与承诺目录

ID：`enterprise-framework-alignment-catalog`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §7.1–7.2、§10.1、§13.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

EA应融入哪些已在使用的框架，在哪些接触点补位？

- 授权业务利益相关者
- 架构师
- 相关SME与实施负责人
- EA应融入哪些已在使用的框架，在哪些接触点补位？
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

对象类型：guide:framework_touchpoint。

```json
{
  "guide:framework_touchpoint": [
    "framework",
    "focus",
    "commitment_evidence",
    "actual_commitment",
    "owner",
    "touchpoint",
    "ea_input",
    "ea_output",
    "gap",
    "action"
  ]
}
```

{
  "name": {
    "meaning": "接触点名称",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "framework": {
    "meaning": "框架/企业既有方法及版本",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "focus": {
    "meaning": "规划、执行、治理等关注领域",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "commitment_evidence": {
    "meaning": "实际使用记录而非口头声明",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "actual_commitment": {
    "meaning": "证据支持的采用情况，不使用无依据分数",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "owner": {
    "meaning": "流程负责人",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "touchpoint": {
    "meaning": "双向接触事件及时点",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "ea_input": {
    "meaning": "EA消费的信息",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "ea_output": {
    "meaning": "EA交付的信息",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "gap": {
    "meaning": "重叠/缺口",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "action": {
    "meaning": "融入或补位动作",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 识别企业实际规划/执行/治理方法、版本与负责人
2. 查批准、资源和连续使用记录区分口头承诺
3. 按成果与信息交接映射接触点
4. 识别已有成果复用、重叠和缺口
5. 协商责任/时点/格式并更新EA路线

## 输出、检查与误读

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

- 不把框架目录当企业已采用清单
- 承诺深度由证据叙述，不凭空创建评分
- 框架重叠不表示包含或优先级，优先级须组织规则

- 不把框架目录当企业已采用清单
- 承诺深度由证据叙述，不凭空创建评分
- 框架重叠不表示包含或优先级，优先级须组织规则


## 视图和交付物

- [企业框架接触与承诺目录](../profiles/enterprise-framework-alignment-catalog-default.md)

- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [organization-model](../deliverables/organization-model.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "因框架知名就标企业已采用",
    "expected": "reject-unsupported-commitment"
  },
  "modification_example": {
    "change": "风险部门新增正式架构风险字段与月度回执",
    "expected": "缺口关闭为已建立接触点，附使用证据；不改变COBIT未知状态"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/enterprise-framework-alignment-catalog.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-enterprise-framework-alignment-catalog-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：frameworks",
      "locator": "examples/addenda/governance/raw-business-materials.json#frameworks"
    }
  ],
  "entities": [
    {
      "id": "enterprise-framework-alignment-catalog-default-1",
      "type": "guide:framework_touchpoint",
      "name": "项目拨款关卡",
      "attributes": {
        "framework": "企业PMO项目管理规程2026",
        "focus": "规划与执行",
        "commitment_evidence": "FW-01最近三次关卡记录",
        "actual_commitment": "已在使用，证据为本虚构案例",
        "owner": "PMO负责人",
        "touchpoint": "章程批准前／月度例外会",
        "ea_input": "范围、预算、资源与已知依赖",
        "ea_output": "架构契约、工作包依赖及例外影响",
        "gap": "关卡尚未引用具体view_id",
        "action": "融入：在章程模板新增架构契约和视图版本引用"
      },
      "evidence": [
        "src-enterprise-framework-alignment-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "enterprise-framework-alignment-catalog-default-2",
      "type": "guide:framework_touchpoint",
      "name": "风险季审",
      "attributes": {
        "framework": "企业ERM风险制度2026",
        "focus": "治理与风险",
        "commitment_evidence": "FW-02季度风险复核记录",
        "actual_commitment": "已在使用",
        "owner": "风险负责人",
        "touchpoint": "候选目标、路线批准前及季度复评",
        "ea_input": "风险偏好、风险登记、影响分析",
        "ea_output": "架构风险、控制与价值不确定性",
        "gap": "尚无架构风险移交字段",
        "action": "补位：定义风险ID、架构状态、控制责任和回执，再由风险部承接"
      },
      "evidence": [
        "src-enterprise-framework-alignment-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "enterprise-framework-alignment-catalog-default-3",
      "type": "guide:framework_touchpoint",
      "name": "COBIT采用声明",
      "attributes": {
        "framework": "COBIT，版本待核实",
        "focus": "信息系统治理",
        "commitment_evidence": "FW-03只有口头名称",
        "actual_commitment": "声明但无实质承诺证据",
        "owner": "未任命",
        "touchpoint": "未建立",
        "ea_input": "待获取采用范围/版本/负责人",
        "ea_output": "待确认对齐需求",
        "gap": "无法证明实际采用",
        "action": "先核实；不得把参考框架名当已存在治理能力"
      },
      "evidence": [
        "src-enterprise-framework-alignment-catalog-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-enterprise-framework-alignment-catalog-default",
    "artifact_id": "enterprise-framework-alignment-catalog",
    "profile_id": "enterprise-framework-alignment-catalog-default",
    "title": "企业框架接触与承诺目录",
    "entity_ids": [
      "enterprise-framework-alignment-catalog-default-1",
      "enterprise-framework-alignment-catalog-default-2",
      "enterprise-framework-alignment-catalog-default-3"
    ],
    "relationship_ids": [],
    "analysis": "FW-01/02已有实际流程，EA分别融入拨款和补齐风险移交；FW-03只有术语承诺，保留未知而不赋成熟度分。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "frameworks"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact enterprise-framework-alignment-catalog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
