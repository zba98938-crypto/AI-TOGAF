# BI数据价值链、语义与控制

`profile_id`: bi-value-chain-controls；`artifact_id`: bi-transition-architecture；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G238 表4-2价值链设计、表4-3存储/处理/监控。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "bi-value-chain-controls",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "结构化表格，含完整属性、方向和证据；不是来源图模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:bi_value_chain。关系类型：ops:data_derivation。

```json
{
  "entities": {
    "ops:bi_value_chain": [
      "layer_kind",
      "input_refs",
      "transformation_rule",
      "business_purpose",
      "owner",
      "quality_controls",
      "protection_controls",
      "metadata_lineage",
      "scope",
      "reference_identity",
      "evidence_detail"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 原始层不得修改源内容
- 有向关系和input_refs一致
- 技术规则与业务规则分开
- 每层有质量/保护/血缘责任

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/bi-value-chain-controls/raw-brief.md",
  "analysis_path": "examples/addenda/operations/bi-value-chain-controls/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚U1读取库存应用。每批原始库存保存不变；TECH-1只统一日期类型，异常隔离。BUS-1以需求量大于可用量识别候选缺件；业务视图经SEM-1解释时点/站点，调度人复核后调拨。库存源及时性未测；看板显示观测时间，过期转人工。每层保留批次/规则/用途血缘和负责人；不进入客户联系方式。流程是项目设计，非强制所有项目有五层。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "CHAIN-S",
      "type": "ops:bi_value_chain",
      "name": "库存源",
      "attributes": {
        "layer_kind": "source",
        "input_refs": [
          "库存应用"
        ],
        "transformation_rule": "源系统事实按原事务时间输出",
        "business_purpose": "提供站点备件事实",
        "owner": "库存系统负责人",
        "quality_controls": "源数量可能延迟，记录提取时间",
        "protection_controls": "仅库存字段，不带客户",
        "metadata_lineage": "数据集STOCK-v1/源系统/提取时间",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "reference_identity": "project-tailored-value-chain; not-mandatory-TOGAF-pipeline",
        "evidence_detail": "虚构U1数据流程访谈与TECH-1/BUS-1草案"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "CHAIN-R",
      "type": "ops:bi_value_chain",
      "name": "库存原始空间",
      "attributes": {
        "layer_kind": "raw",
        "input_refs": [
          "CHAIN-S"
        ],
        "transformation_rule": "不更改源内容，按批次保留原始副本",
        "business_purpose": "可审计及重放",
        "owner": "数据工程师",
        "quality_controls": "完整性校验与批次摘要",
        "protection_controls": "项目受控服务身份",
        "metadata_lineage": "源批次→原始对象映射",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "reference_identity": "project-tailored-value-chain; not-mandatory-TOGAF-pipeline",
        "evidence_detail": "虚构U1数据流程访谈与TECH-1/BUS-1草案"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "CHAIN-P",
      "type": "ops:bi_value_chain",
      "name": "库存准备空间",
      "attributes": {
        "layer_kind": "prepared",
        "input_refs": [
          "CHAIN-R"
        ],
        "transformation_rule": "技术规则统一日期/类型；异常隔离，不覆盖原始",
        "business_purpose": "供不同用途复用",
        "owner": "数据工程师",
        "quality_controls": "数量类型/站点键规则；异常留记录",
        "protection_controls": "角色授权，不任意扩散",
        "metadata_lineage": "规则版本TECH-1/处理作业RUN-11",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "reference_identity": "project-tailored-value-chain; not-mandatory-TOGAF-pipeline",
        "evidence_detail": "虚构U1数据流程访谈与TECH-1/BUS-1草案"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "CHAIN-I",
      "type": "ops:bi_value_chain",
      "name": "缺件信息数据",
      "attributes": {
        "layer_kind": "information",
        "input_refs": [
          "CHAIN-P"
        ],
        "transformation_rule": "项目业务规则：需求数量大于可用数量则候选缺件",
        "business_purpose": "支持U1上门前复核",
        "owner": "运营产品负责人",
        "quality_controls": "业务规则经调度复核；尚未证明源及时性",
        "protection_controls": "看板去掉客户联系方式",
        "metadata_lineage": "业务规则BUS-1/U1/字段定义",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "reference_identity": "project-tailored-value-chain; not-mandatory-TOGAF-pipeline",
        "evidence_detail": "虚构U1数据流程访谈与TECH-1/BUS-1草案"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "CHAIN-V",
      "type": "ops:bi_value_chain",
      "name": "缺件业务视图",
      "attributes": {
        "layer_kind": "business-view",
        "input_refs": [
          "CHAIN-I"
        ],
        "transformation_rule": "语义层解释时点、站点与缺件含义，人工复核后调拨",
        "business_purpose": "调度主管决策",
        "owner": "调度主管",
        "quality_controls": "每次展示观测时间，过期转人工查源",
        "protection_controls": "仅调度角色可读",
        "metadata_lineage": "语义字典SEM-1/用途U1",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "reference_identity": "project-tailored-value-chain; not-mandatory-TOGAF-pipeline",
        "evidence_detail": "虚构U1数据流程访谈与TECH-1/BUS-1草案"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [
    {
      "id": "CHAIN-R1",
      "type": "ops:data_derivation",
      "source": "CHAIN-S",
      "target": "CHAIN-R",
      "label": "提取原始副本",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "CHAIN-R2",
      "type": "ops:data_derivation",
      "source": "CHAIN-R",
      "target": "CHAIN-P",
      "label": "技术准备",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "CHAIN-R3",
      "type": "ops:data_derivation",
      "source": "CHAIN-P",
      "target": "CHAIN-I",
      "label": "业务转换",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "CHAIN-R4",
      "type": "ops:data_derivation",
      "source": "CHAIN-I",
      "target": "CHAIN-V",
      "label": "语义与消费",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "ops:data_derivation": {
        "source_types": [
          "ops:bi_value_chain"
        ],
        "target_types": [
          "ops:bi_value_chain"
        ],
        "meaning": "数据派生/流转，源向目标，具体转换在目标transformation_rule"
      }
    }
  },
  "states": [],
  "view": {
    "id": "v-bi-value-chain-controls",
    "artifact_id": "bi-transition-architecture",
    "profile_id": "bi-value-chain-controls",
    "title": "BI数据价值链、语义与控制",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "CHAIN-S",
      "CHAIN-R",
      "CHAIN-P",
      "CHAIN-I",
      "CHAIN-V"
    ],
    "relationship_ids": [
      "CHAIN-R1",
      "CHAIN-R2",
      "CHAIN-R3",
      "CHAIN-R4"
    ],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-value-chain-controls --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-value-chain-controls --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
