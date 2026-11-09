# 六项通用业务案例

原始材料保存在 [business-materials.json](business-materials.json)。同一个虚构全渠道试点连接人员配置、实施因素、差距依赖、架构增量、过渡服务与价值风险；真实批准均为 `not-granted`。角色材料选自已有充分虚构案例的一项任务，其余五项规划材料明确给出业务前提、责任、范围、原始评分和变化记录。

|制品|充分输入|缺输入|业务变更|
|---|---|---|---|
|任务角色配置图|32小时任务、40小时可用量、完整期间与行为观察|可用工时未知，容量不能判足够|任务增至48小时，可用量40小时，保持能力评价而报告容量不足|
|实施因素目录|1000事件、每小时500条、4小时恢复窗口|排空速率未给定，不推断恢复时长|积压增至3000，恢复需6小时，提出容量或范围复核|
|合并差距、方案和依赖|跨渠道事件键差距关联WP-KEY，前置依赖WP-POLICY|依赖未评审，保留null|增加安全审计WP-AUDIT，保留原依赖|
|架构定义增量|工作包向在线过渡交付有明确内容和验收条件|只有连线没有增量说明，保持缺口|新增离线增量，持久受理与中央确认边界明确|
|过渡状态演进|服务分类、SBB、过渡状态与两个门店范围齐备|服务分类未知，不从布局推断|扩至四门店，SBB变为expanded-pilot，容量验证仍待完成|
|业务价值与风险|演练准则、先验日期、权重、原始评分齐备|一项价值权重缺失，不补等权或0|价值评分5降至3，指数4.1改为2.7，风险仍2.8|

`scripts/planning_case_examples.py`从原始材料构造充分、缺输入和变更模型；`example()`为六项注册profile提供充分输入的内嵌片段。包维护的`bind_foundation_contracts.py`会重新安装这些片段，避免重建时丢失。

通用评测的`tests/enterprise/cases.py`将充分输入作为原profile任务，再为每项增加缺输入和变更两项；Actor仅接收业务材料，预选profile/方法路由与评分规则不注入Actor输入。通用`profile_mutations()`对这六项运行同样的18场景，而非任意拼接文本字段。

独立工程oracle位于`tests/enterprise/planning_cases.py`，从原始工作量、事件数、速率、权重和评分重新计算，并检查实际保存的JSON/Markdown、实体、关系方向及跨域依赖；不会读取构建器的计算输出作为预期值。缺输入正确保留和变更正确反映可以通过行为检查，但不会授予业务接受。评测清单接入不表示原生Agent任务已经执行或独立专业验收完成。

从仓库根复现：

```sh
python3 -B togaf-standard-10th-ai/maintenance/prepare_planning_examples.py
python3 -B -m unittest discover -s tests -p test_planning_cases.py -v
```
