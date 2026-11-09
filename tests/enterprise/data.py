"""Generic manufacturing workload and independent SQL/Decimal reconciliation.

Offline SQLite timings are not OLTP/ERP benchmarks. Quantities use pieces,
CNY cents and Wh; no chemical-specific products, policies or conversions.
"""
import json
import shutil
import sqlite3
import time
from decimal import Decimal
from pathlib import Path
from .runtime import Blocked, save, sha256

SCHEMA = '''
CREATE TABLE sites(id INTEGER PRIMARY KEY,name TEXT);
CREATE TABLE products(id INTEGER PRIMARY KEY,name TEXT,unit TEXT);
CREATE TABLE customers(id INTEGER PRIMARY KEY,name TEXT);
CREATE TABLE suppliers(id INTEGER PRIMARY KEY,name TEXT);
CREATE TABLE orders(id INTEGER PRIMARY KEY,site_id INTEGER,product_id INTEGER,customer_id INTEGER,
 quantity INTEGER,unit_price_cents INTEGER,created_day INTEGER);
CREATE TABLE shipments(id INTEGER PRIMARY KEY,order_id INTEGER,quantity INTEGER,shipped_day INTEGER);
CREATE TABLE returns(id INTEGER PRIMARY KEY,order_id INTEGER,quantity INTEGER);
CREATE TABLE invoices(id INTEGER PRIMARY KEY,order_id INTEGER,amount_cents INTEGER);
CREATE TABLE payments(id INTEGER PRIMARY KEY,invoice_id INTEGER,amount_cents INTEGER);
CREATE TABLE procurement(id INTEGER PRIMARY KEY,supplier_id INTEGER,site_id INTEGER,product_id INTEGER,
 quantity INTEGER,unit_cost_cents INTEGER,due_day INTEGER);
CREATE TABLE receipts(id INTEGER PRIMARY KEY,procurement_id INTEGER,quantity INTEGER,received_day INTEGER);
CREATE TABLE quality(id INTEGER PRIMARY KEY,receipt_id INTEGER,accepted INTEGER,rejected INTEGER);
CREATE TABLE supplier_invoices(id INTEGER PRIMARY KEY,procurement_id INTEGER,amount_cents INTEGER);
CREATE TABLE supplier_payments(id INTEGER PRIMARY KEY,invoice_id INTEGER,amount_cents INTEGER);
CREATE TABLE production(id INTEGER PRIMARY KEY,site_id INTEGER,product_id INTEGER,quantity INTEGER);
CREATE TABLE inventory(id INTEGER PRIMARY KEY,production_id INTEGER,site_id INTEGER,product_id INTEGER,delta INTEGER);
CREATE TABLE energy(id INTEGER PRIMARY KEY,production_id INTEGER,watt_hours INTEGER);
CREATE TABLE incidents(id INTEGER PRIMARY KEY,site_id INTEGER,service TEXT,minutes INTEGER,observed_day INTEGER);
CREATE TABLE events(id INTEGER PRIMARY KEY,order_id INTEGER,kind TEXT,occurred_day INTEGER,arrival_seq INTEGER);
CREATE TABLE assumptions(id TEXT PRIMARY KEY,description TEXT,classification TEXT);
'''

AUDIT_SQL = {
    'order-dimensions': 'SELECT count(*) FROM orders o LEFT JOIN sites s ON s.id=o.site_id LEFT JOIN products p ON p.id=o.product_id LEFT JOIN customers c ON c.id=o.customer_id WHERE s.id IS NULL OR p.id IS NULL OR c.id IS NULL',
    'order-units': "SELECT count(*) FROM products WHERE unit!='pcs'",
    'order-quantity-price': 'SELECT count(*) FROM orders WHERE quantity<=0 OR unit_price_cents<=0',
    'shipment-balance': 'SELECT count(*) FROM shipments s LEFT JOIN orders o ON o.id=s.order_id WHERE o.id IS NULL OR s.quantity<0 OR s.quantity>o.quantity OR s.shipped_day<o.created_day',
    'return-balance': 'SELECT count(*) FROM returns r LEFT JOIN shipments s ON s.order_id=r.order_id WHERE s.id IS NULL OR r.quantity<0 OR r.quantity>s.quantity',
    'invoice-net': 'SELECT count(*) FROM invoices i LEFT JOIN orders o ON o.id=i.order_id LEFT JOIN shipments s ON s.order_id=o.id LEFT JOIN returns r ON r.order_id=o.id WHERE o.id IS NULL OR s.id IS NULL OR i.amount_cents!=(s.quantity-coalesce(r.quantity,0))*o.unit_price_cents',
    'payment-balance': 'SELECT count(*) FROM payments p LEFT JOIN invoices i ON i.id=p.invoice_id WHERE i.id IS NULL OR p.amount_cents<0 OR p.amount_cents>i.amount_cents',
    'procurement-dimensions': 'SELECT count(*) FROM procurement p LEFT JOIN suppliers s ON s.id=p.supplier_id LEFT JOIN products d ON d.id=p.product_id LEFT JOIN sites l ON l.id=p.site_id WHERE s.id IS NULL OR d.id IS NULL OR l.id IS NULL OR p.quantity<=0 OR p.unit_cost_cents<=0',
    'receipt-balance': 'SELECT count(*) FROM receipts r LEFT JOIN procurement p ON p.id=r.procurement_id WHERE p.id IS NULL OR r.quantity<0 OR r.quantity>p.quantity',
    'inspection-balance': 'SELECT count(*) FROM quality q LEFT JOIN receipts r ON r.id=q.receipt_id WHERE r.id IS NULL OR q.accepted<0 OR q.rejected<0 OR q.accepted+q.rejected!=r.quantity',
    'supplier-invoice-net': 'SELECT count(*) FROM supplier_invoices i LEFT JOIN procurement p ON p.id=i.procurement_id LEFT JOIN receipts r ON r.procurement_id=p.id LEFT JOIN quality q ON q.receipt_id=r.id WHERE p.id IS NULL OR q.id IS NULL OR i.amount_cents!=q.accepted*p.unit_cost_cents',
    'supplier-payment-balance': 'SELECT count(*) FROM supplier_payments p LEFT JOIN supplier_invoices i ON i.id=p.invoice_id WHERE i.id IS NULL OR p.amount_cents<0 OR p.amount_cents>i.amount_cents',
    'inventory-balance': 'SELECT count(*) FROM production p LEFT JOIN (SELECT production_id,sum(delta) net,count(*) entries FROM inventory GROUP BY production_id) i ON i.production_id=p.id WHERE coalesce(i.net,1)!=0 OR coalesce(i.entries,0)!=2',
    'inventory-references': 'SELECT count(*) FROM inventory i LEFT JOIN production p ON p.id=i.production_id WHERE p.id IS NULL OR i.site_id!=p.site_id OR i.product_id!=p.product_id OR abs(i.delta)!=p.quantity',
    'production-dimensions': 'SELECT count(*) FROM production p LEFT JOIN sites s ON s.id=p.site_id LEFT JOIN products d ON d.id=p.product_id WHERE s.id IS NULL OR d.id IS NULL OR p.quantity<=0',
    'energy-units': 'SELECT count(*) FROM energy e LEFT JOIN production p ON p.id=e.production_id WHERE p.id IS NULL OR e.watt_hours<=0',
    'event-references': 'SELECT count(*) FROM events e LEFT JOIN orders o ON o.id=e.order_id WHERE o.id IS NULL',
    'event-business-duplicates': 'SELECT count(*) FROM (SELECT order_id,kind FROM events GROUP BY order_id,kind HAVING count(*)!=1)',
    'event-time': 'SELECT count(*) FROM events e JOIN orders o ON o.id=e.order_id WHERE e.occurred_day<o.created_day',
    'event-missing': 'SELECT count(*) FROM orders o WHERE NOT EXISTS(SELECT 1 FROM events e WHERE e.order_id=o.id AND e.kind="order-created")',
}

FACT_SQL = {
    'sales': 'SELECT o.site_id,o.product_id,count(*) orders,sum(o.quantity) ordered_pcs,sum(coalesce(s.quantity,0)) shipped_pcs,sum(coalesce(r.quantity,0)) returned_pcs,sum(coalesce(i.amount_cents,0)) invoiced_cents,sum(coalesce(p.amount_cents,0)) paid_cents FROM orders o LEFT JOIN shipments s ON s.order_id=o.id LEFT JOIN returns r ON r.order_id=o.id LEFT JOIN invoices i ON i.order_id=o.id LEFT JOIN payments p ON p.invoice_id=i.id GROUP BY o.site_id,o.product_id ORDER BY o.site_id,o.product_id',
    'procurement': 'SELECT p.site_id,count(*) purchases,sum(p.quantity) ordered_pcs,sum(r.quantity) received_pcs,sum(q.accepted) accepted_pcs,sum(q.rejected) rejected_pcs,sum(r.received_day>p.due_day) late_receipts,sum(i.amount_cents) supplier_invoiced_cents,sum(pay.amount_cents) supplier_paid_cents FROM procurement p JOIN receipts r ON r.procurement_id=p.id JOIN quality q ON q.receipt_id=r.id JOIN supplier_invoices i ON i.procurement_id=p.id JOIN supplier_payments pay ON pay.invoice_id=i.id GROUP BY p.site_id ORDER BY p.site_id',
    'production': 'SELECT p.site_id,count(*) lots,sum(p.quantity) produced_pcs,sum(e.watt_hours) energy_wh FROM production p JOIN energy e ON e.production_id=p.id GROUP BY p.site_id ORDER BY p.site_id',
    'it': 'SELECT site_id,count(*) incidents,sum(minutes) outage_minutes FROM incidents GROUP BY site_id ORDER BY site_id',
}


def connect(path):
    connection = sqlite3.connect(str(path), timeout=30)
    connection.execute('PRAGMA busy_timeout=30000')
    return connection


def attach_budget(connection,budget):
    def progress():
        try:
            budget.check(dispatch=False)
            return 0
        except Blocked as exc:
            budget.stop_reason = str(exc)
            budget.cancel.set()
            return 1
    connection.set_progress_handler(progress,100000)


def build(directory, orders, seed, budget, chunk=50000):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    db = directory / 'enterprise.sqlite'
    started = time.monotonic()
    connection = connect(db)
    attach_budget(connection,budget)
    try:
        connection.execute('PRAGMA journal_mode=DELETE')
        connection.execute('PRAGMA synchronous=NORMAL')
        connection.executescript(SCHEMA)
        for table, count, label in (('sites', 12, '基地'), ('customers', 12000, '客户'), ('suppliers', 360, '供应商')):
            connection.executemany('INSERT INTO '+table+' VALUES (?,?)', ((i, label+str(i)) for i in range(1, count+1)))
        connection.executemany('INSERT INTO products VALUES (?,?,?)', ((i, '工业组件-'+str(i), 'pcs') for i in range(1, 25)))
        connection.executemany('INSERT INTO assumptions VALUES (?,?,?)', [
            ('capacity', '12个基地，24类工业组件；规模不构成生产能力证明', 'synthetic-assumption'),
            ('authority', '未获得真实业务批准、签署或收益实现证明', 'synthetic-assumption'),
            ('ap-rule', '采购发票按检验接受件数计价；账期余款是合成规则，不是真实供应商合同', 'synthetic-assumption'),
            ('budget', '目标架构预算与职责须由实际利益相关者确认', 'synthetic-assumption')])
        connection.execute('CREATE TEMP TABLE seq(n INTEGER PRIMARY KEY)')
        for start in range(1, orders+1, chunk):
            budget.check()
            end = min(orders+1, start+chunk)
            connection.execute('DELETE FROM seq')
            connection.executemany('INSERT INTO seq VALUES (?)', ((n,) for n in range(start, end)))
            # Different scale seeds, deterministic arithmetic; correlated dimensions are explicit.
            connection.execute('INSERT INTO orders SELECT n,1+(n*7+?)/24%12,1+(n*13+?)%24,1+(n*17+?)%12000,1+(n*19+?)%200,100+(n*23+?)%50000,(n*31+?)%1035 FROM seq', (seed,)*6)
            connection.execute('INSERT INTO shipments SELECT id,id,quantity-id%3,created_day+id%7 FROM orders WHERE id>=? AND id<?', (start,end))
            connection.execute('UPDATE shipments SET quantity=0 WHERE quantity<0 AND id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO returns SELECT id,id,CASE WHEN id%37=0 AND quantity>0 THEN 1 ELSE 0 END FROM shipments WHERE id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO invoices SELECT o.id,o.id,(s.quantity-r.quantity)*o.unit_price_cents FROM orders o JOIN shipments s ON s.id=o.id JOIN returns r ON r.id=o.id WHERE o.id>=? AND o.id<?', (start,end))
            connection.execute('INSERT INTO payments SELECT id,id,amount_cents-CASE WHEN id%11=0 THEN amount_cents/3 ELSE 0 END FROM invoices WHERE id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO procurement SELECT id,1+id%360,site_id,product_id,quantity,unit_price_cents/2+1,created_day+3 FROM orders WHERE id%4=0 AND id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO receipts SELECT id,id,quantity,due_day+CASE WHEN id%28=0 THEN 4 ELSE -1 END FROM procurement WHERE id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO quality SELECT id,id,quantity-CASE WHEN id%44=0 THEN 1 ELSE 0 END,CASE WHEN id%44=0 THEN 1 ELSE 0 END FROM receipts WHERE id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO supplier_invoices SELECT p.id,p.id,q.accepted*p.unit_cost_cents FROM procurement p JOIN quality q ON q.id=p.id WHERE p.id>=? AND p.id<?',(start,end))
            connection.execute('INSERT INTO supplier_payments SELECT id,id,amount_cents-CASE WHEN id%52=0 THEN amount_cents/5 ELSE 0 END FROM supplier_invoices WHERE id>=? AND id<?',(start,end))
            connection.execute('INSERT INTO production SELECT id,site_id,product_id,quantity FROM orders WHERE id%2=0 AND id>=? AND id<?', (start,end))
            for sign, offset in ((1,0),(-1,1)):
                connection.execute('INSERT INTO inventory SELECT id*2+?,id,site_id,product_id,quantity*? FROM production WHERE id>=? AND id<?', (offset,sign,start,end))
            connection.execute('INSERT INTO energy SELECT id,id,quantity*(1000+id%100) FROM production WHERE id>=? AND id<?', (start,end))
            connection.execute('INSERT INTO incidents SELECT id,site_id,"order-service",1+id%120,created_day FROM orders WHERE id%10000=0 AND id>=? AND id<?', (start,end))
            for offset, kind in enumerate(('order-created','shipment-recorded','invoice-recorded')):
                connection.execute('INSERT INTO events SELECT id*3+?,id,?,created_day+?,id*3+? FROM orders WHERE id>=? AND id<?', (offset,kind,offset,offset,start,end))
            connection.commit()
            save(directory / 'build-progress.json', {'orders_written':end-1, 'target_orders':orders})
        budget.check()
        for table, column in (('shipments','order_id'),('returns','order_id'),('invoices','order_id'),('payments','invoice_id'),('receipts','procurement_id'),('quality','receipt_id'),('energy','production_id'),('supplier_invoices','procurement_id'),('supplier_payments','invoice_id'),('inventory','production_id')):
            connection.execute('CREATE UNIQUE INDEX '+table+'_business_key ON '+table+'('+column+')' if table!='inventory' else 'CREATE INDEX inventory_production ON inventory(production_id)')
        connection.execute('CREATE INDEX events_business_key ON events(order_id,kind)')
        connection.commit()
    finally:
        connection.close()
    manifest = {'schema_version':'generic-manufacturing/1', 'orders':orders, 'seed':seed, 'master_seed':20261105,
                'sites':12, 'products':24, 'customers':12000, 'suppliers':360,
                'database_sha256':sha256(db), 'database_bytes':db.stat().st_size,
                'seconds':round(time.monotonic()-started,3),
                'units':{'quantity':'pcs','money':'CNY cents','energy':'Wh'},
                'journal_mode':'DELETE','synchronous':'NORMAL',
                'limits':['Offline synthetic workload, not ERP/OLTP availability or production throughput.']}
    save(directory / 'manifest.json', manifest)
    return manifest


def audit(db, directory, budget):
    directory = Path(directory)
    budget.check()
    connection = connect(db)
    attach_budget(connection,budget)
    try:
        checks = []
        for name, sql in AUDIT_SQL.items():
            budget.check()
            count = connection.execute(sql).fetchone()[0]
            checks.append({'name':name,'sql':sql,'violations':count,'status':'pass' if count==0 else 'fail'})
        counts = {table:connection.execute('SELECT count(*) FROM '+table).fetchone()[0]
                  for table, in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()}
        integrity = connection.execute('PRAGMA integrity_check').fetchone()[0]
    finally:
        connection.close()
    result = {'status':'pass' if integrity=='ok' and all(row['violations']==0 for row in checks) else 'fail',
              'database_sha256':sha256(db),'counts':counts,'integrity_check':integrity,'checks':checks}
    save(directory / 'audit.json', result)
    return result


def derive(db, directory, budget):
    """SQL projection cross-checked by independent per-row Decimal arithmetic."""
    directory = Path(directory)
    connection = connect(db)
    attach_budget(connection,budget)
    facts = {}
    try:
        for name, sql in FACT_SQL.items():
            budget.check()
            cursor = connection.execute(sql)
            columns = [c[0] for c in cursor.description]
            facts[name] = [dict(zip(columns,row)) for row in cursor]
        # No reuse of generator expressions or expected-output reports.
        totals = dict(ordered_pcs=Decimal(0),shipped_pcs=Decimal(0),returned_pcs=Decimal(0),
                      invoiced_cents=Decimal(0),paid_cents=Decimal(0))
        sql = 'SELECT o.quantity,s.quantity,r.quantity,o.unit_price_cents,i.amount_cents,p.amount_cents FROM orders o JOIN shipments s ON s.order_id=o.id JOIN returns r ON r.order_id=o.id JOIN invoices i ON i.order_id=o.id JOIN payments p ON p.invoice_id=i.id'
        cursor = connection.execute(sql)
        scanned = 0
        while True:
            rows = cursor.fetchmany(50000)
            if not rows:
                break
            budget.check()
            for ordered, shipped, returned, price, invoice, paid in rows:
                totals['ordered_pcs'] += Decimal(ordered)
                totals['shipped_pcs'] += Decimal(shipped)
                totals['returned_pcs'] += Decimal(returned)
                totals['invoiced_cents'] += (Decimal(shipped)-Decimal(returned))*Decimal(price)
                totals['paid_cents'] += Decimal(paid)
                if Decimal(invoice)!=(Decimal(shipped)-Decimal(returned))*Decimal(price) or not 0<=paid<=invoice:
                    raise AssertionError('independent financial row oracle: '+str(scanned))
                scanned += 1
        totals = {key:int(value) for key,value in totals.items()}
        sql_totals = {key:sum(row[key] for row in facts['sales']) for key in totals}
        if totals != sql_totals:
            raise AssertionError('SQL/Decimal aggregation mismatch')
    finally:
        connection.close()
    result = {'schema_version':'enterprise-facts/1','database_sha256':sha256(db),
              'classification':'synthetic-transaction-observation', 'facts':facts,
              'independent_oracle':{'scanned_orders':scanned,'decimal_totals':totals,'sql_totals':sql_totals,'status':'pass'},
              'sql':FACT_SQL, 'assumptions':['Budgets, organization, target architecture and approval are not transaction-derived facts.']}
    save(directory / 'facts.json', result)
    write_projection_model(result,directory)
    return result


def dirty_copy(db, directory, rate, budget):
    """Each affected order receives one recorded defect; rate denominator = orders."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    target = directory / 'enterprise.sqlite'
    budget.check()
    shutil.copyfile(db, target)
    connection = connect(target)
    count = connection.execute('SELECT count(*) FROM orders').fetchone()[0]
    affected = max(7, int(count*rate))
    affected = min(affected,count)
    changes = []
    mutations = (
        ('duplicate-event','INSERT INTO events SELECT 1000000000+id,order_id,kind,occurred_day,arrival_seq FROM events WHERE order_id=? AND kind="order-created"','event-business-duplicates'),
        ('late-out-of-order','UPDATE events SET occurred_day=-1,arrival_seq=-id WHERE order_id=?','event-time'),
        ('unit-conflict','UPDATE products SET unit="kg" WHERE id=(SELECT product_id FROM orders WHERE id=?)','order-units'),
        ('financial-error','UPDATE payments SET amount_cents=amount_cents+1000000000 WHERE invoice_id=?','payment-balance'),
        ('inventory-error','UPDATE inventory SET delta=delta+1 WHERE production_id=(?+1)/2*2 AND delta>0','inventory-balance'),
        ('missing-evidence','DELETE FROM events WHERE order_id=? AND kind="order-created"','event-missing'),
        ('missing-reference','UPDATE orders SET customer_id=-1 WHERE id=?','order-dimensions'))
    try:
        for n in range(affected):
            if n%50000==0:
                budget.check()
            # Spread dirty records through the entire population, not only its prefix.
            oid = 1 + n*count//affected
            name, sql, detector = mutations[n%len(mutations)]
            connection.execute(sql,(oid,))
            changes.append({'order_id':oid,'type':name,'expected_detector':detector,'sql':sql})
        connection.commit()
    finally:
        connection.close()
    save(directory / 'mutations.json',{'rate':rate,'denominator_orders':count,'selected_orders':affected,'affected_orders':affected,
        'rate_meaning':'selected mutation targets / sales orders; dimension-unit changes can affect additional linked orders','changes':changes})
    result = audit(target,directory,budget)
    detected = {row['name'] for row in result['checks'] if row['violations']>0}
    expected = {row['expected_detector'] for row in changes}
    if not expected<=detected:
        raise AssertionError('dirty defects silently missed: '+str(expected-detected))
    save(directory / 'negative-verdict.json',{'status':'pass','meaning':'all injected defect classes rejected, not clean-data acceptance','detected':sorted(detected),'expected':sorted(expected)})
    return {'status':'pass','rate':rate,'affected_orders':affected,'detected':sorted(detected),'database_sha256':result['database_sha256']}


def replay(db, directory, budget, limit=1000000, interrupt_after=None, pace_seconds=0):
    """Arrival-order replay; durable receipt, idempotent effects, explicit quarantine.

    arrival_seq is the source ingestion sequence; occurred_day may be out of order.
    Neither a duplicate business key nor an invalid event silently changes state.
    """
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    source = connect(db)
    state = connect(directory / 'replay.sqlite')
    attach_budget(source,budget)
    state.executescript('CREATE TABLE IF NOT EXISTS consumed(event_id INTEGER PRIMARY KEY,order_id INTEGER,kind TEXT); '
        'CREATE TABLE IF NOT EXISTS applied(order_id INTEGER,kind TEXT,PRIMARY KEY(order_id,kind)); '
        'CREATE TABLE IF NOT EXISTS quarantine(event_id INTEGER PRIMARY KEY,reason TEXT); '
        'CREATE TABLE IF NOT EXISTS checkpoint(id INTEGER PRIMARY KEY,last_arrival_seq INTEGER,last_id INTEGER); '
        'INSERT OR IGNORE INTO checkpoint VALUES(1,-1000000000000000000,0);')
    last_seq,last_id = state.execute('SELECT last_arrival_seq,last_id FROM checkpoint').fetchone()
    seen = 0
    started = time.monotonic()
    try:
        cursor = source.execute('SELECT e.id,e.order_id,e.kind,e.occurred_day,e.arrival_seq,o.created_day '
            'FROM events e LEFT JOIN orders o ON o.id=e.order_id '
            'WHERE e.arrival_seq>? OR (e.arrival_seq=? AND e.id>?) ORDER BY e.arrival_seq,e.id LIMIT ?',
            (last_seq,last_seq,last_id,limit))
        while True:
            rows = cursor.fetchmany(10000)
            if not rows:
                break
            budget.check()
            for eid,oid,kind,occurred,arrival,created in rows:
                inserted = state.execute('INSERT OR IGNORE INTO consumed VALUES(?,?,?)',(eid,oid,kind)).rowcount
                if not inserted:
                    continue
                reason = None
                if created is None:
                    reason = 'missing-order-reference'
                elif occurred<created:
                    reason = 'event-before-order'
                elif kind not in ('order-created','shipment-recorded','invoice-recorded'):
                    reason = 'unregistered-event-kind'
                else:
                    applied = state.execute('INSERT OR IGNORE INTO applied VALUES(?,?)',(oid,kind)).rowcount
                    if not applied:
                        reason = 'duplicate-business-event'
                if reason:
                    state.execute('INSERT INTO quarantine VALUES(?,?)',(eid,reason))
            state.execute('UPDATE checkpoint SET last_arrival_seq=?,last_id=? WHERE id=1',(rows[-1][4],rows[-1][0]))
            state.commit()
            seen += len(rows)
            if interrupt_after is not None and seen>=interrupt_after:
                break
            if pace_seconds:
                target = started+pace_seconds*min(1,seen/limit)
                while time.monotonic()<target:
                    budget.check()
                    time.sleep(max(0,min(.2,target-time.monotonic())))
        count = state.execute('SELECT count(*) FROM consumed').fetchone()[0]
        checkpoint_seq,checkpoint_id = state.execute('SELECT last_arrival_seq,last_id FROM checkpoint').fetchone()
        boundary = '(arrival_seq<? OR (arrival_seq=? AND id<=?))'
        parameters = (checkpoint_seq,checkpoint_seq,checkpoint_id)
        oracle_count = source.execute('SELECT count(*) FROM events WHERE '+boundary,parameters).fetchone()[0]
        overlap = source.execute('SELECT id,order_id,kind FROM events WHERE '+boundary+' ORDER BY arrival_seq DESC,id DESC LIMIT 10000',parameters).fetchall()
        state.executemany('INSERT OR IGNORE INTO consumed VALUES(?,?,?)',overlap)
        state.commit()
        if count!=oracle_count or state.execute('SELECT count(*) FROM consumed').fetchone()[0]!=count:
            raise AssertionError('event receipt loss or duplicate application')
        source_groups = dict(source.execute('SELECT kind,count(*) FROM events WHERE '+boundary+' GROUP BY kind',parameters))
        state_groups = dict(state.execute('SELECT kind,count(*) FROM consumed GROUP BY kind'))
        if source_groups!=state_groups:
            raise AssertionError('replay receipt totals mismatch')
        expected_effects = dict(source.execute('SELECT kind,count(*) FROM (SELECT e.order_id,e.kind FROM events e JOIN orders o ON o.id=e.order_id WHERE (e.arrival_seq<? OR (e.arrival_seq=? AND e.id<=?)) AND e.occurred_day>=o.created_day AND e.kind IN ("order-created","shipment-recorded","invoice-recorded") GROUP BY e.order_id,e.kind) GROUP BY kind',parameters))
        actual_effects = dict(state.execute('SELECT kind,count(*) FROM applied GROUP BY kind'))
        if expected_effects!=actual_effects:
            raise AssertionError('independent SQL business-effect oracle mismatch')
        quarantined = dict(state.execute('SELECT reason,count(*) FROM quarantine GROUP BY reason'))
        applied_count = state.execute('SELECT count(*) FROM applied').fetchone()[0]
        if applied_count+sum(quarantined.values())!=count:
            raise AssertionError('received event has neither applied nor explicit quarantine disposition')
    finally:
        source.close();state.close()
    result = {'status':'pass','new_events':seen,'consumed_events':count,'applied_business_events':applied_count,
              'quarantined':quarantined,'checkpoint':{'arrival_seq':checkpoint_seq,'event_id':checkpoint_id},
              'groups':state_groups,'applied_sql_oracle':expected_effects,'seconds':round(time.monotonic()-started,3),'requested_pacing_seconds':pace_seconds,
              'meaning':'durable synthetic arrival replay and idempotent business-key effects, not native streaming skill service'}
    save(directory / ('replay-'+str(checkpoint_seq)+'-'+str(checkpoint_id)+'.json'),result)
    return result


def write_projection_model(facts,directory):
    """One model, stable enterprise IDs, five-dimensional context and SQL evidence."""
    from validate import validate
    context = {'domains':['business','data','application','technology'],'landscape':'strategic',
               'purpose':'portfolio','abstraction':'logical','evolution':'baseline'}
    source_id = 'enterprise-snapshot-'+facts['database_sha256'][:16]
    model = {'schema_version':'2.0','project':{'id':'generic-manufacturing-group','name':'通用制造供应链集团（合成）',
             'version':facts['database_sha256'][:16],'context':context,'is_example':True,
             'approval_status':'candidate','implementation_status':'not-started'},
             'sources':[{'id':source_id,'kind':'example','description':'可重放的合成交易观察；不是真实企业事实或审批。',
                         'locator':'facts.json；database sha256='+facts['database_sha256']}],
             'entities':[],'relationships':[],'views':[],'deliverables':[],'gaps':[],
             'extensions':{'entity_types':{'enterprise:site':'合成基地','enterprise:product':'合成工业组件',
                            'enterprise:sales-observation':'SQL聚合并独立核算的合成订单观察'},
                           'relationship_types':{'enterprise:at-site':{'source_types':['enterprise:sales-observation'],
                            'target_types':['enterprise:site'],'meaning':'统计观察对应的基地'},
                            'enterprise:of-product':{'source_types':['enterprise:sales-observation'],
                            'target_types':['enterprise:product'],'meaning':'统计观察对应的产品'}},
                           'data':{'enterprise:snapshot_sha256':facts['database_sha256'],'enterprise:sql':FACT_SQL,
                                   'enterprise:classification':'synthetic-transaction-observation','enterprise:assumptions':facts['assumptions']}}}
    def entity(identity,kind,name,attributes):
        return {'id':identity,'type':kind,'name':name,'attributes':attributes,
                'context':dict(context),'evidence':[source_id],'certainty':'assumed',
                'approval_status':'candidate','implementation_status':'not-started'}
    for site in range(1,13):
        model['entities'].append(entity('enterprise-site-'+str(site),'enterprise:site','合成基地-'+str(site),{'source_table':'sites','source_id':site}))
    for product in range(1,25):
        model['entities'].append(entity('enterprise-product-'+str(product),'enterprise:product','工业组件-'+str(product),{'source_table':'products','source_id':product,'unit':'pcs'}))
    for row in facts['facts']['sales']:
        identity = 'enterprise-sales-%s-%s'%(row['site_id'],row['product_id'])
        model['entities'].append(entity(identity,'enterprise:sales-observation','基地%s产品%s订单观察'%(row['site_id'],row['product_id']),dict(row,quantity_unit='pcs',money_unit='CNY cents',sql_query='sales')))
        for field,target,relationship in (('site_id','enterprise-site-','enterprise:at-site'),('product_id','enterprise-product-','enterprise:of-product')):
            model['relationships'].append({'id':identity+'-'+field,'type':relationship,'source':identity,
                 'target':target+str(row[field]),'label':'合成统计维度','evidence':[source_id],'certainty':'assumed'})
    issues = validate(model)
    save(Path(directory)/'enterprise-model.json',model)
    save(Path(directory)/'enterprise-model-validation.json',issues)
    if any(issue['level']=='error' for issue in issues):
        raise AssertionError('shared enterprise projection model invalid: '+str(issues))
