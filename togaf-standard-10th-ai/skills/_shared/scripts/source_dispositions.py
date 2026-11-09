"""Reviewed source roles. Binding indicates use, never visual/semantic equivalence.

The per-figure title/purpose is retained in the inventory. Rules below distinguish
project outputs, method explanations, reference taxonomies and illustrative images.
"""

PROFILE_BINDINGS = {
 'ea-service-adm-matrix':'G217/figC-1',
 'msa-federated-governance-diagram':'G21I/fig5-2',
 'msa-source-deployment-diagram':'G21I/fig9-1',
 'risk-security-traceability':'G152/fig5-2',
 'security-adm-concept-map':'G152/fig1-1',
 'security-cross-domain':'G152/fig4-1 G184/fig9-5',
 'business-attribute-profile-default':'G152/fig5-1',
 'value-stream-definition':'G178/fig1-1 G178/fig4-1 G178/fig4-2 G233/fig5-1',
 'value-stream-enabling-capabilities':'G178/fig4-3 G211/fig5-3 G233/fig6-2',
 'value-stream-capability-heatmap':'G178/fig4-4',
 'porter-value-chain':'G178/figA-1 G233/figB-1',
 'ea-value-map-default':'G184/fig11-1 G184/fig11-2',
 'architecture-repository-structure':'G186/fig5-1',
 'architecture-landscape-projection':'G186/fig3-1 G186/fig3-2',
 'architecture-project-schedule-default':'G184/fig10-3 G186/fig5-5 G186/fig5-7 G186/fig5-8 G186/fig5-9 G186/fig5-10',
 'agile-pattern-selection':'G210/fig3-1',
 'agile-ea-development':'G210/fig3-2',
 'agile-solution-collaboration':'G210/fig3-3',
 'agile-cross-development':'G210/fig3-4',
 'agile-cross-functional':'G210/fig3-5',
 'architecture-project-wbs-default':'G188/ex3-22',
 'business-risk-register-default':'G188/img-p54',
 'business-model-canvas':'G18A/fig2-4 G18A/figA-1 G20F/fig5-3 G233/fig4-2',
 'business-model-baseline-target':'G18A/fig7-1 G18A/fig7-2',
 'information-concept-network':'G190/fig2-1 G190/fig5-1 G190/figA-1 G190/figA-3 G190/figA-5 G233/fig4-4',
 'information-capability-use-modify':'G190/fig4-1 G190/figA-2',
 'information-aggregation-generalization':'G190/figA-4',
 'organization-work-network':'G206/fig2-1 G206/fig3-2 G206/fig7-1',
 'organization-capability-overlay':'G206/fig7-2',
 'architecture-skill-matrix-default':'G198/fig6-2',
 'capability-classification':'G211/fig3-2 G233/fig6-1',
 'capability-decomposition':'G211/fig3-3',
 'capability-gap-heatmap':'G211/fig5-1',
 'dtra-adoption-quadrant':'G212/fig5-2',
 'dtra-factor-consequence':'G212/fig5-3',
 'dtra-factor-progression':'G212/fig5-4',
 'digital-readiness-questionnaire-default':'G212/figA-1',
 'ea-service-catalog-default':'G217/fig4-2 G217/fig4-3',
 'ea-service-adm-evidence-map':'G217/figC-1',
 'msa-federated-governance-process':'G21I/fig5-2',
 'soa-layered-reference':'G21I/fig5-3',
 'msa-source-deployment-execution':'G21I/fig9-1',
 'customer-mdm-model-default':'G21B/fig5-1 G21B/fig5-2',
 'mdm-consolidation-collaboration-central':'G21B/fig6-1 G21B/fig6-3 G21B/fig6-4 G21B/fig6-5',
 'mdm-exchange-pattern-default':'G21B/fig6-2',
 'digital-business-reference-tailoring-default':'G21H/fig3-1 G21H/fig4-1',
 'capability-instance-composition':'G233/fig6-3 G233/figC-1',
 'capability-change-overlay':'G233/fig7-1 G233/fig7-2',
 'metadata-business-function-map':'G234/fig3-1 G234/fig5-1',
 'metadata-category-coverage':'G234/fig4-5',
 'metadata-three-part-solution':'G234/fig4-4',
 'metadata-central-hybrid-unified':'G234/fig4-6 G234/fig4-7 G234/fig4-8',
 'metadata-manual-push-pull':'G234/fig4-9',
 'metadata-inference-structure':'G234/fig4-10',
 'bi-baseline-transition-target':'G238/fig3-1 G238/fig3-2 G238/fig3-3 G238/fig3-4',
 'annual-environmental-accounting':'G242/fig3-10',
 'sustainability-architecture-canvas':'G242/fig3-14',
 'sustainability-causal-loop':'G242/fig1-2',
 'sustainability-culture-quadrant':'G242/fig3-2',
 'environmental-decision-log-default':'G242/fig3-13',
 'transition-building-block-trace':'G248/fig2-2 G248/fig2-3',
 'building-block-content-model':'G248/fig3-1',
 'ea-skill-role-proficiency':'G249/table5-2',
 'architecture-role-collaboration':'G249/fig4-1',
}

METHOD_BINDINGS = {
 'reference-model-tailoring':'G248/fig2-1',
 'business-risk-assessment':'G152/fig3-1 G152/fig3-2 G152/fig3-3 G184/fig6-3',
 'scenario-elicitation':'G176/fig3-1 G176/fig3-2 G176/fig5-1 G176/fig6-1',
 'value-stream-definition-method':'G178/fig1-2',
 'architecture-role-skill-assessment':'G249/table5-1 G249/table5-2',
 'architecture-project-scheduling':'G188/fig1-1 G188/fig2-1 G188/fig2-2 G188/fig3-1 G188/fig3-2 G188/fig3-3 G188/fig4-1 G188/fig4-2 G188/fig5-1',
 'dtra-readiness-method':'G212/fig3-1 G212/fig4-1 G212/fig5-1 G212/fig6-1',
 'mdm-identity-analysis':'G21B/fig1-1 G21B/fig1-2 G21B/fig3-1 G21B/fig4-1 G21B/fig4-2 G21B/fig5-3 G21B/fig5-4 G21B/tab4-6',
 'metadata-requirement-method':'G234/fig4-1 G234/fig4-2 G234/fig5-2',
 'metadata-integration-tradeoff':'G234/fig4-3',
 'bi-transition-method':'G238/fig2-1 G238/fig4-1 G238/fig4-2 G238/fig4-3',
 'microservice-boundary-method':'G21I/fig5-1 G21I/fig5-2 G21I/fig5-3 G21I/fig6-1 G21I/fig6-2 G21I/fig9-1 G21I/fig10-1',
 'environment-lifecycle-accounting':'G242/fig3-4 G242/fig3-9 G242/fig3-11 G242/fig3-12',
 'sustainability-option-review':'G242/fig3-1 G242/fig3-3 G242/fig3-5 G242/fig3-6 G242/fig3-7 G242/fig3-8 G242/fig3-15 G242/fig3-16 G242/fig5-1',
}

# Reference structures need local mappings, not copies of the illustrated facts.
# G186/G210 are per-figure; a whole-guide schedule fallback is forbidden.
REFERENCE_GROUPS = {
 'G21D':('government-reference-tailoring-default','政府参考模型的结构及部门L1–L3分类；同一裁剪能力的不同内容样本，不计作多种正式制品。'),
 'G184':('ea-value-map-default','EA能力建设、团队归属、治理及运营的说明模型；用于裁剪组织与方法，不把示意组织或示例分类当项目事实。'),
 'G20F':('transition-architecture-model-default','敏捷交付中全景层级、过渡、ADM与待办列表的协作说明；按目的裁剪，不把ADM循环本身当项目架构图。'),
 'G217':('ea-service-catalog-default','架构服务与DPBoK语境、原则、正式程度及ADM的参考映射；本地服务定义仍需责任和验收证据。图C-1另走证据映射入口，表/方法不等于原图视觉验收。'),
}

# Leftover figures that must not silently inherit a guide-wide viewpoint.
FIGURE_DISPOSITIONS = {
 'G186/fig3-3':('method-or-reference-model-evidence',[],[],'四类 EA 目的说明，不是项目进度图。'),
 'G186/fig4-1':('method-or-reference-model-evidence',[],[],'业务周期与四种架构目的对应，不是排期。'),
 'G186/fig4-2':('reference-or-notation-evidence',[],[],'半座桥示意隐喻，不是架构制品或进度图。'),
 'G186/fig5-2':('explicit-source-review-gap',[],[],'EA 存储库示例实例，不是 fig5-1 结构视点，不借用进度图。'),
 'G186/fig5-3':('explicit-source-review-gap',[],[],'多个候选架构比较，尚无专用视点，不借用进度图。'),
 'G186/fig5-4':('reference-or-notation-evidence',[],[],'建模工具中的参考材料截图，不是进度图。'),
 'G186/fig5-6':('method-or-reference-model-evidence',[],[],'棘手问题解决方法说明，不是任务排期。'),
 'G186/fig6-1':('method-or-reference-model-evidence',[],['architecture-project-scheduling'],'以 ADM 支持四种目的的走查重点，不是甘特排期。'),
 'G186/fig8-1':('explicit-source-review-gap',[],[],'能力与项目连续谱，不是甘特排期。'),
 'G186/fig13-1':('explicit-source-review-gap',[],[],'用存储库管理路线图识别变更，不是进度图。'),
 'G186/fig13-2':('explicit-source-review-gap',[],[],'架构影响分析，不是进度图。'),
 'G186/fig14-1':('method-or-reference-model-evidence',[],[],'预算窗口与按目的划分的架构，不得借用进度图。'),
 'G186/tabB-1':('explicit-source-review-gap',[],[],'利益相关者职责矩阵；表格/方法入口不等于原图视觉验收。'),
}

FIGURE_REASONS = {
 'G217/figC-1':'EA 服务与 ADM 证据映射表入口；表格/方法不等于原图视觉验收。',
 'G21I/fig5-2':'联邦治理过程视点入口；过程表不等于原图视觉验收。',
 'G21I/fig5-3':'SOA 分层参考视点；参考示例按用途裁剪，不要求项目机械复制。',
 'G21I/fig9-1':'源/部署/执行追溯入口；表或派生部署图不等于原图视觉验收。',
 'G210/fig3-1':'敏捷模式选择，不得用甘特代表协作。',
 'G210/fig3-2':'企业架构开发冲刺/DORP 规范，不得用甘特代表敏捷协作。',
 'G210/fig3-3':'解决方案协作冲刺规范，不得用甘特代表敏捷协作。',
 'G210/fig3-4':'跨开发协作规范，不得用甘特代表敏捷协作。',
 'G210/fig3-5':'跨职能冲刺规范，不得用甘特代表敏捷协作。',
}

# These distinct source representations must be surfaced as gaps until a named
# operational profile is implemented; the inventory never silently calls them covered.
EXTRA_VIEWS = {
 'G178/figA-2':('value-network','价值网络需表达参与者间价值交换，不能用价值流或价值链代替。'),
 'G178/figA-3':('lean-value-stream','精益价值流需保留流量、等待、处理及节拍语义，不能用客户价值阶段图代替。'),
 'G18A/fig2-2':('four-box-business-model','四框业务模型需保留客户价值主张、利润公式、关键资源与关键流程。'),
 'G18A/fig2-3':('business-model-cube','业务模型立方体按来源维度分析业务模型，不用九块画布替代。'),
 'G184/fig4-1':('operating-model','运营模式用流程标准化与业务流程集成两轴，不能套用ABCD采用定位。'),
 'G184/fig4-3':('stakeholder-influence-matrix','来源PMI矩阵纵轴为Influence、横轴为Impact；不能替换成兴趣轴；需保留四类介入策略。'),
 'G233/fig4-3':('balanced-scorecard','四视角各有目标和可度量成果，成果实现目标；原图没有跨视角因果边，不能自行补成因果链。'),
}

ORGANIZATION_REFERENCES={'G184/fig5-1','G184/fig9-1','G188/fig3-2','G206/fig3-1','G211/fig3-1','G233/fig4-1'}

def invert(mapping):
    out={}
    for key,figures in mapping.items():
        for fig in figures.split():out.setdefault(fig,[]).append(key)
    return out


PROFILE_BINDINGS.update({
 'ea-service-adm-reference-matrix':'G217/figC-1',
 'ea-service-adm-reference-table':'G217/figC-1',
 'repository-state-view-tree':'G186/fig5-2',
 'repository-parallel-candidates':'G186/fig5-3',
 'repository-target-baseline-comparison':'G186/fig13-1',
 'repository-baseline-target-comparison':'G186/fig13-2',
 'capability-project-continuum':'G186/fig8-1',
 'portfolio-stakeholder-concern-matrix':'G186/tabB-1'})

P=invert(PROFILE_BINDINGS);M=invert(METHOD_BINDINGS)

def disposition(fid, tags, available_profiles, available_methods):
    profiles=[p for p in P.get(fid,[]) if p in available_profiles]
    methods=[m for m in M.get(fid,[]) if m in available_methods]
    if fid in EXTRA_VIEWS:
        suffix,reason=EXTRA_VIEWS[fid]
        candidates=[p for p in available_profiles if p==suffix or p==suffix+'-default']
        return {'disposition':'source-derived-view-profile' if candidates else 'explicit-view-capability-gap',
                'profile_ids':candidates,'method_ids':methods,'reason':reason,
                'implementation_gap':None if candidates else suffix}
    if profiles:
        return {'disposition':'source-derived-view-profile','profile_ids':profiles,'method_ids':methods,
                'reason':FIGURE_REASONS.get(fid,'已指定可执行视图入口；入口保留本图关键建模任务，来源结构与项目字段的逐项等价仍须单独验收。')}
    if methods:
        return {'disposition':'method-or-reference-model-evidence','profile_ids':[],'method_ids':methods,
                'reason':FIGURE_REASONS.get(fid,'本图解释分析步骤、模型或参考内容；登记到对应方法，不能仅据图数推导制品数。')}
    if fid in ORGANIZATION_REFERENCES:
        return {'disposition':'reference-taxonomy-or-example','profile_ids':['organization-work-network'], 'method_ids':[],
                'reason':'组织层级或项目团队示例，支持组织建模；示例汇报关系与业务协作关系须区别，本地组织需重新取证。'}
    if fid in FIGURE_DISPOSITIONS:
        kind,profile_ids,method_ids,reason=FIGURE_DISPOSITIONS[fid]
        keep_profiles=[p for p in profile_ids if p in available_profiles]
        keep_methods=[m for m in method_ids if m in available_methods]
        return {'disposition':kind,'profile_ids':keep_profiles,'method_ids':keep_methods,'reason':reason,
                'implementation_gap':None if keep_profiles or kind!='explicit-source-review-gap' else fid}
    if any(t in tags for t in ['photo','screenshot','legend']):
        return {'disposition':'reference-or-notation-evidence','profile_ids':[],'method_ids':[],
                'reason':'照片、工具界面或记法图例为说明证据；不要求生成相同工具界面，也不据此增加架构制品种类。'}
    guide=fid.split('/')[0]
    if guide in REFERENCE_GROUPS:
        profile,reason=REFERENCE_GROUPS[guide]
        return {'disposition':'reference-taxonomy-or-method-evidence','profile_ids':[profile] if profile in available_profiles else [],
                'method_ids':[],'reason':reason}
    if guide=='G18A':
        return {'disposition':'method-or-reference-model-evidence','profile_ids':['business-model-canvas'],'method_ids':[],
                'reason':'业务模型抽象与战略关系的解释模型；用于明确画布边界和映射，而非额外九块画布。'}
    if guide=='G21H':
        return {'disposition':'reference-taxonomy-or-method-evidence','profile_ids':['digital-business-reference-tailoring-default'],'method_ids':['reference-model-tailoring'],
                'reason':'数字业务/O-AA与TOGAF内容、全景映射的参考解释；DBRM四域十要素和TOGAF四架构域不可混同。'}
    if guide=='G21I' and fid.endswith('fig4-1'):
        return {'disposition':'method-or-reference-model-evidence','profile_ids':[],'method_ids':['microservice-boundary-method'],
                'reason':'重复的TOGAF ADM背景方法图；ADM循环不等同微服务部署架构。'}
    if guide=='G233' and fid.endswith('fig3-1'):
        return {'disposition':'reference-or-notation-evidence','profile_ids':['capability-instance-composition'],'method_ids':['capability-instance-gap-method'],
                'reason':'ArchiMate能力及关系记法参考；用来检验能力类型、实例与实现的不同关系，不把记法元素当项目实体。'}
    if guide=='G211' and fid.endswith('fig5-2'):
        return {'disposition':'source-derived-view-profile','profile_ids':['organization-capability-overlay'],'method_ids':['capability-decomposition-method'],
                'reason':'能力与组织的交叉映射；能力定义独立于组织归属，避免把汇报层级当能力分解。'}
    if guide=='G242' and fid.endswith('fig1-1'):
        return {'disposition':'contextual-evidence-only','profile_ids':[],'method_ids':[],
                'reason':'全球数据量趋势为背景论据，未提供可复用项目架构制品定义；不将历史趋势数值灌入本地事实。'}
    return {'disposition':'explicit-source-review-gap','profile_ids':[],'method_ids':[],
            'reason':'没有登记合适入口；保留明确来源审查缺口，不借用同指南方法宣称已覆盖。'}
