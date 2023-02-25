import requests as rr

url = "http://web-04.challs.olicyber.it/users"

headers = {"Accept": "application/xml"}

r = rr.get(url, headers = headers)

print(r.text)