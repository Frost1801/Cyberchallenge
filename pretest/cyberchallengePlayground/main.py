def encoding1():
    data = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121,
            125]

    result = ""

    for l in data:
        result += chr(l)

    print(result)


def encoding2():
    stringInput = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    result = ""
    byteR = []
    for i in range(1, len(stringInput), 2):
        tmp = stringInput[i] + stringInput[i - 1]
        byteR.append(bytes.fromhex(tmp))

    for b in byteR:
        result += str(b)

    bs = str.encode(result)
    print(bs)

    print(result)
    for c in result:
        result = result.replace('b', '')
        result = result.replace('\'', '')
        result = result.replace('\\', '')
    print(result)

def network8():
    data = "....q.`b....A.0....=E...4.]+x......i.......]...o..f......)c1..j..#....b.7.N..5....+K.z..%ekM...G...S]..m?...al..XT.Q..R.......................H....(.."

    for c in data:
        data = data.replace('.', '')
    b = bytearray(data, "utf8")
    print(data)
    print(b)

network8()
