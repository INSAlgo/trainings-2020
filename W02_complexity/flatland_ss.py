#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    """
    L'astuce à la con : on crée des points virtuels aux deux extrémités
    comme si il y avait des stations en miroir de celles au bout pour pouvoir
    résoudre l'exercice en faisant simplement un max sur le tableau
    """
    c.sort()
    c = [-c[0]] + c + [2*(n-1)-c[-1]]

    return int(max(c[i]-c[i-1] for i in range(1, len(c)))/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
