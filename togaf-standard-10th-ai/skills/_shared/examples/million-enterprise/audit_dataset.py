#!/usr/bin/env python3
"""Independently query persisted ledgers and test deliberate corruptions in memory."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import time

HERE = Path(__file__).resolve().parent

CHECKS = {
    'invalid_order_quantity_or_price': 'SELECT COUNT(*) FROM orders WHERE quantity_kg<=0 OR price_cents_per_kg<=0 OR discount_bps<0 OR discount_bps>10000',
    'order_price_arithmetic': 'SELECT COUNT(*) FROM orders WHERE net_cents != (quantity_kg*price_cents_per_kg*(10000-discount_bps))/10000',
    'unsupported_plant_product': 'SELECT COUNT(*) FROM orders o LEFT JOIN plant_products p ON o.plant_id=p.plant_id AND o.product_id=p.product_id WHERE p.plant_id IS NULL',
    'shipment_quantity_status': '''SELECT COUNT(*) FROM orders o LEFT JOIN shipment_totals s USING(order_id)
        WHERE COALESCE(s.qty,0)>o.quantity_kg OR (o.status='fulfilled' AND COALESCE(s.qty,0)!=o.quantity_kg)
        OR (o.status='partial' AND (COALESCE(s.qty,0)<=0 OR s.qty>=o.quantity_kg))
        OR (o.status IN ('open','cancelled') AND COALESCE(s.qty,0)!=0)''',
    'shipment_temporal_order': '''SELECT COUNT(*) FROM shipments s JOIN orders o USING(order_id)
        WHERE s.shipped_day<o.order_day OR s.event_received_day<s.shipped_day''',
    'return_quantity': '''SELECT COUNT(*) FROM shipments s JOIN return_totals r USING(shipment_id)
        WHERE r.qty>s.quantity_kg OR r.qty<=0''',
    'return_date_and_credit': '''SELECT COUNT(*) FROM returns r JOIN shipments s USING(shipment_id) JOIN orders o USING(order_id)
        WHERE r.returned_day<s.shipped_day OR r.credit_net_cents!=(r.quantity_kg*o.price_cents_per_kg*(10000-o.discount_bps))/10000
        OR r.credit_tax_cents!=(r.credit_net_cents*13)/100 OR r.credit_gross_cents!=r.credit_net_cents+r.credit_tax_cents''',
    'invoice_shipped_amount': '''SELECT COUNT(*) FROM invoices i JOIN orders o USING(order_id) JOIN shipment_totals s USING(order_id)
        WHERE i.net_cents!=(s.qty*o.price_cents_per_kg*(10000-o.discount_bps))/10000
        OR i.tax_cents!=(i.net_cents*13)/100 OR i.gross_cents!=i.net_cents+i.tax_cents''',
    'invoice_temporal_order': '''SELECT COUNT(*) FROM invoices i JOIN shipment_totals s USING(order_id)
        WHERE i.invoice_day<s.last_day OR i.due_day<i.invoice_day''',
    'missing_or_spurious_invoice': '''SELECT COUNT(*) FROM orders o LEFT JOIN shipment_totals s USING(order_id)
        LEFT JOIN invoices i USING(order_id) WHERE (COALESCE(s.qty,0)>0 AND i.invoice_id IS NULL)
        OR (COALESCE(s.qty,0)=0 AND i.invoice_id IS NOT NULL)''',
    'payment_amount': '''SELECT COUNT(*) FROM payments p JOIN invoices i USING(invoice_id)
        LEFT JOIN credits_by_order c USING(order_id) WHERE p.amount_cents!=i.gross_cents-COALESCE(c.gross,0)
        OR p.amount_cents<0 OR p.paid_day<i.invoice_day''',
    'production_inventory': '''SELECT COUNT(*) FROM production_daily WHERE opening_kg<0 OR produced_kg<0 OR closing_kg<0
        OR closing_kg!=opening_kg+produced_kg-shipped_kg''',
    'production_continuity': '''SELECT COUNT(*) FROM (
        SELECT opening_kg,LAG(closing_kg) OVER(PARTITION BY plant_id,product_id ORDER BY production_day) prev
        FROM production_daily) WHERE prev IS NOT NULL AND prev!=opening_kg''',
    'production_shipment_ledger': '''SELECT COUNT(*) FROM production_daily p LEFT JOIN plant_shipments s
        ON p.plant_id=s.plant_id AND p.product_id=s.product_id AND p.production_day=s.day
        WHERE p.shipped_kg!=COALESCE(s.qty,0)''',
    'production_return_ledger': '''SELECT COUNT(*) FROM production_daily p LEFT JOIN plant_returns s
        ON p.plant_id=s.plant_id AND p.product_id=s.product_id AND p.production_day=s.day
        WHERE p.returned_kg!=COALESCE(s.qty,0)''',
    'production_energy_bounds': '''SELECT COUNT(*) FROM production_daily d JOIN products p USING(product_id)
        WHERE ABS((d.electric_wh-250000)-(d.produced_kg*p.energy_wh_per_kg))>d.produced_kg*p.energy_wh_per_kg*0.030001+1''',
    'source_event_temporal_order': 'SELECT COUNT(*) FROM source_events WHERE received_day<event_day',
    'source_event_missing_order': "SELECT COUNT(*) FROM source_events e LEFT JOIN orders o ON e.entity_id=o.order_id WHERE e.entity_type='order' AND o.order_id IS NULL",
    'source_event_missing_shipment': "SELECT COUNT(*) FROM source_events e LEFT JOIN shipments s ON e.entity_id=s.shipment_id WHERE e.entity_type='shipment' AND s.shipment_id IS NULL",
    'source_event_missing_return': "SELECT COUNT(*) FROM source_events e LEFT JOIN returns r ON e.entity_id=r.return_id WHERE e.entity_type='return' AND r.return_id IS NULL",
    'source_event_missing_invoice': "SELECT COUNT(*) FROM source_events e LEFT JOIN invoices i ON e.entity_id=i.invoice_id WHERE e.entity_type='invoice' AND i.invoice_id IS NULL",
}

TEMP_SQL = '''
CREATE TEMP TABLE shipment_totals AS SELECT order_id,SUM(quantity_kg) qty,MAX(shipped_day) last_day FROM shipments GROUP BY order_id;
CREATE UNIQUE INDEX temp.ix_st ON shipment_totals(order_id);
CREATE TEMP TABLE return_totals AS SELECT shipment_id,SUM(quantity_kg) qty FROM returns GROUP BY shipment_id;
CREATE UNIQUE INDEX temp.ix_rt ON return_totals(shipment_id);
CREATE TEMP TABLE credits_by_order AS SELECT s.order_id,SUM(r.credit_gross_cents) gross FROM returns r JOIN shipments s USING(shipment_id) GROUP BY s.order_id;
CREATE UNIQUE INDEX temp.ix_co ON credits_by_order(order_id);
CREATE TEMP TABLE plant_shipments AS SELECT o.plant_id,o.product_id,s.shipped_day day,SUM(s.quantity_kg) qty FROM shipments s JOIN orders o USING(order_id) GROUP BY 1,2,3;
CREATE UNIQUE INDEX temp.ix_ps ON plant_shipments(plant_id,product_id,day);
CREATE TEMP TABLE plant_returns AS SELECT o.plant_id,o.product_id,r.returned_day day,SUM(r.quantity_kg) qty FROM returns r JOIN shipments s USING(shipment_id) JOIN orders o USING(order_id) GROUP BY 1,2,3;
CREATE UNIQUE INDEX temp.ix_pr ON plant_returns(plant_id,product_id,day);
'''


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def audit(path):
    start = time.perf_counter()
    conn = sqlite3.connect(f'file:{Path(path).resolve()}?mode=ro', uri=True)
    conn.execute('PRAGMA temp_store=MEMORY')
    conn.executescript(TEMP_SQL)
    checks = {}
    for name, sql in CHECKS.items():
        tick = time.perf_counter()
        value = conn.execute(sql).fetchone()[0]
        checks[name] = {'violations': value, 'passed': value == 0, 'sql': sql, 'seconds': round(time.perf_counter() - tick, 3)}
        print(name, value, flush=True)
    fk = conn.execute('PRAGMA foreign_key_check').fetchall()
    integrity = conn.execute('PRAGMA integrity_check').fetchone()[0]
    identity = conn.execute('SELECT COUNT(*),MIN(order_id),MAX(order_id),COUNT(DISTINCT order_id) FROM orders').fetchone()
    counts = {r[0]: conn.execute(f'SELECT COUNT(*) FROM "{r[0]}"').fetchone()[0]
              for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()}
    missing_days = conn.execute('''SELECT COUNT(*) FROM plant_shipments s LEFT JOIN production_daily p
        ON s.plant_id=p.plant_id AND s.product_id=p.product_id AND s.day=p.production_day WHERE p.plant_id IS NULL''').fetchone()[0]
    checks['production_missing_shipment_day'] = {'violations': missing_days, 'passed': missing_days == 0}
    conn.close()
    return {'is_example': True, 'passed': all(c['passed'] for c in checks.values()) and not fk and integrity == 'ok'
            and identity[0] == identity[3] == identity[2] and identity[1] == 1,
            'checks': checks, 'foreign_key_violations': fk[:20], 'integrity_check': integrity,
            'order_id_scan': dict(zip(['rows', 'minimum', 'maximum', 'distinct'], identity)), 'counts': counts,
            'database_sha256': file_hash(path), 'seconds': round(time.perf_counter() - start, 3),
            'limits': 'Independent cross-ledger reconciliation of saved synthetic data; not physical process validation or true enterprise acceptance.'}


def negatives(path):
    """Use small real rows from the full DB, independent literal corruptions and SQL.

    No update touches the persistent baseline database. These are real executed
    counterexamples, not a list of desired future checks.
    """
    source = sqlite3.connect(f'file:{Path(path).resolve()}?mode=ro', uri=True)
    source.row_factory = sqlite3.Row
    order = dict(source.execute("SELECT o.* FROM orders o JOIN invoices i USING(order_id) JOIN payments p USING(invoice_id) WHERE o.status='fulfilled' AND NOT EXISTS(SELECT 1 FROM shipments s JOIN returns r USING(shipment_id) WHERE s.order_id=o.order_id) LIMIT 1").fetchone())
    shipped = [dict(r) for r in source.execute('SELECT * FROM shipments WHERE order_id=?', (order['order_id'],))]
    invoice = dict(source.execute('SELECT * FROM invoices WHERE order_id=?', (order['order_id'],)).fetchone())
    payment = dict(source.execute('SELECT * FROM payments WHERE invoice_id=?', (invoice['invoice_id'],)).fetchone())
    production = dict(source.execute('SELECT * FROM production_daily WHERE produced_kg>0 LIMIT 1').fetchone())
    cases = []
    mutations = [
        ('order-money', 'orders', 'net_cents', 1, 'order_price_arithmetic'),
        ('invoice-money', 'invoices', 'gross_cents', 1, 'invoice_shipped_amount'),
        ('payment-money', 'payments', 'amount_cents', 1, 'payment_amount'),
        ('inventory-stock', 'production_daily', 'closing_kg', 1, 'production_inventory'),
        ('shipment-overdelivery', 'shipments', 'quantity_kg', order['quantity_kg'] + 1, 'shipment_quantity_status'),
    ]
    for name, table, field, delta, check in mutations:
        conn = sqlite3.connect(':memory:')
        for t, rows in [('orders', [order]), ('shipments', shipped), ('invoices', [invoice]),
                        ('payments', [payment]), ('production_daily', [production])]:
            keys = list(rows[0]); conn.execute('CREATE TABLE ' + t + '(' + ','.join(keys) + ')')
            conn.executemany('INSERT INTO ' + t + ' VALUES(' + ','.join('?' for _ in keys) + ')', [tuple(r[k] for k in keys) for r in rows])
        conn.execute('CREATE TABLE shipment_totals AS SELECT order_id,SUM(quantity_kg) qty FROM shipments GROUP BY order_id')
        conn.execute('CREATE TABLE credits_by_order(order_id,gross)')
        before = conn.execute(CHECKS[check]).fetchone()[0]
        conn.execute(f'UPDATE {table} SET {field}={field}+?', (delta,))
        if table == 'shipments':
            conn.execute('DELETE FROM shipment_totals'); conn.execute('INSERT INTO shipment_totals SELECT order_id,SUM(quantity_kg) FROM shipments GROUP BY order_id')
        after = conn.execute(CHECKS[check]).fetchone()[0]
        cases.append({'id': name, 'source_order_id': order['order_id'], 'mutation': {table + '.' + field: '+' + str(delta)},
                      'check': check, 'baseline_violations': before, 'mutated_violations': after,
                      'rejected': before == 0 and after > 0})
        conn.close()
    source.close()
    return {'is_example': True, 'passed': all(c['rejected'] for c in cases), 'cases': cases,
            'notice': 'Mutations run in isolated in-memory tables from actual persisted rows; normal million-row baseline is untouched.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=HERE / 'dataset')
    args = parser.parse_args()
    report = audit(args.dataset / 'enterprise.sqlite')
    (args.dataset / 'oracle-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    negative = negatives(args.dataset / 'enterprise.sqlite')
    (args.dataset / 'negative-cases.json').write_text(json.dumps(negative, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'passed': report['passed'], 'negative_passed': negative['passed'], 'counts': report['counts']}, ensure_ascii=False))
    raise SystemExit(not (report['passed'] and negative['passed']))
