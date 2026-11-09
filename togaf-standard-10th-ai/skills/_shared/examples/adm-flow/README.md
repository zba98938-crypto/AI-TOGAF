# 完整ADM架构流程图：可移植运行示例

从当前合同与注册表生成预备阶段、A–H、持续需求管理、各阶段输入／工作／制品／交付物／治理门和ABB／SBB关系。所有候选交付物、制品族与profile均在mapping.json中登记；图面示例不代替完整清单。

在本目录执行，输出必须是不存在的新目录：

```sh
python3 -B ../../scripts/adm.py flow --out /tmp/togaf-adm-flow-new --render

# 另绘已有虚构案例的实际依赖、模型对象与当前检查状态。
python3 -B ../../scripts/adm.py flow \
  --cycle ../omnichannel/adm-delivery/cycles/cycle.json \
  --model ../omnichannel/adm-delivery/model.json \
  --out /tmp/togaf-adm-case-flow-new --render
```

本例复用包内的[全渠道ADM候选交付物案例](../omnichannel/adm-delivery/README.md)。生成过程保持周期只读；未决、过期或不满足判据的工作如实显示。图的实线是常见信息流，实际依赖另从`depends_on`绘制；需求管理是持续过程，不是Phase I。

不加`--render`时仍生成可编辑MMD和嵌入中文字体的SVG，并明确PNG尚未请求。渲染使用当前共享包锁定的本地Node／resvg工具和字体；不联网下载。
