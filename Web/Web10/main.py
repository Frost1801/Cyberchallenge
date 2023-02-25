import requests as rr

url = "http://web-10.challs.olicyber.it/"

r = rr.options(url)

print(r.text)

r = rr.post(url)

print(r.headers)