from base64 import b64decode

b64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
b10 = 664813035583918006462745898431981286737635929725

l = str(b64decode(b64))
print(l)
numBytes = (b10.bit_length() + 7) // 8
r = str(b10.to_bytes(numBytes, "big"))
print(r)
toProcess = [l, r]
for i in range(0, len(toProcess)):
    toProcess[i] = toProcess[i].replace("b", "",1)
    toProcess[i] = toProcess[i].replace("'", "")
print(toProcess[0] + toProcess[1])
