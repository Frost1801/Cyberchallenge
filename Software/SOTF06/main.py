key = b'\xd4\x5c\xdc\xbb\x6b\x1e\xd3\x4a\x4a\x5e\xd2\xdf\xac\x7c'
flag = b'\xb2\x30\xbd\xdc\x10\x7a\xe1\x7b\x2c\x3b\xe2\xec\x99\x01'

for i in range(0, len(key)):
    print(chr(key[i] ^ flag[i]), end="")

