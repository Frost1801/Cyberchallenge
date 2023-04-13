from pwn import *
import re


# function to parse the array of numbers from the string
def parseArrayNumbers(s):
    return [int(i) for i in re.findall(r'-?\d+', s)]


def computePayload(arr):
    arr = parseArrayNumbers(arr.decode("utf-8"))
    tot = sum(arr)
    return bytes(str(tot), "utf-8")


host = "software-17.challs.olicyber.it"
port = 13000

r = remote(host, port)
# sends the character "y" to start the program
r.sendlineafter(b"... Invia un qualsiasi carattere per iniziare ...", b"y")
asw = ""
try:
    while True:
        asw = r.recvline()
        print(asw)
        data = r.recvuntil(b"Somma? :")
        print(data)
        toSend = computePayload(data)
        print(toSend)
        r.sendline(toSend)
except EOFError:
    print("EOF")
