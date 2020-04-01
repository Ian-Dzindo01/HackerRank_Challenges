#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] - arr[i] == d:
                for k in range(j, len(arr)):
                    if arr[k] - arr[j] == d:
                        cnt += 1

    return cnt




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
