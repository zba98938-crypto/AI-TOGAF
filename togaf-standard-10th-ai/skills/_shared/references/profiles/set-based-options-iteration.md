# 集合式并行方案逐轮评估

`profile_id`: set-based-options-iteration；`artifact_id`: options-decision-matrix；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G20F §4.6。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.2。

{
  "id": "set-based-options-iteration",
  "version": "2.2",
  "source_verified": false,
  "layout_notes": "正文方法的操作化表；不是原图复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:sbce_iteration, guide:sbce_constraint。关系类型：。

```json
{
  "entities": {
    "guide:sbce_iteration": [
      "option_id",
      "subsystem",
      "goal",
      "iteration",
      "hypothesis",
      "assessment",
      "evidence_refs",
      "decision_owner",
      "status",
      "decision_reason",
      "new_evidence_refs"
    ],
    "guide:sbce_constraint": [
      "source_option_id",
      "target_option_id",
      "rule",
      "status",
      "evidence_refs"
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
      "id": "A-I1",
      "type": "guide:sbce_iteration",
      "name": "通知 / A / 轮次1",
      "attributes": {
        "option_id": "A",
        "subsystem": "通知",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 1,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "集中队列可复用，待扩大负载验证",
        "evidence_refs": [
          "LAB-1"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "retain",
        "decision_reason": "集中队列可复用，待扩大负载验证",
        "new_evidence_refs": []
      },
      "evidence": [
        "LAB-1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "B-I1",
      "type": "guide:sbce_iteration",
      "name": "通知 / B / 轮次1",
      "attributes": {
        "option_id": "B",
        "subsystem": "通知",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 1,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "事件流需恢复实验",
        "evidence_refs": [
          "LAB-1"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "retain",
        "decision_reason": "事件流需恢复实验",
        "new_evidence_refs": []
      },
      "evidence": [
        "LAB-1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "C-I1",
      "type": "guide:sbce_iteration",
      "name": "目录 / C / 轮次1",
      "attributes": {
        "option_id": "C",
        "subsystem": "目录",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 1,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "已测API契约可兼容",
        "evidence_refs": [
          "LAB-1"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "retain",
        "decision_reason": "已测API契约可兼容",
        "new_evidence_refs": []
      },
      "evidence": [
        "LAB-1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "D-I1",
      "type": "guide:sbce_iteration",
      "name": "目录 / D / 轮次1",
      "attributes": {
        "option_id": "D",
        "subsystem": "目录",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 1,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "夜间文件不满足分钟级目标",
        "evidence_refs": [
          "LAB-1"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "eliminate",
        "decision_reason": "响应窗口不符",
        "new_evidence_refs": [
          "LAB-1"
        ]
      },
      "evidence": [
        "LAB-1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "A-I2",
      "type": "guide:sbce_iteration",
      "name": "通知 / A / 轮次2",
      "attributes": {
        "option_id": "A",
        "subsystem": "通知",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 2,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "180毫秒，满足项目条件",
        "evidence_refs": [
          "LAB-2"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "selected",
        "decision_reason": "180毫秒，满足项目条件",
        "new_evidence_refs": []
      },
      "evidence": [
        "LAB-2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "B-I2",
      "type": "guide:sbce_iteration",
      "name": "通知 / B / 轮次2",
      "attributes": {
        "option_id": "B",
        "subsystem": "通知",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 2,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "恢复实验未满足项目要求",
        "evidence_refs": [
          "LAB-2"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "eliminate",
        "decision_reason": "恢复窗口超限",
        "new_evidence_refs": [
          "LAB-2"
        ]
      },
      "evidence": [
        "LAB-2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "C-I2",
      "type": "guide:sbce_iteration",
      "name": "目录 / C / 轮次2",
      "attributes": {
        "option_id": "C",
        "subsystem": "目录",
        "goal": "可追溯的分钟级预约回执",
        "iteration": 2,
        "hypothesis": "明确契约和恢复策略可满足本项目回执要求",
        "assessment": "A/C接口兼容",
        "evidence_refs": [
          "LAB-2"
        ],
        "decision_owner": "架构与运营评审组",
        "status": "selected",
        "decision_reason": "A/C接口兼容",
        "new_evidence_refs": []
      },
      "evidence": [
        "LAB-2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "CON-AC",
      "type": "guide:sbce_constraint",
      "name": "事件键、事务重试和恢复窗口一致",
      "attributes": {
        "source_option_id": "A",
        "target_option_id": "C",
        "rule": "事件键、事务重试和恢复窗口一致",
        "status": "satisfied",
        "evidence_refs": [
          "LAB-2"
        ]
      },
      "evidence": [
        "LAB-2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "CON-BC",
      "type": "guide:sbce_constraint",
      "name": "事件契约及恢复窗口一致",
      "attributes": {
        "source_option_id": "B",
        "target_option_id": "C",
        "rule": "事件契约及恢复窗口一致",
        "status": "unknown",
        "evidence_refs": [
          "LAB-1"
        ]
      },
      "evidence": [
        "LAB-1"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-set-based-options-iteration",
    "artifact_id": "options-decision-matrix",
    "profile_id": "set-based-options-iteration",
    "title": "set-based-options-iteration",
    "entity_ids": [
      "A-I1",
      "B-I1",
      "C-I1",
      "D-I1",
      "A-I2",
      "B-I2",
      "C-I2",
      "CON-AC",
      "CON-BC"
    ],
    "relationship_ids": [],
    "analysis": "子系统分别并行探索备选；保留每轮淘汰和细化依据，再审跨子系统契约。选定后仍需验证未建模的支付接口；分析选择不等于正式批准。",
    "legend": "项目判断；空白不代表不适用。来源画像、项目观察、淘汰/重开、分析选择和批准分开。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile set-based-options-iteration --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile set-based-options-iteration --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
