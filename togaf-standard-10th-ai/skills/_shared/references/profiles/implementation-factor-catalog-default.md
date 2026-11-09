# 实施因素决策档案

`profile_id`: implementation-factor-catalog-default；`artifact_id`: implementation-factor-catalog；主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G186 §7.4.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "implementation-factor-catalog-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:implementation_factor。关系类型：。

```json
{
  "entities": {
    "guide:implementation_factor": [
      "unit",
      "change_attribute",
      "observation",
      "evidence_refs",
      "effect",
      "required_action",
      "owner",
      "timing",
      "confidence",
      "decision_record"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 只记录具体因素及影响，不默认文化可用分数衡量
- 访谈说有能力不等于已演练、可用容量或正式承诺

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-implementation-factor-catalog-default",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 factors",
      "locator": "examples/addenda/project-management/raw-business-materials.json#factors"
    }
  ],
  "entities": [
    {
      "id": "implementation-factor-catalog-default-1",
      "type": "guide:implementation_factor",
      "name": "东仓专家容量与集成技能",
      "attributes": {
        "unit": "东仓",
        "change_attribute": "转型容量/技能",
        "observation": "2名专家各4小时/周；无事件集成经验",
        "evidence_refs": [
          "IF-01"
        ],
        "effect": "每周8专家小时上限；技术培训和外部集成支持是前置",
        "required_action": "安排培训并验证集成演练，容量计划按8小时而非2FTE",
        "owner": "东仓负责人/技术负责人",
        "timing": "设计评审前",
        "confidence": "访谈自述，尚无演练证据",
        "decision_record": "候选约束，待资源负责人确认"
      },
      "evidence": [
        "src-implementation-factor-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "implementation-factor-catalog-default-2",
      "type": "guide:implementation_factor",
      "name": "西仓关账窗口",
      "attributes": {
        "unit": "西仓",
        "change_attribute": "运营窗口",
        "observation": "关账期间不可参与",
        "evidence_refs": [
          "IF-01"
        ],
        "effect": "不能将跨仓访谈排在关账期",
        "required_action": "取得具体关账日历并调整依赖",
        "owner": "西仓负责人",
        "timing": "日期unknown",
        "confidence": "日期未确定",
        "decision_record": "阻断精确排程，不臆造日期"
      },
      "evidence": [
        "src-implementation-factor-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "implementation-factor-catalog-default-3",
      "type": "guide:implementation_factor",
      "name": "共享客户数据责任分歧",
      "attributes": {
        "unit": "企业数据团队",
        "change_attribute": "组织文化/治理责任",
        "observation": "尚不接受中央治理；目标要求跨仓单号唯一",
        "evidence_refs": [
          "IF-02"
        ],
        "effect": "不能凭技术方案认定变革可吸收",
        "required_action": "安排授权利益相关者澄清责任与权衡，形成控制和培训",
        "owner": "数据负责人/发起人",
        "timing": "目标批准前",
        "confidence": "分歧已记录、解决未证实",
        "decision_record": "不以低成熟度标签替代具体障碍"
      },
      "evidence": [
        "src-implementation-factor-catalog-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-implementation-factor-catalog-default",
    "artifact_id": "implementation-factor-catalog",
    "profile_id": "implementation-factor-catalog-default",
    "title": "实施因素决策档案",
    "entity_ids": [
      "implementation-factor-catalog-default-1",
      "implementation-factor-catalog-default-2",
      "implementation-factor-catalog-default-3"
    ],
    "relationship_ids": [],
    "analysis": "从IF-01/02提取容量、运营窗口、责任文化三项因素；8小时是原料数量相乘所得项目容量，不是TOGAF评分。未知日期阻断排程。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "factors"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile implementation-factor-catalog-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile implementation-factor-catalog-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
