import requests as rr
from bs4 import BeautifulSoup
import re

url = "http://web-15.challs.olicyber.it/"

r = rr.get(url)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("link")

scripts = soup.find_all("script")

external = []
for l in links:
    external.append(rr.get(url + l["href"]).text)

for s in scripts:
    external.append(rr.get(url + s["src"]).text)
for e in external:
    matcher = re.findall("flag\{.+", e)
    if matcher:
        print(matcher)
        break
