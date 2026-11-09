"""Replace placeholder parent_id hierarchies with explicit project semantics."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];cap=json.loads((ROOT/'capabilities.json').read_text())
def row(name,**attrs):return name,attrs
CASES={
'security-policy-architecture':('project:policy_specializes','security_policy','父政策在领域的专门化；方向从一般政策到更具体政策，不代表执行流程或组织汇报',[
 row('订单安全总方针',scope='订单、付款与仓库履约',authority='虚构治理委员会提出，批准状态另行记录',accountability='企业风险负责人',policy_level='企业政策',review_cycle='项目规则：每季度及重大变更后',definition='订单与履约信息按已授权职责访问；政策尚属候选'),
 row('客户订单数据处理政策',scope='客户资料及退款交易',authority='数据负责人建议，须治理委员会接受',accountability='客户数据所有者',policy_level='领域政策',review_cycle='项目规则：每季度及处理目的改变后',definition='仅客户服务和退款处理角色可访问对应目的字段；新用途先审查'),
 row('仓库终端访问政策',scope='共享扫描终端与发运状态',authority='运营安全负责人建议，须运营负责人接受',accountability='仓储服务负责人',policy_level='领域政策',review_cycle='项目规则：每月复核账号，重大变更后复评',definition='个人账号登录；离岗撤权；只允许改写所属仓发运状态')]),
'microservice-decomposition-method':('project:service_partition','service_boundary','父业务边界分割为具有生命周期与数据责任的服务边界；非技术进程或部署包含',[
 row('在线订单履约业务边界',business_function='确认订单、预留库存并协调发运',ownership='跨服务架构组协调边界，不共享单一数据库所有权',cohesion='统一客户履约目标，内部可由契约分离',coupling='订单与库存通过预留契约协作',interface='客户提交订单；内部预留和取消契约',data_responsibility='订单状态归订单服务，库存可用量归库存服务',definition='按业务职责拆分，不能按数据表一表一服务'),
 row('订单确认服务',business_function='接受订单、确认付款状态与维持订单生命周期',ownership='订单产品团队',cohesion='订单状态机及客户确认规则一起变化',coupling='通过预留token调用库存服务；不直接写库存表',interface='POST /orders、GET /orders/{id}；输出订单事件',data_responsibility='订单及确认状态；引用预留token不拥有库存可用量',definition='对内聚交易职责建服务，跨服务一致性需补补偿策略'),
 row('库存预留服务',business_function='为指定订单预留、释放及确认库存',ownership='库存产品团队',cohesion='可用量与预留一致性规则由同团队维护',coupling='消费订单取消，向订单返回预留token和到期时间',interface='POST /reservations、DELETE /reservations/{token}',data_responsibility='库存与预留记录；不复制客户付款信息',definition='为超时和取消提供幂等释放；跨服务补偿仍需演练')]),
'architecture-project-wbs':('project:wbs_decomposes','architecture_task','架构项目WBS整体任务分解为可验收子任务；不是E/F变革工作包依赖，也不是批准关系',[
 row('接口与信息使用架构定义',deliverable='DEL-APP-SPEC-v1，两个仓的接口和信息使用说明',work_package='PM-WBS-1，架构项目任务；非TOGAF变革工作包',owner='架构项目经理',effort={'value':8,'unit':'person-day','basis':'虚构团队估算3+5人日'},dependency='输入应用清单版本2需被业务接受',acceptance='12应用覆盖，接口方向和信息使用/修改分开表达，所有未知附ID与责任',definition='分配工作与验收；估算不代表承诺'),
 row('确认应用范围与职责',deliverable='DEL-APPS-v2，两个仓12应用的职责目录',work_package='PM-WBS-1.1，WBS叶任务',owner='业务分析师',effort={'value':3,'unit':'person-day','basis':'本项目估算'},dependency='仓储负责人提供在用系统清单',acceptance='范围内12应用有唯一ID、职责、负责人；双方业务代表确认边界',definition='形成被接受的输入；不能因团队空闲视作已获开始授权'),
 row('分析接口与信息使用',deliverable='DEL-APP-SPEC-v1，接口和信息使用表',work_package='PM-WBS-1.2，WBS叶任务',owner='应用与数据架构师',effort={'value':5,'unit':'person-day','basis':'本项目估算'},dependency='消费已接受DEL-APPS-v2，未知接口指派调查责任',acceptance='所有12应用覆盖；接口证据可追溯，未知带ID，CRUD与信息使用/修改不混同',definition='依赖和授权另有记录；相邻图形不代表自动顺序')])}
package={'profiles':[],'patches':[],'relationship_definitions':{}}
for aid,(rtype,etype,meaning,rows) in CASES.items():
 p=copy.deepcopy(next(p for p in cap['profiles'] if p['artifact_id']==aid and p['id'].endswith('-default')));ex=p['example'];source=ex['sources'][0];source['description']='虚构业务原料：'+'；'.join(name+'：'+json.dumps(attrs,ensure_ascii=False) for name,attrs in rows)
 for e,(name,attrs) in zip(ex['entities'],rows):e['name']=name;e['attributes']=attrs
 definition={'source_types':[etype],'target_types':[etype],'meaning':meaning}
 ex['extensions']={'relationship_types':{rtype:definition}}
 for edge in ex['relationships']:edge['type']=rtype;edge['label']=meaning
 p['relationship_types']=[rtype];p['hierarchy_relationship_types']=[rtype];p['version']='2.2';p['template']['version']='2.2';p['template']['source_verified']=False
 ex['view']['analysis']='从本例原始职责、权限、契约与验收材料形成明确分解。关系类型为命名空间项目语义，来源仅指导方法。父子结构不赋予批准或执行先后。'
 ex['view']['legend']='嵌套只表示已声明的'+rtype+'关系；候选事实、实际批准与实现状态分开。'
 package['profiles'].append(p);package['relationship_definitions'][rtype]=definition
 package['patches'].append({'group':'work_products','id':aid,'set':{'example':ex,'relationship_types':[rtype]}})
path=ROOT/'capability-addenda/hierarchy-example-repairs.json';path.write_text(json.dumps(package,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'profiles':len(package['profiles'])}))
