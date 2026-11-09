"""Audit contract vocabulary without turning model extensions into core types.

Global extension definitions are a reusable definition pool. A model still has
to embed the extensions it uses; validate.py does not import that pool for it.
Each contract may also provide its own extensions or example extensions.
"""
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def core_vocabulary():
    """The v2 acceptance set built by validate.py, including registry work products."""
    from registry import load
    artifacts, deliverables, _, _ = load()
    meta = json.loads((ROOT / 'metamodel.json').read_text())
    relationships = json.loads((ROOT / 'relationships.json').read_text())['relationships']
    entities = {'activity', 'decision', 'outcome', 'benefit', 'measure', 'gap',
                'evidence', 'repository_asset', 'viewpoint', 'transition', 'milestone'}
    entities.update(meta.get('entity_types', {}))
    for contract in [*artifacts.values(), *deliverables.values()]:
        entities.update(contract.get('entity_types', []))
    return entities, set(relationships) | set(meta.get('relationships', {}))


def audit_contract(row, caps, core=None):
    """Check one declaration in its own scope, including definition validity."""
    from validate import NAMESPACE
    core_entities, core_relations = core if core is not None else core_vocabulary()
    declared = {
        'entity_types': set(row.get('entity_types') or []) | (set(row.get('required_attributes') or {}) - {'*'}),
        'relationship_types': set(row.get('relationship_types') or []),
    }
    cores = {'entity_types': core_entities, 'relationship_types': core_relations}
    pools = {'entity_types': caps.get('extension_entity_definitions', {}),
             'relationship_types': caps.get('extension_relationship_definitions', {})}
    schema = json.loads((ROOT / 'schemas/model.schema.json').read_text())['properties']['extensions']
    problems = []
    definitions = {'entity_types': {}, 'relationship_types': {}}

    # A profile's example must not borrow a different profile's definitions.
    # The explicit global pool is the only shared source of extension meanings.
    for kind in definitions:
        definitions[kind].update({name: value for name, value in pools[kind].items()
                                  if name not in cores[kind]})
    local_names = {'entity_types': set(), 'relationship_types': set()}
    for location, extensions in [('extensions', row.get('extensions', {})),
                                 ('example.extensions', (row.get('example') or {}).get('extensions', {}))]:
        for error in jsonschema.Draft202012Validator(schema).iter_errors(extensions):
            problems.append({'code': 'schema', 'location': location,
                             'id': '/'.join(map(str, error.absolute_path)), 'message': error.message})
        if not isinstance(extensions, dict):
            continue
        for kind in definitions:
            values = extensions.get(kind, {})
            if not isinstance(values, dict):
                continue
            for name, value in values.items():
                if name in local_names[kind] and definitions[kind][name] != value:
                    problems.append({'code': 'conflicting-extension-definition', 'location': location, 'id': name})
                local_names[kind].add(name)
                definitions[kind][name] = value

    # Validate every local definition plus global definitions needed by this
    # contract, and any endpoint types those relationship definitions require.
    needed = {kind: (declared[kind] - cores[kind]) | local_names[kind] for kind in definitions}
    for name in needed['relationship_types']:
        rule = definitions['relationship_types'].get(name)
        if isinstance(rule, dict):
            for field in ('source_types', 'target_types'):
                if isinstance(rule.get(field), list):
                    needed['entity_types'].update(t for t in rule[field] if isinstance(t, str) and t != '*' and t not in core_entities)
    valid = {'entity_types': set(core_entities), 'relationship_types': set(core_relations)}
    for kind in definitions:
        definition_schema = schema['properties'][kind]['additionalProperties']
        for name in sorted(needed[kind]):
            if name not in definitions[kind]:
                continue
            errors = list(jsonschema.Draft202012Validator(definition_schema).iter_errors(definitions[kind][name]))
            code = ('core-vocabulary-override' if name in cores[kind] else
                    'extension-namespace' if not NAMESPACE.fullmatch(name) else
                    'schema' if errors else None)
            if code:
                problems.append({'code': code, 'location': kind, 'id': name,
                                 'message': '; '.join(error.message for error in errors)})
            else:
                valid[kind].add(name)
    for name in sorted(needed['relationship_types'] & valid['relationship_types']):
        if name in core_relations:
            continue
        rule = definitions['relationship_types'][name]
        missing = sorted(set(rule['source_types'] + rule['target_types']) - valid['entity_types'] - {'*'})
        if missing:
            problems.append({'code': 'dangling-reference', 'location': 'relationship_types',
                             'id': name, 'missing_endpoint_types': missing})
            valid['relationship_types'].remove(name)
    return {'id': row['id'],
            'missing_entities': sorted(declared['entity_types'] - valid['entity_types']),
            'missing_relations': sorted(declared['relationship_types'] - valid['relationship_types']),
            'invalid_definitions': problems}


def audit_contracts(caps, core=None):
    core = core if core is not None else core_vocabulary()
    return [dict(audit_contract(row, caps, core), group=group, owner=row.get('owner'))
            for group in ('work_products', 'profiles') for row in caps.get(group, [])]
