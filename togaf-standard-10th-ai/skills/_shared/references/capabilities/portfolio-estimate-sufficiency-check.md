# 组合估算充分性检查

ID：`portfolio-estimate-sufficiency-check`。主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G186 §8.4.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

继续细化是否仍有足够收益，预算决策是否已有充分依据？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 继续细化是否仍有足够收益，预算决策是否已有充分依据？
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

对象类型：guide:estimate_check。

```json
{
  "guide:estimate_check": [
    "sequence",
    "question",
    "finding",
    "evidence_refs",
    "rule",
    "calculation",
    "limitation",
    "next_action"
  ]
}
```

{
  "name": {
    "meaning": "充分性检查项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "sequence": {
    "meaning": "来源十问顺序",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "question": {
    "meaning": "检查问题",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "finding": {
    "meaning": "事实/回答而非统一分数",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "rule": {
    "meaning": "源指南建议或项目规则的归属",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "calculation": {
    "meaning": "如适用显示数据和计算过程",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "limitation": {
    "meaning": "缺口/时效/不可比限制",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "next_action": {
    "meaning": "继续调查或提交决策者的建议",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 逐项回答来源十问，保留第6问负向语义和第10问数量
2. 比较各轮同范围估算与覆盖计数
3. 只在项目明示公式/应急参数时计算第8/9信号
4. 指出风险、时效和关键未知对建议的影响
5. 给停止/继续调查的有据建议，不自动批准预算

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 第6问“有无担忧”与其他问不是同方向，禁止全是即通过
- 第10问是数量，不能硬转是/否
- 8/9为该指南收益递减信号，项目缓冲和公式须明确来源
- 缺范围可比性或深度分母为零时保留未知

- 第6问“有无担忧”与其他问不是同方向，禁止全是即通过
- 第10问是数量，不能硬转是/否
- 8/9为该指南收益递减信号，项目缓冲和公式须明确来源
- 缺范围可比性或深度分母为零时保留未知


## 视图和交付物

- [组合估算充分性十问](../profiles/portfolio-estimate-sufficiency-check-default.md)

- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "缺应急系数却生成10%默认值",
    "expected": "missing-project-contingency"
  },
  "modification_example": {
    "change": "本轮估算106万改125万，覆盖比从2改4",
    "expected": "估算变化25%超过缓冲、比值未下降；收益递减信号均未达到，继续针对高不确定项调查"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/portfolio-estimate-sufficiency-check.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-portfolio-estimate-sufficiency-check-default",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 sufficiency",
      "locator": "examples/addenda/project-management/raw-business-materials.json#sufficiency"
    }
  ],
  "entities": [
    {
      "id": "portfolio-estimate-sufficiency-check-default-1",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q1",
      "attributes": {
        "sequence": 1,
        "question": "每主题工作包按能力连续谱分类且不混保持/改进？",
        "finding": "保持/改进已分离",
        "evidence_refs": [
          "ES-01",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-2",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q2",
      "attributes": {
        "sequence": 2,
        "question": "依赖与级联影响获决策者和实施者认可？",
        "finding": "依赖已由虚构团队确认",
        "evidence_refs": [
          "ES-01",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-3",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q3",
      "attributes": {
        "sequence": 3,
        "question": "EA全景探索是否连续？",
        "finding": "覆盖继续扩展",
        "evidence_refs": [
          "ES-01",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-4",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q4",
      "attributes": {
        "sequence": 4,
        "question": "风险缓解与控制是否加入组合？",
        "finding": "风险控制已纳入",
        "evidence_refs": [
          "ES-01",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-5",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q5",
      "attributes": {
        "sequence": 5,
        "question": "各主题兼顾运营卓越与适用性？",
        "finding": "两类目标均已考虑",
        "evidence_refs": [
          "ES-01",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-6",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q6",
      "attributes": {
        "sequence": 6,
        "question": "是否存在时效性担忧？",
        "finding": "无已知担忧",
        "evidence_refs": [
          "ES-01",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-7",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q7",
      "attributes": {
        "sequence": 7,
        "question": "是否已有粗略估算与应急系数？",
        "finding": "项目10%应急缓冲",
        "evidence_refs": [
          "ES-02",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-8",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q8",
      "attributes": {
        "sequence": 8,
        "question": "覆盖广度增长/深度增长比是否递减？",
        "finding": "是：2小于3",
        "evidence_refs": [
          "ES-02",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": {
          "previous_breadth": 6,
          "previous_depth": 2,
          "current_breadth": 4,
          "current_depth": 2,
          "previous_ratio": 3,
          "current_ratio": 2
        },
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-9",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q9",
      "attributes": {
        "sequence": 9,
        "question": "相邻迭代估算差异是否小于应急系数？",
        "finding": "是：6%小于10%",
        "evidence_refs": [
          "ES-02",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": {
          "previous_CNY": 1000000,
          "current_CNY": 1060000,
          "relative_change": 0.06,
          "contingency": 0.1
        },
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "portfolio-estimate-sufficiency-check-default-10",
      "type": "guide:estimate_check",
      "name": "组合充分性 Q10",
      "attributes": {
        "sequence": 10,
        "question": "多少工作为一次性转型执行？",
        "finding": "1项一次性；2项持续运营",
        "evidence_refs": [
          "ES-04",
          "ES-03"
        ],
        "rule": "G186 §8.4.2第8或9项指示收益递减；差额归一化公式与10%仅本项目规则",
        "calculation": "not-applicable",
        "limitation": "估算为假设，不代表交付保证；十问无加权总分",
        "next_action": "第8/9信号达到，可建议停止本轮细化并提预算，仍由授权方决定"
      },
      "evidence": [
        "src-portfolio-estimate-sufficiency-check-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-portfolio-estimate-sufficiency-check-default",
    "artifact_id": "portfolio-estimate-sufficiency-check",
    "profile_id": "portfolio-estimate-sufficiency-check-default",
    "title": "组合估算充分性十问",
    "entity_ids": [
      "portfolio-estimate-sufficiency-check-default-1",
      "portfolio-estimate-sufficiency-check-default-2",
      "portfolio-estimate-sufficiency-check-default-3",
      "portfolio-estimate-sufficiency-check-default-4",
      "portfolio-estimate-sufficiency-check-default-5",
      "portfolio-estimate-sufficiency-check-default-6",
      "portfolio-estimate-sufficiency-check-default-7",
      "portfolio-estimate-sufficiency-check-default-8",
      "portfolio-estimate-sufficiency-check-default-9",
      "portfolio-estimate-sufficiency-check-default-10"
    ],
    "relationship_ids": [],
    "analysis": "覆盖比3降到2，估算变化6%小于项目10%缓冲，两项文献收益递减信号均达到；建议转预算决策，不将估算当承诺或权重评分。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "sufficiency"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact portfolio-estimate-sufficiency-check --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
