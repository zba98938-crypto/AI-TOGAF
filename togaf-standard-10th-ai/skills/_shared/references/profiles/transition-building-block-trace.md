# 过渡架构与工作包追溯

`profile_id`: transition-building-block-trace；`artifact_id`: transition-architecture-model；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G248/fig2-2。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G248/fig2-2",
  "layout_notes": "目标可成为下一轮基线；每端基数和反向读法独立",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/transition-building-block-trace.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：transition, work_package。关系类型：implements_transition, traces_to, depends_on。

```json
{
  "entities": {
    "transition": [
      "definition",
      "operating_conditions"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 目标可成为下一轮基线；每端基数和反向读法独立

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
      "id": "transition-building-block-trace-state0",
      "type": "transition",
      "name": "基线：旧平台",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 0
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-state1",
      "type": "transition",
      "name": "过渡1：只读副本",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-state2",
      "type": "transition",
      "name": "过渡2：分批写入",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-state3",
      "type": "transition",
      "name": "目标：统一履约",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 3
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-wp",
      "type": "work_package",
      "name": "接口及对账工作包",
      "attributes": {
        "definition": "实现第一过渡的候选工作包"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "transition-building-block-trace-evolve1",
      "type": "traces_to",
      "source": "transition-building-block-trace-state0",
      "target": "transition-building-block-trace-state1",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-evolve2",
      "type": "traces_to",
      "source": "transition-building-block-trace-state1",
      "target": "transition-building-block-trace-state2",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-evolve3",
      "type": "traces_to",
      "source": "transition-building-block-trace-state2",
      "target": "transition-building-block-trace-state3",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-building-block-trace-impl",
      "type": "implements_transition",
      "source": "transition-building-block-trace-wp",
      "target": "transition-building-block-trace-state1",
      "label": "工作包实现可运营过渡",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-transition-building-block-trace",
    "artifact_id": "transition-architecture-model",
    "profile_id": "transition-building-block-trace",
    "title": "过渡架构与工作包追溯／虚构案例",
    "entity_ids": [
      "transition-building-block-trace-state0",
      "transition-building-block-trace-state1",
      "transition-building-block-trace-state2",
      "transition-building-block-trace-state3",
      "transition-building-block-trace-wp"
    ],
    "relationship_ids": [
      "transition-building-block-trace-evolve1",
      "transition-building-block-trace-evolve2",
      "transition-building-block-trace-evolve3",
      "transition-building-block-trace-impl"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile transition-building-block-trace --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile transition-building-block-trace --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
