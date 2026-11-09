"""Index scoped chapter demonstrations without closing whole-deliverable gates."""
import hashlib
import json
from pathlib import Path
from runtime_provenance import fingerprints
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'examples/section-evidence'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    facts=json.loads((HERE/'section-facts.json').read_text());execution=json.loads((HERE/'execution.json').read_text())
    checks=json.loads((HERE/'output-checks.json').read_text())
    assert execution['completed'] and all(r['matched_expected'] for r in execution['runs'])
    assert checks['passed'] and len(checks['checks'])==34
    for name,digest in execution['input_hashes'].items():assert sha(HERE/name)==digest,name
    paths=['examples/section-evidence/'+name for name in ['section-facts.json','analysis.md','raw-materials.md','baseline-model.json','modified-model.json','execution.json','output-checks.json']]
    paths+=['reviews/section-round4-contract.json','reviews/section-round5-cross-review.json']
    for variant in ['baseline','modified']:
        path=HERE/(variant+'-output/manifest.json');manifest=json.loads(path.read_text())
        assert manifest['implementation_dependencies_sha256']==fingerprints(ROOT)
        paths.append(str(path.relative_to(ROOT)))
    evidence=[{'path':path,'sha256':sha(ROOT/path)} for path in paths]
    rows=[]
    for section in facts['sections']:
        rows.append({'id':section['id'],'deliverable_id':section['deliverable_id'],'title':section['title'],
          'facts':'examples/section-evidence/section-facts.json#'+section['id'],
          'baseline_model':'examples/section-evidence/baseline-model.json',
          'modified_model':'examples/section-evidence/modified-model.json',
          'execution':'examples/section-evidence/execution.json','cross_review':'reviews/section-round5-cross-review.json',
          'content_status':'partial-with-explicit-gaps','complete_deliverable':False})
    index={'schema_version':'section-demonstrations/1.0','registry_sha256':sha(ROOT/'capabilities.json'),
      'runtime_fingerprints':fingerprints(ROOT),'evidence':evidence,'sections':rows,
      'limit':'独立项目17章增量附录；不能替代其他项目的同名章节、原全量示例或完整交付物验收。'}
    (ROOT/'reviews/section-case-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'section_demonstrations':len(rows),'limited_deliverable_families':len({r['deliverable_id'] for r in rows})}))
if __name__=='__main__':main()
