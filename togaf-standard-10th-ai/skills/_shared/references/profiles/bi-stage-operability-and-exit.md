# BI多阶段运营与退出条件

`profile_id`: bi-stage-operability-and-exit；`artifact_id`: bi-transition-architecture；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G238 §3.2.1–3.2.4。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "bi-stage-operability-and-exit",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:bi_operating_state。关系类型：。

```json
{
  "entities": {
    "guide:bi_operating_state": [
      "state_ref",
      "evolution_kind",
      "data_flows",
      "raw_and_metadata",
      "consumers",
      "incremental_benefit",
      "known_gap",
      "operating_exit_gate",
      "legacy_requirement_coverage",
      "retirement_authorized",
      "cost_basis",
      "schedule_basis"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- step1基线/step2–3过渡/step4目标不混同
- 目标未覆盖旧需求不得退旧仓
- 数据流方向随状态变化要表达
- 无成本/时间依据不估算或强定期限

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/bi-stage-operability-and-exit/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/bi-stage-operability-and-exit/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构图书平台旧仓支持月报与审计。新需求为设备事件分析；先让旧仓清洗数据供新平台，再让交易原始数据和元数据直接进新平台，消费者分批切换。目标拟退旧仓，但OLD-audit尚未证实覆盖，因此退役未获准。没有成本或工期数据。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "BI-P0",
      "type": "guide:bi_operating_state",
      "name": "BI-B",
      "attributes": {
        "state_ref": "BI-B",
        "evolution_kind": "baseline",
        "data_flows": "交易应用→旧数仓→借阅报表",
        "raw_and_metadata": "旧仓无完整原始/元数据",
        "consumers": "借阅月报依旧数仓",
        "incremental_benefit": "已有历史报表可运行",
        "known_gap": "无法分析设备事件",
        "operating_exit_gate": "新需求和已声明容量/成本约束触发；不是自动替换",
        "legacy_requirement_coverage": {
          "OLD-month": "verified-in-example",
          "OLD-audit": "legacy-service-retained"
        },
        "retirement_authorized": false,
        "cost_basis": "未给成本数据，不用“双份存储”推断总成本翻倍",
        "schedule_basis": "无项目工期，不套用指南3–5年叙述"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "BI-B"
    },
    {
      "id": "BI-P1",
      "type": "guide:bi_operating_state",
      "name": "BI-T1",
      "attributes": {
        "state_ref": "BI-T1",
        "evolution_kind": "transition",
        "data_flows": "旧数仓清洗数据→新平台；设备事件→新平台",
        "raw_and_metadata": "只有新增设备原始流，旧源原始不完整",
        "consumers": "旧月报保持；新事件报表在新平台",
        "incremental_benefit": "新增事件分析",
        "known_gap": "双历史存储、旧源血缘不足",
        "operating_exit_gate": "保留旧报表服务；监控双摄取/备份/访问；恢复可切回旧报表",
        "legacy_requirement_coverage": {
          "OLD-month": "verified-in-example",
          "OLD-audit": "legacy-service-retained"
        },
        "retirement_authorized": false,
        "cost_basis": "未给成本数据，不用“双份存储”推断总成本翻倍",
        "schedule_basis": "无项目工期，不套用指南3–5年叙述"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "BI-T1"
    },
    {
      "id": "BI-P2",
      "type": "guide:bi_operating_state",
      "name": "BI-T2",
      "attributes": {
        "state_ref": "BI-T2",
        "evolution_kind": "transition",
        "data_flows": "交易原始/元数据→新平台；新数据可供旧仓；消费者分批切换",
        "raw_and_metadata": "完整原始和相关元数据",
        "consumers": "旧月报与新事件报表双轨迁移",
        "incremental_benefit": "保留原始并支持重加工/血缘",
        "known_gap": "双存储/双摄取运营成本待测",
        "operating_exit_gate": "每消费者对账后切换；维护两平台支持；可按消费者回退",
        "legacy_requirement_coverage": {
          "OLD-month": "verified-in-example",
          "OLD-audit": "legacy-service-retained"
        },
        "retirement_authorized": false,
        "cost_basis": "未给成本数据，不用“双份存储”推断总成本翻倍",
        "schedule_basis": "无项目工期，不套用指南3–5年叙述"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "BI-T2"
    },
    {
      "id": "BI-P3",
      "type": "guide:bi_operating_state",
      "name": "BI-T",
      "attributes": {
        "state_ref": "BI-T",
        "evolution_kind": "target",
        "data_flows": "新平台→全部合格集市；旧仓退出",
        "raw_and_metadata": "项目相关原始/准备/业务信息有治理",
        "consumers": "两旧需求OLD-month/OLD-audit均覆盖证据待确认",
        "incremental_benefit": "目标历史数据单一来源，保留已有报表投资",
        "known_gap": "未覆盖旧审计需求前不得退役",
        "operating_exit_gate": "旧月报和审计需求全部验证，权限/血缘/恢复已演练才退出",
        "legacy_requirement_coverage": {
          "OLD-month": "verified-in-example",
          "OLD-audit": "pending"
        },
        "retirement_authorized": false,
        "cost_basis": "未给成本数据，不用“双份存储”推断总成本翻倍",
        "schedule_basis": "无项目工期，不套用指南3–5年叙述"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "BI-T"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [
    {
      "id": "BI-B",
      "name": "旧数仓基线",
      "evolution": "baseline",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "数仓运维",
        "service_levels": "沿用试点现有人工保障；未承诺新SLA",
        "data_consistency": "保留旧记录/来源映射，按消费者核对迁移期间的一致性",
        "controls": "受控授权与审计",
        "monitoring": "管家监视错配/积压",
        "rollback": "按状态保留旧主控与可恢复记录",
        "operations": "管家与运维值班，服务告警与人工恢复流程保持可用",
        "dependencies": "前置质量与责任条件满足后进入"
      }
    },
    {
      "id": "BI-T1",
      "name": "新平台承接清洗数据",
      "evolution": "transition",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "双平台运维",
        "service_levels": "沿用试点现有人工保障；未承诺新SLA",
        "data_consistency": "保留旧记录/来源映射，按消费者核对迁移期间的一致性",
        "controls": "受控授权与审计",
        "monitoring": "管家监视错配/积压",
        "rollback": "按状态保留旧主控与可恢复记录",
        "operations": "管家与运维值班，服务告警与人工恢复流程保持可用",
        "dependencies": "前置质量与责任条件满足后进入"
      }
    },
    {
      "id": "BI-T2",
      "name": "新平台全量原始数据",
      "evolution": "transition",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "双平台运维",
        "service_levels": "沿用试点现有人工保障；未承诺新SLA",
        "data_consistency": "保留旧记录/来源映射，按消费者核对迁移期间的一致性",
        "controls": "受控授权与审计",
        "monitoring": "管家监视错配/积压",
        "rollback": "按状态保留旧主控与可恢复记录",
        "operations": "管家与运维值班，服务告警与人工恢复流程保持可用",
        "dependencies": "前置质量与责任条件满足后进入"
      }
    },
    {
      "id": "BI-T",
      "name": "新平台单一历史源",
      "evolution": "target",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "新平台运维",
        "service_levels": "沿用试点现有人工保障；未承诺新SLA",
        "data_consistency": "保留旧记录/来源映射，按消费者核对迁移期间的一致性",
        "controls": "受控授权与审计",
        "monitoring": "管家监视错配/积压",
        "rollback": "按状态保留旧主控与可恢复记录",
        "operations": "管家与运维值班，服务告警与人工恢复流程保持可用",
        "dependencies": "前置质量与责任条件满足后进入"
      }
    }
  ],
  "view": {
    "id": "v-bi-stage-operability-and-exit",
    "artifact_id": "bi-transition-architecture",
    "profile_id": "bi-stage-operability-and-exit",
    "title": "BI多阶段运营与退出条件",
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
      "BI-P0",
      "BI-P1",
      "BI-P2",
      "BI-P3"
    ],
    "relationship_ids": [],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "表格表达正文操作语义，不声称原图复刻。未知显式保留，ID稳定。",
    "allow_mixed_evolution": true,
    "state_ids": [
      "BI-B",
      "BI-T1",
      "BI-T2",
      "BI-T"
    ]
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-stage-operability-and-exit --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-stage-operability-and-exit --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
