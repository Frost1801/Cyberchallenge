# Se vuoi leggere/scrivere da file decommenta qua
fin = open("2023-pretest_pretest-1_1675789007.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma


# candidate è la stringa con quelli del candidato, correct è la stringa di quelli corretti
def calcola_punteggio(correct, candidate):
    correct = [c for c in correct]
    candidate = [char for char in candidate] #converto a char array
    if len(correct) != len(candidate): #controllo la lunghezza
        return 0
    score = 0
    for i in range(0,len(correct)):
        if candidate[i] == correct[i]: #se sono uguali
            score+= 1 #incremento il punteggio
    return score


# variabili globali
Q, N = map(int, fin.readline().strip().split(" "))
correct = fin.readline().strip()

for i in range(N):  # scorre tutti i partecipanti
    candidate = fin.readline().strip()
    print(calcola_punteggio(correct, candidate), file=fout)
