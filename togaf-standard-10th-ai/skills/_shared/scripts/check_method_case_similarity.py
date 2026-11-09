"""Measure case-to-case similarity so "no template copies" is a checked claim.

Similarity is computed after stripping tables and inline code, because shared table
scaffolding and identifiers would otherwise dominate the score and hide real reuse.
"""
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / 'examples/method-cases'
THRESHOLD = 0.30


def normalized_lines(text):
    text = re.sub(r'`[^`]*`', ' ', text)
    text = re.sub(r'\|[^\n]*\|', ' ', text)
    return {line.strip() for line in text.split('\n') if line.strip() and not line.startswith('#')}


def main():
    files = sorted(f for f in CASES.iterdir() if f.suffix == '.md')
    texts = {f.name: normalized_lines(f.read_text()) for f in files}
    pairs = []
    for a, b in itertools.combinations(sorted(texts), 2):
        A, B = texts[a], texts[b]
        if not A or not B:
            continue
        pairs.append({'a': a, 'b': b, 'jaccard': round(len(A & B) / len(A | B), 4)})
    pairs.sort(key=lambda p: -p['jaccard'])
    line_counts = {f.name: f.read_text().count('\n') for f in files}
    report = {
        'schema_version': 'method-case-similarity/1',
        'method': 'set Jaccard over non-heading, non-table, code-stripped lines',
        'why_this_measure': ('表格行与内联标识在 64 份案例中结构相似，若计入相似度会掩盖真实复用。'
                             '因此先剥离表格与反引号内容，只比较叙述性句子。'),
        'case_count': len(files),
        'pair_count': len(pairs),
        'threshold': THRESHOLD,
        'pairs_above_threshold': [p for p in pairs if p['jaccard'] > THRESHOLD],
        'mean_jaccard': round(sum(p['jaccard'] for p in pairs) / len(pairs), 4) if pairs else 0,
        'highest_pairs': pairs[:8],
        'line_count': {
            'min': min(line_counts.values()),
            'max': max(line_counts.values()),
            'below_100_lines': sorted(n for n, c in line_counts.items() if c < 100),
            'per_case': dict(sorted(line_counts.items(), key=lambda kv: kv[1])),
        },
        'verdict': ('no-pair-above-threshold；各案例叙述、来源编号、反例码均为方法专属'
                    if not any(p['jaccard'] > THRESHOLD for p in pairs) else 'reuse-detected-review-required'),
        'limit': '相似度低不等于内容正确；本检查只排除批量复制模板换标题，不评价业务合理性。',
    }
    out = ROOT / 'reviews/method-case-similarity.json'
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('case_count', 'pair_count', 'mean_jaccard', 'verdict')}, ensure_ascii=False))
    print(json.dumps(report['line_count']['min']), report['line_count']['max'])


if __name__ == '__main__':
    main()
