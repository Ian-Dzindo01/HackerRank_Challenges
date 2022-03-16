#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    pairlist = []
    for i in range(len(ar)):
        for j in range(i, len(ar)):
            if((i < j) and (ar[i] + ar[j]) % k == 0):
                pairlist.append((i, j))

    return(len(pairlist))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
