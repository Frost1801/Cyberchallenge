import requests as rr

url = "http://web-08.challs.olicyber.it/login"

payload = {"username": "admin", "password": "admin"}

r = rr.post(url, data = payload)

print(r.text)