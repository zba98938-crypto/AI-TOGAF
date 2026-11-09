"""Independent visual and cell review of Architecture Content, source unchanged."""
from fundamental_review_common import C, DATA, sha
from bs4 import BeautifulSoup
import json, hashlib

FIGURES={
'b00049':'交付物含制品，制品分目录/矩阵/图并描述构建块；存储库保留可复用构建块及架构交付物。|左交付物与右存储库各三类制品之间双向箭头；左Artifacts到三类为无箭头分类线；交付物组与存储库交付物双向联系。|制品与构建块不同身份；无打印基数，不从叠层推计数。',
'b00052':'同一交付物中的多个制品可描述同一构建块，也可描述基线与目标不同状态。|Architecture Definition Document包含四制品；四条描述线指向Customer Services Representative，前两制品指Baseline Call Handling，后两指Target Call Handling。|Describes是描述关系而非执行依赖；例子人物和过程不是案例事实。',
'b00077':'内容框架按ADM组织上下文、定义、实现和变化管理。|顶部Preliminary/Architecture Requirements/Vision；定义中Business含Strategy/Operational，IS含Data/Application，与Technology并列；实现含Opportunities,Solutions,Migration及Implementation Governance；Change Management围外。|分区不是每阶段独立模型或项目顺序，Requirements不是Phase I。',
'b00080':'框架概览将业务、数据、应用、技术及变革上下文放入结构区域。|Business Capabilities与底部Capabilities分区不同；Data/Applications/Technology各有逻辑及物理组件；要求区域含Constraints/Assumptions/Gaps/Locations；下方Work Packages/Contracts。|业务能力与通用能力不可仅因同译名合并；图不规定实体基数。',
'b00106':'在2.3再次用内容框架分类元模型，不是新的图片内容。|与b00080共用同一资产指纹和实体分区，但本处用于元模型结构。|一资产两引用分别定位；不计为两张独立源图。',
'b00110':'一般实体关联所有对象；业务层连接动机、能力、价值流、角色、流程、信息、服务，底层连接数据/应用/技术逻辑与物理组件。|Work Package与Capability以Delivers/Is delivered by关联；Driver→Goal Creates，Goal→Objective Is made specific，Objective→Measure Is tracked against；三域逻辑物理以Realizes/Is realized by配对；表2-3保留154行关系原词。|密集交叉线部分无法仅凭图消除方向语义歧义，表内Used by反向成对及未定义类型另记，未杜撰基数。',
'b00134':'系统、架构、描述、利益相关者、关切、视点、视图、模型种类和模型保持不同身份。|System—Architecture exhibits两端1；Architecture—Description expresses两端1；Description聚合Views/VP端1..*；Viewpoint governs View两端1；ModelKind governs Model=1:1..*；Stakeholder has Concern两端1..*；View addresses Concern两端1..*。|小三角表示标签阅读方向，非关联导航箭头；空心菱形与关系基数按原图保存，不把其他图泛化成此基数。',
'b00148':'嵌套盒示例表达2017年The Open Group地点中开展的业务职能。|五地点列Burlington/Reading/San Francisco/Dynamic-Virtual/Home Offices；Off-site有IT Infrastructure；Outsourced有PR/IT Support/Desktop Support；内部盒按table3-1表示Functions performed in Locations。|不是汇报线、组织拥有权或当前2026地点事实。',
'b00213':'实际企业通过元模型描述进入存储库，标准制品集合组织视点，再选择具体利益相关者视图。|Reference Models与Application Platform有双向箭头；实际企业指向元模型；元模型指向Repository；Repository指向标准制品；标准制品指向Stakeholder Views；Queries/Analysis与Repository双向。|缩略元模型文字不作为新增端点证据；视点方法与具体视图分开，查询不是批准。',
'b00215':'各ADM区域中目录、矩阵、图示为候选制品分类。|Preliminary原则；A利益相关者及愿景图；B业务目录/矩阵/图；C数据/应用；D技术；E项目利益/因子/差距增量；F过渡和价值风险；Requirements需求目录。|制品不是全都必须；同名能力/价值流图在A和B可不同深度，应用Migration/Software Distribution命名与正文3.6.6.13/14一致。',
'b00523':'实施因子目录用Factor/Description/Deduction关联环境因素及迁移影响。|Change in Technology例称消息中心改邮件节约700人，推论培训/重分配并提高优先；Consolidation/Introduction后两行空白。|700仅源例；推论需当前业务证据，空白行不能推成无影响。',
'b00529':'整合差距、备选解决方案和依赖形成跨域规划输入。|No/Architecture/Gap/Potential Solutions/Dependencies五列；业务新订单流程drives applications(2)；应用行有COTS X或内部开发；信息行有客户库或数据集市。|候选尚未选择，不能把COTS X改成最终批准方案；空依赖不等于无依赖。',
'b00534':'以项目为行、过渡架构为列分配增量交付目标。|三列April2018/2019、2019/2020、2020/2021分别Preparation/Initial Operational Capability/Benefits；e-Services从培训流程到e-Licensing到e-Employment Benefits；IT信息逐步共用数据。|示例旧日期不改成本项目期限；空格和省略号保未知，非容量证明。',
'b00542':'TRM服务层面的状态演进表体现各SBB在过渡中的位置。|Information Exchange Services:System A(replace)→B-1(transition)→B-2(new)；Data Management:System D(retain)三列持续。|状态标签不是自动业务验收或风险关闭；系统身份不同不可只改显示名合并。',
'b00549':'项目气泡按价值纵轴、风险横轴和圈大小表示项目规模。|A/B左上，C/D右上，F/G左下，H右下，E跨中心；标题说明size of circle代表Project size。|没有坐标数值、刻度、权重或圈面积公式，不自动算ROI或排项目优先。',
'b00755':'A高层候选构建块，B/C/D逐步选模型、定义状态、差距、路线图并评审，E把差距关联工作包。|中间Requirements Management与A—H实际双向箭头；右侧Step1—9保留；A与E外部粗箭头指相应阶段，三域框指B/C/D。|中心双向箭头与其他ADM图的线样式分别取证；外环无箭头不臆造固定序列。',
'b00769':'Enterprise Continuum分类架构和方案资产，Enterprise Repositories提供实际资源。|两侧Repository↔Continuum的分类/资源方向分开；外部因素→上下文→Architecture；架构/方案之间Guides and Supports双向；Solutions→Deployed Solutions→Architecture Context回馈。|连续体是分类工具不是物理存储库，部署对象不是未实现SBB规格。',
'b00785':'架构连续体四类抽象由基础、共用系统、行业到组织特定。|四类相邻双向箭头，块形只示组合/扩展，无打印数量。|抽象度不是ADM阶段或战略/分段/能力粒度。​',
'b00815':'方案连续体四类从基础、共用、行业到组织特定，支持复用和适配。|四类相邻双向箭头，Common Systems底部独立块为图形组成。|不从块数推SBB多重性或真实产品清单。',
'b00848':'Architecture Continuum与Solutions Continuum对应类之间Guides & Supports双向。|上下各四类，相邻水平双向；四个垂直/斜向双箭头对应同类。|四类之间不是唯一一对一实体匹配，也非四阶段采购流程。',
'b00863':'存储库包含元模型、全景、参考/标准库、治理、要求、方案及能力记录，并与外部来源和委员会联系。|标准与全景有遵循/生成最佳实践方向；外部参考/标准指向内库；全景与标准下指治理；Governance↔Board可见性/升级；Board→Architecture Capability治理；要求↔方案虚线Business outcomes delivered。|箭头表达源关系不是自授权；要求—方案双向虚线不证明成果已实现，源表术语缺口保留。',
'b00876':'Reference Library复用架构连续体进行参考材料分类。|同b00785资产和四类双向箭头，此处上下文为reference materials。|复用图的分类法不表示每份参考资料已审阅或适用于当前组织。'}

TABLES={
'b00114':'36个元模型实体定义形成概念边界，包括通用Capability与Business Capability、Actor与Role、逻辑与物理组件。|逐行定义Actor可以是人/组织/系统；Assumption未充分验证；Constraint阻止方法；Contract功能/非功能交互；Requirement定量需要；Process可分解且操作化能力/服务；Work Package可项目/计划。|定义中的must与属性shall/should/may粒度不同；不能把未知假设当事实。',
'b00117':'175属性行包含通用ID/Description/Category/Source/Owner及按实体指定的标准、生命周期、需求验收和契约质量。|合并单元格按rowspan/colspan保留；Requirement含shall/should/may与Acceptance criteria；Contract含Throughput+period、Growth+period、恢复/隐私/安全；FTE为估计，不等于任职资格。|Role FTE行说明only basic attributes、Function/Process等date说明误写product，Service/Application Component/Technology Component泛型未在实体表独立定义；保留源问题，数值不补造。',
'b00120':'154个源/目标/关系名行逐行保留，区分语义方向及相反措辞。|Driver→Goal Creates；WorkPackage→Capability Delivers；Capability→WorkPackage Is delivered by；Physical与Logical Realizes/Is realized by；Process→Role Involves/Is performed by等可多关系。|Business Service Quality和Service不在36实体表，Used by在某些两端同词不构成规范互逆关系；不臆造类型别名或基数。',
'b00146':'视点说明受众、关切和嵌套盒建模语义。|Management Board/CEO；关切地点与职能；外框Locations、内框Business Functions，嵌套表示职能在地点执行。|无组织汇报或权限多重性，图为2017例子。',
'b00564':'21交付物按产生与消费ADM阶段形成信息依赖。|Communications Plan输出A、输入B—F；Contract输出G、输入G/H；Roadmap输出/输入B—F；Requirements Impact只在Requirements Management；SoAW可多阶段更新；原单元格全部保留。|不是首次产生后才永远可用的顺序表；与阶段具体inputs/outputs细节有差异须逐项核对，末尾逗号等源排版不默补。'}

def write():
    p=C/'fundamental/web-2025/volumes/05-architecture-content/document.json'
    d=json.loads(p.read_text()); r={'schema_version':'fundamental-visual-review/1','volume_id':p.parent.name,'source_document_sha256':sha(p),'figures':[],'tables':[],
       'source_issues':[{'block_id':'b00120','finding_zh':'关系目标Business Service Quality及Service未在实体表定义；保留未定义类型。'},
                        {'block_id':'b00120','finding_zh':'Application Service→Data Entity与Data Entity→Application Service两行均Used by，图中一端Uses，方向措辞不能自动互逆。'},
                        {'block_id':'b00117','finding_zh':'Role FTE属性却说only basic attributes，多处非Product实体标准日期说明沿用product。'}]}
    for kind,findings,target in [('img',FIGURES,'figures'),('table',TABLES,'tables')]:
        blocks=[b for b in d['blocks'] if b['kind']==kind]
        assert {b['id'].rsplit(':',1)[-1] for b in blocks}==set(findings)
        for b in blocks:
            local=b['id'].rsplit(':',1)[-1];a,labels,limits=findings[local].replace('\u200b','').split('|')
            chapter=b['section_path'][0]['title_en'].split('.')[0]
            refs={'1':['G249:s0026'],'2':['G233:s0014'],'3':['G186:s0029'],'4':['G188:s0073'],'5':['G248:s0015'],'6':['G248:s0015'],'7':['G186:s0045']}[chapter]
            row={'block_id':b['id'],'caption_en':b.get('alt',b.get('text_en','').split('\n')[0]),'semantic_review_zh':a,'labels_connections_zh':labels,'limits_zh':[limits],
                 'guide_refs':refs,'source_block_sha256':hashlib.sha256(b['html'].encode()).hexdigest(),'review_status':'source-visual-or-cells-reviewed'}
            if kind=='img':row.update(asset_path=str((p.parent/b['local_asset']).relative_to(C)),asset_sha256=sha(p.parent/b['local_asset']))
            else:
                soup=BeautifulSoup(b['html'],'html.parser')
                row['source_cells']=[[{'text_en':c.get_text(' ',strip=True),'rowspan':int(c.get('rowspan',1)),'colspan':int(c.get('colspan',1))} for c in tr.find_all(['td','th'],recursive=False)] for tr in soup.find_all('tr')]
            r[target].append(row)
    DATA.mkdir(exist_ok=True);dest=DATA/'05-visual-review.json';dest.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    lines=['# 架构内容卷：独立图表审查','', '逐一查看20个独立图片资产，在22处引用中分别按上下文审查；5张HTML表逐行核对并保存真实合并单元格。','']
    for kind in ['figures','tables']:
        for row in r[kind]:lines.extend(['## '+row['block_id'].rsplit(':',1)[-1]+' '+row['caption_en'],'',row['semantic_review_zh'],'',row['labels_connections_zh'],'','边界：'+'；'.join(row['limits_zh']),''])
    dest.with_suffix('.md').write_text('\n'.join(lines)+'\n')
    print({'figures':len(r['figures']),'tables':len(r['tables'])})

if __name__=='__main__':write()
