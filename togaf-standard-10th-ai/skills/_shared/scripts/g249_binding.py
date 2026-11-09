"""Strict source-model binding of the full G249 reasoning context and objects."""
from analysis_projection_binding import _equal

VERSION = 'g249-assessment-binding/1'


def binding_issues(model, analysis):
    issues = []
    data = analysis.get('inputs', {})
    entities = {e['id']: e for e in model.get('entities', [])}
    def issue(identity, message):
        issues.append({'level': 'error', 'code': 'g249-analysis-binding', 'id': analysis['id'] + ':' + identity, 'message': message})
    binding = data.get('model_binding', {})
    if not isinstance(binding, dict) or binding.get('version') != VERSION:
        issue('model_binding', 'G249 reasoning requires explicit versioned context binding.')
        return issues
    context = entities.get(binding.get('context_ref'))
    if not context or context.get('type') != 'guide:g249-assessment-context':
        issue('context_ref', 'Bind an existing guide:g249-assessment-context entity.')
        return issues
    if not _equal(context.get('attributes', {}).get('assessment_inputs'), data):
        issue('context', 'Reasoning inputs differ from the current model context; review and synchronize before reuse.')
    snapshots = data.get('model_objects', [])
    if not isinstance(snapshots, list):
        issue('model_objects', 'Expected current model entity snapshots.')
        return issues
    seen = set()
    for row in snapshots:
        identity = row.get('id') if isinstance(row, dict) else None
        if not identity or identity in seen:
            issue('model_objects', 'Every snapshot needs a unique object ID.')
            continue
        seen.add(identity)
        if not _equal(row, entities.get(identity)):
            issue(identity, 'Task object snapshot differs from the current model entity.')
    selected = set()
    for task in data.get('tasks', []):
        refs = task.get('model_object_refs', [])
        if not isinstance(refs, list) or not refs:
            issue(task.get('id', 'task'), 'Each task must reference current model objects and corresponding snapshots.')
            continue
        for identity in refs:
            if not isinstance(identity, str) or identity not in seen:
                issue(task['id'], 'Task object reference lacks a model snapshot: ' + str(identity))
            else:
                selected.add(identity)
    if selected != seen:
        issue('model_objects', 'Snapshots must exactly cover task model_object_refs, without unreferenced objects.')
    edges = data.get('model_relationships', [])
    if not isinstance(edges, list):
        issue('model_relationships', 'Expected current model relationship snapshots.')
        return issues
    actual_edges = {r['id']: r for r in model.get('relationships', []) if r.get('source') in selected and r.get('target') in selected}
    edge_ids = set()
    for row in edges:
        identity = row.get('id') if isinstance(row, dict) else None
        if not identity or identity in edge_ids:
            issue('model_relationships', 'Every relationship snapshot requires a unique ID.')
            continue
        edge_ids.add(identity)
        if not _equal(row, actual_edges.get(identity)):
            issue(str(identity), 'Task relationship snapshot differs from the current scoped model relationship.')
    if edge_ids != set(actual_edges):
        issue('model_relationships', 'Relationship snapshots must exactly cover model relationships whose endpoints are both in task object scope; additions and removals require review.')
    # Old contexts remain readable with a runtime verification gap. Once supplied,
    # view selection is exact: removing a real view from the snapshot cannot hide
    # it, and a stale added/deleted/changed view cannot satisfy a task's output.
    if 'model_views' in data:
        views = data['model_views']
        if not isinstance(views, list):
            issue('model_views', 'Expected complete task-artifact view snapshots.')
            return issues
        intended = {artifact for task in data.get('tasks', []) for artifact in task.get('artifact_ids', [])}
        actual_views = {v['id']: v for v in model.get('views', []) if v.get('artifact_id') in intended}
        view_ids = set()
        for row in views:
            identity = row.get('id') if isinstance(row, dict) else None
            if not identity or identity in view_ids:
                issue('model_views', 'Every view snapshot requires a unique ID.')
                continue
            view_ids.add(identity)
            if not _equal(row, actual_views.get(identity)):
                issue(str(identity), 'Task view snapshot differs from the selected current model view.')
        if view_ids != set(actual_views):
            issue('model_views', 'Snapshots must exactly cover selected current views of intended task artifacts; additions and removals require review.')
    return issues


def role_binding_issues(model, analysis):
    """Bind optional review policy and collaboration graph to the role records."""
    issues = []
    data = analysis.get('inputs', {})
    def issue(identity, message):
        issues.append({'level': 'error', 'code': 'g249-role-binding', 'id': analysis['id'] + ':' + identity, 'message': message})
    context = {key: data[key] for key in ('hierarchy_policy', 'as_of', 'tier_tailoring_reason') if key in data}
    if context:
        entity = next((e for e in model.get('entities', []) if e['id'] == data.get('policy_context_ref')), None)
        if not entity or entity.get('type') != 'repository_asset' or not _equal(entity.get('attributes', {}).get('role_review_context'), context):
            issue('policy_context_ref', 'Role policy/time/tailoring snapshot requires a matching repository_asset.attributes.role_review_context.')
    linked = [v for v in model.get('views', []) if v.get('profile_id') == 'architecture-role-collaboration'
              and analysis['id'] in v.get('attributes', {}).get('analysis_ids', [])]
    if not linked:
        return issues
    expected = {}
    for role in data.get('roles', []):
        for rel in role.get('relationships', []):
            identity = rel.get('id')
            if identity in expected:
                issue(str(identity), 'Role relationships require globally unique IDs.')
            expected[identity] = (role['id'], rel)
    actual = {r['id']: r for r in model.get('relationships', [])}
    for view in linked:
        if set(view.get('relationship_ids', [])) != set(expected):
            issue(view['id'], 'Collaboration view must match the exact typed relationship selection in the review.')
    core_types = {'collaborates_with', 'reports_to'}
    for identity, (source, rel) in expected.items():
        edge = actual.get(identity, {})
        typ = rel.get('type') if rel.get('type') in core_types else 'g249:' + str(rel.get('type'))
        wanted = {key: value for key, value in rel.items() if key not in ('id', 'type', 'target', 'evidence')}
        attrs = {key: value for key, value in edge.get('attributes', {}).items() if key != 'semantic_type'}
        if (edge.get('source') != source or edge.get('target') != rel.get('target') or edge.get('type') != typ
                or not _equal(edge.get('evidence'), rel.get('evidence')) or not _equal(attrs, wanted)):
            issue(str(identity), 'Graph relationship differs from the typed, scoped, evidenced role snapshot.')
    return issues
