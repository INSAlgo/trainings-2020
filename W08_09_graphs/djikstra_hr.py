from collections import defaultdict
from heapq import heappop, heappush, heapify


def djikstra(n, graph, start):
    hq = [(0, start)]
    heapify(hq)

    dist = [-1]*n

    while hq:
        weight, node = heappop(hq)

        if dist[node-1] != -1:
            continue

        dist[node-1] = weight
        for neigh, w in graph[node].items():
            if dist[neigh-1] == -1:
                heappush(hq, (weight+w, neigh))

    dist.pop(start-1)
    return dist


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())

        graph = defaultdict(lambda : defaultdict(lambda : 10**8))

        # Le test 7 ne passe pas en temps si on ne gère pas les arêtes en doublon...
        # Dure vie
        for _ in range(m):
            a, b, d = map(int, input().split())
            graph[a][b] = min(graph[a][b], d)
            graph[b][a] = min(graph[b][a], d)

        start = int(input())

        print(*djikstra(n, graph, start))

