#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    cnt = 0
    if(len(s) > m):
        for x in range(len(s) - m + 1):
            stepSum = 0
            for y in range(x, x + m):
                stepSum += s[y]

            if(stepSum == d):
                cnt += 1

    elif(len(s) == m):
        if(sum(s) == d):
            return 1
    else:
        return 0

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
