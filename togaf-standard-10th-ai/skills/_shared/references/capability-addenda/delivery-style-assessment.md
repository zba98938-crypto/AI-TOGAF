# 交付风格逐范围比较

来源：G20F §4.7.1 表4-1。此规范扩展既有 `options-decision-matrix`，不新增制品族。

## 输入与缺口

原始材料（历史材料已清理）来自虚构图书馆。需范围、目标、观察、实验、规则来源及有权决策角色。缺证据保留未知，不补默认风格或最优方案。

## 方法

1. 按24个特征提取分范围业务事实，未知保留unknown
2. 对照三种风格的一般画像，解释冲突而非投票
3. 按宏观/微观范围选择单一或混合风格，记录裁剪与负责人
4. 改变风险或范围时重评，不把原选择自动传播给新范围

## 元素与表示

逐字段表保留稳定行ID；风格按范围，备选按option_id与iteration定位。表格相邻不代表依赖；依赖由约束表源/目标显式表示。

```json
{
  "guide:delivery_feature_review": [
    "feature_id",
    "source_guidance",
    "applies",
    "observation",
    "evidence_refs"
  ],
  "guide:delivery_style_decision": [
    "scope_id",
    "styles",
    "owner",
    "rationale",
    "evidence_refs",
    "conflicting_features",
    "tailoring"
  ]
}
```

## 完整案例、修改和评审

初始输入（历史材料已清理）、修改输入（历史材料已清理）、实际执行结果与反例（历史材料已清理）。修改加入收费敏感数据使短信从rapid转混合控制；新并发实验推翻A方案并带证据重开B。评审先核对证据是否改变，再核对选择；不接受直接重写“最佳”结论。

## 调用

`generate.py model.json --profile delivery-style-assessment --layout reference|adaptive --out output`。分析使用 `analyze.py` 的 `delivery-style-review` 方法输入；每次只处理所请求范围。
