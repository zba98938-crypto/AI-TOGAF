# 实施因素目录

ID：`implementation-factor-catalog`。主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G186 §7.4.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些组织文化、转型能力和技能因素改变变革实施安排？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 哪些组织文化、转型能力和技能因素改变变革实施安排？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 范围、五维语境、所用目标与交付物版本
- 原始计划/访谈/验收/估算及来源ID
- 组织授权和容差规则；缺失时不代推

可选：

- 历史项目及组织模板

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:implementation_factor。

```json
{
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
}
```

{
  "name": {
    "meaning": "实施因素",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "unit": {
    "meaning": "业务单元/企业范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "change_attribute": {
    "meaning": "文化、转型能力或技能等具体因素",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "observation": {
    "meaning": "原始观察与当前情况",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "effect": {
    "meaning": "对方案/工作包/时点的实际影响",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "required_action": {
    "meaning": "补强动作及其进入条件",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "owner": {
    "meaning": "动作责任",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "timing": {
    "meaning": "可用窗口与业务约束",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "confidence": {
    "meaning": "依据局限，不使用无依据分数",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision_record": {
    "meaning": "为何采纳此处理及谁仍需确认",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 按业务单元与企业层收集转型属性
2. 区分观察事实、解释和未知
3. 将每个因素连接到具体实施工作或选择影响
4. 记录处理动作、责任、窗口与决策理由
5. 资源/文化变化后重新审视路线与风险

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 只记录具体因素及影响，不默认文化可用分数衡量
- 访谈说有能力不等于已演练、可用容量或正式承诺

- 只记录具体因素及影响，不默认文化可用分数衡量
- 访谈说有能力不等于已演练、可用容量或正式承诺


## 视图和交付物

- [实施因素决策档案](../profiles/implementation-factor-catalog-default.md)

- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "只写“成熟度低”无具体观察或证据",
    "expected": "factor-evidence-gap"
  },
  "modification_example": {
    "change": "新增演练结果证明东仓已掌握集成",
    "expected": "技能缺口可关闭，专家每周8小时容量不自动变多"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/implementation-factor-catalog.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact implementation-factor-catalog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
