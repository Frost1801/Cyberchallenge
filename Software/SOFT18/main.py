import pwnlib.util.packing
from pwn import *
import re

host = "software-18.challs.olicyber.it"
port = 13001


def decodeAnsw(answ):
    answ = answ.decode("utf-8")
    num = re.findall(r'0[xX][0-9a-fA-F]+', answ)[0]
    base = re.findall(r'\d{2}-bit', answ)[0]
    return num,base


def computePayload(payload):
    if payload[1] == '32-bit':
        return p32(int(payload[0], 16))
    elif payload[1] == '64-bit':
        return p64(int(payload[0], 16))


r = remote(host, port)
r.sendlineafter(b"... Invia un qualsiasi carattere per iniziare ...", b"y")
asw = ""
try:
    for i in range (0, 100):
        data = r.recvline()
        print(data)
        if b"Sbagliato" in data:
            print("WRONG")
            break
        toSend = computePayload(decodeAnsw(data))
        print("SENT:" + str(toSend))
        r.send(toSend)
        asw = r.recvline()
        print(asw)
except EOFError:
    print("EOF")
finally:
    print("Flag:" + r.recvline().decode())
    r.close()
