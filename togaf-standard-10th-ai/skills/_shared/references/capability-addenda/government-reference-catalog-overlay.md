# 政府参考目录与本地职责覆盖

制品族 `government-reference-tailoring`；规范 `government-reference-catalog-overlay`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `reference_id`：可携带参考目录稳定ID
- `reference_kind`：sector/function/service分类层级
- `reference_path`：完整路径，同名不能丢上级
- `reference_description`：原目录含义，保持参考身份
- `reference_version`：本地正文sha256，不冒称官方版本审定
- `local_object_ids`：本地职责稳定ID，可多对多复用
- `mapping_type`：项目覆盖/排除/未知，不把分类当本地组织
- `applicability`：适用/范围外/未知
- `reason`：裁剪或映射依据
- `dependencies`：项目依赖及待确认语义，非参考树
- `impact_scope`：变更影响的本地范围
- `source_locator`：章节和源行
- `review_action`：核查/补证行动

关系：{}

## 分析步骤

1. 读取可携带11部门目录并按完整路径定位
2. 从业务职责建立多对多映射，区分参考与本地ID
3. 逐部门明确适用/排除/未知及理由
4. 核对同名路径、变更影响和项目依赖

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 同名养老基金管理保留两个路径和两个职责
- 源目录11部门，不虚构第12项
- 排除必须有范围理由
- 不得将参考分类当能力分解/组织汇报

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile government-reference-catalog-overlay --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/government-reference-catalog.json`
- G21D §1.3、§2.1–12.1、§8.1、§11.1

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
