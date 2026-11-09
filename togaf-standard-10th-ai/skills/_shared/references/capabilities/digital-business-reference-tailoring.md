# 数字业务参考模型裁剪

ID：`digital-business-reference-tailoring`。主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H §2–6；G21H §1.2、§1.4、§3；G21H 表5-1；G21H 表6-1；G21H 表6-2；G21H 表6-3；G21H §4.2.2、§4.5.2–4.5.3 表4-1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些数字业务功能适用于目标企业？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些数字业务功能适用于目标企业？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- reference_domain
- function
- local_mapping

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：dbrm_domain, dbrm_element, digital_business_function, guide:dbrm_applicability, guide:dbrm_mapping_row, guide:competency_overlay。

```json
{
  "dbrm_domain": [
    "definition"
  ],
  "dbrm_element": [
    "definition",
    "local_mapping",
    "applicability"
  ],
  "guide:dbrm_applicability": [
    "dbrm_domain_id",
    "dbrm_domain",
    "element_id",
    "element",
    "reference_identity",
    "local_mapping",
    "local_evidence",
    "applicability",
    "gap",
    "tailoring_reason",
    "relationship_boundary"
  ],
  "guide:dbrm_mapping_row": [
    "source_table",
    "source_row_id",
    "raw_cells",
    "resolved_cells",
    "source_mapping_status",
    "local_object_ids",
    "local_mapping_status",
    "local_evidence",
    "tailoring_reason",
    "review_action",
    "reference_identity"
  ],
  "guide:competency_overlay": [
    "source_row_id",
    "pillar",
    "competency",
    "dpbok_context",
    "context_kind",
    "local_roles",
    "current_evidence",
    "needed_competency",
    "gap",
    "action",
    "next_review",
    "reference_identity"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "reference_domain": {
    "meaning": "参考模型域",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "function": {
    "meaning": "参考功能或实际功能映射",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "local_mapping": {
    "meaning": "参考概念与本地概念的映射",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "gap": {
    "meaning": "基线目标之间的差距引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decision": {
    "meaning": "决策结果、理由和状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "applicability": {
    "meaning": "适用性判据与判断理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `contains` | dbrm_domain,platform → dbrm_element,technology | 明确类型约束的包含：平台含技术；DBRM参考域含核心要素。包含不是授权或组织汇报。 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 明确企业目的与参考域
2. 映射现有目标能力
3. 记录缺口与不适用
4. 连接战略分段能力全景

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 参考模型裁剪不表示全量采用，也不等于最终技术架构
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 参考模型裁剪不表示全量采用，也不等于最终技术架构


## 视图和交付物

- [数字业务参考模型裁剪](../profiles/digital-business-reference-tailoring-default.md)
- [DBRM四域十要素适用性](../profiles/dbrm-element-applicability.md)
- [DBRM与数字架构视角](../profiles/dbrm-digital-perspective-map.md)
- [DBRM与ADM及内容框架](../profiles/dbrm-adm-content-map.md)
- [DBRM与元模型及架构域](../profiles/dbrm-content-domain-map.md)
- [DBRM与全景层级](../profiles/dbrm-landscape-map.md)
- [五支柱十二胜任力与本地责任](../profiles/digital-enablement-competency-overlay.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「数字业务参考模型裁剪」给出：参考模型裁剪不表示全量采用，也不等于最终技术架构",
    "expected": "missing-evidence",
    "why": "参考模型裁剪不表示全量采用，也不等于最终技术架构"
  },
  "modification_example": {
    "change": "在「数字业务参考模型裁剪」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "digital-business-reference-tailoring-default-domain0",
      "type": "dbrm_domain",
      "name": "数字域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "数字"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element00",
      "type": "dbrm_element",
      "name": "客户聚焦",
      "attributes": {
        "definition": "DBRM十核心要素之一：客户聚焦",
        "local_mapping": "本例在线履约需补充客户聚焦的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "数字",
        "parent_id": "digital-business-reference-tailoring-default-domain0"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element01",
      "type": "dbrm_element",
      "name": "数字企业",
      "attributes": {
        "definition": "DBRM十核心要素之一：数字企业",
        "local_mapping": "本例在线履约需补充数字企业的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "数字",
        "parent_id": "digital-business-reference-tailoring-default-domain0"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-domain1",
      "type": "dbrm_domain",
      "name": "战略域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "战略"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element10",
      "type": "dbrm_element",
      "name": "战略语境",
      "attributes": {
        "definition": "DBRM十核心要素之一：战略语境",
        "local_mapping": "本例在线履约需补充战略语境的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "战略",
        "parent_id": "digital-business-reference-tailoring-default-domain1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element11",
      "type": "dbrm_element",
      "name": "业务动机",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务动机",
        "local_mapping": "本例在线履约需补充业务动机的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "战略",
        "parent_id": "digital-business-reference-tailoring-default-domain1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element12",
      "type": "dbrm_element",
      "name": "业务服务与产品",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务服务与产品",
        "local_mapping": "本例在线履约需补充业务服务与产品的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "战略",
        "parent_id": "digital-business-reference-tailoring-default-domain1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-domain2",
      "type": "dbrm_domain",
      "name": "结构域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "结构"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element20",
      "type": "dbrm_element",
      "name": "生态与业务模型",
      "attributes": {
        "definition": "DBRM十核心要素之一：生态与业务模型",
        "local_mapping": "本例在线履约需补充生态与业务模型的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "结构",
        "parent_id": "digital-business-reference-tailoring-default-domain2"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element21",
      "type": "dbrm_element",
      "name": "运营模式",
      "attributes": {
        "definition": "DBRM十核心要素之一：运营模式",
        "local_mapping": "本例在线履约需补充运营模式的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "结构",
        "parent_id": "digital-business-reference-tailoring-default-domain2"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element22",
      "type": "dbrm_element",
      "name": "业务能力模型",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务能力模型",
        "local_mapping": "本例在线履约需补充业务能力模型的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "结构",
        "parent_id": "digital-business-reference-tailoring-default-domain2"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-domain3",
      "type": "dbrm_domain",
      "name": "运营域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "运营"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element30",
      "type": "dbrm_element",
      "name": "业务运营环境",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务运营环境",
        "local_mapping": "本例在线履约需补充业务运营环境的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "运营",
        "parent_id": "digital-business-reference-tailoring-default-domain3"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element31",
      "type": "dbrm_element",
      "name": "数字使能",
      "attributes": {
        "definition": "DBRM十核心要素之一：数字使能",
        "local_mapping": "本例在线履约需补充数字使能的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "运营",
        "parent_id": "digital-business-reference-tailoring-default-domain3"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "digital-business-reference-tailoring-default-contains00",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain0",
      "target": "digital-business-reference-tailoring-default-element00",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains01",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain0",
      "target": "digital-business-reference-tailoring-default-element01",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains10",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain1",
      "target": "digital-business-reference-tailoring-default-element10",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains11",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain1",
      "target": "digital-business-reference-tailoring-default-element11",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains12",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain1",
      "target": "digital-business-reference-tailoring-default-element12",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains20",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain2",
      "target": "digital-business-reference-tailoring-default-element20",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains21",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain2",
      "target": "digital-business-reference-tailoring-default-element21",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains22",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain2",
      "target": "digital-business-reference-tailoring-default-element22",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains30",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain3",
      "target": "digital-business-reference-tailoring-default-element30",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains31",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain3",
      "target": "digital-business-reference-tailoring-default-element31",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-digital-business-reference-tailoring-default",
    "artifact_id": "digital-business-reference-tailoring",
    "profile_id": "digital-business-reference-tailoring-default",
    "title": "数字业务参考模型裁剪／虚构案例",
    "entity_ids": [
      "digital-business-reference-tailoring-default-domain0",
      "digital-business-reference-tailoring-default-element00",
      "digital-business-reference-tailoring-default-element01",
      "digital-business-reference-tailoring-default-domain1",
      "digital-business-reference-tailoring-default-element10",
      "digital-business-reference-tailoring-default-element11",
      "digital-business-reference-tailoring-default-element12",
      "digital-business-reference-tailoring-default-domain2",
      "digital-business-reference-tailoring-default-element20",
      "digital-business-reference-tailoring-default-element21",
      "digital-business-reference-tailoring-default-element22",
      "digital-business-reference-tailoring-default-domain3",
      "digital-business-reference-tailoring-default-element30",
      "digital-business-reference-tailoring-default-element31"
    ],
    "relationship_ids": [
      "digital-business-reference-tailoring-default-contains00",
      "digital-business-reference-tailoring-default-contains01",
      "digital-business-reference-tailoring-default-contains10",
      "digital-business-reference-tailoring-default-contains11",
      "digital-business-reference-tailoring-default-contains12",
      "digital-business-reference-tailoring-default-contains20",
      "digital-business-reference-tailoring-default-contains21",
      "digital-business-reference-tailoring-default-contains22",
      "digital-business-reference-tailoring-default-contains30",
      "digital-business-reference-tailoring-default-contains31"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact digital-business-reference-tailoring --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
