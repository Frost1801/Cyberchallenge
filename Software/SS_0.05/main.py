import pwnlib.util.packing
from pwn import *
import re

host = "piecewise.challs.cyberchallenge.it"
port = 9110


def parseInput(input):
    # regex to accept only integers
    input = input
    nums = re.findall(r'\d+', input)
    little = True if input.find("little") != -1 else False
    if len(nums) < 2:
        return None
    else:
        return nums[0], nums[1], little


def computePayload(number, base, little):
    number = int(number)  # Convert number to an integer
    if base == 64:
        if little:
            res = p64(number, endian='little')
        else:
            res = p64(number, endian='big')
    elif base == 32:
        if little:
            res = p32(number, endian='little')
        else:
            res = p32(number, endian='big')
    else:
        print(number)
    return res


r = remote(host, port)
while True:
    inputData = r.recvline().decode("utf-8").strip()
    print("INPUT: " + inputData)
    parsed = parseInput(inputData)
    payload = None
    if parsed is None:
        r.sendline()
    else:
        number, base, little = parsed
        payload = computePayload(number, int(base), little)
        r.send(payload)
    print("ANSW: " + r.recvline().decode("utf-8").strip())
    print(payload)
