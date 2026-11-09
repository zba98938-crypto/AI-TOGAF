#!/usr/bin/env python3
"""Rebuild the separately authored fictional procedural supplements; no acceptance."""
import json,hashlib,copy
from pathlib import Path
root=Path(__file__).resolve().parents[1];shared=root/'skills/_shared';case_dir=shared/'references/method-cases';out=shared/'references/method-case-materials/procedural-supplements';out.mkdir(parents=True,exist_ok=True)
# These are authored fictional inputs and expected candidate transformations. They
# are neither produced from calculator outputs nor asserted as organization facts.
rows={
'reference-model-tailoring':{2:('新虚构独立补充场景：养老资产投资LF-SUP-INVEST映射G21D财政/投资管理/养老基金管理，仅作分类对照，职责由资产投资组提议承担；它与上文市民预约LF-1场景不同。','从完整目录按路径取参考ID；两侧ID分列，不以reference_id覆盖local_id。','MAP-SUP保留LF-SUP-INVEST及独立reference_id、path和版本；不存在参考同名部门。','若删local_id或用参考域创建部门，应拒绝该映射并保留职责缺口。')},
'mdm-four-plateau-operations-method':{
1:('新虚构四态候选：P0各馆各自维护；P1只读黄金记录分析；P2主数据平台管理限定内核字段并向馆系统分发；P3在P2基础覆盖全馆约定完整读者身份/联络/同意内核；合同与借阅交易保持原主控。各态可共存，日期与成本未知。','将四种来源平台态的使用方式与四个本地候选分别映射，区分分析黄金记录、内核运营写权和完整运营范围。','保留P0/P1/P2/P3四身份；P1不主写，P2只写限定内核，P3扩至全馆约定完整内核而不改交易主控，均candidate。','把P1分析成功写为P2主写已获准，或把四种形态硬配四期，应保留阻断。'),
3:('新虚构逐态条件表：P0现有馆用例、源校验、馆内授权、备份和支持存在；P1跨馆分析、人工核验、只读授权、可重复重建、夜批支持均只是已设计；P2试点内核与P3全馆完整约定内核的用例定义在草案，质量测试、写授权、错合并恢复、积压监控全待验证。','逐态五栏形成条件记录；有设计不等于已验证，不将P0源备份自动复制到P2错合并恢复。','四态×五条件20条候选记录；P2/P3可运营为unknown，当前不接管馆系统写权。','仅补P2授权而无恢复测试，P2/P3仍blocked；补P1读授权不授P2写授权。')},
'msa-contract-consumer-evidence-method':{3:('新虚构契约草案：eligibility/v1.1地址由受控服务目录发布，消费者C-BOOK/C-DESK有独立令牌audience与最小资格权限；移动端C-MOBILE只是拟申请。测试负载每秒20请求、持续10分钟，延迟实测P95=180ms；未做月可用性观察。','逐消费者分别检查地址可发现、令牌作用域、目标audience和未知原因码处理；延迟与月可用性分开。','C-BOOK/C-DESK候选权限矩阵、v1.1地址与发现责任完整；延迟仅在声明负载窗满足200ms，99.5%月可用仍unknown。','把C-MOBILE拟申请当已授权，或用10分钟延迟证据放行月SLA，都应拒绝。')},
'bi-stage-operability-and-exit-method':{
3:('新虚构S1收益为设备事件的可核提示、S2为统一原始供数、S3为减少旧仓双轨；每态列people/systems/data/controls/rollback。业务责任分别为分析负责人/数据负责人/运营负责人；恢复草案均需演练。','按命名状态保存收益、缺口和五条件，收益为预期不是已实现；恢复设计和演练证据分列。','S1/S2/S3均candidate-operability：运营责任已提议、数据对账和恢复未测试；不授可运营。','只有收益说明或三个彩色框时，仍保留运营、对账、回退缺口。'),
4:('新虚构退役清单OLD-monthly/OLD-audit两旧用途、受控只读留存、历史规则版本、字段血缘和恢复演练；新测试只覆盖OLD-audit，OLD-monthly尚未复算。','把每旧用途映射新实现和独立验证；治理、元数据、恢复分别检查，不能以用途已列代替测试。','审计覆盖为教学测试支持，月报覆盖unknown；退役仍blocked，旧仓保留。','删除月报行或用审计测试使全部旧需求已覆盖，都应拒绝退役。')},
'bi-requirement-origin-boundary-method':{2:('新虚构R-SUP-1：审计员应从一个已发布看板指标定位源批次、规则版本和处理时间；R-SUP-2：定义看板“净收入”的版本与生效日。两个需求不含指标值，均由业务工作坊提出。','按单一可验证结果拆分需求，赋项目ID并用验收测试字段列表检查原子性；来源只标项目工作坊，非官方需求ID。','两条候选需求分别以批次/规则/时间可查和术语版本可查验收；重复项按规范化意图对照，保留来源。','把两个需求合成“系统需安全高效完整”或冒用官方电子表格ID，应退回澄清。')},
'government-reference-catalog-overlay-method':{
1:('新虚构范围声明只覆盖养老资产投资与待遇发放；加载包内government-reference-catalog完整11部门、36功能、196服务。','按完整路径定位财政/投资管理/养老基金管理与共享服务/财务共享中心/养老基金管理，末级同名不去重。','完整部门范围台账11项，两采用、九out-of-project-scope；保留两条不同完整路径与源ID。','按末级名合并养老基金节点或虚构第12部门，应拒绝。'),
3:('新虚构范围材料逐部门排除除财政/共享服务外九部门：本试点无对应交付项，未来扩范围再评估，不断言机构不存在这些业务。','每部门分别保存applicability、理由、复评触发和影响未知，不能只把九部门合计写为不适用。','11行逐项采用/范围外台账，九行各自reason相同范围依据但保留各自ID。','把out-of-scope改为institution-not-applicable而无职责证据，应拒绝。'),
6:('新虚构图形要求只画两条采用路径的部门→功能→服务；养老业务办公室协调关系为project-only。','从目录parent_id形成reference_classifies显式边，不将协调/对账关系并入参考分类树。','两条3级路径和4条有向reference_classifies候选边；投资→支付对账另有project-only边。','反转分类边或以decomposes冒称能力分解，应拒绝。'),
7:('新虚构本地映射LOCAL-ASSET承担投资、LOCAL-BENEFIT承担待遇发放、LOCAL-PENSION只协调。','属性记录local_object_ids和project-evidence，节点ID与path保持参考身份；参考分类不创建本地组织。','源参考节点保留reference_id/path/version；两个本地职责附项目映射，协调者不独占路径。','用本地组织名称覆盖reference_path或删原reference_id，应判身份丢失。')},
'dbrm-mapping-suite-method':{
2:('新虚构十要素资料：客户访谈关注无障碍确认；产品团队持有状态查询待办；战略范围跨科室；动机可靠确认；业务产品养老申报；生态财政/待遇/平台；运营模型线上+人工；能力受理/核验；运营环境服务台与运行平台；数字使能受控接口和追溯字段。','逐个十要素映射这些项目资料，保持来源要素ID与本地描述两侧身份，不把四DBRM域改成本地四架构域。','十条candidate-project-mapping，有各自SUP-DBRM证据；本地业务/数据/应用/技术结构另存。','省略其中要素或将参考要素名当本地已实现能力，应保留缺口。'),
5:('新虚构练习要求使用包内dbrm-reference-mappings五张独立表，保留headers、row_id、raw_cells、source_lines及本地来源性质。','完整复制五表来源行作不可改输入，本地映射另设字段；不靠章节名猜单元格。','五表完整源行快照指纹与source_identity=local-body-reference；raw_cells未重写。','将空白填成上一行内容再覆盖raw_cells，应拒绝来源改变。'),
6:('新虚构解释记录按每表维度独立；只允许该表明确分组内的行连续解析，源—和空缺不自动变不适用。','raw与resolved分开；跨组续写、跨表串接均标unknown，不作来源肯定判断。','resolved_cells保留解释来源和组边界；—/空缺状态为source-blank-or-dash，不给不适用。','用上一表对应项填下一表空格，或把—计作不适用，应拒绝。'),
7:('新虚构本地使用只有养老查询、受理核验、财政/待遇/平台三方协作；所有源映射条目都需本地对应或明确unknown。','每源行保存local_object_ids、local_evidence、mapping_status；相同项目对象可被多个源视角引用。','逐行本地候选映射有证据或unknown；unknown不改成not-applicable，保持参考独立。','没有本地对应就删源行、把unknown当不适用，应保留映射缺口。'),
8:('新虚构补充：本项目认为G实施治理需要接口监控；尚无已核实源表6-1的G对应格。','新增PROJECT-G行，type=project-only；不把它插入或反写源table rows/raw_cells。','PROJECT-G有项目理由与未决来源支持；原G21H-T6-1行数/原格不变。','将PROJECT-G伪造为G21H源行并声明官方对应，应拒绝。')},
'digital-enablement-competency-mapping-method':{1:('新虚构教学要求完整读取G21H表4-1五支柱十二胜任力；为每行提议一个本地角色、具体产物/缺口与补证行动，全部是候选分配。','来源的DPBoK语境与本地组织语境分别记录；十二行保留source_row_id/pillar/competency/context，不按个人→团队排等级。','十二条参考-本地overlay，每行partial/unknown和待取证产物；原十角色2语境观察只保留为旧片段，不证明框架全覆盖。','以十二个角色名或源语境自动判人员具备，或用十角色代替十二胜任力，应拒绝。')},
'product-architecture-allocation-method':{
2:('新虚构F-SUBMIT提交受理分给C-CASE，F-STATUS状态查询分给C-STATUS；C-PORTAL只交互入口，C-CASE/STATUS负责业务处理。','为每功能建立function→component有向allocates_function关系，证据逐条指向新分配记录。','REL-SUBMIT为F-SUBMIT→C-CASE，REL-STATUS为F-STATUS→C-STATUS；接口调用仍PORTAL→后端，关系不同。','只按连线位置推功能归属，或用接口调用边顶替allocates_function，应拒绝。'),
4:('新虚构运营能力为受理核验与状态告知，两后端使用TC-API运行；新增F-ASSIST由服务台C-DESK代理申请，代理授权待补。','功能→组件→接口→运营能力/技术依赖分别追溯；新增代理功能改变人和授权链，原两功能关系不覆盖。','F-ASSIST/C-DESK/I-ASSIST均candidate；授权unknown；原C-CASE/STATUS→TC-API依赖保留。','把技术组件当业务功能，或以自助授权放行代理操作，应拒绝。')},
'msa-federated-governance-process-method':{
1:('新虚构两轨：企业EA管标准/跨产品决策；MSA团队管单服务契约、发布、数据和运维细节；企业最小权限是共用护栏，EX-1需企业豁免裁决。','逐项记录decision_scope和裁决主体；MSA细节不可覆盖企业护栏，企业规则不替团队写实现。','EA-TRACK与MSA-TRACK两轨决定台账，EX-1=awaiting-EA-decision；方案仍candidate。','用单轨“层层审批”遗漏团队自治，或以自治绕过EA护栏，应拒绝。'),
2:('新虚构五角色：业务赞助人看价值，业务负责人确认功能，IT负责人管生产控制，EA委员会定标准豁免，MSA团队提方案/实施本范围决定；五者职权由本项目材料明确。','分别建立角色→请求/参加/决定/实施权限，不由头衔自动补授权；申请与裁决区分。','五角色权限矩阵，EX-1申请人MSA团队、裁决者EA委员会，赞助人投资批准不等豁免。','以赞助人或IT批准替代EA豁免、以EA裁决代做团队实现，应拒绝。'),
3:('新虚构发布清单每次记录双人复核、最小权限管道、自动测试和监控；第1次发布测试有结果但第二复核者缺签名，运行反馈发现错误增加。','每次发布有独立控制证据，缺复核保持blocked；反馈产生变更候选不自动授下一发布许可。','REL-1发布blocked（缺第二复核），FEEDBACK-1产生candidate change；EX-1仍待裁决。','用上次复核覆盖本次发布或用拟议监控当风险已可控，应拒绝。')},
'msa-value-resource-evidence-method':{
2:('新虚构预约服务唯一ABF为预约时段判断，预期减少人工核实；备件服务唯一ABF为备件可用判断，业务价值尚未观察；不按一个ABF推定收益已实现。','服务→ABF一一说明，业务价值另记expected/observed；开发/运营资源与价值度量不混。','预约/备件各一ABF，预约value=expected减少核实、备件value=unknown，均无ROI。','两个ABF塞同服务、或一个ABF即已实现价值，应退回边界/度量澄清。'),
4:('新虚构本例定义WP-appointment交付预约试点T-pilot，WP-parts交付备件扩大T-expanded；T-expanded依赖T-pilot验收且运营工时未知。','新建本例工作包与命名状态对象，不再当悬空外部引用；开发/运营计划按月分格绑定状态。','两工作包映射两状态；T-expanded=blocked-by-unknown-operations-plan，不按9人日开发放行运营。','缺状态定义仍声称内部引用完整，或把开发预算覆盖未知运营计划，应拒绝。')},
'bi-usage-goal-measures-method':{
2:('新虚构项目计数目标11月达到1个生产采用自动检查，参考目标只是改善决策；采用证据需负责人、实际工单使用和稳定运行记录，基线0不计算相对增长。','project_metric与reference_goal分字段；计数目标、基线、观察、窗口、责任、来源分别记录。','目标1、基线0、当前观察unknown；reference_goal=改善决策，不能从目标推出采用已发生。','用基线0给增长300%，或把参考目标当实测数字，应拒绝。'),
5:('新虚构U1试点10个预警工单，8个在调度前复核、3个改变调拨；项目比例定义3/10=30%，时效满足比例8/10=80%，仅本试点周；仍无稳定运行证据。','按预警工单10作声明分母分别计算改变比例与时效比例；实际观察、目标、方向各自状态独立。','本周两观察为30%/80%，目标达成unknown，生产采用仍缺稳定运行。','分母换成全体工单不披露，或两个比例直接相加，或据一次试点判生产采用，应拒绝。')},
'bi-business-function-coverage-method':{
1:('新虚构练习加载G238表4-2全部54行，保留宏观/子功能、分组与原定位；本例另给用途待办管理与模型监控计划证据。','来源行和本地判定分列，不将54行当同粒度评分项。','54条source_row snapshot与54条assessment，源ID唯一完整。','漏宏观行或复制子项凑54，应拒绝完整性声明。'),
2:('新虚构范围两城维修试点2026年11月；U1/U2用途待办有责任人、更新记录与审核证据，模型准确性监控只计划2026-11-20试验。','按具体定义映射用途管理源行，运行证据与计划分别取证，其他行保持unknown。','仅G238-T4-2-04=evidenced-in-example，G238-T4-2-47=planned，其余52=unknown。','按两个用途数推两已见行或计划监控计已见，应拒绝。'),
3:('新虚构状态规则四类：evidenced-in-example需符合行定义产物；planned需负责人/时点/验收；unknown为未查；out-of-scope-with-reason须范围理由，仍不等机构不适用。','按证据逐行判定；父组已见不继承给子功能，不计算成熟度。','54行互斥四态；没有证据的不填0、不变不适用。','顶层组一条证据自动传全子行，或unknown改不满足，应拒绝。'),
5:('新虚构业务负责人要求先访谈U1相关数据/模型监控条目，再其余；每未证实行记录负责团队、需证、下一复评触发，具体日期未承诺。','逐行gap_action结合reference_name，不批量仅“待完善”；优先理由=U1关联而非ID大小。','52条unknown各有候选补证行动和责任组；planned行有独立验收条件，仍candidate。','删未知行以提高覆盖率，或没有行动责任就标缺口closed，应拒绝。')},
'bi-application-function-coverage-method':{
1:('新虚构练习加载G238表4-3全部59子功能，保存10详细组与9高层组各自来源身份。','按源行ID闭合59条，不以高层9组替代逐行清单。','59条完整source/assessment，组间对应只作reference mapping。','只登记9高层组或把详细组全继承高层状态，应拒绝。'),
2:('新虚构范围两城维修2026年11月；RUN-SUP-BATCH记录库存文件批交换的输入输出校验值、时点和异常隔离，没有流处理/交互测试。','运行日志仅匹配具体批交换行，不从“交换”名称推流式与交互式。','仅G238-T4-3-20=evidenced-in-example，其余58=unknown；实时/供应商能力仍未决。','把一次夜批证据用来放行流式或秒级项，应拒绝。'),
3:('新虚构逐行采用四态规则；本轮没有planned/不适用的充分材料。','保持1已见、58未知；unknown不等不满足，零已见以外不作性能失败断言。','59行总数闭合，四态计数1/0/58/0；不是能力覆盖率。','用1/59认定平台建设水平，或将58未知自动不适用，应拒绝。'),
5:('新虚构先调查U1需要的时效/批量/权限条目，责任为数据工程/平台组；逐行需要对应功能测试或接口证据。','为每未知行形成以source reference_name命名的具体测试/补证任务，不以采购手册充运行。','58条候选gap_action，含负责组与证据类型；一条补证仅更新该源行。','一个产品手册使所有59已见，或补一条同步升级组内其他项，应拒绝。')},
'mdm-business-function-coverage-method':{
1:('新虚构练习加载G21B表5-3全部29业务功能，每行保留reference_id、分组、定义和来源定位。','复制完整源行建立独立评估条目，不能用“治理”一个宏观项覆盖29。','29行唯一source ID和assessment条目。','漏行或重名合并导致少于29，应拒绝清单完整性。'),
2:('新虚构2026年11月两馆限定自有记录；任命材料已明确所有者/管家职责、范围、任期和接受记录，只证明本范围治理角色，不证明其余功能。','新证据映射“定义并吸纳数据所有者/管家”具体行；原愿任材料仍保留旧版本。','G21B-T5-3-02=evidenced-in-example，其余28=unknown；旧任命意愿不倒改历史。','单愿任或仅一个角色名即判完整治理，应拒绝。'),
3:('新虚构项目四态规则：有匹配职责和实际活动产物才已见，有完整执行安排才计划，其他未知；外部采购范围外仍另记scope。','29行互斥状态，外部采购不得无机构职责理由记不适用。','计数1/0/28/0，外采一行scope=out-of-project-scope、coverage=unknown。','将外部采购未知改机构不适用，或清单完整即成熟度通过，应拒绝。'),
5:('新虚构先补与读者关联、同意及质量有关行，由所有者/管家/安全分别提活动和证据；其他未知行需访谈负责团队。','每源行按具体功能定义写需证任务、提议责任、复评事件；不把已任命当所有任务closed。','28行unknown有候选行动与责任分工，缺真实批准仍candidate。','把任命一次作为29行运行证据或丢弃未知行，应拒绝。')},
'mdm-application-function-coverage-method':{
1:('新虚构练习加载G21B表5-4全部38应用功能，第三操作“定义/删除”来源冲突独立保存。','源ID/定义/分组与冲突分别保留，不默认裁决歧义。','38行来源与assessment闭合，conflicts保留双解释。','为完成清单静默择Delete或丢冲突行，应拒绝。'),
2:('新虚构2026年11月隔离教学演练UNMERGE-SUP：将两误合并来源恢复两映射，重指两消费者，记录更正与撤销审计；只演练取消合并行。','映射实际教学结果到取消合并具体行，源冲突不因该演练关闭。','仅G21B-T5-4-16=evidenced-in-example，其余37=unknown，取消合并由请求推进教学证据。','仅有取消合并需求就判已见，或演练使其他功能连带已见，应拒绝。'),
3:('新虚构四态规则不以“尚无运行证据”推“已确认不存在”；本次没有其他充分计划/不适用材料。','38行逐一状态闭合为1/0/37/0，事实观察和来源语义冲突两个字段。','未知保持unknown；删除传播相关行仍unresolved-conflict，不能承诺。','把语义裁决写为实现测试通过，或把37未知写不具备，应拒绝。'),
5:('新虚构管家提议先补取消合并消费者恢复边界，架构/安全组核对第三操作；其余逐行需对应功能测试。','每未知行按具体reference name形成补证候选，冲突行动包含原文核对与项目契约裁决两个层次。','37未知行有候选gap_action、owner和review trigger；冲突未裁決不close。','只按图标签实现删除并宣布能力具备，或按计划日期自动关闭冲突，应拒绝。')},
'bi-value-chain-controls-method':{
3:('新虚构批次B-SUP-1：RAW-1库存10、需求12；TECH-1只转日期类型，BUS-1按12>10形成缺件候选，SEM-1解释同一站点/时点，CONSUME-1等待调度确认。','逐层输出保存input_record_ids、output_record_ids、rule_id和batch_id；derived_from方向输出→输入或derives方向输入→输出必须按选定词汇声明。','四条声明方向的派生关系与五层记录，原RAW不可变，候选不自动下单。','反转派生方向、就地改库存或只表名血缘无规则版本，应拒绝。'),
4:('新虚构每层责任RAW平台/TECH工程/BUS业务/SEM业务/消费调度；字段仅站点/时点/数量，不含联系方式；源as-of未知则不授实时，质量异常隔离。','逐层核质量、访问范围、元数据和责任，与项目使用授权分开；缺一类登记具体缺口。','五层控制矩阵有字段清单和提议负责人；源时效unknown阻断及时性结论，运行授权candidate。','用血缘存在证明数据正确/及时，或仅技术类型正确就认为口径统一，应拒绝。')},
'bi-model-operating-monitoring-method':{
3:('新虚构影子周样本五笔actual/predicted耗时分别(20,10),(20,5),(20,15),(20,0),(20,20)分钟；误差[10,15,5,20,0]；业务为本周样本提议15分钟阈值，标签质量和访问范围仍未知。','逐条绝对差后排序取中位10；阈值来源/单位/周窗口分列，不改成准确率。','observed median_absolute_error=10分钟、sample_count=5、threshold=15候选；仅该样本值可复算，阈值待裁决不授整体达标。','无阈值批准即判生产达标或将10分钟改85%准确率，应拒绝。'),
5:('新虚构运行记录RUN-SUP-1在影子期作业失败触发stop-suggestions，人工接管；新v0.2只有重训文件、尚无版本测试与业务复核。','保存故障/停止/人工处置时点和证据；监控观察与版本准入分开，review_result针对具体样本和规则。','RUN-SUP-1保留停止事件，v0.2=awaiting-test-and-business-review，不自动投产；标签/安全缺口仍开。','用训练完成恢复建议或让失败期继续输出客户承诺，应拒绝。')},
'agile-collaboration-selection-switch':{6:('新虚构下周期两队三能力分别有范围限定演练记录，但委员会授权尚pending；计划保留B-BOOK/B-CANCEL/G-PRIV和旧DORP历史；第4轮只新增无障碍确认待验收。','生成候选选择及时间差交接两布局；能力和授权分别评估，关闭旧交接只能新增未来状态记录。','跨职能切换为candidate-not-authorized；能力不足分支保留解决方案协作，旧历史hash不改；两布局需要实际生成另取证。','仅DEV-A三能力便切两队，删除旧DORP或在冲刺0生成MVA，应拒绝；缺真实两布局证据不能记渲染通过。')},
}
assert sum(len(v) for v in rows.values())==47
caps=json.loads((shared/'capabilities.json').read_text());methods={m['id']:m for m in caps['analysis_methods']}
profile_by_id={p['id']:p for p in caps['profiles']}
profiles={'reference-model-tailoring':'government-reference-catalog-overlay','government-reference-catalog-overlay-method':'government-reference-catalog-overlay','dbrm-mapping-suite-method':'dbrm-adm-content-map','digital-enablement-competency-mapping-method':'digital-enablement-competency-overlay',**{n+'-method':n for n in ['bi-business-function-coverage','bi-application-function-coverage','mdm-business-function-coverage','mdm-application-function-coverage']}}
def reference_projection(profile):
 return [{'entity_id':e['id'],'reference_attributes':{k:copy.deepcopy(v) for k,v in e['attributes'].items() if k.startswith('reference_') or k in {'source_locator','source_uncertainty','source_row_id','pillar','competency','dpbok_context','context_kind','raw_cells','source_line','source_lines'}}} for e in profile['example']['entities']]

for mid,records in rows.items():
 steps=methods[mid].get('analysis_steps') or methods[mid].get('steps')
 payload={'schema_version':'procedural-teaching-supplement/1','method_id':mid,'date':'2026-11-08','notice':'本轮新增虚构教学材料与作者候选转换结果。原案例缺输入版本保留；不证明真实企业事实、盲测Agent或人的验收。','steps':[{'position':i,'declared_step':steps[i-1],'new_fictional_input':v[0],'transformation':v[1],'candidate_output':v[2],'adverse_variant_expected':v[3],'runtime_execution':'not-claimed-by-written-example','approval_status':'candidate'} for i,v in sorted(records.items())],'accepted':False,'origin':'new-fictional-teaching-materials','source_inputs':[],'candidate_records':[]}
 if mid in profiles:
  p=profile_by_id[profiles[mid]]
  payload['registered_reference_profile']=p['id']
  payload['source_inputs'].append({'path':'../../../capabilities.json','profile_id':p['id'],'reference_rows_sha256':hashlib.sha256(json.dumps(reference_projection(p),ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'purpose':'reference row identities/definitions only; original profile business judgments are not copied as new evidence'})
  payload['reference_rows']=reference_projection(p)
 if mid in {'reference-model-tailoring','government-reference-catalog-overlay-method'}:
  source=shared/'references/source-tables/government-reference-catalog.json';cat=json.loads(source.read_text())
  payload['source_inputs'].append({'path':'../../source-tables/government-reference-catalog.json','sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
  payload['source_catalog_counts']=cat['counts'];payload['department_scope']=[{'reference_id':s['id'],'reference_name':s['name'],'scope':'adopted' if s['name'] in ['财政','共享服务'] else 'out-of-project-scope','reason':'只覆盖养老资产投资与待遇发放，不推断其他机构职责不存在','reassessment':'项目扩大范围时'} for s in cat['sectors']]
  payload['source_catalog_snapshot']={'sectors':cat['sectors'],'nodes':cat['nodes']}
  payload['candidate_records']=[{'local_id':'LF-SUP-INVEST','local_name':'养老资产投资','reference_path':['财政','投资管理','养老基金管理'],'mapping_type':'candidate-project-classification','approval_status':'candidate'}] if mid=='reference-model-tailoring' else []
 if mid=='dbrm-mapping-suite-method':
  source=shared/'references/source-tables/dbrm-reference-mappings.json';d=json.loads(source.read_text());payload['source_inputs'].append({'path':'../../source-tables/dbrm-reference-mappings.json','sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
  payload['source_tables_snapshot']=d['tables'];texts=['无障碍确认访谈','状态查询产品待办','跨科室养老试点范围','可靠确认业务动机','养老申报业务产品','财政/待遇/平台三方协作','线上查询与人工协助运营','受理/核验能力','服务台与受控运行平台','受控接口与追溯字段']
  items=[e for dom in d['taxonomy'] for e in dom['elements']];payload['candidate_records']=[{'reference_element_id':e['id'],'reference_name':e['name'],'project_observation':t,'mapping_status':'candidate-project-mapping','evidence':'SUP-DBRM-'+str(i)} for i,(e,t) in enumerate(zip(items,texts),1)]
 if mid in {'bi-business-function-coverage-method','bi-application-function-coverage-method','mdm-business-function-coverage-method','mdm-application-function-coverage-method'}:
  special={'bi-business-function-coverage-method':{'G238-T4-2-04':'evidenced-in-example','G238-T4-2-47':'planned'},'bi-application-function-coverage-method':{'G238-T4-3-20':'evidenced-in-example'},'mdm-business-function-coverage-method':{'G21B-T5-3-02':'evidenced-in-example'},'mdm-application-function-coverage-method':{'G21B-T5-4-16':'evidenced-in-example'}}[mid]
  for e in profile_by_id[profiles[mid]]['example']['entities']:
   a=e['attributes'];rid=a['reference_id'];payload['candidate_records'].append({'reference_id':rid,'reference_name':a['reference_name'],'reference_group':a['reference_group'],'reference_level':a['reference_level'],'source_locator':a['source_locator'],'coverage_status':special.get(rid,'unknown'),'project_scope':'本轮明确新增虚构教学试点，2026年11月','project_evidence':'SUP-'+rid if rid in special else '未取得该行定义要求的活动或运行证据','proposed_owner':'数据工程组' if 'application' in mid else '业务所有者与管家','gap_action':'取得并按本试点核对“'+a['reference_name']+'”的活动/功能证据；范围、时点与验收另记','next_review':'对应证据取得或范围变更时','approval_status':'candidate'})
 # Concrete records are separately authored from the registered reference fields.
 # No inherited profile coverage judgment is allowed to become new evidence.
 if mid=='mdm-four-plateau-operations-method':
  kernel='读者身份/联络/目的限定同意内核；合同、报价及借阅交易不在内核'
  payload['candidate_records']=[{'id':'P'+str(i),'use_scope':s,'mastership':m,'scope_boundary':kernel,'approval_status':'candidate','operability':'unknown' if i else 'source-operation-in-fictional-material'} for i,s,m in [(0,'各馆旧用例','源系统'),(1,'跨馆只读分析','源系统；MDM分析记录无运营写权'),(2,'两馆约定内核试点','MDM主控限定内核字段'),(3,'全馆约定完整内核用例','MDM主控约定完整内核，交易主控保持')]]
  descriptions={'P0':['各馆旧用例目录SUP-P0-USE','源记录核验SUP-P0-QUALITY','馆内权限SUP-P0-AUTH','源备份SUP-P0-BACKUP；不证明错合并恢复','现有源支持SUP-P0-SUPPORT'], 'P1':['跨馆分析用例草案','人工核验规则草案','只读权限申请草案','分析记录可重复重建草案','夜批值班设计'], 'P2':['两馆内核用例草案','未取得质量测试','未取得内核写授权','未取得错合并恢复演练','未取得积压监控运行记录'], 'P3':['全馆完整约定内核用例草案','未取得全范围质量观察','未取得全范围写授权','未取得全范围恢复演练','未取得全范围监控/支持记录']}
  payload['operating_condition_records']=[{'plateau_id':pid,'condition':field,'input_detail':detail,'evidence_status':'authored-fictional-record' if pid=='P0' else ('designed-not-verified' if pid=='P1' or ix==0 else 'unknown'),'approval_status':'candidate'} for pid,details in descriptions.items() for ix,(field,detail) in enumerate(zip(['use_cases','quality','authorization','recovery','support_monitoring'],details))]
 if mid=='government-reference-catalog-overlay-method':
  node_by_id={x['id']:x for x in cat['nodes']}
  selected=[]
  for leaf in ['G21D-S08-F04-S04','G21D-S11-F05-S06']:
   n=node_by_id[leaf]; selected.extend([n['parent_id'].split('-F')[0],n['parent_id'],leaf])
  payload['candidate_records']=[{'reference_id':rid,'reference_path':node_by_id[rid]['path'] if rid in node_by_id else [next(s['name'] for s in cat['sectors'] if s['id']==rid)],'mapping_type':'candidate-project-classification','local_object_ids':['LOCAL-ASSET'] if rid.startswith('G21D-S08') else ['LOCAL-BENEFIT'],'approval_status':'candidate'} for rid in selected]
  payload['candidate_relationships']=[{'id':'REF-CLASS-'+str(ix),'source':parent,'target':child,'type':'reference_classifies','approval_status':'candidate'} for ix,(parent,child) in enumerate([(selected[0],selected[1]),(selected[1],selected[2]),(selected[3],selected[4]),(selected[4],selected[5])],1)]
  payload['project_relationships']=[{'id':'PROJECT-RECONCILE','source':'LOCAL-ASSET','target':'LOCAL-BENEFIT','type':'project-reconciliation-dependency','coordinator':'LOCAL-PENSION','source_identity':'project-only','approval_status':'candidate'}]
 if mid=='reference-model-tailoring':
  payload['candidate_records'][0].update(reference_id='G21D-S08-F04-S04',local_proposed_owner='资产投资组',reference_source_locator='G21D §8.1 L796')
 if mid=='dbrm-mapping-suite-method':
  payload['local_architecture_domains']=['business','data','application','technology']
  payload['local_row_overlays']=[{'source_table_id':t['id'],'source_row_id':row['id'],'local_object_ids':[],'local_evidence':[],'mapping_status':'unknown','needed_input':'取得并核对该源行维度对应的本地对象、使用阶段/层级与产物；十要素访谈不能替代每行关系证据','approval_status':'candidate'} for t in d['tables'] for row in t['rows']]
  payload['project_only_additions']=[{'id':'PROJECT-G','adm_phase':'G','project_proposal':'接口监控','source_identity':'project-only','source_table_cell_verified':False,'approval_status':'candidate'}]
 if mid=='digital-enablement-competency-mapping-method':
  source=shared/'references/source-tables/dbrm-reference-mappings.json';d=json.loads(source.read_text());t=next(t for t in d['tables'] if t['id']=='G21H-T4-1')
  payload['source_inputs'].append({'path':'../../source-tables/dbrm-reference-mappings.json','sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
  payload['source_tables_snapshot']=[t]
  proposed_roles=['EA-LEAD','DATA-STEWARD','PRODUCT-LEAD','SERVICE-OWNER','DELIVERY-LEAD','ANALYST','DELIVERY-LEAD','OPS-LEAD','SERVICE-OWNER','OPS-LEAD','SECURITY-LEAD','DELIVERY-LEAD']
  payload['candidate_records']=[{'source_row_id':row['id'],'pillar':row['resolved_cells']['pillar'],'competency':row['resolved_cells']['competency'],'dpbok_context':row['resolved_cells']['dpbok_context'],'context_kind':'organizational-scaling-context-not-maturity-level','local_proposed_role':role,'assessment':'unknown','requested_work_product':row['resolved_cells']['competency']+'在养老试点约定范围的独立工作产物及复核记录','gap_action':'取得该工作产物并核对语境与职责范围；不按角色名称判一般人员能力','review_trigger':'工作产物取得或本地协作范围变化','approval_status':'candidate'} for row,role in zip(t['rows'],proposed_roles)]
 if mid in {'bi-business-function-coverage-method','bi-application-function-coverage-method','mdm-business-function-coverage-method','mdm-application-function-coverage-method'}:
  input_details={
   'G238-T4-2-04':{'id':'SUP-G238-T4-2-04','kind':'authored-use-backlog','contents':{'version':'SUP-BACKLOG-1','owner':'试点分析负责人','qualified_use_criteria':'业务责任、所需决策与验收可定位','uses':[{'id':'U1','decision':'缺件预警在调度前人工复核','qualified':True},{'id':'U2','decision':'将月度趋势用于维修队规划','qualified':True}],'update_record':'2026-11-06记录U2口径变更','review_record':'2026-11-07责任人在本虚构材料中确认两项为合格用途'}},
   'G238-T4-2-47':{'id':'SUP-G238-T4-2-47','kind':'authored-plan','contents':{'owner':'模型运营负责人','target_date':'2026-11-20','acceptance':'固定标签样本、声明误差单位与阈值来源，保存一次部署模型准确性监控记录','runtime_observation':'not-supplied'}},
   'G238-T4-3-20':{'id':'SUP-G238-T4-3-20','kind':'authored-batch-run-record','contents':{'schedule':'2026-11-06 02:00计划异步库存文件分发','input_file':'inventory-SUP-01.csv','input_rows':2,'output_file':'inventory-SUP-01-delivered.csv','output_rows':2,'input_records':[{'station':'A','quantity':10},{'station':'B','quantity':8}],'output_records':[{'station':'A','quantity':10},{'station':'B','quantity':8}],'validation':'逐行数量一致','malformed_file':'inventory-SUP-bad.csv','exception_result':'隔离并告警，不覆盖本批有效文件','window_end':'2026-11-06 02:03','limit':'只支持该教学批交换，不含流式/交互式证据'}},
   'G21B-T5-3-02':{'id':'SUP-G21B-T5-3-02','kind':'authored-role-onboarding-record','contents':{'scope':'两馆自有读者身份/联络/目的限定同意内核','owner':'LIB-OWNER','steward':'LIB-STEWARD','term':'2026-11试点','owner_duties':['批准内核口径与用途','裁决质量优先次序'],'steward_duties':['维护来源映射','记录质量问题并协调更正'],'fictional_acceptance_records':['LIB-OWNER-SUP接受本范围职责','LIB-STEWARD-SUP接受本范围职责与每周2小时可用容量'],'BAU_activity':'2026-11-07在材料中登记MDM-SUP-Q1并指派管家跟进','limit':'本轮独立虚构任命/吸纳，不证明其余28功能或真实批准'}},
   'G21B-T5-4-16':{'id':'SUP-G21B-T5-4-16','kind':'authored-unmerge-rehearsal-record','contents':{'operator':'LIB-STEWARD-SUP','environment':'隔离教学模型','before_mapping':{'LIB-A-17':'G-SUP-1','LIB-B-92':'G-SUP-1'},'manual_request':'请求恢复两来源身份','after_mapping':{'LIB-A-17':'G-SUP-17','LIB-B-92':'G-SUP-92'},'consumer_repointing':{'C-A':'G-SUP-17','C-B':'G-SUP-92'},'audit':'撤销原因、前后映射与消费者更正已在本材料留存；历史交易不改写','limit':'仅支持人工取消合并行，不关闭推送第三操作的来源冲突'}}}
  payload['fictional_input_records']=[input_details[rid] for rid in special]
  for row in payload['candidate_records']:
   rid=row['reference_id'];row.update(evidence_ids=['SUP-'+rid] if rid in special else [],implementation_ref='SUP-'+rid if rid in special else 'unknown')
   if rid in special: row['project_evidence']=json.dumps(input_details[rid]['contents'],ensure_ascii=False)
   if rid=='G238-T4-2-47': row.update(plan_owner='模型运营负责人',plan_date='2026-11-20',plan_acceptance=input_details[rid]['contents']['acceptance'])
   if mid.startswith('mdm-'): row['project_scope']='2026年11月两馆自有读者约定内核；本轮独立虚构补充'
  if mid=='mdm-business-function-coverage-method':
   for row in payload['candidate_records']:
    if '采购' in row['reference_name']:row['scope_status']='out-of-project-scope-without-institution-applicability-judgment'
  if mid=='mdm-application-function-coverage-method':
   payload['unresolved_source_conflicts']=[{'reference_id':'G21B-T5-4-24','table_reading':'创建/更新/定义/合并','figure_reading':'Create/Update/Delete/Merge','third_operation_status':'unresolved','project_contract_status':'pending-separate-decision','approval_status':'candidate'}]
 if mid=='product-architecture-allocation-method':
  payload['candidate_records']=[{'function_id':'F-SUBMIT','component_id':'C-CASE','interface_id':'I-SUBMIT','operating_capability':'受理核验','technical_dependency':'TC-API','evidence':'SUP-ALLOC-1','approval_status':'candidate'},{'function_id':'F-STATUS','component_id':'C-STATUS','interface_id':'I-STATUS','operating_capability':'状态告知','technical_dependency':'TC-API','evidence':'SUP-ALLOC-2','approval_status':'candidate'},{'function_id':'F-ASSIST','component_id':'C-DESK','interface_id':'I-ASSIST','operating_capability':'代理受理','authorization':'unknown','evidence':'SUP-ALLOC-3','approval_status':'candidate'}]
  payload['candidate_relationships']=[{'id':'REL-'+r['function_id'],'source':r['function_id'],'target':r['component_id'],'type':'allocates_function','evidence':r['evidence'],'approval_status':'candidate'} for r in payload['candidate_records']]
 if mid=='msa-federated-governance-process-method':
  payload['candidate_records']=[{'role':r,'request':req,'participate':part,'decide':dec,'implement':impl,'approval_status':'candidate'} for r,req,part,dec,impl in [('业务赞助人','价值投资需求','价值取舍','投资范围（项目提议）','不代写技术实现'),('业务负责人','业务功能需求','功能验收','业务功能口径（项目提议）','业务活动与验收'),('IT负责人','生产控制要求','发布风险','生产控制范围（项目提议）','生产支持'),('EA委员会','标准审阅议题','跨产品架构评审','企业标准豁免（项目提议）','不代做单服务实现'),('MSA团队','EX-1豁免申请','服务方案/反馈','护栏内服务细节（项目提议）','本范围契约/发布/数据/运维')]]
  payload['governance_tracks']=[{'id':'EA-TRACK','scope':'企业标准与跨产品决定','guardrail':'最小权限','open_item':'EX-1待EA裁决'},{'id':'MSA-TRACK','scope':'单服务细节与护栏内自治','release':'REL-1缺第二复核签名，blocked','feedback':'FEEDBACK-1只形成候选变更'}]
 if mid=='bi-value-chain-controls-method':
  names=['RAW','TECH','BUS','SEM','CONSUME'];data=[{'station':'A','as_of':'unknown','stock':10,'demand':12},{'date_type_conversion_only':True},{'shortage_candidate':2,'decision_authorized':False},{'definition':'同站点同声明批次需求12减库存10为缺件候选2'},{'decision':'awaiting-dispatcher-confirmation'}]
  payload['candidate_records']=[{'id':n+'-1','batch_id':'B-SUP-1','fields':v,'proposed_owner':o,'approval_status':'candidate'} for n,v,o in zip(names,data,['平台组','工程组','业务组','业务组','调度'])]
  payload['candidate_relationships']=[{'id':'DERIVE-'+str(i),'type':'derived_from','source':names[i]+'-1','target':names[i-1]+'-1','rule_id':'RULE-SUP-'+str(i),'rule_version':'1','batch_id':'B-SUP-1','approval_status':'candidate'} for i in range(1,5)]
 if mid=='bi-model-operating-monitoring-method':
  payload['candidate_records']=[{'id':'SAMPLE-SUP-'+str(i),'actual_minutes':20,'predicted_minutes':v,'absolute_error_minutes':abs(20-v),'approval_status':'candidate'} for i,v in enumerate([10,5,15,0,20],1)]
  payload['candidate_metric']={'metric':'median_absolute_error','value':10,'unit':'minutes','sample_count':5,'window':'authored-shadow-week','threshold_proposal':15,'threshold_approval':'pending','production_acceptance':False}
  payload['candidate_events']=[{'id':'RUN-SUP-1','event':'job-failed','action':'stop-suggestions; manual-takeover','next_version':'v0.2','version_test':'not-supplied','business_review':'pending','approval_status':'candidate'}]
 if mid=='agile-collaboration-selection-switch':
  payload['fictional_input_records']=[{'id':'SUP-'+team+'-'+str(i),'team_id':team,'capability':capability,'demonstration_scope':'图书馆预约/取消/无障碍确认教学试点','authored_demonstration':'范围限定工作产物已由本虚构材料记录；不证明一般人员能力','real_business_acceptance':False} for team in ['DEV-A','DEV-B'] for i,capability in enumerate(['业务开发','企业架构','解决方案开发'],1)]
  payload['candidate_records']=[{'id':'SUP-CURRENT-CHOICE','selected_pattern':'solution','reason':'独立EA与方案持续协作，保留既有历史；下一周期授权未取得','approval_status':'candidate'},{'id':'SUP-NEXT-CHOICE','proposed_pattern':'functional','selection_status':'candidate-not-authorized','team_capability_scope':'两队六份范围限定虚构材料','authorization':'architecture-committee-pending','retained_backlog_ids':['B-BOOK','B-CANCEL','G-PRIV'],'future_handoff_closure':'仅在未来授权后追加状态事件；本轮不关闭旧记录','approval_status':'candidate'}]
  payload['new_sprint_record']={'order':4,'goal':'无障碍确认','timebox':'2周（项目约定）','acceptance':'pending','does_not_depend_on_mode_switch':True}
 if mid=='msa-contract-consumer-evidence-method':
  payload['candidate_records']=[{'consumer_id':c,'contract_version':'eligibility/v1.1','discovery':'受控服务目录','address':'catalog:eligibility/v1.1','token_audience':c if c!='C-MOBILE' else 'pending','permission':'eligibility:read-minimal' if c!='C-MOBILE' else 'not-granted','authorization_evidence':'SUP-AUTH-'+c if c!='C-MOBILE' else 'application-only','unknown_reason_codes':'消费者必须保留未知并转人工；本材料仅设计，消费者测试未取得','approval_status':'candidate'} for c in ['C-BOOK','C-DESK','C-MOBILE']]
  payload['fictional_input_records']=[{'id':'SUP-AUTH-'+c,'kind':'authored-scope-limited-grant-record','consumer_id':c,'audience':c,'scope':'eligibility:read-minimal','real_organization_grant':False} for c in ['C-BOOK','C-DESK']]
  payload['latency_observation']={'load_requests_per_second':20,'window_minutes':10,'authored_P95_ms':180,'project_target_ms':200,'limit':'只支持本负载窗教学数值；不证明独立消费者未知码测试或月SLA'}
  payload['monthly_availability']={'target_percent':99.5,'observation':'unknown','acceptance':'pending'}
 if mid=='bi-stage-operability-and-exit-method':
  payload['candidate_records']=[{'id':sid,'expected_benefit':benefit,'proposed_owner':owner,'operability':'unknown','conditions':{'people':owner+'提议负责，接受记录未取得','systems':'对应状态系统清单草案，健康/恢复测试未知','data':'该状态数据对账未验证','controls':'权限、规则与审计设计待复核','rollback':'已提出恢复草案，未做演练'},'approval_status':'candidate'} for sid,benefit,owner in [('S1','设备事件形成可核提示','分析负责人'),('S2','统一原始供数','数据负责人'),('S3','减少旧仓双轨','运营负责人')]]
  payload['old_use_exit_records']=[{'id':'OLD-audit','new_implementation':'新平台审计回放候选','authored_test_evidence':'SUP-AUDIT逐批源记录、规则版本与历史值比对一致（仅新增虚构资料）','coverage_status':'evidenced-in-example','metadata':'字段血缘与规则版本草案','governance':'留存访问与责任待批准','recovery':'演练未取得','approval_status':'candidate'},{'id':'OLD-monthly','new_implementation':'新平台月报候选','coverage_status':'unknown','missing':'未取得历史月报复算','approval_status':'candidate'}]
  payload['retirement_decision']={'status':'blocked','reason':'月报复算、治理与恢复验证未齐','old_warehouse':'retained','approval_status':'candidate'}
 if mid=='bi-requirement-origin-boundary-method':
  payload['candidate_records']=[{'id':'R-SUP-1','origin':'new-fictional-project-workshop','requester':'审计员','statement':'从一个已发布看板指标查到源批次、规则版本及处理时间','acceptance_test':'对一指定已发布指标检查三个追溯字段与来源记录可定位；缺任何字段则本需求未满足','atomic_result':'该指标来源追溯可定位','duplicate_status':'与R-SUP-2结果不同','source_reference_identity':'project-only; not an official requirements ID','approval_status':'candidate'},{'id':'R-SUP-2','origin':'new-fictional-project-workshop','requester':'业务负责人','statement':'记录看板净收入术语的版本及生效日','acceptance_test':'指定术语可查到定义版本、生效日与负责人的候选复核记录','atomic_result':'术语定义版本可定位','duplicate_status':'与R-SUP-1结果不同','source_reference_identity':'project-only; not an official requirements ID','approval_status':'candidate'}]
 if mid=='msa-value-resource-evidence-method':
  payload['candidate_records']=[{'service_id':'SVC-APPOINTMENT','single_ABF':'预约时段判断','business_value':'expected减少人工核实','observed_business_value':'unknown','work_package_id':'WP-appointment','state_id':'T-pilot','development_plan':'本材料按月记录，与运营工时分列；不由开发计划推已投入','operations_plan':'unknown','ROI':'not-computed','approval_status':'candidate'},{'service_id':'SVC-PARTS','single_ABF':'备件可用判断','business_value':'unknown','observed_business_value':'unknown','work_package_id':'WP-parts','state_id':'T-expanded','development_plan':'9人日仅本例声明开发计划，不是已完成','operations_plan':'unknown','ROI':'not-computed','approval_status':'candidate'}]
  payload['named_state_records']=[{'id':'T-pilot','definition':'预约服务限定试点的候选运营状态','acceptance':'unknown','approval_status':'candidate'},{'id':'T-expanded','definition':'备件服务扩大范围的候选状态','depends_on':'T-pilot acceptance','operations_condition':'运营计划和恢复未核实，blocked','approval_status':'candidate'}]
  payload['work_package_records']=[{'id':'WP-appointment','delivers_state':'T-pilot','approval_status':'candidate'},{'id':'WP-parts','delivers_state':'T-expanded','approval_status':'candidate'}]
 if mid=='bi-usage-goal-measures-method':
  payload['candidate_records']=[{'id':'SUP-ADOPTION-TARGET','metric_kind':'project-count','reference_goal':'改善决策','project_target':1,'baseline':0,'unit':'生产采用的自动检查个数','window':'2026年11月','owner':'试点分析负责人（提议）','observed_value':'unknown','required_adoption_evidence':['负责人接受','真实工单使用','稳定运行记录'],'target_achieved':'unknown','relative_growth':'not-defined-at-zero-baseline','approval_status':'candidate'},{'id':'SUP-U1-CHANGED','metric_kind':'project-fraction','numerator':3,'denominator':10,'denominator_definition':'本虚构试点周的10个预警工单','observed_percent':30,'unit':'percent','target':'unknown','causal_claim':'not-established','approval_status':'candidate'},{'id':'SUP-U1-TIMELY','metric_kind':'project-fraction','numerator':8,'denominator':10,'denominator_definition':'同10个预警工单','observed_percent':80,'unit':'percent','target':'unknown','adoption_status':'stable-production-evidence-missing','approval_status':'candidate'}]
  payload['fictional_input_records']=[{'id':'SUP-WORK-ORDER-'+str(i),'reviewed_before_dispatch':i<=8,'changed_dispatch':i<=3,'scope':'U1试点周','real_runtime_record':False} for i in range(1,11)]
 if not payload['candidate_records']:
  payload['candidate_records']=[{'id':'SUP-STEP-'+str(step['position']),'step_position':step['position'],'candidate_statement':step['candidate_output'],'approval_status':'candidate','accepted':False} for step in payload['steps']]
 file=out/(mid+'.json');file.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 case=case_dir/(mid+'.md');body=case.read_text();heading='## 本轮新增的逐步骤教学补充'
 if heading in body:body=body[:body.index(heading)]+body[body.index('## 评审记录',body.index(heading)):]
 text='## 本轮新增的逐步骤教学补充\n\n2026-11-08新增的独立虚构材料见[完整输入、候选转换、来源行及反例](../method-case-materials/procedural-supplements/'+mid+'.json)。它补充当前注册步骤的教学演练，不倒改上文原案例的缺输入状态，不宣称真实执行、组织批准或盲测通过。\n\n|当前步骤|新增虚构输入|转换与候选输出|变更或反例的预期|\n|---|---|---|---|\n'
 for row in payload['steps']:
  text+='| '+str(row['position'])+'：'+row['declared_step'].replace('|','\\|')+' | '+row['new_fictional_input'].replace('|','\\|')+' | '+row['transformation']+' → '+row['candidate_output']+' | '+row['adverse_variant_expected']+' |\n'
 text+='\n候选输出的来源身份、未知、计划和实际教学观察分别保存。数据行完整性与业务充分性是不同检查；实际生成的多布局、运行监控或人评审需另有执行证据，不能由本表文字授予。\n\n'
 body=body.replace('## 评审记录',text+'## 评审记录',1);case.write_text(body)
print('authored',len(rows),'supplements for',sum(len(v) for v in rows.values()),'steps')
