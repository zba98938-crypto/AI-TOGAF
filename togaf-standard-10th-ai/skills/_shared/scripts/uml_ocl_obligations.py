"""Read-only, source-identity-preserving UML OCL execution scope inventory.

Class invariants, operation body conditions, operation pre/postconditions and
derived features are different obligations. Cataloguing does not execute them.
"""
from collections import defaultdict
from pathlib import Path
from standards import Incomplete,XMI,safe_xml,sha
from standards_coverage import source_identities
ROOT=Path(__file__).resolve().parents[1]
SOURCE_SHA256='e8166c91f51b8a0c015a90101b83d2249d03252e9f9a500a6511654347804f21'

def execution_inventory(data=None,file='uml-2.5.1/UML.xmi'):
    normative=data is None
    if normative:
        data=(ROOT/'standards/sources'/file).read_bytes()
        if sha(data)!=SOURCE_SHA256:raise Incomplete('UML OCL scope source fingerprint changed; review required')
    root=safe_xml(data);source={'file':file,'sha256':sha(data)};identities=source_identities(source,root)
    by_id=defaultdict(list)
    for node in root.iter():
        identity=node.get('{'+XMI+'}id') if isinstance(node.tag,str) else None
        if identity:by_id[identity].append(node)
    def reference(native_id):
        candidates=[identities[node] for node in by_id.get(native_id,())]
        return {'native_id':native_id,'status':'resolved-unique-source-reference' if len(candidates)==1 else
                'ambiguous-source-reference' if candidates else 'missing-source-reference',
                'candidates':candidates,'resolved_target':candidates[0] if len(candidates)==1 else None}
    rules=[];operations=[];derived=[]
    for operation in root.iter('ownedOperation'):
        owner=operation.getparent();references=[]
        if operation.get('bodyCondition'):references.append({'role':'operation-body-condition',**reference(operation.get('bodyCondition'))})
        for kind in ('precondition','postcondition'):
            for child in operation.findall(kind):references.append({'role':'operation-'+kind,**reference(child.get('{'+XMI+'}idref'))})
        operations.append({'native_id':operation.get('{'+XMI+'}id'),'name':operation.get('name'),
            'context':owner.get('name'),'source_identity':identities[operation],'context_identity':identities[owner],
            'constraint_references':references,'is_query':operation.get('isQuery','false')=='true',
            'independent_execution_status':'not-certified','declared_parameter_ids':[p.get('{'+XMI+'}id') for p in operation.findall('ownedParameter')]})
    for rule in root.iter('ownedRule'):
        body=rule.findtext('specification/body')
        if not body or rule.findtext('specification/language')!='OCL':continue
        owner=rule.getparent();operation=owner.tag=='ownedOperation';context=owner.getparent() if operation else owner
        roles=[]
        if operation:
            record=next(row for row in operations if row['source_identity']['key']==identities[owner]['key'])
            roles=[r['role'] for r in record['constraint_references'] if r['native_id']==rule.get('{'+XMI+'}id')]
        rules.append({'native_id':rule.get('{'+XMI+'}id'),'name':rule.get('name'),'context':context.get('name'),
            'kind':'operation-owned-constraint' if operation else 'class-invariant','declared_roles':roles,
            'source_identity':identities[rule],'owner_identity':identities[owner],'context_identity':identities[context],
            'original_body':body,'original_body_sha256':sha(body.encode()),
            'source_native_id_ambiguous':len(by_id[rule.get('{'+XMI+'}id')])>1,
            'execution_status':'not-executed-by-catalog'})
    for feature in root.iter('ownedAttribute'):
        if feature.get('isDerived')!='true':continue
        owner=feature.getparent()
        candidates=[identities[op] for op in owner.findall('ownedOperation') if op.get('name')==feature.get('name')]
        derived.append({'native_id':feature.get('{'+XMI+'}id'),'name':feature.get('name'),'context':owner.get('name'),
            'source_identity':identities[feature],'owner_identity':identities[owner],
            'is_derived_union':feature.get('isDerivedUnion','false')=='true','same_owner_name_query_candidates':candidates,
            'query_resolution':None,'candidate_basis':'same owning source classifier/name only; no equivalence or resolution inferred',
            'independent_execution_status':'not-certified'})
    vertex=next((c for c in root.iter('packagedElement') if c.get('name')=='Vertex' and c.get('{'+XMI+'}type')=='uml:Class'),None)
    inherited=[];todo=[vertex] if vertex is not None else [];visited=set()
    while todo:
        cls=todo.pop();key=identities[cls]['key']
        if key in visited:continue
        visited.add(key)
        for feature in cls.findall('ownedAttribute'):
            if feature.get('name')=='redefinedElement':
                inherited.append({'context':'Vertex','name':'redefinedElement','kind':'inherited-derived-feature',
                    'source_identity':identities[feature],'declaring_classifier':cls.get('name'),
                    'is_derived':feature.get('isDerived')=='true','is_derived_union':feature.get('isDerivedUnion')=='true',
                    'operation_parameter_resolution':None})
        for generalization in cls.findall('generalization'):
            candidates=by_id.get(generalization.get('general'),())
            if len(candidates)==1:todo.extend(candidates)
    summary={'class_ocl_invariants':sum(r['kind']=='class-invariant' for r in rules),
        'operation_owned_ocl_constraints':sum(r['kind']=='operation-owned-constraint' for r in rules),
        'operation_declarations':len(operations),'operation_body_condition_references':sum(r['role']=='operation-body-condition' for op in operations for r in op['constraint_references']),
        'operation_precondition_references':sum(r['role']=='operation-precondition' for op in operations for r in op['constraint_references']),
        'operation_postcondition_references':sum(r['role']=='operation-postcondition' for op in operations for r in op['constraint_references']),
        'derived_features':len(derived),'duplicate_xml_native_id_groups':sum(len(nodes)>1 for nodes in by_id.values()),
        'independent_operation_and_derived_scope':'incomplete','catalog_execution_count':0,
        'body_conditions_are_postcondition_declarations':False,
        'full_standard_acceptance':False}
    return {'schema_version':'uml-ocl-execution-inventory/1','source':source,'source_fingerprint_verified':normative,
        'summary':summary,'ocl_rules':rules,'operations':operations,'derived_features':derived,
        'vertex_inherited_features':inherited,'source_bytes_preserved':True,
        'scope':'Source catalog only. The mapped validator executes class invariants and one bounded finite-Integer query adapter; it does not certify operation pre/postconditions, body-condition equivalence or derived-feature equivalence.'}
