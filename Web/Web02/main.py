import requests as rr

payload = {"id": "flag"}

r = rr.get("http://web-02.challs.olicyber.it/server-records", params = payload)

print(r.text)

