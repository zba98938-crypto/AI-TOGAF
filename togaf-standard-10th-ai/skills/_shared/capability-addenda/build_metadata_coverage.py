# coding: utf-8
"""Create an additive metadata coverage contract; never edit central registries."""
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from expand_source_capabilities import profile, entity, edge

AID = 'metadata-asset-coverage'
PID = 'metadata-application-function-coverage'
MID = 'metadata-application-coverage-review'
CASE = 'examples/addenda/' + PID


def save(path, data):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def checklist():
    table = next(t for t in json.loads((ROOT / 'references/source-tables/metadata-functions.json').read_text())['tables'] if t['table'] == '表5-2')
    facets = {
        641: [('create', '创建元数据'), ('revise', '修订元数据'), ('delete', '删除元数据')],
        642: [('confidentiality', '保密性分类'), ('privacy', '隐私分类'), ('custom-classification', '自定义分类维度')],
        643: [('value-chain', '完整数据价值链关联'), ('lineage', '数据血缘关联')],
        644: [('automated-recording', '自动过程识别并记录元数据；示例算法不是强制清单')],
        645: [('execute-rule', '执行存储库定义的质量规则'), ('capture-result', '捕获规则执行结果')],
        646: [('create-workflow', '创建工作流'), ('visualize-states', '可视化状态'), ('visualize-tasks', '可视化任务')],
        647: [('assign-task', '把任务分配给人员')],
        648: [('view-change-impact', '查看元数据变更的影响')],
        649: [('report-usage', '报告元数据使用情况')],
        650: [('origin', '显示数据起源'), ('transformation', '显示数据转换'), ('transfer', '显示数据传输'), ('classification', '显示数据分类')],
        651: [('completion', '可视化元数据完成情况'), ('associations', '可视化元数据关联'), ('quality', '度量元数据质量'), ('sharing', '组织内共享结果')],
        652: [('accountability', '可视化谁对数据负责')],
        653: [('history', '历史质量度量'), ('current', '当前质量度量'), ('sharing', '组织内共享结果')],
        654: [('multiple-criteria', '多条件搜索'), ('full-text', '全文搜索'), ('autocomplete', '搜索自动补全')],
        655: [('create-normalized-values', '创建规范化值列表'), ('maintain-reference-values', '维护参考值列表')],
        656: [('multiple-environments', '管理多个环境'), ('per-environment-governance', '每环境治理设置'), ('per-environment-administration', '每环境管理设置')],
        657: [('create-permission', '创建访问权限'), ('delete-permission', '删除访问权限'), ('update-permission', '更新访问权限'), ('users-groups', '创建用户和组'), ('role-authorization', '按角色授权，区分批处理/用户角色')],
        658: [('language', '适应不同语言'), ('local-requirements', '适应本地要求')],
        659: [('events', '记录系统事件'), ('modification-history', '保留元数据修改历史'), ('provenance', '保留修改来源'), ('author', '保留修改作者')],
        660: [('database-version', '支持元数据数据库版本管理')],
        661: [('metadata-query', '用SQL或其他语言/接口查询元数据资产；不要求两者并用')],
        662: [('bulk-import', '从文件或接口导入多条元数据；不要求每种格式')],
        663: [('bulk-export', '用非专有文件格式或接口导出多条元数据')],
        664: [('subscribe-events', '监听事件代理的一个或多个事件')],
    }
    functions = []
    for row in table['rows']:
        group = re.split(r'[（(]', row['values'][0])[0]
        functions.append({'id': 'application-function-' + str(row['line']), 'group': group, 'name': row['values'][1], 'source_definition': row['values'][2], 'source_locator': 'G234 §5.2 表5-2 L' + str(row['line']), 'creation_category_check': row['line'] == 641, 'facets': [{'id': fid, 'name': name} for fid, name in facets[row['line']]]})
    # Eight categories are extracted from the source, rather than a second cap.
    creation = next(f for f in functions if f['creation_category_check'])['source_definition']
    names = re.findall(r'\*\*(.*?)\*\*', creation)
    categories = [{'id': 'category-' + str(i + 1), 'name': name} for i, name in enumerate(names)]
    result = {'schema_version': '1.0', 'source': 'G234 §5.2 表5-2', 'source_sha256': table['source_sha256'], 'definition_status': table['definition_status'], 'notice': '功能及完整定义来自随包来源表。facets为便于逐项核验而拆分的源语义，不是新的TOGAF强制认证判据；项目可有依据地裁剪。括号中的算法、格式和接口例子不是全部必须实现。', 'creation_categories': categories, 'functions': functions}
    save('references/source-tables/metadata-application-coverage-requirements.json', result)
    return result


def case(contract):
    """A fictional museum network, distinct from earlier metadata map examples."""
    raw = [
        {'id': 'MCR-SCOPE', 'text': '虚构五馆藏品联盟在2026-10-28评估2026年第四季度候选元数据平台，范围仅是馆藏目录与借展数据的元数据；数据治理负责人负责审查，不声称全企业上线或合规认证。馆方要求逐项核对G234表5-2的功能。'},
        {'id': 'MCR-ASSETS', 'text': '资产清单：A1藏品术语表（业务对象、业务元素、术语及删除/保留日期）；A2藏品数据字典（环境、应用/技术、数据库、表、列）；A3借展数据使用记录（活动、接收/提供方、传输、保护影响评估、访问权限、外部文档URL）；A4藏品分类（保密、隐私、业务价值和自定义维度）；A5数据规则与政策；A6数据问题及业务影响/质量执行问题；A7治理资产（主题/业务/地理分组、组合数据域及管家、所有者、经理、隐私官、保管人、应用所有者）；A8技术质量规则。八类资产均由数据治理负责人管理。'},
        {'id': 'MCR-TOOLS', 'text': '工具清单：T-CATALOG藏品目录工具2.4由平台组负责；T-QUALITY质量执行器1.8由质量组负责；T-WORKFLOW治理工作流3.0由数据治理组负责；T-GATEWAY集成网关1.2由集成组负责。同一工具被多个功能复用，不能复制成多个工具。'},
        {'id': 'MCR-RULE', 'text': '项目审查规则：已实现须有在明确版本/环境/日期对每个所需资产及功能方面的通过观察；计划中须有责任人、目标日期、里程碑和范围的计划证据；不足为未知；不适用须有范围、理由和裁剪授权。记录数量只作清点，不给默认分数或合格线。测试范围为staging-museum，非生产上线证明。'},
        {'id': 'MCR-TAILOR', 'text': '馆方数据治理负责人依据当前范围批准两项不适用：国际化/本地化（658）因本期仅馆内中文平台，无其他语言或本地规则适配需求；事件订阅（664）因本期批量交换，无事件代理。若范围变化，必须重新评审。'},
        {'id': 'MCR-PLAN', 'text': '数据治理负责人2026-10-20确认2026-12-15评审里程碑：目录工具2.4交付变更影响分析、端到端生命周期合规可视化、元数据完成/关联/质量共享报表、历史与当前质量共享报表、元数据数据库版本管理；所有计划范围按逐项验收清单，计划不代表实现。'},
        {'id': 'MCR-UNKNOWN', 'text': '尚未安排元数据自动推断测试；目录工具只有一般产品介绍，不能作为自动记录功能的项目实现证据。元数据活动监控未提供观测。搜索仅核实多条件和全文搜索，自动补全未知。事件日志只核实系统事件与修改历史，修改来源与作者未知。'},
        {'id': 'MCR-CHANGE', 'text': '修改材料：2026-10-28追加测试表明目录工具2.4在staging-museum对A1的事件日志同样保存了修改来源和作者；计划中的数据库版本管理尚无验收，其他结论保持。'},
    ]
    tools = [{'id': tid, 'name': name, 'version': version, 'owner': owner, 'evidence': ['MCR-TOOLS']} for tid, name, version, owner in [('T-CATALOG', '藏品目录工具', '2.4', '平台组'), ('T-QUALITY', '质量执行器', '1.8', '质量组'), ('T-WORKFLOW', '治理工作流', '3.0', '数据治理组'), ('T-GATEWAY', '集成网关', '1.2', '集成组')]]
    names = ['藏品术语表', '藏品数据字典', '借展数据使用记录', '藏品分类', '数据规则与政策', '数据问题及业务影响', '治理资产', '技术质量规则']
    assets = [{'id': 'A' + str(i + 1), 'name': name, 'category': contract['creation_categories'][i]['id'], 'category_name': contract['creation_categories'][i]['name'], 'owner': '数据治理负责人', 'evidence': ['MCR-ASSETS']} for i, name in enumerate(names)]
    scope = {641: [a['id'] for a in assets], 642: ['A4'], 643: ['A3'], 644: ['A2'], 645: ['A8'], 646: ['A6'], 647: ['A6'], 648: ['A1', 'A2'], 649: ['A1'], 650: ['A3'], 651: ['A1'], 652: ['A7'], 653: ['A8'], 654: ['A1'], 655: ['A4'], 656: ['A2'], 657: ['A3'], 658: [], 659: ['A1'], 660: ['A2'], 661: ['A2'], 662: ['A2'], 663: ['A2'], 664: []}
    planned = {648, 650, 651, 653, 660}
    unknown = {644, 649, 654, 659}
    excluded = {658, 664}
    bytool = {645: 'T-QUALITY', 646: 'T-WORKFLOW', 647: 'T-WORKFLOW', 661: 'T-GATEWAY', 662: 'T-GATEWAY', 663: 'T-GATEWAY'}
    versions = {t['id']: t['version'] for t in tools}
    assessments = []
    for function in contract['functions']:
        n = int(function['id'].rsplit('-', 1)[1]);facets = [f['id'] for f in function['facets']]
        state = 'not-applicable' if n in excluded else 'planned' if n in planned else 'unknown' if n in unknown else 'implemented'
        rec = {'id': 'MC-' + str(n), 'function_id': function['id'], 'coverage_scope': '本期馆藏/借展元数据，仅所列资产及源语义方面；不推及全部数据或所有产品功能', 'required_asset_ids': scope[n], 'owner': '数据治理负责人', 'requirement_evidence': ['MCR-SCOPE', 'MCR-ASSETS', 'MCR-RULE'], 'declared_status': state, 'excluded_facets': [], 'bindings': []}
        if state == 'not-applicable':
            rec['exclusion'] = {'reason': '本期仅中文馆内平台，无其他语言/本地要求适配需求' if n == 658 else '本期只有批量交换，没有事件代理', 'authority': '数据治理负责人', 'scope': '2026Q4馆藏/借展项目；范围变更重审', 'evidence': ['MCR-TAILOR']}
        else:
            selected = facets if n not in unknown else ['multiple-criteria', 'full-text'] if n == 654 else ['events', 'modification-history'] if n == 659 else []
            if selected:
                tid = bytool.get(n, 'T-CATALOG')
                binding = {'id': 'B-' + str(n), 'tool_id': tid, 'tool_version': versions[tid], 'asset_ids': scope[n], 'facet_ids': selected, 'status': 'planned' if n in planned else 'implemented'}
                if n in planned:
                    binding['plan'] = {'owner': '数据治理负责人', 'target_date': '2026-12-15', 'milestone': '馆藏目录候选功能评审', 'scope': [{'asset_id': a, 'facet_id': f} for a in scope[n] for f in facets], 'evidence': ['MCR-PLAN']}
                else:
                    observations = []
                    for a in scope[n]:
                        for facet in function['facets']:
                            if facet['id'] not in selected:continue
                            oid = 'OBS-' + str(n) + '-' + a + '-' + facet['id']
                            behavior = '在' + a + '记录上观察到' + facet['name'] + '；仅此资产与功能方面。'
                            raw.append({'id': oid, 'text': '虚构测试记录：2026-10-26，staging-museum，' + tid + '版本' + versions[tid] + '：' + behavior + '结果通过；由平台测试员记录。'})
                            observations.append({'id': oid, 'asset_id': a, 'facet_id': facet['id'], 'observed_behavior': behavior, 'evidence': [oid]})
                    binding['verification'] = {'method': '按馆方逐资产/逐功能验收清单观察并记录', 'observed_at': '2026-10-26', 'environment': 'staging-museum', 'result': 'pass', 'evidence': [o['id'] for o in observations], 'acceptance_observations': observations}
                rec['bindings'].append(binding)
            # Demonstrate the same asset/facet implemented by two tools with
            # distinct observations; two tools never become two source functions.
            if n == 661:
                second = copy.deepcopy(rec['bindings'][0]);second['id'] = 'B-661-CATALOG';second['tool_id'] = 'T-CATALOG';second['tool_version'] = '2.4'
                for obs in second['verification']['acceptance_observations']:
                    obs['id'] += '-CATALOG';obs['evidence'] = [obs['id']]
                    raw.append({'id': obs['id'], 'text': '虚构测试记录：2026-10-26，staging-museum，T-CATALOG 2.4也用查询API对A2成功查询元数据；这与T-GATEWAY 1.2是两个工具实现同一个源功能，不是新增功能。'})
                second['verification']['evidence'] = [o['id'] for o in second['verification']['acceptance_observations']]
                rec['bindings'].append(second)
        assessments.append(rec)
    kinds = {'MCR-SCOPE': 'scope', 'MCR-ASSETS': 'asset-inventory', 'MCR-TOOLS': 'tool-inventory', 'MCR-RULE': 'project-rule', 'MCR-TAILOR': 'tailoring', 'MCR-PLAN': 'plan', 'MCR-UNKNOWN': 'unverified', 'MCR-CHANGE': 'observation'}
    for record in raw:record['kind'] = kinds.get(record['id'], 'observation')
    baseline = {'scope': '五馆联盟2026Q4馆藏目录与借展元数据', 'architecture_state': 'candidate-2026Q4', 'as_of': '2026-10-28', 'owner': '数据治理负责人', 'scope_evidence': ['MCR-SCOPE', 'MCR-RULE'], 'source_ids': [r['id'] for r in raw], 'evidence_records': [{'id': r['id'], 'kind': r['kind']} for r in raw], 'tools': tools, 'assets': assets, 'assessments': assessments}
    modified = copy.deepcopy(baseline)
    row = next(r for r in modified['assessments'] if r['function_id'] == 'application-function-659')
    row['declared_status'] = 'implemented';binding = row['bindings'][0];binding['facet_ids'] += ['provenance', 'author'];binding['verification']['observed_at'] = '2026-10-28';binding['verification']['evidence'].append('MCR-CHANGE')
    for facet, desc in [('provenance', '修改来源'), ('author', '修改作者')]:
        binding['verification']['acceptance_observations'].append({'id': 'OBS-659-A1-' + facet, 'asset_id': 'A1', 'facet_id': facet, 'observed_behavior': '追加测试在A1日志记录中保留了' + desc, 'evidence': ['MCR-CHANGE']})
    return raw, baseline, modified


def model(data, result, contract, version):
    context = {'domains': ['data', 'application'], 'landscape': 'segment', 'purpose': 'project', 'abstraction': 'logical', 'evolution': 'target'}
    sources = [{'id': sid, 'kind': 'example', 'description': '虚构五馆联盟原始业务/验收材料 ' + sid, 'locator': CASE + '/raw-materials.json#' + sid} for sid in data['source_ids']]
    sources.append({'id': 'G234-T52', 'kind': 'local-translation', 'description': '随包G234表5-2；本地译文，官方定义核查单独记录', 'locator': 'references/source-tables/metadata-functions.json'})
    entities, relationships = [], []
    for tool in data['tools']:
        ent = entity(tool['id'], 'g234:metadata-tool', tool['name'], {k: v for k, v in tool.items() if k not in ['id', 'name']});ent['evidence'] = tool['evidence'];ent['version'] = tool['version'];entities.append(ent)
    for asset in data['assets']:
        ent = entity(asset['id'], 'metadata_asset', asset['name'], {k: v for k, v in asset.items() if k not in ['id', 'name']});ent['evidence'] = asset['evidence'];ent['version'] = '1';entities.append(ent)
    rows = {r['id']: r for r in result['rows']}
    for assessment in data['assessments']:
        row = rows[assessment['id']]
        attrs = {'source_function_id': row['function_id'], 'source_group': row['group'], 'source_definition': row['source_definition'], 'project_scope': data['scope'], 'architecture_state': data['architecture_state'], 'as_of': data['as_of'], 'assessment': assessment, 'analysis_result': row, 'coverage_status': row['status']}
        ent = entity(row['id'], 'g234:function-coverage', row['name'] + '／项目覆盖审查', attrs);ent['evidence'] = ['G234-T52'] + assessment['requirement_evidence'];ent['version'] = version;entities.append(ent)
        for aid in assessment['required_asset_ids']:
            rel = edge(assessment['id'] + '-asset-' + aid, 'g234:coverage-of-asset', assessment['id'], aid, '本功能审查范围包含此元数据资产', {'source_function_id': row['function_id']});rel['evidence'] = assessment['requirement_evidence'];relationships.append(rel)
        for binding in assessment['bindings']:
            ev = binding.get('verification', binding.get('plan', {})).get('evidence', ['MCR-UNKNOWN'])
            rel = edge(binding['id'], 'g234:tool-coverage-claim', binding['tool_id'], assessment['id'], '工具在指定资产/功能方面上的覆盖声明，最终状态见审查结果', {'asset_ids': binding['asset_ids'], 'facet_ids': binding['facet_ids'], 'tool_version': binding['tool_version'], 'claimed_status': binding['status']});rel['evidence'] = ev;relationships.append(rel)
    view = {'id': 'v-' + PID, 'artifact_id': AID, 'profile_id': PID, 'title': '五馆联盟元数据应用功能覆盖／' + version, 'context': context, 'entity_ids': [e['id'] for e in entities], 'relationship_ids': [r['id'] for r in relationships], 'analysis': '逐源功能、项目资产和功能方面审核工具证据。修改仅新增事件日志来源/作者的测试，其他未核实功能保持原状态。计划、未知与不适用均可见，不计算覆盖率。', 'legend': '四态为项目操作规则；相同工具ID表示复用，关系表达审查范围或声明，不自动证明实现。', 'attributes': {'analysis_ids': ['metadata-coverage-analysis']}}
    return {'schema_version': '2.0', 'project': {'id': 'museum-metadata-coverage', 'name': '虚构五馆联盟元数据功能审查', 'version': version, 'context': context, 'is_example': True, 'approval_status': 'candidate', 'implementation_status': 'not-started'}, 'sources': sources, 'entities': entities, 'relationships': relationships, 'views': [view], 'deliverables': [], 'gaps': [], 'comparisons': [], 'scopes': [], 'states': [], 'analyses': [{'id': 'metadata-coverage-analysis', 'method_id': MID, 'inputs': data, 'evidence': data['source_ids']}], 'extensions': {'relationship_types': RELATIONS}}


RELATIONS = {
    'g234:coverage-of-asset': {'source_types': ['g234:function-coverage'], 'target_types': ['metadata_asset'], 'meaning': '功能覆盖审查所要求的资产；不表示资产实现软件功能'},
    'g234:tool-coverage-claim': {'source_types': ['g234:metadata-tool'], 'target_types': ['g234:function-coverage'], 'meaning': '工具在明确版本、资产及功能方面的覆盖声明；需读取审查结果，关系存在不自动等于已实现'},
}


def main():
    contract = checklist()
    from metadata_coverage_analysis import review_metadata_coverage
    raw, baseline, modified = case(contract)
    save(CASE + '/raw-materials.json', {'notice': '独立虚构五馆联盟原始业务记录；每个观察均为示例，不是实际工具测试或客户事实。方法提取和整理这些材料，生成器不负责从文本猜测事实。', 'records': raw})
    models = {}
    for variant, data in [('baseline', baseline), ('modified', modified)]:
        result = review_metadata_coverage(data)
        models[variant] = model(data, result, contract, '1' if variant == 'baseline' else '2')
        save(CASE + '/' + variant + '-model.json', models[variant]);save(CASE + '/' + variant + '-analysis.json', result)
        mappings = []
        for assessment in data['assessments']:
            refs = set(assessment['requirement_evidence'])
            refs.update(assessment.get('exclusion', {}).get('evidence', []))
            for binding in assessment['bindings']:refs.update(binding.get('verification', binding.get('plan', {})).get('evidence', []))
            if not assessment['bindings'] and assessment['declared_status'] == 'unknown':refs.add('MCR-UNKNOWN')
            mappings.append({'entity_id': assessment['id'], 'source_function_id': assessment['function_id'], 'field': 'assessment', 'raw_record_ids': sorted(refs), 'operation': 'extract scoped requirement and observations/plans, then run evidence-bounded review'})
        save(CASE + '/' + variant + '-transformation.json', {'raw_source': 'raw-materials.json', 'source_function_checklist': 'references/source-tables/metadata-application-coverage-requirements.json', 'field_mappings': mappings, 'calculator': MID, 'result': variant + '-analysis.json', 'limit': '原料为虚构完整案例；结构化提取由代理进行。计算器审核证据引用与规则，不证明自由文本陈述或外部工具实际成立。'})
    refs = ['G234 §5.2 图5-2、表5-2 L641–664', 'G234 §4.3 图4-5（现有工作产品扩展关系）']
    inputs = ['项目范围、架构状态、观察日期与责任人', '完整源功能清单及逐项裁剪证据', '工具稳定ID、版本、责任人', '元数据资产稳定ID、来源类别及范围', '逐功能要求与资产/方面、实现观察或计划/排除证据']
    steps = ['从表5-2加载全部源功能及完整定义，不用图存在推断实施', '从业务材料识别工具/版本与元数据资产，按稳定ID复用', '按每功能定义选择资产范围及语义方面，排除必须有授权依据', '逐资产/方面检查观察、计划或排除；无评估条目自动为未知', '汇总四态与带ID缺口，修改后重审同一范围/状态及工具版本']
    checks = ['源表每行有一个处置结果；遗漏为未知', '641八类创建对象需逐类资产或明确裁剪，原定义保留子项', '659必须区分事件、修改历史、来源、作者；历史存在不证明其余', '已实现须有逐资产/方面的通过观察，计划不提升为实现', '重复工具复用稳定ID，不重复计算源功能', '参考图/产品介绍不构成实施证据，不创建TOGAF分数或合格线', '不适用须有范围、理由与授权证据；批准状态另记']
    required = {'g234:function-coverage': ['source_function_id', 'source_group', 'source_definition', 'project_scope', 'architecture_state', 'as_of', 'assessment', 'analysis_result', 'coverage_status'], 'g234:metadata-tool': ['version', 'owner', 'evidence'], 'metadata_asset': ['category', 'category_name', 'owner', 'evidence']}
    ex = {'notice': '虚构五馆联盟完整案例，源定义不是项目实施事实', 'sources': models['baseline']['sources'], 'entities': models['baseline']['entities'], 'relationships': models['baseline']['relationships'], 'view': models['baseline']['views'][0], 'analyses': models['baseline']['analyses'], 'extensions': models['baseline']['extensions']}
    p = profile(PID, AID, '元数据应用功能—工具—资产覆盖评估表', 'togaf-information-data', refs, 'catalog', list(required), list(RELATIONS), required, ex, {'version': '1.0', 'source_verified': False, 'structure_basis': '正文表5-2功能定义的项目覆盖评估表；不是图5-2参考功能地图复刻'}, kind='table')
    p.update({'version': '1.0', 'table_orientation': 'records', 'required_inputs': inputs, 'analysis_steps': steps, 'checks': checks, 'method_reference': 'references/capability-addenda/metadata-function-coverage.md', 'missing_input_policy': '缺评估/证据/资产范围为unknown；源功能不被删除，不默认通过；冲突ID、版本和无效证据引用拒绝执行。', 'relationship_definitions': RELATIONS, 'implementation_status': {'definition': 'local-body-reviewed-official-authentication-separate', 'model': 'baseline-and-modified-complete', 'analysis': 'calculator-executed-tests-pending', 'generation': 'pending', 'modification': 'case-declared', 'review': 'pending', 'visual': 'not-applicable-table'}})
    package = {'schema_version': '1.0', 'notice': '扩展既有metadata-asset-coverage；不替换默认分类矩阵或参考功能图，不新增制品族。登记不等于验收。', 'work_products': [], 'profiles': [p], 'analysis_methods': [{'id': MID, 'name': '元数据应用功能覆盖审查', 'owner': 'togaf-information-data', 'source_refs': refs, 'required_inputs': inputs, 'analysis_steps': steps, 'checks': checks, 'missing_input_policy': p['missing_input_policy'], 'output_work_products': [AID], 'calculator_id': MID, 'method_reference': p['method_reference'], 'example_model': CASE + '/baseline-model.json', 'definition_status': 'source-semantics-plus-explicit-project-operational-contract', 'implementation_status': 'calculator-executed-validation-pending'}], 'patches': [{'group': 'work_products', 'id': AID, 'add': {'source_refs': refs, 'optional_inputs': ['按需使用 metadata-application-function-coverage，输入功能/工具/资产覆盖证据；不改变原默认分类矩阵'], 'checks': checks, 'method_profiles': [{'profile_id': PID, 'method_id': MID, 'reference': p['method_reference'], 'decision': '所需元数据应用功能在项目工具与资产范围内有哪些证据、计划、未知和不适用？'}]}}], 'relationship_definitions': RELATIONS, 'entity_definitions': {'g234:metadata-tool': {'meaning': '项目元数据工具/应用的稳定身份与版本；不是源参考功能或资产'}, 'g234:function-coverage': {'meaning': '特定范围/状态/日期的源应用功能覆盖审查记录；不等于功能本体或已实施事实'}}, 'candidate_resolutions': [{'candidate_id': PID, 'status': 'implemented-pending-independent-acceptance', 'work_product_ids': [AID], 'profile_ids': [PID], 'analysis_method_ids': [MID], 'reason': '在现有元数据资产覆盖工作产品上增加项目工具/资产对源功能的四态评估，不把参考功能图误计为已实现'}]}
    save('capability-addenda/metadata-function-coverage-addenda.json', package)
    print({'new_work_products': 0, 'profiles': 1, 'methods': 1, 'source_functions': len(contract['functions']), 'creation_categories': len(contract['creation_categories']), 'baseline': review_metadata_coverage(baseline)['status_counts'], 'modified': review_metadata_coverage(modified)['status_counts']})


if __name__ == '__main__':main()
