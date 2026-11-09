# 集合式并行方案逐轮评估

来源：G20F §4.6。此规范扩展既有 `options-decision-matrix`，不新增制品族。

## 输入与缺口

原始材料（历史材料已清理）来自虚构图书馆。需范围、目标、观察、实验、规则来源及有权决策角色。缺证据保留未知，不补默认风格或最优方案。

## 方法

1. 分子系统识别目标与多个备选，并行做足够架构分析
2. 逐轮用可追溯证据保留/淘汰/细化备选
3. 检查剩余组合的跨子系统约束；证据变化时保留重开历史
4. 选定后继续细化并交授权方；记录未验证耦合

## 元素与表示

逐字段表保留稳定行ID；风格按范围，备选按option_id与iteration定位。表格相邻不代表依赖；依赖由约束表源/目标显式表示。

```json
{
  "guide:sbce_iteration": [
    "option_id",
    "subsystem",
    "goal",
    "iteration",
    "hypothesis",
    "assessment",
    "evidence_refs",
    "decision_owner",
    "status",
    "decision_reason",
    "new_evidence_refs"
  ],
  "guide:sbce_constraint": [
    "source_option_id",
    "target_option_id",
    "rule",
    "status",
    "evidence_refs"
  ]
}
```

## 完整案例、修改和评审

初始输入（历史材料已清理）、修改输入（历史材料已清理）、实际执行结果与反例（历史材料已清理）。修改加入收费敏感数据使短信从rapid转混合控制；新并发实验推翻A方案并带证据重开B。评审先核对证据是否改变，再核对选择；不接受直接重写“最佳”结论。

## 调用

`generate.py model.json --profile set-based-options-iteration --layout reference|adaptive --out output`。分析使用 `analyze.py` 的 `set-based-options-review` 方法输入；每次只处理所请求范围。
