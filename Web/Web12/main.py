import requests as rr
from bs4 import BeautifulSoup
import re

url = "http://web-12.challs.olicyber.it/"

r = rr.get(url)

s = BeautifulSoup(r.text, 'html.parser')

result = s.find_all('p')
for t in result:
    print(re.findall("flag\{.+\}",t.text))

