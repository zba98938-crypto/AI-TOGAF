# 架构成熟度模型

ID：`architecture-maturity-model`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G203 §2.1–2.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

用什么可解释标准评价 EA 能力？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 用什么可解释标准评价 EA 能力？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- element
- level
- description

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：criterion, maturity_criterion, maturity_element。

```json
{}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "element": {
    "meaning": "成熟度要素",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "level": {
    "meaning": "所用模型下的层级",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "description": {
    "meaning": "级别或特征的描述",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence_rule": {
    "meaning": "判断达成所需的证据规则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "weight": {
    "meaning": "明确声明的聚合权重",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 声明选定模型和适用范围
2. 定义要素与级别特征
3. 规定证据及权重
4. 校准评审者理解

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级


## 视图和交付物

- [架构成熟度模型](../profiles/architecture-maturity-model-default.md)
- [ACMM 要素级别矩阵](../profiles/acmm-elements-levels.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构成熟度模型」给出：ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级",
    "expected": "missing-evidence",
    "why": "ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级"
  },
  "modification_example": {
    "change": "在「架构成熟度模型」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "architecture-maturity-model-default-level0",
      "type": "criterion",
      "name": "ACMM 0级",
      "attributes": {
        "level": 0,
        "definition": "无"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-level1",
      "type": "criterion",
      "name": "ACMM 1级",
      "attributes": {
        "level": 1,
        "definition": "初始"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-level2",
      "type": "criterion",
      "name": "ACMM 2级",
      "attributes": {
        "level": 2,
        "definition": "开发中"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-level3",
      "type": "criterion",
      "name": "ACMM 3级",
      "attributes": {
        "level": 3,
        "definition": "已定义"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-level4",
      "type": "criterion",
      "name": "ACMM 4级",
      "attributes": {
        "level": 4,
        "definition": "已管理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-level5",
      "type": "criterion",
      "name": "ACMM 5级",
      "attributes": {
        "level": 5,
        "definition": "已度量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element0",
      "type": "maturity_element",
      "name": "架构流程",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element1",
      "type": "maturity_element",
      "name": "架构开发",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element2",
      "type": "maturity_element",
      "name": "业务关联",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element3",
      "type": "maturity_element",
      "name": "高层管理参与",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element4",
      "type": "maturity_element",
      "name": "运营单元参与",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element5",
      "type": "maturity_element",
      "name": "架构沟通",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element6",
      "type": "maturity_element",
      "name": "IT安全",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element7",
      "type": "maturity_element",
      "name": "架构治理",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-maturity-model-default-element8",
      "type": "maturity_element",
      "name": "投资与采购",
      "attributes": {
        "definition": "评价该要素的实际过程证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "architecture-maturity-model-default-cell0-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element0",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell0-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element0",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell0-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element0",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell0-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element0",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell0-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element0",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell0-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element0",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell1-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element1",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell1-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element1",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell1-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element1",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell1-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element1",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell1-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element1",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell1-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element1",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell2-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element2",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell2-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element2",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell2-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element2",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell2-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element2",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell2-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element2",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell2-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element2",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell3-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element3",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell3-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element3",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell3-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element3",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell3-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element3",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell3-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element3",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell3-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element3",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell4-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element4",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell4-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element4",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell4-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element4",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell4-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element4",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell4-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element4",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell4-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element4",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell5-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element5",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell5-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element5",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell5-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element5",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell5-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element5",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell5-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element5",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell5-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element5",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell6-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element6",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell6-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element6",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell6-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element6",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell6-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element6",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell6-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element6",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell6-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element6",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell7-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element7",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell7-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element7",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell7-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element7",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell7-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element7",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell7-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element7",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell7-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element7",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell8-0",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element8",
      "target": "architecture-maturity-model-default-level0",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell8-1",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element8",
      "target": "architecture-maturity-model-default-level1",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell8-2",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element8",
      "target": "architecture-maturity-model-default-level2",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell8-3",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element8",
      "target": "architecture-maturity-model-default-level3",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell8-4",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element8",
      "target": "architecture-maturity-model-default-level4",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    },
    {
      "id": "architecture-maturity-model-default-cell8-5",
      "type": "traces_to",
      "source": "architecture-maturity-model-default-element8",
      "target": "architecture-maturity-model-default-level5",
      "label": "按G203对应级别特征取证；本例未开展实测",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "evidence_rule": "须有制度、执行或改进证据"
      }
    }
  ],
  "view": {
    "id": "v-architecture-maturity-model-default",
    "artifact_id": "architecture-maturity-model",
    "profile_id": "architecture-maturity-model-default",
    "title": "架构成熟度模型／虚构案例",
    "entity_ids": [
      "architecture-maturity-model-default-level0",
      "architecture-maturity-model-default-level1",
      "architecture-maturity-model-default-level2",
      "architecture-maturity-model-default-level3",
      "architecture-maturity-model-default-level4",
      "architecture-maturity-model-default-level5",
      "architecture-maturity-model-default-element0",
      "architecture-maturity-model-default-element1",
      "architecture-maturity-model-default-element2",
      "architecture-maturity-model-default-element3",
      "architecture-maturity-model-default-element4",
      "architecture-maturity-model-default-element5",
      "architecture-maturity-model-default-element6",
      "architecture-maturity-model-default-element7",
      "architecture-maturity-model-default-element8"
    ],
    "relationship_ids": [
      "architecture-maturity-model-default-cell0-0",
      "architecture-maturity-model-default-cell0-1",
      "architecture-maturity-model-default-cell0-2",
      "architecture-maturity-model-default-cell0-3",
      "architecture-maturity-model-default-cell0-4",
      "architecture-maturity-model-default-cell0-5",
      "architecture-maturity-model-default-cell1-0",
      "architecture-maturity-model-default-cell1-1",
      "architecture-maturity-model-default-cell1-2",
      "architecture-maturity-model-default-cell1-3",
      "architecture-maturity-model-default-cell1-4",
      "architecture-maturity-model-default-cell1-5",
      "architecture-maturity-model-default-cell2-0",
      "architecture-maturity-model-default-cell2-1",
      "architecture-maturity-model-default-cell2-2",
      "architecture-maturity-model-default-cell2-3",
      "architecture-maturity-model-default-cell2-4",
      "architecture-maturity-model-default-cell2-5",
      "architecture-maturity-model-default-cell3-0",
      "architecture-maturity-model-default-cell3-1",
      "architecture-maturity-model-default-cell3-2",
      "architecture-maturity-model-default-cell3-3",
      "architecture-maturity-model-default-cell3-4",
      "architecture-maturity-model-default-cell3-5",
      "architecture-maturity-model-default-cell4-0",
      "architecture-maturity-model-default-cell4-1",
      "architecture-maturity-model-default-cell4-2",
      "architecture-maturity-model-default-cell4-3",
      "architecture-maturity-model-default-cell4-4",
      "architecture-maturity-model-default-cell4-5",
      "architecture-maturity-model-default-cell5-0",
      "architecture-maturity-model-default-cell5-1",
      "architecture-maturity-model-default-cell5-2",
      "architecture-maturity-model-default-cell5-3",
      "architecture-maturity-model-default-cell5-4",
      "architecture-maturity-model-default-cell5-5",
      "architecture-maturity-model-default-cell6-0",
      "architecture-maturity-model-default-cell6-1",
      "architecture-maturity-model-default-cell6-2",
      "architecture-maturity-model-default-cell6-3",
      "architecture-maturity-model-default-cell6-4",
      "architecture-maturity-model-default-cell6-5",
      "architecture-maturity-model-default-cell7-0",
      "architecture-maturity-model-default-cell7-1",
      "architecture-maturity-model-default-cell7-2",
      "architecture-maturity-model-default-cell7-3",
      "architecture-maturity-model-default-cell7-4",
      "architecture-maturity-model-default-cell7-5",
      "architecture-maturity-model-default-cell8-0",
      "architecture-maturity-model-default-cell8-1",
      "architecture-maturity-model-default-cell8-2",
      "architecture-maturity-model-default-cell8-3",
      "architecture-maturity-model-default-cell8-4",
      "architecture-maturity-model-default-cell8-5"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-maturity-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
