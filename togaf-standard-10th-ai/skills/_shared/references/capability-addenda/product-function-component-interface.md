# 产品功能、组件与接口追溯

制品族 `building-block-description`；规范 `product-function-component-interface`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `product`：产品稳定ID
- `requirement`：功能需求及结果
- `operating_capability`：产品对运营能力的要求
- `component_role`：组件职责
- `technical_component`：技术组件/环境与未知边界
- `sender_ref`：发送组件ID
- `receiver_ref`：接收组件ID
- `operation`：接口操作
- `request`：请求数据语义
- `response`：结果与异常语义
- `security`：授权安全约束
- `version`：独立版本，非批准
- `evidence_detail`：原业务材料

关系：{"guide:allocates_function": {"source_types": ["guide:product_function"], "target_types": ["guide:product_component"], "meaning": "产品功能分配到组件实现；非流程先后"}, "guide:interface_sender": {"source_types": ["guide:product_interface"], "target_types": ["guide:product_component"], "meaning": "接口记录指定发送方组件；非该有向边本身作为数据流"}, "guide:interface_receiver": {"source_types": ["guide:product_interface"], "target_types": ["guide:product_component"], "meaning": "接口记录指定接收方组件；真实请求方向由sender/receiver二者共同定义"}}

## 分析步骤

1. 从体验与需求提炼功能
2. 用明确allocates_function关系分配到组件
3. 声明接口发送/接收、数据与版本
4. 关联运营能力与技术组件，分析功能改变的联合影响

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 每功能有需求与至少一个组件分配
- 接口发送/接收与关系端点一致
- 运营/技术并行考虑，不画成串行流程
- 改变功能时更新接口/组件及运营要求

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile product-function-component-interface --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/dbrm-reference-mappings.json`
- G21H §2产品架构定义、§5.3

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
