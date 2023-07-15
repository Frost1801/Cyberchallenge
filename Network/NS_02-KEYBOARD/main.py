import re
import string


def removeCapslock(text):
    active = False


parsed = open("epicallyParsed.txt", "r")
parsed = parsed.read()
print(parsed)
table = str.maketrans('', '', string.ascii_lowercase)
parsed = parsed.translate(table)


import subprocess;print(subprocess.run(["ls", "-l"]));

import os;print(os.popen("cat flag.txt").read())