# 组合估算充分性十问

`profile_id`: portfolio-estimate-sufficiency-check-default；`artifact_id`: portfolio-estimate-sufficiency-check；主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G186 §8.4.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "portfolio-estimate-sufficiency-check-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:estimate_check。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 第6问“有无担忧”与其他问不是同方向，禁止全是即通过
- 第10问是数量，不能硬转是/否
- 8/9为该指南收益递减信号，项目缓冲和公式须明确来源
- 缺范围可比性或深度分母为零时保留未知

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile portfolio-estimate-sufficiency-check-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile portfolio-estimate-sufficiency-check-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
