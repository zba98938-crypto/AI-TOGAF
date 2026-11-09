# 养老业务的政府参考分类裁剪

制品族 `government-reference-tailoring`；规范 `government-reference-tailoring-default`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `reference_level`：sector/function/service
- `reference_path`：来源完整路径
- `definition`：参考定义
- `local_mapping`：本地候选职责映射
- `applicability`：裁剪状态

关系：{"guide:reference_classifies": {"source_types": ["guide:government_reference_node"], "target_types": ["guide:government_reference_node"], "meaning": "目录规定的部门→功能→服务分类方向；不表示本地组织汇报、运行依赖或能力组成"}}

## 分析步骤

1. 按来源目录确定两条路径
2. 用显式reference_classifies关系建立三级分类
3. 用节点属性表达本地覆盖并保持参考身份

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 四条分类关系显式存在
- 不用parent_id猜层级
- 两个同名服务ID和路径不同

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile government-reference-tailoring-default --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/government-reference-catalog.json`
- G21D §1.3、§8.1、§11.1

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
