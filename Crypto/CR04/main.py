

m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

b1 = bytes.fromhex(m1)
b2 = bytes.fromhex(m2)
a = ""

for i,j in zip(b1,b2):
    a+= chr(i^j)
print(a)