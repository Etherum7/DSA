#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#


def findPar(u, parent):
    if u == parent[u]:
        return u
    parent[u] = findPar(parent[u], parent)
    return parent[u]


def union(u, v, parent):
    up = findPar(u, parent)
    vp = findPar(v, parent)
    if up != vp:
        parent[vp] = up


def journeyToMoon(n, astronaut):
    # Write your code here
    parent = [i for i in range(n)]
    count = [0 for i in range(n)]
    res = 0
    for i, j in astronaut:
        union(i, j, parent)
    for i in range(n):
        pk = findPar(i, parent)
        count[pk] += 1
    print(count)
    return(sum([a * (n - a) for a in count]) // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
