#!/bin/python3

import math
import os
import random
import re
import sys

# whyyyy cant I use numpyyyyy?
def larrysArray(A):
    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                cnt += 1

    if cnt % 2 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
