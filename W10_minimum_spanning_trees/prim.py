#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from heapq import heappop, heappush, heapify


# Complete the prims function below.
def prims(n, edges, start):
    graph = defaultdict(list)
    for edge in edges:
        begin, finish, weight = edge
        graph[begin].append((weight, finish))
        graph[finish].append((weight, begin))

    hq = graph[start]
    heapify(hq)
    reached = [False]*(n+1)
    reached[start] = True

    total_weight = 0
    while hq:
        weight, edge = heappop(hq)
        if not reached[edge]:
            total_weight += weight
            reached[edge] = True
        for neighbour in graph[edge]:
            if not reached[neighbour[1]]:
                heappush(hq, neighbour)

    return total_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
