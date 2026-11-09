#!/usr/bin/env python3
"""Create a deterministic, relational million-order synthetic enterprise dataset.

All business rules are declared simulation choices, not real company evidence.
An existing dataset is never overwritten; pass a new --out for another run.
"""
import argparse
import bisect
from collections import defaultdict
from datetime import date, timedelta
import hashlib
import json
from pathlib import Path
import random
import sqlite3
import time

HERE = Path(__file__).resolve().parent
START = date(2024, 1, 1)
END = date(2026, 10, 31)
DAYS = (END - START).days + 1
DATES = [(START + timedelta(days=i)).isoformat() for i in range(DAYS + 91)]
FAMILIES = ['fertilizer', 'purified-acid', 'industrial-salt', 'electronic-grade']
FAMILY_ZH = ['磷肥', '净化磷酸', '工业磷酸盐', '电子级磷酸']
REGIONS = ['西南', '华中', '华东']


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def build(out, count, seed):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    dbpath = out / 'enterprise.sqlite'
    conn = sqlite3.connect(dbpath)
    conn.executescript('''
      PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF; PRAGMA temp_store=MEMORY;
      PRAGMA foreign_keys=ON; PRAGMA cache_size=-65536;
      CREATE TABLE plants(plant_id TEXT PRIMARY KEY,name TEXT,region TEXT,family TEXT,annual_capacity_kg INTEGER);
      CREATE TABLE products(product_id TEXT PRIMARY KEY,name TEXT,family TEXT,pack_kg INTEGER,base_price_cents_per_kg INTEGER,energy_wh_per_kg INTEGER);
      CREATE TABLE customers(customer_id INTEGER PRIMARY KEY,name TEXT,region TEXT,tier TEXT,credit_days INTEGER);
      CREATE TABLE plant_products(plant_id TEXT REFERENCES plants,product_id TEXT REFERENCES products,PRIMARY KEY(plant_id,product_id));
      CREATE TABLE orders(order_id INTEGER PRIMARY KEY,order_day TEXT,customer_id INTEGER REFERENCES customers,
        plant_id TEXT REFERENCES plants,product_id TEXT REFERENCES products,quantity_kg INTEGER CHECK(quantity_kg>0),
        price_cents_per_kg INTEGER,discount_bps INTEGER,net_cents INTEGER,status TEXT,promised_day TEXT,channel TEXT);
      CREATE TABLE shipments(shipment_id INTEGER PRIMARY KEY,order_id INTEGER REFERENCES orders,
        shipped_day TEXT,quantity_kg INTEGER CHECK(quantity_kg>0),event_received_day TEXT);
      CREATE TABLE returns(return_id INTEGER PRIMARY KEY,shipment_id INTEGER REFERENCES shipments,
        returned_day TEXT,quantity_kg INTEGER CHECK(quantity_kg>0),reason TEXT,
        credit_net_cents INTEGER,credit_tax_cents INTEGER,credit_gross_cents INTEGER);
      CREATE TABLE invoices(invoice_id INTEGER PRIMARY KEY,order_id INTEGER UNIQUE REFERENCES orders,
        invoice_day TEXT,net_cents INTEGER,tax_cents INTEGER,gross_cents INTEGER,due_day TEXT);
      CREATE TABLE payments(payment_id INTEGER PRIMARY KEY,invoice_id INTEGER UNIQUE REFERENCES invoices,paid_day TEXT,amount_cents INTEGER);
      CREATE TABLE production_daily(plant_id TEXT REFERENCES plants,product_id TEXT REFERENCES products,production_day TEXT,
        opening_kg INTEGER,produced_kg INTEGER,shipped_kg INTEGER,returned_kg INTEGER,closing_kg INTEGER,electric_wh INTEGER,
        PRIMARY KEY(plant_id,product_id,production_day));
      CREATE TABLE source_events(event_id INTEGER PRIMARY KEY,entity_type TEXT,entity_id INTEGER,event_type TEXT,event_day TEXT,received_day TEXT,source_system TEXT);
    ''')
    rng = random.Random(seed)
    plant_rows = []
    for family in range(4):
        for region in range(3):
            i = family * 3 + region + 1
            plant_rows.append((f'MX-PLANT-{i:02}', f'虚构{REGIONS[region]}{FAMILY_ZH[family]}基地',
                               REGIONS[region], FAMILIES[family], [1800000000, 1400000000, 500000000, 120000000][family]))
    conn.executemany('INSERT INTO plants VALUES(?,?,?,?,?)', plant_rows)
    products = []
    for family in range(4):
        for sku in range(6):
            product_id = f'MX-SKU-{family * 6 + sku + 1:02}'
            products.append((product_id, f'{FAMILY_ZH[family]}规格{sku + 1}', FAMILIES[family],
                             [50, 1000, 25, 25][family], [250, 650, 780, 3500][family] + sku * [12, 20, 35, 160][family],
                             [500, 1200, 950, 2800][family] + sku * 15))
    conn.executemany('INSERT INTO products VALUES(?,?,?,?,?,?)', products)
    conn.executemany('INSERT INTO plant_products VALUES(?,?)',
                     [(plant[0], product[0]) for plant in plant_rows for product in products if plant[3] == product[2]])
    customers = [(i, f'虚构客户-{i:05}', REGIONS[(i - 1) % 3],
                  'strategic' if i <= 500 else 'regional' if i <= 4000 else 'distributor',
                  60 if i <= 500 else 45 if i <= 4000 else 30) for i in range(1, 12001)]
    conn.executemany('INSERT INTO customers VALUES(?,?,?,?,?)', customers)
    # Spring and autumn agriculture peaks, mild growth over the three years,
    # weekday effect; all are explicit simulation assumptions.
    day_cumulative, total = [], 0.0
    for i in range(DAYS):
        d = START + timedelta(days=i)
        seasonal = 1.65 if d.month in (3, 4, 9) else 1.25 if d.month in (2, 8, 10) else 0.8
        weight = seasonal * (0.45 if d.weekday() >= 5 else 1) * (1 + 0.08 * (d.year - 2024))
        total += weight
        day_cumulative.append(total)
    # Use persisted relational outputs to derive production schedules later.
    order_buffer, shipment_buffer, return_buffer, invoice_buffer, payment_buffer, event_buffer = [], [], [], [], [], []
    shipment_id = return_id = invoice_id = payment_id = event_id = 0
    def flush():
        conn.executemany('INSERT INTO orders VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', order_buffer)
        conn.executemany('INSERT INTO shipments VALUES(?,?,?,?,?)', shipment_buffer)
        conn.executemany('INSERT INTO returns VALUES(?,?,?,?,?,?,?,?)', return_buffer)
        conn.executemany('INSERT INTO invoices VALUES(?,?,?,?,?,?,?)', invoice_buffer)
        conn.executemany('INSERT INTO payments VALUES(?,?,?,?)', payment_buffer)
        conn.executemany('INSERT INTO source_events VALUES(?,?,?,?,?,?,?)', event_buffer)
        conn.commit()
        for buffer in (order_buffer, shipment_buffer, return_buffer, invoice_buffer, payment_buffer, event_buffer):
            buffer.clear()
    for order_id in range(1, count + 1):
        day = bisect.bisect_left(day_cumulative, rng.random() * total)
        age = DAYS - 1 - day
        customer_id = 1 + min(11999, int(12000 * rng.random() ** 2.55))
        home = (customer_id - 1) % 3
        u = rng.random()
        family = 0 if u < .48 else 1 if u < .73 else 2 if u < .92 else 3
        product = products[family * 6 + rng.randrange(6)]
        region = home if rng.random() < .8 else rng.randrange(3)
        plant_id = plant_rows[family * 3 + region][0]
        sizes = ([1000, 5000, 10000, 25000, 50000], [1000, 5000, 10000, 20000, 30000],
                 [250, 500, 1000, 3000, 10000], [25, 100, 250, 500, 1000])[family]
        base_qty = rng.choices(sizes, weights=[10, 20, 35, 30, 5])[0]
        qty = base_qty * (2 if customer_id <= 500 and rng.random() < .2 else 1)
        # Prices vary with product, year and independently sampled order conditions.
        price = max(1, round(product[4] * (1 + .035 * ((START + timedelta(days=day)).year - 2024)) * rng.uniform(.94, 1.06)))
        discount = (300 if customer_id <= 500 else 100 if customer_id <= 4000 else 0) + (200 if qty >= 25000 else 0)
        net = qty * price * (10000 - discount) // 10000
        lead = rng.randint(2, 10) if family < 3 else rng.randint(4, 16)
        promised = min(DAYS + 60, day + lead)
        u = rng.random()
        if u < .035:
            status = 'cancelled'
        elif age < lead and u < .75:
            status = 'open'
        elif age < 20 and u < .35:
            status = 'partial'
        elif u < .045:
            status = 'partial'
        else:
            status = 'fulfilled'
        channel = rng.choices(['EDI', 'customer-portal', 'sales-assisted'], weights=[45, 40, 15])[0]
        order_buffer.append((order_id, DATES[day], customer_id, plant_id, product[0], qty, price,
                             discount, net, status, DATES[promised], channel))
        event_id += 1
        event_buffer.append((event_id, 'order', order_id, 'order-created', DATES[day], DATES[day], 'MX-OMS'))
        if status in ('fulfilled', 'partial'):
            shipped_qty = qty if status == 'fulfilled' else max(1, qty * rng.choice([30, 50, 70]) // 100)
            # Two batches occur for bulk orders; no duplicated shipment IDs.
            split = shipped_qty >= 1000 and rng.random() < .23
            amounts = [shipped_qty // 2, shipped_qty - shipped_qty // 2] if split else [shipped_qty]
            return_credit = 0
            last_ship_day = day
            for n, amount in enumerate(amounts):
                shipment_id += 1
                actual = min(DAYS - 1, day + max(0, lead - 2 + n * 2 + (rng.randint(3, 9) if rng.random() < .07 else 0)))
                last_ship_day = max(last_ship_day, actual)
                received = min(DAYS - 1, actual + (rng.randint(1, 4) if rng.random() < .025 else 0))
                shipment_buffer.append((shipment_id, order_id, DATES[actual], amount, DATES[received]))
                event_id += 1
                event_buffer.append((event_id, 'shipment', shipment_id, 'goods-dispatched', DATES[actual], DATES[received], 'MX-WMS'))
                if actual < DAYS - 12 and rng.random() < .018:
                    return_id += 1
                    returned = max(1, amount * rng.choice([5, 10, 20, 100]) // 100)
                    return_day = min(DAYS - 1, actual + rng.randint(2, 12))
                    credit_net = returned * price * (10000 - discount) // 10000
                    credit_tax = credit_net * 13 // 100
                    credit_gross = credit_net + credit_tax
                    return_credit += credit_gross
                    reason = rng.choices(['quality-claim', 'damaged-package', 'wrong-grade', 'customer-excess'], weights=[25, 35, 10, 30])[0]
                    return_buffer.append((return_id, shipment_id, DATES[return_day], returned, reason, credit_net, credit_tax, credit_gross))
                    event_id += 1
                    event_buffer.append((event_id, 'return', return_id, 'return-accepted', DATES[return_day], DATES[return_day], 'MX-CRM'))
            invoice_id += 1
            invoice_day = min(DAYS - 1, last_ship_day + 1)
            invoice_net = shipped_qty * price * (10000 - discount) // 10000
            tax = invoice_net * 13 // 100
            gross = invoice_net + tax
            credit_days = 60 if customer_id <= 500 else 45 if customer_id <= 4000 else 30
            due = invoice_day + credit_days
            invoice_buffer.append((invoice_id, order_id, DATES[invoice_day], invoice_net, tax, gross, DATES[due]))
            event_id += 1
            event_buffer.append((event_id, 'invoice', invoice_id, 'invoice-posted', DATES[invoice_day], DATES[invoice_day], 'MX-ERP'))
            paid = due + rng.randint(-8, 15)
            if paid < DAYS and rng.random() > .015:
                payment_id += 1
                payment_buffer.append((payment_id, invoice_id, DATES[max(invoice_day, paid)], gross - return_credit))
        if order_id % 10000 == 0:
            flush()
        if order_id % 100000 == 0:
            print(f'generated_orders={order_id:,} seconds={time.perf_counter()-started:.1f}', flush=True)
    flush()
    conn.executescript('''
      CREATE INDEX ix_orders_scope ON orders(plant_id,product_id,order_day);
      CREATE INDEX ix_orders_customer ON orders(customer_id);
      CREATE INDEX ix_shipments_order ON shipments(order_id);
      CREATE INDEX ix_shipments_day ON shipments(shipped_day);
      CREATE INDEX ix_returns_shipment ON returns(shipment_id);
      CREATE INDEX ix_returns_day ON returns(returned_day);
      CREATE INDEX ix_invoices_day ON invoices(invoice_day);
      CREATE INDEX ix_events_entity ON source_events(entity_type,entity_id);
    ''')
    print('aggregating_production_schedule', flush=True)
    shipments_daily = {(r[0], r[1], r[2]): r[3] for r in conn.execute('''
        SELECT o.plant_id,o.product_id,s.shipped_day,SUM(s.quantity_kg)
        FROM shipments s JOIN orders o USING(order_id) GROUP BY 1,2,3''')}
    returns_daily = {(r[0], r[1], r[2]): r[3] for r in conn.execute('''
        SELECT o.plant_id,o.product_id,r.returned_day,SUM(r.quantity_kg)
        FROM returns r JOIN shipments s USING(shipment_id) JOIN orders o USING(order_id) GROUP BY 1,2,3''')}
    rows = []
    for plant in plant_rows:
        for product in products:
            if plant[3] != product[2]:
                continue
            # A synthetic committed-demand schedule, not a chemical-process simulator.
            # Returns enter quarantine and are explicitly not used as saleable input.
            stock = rng.randint(100, 500) * product[3]
            for day in range(DAYS):
                key = (plant[0], product[0], DATES[day]); demand = shipments_daily.get(key, 0)
                returned = returns_daily.get(key, 0)
                safety = max(product[3] * 100, demand * rng.randint(5, 12) // 100)
                produced = max(0, ((demand + safety - stock + product[3] - 1) // product[3]) * product[3])
                closing = stock + produced - demand
                # Includes a fixed per-line operating load and process variation.
                electric = max(0, round(produced * product[5] * rng.uniform(.97, 1.03))) + 250000
                rows.append((plant[0], product[0], DATES[day], stock, produced, demand, returned, closing, electric))
                stock = closing
    conn.executemany('INSERT INTO production_daily VALUES(?,?,?,?,?,?,?,?,?)', rows)
    conn.commit()
    conn.execute('ANALYZE')
    conn.commit()
    tables = ['plants', 'products', 'customers', 'plant_products', 'orders', 'shipments', 'returns', 'invoices', 'payments', 'production_daily', 'source_events']
    counts = {t: conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in tables}
    conn.close()
    rules = {'is_example': True, 'seed': seed, 'period': [START.isoformat(), END.isoformat()],
        'units': {'quantity': 'kg integer', 'money': 'CNY cents integer', 'electricity': 'Wh integer'},
        'identity': 'All records generated from declared simulation choices; no real company or personal data.',
        'distribution': {'customers': '12,000, long-tail index power 2.55', 'plants': 12, 'products': 24,
            'monthly': 'spring/autumn demand peaks; weekday bias; 8% annual sampling weight growth',
            'status': 'age-conditioned open/partial/fulfilled plus 3.5% cancellations',
            'shipment_split_probability': .23, 'return_probability_per_shipment': .018, 'late_event_probability': .025},
        'financial': 'invoice net is shipped quantity times discounted price, rounded down to cents; VAT simulated 13%; accepted returns create separate credit, paid amount is invoice gross minus return credits.',
        'inventory': 'Production planning follows synthetic committed shipment demand with packaged safety stock. Returns are quarantined, not counted as saleable closing inventory.',
        'energy': 'Declared SKU intensity times produced kg with independent +/-3% variation plus 250 kWh per daily line; not validated plant physics.',
        'not_claimed': ['real enterprise facts', 'regulatory/tax applicability', 'chemical mass-balance accuracy', 'production capacity certification', 'actual ROI or architecture approval']}
    write_json(out / 'rules.json', rules)
    manifest = {'is_example': True, 'dataset_id': 'MX-MILLION-20261104', 'seed': seed,
        'requested_orders': count, 'counts': counts, 'logical_business_records': sum(counts[t] for t in ['orders','shipments','returns','invoices','payments','production_daily']),
        'source_event_records': counts['source_events'], 'database_bytes': dbpath.stat().st_size,
        'database_sha256': file_hash(dbpath), 'generator_sha256': file_hash(__file__),
        'seconds': round(time.perf_counter() - started, 3), 'limits': rules['not_claimed']}
    write_json(out / 'manifest.json', manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2), flush=True)
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=HERE / 'dataset')
    parser.add_argument('--orders', type=int, default=1000000)
    parser.add_argument('--seed', type=int, default=20261104)
    args = parser.parse_args()
    if args.orders <= 0:
        parser.error('--orders must be positive')
    build(args.out, args.orders, args.seed)
