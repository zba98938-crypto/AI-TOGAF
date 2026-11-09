# 架构成熟度模型

`profile_id`: architecture-maturity-model-default；`artifact_id`: architecture-maturity-model；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G203 §2.1–2.3。

## 构图与定义状态

表示族：`matrix`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：criterion, maturity_element。关系类型：traces_to。

```json
{
  "entities": {},
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-maturity-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-maturity-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
