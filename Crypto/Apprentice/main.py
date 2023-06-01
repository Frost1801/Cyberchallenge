#!/usr/bin/env python3
from Crypto.Hash import SHA3_384

def dec(ciphertext):
    res = b''
    for i in range(0, len(ciphertext), 2):
        digest = ciphertext[i:i+2] #itera sui byte e ne prende 2 alla volta
        for c in range(256):
            if SHA3_384.new(bytes([c])).digest()[:2] == digest:
                res += bytes([c])
                break
    return res

if __name__ == '__main__':
    #open the file
    with open('apprentice_output.txt', 'r') as f:
        encrypted_flag = f.read()
    decrypted_flag = dec(bytes.fromhex(encrypted_flag))
    if decrypted_flag.startswith(b'CCIT{') and decrypted_flag.endswith(b'}'):
        print(decrypted_flag.decode())
    else:
        print("Decryption failed.")
