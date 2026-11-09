# 微服务技术指南

ID：`microservice-technical-guidance`。主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G21I §6–7；G21I §5.2、§5.5、表5-1；G21I §5.3、表5-1、§12.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些技术约束保障微服务实现？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些技术约束保障微服务实现？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- concern
- standard
- rationale

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：microservice_guideline, ops:msa_readiness, ops:msa_governance。

```json
{
  "microservice_guideline": [
    "concern",
    "standard",
    "rationale",
    "applicability",
    "verification",
    "exception"
  ],
  "ops:msa_readiness": [
    "concern",
    "observation",
    "judgment",
    "owner",
    "action",
    "scope",
    "decision_consequence",
    "scoring",
    "evidence_detail"
  ],
  "ops:msa_governance": [
    "authority",
    "roles",
    "decision",
    "decision_status",
    "waiver",
    "controls",
    "feedback",
    "scope",
    "mapping_origin",
    "evidence_detail"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "concern": {
    "meaning": "利益相关者的具体关注点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "standard": {
    "meaning": "适用标准和版本",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rationale": {
    "meaning": "分析或选择的理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "applicability": {
    "meaning": "适用性判据与判断理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "verification": {
    "meaning": "验证方法与验收证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "exception": {
    "meaning": "例外及其治理方式",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `ops:governance_supports` | ops:msa_governance → ops:msa_governance | MSA控制支持IT服务治理；项目明确方向；不声明原图箭头已核实 |
| `ops:governance_aligns` | ops:msa_governance → ops:msa_governance | MSA决策对齐EA政策；项目明确方向；不声明原图箭头已核实 |
| `ops:governance_extends` | ops:msa_governance → ops:msa_governance | MSA增加频繁发布的过程细节；项目明确方向；不声明原图箭头已核实 |
| `ops:governance_constrains` | ops:msa_governance → ops:msa_governance | 企业架构约束团队自治；项目明确方向；不声明原图箭头已核实 |

## 分析步骤

1. 从目标质量选择指南
2. 定义接口运行与治理约束
3. 说明适用与例外
4. 关联合规验证
5. 按单服务全过程检查归属、技能、自治、DevOps与试点学习
6. 分别记录已知、部分和未知，不按条数计成熟度
7. 将每个不足转为责任、行动和进入试点条件
8. OSIMM按独立来源调用，不用ACMM或项目表替代
9. 界定企业护栏和MSA专属决定两条轨道
10. 区分五类角色职责与请求/决定权限
11. 核对每次发布控制和持续反馈
12. 偏离需显式申请并以委员会决定为准
13. 支持/对齐/扩展/约束分别记录方向

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 外部实践补充必须标项目约定，不能冒充指南原文
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 外部实践补充必须标项目约定，不能冒充指南原文


## 视图和交付物

- [微服务技术指南](../profiles/microservice-technical-guidance-default.md)
- [MSA组织与生命周期就绪证据](../profiles/msa-readiness-evidence.md)
- [MSA双轨治理与豁免过程](../profiles/msa-federated-governance-process.md)
- [MSA双轨治理与豁免过程／图形](../profiles/msa-federated-governance-diagram.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「微服务技术指南」给出：外部实践补充必须标项目约定，不能冒充指南原文",
    "expected": "missing-evidence",
    "why": "外部实践补充必须标项目约定，不能冒充指南原文"
  },
  "modification_example": {
    "change": "在「微服务技术指南」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "microservice-technical-guidance-default-record",
      "type": "microservice_guideline",
      "name": "微服务技术指南：订单范围记录",
      "attributes": {
        "concern": "订单完整性与履约连续性",
        "standard": "项目选定标准及版本待核实",
        "rationale": "满足履约连续性与可追溯要求",
        "applicability": "本例订单功能处理客户联系信息",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
        "exception": "虚构订单案例中需验证的例外及其治理方式"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-microservice-technical-guidance-default",
    "artifact_id": "microservice-technical-guidance",
    "profile_id": "microservice-technical-guidance-default",
    "title": "微服务技术指南／虚构案例",
    "entity_ids": [
      "microservice-technical-guidance-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact microservice-technical-guidance --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
