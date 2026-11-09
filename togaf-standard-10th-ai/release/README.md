# TOGAF skills工程预览交付

本目录交付可迁移工程包。六卷基础标准874个编号小节、3522个来源块，以及G226的75节中文正文均已译写，W242C中文原文逐页保全。不同评审人的最终语义验收仍待完成，真实业务批准未授予。

- [skills源码、规范、字体及本地资料包](togaf-skills-engineering-preview.tar.gz)：17入口、共享执行器、当前来源和5版可编辑案例。不包含node_modules、Python环境或浏览器。
- [归档指纹及校验结果](release-manifest.json)：源码归档每个文件与封存清单逐字节核对；原件版权、许可证和原始引用保留。
- [实施证据与未完成项](../quality/implementation-ledger.md)。

在目标目录解包：

```bash
tar -xzf togaf-skills-engineering-preview.tar.gz
cd skills
python3 -B _shared/scripts/local_tool.py doctor
```

可选离线Node依赖包名称、平台和SHA-256见归档清单，在同一目标目录解开，使其位于`skills/_shared/node_modules/`。该依赖包仅适用于本次macOS本机平台；Python依赖、Node运行时及Chrome/Chromium未随包提供。其他环境按[包内依赖说明](../skills/_shared/references/local-package.md)及锁文件准备。

保留17个技能目录与`_shared/`同级。解包到任意自选位置不会自动注册为全局技能；本轮未向外部技能目录安装任何内容。所有运行输出放包内`work/`。

隔离副本的检索、模型校验、生成与渲染证据见[迁移检查](../quality/portability-validation.json)。这证明已测试本机的路径独立性，不是所有平台的运行认证。
