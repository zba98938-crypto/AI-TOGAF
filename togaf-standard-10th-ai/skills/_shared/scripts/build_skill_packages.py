#!/usr/bin/env python3
"""Generate the five reference files each skill package needs, from registry data.

Files written per skill, all under <skill>/references/:
  contracts.md        every owned work product's fields and attribute semantics
  checks.md           machine-checkable assertions (with codes) vs human judgement
  counterexamples.md  each work product's stated wrong input and expected code
  decisions.md        skeleton with TODOs; the only hand-written part
  handoff.md          computed from who produces which entity type for whom

Nothing here is invented prose: every line traces to a registry field. If a field
is missing the script fails rather than writing a placeholder, because a placeholder
would look like coverage.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path
from field_contracts import resolve_semantics, validate_contracts, _spec_problems, apply_contract_overlay

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT.parent

def read(path):
    return json.loads(Path(path).read_text())


def entity_producers(caps):
    """Which skill introduces each entity type, for the handoff computation."""
    producers = defaultdict(set)
    for wp in caps["work_products"]:
        for entity in wp.get("entity_types") or []:
            producers[entity].add(wp["owner"])
    for profile in caps["profiles"]:
        for entity in profile.get("entity_types") or []:
            producers[entity].add(profile["owner"])
    for method in caps["analysis_methods"]:
        for entity in method.get("entity_types") or []:
            producers[entity].add(method["owner"])
    return producers


def render_contracts(skill, products, caps):
    lines = [f"# {skill} 字段契约", "",
             "本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，"
             "字段名与注册表逐字一致。",
             "",
             "本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。",
             ""]
    total_fields = 0
    for wp in products:
        attrs = wp.get("required_attributes") or {}
        semantics = wp.get("attribute_semantics") or {}
        fields = wp.get("fields") or []
        total_fields += len(fields)
        lines.append(f"## {wp.get('name_zh') or wp['id']}")
        lines.append("")
        lines.append(f"- `id`：`{wp['id']}`")
        lines.append(f"- 英文名：{wp.get('name_en') or '未填写'}")
        lines.append(f"- 决策问题：{wp.get('decision') or '未填写'}")
        lines.append(f"- 主责技能：`{wp['owner']}`")
        lines.append(f"- 来源：{'；'.join(wp.get('source_refs') or [])}")
        lines.append(f"- 定义状态：`{wp.get('definition_status') or '未声明'}`")
        inputs = [item if isinstance(item, str) else json.dumps(item, ensure_ascii=False)
                  for item in (wp.get("required_inputs") or [])]
        lines.append(f"- 必需输入：{', '.join(inputs) or '未声明'}")
        optional = [item if isinstance(item, str) else json.dumps(item, ensure_ascii=False)
                    for item in (wp.get("optional_inputs") or [])]
        if optional:
            lines.append(f"- 可选输入：{', '.join(optional)}")
        lines.append(f"- 缺输入策略：{wp.get('missing_input_policy') or '未声明'}")
        lines.append(f"- 字段总数：{len(fields)}；对象类型：{', '.join(wp.get('entity_types') or [])}")
        lines.append(f"- 关系类型：{', '.join(wp.get('relationship_types') or []) or '未声明'}")
        deliverables = wp.get("related_deliverables") or []
        if deliverables:
            lines.append(f"- 关联交付物：{', '.join('`' + d + '`' for d in deliverables)}")
        for did, context in wp.get('related_deliverable_context', {}).items():
            lines.append(f"- `{did}`适用边界：{context}")
        lines.append("")
        steps = wp.get("analysis_steps") or wp.get("analysis") or []
        if steps:
            lines.append("### 分析步骤")
            lines.append("")
            for index, step in enumerate(steps, 1):
                lines.append(f"{index}. {step}")
            lines.append("")
        for entity, entity_fields in attrs.items():
            lines.append(f"### `{entity}` 必填字段（{len(entity_fields)}）")
            lines.append("")
            lines.append("| 字段 | 含义 | 取值规则 |")
            lines.append("| --- | --- | --- |")
            for field in entity_fields:
                sem = resolve_semantics(wp, entity, field)
                if not all(sem.get(k) for k in ("meaning", "value_rule", "definition_origin")):
                    raise ValueError(f"字段契约不完整：{wp['id']}.{entity}.{field}")
                meaning = sem["meaning"].replace("|", "\\|")
                rule = sem["value_rule"].replace("|", "\\|")
                if sem.get("value_schema"):
                    rule += "；类型约束：`" + json.dumps(sem['value_schema'], ensure_ascii=False, separators=(',', ':')).replace('|', '\\|') + "`"
                origin = sem["definition_origin"]
                lines.append(f"| `{field}` | {meaning} | {rule}（来源：`{origin}`） |")
            lines.append("")
        if not attrs:
            lines.append("本工作产品未声明 `required_attributes`；其字段约束须由 owner 补齐后才能机器校验。")
            lines.append("")
        extras = [f for f in fields if f not in {x for v in attrs.values() for x in v}]
        if extras:
            lines.append(f"其余字段（{len(extras)}）：" + "、".join(f"`{f}`" for f in extras))
            lines.append("")
        outputs = wp.get("output") or []
        if outputs:
            lines.append("### 输出")
            lines.append("")
            for item in outputs:
                lines.append(f"- {item}")
            lines.append("")
        relation_semantics = wp.get("relation_semantics")
        if relation_semantics:
            lines.append(f"### 关系语义\n\n{relation_semantics}\n")
    lines.append("---")
    lines.append("")
    lines.append(f"合计 {len(products)} 个工作产品，{total_fields} 个字段。")
    return "\n".join(lines) + "\n"


def render_checks(skill, products, methods):
    machine, human, misreadings = [], [], []
    for item in products + methods:
        for spec in item.get('check_specs', []):
            problems = _spec_problems(spec, item)
            if problems:
                raise ValueError(f"{item['id']}.{spec.get('id')}: {problems}")
            if spec['mode'] == 'machine':
                condition = ', '.join(spec['applies_to']['entity_types'])
                machine.append((item['id'], spec['text'], spec['code'], spec['executor'], condition))
            else:
                human.append((item['id'], spec['text'], spec['mode']))
        for text in item.get('misreadings', []):
            misreadings.append((item['id'], text))

    def dedupe(rows):
        seen, out = set(), []
        for row in rows:
            if row[:2] in seen:
                continue
            seen.add(row[:2])
            out.append(row)
        return out

    machine, human = dedupe(machine), dedupe(human)
    misreadings = dedupe(misreadings)
    lines = [f"# {skill} 检查清单", "",
             "由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。",
             "机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。",
             "字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。",
             ""]
    lines.append(f"## 机器可判（{len(machine)} 条）")
    lines.append("")
    if machine:
        lines.append("| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |")
        lines.append("| --- | --- | --- | --- | --- |")
        for identity, text, code, executor, condition in machine:
            lines.append(f"| `{identity}` | {text.replace('|', chr(92) + '|')} | `{code}` | `{executor}` | 模型含类型：{condition} |")
    else:
        lines.append("本技能暂无可映射到断言码的检查。")
    lines.append("")
    lines.append(f"## 需人工判（{len(human)} 条）")
    lines.append("")
    if human:
        lines.append("| 对象 | 检查 | 判定方式 |")
        lines.append("| --- | --- | --- |")
        for identity, text, mode in dedupe(human):
            lines.append(f"| `{identity}` | {text.replace('|', chr(92) + '|')} | `{mode}`：责任方依据证据判断，不得由生成结果替代 |")
    else:
        lines.append("本技能全部检查均可机器判定。")
    lines.append("")
    lines.append(f"## 常见误读（{len(misreadings)} 条）")
    lines.append("")
    if misreadings:
        lines.append("这些是注册表登记过的读图或读模型错误，读产出前先核对。")
        lines.append("")
        for identity, text in misreadings:
            lines.append(f"- `{identity}`：{text}")
    else:
        lines.append("本技能未登记误读。")
    return "\n".join(lines) + "\n"


def render_counterexamples(skill, products, methods):
    lines = [f"# {skill} 反例集", "",
             "以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。",
             "历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。",
             ""]
    lines.append("## 工作产品反例")
    lines.append("")
    lines.append("| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |")
    lines.append("| --- | --- | --- | --- | --- |")
    missing = []
    for wp in products:
        ce = wp.get("counterexample")
        if not ce:
            missing.append(wp["id"])
            continue
        original = (ce.get("original_expected_text") or "").replace("|", chr(92) + "|")
        lines.append(f"| `{wp['id']}` | {ce.get('input','').replace('|', chr(92)+'|')} "
                     f"| `{ce.get('expected','missing-evidence')}` "
                     f"| {ce.get('why','').replace('|', chr(92)+'|')} | {original or '—'} |")
    lines.append("")
    lines.append("## 工作产品修改示例")
    lines.append("")
    lines.append("| 工作产品 | 变更 | 预期后果 |")
    lines.append("| --- | --- | --- |")
    for wp in products:
        me = wp.get("modification_example")
        if not me:
            continue
        lines.append(f"| `{wp['id']}` | {me.get('change','').replace('|', chr(92)+'|')} "
                     f"| {me.get('expected','').replace('|', chr(92)+'|')} |")
    lines.append("")
    lines.append("## 方法反例")
    lines.append("")
    lines.append("| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |")
    lines.append("| --- | --- | --- | --- | --- |")
    for method in methods:
        ce = method.get("counterexample")
        if not ce:
            continue
        original = (ce.get("original_expected_text") or "").replace("|", chr(92) + "|")
        lines.append(f"| `{method['id']}` | {ce.get('input','').replace('|', chr(92)+'|')} "
                     f"| `{ce.get('expected','missing-evidence')}` "
                     f"| {ce.get('why','').replace('|', chr(92)+'|')} | {original or '—'} |")
    if missing:
        lines.append("")
        lines.append(f"缺反例的工作产品（须在 addenda 中补齐）：{', '.join(missing)}")
    lines.append("")
    lines.append("## 判定说明")
    lines.append("")
    lines.append("- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。")
    lines.append("- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。")
    lines.append("- 通过反例测试不等于业务正确，只说明错误输入没有被放行。")
    return "\n".join(lines) + "\n"


def render_decisions_skeleton(skill, products, methods):
    lines = [f"# {skill} 判断规则", "",
             "本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。",
             "",
             "每条须包含：判据（什么条件下适用）、反例（什么时候不该用）、影响的制品或字段。",
             "至少 5 条，否则该技能不算完成。",
             ""]
    for index in range(1, 6):
        lines.append(f"## 判断 {index}：TODO")
        lines.append("")
        lines.append("- 判据：TODO")
        lines.append("- 反例：TODO")
        lines.append("- 影响：TODO")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"涉及工作产品：{len(products)} 个；方法：{len(methods)} 个。")
    return "\n".join(lines) + "\n"


def render_handoff(skill, products, profiles, methods, producers):
    own_entities = set()
    for item in products + profiles + methods:
        own_entities |= set(item.get("entity_types") or [])

    incoming, outgoing = [], []
    for entity in sorted(own_entities):
        others = sorted(producers.get(entity, set()) - {skill})
        if others:
            incoming.append((entity, others))

    consumers = defaultdict(set)
    for entity, owners in producers.items():
        for owner in owners:
            if owner != skill:
                consumers[entity].add(owner)
    for entity in sorted(own_entities):
        targets = sorted(consumers.get(entity, set()))
        if targets:
            outgoing.append((entity, targets))

    lines = [f"# {skill} 交接说明", "",
             "由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。",
             "交接只是依赖关系，不代表对方已接受或已完成。",
             ""]
    lines.append(f"## 入向（本技能需要、由他方生产，{len(incoming)} 项）")
    lines.append("")
    if incoming:
        lines.append("| 对象类型 | 生产方技能 |")
        lines.append("| --- | --- |")
        for entity, owners in incoming:
            lines.append(f"| `{entity}` | {', '.join(owners)} |")
    else:
        lines.append("本技能不依赖他方生产的对象类型。")
    lines.append("")
    lines.append(f"## 出向（本技能涉及、被他方使用，{len(outgoing)} 项）")
    lines.append("")
    if outgoing:
        lines.append("| 对象类型 | 使用方技能 |")
        lines.append("| --- | --- |")
        for entity, targets in outgoing:
            lines.append(f"| `{entity}` | {', '.join(targets)} |")
    else:
        lines.append("本技能的产出暂未被其他技能引用。")
    lines.append("")
    lines.append("## 交接条件")
    lines.append("")
    lines.append("接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为"
                 "「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。")
    lines.append("")
    lines.append("## 本技能产出的工作产品")
    lines.append("")
    if products:
        lines.append("| 工作产品 | 关联交付物 | 对象类型 |")
        lines.append("| --- | --- | --- |")
        for wp in products:
            deliverable_list = ", ".join("`" + d + "`" for d in (wp.get("related_deliverables") or [])) or "—"
            entities = ", ".join("`" + e + "`" for e in (wp.get("entity_types") or [])) or "—"
            lines.append(f"| `{wp['id']}` | {deliverable_list} | {entities} |")
    else:
        lines.append("本技能不直接产出工作产品。")
    lines.append("")
    lines.append("## 本技能负责的分析方法")
    lines.append("")
    if methods:
        lines.append("| 方法 | 输出工作产品 | 实现状态 |")
        lines.append("| --- | --- | --- |")
        for method in methods:
            outputs = ", ".join("`" + o + "`" for o in (method.get("output_work_products") or [])) or "—"
            lines.append(f"| `{method['id']}` | {outputs} | `{method.get('implementation_status') or '未声明'}` |")
    else:
        lines.append("本技能在注册表中没有独立分析方法，结论通过工作产品契约表达。")
    return "\n".join(lines) + "\n"


ROUTING_MARKER = "## 任务路由表"


def render_routing(skill, profiles, products):
    """Insert a decision-to-view routing table, derived from profile names.

    The table answers "which view do I read for this question" without requiring the
    reader to scan 50 profile files. It is inserted once and replaced on re-run.
    """
    lines = [ROUTING_MARKER, "",
             f"本技能注册 {len(profiles)} 个视图规范、{len(products)} 个工作产品。"
             "先按决策问题选一行，再读对应规范；不要一次生成全部。",
             "",
             "| 决策问题 | 建议规范 | 制品族 |",
             "| --- | --- | --- |"]
    by_family = defaultdict(list)
    for profile in profiles:
        by_family[profile["artifact_id"]].append(profile)
    for family, group in sorted(by_family.items()):
        source_products = [p for p in products if p.get("artifact_id") == family or p["id"] == family]
        question = ""
        if source_products:
            question = source_products[0].get("decision") or ""
        if not question:
            question = group[0].get("name_zh") or group[0].get("name") or family
        compat = [p["id"] for p in group if p["id"].startswith("compat-")]
        specific = [p["id"] for p in group if not p["id"].startswith("compat-")]
        suggested = specific or compat
        lines.append(f"| {question.replace('|', chr(92)+'|')} "
                     f"| {', '.join('`'+p+'`' for p in suggested[:3])} | `{family}` |")
    lines.append("")
    lines.append("**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，"
                 "直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。")
    lines.append("")
    return "\n".join(lines) + "\n"


def insert_routing(skill, text, block):
    """Replace an existing routing block or append one before the package link."""
    if ROUTING_MARKER in text:
        head, _, tail = text.partition(ROUTING_MARKER)
        # Drop only the old generated block: it ends with the "何时不用本技能" paragraph.
        # Hand-written lines after it (e.g. source contract links) are kept.
        remainder = tail
        index = remainder.find("\n## ")
        section = remainder if index < 0 else remainder[:index + 1]
        after = remainder[index + 1:] if index >= 0 else ""
        end = section.find("**何时不用本技能**")
        kept = ""
        if end >= 0:
            line_end = section.find("\n", end)
            kept = section[line_end + 1:] if line_end >= 0 else ""
        if not kept.strip():
            return head + block + "\n" + after  # unchanged behaviour when nothing hand-written follows
        return head + block + "\n\n" + kept.lstrip("\n") + after
    index = text.find("\n按需入口：")
    if index < 0:
        return text.rstrip() + "\n\n" + block
    return text[:index] + "\n" + block + text[index:]


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", help="comma separated skill names")
    parser.add_argument("--references-only", action="store_true",
                        help="only write four generated reference docs; never decisions, SKILL.md or shared reports")
    args = parser.parse_args()

    caps = apply_contract_overlay(read(ROOT / "capabilities.json"))
    problems = validate_contracts(caps)
    if problems:
        raise ValueError('字段/检查契约无效：' + '; '.join(problems[:20]))
    producers = entity_producers(caps)
    only = set(args.only.split(",")) if args.only else None

    skills = sorted({p["owner"] for p in caps["profiles"]}
                    | {w["owner"] for w in caps["work_products"]}
                    | {m["owner"] for m in caps["analysis_methods"]})

    report = {}
    for skill in skills:
        if only and skill not in only:
            continue
        products = [w for w in caps["work_products"] if w["owner"] == skill]
        profiles = [p for p in caps["profiles"] if p["owner"] == skill]
        methods = [m for m in caps["analysis_methods"] if m["owner"] == skill]
        base = SKILLS / skill / "references"
        files = {
            "contracts.md": render_contracts(skill, products, caps),
            "checks.md": render_checks(skill, products, methods),
            "counterexamples.md": render_counterexamples(skill, products, methods),
            "handoff.md": render_handoff(skill, products, profiles, methods, producers),
        }
        decisions = base / "decisions.md"
        if not decisions.exists() and not args.references_only:
            files["decisions.md"] = render_decisions_skeleton(skill, products, methods)
        sizes = {}
        for name, text in files.items():
            sizes[name] = len(text.encode())
            if not args.dry_run:
                write(base / name, text)
        report[skill] = {"files": sizes,
                         "contracts_bytes": sizes["contracts.md"],
                         "products": len(products), "methods": len(methods)}
        # SKILL.md routing table, inserted idempotently.
        skill_md = SKILLS / skill / "SKILL.md"
        if skill_md.is_file() and not args.references_only:
            original = skill_md.read_text()
            updated = insert_routing(skill, original, render_routing(skill, profiles, products))
            if updated != original and not args.dry_run:
                skill_md.write_text(updated)
        print(f"{skill:38} contracts={sizes['contracts.md']:6}B checks={sizes['checks.md']:6}B "
              f"cex={sizes['counterexamples.md']:6}B handoff={sizes['handoff.md']:6}B"
              + ("" if decisions.exists() else "  [decisions skeleton written]"))

    if not args.dry_run and not args.references_only:
        out = ROOT / "reviews/comparison/skill-packages-generation.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"generated": report,
                                   "notice": "decisions.md requires hand writing; skeletons are marked TODO"},
                                  ensure_ascii=False, indent=2) + "\n")
        print("wrote", out)


if __name__ == "__main__":
    main()
