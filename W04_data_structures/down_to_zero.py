#!/bin/python3

import os
import sys
import math


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    """
    La mauvaise approche : toujours réduire le nombre au maximum, or on n'a pas f(n-1)<=f(n).
    Et tester récursivement tous les multiples + la valeur en n-1 explose la récursion (si si)

    Une solution possible : tout précalculer en utilisant les multiples (bottom-up) et mémoiser les valeurs
    En gros c'est de la DP (qui l'eût cru)
    """

    mem = [15] * (10 ** 6 + 1)  # les résultats ne dépassent jamais 15
    mem[0] = 0

    for i in range(1, len(mem)):
        mem[i] = min(mem[i], mem[i - 1] + 1)
        for j in range(2, i+1):
            if i*j < len(mem):
                mem[i*j] = min(mem[i*j], 1 + mem[i])
            else:
                break

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = mem[n]  # ez

        fptr.write(str(result) + '\n')

    fptr.close()
