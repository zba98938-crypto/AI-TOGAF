# G233/figC-1 · 带业务能力实例的招聘员工价值流

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/figC-1.md) · [JSON](../../architecture/diagrams/G233/figC-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 55 页

![英文原图](../assets/G233/figC-1-p0055.png)

PDF 坐标：`[48.2, 210.2, 563.8, 565.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Recruit Employee Value Stream
Postion Vacancy
D)
Hiring Manager
®
Employee Candidate
Define Position
D|
‘Communicate Open
>
Select Final
D>
Offer Position
Onboard Candidates >
Position
Candidates
Program Management i
Facilities Management fi
Human Resource
>
‘Job Posting
a
‘Skills Assessment
ee
‘Compensation
Assign Office Space <>)
watching
Management
Roe Skils and Credentials
4ob Posting Website
‘Salary Bands
oa
Bulking Access
Hiring Manager
‘Management|
Company Webste
FRocruling Application
HR Position
ci}
Contract Management <i
Building Pass Card
‘Score and
HR Application
Management
‘Select Finast
‘Candidates
File Sharing Application
Recruitna éppteaton
Employment
‘Contract
Identity Management
“Bb Posting
1AM Application
Roe Catalog
Hieing Manager
oa
Recruiter
oa
Document Management «fi
Employee Electronic
Postion
Interview Candidates <>
‘Credentials
Description
Fle Sharing Applicaton
Candidate
oa
”
Pre-employment
Information
Schedule Management ff
HR Advisor
o
Document Management if,
Payroll Management
CCotaboratton Appication
FRocruling Application
HR Application
Finance Management if}
Resumé
rs
Risk Management i]
Payro
‘Applicaton
General Ledge
Book interview Times >
Police Check Application
r
‘Compensation
Cover Letter
*
i
Budget
HR Advisor
Invesugate cp}
fa)
Reporable
fences
Banking Application
Candidate
fa)
Financial Analyst CD|
Skills Assessment
a
Reject Unqualied <>
‘Candidates
Benefits Management «fi
‘Approved Poston Ready
Identity Management
Signed Employment @f
Benefits Agpication
‘or
Whats the process? <p)
©)
HR Advaor
o
Health insurance
Gap
SS]
Manageable List of
‘Qualiies Candidates
e
Roterent Pian
Ranked List of
Candidates
e
```

## 概要（历史解释；局部修正见上）

把招聘员工价值流的五个阶段展开成 17 个能力实例，逐层嵌套角色、应用、业务对象与差距，并给出前四个阶段的成果。

## 目的（历史解释；局部修正见上）

附录 C 用一个更偏后台的价值流补足正文的零售案例，演示同一套能力实例建模方法在招聘域的应用；同时暴露该价值流的现实问题（执行时间是要求的两倍多、入职后出现技能差距），为“缩短招聘时间、改善岗位与候选人匹配”的改进目标提供模型基础。

## 阅读顺序（历史解释；局部修正见上）

从左到右五列：Define Position → Communicate Open Position → Select Final Candidates → Offer Position → Onboard Candidates。顶部黄色是触发事件（Position Vacancy），两个紫色是利益相关者（Hiring Manager、Employee Candidate）。每列白卡内自上而下是能力实例；能力框内的紫色是参与者、黄色是角色/流程、青色是应用、黄色矩形是业务对象、白色矩形是数据对象、绿色波浪框是差距，绿色胶囊＋底座是交付物。每列底部紫色八边形（带靶心图标）是阶段成果，Onboard 列没有。带箭头的线跨越列时表示跨阶段的交接。

## 关键含义（历史解释；局部修正见上）

- 五个阶段：Define Position、Communicate Open Position、Select Final Candidates、Offer Position、Onboard Candidates；由职位空缺（Position Vacancy）触发，利益相关者是招聘经理与员工候选人。
- 共 17 个能力实例：Define 3 个（Program Management、HR Position Management、Finance Management）、Communicate 3 个（Job Posting、Document Management、Skills Assessment）、Select 3 个（Skills Assessment、Schedule Management、Identity Management）、Offer 4 个（Compensation Management、Contract Management、Document Management、Risk Management）、Onboard 4 个（Facilities Management、Identity Management、Payroll Management、Benefits Management）。
- 同一能力多次实例化：Document Management 在 Communicate 与 Offer 各一个（前者存简历/求职信，后者存入职前信息）；Skills Assessment 在 Communicate 与 Select 各一个（前者筛掉不合格者，后者打分选终选人）；Identity Management 在 Select 与 Onboard 各一个（前者流程未定并标了 Gap，后者发放电子凭证）。
- 两处跨列交接：Document Management 的简历数据以虚线箭头交给 Select 的 Skills Assessment；Offer 的 Employment Contract 以实线连到 Onboard 的 IAM Application，作为电子凭证的依据。
- 未知流程被显式建模：Select 的 Identity Management 里写着“What's the process?”，下方是一个标着“Gap”的绿色差距框——作者用占位问题表示该能力实例的流程尚未定义，这是本图最值得注意的“未完成”信号。
- Payroll Management 中 HR Application 内嵌 Payroll Application，再有实心箭头指向 Banking Application，表示工资发放到银行；这是图中唯一一条应用→应用的实心数据流。
- Facilities Management 末尾的 Building Pass Card 是绿色交付物（带底座），不是应用；它表示入职时发放的门禁卡这一产出。
- 前四个阶段各有明确的成果八边形（职位已批准可发布、可管理的合格候选人名单、候选人排名名单、已签署的劳动合同）；Onboard Candidates 阶段没有独立成果图形，止于阶段本身。

## 层级（历史解释；局部修正见上）

四层：价值流 → 阶段 → 能力实例 → 组件（利益相关者/角色/应用/业务流程/业务对象/差距）。应用组件内再嵌数据对象或应用过程。Building Pass Card 与 Gap 是能力实例内的产出/差距，不再下钻。

## 线条含义（历史解释；局部修正见上）

虚线向下箭头（无标签）：Company Website → Recruiting Application，表示职位发布到招聘系统。虚线向上斜箭头（无标签）：Communicate 的 Document Management → Select 的 Skills Assessment，表示简历/求职信进入筛选。实线向上箭头（无标签）：Book Interview Times → Collaboration Application。实线向下实心箭头（无标签）：Payroll Application → Banking Application。实线无箭头：Employment Contract → IAM Application。其余关系全部由嵌套表达。

## 易误读点（历史解释；局部修正见上）

- 不要把“What's the process?”当成给读者的提问；它是模型里的占位流程，配合下方“Gap”表示该能力实例的流程尚未定义。
- 不要把“Gap”框当成一个流程或应用；它是 ArchiMate 差距元素，表示需要补上的空白。
- 不要把两条 Document Management / Skills Assessment 当成重复绘制；它们是同一能力在不同阶段的两次实例化，组件不同。
- 不要把 Building Pass Card 当成应用或数据对象；它是设施管理产出的实物交付物。
- 不要把跨列的虚线读成阶段顺序；阶段顺序由列位置表达，跨列线是交接。
- 不要以为每个阶段都有成果图形：前四个阶段各有一个带靶心图标的紫色成果八边形；Onboard Candidates 列没有独立成果图形，图中也没有整条价值流的最终成果图形，与图 6-3 不同。
- 中文稿 PNG 的“合同管理”巨型文字块覆盖了 Offer Position 列，不要据其判断 Contract Management 的组件。

## 元素

```json
[
  {
    "id": "vs_recruit",
    "label_en": "Recruit Employee Value Stream",
    "label_zh": "招聘员工价值流",
    "type": "value_stream",
    "parent": null,
    "position": "沙色大容器"
  },
  {
    "id": "ev_vacancy",
    "label_en": "Position Vacancy",
    "label_zh": "职位空缺",
    "type": "event",
    "parent": "vs_recruit",
    "position": "容器左上（黄）"
  },
  {
    "id": "st_hiring_manager",
    "label_en": "Hiring Manager",
    "label_zh": "招聘经理",
    "type": "stakeholder",
    "parent": null,
    "position": "顶部中左（紫）"
  },
  {
    "id": "st_candidate",
    "label_en": "Employee Candidate",
    "label_zh": "员工候选人",
    "type": "stakeholder",
    "parent": null,
    "position": "顶部右侧（紫）"
  },
  {
    "id": "stg_define",
    "label_en": "Define Position",
    "label_zh": "定义职位",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "order": 1,
    "position": "第一列"
  },
  {
    "id": "stg_communicate",
    "label_en": "Communicate Open Position",
    "label_zh": "发布空缺职位",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "order": 2,
    "position": "第二列"
  },
  {
    "id": "stg_select",
    "label_en": "Select Final Candidates",
    "label_zh": "筛选最终候选人",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "order": 3,
    "position": "第三列"
  },
  {
    "id": "stg_offer",
    "label_en": "Offer Position",
    "label_zh": "发出职位录用",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "order": 4,
    "position": "第四列"
  },
  {
    "id": "stg_onboard",
    "label_en": "Onboard Candidates",
    "label_zh": "候选人入职",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "order": 5,
    "position": "第五列"
  },
  {
    "id": "cap_define_program",
    "label_en": "Program Management",
    "label_zh": "项目群管理",
    "type": "capability",
    "parent": "stg_define",
    "level": 1,
    "order": 1
  },
  {
    "id": "proc_hr_matching",
    "label_en": "Human Resource Matching",
    "label_zh": "人力资源匹配",
    "type": "process",
    "parent": "cap_define_program",
    "order": 1
  },
  {
    "id": "role_hm_define",
    "label_en": "Hiring Manager",
    "label_zh": "招聘经理",
    "type": "role",
    "parent": "cap_define_program",
    "order": 2,
    "description_zh": "角色"
  },
  {
    "id": "cap_hr_position",
    "label_en": "HR Position Management",
    "label_zh": "人力资源职位管理",
    "type": "capability",
    "parent": "stg_define",
    "level": 1,
    "order": 2
  },
  {
    "id": "app_file_sharing_1",
    "label_en": "File Sharing Application",
    "label_zh": "文件共享应用",
    "type": "application",
    "parent": "cap_hr_position",
    "order": 1
  },
  {
    "id": "obj_role_catalog",
    "label_en": "Role Catalog",
    "label_zh": "角色目录",
    "type": "data",
    "parent": "app_file_sharing_1"
  },
  {
    "id": "obj_position_desc",
    "label_en": "Position Description",
    "label_zh": "职位描述",
    "type": "data",
    "parent": "obj_role_catalog"
  },
  {
    "id": "role_hr_advisor_1",
    "label_en": "HR Advisor",
    "label_zh": "人力资源顾问",
    "type": "role",
    "parent": "cap_hr_position",
    "order": 2
  },
  {
    "id": "cap_define_finance",
    "label_en": "Finance Management",
    "label_zh": "财务管理",
    "type": "capability",
    "parent": "stg_define",
    "level": 1,
    "order": 3
  },
  {
    "id": "app_general_ledger",
    "label_en": "General Ledger",
    "label_zh": "总账",
    "type": "application",
    "parent": "cap_define_finance",
    "order": 1
  },
  {
    "id": "obj_comp_budget",
    "label_en": "Compensation Budget",
    "label_zh": "薪酬预算",
    "type": "data",
    "parent": "app_general_ledger"
  },
  {
    "id": "role_fin_analyst",
    "label_en": "Financial Analyst",
    "label_zh": "财务分析师",
    "type": "role",
    "parent": "cap_define_finance",
    "order": 2
  },
  {
    "id": "out_position",
    "label_en": "Approved Position Ready for Posting",
    "label_zh": "职位已批准、可发布",
    "type": "goal",
    "parent": "stg_define"
  },
  {
    "id": "cap_job_posting",
    "label_en": "Job Posting",
    "label_zh": "职位发布",
    "type": "capability",
    "parent": "stg_communicate",
    "level": 1,
    "order": 1
  },
  {
    "id": "app_job_posting_web",
    "label_en": "Job Posting Website",
    "label_zh": "招聘网站",
    "type": "application",
    "parent": "cap_job_posting",
    "order": 1
  },
  {
    "id": "app_company_web",
    "label_en": "Company Website",
    "label_zh": "公司网站",
    "type": "application",
    "parent": "cap_job_posting",
    "order": 2
  },
  {
    "id": "app_recruiting_posting",
    "label_en": "Recruiting Application",
    "label_zh": "招聘应用",
    "type": "application",
    "parent": "cap_job_posting",
    "order": 3
  },
  {
    "id": "dat_job_posting",
    "label_en": "Job Posting",
    "label_zh": "职位发布",
    "type": "data",
    "parent": "app_recruiting_posting",
    "description_zh": "数据对象"
  },
  {
    "id": "role_recruiter",
    "label_en": "Recruiter",
    "label_zh": "招聘人员",
    "type": "role",
    "parent": "cap_job_posting",
    "order": 4
  },
  {
    "id": "role_candidate_1",
    "label_en": "Candidate",
    "label_zh": "候选人",
    "type": "role",
    "parent": "cap_job_posting",
    "order": 5,
    "description_zh": "角色"
  },
  {
    "id": "cap_doc_1",
    "label_en": "Document Management",
    "label_zh": "文档管理",
    "type": "capability",
    "parent": "stg_communicate",
    "level": 1,
    "order": 2
  },
  {
    "id": "app_recruiting_docs",
    "label_en": "Recruiting Application",
    "label_zh": "招聘应用",
    "type": "application",
    "parent": "cap_doc_1",
    "description_zh": "文档"
  },
  {
    "id": "obj_resume",
    "label_en": "Résumé",
    "label_zh": "简历",
    "type": "data",
    "parent": "app_recruiting_docs",
    "order": 1
  },
  {
    "id": "obj_cover_letter",
    "label_en": "Cover Letter",
    "label_zh": "求职信",
    "type": "data",
    "parent": "app_recruiting_docs",
    "order": 2
  },
  {
    "id": "cap_skills_1",
    "label_en": "Skills Assessment",
    "label_zh": "技能评估",
    "type": "capability",
    "parent": "stg_communicate",
    "level": 1,
    "order": 3,
    "description_zh": "初筛"
  },
  {
    "id": "proc_reject",
    "label_en": "Reject Unqualified Candidates",
    "label_zh": "拒绝不合格候选人",
    "type": "process",
    "parent": "cap_skills_1",
    "order": 1
  },
  {
    "id": "role_hr_advisor_2",
    "label_en": "HR Advisor",
    "label_zh": "人力资源顾问",
    "type": "role",
    "parent": "cap_skills_1",
    "order": 2,
    "description_zh": "初筛"
  },
  {
    "id": "out_manageable",
    "label_en": "Manageable List of Qualified Candidates",
    "label_zh": "可管理的合格候选人名单",
    "type": "goal",
    "parent": "stg_communicate"
  },
  {
    "id": "cap_skills_2",
    "label_en": "Skills Assessment",
    "label_zh": "技能评估",
    "type": "capability",
    "parent": "stg_select",
    "level": 1,
    "order": 1,
    "description_zh": "终选"
  },
  {
    "id": "obj_role_skills",
    "label_en": "Role Skills and Credentials",
    "label_zh": "职位技能与资质",
    "type": "data",
    "parent": "cap_skills_2"
  },
  {
    "id": "app_recruiting_score",
    "label_en": "Recruiting Application",
    "label_zh": "招聘应用",
    "type": "application",
    "parent": "cap_skills_2",
    "order": 2,
    "description_zh": "评分"
  },
  {
    "id": "ap_score",
    "label_en": "Score and Select Finalist Candidates",
    "label_zh": "评分并选择入围候选人",
    "type": "process",
    "parent": "app_recruiting_score"
  },
  {
    "id": "role_hm_select",
    "label_en": "Hiring Manager",
    "label_zh": "招聘经理",
    "type": "role",
    "parent": "cap_skills_2",
    "order": 3,
    "description_zh": "终选"
  },
  {
    "id": "proc_interview",
    "label_en": "Interview Candidates",
    "label_zh": "面试候选人",
    "type": "process",
    "parent": "cap_skills_2",
    "order": 4
  },
  {
    "id": "cap_schedule",
    "label_en": "Schedule Management",
    "label_zh": "日程管理",
    "type": "capability",
    "parent": "stg_select",
    "level": 1,
    "order": 2
  },
  {
    "id": "app_collab",
    "label_en": "Collaboration Application",
    "label_zh": "协作应用",
    "type": "application",
    "parent": "cap_schedule",
    "order": 1
  },
  {
    "id": "proc_book",
    "label_en": "Book Interview Times",
    "label_zh": "预约面试时间",
    "type": "process",
    "parent": "cap_schedule",
    "order": 2
  },
  {
    "id": "role_hr_advisor_3",
    "label_en": "HR Advisor",
    "label_zh": "人力资源顾问",
    "type": "role",
    "parent": "cap_schedule",
    "order": 3,
    "description_zh": "排期"
  },
  {
    "id": "role_candidate_2",
    "label_en": "Candidate",
    "label_zh": "候选人",
    "type": "role",
    "parent": "cap_schedule",
    "order": 4,
    "description_zh": "面试"
  },
  {
    "id": "cap_identity_select",
    "label_en": "Identity Management",
    "label_zh": "身份管理",
    "type": "capability",
    "parent": "stg_select",
    "level": 1,
    "order": 3,
    "description_zh": "筛选"
  },
  {
    "id": "proc_whats_process",
    "label_en": "What's the process?",
    "label_zh": "流程是什么？",
    "type": "process",
    "parent": "cap_identity_select",
    "order": 1,
    "description_zh": "占位流程"
  },
  {
    "id": "gap_identity",
    "label_en": "Gap",
    "label_zh": "差距",
    "type": "requirement",
    "parent": "cap_identity_select",
    "order": 2,
    "description_zh": "ArchiMate gap 元素，表示该能力实例的流程尚未定义。"
  },
  {
    "id": "out_ranked",
    "label_en": "Ranked List of Candidates",
    "label_zh": "候选人排名名单",
    "type": "goal",
    "parent": "stg_select"
  },
  {
    "id": "cap_compensation",
    "label_en": "Compensation Management",
    "label_zh": "薪酬管理",
    "type": "capability",
    "parent": "stg_offer",
    "level": 1,
    "order": 1
  },
  {
    "id": "obj_salary_bands",
    "label_en": "Salary Bands",
    "label_zh": "薪资带宽",
    "type": "data",
    "parent": "cap_compensation"
  },
  {
    "id": "cap_contract",
    "label_en": "Contract Management",
    "label_zh": "合同管理",
    "type": "capability",
    "parent": "stg_offer",
    "level": 1,
    "order": 2
  },
  {
    "id": "app_hr_contract",
    "label_en": "HR Application",
    "label_zh": "人力资源应用",
    "type": "application",
    "parent": "cap_contract",
    "description_zh": "合同"
  },
  {
    "id": "obj_employment_contract",
    "label_en": "Employment Contract",
    "label_zh": "劳动合同",
    "type": "data",
    "parent": "app_hr_contract"
  },
  {
    "id": "cap_doc_2",
    "label_en": "Document Management",
    "label_zh": "文档管理",
    "type": "capability",
    "parent": "stg_offer",
    "level": 1,
    "order": 3,
    "description_zh": "入职前"
  },
  {
    "id": "app_file_sharing_2",
    "label_en": "File Sharing Application",
    "label_zh": "文件共享应用",
    "type": "application",
    "parent": "cap_doc_2",
    "description_zh": "入职前"
  },
  {
    "id": "obj_preemployment",
    "label_en": "Pre-employment Information",
    "label_zh": "入职前信息",
    "type": "data",
    "parent": "app_file_sharing_2"
  },
  {
    "id": "cap_risk",
    "label_en": "Risk Management",
    "label_zh": "风险管理",
    "type": "capability",
    "parent": "stg_offer",
    "level": 1,
    "order": 4
  },
  {
    "id": "app_police",
    "label_en": "Police Check Application",
    "label_zh": "警察审查应用",
    "type": "application",
    "parent": "cap_risk"
  },
  {
    "id": "ap_investigate",
    "label_en": "Investigate Reportable Offences",
    "label_zh": "调查可报告的违规行为",
    "type": "process",
    "parent": "app_police"
  },
  {
    "id": "out_signed",
    "label_en": "Signed Employment Contract",
    "label_zh": "已签署的劳动合同",
    "type": "goal",
    "parent": "stg_offer"
  },
  {
    "id": "cap_facilities",
    "label_en": "Facilities Management",
    "label_zh": "设施管理",
    "type": "capability",
    "parent": "stg_onboard",
    "level": 1,
    "order": 1
  },
  {
    "id": "proc_assign_space",
    "label_en": "Assign Office Space",
    "label_zh": "分配办公空间",
    "type": "process",
    "parent": "cap_facilities",
    "order": 1
  },
  {
    "id": "app_building_access",
    "label_en": "Building Access Management",
    "label_zh": "楼宇门禁管理",
    "type": "application",
    "parent": "cap_facilities",
    "order": 2
  },
  {
    "id": "artifact_pass_card",
    "label_en": "Building Pass Card",
    "label_zh": "楼宇门禁卡",
    "type": "artifact",
    "parent": "cap_facilities",
    "order": 3,
    "description_zh": "绿色胶囊＋底座的交付物（与图 7-2 的 Signature Pad 同形），表示入职时发放的门禁卡"
  },
  {
    "id": "cap_identity_onboard",
    "label_en": "Identity Management",
    "label_zh": "身份管理",
    "type": "capability",
    "parent": "stg_onboard",
    "level": 1,
    "order": 2,
    "description_zh": "入职"
  },
  {
    "id": "app_iam",
    "label_en": "IAM Application",
    "label_zh": "身份与访问管理应用",
    "type": "application",
    "parent": "cap_identity_onboard"
  },
  {
    "id": "dat_employee_credentials",
    "label_en": "Employee Electronic Credentials",
    "label_zh": "员工电子凭证",
    "type": "data",
    "parent": "app_iam"
  },
  {
    "id": "cap_payroll",
    "label_en": "Payroll Management",
    "label_zh": "薪资管理",
    "type": "capability",
    "parent": "stg_onboard",
    "level": 1,
    "order": 3
  },
  {
    "id": "app_hr_payroll",
    "label_en": "HR Application",
    "label_zh": "人力资源应用",
    "type": "application",
    "parent": "cap_payroll",
    "order": 1,
    "description_zh": "薪资"
  },
  {
    "id": "app_payroll_app",
    "label_en": "Payroll Application",
    "label_zh": "薪资应用",
    "type": "application",
    "parent": "app_hr_payroll"
  },
  {
    "id": "app_banking",
    "label_en": "Banking Application",
    "label_zh": "银行应用",
    "type": "application",
    "parent": "cap_payroll",
    "order": 2
  },
  {
    "id": "cap_benefits",
    "label_en": "Benefits Management",
    "label_zh": "福利管理",
    "type": "capability",
    "parent": "stg_onboard",
    "level": 1,
    "order": 4
  },
  {
    "id": "app_benefits",
    "label_en": "Benefits Application",
    "label_zh": "福利应用",
    "type": "application",
    "parent": "cap_benefits"
  },
  {
    "id": "obj_health",
    "label_en": "Health Insurance",
    "label_zh": "健康保险",
    "type": "data",
    "parent": "app_benefits",
    "order": 1
  },
  {
    "id": "obj_retirement",
    "label_en": "Retirement Plan",
    "label_zh": "退休计划",
    "type": "data",
    "parent": "app_benefits",
    "order": 2
  }
]
```

## 关系

```json
[
  {
    "from": "app_company_web",
    "to": "app_recruiting_posting",
    "type": "flow",
    "label_en": null,
    "label_zh": null,
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "虚线向下箭头：公司网站发布的职位进入招聘应用。"
  },
  {
    "from": "cap_doc_1",
    "to": "cap_skills_2",
    "type": "flow",
    "label_en": null,
    "label_zh": null,
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "虚线斜向上箭头，从 Communicate 的 Document Management 能力框指向 Select 的 Skills Assessment 能力框，表示简历/求职信进入终选。"
  },
  {
    "from": "proc_book",
    "to": "app_collab",
    "type": "flow",
    "label_en": null,
    "label_zh": null,
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "实线向上箭头：预约面试时间的流程写入协作应用。"
  },
  {
    "from": "app_payroll_app",
    "to": "app_banking",
    "type": "flow",
    "label_en": null,
    "label_zh": null,
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "实线向下实心箭头：薪资应用把发放指令发送给银行应用。"
  },
  {
    "from": "obj_employment_contract",
    "to": "app_iam",
    "type": "association",
    "label_en": null,
    "label_zh": null,
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "实线无箭头，从 Employment Contract 跨列连到 IAM Application，表示合同是电子凭证的依据。"
  },
  {
    "from": "ev_vacancy",
    "to": "vs_recruit",
    "type": "triggering",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "st_hiring_manager",
    "to": "vs_recruit",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "招聘经理是价值流的利益相关者。"
  },
  {
    "from": "st_candidate",
    "to": "vs_recruit",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "员工候选人是价值流的利益相关者。"
  },
  {
    "from": "cap_define_program",
    "to": "stg_define",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_hr_position",
    "to": "stg_define",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_define_finance",
    "to": "stg_define",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_job_posting",
    "to": "stg_communicate",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_doc_1",
    "to": "stg_communicate",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_skills_1",
    "to": "stg_communicate",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_skills_2",
    "to": "stg_select",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_schedule",
    "to": "stg_select",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_identity_select",
    "to": "stg_select",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_compensation",
    "to": "stg_offer",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_contract",
    "to": "stg_offer",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_doc_2",
    "to": "stg_offer",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_risk",
    "to": "stg_offer",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_facilities",
    "to": "stg_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_identity_onboard",
    "to": "stg_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_payroll",
    "to": "stg_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_benefits",
    "to": "stg_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "stg_define",
    "to": "out_position",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "stg_communicate",
    "to": "out_manageable",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "stg_select",
    "to": "out_ranked",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "stg_offer",
    "to": "out_signed",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_recruit",
    "kind": "sequence",
    "name_zh": "招聘员工阶段序列",
    "steps": [
      "stg_define",
      "stg_communicate",
      "stg_select",
      "stg_offer",
      "stg_onboard"
    ],
    "description_zh": "五列从左到右；正文说明该价值流在职位空缺时启动，目标是缩短执行时间并改善技能匹配。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_recruit_instances",
    "title_zh": "阶段×能力实例×组件逐项转录",
    "columns": [
      "阶段",
      "能力实例",
      "应用组件与内嵌对象",
      "角色/流程/对象",
      "阶段成果"
    ],
    "rows": [
      [
        "Define Position 定义职位",
        "Program Management 项目群管理",
        "—",
        "Human Resource Matching 人力资源匹配（流程）；Hiring Manager 招聘经理（角色）",
        "Approved Position Ready for Posting 职位已批准、可发布"
      ],
      [
        "Define Position 定义职位",
        "HR Position Management 人力资源职位管理",
        "File Sharing Application 文件共享应用（Role Catalog 角色目录 → Position Description 职位描述）",
        "HR Advisor 人力资源顾问",
        "同上"
      ],
      [
        "Define Position 定义职位",
        "Finance Management 财务管理",
        "General Ledger 总账（Compensation Budget 薪酬预算）",
        "Financial Analyst 财务分析师",
        "同上"
      ],
      [
        "Communicate Open Position 发布空缺职位",
        "Job Posting 职位发布",
        "Job Posting Website 招聘网站；Company Website 公司网站；Recruiting Application 招聘应用（Job Posting 数据对象）",
        "Recruiter 招聘人员；Candidate 候选人",
        "Manageable List of Qualified Candidates 可管理的合格候选人名单"
      ],
      [
        "Communicate Open Position 发布空缺职位",
        "Document Management 文档管理",
        "Recruiting Application 招聘应用（Résumé 简历；Cover Letter 求职信）",
        "—",
        "同上"
      ],
      [
        "Communicate Open Position 发布空缺职位",
        "Skills Assessment 技能评估",
        "—",
        "Reject Unqualified Candidates 拒绝不合格者（流程）；HR Advisor 人力资源顾问",
        "同上"
      ],
      [
        "Select Final Candidates 筛选最终候选人",
        "Skills Assessment 技能评估",
        "Recruiting Application 招聘应用（Score and Select Finalist Candidates 评分并选择入围者）",
        "Role Skills and Credentials 职位技能与资质（数据）；Hiring Manager 招聘经理；Interview Candidates 面试候选人（流程）",
        "Ranked List of Candidates 候选人排名名单"
      ],
      [
        "Select Final Candidates 筛选最终候选人",
        "Schedule Management 日程管理",
        "Collaboration Application 协作应用",
        "Book Interview Times 预约面试时间（流程）；HR Advisor；Candidate",
        "同上"
      ],
      [
        "Select Final Candidates 筛选最终候选人",
        "Identity Management 身份管理",
        "—",
        "What's the process? 流程是什么？（占位流程）；Gap 差距",
        "同上"
      ],
      [
        "Offer Position 发出职位录用",
        "Compensation Management 薪酬管理",
        "—",
        "Salary Bands 薪资带宽（数据）",
        "Signed Employment Contract 已签署的劳动合同"
      ],
      [
        "Offer Position 发出职位录用",
        "Contract Management 合同管理",
        "HR Application 人力资源应用（Employment Contract 劳动合同）",
        "—",
        "同上"
      ],
      [
        "Offer Position 发出职位录用",
        "Document Management 文档管理",
        "File Sharing Application 文件共享应用（Pre-employment Information 入职前信息）",
        "—",
        "同上"
      ],
      [
        "Offer Position 发出职位录用",
        "Risk Management 风险管理",
        "Police Check Application 警察审查应用（Investigate Reportable Offences 调查可报告违规）",
        "—",
        "同上"
      ],
      [
        "Onboard Candidates 候选人入职",
        "Facilities Management 设施管理",
        "Building Access Management 楼宇门禁管理",
        "Assign Office Space 分配办公空间（流程）；Building Pass Card 楼宇门禁卡（交付物）",
        "无独立成果图形"
      ],
      [
        "Onboard Candidates 候选人入职",
        "Identity Management 身份管理",
        "IAM Application 身份与访问管理应用（Employee Electronic Credentials 员工电子凭证）",
        "—",
        "同上"
      ],
      [
        "Onboard Candidates 候选人入职",
        "Payroll Management 薪资管理",
        "HR Application 人力资源应用 → Payroll Application 薪资应用；Banking Application 银行应用",
        "—",
        "同上"
      ],
      [
        "Onboard Candidates 候选人入职",
        "Benefits Management 福利管理",
        "Benefits Application 福利应用（Health Insurance 健康保险；Retirement Plan 退休计划）",
        "—",
        "同上"
      ]
    ],
    "notes_zh": "同一能力在不同阶段出现多次时分行记录；角色/流程/对象列按图中元素类型标注。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "沙色大框 + V 形图标",
    "meaning_zh": "价值流",
    "explicit": false
  },
  {
    "symbol": "黄色框 + 事件图标",
    "meaning_zh": "触发事件（Position Vacancy）",
    "explicit": false
  },
  {
    "symbol": "紫色六边形 + 双环图标",
    "meaning_zh": "利益相关者（Hiring Manager、Employee Candidate）",
    "explicit": false
  },
  {
    "symbol": "白色阶段卡 + V 形图标",
    "meaning_zh": "价值流阶段",
    "explicit": false
  },
  {
    "symbol": "沙色框 + 能力图标",
    "meaning_zh": "业务能力实例",
    "explicit": false
  },
  {
    "symbol": "青色框 + 左侧双页签",
    "meaning_zh": "应用组件",
    "explicit": false
  },
  {
    "symbol": "黄色矩形 + 箭头/角色图标",
    "meaning_zh": "业务流程 / 业务角色",
    "explicit": false
  },
  {
    "symbol": "黄色直角矩形（应用内）",
    "meaning_zh": "业务对象（Role Catalog、Résumé 等）",
    "explicit": false
  },
  {
    "symbol": "白色直角矩形（应用内）",
    "meaning_zh": "数据对象（Job Posting、Employee Electronic Credentials）",
    "explicit": false
  },
  {
    "symbol": "白色圆角框 + 箭头图标",
    "meaning_zh": "应用过程",
    "explicit": false
  },
  {
    "symbol": "绿色波浪底框 + Gap 图标",
    "meaning_zh": "差距（Gap）",
    "explicit": false
  },
  {
    "symbol": "绿色胶囊 + 底座",
    "meaning_zh": "交付物（Building Pass Card）",
    "explicit": false
  },
  {
    "symbol": "紫色八边形 + 靶心图标",
    "meaning_zh": "阶段成果（ArchiMate Outcome 画法）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "沙色价值流容器内五列：每列一张白色阶段卡，卡内纵向堆叠 3–4 个沙色能力实例框；能力框内自上而下为利益相关者/角色、应用、业务对象/数据对象/流程；阶段卡底部为带靶心图标的成果八边形。"
}
```

## 相关图

```json
[
  {
    "target": "G178/fig4-2",
    "relation": "variant_of",
    "note_zh": "G178 图 4-2 的招聘员工价值流使用同一业务场景，但阶段划分为 Define Position/Communicate Position/Assess Responses/Interview Candidates/Onboard Employee，与本图五阶段不同，属同一价值流的另一版本"
  },
  {
    "target": "G178/fig4-3",
    "relation": "related",
    "note_zh": "G178 图 4-3 把招聘价值流阶段交叉映射到业务能力，可视为本图能力实例的上游映射"
  },
  {
    "target": "G233/fig6-3",
    "relation": "complements",
    "note_zh": "两图使用完全相同的建模风格（阶段列→能力实例→角色/应用/数据/流程），可对照前台零售与后台招聘两个价值流"
  },
  {
    "target": "G233/fig6-1",
    "relation": "related",
    "note_zh": "本图的 HR Position Management、Job Posting、Skills Assessment、Benefits Management、Payroll Management 均为图 6-1 目录中的能力"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "“Building Pass Card”使用绿色胶囊＋底座的图形，既非应用框也非差距框，本文按交付物（artifact）记录；其确切 ArchiMate 类型无法仅凭图形确认。",
    "“What's the process?”与“Gap”组合表达流程未定义，但图中没有文字说明二者的关系；本文按“占位流程＋差距”解释。",
    "Onboard Candidates 阶段没有独立成果图形（前四阶段为带靶心图标的紫色八边形），图中也未画整条价值流的最终成果图形（与图 6-3 不同），无法判断是有意省略还是版面所限。"
  ],
  "analyzed_from": [
    "英文 PDF 第 55 页图 C-1 截图（500 dpi）与 650 dpi 五列分栏放大",
    "英文 PDF 第 54–55 页附录 C 正文",
    "中文稿 G233e_业务能力规划.md 第 939–1006 行（含标签对照表）",
    "figs/zh/g233e_figC-1_zh.png"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
