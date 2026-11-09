#!/usr/bin/env python3
"""Project saved million-record enterprise ledgers into traceable architecture facts."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import time

HERE = Path(__file__).resolve().parent
QUERIES = {
    'enterprise-orders': '''SELECT COUNT(*) order_count,COUNT(DISTINCT customer_id) active_customers,
        SUM(quantity_kg) ordered_kg,SUM(net_cents) booked_net_cents,MIN(order_day) first_order_day,MAX(order_day) last_order_day FROM orders''',
    'enterprise-shipments': '''SELECT COUNT(*) shipment_count,SUM(quantity_kg) shipped_kg,
        SUM(event_received_day>shipped_day) late_event_count,
        MAX(julianday(event_received_day)-julianday(shipped_day)) max_late_days FROM shipments''',
    'enterprise-finance': 'SELECT COUNT(*) invoice_count,SUM(net_cents) invoice_net_cents,SUM(tax_cents) tax_cents,SUM(gross_cents) gross_cents FROM invoices',
    'enterprise-returns': 'SELECT COUNT(*) return_count,SUM(quantity_kg) returned_kg,SUM(credit_gross_cents) credited_gross_cents FROM returns',
    'enterprise-energy': 'SELECT SUM(produced_kg) produced_kg,SUM(electric_wh) electric_wh FROM production_daily',
    'plants': '''SELECT p.plant_id,p.name,p.region,p.family,p.annual_capacity_kg,COUNT(o.order_id) order_count,
        SUM(o.quantity_kg) ordered_kg,SUM(o.net_cents) booked_net_cents,
        COUNT(DISTINCT o.customer_id) active_customers,COUNT(DISTINCT o.product_id) active_products
        FROM plants p LEFT JOIN orders o USING(plant_id) GROUP BY p.plant_id ORDER BY p.plant_id''',
    'plant-shipments': '''SELECT o.plant_id,COUNT(*) shipment_count,SUM(s.quantity_kg) shipped_kg,
        SUM(s.event_received_day>s.shipped_day) late_event_count,
        SUM(s.shipped_day>o.promised_day) late_shipment_count
        FROM shipments s JOIN orders o USING(order_id) GROUP BY o.plant_id ORDER BY o.plant_id''',
    'plant-energy': '''SELECT plant_id,SUM(produced_kg) produced_kg,SUM(electric_wh) electric_wh,
        MIN(closing_kg) minimum_line_closing_kg FROM production_daily GROUP BY plant_id ORDER BY plant_id''',
    'products': '''SELECT p.product_id,p.name,p.family,p.pack_kg,p.energy_wh_per_kg,COUNT(o.order_id) order_count,
        SUM(o.quantity_kg) ordered_kg,SUM(o.net_cents) booked_net_cents FROM products p LEFT JOIN orders o USING(product_id)
        GROUP BY p.product_id ORDER BY p.product_id''',
    'order-status': 'SELECT status,COUNT(*) order_count,SUM(quantity_kg) ordered_kg FROM orders GROUP BY status ORDER BY status',
    'monthly-orders': '''SELECT substr(order_day,1,7) month,COUNT(*) order_count,SUM(quantity_kg) ordered_kg,
        SUM(net_cents) booked_net_cents FROM orders GROUP BY 1 ORDER BY 1''',
    'daily-order-peak': '''SELECT order_day,COUNT(*) order_count FROM orders GROUP BY order_day ORDER BY order_count DESC,order_day LIMIT 10''',
    'customer-concentration': '''SELECT c.tier,COUNT(*) order_count,COUNT(DISTINCT o.customer_id) customers,
        SUM(o.net_cents) booked_net_cents FROM orders o JOIN customers c USING(customer_id) GROUP BY c.tier ORDER BY c.tier''',
    'workload-events': '''SELECT source_system,COUNT(*) event_count,COUNT(DISTINCT event_day) active_days,
        SUM(received_day>event_day) late_events FROM source_events GROUP BY source_system ORDER BY source_system''',
    'workload-event-peaks': '''SELECT source_system,MAX(n) peak_daily_events FROM
        (SELECT source_system,event_day,COUNT(*) n FROM source_events GROUP BY source_system,event_day)
        GROUP BY source_system ORDER BY source_system''',
    'return-reasons': 'SELECT reason,COUNT(*) records,SUM(quantity_kg) returned_kg FROM returns GROUP BY reason ORDER BY reason',
    'overdue-receivables': '''SELECT COUNT(*) invoices,SUM(i.gross_cents) gross_cents FROM invoices i LEFT JOIN payments p USING(invoice_id)
        WHERE p.payment_id IS NULL AND i.due_day<'2026-10-31' ''',
    'order-sample': '''SELECT o.*,COALESCE((SELECT SUM(s.quantity_kg) FROM shipments s WHERE s.order_id=o.order_id),0) shipped_kg,
        (SELECT invoice_id FROM invoices i WHERE i.order_id=o.order_id) invoice_id
        FROM orders o WHERE o.order_id IN (1,19,357,10201,99001,250003,499999,750007,999983,1000000) ORDER BY o.order_id''',
    'annual-production-capacity': '''SELECT d.plant_id,substr(d.production_day,1,4) year,SUM(d.produced_kg) produced_kg,
        p.annual_capacity_kg,COUNT(DISTINCT d.production_day) observed_days FROM production_daily d JOIN plants p USING(plant_id)
        GROUP BY d.plant_id,substr(d.production_day,1,4) ORDER BY 1,2''',
}


def derive(dataset, out):
    dataset, out = Path(dataset), Path(out)
    manifest = json.loads((dataset / 'manifest.json').read_text())
    observed = hashlib.sha256()
    with (dataset / 'enterprise.sqlite').open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            observed.update(chunk)
    if observed.hexdigest() != manifest['database_sha256']:
        raise ValueError('Database bytes differ from the declared manifest; rerun independent audit before projecting facts.')
    conn = sqlite3.connect(f'file:{(dataset / "enterprise.sqlite").resolve()}?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    results, query_records = {}, {}
    for key, sql in QUERIES.items():
        start = time.perf_counter()
        rows = [dict(r) for r in conn.execute(sql)]
        results[key] = [{**r, 'query_id': key} for r in rows]
        query_records[key] = {'sql': sql, 'rows': len(rows), 'seconds': round(time.perf_counter() - start, 3),
                              'database_sha256': manifest['database_sha256']}
        print('query', key, len(rows), flush=True)
    conn.close()
    plant_shipments = {r['plant_id']: r for r in results['plant-shipments']}
    plant_energy = {r['plant_id']: r for r in results['plant-energy']}
    plants = [{**r, 'shipment_metrics': plant_shipments[r['plant_id']], 'energy_metrics': plant_energy[r['plant_id']]} for r in results['plants']]
    event_peaks = {r['source_system']: r for r in results['workload-event-peaks']}
    workloads = [{**r, 'peak': event_peaks[r['source_system']]} for r in results['workload-events']]
    ships = results['enterprise-shipments'][0]
    quality = [{'id': 'MX-OBS-LATE-EVENT', 'kind': 'synthetic_record_aggregate', 'name': '发运事件晚到比例',
                'numerator': ships['late_event_count'], 'denominator': ships['shipment_count'],
                'value_percent': 100 * ships['late_event_count'] / ships['shipment_count'], 'unit': '%',
                'period': ['2024-01-01', '2026-10-31'], 'query_id': 'enterprise-shipments',
                'interpretation': 'received_day 晚于 shipped_day 的比例；不是端到端消息延迟秒数或生产 SLA 证明。'}]
    fact = {'schema_version': 'million-enterprise-facts-1.0', 'is_example': True,
        'source_id': 'MX-MILLION-SQLITE', 'dataset_sha256': manifest['database_sha256'],
        'dataset_path': 'dataset/enterprise.sqlite', 'queries': query_records,
        'enterprise': {key: results[key][0] for key in ['enterprise-orders','enterprise-shipments','enterprise-finance','enterprise-returns','enterprise-energy']},
        'plants': plants, 'products': results['products'], 'order_status': results['order-status'],
        'monthly': results['monthly-orders'], 'application_workloads': workloads, 'quality_observations': quality,
        'customer_segments': results['customer-concentration'], 'return_reasons': results['return-reasons'],
        'overdue_receivables': results['overdue-receivables'], 'peak_order_days': results['daily-order-peak'],
        'annual_production': results['annual-production-capacity'], 'samples': results['order-sample'],
        'boundaries': ['Every measurement above is queried from saved synthetic records.',
            'Application responsibility/deployment, candidate targets, budget, authority and acceptance are separate simulation assumptions in enterprise-brief.md.',
            'Financial totals use integer CNY cents; do not mix ordered, shipped, invoiced, returned and paid amounts.']}
    out.write_text(json.dumps(fact, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return fact


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dataset', type=Path, default=HERE / 'dataset')
    p.add_argument('--out', type=Path, default=HERE / 'derived-facts.json')
    args = p.parse_args(); derive(args.dataset, args.out)
