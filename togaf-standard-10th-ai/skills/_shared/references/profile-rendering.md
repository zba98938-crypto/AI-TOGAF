# 视图模板与表达覆盖

渲染入口是 scripts/profile_render.py 的 render_profile(model, view, profile, layout)。返回可编辑 SVG 与表达覆盖记录；PNG 由同一 SVG 和字体生成。16 个模板族的参数位于 templates/。这是一套项目生成接口，具体来源图等价状态按 profile 单独维护。

## 模板与实例

- artifact_id 标识制品族；profile_id 标识具体视图规范；view.id 标识实际输出。两种布局共享同一选择集和稳定对象 ID。
- reference 使用固定语义结构或 profile.template.positions 给出的参考位置；adaptive 允许按对象数量重新布局。没有经过独立来源核验的模板始终保留 source_verified=false。
- 只有 source_verified=true 才表示维护者已经完成来源结构核验。执行生成器不能自动设置此值，布局相似度、工程测试或 JSON 的历史忠实度标签也不能替代核验。

## 参数约定

| 模板族 | 关键字段与语义 |
|---|---|
| nested-map | category 分类带；显式分解、包含、聚合、组合与视觉包含均保留原关系类型，不因嵌套而改称分解；reference/adaptive 的列数可配置 |
| heatmap | score_field、实体 dimension/scale/colors、scale_id 或 measurements 引用模型量表；显式 anchors/colors 决定填色，字符串量表不足以定义颜色；future-absent 单列表示未来尚不存在 |
| stage-map | value_stage 按 ordinal/order 排列；stage_id 标记所属阶段；capability_instance 的 instance_comprises/contains 等关系嵌套组成；instance_of 保留类型追溯 |
| network | 明确端点、关系类型、方向、确定性和说明；reference 可用 positions；边绕过节点，双向边使用不同端口 |
| canvas | template.canvas_type 选择 bmc、four-box、environment、customer-portrait 或 custom；regions 可声明标签至位置/跨度映射；block 对应该画布标签，不能把非 BMC 画布强塞入九块结构 |
| value-chain | category 区分主要与支持活动；支持活动横带位于主要活动之上；不推断价值流步骤或利润值 |
| er | 属性列表、key/primary_key、可选性、类型；每端 min/max 或 unknown；有界基数保留原数值 |
| sequence | 选定对象均可作为参与者；每条消息需要明确 order；不把备选机制虚构成时间顺序 |
| state | 状态及有条件/触发说明的 transitions_to；项目关系图不自动声明为严格 UML |
| deployment | 显式 located_at/member_of_zone/within_boundary/contains 等关系决定容器或边界；跨边界关系仍需明确方向与说明 |
| roadmap | 明确 start/end 或 start/duration_days 时画时间条；缺日期时显示状态和依赖，不猜测排期 |
| matrix | template.row_types/column_types 定义坐标；单元保留 codes 或关系标签；空白显示未记录；必要行列属性在同 ID 明细区表达 |
| causal | polarity 显示正负影响；loops 作为显式回路登记，强化/平衡的计算需另验证完整边集 |
| quadrant | quadrant 明确四区归属；没有轴名和量表时不添加高低坐标意义 |
| assessment/catalog | 保留维度、分数、单位、量表、证据等字段的评分卡或目录；不自动聚合、排名或判定通过 |

## 表达完整性与边界

SVG 图元保留 data-entity-id 和 data-relationship-id。关系标签过长时，图中编号与图内完整关系清单对应，关系类型、属性、代码和数量不得丢失。

coverage.json 分别报告被表达的对象、关系与属性、遗漏、错误和警告。缺少必要字段、不认识的区块、未知时序、不能定位的端点、无法避让的连线均保留诊断。只有 JSON 留存而图形未表达的字段，不能算图形已表达。

生成状态默认为 generated-awaiting-review；有必要信息遗漏或错误时为 draft-with-gaps。最终仍应核对关系是否可读、节点边界、方向、基数、图例和空间语义。此接口不自动证明业务推理正确、控制有效、来源等价或正式批准。

## 超大图的安全栅格输出

`generate.py --render` 对超过 16,000,000 像素或单边 16,384 像素的 SVG 使用显式 `oversized_policy=tile`：保留完整 SVG，使用 Chromium 将同一拓扑按原始像素尺寸裁成不超过 2048×2048 的 PNG 分块，并输出 `*.tiles.html` 浏览器拼接视图和 `*.tiles.json` 清单。不是将图替换成对象目录，不静默缩图，也不生成不存在的单张 PNG 链接。没有明确分块策略的独立渲染任务仍然阻断超大位图。

每张分块及清单、浏览器视图都纳入生成清单的 SHA-256 与 `output_check` 检查；`monolithic_capacity_claimed=false` 明确表示不能据此声称单图容量通过。总像素仍限制在 512,000,000、最多 512 块；超过预算保留 SVG 并阻断。分块依赖可用的浏览器，不能绕过原生沙箱的浏览器限制。Mermaid 自身的源码/边数限制和人工视觉验收仍单独保留。

通用网络 adaptive 布局在超过 64 个对象时使用紧凑网格；大型图的正交路由优先验证无需全局坐标网格的候选路径，仍检查全部节点障碍，不省略关系。`tests/verify_large_render_repair.py --out NEW_OUTPUT` 可对网络、矩阵、路线图和目录的 100/1000 对象场景重新验证；它不代表全部视点的容量认证。

## 可运行检查

tests/test_profile_render.py 验证分类与评分改变输出、嵌套、画布区块、实例复用、参与者完整性、基数、缺失输入和边路由等行为。scripts/render_profile_examples.py --out OUTPUT --render 实际生成 16 族、两种布局的 32 对 SVG/PNG。示例为渲染器练习；全套技能的来源对标与业务正向验收另行记录。
