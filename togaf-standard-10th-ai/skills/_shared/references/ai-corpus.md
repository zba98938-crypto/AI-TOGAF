# 本包当前解析与本地原文

资料随`_shared/corpus/`一起提供，不依赖原项目目录。覆盖计划内六卷基础标准、26份系列指南及G226、W242C，出版物类型和版本分别保留。范围不是全球TOGAF出版物全集。逐节中文分析与完整中文正文的状态分别记录；六卷874小节、3522来源块以及G226的75节正文已译写；不同评审人的最终校核尚未完成。

从skills包根目录执行：

```bash
python3 -B _shared/scripts/local_tool.py query '业务能力 价值流' --limit 5
python3 -B _shared/scripts/local_tool.py query '架构角色 技能' --document G249 --limit 3
python3 -B _shared/scripts/local_tool.py query 'Requirements Management' --document C220-web-2025:02-architecture-development-method --limit 3
```

当前检索读取章节校订、当前架构解释、扩展语义分析和来源对应中文正文。查询返回包内相对路径、来源定位及指纹。命中只是定位；必须阅读完整章节、原文内容块及相邻上下文，不能以关键词或字段齐全代替理解。

- [指南目录](../corpus/index.json)、[当前章节校订](../corpus/chapters/index.md)、[基础与补充解析](../corpus/quality/extended-publication.json)。
- [当前图示解析](../corpus/figures/current-analysis.md)、[角色和技能](../corpus/architecture/roles/skills.json)、[来源到任务和方法关系](../corpus/architecture/source-method-graph.json)。
- [历史来源身份的包内映射](../corpus/source-map.json)；PDF同字节副本在`corpus/sources/pdf/`，网页原文和离线资源在`corpus/fundamental/web-2025/volumes/`。

PDF使用物理页和内容块；网页使用卷、标题锚点和内容块，不编造页码。区分原始PDF指纹、抽取JSON指纹与分析文件指纹。历史原始路径只作来源身份，按本包映射定位。

区分官方陈述、解释性推导和项目规则。不得把视觉包含解释成人事汇报，把能力实例当子能力，或把缺失技能列填成官方等级。G198/G249量表和角色身份分别保留；W242C的AI训练不等于G249人的Training技能。

历史`source_*`及已否定解释保留审计用途，默认检索不采用它们。外部原始引文URL是出版物元数据，不表示本轮联网检查。角色目标、真实项目事实、观察证据、容量、期间和业务批准必须分别取得依据。

实际正文入口：[六卷逐块中英对照](../corpus/fundamental/chinese-text/README.md)、[G226与W242C](../corpus/supplementary/chinese-text/README.md)。G226中文按节连续译写，原PDF每个来源块完整保留；W242C为现有中文原件，不伪称新译本。
