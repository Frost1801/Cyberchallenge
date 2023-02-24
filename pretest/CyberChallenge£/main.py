# Se vuoi leggere/scrivere da file decommenta qua
fin = open("winner-input-1.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma


#M numero di giocatori, N numero di task, S numero di submission, tasks mappa che associa a id della task il punteggio
playerid = 0
taskid = 1
flag = 2
time = 3

def calcola_classifica(M, N, S, tasks, submissions):
    print()


M, N, S = map(int, fin.readline().strip().split())
tasks = []
submissions = []

for _ in range(N):
    tid, flag, points = fin.readline().strip().split()
    tasks.append((flag, int(points)))

for _ in range(S):
    player, task, submitted, timestamp = fin.readline().strip().split()
    submissions.append((int(player), int(task), submitted, int(timestamp)))

calcola_classifica(M, N, S, tasks, submissions)