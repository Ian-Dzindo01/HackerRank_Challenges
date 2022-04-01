#!/bin/python3

import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(s):
    s.sort()
    min = abs(s[0] - s[1])
    for i in range(1, len(s)-1):
        if abs(s[i] - s[i+1]) < min:
            min = abs(s[i] - s[i+1])

    return min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
