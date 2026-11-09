# DBRM四域十要素适用性

制品族 `digital-business-reference-tailoring`；规范 `dbrm-element-applicability`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `dbrm_domain_id`：DBRM参考域ID
- `dbrm_domain`：数字/战略/结构/运营，与TOGAF四域独立
- `element_id`：参考要素ID
- `element`：原要素名称
- `reference_identity`：参考身份
- `local_mapping`：本地业务映射
- `local_evidence`：原料观察ID
- `applicability`：适用性而非成熟度
- `gap`：缺口和待确认
- `tailoring_reason`：裁剪理由
- `relationship_boundary`：不可从图线猜关系

关系：{}

## 分析步骤

1. 区分DBRM域与TOGAF架构域
2. 逐要素映射业务观察，保留不确定性
3. 只将正文明确分类用于参考分类；不猜图3-1关系
4. 记录未来安全/成熟度映射为缺来源

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 四域十要素完整
- 不生成成熟度分数
- 参考图未定向关系不能改成因果

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile dbrm-element-applicability --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/dbrm-reference-mappings.json`
- G21H §1.2、§1.4、§3

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
