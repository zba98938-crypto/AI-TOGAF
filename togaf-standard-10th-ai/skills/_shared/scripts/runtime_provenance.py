"""Fingerprint the executable generation/validation dependency set."""
import hashlib
import ast
from pathlib import Path

def fingerprints(root=None):
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    scripts=root/'scripts'
    names={'generate.py','profile_render.py','table_expression.py','view_semantics.py',
           'analyze.py','deliverable_assembly.py','render.mjs','registry.py',
           'validate.py','business_policy.py','analysis_binding.py','runtime_provenance.py',
           'organization_derivation.py','metadata_coverage_binding.py','section_evidence.py','governance_check_binding.py',
           'execution_batch.py', 'field_counterexamples.py', 'qianlin_casework.py',
           'evidence_integrity.py', 'render_deliverable_pages.py', 'print_deliverable_pdf.mjs',
           'browser_resolver.mjs', 'raster_tiles.mjs', 'check_geometry.mjs', 'diagram_quality.mjs', 'layered_topology.mjs', 'package_links.py',
           'business_exercise.py', 'bpmn_semantics.py', 'standards.py', 'uml_backend.py', 'UmlValidate.java', 'closure_source_coverage.py',
           'analysis_evidence.py', 'analysis_projection_binding.py'}
    names.update(p.name for pattern in ('*_render.py','*_analysis.py') for p in scripts.glob(pattern))
    # Local imports are executable semantics, including imports inside functions.
    # Follow code dependencies, not arbitrary documentation or historical reports.
    pending = list(names)
    while pending:
        path = scripts / pending.pop()
        if not path.is_file() or path.suffix != '.py':
            continue
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            modules = ([node.module] if isinstance(node, ast.ImportFrom) and node.module
                       else [a.name for a in node.names] if isinstance(node, ast.Import) else [])
            for module in modules:
                name = module.split('.')[0] + '.py'
                if name not in names and (scripts / name).is_file():
                    names.add(name)
                    pending.append(name)
    paths={scripts/name for name in names}
    # Runtime data is executable semantics too: changing a source checklist or
    # template can change outputs without changing any Python module.
    for pattern in ('templates/*.json','references/source-tables/*.json','references/g249/*.json',
                    'references/source-structures/G249-*.json','schemas/*.json',
                    'capability-addenda/field-contracts*.json'):
        paths.update(root.glob(pattern))
    paths.update(root/name for name in ('relationships.json','package-lock.json','requirements.txt',
      'capability-addenda/deliverable-assembly-rules.json','assets/fonts/NotoSansSC.ttf',
      'standards/bpmn-rule-basis.json'))
    return {str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)}
