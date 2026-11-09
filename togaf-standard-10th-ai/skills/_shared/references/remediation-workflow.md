# 双案例与图形证据工作流

用于完整ADM、参考图复核、版本化需求变更或F01–F12复验。读取本技能专属方法后，按关注点选择视图，不能把参考案例当企业事实。

## 建模和生成

- 仓储库组成由显式 contains 决定；外部标准与参考模型分别采纳到对应分区。
- 全景的 breadth、abstraction、time 是坐标；切片必须与实际选择的坐标交集一致。图为类别坐标的展开投影，不表示可量测的几何尺度。
- 安全参考模式核对21概念、P/A共享、E/RM关联及15新增标记。企业裁剪用 view.topology_tailoring = {mode:"project", scope:"适用范围", reason:"逐项理由", omitted_concepts:[...]}; 不能以裁剪标志掩盖错误关联。
- 排期的 milestone 字符串仍是说明。只有 type=milestone、attributes.milestone=true 或 attributes.kind=milestone 才绘制菱形；里程碑起止必须同日。parent_id 支持递归层级；iteration_id 区分同范围多轮ADM，未提供则标为范围汇总。
- `generate.py ... --strict` 拒绝语义/表达错误；默认模式保留显式缺口草稿。完整输出后再做来源和业务评审。

## 图形与明细

长元数据图使用SVG概览与按类型分组、每组8对象分页的HTML明细；主图有明确导航。对象/关系沿用相同ID。coverage的expression_locations分别列真实主图、伴随页和稳定锚点；未输出内容不计已表达。关系只在明细出现时不能宣称主图已有连线。

EA服务×ADM用 `ea-service-adm-matrix` 表达企业映射，`ea-service-adm-reference-matrix` / `ea-service-adm-reference-table` 表达来源参考；未知、明确无关系、不适用、来源未标注分别记录。G217开发支持分类G格保留不确定性。MSA用 `msa-federated-governance-diagram` 区分图5-2六要素与图5-1四层关系，用 `msa-source-deployment-diagram` 表达源码、无业务库、部署和执行链。所有入口保留既有表格和ID。

## 可重复验收

```sh
skills/_shared/.venv/bin/python skills/_shared/scripts/run_remediation_acceptance.py --out output/togaf-remediation-new
```

生成新的测试日志、全量双布局图、字段变更与反例、双案例22份交付物、阶段和需求变更证据、来源入口复核和对照画廊。历史输出保持原状。可用 `--stages tests` 等指定阶段；单次独立运行必须使用新目录。

单案例复验：

```sh
skills/_shared/.venv/bin/python skills/_shared/scripts/enterprise_acceptance.py --case lingang --out output/lingang-new
skills/_shared/.venv/bin/python skills/_shared/scripts/enterprise_acceptance.py --case qianlin --out output/qianlin-new
```

两案均为模拟设计研究、待专业评审。软件模拟只验证设计规则，真实温控仪表、LIMS/MES、现场隔离恢复、业务签章和报价另行取证。工程验证、来源核对、专业评审、业务批准分别记录。C220全文缺失限制标准覆盖范围，不宣布官方等价或认证。
