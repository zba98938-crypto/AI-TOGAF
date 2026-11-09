# ACMM 要素级别矩阵

`profile_id`: acmm-elements-levels；`artifact_id`: architecture-maturity-model；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G203 §2.2–2.3。

## 构图与定义状态

表示族：`matrix`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": null,
  "layout_notes": "六级九要素示例，权重与达成规则显式",
  "review_status": "source-located-awaiting-template-validation"
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

- 六级九要素示例，权重与达成规则显式

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
      "id": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-element0",
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
      "id": "acmm-elements-levels-element1",
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
      "id": "acmm-elements-levels-element2",
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
      "id": "acmm-elements-levels-element3",
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
      "id": "acmm-elements-levels-element4",
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
      "id": "acmm-elements-levels-element5",
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
      "id": "acmm-elements-levels-element6",
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
      "id": "acmm-elements-levels-element7",
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
      "id": "acmm-elements-levels-element8",
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
      "id": "acmm-elements-levels-cell0-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element0",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell0-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element0",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell0-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element0",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell0-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element0",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell0-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element0",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell0-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element0",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell1-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element1",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell1-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element1",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell1-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element1",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell1-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element1",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell1-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element1",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell1-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element1",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell2-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element2",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell2-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element2",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell2-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element2",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell2-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element2",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell2-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element2",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell2-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element2",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell3-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element3",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell3-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element3",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell3-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element3",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell3-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element3",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell3-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element3",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell3-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element3",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell4-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element4",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell4-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element4",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell4-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element4",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell4-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element4",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell4-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element4",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell4-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element4",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell5-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element5",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell5-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element5",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell5-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element5",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell5-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element5",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell5-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element5",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell5-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element5",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell6-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element6",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell6-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element6",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell6-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element6",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell6-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element6",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell6-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element6",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell6-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element6",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell7-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element7",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell7-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element7",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell7-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element7",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell7-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element7",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell7-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element7",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell7-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element7",
      "target": "acmm-elements-levels-level5",
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
      "id": "acmm-elements-levels-cell8-0",
      "type": "traces_to",
      "source": "acmm-elements-levels-element8",
      "target": "acmm-elements-levels-level0",
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
      "id": "acmm-elements-levels-cell8-1",
      "type": "traces_to",
      "source": "acmm-elements-levels-element8",
      "target": "acmm-elements-levels-level1",
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
      "id": "acmm-elements-levels-cell8-2",
      "type": "traces_to",
      "source": "acmm-elements-levels-element8",
      "target": "acmm-elements-levels-level2",
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
      "id": "acmm-elements-levels-cell8-3",
      "type": "traces_to",
      "source": "acmm-elements-levels-element8",
      "target": "acmm-elements-levels-level3",
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
      "id": "acmm-elements-levels-cell8-4",
      "type": "traces_to",
      "source": "acmm-elements-levels-element8",
      "target": "acmm-elements-levels-level4",
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
      "id": "acmm-elements-levels-cell8-5",
      "type": "traces_to",
      "source": "acmm-elements-levels-element8",
      "target": "acmm-elements-levels-level5",
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
    "id": "v-acmm-elements-levels",
    "artifact_id": "architecture-maturity-model",
    "profile_id": "acmm-elements-levels",
    "title": "ACMM 要素级别矩阵／虚构案例",
    "entity_ids": [
      "acmm-elements-levels-level0",
      "acmm-elements-levels-level1",
      "acmm-elements-levels-level2",
      "acmm-elements-levels-level3",
      "acmm-elements-levels-level4",
      "acmm-elements-levels-level5",
      "acmm-elements-levels-element0",
      "acmm-elements-levels-element1",
      "acmm-elements-levels-element2",
      "acmm-elements-levels-element3",
      "acmm-elements-levels-element4",
      "acmm-elements-levels-element5",
      "acmm-elements-levels-element6",
      "acmm-elements-levels-element7",
      "acmm-elements-levels-element8"
    ],
    "relationship_ids": [
      "acmm-elements-levels-cell0-0",
      "acmm-elements-levels-cell0-1",
      "acmm-elements-levels-cell0-2",
      "acmm-elements-levels-cell0-3",
      "acmm-elements-levels-cell0-4",
      "acmm-elements-levels-cell0-5",
      "acmm-elements-levels-cell1-0",
      "acmm-elements-levels-cell1-1",
      "acmm-elements-levels-cell1-2",
      "acmm-elements-levels-cell1-3",
      "acmm-elements-levels-cell1-4",
      "acmm-elements-levels-cell1-5",
      "acmm-elements-levels-cell2-0",
      "acmm-elements-levels-cell2-1",
      "acmm-elements-levels-cell2-2",
      "acmm-elements-levels-cell2-3",
      "acmm-elements-levels-cell2-4",
      "acmm-elements-levels-cell2-5",
      "acmm-elements-levels-cell3-0",
      "acmm-elements-levels-cell3-1",
      "acmm-elements-levels-cell3-2",
      "acmm-elements-levels-cell3-3",
      "acmm-elements-levels-cell3-4",
      "acmm-elements-levels-cell3-5",
      "acmm-elements-levels-cell4-0",
      "acmm-elements-levels-cell4-1",
      "acmm-elements-levels-cell4-2",
      "acmm-elements-levels-cell4-3",
      "acmm-elements-levels-cell4-4",
      "acmm-elements-levels-cell4-5",
      "acmm-elements-levels-cell5-0",
      "acmm-elements-levels-cell5-1",
      "acmm-elements-levels-cell5-2",
      "acmm-elements-levels-cell5-3",
      "acmm-elements-levels-cell5-4",
      "acmm-elements-levels-cell5-5",
      "acmm-elements-levels-cell6-0",
      "acmm-elements-levels-cell6-1",
      "acmm-elements-levels-cell6-2",
      "acmm-elements-levels-cell6-3",
      "acmm-elements-levels-cell6-4",
      "acmm-elements-levels-cell6-5",
      "acmm-elements-levels-cell7-0",
      "acmm-elements-levels-cell7-1",
      "acmm-elements-levels-cell7-2",
      "acmm-elements-levels-cell7-3",
      "acmm-elements-levels-cell7-4",
      "acmm-elements-levels-cell7-5",
      "acmm-elements-levels-cell8-0",
      "acmm-elements-levels-cell8-1",
      "acmm-elements-levels-cell8-2",
      "acmm-elements-levels-cell8-3",
      "acmm-elements-levels-cell8-4",
      "acmm-elements-levels-cell8-5"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile acmm-elements-levels --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile acmm-elements-levels --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
