# TOGAF 本地 skills 包

17个技能入口和共享执行器，使用已保存的六卷基础标准、26份指南及G226、W242C。中文分析与完整中文译文分开记录，六卷874小节与G226的75节正文已译写，W242C中文原文逐页保全；不同评审人的最终语义验收待完成。

当前处于本地工程稳定化阶段。原生 UML 2.5.1 / BPMN 2.0.2 编辑、校验、导出和预览按能力范围返回诊断；局部正反例通过不代表完整设计时能力。全量资料独立复核、完整标准义务、当前版本 507 项独立评测与正式入口切换尚未完成。当前结论只由显式轮次清单及实际证据判定；人工专业验收与真实组织批准保持待签署。

```bash
python3 -B _shared/scripts/local_tool.py doctor
python3 -B _shared/scripts/local_tool.py query '库存 一致性 过渡架构'
python3 -B _shared/scripts/local_tool.py validate work/model.json --report work/validation.json
python3 -B _shared/scripts/local_tool.py generate work/model.json --out work/output --all --render --strict
```

从[工作台](togaf-architecture-workbench/SKILL.md)选择任务，按[已审阅方法路由](_shared/references/reviewed-method-routing.md)读取实际来源。执行约定、依赖和安装说明见[本地包说明](_shared/references/local-package.md)。本包不会自动将来源技能等级变为AI权限或人员认证，不安装到外部技能目录。

保留17个技能目录与`_shared/`同级；所有运行输出放`work/`。`upstream-manifest.json`记录外部只读技能的复制指纹和本地修订；`reading-link-manifest.json`记录阅读链接派生改写。`_shared/corpus/source-map.json`把历史来源身份映射到包内同字节副本。上游出版物版权及许可保留，打包不改变其许可条件。

阅读基础定义和限定条件时，可直接使用[六卷中文正文](_shared/corpus/fundamental/chinese-text/README.md)、[G226/W242C正文](_shared/corpus/supplementary/chinese-text/README.md)；其英文来源块及原图同时保留。理解ADM、制品和不同“上下级”关系，见[系统解释](_shared/references/togaf-explained.md)。
