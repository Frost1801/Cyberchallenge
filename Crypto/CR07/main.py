from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from pwn import remote

r = remote('crypto-07.challs.olicyber.it', 30000)

# DES
r.recvlines(5)
key = bytes.fromhex(r.recvline(False).split(b' = ')[-1].strip(b"'").decode())
cipher = DES.new(key, DES.MODE_CBC)
plaintext = r.recvline(False).split(b' = ')[-1].strip(b"'")

padded = pad(plaintext, 8, 'x923')
print(padded)
print(len(padded))

ciphertext = cipher.encrypt(padded)

r.recvuntil(b'? ')
r.sendline(ciphertext.hex().encode())
r.recvuntil(b'? ')
r.sendline(cipher.iv.hex().encode())
print('------------------------------')

# AES
r.recvlines(5)
plaintext = r.recvline(False).split(b' = ')[-1].strip(b"'")
r.recvuntil(b'? ')
key = get_random_bytes(32)
r.sendline(key.hex().encode())

cipher = AES.new(key, AES.MODE_CFB, segment_size = 24)
padded = pad(plaintext, 16, 'pkcs7')
ciphertext = cipher.encrypt(padded)
r.recvuntil(b'? ')
r.sendline(ciphertext.hex().encode())
r.recvuntil(b'? ')
r.sendline(cipher.iv.hex().encode())
print('------------------------------')

# ChaCha20
r.recvlines(5)
key = bytes.fromhex(r.recvline(False).split(b' = ')[-1].strip(b"'").decode())
ciphertext = bytes.fromhex(r.recvline(False).split(b' = ')[-1].strip(b"'").decode())
nonce = bytes.fromhex(r.recvline(False).split(b' = ')[-1].strip(b"'").decode())
cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
r.sendline(plaintext)
# print(r.recvuntil(b'}'))
# r.interactive()
print(r.recvall(timeout=3))