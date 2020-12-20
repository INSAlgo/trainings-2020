from collections import defaultdict, deque
import os


def BFS(n, graph, start):
    q = deque()
    q.append(start)
    dist = [-1]*(n)
    dist[start-1] = 0

    while q:
        node = q.popleft()

        for neigh in graph[node]:
            if dist[neigh-1] == -1:
                dist[neigh-1] = dist[node-1] + 6
                q.append(neigh)

    dist.pop(start-1)
    return dist


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        graph = defaultdict(list)

        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        start = int(input())

        print(*BFS(n,graph, start))

