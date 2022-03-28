#!/bin/python3

import math
import os
import random
import re
import sys

def maximizingXor(l, r):
    max = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            if i ^ j > max:
                max = i ^ j

    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
