# togaf-security-risk 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：风险包含机会，不只威胁

- 判据：风险是「不确定性对目标的影响」，方向可正可负。登记风险时必须能说明它影响哪个目标、影响方向、以及不确定性来自哪里。
- 反例：只登记「服务器被入侵」「数据泄露」这类威胁事件，把「新技术可能带来成本优势」排除在风险登记册外，导致机会无人负责。
- 影响：`business-risk-register` 的记录范围；`risk_appetite` 的边界表述；风险与目标的关联边。

## 判断 2：控制「设计存在」不等于「运行有效」

- 判据：控制的有效性必须分三层记录：已设计（有控制描述）、已实施（有配置或流程证据）、已验证（有测试或审计结果）。只有第三层能支持「风险已降低」的结论。
- 反例：制度文件写着「每季度轮换密码」就判定控制有效，但从未验证是否执行；审计时才发现三年未轮换。
- 影响：`control_objective` 的 `test_result` 与 `evidence_ref`；`security-audit-record`；`risk_treatment` 的残余风险结论。

## 判断 3：风险接受必须由有权者裁决

- 判据：`risk_appetite` 的 `approval_authority` 必须是具名岗位或角色且已有批准证据；`approval_status` 只能由人工置位，生成或渲染成功不改变批准状态。
- 反例：架构模型生成成功后自动把风险偏好标为 `approved`，或以「团队共识」代替有权裁决。
- 影响：`risk-appetite` 的 `approval_authority` 与 `acceptance_boundary`；`approval-without-evidence` 检查；`approval_status` 字段。

## 判断 4：无量化数据时用定性尺度，不伪造损失金额

- 判据：缺少可信的损失分布时，使用明确的定性等级（如罕见／可能／频繁，低／中／高），并给出每级的判定锚点；有量化数据时才计算期望损失。
- 反例：为了「看起来专业」给每个风险编一个金额，导致总风险值与实际完全脱钩，且无人能复核。
- 影响：`risk_asset` 的 `likelihood_scale` 与 `impact_scale`；`business-risk-assessment` 的输出；`risk-explicit-rule` 计算器要求显式规则。

## 判断 5：法规适用性必须有来源与日期，且与政策分离

- 判据：`applicable-legislation-register` 逐条记录法规名称、适用条款、适用主体、生效与截止日期、来源；`security-policy` 是企业自定的规则，可严于法规但不能替代法规登记。
- 反例：把内部安全政策当作法规义务登记，或写「符合《网络安全法》」而不指明适用条款与主体，导致合规评估无法复核。
- 影响：`legal_obligation` 与 `security_policy` 两个类型；`applicable-control-framework-register` 的独立性；`compliance-assessment` 的证据要求。
