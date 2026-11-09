# 原生建模语言的虚构教学示例

两个输入均为虚构候选设计，不含真实企业数据或业务批准。

- `order-collaboration.bpmn`：单张显式 BPMNDI 协作图，含两个池、两条泳道、任务、消息开始事件、定时边界事件、排他网关、展开子流程、顺序流和消息流。渲染核对17个可见形状、12条连线及名称；不会补造缺失DI。
- `order-domain.uml`：OMG UML 2.5.1 XML类模型，含Model/Package、三个Class、两个PrimitiveType、属性、操作/参数、两条泛化和一条普通二元关联。关联两端基数明确为1与0..*。类图采用矩形分舱、空心泛化三角、无方向关联线和端点基数；布局新生成，不保全UMLDI。

安装共享包README所列Python依赖，并在共享目录按锁文件执行`npm ci`。BPMN另需现有Chrome/Chromium；可通过`TOGAF_BROWSER_PATH`指定已有浏览器，不自动下载。UML栅格使用resvg，不需要浏览器。

以下`SHARED`指安装后的`_shared`绝对路径；输出目录及文件应是全新的。

```sh
SHARED=/absolute/path/to/skills/_shared
python3 -B "$SHARED/scripts/standards.py" render \
  --language bpmn --version 2.0.2 \
  --input "$SHARED/examples/native-modeling/order-collaboration.bpmn" \
  --out /tmp/native-bpmn-example/order.svg
python3 -B "$SHARED/scripts/standards.py" render \
  --language uml --version 2.5.1 \
  --input "$SHARED/examples/native-modeling/order-domain.uml" \
  --out /tmp/native-uml-example/order.svg
```

每次输出SVG、真实PNG和`.render.json`。退出码0仅表示请求的渲染操作成功；1表示明确错误；3表示缺输入、未支持构造或依赖阻断。报告继续声明`conformance_status=incomplete`与`full_language_acceptance=false`。

BPMN要求单张完整可见DI、零导入警告、语义/DI/实际SVG对象ID一致；折叠子流程内部对象另列为隐藏构造。UML仅支持报告声明的类图子集：未解析或外部类型、聚合/组合、导航关联、接口及其它构造明确阻断；缺省属性/参数基数按UML默认1记录，省略[1]是简写。当前UML容量上限为40分类器、20包、100关系及400特性/参数记录，不表示所有容量点均已做视觉验收。

完整BPMN/UML语义、全部442/673构造、独立视觉/专业接受和业务结果仍未授予；ArchiMate 4须先取得授权规范内容，不能用这两个示例代替。
