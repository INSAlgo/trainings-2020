#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10**8)

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
from collections import defaultdict


def cutTheTree(data, edges):
    graph = defaultdict(list)
    total = [-1] * n

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    setTotal(1,1, data, total, graph)

    somme = sum(data)
    total.pop(0)
    return min(abs((somme-i)-i) for i in total)


def setTotal(node, parent, data, total, graph):
    total[node-1] = data[node-1]

    for child in graph[node]:
        if child != parent:
            total[node-1] += setTotal(child, node, data, total, graph)

    return total[node-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))


    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
