# C-MDM四平台态运营计划

`profile_id`: mdm-four-plateau-operations；`artifact_id`: customer-mdm-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §4.4、§6.1.1–6.1.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "mdm-four-plateau-operations",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:mdm_plateau。关系类型：。

```json
{
  "entities": {
    "guide:mdm_plateau": [
      "state_ref",
      "evolution_kind",
      "mastership",
      "golden_record",
      "CRUD_ownership",
      "propagation",
      "use_cases",
      "operating_gate",
      "next_trigger",
      "rollback",
      "scope",
      "source_mapping"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 两个命名transition保留
- 分析黄金态不声称自动双向同步
- 每态有主控/CRUD/可运营门槛/恢复
- 不覆写历史交易事实

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/mdm-four-plateau-operations/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/mdm-four-plateau-operations/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构试点初期三馆源系统各自更新读者。先建立仅用于分析的黄金记录，不同步源；待责任、授权、错合并恢复和事件积压监控验证后，让MDM对约定内核CRUD主控，再扩全馆范围。借阅交易历史保持其历史语境；没有项目日期和成本依据。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MDM-P0",
      "type": "guide:mdm_plateau",
      "name": "MDM-S0",
      "attributes": {
        "state_ref": "MDM-S0",
        "evolution_kind": "baseline",
        "mastership": "源系统",
        "golden_record": "无可信黄金记录",
        "CRUD_ownership": "仅源系统更新",
        "propagation": "仅汇集，不双向同步",
        "use_cases": "历史借阅报表",
        "operating_gate": "已有源记录可供分析但错配未量测",
        "next_trigger": "建立稳定客户键与人工治理",
        "rollback": "源系统保持真源",
        "scope": "读者身份/联络/同意内核，合同与借阅交易不属内核",
        "source_mapping": "G21B表4-6参考态的项目裁剪；不是四个过渡均transition"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "MDM-S0"
    },
    {
      "id": "MDM-P1",
      "type": "guide:mdm_plateau",
      "name": "MDM-T1",
      "attributes": {
        "state_ref": "MDM-T1",
        "evolution_kind": "transition",
        "mastership": "源系统仍为运营主控",
        "golden_record": "有分析黄金记录/稳定组织ID",
        "CRUD_ownership": "源系统更新；管家管理分析记录",
        "propagation": "黄金记录可分发，但不与源自动同步",
        "use_cases": "跨馆读者去重分析",
        "operating_gate": "每次候选合并可人工撤销并留来源",
        "next_trigger": "源质量/SLA/契约验证后才引运营主控",
        "rollback": "停止新分析分发，源系统继续运营",
        "scope": "读者身份/联络/同意内核，合同与借阅交易不属内核",
        "source_mapping": "G21B表4-6参考态的项目裁剪；不是四个过渡均transition"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "MDM-T1"
    },
    {
      "id": "MDM-P2",
      "type": "guide:mdm_plateau",
      "name": "MDM-T2",
      "attributes": {
        "state_ref": "MDM-T2",
        "evolution_kind": "transition",
        "mastership": "C-MDM为约定内核属性主控",
        "golden_record": "运营黄金记录",
        "CRUD_ownership": "内核CRUD通过MDM服务，消费者不得自行写该属性",
        "propagation": "有版本事件分发；重试与幂等按项目规则",
        "use_cases": "读者信息更新和偏好同步",
        "operating_gate": "授权、错合并恢复、事件积压监控通过试点验证",
        "next_trigger": "所有业务范围逐步接入且价值/责任受控",
        "rollback": "冻结写入，按审计重放/恢复到旧主控前先核对数据",
        "scope": "读者身份/联络/同意内核，合同与借阅交易不属内核",
        "source_mapping": "G21B表4-6参考态的项目裁剪；不是四个过渡均transition"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "MDM-T2"
    },
    {
      "id": "MDM-P3",
      "type": "guide:mdm_plateau",
      "name": "MDM-S3",
      "attributes": {
        "state_ref": "MDM-S3",
        "evolution_kind": "target",
        "mastership": "C-MDM约定完整内核范围",
        "golden_record": "制度化可信记录",
        "CRUD_ownership": "责任/生命周期策略一致执行",
        "propagation": "范围内传播受治理；并非所有历史交易改写",
        "use_cases": "全馆合格用例",
        "operating_gate": "业务价值与质量有持续观测，治理长期运行",
        "next_trigger": "持续治理，不是固定日期结束",
        "rollback": "按批准的变更计划恢复；当前仅提案",
        "scope": "读者身份/联络/同意内核，合同与借阅交易不属内核",
        "source_mapping": "G21B表4-6参考态的项目裁剪；不是四个过渡均transition"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "state_id": "MDM-S3"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [
    {
      "id": "MDM-S0",
      "name": "现状归并",
      "evolution": "baseline",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "源系统负责人",
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
      "id": "MDM-T1",
      "name": "分析黄金记录",
      "evolution": "transition",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "数据管家",
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
      "id": "MDM-T2",
      "name": "运营主控",
      "evolution": "transition",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "MDM服务负责人",
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
      "id": "MDM-S3",
      "name": "全范围制度化",
      "evolution": "target",
      "evidence": [
        "case-source"
      ],
      "approval_status": "candidate",
      "implementation_status": "unknown",
      "operating_conditions": {
        "owner": "数据治理负责人",
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
    "id": "v-mdm-four-plateau-operations",
    "artifact_id": "customer-mdm-model",
    "profile_id": "mdm-four-plateau-operations",
    "title": "C-MDM四平台态运营计划",
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
      "MDM-P0",
      "MDM-P1",
      "MDM-P2",
      "MDM-P3"
    ],
    "relationship_ids": [],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "表格表达正文操作语义，不声称原图复刻。未知显式保留，ID稳定。",
    "allow_mixed_evolution": true,
    "state_ids": [
      "MDM-S0",
      "MDM-T1",
      "MDM-T2",
      "MDM-S3"
    ]
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-four-plateau-operations --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-four-plateau-operations --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
