# 云与外包环境数据共享契约

服务提供方应以哪些边界和口径交付可审查环境数据？

依据：G242 §6表6-1。实际读过对应中文正文与既有逐节审计；本轮未重做英文/原图或外部标准核验。字段为项目操作规范。

## 输入与缺口

组织、服务、业务用途及所评估期间/生命周期边界；原始访谈、使用数据、供应商记录及稳定证据ID；适用目标、职责和组织自定决策规则；未知项显式登记。关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 字段

| 字段 | 含义 |
|---|---|
| name | 数据项名 |
| sequence | G242拟议19字段顺序 |
| field_key | 稳定字段key |
| value | 供应方原始值，未知显式保存 |
| unit | 原始单位 |
| period | 该值测量期间 |
| service_boundary | 服务/组织实体/生命周期/分配边界 |
| semantics | 互斥、包含、抵消、复制等含义 |
| evidence_refs | 供应方报告/方法证据ID |
| quality | 完整/未知及口径待确认 |

## 分析步骤

1. 确认提供方、服务、使用实体、期间与服务分配依据
2. 按拟议19字段逐项收集原始值和单位、测量期间
3. 同时保留市场/地点Scope2，设备Scope3包含关系及抵消独列
4. 检查年度/月度、制造/运行水、复制存储与进出流量口径
5. 给缺口/冲突清单后交给独立核算方法；不在数据契约中自动合计排放

## 完整虚构案例

原料（历史材料已清理）组`cloud`。逐行保留G242表6-1拟议最小数据集：Scope2两法并行不相加；设备6000为Scope3总9000子集；抵消5000独列；存储6000含复制。制造水未知，不能宣称全生命周期数据完全。

`artifact_id=cloud-environmental-data-contract`；`profile_id=cloud-environmental-data-contract-default`；`view_id=v-cloud-environmental-data-contract-default`。结果见初始表（历史材料已清理）与修改表（历史材料已清理）。

## 修改与反例

修改：Scope3设备子集从6000更新为7000，总额仍9000。预期：子集更新且仍不相加；两种Scope2与抵消保持独立。

反例：设备子集10000大于同边界Scope3总9000；或要求把两种Scope2相加。预期：scope3-subset-exceeds-total或scope2-bases-not-additive。

## 质量与追溯

- G242提出数据共享模型，不宣称已成为国际标准
- Period允许年/月而若干描述写完整年度，必须逐值声明期间，不自动年化
- 供应方scope标签与消费者组织范围归属不同
- 市场法和地点法不能相加，设备子集不与Scope3总量相加，抵消不抵掉报送原始值
- 复制后存储量不是逻辑原始数据；制造水未知不能记零

执行证据（历史材料已清理）证明模型/生成/修改/规则反例及表内表达，不能替代独立业务评审。表格不计SVG/PNG视觉通过。

## 拟议共享字段（19项）

| 字段key | 名称 | 单位 | 语义 |
|---|---|---|---|
| provider_name | 提供方名称 | text | supplier identifier |
| provider_evaluated_service | 被评估服务 | text | specific service |
| concerned_organization_entities | 相关组织实体 | list | customer entities |
| period | 期间 | year/month | reporting period; annual definitions remain explicit |
| electricity_consumption_kwh | 用电量 | kWh | gross allocated service electricity |
| renewable_electricity_purchased_kwh | 采购可再生电力 | kWh | purchase disclosure; not a subtraction |
| scope2_market_based_kgco2e | Scope2市场法 | kgCO2e | alternative accounting basis; do not add to location-based |
| scope2_location_based_kgco2e | Scope2地点法 | kgCO2e | alternative accounting basis; do not add to market-based |
| pue | PUE | ratio | hosting efficiency; included-allocation must be declared |
| scope2_calculation_comments | Scope2计算说明 | text | optional comments; explicit missing allowed |
| total_scope3_kgco2e | Scope3总量 | kgCO2e | supplier total allocated to service |
| digital_equipment_scope3_kgco2e | 数字设备Scope3子集 | kgCO2e | subset of total_scope3_kgco2e, not additive |
| scope3_calculation_comments | Scope3计算说明 | text | optional comments; explicit missing allowed |
| carbon_credits_offsets_kgco2e | 碳信用与抵消 | kgCO2e | separate disclosure; do not net reported gross emissions |
| digital_waste_kg | 数字废弃物重量 | kg | disposed equipment in declared period/boundary |
| recycled_digital_waste_kg | 回收数字废弃物 | kg | collected for recycling; boundary/lot must be clear |
| water_consumption | 水消耗 | m3 | manufacturing/use phase split or explicit phase scope |
| stored_data_gb_including_replication | 存储数据量含复制 | GB | include all replicas, distinguish logical original |
| network_traffic_gb | 进出网络流量总量 | GB | inbound plus outbound over declared period |

字段数量来自表6-1；注释字段源文可选，缺失必须显式声明，不能假造解释。其他定量字段缺失给可追溯缺口。
