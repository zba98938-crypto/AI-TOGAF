# 架构解析与角色能力入口

这里保存架构语义成果：图中是什么、关系如何读、上下级属于哪一种语义、角色负责什么，以及每项技能的参考要求。

- [可筛选浏览器](explorer.html)：按指南、图类型或角色查看原图和分析。
- [全部图示解析](diagrams/index.md)：原图、完整实体/关系、包含树与可编辑 Mermaid。
- [完整ADM框架与架构流程](adm-flow/README.md)：94来源步骤、23交付物、196制品族的阶段映射，以及13张可编辑流程图。
- [角色职责与能力](roles/index.md)：角色要求、输入输出、协作、完整技能等级、版本区别。
- [26 份指南架构分析](index.md)：输入输出、方法、判断依据与应用步骤。
- [概念定义](concepts.md) · [类型化关系](relationships.md) · [机器知识图谱](knowledge-graph.json)。
- [架构验证](validation.md)；[底层文档转换验证](../quality/validation.md)。

转换覆盖及剩余独立视觉审校见[逐项清单](../quality/conversion-coverage.md)。

## 可以直接回答的问题

|问题|读取入口|
|---|---|
|能力、能力实例、价值流阶段是什么关系？|[G233 元模型](diagrams/G233/fig3-1.md)、[关系说明](relationships.md)|
|图中框中框是否是管理上下级？|各图“上下级与包含”及 hierarchy.views；组织汇报另列|
|企业架构师需要哪些技能及等级？|[G249 企业架构师](roles/G249-enterprise-architect.md)|
|首席架构师和分段架构师分别负责什么？|[首席](roles/G249-chief-architect.md)、[分段](roles/G249-segment-architect.md)|
|两个技能框架可以直接互换吗？|[G198/G249 对比](roles/comparison.md)|

## 当前覆盖

- 26 份指南架构分析；94 个概念、97 条跨指南关系。
- 345 条图示分析（架构、流程、矩阵、图例和问卷等），6225 个图内节点、3725 条关系、4121 条包含/分组。
- 56 个角色档案；16 个角色具有原文技能矩阵列，共 1216 项技能等级要求。
- 242 张有本轮视觉核对记录，其中 242 张核对了完整可见内容；102 条独立图元已有原图文字/表格转录。复核范围和未知项逐条保存。

没有独立数值列的角色明确记录“原文未规定”，并分析其文字职责和能力要求。结构层级、业务组成、类型/实例、架构治理和人事汇报分别表示，未知关系不补造。

## 检索

```sh
python3 tools/togaf_corpus/query.py "企业架构师 技能" --role role --doc G249 --limit 3
python3 tools/togaf_corpus/query.py "能力实例 实例化" --role relationship --limit 5
python3 tools/togaf_corpus/query.py "上下级 组织" --role diagram --limit 5
python3 tools/togaf_corpus/build_architecture.py
python3 tools/togaf_corpus/validate_architecture.py
```
