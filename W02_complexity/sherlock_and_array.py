#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    """
    First, build a cumulative array to avoid computing sums every iteration
    We also add a 0 in the first position to be able to test the first element
    as a middle element

    1 1 4 1 1 becomes
    1 2 6 7 8
    """
    additive_arr = [0, arr[0]]
    for i in range(1, len(arr)):
        additive_arr.append(additive_arr[i] + arr[i])

    """
    This cumulative list enables us to very easily verify ou property
    In our previous example, 4 works because 8 - 6 == 2
    """
    total = sum(arr)
    for i in range(1, len(additive_arr)):
        if additive_arr[-1] - additive_arr[i] == additive_arr[i-1]:
            return "YES"

    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
