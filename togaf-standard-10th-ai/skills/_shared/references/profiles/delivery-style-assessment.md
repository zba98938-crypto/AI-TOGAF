# 交付风格逐范围比较

`profile_id`: delivery-style-assessment；`artifact_id`: options-decision-matrix；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G20F §4.7.1 表4-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.2。

{
  "id": "delivery-style-assessment",
  "version": "2.2",
  "source_verified": false,
  "layout_notes": "正文方法的操作化表；不是原图复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:delivery_feature_review, guide:delivery_style_decision。关系类型：。

```json
{
  "entities": {
    "guide:delivery_feature_review": [
      "feature_id",
      "source_guidance",
      "applies",
      "observation",
      "evidence_refs"
    ],
    "guide:delivery_style_decision": [
      "scope_id",
      "styles",
      "owner",
      "rationale",
      "evidence_refs",
      "conflicting_features",
      "tailoring"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 没有来源或显式项目依据不增加评分/权重/合格线
- 每行事实与结论可追溯，未知不能写零
- 按实例范围和轮次保持稳定ID，改变材料重新生成
- 分析选择不授予正式批准

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "sources": [
    {
      "id": "RAW-01",
      "kind": "example",
      "description": "通知组件只影响预约回执"
    },
    {
      "id": "RAW-02",
      "kind": "example",
      "description": "总计划涉及47个服务点和中央档案"
    },
    {
      "id": "RAW-03",
      "kind": "example",
      "description": "回执复用既有短信接口"
    },
    {
      "id": "RAW-04",
      "kind": "example",
      "description": "跨点身份与历史档案同步复杂"
    },
    {
      "id": "RAW-05",
      "kind": "example",
      "description": "数据库与消息队列已稳定运行"
    },
    {
      "id": "RAW-06",
      "kind": "example",
      "description": "团队拟采用未在本馆使用的事件流技术"
    },
    {
      "id": "RAW-07",
      "kind": "example",
      "description": "法定保存与复核流程保持稳定"
    },
    {
      "id": "RAW-08",
      "kind": "example",
      "description": "线上预约和退款流程正在重新定义"
    },
    {
      "id": "RAW-09",
      "kind": "example",
      "description": "Java维护技能已有排班记录"
    },
    {
      "id": "RAW-10",
      "kind": "example",
      "description": "事件流设计和恢复演练需要培训"
    },
    {
      "id": "RAW-11",
      "kind": "example",
      "description": "线上预约为新业务能力"
    },
    {
      "id": "RAW-12",
      "kind": "example",
      "description": "短信回执属于现有服务扩展"
    },
    {
      "id": "RAW-13",
      "kind": "example",
      "description": "复用既有身份与检索构建块"
    },
    {
      "id": "RAW-14",
      "kind": "example",
      "description": "将集成现有短信及支付服务"
    },
    {
      "id": "RAW-15",
      "kind": "example",
      "description": "节庆通知组件目标两周交付"
    },
    {
      "id": "RAW-16",
      "kind": "example",
      "description": "全馆迁移预计跨一个年度"
    },
    {
      "id": "RAW-17",
      "kind": "example",
      "description": "节庆通知上线窗口两周不可延"
    },
    {
      "id": "RAW-18",
      "kind": "example",
      "description": "档案迁移必须跨年度保存窗口"
    },
    {
      "id": "RAW-19",
      "kind": "example",
      "description": "志愿者和IT预算限制同时存在"
    },
    {
      "id": "RAW-20",
      "kind": "example",
      "description": "馆藏与收费记录不得丢失且需审计"
    },
    {
      "id": "RAW-21",
      "kind": "example",
      "description": "预约退款功能仍在用户试验"
    },
    {
      "id": "RAW-22",
      "kind": "example",
      "description": "跨馆身份与事件契约需要统一"
    },
    {
      "id": "RAW-23",
      "kind": "example",
      "description": "只读短信模板修改影响有限"
    },
    {
      "id": "RAW-24",
      "kind": "example",
      "description": "个人数据和收费迁移失败后果高"
    },
    {
      "id": "LAB-1",
      "kind": "example",
      "description": "通知子系统可保留集中队列A或事件流B；目录子系统可用已测API C或夜间文件D。A/C首轮可实现分钟级回执；D无法满足实时查验。B的恢复能力尚待实验。"
    },
    {
      "id": "LAB-2",
      "kind": "example",
      "description": "第二轮A端到端压测95分位延迟180毫秒，C契约兼容；项目约定预算与恢复窗口均满足。B恢复演练暂未满足项目要求，保留原始失败日志。"
    },
    {
      "id": "LAB-3",
      "kind": "example",
      "description": "变更实验扩大到47馆并发，A延迟800毫秒超出项目500毫秒要求；B的新恢复方案通过演练且与C的新接口契约兼容。规则和实验值均属项目。"
    }
  ],
  "entities": [
    {
      "id": "F01",
      "type": "guide:delivery_feature_review",
      "name": "小规模",
      "attributes": {
        "feature_id": "F01",
        "applies": "yes",
        "observation": "通知组件只影响预约回执",
        "evidence_refs": [
          "RAW-01"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "否"
        }
      },
      "evidence": [
        "RAW-01"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F02",
      "type": "guide:delivery_feature_review",
      "name": "大规模",
      "attributes": {
        "feature_id": "F02",
        "applies": "yes",
        "observation": "总计划涉及47个服务点和中央档案",
        "evidence_refs": [
          "RAW-02"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-02"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F03",
      "type": "guide:delivery_feature_review",
      "name": "简单",
      "attributes": {
        "feature_id": "F03",
        "applies": "yes",
        "observation": "回执复用既有短信接口",
        "evidence_refs": [
          "RAW-03"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "否"
        }
      },
      "evidence": [
        "RAW-03"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F04",
      "type": "guide:delivery_feature_review",
      "name": "复杂",
      "attributes": {
        "feature_id": "F04",
        "applies": "yes",
        "observation": "跨点身份与历史档案同步复杂",
        "evidence_refs": [
          "RAW-04"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-04"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F05",
      "type": "guide:delivery_feature_review",
      "name": "成熟技术",
      "attributes": {
        "feature_id": "F05",
        "applies": "yes",
        "observation": "数据库与消息队列已稳定运行",
        "evidence_refs": [
          "RAW-05"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-05"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F06",
      "type": "guide:delivery_feature_review",
      "name": "新技术",
      "attributes": {
        "feature_id": "F06",
        "applies": "yes",
        "observation": "团队拟采用未在本馆使用的事件流技术",
        "evidence_refs": [
          "RAW-06"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-06"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F07",
      "type": "guide:delivery_feature_review",
      "name": "稳定业务流程",
      "attributes": {
        "feature_id": "F07",
        "applies": "yes",
        "observation": "法定保存与复核流程保持稳定",
        "evidence_refs": [
          "RAW-07"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-07"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F08",
      "type": "guide:delivery_feature_review",
      "name": "变化中的业务流程",
      "attributes": {
        "feature_id": "F08",
        "applies": "yes",
        "observation": "线上预约和退款流程正在重新定义",
        "evidence_refs": [
          "RAW-08"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-08"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F09",
      "type": "guide:delivery_feature_review",
      "name": "已具备技能",
      "attributes": {
        "feature_id": "F09",
        "applies": "yes",
        "observation": "Java维护技能已有排班记录",
        "evidence_refs": [
          "RAW-09"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-09"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F10",
      "type": "guide:delivery_feature_review",
      "name": "需要培养技能",
      "attributes": {
        "feature_id": "F10",
        "applies": "yes",
        "observation": "事件流设计和恢复演练需要培训",
        "evidence_refs": [
          "RAW-10"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-10"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F11",
      "type": "guide:delivery_feature_review",
      "name": "新解决方案",
      "attributes": {
        "feature_id": "F11",
        "applies": "yes",
        "observation": "线上预约为新业务能力",
        "evidence_refs": [
          "RAW-11"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-11"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F12",
      "type": "guide:delivery_feature_review",
      "name": "扩展现有解决方案",
      "attributes": {
        "feature_id": "F12",
        "applies": "yes",
        "observation": "短信回执属于现有服务扩展",
        "evidence_refs": [
          "RAW-12"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-12"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F13",
      "type": "guide:delivery_feature_review",
      "name": "集成现有构建块",
      "attributes": {
        "feature_id": "F13",
        "applies": "yes",
        "observation": "复用既有身份与检索构建块",
        "evidence_refs": [
          "RAW-13"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-13"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F14",
      "type": "guide:delivery_feature_review",
      "name": "集成现有运行服务",
      "attributes": {
        "feature_id": "F14",
        "applies": "yes",
        "observation": "将集成现有短信及支付服务",
        "evidence_refs": [
          "RAW-14"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-14"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F15",
      "type": "guide:delivery_feature_review",
      "name": "短期变革视野",
      "attributes": {
        "feature_id": "F15",
        "applies": "yes",
        "observation": "节庆通知组件目标两周交付",
        "evidence_refs": [
          "RAW-15"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-15"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F16",
      "type": "guide:delivery_feature_review",
      "name": "长期变革视野",
      "attributes": {
        "feature_id": "F16",
        "applies": "yes",
        "observation": "全馆迁移预计跨一个年度",
        "evidence_refs": [
          "RAW-16"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-16"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F17",
      "type": "guide:delivery_feature_review",
      "name": "时间驱动项目（较短时间框架）",
      "attributes": {
        "feature_id": "F17",
        "applies": "yes",
        "observation": "节庆通知上线窗口两周不可延",
        "evidence_refs": [
          "RAW-17"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "否"
        }
      },
      "evidence": [
        "RAW-17"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F18",
      "type": "guide:delivery_feature_review",
      "name": "时间驱动项目（较长时间框架）",
      "attributes": {
        "feature_id": "F18",
        "applies": "yes",
        "observation": "档案迁移必须跨年度保存窗口",
        "evidence_refs": [
          "RAW-18"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-18"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F19",
      "type": "guide:delivery_feature_review",
      "name": "成本驱动项目",
      "attributes": {
        "feature_id": "F19",
        "applies": "yes",
        "observation": "志愿者和IT预算限制同时存在",
        "evidence_refs": [
          "RAW-19"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-19"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F20",
      "type": "guide:delivery_feature_review",
      "name": "质量驱动项目",
      "attributes": {
        "feature_id": "F20",
        "applies": "yes",
        "observation": "馆藏与收费记录不得丢失且需审计",
        "evidence_refs": [
          "RAW-20"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-20"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F21",
      "type": "guide:delivery_feature_review",
      "name": "功能驱动项目",
      "attributes": {
        "feature_id": "F21",
        "applies": "yes",
        "observation": "预约退款功能仍在用户试验",
        "evidence_refs": [
          "RAW-21"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "是",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-21"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F22",
      "type": "guide:delivery_feature_review",
      "name": "结构/架构驱动项目",
      "attributes": {
        "feature_id": "F22",
        "applies": "yes",
        "observation": "跨馆身份与事件契约需要统一",
        "evidence_refs": [
          "RAW-22"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-22"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F23",
      "type": "guide:delivery_feature_review",
      "name": "低风险",
      "attributes": {
        "feature_id": "F23",
        "applies": "yes",
        "observation": "只读短信模板修改影响有限",
        "evidence_refs": [
          "RAW-23"
        ],
        "source_guidance": {
          "rapid": "是",
          "agile": "是",
          "robust": "否"
        }
      },
      "evidence": [
        "RAW-23"
      ],
      "certainty": "assumed"
    },
    {
      "id": "F24",
      "type": "guide:delivery_feature_review",
      "name": "高风险",
      "attributes": {
        "feature_id": "F24",
        "applies": "yes",
        "observation": "个人数据和收费迁移失败后果高",
        "evidence_refs": [
          "RAW-24"
        ],
        "source_guidance": {
          "rapid": "否",
          "agile": "否",
          "robust": "是"
        }
      },
      "evidence": [
        "RAW-24"
      ],
      "certainty": "assumed"
    },
    {
      "id": "decision-archive-program",
      "type": "guide:delivery_style_decision",
      "name": "archive-program",
      "attributes": {
        "scope_id": "archive-program",
        "styles": [
          "robust",
          "agile"
        ],
        "owner": "馆藏与技术负责人",
        "rationale": "全馆数据迁移保留审慎架构控制；有界预约功能按试验迭代",
        "evidence_refs": [
          "RAW-02",
          "RAW-04",
          "RAW-16",
          "RAW-24"
        ],
        "conflicting_features": [
          "F01",
          "F02",
          "F23",
          "F24"
        ],
        "tailoring": "全馆迁移robust；预约功能子项目agile；按过渡出口复核运行和恢复条件"
      },
      "evidence": [
        "RAW-02",
        "RAW-04",
        "RAW-16",
        "RAW-24"
      ],
      "certainty": "assumed"
    },
    {
      "id": "decision-sms-component",
      "type": "guide:delivery_style_decision",
      "name": "sms-component",
      "attributes": {
        "scope_id": "sms-component",
        "styles": [
          "rapid"
        ],
        "owner": "通知服务负责人",
        "rationale": "仅复用现有只读模板；两周窗口且影响低",
        "evidence_refs": [
          "RAW-01",
          "RAW-03",
          "RAW-15",
          "RAW-23"
        ],
        "conflicting_features": [
          "F02",
          "F24"
        ],
        "tailoring": "rapid只适用于只读通知组件，不继承到收费或数据迁移"
      },
      "evidence": [
        "RAW-01",
        "RAW-03",
        "RAW-15",
        "RAW-23"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-delivery-style-assessment",
    "artifact_id": "options-decision-matrix",
    "profile_id": "delivery-style-assessment",
    "title": "delivery-style-assessment",
    "entity_ids": [
      "F01",
      "F02",
      "F03",
      "F04",
      "F05",
      "F06",
      "F07",
      "F08",
      "F09",
      "F10",
      "F11",
      "F12",
      "F13",
      "F14",
      "F15",
      "F16",
      "F17",
      "F18",
      "F19",
      "F20",
      "F21",
      "F22",
      "F23",
      "F24",
      "decision-archive-program",
      "decision-sms-component"
    ],
    "relationship_ids": [],
    "analysis": "跨范围特征同时出现；全馆迁移采用稳健控制，预约按敏捷迭代，初始只读短信可快速。按范围说明理由，没有加权或多数票。",
    "legend": "项目判断；空白不代表不适用。来源画像、项目观察、淘汰/重开、分析选择和批准分开。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile delivery-style-assessment --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile delivery-style-assessment --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
