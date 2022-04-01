#!/bin/python3

import math
import os
import random
import re
import sys

def toys(w):
    w.sort()
    t = w[0]
    cnt = 1

    for i in range(1, len(w)):
        if w[i] > t + 4:
            t = w[i]
            cnt += 1


    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
