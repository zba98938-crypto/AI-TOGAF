#!/usr/bin/env python3
"""Executable synthetic recovery and evidence-bound risk calculations.

No production connections or authority are provided by this tool.
"""
import argparse
import hashlib
import json
import os
import shutil
import sqlite3
import time
from decimal import Decimal
from datetime import date
from pathlib import Path


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def recovery(directory, fault='none'):
    if fault not in ('none', 'invalid-restore', 'restore-failure', 'inconsistent', 'settlement-failure'):
        raise ValueError('unknown recovery fault')
    out = Path(directory)
    out.mkdir(parents=True, exist_ok=False)
    log = []
    def event(action, **detail):
        row = {'action': action, 'wall_ns': time.time_ns(), 'monotonic_ns': time.monotonic_ns(), **detail}
        log.append(row)
        with (out / 'execution.jsonl').open('a') as stream:
            stream.write(json.dumps(row, ensure_ascii=False) + '\n');stream.flush();os.fsync(stream.fileno())
        return row
    db = out / 'live.sqlite'
    expected = {i: [i, 10 + i % 7, i * 101] for i in range(1, 1001)}
    with sqlite3.connect(db) as connection:
        connection.executescript('CREATE TABLE orders(id INTEGER PRIMARY KEY, quantity INTEGER NOT NULL, cents INTEGER NOT NULL); CREATE TABLE applied(event_id TEXT PRIMARY KEY, payload_sha256 TEXT NOT NULL);')
        connection.executemany('INSERT INTO orders VALUES (?,?,?)', expected.values());connection.commit()
        with sqlite3.connect(out / 'snapshot.sqlite') as snapshot:
            connection.backup(snapshot)
    snapshot_sha = sha(out / 'snapshot.sqlite')
    save(out / 'restore-point.json', {'file': 'snapshot.sqlite', 'sha256': snapshot_sha, 'classification': 'synthetic'})
    event('snapshot-created', sha256=snapshot_sha)
    events = []
    for i in range(1, 101):
        item = {'event_id': 'EV-' + str(i), 'order_id': i, 'quantity_delta': i % 3 + 1, 'cents_delta': i * 7, 'committed_ns': time.time_ns()}
        events.append(item)
        if i % 10 == 0:events.append(dict(item))
        expected[i][1] += item['quantity_delta'];expected[i][2] += item['cents_delta']
    with (out / 'events.jsonl').open('w') as stream:
        for item in events:stream.write(json.dumps(item) + '\n')
        stream.flush();os.fsync(stream.fileno())
    def apply_events(connection):
        duplicates = 0
        for line in (out / 'events.jsonl').read_text().splitlines():
            item = json.loads(line)
            digest = hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest()
            existing = connection.execute('SELECT payload_sha256 FROM applied WHERE event_id=?', (item['event_id'],)).fetchone()
            if existing:
                if existing[0] != digest:raise ValueError('conflicting duplicate event')
                duplicates += 1;continue
            connection.execute('INSERT INTO applied VALUES (?,?)', (item['event_id'], digest))
            connection.execute('UPDATE orders SET quantity=quantity+?, cents=cents+? WHERE id=?', (item['quantity_delta'], item['cents_delta'], item['order_id']))
        connection.commit()
        return duplicates
    with sqlite3.connect(db) as connection:
        apply_events(connection)
        connection.execute('UPDATE orders SET quantity=quantity+999');connection.commit()
    cutoff_ns = time.time_ns()
    started = event('failure-detected-writes-frozen', durable_log_sha256=sha(out / 'events.jsonl'), recovery_cutoff_ns=cutoff_ns)
    if fault == 'invalid-restore':
        with (out / 'snapshot.sqlite').open('ab') as stream:stream.write(b'corrupt')
    result = {'classification': 'synthetic-executable-exercise', 'fault': fault, 'production_proof': False,
              'business_acceptance': 'pending', 'recovery_success': False, 'observed_rto_seconds': None,
              'observed_rpo_seconds': None, 'external_operation': 'local-test-double-only'}
    if sha(out / 'snapshot.sqlite') != snapshot_sha:
        event('invalid-restore-point-abort');result['terminal'] = 'abort-and-escalate'
    elif fault == 'restore-failure':
        # Actual failed filesystem operation, never a supplied success observation.
        try:shutil.copyfile(out / 'snapshot.sqlite', out / 'missing-parent/live.sqlite')
        except OSError as exc:event('restore-operation-failed', error=type(exc).__name__)
        result['terminal'] = 'manual-compensation-and-escalate'
    else:
        shutil.copyfile(out / 'snapshot.sqlite', out / 'restore.tmp')
        os.replace(out / 'restore.tmp', db)
        event('database-restored')
        with sqlite3.connect(db) as connection:
            duplicates = apply_events(connection)
            # Replay twice, including persistent restart of the connection.
        with sqlite3.connect(db) as connection:
            second_duplicates = apply_events(connection)
            if fault == 'inconsistent':
                connection.execute('UPDATE orders SET cents=cents+1 WHERE id=1');connection.commit()
            actual = [list(row) for row in connection.execute('SELECT id,quantity,cents FROM orders ORDER BY id')]
            applied = connection.execute('SELECT count(*) FROM applied').fetchone()[0]
        expected_rows = list(expected.values())
        save(out / 'independent-expected.json', expected_rows);save(out / 'actual-restored.json', actual)
        matched = actual == expected_rows and applied == 100
        event('reconciliation-completed', matched=matched, applied_events=applied,
              duplicate_events_ignored=duplicates, second_replay_duplicates=second_duplicates)
        result.update(reconciled=matched, applied_events=applied, second_replay_duplicates=second_duplicates)
        if not matched:result['terminal'] = 'manual-compensation-and-escalate'
        elif fault == 'settlement-failure':
            # Persist a non-rollbackable test-double side effect and retain it.
            save(out / 'external-settlement-test-double.json', {'sent': True, 'confirmed': False, 'automatic_undo': False})
            event('irreversible-test-double-unconfirmed-manual-reconciliation')
            result['terminal'] = 'manual-reconciliation-no-automatic-undo'
        else:
            finished = event('service-restored')
            result.update(terminal='service-restored', recovery_success=True,
                          observed_rto_seconds=(finished['monotonic_ns'] - started['monotonic_ns']) / 1e9,
                          observed_rpo_seconds=0, rpo_measurement='all committed events through recovery cutoff were replayed; zero missing committed events')
    result['evidence'] = {p.name: sha(p) for p in out.iterdir() if p.is_file()}
    save(out / 'result.json', result)
    return result


def risk_analysis(raw):
    required = ('period_start', 'period_end', 'as_of', 'policy_version', 'policy_authority', 'approval_authority', 'scales', 'control_evidence', 'scenarios')
    missing = [k for k in required if not raw.get(k)]
    if missing:raise ValueError('insufficient risk inputs: ' + ', '.join(missing))
    if raw.get('classification') != 'synthetic' or raw.get('real_approval') is not False:
        raise ValueError('this exercise requires explicitly synthetic, unapproved inputs')
    start, end, asof = [date.fromisoformat(raw[k]) for k in ('period_start', 'period_end', 'as_of')]
    if not start <= end <= asof or (asof - end).days > 90:raise ValueError('invalid or stale policy period')
    scales = raw['scales']
    for field in ('likelihood_definitions', 'impact_definitions'):
        if set(scales.get(field, {})) != set(map(str, range(1, 6))) or not all(scales[field].values()):
            raise ValueError('full scale definitions required: ' + field)
    appetite, tolerance = scales['appetite'], scales['tolerance']
    if not 0 < appetite < tolerance <= 25:raise ValueError('invalid risk thresholds')
    controls = {r['id']: r for r in raw['control_evidence']}
    if len(controls)!=len(raw['control_evidence']):raise ValueError('duplicate control evidence ID')
    rows = []
    def score(likelihood, impact):
        if any(type(x) is not int or x not in range(1, 6) for x in (likelihood, impact)):
            raise ValueError('ordinal risk inputs must be integers 1..5')
        return likelihood * impact
    for scenario in raw['scenarios']:
        control = controls.get(scenario.get('control_evidence_id'))
        if not control or control.get('classification') != 'synthetic' or not control.get('observations') or not scenario.get('owner'):
            raise ValueError('scenario requires responsible owner and control evidence')
        if (control.get('period_start'),control.get('period_end'))!=(raw['period_start'],raw['period_end']):
            raise ValueError('control evidence period mismatch')
        gross = score(scenario['likelihood'], scenario['impact'])
        residual = score(scenario['residual_likelihood'], scenario['residual_impact'])
        if scenario.get('residual_score', residual) != residual:raise ValueError('residual score mismatch')
        decision = 'within-appetite' if residual <= appetite else 'escalate' if residual <= tolerance else 'do-not-enter-change'
        rows.append({'id': scenario['id'], 'gross_score': gross, 'residual_score': residual, 'disposition': decision,
                     'control_evidence_id': control['id'], 'owner': scenario['owner'], 'approval_status': 'candidate'})
    values = raw.get('boundary_scores', [])
    if len(values)!=5 or any(type(v) is not int or not 1<=v<=25 for v in values) or not (values[0]<appetite==values[1]<values[2]<tolerance==values[3]<values[4]):
        raise ValueError('five authored boundary scores must cover below/equal/between/equal/above')
    samples=raw.get('boundary_cases',[])
    if len(samples)!=5:raise ValueError('five boundary likelihood/impact observations required')
    calculated=[score(v['likelihood'],v['impact']) for v in samples]
    if calculated!=values:raise ValueError('authored boundary scores do not match calculated ordinal products')
    boundaries = [{'likelihood':sample['likelihood'],'impact':sample['impact'],'score': s, 'disposition': 'within-appetite' if s <= appetite else 'escalate' if s <= tolerance else 'do-not-enter-change'} for sample,s in zip(samples,calculated)]
    return {'classification': 'synthetic-analysis', 'policy_version': raw['policy_version'], 'scenarios': rows,
            'boundary_checks': boundaries, 'production_proof': False, 'risk_acceptance': 'pending',
            'input_sha256': hashlib.sha256(json.dumps(raw, ensure_ascii=False, sort_keys=True).encode()).hexdigest()}


def quality_analysis(raw):
    """Assess an authored observation ledger without inventing source records."""
    required=('period_start','period_end','as_of','policy_version','quality_policy','observations','defects','reconciliation','source')
    if any(not raw.get(k) for k in required):raise ValueError('insufficient quality inputs')
    if raw.get('classification')!='synthetic' or raw.get('real_approval') is not False:raise ValueError('synthetic unapproved inputs required')
    start,end,asof=[date.fromisoformat(raw[k]) for k in ('period_start','period_end','as_of')]
    if not start<=end<=asof or (asof-end).days>90:raise ValueError('invalid or stale quality period')
    if raw.get('conflicting_policy'):raise ValueError('conflicting policy requires authority resolution')
    policy=raw['quality_policy'];observed=raw['observations'];defects=raw['defects']
    if not policy.get('owner') or not policy.get('uniqueness'):raise ValueError('policy owner and uniqueness key required')
    counts=[observed.get(k) for k in ('records','valid','missing_master_key','duplicate_event')]
    if any(type(v) is not int or v<0 for v in counts) or counts[0]<=0:raise ValueError('invalid observed counts')
    total,valid,missing,duplicates=counts
    if valid+missing+duplicates!=total:raise ValueError('observation reconciliation mismatch')
    if raw['reconciliation'].get('valid+quarantined')!=total or raw['reconciliation'].get('denominator')!=total:raise ValueError('denominator mismatch')
    ids=[d.get('id') for d in defects]
    if not all(ids) or len(ids)!=len(set(ids)) or len(defects)!=missing+duplicates:raise ValueError('defect ledger mismatch')
    for kind,count in [('missing_master_key',missing),('duplicate_event',duplicates)]:
        if sum(d.get('kind')==kind for d in defects)!=count:raise ValueError('defect category count mismatch')
    if any(not d.get('owner') or d.get('disposition')!='quarantine' for d in defects):raise ValueError('owned quarantine disposition required')
    threshold=Decimal(str(policy['valid_ratio']));ratio=Decimal(valid)/Decimal(total)
    if not 0<=threshold<=1 or type(policy.get('max_null_key')) is not int or policy['max_null_key']<0:raise ValueError('invalid quality thresholds')
    ratio_pass=ratio>=threshold;key_pass=missing<=policy['max_null_key']
    return {'classification':'synthetic-analysis','policy_version':raw['policy_version'],'period_start':raw['period_start'],'period_end':raw['period_end'],
            'valid_ratio':str(ratio),'ratio_threshold':str(threshold),'ratio_pass':ratio_pass,'key_pass':key_pass,
            'overall_quality_gate':'pass' if ratio_pass and key_pass else 'fail','quarantined':len(defects),
            'defects':defects,'source':raw['source'],'production_proof':False,'business_acceptance':'pending',
            'input_sha256':hashlib.sha256(json.dumps(raw,ensure_ascii=False,sort_keys=True).encode()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['recovery', 'risk', 'quality'])
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--fault', default='none', choices=['none','invalid-restore','restore-failure','inconsistent','settlement-failure'])
    args = parser.parse_args()
    if args.out.exists():parser.error('--out must be new')
    try:
        if args.command == 'recovery':result = recovery(args.out, args.fault)
        else:
            if not args.input:parser.error('--input required for analysis')
            result = (risk_analysis if args.command=='risk' else quality_analysis)(json.loads(args.input.read_text()));args.out.mkdir(parents=True);save(args.out/'result.json',result)
    except (ValueError, OSError) as exc:parser.exit(3, str(exc)+'\n')
    print(json.dumps(result, ensure_ascii=False))
    return 0 if args.command != 'recovery' or result['recovery_success'] else 1


if __name__ == '__main__':raise SystemExit(main())
