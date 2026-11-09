# 虚构全渠道履约示例

从skills包根目录执行。baseline、offline-change、shared-object-change保留未定业务、能力及容量；sufficient与sufficient-policy-change只在声明的虚构证据范围内完成方案比较、角色配置和复评。实际业务批准始终未授予。

```bash
python3 -B _shared/scripts/local_tool.py validate _shared/examples/omnichannel/sufficient.json --report work/validation.json
python3 -B _shared/scripts/local_tool.py generate _shared/examples/omnichannel/sufficient.json --out work/example --all --render --strict
python3 -B _shared/scripts/local_tool.py policy _shared/examples/omnichannel/sufficient-policy-change.json --contract _shared/examples/omnichannel/shared-policy-contract.json --before _shared/examples/omnichannel/sufficient.json --out work/policy-check.json
```

业务原料与人员证据同目录保存。所有时间、人员、评级、测量和政策均为教学数据；输出不代表生产测量或组织已签认。包内来源定位相对skills包根目录。

## ADM全周期演练

[原始材料](adm-business-materials.md)及[共享模型](adm/model.json)关联Preliminary、A—H和持续需求管理94项来源步骤。所有签署、测量与交付均是给定虚构情景，非实际批准。重定位仅改写来源路径及相应输入指纹，见[迁移记录](adm/relocation-record.json)。

```bash
python3 -B _shared/scripts/local_tool.py adm check --model _shared/examples/omnichannel/adm/model.json --cycle _shared/examples/omnichannel/adm/cycles/cycle.json --require-complete --require-source-coverage
python3 -B _shared/scripts/local_tool.py adm report --model _shared/examples/omnichannel/adm/model-policy-v2.json --cycle _shared/examples/omnichannel/adm/cycles/cycle-policy-v2-needs-review.json
```

第二条命令显示政策变化后需要复核的旧记录，不会自动重新批准。

## ADM到正式交付物

[新增同一情景贯通案例](adm-delivery/README.md)将阶段工作关联到23种结构化正式交付物、90章正文及实际生成接口；候选状态和独立业务接受边界保留。此前adm/中的阶段案例与0正式交付物历史仍保留。
