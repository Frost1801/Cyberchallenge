import requests as rr
from bs4 import BeautifulSoup
import re

url = "http://web-16.challs.olicyber.it"


def scanSite(siteUrl, checked):
    r = rr.get(siteUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    hrefs = soup.find_all("a")
    titles = soup.find_all("h1")
    result = searchTitles(titles)
    if result:
        print(result)
        return True
    checked[siteUrl] = True
    for s in hrefs:
        if (url + s["href"]) not in checked.keys():
            found = scanSite(url + s["href"], checked)
            if found:
                return
            print(url + s["href"])
    return False



def searchTitles(ttls):
    for t in ttls:
        matcher = re.findall("flag\{.+", t.contents[0])
        if matcher:
            return matcher
    return None

checked = {}
scanSite(url, checked)
