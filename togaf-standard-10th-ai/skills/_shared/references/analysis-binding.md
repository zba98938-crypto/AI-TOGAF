# 分析输入与当前模型的绑定

模型仍使用 schema 2.0。`analyses[].inputs` 内的快照必须与该方法、该视图实际投影的当前模型内容一致；校验和生成共用同一检查。旧分析不能仅因来源和 ID 存在而继续显示过期结论，也不会由校验器自动同步或改写。

模型快照方法依次使用显式绑定、引用该分析的已登记 profile、合同允许且唯一的固定 ID 投影。无法确定时报 `analysis-binding-required`，候选不唯一时报 `analysis-binding-ambiguous`；字段变化时报 `analysis-model-field-mismatch`，错误带对象与字段路径。

显式接口位于 `inputs.model_binding`：

```json
{
  "version": "analysis-binding/1",
  "projection": "full",
  "view_ids": ["selected-view"],
  "selectors": {"record_id": "selected-register"}
}
```

该例适用于支持 `record_id` 的单记录合同；其他方法只能使用各自登记的 projection 和 selector。`view_ids` 指向引用当前 analysis 的视图。不能传任意 JSONPath，也不能把快照型降级为 independent。已有治理检查的 `governance-checks/1` 绑定保持兼容。

场景分析分别检查流程关联、痛点结果、转换审计投影；环境核算分别检查年度行和核算依据投影。某个视图没有投影的历史记录或专业说明不会被强制等同于当前模型对象。内部任务、指标和要求的局部 ID 不要求在全模型范围登记。固定消费字段同时核对存在性，删除快照字段不能绕过检查。

独立评分规则只做来源与输入契约检查；迁移分析保留工作包和过渡引用核验，自由数值和历史观测不会被误当作当前实体快照。`evaluate(analysis, model=None)` 仍可独立计算；没有模型时不宣称完成主模型来源或快照绑定。

证据字段按方法契约识别，包括嵌套证据列表和按判据组织的 `score_evidence`。每个引用须为非空字符串，带模型时必须在 `sources` 中；提供 `source_ids` 清单时还须属于该清单。外部计划、架构和业务目标引用不因字段名称以 `_ref` 结尾而被误认作来源。空证据是否形成缺口由具体方法决定，错误形状始终返回可读诊断。

数值输入拒绝布尔值、非有限数和非标准 JSON 数值常量；计算溢出也会被拒绝。原有单位、区间、项目公式及合法布尔状态字段保持其含义。工程计算、快照一致和证据登记均不等于专业充分性、来源真实性或业务批准。
