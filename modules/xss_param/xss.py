from urllib.parse import urlparse
from core.libs import random_str,urlencoder,insert_to_params_name
from wordlists import XSS

class Scan:
    def __init__(self,opts,r):
        self.http = r
        self.opts = opts
        self.payloads = XSS(opts['blindxss']).payloads
    def reflect(self,url,method='GET'):
        ref = []
        txt = f'scan{random_str(2)}'
        for u in insert_to_params_name(url,txt):
            if method == 'GET':
                r = self.http.send(method,u)
            else:
                r = self.http.send(method,u.split('?')[0],body=urlparse(u).query)
            if r != 0:
                if txt in r.content.decode('utf-8'):
                    ref.append(txt)
        return ref
    def start(self,methods=['GET','POST']):
        http = self.http
        for method in methods:
            v = self.reflect(self.opts['url'],method=method)
            if len(v) > 0:
                for payload in self.payloads:
                    for nurl in insert_to_params_name(self.opts['url'],urlencoder(payload)):
                        if method == 'GET':
                            r = http.send(method,nurl)
                        else:
                            r = http.send(method,self.opts['url'].split('?')[0],body=urlparse(nurl).query)
                        if r != 0:
                            if payload in r.content.decode('utf-8'):
                                print(f'[XSS Parameter Name: {method}] :> {nurl}\n')
                                return {method:nurl}
