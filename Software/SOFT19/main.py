from pwn import *

host = "software-19.challs.olicyber.it"
port = 13002
local = False


def parseInput(s):
    return s.split(" ")[1].split(":")[0].strip()


def parseNumber(num):
    hexNum = hex(int(num))
    return bytes(hexNum, "utf-8")


if local:
    r = process(["./sw-19"])
else:
    r = remote(host, port)

e = ELF("sw-19")
functAddr = e.sym
r.sendlineafter(b"Invia un qualsiasi carattere per iniziare ...", b"y")
try:
    for i in range(0, 20):
        answ = r.recv().decode()
        print(answ)
        toSend = functAddr[parseInput(answ)]
        toSend = parseNumber(toSend)
        print(toSend)
        r.sendline(toSend)
    print(r.recvline())
except EOFError:
    print("EOF")
