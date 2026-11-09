"""Cumulative four-batch guard; continuing never resets time/session/resources."""
import threading,time
from .runtime import Blocked,Budget,save

class BatchExhausted(Blocked):
    """Only this normal boundary permits sealing and advancing a batch."""

class CampaignBudget(Budget):
    def __init__(self,out,state=None):
        state=state or {}
        super().__init__(out,max_hours=16,max_sessions=4000,started_wall=state.get('started_wall'),prior_sessions=state.get('sessions'),prior_output_roots=state.get('prior_output_roots',()))
        self.batch=state.get('batch',0);self.batch_started_wall=state.get('batch_started_wall');self.batch_session_start=state.get('batch_session_start',0)
        self.batch_state=state.get('batch_state','active' if self.batch_started_wall else 'none')
        self.batch_history=list(state.get('batch_history',[]))
        self.consecutive_timeouts=state.get('consecutive_timeouts',0);self.consecutive_429=state.get('consecutive_429',0)
        if state.get('stop_reason'):self.trip(state['stop_reason'])
        self.heartbeat_stop=threading.Event();self.phase='preflight';self.case='none'
    def trip(self,reason):
        with self.lock:self.stop_reason=reason;self.cancel.set()
    def begin_batch(self,resume=False):
        with self.lock:
            super().check()
            if resume:
                if self.batch_state!='active':raise Blocked('no active batch to resume')
                self.check()
            else:
                if self.batch_state=='active':raise Blocked('active batch must be sealed before next batch')
                if self.batch>=4:raise Blocked('four batch allowance exhausted')
                self.batch+=1;self.batch_started_wall=time.time();self.batch_session_start=len(self.sessions);self.batch_state='active'
            self.persist()
    def seal_batch(self,reason):
        with self.lock:
            if self.batch_state!='active':raise Blocked('no active batch to seal')
            self.batch_history.append({'batch':self.batch,'started_wall':self.batch_started_wall,'sealed_wall':time.time(),'sessions_used':len(self.sessions)-self.batch_session_start,'reason':reason})
            self.batch_state='sealed';self.persist()
    def check(self,dispatch=True,force=False):
        super().check(dispatch,force)
        with self.lock:
            if self.batch_state=='active':
                if time.time()-self.batch_started_wall >= 14400-(600 if dispatch else 0):raise BatchExhausted('batch time allowance exhausted; seal before next batch')
                if dispatch and len(self.sessions)-self.batch_session_start>=1000:raise BatchExhausted('batch session allowance exhausted')
    def allocate_session(self,case_id,role):
        with self.lock:
            if self.batch_state!='active':raise Blocked('an active batch is required for session dispatch')
            self.case=case_id;number=super().allocate_session(case_id,role);self.persist();return number
    def observe_http(self,status):
        with self.lock:
            self.consecutive_429=self.consecutive_429+1 if status==429 else 0
            if self.consecutive_429>=2:self.trip('two consecutive HTTP 429 responses')
            self.persist()
    def observe_session(self,status,reason=None):
        with self.lock:
            self.consecutive_timeouts=self.consecutive_timeouts+1 if status=='timeout' else 0
            if self.consecutive_timeouts>=2:self.trip('two consecutive session timeouts')
            self.persist()
    def state(self):
        return {**self.snapshot(),'sessions':self.sessions,'batch':self.batch,'batch_state':self.batch_state,'batch_history':self.batch_history,'batch_started_wall':self.batch_started_wall,'batch_session_start':self.batch_session_start,'consecutive_timeouts':self.consecutive_timeouts,'consecutive_429':self.consecutive_429,'limits':{'max_hours':16,'max_sessions':4000,'batches':4,'hours_per_batch':4,'sessions_per_batch':1000,'concurrency_stages':[1,2,4],'session_timeout_seconds':600},'model_request_or_money_cap':False}
    def persist(self):save(self.out/'campaign-ledger.json',self.state())
    def start_heartbeat(self):
        def tick():
            while not self.heartbeat_stop.wait(60):
                row={'phase':self.phase,'case':self.case,'elapsed_seconds':round(time.monotonic()-self.started),'remaining_seconds':max(0,round(self.deadline-time.monotonic())),'remaining_sessions':4000-len(self.sessions),'batch':self.batch,'stop_reason':self.stop_reason}
                save(self.out/'heartbeat.json',row);print(row,flush=True)
        self.heartbeat=threading.Thread(target=tick,daemon=True);self.heartbeat.start()
    def close(self):
        self.heartbeat_stop.set()
        if hasattr(self,'heartbeat'):self.heartbeat.join(timeout=2)
        self.persist()
