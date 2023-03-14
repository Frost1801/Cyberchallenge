import re

c = "104e137f425954137f74107f525511457f5468134d7f146c4c"
maxN = 2 ** 8
ba = bytes.fromhex(c)
ar = []

pattern = re.compile("[ -~]+")

for i in range(0, maxN):
    r = ""
    for b in ba:
        r += chr(b ^ i)
    if re.fullmatch(pattern, r):
        ar.append(r)
        print(r)
