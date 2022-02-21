#!/bin/python3

import math
import os
import random
import re
import sys

def fairRations(B):
    breads = 0
    for i in range(len(B)):
        if B[i]%2 == 1:
            breads += 2
            if i < len(B)-1:
                B[i+1] += 1

    if B[len(B)-1]%2 == 1:
        return "NO"
    else:
        return str(breads)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
