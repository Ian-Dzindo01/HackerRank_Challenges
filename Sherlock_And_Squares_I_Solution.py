#!/bin/python3

import math
import os
import random
import re
import sys
import math

def squares(a, b):
    cnt = 0
    for i in range(a, b+1):
        if math.sqrt(i).is_integer():
            cnt += 1

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

# this code does not execute within time limits for some of the examples.
