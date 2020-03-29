#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    cnt = 0
    index = 0
    while True:
        if index+2 <= len(c) - 1:
            if c[index+2] == 0:
                index += 2
                cnt += 1
            else:
                index +=1
                cnt += 1
        else:
            index += 1
            cnt += 1

        if index == len(c) - 1:
            return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
