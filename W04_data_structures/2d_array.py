#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxi = -800000000000
    for x in range(1, 5):
        for y in range(1, 5):
            maxi = max(maxi, arr[y][x]
                       + arr[y - 1][x - 1] + arr[y - 1][x] + arr[y - 1][x + 1]
                       + arr[y + 1][x - 1] + arr[y + 1][x] + arr[y + 1][x + 1])

    return maxi


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
