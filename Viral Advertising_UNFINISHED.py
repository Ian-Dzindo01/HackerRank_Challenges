#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    cnt = 2
    follow = cnt
    for d in range(n-1):
        follow = math.floor(follow*3/2)
        cnt += follow

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
