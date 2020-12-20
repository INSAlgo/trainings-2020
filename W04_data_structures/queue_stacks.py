import os
from collections import deque

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    queue = deque()

    for _ in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            queue.append(query[1])
        elif query[0] == 2:
            queue.popleft()
        else:
            fptr.write(str(queue[0]) + '\n')

    fptr.close()
