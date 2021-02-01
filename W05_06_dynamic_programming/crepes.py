n, k = map(int, input().split())
l = [0 for i in range(k)]

input()
for i in map(int, input().split()):
    if i < k:
        l[i] = 1

for j in range(1, n):
    input()
    poids = [int(i) for i in input().split()]
    for pos in range(k - 1, -1, -1):
        if l[pos] == j:

            for obj in poids:
                
                if obj + pos < k:
                    l[obj + pos] = j + 1

for pos in range(k - 1, -1, -1):
    if l[pos] == n:
        print(pos)
        break
else:
    print(-1)
