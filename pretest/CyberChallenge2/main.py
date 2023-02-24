from collections import defaultdict

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("selection-input-1.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma


# N candidati, M numero selezionati (ossia numero di skill), S n. skill per candidato
# required sono le tipologie di skill richieste
def solve(N, S, M, required_skills_list, players):
    skillRequiredN = {}  # dizionario, per ogni skill ci dice quante persone vogliamo selezionare
    for s in required_skills_list:
        if s in skillRequiredN:
            skillRequiredN[s] += 1
        else:
            skillRequiredN[s] = 1
    assignments = {}
    for s in skillRequiredN.keys():
        assignments[s] = [None] * skillRequiredN[s]
    for i in range(1, len(players) + 1):  # scorre i player
        for j in players[str(i) + '\n']:  # scorre le skill del player
            for a in assignments[j]:
                if a is None:
                    a = [players[i]]
                else:
                    for p in reversed(a):
                        if p[j] < players[i][j]:
                            a = players[i]

    return getTotal(assignments, players)



def getTotal(assigments, players):
    total = 0
    for s in assigments:
        for p in assigments[s]:
            if p is not None:
                total += players[p][s]
    return total

# numero di testcase da gestire, in questo caso sarebbe il numero di team penso
T = int(fin.readline().strip())

# ripete questa cosa per ogni team che ci viene sottoposto
for _ in range(T):

    N, M, S = list(map(int, fin.readline().strip().split()))
    required_skills_list = list(map(str, fin.readline().strip().split()))
    players = {}
    for i in range(N):
        id = fin.readline()
        players[id] = defaultdict(int)
        for j in range(S):
            skill, level = fin.readline().strip().split()
            level = int(level)
            players[id][skill] = level  # associa ad ogni player per ogni sua skill un certo livello, quindi players è
            # un array bidimensionale

    print(solve(N, S, M, required_skills_list, players), file=fout)
