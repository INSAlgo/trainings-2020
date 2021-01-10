t = int(input())
n = int(input())
planetes = []
nbType = [set() for i in range(n)]
for i in range(n):
    planetes.append([int(j) for j in input().split()])
    nbType[planetes[i][2]].add(i)
d = int(input())
missions = [int(i) for i in input().split()]

dist = [0 for i in range(n)]


def calcDist(pa, pb):
    return abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])


for i in range(1, d):
    for posi in nbType[missions[i]]:
        dist[posi] = min([calcDist(planetes[posi], planetes[j]) + dist[j]] for j in nbType[missions[i - 1]])[0]

print(min(dist[j] for j in nbType[missions[d - 1]]))
