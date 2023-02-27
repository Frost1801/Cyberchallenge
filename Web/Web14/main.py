import requests as rr
from bs4 import BeautifulSoup
from bs4 import Comment


def isComment(tag):
    return isinstance(tag, Comment)


url = "http://web-14.challs.olicyber.it/"

r = rr.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for tag in soup.find_all(string=isComment):
    print(tag)
