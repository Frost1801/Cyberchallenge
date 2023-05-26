from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import random
import os
import signal
import string
def generate_secure_random_password():
    with open("wordlist.txt", "r") as f:
        passwords = f.readlines()
    chosen = random.choice(passwords).strip() # removing trailing \n
    cipher = DES.new(key = b"\x00"*8, mode = DES.MODE_ECB)
    random_psw = cipher.encrypt(pad(chosen.encode(), 8))
    return random_psw.hex()[:12]

wordlist_file = "wordlist.txt"
output_file = "dictionary.txt"

with open(wordlist_file, "r") as f:
    passwords = f.readlines()

with open(output_file, "w") as f:
    for password in passwords:
        random_password = generate_secure_random_password()
        f.write(random_password + "\n")
