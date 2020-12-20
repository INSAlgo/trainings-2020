#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    stack = deque()
    for char in s:
        if char in ["[", '(', '{']:
            stack.append(char)
        else:
            if not stack:
                return False

            if char == "]":
                last = stack.pop()
                if last != "[":
                    return False
            elif char == "}":
                last = stack.pop()
                if last != "{":
                    return False
            else:
                last = stack.pop()
                if last != "(":
                    return False

    return not stack


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(("YES" if result else "NO") + '\n')

    fptr.close()
