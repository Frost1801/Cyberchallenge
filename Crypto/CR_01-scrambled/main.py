import re
import random


def scramble(message, key):
    W = len(key) #W = 7 (lunghezza della lista)
    while len(message) % (2 * W): #aggiunge del padding fino a quando non abbiamo una lunghezza divisibile per 14
        message += "#"

    for _ in range(128): #_ è usata come variabile di ciclo, ma non viene usata
        message = message[1:] + message[:1] #shifta di 1 a destra
        message = message[0::2] + message[1::2]
        message = message[1:] + message[:1] #shifta di 1 a destra

        res = ""

        for j in range(0, len(message), W):
            for k in range(W):
                res += message[j:j + W][key[k]]
        message = res

    return message

def reverseCenterShift (message):
    message_len = len(message)
    half_len = message_len // 2

    first_half = message[0:half_len]
    second_half = message[half_len:]

    original_message = ""
    for i in range(half_len):
        original_message += first_half[i] + second_half[i]

    if message_len % 2 != 0:
        original_message += second_half[-1]

    message = original_message

    return message

def unscramble(message, key):
    W = len(key)

    for _ in range(128):
        res = ""
        for j in range(0, len(message), W):
            chunk = message[j:j + W]
            unscrambled_chunk = [''] * W
            for k in range(W):
                unscrambled_chunk[key[k]] = chunk[k]
            res += ''.join(unscrambled_chunk)
        message = res

        message = message[-1] + message[:-1] #shifta di 1 a sinistra
        message = reverseCenterShift(message)
        message = message[-1] + message[:-1] #shifta di 1 a sinistra


    message = message.replace('#', '')
    return message

flag = "CCIT{write_flag_here_before_the_ctf}"
key = list(range(7)) #crea una lista da 0 a 6
#costruttore di lista
random.shuffle(key)
scrambled = scramble(flag, key)

print(scrambled)

flag = unscramble(scrambled, key)
print(flag)

realFlag = "l_4Tnb_3cnnbcg3r3slCCm4Id__gb4u}ct{0mr3sds"
result = ""
while not re.findall("CCIT{.*}", result):
    key = list(range(7))
    random.shuffle(key)
    result = unscramble(realFlag, key)
    print(result)
