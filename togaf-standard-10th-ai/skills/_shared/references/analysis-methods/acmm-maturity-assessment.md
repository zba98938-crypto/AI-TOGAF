# ACMM 成熟度评价

方法 ID：acmm-maturity-assessment。主责：togaf-ea-capability。来源：G203 §2。步骤与输出结构是本技能的操作约定。

## 输入

- 模型
- 要素特征
- 证据
- 权重或达成规则

## 实际分析步骤

1. 按六级九要素示例裁剪
2. 逐特征评价
3. 分别报告加权等级与级别达成比例

每一步保留输入、转换与结果的追溯。先进行业务判断并记录理由，再把对象和关系写入模型；脚本只在已给出完整规则时计算。

## 显式规则计算入口

模型 `analyses` 条目的 `method_id` 使用 `maturity-weighted`，并提供相应规则、量尺和输入引用。执行 `python scripts/analyze.py model.json --evaluate <analysis-id>`；该命令相对于共享工具目录。计算器只执行已声明规则，不代替证据、方案权衡或批准。输入结构与完整虚构案例见 analysis_cases.py（历史材料已清理） 和 [评价操作手册](../assessment-handbook.md)。

## 输出与评审

- [架构成熟度评分卡](../capabilities/architecture-maturity-scorecard.md)

- 无显式权重与规则不计算统一总分

记录阻断缺口；无明确规则不计算数值或形成确定结论。

修改分析时保留范围、模型版本和稳定 ID，并对输入变化重算或重评。评审分别核对事实证据、方法适用性、运算及结论，不能仅检查文件生成成功。
## 完整操作案例

读取 [用九要素证据形成ACMM评分卡](../method-cases/acmm-maturity-assessment.md)：包含完整虚构原始材料、来源与项目规则、逐步推理、稳定 ID 结果、修改演练、反例和评审记录。 教学材料保留推理、修改和反例说明；历史执行产物已清理，当前模型须重新运行。不要把计算器 ID 与本方法 ID 混用。
