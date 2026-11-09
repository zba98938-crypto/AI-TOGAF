# -*- coding: utf-8 -*-
"""Observable draft gaps for the five C220 E/F planning artifacts.

The field layout is a project convention. No weights, indices, approval or optimum
are inferred from the presence of an artifact or from successful rendering.
"""
import math
from datetime import date

ARTIFACTS = {
    'implementation-factor-catalog',
    'consolidated-gaps-solutions-dependencies-matrix',
    'architecture-definition-increments-table',
    'transition-architecture-state-evolution-table',
    'business-value-risk-matrix',
}


def check(model):
    entities = {e['id']: e for e in model.get('entities', [])}
    edges = {e['id']: e for e in model.get('relationships', [])}
    sources = {s['id']: s for s in model.get('sources', [])}
    findings = []

    def issue(level, code, identity, text):
        findings.append({'level': level, 'code': code, 'id': identity, 'message': text})

    for view in model.get('views', []):
        artifact = view['artifact_id']
        if artifact not in ARTIFACTS:
            continue
        selected = [entities[i] for i in view['entity_ids'] if i in entities]
        if artifact == 'architecture-definition-increments-table':
            for identity in view['relationship_ids']:
                edge = edges.get(identity, {})
                if edge.get('type') == 'implements_transition' and not edge.get('attributes', {}).get('increment_description'):
                    issue('warning', 'foundation-increment-gap', identity, '缺少项目在该过渡架构中的具体增量交付；只连线不足以定义增量。')
        for entity in selected:
            attrs = entity.get('attributes', {})
            identity = entity['id']
            if artifact == 'implementation-factor-catalog' and entity['type'] == 'implementation_factor':
                if not attrs.get('deduction') or not attrs.get('action_or_constraint'):
                    issue('warning', 'foundation-factor-deduction', identity, '实施因素需要推导出的行动或约束；仅列风险/假设名称仍有缺口。')
            if artifact == 'consolidated-gaps-solutions-dependencies-matrix' and entity['type'] == 'gap':
                for field in ('solution_refs', 'dependency_refs'):
                    if not isinstance(attrs.get(field), list):
                        issue('warning', 'foundation-gap-link', identity, field+'未评价；空列表只在明确评审无对应项时使用。')
                    else:
                        for ref in attrs[field]:
                            if ref not in entities:
                                issue('error', 'foundation-planning-reference', identity, field+'引用不存在：'+str(ref))
            if artifact == 'transition-architecture-state-evolution-table' and entity['type'] == 'sbb':
                if not all(attrs.get(f) for f in ('service_taxonomy', 'proposed_state', 'transition_ref', 'service_refs')):
                    issue('warning', 'foundation-transition-evolution', identity, 'SBB缺少服务分类、过渡状态或服务影响；不能由图形位置补出状态。')
                for ref in [attrs.get('transition_ref')] + (attrs.get('service_refs') if isinstance(attrs.get('service_refs'), list) else []):
                    if ref and ref not in entities:
                        issue('error', 'foundation-planning-reference', identity, '过渡或服务引用不存在：'+str(ref))
            if artifact != 'business-value-risk-matrix' or entity['type'] != 'work_package':
                continue
            observed = False
            for field in ('value_index', 'risk_index'):
                value = attrs.get(field)
                if value is None:
                    issue('warning', 'foundation-index-unknown', identity, field+'未评价；未知不转换为0，不据此排序。')
                elif type(value) not in (int, float) or not math.isfinite(value):
                    issue('error', 'foundation-index-value', identity, field+'必须是有限数值或未知；不能使用布尔值或文字代替指数。')
                else:
                    observed = True
            if observed:
                basis = attrs.get('criteria_basis')
                valid = (isinstance(basis, dict) and isinstance(basis.get('method'), str)
                         and bool(basis['method'].strip()) and isinstance(basis.get('source_refs'), list)
                         and bool(basis['source_refs']) and all(isinstance(ref, str) for ref in basis['source_refs']))
                if valid:
                    valid = all(ref in sources for ref in basis['source_refs'])
                if not valid:
                    issue('warning', 'foundation-index-basis', identity, '已填指数缺少可追溯准则和计算方法；保留候选，不能解释为有效排名。')
                # A claim of assessed (approved criteria) is stronger than a draft value.
                if attrs.get('evaluation_state') == 'assessed':
                    evidence = basis.get('approval_evidence', []) if isinstance(basis, dict) else []
                    approved = isinstance(evidence, list) and bool(evidence) and all(isinstance(ref, str) and ref in sources for ref in evidence)
                    approved = approved and any(sources[ref]['kind'] not in ('example', 'assumption', 'figure-interpretation') for ref in evidence)
                    approved = approved and bool(basis.get('approved_by')) and basis.get('criteria_defined_before_options') is True
                    if approved:
                        try:
                            defined = date.fromisoformat(basis['defined_on'])
                            accepted = date.fromisoformat(basis['approved_on'])
                            disclosed = date.fromisoformat(basis['options_disclosed_on'])
                            approved = defined <= accepted < disclosed
                        except (KeyError, TypeError, ValueError):
                            approved = False
                    if not valid or not approved:
                        issue('error', 'foundation-criteria-approval', identity, '声明已评价需证明高层预先制定并批准准则/权重；虚构材料或事后补准则不能证明真实批准。')
                    criteria = basis.get('criteria', []) if isinstance(basis, dict) else []
                    scores = attrs.get('criterion_scores', {})
                    ids = [c.get('id') for c in criteria if isinstance(c, dict)] if isinstance(criteria, list) else []
                    weights_valid = (bool(ids) and len(ids) == len(criteria)
                                     and all(isinstance(i, str) and i.strip() for i in ids)
                                     and len(ids) == len(set(ids))
                                     and all(c.get('dimension') in ('value', 'risk') for c in criteria))
                    for dimension, index in [('value', 'value_index'), ('risk', 'risk_index')]:
                        selected = [c for c in criteria if isinstance(c, dict) and c.get('dimension') == dimension] if isinstance(criteria, list) else []
                        def numeric(v):
                            return type(v) in (int, float) and math.isfinite(v)
                        valid_dimension = (weights_valid and bool(selected)
                                           and all(numeric(c.get('weight')) and c['weight'] >= 0 for c in selected))
                        valid_dimension = valid_dimension and math.isclose(sum(c['weight'] for c in selected), 1.0, abs_tol=1e-9)
                        if not valid_dimension:
                            issue('error', 'foundation-criteria-weights', identity, dimension+'准则缺少唯一ID、非负权重及总和1的明确规则；不能自动补等权。')
                            continue
                        if not isinstance(scores, dict) or not all(numeric(scores.get(c['id'])) for c in selected):
                            issue('error', 'foundation-criteria-scores', identity, dimension+'指数缺少逐准则的有限原始评分，不能由最终数字倒推证据。')
                            continue
                        expected = sum(scores[c['id']]*c['weight'] for c in selected)
                        if not numeric(attrs.get(index)) or not math.isclose(attrs[index], expected, rel_tol=1e-9, abs_tol=1e-9):
                            issue('error', 'foundation-index-calculation', identity, index+'与声明的逐准则加权计算不一致；取整或其他方法须保留草稿并明确新计算契约。')
    return findings
