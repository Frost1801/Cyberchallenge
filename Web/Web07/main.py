import requests as rr

url = "http://web-07.challs.olicyber.it/"

r = rr.get(url)

print(r.headers)

r = rr.head(url)

print(r.headers)
