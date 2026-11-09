# 百万级虚构企业数据接口

企业：虚构「黔磷寰宇新材集团」，命名空间 `MX-`，与既有黔磷案例行业语境兼容，但不复用其交易记录或真实企业身份。

根目录：`skills/_shared/examples/million-enterprise/`。

| 文件 | 用途 |
| --- | --- |
| `build_dataset.py` | 确定性生成器，默认 1,000,000 笔唯一订单；SQLite 批量写入 |
| `dataset/enterprise.sqlite` | 持久化主数据、百万订单、发运、退货、发票、付款、日生产能源记录 |
| `dataset/rules.json` | 数据单位、模拟设定、范围与分布规则 |
| `dataset/manifest.json` | 实际行数、数据库哈希、种子、运行时间、资产身份 |
| `dataset/oracle-report.json` | 从已保存数据库独立 SQL 重算的完整性、金额、数量及库存检查 |
| `dataset/negative-cases.json` | 独立异常样本及其预期拒绝条件，不污染正常数据库 |
| `derived-facts.json` | 从真实保存的百万级记录聚合的站点、产品、销量/金额/状态、质量及运营事实，附 SQL 与来源标识 |
| `enterprise-brief.md` | 明确为模拟的企业组织、业务能力、应用与数据流、候选目标和关注点 |

`derived-facts.json` 顶层提供 `is_example: true`、`dataset_sha256`、`source_id`、`queries`、`enterprise`、`plants`、`products`、`order_status`、`monthly`、`application_workloads`、`quality_observations`。每个统计附 `query_id`，查询定义可直接在 SQLite 重放。其余架构职责/部署/安全/迁移/预算为 `synthetic_architecture_assumption`，不得混入观测事实。

主表：`orders(order_id,order_day,customer_id,plant_id,product_id,quantity_kg,price_cents_per_kg,discount_bps,net_cents,status,promised_day,channel)`；`shipments(shipment_id,order_id,shipped_day,quantity_kg,event_received_day)`；`returns(return_id,shipment_id,returned_day,quantity_kg,reason)`；`invoices(invoice_id,order_id,invoice_day,net_cents,tax_cents,gross_cents,due_day)`；`payments(payment_id,invoice_id,paid_day,amount_cents)`；`production_daily(plant_id,product_id,production_day,opening_kg,produced_kg,shipped_kg,returned_kg,closing_kg,electric_wh)`。

所有数量为整数 kg、金额为整数分、电能为整数 Wh。业务日期用 ISO 日期字符串，2024-01-01 至 2026-10-31。年/月/日分布有季节性，客户长尾、各产品包装/批量不同、订单年龄影响完成度，发运允许分批，少量退货及晚到消息。生成器逐交易独立取样，不复制小样本凑体量。

架构视图应聚合业务记录并保留查询溯源；百万原始交易是工作负载与业务度量证据，不是要求绘制百万节点。不要把小范围的制品表达验证宣称为全库处理已通过，须同时报告数据库扫描/聚合的实际结果。
