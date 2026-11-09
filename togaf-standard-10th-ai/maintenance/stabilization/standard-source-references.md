# 机器来源引用的精确身份诊断

`standards_coverage.py` 在已校验指纹的本地 CMOF/XMI 来源中生成附加引用台账。它分别记录来源文件、登记的逻辑文档 URI、包的 `Package.uri`、原始 fragment、XML 命名空间和类型 QName，避免把“存在同名文件”或“存在同名构造”计为规范来源闭包。

保持现有命令、`native-design-time-coverage/1`、`items`、`missing_machine_imports`、UML `source_identity_provenance` 和全部现有义务 ID。新增字段是 `machine_reference_provenance` 与 `machine_reference_summary`。文件名缺失集合继续作为兼容信息；来源完整性使用新增精确身份门及原有条件判定。完整适用性、语义验收、完整标准能力和真实组织批准均不会由引用诊断自动提升。

## 解析和状态

每个 href 保留原文及源文件 SHA-256、行号、XML 路径和完整来源身份。注册表来自当轮已验证来源的显式 `url`，没有自动生成 HTTP/HTTPS、日期路径、包 URI 或 basename 别名。URI 的标准相对解析与包内路径解析分别执行；仓库范围内合法的 `../` 相对路径可用，越界、符号链接逃逸和危险协议被拒绝。未登记文件只检查路径元数据，不读取其内容。解析仅使用已取得的本地 XML，未登记外部依赖不会触发网络请求。

`xml_base_context` 按根到引用元素的顺序原样保留真正 XML namespace 的全部 `xml:base`，包括空值及每条来源定位，状态为 `base-chain-preserved`。祖先链有任意非空值时，相对 href（含同文档 fragment 和无 scheme 的网络路径）标作 `relative-resolution-with-base-unadjudicated`：不猜测基址迁移，不解析逻辑/物理目标，`local_target` 与 `resolved_target` 均为空，来源门未完成。空的子级 base 不覆盖这个未知处理。已有 scheme 的绝对 href 不受 `xml:base` 改写，仍按其自身精确注册与安全规则判断；全空 base 链保留后可使用既有相对解析。

- `logical_registration_status`：精确登记、未登记、歧义登记或逻辑 URI 不可用。登记的文档 URI 与目标包 URI 分列，不能相互替代。
- `local_file_status`：已登记本地机器文件、缺文件、未登记文件、外部文档未解析及路径/URI拒绝。物理文件可读不等于逻辑来源已登记。
- `fragment_status`：唯一精确 ID、缺 ID、重复歧义或未给 fragment 待裁决。重复 ID 保留全部候选，不按期望类型、同名 owner 或树位置自动选择。
- `type_comparison`：对显式 XMI 类型值使用所在元素的命名空间绑定得到 expanded QName；目标 QName来自其显式 XMI 类型或有命名空间的声明元素。前缀拼写不同而 namespace URI 和本地名相同可以匹配。命名空间不同显式呈现；相同命名空间的不同 metaclass 记为 `type-difference-unadjudicated`，不猜测继承。缺省、未绑定或无效 QName 保持 `unknown-type`。XMI ID/type 属性必须属于已支持的实际 XMI namespace，外来同名属性不作为原生 ID/type。

只有逻辑文档精确登记、登记与本地文件一致、原始 fragment 唯一、QName已绑定且相等的引用才可提供 `resolved_target` 和 `qualified_identity_complete=true`。源码层有未知来源 URI、未知 XMI namespace 或重复原生 ID时，整个机器来源身份门仍未完成。相等 QName是类型标识相等事实，`metamodel_type_conformance` 仍标作未裁决；本组没有实现元类型继承或执行适配。

未登记引用可附带 `unregistered_fragment_inventory_matches`：在所有已取得文件中按**完全相同的原始 fragment**列出声明身份和独立的 candidate QName comparison。此清单不限制同文件名或相近日期，不隐藏多个匹配，也不构成文档映射或 reference type 判定。即使存在唯一同 ID、同 QName 候选，原 URI仍未登记、`resolved_target` 仍为空，完整性仍失败。原始 `Core-Foundation-*` 不去前缀；外部 CMOF String 在本地 DC 中存在同 ID也不能替代其外部文档身份。

## 当前官方材料的实际结果

BPMN 5 个 CMOF共 163 次 href：47 个包内精确 fragment，其中 46 个具备精确逻辑登记与一致 QName；`Infrastructure.cmof` 到 20100502/BPMNDI 的本地 fragment 可读，但清单登记的是 20100501 路由，仍未完成。四个 Semantic 原始 fragment 缺失；112 次外部基础 CMOF依赖显式保留，不能自动接受。

UML/XMI 7 个机器文件共 339 次 href。它们的原始绝对 HTTP逻辑 URI均未在当前 HTTPS取得清单中精确登记，故没有真实 reference target 解析成功。237 条没有显式期望 XMI类型，保持未判定。StandardProfile 的 34 条 Class期望 QName使用 UML/20161101 namespace；已取得 UML同 ID声明的 namespace是 UML/20131001，这个差异只呈现在全局 fragment库存候选比较中，不作为合法 reference解析或命名空间迁移依据。已知 8 组 UML重复原生 ID及旧定位仍保留。

| 现有条目集合 | 数量 | 排序 ID清单 SHA-256 |
|---|---:|---|
| UML 2.5.1 | 5,779 | `1ebf53efcebfee41e3c905d21e44da2e8d0a33bc1d88f8f4aabd6cf45244aa24` |
| BPMN 2.0.2 | 4,147 | `ec17e19fe5252b8432169058a8ecbf80d1c822f2a0d919eaf5aaa38b44c6ff9c` |

## 验证与复现

新测试 `test_standard_source_references` 使用独立构造的本地输入验证真实 URI注册、fragment、QName、歧义、未知类型、路径边界和候选不可升格，并独立解析当前规范核对实际 href、定位、原始片段和 QName候选事实。`test_standards_coverage` 验证既有条目摘要与缺片段/命名空间冲突不能关闭来源门；`test_uml_source_identity` 保留已有重复声明和旧 ID契约。发布证据门也纳入正式验证。

```sh
python3 -B tests/run_native_standard_evidence.py --out output/<新的空轮次> \
  test_standard_source_references test_standards_coverage \
  test_uml_source_identity test_stabilization_standard_gate
python3 -B togaf-standard-10th-ai/skills/_shared/scripts/standards_coverage.py \
  --language bpmn --version 2.0.2 --out output/<新的空文件>.json
```

CLI为尚未完成的规范返回 3，同时输出可审查台账。本轮证据位于 `output/standard-source-references-20261109/`，各次实际执行和诊断分别保留，使用最终交接清单指定当前轮次。首轮规范回归夹具错误地要求未登记 HTTP引用存在本地 target，留下 66 次执行、1 个错误；纠正该断言后，后续轮次按 inventory-only 事实验证。该历史未覆盖或替换。

范围限制：当前登记表不是官方 URI别名或命名空间映射证明；没有下载或替换规范原件，没有裁决全文适用性，没有执行类型继承、语义适配或原 Semantic身份补齐。专业人工验收及组织批准保持待签署。
