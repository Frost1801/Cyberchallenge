import requests
from requests import Session

url1 = "http://web-06.challs.olicyber.it/token"
url2 = "http://web-06.challs.olicyber.it/flag"

with Session () as s:
    s.get(url1)
    r = s.get(url2)
print(r.text)

