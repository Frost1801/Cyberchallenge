import requests as rr
url  = "http://web-03.challs.olicyber.it/flag"

headers = {"x-Password": "admin"}

r = rr.get(url, headers = headers)

print(r.text)
