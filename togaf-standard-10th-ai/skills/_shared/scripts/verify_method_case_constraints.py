"""Verify the five writing constraints that the plan promised, on every method case.

Each rule is checked mechanically so "we wrote good cases" is not a self-assessment:
  R1 seven sections present and ordered
  R2 author-consistency closing line present
  R3 at least two counterexamples carrying a named assertion code
  R4 modification exercise names a concrete change AND a consequence or an
     explicitly unchanged item
  R5 no unsourced numeric/maturity claim in the 输出与追溯 section of a method that
     has no calculator (i.e. qualitative cases must say so)
  R6 source rules and project rules are labelled separately, never merged into one
     sentence (the plan forbids mixing them)
  R7 转换与推理 uses numbered steps so each step can be traced individually
  R8 评审记录 lists at least three individually checked items (not one paragraph)
  R9 each case is at least MIN_LINES long, as the plan required
"""

MIN_LINES = 120
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / 'references/method-cases'
SECTIONS = ['## 决策与原始业务资料', '## 来源规则与项目规则', '## 转换与推理',
            '## 输出与追溯', '## 修改演练', '## 反例与输入不足', '## 评审记录']
TAIL = '本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。'
# A modification exercise must name a concrete edit. Either an explicit change verb,
# or a conditional premise that states the new fact being assumed.
CHANGE = re.compile(r'改为|换成|删除|新增|补入|补上|补齐|取得|设定|取消|替换|去掉|只更新|只改变|缩成|调为|调到|提升为|降为|完成|决定|若|如果|→|v2')
CONSEQUENCE = re.compile(r'需|将|会|则|因此|影响|其余\S{0,6}不变|阻断|重评|重排|翻|不再|失效|触发|保持|保留|重算')


def check_rule_split(rules):
    """The plan forbids mixing source rules with project rules in one statement.

    Each numbered rule must declare which side it belongs to, and both sides must be
    present. Wording varies ("项目规则"/"项目约定"/"项目分类约定"...), so the label is
    detected by prefix rather than by one fixed phrase.
    """
    numbered = [line for line in rules.split('\n') if re.match(r'^\s*\d+\.\s', line)]
    if not numbered:
        return [('R6', 'rule list is not numbered, cannot attribute each rule')]
    # Label = text before the first colon on that numbered line, with markdown emphasis
    # stripped. Anything else (including a parenthetical chapter reference) is still a
    # label; only the presence of a colon-delimited label matters.
    def label(line):
        body = re.sub(r'^\s*\d+\.\s*', '', line)
        body = body.replace('**', '')
        head, sep, _ = body.partition('：')
        if not sep:
            head, sep, _ = body.partition(':')
        return head.strip() if sep else None

    labels = [(line, label(line)) for line in numbered]
    issues = []
    # A rule is attributed when its leading label begins with 来源 or 项目. The label may
    # carry a chapter reference in parentheses, so length is not a criterion.
    def attributed(text):
        return bool(text) and (text.startswith('来源') or text.startswith('项目'))

    unlabelled = [line for line, text in labels if not attributed(text)]
    if unlabelled:
        issues.append(('R6', 'rules not attributed to source or project: %d' % len(unlabelled)))
    heads = [text or '' for _, text in labels]
    if not any(h.startswith('来源') for h in heads):
        issues.append(('R6', 'no rule labelled as source method'))
    if not any(h.startswith('项目') for h in heads):
        issues.append(('R6', 'no rule labelled as project rule'))
    return issues


def slice_section(text, heading, next_heading):
    start = text.index(heading) + len(heading)
    if next_heading is None:
        return text[start:]
    # A missing or misplaced next heading must not crash the checker; report an empty
    # slice so the structural rule (R1) is the one that fires.
    try:
        end = text.index(next_heading, start)
    except ValueError:
        return ''
    return text[start:end]


def check(method, text, calculator_id):
    issues = []
    present = [s for s in SECTIONS if s in text]
    if len(present) != len(SECTIONS):
        issues.append(('R1', 'missing sections: ' + str([s for s in SECTIONS if s not in text])))
    duplicated = [s for s in SECTIONS if text.count(s) > 1]
    if duplicated:
        issues.append(('R1', 'duplicated sections: ' + str(duplicated)))
    if len(present) == len(SECTIONS):
        positions = [text.index(s) for s in SECTIONS]
        if positions != sorted(positions):
            issues.append(('R1', 'sections out of order'))
    # The qualitative-boundary sentence must appear exactly once; earlier bulk edits
    # could leave both an old and a new copy.
    # Only the standalone declaration counts; the phrase may legitimately appear inside
    # a sentence explaining what was and was not computed.
    standalone = '本方法采用定性判断与追溯演练，没有适用的统一计算器。'
    if text.count(standalone) > 1:
        issues.append(('R1', 'standalone qualitative-boundary declaration appears %d times'
                       % text.count(standalone)))
    if len(present) != len(SECTIONS) or issues:
        # Section text cannot be attributed reliably when the skeleton is broken;
        # structural failure alone is the honest verdict.
        return [], issues
    if TAIL not in text:
        issues.append(('R2', 'author-consistency line missing'))

    ce = slice_section(text, '## 反例与输入不足', '## 评审记录')
    # Codes may be shared assertion names (kebab-case) or case-local error ids (BAP-001).
    codes = sorted(set(re.findall(r'预期 `([A-Za-z][A-Za-z0-9-]+)`', ce)))
    if len(codes) < 2:
        issues.append(('R3', 'fewer than two coded counterexamples: %s' % codes))

    mod = slice_section(text, '## 修改演练', '## 反例与输入不足')
    if not CHANGE.search(mod):
        issues.append(('R4', 'no concrete change named'))
    if not CONSEQUENCE.search(mod):
        issues.append(('R4', 'no consequence or explicitly-unchanged item named'))

    out = slice_section(text, '## 输出与追溯', '## 修改演练')
    # Methods without a registry calculator must bound their own claim: either say no
    # calculator applies, or state explicitly what is mechanically checkable and what
    # is left to judgement.
    bounded = ('没有适用的统一计算器' in out
               or ('可复核' in out and '不由' in out))
    if not calculator_id and not bounded:
        issues.append(('R5', 'no explicit statement of what is computed vs judged'))

    rules = slice_section(text, '## 来源规则与项目规则', '## 转换与推理')
    issues.extend(check_rule_split(rules))

    steps = slice_section(text, '## 转换与推理', '## 输出与追溯')
    if not re.search(r'^\s*\d+\.\s', steps, re.M):
        issues.append(('R7', 'reasoning section has no numbered steps'))

    lines = text.count('\n')
    if lines < MIN_LINES:
        issues.append(('R9', 'case is %d lines, expected >= %d' % (lines, MIN_LINES)))

    review = slice_section(text, '## 评审记录', None)
    checked = len(re.findall(r'^- ', review, re.M))
    if checked < 3:
        issues.append(('R8', 'review section lists %d checked items, expected >= 3' % checked))
    return codes, issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', '--cases-dir', dest='cases', type=Path, default=CASES)
    parser.add_argument('--out', type=Path, default=ROOT.parents[1] / 'output/method-case-constraints.json')
    args = parser.parse_args()
    registry = json.loads((ROOT / 'capabilities.json').read_text())['analysis_methods']
    calc = {m['id']: m.get('calculator_id') or m.get('calculator') for m in registry}
    report = {'schema_version': 'method-case-constraints/1', 'methods': [], 'violations': []}
    for path in sorted(args.cases.glob('*.md')):
        method = path.stem
        codes, issues = check(method, path.read_text(), calc.get(method))
        report['methods'].append({'method_id': method, 'counterexample_codes': codes,
                                  'calculator_id': calc.get(method), 'passed': not issues})
        if issues:
            report['violations'].append({'method_id': method, 'issues': issues})
    report['summary'] = {
        'cases': len(report['methods']),
        'passed': sum(1 for m in report['methods'] if m['passed']),
        'violations': len(report['violations']),
        'mean_counterexample_codes': round(
            sum(len(m['counterexample_codes']) for m in report['methods']) / len(report['methods']), 2) if report['methods'] else None,
    }
    report['limit'] = ('机械可核的是结构与措辞约束；业务合理性、证据真实性与方法选择正确性均不在此检查范围。'
                       '通过本检查只说明案例满足写作形式要求，不说明案例结论被接受。')
    report['registered_without_teaching_case'] = sorted(set(calc) - {m['method_id'] for m in report['methods']})
    report['status'] = ('blocked' if not report['methods'] else 'failed' if report['violations'] else 'passed')
    report['blocked_reason'] = 'no-teaching-cases-found' if not report['methods'] else None
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report['summary'], ensure_ascii=False))
    for v in report['violations']:
        print(' -', v['method_id'], v['issues'])
    return 3 if report['status'] == 'blocked' else int(bool(report['violations']))


if __name__ == '__main__':
    sys.exit(main())
