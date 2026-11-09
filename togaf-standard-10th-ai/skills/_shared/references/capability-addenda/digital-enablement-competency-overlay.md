# 五支柱十二胜任力与本地责任

制品族 `digital-business-reference-tailoring`；规范 `digital-enablement-competency-overlay`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `source_row_id`：完整12源行引用
- `pillar`：数字使能五支柱
- `competency`：源胜任力名称，运营/运营管理变体单列来源
- `dpbok_context`：I–IV组织规模语境
- `context_kind`：不是成熟度/得分
- `local_roles`：多责任角色稳定ID
- `current_evidence`：已具备能力的观察依据
- `needed_competency`：项目需要的工作能力
- `gap`：缺口，不量化伪评分
- `action`：改进行动与责任
- `next_review`：复评触发或时间
- `reference_identity`：参考表身份

关系：{}

## 分析步骤

1. 逐行读取五支柱十二胜任力及语境
2. 从本地资料识别责任角色与观察证据
3. 区分已观察、未验证与欠缺
4. 用多角色协作和行动填补缺口，不把语境当成熟度级别

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 12行完整且不重复
- 同一胜任力允许多个角色
- 不能把context IV打4分
- 所有缺口有关联行动

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile digital-enablement-competency-overlay --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/dbrm-reference-mappings.json`
- G21H §4.2.2、§4.5.2–4.5.3 表4-1

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
