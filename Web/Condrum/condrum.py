import requests
import re

target = "http://conundrum.challs.cyberchallenge.it/random"

payload = [1792, 1313, 3480, 1151, 1302, 1582, 9311,
	3741, 1358, 1049, 1254, 1732, 1289, 1524, 8608, 1986, 1289, 7144, 1585, 1487]

for num in payload:
	r = requests.post(target, data=str(num))
	reg = re.findall("CCIT{.*}", r.text)
	if reg:
		print(reg[0])
		break
