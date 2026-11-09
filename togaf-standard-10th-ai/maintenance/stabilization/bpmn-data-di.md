# BPMN 数据 DI 局部视图

`bpmn_data_render.py` 与固定的 `bpmn_data_scene.mjs` /
`bpmn_data_render.mjs` 为现有 `bpmn_render` 增加原生数据视图。
源码仍在 `codex/standards-next` 隔离工作树。现有原生包和
`standards.py render --language bpmn --version 2.0.2` 命令保持兼容。

适用范围是明确的单个 Process/Collaboration DI 视图，包含可见 Activity、
Event 和 Process 所属的 DataInput、DataOutput、DataObjectReference、
DataStoreReference 与 DataAssociation。依据 PDF 物理 251、398 页，数据
图示可选；未图示项保存为 `data_depiction_inventory`，不会因省略数据图示
产生模型错误，也不算这些图形已执行验证。折叠 SubProcess 内部数据继续
记录为隐藏项。已有流程视图的严格必要元素检查保持其原有含义。

每个 Bounds、waypoint 与 BPMNLabel 坐标保存原始字符串。浏览器只在调用
已安装符号库时转换数值；源 XML 不改写。实际 SVG 按 BPMNPlane 顺序绘制，
报告逐项记录源平面位置、图形 ID、原始坐标和显式端点。没有 BPMNLabel
坐标时，仅派生标签排版并单独说明来源；不生成节点或连线布局。

PDF 物理 405、441 页规定，当图示端点与模型端点不同才需要显式 DI 端点。
本批缩窄既有 `di-edge-endpoint` 规则：当前平面可唯一推断直接图示数据
端点时，不要求制造冗余覆盖；隐藏或歧义端点必须提供对应 sourceElement /
targetElement。渲染器核对覆盖是否表达原生数据项、所属 Activity/Event 或
其所属 Process 的 Pool，拒绝用无关同级业务对象冒充端点。引用其他视图、
重复图示及无法证明的端点到边的简写均不静默接受。

图形依据为本地官方 PDF：物理 242/244 页输入输出标记，423 页
Table 12.21 数据符号，398 页局部图与 Z-order，405/441/442 页 DI 端点与
连线表达。固定符号调用现有 bpmn-js 18.31.1，PNG 使用现有 resvg 2.6.2；
渲染只加载本机固定库和内嵌字体，外部资源请求全部阻断。

验证位于 `output/bpmn-data-di-20261109/`。16 项新增测试在 `attempt-04`
实际通过；`regression-02` 联合执行当前 Data/Comp、引用、设计时、原生渲染
和公开 CLI 共 125 项，失败、错误、跳过均为零。运行期间另一个资料测试
文件变化，正式 runner 因此保留 `passed=false`，本组不将它当作全工程
源码冻结证据。root 统一冻结后仍需全量正式验证。此前失败日志与图像保留。

`visual-qa-04` 保存当前源码实际产生的原生模型、SVG、PNG 和报告。与本机
官方 Table 12.21 对照，输入空心箭头、输出实心箭头、集合三条竖线及数据
存储符号一致；两个视图的标签、连线、业务端点及折叠图形经 agent 视觉复核。
这不等于人工专业验收或真实组织签署。旧图像中的标签相交与局部视图端点
位置问题记入视觉历史，不覆盖旧图像。

`bpmn-data-di-binding-additions.json` 是 9 条独立、可追加的源绑定，与此前
Data/Comp 的 30 条不重叠。全部保持有限夹具验证状态，未宣布整个构造、
交换要求或规范正文义务完成。

复现：

```sh
TOGAF_BROWSER_PATH=/Users/Shared/ai-togaf-browser-20261106-01/chrome-headless-shell-mac-arm64/chrome-headless-shell \
python3 -B tests/run_native_standard_evidence.py --out output/<new-empty-round> \
  test_bpmn_data_di test_bpmn_data_compensation test_bpmn_reference_semantics \
  test_bpmn_design_time test_bpmn_render test_native_standard_cli
```

SequenceFlow 数据简写、混合 choreography 数据视图、MI inputDataItem /
outputDataItem 角色到类型映射、受控渲染调度器的新 backend 接入及全部图形
义务的完整覆盖仍需独立验证。本批未执行模型会话；完整 507 项、人工专业
验收和组织批准均由后续正式轮次单独记录。
