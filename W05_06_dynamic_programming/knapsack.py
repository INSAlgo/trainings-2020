#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    
    l=[0 for i in range(k+1)]
    l[0]=1
    for i in range(k+1):
        for val in arr:
            if l[i]==1 and val+i<=k:
                l[i+val]=1
    
    for i in range(k,-1,-1):
        if l[i]==1:
            return i
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for i in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
