"""Replay author-selected natural-language tasks with actual inputs and outputs.
This records this assistant's task selection, not a blind or independent LLM eval.
"""
import copy,hashlib,json
from pathlib import Path
from registry import ROOT,load
from verify_artifact_profiles import verify_profile,inputs,negative_cases,express

TASKS=[
('togaf-application-architecture','compat-application-communication-diagram','请按原料分析应用职责和通信方向，生成应用通信图，说明它与消息顺序图的区别。','静态通信分析；不把部署位置或调用时序当应用职责'),
('togaf-architecture-workbench','agile-ea-development','请为原料中的EA工作安排开发冲刺，区分准备、产生、评审与DORP门禁，保留协作关系。','按信息依赖组织敏捷协作，门禁合法交叉独立判定'),
('togaf-artifact-review','architecture-acceptance-criteria-default','请形成架构成果验收准则，分别记录结构、来源、专业和业务判断，不自动批准。','按目的与证据分离验收层次'),
('togaf-business-models-processes','compat-process-flow-diagram','请把原料中的触发、角色、分支和异常整理成流程图，说明终止条件。','从事件到成果走查行为及条件；不是功能分类'),
('togaf-change-value','technical-debt-register-default','请登记技术与架构债的影响、责任和处置，证据不足时保留未知。','按影响与反馈形成可复核债务处置'),
('togaf-ea-capability','architecture-repository-structure','请建立架构存储库结构，说明全景属于哪个分区，外部标准和治理如何连接。','显式包含、采纳和治理；全景不是整个库'),
('togaf-gap-solutions','building-block-description-default','请区分ABB逻辑需要和SBB实现候选，给出构建块及差距处理依据。','先架构要求，再评估实现；realizes方向不得颠倒'),
('togaf-implementation-governance','decision-delegation-register-default','请分析哪些决定可以委派、谁有权决定，以及可逆性和授权证据。','授权、角色和真实决定分开；候选申请不视为允许'),
('togaf-information-data','metadata-inference-structure','请区分结构化、半结构化和非结构化来源，表达剖析读取、结构上推与元数据上行。','先识别来源结构和访问限制，再验证处理链方向与端点'),
('togaf-migration-roadmap','rollback-plan-default','请为原料中的过渡安排回退触发、责任、数据核对和恢复验收。','过渡必须可运营；排期、切换与回退分别取证'),
('togaf-organization-roles','compat-organization-decomposition-diagram','请区分组织汇报层级与业务协作，生成有依据的组织分解图。','组织包含不等于协作或能力分解'),
('togaf-requirements','compat-requirements-catalog','请整理原料中的需求、来源、责任和可验证接受条件，识别缺失输入。','需求版本和来源可追溯；无测量不能生成确认事实'),
('togaf-security-risk','security-adm-concept-map','请把安全与风险整合进ADM，保留P/A共享、需求管理关联和ISM/ERM新增概念。','参考结构核对与企业适用裁剪分开'),
('togaf-strategy-capabilities','compat-business-capability-map','请以业务成果定义能力并生成能力地图，不以应用或部门代替能力。','区分能力分类、组织归属和实现实例'),
('togaf-technology-architecture','msa-source-deployment-diagram','请分析源码、公共库、部署包和运行实例的追溯，说明执行环境及业务边界。','源码构建部署单元，再部署执行实例；共享库没有业务服务'),
('togaf-value-streams','compat-value-stream-map','请按利益相关者价值定义价值流阶段及退出条件，区分价值阶段与内部作业步骤。','从期望价值界定阶段，能力映射不表示时间顺序'),
('togaf-vision-scenarios','scenario-traceability-matrix-default','请从业务问题推导目标、环境、人员和系统职责，生成业务场景追溯矩阵。','场景用于发现验证需求；预算和业务批准保持未知')]

def run(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True);ps=load()[2];rows=[]
 for owner,pid,prompt,method in TASKS:
  p=ps[pid];assert p['owner']==owner,(pid,p['owner'],owner)
  m,v=inputs(p);folder=out/owner;result,_=verify_profile(p,folder)
  negatives,_=negative_cases(m,v,p);missing=[c for c in negatives if c['id']=='required-field']
  if not missing:
   absent=copy.deepcopy(v);absent['entity_ids'].append('MISSING-BUSINESS-INPUT')
   missing=[{'model':copy.deepcopy(m),'view':absent,'expected_code':'view-entity-missing','id':'required-input-reference'}]
  rejected=[]
  for c in missing:
   _,report=express(c['model'],c['view'],p,'reference');rejected.append(c['expected_code'] in {e['code'] for e in report['errors']})
  files=[ROOT.parent/owner/'SKILL.md',ROOT.parent/owner/'references/method.md']
  record={'owner':owner,'prompt':prompt,'supplied_input':m,'selected_profile':pid,'selected_method':method,
   'selection_by':'本轮助手阅读任务及技能后人工选择；非自动路由评分或盲测',
   'instructions_sha256':{str(f.relative_to(ROOT.parent)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},
   'executed_profile_cases':result,'missing_required_input_rejected':bool(rejected) and all(rejected),
   'response':'已按提供原料生成对应制品、业务字段修改和缺输入反例。选择依据：'+method+'。原料为模拟/参考输入，待专业评审；生成不授予业务批准。',
   'approval_status':'candidate','professional_review':'pending',
   'limit':'覆盖17个技能的一项真实自然语言执行任务；不是所有表达方式、所有模型配置或独立模型泛化能力证明。'}
  (folder/'task.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');rows.append({'owner':owner,'profile_id':pid,'failures':result['failures'],'missing_required_input_rejected':record['missing_required_input_rejected'],'task':owner+'/task.json'})
 summary={'tasks':rows,'passed':all(not r['failures'] and r['missing_required_input_rejected'] for r in rows),'limit':'助手已选择方法的自然语言任务实做回放；无第二模型、盲测或专业业务批准。'}
 (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');return summary
