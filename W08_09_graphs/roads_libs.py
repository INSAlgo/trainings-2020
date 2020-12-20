#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib * n

    hasLib = [False] * n
    totalCost = 0
    totalLib = 0
    firstNoLib = 0
    totalCost = 0

    while (totalLib < n):
        while (firstNoLib < n - 1 and hasLib[firstNoLib]):
            firstNoLib += 1

        newRoads = DFS(firstNoLib, cities, hasLib) - 1
        totalCost += newRoads * c_road
        totalLib += newRoads

        totalLib += 1
        totalCost += c_lib

    return totalCost


def DFS(city, cities, hasLib):
    if hasLib[city]:
        return 0
    else:
        hasLib[city] = True
        somme = 1

        for vois in cities[city]:
            somme += DFS(vois, cities, hasLib)

        return somme


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = [[] for i in range(n)]

        for _ in range(m):
            a, b = map(int, input().rstrip().split())
            cities[a - 1].append(b - 1)
            cities[b - 1].append(a - 1)

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
