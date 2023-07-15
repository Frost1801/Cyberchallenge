from pwn import *

def GCD(a, b):
    reminder = a % b
    while reminder != 0:
        a = b
        b = reminder
        reminder = a % b
    return b


def extendedEuclid(a, b):
    if b == 0:
        return 1, 0
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while b != 0:
        q = a // b
        r = a % b
        stmp = s0
        ttmp = t0
        s0 = s1
        t0 = t1
        s1 = stmp - q * s1
        t1 = ttmp - q * t0
        a = b
        b = r
    return s0, t0

def main():
    host = "crypto-09.challs.olicyber.it"
    port = 30002
    r = remote(host, port)
    print(r.recvuntil(b"In bocca al lupo!\n"))
    r.recvline()
    q = r.recvline()
    print(q)
    print(extendedEuclid(108,173))

if __name__ == "__main__":
    main()
