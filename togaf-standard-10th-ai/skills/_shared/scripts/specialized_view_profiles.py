"""Build specialized source-topology profiles. Registration is not source verification."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def entity(identity, typ, name, **attrs):
    return {'id': identity, 'type': typ, 'name': name, 'attributes': attrs,
            'evidence': ['example-source'], 'certainty': 'assumed'}


def edge(identity, source, target, typ, label, **attrs):
    attrs.setdefault('meaning', label)
    return {'id': identity, 'source': source, 'target': target, 'type': typ,
            'label': label, 'attributes': attrs, 'evidence': ['example-source'],
            'certainty': 'assumed'}


def profile(pid, artifact, name, owner, refs, kind, entities, relations, extensions, checks):
    example = {
        'notice': '来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。',
        'sources': [{'id': 'example-source', 'kind': 'example',
                     'description': '专用拓扑验收示例：' + ', '.join(refs) + '；来源图解释与候选企业场景分开。'}],
        'entities': entities, 'relationships': relations, 'extensions': extensions,
        'view': {
            'id': 'v-' + pid, 'artifact_id': artifact, 'profile_id': pid,
            'title': name + '／来源结构专用示例',
            'entity_ids': [e['id'] for e in entities],
            'relationship_ids': [r['id'] for r in relations],
            'analysis': '明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。',
            'legend': '虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。'
        }
    }
    from profile_examples import declare_relationship_extensions
    declare_relationship_extensions(example, REL_DEFS)
    return {
        'id': pid, 'artifact_id': artifact, 'name': name, 'name_zh': name,
        'owner': owner, 'renderer': 'deployment', 'output_kind': 'diagram',
        'source_refs': refs, 'version': '2.3',
        'required_attributes': {'*': ['definition']},
        'required_relationship_attributes': {'*': ['meaning']},
        'entity_types': sorted({e['type'] for e in entities}),
        'relationship_types': sorted({r['type'] for r in relations}),
        'checks': checks,
        'decision': '以专用来源结构支持建模任务；来源图与项目字段的逐项等价仍须单独验收。',
        'definition_status': 'source-derived-view-with-project-construction-rules',
        'template': {
            'id': pid, 'version': '2.3', 'source_verified': False,
            'source_figure': refs[0], 'source_topology': kind,
            'separate_detail_ledger': True,
            'review_status': 'source-topology-registered-awaiting-independent-review',
            'layout_notes': checks[0]
        },
        'example': example
    }


def work_product(pid, name, owner, refs, example, entity_types, relationship_types):
    from registry_consistency import DELIVERY_LINKS
    return {
        'related_deliverables': DELIVERY_LINKS.get(pid, []),
        'counterexample': {'input': '删除所选对象必需的definition属性，保持ID与视图选择。', 'expected': 'missing-profile-attribute', 'why': '缺少对象含义，不能声称结构完整。'},
        'modification_example': {'change': '修改同ID对象的definition，保持角色及类型不变。', 'expected': '双布局输出表达新定义并可定位到对象；旧版不作为当前事实。'},
        'id': pid, 'artifact_id': pid, 'name': name, 'name_zh': name, 'name_en': name,
        'owner': owner, 'kind': 'diagram', 'renderer': 'deployment',
        'source_refs': refs, 'example': example,
        'entity_types': entity_types, 'relationship_types': relationship_types,
        'required_attributes': {'*': ['definition']},
        'attribute_semantics': {
            'definition': {
                'meaning': '对象在本视点中的可检查定义',
                'value_rule': '使用可追溯描述；未确定内容标为假设或缺口。',
                'definition_origin': 'project-operational-convention-guided-by-cited-source'
            }
        },
        'fields': ['name', 'definition', 'evidence', 'certainty'],
        'required_inputs': ['视点问题与范围', '带来源的对象、关系及定义'],
        'optional_inputs': ['企业裁剪及例外说明'],
        'output': ['可编辑SVG/PNG概览', '同ID的可读伴随明细与coverage表示位置'],
        'analysis_steps': ['确认视点问题、范围和来源，区分参考结构与企业事实。',
                           '用显式对象和类型化关系建模，核查边界、方向及完整性。',
                           '生成视图与明细，记录取舍、缺口并复核来源及业务适用性。'],
        'decision': '依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。',
        'semantic_checks': ['关系端点及类型有效', '专用拓扑检查通过', '必要字段可追溯到实际输出'],
        'check_specs': [{'id':'topology-'+str(i),'text':text,'mode':'review','source':'semantic_checks'} for i,text in enumerate(['关系端点及类型有效','专用拓扑检查通过','必要字段可追溯到实际输出'])],
        'misreadings': ['登记来源或成功生成不表示来源等价', '参考示例的固定结构不直接强制所有企业采用'],
        'definition_status': 'source-derived-view-with-project-construction-rules',
        'missing_input_policy': '关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。'
    }


def architecture_repository():
    es = [
        entity('ent-enterprise', 'repository_container', '企业存储库',
               definition='比架构库更宽的企业级存储范围', container_role='enterprise'),
        entity('ent-archrepo', 'repository_container', '架构存储库',
               definition='含七分区与架构能力，不等于全景本身', container_role='architecture'),
        entity('part-metamodel', 'repository_partition', '架构元模型',
               definition='规定全景制品如何按框架结构化', partition_role='metamodel'),
        entity('part-landscape', 'repository_partition', '架构全景',
               definition='战略/分段/能力三层；只是分区之一', partition_role='landscape'),
        entity('part-solutions', 'repository_partition', '解决方案全景',
               definition='解决方案构建块容器', partition_role='solutions'),
        entity('part-reference', 'repository_partition', '参考库',
               definition='组织参考材料', partition_role='reference'),
        entity('part-standards', 'repository_partition', '标准库',
               definition='业务/数据/应用/技术标准', partition_role='standards'),
        entity('part-requirements', 'repository_partition', '架构需求库',
               definition='驱动与需求材料', partition_role='requirements'),
        entity('part-governance', 'repository_partition', '治理库',
               definition='决策日志、合规与能力评估', partition_role='governance'),
        entity('part-capability', 'repository_partition', '架构能力',
               definition='技能、方法与能力资产', partition_role='capability'),
        entity('ext-refs', 'repository_external', '外部参考模型',
               definition='位于架构库外侧，被采纳而非内含', external_role='reference-model'),
        entity('ext-std', 'repository_external', '外部标准',
               definition='位于架构库外侧', external_role='standard'),
        entity('ext-board', 'repository_external', '架构委员会',
               definition='治理可见性与上报，并引导架构能力', external_role='board'),
        entity('asset-strategic', 'repository_asset', '战略架构入口',
               definition='全景中的战略层入口，不是整个库', asset_kind='landscape-entry')
    ]
    rs = [
        edge('c-ent-arch', 'ent-enterprise', 'ent-archrepo', 'project:contains', '企业库包含架构库'),
        edge('c-arch-meta', 'ent-archrepo', 'part-metamodel', 'project:contains', '架构库包含元模型'),
        edge('c-arch-land', 'ent-archrepo', 'part-landscape', 'project:contains', '架构库包含全景分区'),
        edge('c-arch-sol', 'ent-archrepo', 'part-solutions', 'project:contains', '架构库包含解决方案全景'),
        edge('c-arch-ref', 'ent-archrepo', 'part-reference', 'project:contains', '架构库包含参考库'),
        edge('c-arch-std', 'ent-archrepo', 'part-standards', 'project:contains', '架构库包含标准库'),
        edge('c-arch-req', 'ent-archrepo', 'part-requirements', 'project:contains', '架构库包含需求库'),
        edge('c-arch-gov', 'ent-archrepo', 'part-governance', 'project:contains', '架构库包含治理库'),
        edge('c-arch-cap', 'ent-archrepo', 'part-capability', 'project:contains', '架构库包含架构能力'),
        edge('c-land-asset', 'part-landscape', 'asset-strategic', 'project:contains', '全景包含战略入口'),
        edge('r-struct', 'part-metamodel', 'part-landscape', 'project:structured_by', '全景制品按框架结构化'),
        edge('r-enable', 'part-landscape', 'part-solutions', 'project:enables', '全景使能解决方案全景'),
        edge('r-gov', 'part-governance', 'part-landscape', 'project:governs', '治理库治理全景'),
        edge('r-adopt-std', 'ext-std', 'part-standards', 'project:adopts', '外部标准被采纳'),
        edge('r-adopt', 'ext-refs', 'part-reference', 'project:adopts', '外部参考被采纳'),
        edge('r-vis', 'ext-board', 'part-governance', 'project:visibility_escalation', '可见性与上报'),
        edge('r-steer', 'ext-board', 'part-capability', 'project:steers', '引导并管理能力'),
        edge('r-out', 'part-solutions', 'part-requirements', 'project:delivers_outcomes', '业务成果交付')
    ]
    ext = {'relationship_types': {k: REL_DEFS[k] for k in (
        'project:contains', 'project:governs', 'project:enables', 'project:adopts',
        'project:visibility_escalation', 'project:steers', 'project:delivers_outcomes',
        'project:structured_by')}}
    return profile('architecture-repository-structure', 'architecture-repository-structure',
                   '架构存储库结构', 'togaf-ea-capability', ['G186/fig5-1'],
                   'architecture-repository', es, rs, ext,
                   ['企业库⊃架构库⊃七分区+能力；外部对象在外侧', '全景不是整个存储库'])


def architecture_landscape():
    es = [
        entity('land-volume', 'landscape_projection', 'EA 全景',
               definition='全部潜在架构内容的体积，不是某一个架构或存储库',
               recency='正文讨论的第四特征，本图不画轴'),
        entity('axis-breadth', 'landscape_dimension', '广度（主题）',
               definition='按领域、组织或举措界定的覆盖范围', axis='breadth'),
        entity('axis-abs', 'landscape_dimension', '详细程度',
               definition='展开到回答当前问题所需即可', axis='abstraction'),
        entity('axis-time', 'landscape_dimension', '时间（规划期）',
               definition='从当前到目标架构的时间点', axis='time'),
        entity('slice-project', 'landscape_slice', '当前架构项目切片',
               definition='全景内的项目范围，不是第二个存储库',
               breadth='履约域', abstraction='逻辑', time='本预算年'),
        entity('obj-capability', 'capability', '预约改约能力',
               definition='同一对象可按三轴投影回模型',
               breadth='履约域', abstraction='逻辑', time='本预算年')
    ]
    rs = [
        edge('p-b', 'land-volume', 'axis-breadth', 'project:projects_to', '沿广度投影'),
        edge('p-a', 'land-volume', 'axis-abs', 'project:projects_to', '沿抽象投影'),
        edge('p-t', 'land-volume', 'axis-time', 'project:projects_to', '沿时间投影'),
        edge('p-s', 'land-volume', 'slice-project', 'project:contains', '项目切片位于全景内'),
        edge('p-o', 'obj-capability', 'slice-project', 'project:projects_to', '对象投影到本项目切片')
    ]
    return profile('architecture-landscape-projection', 'architecture-landscape-projection',
                   '架构全景投影', 'togaf-ea-capability', ['G186/fig3-1', 'G186/fig3-2'],
                   'architecture-landscape', es, rs, {},
                   ['三轴投影；时效性不作第四轴', '项目切片在全景内，不是第二个存储库'])


CONCEPTS = [
    ('P', 'business_drivers', '业务驱动 / 目标', False),
    ('P', 'security_principles', '安全原则', False),
    ('P', 'risk_appetite', '风险偏好', True),
    ('P', 'key_risk_areas', '关键风险领域 / 业务影响', True),
    ('A', 'security_resource_plan', '安全资源计划', False),
    ('B', 'security_policy_architecture', '安全政策架构', True),
    ('B', 'security_domain_model', '安全域模型', False),
    ('B', 'trust_framework', '信任框架', True),
    ('B', 'risk_assessment', '风险评估', True),
    ('B', 'business_risk_model', '业务风险模型 / 风险登记', True),
    ('B', 'law_register', '适用法律法规登记', True),
    ('B', 'control_framework_register', '适用控制框架登记', True),
    ('C', 'security_services_catalog', '安全服务目录', True),
    ('C', 'security_classification', '安全分类', True),
    ('C', 'data_quality', '数据质量', True),
    ('D', 'security_standards', '安全标准', False),
    ('E', 'business_attribute_profile', '业务属性概况', True),
    ('E', 'control_objectives', '控制目标 / 安全目标', True),
    ('F', 'risk_mitigation_plan', '风险缓解计划', False),
    ('G', 'security_audit', '安全审计', True),
    ('G', 'security_training', '安全培训与意识', True),
]


def security_adm():
    phases = [('P', 'Preliminary'), ('A', 'A. Architecture Vision'),
              ('B', 'B. Business Architecture'), ('C', 'C. Information Systems Architectures'),
              ('D', 'D. Technology Architecture'), ('E', 'E. Opportunities and Solutions'),
              ('F', 'F. Migration Planning'), ('G', 'G. Implementation Governance'),
              ('H', 'H. Architecture Change Management'), ('RM', 'Requirements Management')]
    es = [entity('phase-' + code, 'adm_phase', label,
                 definition='ADM 阶段，不是自动批准点', phase_code=code)
          for code, label in phases]
    es += [entity('c-' + key, 'security_risk_concept', name,
                  definition='来源概念：' + name, concept_key=key, phase_code=phase,
                  ism_erm_addition=added)
           for phase, key, name, added in CONCEPTS]
    es += [
        entity('ism', 'ism_process', '信息安全管理', definition='持续循环，不是一次活动'),
        entity('erm', 'erm_process', '企业风险管理', definition='持续循环，不是一次活动'),
        entity('svc-iam', 'security_service', '身份与访问管理', definition='服务目录展开项'),
        entity('svc-mon', 'security_service', '安全监控', definition='服务目录展开项')
    ]
    rs = [edge('assoc-' + key, 'phase-' + phase, 'c-' + key, 'project:associates',
               '阶段关联概念组', notation='unarrowed')
          for phase, key, name, added in CONCEPTS]
    rs += [
        edge('ism-loop', 'ism', 'ism', 'project:continues', 'ISM 持续循环'),
        edge('erm-loop', 'erm', 'erm', 'project:continues', 'ERM 持续循环'),
        edge('cat-iam', 'c-security_services_catalog', 'svc-iam', 'project:catalog_expands', '目录展开'),
        edge('cat-mon', 'c-security_services_catalog', 'svc-mon', 'project:catalog_expands', '目录展开')
    ]
    # Preliminary and A share the first concept group. RM also associates
    # with business attributes / control objectives; E/F curve ambiguity remains explicit.
    for phase, key, name, added in CONCEPTS[:5]:
        other = 'A' if phase == 'P' else 'P'
        rs.append(edge('assoc-shared-' + key, 'phase-' + other, 'c-' + key,
                       'project:associates', 'P/A 共享概念组', notation='unarrowed'))
    for key in ('business_attribute_profile', 'control_objectives'):
        rs.append(edge('assoc-rm-' + key, 'phase-RM', 'c-' + key,
                       'project:associates', '持续需求管理关联', notation='unarrowed'))
    return profile('security-adm-concept-map', 'security-blueprint',
                   '安全与ADM概念整合', 'togaf-security-risk', ['G152/fig1-1'],
                   'security-adm-map', es, rs, {},
                   ['阶段—概念组无方向关联；H 无概念组', '下划线概念为 ISM/ERM 新增'])


def metadata_inference():
    es = [
        entity('zone-meta', 'metadata_zone', 'METADATA', definition='元数据管理分区', zone='METADATA'),
        entity('zone-data', 'metadata_zone', 'DATA', definition='数据与剖析分区', zone='DATA'),
        entity('mgmt', 'metadata_management', '元数据管理',
               definition='接收上行技术元数据', access_condition='仅已批准模式', cost='目录维护工时',
               zone='METADATA'),
        entity('prof', 'data_profiling', '数据剖析',
               definition='读取来源并上推结构', access_condition='抽样须独立批准', cost='百万文件扫描成本',
               zone='DATA'),
        entity('src-s', 'inference_source', '结构化来源',
               definition='模式可从字典采集', data_structure='structured',
               schema_access='可读字段模式', content_access='无需读取实际值',
               governance_claim='schema-available', access_condition='字典只读', cost='低'),
        entity('src-h', 'inference_source', '半结构化来源',
               definition='有结构但不保证稳定', data_structure='semi-structured',
               schema_access='逐文件结构', content_access='仅抽样',
               governance_claim='partial', access_condition='抽样批准', cost='中'),
        entity('src-u', 'inference_source', '非结构化来源',
               definition='须先抽取最低结构', data_structure='unstructured',
               schema_access='无稳定字段模式', content_access='内容扫描需隐私评估',
               governance_claim='ungoverned-until-scanned', access_condition='内容扫描批准', cost='高')
    ]
    rs = [
        edge('read-s', 'prof', 'src-s', 'project:profiling_reads', '剖析读取结构化'),
        edge('read-h', 'prof', 'src-h', 'project:profiling_reads', '剖析读取半结构化'),
        edge('read-u', 'prof', 'src-u', 'project:profiling_reads', '剖析读取非结构化'),
        edge('lift-uh', 'src-u', 'src-h', 'project:structure_lifts', '非结构化上推半结构'),
        edge('lift-hs', 'src-h', 'src-s', 'project:structure_lifts', '半结构上推结构'),
        edge('up-p', 'prof', 'mgmt', 'project:metadata_uplinks', '剖析结果上行'),
        edge('up-s', 'src-s', 'mgmt', 'project:metadata_uplinks', '结构化技术元数据上行')
    ]
    return profile('metadata-inference-structure', 'metadata-inference-design',
                   '技术元数据推断架构', 'togaf-information-data', ['G234/fig4-10'],
                   'metadata-inference', es, rs, {},
                   ['剖析与结构化来源可跨 DATA→METADATA', '访问条件与成本必须带来源'])


def soa_layered():
    layers = [
        ('consumer-interface', '消费者接口'),
        ('business-process', '业务流程'),
        ('services', '服务'),
        ('service-component', '服务组件'),
        ('operational-systems', '运营系统')
    ]
    concerns = [('integration', '集成'), ('qos', '服务质量'),
                ('information', '信息'), ('governance', '治理')]
    es = [entity('layer-' + key, 'soa_layer', name, definition='SOA 参考层：' + name, layer=key)
          for key, name in layers]
    es += [entity('concern-' + key, 'soa_concern', name, definition='跨层关注：' + name, concern=key)
           for key, name in concerns]
    rs = [edge('map-' + layers[i][0], 'layer-' + layers[i][0], 'layer-' + layers[i + 1][0],
               'project:maps_to', '层间映射')
          for i in range(len(layers) - 1)]
    rs += [edge('x-' + ck + '-' + lk, 'concern-' + ck, 'layer-' + lk, 'project:cross_cuts_soa',
                '横切 ' + cn)
           for ck, cn in concerns for lk, ln in layers]
    return profile('soa-layered-reference', 'soa-layered-reference',
                   'SOA 分层参考', 'togaf-technology-architecture', ['G21I/fig5-3'],
                   'soa-layered', es, rs, {},
                   ['五层加四种跨层关注点', '参考层按用途裁剪，不要求机械复制'])


ENTITY_DEFS = {
    'repository_container': {'meaning': '存储库容器：企业库或架构库，不是全景本身。', 'level': 'guide-extension'},
    'repository_partition': {'meaning': '架构库分区或能力，全景只是其中之一。', 'level': 'guide-extension'},
    'repository_external': {'meaning': '架构库外侧的参考、标准或委员会。', 'level': 'guide-extension'},
    'repository_asset': {'meaning': '分区内的资产入口。', 'level': 'guide-extension'},
    'landscape_projection': {'meaning': 'EA 全景体积，可按轴投影。', 'level': 'guide-extension'},
    'landscape_dimension': {'meaning': '广度、抽象或时间轴，不是流程。', 'level': 'guide-extension'},
    'landscape_slice': {'meaning': '全景内的项目切片。', 'level': 'guide-extension'},
    'adm_phase': {'meaning': 'ADM 阶段标识，不是批准记录。', 'level': 'guide-extension'},
    'security_risk_concept': {'meaning': '安全与风险概念，可标 ISM/ERM 新增。', 'level': 'guide-extension'},
    'ism_process': {'meaning': '信息安全管理持续过程。', 'level': 'guide-extension'},
    'erm_process': {'meaning': '企业风险管理持续过程。', 'level': 'guide-extension'},
    'security_service': {'meaning': '安全服务目录展开项。', 'level': 'guide-extension'},
    'data_profiling': {'meaning': '数据剖析活动。', 'level': 'guide-extension'},
    'metadata_management': {'meaning': '元数据管理活动。', 'level': 'guide-extension'},
    'metadata_zone': {'meaning': 'METADATA 或 DATA 分区。', 'level': 'guide-extension'},
    'soa_layer': {'meaning': 'SOA 参考水平层。', 'level': 'guide-extension'},
    'soa_concern': {'meaning': 'SOA 跨层关注点。', 'level': 'guide-extension'},
}

REL_DEFS = {
    'project:contains': {'meaning': '组成或位于之内', 'source_types': ['*'], 'target_types': ['*']},
    'project:governs': {'meaning': '治理作用', 'source_types': ['repository_partition'], 'target_types': ['repository_partition']},
    'project:enables': {'meaning': '使能', 'source_types': ['*'], 'target_types': ['*']},
    'project:adopts': {'meaning': '采纳外部材料', 'source_types': ['repository_external'], 'target_types': ['repository_partition']},
    'project:visibility_escalation': {'meaning': '可见性与上报', 'source_types': ['repository_external'], 'target_types': ['repository_partition']},
    'project:steers': {'meaning': '引导能力', 'source_types': ['repository_external'], 'target_types': ['repository_partition']},
    'project:delivers_outcomes': {'meaning': '业务成果交付', 'source_types': ['repository_partition'], 'target_types': ['repository_partition']},
    'project:structured_by': {'meaning': '按框架结构化', 'source_types': ['repository_partition'], 'target_types': ['repository_partition']},
    'project:projects_to': {'meaning': '按轴或切片投影', 'source_types': ['*'], 'target_types': ['*']},
    'project:associates': {'meaning': '无方向关联', 'source_types': ['adm_phase'], 'target_types': ['security_risk_concept']},
    'project:continues': {'meaning': '持续循环', 'source_types': ['ism_process', 'erm_process'], 'target_types': ['ism_process', 'erm_process']},
    'project:catalog_expands': {'meaning': '目录展开', 'source_types': ['security_risk_concept'], 'target_types': ['security_service']},
    'project:profiling_reads': {'meaning': '剖析读取来源', 'source_types': ['data_profiling'], 'target_types': ['inference_source']},
    'project:structure_lifts': {'meaning': '结构上推', 'source_types': ['inference_source'], 'target_types': ['inference_source']},
    'project:metadata_uplinks': {'meaning': '元数据上行', 'source_types': ['data_profiling', 'inference_source'], 'target_types': ['metadata_management']},
    'project:maps_to': {'meaning': '层间映射', 'source_types': ['soa_layer'], 'target_types': ['soa_layer']},
    'project:cross_cuts_soa': {'meaning': '跨层关注覆盖', 'source_types': ['soa_concern'], 'target_types': ['soa_layer']},
}


def derive_shared_object_outputs(entities, relationships, title='共享对象派生'):
    """Same object IDs yield catalog, process and deployment views. Table ≠ figure acceptance."""
    from profile_render import render_profile
    view = {
        'id': 'v-shared-dual', 'title': title,
        'entity_ids': [e['id'] for e in entities],
        'relationship_ids': [r['id'] for r in relationships],
        'legend': '同一对象派生目录、过程与部署图；表/方法不等于原图视觉验收。',
        '_is_example': True
    }
    model = {'entities': entities, 'relationships': relationships}
    notice = '同一对象派生；表/方法/过程图不等于原图视觉验收。'
    outputs = {}
    for kind, renderer in (('catalog', 'catalog'), ('process', 'network'), ('deployment', 'deployment')):
        profile = {
            'id': 'derived-' + kind, 'renderer': renderer,
            'output_kind': 'table' if kind == 'catalog' else 'diagram',
            'template': {'source_verified': False, 'coverage_notice': notice},
            'required_attributes': {}
        }
        svg, report = render_profile(model, view, profile, 'reference')
        outputs[kind] = {'svg': svg, 'report': report}
    return outputs


def builders():
    return [architecture_repository(), architecture_landscape(), security_adm(),
            metadata_inference(), soa_layered()]


def write_docs(profiles):
    for p in profiles:
        path = ROOT / 'references/profiles' / (p['id'] + '.md')
        types = ', '.join(p['entity_types'])
        rels = ', '.join(p['relationship_types'])
        body = f"""# {p['name']}

`profile_id`: {p['id']}；`artifact_id`: {p['artifact_id']}；主责：[{p['owner']}](../../../{p['owner']}/SKILL.md)。

来源：{'；'.join(p['source_refs'])}。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：{p['version']}。

{json.dumps(p['template'], ensure_ascii=False, indent=2)}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。登记来源不等于实现视点已通过。

## 必需模型内容

对象类型：{types}。关系类型：{rels}。

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图或进度图。

## 检查与追溯

{chr(10).join('- ' + c for c in p['checks'])}

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。
"""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body)
        if p['artifact_id'] == p['id']:
            w = work_product(p['id'], p['name'], p['owner'], p['source_refs'], p['example'], p['entity_types'], p['relationship_types'])
            definition = ROOT / 'references/capabilities' / (p['id'] + '.md')
            definition.parent.mkdir(parents=True, exist_ok=True)
            definition.write_text(body + '\n## 分析与决策\n\n' + '\n'.join('- ' + x for x in w['analysis_steps']) + '\n\n' + w['decision'] + '\n\n字段：' + ', '.join(w['fields']) + '\n\n误读：' + '；'.join(w['misreadings']) + '\n')


def apply_registry(profiles):
    path = ROOT / 'capabilities.json'
    cap = json.loads(path.read_text())
    current = {p['id']: p for p in cap['profiles']}
    work = {w['id']: w for w in cap['work_products']}
    for p in profiles:
        if p['id'] == 'metadata-inference-structure' and p['id'] in current:
            base = copy.deepcopy(current[p['id']])
            base.update({k: p[k] for k in p if k != 'example'})
            base['example'] = p['example']
            base['template'] = {**base.get('template', {}), **p['template']}
            base['template']['source_verified'] = False
            current[p['id']] = base
        else:
            current[p['id']] = p
        if p['artifact_id'] == p['id']:
            work[p['id']] = work_product(p['id'], p['name'], p['owner'], p['source_refs'],
                                         p['example'], p['entity_types'], p['relationship_types'])
    if 'risk-security-traceability' in current:
        refs = [r for r in current['risk-security-traceability'].get('source_refs', []) if 'fig1-1' not in r]
        if 'G152/fig5-2' not in refs:
            refs.append('G152/fig5-2')
        current['risk-security-traceability']['source_refs'] = refs
    agile = ('agile-pattern-selection', 'agile-ea-development', 'agile-solution-collaboration',
             'agile-cross-development', 'agile-cross-functional')
    for pid in agile:
        if pid not in current:
            continue
        item = current[pid]
        item['definition_status'] = 'source-derived-view-with-project-construction-rules'
        item['blocked_source'] = {
            'tier': 'available-unverified',
            'reason': '本机原图或裁图可用；文件可用不等于语义已核。source_verified 仍为 false，直至独立评审。'
        }
        item.setdefault('template', {})['source_verified'] = False
    for pid, notice in (
        ('ea-service-adm-evidence-map', '表/方法入口不等于原图视觉验收。'),
        ('msa-federated-governance-process', '过程表不等于原图视觉验收。'),
        ('msa-source-deployment-execution', '表或派生部署图不等于原图视觉验收。'),
    ):
        if pid in current:
            current[pid].setdefault('template', {})['coverage_notice'] = notice
            current[pid]['template']['source_verified'] = False
    from companion_profiles import enrich_governance
    enrich_governance(current['msa-federated-governance-process'])
    cap['profiles'] = list(current.values())
    cap['work_products'] = list(work.values())
    cap.setdefault('default_profiles', {})
    for p in profiles:
        if p['artifact_id'] == p['id']:
            cap['default_profiles'].setdefault(p['id'], p['id'])
    cap.setdefault('extension_relationship_definitions', {}).update(REL_DEFS)
    path.write_text(json.dumps(cap, ensure_ascii=False, indent=2) + '\n')
    meta_path = ROOT / 'metamodel.json'
    meta = json.loads(meta_path.read_text())
    types = meta.setdefault('entity_types', {})
    for name, definition in ENTITY_DEFS.items():
        types.setdefault(name, definition)
    for name in REL_DEFS:
        meta.get('relationships', {}).pop(name, None)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')


def refresh_source_availability():
    """Align blocked_source with local assets; never set source_verified."""
    from classify_source_verification import classify, english_crops, load as loadj
    from collections import defaultdict
    cap_path = ROOT / 'capabilities.json'
    cap = json.loads(cap_path.read_text())
    registry = loadj(ROOT / 'evidence-registry.json') if (ROOT / 'evidence-registry.json').is_file() else {'figures': []}
    crops = english_crops()
    routings = defaultdict(list)
    for figure in cap.get('figure_profiles', []):
        for pid in figure.get('profile_ids') or []:
            routings[pid].append(figure['id'])
    for profile in cap['profiles']:
        tier, reason, evidence = classify(profile, routings.get(profile['id'], []), registry, crops)
        profile['blocked_source'] = {'tier': tier, 'reason': reason, 'asset_evidence': evidence}
        if profile.get('template'):
            profile['template']['source_verified'] = False
    cap_path.write_text(json.dumps(cap, ensure_ascii=False, indent=2) + '\n')


def main():
    from companion_profiles import build as companion_build
    from repository_reference_profiles import build as repository_build
    profiles = builders() + companion_build(json.loads((ROOT/'capabilities.json').read_text())) + repository_build()
    write_docs(profiles)
    apply_registry(profiles)
    refresh_source_availability()
    print(json.dumps({p['id']: {'entities': len(p['example']['entities']),
                                'relationships': len(p['example']['relationships'])}
                      for p in profiles}, ensure_ascii=False))


if __name__ == '__main__':
    main()
