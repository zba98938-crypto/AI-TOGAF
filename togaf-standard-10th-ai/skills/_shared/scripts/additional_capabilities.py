"""Distinct reference-view capabilities found by MD/image/JSON comparison.
Rows are operational project contracts; source examples are never project facts."""
ROWS = '''
value-network|价值网络 / Value Network|value|G178/figA-2|diagram/network|value_network_actor|role,value_exchange,beneficiary,conditions|判断多个参与者如何交换有形或无形价值以及网络依赖|确定网络边界和受益者；识别参与者角色；逐方向定义价值交换及对价；识别依赖与失衡；核实每条交换的依据|价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值
lean-value-stream|精益价值流 / Lean Value Stream|value|G178/figA-3|diagram/lean-flow|lean_process|function,lead_time,processing_time,complete_accurate,unit,queue|识别信息物料流中的等待、返工和浪费|确定产品范围和时间边界；记录信息流与工作流；逐流程采集LT/PT与完整准确率；统一时间单位和工作日口径；分析瓶颈和改进机会|精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比
four-box-business-model|四框业务模型 / Four-Box Business Model|business|G18A/fig2-2|diagram/four-box|business_model_component|component,detail,assumptions|评价客户价值主张能否由利润公式、资源和流程支持|明确客户任务与价值主张；定义收入成本利润的候选公式；识别关键资源与流程；检验四框的一致性与约束；记录方案假设和验证方法|四框不能用九块画布或六维立方体的字段替代，利润公式需要明确变量而非捏造收益
business-model-cube|业务模型立方体 / Business Model Cube|business|G18A/fig2-3|diagram/cube|business_model_dimension|dimension,detail,local_mapping|检查价值主张、客户、伙伴、活动、胜任力和价值公式及其关系是否一致|分别界定六个并列维度；采集本地内容并注明来源；只声明有依据的维度间关系；分析价值创造与获取约束；标记关系缺口|中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级
operating-model|运营模式 / Operating Model|business|G184/fig4-1|diagram/quadrant|operating_model|integration,standardization,scope,rationale,quadrant|决定业务流程跨单元集成与标准化的合理程度|界定业务单元和流程范围；分别评估业务流程集成和标准化；按高低组合定位；检验数据共享和治理要求；允许企业内不同范围并存不同模式|两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序
stakeholder-influence-matrix|利益相关者影响力与影响程度矩阵 / Stakeholder Influence-Impact Matrix|vision|G184/fig4-3|diagram/quadrant|stakeholder|influence,impact,engagement,concern,quadrant|依据影响力与所受影响程度选择介入策略|明确决策和关注点；分别取得Influence与Impact证据；按高低定位；选择重点管理令其满意随时告知或监督；核实问责与沟通边界|来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权
balanced-scorecard|平衡计分卡目标与成果 / Balanced Scorecard Goals and Outcomes|strategy|G233/fig4-3|diagram/perspectives|goal|perspective,definition,metric,unit,target,period|从四个视角识别可追溯目标与可度量成果以驱动能力改进|分别提出客户学习成长内部流程财务目标；定义成果度量基线目标单位与期间；用成果实现目标关系连接；继续追溯能力实例；检验指标可验证性|目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链
'''.strip()

def append_rows(original):
    return original+'\n'+ROWS
