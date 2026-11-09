"""Add an explicit, checkable assertion code to each early case's counterexample section.

The 19 pre-existing cases described their counterexamples in prose only. Prose cannot
be checked, so each bullet gets exactly one code chosen from codes that already exist
in executable checkers, the registry counterexample contracts, or the declared
assertion-code table. Nothing is invented, and no wording is claimed as new evidence.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / 'examples/method-cases'

# method -> [(matcher substring in the existing bullet, assertion code, short reason)]
PLAN = {
    'scenario-elicitation': [
        ('只收到sc-1时不能输出', 'missing-evidence', '单一受访者观点不足以支撑“必须重写”的结论'),
        ('重名‘接单’', 'duplicate-id', '两个不同流程共用一个名称而未分配稳定标识'),
    ],
    'option-weighted-decision': [
        ('金额', 'measurement-basis-gap', '偏好评分不能由原始金额直接代入'),
    ],
    'business-risk-assessment': [
        ('概率', 'measurement-evidence-gap', '在缺少概率与损失证据时给出定量等级'),
    ],
    'business-impact-method': [
        ('200次报名', 'measurement-basis-gap', '用业务量乘任意单价折算每小时损失'),
        ('发生概率80%', 'measurement-evidence-gap', '影响严重度不能推出事件发生概率'),
    ],
    'acmm-maturity-assessment': [
        ('等级', 'unsourced-maturity-rating', '成熟度等级缺少评据来源'),
    ],
    'dtra-readiness-method': [
        ('评分', 'unsourced-maturity-rating', '就绪度评分缺少证据来源'),
    ],
    'capability-decomposition-method': [
        ('串成子能力', 'core-vocabulary-override', '把流程步骤当作能力分解'),
        ('视觉分组', 'undefined-entity-type', '把视觉分组当作可继承的父能力'),
    ],
    'capability-instance-gap-method': [
        ('子能力', 'core-vocabulary-override', '把语境实现误作能力分解'),
        ('同名库存实例', 'duplicate-id', '同名不同范围的实例未按范围区分标识'),
    ],
    'value-stream-definition-method': [
        ('企业价值链区块', 'core-vocabulary-override', '把价值链阶段直接当作顾客价值流阶段'),
        ('横向排列', 'missing-evidence', '排版顺序不构成价值递进的证据'),
    ],
    'metadata-requirement-method': [
        ('强制交付', 'core-vocabulary-override', '把参考资产全集当作本项目强制范围'),
        ('同名术语', 'missing-evidence', '同名不构成同义证据'),
    ],
    'metadata-integration-tradeoff': [
        ('统一式=拉取', 'undefined-entity-type', '把两种不同维度的分类混为一谈'),
        ('静默画一条pull箭头', 'missing-evidence', '在禁止代理的生产环境中虚构拉取路径'),
    ],
    'mdm-identity-analysis': [
        ('相似度0.8', 'measurement-evidence-gap', '自动合并阈值缺少证据与复核'),
        ('Centralized', 'core-vocabulary-override', '把不同来源的术语当作同义'),
    ],
    'bi-transition-method': [
        ('四张不同颜色图', 'missing-evidence', '图示本身不证明可迁移'),
        ('参考目标', 'approval-without-evidence', '参考目标被当作采购或退役决定'),
    ],
    'microservice-boundary-method': [
        ('七个页面', 'core-vocabulary-override', '把界面页面当作业务服务边界'),
        ('相同数据库表被多个服务直接写', 'relation-endpoint-type', '共享写权破坏声明的数据所有权'),
        ('没有失败恢复证据', 'missing-evidence', '缺少演练证据即宣称已实现且可靠'),
    ],
    'architecture-role-skill-assessment': [
        ('平均2.33', 'unsourced-maturity-rating', '平均值没有组织成熟度含义'),
        ('0.1全时当量', 'measurement-basis-gap', '等级相同不等于可交付当量相同'),
        ('证书名称', 'missing-evidence', '证书不能替代行为证据'),
    ],
    'architecture-project-scheduling': [
        ('删除C→D依赖', 'missing-evidence', '删去真实依赖会让评审排在研究完成前'),
        ('A依赖E产生循环', 'cycle', '依赖成环时不得输出看似完整的排程'),
    ],
    'environment-lifecycle-accounting': [
        ('历史', 'measurement-basis-gap', '历史排放不因退役从本期抹去'),
    ],
    'sustainability-option-review': [
        ('−390', 'measurement-basis-gap', '静默改写来源数值会丢失来源冲突'),
        ('抵消积分', 'unsourced-maturity-rating', '未声明方法即用抵消抵减新增制造'),
    ],
    'reference-model-tailoring': [
        ('四参考域', 'core-vocabulary-override', '把参考域直接等同四架构域'),
        ('参考服务框', 'undefined-entity-type', '把参考结构当作现有组织或部署事实'),
        ('没有找到本地对应项', 'missing-evidence', '未找到不等于不适用'),
    ],
}


def main():
    changed = []
    for method, rules in PLAN.items():
        path = CASES / (method + '.md')
        text = path.read_text()
        if '## 反例与输入不足' not in text:
            raise SystemExit('no counterexample section: ' + method)
        start = text.index('## 反例与输入不足')
        end = text.index('## 评审记录', start)
        body = text[start:end]
        if '预期 `' in body:
            continue
        lines = body.split('\n')
        out = []
        used = set()
        for line in lines:
            stripped = line.strip()
            target = next((rule for rule in rules
                           if rule[0] in line and rule[1] not in used), None)
            if stripped and not stripped.startswith('#') and target is None and rules and not used:
                target = rules[0]
            if stripped and not stripped.startswith('#') and target is not None:
                needle, code, why = target
                used.add(code)
                if stripped.startswith('-'):
                    line = stripped.rstrip('。') + '。预期 `%s`（%s）。' % (code, why)
                else:
                    line = '- **错误做法**：' + stripped.rstrip('。') + '。预期 `%s`（%s）。' % (code, why)
            out.append(line)
        text = text[:start] + '\n'.join(out) + text[end:]
        path.write_text(text)
        changed.append((method, sorted(used)))
    print(json.dumps({'patched': len(changed), 'detail': changed}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
