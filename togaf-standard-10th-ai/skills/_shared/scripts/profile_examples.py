"""Wrap registered example fragments without repairing their business content."""
import copy


DEFAULT_CONTEXT = dict(domains=['business', 'data', 'application', 'technology'],
                       landscape='segment', purpose='project', abstraction='logical',
                       evolution='target')


def normalize_example(profile):
    """Return a full v2 model; declared context/state always wins over defaults."""
    model = copy.deepcopy(profile['example'])
    view = model.pop('view')
    supporting_views = model.pop('supporting_views', [])
    for key in ('notice', 'raw_input', 'analysis_path', 'raw_input_group'):
        model.pop(key, None)
    context = copy.deepcopy(view.get('context', DEFAULT_CONTEXT))
    states = {row['id']: row for row in model.get('states', [])}
    if view.get('state_id') in states:
        context['evolution'] = states[view['state_id']]['evolution']
    model.update(schema_version='2.0', project={
        'id': 'example-' + profile['id'], 'name': '虚构能力示例：' + profile['name'],
        'version': '1', 'context': context, 'is_example': True,
        'approval_status': 'candidate', 'implementation_status': 'not-started'},
        views=[view] + supporting_views, deliverables=[], gaps=[])
    view.setdefault('context', copy.deepcopy(context))
    return model


def declare_relationship_extensions(example, definitions):
    """Builder-only helper: embed the declared vocabulary actually used by a case."""
    used = {row['type'] for row in example.get('relationships', []) if ':' in row['type']}
    if not used:
        return example
    target = example.setdefault('extensions', {}).setdefault('relationship_types', {})
    for name in sorted(used):
        if name not in definitions and name not in target:
            raise ValueError('Missing example relationship definition: ' + name)
        if name in definitions:
            if name in target and target[name] != definitions[name]:
                raise ValueError('Conflicting example relationship definition: ' + name)
            target[name] = copy.deepcopy(definitions[name])
    return example
