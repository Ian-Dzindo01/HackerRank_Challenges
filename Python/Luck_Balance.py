#!/bin/python3

import math
import os
import random
import re
import sys

# 2D array denoting if the amount of luck that can be lost in the contest and whether the contest is important

def luckBalance(k, a):
    res = 0

    res += sum([i[0] for i in a if i[1] == 0])

    l2 = sorted([i[0] for i in a if i[1] == 1], reverse=True)

    res +=  sum(l2[:k])

    res -= sum(l2[k:])

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
