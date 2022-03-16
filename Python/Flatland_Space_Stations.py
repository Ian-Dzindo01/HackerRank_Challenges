#!/bin/python3

import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):
    answer = 0
    c.sort()

    for i in range(1, len(c)):
        answer = max(answer, (c[i] - c[i-1]) // 2)    # finding intermediate distances

    answer = max(answer, c[0], n-1 - c[-1])       # checking distance for first and last cities

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
