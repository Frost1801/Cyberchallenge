import requests as rr

url = "http://web-09.challs.olicyber.it/login"

payload = {"username": "admin", "password": "admin"}

r = rr.post(url, json=payload)



print(r.text)
