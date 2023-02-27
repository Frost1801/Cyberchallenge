import requests as rr
from bs4 import BeautifulSoup

url = "http://web-13.challs.olicyber.it/"

result = "flag{"

r = rr.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(r.text)

highlighted = soup.find_all("span")

for t in highlighted:
    result+= t.text
result += "}"
print(result)