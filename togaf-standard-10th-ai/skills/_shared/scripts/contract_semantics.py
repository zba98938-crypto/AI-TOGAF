"""Semantic assertions for contract-level counterexamples.

Each check enforces one assertion code that the counterexample registry names but
that no validator emitted yet. Two design rules keep these honest:

1. A check fires only when the model actually contains the relevant object type.
   A model that does not cover the subject is not a failure.
2. Attribute names come from the registered contracts, not from intuition. Where a
   contract allows several spellings, all are accepted, because rejecting a valid
   model would be worse than missing one bad field.

These are structural honesty checks, not business correctness judgements.
"""


def _text(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple)):
        return len(value) > 0
    return value is not None


def _first(attrs, *names):
    for name in names:
        if name in attrs and attrs[name] not in (None, "", []):
            return attrs[name]
    return None


def _entities(entities, type_name):
    return [e for e in entities.values() if e.get("type") == type_name]


def semantic_issues(model, entities, relationships):
    issues = []

    def issue(code, identity, message, level="error"):
        issues.append({"level": level, "code": code, "id": identity, "message": message})

    # --- reject-unsupported-commitment ---------------------------------------
    # A framework touchpoint that claims an actual commitment must carry evidence.
    for entity in _entities(entities, "guide:framework_touchpoint"):
        attrs = entity.get("attributes") or {}
        commitment = _first(attrs, "actual_commitment", "commitment", "touchpoint")
        evidence = _first(attrs, "commitment_evidence", "evidence_refs", "evidence")
        if _text(commitment) and not _text(evidence):
            issue("reject-unsupported-commitment", entity["id"],
                  "声明了框架接触的承诺，但没有承诺证据。")

    # --- factor-evidence-gap -------------------------------------------------
    for entity in _entities(entities, "guide:implementation_factor"):
        attrs = entity.get("attributes") or {}
        if not _text(_first(attrs, "evidence_refs", "evidence", "source", "observation")):
            issue("factor-evidence-gap", entity["id"], "实施因素缺少来源或证据。")

    # --- all-staff-coverage-gap ----------------------------------------------
    # Only applies when a skill matrix declares a population and holders.
    matrix_skills = _entities(entities, "skill")
    populations = []
    holders = set()
    for entity in matrix_skills:
        attrs = entity.get("attributes") or {}
        population = _first(attrs, "population", "required_headcount")
        if isinstance(population, (int, float)) and population > 0:
            populations.append((entity["id"], population, attrs))
        holder = _first(attrs, "holder_ref", "holder", "person_ref")
        if _text(holder):
            holders.add(holder if isinstance(holder, str) else str(holder))
    for identity, population, attrs in populations:
        covered = _first(attrs, "covered_count", "assessed_count")
        if isinstance(covered, (int, float)) and covered < population:
            issue("all-staff-coverage-gap", identity,
                  f"技能矩阵仅覆盖 {covered} / {population} 人。")

    # --- authorization-not-ready ---------------------------------------------
    for entity in _entities(entities, "guide:project_authorization"):
        attrs = entity.get("attributes") or {}
        preconditions = attrs.get("preconditions") or []
        if not isinstance(preconditions, list):
            continue
        unaccepted = [p for p in preconditions
                      if isinstance(p, dict) and p.get("accepted") is False]
        status = str(_first(attrs, "authorization_status", "status") or "").lower()
        started = str(_first(attrs, "implementation_status") or "").lower()
        if unaccepted and (status in {"approved", "granted"} or started in {"in-progress", "realized"}):
            issue("authorization-not-ready", entity["id"],
                  "前置条件尚未接受，但授权或执行已记录为通过。")

    # --- closure-products-not-accepted ---------------------------------------
    for entity in _entities(entities, "guide:closure_record"):
        attrs = entity.get("attributes") or {}
        products = attrs.get("products")
        if not isinstance(products, list):
            continue
        unaccepted = [p for p in products if isinstance(p, dict) and p.get("accepted") is False]
        reason = str(attrs.get("closure_reason") or "").lower()
        if unaccepted and reason in {"completed", "completed-accepted", "closed"}:
            issue("closure-products-not-accepted", entity["id"],
                  f"收尾标记为完成，但有 {len(unaccepted)} 项成果未被接受。")

    # --- criterion-result-contradiction --------------------------------------
    for entity in _entities(entities, "criterion"):
        attrs = entity.get("attributes") or {}
        required = attrs.get("required_total")
        observed = attrs.get("observed_total")
        result = str(_first(attrs, "result", "verdict") or "").lower()
        try:
            if required is not None and observed is not None:
                if float(observed) < float(required) and result in {"pass", "passed", "met"}:
                    issue("criterion-result-contradiction", entity["id"],
                          "判据判定为通过，但观察值低于要求值。")
        except (TypeError, ValueError):
            pass

    # --- dependency-cycle -----------------------------------------------------
    graph = {}
    cycle_types = {"depends_on", "guide:backlog_depends_on", "g20f:story-depends-on",
                   "business_dependency", "external_dependency"}
    for relation in relationships.values():
        if relation["type"] in cycle_types:
            graph.setdefault(relation["source"], set()).add(relation["target"])
    visiting, visited, reported = set(), set(), set()

    def walk(node, stack):
        if node in visiting:
            if node not in reported:
                reported.add(node)
                start = stack.index(node) if node in stack else 0
                issue("dependency-cycle", node,
                      "依赖存在环：" + " → ".join(stack[start:] + [node]))
            return True
        if node in visited:
            return False
        visiting.add(node)
        for neighbor in graph.get(node, ()):
            if walk(neighbor, stack + [neighbor]):
                visiting.discard(node)
                return True
        visiting.discard(node)
        visited.add(node)
        return False

    for node in list(graph):
        walk(node, [node])

    # --- dual-entry-trace-gap -------------------------------------------------
    for entity in _entities(entities, "guide:dual_entry_opportunity"):
        attrs = entity.get("attributes") or {}
        use_side = _first(attrs, "use_id", "use_ref", "purpose_ref")
        infra_side = _first(attrs, "infrastructure_id", "infrastructure_ref")
        if not (_text(use_side) or _text(infra_side)):
            issue("dual-entry-trace-gap", entity["id"],
                  "双入口机会既未连接用途侧也未连接基础设施侧。")

    # --- learning-evidence-gap -----------------------------------------------
    for entity in _entities(entities, "guide:sustainability_learning"):
        attrs = entity.get("attributes") or {}
        if not _text(_first(attrs, "evidence_refs", "evidence", "current_evidence",
                            "application_check")):
            issue("learning-evidence-gap", entity["id"], "学习项缺少效果证据。")

    # --- missing-project-contingency -----------------------------------------
    # Only an object that carries an estimate value can be missing contingency.
    # The sufficiency checklist asks questions about estimates; it is not itself one.
    for entity in _entities(entities, "guide:estimate_check"):
        attrs = entity.get("attributes") or {}
        carries_estimate = any(key in attrs for key in
                               ("estimate", "estimate_value", "value", "effort", "investment"))
        if not carries_estimate:
            continue
        has_contingency = _text(_first(attrs, "contingency", "fallback", "tolerance"))
        limitation = str(_first(attrs, "limitation", "status") or "").lower()
        if not has_contingency and ("assumption" in limitation or "假设" in limitation
                                    or attrs.get("has_contingency") is False):
            issue("missing-project-contingency", entity["id"],
                  "估算声明为假设，但未给出应急或容差安排。")

    # --- procurement-transparency-gap ----------------------------------------
    for entity in _entities(entities, "guide:sustainable_procurement"):
        attrs = entity.get("attributes") or {}
        if not _text(_first(attrs, "lifecycle_evidence", "evidence_refs", "evidence")):
            issue("procurement-transparency-gap", entity["id"],
                  "采购要求缺少可核的透明度或生命周期证据。")

    # --- carbon-data-metadata-gap --------------------------------------------
    for entity in _entities(entities, "guide:carbon_reference_data"):
        attrs = entity.get("attributes") or {}
        required = {
            "边界": _first(attrs, "lifecycle_boundary", "boundary"),
            "单位": _first(attrs, "unit"),
            "因子来源": _first(attrs, "source_locator", "source_version", "source"),
        }
        missing = [name for name, value in required.items() if not _text(value)]
        if missing:
            issue("carbon-data-metadata-gap", entity["id"],
                  "碳数据缺少元数据：" + ",".join(missing))

    # --- scope3-subset-exceeds-total -----------------------------------------
    for entity in _entities(entities, "environment_measure"):
        attrs = entity.get("attributes") or {}
        total = _first(attrs, "scope_total", "total_value")
        subset = _first(attrs, "scope_subset", "subset_value")
        try:
            if total is not None and subset is not None and float(subset) > float(total):
                issue("scope3-subset-exceeds-total", entity["id"],
                      "子集数值超过所属总量。")
        except (TypeError, ValueError):
            pass

    # --- unsourced-maturity-rating -------------------------------------------
    for entity in _entities(entities, "maturity_observation"):
        attrs = entity.get("attributes") or {}
        rating = _first(attrs, "level", "rating")
        evidence = _first(attrs, "evidence", "evidence_refs")
        if rating is not None and not _text(evidence):
            issue("unsourced-maturity-rating", entity["id"], "成熟度评级没有证据来源。")

    return issues
