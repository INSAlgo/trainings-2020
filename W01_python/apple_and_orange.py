#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    count_a = 0
    for apple in apples:
        if s <= a + apple <= t:
            count_a += 1

    count_b = 0
    for orange in oranges:
        if s <= b + orange <= t:
            count_b += 1

    print(count_a)
    print(count_b)
