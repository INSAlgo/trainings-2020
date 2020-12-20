#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(n, t):
    if t[n] != -1:
        return t[n]

    t[n] = fibonacciModified(n-2, t) + fibonacciModified(n-1, t)**2
    return t[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1, t2, n = map(int, input().split())

    t = [-1]*(n+1)
    t[1] = t1
    t[2] = t2

    result = fibonacciModified(n, t)

    fptr.write(str(result) + '\n')

    fptr.close()
