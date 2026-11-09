# 运营模式四子模型及资源取舍

制品族 `operating-model`；规范 `operating-model-four-submodels`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `submodel`：posture/service/organization/resource四类
- `customer_segment`：目标客户细分
- `decision`：本子模型业务选择
- `implication`：对相关模型的影响
- `linked_submodels`：显式互相约束的子模型ID，不表示层级
- `measures`：成本/前置时间/质量/灵活性/敏捷性独立证据
- `capacity`：带单位/时间/依据的本地资源计算
- `action`：缺口行动
- `evidence_detail`：原料引用
- `reference_identity`：四子模型参考身份

关系：{}

## 分析步骤

1. 由价值主张和客户细分提出战略姿态
2. 定义服务交付、角色交互与所需资源
3. 比较成本/时间/质量/灵活性/敏捷性而不造加权总分
4. 核对资源缺口并调整范围或补充能力

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 四子模型不漏
- 资源缺口必须计算依据/单位/期间和行动
- 未知成本或时长不捏造
- 四子模型不是四象限

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile operating-model-four-submodels --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/dbrm-reference-mappings.json`
- G21H §4.4.2、§5.3

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
