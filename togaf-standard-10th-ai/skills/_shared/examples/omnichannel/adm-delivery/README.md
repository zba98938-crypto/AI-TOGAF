# 同一情景的ADM与正式交付物

模型含23种候选正式交付物、90章具体论证、33视图，与9阶段/94来源步骤在同一模型及周期中关联。原始材料和本轮新增的交付物材料补充位于materials/；新增计划是作者提案，未冒称旧情景已审批新文档。全部候选，真实批准及全范围独立业务接受未授予。

从skills包根目录执行：

```sh
python3 -B _shared/scripts/local_tool.py validate _shared/examples/omnichannel/adm-delivery/model.json --report work/adm-delivery-validation.json
python3 -B _shared/scripts/local_tool.py adm check --model _shared/examples/omnichannel/adm-delivery/model.json --cycle _shared/examples/omnichannel/adm-delivery/cycles/cycle.json --require-complete --require-source-coverage
python3 -B _shared/scripts/local_tool.py generate _shared/examples/omnichannel/adm-delivery/model.json --out work/adm-delivery --all --strict
python3 -B _shared/scripts/local_tool.py adm report --model _shared/examples/omnichannel/adm-delivery/model-policy-v2.json --cycle _shared/examples/omnichannel/adm-delivery/cycles/cycle.json
```

最后一项应显示政策2→1件、24→8小时改变后旧记录需要重审。文本/JSON/适用SVG实际生成不代替PNG目视或专业语义验收。应用迁移排期只选有给定窗口的工作包，生产应用迁移日期未知。

[输入材料](materials/adm-delivery-materials.json) · [阶段映射](stage-deliverable-map.json) · [仅路径重定位记录](relocation-record.json)
