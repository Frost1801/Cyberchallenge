import requests as rr
from requests import Session

urlFlag = "http://web-11.challs.olicyber.it/flag_piece"

urlLogin = "http://web-11.challs.olicyber.it/login"

payload = {"username": "admin", "password": "admin"}

flag = ""

with Session() as s:
    r = s.post(urlLogin, json=payload)
    params = {"index": "0", "csrf": ""}
    for i in range(0, 4):
        csrf = r.json()["csrf"]
        params["csrf"] = csrf
        params["index"] = str(i)
        r = s.get(urlFlag, params=params)
        flag += r.json()["flag_piece"]
        print(r.text)
print(flag)