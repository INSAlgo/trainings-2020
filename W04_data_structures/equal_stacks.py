#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    """
    solve using the object deque from the collection module
    """
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    d1 = deque(h1)
    d2 = deque(h2)
    d3 = deque(h3)

    while d1 and d2 and d3:
        if s1 == s2 == s3:
            return s1
        elif s1 > s2:
            s1 -= d1.popleft()
        elif s3 > s2:
            s3 -= d3.popleft()
        else:
            s2 -= d2.popleft()

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
