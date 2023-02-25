class shiftRegister():
    def __init__(self):
        self.list = [1, 1, 1, 1, 1, 1]
        self.old = self.list.copy()

    def next(self):
        self.old = self.list.copy()
        for i in range(1, len(self.list)):
            self.list[i] = self.old[i - 1]
        self.list[0] = self.old[1] ^ self.old[4]


sr = shiftRegister()  # il pattern si ripete ogni 31 iterazioni
for i in range(0, 6):
    sr.next()
for j in range(0, 10):
    for i in range(0, 31):
        print(str(sr.list[len(sr.list) - 1]), end="")
        sr.next()
    print()
