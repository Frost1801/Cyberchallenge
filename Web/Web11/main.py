import requests as rr
from requests import Session

urlFlag = "http://web-11.challs.olicyber.it/flag_piece"

urlLogin = "http://web-11.challs.olicyber.it/login"

payload = {"username": "admin", "password": "admin"}

params = {"index": "", "csrf": ""}

flag = ""
with Session():
    for i in range(0, 3):
        r = rr.post(urlLogin, json=payload)
        print(r.text)
        params["index"] = str(i)
        params["csrf"] = r.text[1]
        r1 = rr.get(urlFlag, json=params)
        print(r1)
        flag += r1.text
print(flag)
