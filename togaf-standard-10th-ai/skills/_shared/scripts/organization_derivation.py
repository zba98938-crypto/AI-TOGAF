"""Check declared organization/information associations, not exchange occurrence.

G190 section 4 and G206 section 5 motivate following organization-capability-
information associations. This project's explicit reference contract requires
support for BOTH exchange endpoints. It does not infer that information was sent,
that a capability was exercised, or that an organization must modify information.

Legacy free-text information_ref/derivation_path remains a manual declaration and
receives an unverified-derivation warning. Structured attributes are:
  information_ref_id: stable information entity ID
  derivation_relationship_ids: explicit set/list of supporting relationship IDs

owned_by is capability -> organization; traversing from an organization to its
capability does not reverse that stored relation. uses_information and
modifies_information are capability -> information. List order is immaterial.
This module is pure, performs no IO, and does not mutate the supplied model.
"""


def validate_organization_derivations(model, relationship_ids=None):
    """Return validate-compatible issues for selected information exchanges.

    relationship_ids limits exchange selection only; supporting entities and
    relationships are always resolved against the WHOLE model. The caller must
    still run general schema, provenance, type, state, and identity validation.
    Evidence checks here establish resolvable declarations, not their truth.
    """
    issues = []

    def issue(level, code, obj, message):
        issues.append({'level': level, 'code': code, 'id': obj, 'message': message})

    def index(records):
        result, duplicates = {}, set()
        for record in records:
            rid = record.get('id')
            if not isinstance(rid, str):
                continue
            if rid in result:
                duplicates.add(rid)
            result[rid] = record
        return result, duplicates

    entities, duplicate_entities = index(model.get('entities', []))
    relations, duplicate_relations = index(model.get('relationships', []))
    sources, duplicate_sources = index(model.get('sources', []))
    selected = None if relationship_ids is None else set(relationship_ids)

    for exchange in model.get('relationships', []):
        if exchange.get('type') != 'organization_information_exchange':
            continue
        xid = exchange.get('id', '<missing-exchange-id>')
        if selected is not None and xid not in selected:
            continue
        attrs = exchange.get('attributes', {})
        if not isinstance(attrs, dict):
            issue('error', 'invalid-derivation-contract', xid, '交换属性须为对象。')
            continue
        fields = ('information_ref_id', 'derivation_relationship_ids')
        if not any(field in attrs for field in fields):
            issue('warning', 'unverified-derivation', xid,
                  '仅有人工信息/派生声明；未提供结构化引用，不能称派生链已验证。')
            continue
        if not all(field in attrs for field in fields):
            issue('error', 'incomplete-derivation-contract', xid,
                  '结构化派生须同时提供 information_ref_id 和 derivation_relationship_ids。')
            continue
        info_id, path_ids = (attrs[field] for field in fields)
        if not isinstance(info_id, str) or not info_id.strip():
            issue('error', 'invalid-information-reference', xid, 'information_ref_id 须为非空稳定ID。')
            continue
        if (not isinstance(path_ids, list) or not path_ids
                or any(not isinstance(rid, str) or not rid.strip() for rid in path_ids)):
            issue('error', 'invalid-derivation-path', xid, '派生关系须为非空稳定关系ID列表。')
            continue
        if len(set(path_ids)) != len(path_ids):
            issue('error', 'duplicate-derivation-reference', xid, '派生关系ID不可重复。')
            continue
        if info_id not in entities:
            issue('error', 'unknown-information-reference', xid, '信息对象不存在：' + info_id)
            continue
        if info_id in duplicate_entities or xid in duplicate_relations:
            issue('error', 'ambiguous-derivation-id', xid, '信息或交换ID在模型中重复。')
            continue
        if entities[info_id].get('type') != 'information':
            issue('error', 'derivation-information-type', xid,
                  'information_ref_id 必须指向信息概念，而非同名组织、对象或能力。')
            continue
        endpoint_ids = [exchange.get('source'), exchange.get('target')]
        if any(eid not in entities or eid in duplicate_entities
               or entities[eid].get('type') != 'organization' for eid in endpoint_ids):
            issue('error', 'derivation-organization-endpoint', xid,
                  '交换两端必须是唯一、存在的组织ID。')
            continue

        def evidence(record):
            refs = record.get('evidence', [])
            if (not isinstance(refs, list) or not refs
                    or any(not isinstance(ref, str) or ref not in sources
                           or ref in duplicate_sources for ref in refs)):
                issue('error', 'derivation-evidence-reference', xid,
                      '交换及派生关系须有可解析的声明证据：' + str(record.get('id')))

        evidence(exchange)
        ownership, information = {}, {}
        valid = True
        for rid in path_ids:
            edge = relations.get(rid)
            if edge is None or rid in duplicate_relations:
                issue('error', 'unknown-derivation-reference', xid, '派生关系缺失或ID不唯一：' + rid)
                valid = False
                continue
            evidence(edge)
            source, target = edge.get('source'), edge.get('target')
            if (source not in entities or target not in entities
                    or source in duplicate_entities or target in duplicate_entities):
                issue('error', 'derivation-dangling-endpoint', xid, '派生关系端点缺失或不唯一：' + rid)
                valid = False
                continue
            typ = edge.get('type')
            if typ == 'owned_by':
                if entities[source].get('type') != 'capability' or target not in endpoint_ids:
                    issue('error', 'derivation-ownership-direction', xid,
                          'owned_by 必须从能力指向本交换的一端组织：' + rid)
                    valid = False
                else:
                    ownership[rid] = (source, target)
            elif typ in ('uses_information', 'modifies_information'):
                if entities[source].get('type') != 'capability' or target != info_id:
                    issue('error', 'derivation-information-direction', xid,
                          '信息使用/修改必须从能力指向被引用信息概念：' + rid)
                    valid = False
                else:
                    information[rid] = source
            else:
                issue('error', 'unsupported-derivation-relation', xid,
                      '派生支持只接受 owned_by 与能力的信息使用/修改关系：' + rid)
                valid = False
            # A named exchange state cannot borrow support from another named state.
            # Unspecified state is left to the general model validator, not inferred.
            named_state = exchange.get('state_id')
            if named_state and any(record.get('state_id') not in (None, named_state)
                                   for record in (edge, entities[source], entities[target])):
                issue('error', 'derivation-state-conflict', xid, '派生支持属于不同命名状态：' + rid)
                valid = False
        if not valid:
            continue
        used = set()
        for endpoint in dict.fromkeys(endpoint_ids):
            pairs = [(oid, iid) for oid, (capability, organization) in ownership.items()
                     for iid, information_capability in information.items()
                     if organization == endpoint and capability == information_capability]
            if not pairs:
                issue('error', 'disconnected-organization-derivation', xid,
                      '组织缺少经同一能力关联到所选信息的完整支持路径：' + endpoint)
            for oid, iid in pairs:
                used.update((oid, iid))
        for rid in set(path_ids) - used:
            issue('error', 'unused-derivation-reference', xid, '声明关系不属于任一端点的完整支持路径：' + rid)
    return issues
