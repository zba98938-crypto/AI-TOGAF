# 大规模测试数据生成源码

此目录只保留生成器、独立SQL核算器、聚合工具与数据契约。大型SQLite、失败数据库、投影图片和历史验收结果已从核心包清理。数据全部为虚构测试材料。

按需在技能集合外创建数据：

```sh
python build_dataset.py --out /tmp/togaf-dataset --orders 1000000 --seed 20261104
python audit_dataset.py --dataset /tmp/togaf-dataset
python derive_facts.py --dataset /tmp/togaf-dataset --out /tmp/togaf-derived-facts.json
```

首次使用宜选择小规模输入确认环境，百万测试按需运行；生成数量不证明真实业务能力或化工过程守恒。接口见[数据契约](CONTRACT.md)。
