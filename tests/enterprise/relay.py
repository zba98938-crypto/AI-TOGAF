"""Credential-shielding loopback relay to the SAME configured model endpoint.

Transport authentication stays in harness memory, never in Actor files or env.
Only model API paths are forwarded. This is not a provider/model fallback.
"""
import http.client
import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
from .runtime import Blocked


class ProviderRelay:
    def __init__(self,config,environment,on_response=None):
        url_match = re.search(r'^base_url\s*=\s*(".*?")\s*$',config,re.M)
        if not url_match:
            raise Blocked('credential isolation requires an explicit configured base_url')
        self.upstream = urlsplit(json.loads(url_match.group(1)))
        if self.upstream.scheme not in ('http','https'):
            raise Blocked('unsupported configured transport')
        bearer = re.search(r'^experimental_bearer_token\s*=\s*(".*?")\s*$',config,re.M)
        env_key = re.search(r'^env_key\s*=\s*(".*?")\s*$',config,re.M)
        self.token = json.loads(bearer.group(1)) if bearer else environment.get(json.loads(env_key.group(1)),'') if env_key else ''
        self.requests = 0
        self.lock = threading.Lock()
        relay = self
        class Handler(BaseHTTPRequestHandler):
            protocol_version = 'HTTP/1.1'
            def log_message(self,*args):
                pass
            def do_GET(self):
                self.forward()
            def do_POST(self):
                self.forward()
            def forward(self):
                suffix = self.path.split('?',1)[0].rstrip('/').split('/')[-1]
                if suffix not in ('responses','models'):
                    self.send_error(403,'Only configured model endpoints are forwarded')
                    return
                length = int(self.headers.get('Content-Length','0'))
                if length>64*1024**2:
                    self.send_error(413)
                    return
                connection = None
                try:
                    kind = http.client.HTTPSConnection if relay.upstream.scheme=='https' else http.client.HTTPConnection
                    connection = kind(relay.upstream.hostname,relay.upstream.port,timeout=120)
                    upstream_path = relay.upstream.path.rstrip('/')+'/'+suffix
                    if '?' in self.path:
                        upstream_path += '?'+self.path.split('?',1)[1]
                    headers = {k:v for k,v in self.headers.items() if k.lower() not in ('host','authorization','connection','transfer-encoding')}
                    if relay.token:
                        headers['Authorization'] = 'Bearer '+relay.token
                    headers['Connection'] = 'close'
                    with relay.lock:
                        relay.requests += 1
                    connection.request(self.command,upstream_path,body=self.rfile.read(length),headers=headers)
                    response = connection.getresponse()
                    if on_response:on_response(response.status)
                    self.send_response(response.status)
                    for key,value in response.getheaders():
                        if key.lower() not in ('connection','transfer-encoding'):
                            self.send_header(key,value)
                    self.send_header('Connection','close')
                    self.end_headers()
                    self.close_connection = True
                    while True:
                        data = response.read1(65536)
                        if not data:
                            break
                        self.wfile.write(data)
                        self.wfile.flush()
                except (BrokenPipeError,ConnectionResetError):
                    pass
                except Exception:
                    # Do not put endpoint credentials or exception locals in evidence logs.
                    self.close_connection = True
                finally:
                    if connection:
                        connection.close()
        self.server = ThreadingHTTPServer(('127.0.0.1',0),Handler)
        self.server.daemon_threads = True
        self.thread = threading.Thread(target=self.server.serve_forever,daemon=True)
        self.thread.start()
        address = 'http://127.0.0.1:'+str(self.server.server_port)+'/v1'
        # Keep the provider identity/model, but replace transport auth with the in-memory relay.
        config = re.sub(r'^base_url\s*=.*$', 'base_url = '+json.dumps(address),config,flags=re.M)
        config = re.sub(r'^(experimental_bearer_token|env_key|requires_openai_auth)\s*=.*\n?', '',config,flags=re.M)
        self.config = config.rstrip()+'\nrequires_openai_auth = false\n'

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)
