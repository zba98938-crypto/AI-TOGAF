# 年度环境核算：生命周期与组织Scope

`profile_id`: annual-environmental-accounting；`artifact_id`: environmental-is-assessment；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242 §3.6, §3.6.1–3.6.3; Figure3-10；G242 Chapter6; English PDF98–99。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "source_verified": false,
  "layout_notes": "年度核算表采用图3-10的对象与生命周期维度，精确图形等价仍未验收。",
  "review_status": "source-semantics-reviewed-project-form",
  "verification_evidence": "reviews/source-verification/annual-environmental-accounting.json"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：environment_measure。关系类型：。

```json
{
  "entities": {
    "environment_measure": [
      "year",
      "scope",
      "object",
      "lifecycle_stage",
      "unit",
      "value",
      "allocation",
      "evidence",
      "overlap_group",
      "boundary_id",
      "period_kind",
      "value_basis"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 单位、期间、组织边界和来源齐全
- 市场法/地区法不可相加
- 总Scope3与设备子集不可相加
- 毛排放不扣抵消
- 选择统一组织视角并防重复归属
- 月与年口径不明即阻断自动汇总
- 印刷数与复算数分存，不能自动解释为舍入
- 数据缺失时只能称小计或估计，不能称完整实测

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构图书馆完整案例；数据与阈值不是TOGAF规定。",
  "sources": [
    {
      "id": "E-R1",
      "kind": "example",
      "description": "案例核算规则：同一图书馆数字服务，2025/2026均服务30000次预约。组织运营边界、地理范围和功能单位一致。年度电力使用量按地区法，设备非使用阶段按本案例采购分配规则；不用厂商整个LCA值再次叠加运行。Scope1无直接来源的结论来自完整设备清单。所有数值均为虚构教学资料。",
      "locator": "case.json#raw_records/E-R1"
    },
    {
      "id": "E-R2",
      "kind": "example",
      "description": "2026独立服务器电表1000kWh，员工设备电表200kWh，互不重叠。虚构地区因子0.4kgCO2e/kWh。客户终端与本服务相关用电估计100kWh，按明确25%归属比例计入服务；该估计不代表行业通用比例。",
      "locator": "case.json#raw_records/E-R2"
    },
    {
      "id": "E-R3",
      "kind": "example",
      "description": "2026供应商非使用生命周期分配记录：服务器设备120kgCO2e、员工设备60kgCO2e；已含本例定义的生产、运输、维护和报废分配，排除运行用电。分包数字服务30kgCO2e、公网20kgCO2e，均明确不包含云服务与客户终端。",
      "locator": "case.json#raw_records/E-R3"
    },
    {
      "id": "E-R4",
      "kind": "example",
      "description": "云供应商对本图书馆课程预约服务的2026完整年报告：电力300kWh，可再生采购60kWh；提供方Scope2市场法80、地区法110kgCO2e；分配总Scope3为60，其中设备40。报告均为毛排放。Scope1为0已在说明中确认。供应商另披露30kg抵消。本组织不把该供应商抵消冒充自己的抵消。",
      "locator": "case.json#raw_records/E-R4"
    },
    {
      "id": "E-R5",
      "kind": "example",
      "description": "云补充报告：PUE1.2；数字废弃物10kg，其中7kg被收集用于回收；水500L；含复制后的存储120GB；期间总进出网络流量200GB。所报排放已含PUE影响，不再次乘PUE。",
      "locator": "case.json#raw_records/E-R5"
    },
    {
      "id": "E-R6",
      "kind": "example",
      "description": "2025同一边界、同一生命周期分配规则及同一地区法的审定教学记录：服务器电力440、服务器非使用150、云180、分包30、公网20、员工电力88、员工非使用80、客户终端12kgCO2e。2026组织自购抵消40kg，独立登记。",
      "locator": "case.json#raw_records/E-R6"
    },
    {
      "id": "E-R7",
      "kind": "example",
      "description": "供应商更正2026地区法计算因子，提供方Scope2地区法由110改为140kgCO2e。总Scope3仍60，设备子集40不变；原报告保留并由更正版取代，不能两份相加。",
      "locator": "case.json#raw_records/E-R7"
    }
  ],
  "entities": [
    {
      "id": "e-onprem-use",
      "type": "environment_measure",
      "name": "服务器运行",
      "attributes": {
        "id": "e-onprem-use",
        "object": "服务器运行",
        "organization_scope": "Scope 2",
        "lifecycle_stage": "use",
        "activity": 1000,
        "activity_unit": "kWh",
        "factor_ref": "factor-grid-A",
        "allocation": 1,
        "value": 400,
        "unit": "kgCO2e",
        "evidence": [
          "E-R2"
        ],
        "overlap_group": "server-use",
        "year": 2026,
        "scope": "Scope 2",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-onprem-nonuse",
      "type": "environment_measure",
      "name": "服务器非使用生命周期",
      "attributes": {
        "id": "e-onprem-nonuse",
        "object": "服务器非使用生命周期",
        "organization_scope": "Scope 3",
        "lifecycle_stage": "non-use-allocated",
        "value": 120,
        "unit": "kgCO2e",
        "allocation": 1,
        "evidence": [
          "E-R3"
        ],
        "overlap_group": "server-nonuse",
        "year": 2026,
        "scope": "Scope 3",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-cloud",
      "type": "environment_measure",
      "name": "云服务",
      "attributes": {
        "id": "e-cloud",
        "object": "云服务",
        "organization_scope": "Scope 3",
        "provider_scope_refs": [
          "Scope 2 location-based",
          "Scope 3 total"
        ],
        "lifecycle_stage": "allocated-service-lifecycle",
        "cloud_ref": "cloud-lib-2026",
        "value": 170,
        "unit": "kgCO2e",
        "allocation": 1,
        "evidence": [
          "E-R4",
          "E-R5"
        ],
        "overlap_group": "cloud-service",
        "year": 2026,
        "scope": "Scope 3",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R4",
        "E-R5"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-subcontract",
      "type": "environment_measure",
      "name": "分包数字服务",
      "attributes": {
        "id": "e-subcontract",
        "object": "分包数字服务",
        "organization_scope": "Scope 3",
        "lifecycle_stage": "allocated-service-lifecycle",
        "value": 30,
        "unit": "kgCO2e",
        "allocation": 1,
        "evidence": [
          "E-R3"
        ],
        "overlap_group": "subcontract-excludes-cloud-network",
        "year": 2026,
        "scope": "Scope 3",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-network",
      "type": "environment_measure",
      "name": "公共网络",
      "attributes": {
        "id": "e-network",
        "object": "公共网络",
        "organization_scope": "Scope 3",
        "lifecycle_stage": "allocated-service-lifecycle",
        "value": 20,
        "unit": "kgCO2e",
        "allocation": 1,
        "evidence": [
          "E-R3"
        ],
        "overlap_group": "public-network-excludes-cloud-customer",
        "year": 2026,
        "scope": "Scope 3",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-workplace-use",
      "type": "environment_measure",
      "name": "员工设备运行",
      "attributes": {
        "id": "e-workplace-use",
        "object": "员工设备运行",
        "organization_scope": "Scope 2",
        "lifecycle_stage": "use",
        "activity": 200,
        "activity_unit": "kWh",
        "factor_ref": "factor-grid-A",
        "allocation": 1,
        "value": 80,
        "unit": "kgCO2e",
        "evidence": [
          "E-R2"
        ],
        "overlap_group": "workplace-use",
        "year": 2026,
        "scope": "Scope 2",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-workplace-nonuse",
      "type": "environment_measure",
      "name": "员工设备非使用生命周期",
      "attributes": {
        "id": "e-workplace-nonuse",
        "object": "员工设备非使用生命周期",
        "organization_scope": "Scope 3",
        "lifecycle_stage": "non-use-allocated",
        "value": 60,
        "unit": "kgCO2e",
        "allocation": 1,
        "evidence": [
          "E-R3"
        ],
        "overlap_group": "workplace-nonuse",
        "year": 2026,
        "scope": "Scope 3",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "e-customer",
      "type": "environment_measure",
      "name": "客户终端服务分配",
      "attributes": {
        "id": "e-customer",
        "object": "客户终端服务分配",
        "organization_scope": "Scope 3",
        "lifecycle_stage": "use-allocated",
        "activity": 100,
        "activity_unit": "kWh",
        "factor_ref": "factor-grid-A",
        "allocation": 0.25,
        "value": 10,
        "unit": "kgCO2e",
        "evidence": [
          "E-R2"
        ],
        "overlap_group": "customer-terminals",
        "year": 2026,
        "scope": "Scope 3",
        "period_kind": "year",
        "value_basis": "full-year",
        "boundary_id": "boundary-library-digital"
      },
      "evidence": [
        "E-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    }
  ],
  "relationships": [],
  "analyses": [
    {
      "id": "analysis-environment-lifecycle-accounting",
      "method_id": "environmental-annual-accounting",
      "inputs": {
        "boundary": {
          "id": "boundary-library-digital",
          "organization": "虚构市民图书馆",
          "geography": "虚构地区A",
          "service": "课程预约和相关数字运行",
          "period": "2026",
          "period_kind": "year",
          "value_basis": "full-year",
          "functional_unit": "30000次预约/年",
          "scope_perspective": "organization",
          "scope2_basis": "location-based",
          "lifecycle_rule": "运营用电在当期计量；非使用生命周期按E-R1/E-R3声明的采购分配计算；非通用TOGAF公式",
          "coverage_status": "complete-for-declared-fictional-boundary",
          "scope1_status": "zero-with-evidence",
          "scope1_evidence": [
            "E-R1",
            "E-R4"
          ],
          "cadence": "annual",
          "comparison_horizon_years": 2
        },
        "factor": {
          "id": "factor-grid-A",
          "value": 0.4,
          "numerator_unit": "kgCO2e",
          "denominator_unit": "kWh",
          "period": "2026",
          "geography": "虚构地区A",
          "evidence": [
            "E-R2"
          ],
          "origin": "fictional-project-assumption"
        },
        "rows": [
          {
            "id": "e-onprem-use",
            "object": "服务器运行",
            "organization_scope": "Scope 2",
            "lifecycle_stage": "use",
            "activity": 1000,
            "activity_unit": "kWh",
            "factor_ref": "factor-grid-A",
            "allocation": 1,
            "value": 400,
            "unit": "kgCO2e",
            "evidence": [
              "E-R2"
            ],
            "overlap_group": "server-use"
          },
          {
            "id": "e-onprem-nonuse",
            "object": "服务器非使用生命周期",
            "organization_scope": "Scope 3",
            "lifecycle_stage": "non-use-allocated",
            "value": 120,
            "unit": "kgCO2e",
            "allocation": 1,
            "evidence": [
              "E-R3"
            ],
            "overlap_group": "server-nonuse"
          },
          {
            "id": "e-cloud",
            "object": "云服务",
            "organization_scope": "Scope 3",
            "provider_scope_refs": [
              "Scope 2 location-based",
              "Scope 3 total"
            ],
            "lifecycle_stage": "allocated-service-lifecycle",
            "cloud_ref": "cloud-lib-2026",
            "value": 170,
            "unit": "kgCO2e",
            "allocation": 1,
            "evidence": [
              "E-R4",
              "E-R5"
            ],
            "overlap_group": "cloud-service"
          },
          {
            "id": "e-subcontract",
            "object": "分包数字服务",
            "organization_scope": "Scope 3",
            "lifecycle_stage": "allocated-service-lifecycle",
            "value": 30,
            "unit": "kgCO2e",
            "allocation": 1,
            "evidence": [
              "E-R3"
            ],
            "overlap_group": "subcontract-excludes-cloud-network"
          },
          {
            "id": "e-network",
            "object": "公共网络",
            "organization_scope": "Scope 3",
            "lifecycle_stage": "allocated-service-lifecycle",
            "value": 20,
            "unit": "kgCO2e",
            "allocation": 1,
            "evidence": [
              "E-R3"
            ],
            "overlap_group": "public-network-excludes-cloud-customer"
          },
          {
            "id": "e-workplace-use",
            "object": "员工设备运行",
            "organization_scope": "Scope 2",
            "lifecycle_stage": "use",
            "activity": 200,
            "activity_unit": "kWh",
            "factor_ref": "factor-grid-A",
            "allocation": 1,
            "value": 80,
            "unit": "kgCO2e",
            "evidence": [
              "E-R2"
            ],
            "overlap_group": "workplace-use"
          },
          {
            "id": "e-workplace-nonuse",
            "object": "员工设备非使用生命周期",
            "organization_scope": "Scope 3",
            "lifecycle_stage": "non-use-allocated",
            "value": 60,
            "unit": "kgCO2e",
            "allocation": 1,
            "evidence": [
              "E-R3"
            ],
            "overlap_group": "workplace-nonuse"
          },
          {
            "id": "e-customer",
            "object": "客户终端服务分配",
            "organization_scope": "Scope 3",
            "lifecycle_stage": "use-allocated",
            "activity": 100,
            "activity_unit": "kWh",
            "factor_ref": "factor-grid-A",
            "allocation": 0.25,
            "value": 10,
            "unit": "kgCO2e",
            "evidence": [
              "E-R2"
            ],
            "overlap_group": "customer-terminals"
          }
        ],
        "cloud_record": {
          "id": "cloud-lib-2026",
          "provider_name": "虚构云服务商",
          "provider_evaluated_service": "课程预约服务",
          "concerned_organization_entities": [
            "虚构市民图书馆"
          ],
          "period": "2026",
          "electricity_consumption_kwh": 300,
          "renewable_electricity_purchased_kwh": 60,
          "scope2_market_based_kgco2e": 80,
          "scope2_location_based_kgco2e": 110,
          "pue": 1.2,
          "scope2_calculation_comments": "完整年度，均为毛排放；已经含PUE，不再放大。Scope1为0。",
          "total_scope3_kgco2e": 60,
          "digital_equipment_scope3_kgco2e": 40,
          "scope3_calculation_comments": "设备40属于总量60；两者不可相加。完整服务生命周期分配。",
          "carbon_credits_offsets_kgco2e": 30,
          "digital_waste_kg": 10,
          "recycled_digital_waste_kg": 7,
          "water_consumption": {
            "value": 500,
            "unit": "L"
          },
          "stored_data_gb_including_replication": 120,
          "network_traffic_gb": 200,
          "period_kind": "year",
          "value_basis": "full-year",
          "emissions_basis": "gross",
          "evidence": [
            "E-R4",
            "E-R5"
          ],
          "scope1": {
            "status": "zero-with-evidence",
            "evidence": [
              "E-R4"
            ]
          }
        },
        "prior_year": {
          "period": "2025",
          "boundary_id": "boundary-library-digital",
          "scope2_basis": "location-based",
          "functional_unit": "30000次预约/年",
          "unit": "kgCO2e",
          "rows": [
            440,
            150,
            180,
            30,
            20,
            88,
            80,
            12
          ],
          "row_ids": [
            "e-onprem-use",
            "e-onprem-nonuse",
            "e-cloud",
            "e-subcontract",
            "e-network",
            "e-workplace-use",
            "e-workplace-nonuse",
            "e-customer"
          ],
          "evidence": [
            "E-R6"
          ],
          "period_kind": "year",
          "value_basis": "full-year",
          "lifecycle_rule": "运营用电在当期计量；非使用生命周期按E-R1/E-R3声明的采购分配计算；非通用TOGAF公式"
        },
        "offsets": {
          "organization": {
            "value": 40,
            "unit": "kgCO2e",
            "evidence": [
              "E-R6"
            ]
          },
          "provider": {
            "value": 30,
            "unit": "kgCO2e",
            "evidence": [
              "E-R4"
            ]
          },
          "treatment": "separate-no-deduction"
        },
        "rules": {
          "source_refs": [
            "E-R1",
            "E-R2",
            "E-R3",
            "E-R4",
            "E-R6"
          ],
          "aggregation": "sum mutually exclusive rows after same-boundary/time/unit and perspective checks",
          "cloud": "selected provider scope2 basis plus provider total_scope3; never add equipment subset, alternative basis, PUE or offsets",
          "percentage_change": "(current_gross-prior_gross)/prior_gross*100; project convention"
        },
        "source_ids": [
          "E-R1",
          "E-R2",
          "E-R3",
          "E-R4",
          "E-R5",
          "E-R6",
          "E-R7"
        ]
      },
      "evidence": [
        "E-R1",
        "E-R2",
        "E-R3",
        "E-R4",
        "E-R5",
        "E-R6",
        "E-R7"
      ]
    }
  ],
  "view": {
    "id": "library-environment",
    "artifact_id": "environmental-is-assessment",
    "profile_id": "annual-environmental-accounting",
    "title": "年度环境核算：生命周期与组织Scope",
    "entity_ids": [
      "e-onprem-use",
      "e-onprem-nonuse",
      "e-cloud",
      "e-subcontract",
      "e-network",
      "e-workplace-use",
      "e-workplace-nonuse",
      "e-customer"
    ],
    "relationship_ids": [],
    "analysis": "原始陈述、分析规则和修改记录均保留稳定引用；计算只采用显式项目规则。",
    "legend": "虚构图书馆案例。空白矩阵格为未确认；相邻/包含不代表额外关系；规则和数值不是TOGAF默认值。",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "baseline"
    },
    "attributes": {
      "analysis_ids": [
        "analysis-environment-lifecycle-accounting"
      ]
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile annual-environmental-accounting --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile annual-environmental-accounting --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
